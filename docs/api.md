# 管理 API

运行时 `/docs` 和 `/openapi.json` 是完整接口定义；`docs/openapi.json` 是提交版本的导出。所有管理数据接口要求管理员 Cookie；写入同时要求 `Origin: CONSOLE_ORIGIN` 和 `X-CSRF-Token`。`POST /api/v1/login` 接受 username/password，返回 username/csrf 并设置 HttpOnly Cookie。`GET /api/v1/me` 恢复页面会话；`POST /api/v1/logout` 删除 Redis 会话。

## 通用资源

路径资源包括 `tools`、`groups`、`bindings`、`config-profiles`、`secrets`、`auth-profiles`、`access-keys`。

| 请求 | 行为 |
|---|---|
| `GET /api/v1/{resource}?offset=0&limit=50&q=...` | 分页和 ID 子串筛选，返回 items/total；bindings、access-keys 支持 group_id |
| `GET /api/v1/{resource}/{id}` | 单个对象，包含 id/version；组额外包含 endpoint/client_example |
| `POST /api/v1/{resource}` | `{ "id": "stable-id", "data": {...} }`，返回 201 |
| `PUT /api/v1/{resource}/{id}` | `{ "version": 1, "data": {...} }`，按字段更新，成功 version 加一 |
| `DELETE /api/v1/{resource}/{id}?version=1` | 版本校验及引用检查；被引用时 409 和 dependencies |
| `GET /api/v1/{resource}/{id}/dependencies` | 删除影响对象列表 |
| `POST /api/v1/bindings/{id}/validate` | 验证有效配置，不返回解析后的配置 |
| `GET /api/v1/auth-profiles/{id}/compatibility` | 检查发现、PKCE、客户端注册能力，明确列出不足 |
| `POST /api/v1/access-keys/{id}/rotate` | `{ "version": 1, "data": {"expires_at": "..."} }`；原子撤销旧 Key、创建新 Key |
| `GET /api/v1/audit` | 分页、按 object_id 子串筛选，不提供审计编辑接口 |

创建工具和删除工具不允许；工具通过代码部署管理，只能在 Web/API 修改全局 enabled。`Group.id` 就是不可修改的路由名称，仅接受小写字母开头、小写字母/数字/连字符，最长 63 位。`api`、`health`、`docs` 等保留名称不可创建。

## Data 字段

- groups：`enabled`（默认 false）、`auth_profile_id`（默认 null，公开）。
- bindings：`group_id`、`tool_id`、`exposed_name`、`profile_id`、`overrides`（对象）、`enabled`（默认 false）。同组 tool_id 和 exposed_name 分别唯一。
- config-profiles：`values` 对象。密钥格式 `{"$secret":"id"}`。
- secrets：创建必填 `value`，可选 description。读取 value 固定为掩码；更新省略 value 即保留。数据库保存 Fernet 密文和 key_version。
- auth-profiles：`mode` 为 public/static/oauth。OAuth 使用 issuer、validation（jwt/introspection）、jwks_url 或 introspection_url、scopes 列表；introspection 可配置 client_id/client_secret，client_secret 必须是密钥引用。
- access-keys：创建必须 group_id，可选带时区 ISO expires_at。返回 token 仅一次；读取不返回 token 或摘要。只允许修改 revoked；轮换使用专门接口。
- tools：只允许更新 enabled。读取包含参数 schema、配置 schema、版本、指纹和 available。

未知字段和错误类型返回 422；版本冲突、重复唯一字段和外键冲突返回 409。全体管理员具有相同权限。变更与审计在同一事务提交；跨资源校验期间使用 PostgreSQL 事务 advisory lock，以防配置更新与新建绑定之间的写偏差。管理写吞吐以正确性优先，MCP 只读请求不获取该锁。

配置 schema 简单字段在 UI 中显示继承与覆盖状态；复杂嵌套对象使用 JSON 编辑并由服务端完整验证。共享配置集使用 JSON 编辑，以适配不同工具的配置集合。

## 批量工具绑定

`POST /api/v1/bindings/batch` 接受 `{"items":[{"id":"support-echo","data":{"group_id":"support","tool_id":"demo.echo","exposed_name":"echo","enabled":false}}]}`。

一次 1–200 项，必须属于同一组；每项配置字段与单条创建一致。整批与每项审计在同一个事务中提交，任何一项配置错误、重名或引用失效都会全部回滚。成功返回 201 和 `items`；失败返回 422/409，包含失败项的序号 `item`（从 1 开始）、`id` 和原因。不会覆盖或自动跳过已有绑定。网络中断而无法确认提交结果时，应先查询绑定列表再重试；再次提交已存在的 ID 会返回冲突。

组详情的 `client_example` 按 `auth_mode` 生成：静态认证包含 `headers.Authorization: "Bearer <YOUR_GROUP_ACCESS_KEY>"`，使用前必须替换占位符；公开及 OAuth 模式不附带静态密钥。该接口不会返回真实访问密钥原文。

## 批量删除

`POST /api/v1/{resource}/batch-delete`，请求为 `{"items":[{"id":"example","version":1}]}`，一次 1–200 项，不允许重复 ID 或删除工具目录。成功返回 `{"deleted":1}`。整批使用同一事务，任何一项版本冲突或仍有引用时全部回滚（包含审计记录）。不级联删除引用对象，需先删除绑定、访问密钥或修改相关配置。
