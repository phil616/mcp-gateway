# 网盘用户 APIKey MCP 工具

`plugins/storage/plugin.py` 将 `plugins/storage/docs/openapi.yaml` 中普通用户可通过 API Key 使用的 17 个操作注册为 `storage.*` 工具。调用方每次提供 `{api_key, request}`，插件只将该 Key 作为上游 `Authorization: Bearer ...` 发送，不保存、不使用共享凭据，也不透传网关入站 Bearer。

本文属于第三方插件接入文档。命令从仓库根目录执行；上游资料见 [资料边界](docs/README.md)，网关通用能力见 [主体文档](../../docs/README.md)。

## 接口范围

| 工具 ID（省略 `storage.`） | 功能 |
| --- | --- |
| `list_available_storage_backends` | 列出创建项目可用的存储后端 |
| `list_projects` / `create_project` / `get_project` | 列表、创建、查询项目 |
| `list_nodes` / `create_directory` | 列目录、创建目录 |
| `get_node` / `update_node` / `delete_node` | 查询、重命名/移动、删除节点 |
| `create_download` | 申请下载地址 |
| `download_local_content` / `head_local_content` | 本地文件正文、元数据 |
| `create_upload` / `upload_local_content` | 创建上传、发送本地文件正文 |
| `presign_upload_parts` / `complete_upload` / `abort_upload` | 分片签名、提交、取消上传 |

注册采用经人工审阅的操作白名单，并检查 APIKey 认证和用户 Scope。**项目修改、项目删除虽然支持 API Key，但只允许管理员，因此不注册。** 项目成员和 `/admin/*` 管理接口均不注册。账户、个人密钥管理、分享管理只支持 Session，不属于本次 APIKey 接入；公开分享、登录、OIDC、健康检查也不注册。

权限由上游实时校验：用户权限 ∩ Key Scope ∩ Key 项目范围。创建项目及列可用存储后端要求 `projects:create`、所有项目范围和用户全局写入权限。上传后续操作仍受上传会话所属用户约束。

## 配置和调用

配置只有必填 `base_url`：网盘 HTTPS 根地址，不含 `/api/v1`。文档未提供实际部署地址，因此不设置猜测的默认域名。本地测试允许回环 HTTP。配置不包含 API Key。

在管理端创建/选择组，绑定需要的 `storage.*` 工具并设置 `base_url`；可复用同一个配置集。绑定示例：

```json
{
  "id": "storage-projects",
  "data": {
    "group_id": "storage",
    "tool_id": "storage.list_projects",
    "exposed_name": "storage_list_projects",
    "overrides": {"base_url": "https://你的网盘API域名"},
    "enabled": false
  }
}
```

按[新增工具指南](../../docs/agent-tool-guide.md#6-将工具绑定到组)校验并启用绑定与组。组 MCP 端点是 `https://你的网关/storage/mcp`。网关组访问 Key 与网盘 API Key 相互独立。

调用 `storage_list_projects`：

```json
{"api_key":"调用方的网盘APIKey","request":{}}
```

`request.path` 保留文档原始参数名，如 `projectID`、`nodeID`、`uploadID`；`request.query` 为查询参数；`request.body` 为 JSON 请求体。未知参数、错误 UUID 和非法请求头在发请求前拒绝；不主动填充缺省字段。

列目录 request：

```json
{"path":{"projectID":"12345678-1234-4234-8234-123456789abc"},"query":{"parent_id":""}}
```

创建项目必须提供 `body.name` 和 `body.storage_backend_id`。创建上传时应明确提供真实 `body.size`，省略时上游按零处理。

本地上传顺序是 `create_upload` → `upload_local_content` → `complete_upload`。正文通过 `request.body_base64` 传入，空文件用空字符串，单次解码上限 10 MiB：

```json
{"path":{"uploadID":"12345678-1234-4234-8234-123456789abc"},"body_base64":"aGVsbG8="}
```

本地下载返回 `data.body_base64`、字节数 `data.size` 和内容元数据 `data.headers`。无论文件 MIME 类型如何都按原始字节处理。较大文件使用 `request.header.Range` 分段读取：

```json
{"path":{"nodeID":"12345678-1234-4234-8234-123456789abc"},"header":{"Range":"bytes=0-1048575"}}
```

只支持单 Range；HEAD 返回完整文件元数据，上游忽略 Range。JSON 响应及本地文件下载均限 10 MiB；JSON 请求限 1 MiB。本地超过 10 MiB 的上传需客户端直接调用 HTTP 内容接口。S3/OSS 单次或分片上传按上游返回的 URL、method、headers 由客户端直接完成，然后调用 `complete_upload`；插件不会访问外部预签名 URL，也不会将 API Key 发往对象存储。预签名地址按原样返回以供使用。

## 返回和错误

成功：`{"ok":true,"status":200,"data":...}`，保留 201、204、206 等真实状态；204 的 data 为 null。失败：`{"ok":false,"status":401,"error":"upstream_http_error"}`。无 HTTP 响应时 status 为 null。错误不包含上游正文或凭据。

超时、传输失败、非法参数、非法 Base64、请求/响应超限、无效 JSON 分别返回稳定错误码。调用方须检查 `ok`；业务失败不等于 MCP 框架 `isError`。无自动重试或重定向。提交上传不保证幂等，超时后应检查节点状态再处理。删除目录会删除子树，调用前确认目标。

## 维护与部署

```sh
uv sync --frozen
uv run python scripts/generate_storage.py --check
uv run gateway plugins check
uv run ruff check backend sdk plugins tests migrations scripts
uv run pytest -q tests/test_storage.py
uv run python tests/run.py tests/test_storage.py tests/test_storage_gateway.py
```

源文档更新后运行 `uv run python scripts/generate_storage.py`，审阅契约变化；新增接口需先核实普通用户权限，再更新生成器白名单。PyYAML 仅为开发依赖；运行时使用生成的 Python 契约，不读取 YAML 文档。

部署遵循网关现有整批更新流程：

```sh
docker compose --profile setup build backend migrate sync
docker compose run --rm --no-deps backend gateway plugins check
docker compose stop backend
docker compose run --rm migrate
docker compose run --rm sync
docker compose up -d --force-recreate backend
```

目录同步和全部 worker 更新后再配置组绑定；新增工具不会自动绑定到已有组。本次测试使用隔离环境与受控上游，不需要真实网盘 API Key。
