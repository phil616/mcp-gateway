# 认证与兼容性

管理员登录、Agent 入站认证、工具出站凭据相互独立。管理员密码使用 Argon2id；随机会话存入 Redis，Cookie 仅发送到后端 `/api/v1`。会话有固定到期时间，退出立即删除。登录按直接连接的 IP 限制为每 5 分钟 10 次；反向代理须正确设置可信代理地址，不能无条件信任互联网传来的 forwarded headers。

## 管理员创建、登录与恢复

管理员仅通过部署环境的 CLI 创建，没有公开注册接口，也没有独立邮箱字段或邮箱验证码。

```bash
uv run gateway admin-create admin
uv run gateway admin-reset-password admin
```

命令会交互式读取并确认密码。Docker 部署使用 `docker compose run --rm backend gateway admin-create admin`（重置时替换子命令）。创建、重置和服务必须连接同一个 `DATABASE_URL`，否则创建的账号不会出现在当前服务中。

- 新用户名长度 1–128，不允许空白和不可打印字符；支持中文和邮箱形式，区分大小写。例如 `Admin@example.com` 与 `admin@example.com` 是不同账号。不会按邮箱格式验证、自动去空格或转小写。
- 新建/重置密码长度 12–1024；密码中的空格保留。登录兼容已有短密码和旧用户名，最长密码同为 1024。
- 重复创建返回明确错误，修改密码使用 `admin-reset-password`。旧版本创建的超长密码可通过此命令恢复。
- 每次管理请求检查账号是否仍存在、密码版本是否一致；重置密码使该账号所有旧会话失效。重新登录使当前浏览器旧会话失效，退出立即删除会话。
- 本次会话格式升级后，升级前已登录的用户需重新登录；无需数据库迁移。

网页登录成功后会再调用 `/api/v1/me`，确认浏览器实际发送了 Cookie 才进入控制台。会话过期返回登录页并清除前端缓存；登录、会话和管理 API 响应禁止缓存。

本地 HTTP 开发使用 `COOKIE_SECURE=false`；HTTPS 部署使用 `COOKIE_SECURE=true`。`CONSOLE_ORIGIN` 必须与浏览器来源匹配，`VITE_API_URL` 指向后端。如果 `/login` 返回成功而 `/me` 返回 401，检查 Cookie 是否被 Secure 属性、域名或浏览器跨站 Cookie 策略阻止。生产环境建议前后端同站部署。403 表示 Origin/CSRF 校验失败；429 表示同一来源 IP 在 5 分钟内超过 10 次登录请求（包括成功登录），应等待后重试。

## 组模式

- public：不要求 Bearer；新组仍默认禁用，需要显式启用。
- static：高熵 Key 仅保存 SHA-256 摘要，绑定到单个组，检查 expires_at/revoked。轮换在同一事务中撤销旧 Key 并生成新 Key。
- oauth：只作为资源服务器接受外部 IDP 签发的访问令牌；不实现授权页面、IDP、令牌签发、OAuth 代理。

每组 audience/resource 固定为 `PUBLIC_URL/{group}/mcp`，必须与客户端使用的端点完全一致。JWT 接受 RS256、ES256、EdDSA，通过管理员提供的 HTTPS JWKS 校验签名、issuer、audience、exp、sub 和必要 scopes；验证 nbf（若存在）。为保持简单，每个请求获取 JWKS，不跨请求缓存。

Introspection 向配置的 HTTPS 地址发送 token，可使用 client_secret_basic；要求 active=true、aud 包含组端点、若返回 exp 则必须未过期、scope 包含必要权限。iss 若返回必须匹配；未返回时由指定 introspection 端点提供信任来源。不将入站 token 注入工具配置。

错误返回 Bearer challenge。OAuth metadata 位于 `/.well-known/oauth-protected-resource/{group}/mcp`，包含 resource、authorization_servers、scopes_supported、bearer_methods_supported。scope 不足返回 403 / insufficient_scope；其他令牌错误返回 401 / invalid_token。禁用/不存在的组返回 404。IDP 网络故障、非成功 HTTP 响应或无法解析的响应返回 503，不再伪装为客户端令牌错误。远程验证在数据库快照事务释放后执行，调用继续使用该请求已经读取的认证与工具配置。

## 接受令牌与完整登录流程的区别

能接受 JWT 或 introspection token，并不等于任意 MCP 客户端都能完成登录。完整流程还需要 IDP 提供：

1. 匹配 issuer 的 OAuth/OIDC 发现元数据和 authorization/token endpoints。
2. Authorization Code + PKCE S256。
3. `resource` 参数及资源受限 audience，不能只验证 client_id audience。
4. 至少一种客户端接入方式：预注册 client_id、动态注册或客户端元数据文档。

兼容性 API 检查公开元数据并列出缺失能力；资源 audience 仍需实际令牌集成测试。旧 OAuth 2.0 IDP 缺少上述能力时，管理员可能仍可提供预先获取的合适 Bearer token，但不能声称支持标准 MCP 完整授权。规范依据：[MCP 2025-11-25 Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)。

验收环境的 `tests/idp.py` 支持临时 HTTPS 证书、JWKS、动态注册、PKCE S256、资源绑定 JWT 和 introspection。真实 FastMCP OAuth 客户端执行发现、注册、挑战码交换；自动同意 fixture 仅替代浏览器用户确认。测试同时验证不具备 PKCE 的 legacy IDP 的明确兼容性失败。测试 IDP 不得暴露到生产网络。

## 静态访问密钥的客户端配置

组详情的连接示例会根据认证模式生成。静态模式的示例包含 HTTP 请求头：

```json
{
  "mcpServers": {
    "support": {
      "type": "http",
      "url": "https://mcp.example.com/support/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_GROUP_ACCESS_KEY>"
      }
    }
  }
}
```

将 `<YOUR_GROUP_ACCESS_KEY>` 整体替换为属于该组、尚未到期且未撤销的访问密钥原文，保留 `Bearer ` 前缀。不要使用密钥 ID、掩码或工具访问上游服务的密钥。客户端必须支持远程 Streamable HTTP 和自定义 HTTP 请求头；如果客户端使用独立的请求头设置界面，填写相同的 `Authorization` 值即可。

密钥原文只在创建或轮换时展示一次，服务端不能回读，因此配置示例只包含占位符。丢失原文时请新建或轮换访问密钥；轮换后需更新客户端配置。仅创建静态认证配置还不够，组必须关联该配置并创建属于该组的访问密钥。

公开模式的示例不包含认证头；OAuth 模式使用外部授权流程，不应填入组静态密钥。示例格式参考 [FastMCP 客户端配置](https://gofastmcp.com/clients/client)。


## 连接时提示 `The argument 'file' cannot be empty. Received ''`

这条错误可由 Node.js 的 `child_process.spawn("")` 产生，表示本地启动命令为空。对于本网关，首先检查是否误选了 stdio 传输；这不是要求给工具补一个 `file` 参数，也不应通过填入 Python 或 Node 命令来掩盖错误。

网关端点是远程 Streamable HTTP。Claude Code 的 `.mcp.json` 条目必须包含 `"type":"http"`；仅写 `url` 不能保证被识别为远程服务。现有注册需要更新类型并删除 `command`、`args` 等本地进程配置，然后重新连接。保留静态端点的 `headers.Authorization`。

VS Code 的 `.vscode/mcp.json` 使用顶层 `servers`（不是 `mcpServers`），内部条目同样使用 `type: http`、`url` 和 `headers`。其他客户端应在界面中选择 HTTP / Streamable HTTP 并按其配置规范填写字段；不能把一种客户端的 JSON 格式视为所有客户端通用。

如果修正类型后依然报错，请提供客户端名称、版本、完整错误栈和去除密钥后的配置，以确认是否是客户端其他本地命令的问题。

参考：[Claude Code 远程 MCP 配置](https://code.claude.com/docs/en/mcp)、[VS Code MCP 配置](https://code.visualstudio.com/docs/agents/reference/mcp-configuration)、[Node.js 子进程接口](https://nodejs.org/api/child_process.html)。

## OpenCode 配置

在组详情选择 OpenCode 标签，将示例合并到 `opencode.json`。OpenCode 使用顶层 `mcp` 和 `type: remote`，不能直接使用 Claude Code 的配置格式。静态密钥模式设置 `oauth: false`，避免触发自动 OAuth 授权。

```json
{
  "mcp": {
    "support": {
      "type": "remote",
      "url": "http://localhost:8000/support/mcp",
      "oauth": false,
      "headers": { "Authorization": "Bearer <YOUR_GROUP_ACCESS_KEY>" }
    }
  }
}
```

替换密钥后执行 `opencode mcp list` 查看连接状态。OAuth 组不应设置 `oauth: false`。
参考：[OpenCode MCP 配置](https://opencode.ai/docs/mcp-servers/)。

## 浏览器 MCP 连接

MCP 端点允许控制台来源和后端公共来源，支持 Authorization、MCP-Protocol-Version 等传输请求头，并暴露 WWW-Authenticate 以便客户端发现 OAuth。开发模式下控制台回环地址别名与管理端保持一致；不允许任意第三方网页跨域访问。管理 API 仍使用独立的 Cookie、Origin 和 CSRF 校验。
