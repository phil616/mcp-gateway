"""Guard the evaluation against accepting plausible-looking but unexecuted answers."""

from copy import deepcopy

from scenarios.fulfillment.run import EXPECTED, evaluate


def valid_run_and_state():
    merchant, group = "east", "codex-east"
    events = [
        {"group": group, "merchant": merchant, "action": action} for action in ("orders", "policy")
    ]
    events += [
        {
            "group": group,
            "merchant": merchant,
            "action": "tracking",
            "order_id": "ORD-101",
            "status": status,
        }
        for status in (503, 200)
    ]
    events += [
        {"group": group, "merchant": merchant, "action": "draft", "order_id": order, "status": 200}
        for order in EXPECTED[merchant]
    ]
    cases = {
        merchant + ":" + order: {"case_id": "CASE-EAST-" + order, "status": "draft"}
        for order in EXPECTED[merchant]
    }
    answer = {
        "merchant": merchant,
        "as_of": "2026-09-27T12:00:00+00:00",
        "threshold_hours": 48,
        "escalated": [
            {"order_id": order, "case_id": "CASE-EAST-" + order, "stale_hours": hours}
            for order, hours in EXPECTED[merchant].items()
        ],
        "skipped": [
            {"order_id": order, "reason": "not eligible"}
            for order in ("ORD-102", "ORD-103", "ORD-105")
        ],
    }
    return {
        "group": group,
        "completed": True,
        "answer": answer,
        "tool_calls": [{"tool": "find_orders"}],
        "credential_leak_detected": False,
    }, {"events": events, "cases": cases}


def test_no_success_from_answer_without_side_effect_evidence():
    run, state = valid_run_and_state()
    assert evaluate(run, state)["passed"]
    assert not evaluate(run, {"events": [], "cases": {}})["passed"]


def test_rejects_wrong_merchant_and_duplicate_or_wrong_case():
    run, state = valid_run_and_state()
    contaminated = deepcopy(state)
    contaminated["events"][0]["merchant"] = "west"
    assert not evaluate(run, contaminated)["passed"]
    run["answer"]["escalated"][0]["case_id"] = "invented"
    assert not evaluate(run, state)["passed"]


def test_rejects_hidden_rejected_writes_and_no_recovery():
    run, state = valid_run_and_state()
    state["events"].append(
        {
            "group": run["group"],
            "merchant": "east",
            "action": "draft",
            "order_id": "ORD-103",
            "status": 422,
        }
    )
    assert not evaluate(run, state)["passed"]
    state["events"].pop()
    state["events"] = [e for e in state["events"] if e.get("status") != 503]
    assert not evaluate(run, state)["passed"]
