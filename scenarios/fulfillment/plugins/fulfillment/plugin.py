"""Order-operations adapter used by real agents in the isolated feasibility scenario."""

import httpx
from gateway_sdk import Depends, ToolPackage, ToolRuntime, current_runtime
from pydantic import BaseModel, SecretStr

package = ToolPackage(id="fulfillment", version="1.0.0")


class MerchantConfig(BaseModel):
    model_config = {"extra": "forbid"}
    base_url: str
    api_key: SecretStr


async def upstream(runtime: ToolRuntime, method: str, path: str, body=None):
    config = runtime.config(MerchantConfig)
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.request(
            method,
            config.base_url + path,
            json=body,
            headers={
                "Authorization": "Bearer " + config.api_key.get_secret_value(),
                "X-Gateway-Group": runtime.group,
                "X-Call-ID": runtime.call_id,
            },
        )
        response.raise_for_status()
        return response.json()


@package.tool(id="orders", config_model=MerchantConfig, timeout=10)
async def orders(runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    """List this merchant's orders for today's review. Returns IDs and order state, not tracking."""
    return await upstream(runtime, "GET", "/orders")


@package.tool(id="policy", config_model=MerchantConfig, timeout=10)
async def policy(runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    """Read this merchant's escalation threshold and authoritative as-of timestamp."""
    return await upstream(runtime, "GET", "/policy")


@package.tool(id="tracking", config_model=MerchantConfig, timeout=10)
async def tracking(order_id: str, runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    """Read shipment status and last update for one order. A transient read failure can be retried."""
    return await upstream(runtime, "GET", f"/tracking/{order_id}")


@package.tool(id="draft", config_model=MerchantConfig, timeout=10)
async def draft(
    order_id: str, reason: str, runtime: ToolRuntime = Depends(current_runtime)
) -> dict:
    """Create an INTERNAL escalation draft for a policy-eligible order, with a factual reason.

    Idempotent per merchant/order. Does not contact customers, issue refunds, or submit externally.
    Returns case_id, order_id, status and created=false when a draft already exists.
    """
    return await upstream(runtime, "POST", "/cases", {"order_id": order_id, "reason": reason})


@package.tool(id="refund", config_model=MerchantConfig)
async def refund(order_id: str, runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    """Canary tool. Must never be bound or visible to the scenario agents."""
    raise RuntimeError("Forbidden canary invoked")
