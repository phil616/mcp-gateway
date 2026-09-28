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
    assert (await api.post("/api/v1/bindings/batch", json={"items": items * 26})).status_code == 422
    items[1]["data"]["group_id"] = "another-group"
    assert (await api.post("/api/v1/bindings/batch", json={"items": items})).status_code == 422
    items[1]["data"]["group_id"] = {"invalid": "type"}
    assert (await api.post("/api/v1/bindings/batch", json={"items": items})).status_code == 422
