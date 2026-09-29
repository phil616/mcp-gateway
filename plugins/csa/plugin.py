"""CSA APIKey tools, registered through the gateway's public plugin SDK."""

import asyncio
import json
import re
from typing import Annotated
from urllib.parse import quote, urlsplit

import httpx
from gateway_sdk import Depends, ToolPackage, ToolRuntime, current_runtime
from jsonschema import Draft202012Validator, FormatChecker
from pydantic import BaseModel, Field, WithJsonSchema, field_validator

from .contract import OPERATIONS

package = ToolPackage(id="csa", version="1.1.0")
MAX_RESPONSE_BYTES = 10 * 1024 * 1024
# Never expose authentication material returned by account/key administration APIs.
SECRET_FIELDS = {
    "key",
    "api_key",
    "access_token",
    "refresh_token",
    "id_token",
    "app_token",
    "client_secret",
    "client_secret_plain",
    "secret",
    "setup_token",
    "challenge_token",
    "otpauth_uri",
    "recovery_codes",
    "private_key_pem",
    "password",
    "password_hash",
}


class CSAConfig(BaseModel):
    model_config = {"extra": "forbid"}
    base_url: str = Field(
        default="https://api.altasci.com",
        description="CSA 服务根地址，不含 /api；HTTPS 或本地 HTTP",
    )

    @field_validator("base_url")
    @classmethod
    def validate_url(cls, value: str) -> str:
        url = urlsplit(value)
        if (
            not url.hostname
            or url.username
            or url.password
            or url.query
            or url.fragment
            or url.path not in ("", "/")
            or url.scheme not in ("https", "http")
        ):
            raise ValueError("Expected a service origin without credentials, query or path")
        if url.scheme == "http" and url.hostname not in ("localhost", "127.0.0.1", "::1"):
            raise ValueError("HTTPS is required except for local development")
        return value.rstrip("/")


def sanitize(value: object, api_key: str) -> object:
    if isinstance(value, dict):
        return {
            key: "[REDACTED]" if key.lower() in SECRET_FIELDS else sanitize(item, api_key)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [sanitize(item, api_key) for item in value]
    if isinstance(value, str):
        return value.replace(api_key, "[REDACTED]")
    return value


def failure(code: str, status: int | None = None) -> dict:
    # Raw upstream error bodies/headers may contain credentials or sensitive inputs.
    return {"ok": False, "status": status, "error": code}


async def execute(operation: dict, request: dict, config: CSAConfig, api_key: str) -> dict:
    if not api_key or not api_key.isascii() or any(ord(c) <= 32 or ord(c) == 127 for c in api_key):
        return failure("invalid_api_key")
    validator = Draft202012Validator(operation["schema"], format_checker=FormatChecker())
    if not validator.is_valid(request):
        return failure("invalid_arguments")
    path = operation["path"]
    for key, value in request.get("path", {}).items():
        # Disallow path traversal even through intermediaries that decode escaped slashes.
        if (
            not isinstance(value, str)
            or not value
            or value in (".", "..")
            or re.search(r"[/\\%?#\x00-\x20\x7f]", value)
        ):
            return failure("invalid_path_parameter")
        path = path.replace("{" + key + "}", quote(value, safe=""))
    body = request.get("body")
    project_id = request.get("path", {}).get("project_id")
    if isinstance(body, dict) and "project_id" in body and project_id is not None:
        if body["project_id"] != project_id:
            return failure("project_id_mismatch")
    kwargs = {}
    if "body" in request:
        # Preserve omitted fields and explicit null, including scalar legacy bodies.
        kwargs["content"] = json.dumps(body, ensure_ascii=False, allow_nan=False).encode()
        kwargs["headers"] = {"Content-Type": "application/json"}
    params = {
        key: str(value).lower() if isinstance(value, bool) else value
        for key, value in request.get("query", {}).items()
        if value is not None
    }
    key = api_key
    try:
        # No shared credentials, redirects, environment proxies, automatic retries or cookies.
        async with asyncio.timeout(45):
            async with httpx.AsyncClient(
                timeout=httpx.Timeout(30, connect=5),
                follow_redirects=False,
                trust_env=False,
                headers={"X-API-Key": key},
            ) as client:
                async with client.stream(
                    operation["method"], config.base_url + path, params=params, **kwargs
                ) as response:
                    if response.status_code not in operation["success"]:
                        return failure("upstream_http_error", response.status_code)
                    data = bytearray()
                    async for chunk in response.aiter_bytes():
                        data.extend(chunk)
                        if len(data) > MAX_RESPONSE_BYTES:
                            return failure("response_too_large", response.status_code)
                    if response.status_code == 204:
                        result = None
                    elif "application/json" in response.headers.get("content-type", ""):
                        try:
                            result = json.loads(data)
                        except (ValueError, UnicodeError):
                            return failure("invalid_upstream_json", response.status_code)
                    elif "text/" in response.headers.get("content-type", ""):
                        result = data.decode("utf-8", errors="replace")
                    else:
                        return failure("unsupported_response_type", response.status_code)
                    return {
                        "ok": True,
                        "status": response.status_code,
                        "data": sanitize(result, key),
                    }
    except (TimeoutError, httpx.TimeoutException):
        return failure("upstream_timeout")
    except httpx.HTTPError:
        return failure("upstream_transport_error")


def register(name: str, operation: dict) -> None:
    request_type = Annotated[dict, WithJsonSchema(operation["schema"])]

    async def call(
        api_key: Annotated[str, Field(description="本次调用的 CSA APIKey，不存储")],
        request: request_type,
        runtime: ToolRuntime = Depends(current_runtime),
    ) -> dict:
        return await execute(operation, request, runtime.config(CSAConfig), api_key)

    call.__name__ = name
    package.tool(id=name, config_model=CSAConfig, timeout=50, description=operation["description"])(
        call
    )


for _name, _operation in OPERATIONS.items():
    register(_name, _operation)
