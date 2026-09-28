import logging

from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from gateway.app import create_app
from gateway.http_errors import console_origins
from gateway.settings import Settings


def settings(**kwargs):
    return Settings(
        master_key=Fernet.generate_key().decode(),
        _env_file=None,
        **{"console_origin": "http://localhost:5173", **kwargs},
    )


def test_loopback_aliases_are_limited_to_local_http():
    origins = console_origins(settings(cookie_secure=False))
    assert "http://127.0.0.1:5173" in origins
    assert "http://[::1]:5173" in origins
    assert "http://127.0.0.1:5174" not in origins
    assert console_origins(settings(cookie_secure=True)) == ["http://localhost:5173"]
    assert console_origins(
        settings(cookie_secure=False, console_origin="https://console.example.com")
    ) == ["https://console.example.com"]


def test_preflight_error_has_json_request_id_and_log(caplog):
    app = create_app(settings(cookie_secure=False))
    client = TestClient(app)
    with caplog.at_level(logging.WARNING, logger="uvicorn.error"):
        rejected = client.options(
            "/api/v1/login",
            headers={
                "Origin": "http://wrong.example",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "content-type,x-csrf-token",
            },
        )
    assert rejected.status_code == 400
    assert "CORS preflight rejected" in rejected.json()["detail"]
    assert rejected.headers["x-request-id"] in caplog.text
    assert "status=400" in caplog.text
    assert "access-control-allow-origin" not in rejected.headers
    allowed = client.options(
        "/api/v1/login",
        headers={
            "Origin": "http://127.0.0.1:5173",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type,x-csrf-token",
        },
    )
    assert allowed.status_code == 200
    assert allowed.headers["access-control-allow-origin"] == "http://127.0.0.1:5173"


def test_unexpected_error_logs_location_without_sensitive_values(caplog):
    app = create_app(settings())

    @app.get("/diagnostic-probe")
    async def probe():
        raise RuntimeError("secret-must-not-be-logged")

    with caplog.at_level(logging.ERROR, logger="uvicorn.error"):
        result = TestClient(app).get(
            "/diagnostic-probe?token=private-query", headers={"Origin": "http://localhost:5173"}
        )
    assert result.headers["access-control-allow-origin"] == "http://localhost:5173"
    assert "X-Request-ID" in result.headers["access-control-expose-headers"]
    assert result.status_code == 500
    assert result.headers["x-request-id"] in caplog.text
    assert "RuntimeError" in caplog.text and "probe" in caplog.text
    assert "secret-must-not-be-logged" not in caplog.text
    assert "private-query" not in caplog.text
