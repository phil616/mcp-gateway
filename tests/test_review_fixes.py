"""Regression coverage for confirmed transport, isolation and diagnostic defects."""

import asyncio
import io
import logging
import threading
from contextlib import asynccontextmanager
from types import SimpleNamespace
from unittest.mock import AsyncMock

import anyio
import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi import HTTPException
from fastapi.testclient import TestClient
from gateway.app import create_app
from gateway.auth import authorize, login
from gateway.mcp import BoundTool, GroupDispatch, Snapshot, snapshot
from gateway.models import AuthProfile, Group
from gateway.settings import Settings
from gateway_sdk import EmptyConfig, ToolPackage
from starlette.requests import Request
from starlette.responses import JSONResponse


def make_app():
    return create_app(
        Settings(
            master_key=Fernet.generate_key().decode(),
            cookie_secure=False,
            public_url="http://localhost:8000",
            console_origin="http://localhost:5173",
            _env_file=None,
        )
    )


def test_browser_mcp_headers_and_management_remain_separate():
    client = TestClient(make_app())
    headers = {
        "Origin": "http://localhost:5173",
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "authorization,content-type,mcp-protocol-version",
    }
    assert client.options("/test/mcp", headers=headers).status_code == 200
    assert client.options("/api/v1/login", headers=headers).status_code == 400
    headers["Origin"] = "http://127.0.0.1:5173"
    assert client.options("/test/mcp", headers=headers).status_code == 200
    headers["Origin"] = "https://untrusted.example"
    assert client.options("/test/mcp", headers=headers).status_code == 400


def test_oauth_releases_database_and_keeps_request_id(monkeypatch):
    app = make_app()
    active = False

    class DB:
        @asynccontextmanager
        async def begin(self):
            nonlocal active
            active = True
            try:
                yield
            finally:
                active = False

        async def execute(self, *args):
            pass

        async def get(self, model, id):
            if model is Group:
                return SimpleNamespace(id=id, data={"enabled": True}, auth_profile_id="auth")
            if model is AuthProfile:
                return SimpleNamespace(
                    data={
                        "mode": "oauth",
                        "validation": "introspection",
                        "client_secret": {"$secret": "upstream"},
                    }
                )

        async def scalars(self, *args):
            return SimpleNamespace(all=lambda: [])

    @asynccontextmanager
    async def sessions():
        yield DB()

    async def resolve(*args):
        assert active
        return "snapshot-secret"

    async def auth(state, db, group, profile, authorization, *, client_secret):
        assert not active and db is None
        assert client_secret == "snapshot-secret"
        return "caller"

    async def inner(scope, receive, send):
        await JSONResponse({"id": snapshot.get().request_id})(scope, receive, send)

    app.state.sessions = sessions
    app.state.service.resolve = resolve
    monkeypatch.setattr("gateway.mcp.authorize", auth)
    for route in app.router.routes:
        if getattr(route, "path", "") == "/{group}/mcp":
            route.app = GroupDispatch(inner, app.state)
    response = TestClient(app).get("/test/mcp", headers={"Origin": "http://127.0.0.1:5173"})
    assert response.status_code == 200
    assert response.json()["id"] == response.headers["x-request-id"]
    assert "WWW-Authenticate" in response.headers["access-control-expose-headers"]


@pytest.mark.parametrize(
    "payload,status",
    [
        ({"active": True, "aud": "http://localhost:8000/test/mcp", "scope": "tools:call"}, 200),
        ({"active": True, "aud": "wrong", "scope": "tools:call"}, 401),
        ({"active": True, "aud": "http://localhost:8000/test/mcp", "exp": 1}, 401),
        ({"active": False}, 401),
        ({"active": True, "aud": "http://localhost:8000/test/mcp"}, 403),
        ({"error": "bad upstream"}, 503),
        ("not-json", 503),
    ],
)
async def test_introspection_optional_exp_and_failures(monkeypatch, payload, status):
    original = httpx.AsyncClient

    def handler(request):
        assert request.headers["authorization"].startswith("Basic ")
        return (
            httpx.Response(200, text=payload)
            if isinstance(payload, str)
            else httpx.Response(200, json=payload)
        )

    monkeypatch.setattr(
        "gateway.auth.httpx.AsyncClient",
        lambda **kw: original(transport=httpx.MockTransport(handler), **kw),
    )
    state = SimpleNamespace(settings=make_app().state.settings)
    profile = {
        "mode": "oauth",
        "validation": "introspection",
        "issuer": "https://idp.example",
        "introspection_url": "https://idp.example/introspect",
        "scopes": ["tools:call"],
        "client_id": "gateway",
    }
    try:
        await authorize(
            state,
            None,
            SimpleNamespace(id="test"),
            profile,
            "Bearer sample",
            client_secret="secret",
        )
        actual = 200
    except HTTPException as exc:
        actual = exc.status_code
    assert actual == status


async def test_idp_failure_is_not_invalid_token():
    def handler(request):
        return httpx.Response(500, text="sensitive upstream error")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        state = SimpleNamespace(settings=make_app().state.settings, http=http)
        with pytest.raises(HTTPException) as error:
            await authorize(
                state,
                None,
                SimpleNamespace(id="test"),
                {
                    "mode": "oauth",
                    "validation": "jwt",
                    "issuer": "https://idp.example",
                    "jwks_url": "https://idp.example/jwks",
                },
                "Bearer sample",
            )
        assert error.value.status_code == 503
        assert "sensitive" not in error.value.detail
        assert "WWW-Authenticate" not in error.value.headers


async def test_timed_out_tool_does_not_block_login(monkeypatch):
    stop = threading.Event()
    package = ToolPackage("regression", "1")

    @package.tool(id="blocking", timeout=0.05)
    def blocking() -> str:
        stop.wait(3)
        return "done"

    spec = package.tools["regression.blocking"]
    tool = BoundTool(name="blocking", parameters=spec.tool.parameters)
    tool._spec, tool._config = spec, EmptyConfig()
    tool._limiter, tool._pending = asyncio.Semaphore(1), set()
    token = snapshot.set(Snapshot("test", "caller", "request", {"blocking": tool}))
    default = anyio.to_thread.current_default_thread_limiter()
    previous = default.total_tokens
    default.total_tokens = 1
    app = make_app()
    app.state.auth_limiter = anyio.CapacityLimiter(1)
    app.state.redis = SimpleNamespace(eval=AsyncMock(return_value=1), set=AsyncMock())

    @asynccontextmanager
    async def sessions():
        yield SimpleNamespace(get=AsyncMock(return_value=SimpleNamespace(password_hash="hash")))

    app.state.sessions = sessions
    monkeypatch.setattr("gateway.auth.passwords", SimpleNamespace(verify=lambda *args: True))
    request = Request(
        {
            "type": "http",
            "app": app,
            "headers": [(b"origin", b"http://localhost:5173")],
            "client": ("127.0.0.1", 1234),
        }
    )
    try:
        with pytest.raises(Exception, match="timed out"):
            await tool.run({})
        assert tool._pending and tool._limiter.locked()
        sid, csrf = await asyncio.wait_for(login(request, "admin", "password"), timeout=0.5)
        assert sid and csrf
    finally:
        stop.set()
        await asyncio.gather(*tool._pending)
        snapshot.reset(token)
        default.total_tokens = previous


async def test_tool_error_logs_safe_location():
    package = ToolPackage("diagnostic", "1")

    @package.tool(id="broken")
    async def broken() -> str:
        raise RuntimeError("secret-never-log-this")

    spec = package.tools["diagnostic.broken"]
    tool = BoundTool(name="broken", parameters=spec.tool.parameters)
    tool._spec, tool._config = spec, EmptyConfig()
    tool._limiter, tool._pending = asyncio.Semaphore(1), set()
    token = snapshot.set(Snapshot("test", "caller", "known-request", {"broken": tool}))
    output = io.StringIO()
    handler = logging.StreamHandler(output)
    logger = logging.getLogger("gateway.calls")
    logger.addHandler(handler)
    try:
        with pytest.raises(Exception, match="Tool execution failed"):
            await tool.run({})
    finally:
        snapshot.reset(token)
        logger.removeHandler(handler)
    text = output.getvalue()
    assert "known-request" in text and "broken" in text and "locations=" in text
    assert "secret-never-log-this" not in text
