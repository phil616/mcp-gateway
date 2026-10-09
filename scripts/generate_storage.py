"""Compile reviewed user API operations into an offline, fingerprinted contract."""

import argparse
import hashlib
import re
from pathlib import Path
from pprint import pformat

import yaml

ROOT = Path(__file__).resolve().parents[1]
# Reviewed against api.md and api-keys.md. Scope support alone does not imply user access:
# updateProject/deleteProject and all membership operations require administrators.
USER_OPERATIONS = {
    "listAvailableStorageBackends",
    "listProjects",
    "createProject",
    "getProject",
    "listNodes",
    "createDirectory",
    "createUpload",
    "getNode",
    "updateNode",
    "deleteNode",
    "createDownload",
    "downloadLocalContent",
    "headLocalContent",
    "presignUploadParts",
    "uploadLocalContent",
    "completeUpload",
    "abortUpload",
}
USER_SCOPES = {"projects:read", "projects:create", "files:read", "files:write", "files:delete"}


def compile_contract(source):
    document = yaml.safe_load(source)

    def expand(value):
        if isinstance(value, list):
            return [expand(item) for item in value]
        if not isinstance(value, dict):
            return value
        if "$ref" in value:
            ref = value["$ref"]
            assert ref.startswith("#/components/")
            target = document
            for part in ref[2:].split("/"):
                target = target[part]
            return expand({**target, **{k: v for k, v in value.items() if k != "$ref"}})
        return {key: expand(item) for key, item in value.items()}

    operations = {}
    for path, methods in document["paths"].items():
        for method, op in methods.items():
            if method not in {"get", "head", "post", "put", "patch", "delete"}:
                continue
            if op["operationId"] not in USER_OPERATIONS:
                continue
            assert {"apiKeyBearer": []} in op.get("security", [])
            assert op["x-api-scope"] in USER_SCOPES
            assert not path.startswith("/api/v1/admin/")
            name = re.sub(r"(?<!^)(?=[A-Z])", "_", op["operationId"]).lower()
            assert name not in operations
            schema = {"type": "object", "properties": {}, "additionalProperties": False}
            required = []
            params = {}
            for p in expand(methods.get("parameters", []) + op.get("parameters", [])):
                params[p["in"], p["name"]] = p
            for location in ("path", "query", "header"):
                group_params = [p for p in params.values() if p["in"] == location]
                if not group_params:
                    continue
                props = {p["name"]: p["schema"] for p in group_params}
                if location == "header":
                    assert set(props) == {"Range"}
                    props["Range"]["pattern"] = r"^bytes=(?:[0-9]+-[0-9]*|-[0-9]+)$"
                if location == "query" and "parent_id" in props:
                    props["parent_id"] = {"anyOf": [props["parent_id"], {"const": ""}]}
                group = {"type": "object", "properties": props, "additionalProperties": False}
                needed = [p["name"] for p in group_params if p.get("required")]
                if needed:
                    group["required"] = needed
                    required.append(location)
                schema["properties"][location] = group
            body = expand(op.get("requestBody", {}))
            content = body.get("content", {})
            binary = "application/octet-stream" in content
            if binary:
                schema["properties"]["body_base64"] = {
                    "type": "string",
                    "contentEncoding": "base64",
                    "maxLength": 4 * ((10 * 1024 * 1024 + 2) // 3),
                    "description": "原始文件的标准 Base64；最多 10 MiB，空文件传空字符串。",
                }
                required.append("body_base64")
            elif content:
                assert set(content) == {"application/json"}
                schema["properties"]["body"] = content["application/json"]["schema"]
                if body.get("required"):
                    required.append("body")
            if required:
                schema["required"] = required
            description = (
                f"网盘：{op['summary']}。{method.upper()} {path}。"
                f"每次传入用户 API Key；所需 Scope：{op['x-api-scope']}，"
                "用户当前权限与密钥项目范围仍由上游校验。"
                + (
                    "只读查询。"
                    if method in {"get", "head"}
                    else "会执行写入、删除或签名操作；不自动重试。"
                )
                + op.get("description", "")
            )
            if "Upload" in op["operationId"] or "Content" in op["operationId"]:
                description += (
                    "本地文件正文使用 Base64，单次最多 10 MiB；大文件下载使用 Range。"
                    "外部预签名 URL 由客户端直接访问，不携带 API Key。"
                    "创建上传时明确提供真实 size；完成上传不保证幂等。"
                )
            if op["x-api-scope"] == "projects:create":
                description += "密钥须为 all_projects，用户须具备全局写入权限。"
            operations[name] = {
                "method": method.upper(),
                "path": path,
                "scope": op["x-api-scope"],
                "schema": schema,
                "description": description,
                "binary_request": binary,
                "binary_response": op["operationId"] == "downloadLocalContent",
                "success": [
                    int(c) for c in op["responses"] if str(c).isdigit() and 200 <= int(c) < 300
                ],
            }
    assert len(operations) == len(USER_OPERATIONS), "Reviewed operations missing from source"
    return operations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = (ROOT / "plugins/storage/docs/openapi.yaml").read_bytes()
    operations = compile_contract(source)
    output = (
        "# Generated by scripts/generate_storage.py; do not edit.\n"
        f'SOURCE_SHA256 = "{hashlib.sha256(source).hexdigest()}"\n'
        + "OPERATIONS = "
        + pformat(operations, width=100, sort_dicts=True)
        + "\n"
    )
    target = ROOT / "plugins/storage/contract.py"
    if args.check:
        if not target.exists() or target.read_text() != output:
            raise SystemExit(
                "Storage contract is stale; run uv run python scripts/generate_storage.py"
            )
    else:
        target.write_text(output)
    print(f"Storage contract: {len(operations)} user tools")


if __name__ == "__main__":
    main()
