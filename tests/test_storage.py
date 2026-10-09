"""Offline contract, HTTP protocol and real MCP adapter checks."""

import asyncio
import base64
import importlib
import json
import subprocess
from pathlib import Path

import httpx
import pytest
import yaml
from fastmcp import Client, FastMCP
from gateway.catalog import Catalog
from gateway.mcp import BoundTool, Snapshot, snapshot
from jsonschema import Draft202012Validator
from pydantic import ValidationError

ROOT = Path(__file__).resolve().parents[1]
Catalog(str(ROOT / "plugins"))
plugin = importlib.import_module("plugins.storage.plugin")
ID = "12345678-1234-4234-8234-123456789abc"
CONFIG = plugin.StorageConfig(base_url="https://storage.example")


@pytest.fixture
def upstream(monkeypatch):
    requests, clients = [], []
    result = [httpx.Response(200, json={"items": []})]
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


async def call(name, request, key="test-storage-secret"):
    return await plugin.execute(plugin.OPERATIONS[name], request, CONFIG, key)


def test_reviewed_surface_and_fresh_contract():
    subprocess.run(
        ["uv", "run", "python", "scripts/generate_storage.py", "--check"], cwd=ROOT, check=True
    )
    document = yaml.safe_load((ROOT / "plugins/storage/docs/openapi.yaml").read_bytes())
    expected = {
        (method.upper(), path)
        for path, methods in document["paths"].items()
        for method, op in methods.items()
        if isinstance(op, dict)
        and {"apiKeyBearer": []} in op.get("security", [])
        and op.get("x-api-scope") not in {"projects:write", "projects:delete"}
    }
    assert {(o["method"], o["path"]) for o in plugin.OPERATIONS.values()} == expected
    assert len(expected) == 17
    for spec in plugin.package.tools.values():
        assert set(spec.tool.parameters["properties"]) == {"api_key", "request"}
        Draft202012Validator.check_schema(spec.tool.parameters)
        assert set(spec.config_model.model_fields) == {"base_url"}


@pytest.mark.parametrize(
    "url",
    [
        "https://u:p@example.com",
        "https://example.com/api/v1",
        "http://remote.example",
        "https://example.com?key=x",
        "file:///etc/passwd",
        "https://example.com#x",
    ],
)
def test_config_rejects_non_origins(url):
    with pytest.raises(ValidationError):
        plugin.StorageConfig(base_url=url)


async def test_method_path_query_body_and_no_content(upstream):
    requests, clients, response = upstream
    assert (await call("list_nodes", {"path": {"projectID": ID}, "query": {"parent_id": ""}}))["ok"]
    assert requests[-1].url.path == f"/api/v1/projects/{ID}/nodes"
    assert dict(requests[-1].url.params) == {"parent_id": ""}
    assert requests[-1].headers["Authorization"] == "Bearer test-storage-secret"
    assert "cookie" not in requests[-1].headers and "x-api-key" not in requests[-1].headers
    response[0] = httpx.Response(201, json={"id": ID})
    payload = {"name": "资料", "storage_backend_id": ID}
    assert (await call("create_project", {"body": payload}))["ok"]
    assert json.loads(requests[-1].content) == payload
    assert requests[-1].method == "POST"
    response[0] = httpx.Response(204)
    assert await call("delete_node", {"path": {"nodeID": ID}}) == {
        "ok": True,
        "status": 204,
        "data": None,
    }
    assert all(c.is_closed for c in clients)


@pytest.mark.parametrize(
    "name,payload",
    [
        ("get_node", {"path": {"nodeID": "../admin"}}),
        ("get_project", {}),
        ("list_projects", {"query": {"limit": 10}}),
        ("list_projects", {"header": {"Authorization": "bad"}}),
        ("update_node", {"path": {"nodeID": ID}, "body": {}}),
        ("create_directory", {"path": {"projectID": ID}, "body": {"name": "x", "bad": 1}}),
        ("presign_upload_parts", {"path": {"uploadID": ID}, "body": {"part_numbers": [1, 1]}}),
        ("download_local_content", {"path": {"nodeID": ID}, "header": {"Range": "bytes=1-2,3-4"}}),
        ("download_local_content", {"path": {"nodeID": ID}, "header": {"Range": "x\r\nX: y"}}),
    ],
)
async def test_invalid_arguments_no_http(upstream, name, payload):
    assert (await call(name, payload))["error"] == "invalid_arguments"
    assert not upstream[0]


@pytest.mark.parametrize("key", ["", "has space", "x\r\ny", "中文"])
async def test_invalid_credentials(upstream, key):
    assert (await call("list_projects", {}, key))["error"] == "invalid_api_key"
    assert not upstream[0]


async def test_binary_roundtrip_and_head(upstream):
    requests, _, response = upstream
    raw = b'\x00\xff{"arbitrary":"bytes"}\r\n'
    encoded = base64.b64encode(raw).decode()
    response[0] = httpx.Response(204)
    assert (await call("upload_local_content", {"path": {"uploadID": ID}, "body_base64": encoded}))[
        "ok"
    ]
    assert requests[-1].content == raw and requests[-1].method == "PUT"
    assert requests[-1].headers["content-type"] == "application/octet-stream"
    response[0] = httpx.Response(
        206,
        content=raw,
        headers={
            "Content-Type": "application/json",
            "Content-Range": "bytes 0-24/100",
            "Set-Cookie": "private-cookie",
            "X-Private": "secret",
        },
    )
    result = await call(
        "download_local_content", {"path": {"nodeID": ID}, "header": {"Range": "bytes=0-24"}}
    )
    assert result["data"]["body_base64"] == encoded
    assert result["status"] == 206
    assert result["data"]["headers"]["content-range"] == "bytes 0-24/100"
    assert "set-cookie" not in result["data"]["headers"]
    assert requests[-1].headers["Range"] == "bytes=0-24"
    response[0] = httpx.Response(200, headers={"Content-Length": "999"})
    result = await call("head_local_content", {"path": {"nodeID": ID}})
    assert result["data"] == {"headers": {"content-length": "999"}}
    assert requests[-1].method == "HEAD"


async def test_invalid_base64_and_request_size(upstream, monkeypatch):
    payload = {"path": {"uploadID": ID}, "body_base64": "%%%"}
    assert (await call("upload_local_content", payload))["error"] == "invalid_base64"
    monkeypatch.setattr(plugin, "MAX_UPLOAD_BYTES", 1)
    payload["body_base64"] = "eHg="
    assert (await call("upload_local_content", payload))["error"] == "request_too_large"
    monkeypatch.setattr(plugin, "MAX_JSON_BYTES", 1)
    assert (await call("complete_upload", {"path": {"uploadID": ID}, "body": {}}))[
        "error"
    ] == "request_too_large"
    assert not upstream[0]


async def test_binary_base64_is_not_redacted(upstream):
    upstream[2][0] = httpx.Response(200, content=b"hello")
    result = await call("download_local_content", {"path": {"nodeID": ID}}, key="aGVs")
    assert base64.b64decode(result["data"]["body_base64"]) == b"hello"


@pytest.mark.parametrize("status", [301, 307, 400, 401, 403, 409, 416, 429, 500])
async def test_errors_never_retry_or_follow_redirects(upstream, status):
    upstream[2][0] = httpx.Response(
        status, text="test-storage-secret", headers={"Location": "https://other.example"}
    )
    assert await call("list_projects", {}) == {
        "ok": False,
        "status": status,
        "error": "upstream_http_error",
    }
    assert len(upstream[0]) == 1 and upstream[1][0].is_closed


async def test_response_bounds_errors_and_presigned_urls(upstream, monkeypatch):
    response = upstream[2]
    url = "https://bucket.example/file?signature=short-lived"
    response[0] = httpx.Response(200, json={"delivery": "external", "url": url})
    assert (await call("create_download", {"path": {"nodeID": ID}}))["data"]["url"] == url
    assert len(upstream[0]) == 1  # The adapter never follows delivery URLs.
    response[0] = httpx.Response(200, json={"message": "test-storage-secret"})
    assert "test-storage-secret" not in str(await call("list_projects", {}))
    response[0] = httpx.Response(200, content=b"{bad", headers={"Content-Type": "application/json"})
    assert (await call("list_projects", {}))["error"] == "invalid_upstream_json"
    response[0] = httpx.ReadTimeout("private")
    assert (await call("list_projects", {}))["error"] == "upstream_timeout"
    response[0] = httpx.ConnectError("private")
    assert (await call("list_projects", {}))["error"] == "upstream_transport_error"
    monkeypatch.setattr(plugin, "MAX_RESPONSE_BYTES", 2)
    response[0] = httpx.Response(200, content=b"abc")
    assert (await call("download_local_content", {"path": {"nodeID": ID}}))[
        "error"
    ] == "response_too_large"
    assert all(c.is_closed for c in upstream[1])


async def test_real_mcp_binding_and_per_call_credentials(upstream):
    server = FastMCP("storage-test")
    spec = plugin.package.tools["storage.list_projects"]
    bound = BoundTool(
        name="projects",
        description=spec.tool.description,
        parameters=spec.tool.parameters,
        output_schema=spec.tool.output_schema,
    )
    bound._spec, bound._config = spec, CONFIG
    bound._limiter, bound._pending = asyncio.Semaphore(2), set()
    server.add_tool(bound)
    token = snapshot.set(Snapshot("storage-test", "caller", "request", {"projects": bound}))
    try:
        async with Client(server) as client:
            listed = await client.list_tools()
            assert set(listed[0].input_schema["properties"]) == {"api_key", "request"}
            results = await asyncio.gather(
                *(
                    client.call_tool("projects", {"api_key": f"caller-{n}", "request": {}})
                    for n in range(8)
                )
            )
            assert all(r.data["ok"] for r in results)
            assert {r.headers["authorization"] for r in upstream[0]} == {
                f"Bearer caller-{n}" for n in range(8)
            }
            bad = await client.call_tool("projects", {"request": {}}, raise_on_error=False)
            assert bad.is_error
    finally:
        snapshot.reset(token)


async def test_mcp_excludes_admin_and_session_only_operations():
    server = FastMCP("storage-surface")
    for spec in plugin.package.tools.values():
        server.add_tool(spec.tool)
    async with Client(server) as client:
        names = {t.name for t in await client.list_tools()}
        assert names == {"storage." + name for name in plugin.OPERATIONS}
        for name in (
            "update_project",
            "delete_project",
            "list_project_members",
            "create_share",
            "create_api_key",
            "list_users",
            "login",
        ):
            assert "storage." + name not in names
            assert (await client.call_tool("storage." + name, {}, raise_on_error=False)).is_error


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
    task = asyncio.create_task(call("list_projects", {}))
    await entered.wait()
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert clients[0].is_closed
