import asyncio
import time

from gateway_sdk import Depends, ToolPackage, ToolRuntime, current_runtime
from pydantic import BaseModel, SecretStr

package = ToolPackage(id="demo", version="1.0.0")


class EchoConfig(BaseModel):
    model_config = {"extra": "forbid"}
    prefix: str = "Hello"
    api_key: SecretStr


@package.tool(id="echo", config_model=EchoConfig)
async def echo(message: str, runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    """Demonstrate group-specific configuration without returning credentials."""
    config = runtime.config(EchoConfig)
    await asyncio.sleep(0.01)
    return {"message": f"{config.prefix} {message}", "group": runtime.group}


@package.tool(id="wait", timeout=0.2)
def wait(seconds: float = 0.05) -> str:
    """Demonstrate bounded synchronous execution and timeouts."""
    time.sleep(min(max(seconds, 0), 2))
    return "done"
