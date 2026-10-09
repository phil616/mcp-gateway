# API Examples

Examples below match current routes. Replace IDs and tokens with values from your environment.

## Login

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"admin-password"}'
```

If the response has `requires_2fa: true`, complete the challenge first (the challenge token is not an access token):

```bash
curl -X POST http://localhost:8000/api/2fa/verify \
  -H "Content-Type: application/json" \
  -d '{"challenge_token":"<CHALLENGE_TOKEN>","code":"<TOTP_OR_RECOVERY_CODE>"}'
```

Use the returned `access_token`:

```bash
TOKEN=...
curl http://localhost:8000/api/users/me \
  -H "Authorization: Bearer $TOKEN"
```

## Create Ticket

```bash
curl -X POST http://localhost:8000/api/tickets \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cannot access service",
    "ticket_type": "technical",
    "content": "The dashboard returns 500."
  }'
```

## Admin Reply Ticket

```bash
curl -X POST http://localhost:8000/api/tickets/$TICKET_ID/reply \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"feedback":"Issue has been fixed."}'
```

## Apply Business Account

```bash
curl -X POST http://localhost:8000/api/business-accounts/me/apply \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Example Co",
    "tax_number": "91310000XXXXXXXXXX",
    "contact_person_name": "Alice",
    "contact_phone": "13800138000"
  }'
```

Admin activation:

```bash
curl -X PUT http://localhost:8000/api/business-accounts/$ACCOUNT_ID \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "assigned_email": "customer@example.com",
    "user_code": "U10001"
  }'
```

## Create OAuth Client

```bash
curl -X POST http://localhost:8000/api/oauth/clients/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dashboard",
    "redirect_uris": ["http://localhost:5173/oauth/callback"],
    "grant_types": ["authorization_code", "refresh_token"],
    "scopes": ["openid", "profile", "email", "offline_access"],
    "is_confidential": false,
    "is_enabled": true
  }'
```

## OAuth Authorization Code Flow

Use the `client_id` returned by client creation. HTTP redirect URIs are accepted only for loopback hosts such as localhost. Public clients use S256 PKCE; retain the corresponding verifier until code exchange.

1. Establish a session using a business JWT. This curl request stores cookies in a curl cookie jar; it does **not** sign a separate browser in. A browser frontend must call this endpoint with `credentials: "include"`:

```bash
curl -c oauth-cookies.txt -X POST http://localhost:8000/oauth/session \
  -H "Authorization: Bearer $TOKEN" \
  -i
```

2. After establishing the session in the same browser, navigate to (replace all placeholders and URL-encode their values):

```text
http://localhost:8000/oauth/authorize?response_type=code&client_id=<CLIENT_ID>&redirect_uri=http%3A%2F%2Flocalhost%3A5173%2Foauth%2Fcallback&scope=openid%20profile%20email%20offline_access&state=abc&code_challenge=<S256_CHALLENGE>&code_challenge_method=S256
```

3. Exchange code:

```bash
curl -X POST http://localhost:8000/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  --data-urlencode "client_id=$CLIENT_ID" \
  --data-urlencode "code=$CODE" \
  -d "redirect_uri=http://localhost:5173/oauth/callback" \
  --data-urlencode "code_verifier=$CODE_VERIFIER"
```

## Application Key

```bash
curl -X POST http://localhost:8000/api/application-key/create \
  -H "Authorization: Bearer $TOKEN"
```

Validate:

```bash
curl -X POST http://localhost:8000/api/application-key/validate \
  -H "Content-Type: application/json" \
  -d '{"key":"'"$APPLICATION_KEY"'"}'
```

## Service Upload

```bash
curl -X PUT http://localhost:8000/api/upload/backup.tar.gz \
  -H "X-API-Key: $UPLOAD_API_KEY" \
  -H "Content-Type: application/gzip" \
  --data-binary @backup.tar.gz
```

## Send Common Email

```bash
curl -X POST http://localhost:8000/api/email/send-common \
  -H "X-API-Key: $UPLOAD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "System Notice",
    "content": "Deployment completed.",
    "message_id": "deploy-001",
    "recipients": ["user@example.com"]
  }'
```

## Project File Upload

Obtain a project upload grant with an administrator token. Parameters are in the query string:

```bash
curl -X POST "http://localhost:8000/api/projects/$PROJECT_ID/files/upload-url?filename=report.pdf&content_type=application%2Fpdf" \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

Use the returned `upload_url` unchanged, including its query token:

```bash
curl -X PUT "$UPLOAD_URL" -H "Content-Type: application/pdf" --data-binary @report.pdf
```

Then register metadata using the returned storage_key and actual byte length. The body project_id must match the path:

```bash
curl -X POST "http://localhost:8000/api/projects/$PROJECT_ID/files" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"project_id":"<PROJECT_ID>","filename":"report.pdf","original_filename":"report.pdf","storage_key":"<STORAGE_KEY>","file_size":<ACTUAL_BYTES>,"mime_type":"application/pdf"}'
```

## Quote and Order

Read the current catalog before quoting. Use its actual revision and active item IDs:

```bash
curl http://localhost:8000/api/shop/catalog -H "Authorization: Bearer $TOKEN"
curl -X POST http://localhost:8000/api/shop/quote \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"revision":<CATALOG_REVISION>,"plan":"popular","item_ids":["backend"],"requirements":"需求说明"}'
```

Add a unique `request_id` (16–64 letters/digits/underscores/hyphens) to the same JSON and POST to `/api/shop/orders`. Reuse it only to retry the same order. With an agent code, first quote with `agent_code`, then include both `agent_code` and the returned `referral.revision` as `agent_revision` when submitting the order. All quote amounts are integer CNY cents.

## Data Export (Super Administrator)

```bash
curl http://localhost:8000/api/admin/data-export/catalog \
  -H "Authorization: Bearer $SUPER_ADMIN_TOKEN"
curl --fail-with-body -X POST http://localhost:8000/api/admin/data-export \
  -H "Authorization: Bearer $SUPER_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"datasets":["projects","tickets"]}' \
  -o system-data-export.json
```

The export uses MongoDB Canonical Extended JSON v2, not ordinary API response models. See field documentation（上游引用 `data-export-fields.md`，本仓库未收录）. Replace every `<...>` placeholder before running examples; numeric placeholders must be unquoted JSON numbers.
