import hashlib
import json
import logging
import secrets
import time
from datetime import UTC, datetime

import httpx
import jwt
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError
from fastapi import HTTPException, Request
from sqlalchemy import select

from .http_errors import console_origins
from .models import AdminUser, GroupAccessKey

passwords = PasswordHasher()
DUMMY_HASH = passwords.hash("unused-random-login-timing-value")


def session_key(sid):
    return "session:" + hashlib.sha256(sid.encode()).hexdigest()


def credential_version(password_hash):
    return hashlib.sha256(password_hash.encode()).hexdigest()


async def admin(request: Request):
    state = request.app.state
    sid = request.cookies.get("gateway_session", "")
    value = await state.redis.get(session_key(sid)) if sid else None
    if not value:
        raise HTTPException(401, "Login required")
    try:
        session = json.loads(value)
        if not isinstance(session, dict) or not all(
            isinstance(session.get(key), str) and session[key]
            for key in ("username", "csrf", "credential_version")
        ):
            raise ValueError()
    except (ValueError, TypeError):
        await state.redis.delete(session_key(sid))
        raise HTTPException(401, "Session expired; please sign in again") from None
    async with state.sessions() as db:
        user = await db.get(AdminUser, session["username"])
    if not user or not secrets.compare_digest(
        session["credential_version"].encode(), credential_version(user.password_hash).encode()
    ):
        await state.redis.delete(session_key(sid))
        raise HTTPException(401, "Session expired; please sign in again")
    if request.method not in {"GET", "HEAD", "OPTIONS"}:
        if request.headers.get("origin") not in console_origins(
            state.settings
        ) or not secrets.compare_digest(
            request.headers.get("x-csrf-token", "").encode(), session["csrf"].encode()
        ):
            raise HTTPException(403, "CSRF validation failed")
    return {"username": session["username"], "csrf": session["csrf"]}


async def login(request, username, password):
    state = request.app.state
    if request.headers.get("origin") not in console_origins(state.settings):
        raise HTTPException(403, "Origin rejected")
    peer = request.client.host if request.client else "unknown"
    key = "login:" + hashlib.sha256(peer.encode()).hexdigest()
    count = await state.redis.eval(
        "local n=redis.call('INCR',KEYS[1]); if n==1 then redis.call('EXPIRE',KEYS[1],300) end; return n",
        1,
        key,
    )
    if count > 10:
        raise HTTPException(429, "Too many login attempts", headers={"Retry-After": "300"})
    async with state.sessions() as db:
        user = await db.get(AdminUser, username)
    import anyio

    try:
        await anyio.to_thread.run_sync(
            passwords.verify,
            user.password_hash if user else DUMMY_HASH,
            password,
            limiter=state.auth_limiter,
        )
        if not user:
            raise HTTPException(401, "Invalid credentials")
    except (VerificationError, InvalidHashError):
        raise HTTPException(401, "Invalid credentials") from None

    sid, csrf = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
    # Reauthentication invalidates the previous session.
    old = request.cookies.get("gateway_session")
    if old:
        await state.redis.delete(session_key(old))
    await state.redis.set(
        session_key(sid),
        json.dumps(
            {
                "username": username,
                "csrf": csrf,
                "credential_version": credential_version(user.password_hash),
            }
        ),
        ex=state.settings.session_seconds,
    )
    return sid, csrf


def auth_response(response):
    response.raise_for_status()
    try:
        data = response.json()
        if not isinstance(data, dict):
            raise ValueError()
        return data
    except ValueError:
        raise HTTPException(503, "Invalid authentication service response") from None


async def authorize(state, db, group, profile, authorization, *, client_secret=None):
    mode = profile.get("mode", "public")
    if mode == "public":
        return "anonymous"
    resource = state.settings.public_url.rstrip("/") + f"/{group.id}/mcp"
    metadata = (
        state.settings.public_url.rstrip("/")
        + f"/.well-known/oauth-protected-resource/{group.id}/mcp"
    )
    scopes = profile.get("scopes", [])
    challenge = (
        f'Bearer resource_metadata="{metadata}", scope="{" ".join(scopes)}"'
        if mode == "oauth"
        else 'Bearer realm="gateway"'
    )

    def reject(status=401):
        error = "insufficient_scope" if status == 403 else "invalid_token"
        raise HTTPException(
            status,
            "Insufficient scope" if status == 403 else "Invalid access token",
            headers={"WWW-Authenticate": challenge + f', error="{error}"'},
        )

    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        reject()
    token = parts[1]
    if mode == "static":
        digest = hashlib.sha256(token.encode()).hexdigest()
        keys = (
            await db.scalars(select(GroupAccessKey).where(GroupAccessKey.group_id == group.id))
        ).all()
        for key in keys:
            data = key.data
            if data.get("revoked"):
                continue
            if data.get("expires_at") and datetime.fromisoformat(
                data["expires_at"]
            ) <= datetime.now(UTC):
                continue
            if secrets.compare_digest(data["digest"], digest):
                return key.id
        reject()
    try:
        if profile["validation"] == "jwt":
            response = await state.http.get(profile["jwks_url"])
            data = auth_response(response)
            try:
                jwks = jwt.PyJWKSet.from_dict(data)
            except (ValueError, jwt.PyJWTError):
                raise HTTPException(503, "Invalid authentication service response") from None
            header = jwt.get_unverified_header(token)
            if header.get("alg") not in {"RS256", "ES256", "EdDSA"}:
                reject()
            matches = [
                k
                for k in jwks.keys
                if k.key_id == header.get("kid") and k.public_key_use in {None, "sig"}
            ]
            if len(matches) != 1:
                reject()
            claims = jwt.decode(
                token,
                matches[0].key,
                algorithms=[header["alg"]],
                audience=resource,
                issuer=profile["issuer"],
                options={"require": ["exp", "iss", "aud", "sub"]},
            )
        else:
            secret = client_secret
            auth = (profile["client_id"], secret) if profile.get("client_id") and secret else None
            # Credentialed validation must not reuse cookies across groups.
            async with httpx.AsyncClient(timeout=10, follow_redirects=False) as client:
                response = await client.post(
                    profile["introspection_url"], data={"token": token}, auth=auth
                )
            claims = auth_response(response)
            if not isinstance(claims.get("active"), bool) or any(
                key in claims
                and (isinstance(claims[key], bool) or not isinstance(claims[key], (int, float)))
                for key in ("exp", "nbf")
            ):
                raise HTTPException(503, "Invalid authentication service response")
            audience = claims.get("aud", [])
            if isinstance(audience, str):
                audience = [audience]
            if (
                claims.get("active") is not True
                or resource not in audience
                or ("exp" in claims and claims["exp"] <= time.time())
            ):
                reject()
            if (
                claims.get("iss", profile["issuer"]) != profile["issuer"]
                or claims.get("nbf", 0) > time.time()
            ):
                reject()
        granted = claims.get("scope", "").split()
        if not set(scopes).issubset(granted):
            reject(403)
        return str(claims.get("sub", "external"))
    except HTTPException:
        raise
    except httpx.HTTPError as exc:
        logging.getLogger("uvicorn.error").warning(
            "oauth_unavailable group=%s error_type=%s", group.id, type(exc).__name__
        )
        raise HTTPException(
            503, "Authentication service unavailable", headers={"Retry-After": "5"}
        ) from None
    except Exception:
        reject()
