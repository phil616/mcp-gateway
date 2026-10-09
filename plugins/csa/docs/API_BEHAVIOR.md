# API 行为约定

本文补充 [逐接口参考](API_REFERENCE.md) 中 JSON Schema 无法表达的业务规则。接口字段、参数位置、默认值、长度、枚举和分页上限见参考；机器可读版本为 [openapi.json](openapi.json)。不应把所有 POST 当作 201、所有 DELETE 当作 204，也不应把所有响应包装成 `{data: ...}`。

## 地址、认证及错误

- 业务接口前缀为 `/api`。OAuth/OIDC 使用 `/oauth/*`、`/.well-known/*`。`/api/` 才是存活检查；返回 `{"Hello":"World"}`，不会检查数据库。`/api/upload/health` 会 ping MongoDB，不可用时返回 503。
- 业务接口使用 `Authorization: Bearer <平台 JWT>`。缺少或无效凭据为 401，禁用用户为 403。角色从数据库用户读取；`admin` 为管理员，超级管理员还必须有 `is_super_admin=true`。
- 可选双 token 认证只有在配置允许时才接受 OAuth access token，且要求 client_id/audience 位于内部允许名单、scope 含 openid 或 profile、roles 含 user 或 admin、用户有效且 auth_version 匹配。OAuth id_token 和 client_credentials 服务身份不是通用平台登录凭据。
- 上传和邮件使用 `X-API-Key: <UPLOAD_API_KEY>`；用户 application key 不能替代此头。文件授权使用 URL query `token`，不能用平台 JWT 替代。
- HTTPException 通常返回 `{"detail": ...}`；detail 可为字符串或对象。默认输入校验为 422，detail 为错误数组。`/api/blobs/*` 与 `/api/admin/system-keys/import-oauth` 的请求模型校验失败改为 **400**，固定 detail 为 `敏感请求参数格式无效`，不回显原始敏感参数。
- OAuth 协议异常使用 `{"error":"...","error_description":"..."}`（后者可缺省）；同一 OAuth 端点的其他 HTTPException 仍使用 detail，例如格式错误的 Basic 凭据、UserInfo 无效 token。不能假设所有错误都是 OAuth error 对象。
- 限流接口和速率见逐接口参考的 `x-rate-limit`，按客户端 IP，超限 429，响应 `{"error":"Rate limit exceeded: ..."}`。不能仅凭 app limiter 的默认配置认定每个路由均受 200/minute 保护。
- MongoDB ConnectionFailure 的全局响应为 503，含 `detail`、`code=database_unavailable`、`request_id`，`Retry-After: 5`。系统密钥不可用的全局响应同为 503，code 为 `system_key_unavailable`，`Retry-After: 30`；端点自己捕获异常时可能返回自己的错误。
- 经请求追踪中间件正常返回的响应含 `X-Request-ID` 与 `X-Process-Time`。客户端 Request ID 仅接受 1–128 位 `[A-Za-z0-9._:-]`，否则重新生成。TrustedHost 拒绝、未捕获异常等外层响应不保证有这些头；500 也不保证是 JSON。
- 尾斜杠不匹配可能触发 307；OAuth 客户端列表和创建的规范路径包含末尾 `/`。路径不存在为 404，方法不支持为 405。生产环境可能关闭 `/docs`、`/redoc`、`/openapi.json`（ENABLE_API_DOCS）。

## 登录、验证与用户

- 邮箱密码登录与短信登录均返回联合类型：未启用 TOTP 返回 access_token/token_type/expires_in；启用 TOTP 返回 requires_2fa/challenge_token/expires_in，必须再调用 `/api/2fa/verify`。此时不能把 challenge_token 当 access_token。
- `/api/auth/token` 接收表单 username（邮箱）、password；TOTP 用户返回 403，需使用 JSON 登录完成二次验证。此入口不是 `/oauth/token` 的授权码兑换接口。
- 短信登录在手机号尚未绑定时自动注册，内部邮箱标识为 `<phone_number>@dreamreflex.com`。验证码失效或错误通常为 400；发送邮箱或短信验证码的服务失败返回 503。
- 普通改密和兼容的 change-password-simple 都需要 old_password。密码重置/变更会增加 auth_version 并撤销旧认证材料；客户端应重新登录。change-email 响应包含新邮箱的 access_token。修改手机号使用新号码收到的验证码，已被其他用户占用返回 400。
- TOTP 设置返回 setup_token、secret、otpauth_uri 和 expires_in；确认启用才返回一次性恢复码。恢复码每个只能使用一次；重新生成使旧恢复码失效。关闭 TOTP 和重生成恢复码需要当前 TOTP 或恢复码。设置/挑战令牌有期限和使用次数约束。
- TOTP 与 Passkey 互斥：存在任何 Passkey 凭证或已启用 Passkey 时无法启用 TOTP（409）；启用 TOTP 后无法注册、启用或通过 Passkey 登录（409）。普通管理员不能通过改资料、重置密码或重置 TOTP 接管超级管理员（403）。
- `/api/auth/oauth/callback` 用配置的 dashboard client 和 issuer 换取 OAuth token，再返回 app_token、user、oauth、state。不存在的邮箱会创建本地用户。此实现没有在回调分支重复执行本地 TOTP 挑战或 is_active 拒绝；不能把它描述成与密码登录完全相同。禁用用户的 app_token 随后访问受保护业务接口仍会被拒绝。
- 用户搜索参数为 query，按邮箱前缀搜索，最多 20 条；用户列表关键词为 keyword。check-exists 请求为 identifier（邮箱或手机号），不能传 email/phone_number 代替。
- 注销申请返回 202，重复 pending 申请保持幂等；管理员不能自助申请。取消无 pending 申请返回 409。申请本身不会停用账号；管理员执行最终删除前检查项目、OAuth 客户端、业务账号等阻塞资源，未清零返回 409。项目删除当前保留软删除记录，注销资源计数仍包含这些记录，不能承诺删除项目后必然可注销。

## 工单、业务账号、联系表单和负责人

- 工单类型 financial/technical/business，状态 pending/replied。更新必须是创建者且状态 pending，管理员身份不绕过创建者限制。重复回复为 400；普通用户只能访问或删除自己的工单。工单列表的状态查询参数是 status_filter。
- 业务账号每用户一条；pending、active、disabled 均不允许重复申请（400）。用户仅编辑资料。管理员为 pending 记录填齐 assigned_email 和 user_code 后自动激活；显式激活但缺少两项信息为 400。列表使用 status_filter。资料更新省略字段保持原值，字符串修剪为空后保存 null。
- 联系表单 `POST /api/owa/info` 必须提交 name、email、message、turnstileToken；验证失败为 400。管理员可查询和更新 is_processed/admin_notes。第一次置为已处理时记录处理时间和管理员邮箱；再置回 false 不自动清空历史处理信息。
- 负责人列表 skip=0、limit=100（最多 500），普通用户传 include_inactive=true 返回 403。重复标签和仍被项目引用的标签删除会被拒绝。

## 项目、文件、链接、任务与财务

- 项目创建/更新/删除、文件登记、链接、任务写操作需要管理员；普通用户只访问自己项目。设置负责人和评分允许所属用户或管理员。评分为 1–5；负责人请求对象 `{"responsible_tag_id":null}` 可清除负责人。
- 项目删除为软删除并清理关联文件、链接、任务和财务；保留订单/佣金审计，未结清佣金置 invalid。佣金已 settled 时删除返回 409。已删除项目不会在正常项目列表和详情返回。
- 创建文件、链接、任务、财务条目时，body.project_id 必须等于路径 project_id。**当前不一致时抛出未处理 ValueError，外部表现为 500，而非 422**。此为现有实现行为，调用方应保证一致。
- 创建文件先申请 `POST /api/projects/{project_id}/files/upload-url?filename=...&content_type=...`，再向返回 URL PUT 原始字节，最后登记 ProjectFileCreate。filename/content_type 是查询参数，不是 JSON 请求体。
- 文件登记必须绑定该项目和实际完成的上传授权，匹配 storage_key、大小、MIME。字段 oss_key 仅为 storage_key 的兼容输入；两者都给出时须一致。不能直接登记外部 URL 或把服务间上传当成项目上传。旧 OSS 文件不能直接下载，返回 409 并要求迁移。
- 文件列表支持 filename 模糊匹配、tag 精确匹配；任务列表使用 status 查询参数。列表的 limit 默认和上限因资源而异，见逐接口参考。
- 财务 amount 为金额浮点数（元），与商城整数分不同。income 存绝对值的正值，expense 存负值，四舍五入至两位小数；创建时普通用户状态强制为 unverified。只有管理员可修改状态；普通用户不能修改或删除 verified 条目（403）。列表带筛选和汇总，不能用单页 items 自行替代服务端汇总。

## 文件流与邮件

- `PUT /api/upload/{filename}` 为服务间上传，成功 201，返回 message/data 包装；data.etag 是 SHA-256，data.request_id 是 blob_id，**不是** X-Request-ID。filename 1–255 字符，首位必须为 ASCII 字母或数字，其余仅 `[A-Za-z0-9._-]`，不允许目录路径。
- 服务间上传空文件、非法文件名或非法 Content-Length 为 400；超过 UPLOAD_MAX_BYTES 为 413；存储错误为 503，其他被捕获错误为 500。
- `PUT /api/blobs/uploads/{grant_id}?token=...` 成功 201，直接返回 message/storage_key/size/sha256，不含 data。上传授权为一次性；授权无效、过期、已用或正在使用为 403。大小超限、空内容、MIME 不匹配在此路径为 **400**，不是服务间上传的 413。
- 下载授权在有效期内可重复使用。下载返回原始文件字节、元数据 MIME 和 Content-Disposition/Content-Length，禁止缓存；不返回 JSON，不支持文档中未声明的 Range/断点续传承诺。授权申请默认一小时，实际按返回 expires_in 使用。
- `/api/email/send-common` 成功 200，输入 title/content/message_id/recipients；recipients 1–50 个邮箱，message_id 1–128 位 `[A-Za-z0-9._:-]`。sendTime 由服务端生成。邮件发送失败为 500，成功响应 message_id 可为 null。

## OAuth/OIDC 与客户端

- 授权页 GET 成功为 200 HTML。未登录时 302 至登录页；POST 授权结果通过 302 Location 返回。client_id/redirect_uri 无效时禁止重定向到不可信地址；其他协议错误可在 redirect_uri 上带 error/error_description/state。
- 授权页接受平台 Bearer 或 OAuth 会话 Cookie；有 Bearer 时优先使用。POST 表单 decision=approve 为同意，其他值按拒绝处理。公共客户端需要 PKCE，使用 S256。
- `/oauth/token` 使用 application/x-www-form-urlencoded；client_id/client_secret 支持 Basic 或表单，代码优先使用非空表单值。authorization_code 需 code/redirect_uri 和匹配的 PKCE verifier；refresh_token 需刷新令牌；client_credentials 仅机密客户端可用。
- 授权码只能兑换一次。刷新令牌兑换后轮转，scope 只可缩小。授权码流程只有同时允许 refresh_token grant 且 scope 包含 offline_access 时才发刷新令牌；scope 包含 openid 才发 id_token。TokenResponse 中可空字段会出现 null，不代表必有可用令牌。
- UserInfo 仅接受 OAuth access token。sub、roles、ver 始终返回；profile 释放 name/preferred_username/picture，email 释放 email/email_verified，groups 释放 groups。未授权的可选 claims 缺省，而不是统一返回 null。
- Discovery issuer 来自配置，不使用请求 Host。JWKS 发布可用 RSA 公钥；没有可用激活签名密钥时返回 503，不返回假成功的空列表。
- POST /oauth/session 使用平台 JWT，remember 为 query 布尔值，默认 true。Cookie 为 HttpOnly、SameSite=Lax，domain/secure 按部署配置；remember=true 时寿命取配置上限与 JWT 剩余寿命的较小值，false 为会话 Cookie。DELETE 只清除 Cookie，不撤销 JWT 本身。
- 客户端列表 scope=mine 为默认，scope=all 仅管理员。client_id 由服务端生成；示例中应使用创建响应中的 client_id。机密客户端 secret 只在创建时明文返回；后续读取不返回原明文。重定向 URI 必须是无凭据、无片段的 HTTPS URL，仅回环主机允许 HTTP；issuer 与 Cookie 的 HTTP 配置另见环境文档。

## Passkey 与应用密钥

- registration-options/authentication-options 均返回 `{options,session_id}`。注册 options 的 user.id 是每账号独立的稳定随机 handle，注册要求 resident key；认证 options 不预先指定账号。
- register 提交浏览器 WebAuthn 凭证 JSON（id/rawId/type/response）以及顶层 session_id，可带 nickname。认证请求则使用 session_id/credential_id/authenticator_data/client_data_json/signature/raw_id 这些蛇形字段；二进制字段使用 base64url。
- 凭证列表中的 id 是数据库记录 ID；管理路径 `{credential_id}` 使用 **credential_id 字段**，不是 id。昵称支持 `{"nickname":"电脑"}` 和兼容的 JSON 字符串 `"电脑"`；toggle 只使用 `{"enabled":true}` 对象。
- 删除最后一个凭证前必须先禁用 Passkey 登录，否则 409；仅禁用而不删除凭证仍不能启用 TOTP。不存在或不属于自己的凭证返回 404。
- 应用密钥每用户最多一个，重复创建 400；无密钥时 info 返回 `{has_key:false,message:...}`（200），有密钥返回 metadata。create/rotate 才返回明文 key；轮转后旧 key 失效。status 支持对象 `{"is_active":false}` 和兼容的 JSON 布尔值。validate 用 body.key，不接受 URL key；无效密钥为 401。

## 商城与代理

- 商城目录仅登录可读，普通目录只返回 active 商品；管理员目录包括下架项。PUT 保存整个目录，请求 revision 必须匹配，成功加一，冲突 409。目录必须含 custom/popular 两个套餐，商品 ID 不得重复。
- 商城/佣金金额单位均为人民币分。quote 允许空选项，下单必须至少一项；重复商品 422，未知/下架商品 409，目录 revision 过期 409。客户端不得传金额；Selection 系列额外字段为 422。
- orders 成功或幂等重放均为 201，返回 id/order。幂等键是用户 ID + request_id；重复 key 返回首次订单快照，即使新请求内容不同。首次下单时检查目录及代理修订号；重复 key 指向已删除订单为 409。
- quote 可带 agent_code，成功返回 referral.revision；orders/assistant 使用优惠码时还需 agent_revision，过期或缺失为 409。优惠码不存在、代理用户失效或使用自己的优惠码为 422。优惠按 `(subtotal*rate_bps+5000)//10000` 计算，佣金等于优惠额。
- assistant 返回 message 与可空 selection；未配置为 503，上游请求或结果无效为 502。工具只更新选项，不会提交订单或支付。
- agents/me 未开通时返回 JSON null（200）；activate 自助开通，重复调用返回现有账号（200），冲突重试耗尽为 503。代理响应不含数据库 _id，也不返回底层 changes 调级审计数组。
- 管理员代理更新需 revision。一级 10%、二级 25%，三级使用 rate_percent（0–100，最多两位小数）；冲突或记录不存在为 409。历史订单不重算。
- commissions 列表支持 state，管理员另支持 agent_id；skip/limit 只影响 items，totals 不受 state 和分页影响。普通代理明细不含 buyer_email，管理员明细包含它。
- 佣金只能 pending→confirmed/invalid、confirmed→settled/invalid；操作 note 不能仅空格，confirmed 还需 receipt_confirmed=true。不合法转换为 422，记录不存在/已删除/expected_status 过期为 409。终态不能再次转换。

## 系统密钥与数据导出

- 系统密钥读取、生成、激活、校验、停用、删除、reconcile 需要管理员，**import-oauth 需要超级管理员**。初始化/生成/导入成功为 201，删除成功为 204；公钥导出返回 JSON 中 public_key_pem，不是 PEM 文件流。
- 初始化仅允许尚无激活 OAuth 密钥的状态；激活、停用、删除受用途、校验、保留期约束。冲突为 409，材料校验错误为 400，其他系统密钥服务异常为 503。import-oauth 可通过 activate 请求立即激活。
- 数据导出 catalog/documentation/download 三个操作都需要超级管理员。datasets 1–28 项，必须来自 catalog、不能重复，额外字段 422。documentation 返回 Markdown 附件；download 返回 application/json 附件。
- 导出保留原始数据库字段（包括敏感认证材料的已存储形式），不是用户 API 的安全投影。data 为按集合名组织的 Canonical Extended JSON v2 原始文档数组；在线逐集合读取不是同一时间点快照。详情见 字段说明（上游引用 `data-export-fields.md`，本仓库未收录）。读取准备阶段失败为 503；客户端仍需检查完整 JSON 和 complete 标记，以识别传输中断。
