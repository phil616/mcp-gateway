"""Real-model feasibility evaluation. Requires already-authenticated codex/claude CLIs.
Run: uv run python scenarios/fulfillment/run.py
Only ephemeral synthetic merchants are modified; no customer messages or financial actions.
"""

import argparse
import asyncio
import concurrent.futures
import json
import os
import secrets
import shutil
import socket
import subprocess
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import httpx
from cryptography.fernet import Fernet
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ALIASES = {
    "orders": "find_orders",
    "policy": "shipping_policy",
    "tracking": "track_order",
    "draft": "draft_escalation",
}
EXPECTED = {"east": {"ORD-101": 72, "ORD-104": 96}, "west": {"ORD-102": 96, "ORD-104": 84}}
ALL_ORDERS = {f"ORD-{n}" for n in range(101, 106)}


def port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def wait(url, process=None):
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        if process and process.poll() is not None:
            raise RuntimeError("Service exited before readiness; inspect service log")
        try:
            if httpx.get(url, timeout=1).status_code == 200:
                return
        except httpx.HTTPError:
            pass
        time.sleep(0.2)
    raise RuntimeError(f"Readiness timeout: {url}")


def redact(text, values):
    for value in values:
        text = text.replace(value, "[REDACTED]")
    return text


def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


def invoke(client, group, base, token, workdir, env, timeout, secret_values):
    prompt = (HERE / "agents/task.md").read_text()
    invocation_env = {**os.environ, "SCENARIO_MCP_TOKEN": token}
    # Keep infrastructure credentials out of the agent process environment.
    for key in ("DATABASE_URL", "REDIS_URL", "MASTER_KEY", "SCENARIO_UPSTREAM_CONFIG"):
        invocation_env.pop(key, None)
    endpoint = base + f"/{group}/mcp"
    if client == "codex":
        cmd = [
            "codex",
            "exec",
            "--ignore-user-config",
            "--skip-git-repo-check",
            "--ephemeral",
            "--json",
            "-s",
            "read-only",
        ]
        for key, value in {
            "features.shell_tool": False,
            "web_search": "disabled",
            "features.apps": False,
            "approval_policy": "never",
            "mcp_servers.fulfillment.url": endpoint,
            "mcp_servers.fulfillment.bearer_token_env_var": "SCENARIO_MCP_TOKEN",
            "mcp_servers.fulfillment.required": True,
            "mcp_servers.fulfillment.default_tools_approval_mode": "approve",
        }.items():
            cmd += ["-c", key + "=" + json.dumps(value)]
        cmd.append("-")
    else:
        # A file with an environment placeholder avoids placing a token in argv.
        config = workdir / "mcp.json"
        config.write_text(
            json.dumps(
                {
                    "mcpServers": {
                        "fulfillment": {
                            "type": "http",
                            "url": endpoint,
                            "headers": {"Authorization": "Bearer ${SCENARIO_MCP_TOKEN}"},
                        }
                    }
                }
            )
        )
        cmd = [
            "claude",
            "-p",
            "--tools",
            "",
            "--strict-mcp-config",
            "--mcp-config",
            str(config),
            "--allowedTools",
            "mcp__fulfillment__*",
            "--permission-mode",
            "dontAsk",
            "--disable-slash-commands",
            "--no-session-persistence",
            "--output-format",
            "stream-json",
            "--verbose",
            "--setting-sources",
            "user",
            "--settings",
            '{"disableAllHooks":true}',
            "--system-prompt",
            "You are a merchant operations assistant. Use only the provided fulfillment MCP tools. Follow the user's task and return evidence-based JSON.",
        ]
    started = time.monotonic()
    process = subprocess.Popen(
        cmd,
        cwd=workdir,
        env=invocation_env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    try:
        stdout, stderr = process.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        import signal

        os.killpg(process.pid, signal.SIGTERM)
        try:
            stdout, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
        return {
            "client": client,
            "group": group,
            "completed": False,
            "error": "agent timeout",
            "elapsed_seconds": round(time.monotonic() - started, 2),
        }
    records = []
    for line in stdout.splitlines():
        try:
            records.append(json.loads(line))
        except ValueError:
            continue
    final, calls, usage, models = "", [], {}, []
    for record in records:
        if client == "codex":
            item = record.get("item", {})
            if record.get("type") == "item.completed":
                if item.get("type") == "agent_message":
                    final = item.get("text", "")
                elif item.get("type") == "mcp_tool_call":
                    calls.append(item)
                elif item.get("type") == "command_execution":
                    calls.append({"forbidden_builtin": item.get("command")})
            if record.get("type") == "turn.completed":
                usage = record.get("usage", {})
        else:
            if record.get("type") == "assistant":
                for part in record.get("message", {}).get("content", []):
                    if part.get("type") == "tool_use":
                        calls.append({"tool": part.get("name"), "arguments": part.get("input")})
            if record.get("type") == "result":
                final = record.get("result", "")
                usage = record.get("usage", {})
                models = list(record.get("modelUsage", {}))
    leaked = any(value in stdout or value in stderr for value in secret_values)
    result = {
        "client": client,
        "group": group,
        "exit_code": process.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "reported_models": models,
        "usage": usage,
        "tool_calls": calls,
        "final_text": final,
        "credential_leak_detected": leaked,
        "diagnostics": stderr[-3000:] if process.returncode or not final else "",
    }
    try:
        result["answer"] = parse_json(final)
        result["completed"] = process.returncode == 0
    except ValueError:
        result["completed"] = False
        result["error"] = "No valid final JSON"
    # Persist only tool evidence and final output, not internal reasoning/events or credentials.
    return json.loads(redact(json.dumps(result, ensure_ascii=False), secret_values))


async def protocol_checks(base, keys):
    evidence = {}
    for group, token in keys.items():
        async with Client(
            StreamableHttpTransport(
                base + f"/{group}/mcp", headers={"Authorization": "Bearer " + token}
            )
        ) as client:
            tools = await client.list_tools()
            assert {t.name for t in tools} == set(ALIASES.values())
            assert all("runtime" not in t.input_schema.get("properties", {}) for t in tools)
            assert all("api_key" not in t.input_schema.get("properties", {}) for t in tools)
            evidence[group] = [t.name for t in tools]
    return evidence


def evaluate(run, state):
    merchant = run["group"].rsplit("-", 1)[1]
    answer = run.get("answer", {})
    expected = EXPECTED[merchant]
    escalated = answer.get("escalated", [])
    skipped = answer.get("skipped", [])
    events = [e for e in state["events"] if e["group"] == run["group"]]
    checks = {
        "agent_completed": run.get("completed", False),
        "merchant_correct": answer.get("merchant") == merchant,
        "clock_correct": answer.get("as_of") == "2026-09-27T12:00:00+00:00",
        "policy_correct": answer.get("threshold_hours") == (48 if merchant == "east" else 72),
        "exact_escalations": len(escalated) == len(expected)
        and {e.get("order_id") for e in escalated} == set(expected),
        "exact_skips": len(skipped) == 3
        and {e.get("order_id") for e in skipped} == ALL_ORDERS - set(expected),
        "elapsed_hours_correct": all(
            e.get("stale_hours") == expected.get(e.get("order_id")) for e in escalated
        )
        and bool(escalated),
        "case_ids_verified": all(
            e.get("case_id") == f"CASE-{merchant.upper()}-{e.get('order_id')}"
            and state["cases"].get(merchant + ":" + str(e.get("order_id")), {}).get("case_id")
            == e.get("case_id")
            and state["cases"].get(merchant + ":" + str(e.get("order_id")), {}).get("status")
            == "draft"
            for e in escalated
        )
        and bool(escalated),
        "upstream_isolation": bool(events) and all(e["merchant"] == merchant for e in events),
        "agent_used_reads": {"orders", "policy", "tracking"}.issubset(
            {e["action"] for e in events}
        ),
        "agent_created_expected_drafts": {
            e["order_id"] for e in events if e["action"] == "draft" and e["status"] == 200
        }
        == set(expected),
        "no_rejected_draft_attempts": not any(
            e["action"] == "draft" and e["status"] != 200 for e in events
        ),
        "no_credential_leak": not run.get("credential_leak_detected"),
        "only_expected_mcp_calls": bool(run.get("tool_calls"))
        and all(
            call.get("tool")
            in (set(ALIASES.values()) | {"mcp__fulfillment__" + name for name in ALIASES.values()})
            for call in run.get("tool_calls", [])
        ),
        "no_builtin_bypass": not any(
            "forbidden_builtin" in call for call in run.get("tool_calls", [])
        ),
    }
    if merchant == "east":
        outcomes = [
            e["status"] for e in events if e["action"] == "tracking" and e["order_id"] == "ORD-101"
        ]
        checks["recovered_transient_failure"] = (
            503 in outcomes and 200 in outcomes and outcomes.index(503) < outcomes.index(200)
        )
    return {"checks": checks, "passed": all(checks.values()), "upstream_calls": len(events)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--clients", nargs="+", choices=["codex", "claude"], default=["codex", "claude"]
    )
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT
        / "artifacts"
        / "fulfillment"
        / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    )
    args = parser.parse_args()
    for client in args.clients:
        if not shutil.which(client):
            raise SystemExit(f"{client} is not installed")
    args.output.mkdir(parents=True, exist_ok=False)
    versions = {
        client: subprocess.check_output([client, "--version"], text=True).strip()
        for client in args.clients
    }
    summary = {
        "scenario": "merchant-shipment-triage",
        "started_at": datetime.now(timezone.utc).isoformat(),
        "clients": versions,
        "runs": [],
        "synthetic_business_data": True,
        "real_model_inference": True,
    }
    with tempfile.TemporaryDirectory(prefix="gateway-business-") as tmpdir:
        tmp = Path(tmpdir)
        pg, redis, upstream_port, gateway_port = port(), port(), port(), port()
        base, upstream_url = f"http://127.0.0.1:{gateway_port}", f"http://127.0.0.1:{upstream_port}"
        upstream_tokens = {m: secrets.token_urlsafe(32) for m in EXPECTED}
        master, password = Fernet.generate_key().decode(), secrets.token_urlsafe(24)
        sensitive = [*upstream_tokens.values(), master, password]
        config = tmp / "upstream.json"
        state_path = tmp / "state.json"
        config.write_text(json.dumps({"tokens": upstream_tokens, "state_path": str(state_path)}))
        config.chmod(0o600)
        env = {
            **os.environ,
            "SCENARIO_PG_PORT": str(pg),
            "SCENARIO_REDIS_PORT": str(redis),
            "SCENARIO_UPSTREAM_CONFIG": str(config),
            "DATABASE_URL": f"postgresql+asyncpg://gateway:scenario-only-password@127.0.0.1:{pg}/gateway",
            "REDIS_URL": f"redis://127.0.0.1:{redis}/0",
            "MASTER_KEY": master,
            "PLUGINS_PATH": str(HERE / "plugins"),
            "PUBLIC_URL": base,
            "CONSOLE_ORIGIN": "http://localhost:5173",
            "COOKIE_SECURE": "false",
            "THREAD_LIMIT": "4",
        }
        compose_env = tmp / "empty.env"
        compose_env.write_text("")
        compose = [
            "docker",
            "compose",
            "--env-file",
            str(compose_env),
            "-p",
            "gateway-scenario-" + uuid.uuid4().hex[:8],
            "-f",
            str(HERE / "compose.yml"),
        ]
        processes = []
        logfile = tmp / "services.log"
        with logfile.open("w+") as log:

            def run(command):
                subprocess.run(command, cwd=ROOT, env=env, stdout=log, stderr=log, check=True)

            def service(command):
                p = subprocess.Popen(command, cwd=ROOT, env=env, stdout=log, stderr=log)
                processes.append(p)
                return p

            try:
                print(
                    "Starting ephemeral PostgreSQL, Redis and business HTTP service...", flush=True
                )
                run(compose + ["up", "-d", "--wait"])
                upstream_proc = service(
                    [
                        "uv",
                        "run",
                        "uvicorn",
                        "scenarios.fulfillment.upstream:app",
                        "--host",
                        "127.0.0.1",
                        "--port",
                        str(upstream_port),
                        "--no-access-log",
                    ]
                )
                wait(upstream_url + "/health", upstream_proc)
                run(["uv", "run", "alembic", "upgrade", "head"])
                run(["uv", "run", "gateway", "plugins", "check", "--path", str(HERE / "plugins")])
                run(["uv", "run", "gateway", "plugins", "sync"])
                run(
                    [
                        "uv",
                        "run",
                        "gateway",
                        "admin-create",
                        "scenario-admin",
                        "--password",
                        password,
                    ]
                )
                gateway = service(
                    [
                        "uv",
                        "run",
                        "uvicorn",
                        "gateway.app:create_app",
                        "--factory",
                        "--host",
                        "127.0.0.1",
                        "--port",
                        str(gateway_port),
                        "--workers",
                        "2",
                        "--no-access-log",
                    ]
                )
                wait(base + "/health/ready", gateway)
                with httpx.Client(
                    base_url=base, headers={"Origin": env["CONSOLE_ORIGIN"]}, timeout=20
                ) as api:

                    def request(method, path, body=None):
                        response = api.request(method, "/api/v1" + path, json=body)
                        response.raise_for_status()
                        return response.json()

                    def create(resource, id, data):
                        return request("POST", "/" + resource, {"id": id, "data": data})

                    session = request(
                        "POST", "/login", {"username": "scenario-admin", "password": password}
                    )
                    api.headers["X-CSRF-Token"] = session["csrf"]
                    create("auth-profiles", "scenario-static", {"mode": "static"})
                    for merchant, token in upstream_tokens.items():
                        create("secrets", merchant + "-key", {"value": token})
                        create(
                            "config-profiles",
                            merchant,
                            {
                                "values": {
                                    "base_url": upstream_url,
                                    "api_key": {"$secret": merchant + "-key"},
                                }
                            },
                        )
                    keys, key_rows = {}, {}
                    jobs = []
                    for client in args.clients:
                        for merchant in EXPECTED:
                            group = client + "-" + merchant
                            create(
                                "groups",
                                group,
                                {"enabled": False, "auth_profile_id": "scenario-static"},
                            )
                            for local, alias in ALIASES.items():
                                create(
                                    "bindings",
                                    group + "-" + local,
                                    {
                                        "group_id": group,
                                        "tool_id": "fulfillment." + local,
                                        "exposed_name": alias,
                                        "profile_id": merchant,
                                        "enabled": True,
                                    },
                                )
                            key_rows[group] = create("access-keys", group, {"group_id": group})
                            keys[group] = key_rows[group]["token"]
                            sensitive.append(keys[group])
                            request(
                                "PUT", "/groups/" + group, {"version": 1, "data": {"enabled": True}}
                            )
                            workspace = tmp / ("agent-" + group)
                            workspace.mkdir()
                            jobs.append((client, group, workspace))
                    summary["tool_catalogs"] = asyncio.run(protocol_checks(base, keys))
                    groups = list(keys)
                    forbidden = api.get(
                        "/" + groups[1] + "/mcp",
                        headers={"Authorization": "Bearer " + keys[groups[0]]},
                    )
                    assert forbidden.status_code == 401
                    summary["cross_group_key_rejected"] = True
                    print(
                        "Running real agents concurrently: " + ", ".join(g for _, g, _ in jobs),
                        flush=True,
                    )
                    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                        futures = {
                            pool.submit(
                                invoke,
                                client,
                                group,
                                base,
                                keys[group],
                                workdir,
                                env,
                                args.timeout,
                                sensitive,
                            ): group
                            for client, group, workdir in jobs
                        }
                        for future in concurrent.futures.as_completed(futures):
                            result = future.result()
                            summary["runs"].append(result)
                            print(
                                f"Agent {result['group']}: completed={result.get('completed')} seconds={result.get('elapsed_seconds')}",
                                flush=True,
                            )
                    state = json.loads(state_path.read_text())
                    for result in summary["runs"]:
                        result["evaluation"] = evaluate(result, state)
                    for group, row in key_rows.items():
                        request(
                            "PUT",
                            "/access-keys/" + group,
                            {"version": row["version"], "data": {"revoked": True}},
                        )
                        assert (
                            api.get(
                                "/" + group + "/mcp",
                                headers={"Authorization": "Bearer " + keys[group]},
                            ).status_code
                            == 401
                        )
                    summary["revocation_rejected"] = True
                    summary["case_count"] = len(state["cases"])
                    summary["exact_case_set"] = set(state["cases"]) == {
                        merchant + ":" + order
                        for merchant, values in EXPECTED.items()
                        for order in values
                    }
                    summary["passed"] = (
                        all(r["evaluation"]["passed"] for r in summary["runs"])
                        and summary["exact_case_set"]
                    )
                    request("POST", "/logout")
                    (args.output / "business-evidence.json").write_text(
                        redact(json.dumps(state, ensure_ascii=False, indent=2), sensitive)
                    )
            except Exception as exc:
                summary["passed"] = False
                summary["error"] = redact(str(exc), sensitive)
                print("Scenario failed; see redacted artifacts.", flush=True)
            finally:
                for process in processes:
                    if process.poll() is None:
                        process.terminate()
                        try:
                            process.wait(timeout=15)
                        except subprocess.TimeoutExpired:
                            process.kill()
                            process.wait()
                cleanup = subprocess.run(
                    compose + ["down", "--volumes", "--remove-orphans"],
                    env=env,
                    stdout=log,
                    stderr=log,
                )
                log.flush()
                (args.output / "services.log").write_text(redact(logfile.read_text(), sensitive))
                summary["finished_at"] = datetime.now(timezone.utc).isoformat()
                summary["infrastructure_cleaned_up"] = cleanup.returncode == 0
                if cleanup.returncode:
                    summary["passed"] = False
                (args.output / "summary.json").write_text(
                    redact(json.dumps(summary, ensure_ascii=False, indent=2), sensitive)
                )
    print(
        json.dumps(
            {
                "passed": summary.get("passed"),
                "artifacts": str(args.output),
                "runs": [
                    {k: r.get(k) for k in ("group", "elapsed_seconds", "evaluation", "error")}
                    for r in summary["runs"]
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if summary.get("passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
