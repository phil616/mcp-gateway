"""Credential boundary and complete management session regression tests."""

import os
import subprocess
import uuid
from contextlib import asynccontextmanager
from types import SimpleNamespace
from unittest.mock import AsyncMock

import anyio
import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from gateway.app import create_app
from gateway.auth import passwords, session_key
from gateway.cli import app as cli
from gateway.credentials import AdminCredentials, LoginBody
from gateway.settings import Settings
from pydantic import ValidationError
from typer.testing import CliRunner


@pytest.mark.parametrize("username", ["admin", "Admin", "person@example.com", "管理员", "x" * 128])
def test_creation_and_login_share_identity(username):
    values = {"username": username, "password": " exact password "}
    assert AdminCredentials(**values).model_dump() == LoginBody(**values).model_dump() == values


@pytest.mark.parametrize(
    "username,password",
    [
        ("", "valid-password"),
        ("x" * 129, "valid-password"),
        (" admin", "valid-password"),
        ("admin ", "valid-password"),
        ("ad\nmin", "valid-password"),
        ("admin", "short"),
        ("admin", "x" * 1025),
    ],
)
def test_cli_rejects_invalid_credentials_before_database(username, password):
    result = CliRunner().invoke(cli, ["admin-create", username, "--password", password])
    assert result.exit_code == 2
    assert "Invalid value" in result.output
    if len(password) > 100:
        assert password not in result.output


def test_password_bounds_and_legacy_login():
    for length in (12, 1024):
        AdminCredentials(username="admin", password="x" * length)
    # Keep old short passwords and unusual IDs usable until an explicit reset.
    assert LoginBody(username=" old ", password="short").username == " old "
    with pytest.raises(ValidationError):
        LoginBody(username="admin", password="x" * 1025)


@pytest.fixture
def auth_client():
    app = create_app(
        Settings(
            master_key=Fernet.generate_key().decode(),
            cookie_secure=False,
            console_origin="http://localhost:5173",
            public_url="http://localhost:8000",
            _env_file=None,
        )
    )
    users = {"admin": SimpleNamespace(password_hash=passwords.hash("test-password-1234"))}
    store = {}
    redis = SimpleNamespace(
        get=AsyncMock(side_effect=lambda k: store.get(k)),
        set=AsyncMock(side_effect=lambda k, v, **kw: store.__setitem__(k, v)),
        delete=AsyncMock(side_effect=lambda k: store.pop(k, None)),
        eval=AsyncMock(return_value=1),
    )

    @asynccontextmanager
    async def sessions():
        yield SimpleNamespace(get=AsyncMock(side_effect=lambda model, key: users.get(key)))

    app.state.sessions, app.state.redis = sessions, redis
    app.state.auth_limiter = anyio.CapacityLimiter(4)
    client = TestClient(app, headers={"Origin": "http://localhost:5173"})
    yield client, users, store, redis
    client.close()


def sign_in(client, **kwargs):
    return client.post(
        "/api/v1/login",
        json={
            "username": "admin",
            "password": "test-password-1234",
            **kwargs,
        },
    )


def test_login_rotation_csrf_logout_and_revocation(auth_client):
    client, users, store, redis = auth_client
    assert client.get("/api/v1/me").status_code == 401
    first = sign_in(client)
    assert first.status_code == 200
    assert "HttpOnly" in first.headers["set-cookie"]
    assert "Path=/api/v1" in first.headers["set-cookie"]
    assert first.headers["cache-control"] == "no-store"
    old_key = session_key(client.cookies["gateway_session"])
    assert client.get("/api/v1/me").json() == first.json()
    assert "credential_version" not in first.json()
    second = sign_in(client)
    assert old_key not in store
    assert first.json()["csrf"] != second.json()["csrf"]
    assert client.post("/api/v1/logout").status_code == 403
    assert (
        client.post("/api/v1/logout", headers={"X-CSRF-Token": first.json()["csrf"]}).status_code
        == 403
    )
    assert (
        client.post(
            "/api/v1/logout",
            headers={"Origin": "https://evil.example", "X-CSRF-Token": second.json()["csrf"]},
        ).status_code
        == 403
    )
    assert (
        client.post("/api/v1/logout", headers={"X-CSRF-Token": second.json()["csrf"]}).status_code
        == 200
    )
    assert client.get("/api/v1/me").status_code == 401
    assert not store
    sign_in(client)
    users["admin"].password_hash = passwords.hash("replacement-password")
    assert client.get("/api/v1/me").status_code == 401
    sign_in(client, password="replacement-password")
    users.clear()
    assert client.get("/api/v1/me").status_code == 401


@pytest.mark.parametrize(
    "stored", [None, "broken", "[]", "null", "{}", '{"username":"admin","csrf":"old"}']
)
def test_expired_or_malformed_session_is_401(auth_client, stored):
    client, users, store, redis = auth_client
    sign_in(client)
    store[session_key(client.cookies["gateway_session"])] = stored
    assert client.get("/api/v1/me").status_code == 401


def test_login_failures_are_consistent_and_do_not_echo_password(auth_client):
    client, users, store, redis = auth_client
    assert sign_in(client, username="Admin").status_code == 401
    assert sign_in(client, password="wrong").status_code == 401
    users["admin"].password_hash = "invalid-hash"
    assert sign_in(client).status_code == 401
    secret = "secret" * 200
    result = sign_in(client, password=secret)
    assert result.status_code == 422 and secret not in result.text
    assert sign_in(client, email="admin@example.com").status_code == 422
    client.headers["Origin"] = "https://evil.example"
    assert sign_in(client).status_code == 403
    client.headers["Origin"] = "http://localhost:5173"
    redis.eval.return_value = 11
    limited = sign_in(client)
    assert limited.status_code == 429 and limited.headers["retry-after"] == "300"
    assert not store


@pytest.mark.skipif(
    not os.environ.get("TEST_BASE_URL"), reason="requires isolated acceptance runner"
)
async def test_real_cli_create_login_duplicate_and_password_reset():
    username = f"Admin-{uuid.uuid4().hex[:10]}@example.com"
    password = " test-cli-password "

    def command(name, value=password):
        return subprocess.run(
            ["uv", "run", "gateway", name, username, "--password", value],
            capture_output=True,
            text=True,
        )

    assert command("admin-create").returncode == 0
    duplicate = command("admin-create")
    assert duplicate.returncode != 0 and "already exists" in duplicate.stderr
    async with httpx.AsyncClient(
        # Repeated logins in this scenario must not exhaust the other tests' IP quota.
        transport=httpx.AsyncHTTPTransport(local_address="127.0.0.2"),
        base_url=os.environ["TEST_BASE_URL"].replace("localhost", "127.0.0.1"),
        headers={"Origin": os.environ["CONSOLE_ORIGIN"]},
    ) as client:
        result = await client.post(
            "/api/v1/login", json={"username": username, "password": password}
        )
        assert result.status_code == 200, result.text
        assert (await client.get("/api/v1/me")).json()["username"] == username
        assert command("admin-reset-password", "new-cli-password").returncode == 0
        assert (await client.get("/api/v1/me")).status_code == 401
        assert (
            await client.post("/api/v1/login", json={"username": username, "password": password})
        ).status_code == 401
        result = await client.post(
            "/api/v1/login", json={"username": username, "password": "new-cli-password"}
        )
        assert result.status_code == 200
        assert (
            await client.post("/api/v1/logout", headers={"X-CSRF-Token": result.json()["csrf"]})
        ).status_code == 200
