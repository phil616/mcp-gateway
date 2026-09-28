from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def now():
    return datetime.now(UTC)


class Base(DeclarativeBase):
    pass


class Record:
    id: Mapped[str] = mapped_column(String(128), primary_key=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    data: Mapped[dict] = mapped_column(JSONB, default=dict)


class ToolDefinition(Record, Base):
    __tablename__ = "tools"


class AuthProfile(Record, Base):
    __tablename__ = "auth_profiles"


class Secret(Record, Base):
    __tablename__ = "secrets"


class ConfigProfile(Record, Base):
    __tablename__ = "config_profiles"


class Group(Record, Base):
    __tablename__ = "groups"
    auth_profile_id: Mapped[str | None] = mapped_column(ForeignKey("auth_profiles.id"))


class ToolBinding(Record, Base):
    __tablename__ = "bindings"
    group_id: Mapped[str] = mapped_column(ForeignKey("groups.id"))
    tool_id: Mapped[str] = mapped_column(ForeignKey("tools.id"))
    profile_id: Mapped[str | None] = mapped_column(ForeignKey("config_profiles.id"))
    exposed_name: Mapped[str] = mapped_column(String(128))
    __table_args__ = (
        UniqueConstraint("group_id", "tool_id"),
        UniqueConstraint("group_id", "exposed_name"),
    )


class GroupAccessKey(Record, Base):
    __tablename__ = "access_keys"
    group_id: Mapped[str] = mapped_column(ForeignKey("groups.id"))


class AdminUser(Base):
    __tablename__ = "admins"
    id: Mapped[str] = mapped_column(String(128), primary_key=True)
    password_hash: Mapped[str] = mapped_column(String)


class AuditEvent(Base):
    __tablename__ = "audit"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    actor: Mapped[str] = mapped_column(String)
    action: Mapped[str] = mapped_column(String)
    resource: Mapped[str] = mapped_column(String)
    object_id: Mapped[str] = mapped_column(String)


class Artifact(Base):
    __tablename__ = "artifact"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fingerprint: Mapped[str] = mapped_column(String)


RESOURCES = {
    "tools": ToolDefinition,
    "groups": Group,
    "bindings": ToolBinding,
    "config-profiles": ConfigProfile,
    "secrets": Secret,
    "auth-profiles": AuthProfile,
    "access-keys": GroupAccessKey,
}
