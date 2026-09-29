import uuid

import pytest


@pytest.mark.asyncio
async def test_atomic_batch_bindings(api):
    group = "batch-" + uuid.uuid4().hex[:8]
    assert (await api.post("/api/v1/groups", json={"id": group, "data": {}})).status_code == 201
    items = [
        {
            "id": group + "-wait",
            "data": {
                "group_id": group,
                "tool_id": "demo.wait",
                "exposed_name": "wait",
                "enabled": True,
            },
        },
        {
            "id": group + "-echo",
            "data": {
                "group_id": group,
                "tool_id": "demo.echo",
                "exposed_name": "echo",
                "enabled": True,
            },
        },
    ]
    # Missing required echo config rolls back the earlier valid item and its audit event.
    result = await api.post("/api/v1/bindings/batch", json={"items": items})
    assert result.status_code == 422, result.text
    assert result.json()["detail"]["item"] == 2
    assert (await api.get("/api/v1/bindings", params={"group_id": group})).json()["total"] == 0
    audit = (await api.get("/api/v1/audit", params={"q": group + "-wait"})).json()
    assert audit["total"] == 0
    items[1]["data"]["enabled"] = False
    items[1]["data"]["exposed_name"] = "wait"
    result = await api.post("/api/v1/bindings/batch", json={"items": items})
    assert result.status_code == 409
    assert (await api.get("/api/v1/bindings", params={"group_id": group})).json()["total"] == 0
    items[1]["data"]["exposed_name"] = "echo"
    result = await api.post("/api/v1/bindings/batch", json={"items": items})
    assert result.status_code == 201, result.text
    assert len(result.json()["items"]) == 2
    assert (await api.post("/api/v1/bindings/batch", json={"items": items})).status_code == 409
    assert (await api.get("/api/v1/bindings", params={"group_id": group})).json()["total"] == 2
    assert (await api.post("/api/v1/bindings/batch", json={"items": []})).status_code == 422
    assert (
        await api.post("/api/v1/bindings/batch", json={"items": items * 101})
    ).status_code == 422
    items[1]["data"]["group_id"] = "another-group"
    assert (await api.post("/api/v1/bindings/batch", json={"items": items})).status_code == 422
    items[1]["data"]["group_id"] = {"invalid": "type"}
    assert (await api.post("/api/v1/bindings/batch", json={"items": items})).status_code == 422


@pytest.mark.asyncio
async def test_batch_delete_atomic_versions_and_dependencies(api):
    prefix = "delete-" + uuid.uuid4().hex[:8]
    ids = [prefix + "-a", prefix + "-b"]
    for id in ids:
        assert (await api.post("/api/v1/groups", json={"id": id, "data": {}})).status_code == 201
    items = [{"id": id, "version": 1} for id in ids]
    result = await api.post(
        "/api/v1/groups/batch-delete", json={"items": [items[0], {**items[1], "version": 99}]}
    )
    assert result.status_code == 409
    assert (await api.get("/api/v1/groups/" + ids[0])).status_code == 200
    binding = {
        "id": prefix,
        "data": {
            "group_id": ids[1],
            "tool_id": "demo.wait",
            "exposed_name": "wait",
            "enabled": False,
        },
    }
    assert (await api.post("/api/v1/bindings", json=binding)).status_code == 201
    assert (await api.post("/api/v1/groups/batch-delete", json={"items": items})).status_code == 409
    assert (await api.get("/api/v1/groups/" + ids[0])).status_code == 200
    assert (
        await api.post(
            "/api/v1/bindings/batch-delete", json={"items": [{"id": prefix, "version": 1}]}
        )
    ).status_code == 200
    assert (
        await api.post("/api/v1/groups/batch-delete", json={"items": items + items})
    ).status_code == 422
    assert (await api.post("/api/v1/groups/batch-delete", json={"items": items})).json() == {
        "deleted": 2
    }
    for id in ids:
        assert (await api.get("/api/v1/groups/" + id)).status_code == 404
    assert (
        await api.post(
            "/api/v1/tools/batch-delete", json={"items": [{"id": "demo.wait", "version": 1}]}
        )
    ).status_code == 422
    assert (await api.post("/api/v1/groups/batch-delete", json={"items": []})).status_code == 422


@pytest.mark.asyncio
async def test_batch_more_than_fifty_bindings(api):
    group = "large-" + uuid.uuid4().hex[:8]
    assert (await api.post("/api/v1/groups", json={"id": group, "data": {}})).status_code == 201
    tools = (await api.get("/api/v1/tools", params={"q": "csa.", "limit": 200})).json()["items"]
    assert len(tools) > 50
    items = [
        {
            "id": group + "-" + str(i),
            "data": {
                "group_id": group,
                "tool_id": t["id"],
                "exposed_name": "tool-" + str(i),
                "enabled": False,
            },
        }
        for i, t in enumerate(tools)
    ]
    result = await api.post("/api/v1/bindings/batch", json={"items": items}, timeout=60)
    assert result.status_code == 201, result.text
    assert len(result.json()["items"]) == len(tools)
