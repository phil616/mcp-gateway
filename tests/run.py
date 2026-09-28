"""Run all acceptance tests against ephemeral Compose PostgreSQL/Redis/TLS IDP.
Usage: uv run python tests/run.py
"""

import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

import httpx
from cryptography.fernet import Fernet
from make_certs import generate
from redis import Redis as RedisClient

ROOT = Path(__file__).resolve().parent.parent


def port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def wait(url, env):
    import ssl

    ctx = ssl.create_default_context(cafile=env["SSL_CERT_FILE"])
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        try:
            if httpx.get(url, verify=ctx, timeout=1).status_code == 200:
                return
        except httpx.HTTPError:
            pass
        time.sleep(0.2)
    raise RuntimeError(f"Service not ready: {url}")


def main():
    os.chdir(ROOT)
    with tempfile.TemporaryDirectory(prefix="gateway-acceptance-") as tmp:
        cert, key = generate(tmp)
        pg, redis, idp, backend, console = port(), port(), port(), port(), port()
        env = {
            **os.environ,
            "TEST_PG_PORT": str(pg),
            "TEST_REDIS_PORT": str(redis),
            "TEST_IDP_PORT": str(idp),
            "TEST_CERT_DIR": tmp,
            "TEST_TLS_KEY": key,
            "TEST_IDP_URL": f"https://localhost:{idp}",
            "SSL_CERT_FILE": cert,
            "DATABASE_URL": f"postgresql+asyncpg://gateway:test-only-password@localhost:{pg}/gateway",
            "REDIS_URL": f"redis://localhost:{redis}/0",
            "MASTER_KEY": Fernet.generate_key().decode(),
            "PUBLIC_URL": f"http://localhost:{backend}",
            "TEST_BASE_URL": f"http://localhost:{backend}",
            "CONSOLE_ORIGIN": f"http://localhost:{console}",
            "TEST_CONSOLE_URL": f"http://localhost:{console}",
            "VITE_API_URL": f"http://localhost:{backend}",
            "COOKIE_SECURE": "false",
            "THREAD_LIMIT": "2",
        }
        plugins = Path(tmp) / "plugins"
        shutil.copytree(ROOT / "plugins", plugins)
        shutil.copytree(ROOT / "tests" / "probe", plugins / "probe")
        env["PLUGINS_PATH"] = str(plugins)
        # Do not let a development .env alter this isolated Compose deployment.
        envfile = Path(tmp) / "compose.env"
        envfile.write_text("")
        compose = [
            "docker",
            "compose",
            "--env-file",
            str(envfile),
            "-p",
            "gateway-test-" + uuid.uuid4().hex[:8],
            "-f",
            "compose.test.yml",
        ]
        processes = []
        logpath = Path(tmp) / "servers.log"
        with logpath.open("w+") as log:

            def run(args):
                subprocess.run(args, env=env, check=True)

            try:
                run(compose + ["up", "-d", "--build", "--wait"])
                wait(env["TEST_IDP_URL"] + "/jwks", env)
                run(["uv", "run", "alembic", "upgrade", "head"])
                run(["uv", "run", "gateway", "plugins", "check", "--path", str(plugins)])
                run(["uv", "run", "gateway", "plugins", "sync"])
                run(
                    [
                        "uv",
                        "run",
                        "gateway",
                        "admin-create",
                        "admin",
                        "--password",
                        "test-password-1234",
                    ]
                )
                proc = subprocess.Popen(
                    [
                        "uv",
                        "run",
                        "uvicorn",
                        "gateway.app:create_app",
                        "--factory",
                        "--port",
                        str(backend),
                        "--workers",
                        "2",
                        "--no-access-log",
                    ],
                    env=env,
                    stdout=log,
                    stderr=log,
                )
                processes.append(proc)
                wait(env["PUBLIC_URL"] + "/health/ready", env)
                result = subprocess.run(["uv", "run", "pytest", "-q", *sys.argv[1:]], env=env)
                if result.returncode:
                    log.flush()
                    print(logpath.read_text())
                if result.returncode == 0 and not sys.argv[1:]:
                    # Independent suites share one loopback IP. Reset only login counters
                    # in this runner-owned ephemeral Redis, keeping sessions/config intact.
                    with RedisClient.from_url(env["REDIS_URL"]) as rate_store:
                        keys = list(rate_store.scan_iter("login:*"))
                        if keys:
                            rate_store.delete(*keys)
                    run(["npm", "--prefix", "frontend", "run", "build"])
                    frontend = subprocess.Popen(
                        [
                            "npm",
                            "--prefix",
                            "frontend",
                            "run",
                            "preview",
                            "--",
                            "--port",
                            str(console),
                            "--strictPort",
                        ],
                        env=env,
                        stdout=log,
                        stderr=log,
                        start_new_session=True,
                    )
                    processes.append(frontend)
                    wait(env["TEST_CONSOLE_URL"], env)
                    browser = subprocess.run(
                        ["npx", "playwright", "test"], cwd=ROOT / "frontend", env=env
                    )
                    if browser.returncode:
                        result = browser
                # The same Redis-backed session and PostgreSQL objects must survive restart.
                persisted = httpx.Client(
                    base_url=env["PUBLIC_URL"], headers={"Origin": env["CONSOLE_ORIGIN"]}
                )
                signed_in = persisted.post(
                    "/api/v1/login", json={"username": "admin", "password": "test-password-1234"}
                )
                signed_in.raise_for_status()
                before_groups = persisted.get("/api/v1/groups?limit=200").json()
                before_tools = persisted.get("/api/v1/tools?limit=200").json()
                proc.terminate()
                proc.wait(timeout=20)
                proc = subprocess.Popen(
                    [
                        "uv",
                        "run",
                        "uvicorn",
                        "gateway.app:create_app",
                        "--factory",
                        "--port",
                        str(backend),
                        "--workers",
                        "2",
                        "--no-access-log",
                    ],
                    env=env,
                    stdout=log,
                    stderr=log,
                )
                processes.append(proc)
                wait(env["PUBLIC_URL"] + "/health/ready", env)
                assert persisted.get("/api/v1/me").status_code == 200
                assert persisted.get("/api/v1/groups?limit=200").json() == before_groups
                assert persisted.get("/api/v1/tools?limit=200").json() == before_tools
                persisted.close()
                print(
                    "Restart recovery: administrator session, groups, tool catalog and readiness verified"
                )
                return result.returncode
            except Exception:
                log.flush()
                print(logpath.read_text())
                raise
            finally:
                for proc in processes:
                    if proc.poll() is None:
                        if proc is locals().get("frontend"):
                            import signal

                            os.killpg(proc.pid, signal.SIGTERM)
                        else:
                            proc.terminate()
                        try:
                            proc.wait(timeout=20)
                        except subprocess.TimeoutExpired:
                            proc.kill()
                subprocess.run(
                    compose + ["down", "--volumes", "--remove-orphans"],
                    env=env,
                    stdout=subprocess.DEVNULL,
                )


if __name__ == "__main__":
    raise SystemExit(main())
