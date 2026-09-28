# 验证记录

本次实现验证环境：Python 3.13、FastMCP 4.0.10、PostgreSQL 17、Redis 7、Node 24、Chromium（Playwright）。

通过 `uv run python tests/run.py`：

- **8 项后端测试**：真实 Streamable HTTP MCP 客户端；插件发现/历史保留/指纹拒绝；注入 schema；跨组密钥隔离；运行时绑定与全局工具启停；配置回滚、引用保护、并发版本冲突；静态 Key 过期/跨组/撤销/轮换；JWT/introspection 拒绝错误令牌；真实 OAuth 发现/DCR/PKCE/资源标识；legacy IDP 兼容性失败；同步线程上限、超时、异常脱敏。
- **1 项 Chromium 端到端测试**：管理员登录 → 创建密钥、配置集、组、绑定 → 启用工具 → 查看组详情 → 真实 MCP 客户端调用成功。
- **两个 Uvicorn worker 重启恢复**：相同管理员会话仍有效，组与工具目录内容一致，readiness 正常。
- 临时 PostgreSQL、Redis 和 HTTPS IDP 由独立 Compose 项目启动，使用随机端口和测试数据，结束后自动清理。

另外通过 Python Ruff 检查与格式检查、TypeScript/Vite 生产构建、前后端 Docker 镜像构建、默认 Compose 迁移/目录同步/服务启动、根包与独立 SDK wheel 构建。npm audit 未报告漏洞。

构建仍提示 Ant Design 共享 chunk 较大；不影响启动或功能。OAuth 测试客户端使用内存令牌存储，测试中会出现相应提示。Gunicorn 部署命令已提供，实际多 worker 验收使用 Uvicorn；测试 IDP 不代表所有商业 IDP 的租户配置均兼容。
