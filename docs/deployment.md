# 部署与故障排查

完整环境变量及宿主机/Compose 默认值差异见[配置参考](configuration.md)。

默认 Compose 仅发布前端 nginx 的 `5173` 端口（可用 `GATEWAY_PORT` 修改），后端 `8000`、PostgreSQL 和 Redis 只在 Docker 内网访问。前端通过同源地址请求 API，nginx 转发 `/api/`、`/{group}/mcp`、`/.well-known/`、`/health/`、`/docs`、`/redoc` 和 `/openapi.json`；其他路径提供管理页面。迁移、目录同步仍是独立部署命令。

## 单域名 HTTPS

只使用 `https://mcp.example.com` 时，`.env` 配置：

```dotenv
PUBLIC_URL=https://mcp.example.com
COOKIE_SECURE=true
GATEWAY_PORT=5173
# CONSOLE_ORIGIN 默认继承 PUBLIC_URL；已有旧值时删除或改成相同地址。
```

将域名的所有请求代理到 `http://127.0.0.1:5173`。以下适用于宿主机 nginx 或 host 网络 OpenResty，域名和证书路径需替换。桥接网络代理容器应使用可达的宿主机地址，或加入 Compose 网络后代理 `frontend:80`。

```nginx
server {
    listen 80;
    server_name mcp.example.com;
    return 301 https://$host$request_uri;
}
server {
    listen 443 ssl;
    server_name mcp.example.com;
    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;
    location / {
        proxy_pass http://127.0.0.1:5173;
        proxy_http_version 1.1;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Connection "";
        proxy_buffering off;
        proxy_cache off;
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
    }
}
```

两层代理均关闭响应缓冲，保留 MCP 流式响应。不要改写请求路径、拦截 OPTIONS 或额外添加 CORS 响应头。管理页面为 `/`，API 文档为 `/docs`，MCP 地址为 `/{group}/mcp`。

仅更新代理或入口配置、且数据库与插件制品已经同步时执行（代码发布须使用下文整批流程）：

```sh
docker compose up -d --build --wait backend frontend
curl -f http://localhost:5173/health/ready
```

以后只修改域名时，前端无需重新构建，执行 `docker compose up -d --force-recreate --wait backend` 更新后端环境变量。`PUBLIC_URL` 决定 MCP 端点和 OAuth resource URL，必须与外部访问地址一致。HTTPS 设置 `COOKIE_SECURE=true`；本地 HTTP 设置为 `false`。管理写入仍验证 Origin 和 CSRF。

独立前端部署可在构建时设置 `VITE_API_URL` 并配置后端 `CONSOLE_ORIGIN`；默认 Compose 固定使用同源访问。不要把 `.env` 打入镜像。

外部 PostgreSQL URI 必须是 `postgresql+asyncpg://...`。设置 DATABASE_URL/REDIS_URL 即可接入外部服务；Compose 的依赖服务可以仍运行，也可以直接使用构建后的后端镜像部署。数据库连接池为每 worker 独立实例，容量预算需乘 worker 数。

## 多 worker 与生命周期

```sh
uv run uvicorn gateway.app:create_app --factory --host 0.0.0.0 --port 8000 --workers 2 --no-access-log
```

可以安装 Gunicorn 与 `uvicorn-worker` 后使用：

```sh
gunicorn 'gateway.app:create_app()' -k uvicorn_worker.UvicornWorker -w 2 -b 0.0.0.0:8000
```

Gunicorn 属于可选部署依赖；仓库验收 runner 使用两个 Uvicorn worker。MCP 为无状态 Streamable HTTP，初始化与调用可落在不同 worker，无需粘滞。每个请求以 PostgreSQL REPEATABLE READ 读取组、认证、绑定、工具和密钥快照；提交之后的新请求使用新配置，正在执行的调用继续使用旧副本。Redis 只保存管理员会话/登录限流，不缓存组权限。

FastAPI lifespan 管理 FastMCP lifespan、数据库连接池、Redis、HTTP 客户端和同步工具并发容量。健康检查 `/health/live` 不访问数据库；`/health/ready` 检查数据库、Redis和部署指纹。`THREAD_LIMIT` 默认为每 worker 16，工具超时包含容量排队时间。管理员密码验证使用独立的每 worker 4 个线程容量，不与同步工具争抢默认线程名额。同步线程超时后仍占用容量直到完成，不能强制撤销外部副作用。

代码发布采用整批停止/重启：停止所有旧 worker → 安装新制品 → 迁移 → plugins check → plugins sync → 启动所有 worker。新增工具只进入目录，不会自动绑定。启动时指纹不匹配会失败；发布中不得让旧代码 worker 继续处理新目录配置。每个 worker 必须使用相同镜像及插件目录，不支持运行时热加载。

## 密钥与备份

MASTER_KEY 是 URL-safe base64 的 32 字节 Fernet 主密钥，来自部署 secret；KEY_VERSION 默认为 1。加密使用认证加密，数据库不包含主密钥。备份 PostgreSQL 与主密钥分别存储；只备份数据库不能恢复密钥。当前版本只加载一个主密钥版本，轮换主密钥需要停机迁移全部密文并更新 KEY_VERSION；没有自动主密钥轮换命令。组访问 Key 可通过 Web 原子轮换。

Redis 持久化用于尽量保留管理员会话；丢失 Redis 数据会退出登录并清空限流状态，不影响工具组配置。数据库变更和无值审计原子提交。默认日志仅记录 request ID、group、tool、elapsed_ms、status；关闭 Uvicorn access log 避免意外记录查询参数。工具失败另记录异常类型和代码位置，但不记录异常正文。HTTP 响应与工具日志使用同一个 request ID。日志不记录工具参数、结果正文和凭据。

## 故障排查

| 现象 | 检查 |
|---|---|
| 启动失败 artifact mismatch | 使用同一插件制品运行 plugins check / sync，整批重启 |
| 插件无法导入 | plugins check 提供入口路径与异常；依赖在构建阶段安装 |
| MCP 404 | 组是否存在且 enabled；路径必须精确为 `/{group}/mcp` |
| tools/list 为空 | 绑定 enabled、工具 enabled/available；重新查询列表 |
| 管理 API 403 | 前端 origin、Cookie Secure/HTTPS、CSRF header |
| 配置保存 422 | 查看字段路径；必填字段和 SecretStr 引用；嵌套覆盖是整个字段替换 |
| 更新或删除 409 | 刷新 version；查看引用依赖；同组工具/暴露名称唯一 |
| OAuth 401/403 | metadata URL、issuer、组完整 URL audience、exp、scope、JWKS kid |
| OAuth 登录失败 | 运行兼容检查，确认 PKCE、resource 和客户端注册；不能只勾选 OAuth 模式 |
| 工具超时 | 上游 I/O 超时、线程容量、CPU 密集任务；同步线程可能仍执行 |
| ready 503 | PostgreSQL/Redis 连通、迁移、制品一致性 |

## 验收覆盖

`tests/run.py` 使用随机端口、独立 Compose 项目、临时数据库和 TLS IDP。覆盖插件导入失败/重复 ID、schema 注入隐藏、并发跨组密钥摘要验证、动态绑定/全局工具启停、配置回滚和版本冲突、引用删除保护、公开/静态/JWT/introspection、真实 OAuth PKCE 授权与不足能力 IDP、同步线程上限/超时/异常脱敏、两个 worker 的撤销、新进程恢复、浏览器登录创建密钥/配置/组/绑定后真实 MCP 调用。测试 IDP 只替代外部服务，不测试特定商业 IDP 的租户策略。

### API 返回 400，但没有错误信息

先区分浏览器 Network 中的 `OPTIONS` 预检与实际 API/MCP 请求。CORS 预检被拒绝时返回 400，响应提示检查 `CONSOLE_ORIGIN`、请求方法和请求头；浏览器可能因来源不被允许而禁止 JavaScript 读取该响应。

仅在 `COOKIE_SECURE=false` 且 `CONSOLE_ORIGIN` 是本地 HTTP 回环地址时，网关接受同协议、同端口的 `localhost`、`127.0.0.1`、`[::1]` 别名。前端对本地 HTTP API 使用与页面相同的回环主机名，避免 Cookie 跨站丢失。HTTPS 或非本地域名仍须与配置的来源精确一致。

所有 HTTP 响应包含 `X-Request-ID`。即使启动时使用 `--no-access-log`，4xx/5xx 仍记录 `http_failure`，包含请求编号、方法、路径、状态、来源和耗时。意外异常另记录类型及代码位置，不记录异常参数、请求正文、查询串或凭据。前端显示 API 错误时附上请求编号；网络/CORS 错误则提供 API 地址及来源配置检查提示。

```sh
docker compose logs --tail=200 backend
# 按界面提示的请求编号在日志中定位；不要把 API Key 放进日志或反馈截图。
```
