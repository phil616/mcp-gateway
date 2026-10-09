# 配置参考

后端通过 Pydantic Settings 读取环境变量及当前工作目录的 `.env`，进程环境变量优先。以下默认值来自 `backend/gateway/settings.py`；Compose 会显式覆盖部分默认值。修改配置后需要重建进程。

| 变量 | 后端默认值 | 用途 |
| --- | --- | --- |
| `DATABASE_URL` | `postgresql+asyncpg://gateway:gateway@localhost:5432/gateway` | PostgreSQL 异步连接串 |
| `REDIS_URL` | `redis://localhost:6379/0` | 会话和限流存储 |
| `MASTER_KEY` | 必填 | Fernet 主密钥；必须保留以解密数据库中的上游密钥 |
| `KEY_VERSION` | `1` | 密文密钥版本；不能单独修改来完成主密钥轮换 |
| `PUBLIC_URL` | `http://localhost:8000` | 对外地址，用于组端点及 OAuth resource |
| `CONSOLE_ORIGIN` | `http://localhost:5173` | 浏览器控制台来源，协议、主机和端口需匹配 |
| `PLUGINS_PATH` | `plugins` | 插件根目录，相对路径以进程工作目录为准 |
| `COOKIE_SECURE` | `true` | HTTPS Cookie；本地 HTTP 必须设置 false |
| `SESSION_SECONDS` | `28800` | 管理员会话固定有效秒数，最小 1 |
| `THREAD_LIMIT` | `16` | 每 worker 同步工具容量，范围 1–128 |

## Compose 与宿主机的差异

Compose 默认数据库主机为 `postgres`，Redis 主机为 `redis`，公共地址为 `http://localhost:5173`，`CONSOLE_ORIGIN` 默认继承公共地址，`COOKIE_SECURE` 默认 false。这些是 `compose.yml` 的行为，不是 Settings 自身的继承规则。

Compose 还读取 `GATEWAY_PORT`（宿主机入口端口，默认 5173）和 `WORKERS`（Uvicorn worker 数，默认 1）。改变入口端口时也要修改 PUBLIC_URL，二者不会自动联动。

默认 Compose 没有传递 `PLUGINS_PATH` 和 `SESSION_SECONDS`；仅在宿主机 `.env` 增加它们不会改变容器设置。需要在 Compose override 中为 backend 及相关 setup 服务显式添加 environment；自定义插件目录必须让 sync 与 backend 使用相同制品。`plugins check` 单独通过 `--path` 选择目录，不读取 PLUGINS_PATH。

宿主机开发应提供可从宿主机连接的 PostgreSQL/Redis；默认 Compose 的二者不发布端口。不要把容器内部 DNS 名称直接用作宿主机连接地址。Vite 开发默认代理本机 8000 后端，因此通常设置 PUBLIC_URL 为 `http://localhost:8000`，CONSOLE_ORIGIN 为 `http://localhost:5173`。

## 前端构建

`VITE_API_URL` 是前端构建变量，默认 Compose 的构建参数为 `/`，使用同源 nginx 转发。独立前端在构建时指定后端地址，并设置后端 CONSOLE_ORIGIN。已构建的静态文件不会读取运行时容器环境变量来修改 API 地址。

本地初始化见[快速开始](../README.md)，HTTPS、发布顺序和备份见[部署指南](deployment.md)。
