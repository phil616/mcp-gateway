"""Real HTTP MCP routing, management binding and caller credentials (tests/run.py)."""

import asyncio
import json
import os
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import httpx
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from test_gateway import create, update

BASE = os.environ.get("TEST_BASE_URL", "http://localhost:8000")


async def test_csa_group_binding_and_caller_keys(api):
    # The synced gateway catalog cannot bind admin/service operations.
    for tool_id in (
        "csa.list_users",
        "csa.reply_ticket",
        "csa.download_export",
        "csa.upload_file",
        "csa.send_common_email",
    ):
        response = await api.get("/api/v1/tools/" + tool_id)
        assert response.status_code == 404
    received = []

    class Upstream(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            credential = self.headers.get("X-API-Key")
            received.append((credential, self.headers.get("Authorization")))
            valid = credential in ("caller-a", "caller-b")
            self.send_response(200 if valid else 401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps(
                    {"id": credential[-1]} if valid else {"detail": "invalid-private-key"}
                ).encode()
            )

    server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        suffix = uuid.uuid4().hex[:8]
        gid = "csa-" + suffix
        await create(api, "auth-profiles", gid, {"mode": "static"})
        await create(api, "groups", gid, {"auth_profile_id": gid, "enabled": True})
        binding = await create(
            api,
            "bindings",
            gid,
            {
                "group_id": gid,
                "tool_id": "csa.get_me",
                "exposed_name": "csa_me",
                "enabled": True,
                "overrides": {"base_url": f"http://127.0.0.1:{server.server_port}"},
            },
        )
        key = await create(api, "access-keys", gid, {"group_id": gid})
        endpoint = f"{BASE}/{gid}/mcp"
        async with httpx.AsyncClient() as raw:
            assert (await raw.get(endpoint)).status_code == 401
            assert (
                await raw.get(endpoint, headers={"Authorization": "Bearer caller-a"})
            ).status_code == 401
        transport = StreamableHttpTransport(
            endpoint, headers={"Authorization": "Bearer " + key["token"]}
        )
        async with Client(transport) as client:
            listed = await client.list_tools()
            assert [t.name for t in listed] == ["csa_me"]
            assert set(listed[0].input_schema["properties"]) == {"api_key", "request"}
            results = await asyncio.gather(
                *(
                    client.call_tool("csa_me", {"api_key": "caller-" + owner, "request": {}})
                    for owner in ("a", "b")
                )
            )
            assert [result.data["data"]["id"] for result in results] == ["a", "b"]
            bad = await client.call_tool("csa_me", {"api_key": "invalid", "request": {}})
            assert bad.data == {"ok": False, "status": 401, "error": "upstream_http_error"}
        assert {row[0] for row in received} == {"caller-a", "caller-b", "invalid"}
        assert all(row[1] is None for row in received)
        stored = (await api.get(f"/api/v1/bindings/{gid}")).json()
        assert "api_key" not in json.dumps(stored)
        await update(api, "bindings", binding, {"enabled": False})
        async with Client(transport) as client:
            assert await client.list_tools() == []
    finally:
        await asyncio.to_thread(server.shutdown)
        server.server_close()
        thread.join(timeout=2)
