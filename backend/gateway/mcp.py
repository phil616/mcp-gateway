import asyncio
import inspect
import logging
import time
import traceback
import uuid
from contextvars import ContextVar
from dataclasses import dataclass

from fastapi import HTTPException
from fastmcp.exceptions import ToolError
from fastmcp.server.providers import Provider
from fastmcp.tools import Tool
from gateway_sdk import ToolRuntime, _runtime
from pydantic import PrivateAttr
from sqlalchemy import select
from starlette.requests import Request
from starlette.responses import JSONResponse

from .auth import authorize
from .http_errors import mcp_origins
from .models import AuthProfile, Group, ToolBinding, ToolDefinition

log = logging.getLogger("gateway.calls")


@dataclass(frozen=True)
class Snapshot:
    group: str
    caller: str
    request_id: str
    tools: dict


snapshot: ContextVar[Snapshot] = ContextVar("gateway_snapshot")


class BoundTool(Tool):
    _spec: object = PrivateAttr()
    _config: object = PrivateAttr()
    _limiter: object = PrivateAttr()
    _pending: object = PrivateAttr()

    async def run(self, arguments):
        ctx = snapshot.get()
        if self.name not in ctx.tools:
            raise ToolError("Tool unavailable in this group")
        token = _runtime.set(
            ToolRuntime(ctx.group, str(uuid.uuid4()), self._config.model_copy(deep=True))
        )
        started, status = time.monotonic(), "error"
        try:

            async def execute():
                synchronous = not inspect.iscoroutinefunction(self._spec.tool.fn)
                if synchronous:
                    await self._limiter.acquire()
                task = asyncio.create_task(self._spec.tool.run(arguments))
                self._pending.add(task)

                def finished(done):
                    self._pending.discard(done)
                    if synchronous:
                        self._limiter.release()
                    if not done.cancelled():
                        done.exception()

                task.add_done_callback(finished)
                try:
                    return await asyncio.shield(task)
                except asyncio.CancelledError:
                    if inspect.iscoroutinefunction(self._spec.tool.fn):
                        task.cancel()
                    raise

            result = await asyncio.wait_for(execute(), timeout=self._spec.timeout)
            status = "ok"
            return result
        except TimeoutError:
            status = "timeout"
            raise ToolError("Tool execution timed out") from None
        except Exception as exc:
            log.error(
                "tool_error request=%s group=%s tool=%s error_type=%s locations=%s",
                ctx.request_id,
                ctx.group,
                self.name,
                type(exc).__name__,
                [(f.filename, f.lineno, f.name) for f in traceback.extract_tb(exc.__traceback__)],
            )
            # Plugin exceptions can contain upstream credentials; never expose their text.
            raise ToolError("Tool execution failed") from None
        finally:
            _runtime.reset(token)
            log.info(
                "request=%s group=%s tool=%s elapsed_ms=%.1f status=%s",
                ctx.request_id,
                ctx.group,
                self.name,
                (time.monotonic() - started) * 1000,
                status,
            )


class GroupProvider(Provider):
    async def _list_tools(self):
        ctx = snapshot.get(None)
        return list(ctx.tools.values()) if ctx else []

    async def _get_tool(self, name, version=None):
        ctx = snapshot.get(None)
        return ctx.tools.get(name) if ctx else None


class GroupDispatch:
    def __init__(self, app, state):
        self.app, self.state = app, state

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return
        state = self.state
        group_id = scope["path_params"]["group"]
        request = Request(scope)
        try:
            origin = request.headers.get("origin")
            if origin and origin not in mcp_origins(state.settings):
                raise HTTPException(403, "Origin rejected")
            async with state.sessions() as db:
                async with db.begin():
                    # One coherent snapshot, even when a concurrent management transaction commits.
                    from sqlalchemy import text

                    await db.execute(text("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ"))
                    group = await db.get(Group, group_id)
                    if not group or not group.data["enabled"]:
                        raise HTTPException(404, "Group unavailable")
                    profile = (
                        await db.get(AuthProfile, group.auth_profile_id)
                        if group.auth_profile_id
                        else None
                    )
                    auth_data = dict(profile.data) if profile else {}
                    oauth = auth_data.get("mode") == "oauth"
                    secret = None
                    if oauth:
                        # Capture secrets in the same snapshot; network I/O runs after release.
                        if auth_data.get("validation") == "introspection":
                            secret = await state.service.resolve(db, auth_data.get("client_secret"))
                    else:
                        caller = await authorize(
                            state, db, group, auth_data, request.headers.get("authorization", "")
                        )
                    bindings = (
                        await db.scalars(
                            select(ToolBinding).where(ToolBinding.group_id == group_id)
                        )
                    ).all()
                    tools = {}
                    for binding in bindings:
                        definition = await db.get(ToolDefinition, binding.tool_id)
                        if (
                            not binding.data["enabled"]
                            or not definition.data["available"]
                            or not definition.data["enabled"]
                        ):
                            continue
                        spec = state.catalog.tools.get(binding.tool_id)
                        if not spec:
                            continue
                        config = await state.service.config(db, binding)
                        tool = BoundTool(
                            name=binding.exposed_name,
                            description=spec.tool.description,
                            parameters=spec.tool.parameters,
                            output_schema=spec.tool.output_schema,
                        )
                        tool._spec, tool._config = spec, config
                        tool._limiter, tool._pending = state.tool_limiter, state.pending_tools
                        tools[tool.name] = tool
            if oauth:
                caller = await authorize(
                    state,
                    None,
                    group,
                    auth_data,
                    request.headers.get("authorization", ""),
                    client_secret=secret,
                )
            ctx = Snapshot(group_id, caller, request.state.request_id, tools)
            token = snapshot.set(ctx)
            try:
                child = dict(scope)
                child.update(path="/mcp", raw_path=b"/mcp", root_path="")

                await self.app(child, receive, send)
            finally:
                snapshot.reset(token)
        except HTTPException as exc:
            await JSONResponse({"detail": exc.detail}, exc.status_code, headers=exc.headers)(
                scope, receive, send
            )
