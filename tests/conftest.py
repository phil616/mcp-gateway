import os

import httpx
import pytest

BASE = os.environ.get("TEST_BASE_URL", "http://localhost:8000")


@pytest.fixture
async def api():
    async with httpx.AsyncClient(
        base_url=BASE, headers={"Origin": os.environ.get("CONSOLE_ORIGIN", "http://localhost:5173")}
    ) as client:
        login = await client.post(
            "/api/v1/login", json={"username": "admin", "password": "test-password-1234"}
        )
        assert login.status_code == 200, login.text
        client.headers["X-CSRF-Token"] = login.json()["csrf"]
        yield client
