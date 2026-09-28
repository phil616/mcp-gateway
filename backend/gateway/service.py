"""Transactional management and immutable request snapshot construction."""

import hashlib
import re
import secrets
from datetime import datetime

from cryptography.fernet import Fernet
from fastapi import HTTPException
from pydantic import ValidationError
from sqlalchemy import select, text

from .contracts import CONTRACTS
from .models import (
    RESOURCES,
    AuditEvent,
    AuthProfile,
    ConfigProfile,
    Group,
    GroupAccessKey,
    Secret,
    ToolBinding,
    ToolDefinition,
)

RESERVED = {"api", "health", "docs", "redoc", "openapi", "static", "oauth", "mcp"}


def fail(message, status=422):
    raise HTTPException(status, message)


def refs(value):
    if isinstance(value, dict):
        if set(value) == {"$secret"}:
            if not isinstance(value["$secret"], str) or not value["$secret"]:
                fail("Secret reference must be a nonempty ID")
            return {value["$secret"]}
        return set().union(*(refs(v) for v in value.values()), set())
    if isinstance(value, list):
        return set().union(*(refs(v) for v in value), set())
    return set()


def public(row):
    data = dict(row.data)
    for key in ("ciphertext", "digest"):
        data.pop(key, None)
    if isinstance(row, Secret):
        data["value"] = "********"
    return {"id": row.id, "version": row.version, **data}


class Service:
    def __init__(self, settings, catalog):
        self.settings, self.catalog = settings, catalog
        self.cipher = Fernet(settings.master_key.encode())

    async def resolve(self, session, value):
        if isinstance(value, dict):
            if set(value) == {"$secret"}:
                refs(value)
                row = await session.get(Secret, value["$secret"])
                if not row:
                    fail("Secret reference does not exist")
                if row.data["key_version"] != self.settings.key_version:
                    fail("Secret master key version is not available")
                return self.cipher.decrypt(row.data["ciphertext"].encode()).decode()
            return {k: await self.resolve(session, v) for k, v in value.items()}
        if isinstance(value, list):
            return [await self.resolve(session, v) for v in value]
        return value

    async def config(self, session, binding):
        spec = self.catalog.tools.get(binding.tool_id)
        if not spec:
            fail("Tool code is unavailable")
        values = {}
        if binding.profile_id:
            profile = await session.get(ConfigProfile, binding.profile_id)
            if not profile:
                fail("Configuration profile does not exist")
            values.update(profile.data["values"])
        values.update(binding.data.get("overrides", {}))
        schema = spec.config_model.model_json_schema()

        def check_secrets(value, node):
            if "$ref" in node:
                node = schema.get("$defs", {}).get(node["$ref"].split("/")[-1], {})
            for branch in node.get("anyOf", []) + node.get("oneOf", []):
                if branch.get("type") != "null":
                    check_secrets(value, branch)
            if node.get("writeOnly") and not (
                isinstance(value, dict) and set(value) == {"$secret"}
            ):
                fail("Secret fields require explicit {$secret: id} references")
            if isinstance(value, dict):
                for k, v in value.items():
                    check_secrets(
                        v,
                        node.get("properties", {}).get(
                            k,
                            node.get("additionalProperties", {})
                            if isinstance(node.get("additionalProperties"), dict)
                            else {},
                        ),
                    )
            if isinstance(value, list):
                for v in value:
                    check_secrets(v, node.get("items", {}))

        check_secrets(values, schema)
        try:
            return spec.config_model.model_validate(await self.resolve(session, values))
        except ValidationError as exc:
            fail(
                {
                    "message": "Invalid tool configuration",
                    "fields": [list(e["loc"]) for e in exc.errors()],
                }
            )

    async def validate_all(self, session):
        await session.flush()
        for profile in (await session.scalars(select(ConfigProfile))).all():
            await self.resolve(session, profile.data["values"])
        for group in (await session.scalars(select(Group))).all():
            if group.auth_profile_id and not await session.get(AuthProfile, group.auth_profile_id):
                fail("Authentication profile does not exist")
        for binding in (await session.scalars(select(ToolBinding))).all():
            await self.resolve(session, binding.data.get("overrides", {}))
            definition = await session.get(ToolDefinition, binding.tool_id)
            if binding.data.get("enabled") and definition.data.get("available"):
                await self.config(session, binding)
        for profile in (await session.scalars(select(AuthProfile))).all():
            if profile.data.get("client_secret"):
                await self.resolve(session, profile.data["client_secret"])

    async def dependencies(self, session, resource, id):
        result = []
        for name, model in RESOURCES.items():
            for row in (await session.scalars(select(model))).all():
                used = (
                    (resource == "secrets" and id in refs(row.data))
                    or (
                        resource == "config-profiles"
                        and isinstance(row, ToolBinding)
                        and row.profile_id == id
                    )
                    or (
                        resource == "auth-profiles"
                        and isinstance(row, Group)
                        and row.auth_profile_id == id
                    )
                    or (
                        resource == "groups"
                        and isinstance(row, (ToolBinding, GroupAccessKey))
                        and row.group_id == id
                    )
                    or (resource == "tools" and isinstance(row, ToolBinding) and row.tool_id == id)
                )
                if used:
                    result.append({"resource": name, "id": row.id})
        return result

    async def mutate(self, session, actor, resource, id, body, version=None, delete=False):
        if resource not in RESOURCES:
            fail("Unknown resource", 404)
        await session.execute(text("SELECT pg_advisory_xact_lock(671923)"))
        model = RESOURCES[resource]
        row = await session.get(model, id)
        if version is None and row:
            fail("Already exists", 409)
        if version is not None and (not row or row.version != version):
            fail("Version conflict", 409)
        if delete:
            if resource == "tools":
                fail("Tool definitions are managed by deployment")
            dependencies = await self.dependencies(session, resource, id)
            if dependencies:
                fail({"dependencies": dependencies}, 409)
            await session.delete(row)
        else:
            if not re.fullmatch(r"[a-zA-Z0-9_.-]{1,128}", id):
                fail("Invalid ID")
            try:
                data = CONTRACTS[resource].model_validate(body).model_dump(exclude_unset=True)
            except ValidationError as exc:
                fail(
                    {
                        "message": "Invalid management data",
                        "fields": [list(e["loc"]) for e in exc.errors()],
                    }
                )
            allowed = {
                "groups": {"enabled", "auth_profile_id"},
                "bindings": {
                    "group_id",
                    "tool_id",
                    "profile_id",
                    "exposed_name",
                    "overrides",
                    "enabled",
                },
                "config-profiles": {"values"},
                "secrets": {"value", "description"},
                "auth-profiles": {
                    "mode",
                    "issuer",
                    "validation",
                    "jwks_url",
                    "introspection_url",
                    "client_id",
                    "client_secret",
                    "scopes",
                },
                "access-keys": {"group_id", "expires_at", "revoked"},
                "tools": {"enabled"},
            }[resource]
            if set(data) - allowed:
                fail("Unknown fields: " + ", ".join(sorted(set(data) - allowed)))
            for field in ("enabled", "revoked"):
                if field in data and not isinstance(data[field], bool):
                    fail(f"{field} must be a boolean")
            if row is None:
                if resource == "tools":
                    fail("Tool definitions are managed by deployment")
                row = model(id=id, data={}, version=1)
                session.add(row)
            else:
                row.version += 1
            merged = {**row.data, **data}
            if resource == "groups":
                if not re.fullmatch(r"[a-z][a-z0-9-]{0,62}", id) or id in RESERVED:
                    fail("Invalid or reserved group name")
                merged.setdefault("enabled", False)
                merged.setdefault("auth_profile_id", None)
                row.auth_profile_id = merged["auth_profile_id"]
            elif resource == "bindings":
                for field in ("group_id", "tool_id", "exposed_name"):
                    if not merged.get(field):
                        fail(f"Missing {field}")
                if not re.fullmatch(r"[a-zA-Z0-9_.-]{1,128}", merged["exposed_name"]):
                    fail("Invalid exposed name")
                merged.setdefault("enabled", False)
                merged.setdefault("overrides", {})
                merged.setdefault("profile_id", None)
                if not isinstance(merged["overrides"], dict):
                    fail("overrides must be an object")
                for field in ("group_id", "tool_id", "profile_id", "exposed_name"):
                    setattr(row, field, merged[field])
                definition = await session.get(ToolDefinition, row.tool_id)
                if not definition or (
                    not definition.data["available"] and (version is None or merged["enabled"])
                ):
                    fail("Tool code is unavailable")
                # Drafts can be incomplete; activation is always strict.
                if merged["enabled"]:
                    row.data = merged
                    await self.config(session, row)
            elif resource == "config-profiles":
                if not isinstance(merged.get("values"), dict):
                    fail("values must be an object")
            elif resource == "secrets":
                value = data.pop("value", None)
                if value is not None:
                    if not isinstance(value, str) or not value:
                        fail("Secret value must be a nonempty string")
                    merged["ciphertext"] = self.cipher.encrypt(value.encode()).decode()
                    merged["key_version"] = self.settings.key_version
                if not merged.get("ciphertext"):
                    fail("Secret value required")
                merged.pop("value", None)
            elif resource == "auth-profiles":
                if merged.get("mode") not in {"public", "static", "oauth"}:
                    fail("mode must be public, static or oauth")
                if merged["mode"] == "oauth":
                    if merged.get("validation") not in {"jwt", "introspection"}:
                        fail("OAuth validation must be jwt or introspection")
                    url_key = "jwks_url" if merged["validation"] == "jwt" else "introspection_url"
                    for field in ("issuer", url_key):
                        if not isinstance(merged.get(field), str) or not merged[field].startswith(
                            "https://"
                        ):
                            fail(f"{field} requires HTTPS")
                    if merged.get("client_secret") and not (
                        isinstance(merged["client_secret"], dict)
                        and set(merged["client_secret"]) == {"$secret"}
                    ):
                        fail("client_secret requires a secret reference")
                    scopes = merged.setdefault("scopes", [])
                    if not isinstance(scopes, list) or not all(
                        isinstance(s, str) and re.fullmatch(r"[\x21\x23-\x5B\x5D-\x7E]+", s)
                        for s in scopes
                    ):
                        fail("Invalid scopes")
            elif resource == "access-keys":
                if not merged.get("group_id"):
                    fail("group_id required")
                if version is not None and set(data) - {"revoked"}:
                    fail("Access key identity and expiry are immutable; create a replacement")
                if merged.get("expires_at"):
                    try:
                        expiry = datetime.fromisoformat(merged["expires_at"])
                        if expiry.tzinfo is None:
                            raise ValueError()
                    except (ValueError, TypeError):
                        fail("expires_at must be an ISO datetime with timezone")
                row.group_id = merged["group_id"]
                merged.setdefault("revoked", False)
                if version is None:
                    token = secrets.token_urlsafe(32)
                    merged["digest"] = hashlib.sha256(token.encode()).hexdigest()
            row.data = merged
            await self.validate_all(session)
        session.add(
            AuditEvent(
                actor=actor,
                action="delete" if delete else "update" if version else "create",
                resource=resource,
                object_id=id,
            )
        )
        await session.flush()
        result = None if delete else public(row)
        if not delete and resource == "access-keys" and version is None:
            result["token"] = token
        return result
