"""HTTP diagnostics without request bodies, query strings or credentials."""

from urllib.parse import urlsplit, urlunsplit

from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

LOOPBACK = {"localhost", "127.0.0.1", "::1"}


def console_origins(settings):
    origins = [settings.console_origin]
    parsed = urlsplit(settings.console_origin)
    # Local HTTP development only. Production origins remain exact matches.
    if not settings.cookie_secure and parsed.scheme == "http" and parsed.hostname in LOOPBACK:
        for host in sorted(LOOPBACK):
            netloc = f"[{host}]" if ":" in host else host
            if parsed.port is not None:
                netloc += f":{parsed.port}"
            alias = urlunsplit((parsed.scheme, netloc, "", "", ""))
            if alias not in origins:
                origins.append(alias)
    return origins


class DiagnosticCORSMiddleware(CORSMiddleware):
    def preflight_response(self, request_headers):
        response = super().preflight_response(request_headers)
        if response.status_code != 400:
            return response
        return JSONResponse(
            status_code=400,
            headers={
                k: v
                for k, v in response.headers.items()
                if k not in {"content-type", "content-length"}
            },
            content={
                "detail": "CORS preflight rejected: check CONSOLE_ORIGIN, request method and headers"
            },
        )


def mcp_origins(settings):
    return list(dict.fromkeys([*console_origins(settings), settings.public_url.rstrip("/")]))


def is_mcp_path(path):
    return path.endswith("/mcp") and not path.startswith("/api/")


class GatewayCORSMiddleware:
    """Keep management CSRF headers separate from browser MCP transport headers."""

    def __init__(self, app, settings):
        self.management = DiagnosticCORSMiddleware(
            app,
            allow_origins=console_origins(settings),
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "X-CSRF-Token"],
            expose_headers=["X-Request-ID"],
        )
        self.mcp = DiagnosticCORSMiddleware(
            app,
            allow_origins=mcp_origins(settings),
            allow_methods=["GET", "POST", "DELETE"],
            allow_headers=[
                "Authorization",
                "Content-Type",
                "MCP-Protocol-Version",
                "MCP-Session-Id",
                "Last-Event-ID",
            ],
            expose_headers=["X-Request-ID", "WWW-Authenticate", "MCP-Session-Id"],
        )

    async def __call__(self, scope, receive, send):
        middleware = self.mcp if is_mcp_path(scope.get("path", "")) else self.management
        await middleware(scope, receive, send)
