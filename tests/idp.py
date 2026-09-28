"""TEST ONLY: automatic consent IDP with PKCE, DCR and resource-bound tokens."""

import base64
import hashlib
import json
import os
import secrets
import time
from pathlib import Path

import jwt
from cryptography.hazmat.primitives import serialization
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()
issuer = os.environ.get("TEST_IDP_URL", "https://localhost:9443")
key = serialization.load_pem_private_key(
    Path(os.environ["TEST_TLS_KEY"]).read_bytes(), password=None
)
public = json.loads(jwt.algorithms.RSAAlgorithm.to_jwk(key.public_key()))
public.update(kid="test", use="sig", alg="RS256")
codes = {}
clients = {}
opaque = {}


@app.get("/.well-known/oauth-authorization-server")
@app.get("/.well-known/openid-configuration")
async def discovery():
    return {
        "issuer": issuer,
        "authorization_endpoint": issuer + "/authorize",
        "token_endpoint": issuer + "/token",
        "registration_endpoint": issuer + "/register",
        "jwks_uri": issuer + "/jwks",
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code"],
        "code_challenge_methods_supported": ["S256"],
        "token_endpoint_auth_methods_supported": ["none"],
        "scopes_supported": ["tools:call"],
    }


@app.get("/jwks")
async def jwks():
    return {"keys": [public]}


@app.post("/register")
async def register(request: Request):
    data = await request.json()
    id = secrets.token_urlsafe(16)
    clients[id] = data
    return {**data, "client_id": id, "token_endpoint_auth_method": "none"}


@app.get("/authorize")
async def authorize(request: Request):
    p = dict(request.query_params)
    if (
        p.get("client_id") not in clients
        or p.get("redirect_uri") not in clients[p["client_id"]]["redirect_uris"]
    ):
        raise HTTPException(400, "invalid_client")
    if p.get("code_challenge_method") != "S256" or not p.get("resource"):
        raise HTTPException(400, "PKCE S256 and resource required")
    code = secrets.token_urlsafe(24)
    codes[code] = p
    from urllib.parse import urlencode

    return RedirectResponse(
        p["redirect_uri"] + "?" + urlencode({"code": code, "state": p["state"], "iss": issuer}),
        status_code=302,
    )


def mint(audience, scope="tools:call", **overrides):
    claims = {
        "iss": issuer,
        "sub": "test-user",
        "aud": audience,
        "iat": int(time.time()),
        "exp": int(time.time()) + 300,
        "scope": scope,
        **overrides,
    }
    return jwt.encode(claims, key, algorithm="RS256", headers={"kid": "test"}), claims


@app.post("/token")
async def token(request: Request):
    data = dict(await request.form())
    stored = codes.pop(data.get("code"), None)
    challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(data.get("code_verifier", "").encode()).digest())
        .rstrip(b"=")
        .decode()
    )
    if (
        not stored
        or stored["code_challenge"] != challenge
        or data.get("client_id") != stored["client_id"]
        or data.get("redirect_uri") != stored["redirect_uri"]
        or data.get("resource") != stored["resource"]
    ):
        raise HTTPException(400, "invalid_grant")
    token, _ = mint(stored["resource"], stored.get("scope", ""))
    return {
        "access_token": token,
        "token_type": "Bearer",
        "expires_in": 300,
        "scope": stored.get("scope", ""),
    }


@app.post("/introspect")
async def introspect(request: Request):
    if request.cookies:
        raise HTTPException(400, "An introspection request reused credentialed cookie state")
    response = JSONResponse(opaque.get((await request.form()).get("token"), {"active": False}))
    response.set_cookie("idp-session", "must-not-be-reused")
    return response


@app.post("/test/token")
async def test_token(request: Request):
    data = await request.json()
    token, claims = mint(data.pop("audience"), **data.pop("claims", {}))
    if data.get("opaque"):
        token = secrets.token_urlsafe(32)
        opaque[token] = {"active": True, **claims}
    return {"token": token}


@app.get("/legacy/.well-known/openid-configuration")
async def legacy():
    return {
        "issuer": issuer + "/legacy",
        "authorization_endpoint": issuer + "/authorize",
        "token_endpoint": issuer + "/token",
        "response_types_supported": ["token"],
    }
