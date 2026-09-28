from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    database_url: str = "postgresql+asyncpg://gateway:gateway@localhost:5432/gateway"
    redis_url: str = "redis://localhost:6379/0"
    public_url: str = "http://localhost:8000"
    console_origin: str = "http://localhost:5173"
    master_key: str
    key_version: str = "1"
    plugins_path: str = "plugins"
    cookie_secure: bool = True
    session_seconds: int = 28800
    thread_limit: int = Field(default=16, ge=1, le=128)
