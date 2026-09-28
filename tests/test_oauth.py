import os
import uuid
from urllib.parse import parse_qs, urlparse

import httpx
import pytest
from fastmcp import Client
from fastmcp.client.auth import OAuth
from mcp.client.auth import AuthorizationCodeResult
from test_gateway import BASE, create

IDP = os.environ.get("TEST_IDP_URL", "https://localhost:9443")


class AutomaticConsent(OAuth):
    """Follow the test IDP's consent redirect, preserving the real client's PKCE flow."""

    async def redirect_handler(self, authorization_url):
        async with httpx.AsyncClient() as client:
            response = await client.get(authorization_url)
            assert response.status_code == 302, response.text
            query = parse_qs(urlparse(response.headers["location"]).query)
            self.result = AuthorizationCodeResult(
                code=query["code"][0], state=query["state"][0], iss=query["iss"][0]
            )

    async def callback_handler(self):
        return self.result


@pytest.mark.asyncio
async def test_oauth_discovery_pkce_real_client_and_rejections(api):
    gid = "oauth-" + uuid.uuid4().hex[:8]
    await create(
        api,
        "auth-profiles",
        gid,
        {
            "mode": "oauth",
            "issuer": IDP,
            "validation": "jwt",
            "jwks_url": IDP + "/jwks",
            "scopes": ["tools:call"],
        },
    )
    await create(api, "groups", gid, {"enabled": True, "auth_profile_id": gid})
    await create(
        api,
        "bindings",
        gid,
        {"group_id": gid, "tool_id": "demo.wait", "exposed_name": "wait", "enabled": True},
    )
    resource = f"{BASE}/{gid}/mcp"
    metadata = await api.get(f"/.well-known/oauth-protected-resource/{gid}/mcp")
    assert metadata.json()["resource"] == resource
    assert metadata.json()["authorization_servers"] == [IDP]
    challenge = await api.get(f"/{gid}/mcp")
    assert (
        challenge.status_code == 401
        and "resource_metadata=" in challenge.headers["www-authenticate"]
    )
    async with Client(resource, auth=AutomaticConsent(resource, scopes=["tools:call"])) as client:
        assert len(await client.list_tools()) == 1
        assert (await client.call_tool("wait", {"seconds": 0})).data == "done"
    async with httpx.AsyncClient() as client:
        for claims, status in [
            ({"exp": 1}, 401),
            ({"aud": BASE + "/other/mcp"}, 401),
            ({"scope": ""}, 403),
            ({"iss": "https://wrong.example"}, 401),
        ]:
            result = await client.post(
                IDP + "/test/token", json={"audience": resource, "claims": claims}
            )
            response = await client.get(
                resource, headers={"Authorization": "Bearer " + result.json()["token"]}
            )
            assert response.status_code == status, response.text
    # An IDP without PKCE and resource support cannot complete the MCP flow.
    legacy = "legacy-" + uuid.uuid4().hex[:8]
    await create(
        api,
        "auth-profiles",
        legacy,
        {
            "mode": "oauth",
            "issuer": IDP + "/legacy",
            "validation": "jwt",
            "jwks_url": IDP + "/jwks",
        },
    )
    await create(api, "groups", legacy, {"enabled": True, "auth_profile_id": legacy})
    report = await api.get(f"/api/v1/auth-profiles/{legacy}/compatibility")
    assert report.status_code == 200
    assert not report.json()["discovery_checks_passed"]
    assert "IDP does not advertise PKCE S256" in report.json()["issues"]
    with pytest.raises(Exception):
        async with Client(
            f"{BASE}/{legacy}/mcp", auth=AutomaticConsent(f"{BASE}/{legacy}/mcp"), timeout=5
        ):
            pass


@pytest.mark.asyncio
async def test_introspection_resource_scope_and_inactive(api):
    gid = "opaque-" + uuid.uuid4().hex[:8]
    await create(
        api,
        "auth-profiles",
        gid,
        {
            "mode": "oauth",
            "issuer": IDP,
            "validation": "introspection",
            "introspection_url": IDP + "/introspect",
            "scopes": ["tools:call"],
        },
    )
    await create(api, "groups", gid, {"enabled": True, "auth_profile_id": gid})
    resource = f"{BASE}/{gid}/mcp"
    async with httpx.AsyncClient() as client:
        result = await client.post(IDP + "/test/token", json={"audience": resource, "opaque": True})
        from fastmcp.client.transports import StreamableHttpTransport

        async with Client(
            StreamableHttpTransport(
                resource, headers={"Authorization": "Bearer " + result.json()["token"]}
            )
        ) as mcp:
            assert await mcp.list_tools() == []
        for claims, status in [
            ({"active": False}, 401),
            ({"scope": ""}, 403),
            ({"aud": "wrong"}, 401),
            ({"exp": 1}, 401),
        ]:
            result = await client.post(
                IDP + "/test/token", json={"audience": resource, "opaque": True, "claims": claims}
            )
            response = await client.get(
                resource, headers={"Authorization": "Bearer " + result.json()["token"]}
            )
            assert response.status_code == status
