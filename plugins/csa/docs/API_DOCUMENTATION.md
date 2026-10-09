# API Documentation

本页为全部接口索引。完整参数、Schema、状态码和响应媒体类型见 [API_REFERENCE.md](API_REFERENCE.md)，业务约束与异常行为见 [API_BEHAVIOR.md](API_BEHAVIOR.md)，机器可读契约见 [openapi.json](openapi.json)。

运行 `uv run python -m scripts.generate_api_docs --check` 检查自动生成文档是否同步；测试同时检查本页是否遗漏或重复接口。

## 通用约定

- API 基础路径：`/api`
- OAuth/OIDC 标准端点不带 `/api` 前缀：`/oauth/*`、`/.well-known/*`
- 业务认证：`Authorization: Bearer <access_token>`
- 服务间上传/邮件认证：`X-API-Key: <UPLOAD_API_KEY>`
- 分页参数通常为 `skip`、`limit`
- 管理员权限由 `UserRole.ADMIN` 判断

## 服务状态

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/` | 公开 | 基础服务存活检查 |

## 认证与用户

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/auth/send-code` | 公开，限流 | 发送邮箱验证码 |
| POST | `/api/auth/register` | 公开，限流 | 邮箱验证码注册 |
| POST | `/api/auth/login` | 公开，限流 | JSON 登录；未启用 TOTP 时返回 JWT，已启用时返回短期二次验证挑战 |
| POST | `/api/auth/token` | 公开，限流 | OAuth2 password form 登录，供 Swagger 授权使用；TOTP 用户不可用此入口旁路 |
| GET | `/api/auth/me` | 登录 | 获取当前用户 |
| POST | `/api/auth/send-sms-code` | 公开，限流 | 发送短信验证码 |
| POST | `/api/auth/login-by-sms` | 公开，限流 | 短信登录，不存在用户会自动注册；TOTP 用户仍需完成二次验证 |
| POST | `/api/2fa/verify` | 公开，限流 | 使用 TOTP 或一次性恢复码完成登录二次验证 |
| GET | `/api/2fa/totp/status` | 登录 | 获取 TOTP、恢复码和 Passkey 互斥状态 |
| POST | `/api/2fa/totp/setup` | 登录 | 创建短期设置会话并返回扫码 URI 和手动密钥 |
| POST | `/api/2fa/totp/confirm` | 登录 | 校验首次动态码、启用 TOTP，并仅本次返回恢复码 |
| POST | `/api/2fa/totp/disable` | 登录 | 校验 TOTP 或恢复码后关闭二次验证 |
| POST | `/api/2fa/totp/recovery-codes/regenerate` | 登录 | 校验当前凭据后作废旧恢复码并仅本次返回新恢复码 |
| POST | `/api/auth/change-phone-number` | 登录 | 使用短信验证码修改手机号 |
| POST | `/api/auth/reset-password-by-sms` | 公开，限流 | 短信重置密码 |
| POST | `/api/auth/reset-password-by-email` | 公开，限流 | 邮箱验证码重置密码 |
| POST | `/api/auth/admin/change-password` | 管理员 | 按邮箱修改用户密码 |
| POST | `/api/auth/oauth/callback` | 公开 | 后端交换 OAuth 授权码并创建本地会话 |

用户管理：

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/users/me` | 登录 | 获取当前用户资料 |
| PATCH | `/api/users/me` | 登录 | 更新当前用户资料 |
| POST | `/api/users/me/change-password` | 登录 | 校验旧密码后改密 |
| POST | `/api/users/me/change-password-simple` | 登录 | 兼容路径（已弃用，仍须校验旧密码） |
| POST | `/api/users/me/change-email` | 登录 | 验证码修改邮箱并返回新 token |
| GET | `/api/users/me/deletion-request` | 登录 | 查看自己的待处理账号注销申请 |
| POST | `/api/users/me/deletion-request` | 登录（非管理员） | 提交账号注销申请，账号不会立即删除 |
| DELETE | `/api/users/me/deletion-request` | 登录 | 取消待处理的账号注销申请 |
| POST | `/api/users/check-exists` | 公开 | 检查邮箱或手机号是否存在 |
| GET | `/api/users/search` | 管理员 | 按邮箱前缀搜索 |
| GET | `/api/users` | 管理员 | 用户列表 |
| GET | `/api/users/deletion-requests` | 管理员 | 查看注销申请和待清理资源计数 |
| DELETE | `/api/users/deletion-requests/{request_id}/account` | 管理员 | 关联业务资源清零后永久删除账号及认证数据 |
| GET | `/api/users/{user_id}` | 管理员 | 用户详情 |
| PATCH | `/api/users/{user_id}` | 管理员 | 更新用户资料、角色、状态 |
| POST | `/api/users/{user_id}/reset-password` | 管理员 | 重置用户密码 |
| DELETE | `/api/users/{user_id}/2fa/totp` | 管理员 | 救援锁定账号，重置 TOTP、恢复码和待处理挑战 |

## 系统密钥管理（管理员）

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/admin/system-keys/status` | 管理员 | 获取五类密钥用途的激活和健康状态 |
| GET | `/api/admin/system-keys` | 管理员 | 查询密钥元数据，不返回私钥/对称明文 |
| POST | `/api/admin/system-keys/initialize-oauth` | 管理员，限流 | 生成并激活首个 OAuth RSA 密钥 |
| POST | `/api/admin/system-keys/generate` | 管理员，限流 | 生成待校验、待激活的轮换密钥 |
| POST | `/api/admin/system-keys/import-oauth` | 超级管理员，限流 | 导入 PKCS#8 RSA 私钥并立即加密入库 |
| POST | `/api/admin/system-keys/{kid}/validate` | 管理员，限流 | 校验密文、算法、强度、指纹及公私钥匹配 |
| POST | `/api/admin/system-keys/{kid}/activate` | 管理员，限流 | 原子切换指定用途的激活 KID |
| POST | `/api/admin/system-keys/{kid}/disable` | 管理员，限流 | 停用非激活密钥 |
| DELETE | `/api/admin/system-keys/{kid}` | 管理员，限流 | 保留期结束后删除已停用密钥 |
| POST | `/api/admin/system-keys/reconcile` | 管理员，限流 | 全库一致性校验并修复派生状态 |
| GET | `/api/admin/system-keys/{kid}/public-key` | 管理员 | 导出 RSA 公钥 PEM |
| GET | `/api/admin/system-keys/audit/events` | 管理员 | 查询 MongoDB 密钥审计事件 |

私钥、对称密钥和根加密 Secret 永不由读取接口返回。

## 工单

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/tickets` | 登录 | 创建工单 |
| GET | `/api/tickets` | 登录 | 列表，管理员看全部，普通用户看自己的 |
| GET | `/api/tickets/{ticket_id}` | 登录 | 详情 |
| PUT | `/api/tickets/{ticket_id}` | 创建者 | 只能更新待回复工单 |
| POST | `/api/tickets/{ticket_id}/reply` | 管理员 | 回复并置为 `replied` |
| DELETE | `/api/tickets/{ticket_id}` | 创建者或管理员 | 删除 |

工单类型：`financial`、`technical`、`business`。状态：`pending`、`replied`。

## 业务账号

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/business-accounts/me` | 登录 | 当前用户业务账号 |
| POST | `/api/business-accounts/me/apply` | 登录 | 申请业务账号，初始 `pending` |
| PATCH | `/api/business-accounts/me` | 登录 | 更新业务账号可编辑字段 |
| GET | `/api/business-accounts` | 管理员 | 列表，可按状态过滤 |
| GET | `/api/business-accounts/{account_id}` | 所属用户或管理员 | 详情 |
| PUT | `/api/business-accounts/{account_id}` | 管理员 | 分配邮箱、用户识别码、调整状态 |
| DELETE | `/api/business-accounts/{account_id}` | 管理员 | 删除业务账号，供账号注销前人工清理 |

状态：`pending`、`active`、`disabled`。

## 项目

项目本体：

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/projects` | 管理员 | 为用户创建项目 |
| GET | `/api/projects` | 管理员 | 项目列表，可按 owner email 过滤 |
| GET | `/api/projects/me` | 登录 | 当前用户项目列表 |
| GET | `/api/projects/{project_id}` | 所属用户或管理员 | 项目详情 |
| PUT | `/api/projects/{project_id}` | 管理员 | 更新项目 |
| DELETE | `/api/projects/{project_id}` | 管理员 | 软删除项目、清理关联资源；已结清佣金的项目不可删除 |
| PUT | `/api/projects/{project_id}/responsible-tag` | 所属用户或管理员 | 设置负责人标签 |
| PUT | `/api/projects/{project_id}/rating` | 所属用户或管理员 | 设置 1-5 评分 |

项目文件：

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/projects/{project_id}/files/upload-url` | 管理员 | 获取 MongoDB GridFS 一次性上传 URL |
| POST | `/api/projects/{project_id}/files` | 管理员 | 上传后创建文件记录 |
| GET | `/api/projects/{project_id}/files` | 所属用户或管理员 | 文件列表 |
| POST | `/api/projects/files/{file_id}/download-url` | 所属用户或管理员 | 下载预签名 URL |
| PUT | `/api/projects/files/{file_id}` | 管理员 | 更新文件信息 |
| DELETE | `/api/projects/files/{file_id}` | 管理员 | 删除文件和 GridFS 内容 |

项目链接、任务、财务：

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/projects/{project_id}/links` | 管理员 | 创建链接 |
| GET | `/api/projects/{project_id}/links` | 所属用户或管理员 | 链接列表 |
| PUT | `/api/projects/links/{link_id}` | 管理员 | 更新链接 |
| DELETE | `/api/projects/links/{link_id}` | 管理员 | 删除链接 |
| POST | `/api/projects/{project_id}/tasks` | 管理员 | 创建任务 |
| GET | `/api/projects/{project_id}/tasks` | 所属用户或管理员 | 任务列表，可按状态过滤 |
| PUT | `/api/projects/tasks/{task_id}` | 管理员 | 更新任务 |
| DELETE | `/api/projects/tasks/{task_id}` | 管理员 | 删除任务 |
| POST | `/api/projects/{project_id}/finances` | 所属用户或管理员 | 创建财务条目 |
| GET | `/api/projects/{project_id}/finances` | 所属用户或管理员 | 财务列表和汇总 |
| PUT | `/api/projects/finances/{entry_id}` | 所属用户或管理员 | 普通用户仅修改未核对条目且不能修改状态 |
| DELETE | `/api/projects/finances/{entry_id}` | 所属用户或管理员 | 普通用户仅删除未核对条目 |

## 负责人标签

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/responsible-tags` | 管理员 | 创建标签 |
| GET | `/api/responsible-tags` | 登录 | 列表；普通用户默认只看启用标签 |
| PUT | `/api/responsible-tags/{tag_id}` | 管理员 | 更新标签 |
| DELETE | `/api/responsible-tags/{tag_id}` | 管理员 | 删除未被项目使用的标签 |

## OAuth2/OIDC

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/oauth/authorize` | OAuth 会话 | 授权页 |
| POST | `/oauth/authorize` | OAuth 会话 | 同意/拒绝授权 |
| POST | `/oauth/token` | client | 支持 `authorization_code`、`refresh_token`、`client_credentials` |
| GET | `/oauth/userinfo` | OAuth access token | OIDC UserInfo |
| POST | `/oauth/session` | 业务 JWT | 写入 OAuth 授权 Cookie |
| DELETE | `/oauth/session` | 浏览器 | 清除 OAuth 授权 Cookie |
| GET | `/.well-known/openid-configuration` | 公开 | OIDC Discovery |
| GET | `/.well-known/jwks.json` | 公开 | JWKS |

OAuth 客户端管理：

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/oauth/clients/` | 登录 | 查看自己的客户端；管理员可 `scope=all` |
| POST | `/api/oauth/clients/` | 登录 | 创建 OAuth client |
| PUT | `/api/oauth/clients/{client_id}` | 所属用户或管理员 | 更新 client |
| DELETE | `/api/oauth/clients/{client_id}` | 所属用户或管理员 | 删除 client |

## Passkey

Passkey 与 TOTP 二次验证互斥。存在任一已注册 Passkey 时不能启用 TOTP；启用 TOTP 后不能注册、启用或使用 Passkey 登录。

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/passkey/registration-options` | 登录 | 获取注册选项 |
| POST | `/api/passkey/register` | 登录 | 注册凭证 |
| GET | `/api/passkey/authentication-options` | 公开 | 获取认证选项 |
| POST | `/api/passkey/authenticate` | 公开 | Passkey 登录 |
| GET | `/api/passkey/credentials` | 登录 | 凭证列表 |
| PUT | `/api/passkey/credentials/{credential_id}/nickname` | 登录 | 修改昵称 |
| PUT | `/api/passkey/credentials/{credential_id}/primary` | 登录 | 设置主凭证 |
| DELETE | `/api/passkey/credentials/{credential_id}` | 登录 | 删除凭证；删除最后一个前必须先禁用 Passkey 登录 |
| PUT | `/api/passkey/toggle` | 登录 | 启用/禁用 Passkey 登录 |

Passkey 注册使用每个账号独立、稳定且不包含邮箱等个人信息的随机 user handle。
由于认证入口采用无用户名的 discoverable credential 流程，注册选项要求 resident key。

## 应用密钥、上传、邮件、联系表单

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/application-key/create` | 登录 | 创建用户 application key |
| GET | `/api/application-key/info` | 登录 | 查看 key 信息 |
| POST | `/api/application-key/rotate` | 登录 | 轮转 key |
| PUT | `/api/application-key/status` | 登录 | 启用/禁用 key |
| POST | `/api/application-key/validate` | JSON key | 验证 key 并返回用户信息；密钥不进入 URL |
| GET | `/api/api-keys` | 登录（只读） | 查看自己的账号 APIKey |
| GET | `/api/api-keys/{key_id}` | 登录（只读） | 查看自己的 APIKey 密钥 |
| GET | `/api/admin/api-keys` | 管理员 | 查询所有用户 APIKey |
| POST | `/api/admin/api-keys` | 管理员 | 为用户创建 APIKey |
| GET | `/api/admin/api-keys/{key_id}` | 管理员 | 查看 APIKey 密钥 |
| PATCH | `/api/admin/api-keys/{key_id}` | 管理员 | 修改名称或启停状态 |
| POST | `/api/admin/api-keys/{key_id}/rotate` | 管理员 | 重置 APIKey |
| DELETE | `/api/admin/api-keys/{key_id}` | 管理员 | 删除 APIKey |
| GET | `/api/upload/health` | 公开 | MongoDB GridFS 上传服务状态 |
| PUT | `/api/upload/{filename}` | `X-API-Key` | 服务间直传文件到 GridFS |
| PUT | `/api/blobs/uploads/{grant_id}` | 短期 token | 使用一次性授权上传文件 |
| GET | `/api/blobs/downloads/{grant_id}` | 短期 token | 下载 GridFS 文件 |
| POST | `/api/email/send-common` | `X-API-Key` | 发送通用模板邮件 |
| POST | `/api/owa/info` | 公开 + Turnstile | 提交联系表单 |
| GET | `/api/owa/info` | 管理员 | 表单列表 |
| GET | `/api/owa/info/{contact_id}` | 管理员 | 表单详情 |
| PUT | `/api/owa/info/{contact_id}` | 管理员 | 更新处理状态 |
| DELETE | `/api/owa/info/{contact_id}` | 管理员 | 删除表单 |

## 商城

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/shop/catalog` | 登录 | 上架商品目录 |
| GET | `/api/shop/admin/catalog` | 管理员 | 完整商品目录 |
| PUT | `/api/shop/admin/catalog` | 管理员 | 以 revision 并发控制保存目录 |
| POST | `/api/shop/quote` | 登录 | 报价与代理优惠校验，允许空选项 |
| POST | `/api/shop/orders` | 登录 | 以 request_id 幂等创建订单/项目，成功 201 |
| POST | `/api/shop/assistant` | 登录 | 商城咨询及选项建议，不提交订单 |

## 代理及佣金

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/agents/me` | 登录 | 当前代理资料，未开通返回 null |
| POST | `/api/agents/activate` | 登录 | 幂等开通一级代理，成功 200 |
| GET | `/api/agents/admin/accounts` | 管理员 | 代理查询与分页 |
| PUT | `/api/agents/admin/accounts/{user_id}` | 管理员 | 按 revision 调整等级、比例 |
| GET | `/api/agents/commissions` | 登录 | 自己的佣金明细和汇总 |
| GET | `/api/agents/admin/commissions` | 管理员 | 所有佣金，可按 agent_id 筛选 |
| PUT | `/api/agents/admin/commissions/{order_id}` | 管理员 | 按 expected_status 确认、作废或结清 |

## 数据导出

| Method | Path | 权限 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/admin/data-export/catalog` | 超级管理员 | 可导出数据集目录 |
| GET | `/api/admin/data-export/documentation` | 超级管理员 | 下载 Markdown 字段文档 |
| POST | `/api/admin/data-export` | 超级管理员 | 按 datasets 导出原始 MongoDB Extended JSON 附件 |
