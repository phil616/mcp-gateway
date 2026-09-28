"""Partial-update data contracts, also exported in the management OpenAPI schema."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, StrictBool


class Patch(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class GroupData(Patch):
    enabled: StrictBool = False
    auth_profile_id: str | None = None


class BindingData(Patch):
    group_id: str = ""
    tool_id: str = ""
    profile_id: str | None = None
    exposed_name: str = ""
    enabled: StrictBool = False
    overrides: dict = Field(default_factory=dict)


class ConfigData(Patch):
    values: dict = Field(default_factory=dict)


class SecretData(Patch):
    value: str = Field(default="", min_length=1)
    description: str = ""


class AuthData(Patch):
    mode: Literal["public", "static", "oauth"] = "public"
    issuer: str = ""
    validation: Literal["jwt", "introspection"] = "jwt"
    jwks_url: str = ""
    introspection_url: str = ""
    client_id: str = ""
    client_secret: dict | None = None
    scopes: list[str] = Field(default_factory=list)


class AccessKeyData(Patch):
    group_id: str = ""
    expires_at: str | None = None
    revoked: StrictBool = False


class ToolData(Patch):
    enabled: StrictBool = True


CONTRACTS = {
    "groups": GroupData,
    "bindings": BindingData,
    "config-profiles": ConfigData,
    "secrets": SecretData,
    "auth-profiles": AuthData,
    "access-keys": AccessKeyData,
    "tools": ToolData,
}
