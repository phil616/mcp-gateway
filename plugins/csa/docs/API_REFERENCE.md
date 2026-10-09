# API 完整参考（自动生成）

由 `python -m scripts.generate_api_docs` 生成；不要直接编辑。

共 **151** 个接口操作。字段、必填性、默认值、枚举、范围、媒体类型和响应结构来自运行时 OpenAPI。
阅读时同时参照 [行为约定](API_BEHAVIOR.md)、[接口索引](API_DOCUMENTATION.md) 和 [调用示例](API_EXAMPLES.md)。
机器可读契约见 [openapi.json](openapi.json)。`$ref` 指向本文末尾同名 Schema；`required` 表示必须存在，`null` 与缺省不同。
JSON Schema 不能完整表达字段之间的校验、资源归属、状态转换；请同时阅读行为约定和自定义校验索引。

## 接口目录

| 方法 | 路径 | 权限入口 | 成功状态 |
| --- | --- | --- | --- |
| GET | `/.well-known/jwks.json` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/.well-known/openid-configuration` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/2fa/totp/confirm` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/2fa/totp/disable` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/2fa/totp/recovery-codes/regenerate` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/2fa/totp/setup` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/2fa/totp/status` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/2fa/verify` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/admin/api-keys` | 管理员 | 200 |
| POST | `/api/admin/api-keys` | 管理员 | 201 |
| DELETE | `/api/admin/api-keys/{key_id}` | 管理员 | 204 |
| GET | `/api/admin/api-keys/{key_id}` | 管理员 | 200 |
| PATCH | `/api/admin/api-keys/{key_id}` | 管理员 | 200 |
| POST | `/api/admin/api-keys/{key_id}/rotate` | 管理员 | 200 |
| POST | `/api/admin/data-export` | 超级管理员 | 200 |
| GET | `/api/admin/data-export/catalog` | 超级管理员 | 200 |
| GET | `/api/admin/data-export/documentation` | 超级管理员 | 200 |
| GET | `/api/admin/system-keys` | 管理员 | 200 |
| GET | `/api/admin/system-keys/audit/events` | 管理员 | 200 |
| POST | `/api/admin/system-keys/generate` | 管理员 | 201 |
| POST | `/api/admin/system-keys/import-oauth` | 超级管理员 | 201 |
| POST | `/api/admin/system-keys/initialize-oauth` | 管理员 | 201 |
| POST | `/api/admin/system-keys/reconcile` | 管理员 | 200 |
| GET | `/api/admin/system-keys/status` | 管理员 | 200 |
| DELETE | `/api/admin/system-keys/{kid}` | 管理员 | 204 |
| POST | `/api/admin/system-keys/{kid}/activate` | 管理员 | 200 |
| POST | `/api/admin/system-keys/{kid}/disable` | 管理员 | 200 |
| GET | `/api/admin/system-keys/{kid}/public-key` | 管理员 | 200 |
| POST | `/api/admin/system-keys/{kid}/validate` | 管理员 | 200 |
| POST | `/api/agents/activate` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/agents/admin/accounts` | 管理员 | 200 |
| PUT | `/api/agents/admin/accounts/{user_id}` | 管理员 | 200 |
| GET | `/api/agents/admin/commissions` | 管理员 | 200 |
| PUT | `/api/agents/admin/commissions/{order_id}` | 管理员 | 200 |
| GET | `/api/agents/commissions` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/agents/me` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/api-keys` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/api-keys/{key_id}` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/application-key/create` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/application-key/info` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/application-key/rotate` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/application-key/status` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/application-key/validate` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/admin/change-password` | 管理员 | 200 |
| POST | `/api/auth/change-phone-number` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/auth/login` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/login-by-sms` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/auth/me` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/auth/oauth/callback` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/register` | 公开；业务凭据要求见接口说明 | 201 |
| POST | `/api/auth/reset-password-by-email` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/reset-password-by-sms` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/send-code` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/send-sms-code` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/api/auth/token` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/blobs/downloads/{grant_id}` | 短期授权 URL 中的 token | 200 |
| PUT | `/api/blobs/uploads/{grant_id}` | 短期授权 URL 中的 token | 201 |
| GET | `/api/business-accounts` | 管理员 | 200 |
| GET | `/api/business-accounts/me` | 登录；资源归属限制见接口说明 | 200 |
| PATCH | `/api/business-accounts/me` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/business-accounts/me/apply` | 登录；资源归属限制见接口说明 | 201 |
| DELETE | `/api/business-accounts/{account_id}` | 管理员 | 204 |
| GET | `/api/business-accounts/{account_id}` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/business-accounts/{account_id}` | 管理员 | 200 |
| POST | `/api/email/send-common` | X-API-Key（UPLOAD_API_KEY） | 200 |
| GET | `/api/oauth/clients/` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/oauth/clients/` | 登录；资源归属限制见接口说明 | 201 |
| DELETE | `/api/oauth/clients/{client_id}` | 登录；资源归属限制见接口说明 | 204 |
| PUT | `/api/oauth/clients/{client_id}` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/owa/info` | 管理员 | 200 |
| POST | `/api/owa/info` | 公开；业务凭据要求见接口说明 | 201 |
| DELETE | `/api/owa/info/{contact_id}` | 管理员 | 204 |
| GET | `/api/owa/info/{contact_id}` | 管理员 | 200 |
| PUT | `/api/owa/info/{contact_id}` | 管理员 | 200 |
| POST | `/api/passkey/authenticate` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/passkey/authentication-options` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/passkey/credentials` | 登录；资源归属限制见接口说明 | 200 |
| DELETE | `/api/passkey/credentials/{credential_id}` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/passkey/credentials/{credential_id}/nickname` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/passkey/credentials/{credential_id}/primary` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/passkey/register` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/passkey/registration-options` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/passkey/toggle` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/projects` | 管理员 | 200 |
| POST | `/api/projects` | 管理员 | 201 |
| DELETE | `/api/projects/files/{file_id}` | 管理员 | 204 |
| PUT | `/api/projects/files/{file_id}` | 管理员 | 200 |
| POST | `/api/projects/files/{file_id}/download-url` | 登录；资源归属限制见接口说明 | 200 |
| DELETE | `/api/projects/finances/{entry_id}` | 登录；资源归属限制见接口说明 | 204 |
| PUT | `/api/projects/finances/{entry_id}` | 登录；资源归属限制见接口说明 | 200 |
| DELETE | `/api/projects/links/{link_id}` | 管理员 | 204 |
| PUT | `/api/projects/links/{link_id}` | 管理员 | 200 |
| GET | `/api/projects/me` | 登录；资源归属限制见接口说明 | 200 |
| DELETE | `/api/projects/tasks/{task_id}` | 管理员 | 204 |
| PUT | `/api/projects/tasks/{task_id}` | 管理员 | 200 |
| DELETE | `/api/projects/{project_id}` | 管理员 | 204 |
| GET | `/api/projects/{project_id}` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/projects/{project_id}` | 管理员 | 200 |
| GET | `/api/projects/{project_id}/files` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/projects/{project_id}/files` | 管理员 | 201 |
| POST | `/api/projects/{project_id}/files/upload-url` | 管理员 | 200 |
| GET | `/api/projects/{project_id}/finances` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/projects/{project_id}/finances` | 登录；资源归属限制见接口说明 | 201 |
| GET | `/api/projects/{project_id}/links` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/projects/{project_id}/links` | 管理员 | 201 |
| PUT | `/api/projects/{project_id}/rating` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/projects/{project_id}/responsible-tag` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/projects/{project_id}/tasks` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/projects/{project_id}/tasks` | 管理员 | 201 |
| GET | `/api/responsible-tags` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/responsible-tags` | 管理员 | 201 |
| DELETE | `/api/responsible-tags/{tag_id}` | 管理员 | 204 |
| PUT | `/api/responsible-tags/{tag_id}` | 管理员 | 200 |
| GET | `/api/shop/admin/catalog` | 管理员 | 200 |
| PUT | `/api/shop/admin/catalog` | 管理员 | 200 |
| POST | `/api/shop/assistant` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/shop/catalog` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/shop/orders` | 登录；资源归属限制见接口说明 | 201 |
| POST | `/api/shop/quote` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/tickets` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/tickets` | 登录；资源归属限制见接口说明 | 201 |
| DELETE | `/api/tickets/{ticket_id}` | 登录；资源归属限制见接口说明 | 204 |
| GET | `/api/tickets/{ticket_id}` | 登录；资源归属限制见接口说明 | 200 |
| PUT | `/api/tickets/{ticket_id}` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/tickets/{ticket_id}/reply` | 管理员 | 200 |
| GET | `/api/upload/health` | 公开；业务凭据要求见接口说明 | 200 |
| PUT | `/api/upload/{filename}` | X-API-Key（UPLOAD_API_KEY） | 201 |
| GET | `/api/users` | 管理员 | 200 |
| POST | `/api/users/check-exists` | 公开；业务凭据要求见接口说明 | 200 |
| GET | `/api/users/deletion-requests` | 管理员 | 200 |
| DELETE | `/api/users/deletion-requests/{request_id}/account` | 管理员 | 200 |
| GET | `/api/users/me` | 登录；资源归属限制见接口说明 | 200 |
| PATCH | `/api/users/me` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/users/me/change-email` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/users/me/change-password` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/users/me/change-password-simple` | 登录；资源归属限制见接口说明 | 200 |
| DELETE | `/api/users/me/deletion-request` | 登录；资源归属限制见接口说明 | 200 |
| GET | `/api/users/me/deletion-request` | 登录；资源归属限制见接口说明 | 200 |
| POST | `/api/users/me/deletion-request` | 登录；资源归属限制见接口说明 | 202 |
| GET | `/api/users/search` | 管理员 | 200 |
| GET | `/api/users/{user_id}` | 管理员 | 200 |
| PATCH | `/api/users/{user_id}` | 管理员 | 200 |
| DELETE | `/api/users/{user_id}/2fa/totp` | 管理员 | 200 |
| POST | `/api/users/{user_id}/reset-password` | 管理员 | 200 |
| GET | `/oauth/authorize` | 平台 Bearer 或 OAuth Cookie；未登录时 302 跳转登录页 | 200, 302 |
| POST | `/oauth/authorize` | 平台 Bearer 或 OAuth Cookie；未登录时 302 跳转登录页 | 302 |
| DELETE | `/oauth/session` | 公开；业务凭据要求见接口说明 | 200 |
| POST | `/oauth/session` | PlatformBearer | 200 |
| POST | `/oauth/token` | 按客户端类型使用 Basic 或表单凭据；公共客户端无需 secret | 200 |
| GET | `/oauth/userinfo` | OAuthAccessToken | 200 |

## GET /.well-known/jwks.json

JWKS 公钥列表

权限：公开；业务凭据要求见接口说明。

处理器：`app.endpoint.oauth.jwks`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "keys": {
              "items": {
                "properties": {
                  "alg": {
                    "type": "string"
                  },
                  "e": {
                    "type": "string"
                  },
                  "kid": {
                    "type": "string"
                  },
                  "kty": {
                    "type": "string"
                  },
                  "n": {
                    "type": "string"
                  },
                  "use": {
                    "type": "string"
                  }
                },
                "required": [
                  "kty",
                  "use",
                  "kid",
                  "alg",
                  "n",
                  "e"
                ],
                "type": "object"
              },
              "type": "array"
            }
          },
          "required": [
            "keys"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /.well-known/openid-configuration

OIDC Discovery

权限：公开；业务凭据要求见接口说明。

处理器：`app.endpoint.oauth.openid_configuration`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "authorization_endpoint": {
              "type": "string"
            },
            "claim_types_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "claims_parameter_supported": {
              "type": "boolean"
            },
            "claims_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "code_challenge_methods_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "grant_types_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "id_token_signing_alg_values_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "issuer": {
              "type": "string"
            },
            "jwks_uri": {
              "type": "string"
            },
            "request_parameter_supported": {
              "type": "boolean"
            },
            "request_uri_parameter_supported": {
              "type": "boolean"
            },
            "response_modes_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "response_types_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "scopes_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "subject_types_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "token_endpoint": {
              "type": "string"
            },
            "token_endpoint_auth_methods_supported": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "userinfo_endpoint": {
              "type": "string"
            }
          },
          "required": [
            "issuer",
            "authorization_endpoint",
            "token_endpoint",
            "userinfo_endpoint",
            "jwks_uri",
            "response_types_supported",
            "subject_types_supported",
            "id_token_signing_alg_values_supported",
            "scopes_supported",
            "token_endpoint_auth_methods_supported",
            "grant_types_supported",
            "code_challenge_methods_supported",
            "claims_supported",
            "response_modes_supported",
            "claim_types_supported",
            "request_parameter_supported",
            "request_uri_parameter_supported",
            "claims_parameter_supported"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/

Api Root

权限：公开；业务凭据要求见接口说明。

处理器：`app.endpoint.root_router.api_root`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": {
            "type": "string"
          },
          "title": "Response Api Root Api  Get",
          "type": "object"
        }
      }
    },
    "description": "Successful Response"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/2fa/totp/confirm

确认启用 TOTP 并生成一次性恢复码

权限：登录；资源归属限制见接口说明。

限流：`5/minute`，按客户端 IP。

处理器：`app.endpoint.two_factor.confirm_totp`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TotpConfirmRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/RecoveryCodesResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/2fa/totp/disable

关闭 TOTP 二次验证

权限：登录；资源归属限制见接口说明。

限流：`5/minute`，按客户端 IP。

处理器：`app.endpoint.two_factor.disable_totp`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TotpCodeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TwoFactorActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/2fa/totp/recovery-codes/regenerate

重新生成一次性恢复码

权限：登录；资源归属限制见接口说明。

限流：`5/minute`，按客户端 IP。

处理器：`app.endpoint.two_factor.regenerate_recovery_codes`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TotpCodeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/RecoveryCodesResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/2fa/totp/setup

开始设置 TOTP

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.two_factor.setup_totp`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TotpSetupResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/2fa/totp/status

获取 TOTP 状态

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.two_factor.get_totp_status`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TotpStatusResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/2fa/verify

完成登录二次验证

权限：公开；业务凭据要求见接口说明。

限流：`10/minute`，按客户端 IP。

处理器：`app.endpoint.two_factor.verify_login_two_factor`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TwoFactorVerifyRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Token"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/api-keys

管理员查询所有 APIKey

权限：管理员。

处理器：`app.endpoint.access_api_keys.admin_keys`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "user_id",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "User Id"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeyList"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/api-keys

管理员为用户创建 APIKey

权限：管理员。

处理器：`app.endpoint.access_api_keys.create_key`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AccessApiKeyCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeySecret"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/admin/api-keys/{key_id}

管理员删除 APIKey

权限：管理员。

处理器：`app.endpoint.access_api_keys.delete_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "key_id",
    "required": true,
    "schema": {
      "title": "Key Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/api-keys/{key_id}

管理员查看 APIKey 密钥

权限：管理员。

处理器：`app.endpoint.access_api_keys.admin_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "key_id",
    "required": true,
    "schema": {
      "title": "Key Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeySecret"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PATCH /api/admin/api-keys/{key_id}

管理员修改 APIKey 名称或启用状态

权限：管理员。

处理器：`app.endpoint.access_api_keys.update_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "key_id",
    "required": true,
    "schema": {
      "title": "Key Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AccessApiKeyUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeyResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/api-keys/{key_id}/rotate

管理员重置 APIKey，旧密钥立即失效

权限：管理员。

处理器：`app.endpoint.access_api_keys.rotate_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "key_id",
    "required": true,
    "schema": {
      "title": "Key Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeySecret"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/data-export

Download Export

权限：超级管理员。

处理器：`app.endpoint.data_export.download_export`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ExportRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "complete": {
              "const": true
            },
            "completed_at": {
              "type": "string"
            },
            "counts": {
              "additionalProperties": {
                "type": "integer"
              },
              "type": "object"
            },
            "data": {
              "additionalProperties": {
                "items": {
                  "additionalProperties": true,
                  "description": "MongoDB Canonical Extended JSON v2 原始文档，见 data-export-fields.md",
                  "type": "object"
                },
                "type": "array"
              },
              "type": "object"
            },
            "metadata": {
              "properties": {
                "consistency": {
                  "const": "live_non_snapshot"
                },
                "encoding": {
                  "type": "string"
                },
                "exported_by": {
                  "type": "string"
                },
                "format_version": {
                  "type": "string"
                },
                "selected_datasets": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "started_at": {
                  "type": "string"
                }
              },
              "required": [
                "format_version",
                "encoding",
                "started_at",
                "exported_by",
                "selected_datasets",
                "consistency"
              ],
              "type": "object"
            }
          },
          "required": [
            "metadata",
            "data",
            "counts",
            "completed_at",
            "complete"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/HTTPValidationError"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "输入校验失败或业务字段组合不合法"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/data-export/catalog

Get Catalog

权限：超级管理员。

处理器：`app.endpoint.data_export.get_catalog`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "datasets": {
              "items": {
                "properties": {
                  "collections": {
                    "items": {
                      "type": "string"
                    },
                    "type": "array"
                  },
                  "group": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "label": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "label",
                  "group",
                  "collections"
                ],
                "type": "object"
              },
              "type": "array"
            }
          },
          "required": [
            "datasets"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/data-export/documentation

Get Documentation

权限：超级管理员。

处理器：`app.endpoint.data_export.get_documentation`。

### 响应

```json
{
  "200": {
    "content": {
      "text/markdown": {
        "schema": {
          "format": "binary",
          "type": "string"
        }
      }
    },
    "description": "字段文档附件",
    "headers": {
      "Content-Disposition": {
        "schema": {
          "type": "string"
        }
      }
    }
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/system-keys

列出系统密钥

权限：管理员。

处理器：`app.endpoint.system_keys.list_system_keys`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "purpose",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/SystemKeyPurpose"
        },
        {
          "type": "null"
        }
      ],
      "title": "Purpose"
    }
  },
  {
    "in": "query",
    "name": "status",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/SystemKeyStatus"
        },
        {
          "type": "null"
        }
      ],
      "title": "Status"
    }
  },
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/system-keys/audit/events

密钥审计记录

权限：管理员。

处理器：`app.endpoint.system_keys.list_system_key_audit_events`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "purpose",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/SystemKeyPurpose"
        },
        {
          "type": "null"
        }
      ],
      "title": "Purpose"
    }
  },
  {
    "in": "query",
    "name": "kid",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Kid"
    }
  },
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyAuditListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/generate

生成待激活系统密钥

权限：管理员。

限流：`10/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.generate_system_key`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SystemKeyGenerateRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/import-oauth

导入已有 OAuth PKCS#8 RSA 私钥

权限：超级管理员。

限流：`3/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.import_oauth_key`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OAuthKeyImportRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/initialize-oauth

初始化并激活首个 OAuth 密钥

权限：管理员。

限流：`5/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.initialize_oauth_key`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OAuthKeyInitializeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/reconcile

检查并修复密钥状态

权限：管理员。

限流：`5/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.reconcile_system_keys`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyReconcileResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/system-keys/status

系统密钥健康状态

权限：管理员。

处理器：`app.endpoint.system_keys.get_system_key_health`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyHealthResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/admin/system-keys/{kid}

删除已停用密钥

权限：管理员。

限流：`5/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.delete_system_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "kid",
    "required": true,
    "schema": {
      "title": "Kid",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/{kid}/activate

激活系统密钥

权限：管理员。

限流：`10/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.activate_system_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "kid",
    "required": true,
    "schema": {
      "title": "Kid",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/{kid}/disable

停用非激活密钥

权限：管理员。

限流：`10/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.disable_system_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "kid",
    "required": true,
    "schema": {
      "title": "Kid",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/admin/system-keys/{kid}/public-key

导出公钥

权限：管理员。

处理器：`app.endpoint.system_keys.get_system_public_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "kid",
    "required": true,
    "schema": {
      "title": "Kid",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemPublicKeyResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/admin/system-keys/{kid}/validate

验证密钥材料

权限：管理员。

限流：`20/minute`，按客户端 IP。

处理器：`app.endpoint.system_keys.validate_system_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "kid",
    "required": true,
    "schema": {
      "title": "Kid",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SystemKeyActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/agents/activate

Activate

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.agents.activate`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "created_at": {
              "format": "date-time",
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "level": {
              "type": "integer"
            },
            "rate_bps": {
              "type": "integer"
            },
            "revision": {
              "type": "integer"
            },
            "user_id": {
              "type": "string"
            }
          },
          "required": [
            "user_id",
            "email",
            "code",
            "level",
            "rate_bps",
            "revision",
            "created_at"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/agents/admin/accounts

Accounts

权限：管理员。

处理器：`app.endpoint.agents.accounts`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "search",
    "required": false,
    "schema": {
      "default": "",
      "maxLength": 100,
      "title": "Search",
      "type": "string"
    }
  },
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "items": {
              "items": {
                "properties": {
                  "code": {
                    "type": "string"
                  },
                  "created_at": {
                    "format": "date-time",
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "level": {
                    "type": "integer"
                  },
                  "rate_bps": {
                    "type": "integer"
                  },
                  "revision": {
                    "type": "integer"
                  },
                  "user_id": {
                    "type": "string"
                  }
                },
                "required": [
                  "user_id",
                  "email",
                  "code",
                  "level",
                  "rate_bps",
                  "revision",
                  "created_at"
                ],
                "type": "object"
              },
              "type": "array"
            },
            "total": {
              "type": "integer"
            }
          },
          "required": [
            "total",
            "items"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/agents/admin/accounts/{user_id}

Update Account

权限：管理员。

处理器：`app.endpoint.agents.update_account`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "user_id",
    "required": true,
    "schema": {
      "title": "User Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AgentUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "code": {
                  "type": "string"
                },
                "created_at": {
                  "format": "date-time",
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "level": {
                  "type": "integer"
                },
                "rate_bps": {
                  "type": "integer"
                },
                "revision": {
                  "type": "integer"
                },
                "user_id": {
                  "type": "string"
                }
              },
              "required": [
                "user_id",
                "email",
                "code",
                "level",
                "rate_bps",
                "revision",
                "created_at"
              ],
              "type": "object"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/agents/admin/commissions

All Commissions

权限：管理员。

处理器：`app.endpoint.agents.all_commissions`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "state",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "enum": [
            "pending",
            "confirmed",
            "invalid",
            "settled"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "State"
    }
  },
  {
    "in": "query",
    "name": "agent_id",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Id"
    }
  },
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "items": {
              "items": {
                "properties": {
                  "agent_id": {
                    "type": "string"
                  },
                  "amount": {
                    "type": "integer"
                  },
                  "buyer_email": {
                    "type": "string"
                  },
                  "code": {
                    "type": "string"
                  },
                  "created_at": {
                    "format": "date-time",
                    "type": "string"
                  },
                  "deleted": {
                    "type": "boolean"
                  },
                  "history": {
                    "items": {
                      "properties": {
                        "actor_id": {
                          "title": "Actor Id",
                          "type": "string"
                        },
                        "at": {
                          "format": "date-time",
                          "title": "At",
                          "type": "string"
                        },
                        "note": {
                          "title": "Note",
                          "type": "string"
                        },
                        "status": {
                          "enum": [
                            "pending",
                            "confirmed",
                            "invalid",
                            "settled"
                          ],
                          "title": "Status",
                          "type": "string"
                        }
                      },
                      "required": [
                        "status",
                        "actor_id",
                        "note"
                      ],
                      "title": "CommissionEvent",
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "order_id": {
                    "type": "string"
                  },
                  "rate_bps": {
                    "type": "integer"
                  },
                  "status": {
                    "enum": [
                      "pending",
                      "confirmed",
                      "invalid",
                      "settled"
                    ],
                    "type": "string"
                  },
                  "subtotal": {
                    "type": "integer"
                  },
                  "total": {
                    "type": "integer"
                  }
                },
                "required": [
                  "order_id",
                  "created_at",
                  "deleted",
                  "subtotal",
                  "total",
                  "code",
                  "rate_bps",
                  "agent_id",
                  "amount",
                  "status",
                  "history",
                  "buyer_email"
                ],
                "type": "object"
              },
              "type": "array"
            },
            "total": {
              "type": "integer"
            },
            "totals": {
              "properties": {
                "confirmed": {
                  "type": "integer"
                },
                "invalid": {
                  "type": "integer"
                },
                "pending": {
                  "type": "integer"
                },
                "settled": {
                  "type": "integer"
                }
              },
              "required": [
                "pending",
                "confirmed",
                "invalid",
                "settled"
              ],
              "type": "object"
            }
          },
          "required": [
            "items",
            "total",
            "totals"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/agents/admin/commissions/{order_id}

Change Commission

权限：管理员。

处理器：`app.endpoint.agents.change_commission`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "order_id",
    "required": true,
    "schema": {
      "$ref": "#/components/schemas/PydanticObjectId"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CommissionUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/HTTPValidationError"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "输入校验失败或业务字段组合不合法"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/agents/commissions

My Commissions

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.agents.my_commissions`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "state",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "enum": [
            "pending",
            "confirmed",
            "invalid",
            "settled"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "State"
    }
  },
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "items": {
              "items": {
                "properties": {
                  "agent_id": {
                    "type": "string"
                  },
                  "amount": {
                    "type": "integer"
                  },
                  "code": {
                    "type": "string"
                  },
                  "created_at": {
                    "format": "date-time",
                    "type": "string"
                  },
                  "deleted": {
                    "type": "boolean"
                  },
                  "history": {
                    "items": {
                      "properties": {
                        "actor_id": {
                          "title": "Actor Id",
                          "type": "string"
                        },
                        "at": {
                          "format": "date-time",
                          "title": "At",
                          "type": "string"
                        },
                        "note": {
                          "title": "Note",
                          "type": "string"
                        },
                        "status": {
                          "enum": [
                            "pending",
                            "confirmed",
                            "invalid",
                            "settled"
                          ],
                          "title": "Status",
                          "type": "string"
                        }
                      },
                      "required": [
                        "status",
                        "actor_id",
                        "note"
                      ],
                      "title": "CommissionEvent",
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "order_id": {
                    "type": "string"
                  },
                  "rate_bps": {
                    "type": "integer"
                  },
                  "status": {
                    "enum": [
                      "pending",
                      "confirmed",
                      "invalid",
                      "settled"
                    ],
                    "type": "string"
                  },
                  "subtotal": {
                    "type": "integer"
                  },
                  "total": {
                    "type": "integer"
                  }
                },
                "required": [
                  "order_id",
                  "created_at",
                  "deleted",
                  "subtotal",
                  "total",
                  "code",
                  "rate_bps",
                  "agent_id",
                  "amount",
                  "status",
                  "history"
                ],
                "type": "object"
              },
              "type": "array"
            },
            "total": {
              "type": "integer"
            },
            "totals": {
              "properties": {
                "confirmed": {
                  "type": "integer"
                },
                "invalid": {
                  "type": "integer"
                },
                "pending": {
                  "type": "integer"
                },
                "settled": {
                  "type": "integer"
                }
              },
              "required": [
                "pending",
                "confirmed",
                "invalid",
                "settled"
              ],
              "type": "object"
            }
          },
          "required": [
            "items",
            "total",
            "totals"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/agents/me

Me

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.agents.me`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "code": {
                  "type": "string"
                },
                "created_at": {
                  "format": "date-time",
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "level": {
                  "type": "integer"
                },
                "rate_bps": {
                  "type": "integer"
                },
                "revision": {
                  "type": "integer"
                },
                "user_id": {
                  "type": "string"
                }
              },
              "required": [
                "user_id",
                "email",
                "code",
                "level",
                "rate_bps",
                "revision",
                "created_at"
              ],
              "type": "object"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/api-keys

只读查看自己的 APIKey

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.access_api_keys.my_keys`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeyList"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/api-keys/{key_id}

查看自己的 APIKey 密钥

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.access_api_keys.my_key`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "key_id",
    "required": true,
    "schema": {
      "title": "Key Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccessApiKeySecret"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/application-key/create

创建应用密钥

权限：登录；资源归属限制见接口说明。

创建新的应用密钥

每个用户只能创建一个应用密钥，创建后无法删除只能轮转

处理器：`app.endpoint.api_key.create_application_key`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "application_key": {
              "properties": {
                "created_at": {
                  "format": "date-time",
                  "type": "string"
                },
                "id": {
                  "type": "string"
                },
                "is_active": {
                  "type": "boolean"
                },
                "key": {
                  "type": "string"
                },
                "key_preview": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "is_active",
                "key_preview",
                "key",
                "created_at"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "application_key"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/application-key/info

获取我的应用密钥信息

权限：登录；资源归属限制见接口说明。

获取当前用户的应用密钥信息

处理器：`app.endpoint.api_key.get_my_application_key`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "has_key": {
                  "const": false
                },
                "message": {
                  "type": "string"
                }
              },
              "required": [
                "has_key",
                "message"
              ],
              "type": "object"
            },
            {
              "properties": {
                "application_key": {
                  "properties": {
                    "created_at": {
                      "format": "date-time",
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "is_active": {
                      "type": "boolean"
                    },
                    "key_preview": {
                      "type": "string"
                    },
                    "last_used_at": {
                      "anyOf": [
                        {
                          "format": "date-time",
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "updated_at": {
                      "anyOf": [
                        {
                          "format": "date-time",
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "is_active",
                    "key_preview",
                    "last_used_at",
                    "created_at",
                    "updated_at"
                  ],
                  "type": "object"
                },
                "has_key": {
                  "const": true
                }
              },
              "required": [
                "has_key",
                "application_key"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/application-key/rotate

轮转应用密钥

权限：登录；资源归属限制见接口说明。

轮转应用密钥，生成新的密钥值

处理器：`app.endpoint.api_key.rotate_application_key`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "application_key": {
              "properties": {
                "id": {
                  "type": "string"
                },
                "is_active": {
                  "type": "boolean"
                },
                "key": {
                  "type": "string"
                },
                "key_preview": {
                  "type": "string"
                },
                "updated_at": {
                  "anyOf": [
                    {
                      "format": "date-time",
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ]
                }
              },
              "required": [
                "id",
                "is_active",
                "key_preview",
                "key",
                "updated_at"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "application_key"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/application-key/status

启用/禁用应用密钥

权限：登录；资源归属限制见接口说明。

启用或禁用应用密钥

- **is_active**: true启用，false禁用

处理器：`app.endpoint.api_key.toggle_application_key_status`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/ApiKeyToggleStatus"
          },
          {
            "type": "boolean"
          }
        ],
        "description": "状态对象；兼容旧版布尔值请求体",
        "title": "Payload"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "application_key": {
              "properties": {
                "id": {
                  "type": "string"
                },
                "is_active": {
                  "type": "boolean"
                },
                "updated_at": {
                  "anyOf": [
                    {
                      "format": "date-time",
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ]
                }
              },
              "required": [
                "id",
                "is_active",
                "updated_at"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "application_key"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/application-key/validate

验证应用密钥并获取用户信息

权限：公开；业务凭据要求见接口说明。

验证应用密钥并返回用户信息

此端点用于应用密钥认证，返回用户信息用于OAuth token生成

处理器：`app.endpoint.api_key.validate_application_key`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ApiKeyValidationRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "user": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "full_name": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ]
                },
                "id": {
                  "type": "string"
                },
                "is_active": {
                  "type": "boolean"
                }
              },
              "required": [
                "id",
                "email",
                "full_name",
                "is_active"
              ],
              "type": "object"
            }
          },
          "required": [
            "user"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/admin/change-password

管理员修改用户密码

权限：管理员。

管理员修改任意用户密码（仅管理员可用）

- **email**: 要修改密码的用户邮箱
- **new_password**: 新密码（至少8位）

需要管理员权限

处理器：`app.endpoint.auth.admin_change_user_password`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AdminChangePasswordRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AdminChangePasswordResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/change-phone-number

修改手机号码

权限：登录；资源归属限制见接口说明。

修改手机号码（需要登录状态）

- **new_phone_number**: 新手机号码（11位）
- **verification_code**: 短信验证码（6位数字）

处理器：`app.endpoint.auth.change_phone_number`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ChangePhoneNumberRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ChangePhoneNumberResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/login

用户登录（JSON格式）

权限：公开；业务凭据要求见接口说明。

限流：`10/minute`，按客户端 IP。

用户登录（JSON格式）

**适用于直接API调用**

- **email**: 邮箱地址
- **password**: 密码

未启用 TOTP 返回 JWT；已启用时返回 requires_2fa/challenge_token，需调用 /api/2fa/verify。

注意：此接口接收JSON数据（application/json）

处理器：`app.endpoint.auth.login`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UserLogin"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/Token"
            },
            {
              "$ref": "#/components/schemas/TwoFactorChallengeResponse"
            }
          ],
          "title": "Response Login Api Auth Login Post"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/login-by-sms

短信登录

权限：公开；业务凭据要求见接口说明。

限流：`10/minute`，按客户端 IP。

短信登录

- **phone_number**: 手机号码（11位）
- **verification_code**: 短信验证码（6位数字）

处理器：`app.endpoint.auth.login_by_sms`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SMSLoginRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/Token"
            },
            {
              "$ref": "#/components/schemas/TwoFactorChallengeResponse"
            }
          ],
          "title": "Response Login By Sms Api Auth Login By Sms Post"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/auth/me

获取当前用户信息

权限：登录；资源归属限制见接口说明。

获取当前登录用户信息

需要Bearer Token认证

处理器：`app.endpoint.auth.get_current_user_info`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/oauth/callback

OAuth 授权码模式回调处理

权限：公开；业务凭据要求见接口说明。

处理授权码回调，向授权服务器换取令牌并建立本地会话

处理器：`app.endpoint.auth.oauth_callback`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OAuthCallbackRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/OAuthCallbackResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/register

用户注册

权限：公开；业务凭据要求见接口说明。

限流：`5/hour`，按客户端 IP。

用户注册

- **email**: 邮箱地址
- **password**: 密码（至少8位）
- **verification_code**: 邮箱验证码（6位数字）

处理器：`app.endpoint.auth.register`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UserRegister"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/reset-password-by-email

邮箱重置密码

权限：公开；业务凭据要求见接口说明。

限流：`5/hour`，按客户端 IP。

通过邮箱验证码重置密码

- **email**: 邮箱地址
- **verification_code**: 邮箱验证码（6位数字）
- **new_password**: 新密码（8-128位）

处理器：`app.endpoint.auth.reset_password_by_email`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/EmailResetPasswordRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/EmailResetPasswordResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/reset-password-by-sms

短信重置密码

权限：公开；业务凭据要求见接口说明。

限流：`5/hour`，按客户端 IP。

通过短信验证码重置密码

- **phone_number**: 手机号码（11位）
- **verification_code**: 短信验证码（6位数字）
- **new_password**: 新密码（8-128位）

处理器：`app.endpoint.auth.reset_password_by_sms`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SMSResetPasswordRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SMSResetPasswordResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/send-code

发送邮箱验证码

权限：公开；业务凭据要求见接口说明。

限流：`3/minute`，按客户端 IP。

发送邮箱验证码

- **email**: 邮箱地址

处理器：`app.endpoint.auth.send_verification_code`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SendVerificationCodeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SendVerificationCodeResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/send-sms-code

发送短信验证码

权限：公开；业务凭据要求见接口说明。

限流：`3/minute`，按客户端 IP。

发送短信验证码

- **phone_number**: 手机号码（11位）

处理器：`app.endpoint.auth.send_sms_code`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SendSMSCodeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SendSMSCodeResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/auth/token

OAuth2标准登录（Swagger认证使用）

权限：公开；业务凭据要求见接口说明。

限流：`10/minute`，按客户端 IP。

OAuth2标准密码流登录（符合OAuth2规范）

**Swagger UI认证请使用此接口**

- **username**: 邮箱地址（OAuth2标准使用username字段，但我们接受邮箱）
- **password**: 密码

返回JWT访问令牌

注意：此接口接收表单数据（application/x-www-form-urlencoded），不是JSON

处理器：`app.endpoint.auth.login_for_access_token`。

### 请求体

```json
{
  "content": {
    "application/x-www-form-urlencoded": {
      "schema": {
        "$ref": "#/components/schemas/Body_login_for_access_token_api_auth_token_post"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Token"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/blobs/downloads/{grant_id}

使用短期授权下载 MongoDB GridFS 文件

权限：短期授权 URL 中的 token。

处理器：`app.endpoint.blobs.download_blob`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "grant_id",
    "required": true,
    "schema": {
      "title": "Grant Id",
      "type": "string"
    }
  },
  {
    "in": "query",
    "name": "token",
    "required": true,
    "schema": {
      "maxLength": 256,
      "minLength": 32,
      "title": "Token",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/octet-stream": {
        "schema": {
          "format": "binary",
          "type": "string"
        }
      }
    },
    "description": "文件流；下载 MIME 取决于文件元数据",
    "headers": {
      "Content-Disposition": {
        "schema": {
          "type": "string"
        }
      }
    }
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/blobs/uploads/{grant_id}

使用短期授权上传到 MongoDB GridFS

权限：短期授权 URL 中的 token。

处理器：`app.endpoint.blobs.upload_blob`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "grant_id",
    "required": true,
    "schema": {
      "title": "Grant Id",
      "type": "string"
    }
  },
  {
    "in": "query",
    "name": "token",
    "required": true,
    "schema": {
      "maxLength": 256,
      "minLength": 32,
      "title": "Token",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/octet-stream": {
      "schema": {
        "format": "binary",
        "type": "string"
      }
    }
  },
  "description": "原始文件字节，不使用 multipart/form-data",
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            },
            "sha256": {
              "type": "string"
            },
            "size": {
              "type": "integer"
            },
            "storage_key": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "storage_key",
            "size",
            "sha256"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/business-accounts

获取业务账号列表（管理员）

权限：管理员。

管理员获取业务账号列表，支持按状态过滤和分页。

处理器：`app.endpoint.business_accounts.list_business_accounts`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 10,
      "description": "返回的记录数",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按状态过滤",
    "in": "query",
    "name": "status_filter",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/BusinessAccountStatus"
        },
        {
          "type": "null"
        }
      ],
      "description": "按状态过滤",
      "title": "Status Filter"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/BusinessAccountListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/business-accounts/me

获取当前用户的业务账号

权限：登录；资源归属限制见接口说明。

获取当前登录用户的业务账号。如未申请或未创建，将返回 404。

处理器：`app.endpoint.business_accounts.get_my_business_account`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/BusinessAccountResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PATCH /api/business-accounts/me

更新当前用户的业务账号资料

权限：登录；资源归属限制见接口说明。

更新当前登录用户业务账号中可编辑字段：
- 公司抬头
- 税号
- 认证信息
- 通信地址

处理器：`app.endpoint.business_accounts.update_my_business_account`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/BusinessAccountUpdateRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/BusinessAccountResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/business-accounts/me/apply

申请创建业务账号

权限：登录；资源归属限制见接口说明。

申请创建业务账号。

- 如果当前用户尚无业务账号，则创建一条 `pending` 状态的记录
- 如果已存在申请或已激活账号，将返回错误提示

处理器：`app.endpoint.business_accounts.apply_business_account`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/BusinessAccountApplyRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/BusinessAccountResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/business-accounts/{account_id}

管理员删除业务账号

权限：管理员。

删除业务账号；主要用于处理账号注销申请前的人工资源清理。

处理器：`app.endpoint.business_accounts.admin_delete_business_account`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "account_id",
    "required": true,
    "schema": {
      "title": "Account Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/business-accounts/{account_id}

获取业务账号详情

权限：登录；资源归属限制见接口说明。

获取业务账号详情。

- 管理员可以查看任意业务账号
- 普通用户只能查看自己的业务账号

处理器：`app.endpoint.business_accounts.get_business_account`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "account_id",
    "required": true,
    "schema": {
      "title": "Account Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/BusinessAccountResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/business-accounts/{account_id}

管理员更新业务账号

权限：管理员。

管理员更新业务账号信息，包括：

- 分配专属邮箱
- 设置用户识别码
- 调整账号状态
- 修改业务信息字段

处理器：`app.endpoint.business_accounts.admin_update_business_account`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "account_id",
    "required": true,
    "schema": {
      "title": "Account Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/BusinessAccountAdminUpdateRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/BusinessAccountResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/email/send-common

发送通用邮件

权限：X-API-Key（UPLOAD_API_KEY）。

发送通用邮件（使用common.html模板）

需要在请求头中提供 X-API-Key 进行身份验证

- **title**: 邮件标题
- **content**: 邮件内容
- **message_id**: 消息ID
- **recipients**: 收件人列表（邮箱地址数组）

注意：sendTime 由系统自动生成（上海时区的当前发送时间），无需在请求中提供。

Example:
    ```json
    {
        "title": "系统通知",
        "content": "这是一条测试消息",
        "message_id": "msg-123456",
        "recipients": ["user@example.com", "admin@example.com"]
    }
    ```

处理器：`app.endpoint.email.send_common_email`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "header",
    "name": "x-api-key",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "X-Api-Key"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SendCommonEmailRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/SendCommonEmailResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/oauth/clients/

获取 OAuth 客户端列表

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.oauth_clients.list_oauth_clients`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "description": "返回的记录数",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "mine 查看自己的客户端，all（仅管理员）查看全部",
    "in": "query",
    "name": "scope",
    "required": false,
    "schema": {
      "default": "mine",
      "description": "mine 查看自己的客户端，all（仅管理员）查看全部",
      "enum": [
        "mine",
        "all"
      ],
      "title": "Scope",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/OAuthClientListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/oauth/clients/

创建 OAuth 客户端

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.oauth_clients.create_oauth_client`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OAuthClientCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/OAuthClientRead"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/oauth/clients/{client_id}

删除 OAuth 客户端

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.oauth_clients.delete_oauth_client`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "client_id",
    "required": true,
    "schema": {
      "title": "Client Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/oauth/clients/{client_id}

更新 OAuth 客户端

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.oauth_clients.update_oauth_client`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "client_id",
    "required": true,
    "schema": {
      "title": "Client Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OAuthClientUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/OAuthClientRead"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/owa/info

获取联系表单列表（管理员）

权限：管理员。

获取联系表单列表（仅管理员）

- 支持分页和状态过滤
- 按创建时间倒序排列

处理器：`app.endpoint.contacts.list_contacts`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 10,
      "description": "返回的记录数",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按处理状态过滤",
    "in": "query",
    "name": "is_processed",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "按处理状态过滤",
      "title": "Is Processed"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ContactListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/owa/info

提交联系我们表单

权限：公开；业务凭据要求见接口说明。

限流：`5/minute`，按客户端 IP。

提交联系我们表单（公开接口，需要 Cloudflare Turnstile 验证）

- **name**: 称呼
- **email**: 有效邮箱地址
- **message**: 消息内容
- **turnstileToken**: Cloudflare Turnstile 验证令牌

注意：提交后会自动发送通知邮件给管理员。

处理器：`app.endpoint.contacts.create_contact`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ContactCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ContactResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/owa/info/{contact_id}

删除联系表单（管理员）

权限：管理员。

删除联系表单（仅管理员）

处理器：`app.endpoint.contacts.delete_contact`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "contact_id",
    "required": true,
    "schema": {
      "title": "Contact Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/owa/info/{contact_id}

获取联系表单详情（管理员）

权限：管理员。

获取联系表单详情（仅管理员）

处理器：`app.endpoint.contacts.get_contact`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "contact_id",
    "required": true,
    "schema": {
      "title": "Contact Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ContactResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/owa/info/{contact_id}

更新联系表单（管理员）

权限：管理员。

更新联系表单（仅管理员）

- **is_processed**: 是否已处理（可选）
- **admin_notes**: 管理员备注（可选）

处理器：`app.endpoint.contacts.update_contact`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "contact_id",
    "required": true,
    "schema": {
      "title": "Contact Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ContactUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ContactResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/passkey/authenticate

通行密钥认证

权限：公开；业务凭据要求见接口说明。

限流：`10/minute`，按客户端 IP。

使用通行密钥进行认证

返回JWT访问令牌

处理器：`app.endpoint.passkey.authenticate_passkey`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/Body_authenticate_passkey_api_passkey_authenticate_post"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "access_token": {
              "type": "string"
            },
            "expires_in": {
              "type": "integer"
            },
            "token_type": {
              "type": "string"
            },
            "user": {
              "description": "用户响应Schema",
              "properties": {
                "avatar_url": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "default": null,
                  "description": "头像URL",
                  "title": "Avatar Url"
                },
                "bio": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "default": null,
                  "description": "个人简介",
                  "title": "Bio"
                },
                "created_at": {
                  "description": "创建时间",
                  "format": "date-time",
                  "title": "Created At",
                  "type": "string"
                },
                "email": {
                  "description": "用户邮箱",
                  "format": "email",
                  "title": "Email",
                  "type": "string"
                },
                "full_name": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "default": null,
                  "description": "用户姓名",
                  "title": "Full Name"
                },
                "groups": {
                  "description": "用户所属的组（用于 OIDC groups claim，如下游应用的权限映射）",
                  "items": {
                    "type": "string"
                  },
                  "title": "Groups",
                  "type": "array"
                },
                "id": {
                  "description": "用户ID",
                  "title": "Id",
                  "type": "string"
                },
                "is_active": {
                  "description": "账号状态",
                  "title": "Is Active",
                  "type": "boolean"
                },
                "is_super_admin": {
                  "default": false,
                  "description": "是否为超级管理员",
                  "title": "Is Super Admin",
                  "type": "boolean"
                },
                "passkey_enabled": {
                  "default": false,
                  "description": "是否启用通行密钥登录",
                  "title": "Passkey Enabled",
                  "type": "boolean"
                },
                "phone_number": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "default": null,
                  "description": "联系方式",
                  "title": "Phone Number"
                },
                "role": {
                  "$ref": "#/components/schemas/UserRole",
                  "description": "用户角色"
                },
                "two_factor_enabled": {
                  "default": false,
                  "description": "是否启用 TOTP 二次验证",
                  "title": "Two Factor Enabled",
                  "type": "boolean"
                },
                "updated_at": {
                  "anyOf": [
                    {
                      "format": "date-time",
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "default": null,
                  "description": "更新时间",
                  "title": "Updated At"
                }
              },
              "required": [
                "email",
                "id",
                "role",
                "is_active",
                "created_at"
              ],
              "title": "UserResponse",
              "type": "object"
            }
          },
          "required": [
            "access_token",
            "token_type",
            "expires_in",
            "user"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "账号不可用或无权执行操作"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "429": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "error": {
              "type": "string"
            }
          },
          "required": [
            "error"
          ],
          "type": "object"
        }
      }
    },
    "description": "按客户端 IP 限流"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/passkey/authentication-options

获取通行密钥认证选项

权限：公开；业务凭据要求见接口说明。

获取通行密钥认证选项

此端点用于通行密钥登录，不需要认证。
返回通用选项，允许浏览器提示用户选择已注册的通行密钥。

处理器：`app.endpoint.passkey.get_authentication_options`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "options": {
              "properties": {
                "allowCredentials": {
                  "items": {
                    "properties": {
                      "id": {
                        "type": "string"
                      },
                      "type": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "type"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "challenge": {
                  "type": "string"
                },
                "rpId": {
                  "type": "string"
                },
                "timeout": {
                  "type": "integer"
                },
                "userVerification": {
                  "type": "string"
                }
              },
              "required": [
                "challenge",
                "timeout",
                "rpId",
                "allowCredentials",
                "userVerification"
              ],
              "type": "object"
            },
            "session_id": {
              "type": "string"
            }
          },
          "required": [
            "options",
            "session_id"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/passkey/credentials

获取我的通行密钥列表

权限：登录；资源归属限制见接口说明。

获取当前用户的所有通行密钥

处理器：`app.endpoint.passkey.get_my_credentials`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "items": {
            "properties": {
              "created_at": {
                "format": "date-time",
                "type": "string"
              },
              "credential_id": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "is_primary": {
                "type": "boolean"
              },
              "last_used_at": {
                "anyOf": [
                  {
                    "format": "date-time",
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "nickname": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "sign_count": {
                "type": "integer"
              }
            },
            "required": [
              "id",
              "credential_id",
              "nickname",
              "is_primary",
              "sign_count",
              "last_used_at",
              "created_at"
            ],
            "type": "object"
          },
          "type": "array"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/passkey/credentials/{credential_id}

删除通行密钥

权限：登录；资源归属限制见接口说明。

删除指定的通行密钥

- **credential_id**: 通行密钥ID

处理器：`app.endpoint.passkey.delete_credential`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "credential_id",
    "required": true,
    "schema": {
      "title": "Credential Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/passkey/credentials/{credential_id}/nickname

更新通行密钥昵称

权限：登录；资源归属限制见接口说明。

更新指定通行密钥的昵称

- **credential_id**: 通行密钥ID
- **nickname**: 新的昵称

处理器：`app.endpoint.passkey.update_credential_nickname`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "credential_id",
    "required": true,
    "schema": {
      "title": "Credential Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/PasskeyNicknameUpdate"
          },
          {
            "type": "string"
          }
        ],
        "description": "新昵称；兼容旧版字符串请求体",
        "title": "Payload"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "credential": {
              "properties": {
                "id": {
                  "type": "string"
                },
                "nickname": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ]
                }
              },
              "required": [
                "id",
                "nickname"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "credential"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/passkey/credentials/{credential_id}/primary

设置主通行密钥

权限：登录；资源归属限制见接口说明。

设置指定的通行密钥为主通行密钥

- **credential_id**: 通行密钥ID

处理器：`app.endpoint.passkey.set_primary_credential`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "credential_id",
    "required": true,
    "schema": {
      "title": "Credential Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "credential": {
              "properties": {
                "id": {
                  "type": "string"
                },
                "is_primary": {
                  "type": "boolean"
                },
                "nickname": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ]
                }
              },
              "required": [
                "id",
                "nickname",
                "is_primary"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "credential"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/passkey/register

注册通行密钥

权限：登录；资源归属限制见接口说明。

注册新的通行密钥

请求体为WebAuthn凭证数据JSON，需包含 session_id 字段。
可选传入 nickname 字段指定通行密钥昵称。

处理器：`app.endpoint.passkey.register_passkey`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "properties": {
          "id": {
            "type": "string"
          },
          "nickname": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ]
          },
          "rawId": {
            "type": "string"
          },
          "response": {
            "properties": {
              "attestationObject": {
                "type": "string"
              },
              "clientDataJSON": {
                "type": "string"
              }
            },
            "required": [
              "clientDataJSON",
              "attestationObject"
            ],
            "type": "object"
          },
          "session_id": {
            "type": "string"
          },
          "type": {
            "const": "public-key"
          }
        },
        "required": [
          "session_id",
          "id",
          "rawId",
          "type",
          "response"
        ],
        "type": "object"
      }
    }
  },
  "description": "WebAuthn 注册 JSON；二进制字段使用 base64url。由处理器读取并校验。",
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "credential": {
              "properties": {
                "created_at": {
                  "format": "date-time",
                  "type": "string"
                },
                "credential_id": {
                  "type": "string"
                },
                "id": {
                  "type": "string"
                },
                "is_primary": {
                  "type": "boolean"
                },
                "nickname": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "null"
                    }
                  ]
                }
              },
              "required": [
                "id",
                "credential_id",
                "nickname",
                "is_primary",
                "created_at"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "credential"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/passkey/registration-options

获取通行密钥注册选项

权限：登录；资源归属限制见接口说明。

获取通行密钥注册选项

返回WebAuthn凭证创建选项，用于浏览器创建新的通行密钥

处理器：`app.endpoint.passkey.get_registration_options`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "options": {
              "properties": {
                "attestation": {
                  "type": "string"
                },
                "authenticatorSelection": {
                  "properties": {
                    "requireResidentKey": {
                      "type": "boolean"
                    },
                    "residentKey": {
                      "type": "string"
                    },
                    "userVerification": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "challenge": {
                  "type": "string"
                },
                "excludeCredentials": {
                  "items": {
                    "properties": {
                      "id": {
                        "type": "string"
                      },
                      "type": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "type"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "pubKeyCredParams": {
                  "items": {
                    "properties": {
                      "alg": {
                        "type": "integer"
                      },
                      "type": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "type",
                      "alg"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "rp": {
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "name",
                    "id"
                  ],
                  "type": "object"
                },
                "timeout": {
                  "type": "integer"
                },
                "user": {
                  "properties": {
                    "displayName": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "displayName"
                  ],
                  "type": "object"
                }
              },
              "required": [
                "challenge",
                "rp",
                "user",
                "pubKeyCredParams",
                "timeout",
                "excludeCredentials",
                "authenticatorSelection",
                "attestation"
              ],
              "type": "object"
            },
            "session_id": {
              "type": "string"
            }
          },
          "required": [
            "options",
            "session_id"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/passkey/toggle

启用/禁用通行密钥登录

权限：登录；资源归属限制见接口说明。

启用或禁用通行密钥登录

- **enabled**: true启用，false禁用

处理器：`app.endpoint.passkey.toggle_passkey`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/PasskeyToggleRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            },
            "passkey_enabled": {
              "type": "boolean"
            }
          },
          "required": [
            "message",
            "passkey_enabled"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects

获取项目列表（管理员）

权限：管理员。

管理员获取项目列表，可按用户邮箱过滤。

处理器：`app.endpoint.projects.list_projects`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 10,
      "description": "返回的记录数",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按所属用户邮箱过滤",
    "in": "query",
    "name": "owner_email",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按所属用户邮箱过滤",
      "title": "Owner Email"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects

创建项目（管理员）

权限：管理员。

管理员为指定用户创建项目。

处理器：`app.endpoint.projects.create_project`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/projects/files/{file_id}

删除项目文件（管理员）

权限：管理员。

管理员删除项目文件（同时删除 MongoDB GridFS 数据）。

处理器：`app.endpoint.projects.delete_project_file`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "file_id",
    "required": true,
    "schema": {
      "title": "File Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/files/{file_id}

更新项目文件（管理员）

权限：管理员。

管理员更新项目文件（主要是标签和文件名）。

处理器：`app.endpoint.projects.update_project_file`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "file_id",
    "required": true,
    "schema": {
      "title": "File Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectFileUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFileResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects/files/{file_id}/download-url

获取 MongoDB 文件下载授权URL

权限：登录；资源归属限制见接口说明。

获取 MongoDB 中目标文件的短期下载 URL。

- 管理员可以下载任意项目的文件
- 普通用户只能下载自己项目的文件

处理器：`app.endpoint.projects.get_file_download_url`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "file_id",
    "required": true,
    "schema": {
      "title": "File Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFileDownloadUrlResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/projects/finances/{entry_id}

删除项目财务条目

权限：登录；资源归属限制见接口说明。

删除财务条目。

- 管理员可删除任何条目
- 普通用户只能删除自己项目下未核对的条目

处理器：`app.endpoint.projects.delete_finance_entry`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "entry_id",
    "required": true,
    "schema": {
      "title": "Entry Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/finances/{entry_id}

更新项目财务条目

权限：登录；资源归属限制见接口说明。

更新财务条目信息。

- 管理员可修改所有字段
- 普通用户只能修改未核对条目的基础信息，不能修改状态

处理器：`app.endpoint.projects.update_finance_entry`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "entry_id",
    "required": true,
    "schema": {
      "title": "Entry Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectFinanceEntryUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFinanceEntryResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/projects/links/{link_id}

删除项目链接（管理员）

权限：管理员。

管理员删除项目链接。

处理器：`app.endpoint.projects.delete_project_link`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "link_id",
    "required": true,
    "schema": {
      "title": "Link Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/links/{link_id}

更新项目链接（管理员）

权限：管理员。

管理员更新项目链接。

处理器：`app.endpoint.projects.update_project_link`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "link_id",
    "required": true,
    "schema": {
      "title": "Link Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectLinkUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectLinkResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects/me

获取我的项目列表

权限：登录；资源归属限制见接口说明。

普通用户获取自己的项目列表。

处理器：`app.endpoint.projects.list_my_projects`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 10,
      "description": "返回的记录数",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/projects/tasks/{task_id}

删除项目任务（管理员）

权限：管理员。

管理员删除项目任务。

处理器：`app.endpoint.projects.delete_project_task`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "task_id",
    "required": true,
    "schema": {
      "title": "Task Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/tasks/{task_id}

更新项目任务（管理员）

权限：管理员。

管理员更新项目任务（标题、详情或状态）。

处理器：`app.endpoint.projects.update_project_task`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "task_id",
    "required": true,
    "schema": {
      "title": "Task Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectTaskUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectTaskResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/projects/{project_id}

删除项目（管理员）

权限：管理员。

管理员软删除项目并清理文件、链接、任务和财务，保留订单/佣金审计。
已结清佣金的项目不可删除（409）。

处理器：`app.endpoint.projects.delete_project`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects/{project_id}

获取项目详情

权限：登录；资源归属限制见接口说明。

获取项目详情。

- 管理员可以查看任意项目
- 普通用户只能查看自己的项目

处理器：`app.endpoint.projects.get_project`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/{project_id}

更新项目（管理员）

权限：管理员。

管理员更新项目内容或概述。

处理器：`app.endpoint.projects.update_project`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects/{project_id}/files

获取项目文件列表

权限：登录；资源归属限制见接口说明。

获取项目文件列表，支持按文件名和标签筛选。

- 管理员可以查看任意项目的文件
- 普通用户只能查看自己项目的文件

处理器：`app.endpoint.projects.list_project_files`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  },
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "description": "返回的记录数",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按文件名筛选（模糊匹配）",
    "in": "query",
    "name": "filename",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按文件名筛选（模糊匹配）",
      "title": "Filename"
    }
  },
  {
    "description": "按标签筛选（精确匹配）",
    "in": "query",
    "name": "tag",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按标签筛选（精确匹配）",
      "title": "Tag"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFileListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects/{project_id}/files

创建项目文件记录（管理员）

权限：管理员。

管理员创建项目文件记录。

注意：此接口应在 GridFS 上传完成后调用，用于登记文件元数据。

处理器：`app.endpoint.projects.create_project_file`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectFileCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFileResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects/{project_id}/files/upload-url

获取 MongoDB 文件上传授权URL（管理员）

权限：管理员。

管理员获取一次性上传 URL；文件流经 API 并直接写入 MongoDB GridFS，
不写入容器或宿主机文件系统。

处理器：`app.endpoint.projects.get_file_upload_url`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  },
  {
    "description": "文件名",
    "in": "query",
    "name": "filename",
    "required": true,
    "schema": {
      "description": "文件名",
      "title": "Filename",
      "type": "string"
    }
  },
  {
    "description": "文件MIME类型",
    "in": "query",
    "name": "content_type",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "文件MIME类型",
      "title": "Content Type"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFileUploadUrlResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects/{project_id}/finances

获取项目财务条目列表

权限：登录；资源归属限制见接口说明。

获取项目财务条目列表，并返回已核对的收入/支出总和。

处理器：`app.endpoint.projects.list_finance_entries`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  },
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "description": "返回的记录数",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按状态筛选（verified/unverified）",
    "in": "query",
    "name": "status",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按状态筛选（verified/unverified）",
      "title": "Status"
    }
  },
  {
    "description": "按类型筛选（income/expense）",
    "in": "query",
    "name": "entry_type",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按类型筛选（income/expense）",
      "title": "Entry Type"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFinanceEntryListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects/{project_id}/finances

创建项目财务条目

权限：登录；资源归属限制见接口说明。

为项目创建财务条目。

- 管理员可为任何项目创建，并可指定条目状态
- 普通用户只能为自己的项目创建，且条目默认未核对

处理器：`app.endpoint.projects.create_finance_entry`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectFinanceEntryCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectFinanceEntryResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects/{project_id}/links

获取项目链接列表

权限：登录；资源归属限制见接口说明。

获取项目链接列表。

- 管理员可以查看任意项目的链接
- 普通用户只能查看自己项目的链接

处理器：`app.endpoint.projects.list_project_links`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  },
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "description": "返回的记录数",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectLinkListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects/{project_id}/links

创建项目链接（管理员）

权限：管理员。

管理员为项目创建文档链接。

处理器：`app.endpoint.projects.create_project_link`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectLinkCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectLinkResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/{project_id}/rating

设置项目评分

权限：登录；资源归属限制见接口说明。

设置或调整项目评分。

- 管理员和项目所属用户可以调用
- 评分范围为 1-5

处理器：`app.endpoint.projects.update_project_rating`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectRatingUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/projects/{project_id}/responsible-tag

设置项目负责人

权限：登录；资源归属限制见接口说明。

设置项目负责人。

- 管理员和项目所属用户可以调用
- 传入null可清除负责人

处理器：`app.endpoint.projects.update_project_responsible_tag`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectResponsibleTagUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/projects/{project_id}/tasks

获取项目任务列表

权限：登录；资源归属限制见接口说明。

获取项目任务列表，支持按状态筛选。

- 管理员可以查看任意项目的任务
- 普通用户只能查看自己项目的任务

处理器：`app.endpoint.projects.list_project_tasks`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  },
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "description": "返回的记录数",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按状态筛选（pending=未完成, completed=已完成）",
    "in": "query",
    "name": "status",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按状态筛选（pending=未完成, completed=已完成）",
      "title": "Status"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectTaskListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/projects/{project_id}/tasks

创建项目任务（管理员）

权限：管理员。

管理员为项目创建任务。

处理器：`app.endpoint.projects.create_project_task`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "project_id",
    "required": true,
    "schema": {
      "title": "Project Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ProjectTaskCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ProjectTaskResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/responsible-tags

获取负责人列表

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.responsible_tags.list_responsible_tags`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 100,
      "description": "返回的记录数",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "是否包含停用标签（仅管理员可用）",
    "in": "query",
    "name": "include_inactive",
    "required": false,
    "schema": {
      "default": false,
      "description": "是否包含停用标签（仅管理员可用）",
      "title": "Include Inactive",
      "type": "boolean"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ResponsibleTagListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/responsible-tags

创建负责人（管理员）

权限：管理员。

处理器：`app.endpoint.responsible_tags.create_responsible_tag`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ResponsibleTagCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ResponsibleTagResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/responsible-tags/{tag_id}

删除负责人（管理员）

权限：管理员。

处理器：`app.endpoint.responsible_tags.delete_responsible_tag`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "tag_id",
    "required": true,
    "schema": {
      "title": "Tag Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/responsible-tags/{tag_id}

更新负责人（管理员）

权限：管理员。

处理器：`app.endpoint.responsible_tags.update_responsible_tag`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "tag_id",
    "required": true,
    "schema": {
      "title": "Tag Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ResponsibleTagUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ResponsibleTagResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/shop/admin/catalog

Admin Catalog

权限：管理员。

处理器：`app.endpoint.shop.admin_catalog`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/CatalogData"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/shop/admin/catalog

Save Catalog

权限：管理员。

处理器：`app.endpoint.shop.save_catalog`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CatalogData"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/CatalogData"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/shop/assistant

Assistant

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.shop.assistant`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AssistantRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            },
            "selection": {
              "anyOf": [
                {
                  "additionalProperties": false,
                  "properties": {
                    "item_ids": {
                      "items": {
                        "type": "string"
                      },
                      "maxItems": 100,
                      "title": "Item Ids",
                      "type": "array"
                    },
                    "plan": {
                      "default": "popular",
                      "enum": [
                        "custom",
                        "popular"
                      ],
                      "title": "Plan",
                      "type": "string"
                    },
                    "requirements": {
                      "default": "",
                      "maxLength": 1000,
                      "title": "Requirements",
                      "type": "string"
                    }
                  },
                  "title": "Selection",
                  "type": "object"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "message",
            "selection"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/HTTPValidationError"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "输入校验失败或业务字段组合不合法"
  },
  "502": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "上游服务请求或返回数据无效"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/shop/catalog

Catalog

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.shop.catalog`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/CatalogData"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/shop/orders

Create Order

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.shop.create_order`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OrderCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "id": {
              "type": "string"
            },
            "order": {
              "properties": {
                "currency": {
                  "const": "CNY",
                  "default": "CNY",
                  "title": "Currency",
                  "type": "string"
                },
                "discount": {
                  "default": 0,
                  "title": "Discount",
                  "type": "integer"
                },
                "items": {
                  "items": {
                    "$ref": "#/components/schemas/OrderLine"
                  },
                  "title": "Items",
                  "type": "array"
                },
                "plan": {
                  "$ref": "#/components/schemas/ShopPlan"
                },
                "referral": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/ReferralSnapshot"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "default": null
                },
                "requirements": {
                  "title": "Requirements",
                  "type": "string"
                },
                "revision": {
                  "title": "Revision",
                  "type": "integer"
                },
                "subtotal": {
                  "default": 0,
                  "title": "Subtotal",
                  "type": "integer"
                },
                "total": {
                  "title": "Total",
                  "type": "integer"
                }
              },
              "required": [
                "revision",
                "plan",
                "items",
                "total",
                "requirements"
              ],
              "title": "OrderSnapshot",
              "type": "object"
            }
          },
          "required": [
            "id",
            "order"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/HTTPValidationError"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "输入校验失败或业务字段组合不合法"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/shop/quote

Preview Quote

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.shop.preview_quote`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/OrderQuote"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "currency": {
              "const": "CNY",
              "default": "CNY",
              "title": "Currency",
              "type": "string"
            },
            "discount": {
              "default": 0,
              "title": "Discount",
              "type": "integer"
            },
            "items": {
              "items": {
                "$ref": "#/components/schemas/OrderLine"
              },
              "title": "Items",
              "type": "array"
            },
            "plan": {
              "$ref": "#/components/schemas/ShopPlan"
            },
            "referral": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/ReferralSnapshot"
                },
                {
                  "type": "null"
                }
              ],
              "default": null
            },
            "requirements": {
              "title": "Requirements",
              "type": "string"
            },
            "revision": {
              "title": "Revision",
              "type": "integer"
            },
            "subtotal": {
              "default": 0,
              "title": "Subtotal",
              "type": "integer"
            },
            "total": {
              "title": "Total",
              "type": "integer"
            }
          },
          "required": [
            "revision",
            "plan",
            "items",
            "total",
            "requirements"
          ],
          "title": "OrderSnapshot",
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/HTTPValidationError"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "输入校验失败或业务字段组合不合法"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/tickets

获取工单列表

权限：登录；资源归属限制见接口说明。

获取工单列表

- 管理员可以查看所有工单
- 普通用户只能查看自己的工单
- 支持分页和状态过滤

处理器：`app.endpoint.tickets.list_tickets`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过的记录数",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过的记录数",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回的记录数",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 10,
      "description": "返回的记录数",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按状态过滤",
    "in": "query",
    "name": "status_filter",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/TicketStatus"
        },
        {
          "type": "null"
        }
      ],
      "description": "按状态过滤",
      "title": "Status Filter"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TicketListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/tickets

创建工单

权限：登录；资源归属限制见接口说明。

创建工单（客户）

- **title**: 工单标题
- **ticket_type**: 工单类型（financial/technical/business）
- **content**: 工单内容

处理器：`app.endpoint.tickets.create_ticket`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TicketCreate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TicketResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/tickets/{ticket_id}

删除工单

权限：登录；资源归属限制见接口说明。

删除工单

- 创建者可以删除自己的工单
- 管理员可以删除任何工单

处理器：`app.endpoint.tickets.delete_ticket`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "ticket_id",
    "required": true,
    "schema": {
      "title": "Ticket Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "204": {
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/tickets/{ticket_id}

获取工单详情

权限：登录；资源归属限制见接口说明。

获取工单详情

- 管理员可以查看所有工单
- 普通用户只能查看自己的工单

处理器：`app.endpoint.tickets.get_ticket`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "ticket_id",
    "required": true,
    "schema": {
      "title": "Ticket Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TicketResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/tickets/{ticket_id}

更新工单

权限：登录；资源归属限制见接口说明。

更新工单（仅创建者可更新待回复的工单）

- **title**: 工单标题（可选）
- **content**: 工单内容（可选）

处理器：`app.endpoint.tickets.update_ticket`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "ticket_id",
    "required": true,
    "schema": {
      "title": "Ticket Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TicketUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TicketResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/tickets/{ticket_id}/reply

回复工单（管理员）

权限：管理员。

回复工单并标记为已回复（仅管理员）

- **feedback**: 反馈结果

处理器：`app.endpoint.tickets.reply_ticket`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "ticket_id",
    "required": true,
    "schema": {
      "title": "Ticket Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TicketReply"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TicketResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/upload/health

Upload Health

权限：公开；业务凭据要求见接口说明。

检查上传服务健康状态

Returns:
    dict: 服务状态信息

处理器：`app.endpoint.upload.upload_health`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            },
            "mongodb_available": {
              "type": "boolean"
            },
            "service": {
              "type": "string"
            },
            "status": {
              "type": "string"
            },
            "storage": {
              "type": "string"
            }
          },
          "required": [
            "service",
            "status",
            "storage",
            "mongodb_available",
            "message"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            },
            "mongodb_available": {
              "type": "boolean"
            },
            "service": {
              "type": "string"
            },
            "status": {
              "type": "string"
            },
            "storage": {
              "type": "string"
            }
          },
          "required": [
            "service",
            "status",
            "storage",
            "mongodb_available",
            "message"
          ],
          "type": "object"
        }
      }
    },
    "description": "MongoDB 不可用"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PUT /api/upload/{filename}

Upload File

权限：X-API-Key（UPLOAD_API_KEY）。

上传文件到 MongoDB GridFS

需要在请求头中提供 X-API-Key 进行身份验证

Args:
    filename: 目标文件名（1–255 字符，ASCII 字母或数字开头，其余仅字母、数字、点、下划线和连字符；不含路径）
    request: FastAPI请求对象
    x_api_key: API密钥（从请求头获取）

Returns:
    JSONResponse: 上传结果

Example:
    curl --fail --retry 3 -H "X-API-Key: secret123" --upload-file file.tar.gz              http://localhost:8000/api/upload/backup-20241108.tar.gz
    
    或使用 tar 命令直接上传：
    tar -C /path/to/folder -czf - . |         curl --fail --retry 3 -H "X-API-Key: secret123" --upload-file -              http://localhost:8000/api/upload/dir-$(date +%F).tar.gz

处理器：`app.endpoint.upload.upload_file`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "filename",
    "required": true,
    "schema": {
      "title": "Filename",
      "type": "string"
    }
  },
  {
    "in": "header",
    "name": "x-api-key",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "X-Api-Key"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/octet-stream": {
      "schema": {
        "format": "binary",
        "type": "string"
      }
    }
  },
  "description": "原始文件字节，不使用 multipart/form-data",
  "required": true
}
```

### 响应

```json
{
  "201": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "data": {
              "properties": {
                "blob_id": {
                  "type": "string"
                },
                "etag": {
                  "type": "string"
                },
                "filename": {
                  "type": "string"
                },
                "original_filename": {
                  "type": "string"
                },
                "request_id": {
                  "type": "string"
                },
                "storage_key": {
                  "type": "string"
                },
                "success": {
                  "type": "boolean"
                },
                "url": {
                  "type": "string"
                }
              },
              "required": [
                "success",
                "filename",
                "original_filename",
                "url",
                "etag",
                "request_id",
                "blob_id",
                "storage_key"
              ],
              "type": "object"
            },
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message",
            "data"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "413": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "上传内容超过允许的大小"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "500": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "内部处理失败；未捕获异常可能为非 JSON 响应"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用或操作暂时无法完成"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/users

管理员获取用户列表

权限：管理员。

管理员分页获取用户列表

处理器：`app.endpoint.users.list_users`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过数量",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过数量",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回数量",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "description": "返回数量",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "按邮箱关键字模糊查询",
    "in": "query",
    "name": "keyword",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "按邮箱关键字模糊查询",
      "title": "Keyword"
    }
  },
  {
    "description": "角色过滤",
    "in": "query",
    "name": "role",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/UserRole"
        },
        {
          "type": "null"
        }
      ],
      "description": "角色过滤",
      "title": "Role"
    }
  },
  {
    "description": "账号状态过滤",
    "in": "query",
    "name": "is_active",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "账号状态过滤",
      "title": "Is Active"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/users/check-exists

检查用户是否存在

权限：公开；业务凭据要求见接口说明。

检查用户是否已注册（用于忘记密码前的验证）。

处理器：`app.endpoint.users.check_user_exists`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CheckUserExistsRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/CheckUserExistsResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/users/deletion-requests

管理员查看账号注销申请

权限：管理员。

处理器：`app.endpoint.users.list_account_deletion_requests`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "跳过数量",
    "in": "query",
    "name": "skip",
    "required": false,
    "schema": {
      "default": 0,
      "description": "跳过数量",
      "minimum": 0,
      "title": "Skip",
      "type": "integer"
    }
  },
  {
    "description": "返回数量",
    "in": "query",
    "name": "limit",
    "required": false,
    "schema": {
      "default": 20,
      "description": "返回数量",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  {
    "description": "申请状态",
    "in": "query",
    "name": "status",
    "required": false,
    "schema": {
      "$ref": "#/components/schemas/AccountDeletionRequestStatus",
      "default": "pending",
      "description": "申请状态"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccountDeletionRequestListResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/users/deletion-requests/{request_id}/account

管理员执行账号注销

权限：管理员。

处理器：`app.endpoint.users.delete_account_from_request`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "request_id",
    "required": true,
    "schema": {
      "title": "Request Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/users/me

获取当前用户信息（新版）

权限：登录；资源归属限制见接口说明。

获取当前登录用户的完整信息。

处理器：`app.endpoint.users.get_me`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PATCH /api/users/me

更新当前用户资料

权限：登录；资源归属限制见接口说明。

更新当前登录用户的基础资料。

处理器：`app.endpoint.users.update_me`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UserProfileUpdate"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/users/me/change-email

修改当前用户邮箱

权限：登录；资源归属限制见接口说明。

修改当前登录用户的邮箱地址。

处理器：`app.endpoint.users.change_my_email`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ChangeEmailRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ChangeEmailResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/users/me/change-password

修改当前用户密码

权限：登录；资源归属限制见接口说明。

修改当前登录用户的密码。

处理器：`app.endpoint.users.change_my_password`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UserPasswordChangeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/users/me/change-password-simple

修改当前用户密码（兼容路径，仍需验证旧密码）

权限：登录；资源归属限制见接口说明。

**已弃用，仍可调用。**

兼容旧路径；为防止被窃取的会话直接接管账号，仍需验证当前密码。

处理器：`app.endpoint.users.change_my_password_simple`。

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UserPasswordChangeRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/users/me/deletion-request

取消当前账号注销申请

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.users.cancel_my_account_deletion`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/users/me/deletion-request

查看当前账号注销申请

权限：登录；资源归属限制见接口说明。

处理器：`app.endpoint.users.get_my_deletion_request`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/MyAccountDeletionStatusResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/users/me/deletion-request

申请注销当前账号

权限：登录；资源归属限制见接口说明。

提交注销申请；账号在管理员完成关联资源清理前仍可正常使用。

处理器：`app.endpoint.users.request_my_account_deletion`。

### 响应

```json
{
  "202": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/AccountDeletionRequestResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "409": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "资源、版本、状态或互斥条件冲突"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/users/search

搜索用户（管理员）

权限：管理员。

管理员按邮箱关键字搜索用户，用于下拉选择。

处理器：`app.endpoint.users.search_users`。

### 路径、查询、请求头参数

```json
[
  {
    "description": "按邮箱前缀模糊搜索",
    "in": "query",
    "name": "query",
    "required": true,
    "schema": {
      "description": "按邮箱前缀模糊搜索",
      "maxLength": 128,
      "minLength": 1,
      "title": "Query",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "items": {
            "$ref": "#/components/schemas/UserResponse"
          },
          "title": "Response Search Users Api Users Search Get",
          "type": "array"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /api/users/{user_id}

管理员查看用户详情

权限：管理员。

处理器：`app.endpoint.users.get_user_detail`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "user_id",
    "required": true,
    "schema": {
      "title": "User Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## PATCH /api/users/{user_id}

管理员更新用户资料

权限：管理员。

处理器：`app.endpoint.users.update_user`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "user_id",
    "required": true,
    "schema": {
      "title": "User Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AdminUserUpdateRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /api/users/{user_id}/2fa/totp

管理员重置用户的 TOTP 二次验证

权限：管理员。

处理器：`app.endpoint.users.admin_reset_user_totp`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "user_id",
    "required": true,
    "schema": {
      "title": "User Id",
      "type": "string"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /api/users/{user_id}/reset-password

管理员重置用户密码

权限：管理员。

处理器：`app.endpoint.users.reset_user_password`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "path",
    "name": "user_id",
    "required": true,
    "schema": {
      "title": "User Id",
      "type": "string"
    }
  }
]
```

### 请求体

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AdminResetPasswordRequest"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UserActionResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "403": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务错误；detail 可以是字符串或结构化对象"
  },
  "404": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "目标资源不存在或不可见"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /oauth/authorize

OAuth2 授权端点

权限：平台 Bearer 或 OAuth Cookie；未登录时 302 跳转登录页。

处理器：`app.endpoint.oauth.authorize`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "response_type",
    "required": true,
    "schema": {
      "maxLength": 32,
      "title": "Response Type",
      "type": "string"
    }
  },
  {
    "in": "query",
    "name": "client_id",
    "required": true,
    "schema": {
      "maxLength": 128,
      "minLength": 1,
      "title": "Client Id",
      "type": "string"
    }
  },
  {
    "in": "query",
    "name": "redirect_uri",
    "required": true,
    "schema": {
      "maxLength": 2048,
      "minLength": 1,
      "title": "Redirect Uri",
      "type": "string"
    }
  },
  {
    "in": "query",
    "name": "scope",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 2048,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "",
      "title": "Scope"
    }
  },
  {
    "in": "query",
    "name": "state",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "State"
    }
  },
  {
    "in": "query",
    "name": "nonce",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Nonce"
    }
  },
  {
    "in": "query",
    "name": "code_challenge",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 128,
          "minLength": 43,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Code Challenge"
    }
  },
  {
    "in": "query",
    "name": "code_challenge_method",
    "required": false,
    "schema": {
      "anyOf": [
        {
          "maxLength": 16,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Code Challenge Method"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "text/html": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "Successful Response"
  },
  "302": {
    "description": "重定向，目标见 Location",
    "headers": {
      "Location": {
        "schema": {
          "type": "string"
        }
      }
    }
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "error": {
                  "type": "string"
                },
                "error_description": {
                  "type": "string"
                }
              },
              "required": [
                "error"
              ],
              "type": "object"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "OAuth 协议或客户端认证错误"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "error": {
                  "type": "string"
                },
                "error_description": {
                  "type": "string"
                }
              },
              "required": [
                "error"
              ],
              "type": "object"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "OAuth 协议或客户端认证错误"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /oauth/authorize

OAuth2 授权确认

权限：平台 Bearer 或 OAuth Cookie；未登录时 302 跳转登录页。

处理器：`app.endpoint.oauth.authorize_submit`。

### 请求体

```json
{
  "content": {
    "application/x-www-form-urlencoded": {
      "schema": {
        "$ref": "#/components/schemas/Body_authorize_submit_oauth_authorize_post"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "302": {
    "description": "重定向，目标见 Location",
    "headers": {
      "Location": {
        "schema": {
          "type": "string"
        }
      }
    }
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "error": {
                  "type": "string"
                },
                "error_description": {
                  "type": "string"
                }
              },
              "required": [
                "error"
              ],
              "type": "object"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "OAuth 协议或客户端认证错误"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "error": {
                  "type": "string"
                },
                "error_description": {
                  "type": "string"
                }
              },
              "required": [
                "error"
              ],
              "type": "object"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "OAuth 协议或客户端认证错误"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## DELETE /oauth/session

清除 OAuth 授权流程登录态

权限：公开；业务凭据要求见接口说明。

处理器：`app.endpoint.oauth.revoke_oauth_session`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /oauth/session

建立 OAuth 授权流程登录态（设置Cookie）

权限：PlatformBearer。

处理器：`app.endpoint.oauth.create_oauth_session`。

### 路径、查询、请求头参数

```json
[
  {
    "in": "query",
    "name": "remember",
    "required": false,
    "schema": {
      "default": true,
      "title": "Remember",
      "type": "boolean"
    }
  }
]
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "message": {
              "type": "string"
            }
          },
          "required": [
            "message"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## POST /oauth/token

OAuth2 令牌端点

权限：按客户端类型使用 Basic 或表单凭据；公共客户端无需 secret。

处理器：`app.endpoint.oauth.token`。

### 请求体

```json
{
  "content": {
    "application/x-www-form-urlencoded": {
      "schema": {
        "$ref": "#/components/schemas/Body_token_oauth_token_post"
      }
    }
  },
  "required": true
}
```

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/TokenResponse"
        }
      }
    },
    "description": "Successful Response"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "error": {
                  "type": "string"
                },
                "error_description": {
                  "type": "string"
                }
              },
              "required": [
                "error"
              ],
              "type": "object"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "OAuth 协议或客户端认证错误"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "anyOf": [
            {
              "properties": {
                "error": {
                  "type": "string"
                },
                "error_description": {
                  "type": "string"
                }
              },
              "required": [
                "error"
              ],
              "type": "object"
            },
            {
              "properties": {
                "detail": {}
              },
              "required": [
                "detail"
              ],
              "type": "object"
            }
          ]
        }
      }
    },
    "description": "OAuth 协议或客户端认证错误"
  },
  "422": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/HTTPValidationError"
        }
      }
    },
    "description": "Validation Error"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```


## GET /oauth/userinfo

OIDC UserInfo

权限：OAuthAccessToken。

处理器：`app.endpoint.oauth.userinfo`。

### 响应

```json
{
  "200": {
    "content": {
      "application/json": {
        "schema": {
          "description": "sub、roles、ver 始终返回；其他 claims 按 scope 返回。",
          "properties": {
            "email": {
              "type": "string"
            },
            "email_verified": {
              "type": "boolean"
            },
            "groups": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "name": {
              "type": "string"
            },
            "picture": {
              "type": "string"
            },
            "preferred_username": {
              "type": "string"
            },
            "roles": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "sub": {
              "type": "string"
            },
            "ver": {
              "type": "integer"
            }
          },
          "required": [
            "sub",
            "roles",
            "ver"
          ],
          "type": "object"
        }
      }
    },
    "description": "成功"
  },
  "400": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "业务参数、凭据或状态无效；具体规则见 API_BEHAVIOR.md"
  },
  "401": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "detail": {}
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "缺少、无效或失效的认证凭据"
  },
  "503": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "code": {
              "type": "string"
            },
            "detail": {},
            "request_id": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "detail"
          ],
          "type": "object"
        }
      }
    },
    "description": "依赖服务不可用；全局异常含 code/request_id 和 Retry-After，详见行为约定"
  },
  "default": {
    "content": {
      "application/json": {
        "schema": {
          "additionalProperties": true,
          "type": "object"
        }
      },
      "text/html": {
        "schema": {
          "type": "string"
        }
      },
      "text/plain": {
        "schema": {
          "type": "string"
        }
      }
    },
    "description": "基础设施/未捕获错误；详见 API_BEHAVIOR.md 的全局错误约定"
  }
}
```

## Schema 字典

### AccessApiKeyCreate

```json
{
  "additionalProperties": false,
  "properties": {
    "name": {
      "maxLength": 64,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "user_id": {
      "maxLength": 24,
      "minLength": 24,
      "title": "User Id",
      "type": "string"
    }
  },
  "required": [
    "user_id",
    "name"
  ],
  "title": "AccessApiKeyCreate",
  "type": "object"
}
```

### AccessApiKeyList

```json
{
  "properties": {
    "items": {
      "items": {
        "$ref": "#/components/schemas/AccessApiKeyResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "items",
    "total"
  ],
  "title": "AccessApiKeyList",
  "type": "object"
}
```

### AccessApiKeyResponse

```json
{
  "properties": {
    "created_at": {
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "created_by": {
      "title": "Created By",
      "type": "string"
    },
    "id": {
      "title": "Id",
      "type": "string"
    },
    "is_active": {
      "title": "Is Active",
      "type": "boolean"
    },
    "key_preview": {
      "title": "Key Preview",
      "type": "string"
    },
    "last_used_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Last Used At"
    },
    "name": {
      "title": "Name",
      "type": "string"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Updated At"
    },
    "user_id": {
      "title": "User Id",
      "type": "string"
    }
  },
  "required": [
    "id",
    "user_id",
    "name",
    "key_preview",
    "is_active",
    "created_by",
    "created_at",
    "updated_at",
    "last_used_at"
  ],
  "title": "AccessApiKeyResponse",
  "type": "object"
}
```

### AccessApiKeySecret

```json
{
  "properties": {
    "created_at": {
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "created_by": {
      "title": "Created By",
      "type": "string"
    },
    "id": {
      "title": "Id",
      "type": "string"
    },
    "is_active": {
      "title": "Is Active",
      "type": "boolean"
    },
    "key": {
      "title": "Key",
      "type": "string"
    },
    "key_preview": {
      "title": "Key Preview",
      "type": "string"
    },
    "last_used_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Last Used At"
    },
    "name": {
      "title": "Name",
      "type": "string"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Updated At"
    },
    "user_id": {
      "title": "User Id",
      "type": "string"
    }
  },
  "required": [
    "id",
    "user_id",
    "name",
    "key_preview",
    "is_active",
    "created_by",
    "created_at",
    "updated_at",
    "last_used_at",
    "key"
  ],
  "title": "AccessApiKeySecret",
  "type": "object"
}
```

### AccessApiKeyUpdate

```json
{
  "additionalProperties": false,
  "properties": {
    "is_active": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "title": "Is Active"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 64,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Name"
    }
  },
  "title": "AccessApiKeyUpdate",
  "type": "object"
}
```

### AccountDeletionBlockers

```json
{
  "description": "必须由管理员先行清理的账号关联资源。",
  "properties": {
    "business_accounts": {
      "default": 0,
      "description": "关联业务账号数量",
      "minimum": 0.0,
      "title": "Business Accounts",
      "type": "integer"
    },
    "oauth_clients": {
      "default": 0,
      "description": "用户拥有的 OAuth 应用数量",
      "minimum": 0.0,
      "title": "Oauth Clients",
      "type": "integer"
    },
    "projects": {
      "default": 0,
      "description": "关联项目数量",
      "minimum": 0.0,
      "title": "Projects",
      "type": "integer"
    }
  },
  "title": "AccountDeletionBlockers",
  "type": "object"
}
```

### AccountDeletionRequestListResponse

```json
{
  "description": "管理员账号注销申请列表。",
  "properties": {
    "items": {
      "description": "注销申请列表",
      "items": {
        "$ref": "#/components/schemas/AccountDeletionRequestResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "申请总数",
      "minimum": 0.0,
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total"
  ],
  "title": "AccountDeletionRequestListResponse",
  "type": "object"
}
```

### AccountDeletionRequestResponse

```json
{
  "description": "账号注销申请及其当前清理状态。",
  "properties": {
    "blockers": {
      "$ref": "#/components/schemas/AccountDeletionBlockers"
    },
    "can_delete": {
      "default": false,
      "description": "关联业务资源是否已经清理完成",
      "title": "Can Delete",
      "type": "boolean"
    },
    "cancelled_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "取消时间",
      "title": "Cancelled At"
    },
    "id": {
      "description": "注销申请 ID",
      "title": "Id",
      "type": "string"
    },
    "requested_at": {
      "description": "申请时间",
      "format": "date-time",
      "title": "Requested At",
      "type": "string"
    },
    "status": {
      "$ref": "#/components/schemas/AccountDeletionRequestStatus",
      "description": "申请状态"
    },
    "updated_at": {
      "description": "更新时间",
      "format": "date-time",
      "title": "Updated At",
      "type": "string"
    },
    "user_email": {
      "description": "申请时的邮箱快照",
      "title": "User Email",
      "type": "string"
    },
    "user_id": {
      "description": "用户 ID",
      "title": "User Id",
      "type": "string"
    }
  },
  "required": [
    "id",
    "user_id",
    "user_email",
    "status",
    "requested_at",
    "updated_at"
  ],
  "title": "AccountDeletionRequestResponse",
  "type": "object"
}
```

### AccountDeletionRequestStatus

```json
{
  "description": "账号注销申请状态。",
  "enum": [
    "pending",
    "processing",
    "cancelled"
  ],
  "title": "AccountDeletionRequestStatus",
  "type": "string"
}
```

### AdminChangePasswordRequest

```json
{
  "description": "管理员修改用户密码请求Schema",
  "properties": {
    "email": {
      "description": "要修改密码的用户邮箱",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "new_password": {
      "description": "新密码（8-128位）",
      "maxLength": 128,
      "minLength": 8,
      "title": "New Password",
      "type": "string"
    }
  },
  "required": [
    "email",
    "new_password"
  ],
  "title": "AdminChangePasswordRequest",
  "type": "object"
}
```

### AdminChangePasswordResponse

```json
{
  "description": "管理员修改用户密码响应Schema",
  "properties": {
    "email": {
      "description": "被修改密码的用户邮箱",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "message",
    "email"
  ],
  "title": "AdminChangePasswordResponse",
  "type": "object"
}
```

### AdminResetPasswordRequest

```json
{
  "description": "管理员重置指定用户密码",
  "properties": {
    "new_password": {
      "description": "新密码（8-128位）",
      "maxLength": 128,
      "minLength": 8,
      "title": "New Password",
      "type": "string"
    }
  },
  "required": [
    "new_password"
  ],
  "title": "AdminResetPasswordRequest",
  "type": "object"
}
```

### AdminUserUpdateRequest

```json
{
  "description": "管理员更新用户档案",
  "properties": {
    "avatar_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "头像URL",
      "title": "Avatar Url"
    },
    "bio": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "个人简介",
      "title": "Bio"
    },
    "full_name": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户姓名",
      "title": "Full Name"
    },
    "groups": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户所属的组（用于 OIDC groups claim）；传入空数组表示清空",
      "title": "Groups"
    },
    "is_active": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "账号状态",
      "title": "Is Active"
    },
    "phone_number": {
      "anyOf": [
        {
          "maxLength": 32,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Phone Number"
    },
    "role": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/UserRole"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户角色"
    }
  },
  "title": "AdminUserUpdateRequest",
  "type": "object"
}
```

### AgentUpdate

```json
{
  "properties": {
    "level": {
      "enum": [
        1,
        2,
        3
      ],
      "title": "Level",
      "type": "integer"
    },
    "rate_percent": {
      "anyOf": [
        {
          "maximum": 100.0,
          "minimum": 0.0,
          "type": "number"
        },
        {
          "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d{0,2}0*$",
          "type": "string"
        }
      ],
      "default": 0,
      "title": "Rate Percent"
    },
    "revision": {
      "minimum": 1.0,
      "title": "Revision",
      "type": "integer"
    }
  },
  "required": [
    "level",
    "revision"
  ],
  "title": "AgentUpdate",
  "type": "object"
}
```

### ApiKeyToggleStatus

```json
{
  "description": "API密钥状态切换Schema",
  "properties": {
    "is_active": {
      "description": "是否启用",
      "title": "Is Active",
      "type": "boolean"
    }
  },
  "required": [
    "is_active"
  ],
  "title": "ApiKeyToggleStatus",
  "type": "object"
}
```

### ApiKeyValidationRequest

```json
{
  "description": "应用密钥验证请求；密钥必须放在请求体，避免进入 URL 和访问日志。",
  "properties": {
    "key": {
      "description": "应用密钥",
      "maxLength": 256,
      "minLength": 32,
      "title": "Key",
      "type": "string"
    }
  },
  "required": [
    "key"
  ],
  "title": "ApiKeyValidationRequest",
  "type": "object"
}
```

### AssistantRequest

```json
{
  "properties": {
    "agent_code": {
      "anyOf": [
        {
          "pattern": "^[0-9a-fA-F]{8}$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Code"
    },
    "agent_revision": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Revision"
    },
    "messages": {
      "items": {
        "$ref": "#/components/schemas/ChatMessage"
      },
      "maxItems": 20,
      "minItems": 1,
      "title": "Messages",
      "type": "array"
    },
    "revision": {
      "minimum": 1.0,
      "title": "Revision",
      "type": "integer"
    },
    "selection": {
      "$ref": "#/components/schemas/Selection"
    }
  },
  "required": [
    "messages",
    "selection",
    "revision"
  ],
  "title": "AssistantRequest",
  "type": "object"
}
```

### Body_authenticate_passkey_api_passkey_authenticate_post

```json
{
  "properties": {
    "authenticator_data": {
      "description": "认证器数据（base64url）",
      "title": "Authenticator Data",
      "type": "string"
    },
    "client_data_json": {
      "description": "客户端数据JSON（base64url编码的原始字节）",
      "title": "Client Data Json",
      "type": "string"
    },
    "credential_id": {
      "description": "凭证ID（base64url）",
      "title": "Credential Id",
      "type": "string"
    },
    "raw_id": {
      "description": "原始凭证ID（base64url）",
      "title": "Raw Id",
      "type": "string"
    },
    "session_id": {
      "description": "认证会话ID",
      "title": "Session Id",
      "type": "string"
    },
    "signature": {
      "description": "签名（base64url）",
      "title": "Signature",
      "type": "string"
    }
  },
  "required": [
    "session_id",
    "credential_id",
    "authenticator_data",
    "client_data_json",
    "signature",
    "raw_id"
  ],
  "title": "Body_authenticate_passkey_api_passkey_authenticate_post",
  "type": "object"
}
```

### Body_authorize_submit_oauth_authorize_post

```json
{
  "properties": {
    "client_id": {
      "maxLength": 128,
      "minLength": 1,
      "title": "Client Id",
      "type": "string"
    },
    "code_challenge": {
      "anyOf": [
        {
          "maxLength": 128,
          "minLength": 43,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Code Challenge"
    },
    "code_challenge_method": {
      "anyOf": [
        {
          "maxLength": 16,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Code Challenge Method"
    },
    "decision": {
      "maxLength": 16,
      "title": "Decision",
      "type": "string"
    },
    "nonce": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Nonce"
    },
    "redirect_uri": {
      "maxLength": 2048,
      "minLength": 1,
      "title": "Redirect Uri",
      "type": "string"
    },
    "response_type": {
      "maxLength": 32,
      "title": "Response Type",
      "type": "string"
    },
    "scope": {
      "default": "",
      "maxLength": 2048,
      "title": "Scope",
      "type": "string"
    },
    "state": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "State"
    }
  },
  "required": [
    "response_type",
    "client_id",
    "redirect_uri",
    "decision"
  ],
  "title": "Body_authorize_submit_oauth_authorize_post",
  "type": "object"
}
```

### Body_login_for_access_token_api_auth_token_post

```json
{
  "properties": {
    "client_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Client Id"
    },
    "client_secret": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "format": "password",
      "title": "Client Secret"
    },
    "grant_type": {
      "anyOf": [
        {
          "pattern": "^password$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Grant Type"
    },
    "password": {
      "format": "password",
      "title": "Password",
      "type": "string"
    },
    "scope": {
      "default": "",
      "title": "Scope",
      "type": "string"
    },
    "username": {
      "title": "Username",
      "type": "string"
    }
  },
  "required": [
    "username",
    "password"
  ],
  "title": "Body_login_for_access_token_api_auth_token_post",
  "type": "object"
}
```

### Body_token_oauth_token_post

```json
{
  "properties": {
    "client_id": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Client Id"
    },
    "client_secret": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Client Secret"
    },
    "code": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Code"
    },
    "code_verifier": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Code Verifier"
    },
    "grant_type": {
      "maxLength": 64,
      "title": "Grant Type",
      "type": "string"
    },
    "redirect_uri": {
      "anyOf": [
        {
          "maxLength": 2048,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Redirect Uri"
    },
    "refresh_token": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Refresh Token"
    },
    "scope": {
      "anyOf": [
        {
          "maxLength": 2048,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Scope"
    }
  },
  "required": [
    "grant_type"
  ],
  "title": "Body_token_oauth_token_post",
  "type": "object"
}
```

### BusinessAccountAdminUpdateRequest

```json
{
  "description": "管理员更新业务账号字段",
  "properties": {
    "assigned_email": {
      "anyOf": [
        {
          "format": "email",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "专属邮箱（管理员分配）",
      "title": "Assigned Email"
    },
    "certification_info": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "认证信息",
      "title": "Certification Info"
    },
    "communication_address": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "通信地址",
      "title": "Communication Address"
    },
    "company_name": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "公司抬头",
      "title": "Company Name"
    },
    "contact_person_name": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系人（委托人）姓名",
      "title": "Contact Person Name"
    },
    "contact_phone": {
      "anyOf": [
        {
          "maxLength": 32,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Contact Phone"
    },
    "status": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/BusinessAccountStatus"
        },
        {
          "type": "null"
        }
      ],
      "description": "业务账号状态（管理员可调整）"
    },
    "tax_number": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "税号",
      "title": "Tax Number"
    },
    "user_code": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户识别码（管理员分配）",
      "title": "User Code"
    }
  },
  "title": "BusinessAccountAdminUpdateRequest",
  "type": "object"
}
```

### BusinessAccountApplyRequest

```json
{
  "description": "用户申请创建业务账号时可填写的字段（均为可选）",
  "properties": {
    "certification_info": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "认证信息",
      "title": "Certification Info"
    },
    "communication_address": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "通信地址",
      "title": "Communication Address"
    },
    "company_name": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "公司抬头",
      "title": "Company Name"
    },
    "contact_person_name": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系人（委托人）姓名",
      "title": "Contact Person Name"
    },
    "contact_phone": {
      "anyOf": [
        {
          "maxLength": 32,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Contact Phone"
    },
    "tax_number": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "税号",
      "title": "Tax Number"
    }
  },
  "title": "BusinessAccountApplyRequest",
  "type": "object"
}
```

### BusinessAccountListResponse

```json
{
  "description": "业务账号列表响应",
  "properties": {
    "items": {
      "description": "业务账号列表",
      "items": {
        "$ref": "#/components/schemas/BusinessAccountResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "BusinessAccountListResponse",
  "type": "object"
}
```

### BusinessAccountResponse

```json
{
  "description": "业务账号响应 Schema",
  "properties": {
    "assigned_email": {
      "anyOf": [
        {
          "format": "email",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "专属邮箱（管理员分配）",
      "title": "Assigned Email"
    },
    "certification_info": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "认证信息",
      "title": "Certification Info"
    },
    "communication_address": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "通信地址",
      "title": "Communication Address"
    },
    "company_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "公司抬头",
      "title": "Company Name"
    },
    "contact_person_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系人（委托人）姓名",
      "title": "Contact Person Name"
    },
    "contact_phone": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Contact Phone"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "id": {
      "description": "业务账号ID",
      "title": "Id",
      "type": "string"
    },
    "owner_email": {
      "description": "所属用户邮箱",
      "title": "Owner Email",
      "type": "string"
    },
    "owner_id": {
      "description": "所属用户ID",
      "title": "Owner Id",
      "type": "string"
    },
    "status": {
      "$ref": "#/components/schemas/BusinessAccountStatus"
    },
    "tax_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "税号",
      "title": "Tax Number"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    },
    "user_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户识别码（管理员分配）",
      "title": "User Code"
    }
  },
  "required": [
    "id",
    "status",
    "owner_id",
    "owner_email",
    "created_at"
  ],
  "title": "BusinessAccountResponse",
  "type": "object"
}
```

### BusinessAccountStatus

```json
{
  "description": "业务账号状态",
  "enum": [
    "pending",
    "active",
    "disabled"
  ],
  "title": "BusinessAccountStatus",
  "type": "string"
}
```

### BusinessAccountUpdateRequest

```json
{
  "description": "用户更新业务账号可编辑字段",
  "properties": {
    "certification_info": {
      "anyOf": [
        {
          "maxLength": 512,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "认证信息",
      "title": "Certification Info"
    },
    "communication_address": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "通信地址",
      "title": "Communication Address"
    },
    "company_name": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "公司抬头",
      "title": "Company Name"
    },
    "contact_person_name": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系人（委托人）姓名",
      "title": "Contact Person Name"
    },
    "contact_phone": {
      "anyOf": [
        {
          "maxLength": 32,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Contact Phone"
    },
    "tax_number": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "税号",
      "title": "Tax Number"
    }
  },
  "title": "BusinessAccountUpdateRequest",
  "type": "object"
}
```

### CatalogData

```json
{
  "properties": {
    "items": {
      "items": {
        "$ref": "#/components/schemas/ShopItem"
      },
      "maxItems": 100,
      "title": "Items",
      "type": "array"
    },
    "plans": {
      "items": {
        "$ref": "#/components/schemas/ShopPlan"
      },
      "maxItems": 2,
      "minItems": 2,
      "title": "Plans",
      "type": "array"
    },
    "revision": {
      "minimum": 1.0,
      "title": "Revision",
      "type": "integer"
    }
  },
  "required": [
    "revision",
    "plans",
    "items"
  ],
  "title": "CatalogData",
  "type": "object"
}
```

### ChangeEmailRequest

```json
{
  "description": "修改邮箱请求",
  "properties": {
    "new_email": {
      "description": "新邮箱地址",
      "format": "email",
      "title": "New Email",
      "type": "string"
    },
    "verification_code": {
      "description": "邮箱验证码",
      "maxLength": 6,
      "minLength": 6,
      "title": "Verification Code",
      "type": "string"
    }
  },
  "required": [
    "new_email",
    "verification_code"
  ],
  "title": "ChangeEmailRequest",
  "type": "object"
}
```

### ChangeEmailResponse

```json
{
  "description": "修改邮箱响应",
  "properties": {
    "access_token": {
      "description": "新的访问令牌",
      "title": "Access Token",
      "type": "string"
    },
    "email": {
      "description": "新邮箱地址",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "expires_in": {
      "description": "过期时间（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    },
    "token_type": {
      "default": "bearer",
      "description": "令牌类型",
      "title": "Token Type",
      "type": "string"
    }
  },
  "required": [
    "message",
    "email",
    "access_token",
    "expires_in"
  ],
  "title": "ChangeEmailResponse",
  "type": "object"
}
```

### ChangePhoneNumberRequest

```json
{
  "description": "修改手机号码请求Schema",
  "properties": {
    "new_phone_number": {
      "description": "新手机号码",
      "maxLength": 11,
      "minLength": 11,
      "title": "New Phone Number",
      "type": "string"
    },
    "verification_code": {
      "description": "短信验证码",
      "maxLength": 6,
      "minLength": 6,
      "title": "Verification Code",
      "type": "string"
    }
  },
  "required": [
    "new_phone_number",
    "verification_code"
  ],
  "title": "ChangePhoneNumberRequest",
  "type": "object"
}
```

### ChangePhoneNumberResponse

```json
{
  "description": "修改手机号码响应Schema",
  "properties": {
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    },
    "phone_number": {
      "description": "新手机号码",
      "title": "Phone Number",
      "type": "string"
    }
  },
  "required": [
    "message",
    "phone_number"
  ],
  "title": "ChangePhoneNumberResponse",
  "type": "object"
}
```

### ChatMessage

```json
{
  "properties": {
    "content": {
      "maxLength": 4000,
      "minLength": 1,
      "title": "Content",
      "type": "string"
    },
    "role": {
      "enum": [
        "user",
        "assistant"
      ],
      "title": "Role",
      "type": "string"
    }
  },
  "required": [
    "role",
    "content"
  ],
  "title": "ChatMessage",
  "type": "object"
}
```

### CheckUserExistsRequest

```json
{
  "description": "检查用户是否存在请求",
  "properties": {
    "identifier": {
      "description": "邮箱或手机号",
      "minLength": 1,
      "title": "Identifier",
      "type": "string"
    }
  },
  "required": [
    "identifier"
  ],
  "title": "CheckUserExistsRequest",
  "type": "object"
}
```

### CheckUserExistsResponse

```json
{
  "description": "检查用户是否存在响应",
  "properties": {
    "exists": {
      "description": "用户是否存在",
      "title": "Exists",
      "type": "boolean"
    },
    "identifier_type": {
      "description": "标识符类型(email/phone)",
      "title": "Identifier Type",
      "type": "string"
    }
  },
  "required": [
    "exists",
    "identifier_type"
  ],
  "title": "CheckUserExistsResponse",
  "type": "object"
}
```

### CommissionUpdate

```json
{
  "properties": {
    "expected_status": {
      "enum": [
        "pending",
        "confirmed",
        "invalid",
        "settled"
      ],
      "title": "Expected Status",
      "type": "string"
    },
    "note": {
      "maxLength": 500,
      "minLength": 1,
      "title": "Note",
      "type": "string"
    },
    "receipt_confirmed": {
      "default": false,
      "title": "Receipt Confirmed",
      "type": "boolean"
    },
    "status": {
      "enum": [
        "confirmed",
        "invalid",
        "settled"
      ],
      "title": "Status",
      "type": "string"
    }
  },
  "required": [
    "expected_status",
    "status",
    "note"
  ],
  "title": "CommissionUpdate",
  "type": "object"
}
```

### ContactCreate

```json
{
  "description": "创建联系我们表单Schema",
  "properties": {
    "email": {
      "description": "邮箱",
      "format": "email",
      "maxLength": 320,
      "title": "Email",
      "type": "string"
    },
    "message": {
      "description": "消息内容",
      "maxLength": 5000,
      "minLength": 1,
      "title": "Message",
      "type": "string"
    },
    "name": {
      "description": "称呼",
      "maxLength": 100,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "turnstileToken": {
      "description": "Cloudflare Turnstile 验证令牌",
      "maxLength": 4096,
      "minLength": 1,
      "title": "Turnstiletoken",
      "type": "string"
    }
  },
  "required": [
    "name",
    "email",
    "message",
    "turnstileToken"
  ],
  "title": "ContactCreate",
  "type": "object"
}
```

### ContactListResponse

```json
{
  "description": "联系我们表单列表响应Schema",
  "properties": {
    "items": {
      "description": "联系表单列表",
      "items": {
        "$ref": "#/components/schemas/ContactResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "ContactListResponse",
  "type": "object"
}
```

### ContactResponse

```json
{
  "description": "联系我们表单响应Schema",
  "properties": {
    "admin_notes": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "管理员备注",
      "title": "Admin Notes"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "email": {
      "description": "邮箱",
      "title": "Email",
      "type": "string"
    },
    "id": {
      "description": "联系表单ID",
      "title": "Id",
      "type": "string"
    },
    "is_processed": {
      "description": "是否已处理",
      "title": "Is Processed",
      "type": "boolean"
    },
    "message": {
      "description": "消息内容",
      "title": "Message",
      "type": "string"
    },
    "name": {
      "description": "称呼",
      "title": "Name",
      "type": "string"
    },
    "processed_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "处理时间",
      "title": "Processed At"
    },
    "processed_by": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "处理人（管理员邮箱）",
      "title": "Processed By"
    },
    "remote_ip": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端IP地址",
      "title": "Remote Ip"
    }
  },
  "required": [
    "id",
    "name",
    "email",
    "message",
    "is_processed",
    "created_at"
  ],
  "title": "ContactResponse",
  "type": "object"
}
```

### ContactUpdate

```json
{
  "description": "更新联系我们表单Schema（管理员）",
  "properties": {
    "admin_notes": {
      "anyOf": [
        {
          "maxLength": 2000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "管理员备注",
      "title": "Admin Notes"
    },
    "is_processed": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "是否已处理",
      "title": "Is Processed"
    }
  },
  "title": "ContactUpdate",
  "type": "object"
}
```

### EmailResetPasswordRequest

```json
{
  "description": "邮箱重置密码请求",
  "properties": {
    "email": {
      "description": "邮箱地址",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "new_password": {
      "description": "新密码",
      "maxLength": 128,
      "minLength": 8,
      "title": "New Password",
      "type": "string"
    },
    "verification_code": {
      "description": "邮箱验证码",
      "maxLength": 6,
      "minLength": 6,
      "title": "Verification Code",
      "type": "string"
    }
  },
  "required": [
    "email",
    "verification_code",
    "new_password"
  ],
  "title": "EmailResetPasswordRequest",
  "type": "object"
}
```

### EmailResetPasswordResponse

```json
{
  "description": "邮箱重置密码响应",
  "properties": {
    "email": {
      "description": "邮箱地址",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "message",
    "email"
  ],
  "title": "EmailResetPasswordResponse",
  "type": "object"
}
```

### ExportRequest

```json
{
  "additionalProperties": false,
  "properties": {
    "datasets": {
      "items": {
        "type": "string"
      },
      "maxItems": 28,
      "minItems": 1,
      "title": "Datasets",
      "type": "array"
    }
  },
  "required": [
    "datasets"
  ],
  "title": "ExportRequest",
  "type": "object"
}
```

### HTTPValidationError

```json
{
  "properties": {
    "detail": {
      "items": {
        "$ref": "#/components/schemas/ValidationError"
      },
      "title": "Detail",
      "type": "array"
    }
  },
  "title": "HTTPValidationError",
  "type": "object"
}
```

### MyAccountDeletionStatusResponse

```json
{
  "description": "当前用户的注销申请状态。",
  "properties": {
    "pending": {
      "description": "是否存在待处理的注销申请",
      "title": "Pending",
      "type": "boolean"
    },
    "request": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/AccountDeletionRequestResponse"
        },
        {
          "type": "null"
        }
      ],
      "description": "待处理申请；没有申请时为空"
    }
  },
  "required": [
    "pending"
  ],
  "title": "MyAccountDeletionStatusResponse",
  "type": "object"
}
```

### OAuthCallbackRequest

```json
{
  "properties": {
    "code": {
      "description": "授权码",
      "maxLength": 256,
      "minLength": 32,
      "title": "Code",
      "type": "string"
    },
    "code_verifier": {
      "description": "PKCE code_verifier",
      "maxLength": 128,
      "minLength": 43,
      "title": "Code Verifier",
      "type": "string"
    },
    "redirect_uri": {
      "anyOf": [
        {
          "maxLength": 2048,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "回调地址，默认使用配置项中的redirect_uri",
      "title": "Redirect Uri"
    },
    "state": {
      "description": "原样回传的state",
      "maxLength": 512,
      "minLength": 16,
      "title": "State",
      "type": "string"
    }
  },
  "required": [
    "code",
    "state",
    "code_verifier"
  ],
  "title": "OAuthCallbackRequest",
  "type": "object"
}
```

### OAuthCallbackResponse

```json
{
  "properties": {
    "app_token": {
      "description": "本地系统访问令牌",
      "title": "App Token",
      "type": "string"
    },
    "expires_in": {
      "description": "本地令牌有效期（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "oauth": {
      "$ref": "#/components/schemas/TokenResponse",
      "description": "OAuth2 授权服务器返回的令牌集合"
    },
    "state": {
      "description": "用于CSRF校验的state值",
      "title": "State",
      "type": "string"
    },
    "token_type": {
      "default": "Bearer",
      "description": "本地令牌类型",
      "title": "Token Type",
      "type": "string"
    },
    "user": {
      "$ref": "#/components/schemas/UserResponse",
      "description": "已登录用户信息"
    }
  },
  "required": [
    "app_token",
    "expires_in",
    "user",
    "oauth",
    "state"
  ],
  "title": "OAuthCallbackResponse",
  "type": "object"
}
```

### OAuthClientCreate

```json
{
  "properties": {
    "grant_types": {
      "description": "允许的授权类型",
      "items": {
        "type": "string"
      },
      "maxItems": 3,
      "title": "Grant Types",
      "type": "array"
    },
    "is_confidential": {
      "default": true,
      "description": "是否为机密客户端",
      "title": "Is Confidential",
      "type": "boolean"
    },
    "is_enabled": {
      "default": true,
      "description": "客户端是否启用",
      "title": "Is Enabled",
      "type": "boolean"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端名称",
      "title": "Name"
    },
    "redirect_uris": {
      "description": "允许的重定向URI列表",
      "items": {
        "type": "string"
      },
      "maxItems": 20,
      "minItems": 1,
      "title": "Redirect Uris",
      "type": "array"
    },
    "scopes": {
      "description": "允许的scope集合",
      "items": {
        "type": "string"
      },
      "maxItems": 30,
      "title": "Scopes",
      "type": "array"
    }
  },
  "required": [
    "redirect_uris"
  ],
  "title": "OAuthClientCreate",
  "type": "object"
}
```

### OAuthClientListResponse

```json
{
  "properties": {
    "items": {
      "description": "客户端列表",
      "items": {
        "$ref": "#/components/schemas/OAuthClientRead"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数量",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total"
  ],
  "title": "OAuthClientListResponse",
  "type": "object"
}
```

### OAuthClientRead

```json
{
  "properties": {
    "client_id": {
      "description": "客户端ID",
      "title": "Client Id",
      "type": "string"
    },
    "client_secret_plain": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端密钥明文，仅在创建后返回一次",
      "title": "Client Secret Plain"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "grant_types": {
      "description": "允许的授权类型",
      "items": {
        "type": "string"
      },
      "maxItems": 3,
      "title": "Grant Types",
      "type": "array"
    },
    "has_client_secret": {
      "default": false,
      "description": "是否已配置客户端密钥",
      "title": "Has Client Secret",
      "type": "boolean"
    },
    "id": {
      "description": "文档ID",
      "title": "Id",
      "type": "string"
    },
    "is_confidential": {
      "default": true,
      "description": "是否为机密客户端",
      "title": "Is Confidential",
      "type": "boolean"
    },
    "is_enabled": {
      "default": true,
      "description": "客户端是否启用",
      "title": "Is Enabled",
      "type": "boolean"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端名称",
      "title": "Name"
    },
    "owner_email": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端所属用户邮箱（仅管理员可见）",
      "title": "Owner Email"
    },
    "owner_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端所属用户ID",
      "title": "Owner Id"
    },
    "redirect_uris": {
      "description": "允许的重定向URI列表",
      "items": {
        "type": "string"
      },
      "maxItems": 20,
      "minItems": 1,
      "title": "Redirect Uris",
      "type": "array"
    },
    "scopes": {
      "description": "允许的scope集合",
      "items": {
        "type": "string"
      },
      "maxItems": 30,
      "title": "Scopes",
      "type": "array"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    }
  },
  "required": [
    "redirect_uris",
    "id",
    "client_id",
    "created_at"
  ],
  "title": "OAuthClientRead",
  "type": "object"
}
```

### OAuthClientUpdate

```json
{
  "properties": {
    "client_secret": {
      "anyOf": [
        {
          "maxLength": 256,
          "minLength": 32,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "如果提供则更新客户端密钥",
      "title": "Client Secret"
    },
    "grant_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "description": "允许的授权类型：authorization_code、refresh_token等",
      "title": "Grant Types"
    },
    "is_confidential": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "是否为机密客户端",
      "title": "Is Confidential"
    },
    "is_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端是否启用",
      "title": "Is Enabled"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 128,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "客户端名称",
      "title": "Name"
    },
    "redirect_uris": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "maxItems": 20,
          "minItems": 1,
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "description": "允许的重定向URI列表",
      "title": "Redirect Uris"
    },
    "scopes": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "description": "允许的scope集合",
      "title": "Scopes"
    }
  },
  "title": "OAuthClientUpdate",
  "type": "object"
}
```

### OAuthKeyImportRequest

```json
{
  "properties": {
    "activate": {
      "default": false,
      "title": "Activate",
      "type": "boolean"
    },
    "expires_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Expires At"
    },
    "kid": {
      "maxLength": 128,
      "minLength": 1,
      "title": "Kid",
      "type": "string"
    },
    "private_key_pem": {
      "maxLength": 65536,
      "minLength": 128,
      "title": "Private Key Pem",
      "type": "string"
    }
  },
  "required": [
    "kid",
    "private_key_pem"
  ],
  "title": "OAuthKeyImportRequest",
  "type": "object"
}
```

### OAuthKeyInitializeRequest

```json
{
  "properties": {
    "expires_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Expires At"
    },
    "kid": {
      "anyOf": [
        {
          "maxLength": 128,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Kid"
    },
    "rsa_bits": {
      "default": 3072,
      "maximum": 8192.0,
      "minimum": 2048.0,
      "title": "Rsa Bits",
      "type": "integer"
    }
  },
  "title": "OAuthKeyInitializeRequest",
  "type": "object"
}
```

### OrderCreate

```json
{
  "additionalProperties": false,
  "properties": {
    "agent_code": {
      "anyOf": [
        {
          "pattern": "^[0-9a-fA-F]{8}$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Code"
    },
    "agent_revision": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Revision"
    },
    "item_ids": {
      "items": {
        "type": "string"
      },
      "maxItems": 100,
      "title": "Item Ids",
      "type": "array"
    },
    "plan": {
      "default": "popular",
      "enum": [
        "custom",
        "popular"
      ],
      "title": "Plan",
      "type": "string"
    },
    "request_id": {
      "maxLength": 64,
      "minLength": 16,
      "pattern": "^[a-zA-Z0-9_-]+$",
      "title": "Request Id",
      "type": "string"
    },
    "requirements": {
      "default": "",
      "maxLength": 1000,
      "title": "Requirements",
      "type": "string"
    },
    "revision": {
      "minimum": 1.0,
      "title": "Revision",
      "type": "integer"
    }
  },
  "required": [
    "revision",
    "request_id"
  ],
  "title": "OrderCreate",
  "type": "object"
}
```

### OrderLine

```json
{
  "properties": {
    "description": {
      "title": "Description",
      "type": "string"
    },
    "group": {
      "title": "Group",
      "type": "string"
    },
    "item_id": {
      "title": "Item Id",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "type": "string"
    },
    "price": {
      "title": "Price",
      "type": "integer"
    }
  },
  "required": [
    "item_id",
    "name",
    "description",
    "group",
    "price"
  ],
  "title": "OrderLine",
  "type": "object"
}
```

### OrderQuote

```json
{
  "additionalProperties": false,
  "properties": {
    "agent_code": {
      "anyOf": [
        {
          "pattern": "^[0-9a-fA-F]{8}$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Code"
    },
    "agent_revision": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "Agent Revision"
    },
    "item_ids": {
      "items": {
        "type": "string"
      },
      "maxItems": 100,
      "title": "Item Ids",
      "type": "array"
    },
    "plan": {
      "default": "popular",
      "enum": [
        "custom",
        "popular"
      ],
      "title": "Plan",
      "type": "string"
    },
    "requirements": {
      "default": "",
      "maxLength": 1000,
      "title": "Requirements",
      "type": "string"
    },
    "revision": {
      "minimum": 1.0,
      "title": "Revision",
      "type": "integer"
    }
  },
  "required": [
    "revision"
  ],
  "title": "OrderQuote",
  "type": "object"
}
```

### OrderSnapshot

```json
{
  "properties": {
    "currency": {
      "const": "CNY",
      "default": "CNY",
      "title": "Currency",
      "type": "string"
    },
    "discount": {
      "default": 0,
      "title": "Discount",
      "type": "integer"
    },
    "items": {
      "items": {
        "$ref": "#/components/schemas/OrderLine"
      },
      "title": "Items",
      "type": "array"
    },
    "plan": {
      "$ref": "#/components/schemas/ShopPlan"
    },
    "referral": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/ReferralSnapshot"
        },
        {
          "type": "null"
        }
      ]
    },
    "requirements": {
      "title": "Requirements",
      "type": "string"
    },
    "revision": {
      "title": "Revision",
      "type": "integer"
    },
    "subtotal": {
      "default": 0,
      "title": "Subtotal",
      "type": "integer"
    },
    "total": {
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "revision",
    "plan",
    "items",
    "total",
    "requirements"
  ],
  "title": "OrderSnapshot",
  "type": "object"
}
```

### PasskeyNicknameUpdate

```json
{
  "description": "更新通行密钥昵称的结构化请求。",
  "properties": {
    "nickname": {
      "description": "新昵称",
      "maxLength": 64,
      "minLength": 1,
      "title": "Nickname",
      "type": "string"
    }
  },
  "required": [
    "nickname"
  ],
  "title": "PasskeyNicknameUpdate",
  "type": "object"
}
```

### PasskeyToggleRequest

```json
{
  "description": "启用或禁用通行密钥登录。",
  "properties": {
    "enabled": {
      "description": "是否启用",
      "title": "Enabled",
      "type": "boolean"
    }
  },
  "required": [
    "enabled"
  ],
  "title": "PasskeyToggleRequest",
  "type": "object"
}
```

### ProjectCreate

```json
{
  "description": "管理员创建项目",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 1000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "项目描述",
      "title": "Description"
    },
    "name": {
      "description": "项目名称",
      "maxLength": 200,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "overview_markdown": {
      "default": "",
      "description": "项目概述（Markdown格式）",
      "title": "Overview Markdown",
      "type": "string"
    },
    "owner_email": {
      "description": "所属用户邮箱",
      "format": "email",
      "title": "Owner Email",
      "type": "string"
    },
    "rating": {
      "default": 3,
      "description": "项目评分（1-5）",
      "maximum": 5.0,
      "minimum": 1.0,
      "title": "Rating",
      "type": "integer"
    },
    "responsible_tag_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "负责人ID（可选）",
      "title": "Responsible Tag Id"
    }
  },
  "required": [
    "owner_email",
    "name"
  ],
  "title": "ProjectCreate",
  "type": "object"
}
```

### ProjectFileCreate

```json
{
  "description": "创建项目文件（MongoDB GridFS 上传完成后调用）。",
  "properties": {
    "file_size": {
      "description": "文件大小（字节）",
      "minimum": 0.0,
      "title": "File Size",
      "type": "integer"
    },
    "filename": {
      "description": "文件名",
      "maxLength": 500,
      "minLength": 1,
      "title": "Filename",
      "type": "string"
    },
    "mime_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "MIME类型",
      "title": "Mime Type"
    },
    "original_filename": {
      "description": "原始文件名",
      "maxLength": 500,
      "minLength": 1,
      "title": "Original Filename",
      "type": "string"
    },
    "oss_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "兼容旧客户端的字段名；其值会作为 MongoDB storage_key 使用",
      "title": "Oss Key"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "storage_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "MongoDB GridFS 逻辑存储键",
      "title": "Storage Key"
    },
    "tags": {
      "description": "标签列表",
      "items": {
        "type": "string"
      },
      "title": "Tags",
      "type": "array"
    }
  },
  "required": [
    "project_id",
    "filename",
    "original_filename",
    "file_size"
  ],
  "title": "ProjectFileCreate",
  "type": "object"
}
```

### ProjectFileDownloadUrlResponse

```json
{
  "description": "项目文件下载预签名URL响应",
  "properties": {
    "download_url": {
      "description": "下载预签名URL",
      "title": "Download Url",
      "type": "string"
    },
    "expires_in": {
      "description": "URL有效期（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "filename": {
      "description": "文件名",
      "title": "Filename",
      "type": "string"
    }
  },
  "required": [
    "download_url",
    "filename",
    "expires_in"
  ],
  "title": "ProjectFileDownloadUrlResponse",
  "type": "object"
}
```

### ProjectFileListResponse

```json
{
  "description": "项目文件列表响应",
  "properties": {
    "items": {
      "description": "文件列表",
      "items": {
        "$ref": "#/components/schemas/ProjectFileResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "ProjectFileListResponse",
  "type": "object"
}
```

### ProjectFileResponse

```json
{
  "description": "项目文件响应",
  "properties": {
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "file_size": {
      "description": "文件大小（字节）",
      "title": "File Size",
      "type": "integer"
    },
    "filename": {
      "description": "文件名",
      "title": "Filename",
      "type": "string"
    },
    "id": {
      "description": "文件ID",
      "title": "Id",
      "type": "string"
    },
    "mime_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "MIME类型",
      "title": "Mime Type"
    },
    "original_filename": {
      "description": "原始文件名",
      "title": "Original Filename",
      "type": "string"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "tags": {
      "description": "标签列表",
      "items": {
        "type": "string"
      },
      "title": "Tags",
      "type": "array"
    }
  },
  "required": [
    "id",
    "project_id",
    "filename",
    "original_filename",
    "file_size",
    "tags",
    "created_at"
  ],
  "title": "ProjectFileResponse",
  "type": "object"
}
```

### ProjectFileUpdate

```json
{
  "description": "更新项目文件（主要是标签）",
  "properties": {
    "filename": {
      "anyOf": [
        {
          "maxLength": 500,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "文件名",
      "title": "Filename"
    },
    "tags": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "description": "标签列表",
      "title": "Tags"
    }
  },
  "title": "ProjectFileUpdate",
  "type": "object"
}
```

### ProjectFileUploadUrlResponse

```json
{
  "description": "项目文件 MongoDB 一次性上传 URL 响应。",
  "properties": {
    "expires_in": {
      "description": "URL有效期（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "oss_key": {
      "description": "兼容旧客户端的 storage_key 别名",
      "title": "Oss Key",
      "type": "string"
    },
    "storage_key": {
      "description": "MongoDB GridFS 逻辑存储键",
      "title": "Storage Key",
      "type": "string"
    },
    "upload_url": {
      "description": "上传预签名URL",
      "title": "Upload Url",
      "type": "string"
    }
  },
  "required": [
    "upload_url",
    "storage_key",
    "oss_key",
    "expires_in"
  ],
  "title": "ProjectFileUploadUrlResponse",
  "type": "object"
}
```

### ProjectFinanceEntryCreate

```json
{
  "description": "创建项目财务条目",
  "properties": {
    "amount": {
      "description": "金额（人民币）",
      "title": "Amount",
      "type": "number"
    },
    "date": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目日期",
      "title": "Date"
    },
    "entry_type": {
      "description": "类型（income=收入, expense=支出）",
      "pattern": "^(income|expense)$",
      "title": "Entry Type",
      "type": "string"
    },
    "name": {
      "description": "条目名称",
      "maxLength": 200,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "note": {
      "anyOf": [
        {
          "maxLength": 2000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目说明",
      "title": "Note"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "status": {
      "anyOf": [
        {
          "pattern": "^(verified|unverified)$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目状态（仅管理员可设置）",
      "title": "Status"
    },
    "tags": {
      "description": "标签列表",
      "items": {
        "type": "string"
      },
      "title": "Tags",
      "type": "array"
    }
  },
  "required": [
    "project_id",
    "name",
    "amount",
    "entry_type"
  ],
  "title": "ProjectFinanceEntryCreate",
  "type": "object"
}
```

### ProjectFinanceEntryListResponse

```json
{
  "description": "财务条目列表响应",
  "properties": {
    "balance": {
      "description": "余额（收入和支出之和）",
      "title": "Balance",
      "type": "number"
    },
    "items": {
      "description": "条目列表",
      "items": {
        "$ref": "#/components/schemas/ProjectFinanceEntryResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    },
    "total_expense": {
      "description": "已核对支出总和（负数）",
      "title": "Total Expense",
      "type": "number"
    },
    "total_income": {
      "description": "已核对收入总和",
      "title": "Total Income",
      "type": "number"
    }
  },
  "required": [
    "total",
    "items",
    "total_income",
    "total_expense",
    "balance"
  ],
  "title": "ProjectFinanceEntryListResponse",
  "type": "object"
}
```

### ProjectFinanceEntryResponse

```json
{
  "description": "财务条目响应",
  "properties": {
    "amount": {
      "description": "金额（人民币）",
      "title": "Amount",
      "type": "number"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "created_by_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "创建者ID",
      "title": "Created By Id"
    },
    "date": {
      "description": "条目日期",
      "format": "date-time",
      "title": "Date",
      "type": "string"
    },
    "entry_type": {
      "description": "条目类型（income=收入, expense=支出）",
      "title": "Entry Type",
      "type": "string"
    },
    "id": {
      "description": "条目ID",
      "title": "Id",
      "type": "string"
    },
    "name": {
      "description": "条目名称",
      "title": "Name",
      "type": "string"
    },
    "note": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目说明",
      "title": "Note"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "status": {
      "description": "条目状态（verified=已核对, unverified=未核对）",
      "title": "Status",
      "type": "string"
    },
    "tags": {
      "description": "标签列表",
      "items": {
        "type": "string"
      },
      "title": "Tags",
      "type": "array"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    },
    "verified_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "核对时间",
      "title": "Verified At"
    },
    "verified_by_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "核对人ID（管理员）",
      "title": "Verified By Id"
    }
  },
  "required": [
    "id",
    "project_id",
    "name",
    "status",
    "tags",
    "amount",
    "entry_type",
    "date",
    "created_at"
  ],
  "title": "ProjectFinanceEntryResponse",
  "type": "object"
}
```

### ProjectFinanceEntryUpdate

```json
{
  "description": "更新项目财务条目",
  "properties": {
    "amount": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "description": "金额（人民币）",
      "title": "Amount"
    },
    "date": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目日期",
      "title": "Date"
    },
    "entry_type": {
      "anyOf": [
        {
          "pattern": "^(income|expense)$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "类型（income=收入, expense=支出）",
      "title": "Entry Type"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 200,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目名称",
      "title": "Name"
    },
    "note": {
      "anyOf": [
        {
          "maxLength": 2000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目说明",
      "title": "Note"
    },
    "status": {
      "anyOf": [
        {
          "pattern": "^(verified|unverified)$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "条目状态（仅管理员可设置）",
      "title": "Status"
    },
    "tags": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "description": "标签列表",
      "title": "Tags"
    }
  },
  "title": "ProjectFinanceEntryUpdate",
  "type": "object"
}
```

### ProjectLinkCreate

```json
{
  "description": "创建项目链接",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 500,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "链接描述",
      "title": "Description"
    },
    "name": {
      "description": "链接名称",
      "maxLength": 200,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "url": {
      "description": "链接URL",
      "maxLength": 2000,
      "minLength": 1,
      "title": "Url",
      "type": "string"
    }
  },
  "required": [
    "project_id",
    "name",
    "url"
  ],
  "title": "ProjectLinkCreate",
  "type": "object"
}
```

### ProjectLinkListResponse

```json
{
  "description": "项目链接列表响应",
  "properties": {
    "items": {
      "description": "链接列表",
      "items": {
        "$ref": "#/components/schemas/ProjectLinkResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "ProjectLinkListResponse",
  "type": "object"
}
```

### ProjectLinkResponse

```json
{
  "description": "项目链接响应",
  "properties": {
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "链接描述",
      "title": "Description"
    },
    "id": {
      "description": "链接ID",
      "title": "Id",
      "type": "string"
    },
    "name": {
      "description": "链接名称",
      "title": "Name",
      "type": "string"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    },
    "url": {
      "description": "链接URL",
      "title": "Url",
      "type": "string"
    }
  },
  "required": [
    "id",
    "project_id",
    "name",
    "url",
    "created_at"
  ],
  "title": "ProjectLinkResponse",
  "type": "object"
}
```

### ProjectLinkUpdate

```json
{
  "description": "更新项目链接",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 500,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "链接描述",
      "title": "Description"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 200,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "链接名称",
      "title": "Name"
    },
    "url": {
      "anyOf": [
        {
          "maxLength": 2000,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "链接URL",
      "title": "Url"
    }
  },
  "title": "ProjectLinkUpdate",
  "type": "object"
}
```

### ProjectListResponse

```json
{
  "description": "项目列表响应",
  "properties": {
    "items": {
      "description": "项目列表",
      "items": {
        "$ref": "#/components/schemas/ProjectResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "ProjectListResponse",
  "type": "object"
}
```

### ProjectRatingUpdate

```json
{
  "description": "更新项目评分",
  "properties": {
    "rating": {
      "description": "项目评分（1-5）",
      "maximum": 5.0,
      "minimum": 1.0,
      "title": "Rating",
      "type": "integer"
    }
  },
  "required": [
    "rating"
  ],
  "title": "ProjectRatingUpdate",
  "type": "object"
}
```

### ProjectResponse

```json
{
  "description": "项目响应",
  "properties": {
    "completion_rate": {
      "default": 0.0,
      "description": "完成度（百分比，0-100）",
      "maximum": 100.0,
      "minimum": 0.0,
      "title": "Completion Rate",
      "type": "number"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "项目描述",
      "title": "Description"
    },
    "id": {
      "description": "项目ID",
      "title": "Id",
      "type": "string"
    },
    "name": {
      "description": "项目名称",
      "title": "Name",
      "type": "string"
    },
    "order": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/OrderSnapshot"
        },
        {
          "type": "null"
        }
      ]
    },
    "overview_markdown": {
      "description": "项目概述（Markdown格式）",
      "title": "Overview Markdown",
      "type": "string"
    },
    "owner_email": {
      "description": "所属用户邮箱",
      "format": "email",
      "title": "Owner Email",
      "type": "string"
    },
    "owner_id": {
      "description": "所属用户ID",
      "title": "Owner Id",
      "type": "string"
    },
    "rating": {
      "description": "项目评分（1-5）",
      "maximum": 5.0,
      "minimum": 1.0,
      "title": "Rating",
      "type": "integer"
    },
    "responsible_tag": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/ProjectResponsibleTagSummary"
        },
        {
          "type": "null"
        }
      ],
      "description": "负责人摘要"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    }
  },
  "required": [
    "id",
    "owner_id",
    "owner_email",
    "name",
    "overview_markdown",
    "rating",
    "created_at"
  ],
  "title": "ProjectResponse",
  "type": "object"
}
```

### ProjectResponsibleTagSummary

```json
{
  "description": "项目负责人摘要",
  "properties": {
    "id": {
      "description": "负责人ID",
      "title": "Id",
      "type": "string"
    },
    "label": {
      "description": "负责人名称",
      "title": "Label",
      "type": "string"
    }
  },
  "required": [
    "id",
    "label"
  ],
  "title": "ProjectResponsibleTagSummary",
  "type": "object"
}
```

### ProjectResponsibleTagUpdate

```json
{
  "description": "更新项目负责人",
  "properties": {
    "responsible_tag_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "负责人ID（为null表示清除）",
      "title": "Responsible Tag Id"
    }
  },
  "title": "ProjectResponsibleTagUpdate",
  "type": "object"
}
```

### ProjectTaskCreate

```json
{
  "description": "创建项目任务",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 2000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "任务详情",
      "title": "Description"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "title": {
      "description": "任务标题",
      "maxLength": 200,
      "minLength": 1,
      "title": "Title",
      "type": "string"
    }
  },
  "required": [
    "project_id",
    "title"
  ],
  "title": "ProjectTaskCreate",
  "type": "object"
}
```

### ProjectTaskListResponse

```json
{
  "description": "项目任务列表响应",
  "properties": {
    "items": {
      "description": "任务列表",
      "items": {
        "$ref": "#/components/schemas/ProjectTaskResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "ProjectTaskListResponse",
  "type": "object"
}
```

### ProjectTaskResponse

```json
{
  "description": "项目任务响应",
  "properties": {
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "任务详情",
      "title": "Description"
    },
    "id": {
      "description": "任务ID",
      "title": "Id",
      "type": "string"
    },
    "project_id": {
      "description": "项目ID",
      "title": "Project Id",
      "type": "string"
    },
    "status": {
      "description": "任务状态（pending=未完成, completed=已完成）",
      "title": "Status",
      "type": "string"
    },
    "title": {
      "description": "任务标题",
      "title": "Title",
      "type": "string"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    }
  },
  "required": [
    "id",
    "project_id",
    "title",
    "status",
    "created_at"
  ],
  "title": "ProjectTaskResponse",
  "type": "object"
}
```

### ProjectTaskUpdate

```json
{
  "description": "更新项目任务",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 2000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "任务详情",
      "title": "Description"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "任务状态（pending=未完成, completed=已完成）",
      "title": "Status"
    },
    "title": {
      "anyOf": [
        {
          "maxLength": 200,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "任务标题",
      "title": "Title"
    }
  },
  "title": "ProjectTaskUpdate",
  "type": "object"
}
```

### ProjectUpdate

```json
{
  "description": "管理员更新项目",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 1000,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "项目描述",
      "title": "Description"
    },
    "name": {
      "anyOf": [
        {
          "maxLength": 200,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "项目名称",
      "title": "Name"
    },
    "overview_markdown": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "项目概述（Markdown格式）",
      "title": "Overview Markdown"
    },
    "rating": {
      "anyOf": [
        {
          "maximum": 5.0,
          "minimum": 1.0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "description": "项目评分（1-5）",
      "title": "Rating"
    },
    "responsible_tag_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "负责人ID（传null可清除）",
      "title": "Responsible Tag Id"
    }
  },
  "title": "ProjectUpdate",
  "type": "object"
}
```

### PydanticObjectId

```json
{
  "example": "5eb7cf5a86d9755df3a6c593",
  "maxLength": 24,
  "minLength": 24,
  "pattern": "^[0-9a-f]{24}$",
  "type": "string"
}
```

### RecoveryCodesResponse

```json
{
  "description": "仅在生成时返回一次的恢复码。",
  "properties": {
    "message": {
      "title": "Message",
      "type": "string"
    },
    "recovery_codes": {
      "items": {
        "type": "string"
      },
      "title": "Recovery Codes",
      "type": "array"
    }
  },
  "required": [
    "message",
    "recovery_codes"
  ],
  "title": "RecoveryCodesResponse",
  "type": "object"
}
```

### ReferralSnapshot

```json
{
  "properties": {
    "agent_id": {
      "title": "Agent Id",
      "type": "string"
    },
    "code": {
      "title": "Code",
      "type": "string"
    },
    "level": {
      "title": "Level",
      "type": "integer"
    },
    "rate_bps": {
      "title": "Rate Bps",
      "type": "integer"
    },
    "revision": {
      "title": "Revision",
      "type": "integer"
    }
  },
  "required": [
    "agent_id",
    "code",
    "level",
    "rate_bps",
    "revision"
  ],
  "title": "ReferralSnapshot",
  "type": "object"
}
```

### ResponsibleTagCreate

```json
{
  "description": "创建负责人",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 500,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "标签描述",
      "title": "Description"
    },
    "label": {
      "description": "标签名称",
      "maxLength": 100,
      "minLength": 1,
      "title": "Label",
      "type": "string"
    }
  },
  "required": [
    "label"
  ],
  "title": "ResponsibleTagCreate",
  "type": "object"
}
```

### ResponsibleTagListResponse

```json
{
  "description": "负责人列表响应",
  "properties": {
    "items": {
      "description": "标签列表",
      "items": {
        "$ref": "#/components/schemas/ResponsibleTagResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "ResponsibleTagListResponse",
  "type": "object"
}
```

### ResponsibleTagResponse

```json
{
  "description": "负责人响应",
  "properties": {
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "标签描述",
      "title": "Description"
    },
    "id": {
      "description": "标签ID",
      "title": "Id",
      "type": "string"
    },
    "is_active": {
      "description": "是否可用",
      "title": "Is Active",
      "type": "boolean"
    },
    "label": {
      "description": "标签名称",
      "title": "Label",
      "type": "string"
    },
    "updated_at": {
      "description": "更新时间",
      "format": "date-time",
      "title": "Updated At",
      "type": "string"
    }
  },
  "required": [
    "id",
    "label",
    "is_active",
    "created_at",
    "updated_at"
  ],
  "title": "ResponsibleTagResponse",
  "type": "object"
}
```

### ResponsibleTagUpdate

```json
{
  "description": "更新负责人",
  "properties": {
    "description": {
      "anyOf": [
        {
          "maxLength": 500,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "标签描述",
      "title": "Description"
    },
    "is_active": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "是否可用",
      "title": "Is Active"
    },
    "label": {
      "anyOf": [
        {
          "maxLength": 100,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "标签名称",
      "title": "Label"
    }
  },
  "title": "ResponsibleTagUpdate",
  "type": "object"
}
```

### SMSLoginRequest

```json
{
  "description": "短信登录请求Schema",
  "properties": {
    "phone_number": {
      "description": "手机号码",
      "maxLength": 11,
      "minLength": 11,
      "title": "Phone Number",
      "type": "string"
    },
    "verification_code": {
      "description": "短信验证码",
      "maxLength": 6,
      "minLength": 6,
      "title": "Verification Code",
      "type": "string"
    }
  },
  "required": [
    "phone_number",
    "verification_code"
  ],
  "title": "SMSLoginRequest",
  "type": "object"
}
```

### SMSResetPasswordRequest

```json
{
  "description": "短信重置密码请求Schema",
  "properties": {
    "new_password": {
      "description": "新密码",
      "maxLength": 128,
      "minLength": 8,
      "title": "New Password",
      "type": "string"
    },
    "phone_number": {
      "description": "手机号码",
      "maxLength": 11,
      "minLength": 11,
      "title": "Phone Number",
      "type": "string"
    },
    "verification_code": {
      "description": "短信验证码",
      "maxLength": 6,
      "minLength": 6,
      "title": "Verification Code",
      "type": "string"
    }
  },
  "required": [
    "phone_number",
    "verification_code",
    "new_password"
  ],
  "title": "SMSResetPasswordRequest",
  "type": "object"
}
```

### SMSResetPasswordResponse

```json
{
  "description": "短信重置密码响应Schema",
  "properties": {
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    },
    "phone_number": {
      "description": "手机号码",
      "title": "Phone Number",
      "type": "string"
    }
  },
  "required": [
    "message",
    "phone_number"
  ],
  "title": "SMSResetPasswordResponse",
  "type": "object"
}
```

### Selection

```json
{
  "additionalProperties": false,
  "properties": {
    "item_ids": {
      "items": {
        "type": "string"
      },
      "maxItems": 100,
      "title": "Item Ids",
      "type": "array"
    },
    "plan": {
      "default": "popular",
      "enum": [
        "custom",
        "popular"
      ],
      "title": "Plan",
      "type": "string"
    },
    "requirements": {
      "default": "",
      "maxLength": 1000,
      "title": "Requirements",
      "type": "string"
    }
  },
  "title": "Selection",
  "type": "object"
}
```

### SendCommonEmailRequest

```json
{
  "description": "发送通用邮件请求",
  "properties": {
    "content": {
      "maxLength": 50000,
      "minLength": 1,
      "title": "Content",
      "type": "string"
    },
    "message_id": {
      "maxLength": 128,
      "minLength": 1,
      "pattern": "^[A-Za-z0-9._:-]+$",
      "title": "Message Id",
      "type": "string"
    },
    "recipients": {
      "items": {
        "format": "email",
        "type": "string"
      },
      "maxItems": 50,
      "minItems": 1,
      "title": "Recipients",
      "type": "array"
    },
    "title": {
      "maxLength": 200,
      "minLength": 1,
      "title": "Title",
      "type": "string"
    }
  },
  "required": [
    "title",
    "content",
    "message_id",
    "recipients"
  ],
  "title": "SendCommonEmailRequest",
  "type": "object"
}
```

### SendCommonEmailResponse

```json
{
  "description": "发送通用邮件响应",
  "properties": {
    "message": {
      "title": "Message",
      "type": "string"
    },
    "message_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Message Id"
    },
    "recipients": {
      "items": {
        "type": "string"
      },
      "title": "Recipients",
      "type": "array"
    },
    "success": {
      "title": "Success",
      "type": "boolean"
    }
  },
  "required": [
    "success",
    "message",
    "recipients"
  ],
  "title": "SendCommonEmailResponse",
  "type": "object"
}
```

### SendSMSCodeRequest

```json
{
  "description": "发送短信验证码请求Schema",
  "properties": {
    "phone_number": {
      "description": "手机号码",
      "maxLength": 11,
      "minLength": 11,
      "title": "Phone Number",
      "type": "string"
    }
  },
  "required": [
    "phone_number"
  ],
  "title": "SendSMSCodeRequest",
  "type": "object"
}
```

### SendSMSCodeResponse

```json
{
  "description": "发送短信验证码响应Schema",
  "properties": {
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    },
    "phone_number": {
      "description": "手机号码",
      "title": "Phone Number",
      "type": "string"
    }
  },
  "required": [
    "message",
    "phone_number"
  ],
  "title": "SendSMSCodeResponse",
  "type": "object"
}
```

### SendVerificationCodeRequest

```json
{
  "description": "发送验证码请求Schema",
  "properties": {
    "email": {
      "description": "邮箱地址",
      "format": "email",
      "title": "Email",
      "type": "string"
    }
  },
  "required": [
    "email"
  ],
  "title": "SendVerificationCodeRequest",
  "type": "object"
}
```

### SendVerificationCodeResponse

```json
{
  "description": "发送验证码响应Schema",
  "properties": {
    "email": {
      "description": "邮箱地址",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "message",
    "email"
  ],
  "title": "SendVerificationCodeResponse",
  "type": "object"
}
```

### ShopItem

```json
{
  "properties": {
    "active": {
      "default": true,
      "title": "Active",
      "type": "boolean"
    },
    "custom_price": {
      "maximum": 100000000.0,
      "minimum": 0.0,
      "title": "Custom Price",
      "type": "integer"
    },
    "description": {
      "default": "",
      "maxLength": 1000,
      "title": "Description",
      "type": "string"
    },
    "group": {
      "default": "",
      "maxLength": 100,
      "title": "Group",
      "type": "string"
    },
    "id": {
      "maxLength": 64,
      "minLength": 1,
      "pattern": "^[a-zA-Z0-9_-]+$",
      "title": "Id",
      "type": "string"
    },
    "name": {
      "maxLength": 100,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "popular_price": {
      "maximum": 100000000.0,
      "minimum": 0.0,
      "title": "Popular Price",
      "type": "integer"
    }
  },
  "required": [
    "id",
    "name",
    "custom_price",
    "popular_price"
  ],
  "title": "ShopItem",
  "type": "object"
}
```

### ShopPlan

```json
{
  "properties": {
    "delivery": {
      "maxLength": 200,
      "minLength": 1,
      "title": "Delivery",
      "type": "string"
    },
    "id": {
      "enum": [
        "custom",
        "popular"
      ],
      "title": "Id",
      "type": "string"
    },
    "name": {
      "maxLength": 100,
      "minLength": 1,
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "delivery"
  ],
  "title": "ShopPlan",
  "type": "object"
}
```

### SystemKeyActionResponse

```json
{
  "properties": {
    "key": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/SystemKeyRead"
        },
        {
          "type": "null"
        }
      ]
    },
    "message": {
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "message"
  ],
  "title": "SystemKeyActionResponse",
  "type": "object"
}
```

### SystemKeyAuditListResponse

```json
{
  "properties": {
    "items": {
      "items": {
        "$ref": "#/components/schemas/SystemKeyAuditRead"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "SystemKeyAuditListResponse",
  "type": "object"
}
```

### SystemKeyAuditRead

```json
{
  "properties": {
    "actor_id": {
      "title": "Actor Id",
      "type": "string"
    },
    "actor_ip": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Actor Ip"
    },
    "created_at": {
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "details": {
      "additionalProperties": true,
      "title": "Details",
      "type": "object"
    },
    "event_type": {
      "title": "Event Type",
      "type": "string"
    },
    "id": {
      "title": "Id",
      "type": "string"
    },
    "kid": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Kid"
    },
    "message": {
      "title": "Message",
      "type": "string"
    },
    "outcome": {
      "title": "Outcome",
      "type": "string"
    },
    "purpose": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/SystemKeyPurpose"
        },
        {
          "type": "null"
        }
      ]
    },
    "request_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Request Id"
    }
  },
  "required": [
    "id",
    "event_type",
    "outcome",
    "purpose",
    "kid",
    "actor_id",
    "actor_ip",
    "request_id",
    "message",
    "details",
    "created_at"
  ],
  "title": "SystemKeyAuditRead",
  "type": "object"
}
```

### SystemKeyGenerateRequest

```json
{
  "properties": {
    "expires_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Expires At"
    },
    "kid": {
      "anyOf": [
        {
          "maxLength": 128,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Kid"
    },
    "purpose": {
      "$ref": "#/components/schemas/SystemKeyPurpose"
    },
    "rsa_bits": {
      "anyOf": [
        {
          "maximum": 8192.0,
          "minimum": 2048.0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "Rsa Bits"
    }
  },
  "required": [
    "purpose"
  ],
  "title": "SystemKeyGenerateRequest",
  "type": "object"
}
```

### SystemKeyHealthResponse

```json
{
  "properties": {
    "cache_loaded_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Cache Loaded At"
    },
    "load_errors": {
      "additionalProperties": {
        "type": "string"
      },
      "title": "Load Errors",
      "type": "object"
    },
    "purposes": {
      "additionalProperties": {
        "$ref": "#/components/schemas/SystemKeyPurposeHealth"
      },
      "title": "Purposes",
      "type": "object"
    },
    "status": {
      "title": "Status",
      "type": "string"
    }
  },
  "required": [
    "status",
    "purposes",
    "load_errors",
    "cache_loaded_at"
  ],
  "title": "SystemKeyHealthResponse",
  "type": "object"
}
```

### SystemKeyKind

```json
{
  "enum": [
    "rsa_private_key",
    "symmetric_secret"
  ],
  "title": "SystemKeyKind",
  "type": "string"
}
```

### SystemKeyListResponse

```json
{
  "properties": {
    "items": {
      "items": {
        "$ref": "#/components/schemas/SystemKeyRead"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "SystemKeyListResponse",
  "type": "object"
}
```

### SystemKeyPurpose

```json
{
  "description": "系统内部密钥用途；每个用途拥有独立的激活指针。",
  "enum": [
    "oauth_signing",
    "internal_jwt",
    "totp_encryption",
    "application_key_hmac",
    "verification_code_hmac"
  ],
  "title": "SystemKeyPurpose",
  "type": "string"
}
```

### SystemKeyPurposeHealth

```json
{
  "properties": {
    "active_kid": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Active Kid"
    },
    "message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Message"
    },
    "revision": {
      "title": "Revision",
      "type": "integer"
    },
    "status": {
      "title": "Status",
      "type": "string"
    }
  },
  "required": [
    "active_kid",
    "revision",
    "status",
    "message"
  ],
  "title": "SystemKeyPurposeHealth",
  "type": "object"
}
```

### SystemKeyRead

```json
{
  "properties": {
    "activated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Activated At"
    },
    "activated_by": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Activated By"
    },
    "algorithm": {
      "title": "Algorithm",
      "type": "string"
    },
    "created_at": {
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "created_by": {
      "title": "Created By",
      "type": "string"
    },
    "delete_after": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Delete After"
    },
    "disabled_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Disabled At"
    },
    "expires_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Expires At"
    },
    "failure_count": {
      "title": "Failure Count",
      "type": "integer"
    },
    "fingerprint_sha256": {
      "title": "Fingerprint Sha256",
      "type": "string"
    },
    "is_active": {
      "title": "Is Active",
      "type": "boolean"
    },
    "key_size": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "Key Size"
    },
    "kid": {
      "title": "Kid",
      "type": "string"
    },
    "kind": {
      "$ref": "#/components/schemas/SystemKeyKind"
    },
    "last_error": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Last Error"
    },
    "last_validated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Last Validated At"
    },
    "not_before": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Not Before"
    },
    "publish_in_jwks": {
      "title": "Publish In Jwks",
      "type": "boolean"
    },
    "purpose": {
      "$ref": "#/components/schemas/SystemKeyPurpose"
    },
    "retired_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Retired At"
    },
    "schema_version": {
      "title": "Schema Version",
      "type": "integer"
    },
    "status": {
      "$ref": "#/components/schemas/SystemKeyStatus"
    }
  },
  "required": [
    "kid",
    "purpose",
    "kind",
    "algorithm",
    "status",
    "is_active",
    "publish_in_jwks",
    "fingerprint_sha256",
    "key_size",
    "schema_version",
    "created_at",
    "created_by",
    "activated_at",
    "activated_by",
    "retired_at",
    "disabled_at",
    "not_before",
    "expires_at",
    "delete_after",
    "last_validated_at",
    "last_error",
    "failure_count"
  ],
  "title": "SystemKeyRead",
  "type": "object"
}
```

### SystemKeyReconcileResponse

```json
{
  "properties": {
    "expired": {
      "title": "Expired",
      "type": "integer"
    },
    "healthy": {
      "title": "Healthy",
      "type": "integer"
    },
    "invalid": {
      "title": "Invalid",
      "type": "integer"
    },
    "message": {
      "title": "Message",
      "type": "string"
    },
    "orphaned_active": {
      "title": "Orphaned Active",
      "type": "integer"
    }
  },
  "required": [
    "message",
    "healthy",
    "invalid",
    "expired",
    "orphaned_active"
  ],
  "title": "SystemKeyReconcileResponse",
  "type": "object"
}
```

### SystemKeyStatus

```json
{
  "enum": [
    "pending",
    "active",
    "retired",
    "disabled",
    "error"
  ],
  "title": "SystemKeyStatus",
  "type": "string"
}
```

### SystemPublicKeyResponse

```json
{
  "properties": {
    "algorithm": {
      "title": "Algorithm",
      "type": "string"
    },
    "fingerprint_sha256": {
      "title": "Fingerprint Sha256",
      "type": "string"
    },
    "kid": {
      "title": "Kid",
      "type": "string"
    },
    "public_key_pem": {
      "title": "Public Key Pem",
      "type": "string"
    }
  },
  "required": [
    "kid",
    "algorithm",
    "fingerprint_sha256",
    "public_key_pem"
  ],
  "title": "SystemPublicKeyResponse",
  "type": "object"
}
```

### TicketCreate

```json
{
  "description": "创建工单Schema",
  "properties": {
    "content": {
      "description": "工单内容",
      "minLength": 1,
      "title": "Content",
      "type": "string"
    },
    "ticket_type": {
      "$ref": "#/components/schemas/TicketType",
      "description": "工单类型"
    },
    "title": {
      "description": "工单标题",
      "maxLength": 200,
      "minLength": 1,
      "title": "Title",
      "type": "string"
    }
  },
  "required": [
    "title",
    "ticket_type",
    "content"
  ],
  "title": "TicketCreate",
  "type": "object"
}
```

### TicketListResponse

```json
{
  "description": "工单列表响应Schema",
  "properties": {
    "items": {
      "description": "工单列表",
      "items": {
        "$ref": "#/components/schemas/TicketResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total",
    "items"
  ],
  "title": "TicketListResponse",
  "type": "object"
}
```

### TicketReply

```json
{
  "description": "回复工单Schema（管理员）",
  "properties": {
    "feedback": {
      "description": "反馈结果",
      "minLength": 1,
      "title": "Feedback",
      "type": "string"
    }
  },
  "required": [
    "feedback"
  ],
  "title": "TicketReply",
  "type": "object"
}
```

### TicketResponse

```json
{
  "description": "工单响应Schema",
  "properties": {
    "content": {
      "description": "工单内容",
      "minLength": 1,
      "title": "Content",
      "type": "string"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "creator_email": {
      "description": "创建者邮箱",
      "title": "Creator Email",
      "type": "string"
    },
    "feedback": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "反馈结果",
      "title": "Feedback"
    },
    "id": {
      "description": "工单ID",
      "title": "Id",
      "type": "string"
    },
    "replied_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "回复时间",
      "title": "Replied At"
    },
    "responder_email": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "回复者邮箱",
      "title": "Responder Email"
    },
    "status": {
      "$ref": "#/components/schemas/TicketStatus",
      "description": "工单状态"
    },
    "ticket_type": {
      "$ref": "#/components/schemas/TicketType",
      "description": "工单类型"
    },
    "title": {
      "description": "工单标题",
      "maxLength": 200,
      "minLength": 1,
      "title": "Title",
      "type": "string"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    }
  },
  "required": [
    "title",
    "ticket_type",
    "content",
    "id",
    "status",
    "creator_email",
    "created_at"
  ],
  "title": "TicketResponse",
  "type": "object"
}
```

### TicketStatus

```json
{
  "description": "工单状态枚举",
  "enum": [
    "pending",
    "replied"
  ],
  "title": "TicketStatus",
  "type": "string"
}
```

### TicketType

```json
{
  "description": "工单类型枚举",
  "enum": [
    "financial",
    "technical",
    "business"
  ],
  "title": "TicketType",
  "type": "string"
}
```

### TicketUpdate

```json
{
  "description": "更新工单Schema（仅客户可用）",
  "properties": {
    "content": {
      "anyOf": [
        {
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "工单内容",
      "title": "Content"
    },
    "title": {
      "anyOf": [
        {
          "maxLength": 200,
          "minLength": 1,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "工单标题",
      "title": "Title"
    }
  },
  "title": "TicketUpdate",
  "type": "object"
}
```

### Token

```json
{
  "description": "Token响应Schema",
  "properties": {
    "access_token": {
      "description": "访问令牌",
      "title": "Access Token",
      "type": "string"
    },
    "expires_in": {
      "description": "过期时间（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "token_type": {
      "default": "bearer",
      "description": "令牌类型",
      "title": "Token Type",
      "type": "string"
    }
  },
  "required": [
    "access_token",
    "expires_in"
  ],
  "title": "Token",
  "type": "object"
}
```

### TokenResponse

```json
{
  "properties": {
    "access_token": {
      "title": "Access Token",
      "type": "string"
    },
    "expires_in": {
      "title": "Expires In",
      "type": "integer"
    },
    "id_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Id Token"
    },
    "refresh_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Refresh Token"
    },
    "scope": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Scope"
    },
    "token_type": {
      "default": "Bearer",
      "title": "Token Type",
      "type": "string"
    }
  },
  "required": [
    "access_token",
    "expires_in"
  ],
  "title": "TokenResponse",
  "type": "object"
}
```

### TotpCodeRequest

```json
{
  "description": "验证当前 TOTP 或恢复码。",
  "properties": {
    "code": {
      "maxLength": 32,
      "minLength": 6,
      "title": "Code",
      "type": "string"
    }
  },
  "required": [
    "code"
  ],
  "title": "TotpCodeRequest",
  "type": "object"
}
```

### TotpConfirmRequest

```json
{
  "description": "确认启用 TOTP。",
  "properties": {
    "code": {
      "maxLength": 6,
      "minLength": 6,
      "title": "Code",
      "type": "string"
    },
    "setup_token": {
      "maxLength": 256,
      "minLength": 32,
      "title": "Setup Token",
      "type": "string"
    }
  },
  "required": [
    "setup_token",
    "code"
  ],
  "title": "TotpConfirmRequest",
  "type": "object"
}
```

### TotpSetupResponse

```json
{
  "description": "TOTP 设置所需的扫码信息。",
  "properties": {
    "expires_in": {
      "description": "设置会话有效期（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "otpauth_uri": {
      "description": "认证器应用可扫描的 otpauth URI",
      "title": "Otpauth Uri",
      "type": "string"
    },
    "secret": {
      "description": "供无法扫码时手动输入的 TOTP 密钥",
      "title": "Secret",
      "type": "string"
    },
    "setup_token": {
      "description": "确认设置时使用的短期令牌",
      "title": "Setup Token",
      "type": "string"
    }
  },
  "required": [
    "setup_token",
    "secret",
    "otpauth_uri",
    "expires_in"
  ],
  "title": "TotpSetupResponse",
  "type": "object"
}
```

### TotpStatusResponse

```json
{
  "description": "当前用户的二次验证状态。",
  "properties": {
    "enabled": {
      "title": "Enabled",
      "type": "boolean"
    },
    "has_passkeys": {
      "title": "Has Passkeys",
      "type": "boolean"
    },
    "passkey_enabled": {
      "title": "Passkey Enabled",
      "type": "boolean"
    },
    "recovery_codes_remaining": {
      "minimum": 0.0,
      "title": "Recovery Codes Remaining",
      "type": "integer"
    }
  },
  "required": [
    "enabled",
    "recovery_codes_remaining",
    "passkey_enabled",
    "has_passkeys"
  ],
  "title": "TotpStatusResponse",
  "type": "object"
}
```

### TwoFactorActionResponse

```json
{
  "description": "TOTP 状态变更响应。",
  "properties": {
    "enabled": {
      "title": "Enabled",
      "type": "boolean"
    },
    "message": {
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "message",
    "enabled"
  ],
  "title": "TwoFactorActionResponse",
  "type": "object"
}
```

### TwoFactorChallengeResponse

```json
{
  "description": "第一步登录成功后返回的 TOTP 挑战。",
  "properties": {
    "challenge_token": {
      "description": "短期一次性二次验证令牌",
      "title": "Challenge Token",
      "type": "string"
    },
    "expires_in": {
      "description": "挑战有效期（秒）",
      "title": "Expires In",
      "type": "integer"
    },
    "requires_2fa": {
      "const": true,
      "default": true,
      "title": "Requires 2Fa",
      "type": "boolean"
    }
  },
  "required": [
    "challenge_token",
    "expires_in"
  ],
  "title": "TwoFactorChallengeResponse",
  "type": "object"
}
```

### TwoFactorVerifyRequest

```json
{
  "description": "完成登录二次验证。",
  "properties": {
    "challenge_token": {
      "maxLength": 256,
      "minLength": 32,
      "title": "Challenge Token",
      "type": "string"
    },
    "code": {
      "description": "TOTP 或一次性恢复码",
      "maxLength": 32,
      "minLength": 6,
      "title": "Code",
      "type": "string"
    }
  },
  "required": [
    "challenge_token",
    "code"
  ],
  "title": "TwoFactorVerifyRequest",
  "type": "object"
}
```

### UserActionResponse

```json
{
  "description": "通用用户操作响应",
  "properties": {
    "message": {
      "description": "响应消息",
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "message"
  ],
  "title": "UserActionResponse",
  "type": "object"
}
```

### UserListResponse

```json
{
  "description": "用户列表响应",
  "properties": {
    "items": {
      "description": "用户列表",
      "items": {
        "$ref": "#/components/schemas/UserResponse"
      },
      "title": "Items",
      "type": "array"
    },
    "total": {
      "description": "总数",
      "minimum": 0.0,
      "title": "Total",
      "type": "integer"
    }
  },
  "required": [
    "total"
  ],
  "title": "UserListResponse",
  "type": "object"
}
```

### UserLogin

```json
{
  "description": "用户登录Schema",
  "properties": {
    "email": {
      "description": "用户邮箱",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "password": {
      "description": "密码",
      "maxLength": 128,
      "minLength": 1,
      "title": "Password",
      "type": "string"
    }
  },
  "required": [
    "email",
    "password"
  ],
  "title": "UserLogin",
  "type": "object"
}
```

### UserPasswordChangeRequest

```json
{
  "description": "用户修改密码",
  "properties": {
    "new_password": {
      "description": "新密码",
      "maxLength": 128,
      "minLength": 8,
      "title": "New Password",
      "type": "string"
    },
    "old_password": {
      "description": "当前密码",
      "maxLength": 128,
      "minLength": 8,
      "title": "Old Password",
      "type": "string"
    }
  },
  "required": [
    "old_password",
    "new_password"
  ],
  "title": "UserPasswordChangeRequest",
  "type": "object"
}
```

### UserProfileUpdate

```json
{
  "description": "用户自助资料更新",
  "properties": {
    "avatar_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "头像URL",
      "title": "Avatar Url"
    },
    "bio": {
      "anyOf": [
        {
          "maxLength": 256,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "个人简介",
      "title": "Bio"
    },
    "full_name": {
      "anyOf": [
        {
          "maxLength": 64,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户姓名",
      "title": "Full Name"
    },
    "phone_number": {
      "anyOf": [
        {
          "maxLength": 32,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Phone Number"
    }
  },
  "title": "UserProfileUpdate",
  "type": "object"
}
```

### UserRegister

```json
{
  "description": "用户注册Schema",
  "properties": {
    "email": {
      "description": "用户邮箱",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "password": {
      "description": "密码（8-128位）",
      "maxLength": 128,
      "minLength": 8,
      "title": "Password",
      "type": "string"
    },
    "verification_code": {
      "description": "邮箱验证码",
      "maxLength": 6,
      "minLength": 6,
      "title": "Verification Code",
      "type": "string"
    }
  },
  "required": [
    "email",
    "password",
    "verification_code"
  ],
  "title": "UserRegister",
  "type": "object"
}
```

### UserResponse

```json
{
  "description": "用户响应Schema",
  "properties": {
    "avatar_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "头像URL",
      "title": "Avatar Url"
    },
    "bio": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "个人简介",
      "title": "Bio"
    },
    "created_at": {
      "description": "创建时间",
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "email": {
      "description": "用户邮箱",
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "full_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "用户姓名",
      "title": "Full Name"
    },
    "groups": {
      "description": "用户所属的组（用于 OIDC groups claim，如下游应用的权限映射）",
      "items": {
        "type": "string"
      },
      "title": "Groups",
      "type": "array"
    },
    "id": {
      "description": "用户ID",
      "title": "Id",
      "type": "string"
    },
    "is_active": {
      "description": "账号状态",
      "title": "Is Active",
      "type": "boolean"
    },
    "is_super_admin": {
      "default": false,
      "description": "是否为超级管理员",
      "title": "Is Super Admin",
      "type": "boolean"
    },
    "passkey_enabled": {
      "default": false,
      "description": "是否启用通行密钥登录",
      "title": "Passkey Enabled",
      "type": "boolean"
    },
    "phone_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "联系方式",
      "title": "Phone Number"
    },
    "role": {
      "$ref": "#/components/schemas/UserRole",
      "description": "用户角色"
    },
    "two_factor_enabled": {
      "default": false,
      "description": "是否启用 TOTP 二次验证",
      "title": "Two Factor Enabled",
      "type": "boolean"
    },
    "updated_at": {
      "anyOf": [
        {
          "format": "date-time",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "更新时间",
      "title": "Updated At"
    }
  },
  "required": [
    "email",
    "id",
    "role",
    "is_active",
    "created_at"
  ],
  "title": "UserResponse",
  "type": "object"
}
```

### UserRole

```json
{
  "description": "用户角色枚举",
  "enum": [
    "admin",
    "user"
  ],
  "title": "UserRole",
  "type": "string"
}
```

### ValidationError

```json
{
  "properties": {
    "ctx": {
      "title": "Context",
      "type": "object"
    },
    "input": {
      "title": "Input"
    },
    "loc": {
      "items": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "integer"
          }
        ]
      },
      "title": "Location",
      "type": "array"
    },
    "msg": {
      "title": "Message",
      "type": "string"
    },
    "type": {
      "title": "Error Type",
      "type": "string"
    }
  },
  "required": [
    "loc",
    "msg",
    "type"
  ],
  "title": "ValidationError",
  "type": "object"
}
```

## 自定义校验索引

以下为请求模型自定义校验器的代码说明与拒绝信息；触发条件见链接中的校验器。默认请求模型校验失败为 422，敏感路径例外见行为约定。

- `AccessApiKeyCreate.validate_name`（app/schemas/access_api_key.py:13（上游引用 `../app/schemas/access_api_key.py#L13`，本仓库未收录））：密钥名称不能为空
- `AccessApiKeyUpdate.validate_value`（app/schemas/access_api_key.py:26（上游引用 `../app/schemas/access_api_key.py#L26`，本仓库未收录））：字段不能为空
- `BusinessAccountUpdateRequest.validate_non_empty`（app/schemas/business_account.py:55（上游引用 `../app/schemas/business_account.py#L55`，本仓库未收录））：至少提供一个需要更新的字段
- `BusinessAccountAdminUpdateRequest.validate_non_empty`（app/schemas/business_account.py:75（上游引用 `../app/schemas/business_account.py#L75`，本仓库未收录））：至少提供一个需要更新的字段
- 共享校验 `_validate_redirect_uris`（app/schemas/oauth.py:132（上游引用 `../app/schemas/oauth.py#L132`，本仓库未收录））：redirect_uri 格式无效；redirect_uri 禁止凭据、片段或空主机；redirect_uri 必须使用 HTTPS；仅回环地址可使用 HTTP
- 共享校验 `_validate_grant_types`（app/schemas/oauth.py:148（上游引用 `../app/schemas/oauth.py#L148`，本仓库未收录））：包含不支持的 grant_type；refresh_token 必须与 authorization_code 配合使用
- 共享校验 `_validate_scopes`（app/schemas/oauth.py:158（上游引用 `../app/schemas/oauth.py#L158`，本仓库未收录））：scope 格式无效
- `OAuthClientBase.validate_redirect_uris`（app/schemas/oauth.py:21（上游引用 `../app/schemas/oauth.py#L21`，本仓库未收录））：调用上述共享校验函数，见源码条件
- `OAuthClientBase.validate_grant_types`（app/schemas/oauth.py:26（上游引用 `../app/schemas/oauth.py#L26`，本仓库未收录））：调用上述共享校验函数，见源码条件
- `OAuthClientBase.validate_scopes`（app/schemas/oauth.py:31（上游引用 `../app/schemas/oauth.py#L31`，本仓库未收录））：调用上述共享校验函数，见源码条件
- `OAuthClientBase.validate_public_client`（app/schemas/oauth.py:35（上游引用 `../app/schemas/oauth.py#L35`，本仓库未收录））：公共客户端不能使用 client_credentials
- `OAuthClientUpdate.validate_redirect_uris`（app/schemas/oauth.py:62（上游引用 `../app/schemas/oauth.py#L62`，本仓库未收录））：调用上述共享校验函数，见源码条件
- `OAuthClientUpdate.validate_grant_types`（app/schemas/oauth.py:67（上游引用 `../app/schemas/oauth.py#L67`，本仓库未收录））：调用上述共享校验函数，见源码条件
- `OAuthClientUpdate.validate_scopes`（app/schemas/oauth.py:72（上游引用 `../app/schemas/oauth.py#L72`，本仓库未收录））：调用上述共享校验函数，见源码条件
- 共享校验 `_validate_http_url`（app/schemas/project.py:10（上游引用 `../app/schemas/project.py#L10`，本仓库未收录））：URL 格式无效；URL 必须是绝对 HTTP(S) 地址；URL 不允许包含凭据
- `ProjectUpdate.validate_non_empty`（app/schemas/project.py:61（上游引用 `../app/schemas/project.py#L61`，本仓库未收录））：至少提供一个需要更新的字段
- `ProjectFileCreate.validate_storage_key`（app/schemas/project.py:136（上游引用 `../app/schemas/project.py#L136`，本仓库未收录））：必须提供 storage_key；storage_key 与兼容字段 oss_key 不一致
- `ProjectFileUpdate.validate_non_empty`（app/schemas/project.py:151（上游引用 `../app/schemas/project.py#L151`，本仓库未收录））：至少提供一个需要更新的字段
- `ProjectLinkUpdate.validate_non_empty`（app/schemas/project.py:229（上游引用 `../app/schemas/project.py#L229`，本仓库未收录））：至少提供一个需要更新的字段
- `ProjectTaskUpdate.validate_non_empty`（app/schemas/project.py:281（上游引用 `../app/schemas/project.py#L281`，本仓库未收录））：至少提供一个需要更新的字段
- `ProjectFinanceEntryUpdate.validate_non_empty`（app/schemas/project.py:343（上游引用 `../app/schemas/project.py#L343`，本仓库未收录））：至少提供一个需要更新的字段
- `ResponsibleTagResponse.convert_object_id`（app/schemas/responsible_tag.py:34（上游引用 `../app/schemas/responsible_tag.py#L34`，本仓库未收录））：调用上述共享校验函数，见源码条件
- `CatalogData.unique_ids`（app/schemas/shop.py:34（上游引用 `../app/schemas/shop.py#L34`，本仓库未收录））：必须包含定制版和畅销版；商品编号不能重复
- `OAuthKeyImportRequest.validate_private_pem_envelope`（app/schemas/system_key.py:29（上游引用 `../app/schemas/system_key.py#L29`，本仓库未收录））：必须提交 PKCS#8 PEM 私钥
- `TotpConfirmRequest.validate_code`（app/schemas/two_factor.py:38（上游引用 `../app/schemas/two_factor.py#L38`，本仓库未收录））：TOTP 验证码必须为 6 位数字
- `UserRegister.validate_password`（app/schemas/user.py:25（上游引用 `../app/schemas/user.py#L25`，本仓库未收录））：密码长度至少为8位；密码长度不能超过128位
- `AdminChangePasswordRequest.validate_password`（app/schemas/user.py:103（上游引用 `../app/schemas/user.py#L103`，本仓库未收录））：密码长度至少为8位；密码长度不能超过128位
- `AdminResetPasswordRequest.validate_password`（app/schemas/user.py:125（上游引用 `../app/schemas/user.py#L125`，本仓库未收录））：密码长度至少为8位；密码长度不能超过128位
- `UserProfileUpdate.validate_non_empty`（app/schemas/user.py:142（上游引用 `../app/schemas/user.py#L142`，本仓库未收录））：至少提供一个需要更新的字段
- `UserPasswordChangeRequest.validate_new_password`（app/schemas/user.py:156（上游引用 `../app/schemas/user.py#L156`，本仓库未收录））：新密码长度至少为8位；新密码长度不能超过128位
- `ChangeEmailRequest.validate_verification_code`（app/schemas/user.py:172（上游引用 `../app/schemas/user.py#L172`，本仓库未收录））：验证码必须为数字；验证码必须为6位
- `CheckUserExistsRequest.validate_identifier`（app/schemas/user.py:245（上游引用 `../app/schemas/user.py#L245`，本仓库未收录））：请输入有效的邮箱地址；请输入有效的11位手机号码
- `AdminUserUpdateRequest.normalize_groups`（app/schemas/user.py:281（上游引用 `../app/schemas/user.py#L281`，本仓库未收录））：单个用户组名称长度不能超过64位
- `AdminUserUpdateRequest.validate_non_empty`（app/schemas/user.py:297（上游引用 `../app/schemas/user.py#L297`，本仓库未收录））：至少提供一个需要更新的字段
- `SendSMSCodeRequest.validate_phone_number`（app/schemas/user.py:313（上游引用 `../app/schemas/user.py#L313`，本仓库未收录））：手机号码必须为数字；手机号码必须为11位；手机号码格式不正确
- `SMSLoginRequest.validate_phone_number`（app/schemas/user.py:338（上游引用 `../app/schemas/user.py#L338`，本仓库未收录））：手机号码必须为数字；手机号码必须为11位；手机号码格式不正确
- `SMSLoginRequest.validate_verification_code`（app/schemas/user.py:349（上游引用 `../app/schemas/user.py#L349`，本仓库未收录））：验证码必须为数字；验证码必须为6位
- `ChangePhoneNumberRequest.validate_phone_number`（app/schemas/user.py:365（上游引用 `../app/schemas/user.py#L365`，本仓库未收录））：手机号码必须为数字；手机号码必须为11位；手机号码格式不正确
- `ChangePhoneNumberRequest.validate_verification_code`（app/schemas/user.py:376（上游引用 `../app/schemas/user.py#L376`，本仓库未收录））：验证码必须为数字；验证码必须为6位
- `SMSResetPasswordRequest.validate_phone_number`（app/schemas/user.py:400（上游引用 `../app/schemas/user.py#L400`，本仓库未收录））：手机号码必须为数字；手机号码必须为11位；手机号码格式不正确
- `SMSResetPasswordRequest.validate_verification_code`（app/schemas/user.py:411（上游引用 `../app/schemas/user.py#L411`，本仓库未收录））：验证码必须为数字；验证码必须为6位
- `SMSResetPasswordRequest.validate_new_password`（app/schemas/user.py:420（上游引用 `../app/schemas/user.py#L420`，本仓库未收录））：新密码长度至少为8位；新密码长度不能超过128位
- `EmailResetPasswordRequest.validate_verification_code`（app/schemas/user.py:444（上游引用 `../app/schemas/user.py#L444`，本仓库未收录））：验证码必须为数字；验证码必须为6位
- `EmailResetPasswordRequest.validate_new_password`（app/schemas/user.py:453（上游引用 `../app/schemas/user.py#L453`，本仓库未收录））：新密码长度至少为8位；新密码长度不能超过128位
