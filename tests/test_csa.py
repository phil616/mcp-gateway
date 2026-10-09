"""Offline contract and HTTP adapter tests; no real CSA credentials or writes."""

import asyncio
import importlib
import json
import subprocess
from pathlib import Path

import httpx
import pytest
from fastmcp import Client, FastMCP
from gateway.catalog import Catalog
from gateway.mcp import BoundTool, Snapshot, snapshot
from jsonschema import Draft202012Validator
from pydantic import ValidationError

ROOT = Path(__file__).resolve().parents[1]
Catalog(str(ROOT / "plugins"))
plugin = importlib.import_module("plugins.csa.plugin")


@pytest.fixture
def upstream(monkeypatch):
    requests = []
    clients = []
    result = [httpx.Response(200, json={"id": "example"})]
    real_client = httpx.AsyncClient

    async def handle(request):
        requests.append(request)
        await asyncio.sleep(0)
        if isinstance(result[0], Exception):
            raise result[0]
        return result[0]

    def factory(**kwargs):
        assert kwargs["follow_redirects"] is False
        assert kwargs["trust_env"] is False
        client = real_client(**kwargs, transport=httpx.MockTransport(handle))
        clients.append(client)
        return client

    monkeypatch.setattr(plugin.httpx, "AsyncClient", factory)
    return requests, clients, result


async def call(name, request, api_key="test-csa-secret"):
    return await plugin.execute(plugin.OPERATIONS[name], request, plugin.CSAConfig(), api_key)


def test_contract_is_fresh_and_covers_only_user_apikey_operations():
    subprocess.run(
        ["uv", "run", "python", "scripts/generate_csa.py", "--check"], cwd=ROOT, check=True
    )
    source = json.loads((ROOT / "plugins/csa/docs/openapi.json").read_text())
    expected = {
        (method.upper(), path)
        for path, methods in source["paths"].items()
        for method, op in methods.items()
        if {"AccountAPIKey": []} in op.get("security", [])
        and op.get("x-access") == "登录；资源归属限制见接口说明"
    }
    assert {(op["method"], op["path"]) for op in plugin.OPERATIONS.values()} == expected
    assert len(expected) == 61
    for spec in plugin.package.tools.values():
        props = spec.tool.parameters["properties"]
        assert set(props) == {"api_key", "request"}
        Draft202012Validator.check_schema(spec.tool.parameters)
        assert set(spec.config_model.model_fields) == {"base_url"}


@pytest.mark.parametrize(
    "url",
    [
        "https://user:pass@example.com",
        "https://example.com/api",
        "https://example.com?key=x",
        "http://remote.example",
        "file:///etc/passwd",
        "https://example.com#fragment",
    ],
)
def test_invalid_config_origins(url):
    with pytest.raises(ValidationError):
        plugin.CSAConfig(base_url=url)


async def test_exact_path_query_and_credentials(upstream):
    requests, clients, _ = upstream
    await call("list_oauth_clients", {"query": {"scope": "mine", "skip": 0}})
    assert requests[0].url.path == "/api/oauth/clients/"
    assert dict(requests[0].url.params) == {"scope": "mine", "skip": "0"}
    assert requests[0].url.host == "api.altasci.com"
    assert requests[0].headers["x-api-key"] == "test-csa-secret"
    assert "authorization" not in requests[0].headers
    assert clients[0].is_closed
    await call("list_responsible_tags", {"query": {"include_inactive": False}})
    assert requests[1].url.params["include_inactive"] == "false"


async def test_json_omission_null_and_no_content(upstream):
    requests, _, response = upstream
    response[0] = httpx.Response(200, json={})
    await call("update_me", {"body": {"bio": None}})
    assert json.loads(requests[-1].content) == {"bio": None}
    await call("toggle_application_key_status", {"body": False})
    assert json.loads(requests[-1].content) is False
    response[0] = httpx.Response(204)
    result = await call("delete_ticket", {"path": {"ticket_id": "abc"}})
    assert result == {"ok": True, "status": 204, "data": None}


@pytest.mark.parametrize(
    "name,payload",
    [
        ("list_tickets", {"query": {"limit": 101}}),
        ("list_tickets", {"query": {"status_filter": "bad"}}),
        ("list_tickets", {"query": {"api_key": "bad"}}),
        ("get_ticket", {}),
        ("get_ticket", {"path": {"ticket_id": "../users"}}),
        ("get_ticket", {"path": {"ticket_id": "%2e%2e"}}),
        ("create_ticket", {"body": {"title": "missing fields"}}),
        (
            "create_order",
            {
                "body": {
                    "revision": 1,
                    "plan": "popular",
                    "item_ids": [],
                    "request_id": "too-short",
                    "amount": 1,
                }
            },
        ),
        (
            "create_finance_entry",
            {
                "path": {"project_id": "a"},
                "body": {
                    "project_id": "b",
                    "name": "test",
                    "amount": 10,
                    "entry_type": "income",
                    "date": "2026-09-29",
                },
            },
        ),
    ],
)
async def test_invalid_arguments_never_reach_upstream(upstream, name, payload):
    result = await call(name, payload)
    assert not result["ok"]
    assert not upstream[0]


@pytest.mark.parametrize("key", ["", "bad\r\nheader", "bad key", "中文"])
async def test_invalid_keys_never_reach_upstream(upstream, key):
    assert (await call("get_me", {}, key))["error"] == "invalid_api_key"
    assert not upstream[0]


@pytest.mark.parametrize("status", [301, 307, 400, 401, 403, 409, 422, 429, 500, 503])
async def test_errors_are_sanitized_without_retry_or_redirect(upstream, status):
    requests, clients, response = upstream
    response[0] = httpx.Response(
        status, text="test-csa-secret private input", headers={"Location": "https://other.example"}
    )
    result = await call("get_me", {})
    assert result == {"ok": False, "status": status, "error": "upstream_http_error"}
    assert len(requests) == 1 and clients[0].is_closed


async def test_invalid_json_response(upstream):
    _, _, response = upstream
    response[0] = httpx.Response(200, content=b"{bad", headers={"content-type": "application/json"})
    assert (await call("get_me", {}))["error"] == "invalid_upstream_json"


async def test_credentials_redacted_and_network_failure(upstream):
    _, _, response = upstream
    response[0] = httpx.Response(
        200,
        json={
            "key": "generated-secret",
            "nested": {"message": "test-csa-secret"},
            "recovery_codes": ["code"],
        },
    )
    result = await call("get_me", {})
    assert "generated-secret" not in str(result) and "test-csa-secret" not in str(result)
    assert result["data"]["recovery_codes"] == "[REDACTED]"
    response[0] = httpx.ReadTimeout("test-csa-secret")
    assert (await call("get_me", {}))["error"] == "upstream_timeout"
    response[0] = httpx.ConnectError("test-csa-secret")
    assert (await call("get_me", {}))["error"] == "upstream_transport_error"


async def test_real_mcp_schema_call_and_per_call_key_isolation(upstream):
    server = FastMCP("csa-contract-test")
    spec = plugin.package.tools["csa.list_tickets"]
    bound = BoundTool(
        name="tickets",
        description=spec.tool.description,
        parameters=spec.tool.parameters,
        output_schema=spec.tool.output_schema,
    )
    bound._spec, bound._config = spec, plugin.CSAConfig()
    bound._limiter, bound._pending = asyncio.Semaphore(2), set()
    server.add_tool(bound)
    token = snapshot.set(Snapshot("csa-test", "caller", "request", {"tickets": bound}))
    try:
        async with Client(server) as client:
            listed = await client.list_tools()
            assert set(listed[0].input_schema["properties"]) == {"api_key", "request"}
            results = await asyncio.gather(
                *(
                    client.call_tool(
                        "tickets", {"api_key": f"caller-{n}", "request": {"query": {"skip": n}}}
                    )
                    for n in range(8)
                )
            )
            assert all(result.data["ok"] for result in results)
            for request in upstream[0]:
                assert request.headers["x-api-key"] == "caller-" + request.url.params["skip"]
            assert all(client.is_closed for client in upstream[1])
            bad = await client.call_tool("tickets", {"request": {}}, raise_on_error=False)
            assert bad.is_error
    finally:
        snapshot.reset(token)


async def test_size_limit_and_json_null(upstream, monkeypatch):
    _, clients, response = upstream
    response[0] = httpx.Response(
        200, json=None, content=b"null", headers={"content-type": "application/json"}
    )
    assert (await call("me", {}))["data"] is None
    monkeypatch.setattr(plugin, "MAX_RESPONSE_BYTES", 8)
    response[0] = httpx.Response(
        200, content=b"x" * 9, headers={"content-type": "application/json"}
    )
    assert (await call("get_me", {}))["error"] == "response_too_large"
    assert all(client.is_closed for client in clients)


async def test_cancellation_closes_client(monkeypatch):
    entered = asyncio.Event()
    clients = []
    real_client = httpx.AsyncClient

    async def handle(request):
        entered.set()
        await asyncio.Event().wait()

    def factory(**kwargs):
        client = real_client(**kwargs, transport=httpx.MockTransport(handle))
        clients.append(client)
        return client

    monkeypatch.setattr(plugin.httpx, "AsyncClient", factory)
    task = asyncio.create_task(call("get_me", {}))
    await entered.wait()
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert clients[0].is_closed


async def test_project_mismatch_and_order_id_preserved(upstream):
    payload = {
        "path": {"project_id": "project-a"},
        "body": {
            "project_id": "project-b",
            "name": "test",
            "amount": 10,
            "entry_type": "income",
            "date": "2026-09-29",
        },
    }
    result = await call("create_finance_entry", payload)
    assert result["error"] == "project_id_mismatch"
    assert not upstream[0]
    upstream[2][0] = httpx.Response(201, json={"id": "order"})
    order = {
        "revision": 1,
        "plan": "popular",
        "item_ids": ["backend"],
        "request_id": "stable-request-0001",
    }
    result = await call("create_order", {"body": order})
    assert result["ok"]
    assert json.loads(upstream[0][0].content) == order


async def test_mcp_exposes_only_user_tools():
    specs = Catalog(str(ROOT / "plugins")).tools
    server = FastMCP("csa-user-surface")
    for name, spec in specs.items():
        if name.startswith("csa."):
            server.add_tool(spec.tool)
    excluded = {
        "csa.list_users",
        "csa.create_project",
        "csa.reply_ticket",
        "csa.download_export",
        "csa.admin_catalog",
        "csa.create_key",
        "csa.upload_file",
        "csa.send_common_email",
    }
    async with Client(server) as client:
        names = {tool.name for tool in await client.list_tools()}
        assert names == {"csa." + name for name in plugin.OPERATIONS}
        assert len(names) == 61
        assert not excluded.intersection(specs)
        for name in excluded:
            result = await client.call_tool(
                name, {"api_key": "unused", "request": {}}, raise_on_error=False
            )
            assert result.is_error
