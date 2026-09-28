FROM python:3.13-slim AS base
COPY --from=ghcr.io/astral-sh/uv:0.11.6 /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY backend ./backend
COPY sdk ./sdk
RUN uv sync --frozen --no-dev
ENV PATH="/app/.venv/bin:$PATH"

FROM base AS test-idp
COPY tests ./tests
CMD ["uvicorn", "tests.idp:app", "--host", "0.0.0.0", "--port", "9443", "--ssl-keyfile", "/certs/key.pem", "--ssl-certfile", "/certs/cert.pem", "--no-access-log"]

FROM base AS runtime
COPY plugins ./plugins
COPY migrations ./migrations
COPY alembic.ini ./
RUN useradd --uid 10001 --create-home gateway
USER gateway
EXPOSE 8000
CMD ["uvicorn", "gateway.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
