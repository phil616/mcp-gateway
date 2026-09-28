"""Synthetic business system; real HTTP with token-scoped merchant data and durable evidence."""

import json
import os
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request

app = FastAPI()
config = json.loads(Path(os.environ["SCENARIO_UPSTREAM_CONFIG"]).read_text())
state_path = Path(config["state_path"])
AS_OF = "2026-09-27T12:00:00+00:00"
DATA = {
    "east": {
        "hours": 48,
        "tracking": {
            "ORD-101": ("in_transit", "2026-09-24T12:00:00+00:00"),
            "ORD-102": ("delivered", "2026-09-23T12:00:00+00:00"),
            "ORD-103": ("in_transit", "2026-09-26T12:00:00+00:00"),
            "ORD-104": ("exception", "2026-09-23T12:00:00+00:00"),
            "ORD-105": ("cancelled", "2026-09-20T12:00:00+00:00"),
        },
    },
    "west": {
        "hours": 72,
        "tracking": {
            "ORD-101": ("in_transit", "2026-09-25T00:00:00+00:00"),
            "ORD-102": ("exception", "2026-09-23T12:00:00+00:00"),
            "ORD-103": ("in_transit", "2026-09-25T12:00:00+00:00"),
            "ORD-104": ("in_transit", "2026-09-24T00:00:00+00:00"),
            "ORD-105": ("cancelled", "2026-09-20T12:00:00+00:00"),
        },
    },
}
state = {"events": [], "cases": {}, "transient_failures": []}


def persist():
    temp = state_path.with_suffix(".tmp")
    temp.write_text(json.dumps(state, indent=2))
    temp.replace(state_path)


persist()


def authenticate(request):
    authorization = request.headers.get("authorization", "")
    for merchant, token in config["tokens"].items():
        if authorization == "Bearer " + token:
            return merchant
    raise HTTPException(401, "Invalid upstream credential")


def record(request, merchant, action, order_id=None, **details):
    state["events"].append(
        {
            "merchant": merchant,
            "group": request.headers.get("x-gateway-group"),
            "call_id": request.headers.get("x-call-id"),
            "action": action,
            "order_id": order_id,
            **details,
        }
    )
    persist()


@app.get("/health")
async def health():
    return {"status": "ready"}


@app.get("/orders")
async def orders(request: Request):
    merchant = authenticate(request)
    record(request, merchant, "orders")
    return {
        "merchant": merchant,
        "orders": [
            {"order_id": id, "order_state": "cancelled" if v[0] == "cancelled" else "paid"}
            for id, v in DATA[merchant]["tracking"].items()
        ],
    }


@app.get("/policy")
async def policy(request: Request):
    merchant = authenticate(request)
    record(request, merchant, "policy")
    return {
        "merchant": merchant,
        "as_of": AS_OF,
        "stale_after_hours": DATA[merchant]["hours"],
        "rule": "Create a draft only for paid orders whose shipment is in_transit or exception and whose last update is strictly older than stale_after_hours. Exclude delivered and cancelled orders. No refunds or customer messages.",
    }


@app.get("/tracking/{order_id}")
async def tracking(order_id: str, request: Request):
    merchant = authenticate(request)
    if order_id not in DATA[merchant]["tracking"]:
        raise HTTPException(404, "Unknown order")
    group = request.headers.get("x-gateway-group", "")
    # One failure per east agent, so both clients must recover independently.
    if merchant == "east" and order_id == "ORD-101" and group not in state["transient_failures"]:
        state["transient_failures"].append(group)
        record(request, merchant, "tracking", order_id, status=503)
        raise HTTPException(503, "Injected temporary carrier outage")
    status, at = DATA[merchant]["tracking"][order_id]
    record(request, merchant, "tracking", order_id, status=200)
    return {
        "merchant": merchant,
        "order_id": order_id,
        "shipment_status": status,
        "last_update": at,
    }


@app.post("/cases")
async def draft(request: Request):
    merchant = authenticate(request)
    body = await request.json()
    order_id, reason = body.get("order_id"), body.get("reason", "")
    row = DATA[merchant]["tracking"].get(order_id)
    eligible = (
        row
        and row[0] in {"in_transit", "exception"}
        and (datetime.fromisoformat(AS_OF) - datetime.fromisoformat(row[1])).total_seconds() / 3600
        > DATA[merchant]["hours"]
    )
    if not eligible or not isinstance(reason, str) or len(reason.strip()) < 10:
        record(request, merchant, "draft", order_id, status=422)
        raise HTTPException(422, "Order is not policy-eligible or reason is missing")
    key = merchant + ":" + order_id
    created = key not in state["cases"]
    if created:
        state["cases"][key] = {
            "case_id": f"CASE-{merchant.upper()}-{order_id}",
            "merchant": merchant,
            "order_id": order_id,
            "status": "draft",
            "reason": reason,
        }
    record(request, merchant, "draft", order_id, status=200, created=created)
    return {**state["cases"][key], "created": created}
