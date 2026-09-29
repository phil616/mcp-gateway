import asyncio
import logging
import time
import traceback
import uuid
from contextlib import asynccontextmanager

import anyio
import httpx
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from redis.asyncio import Redis
from sqlalchemy import func, select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from starlette.routing import Route

from .auth import admin, login, session_key
from .catalog import Catalog
from .credentials import LoginBody
from .http_errors import GatewayCORSMiddleware, console_origins, is_mcp_path, mcp_origins
from .mcp import GroupDispatch, GroupProvider
from .models import RESOURCES, AuditEvent, AuthProfile, Group
from .service import Service, public
from .settings import Settings


class CreateBody(BaseModel):
    id: str
    data: dict


class BatchBindingsBody(BaseModel):
    items: list[CreateBody] = Field(min_length=1, max_length=200)


class DeleteItem(BaseModel):
    id: str
    version: int = Field(ge=1)


class BatchDeleteBody(BaseModel):
    items: list[DeleteItem] = Field(min_length=1, max_length=200)


class UpdateBody(BaseModel):
    version: int = Field(ge=1)
    data: dict


def create_app(settings=None):
    settings = settings or Settings()
    logger = logging.getLogger("gateway.calls")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(logging.StreamHandler())
    logger.propagate = False
    catalog = Catalog(settings.plugins_path)
    mcp = FastMCP("MCP Gateway", providers=[GroupProvider()], mask_error_details=True)
    mcp_app = mcp.http_app(path="/mcp", stateless_http=True, json_response=True)

    @asynccontextmanager
    async def lifespan(app):
        anyio.to_thread.current_default_thread_limiter().total_tokens = settings.thread_limit
        app.state.tool_limiter = asyncio.Semaphore(settings.thread_limit)
        app.state.auth_limiter = anyio.CapacityLimiter(4)
        app.state.pending_tools = set()
        app.state.engine = create_async_engine(settings.database_url, pool_pre_ping=True)
        app.state.sessions = async_sessionmaker(app.state.engine, expire_on_commit=False)
        app.state.redis = Redis.from_url(settings.redis_url, decode_responses=True)
        app.state.http = httpx.AsyncClient(timeout=10, follow_redirects=False)
        try:
            async with app.state.sessions() as db:
                await catalog.verify(db)
            await app.state.redis.ping()
            async with mcp_app.lifespan(app):
                yield
        finally:
            if app.state.pending_tools:
                await asyncio.gather(*app.state.pending_tools, return_exceptions=True)
            await app.state.http.aclose()
            await app.state.redis.aclose()
            await app.state.engine.dispose()

    app = FastAPI(title="MCP Gateway Management", version="0.1.0", lifespan=lifespan)
    app.state.settings, app.state.catalog = settings, catalog
    app.state.service = Service(settings, catalog)
    app.add_middleware(GatewayCORSMiddleware, settings=settings)

    @app.middleware("http")
    async def http_diagnostics(request: Request, call_next):
        request_id = uuid.uuid4().hex
        request.state.request_id = request_id
        start = time.monotonic()
        log = logging.getLogger("uvicorn.error")
        try:
            response = await call_next(request)
        except Exception as exc:
            log.error(
                "http_error request_id=%s method=%s path=%r status=500 error_type=%s locations=%s",
                request_id,
                request.method,
                request.url.path,
                type(exc).__name__,
                [
                    (frame.filename, frame.lineno, frame.name)
                    for frame in traceback.extract_tb(exc.__traceback__)
                ],
            )
            response = JSONResponse(
                status_code=500,
                content={
                    "detail": "Internal server error; use the request ID to locate the server log"
                },
            )
            origin = request.headers.get("origin")
            if origin in (
                mcp_origins(settings)
                if is_mcp_path(request.url.path)
                else console_origins(settings)
            ):
                response.headers.update(
                    {
                        "Access-Control-Allow-Origin": origin,
                        "Access-Control-Allow-Credentials": "true",
                        "Access-Control-Expose-Headers": "X-Request-ID",
                        "Vary": "Origin",
                    }
                )
        if request.url.path.startswith("/api/v1"):
            response.headers["Cache-Control"] = "no-store"
        response.headers["X-Request-ID"] = request_id
        if response.status_code >= 400:
            log.warning(
                "http_failure request_id=%s method=%s path=%r status=%s origin=%r duration_ms=%.1f",
                request_id,
                request.method,
                request.url.path,
                response.status_code,
                request.headers.get("origin"),
                (time.monotonic() - start) * 1000,
            )
        return response

    @app.exception_handler(RequestValidationError)
    async def validation_error(request, exc):
        # Pydantic errors otherwise echo submitted passwords back to the client.
        return JSONResponse(
            status_code=422,
            content={
                "detail": [
                    {"loc": error["loc"], "msg": error["msg"], "type": error["type"]}
                    for error in exc.errors()
                ]
            },
        )

    @app.exception_handler(IntegrityError)
    async def conflict(request, exc):
        return JSONResponse(
            {"detail": "Referenced object missing or unique constraint conflict"}, status_code=409
        )

    @app.get("/health/live")
    async def live():
        return {"status": "ok"}

    @app.get("/health/ready")
    async def ready():
        try:
            async with app.state.sessions() as db:
                await db.execute(text("SELECT 1"))
                await catalog.verify(db)
            await app.state.redis.ping()
        except Exception:
            raise HTTPException(503, "Dependencies or plugin artifact unavailable") from None
        return {"status": "ready"}

    @app.post("/api/v1/login")
    async def sign_in(body: LoginBody, request: Request):
        sid, csrf = await login(request, body.username, body.password)
        response = JSONResponse({"username": body.username, "csrf": csrf})
        response.set_cookie(
            "gateway_session",
            sid,
            httponly=True,
            secure=settings.cookie_secure,
            samesite="none" if settings.cookie_secure else "lax",
            max_age=settings.session_seconds,
            path="/api/v1",
        )
        return response

    @app.get("/api/v1/me")
    async def me(user=Depends(admin)):
        return user

    @app.post("/api/v1/logout")
    async def logout(request: Request, user=Depends(admin)):
        sid = request.cookies.get("gateway_session", "")
        await app.state.redis.delete(session_key(sid))
        response = JSONResponse({"ok": True})
        response.delete_cookie(
            "gateway_session",
            path="/api/v1",
            secure=settings.cookie_secure,
            httponly=True,
            samesite="none" if settings.cookie_secure else "lax",
        )
        return response

    @app.get("/api/v1/audit")
    async def audit(
        offset: int = Query(0, ge=0),
        limit: int = Query(50, ge=1, le=200),
        q: str = "",
        user=Depends(admin),
    ):
        async with app.state.sessions() as db:
            statement = (
                select(AuditEvent)
                .where(AuditEvent.object_id.contains(q))
                .order_by(AuditEvent.id.desc())
            )
            rows = (await db.scalars(statement.offset(offset).limit(limit))).all()
            total = await db.scalar(select(func.count()).select_from(statement.subquery()))
            return {
                "items": [
                    {
                        "id": r.id,
                        "at": r.at,
                        "actor": r.actor,
                        "action": r.action,
                        "resource": r.resource,
                        "object_id": r.object_id,
                    }
                    for r in rows
                ],
                "total": total,
            }

    def model_for(resource):
        if resource not in RESOURCES:
            raise HTTPException(404, "Unknown resource")
        return RESOURCES[resource]

    @app.get("/api/v1/{resource}")
    async def listing(
        resource: str,
        offset: int = Query(0, ge=0),
        limit: int = Query(50, ge=1, le=200),
        q: str = "",
        group_id: str | None = None,
        user=Depends(admin),
    ):
        model = model_for(resource)
        statement = select(model).where(model.id.contains(q)).order_by(model.id)
        if group_id and hasattr(model, "group_id"):
            statement = statement.where(model.group_id == group_id)
        async with app.state.sessions() as db:
            rows = (await db.scalars(statement.offset(offset).limit(limit))).all()
            total = await db.scalar(select(func.count()).select_from(statement.subquery()))
            return {"items": [public(r) for r in rows], "total": total}

    @app.get("/api/v1/{resource}/{id}")
    async def detail(resource: str, id: str, user=Depends(admin)):
        async with app.state.sessions() as db:
            row = await db.get(model_for(resource), id)
            if not row:
                raise HTTPException(404, "Not found")
            result = public(row)
            if resource == "groups":
                endpoint = settings.public_url.rstrip("/") + f"/{id}/mcp"
                result["endpoint"] = endpoint
                from .models import ToolBinding, ToolDefinition

                profile = (
                    await db.get(AuthProfile, row.auth_profile_id) if row.auth_profile_id else None
                )
                result["auth_mode"] = profile.data["mode"] if profile else "public"
                bindings = (
                    await db.scalars(select(ToolBinding).where(ToolBinding.group_id == id))
                ).all()
                effective = []
                for binding in bindings:
                    definition = await db.get(ToolDefinition, binding.tool_id)
                    if (
                        row.data["enabled"]
                        and binding.data["enabled"]
                        and definition.data["enabled"]
                        and definition.data["available"]
                    ):
                        effective.append({"tool_id": binding.tool_id, "name": binding.exposed_name})
                result["effective_tools"] = effective
                connection = {"type": "http", "url": endpoint}
                if result["auth_mode"] == "static":
                    connection["headers"] = {"Authorization": "Bearer <YOUR_GROUP_ACCESS_KEY>"}
                result["client_example"] = {"mcpServers": {id: connection}}
                remote = {**connection, "type": "remote"}
                if result["auth_mode"] != "oauth":
                    remote["oauth"] = False
                result["client_examples"] = {
                    "claude": result["client_example"],
                    "opencode": {"mcp": {id: remote}},
                    "vscode": {"servers": {id: connection}},
                }
            return result

    @app.get("/api/v1/{resource}/{id}/dependencies")
    async def dependencies(resource: str, id: str, user=Depends(admin)):
        model_for(resource)
        async with app.state.sessions() as db:
            return {"items": await app.state.service.dependencies(db, resource, id)}

    @app.post("/api/v1/bindings/batch", status_code=201)
    async def batch_bindings(body: BatchBindingsBody, user=Depends(admin)):
        groups = [item.data.get("group_id") for item in body.items]
        if not all(isinstance(g, str) and g for g in groups) or len(set(groups)) != 1:
            raise HTTPException(422, "Batch bindings must belong to one group")
        async with app.state.sessions() as db, db.begin():
            results = []
            for index, item in enumerate(body.items):
                try:
                    results.append(
                        await app.state.service.mutate(
                            db, user["username"], "bindings", item.id, item.data
                        )
                    )
                except HTTPException as exc:
                    raise HTTPException(
                        exc.status_code,
                        {
                            "message": "整批未创建，请修正失败项后重新提交",
                            "item": index + 1,
                            "id": item.id,
                            "reason": exc.detail,
                        },
                    ) from None
                except IntegrityError:
                    raise HTTPException(
                        409,
                        {
                            "message": "整批未创建：绑定、暴露名称重复或引用对象不存在",
                            "item": index + 1,
                            "id": item.id,
                        },
                    ) from None
            return {"items": results}

    @app.post("/api/v1/{resource}/batch-delete")
    async def batch_delete(resource: str, body: BatchDeleteBody, user=Depends(admin)):
        model_for(resource)
        if resource == "tools":
            raise HTTPException(422, "Tools cannot be deleted")
        if len({item.id for item in body.items}) != len(body.items):
            raise HTTPException(422, "Duplicate IDs in deletion batch")
        async with app.state.sessions() as db, db.begin():
            # Stable lock order avoids deadlocks between overlapping batches.
            for item in sorted(body.items, key=lambda item: item.id):
                try:
                    await app.state.service.mutate(
                        db, user["username"], resource, item.id, {}, item.version, delete=True
                    )
                except HTTPException as exc:
                    raise HTTPException(
                        exc.status_code,
                        {"message": "整批未删除", "id": item.id, "reason": exc.detail},
                    ) from None
        return {"deleted": len(body.items)}

    @app.post("/api/v1/{resource}", status_code=201)
    async def create(resource: str, body: CreateBody, user=Depends(admin)):
        async with app.state.sessions() as db, db.begin():
            return await app.state.service.mutate(
                db, user["username"], resource, body.id, body.data
            )

    @app.put("/api/v1/{resource}/{id}")
    async def update(resource: str, id: str, body: UpdateBody, user=Depends(admin)):
        async with app.state.sessions() as db, db.begin():
            return await app.state.service.mutate(
                db, user["username"], resource, id, body.data, body.version
            )

    @app.delete("/api/v1/{resource}/{id}")
    async def delete(resource: str, id: str, version: int = Query(ge=1), user=Depends(admin)):
        async with app.state.sessions() as db, db.begin():
            await app.state.service.mutate(
                db, user["username"], resource, id, {}, version, delete=True
            )
        return {"ok": True}

    @app.post("/api/v1/bindings/{id}/validate")
    async def validate(id: str, user=Depends(admin)):
        async with app.state.sessions() as db:
            row = await db.get(RESOURCES["bindings"], id)
            if not row:
                raise HTTPException(404, "Not found")
            await app.state.service.config(db, row)
        return {"valid": True}

    @app.post("/api/v1/access-keys/{id}/rotate")
    async def rotate_key(id: str, body: UpdateBody, user=Depends(admin)):
        import uuid

        from .models import GroupAccessKey

        async with app.state.sessions() as db, db.begin():
            await db.execute(text("SELECT pg_advisory_xact_lock(671923)"))
            old = await db.get(GroupAccessKey, id)
            if not old:
                raise HTTPException(404, "Not found")
            group_id = old.group_id
            await app.state.service.mutate(
                db, user["username"], "access-keys", id, {"revoked": True}, body.version
            )
            if set(body.data) - {"expires_at"}:
                raise HTTPException(422, "Only expires_at can be supplied for rotation")
            return await app.state.service.mutate(
                db,
                user["username"],
                "access-keys",
                "key-" + uuid.uuid4().hex,
                {"group_id": group_id, **body.data},
            )

    @app.get("/api/v1/auth-profiles/{id}/compatibility")
    async def compatibility(id: str, user=Depends(admin)):
        from urllib.parse import urlsplit

        async with app.state.sessions() as db:
            profile = await db.get(AuthProfile, id)
            if not profile or profile.data.get("mode") != "oauth":
                raise HTTPException(422, "Select an OAuth authentication profile")
            issuer = profile.data["issuer"].rstrip("/")
        url = urlsplit(issuer)
        candidates = [
            f"{url.scheme}://{url.netloc}/.well-known/oauth-authorization-server{url.path}",
            issuer + "/.well-known/openid-configuration",
        ]
        metadata = None
        for candidate in candidates:
            try:
                response = await app.state.http.get(candidate)
                if response.status_code == 200 and response.json().get("issuer") == issuer:
                    metadata = response.json()
                    break
            except (httpx.HTTPError, ValueError):
                continue
        issues = []
        if metadata is None:
            issues.append("IDP discovery metadata missing or issuer mismatch")
            metadata = {}
        if "S256" not in metadata.get("code_challenge_methods_supported", []):
            issues.append("IDP does not advertise PKCE S256")
        if "code" not in metadata.get("response_types_supported", []):
            issues.append("IDP does not advertise authorization code flow")
        if not (
            metadata.get("registration_endpoint")
            or metadata.get("client_id_metadata_document_supported")
        ):
            issues.append(
                "Configure a preregistered client; IDP does not advertise dynamic registration or client metadata documents"
            )
        return {
            "token_validation": profile.data["validation"],
            "discovery_checks_passed": not issues,
            "issues": issues,
            "resource_audience": "Requires an integration test with a resource-bound token; discovery alone cannot prove support",
        }

    @app.get("/.well-known/oauth-protected-resource/{group}/mcp")
    async def metadata(group: str):
        async with app.state.sessions() as db:
            row = await db.get(Group, group)
            profile = (
                await db.get(AuthProfile, row.auth_profile_id)
                if row and row.auth_profile_id
                else None
            )
            if not row or not row.data["enabled"] or not profile or profile.data["mode"] != "oauth":
                raise HTTPException(404, "OAuth resource unavailable")
            return {
                "resource": settings.public_url.rstrip("/") + f"/{group}/mcp",
                "authorization_servers": [profile.data["issuer"]],
                "scopes_supported": profile.data.get("scopes", []),
                "bearer_methods_supported": ["header"],
            }

    app.router.routes.append(
        Route("/{group}/mcp", GroupDispatch(mcp_app, app.state), methods=["GET", "POST", "DELETE"])
    )
    from fastapi.openapi.utils import get_openapi

    from .contracts import CONTRACTS

    def openapi():
        if app.openapi_schema is None:
            schema = get_openapi(title=app.title, version=app.version, routes=app.routes)
            for contract in CONTRACTS.values():
                schema["components"]["schemas"][contract.__name__] = contract.model_json_schema()
            schema["info"]["description"] = "Resource-specific data schemas: " + ", ".join(
                f"{r}: {c.__name__}" for r, c in CONTRACTS.items()
            )
            app.openapi_schema = schema
        return app.openapi_schema

    app.openapi = openapi
    return app
