"""Integration tests require migrated, isolated PostgreSQL and Redis from .env."""

import asyncio
import os
import time
import uuid

import httpx
import pytest
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from gateway.catalog import Catalog

BASE = os.environ.get("TEST_BASE_URL", "http://localhost:8000")


async def create(api, resource, id, data):
    result = await api.post("/api/v1/" + resource, json={"id": id, "data": data})
    assert result.status_code == 201, result.text
    return result.json()


async def update(api, resource, row, data):
    result = await api.put(
        f"/api/v1/{resource}/{row['id']}", json={"version": row["version"], "data": data}
    )
    assert result.status_code == 200, result.text
    return result.json()


@pytest.mark.asyncio
async def test_management_mcp_isolation_dynamic_and_revocation(api):
    suffix = uuid.uuid4().hex[:8]
    groups = []
    for n in range(2):
        gid = f"g{n}-{suffix}"
        secret = await create(api, "secrets", gid, {"value": f"upstream-key-{n}"})
        assert secret["value"] == "********" and "ciphertext" not in secret
        await create(
            api,
            "config-profiles",
            gid,
            {"values": {"prefix": f"prefix{n}", "api_key": {"$secret": gid}}},
        )
        group = await create(api, "groups", gid, {})
        assert not group["enabled"]
        binding = await create(
            api,
            "bindings",
            gid,
            {
                "group_id": gid,
                "tool_id": "demo.echo",
                "exposed_name": "echo",
                "profile_id": gid,
                "enabled": True,
            },
        )
        group = await update(api, "groups", group, {"enabled": True})
        groups.append((group, binding))

    async def call(n):
        group, _ = groups[n]
        async with Client(f"{BASE}/{group['id']}/mcp") as client:
            tools = await client.list_tools()
            assert [t.name for t in tools] == ["echo"]
            assert "runtime" not in tools[0].input_schema["properties"]
            result = await client.call_tool("echo", {"message": "world"})
            assert result.data == {"message": f"prefix{n} world", "group": group["id"]}

    await asyncio.gather(*(call(n % 2) for n in range(12)))
    group, binding = groups[0]
    # Serializable management validation, optimistic conflict, and dependencies.
    bad = await api.put(
        f"/api/v1/config-profiles/{group['id']}", json={"version": 1, "data": {"values": {}}}
    )
    assert bad.status_code == 422
    delete = await api.delete(f"/api/v1/secrets/{group['id']}?version=1")
    assert delete.status_code == 409 and delete.json()["detail"]["dependencies"]
    conflict = await api.put(
        f"/api/v1/groups/{group['id']}", json={"version": 1, "data": {"enabled": False}}
    )
    assert conflict.status_code == 409
    binding = await update(api, "bindings", binding, {"enabled": False})
    async with Client(f"{BASE}/{group['id']}/mcp") as client:
        assert await client.list_tools() == []
    binding = await update(api, "bindings", binding, {"enabled": True})
    profile = await create(api, "auth-profiles", group["id"], {"mode": "static"})
    group = await update(api, "groups", group, {"auth_profile_id": profile["id"]})
    key = await create(api, "access-keys", group["id"], {"group_id": group["id"]})
    assert "digest" not in key
    assert (await api.get(f"/{group['id']}/mcp")).status_code == 401
    async with Client(
        StreamableHttpTransport(
            f"{BASE}/{group['id']}/mcp", headers={"Authorization": "Bearer " + key["token"]}
        )
    ) as client:
        assert len(await client.list_tools()) == 1
    await update(api, "access-keys", key, {"revoked": True})
    for _ in range(8):
        async with httpx.AsyncClient() as raw:
            assert (
                await raw.get(
                    f"{BASE}/{group['id']}/mcp", headers={"Authorization": "Bearer " + key["token"]}
                )
            ).status_code == 401
    csrf = api.headers.pop("X-CSRF-Token")
    assert (await api.post("/api/v1/groups", json={"id": "no-csrf", "data": {}})).status_code == 403
    api.headers["X-CSRF-Token"] = csrf


@pytest.mark.asyncio
async def test_sync_timeout_health_and_cleanup(api):
    gid = "wait-" + uuid.uuid4().hex[:8]
    await create(api, "groups", gid, {"enabled": True})
    await create(
        api,
        "bindings",
        gid,
        {"group_id": gid, "tool_id": "demo.wait", "exposed_name": "wait", "enabled": True},
    )
    async with Client(f"{BASE}/{gid}/mcp") as client:
        start = time.monotonic()
        task = asyncio.create_task(client.call_tool("wait", {"seconds": 1.5}, raise_on_error=False))
        await asyncio.sleep(0.05)
        assert (await api.get("/health/live")).status_code == 200
        result = await task
        assert result.is_error
        assert time.monotonic() - start < 0.9
        assert (await client.call_tool("wait", {"seconds": 0.01})).data == "done"


def test_discovery_contract_and_failures(tmp_path):
    catalog = Catalog("plugins")
    assert "runtime" not in catalog.tools["demo.echo"].tool.parameters["properties"]
    p = tmp_path / "bad"
    p.mkdir()
    (p / "plugin.py").write_text("import missing_gateway_dependency_xyz")
    with pytest.raises(ValueError, match="missing_gateway_dependency_xyz"):
        Catalog(str(tmp_path))
    (p / "plugin.py").write_text(
        'from gateway_sdk import ToolPackage\npackage=ToolPackage("same","1")'
    )
    other = tmp_path / "other"
    other.mkdir()
    (other / "plugin.py").write_text((p / "plugin.py").read_text())
    with pytest.raises(ValueError, match="Duplicate package"):
        Catalog(str(tmp_path))


@pytest.mark.asyncio
async def test_real_credentials_thread_bound_and_error_redaction(api):
    import hashlib

    # The runner adds a test-only plugin, never part of production artifacts.
    if not os.environ.get("TEST_BASE_URL"):
        pytest.skip("Run tests/run.py to provision the probe plugin")
    suffix = uuid.uuid4().hex[:8]
    group_ids = [f"probe{n}-{suffix}" for n in range(2)]
    for n, gid in enumerate(group_ids):
        await create(api, "secrets", gid, {"value": f"credential-{n}"})
        await create(api, "groups", gid, {"enabled": True})
        await create(
            api,
            "bindings",
            gid,
            {
                "group_id": gid,
                "tool_id": "probe.credential",
                "exposed_name": "credential",
                "enabled": True,
                "overrides": {"key": {"$secret": gid}},
            },
        )

    async def call(n):
        async with Client(f"{BASE}/{group_ids[n]}/mcp") as client:
            result = await client.call_tool("credential", {})
            assert result.data == {
                "group": group_ids[n],
                "digest": hashlib.sha256(f"credential-{n}".encode()).hexdigest(),
            }

    await asyncio.gather(*(call(n % 2) for n in range(20)))
    gid = group_ids[0]
    for name in ("blocked", "stats", "failure"):
        await create(
            api,
            "bindings",
            gid + "-" + name,
            {"group_id": gid, "tool_id": "probe." + name, "exposed_name": name, "enabled": True},
        )

    async def blocking():
        async with Client(f"{BASE}/{gid}/mcp") as client:
            assert (await client.call_tool("blocked", {}, raise_on_error=False)).is_error

    await asyncio.gather(*(blocking() for _ in range(12)))
    await asyncio.sleep(0.6)
    for _ in range(10):
        async with Client(f"{BASE}/{gid}/mcp") as client:
            stats = (await client.call_tool("stats", {})).data
            assert stats["active"] == 0 and stats["peak"] <= 2
            result = await client.call_tool("failure", {}, raise_on_error=False)
            assert result.is_error and "sensitive-upstream-token" not in str(result)


@pytest.mark.asyncio
async def test_global_toggle_static_group_expiry_rotation_and_input_validation(api):
    gid = "static-" + uuid.uuid4().hex[:8]
    await create(api, "auth-profiles", gid, {"mode": "static"})
    group = await create(api, "groups", gid, {"enabled": True, "auth_profile_id": gid})
    await create(api, "groups", gid + "-other", {"enabled": True, "auth_profile_id": gid})
    binding = await create(
        api,
        "bindings",
        gid,
        {"group_id": gid, "tool_id": "demo.wait", "exposed_name": "wait", "enabled": True},
    )
    key = await create(api, "access-keys", gid, {"group_id": gid})
    expired = await create(
        api,
        "access-keys",
        gid + "-expired",
        {"group_id": gid, "expires_at": "2000-01-01T00:00:00+00:00"},
    )
    for path, token in [(gid + "-other", key["token"]), (gid, expired["token"])]:
        assert (
            await api.get(f"/{path}/mcp", headers={"Authorization": "Bearer " + token})
        ).status_code == 401
    rotation = await api.post(
        f"/api/v1/access-keys/{gid}/rotate", json={"version": key["version"], "data": {}}
    )
    assert rotation.status_code == 200
    assert (
        await api.get(f"/{gid}/mcp", headers={"Authorization": "Bearer " + key["token"]})
    ).status_code == 401
    token = rotation.json()["token"]
    detail = (await api.get(f"/api/v1/groups/{gid}")).json()
    example = detail["client_example"]
    connection = example["mcpServers"][gid]
    assert detail["client_examples"]["opencode"] == {
        "mcp": {gid: {**connection, "type": "remote", "oauth": False}}
    }
    assert detail["client_examples"]["vscode"] == {"servers": {gid: connection}}
    assert connection["type"] == "http"
    assert "command" not in connection and "args" not in connection
    assert connection["headers"] == {"Authorization": "Bearer <YOUR_GROUP_ACCESS_KEY>"}
    assert token not in str(detail) and key["token"] not in str(detail)
    assert (await api.get(f"/{gid}/mcp", headers=connection["headers"])).status_code == 401
    assert (await api.get(f"/{gid}/mcp")).status_code == 401
    connection["headers"]["Authorization"] = connection["headers"]["Authorization"].replace(
        "<YOUR_GROUP_ACCESS_KEY>", token
    )
    # Consume the exported configuration directly, without constructing a transport by hand.
    async with Client(example) as configured_client:
        assert [t.name for t in await configured_client.list_tools()] == ["wait"]
        result = await configured_client.call_tool("wait", {"seconds": 0})
        assert not result.is_error
    tool = (await api.get("/api/v1/tools/demo.wait")).json()
    tool = await update(api, "tools", tool, {"enabled": False})
    async with Client(
        StreamableHttpTransport(f"{BASE}/{gid}/mcp", headers={"Authorization": "Bearer " + token})
    ) as client:
        assert await client.list_tools() == []
    await update(api, "tools", tool, {"enabled": True})
    async with Client(
        StreamableHttpTransport(f"{BASE}/{gid}/mcp", headers={"Authorization": "Bearer " + token})
    ) as client:
        assert len(await client.list_tools()) == 1
    for resource, data in [
        ("groups", {"enabled": "false"}),
        ("auth-profiles", {"mode": []}),
        ("config-profiles", {"values": {"key": {"$secret": []}}}),
    ]:
        invalid = await api.post(
            f"/api/v1/{resource}", json={"id": "bad-" + uuid.uuid4().hex, "data": data}
        )
        assert invalid.status_code == 422
    # A failed write must leave no matching audit event.
    audit = await api.get("/api/v1/audit?q=bad-")
    assert audit.json()["total"] == 0
    races = await asyncio.gather(
        *(
            api.put(
                f"/api/v1/groups/{gid}",
                json={"version": group["version"], "data": {"enabled": False}},
            )
            for _ in range(2)
        )
    )
    assert sorted(r.status_code for r in races) == [200, 409]
    assert (
        await api.get(f"/{gid}/mcp", headers={"Authorization": "Bearer " + token})
    ).status_code == 404
    result = await api.delete(f"/api/v1/bindings/{binding['id']}?version={binding['version']}")
    assert result.status_code == 200


@pytest.mark.asyncio
async def test_catalog_removal_retains_history_and_rejects_stale_artifact(tmp_path):
    from gateway.models import ToolDefinition
    from gateway.settings import Settings
    from sqlalchemy import select
    from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

    root = tmp_path / "new_plugins"
    entry = root / "package1"
    entry.mkdir(parents=True)
    (entry / "plugin.py").write_text(
        'from gateway_sdk import ToolPackage\npackage=ToolPackage("temporary","1")\n@package.tool(id="new")\nasync def new(value: str) -> str:\n return value\n'
    )
    catalog = Catalog(str(root))
    engine = create_async_engine(Settings().database_url)
    try:
        async with async_sessionmaker(engine)() as db:
            await catalog.sync(db)
            new = await db.get(ToolDefinition, "temporary.new")
            assert new.data["available"]
            old = await db.get(ToolDefinition, "demo.echo")
            assert old and not old.data["available"]
            with pytest.raises(RuntimeError, match="artifact mismatch"):
                await Catalog("plugins").verify(db)
            (entry / "plugin.py").unlink()
            await Catalog(str(root)).sync(db)
            await db.refresh(new)
            assert not new.data["available"]
            assert len((await db.scalars(select(ToolDefinition))).all()) >= 3
            await db.rollback()  # Isolate this catalog experiment from HTTP workers.
    finally:
        await engine.dispose()
