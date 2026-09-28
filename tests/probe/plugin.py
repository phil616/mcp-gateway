"""Only copied into the ephemeral acceptance plugin directory."""

import asyncio
import hashlib
import threading
import time

from gateway_sdk import Depends, ToolPackage, ToolRuntime, current_runtime
from pydantic import BaseModel, SecretStr

package = ToolPackage(id="probe", version="1")


class Config(BaseModel):
    key: SecretStr


@package.tool(id="credential", config_model=Config)
async def credential(runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    before = runtime.config(Config).key.get_secret_value()
    await asyncio.sleep(0.03)
    after = runtime.config(Config).key.get_secret_value()
    assert before == after
    return {"group": runtime.group, "digest": hashlib.sha256(after.encode()).hexdigest()}


active = 0
peak = 0
lock = threading.Lock()


@package.tool(id="blocked", timeout=0.15)
def blocked() -> str:
    global active, peak
    with lock:
        active += 1
        peak = max(peak, active)
    try:
        time.sleep(0.5)
        return "done"
    finally:
        with lock:
            active -= 1


@package.tool(id="stats")
async def stats() -> dict:
    with lock:
        return {"active": active, "peak": peak}


@package.tool(id="failure")
async def failure() -> str:
    raise RuntimeError("sensitive-upstream-token-must-not-leak")
