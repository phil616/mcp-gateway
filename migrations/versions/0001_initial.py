"""Initial gateway schema."""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    for name in (
        "tools",
        "auth_profiles",
        "secrets",
        "config_profiles",
        "groups",
        "bindings",
        "access_keys",
    ):
        columns = [
            sa.Column("id", sa.String(128), primary_key=True),
            sa.Column("version", sa.Integer(), nullable=False),
            sa.Column("data", JSONB(), nullable=False),
        ]
        if name == "groups":
            columns.append(
                sa.Column("auth_profile_id", sa.String(128), sa.ForeignKey("auth_profiles.id"))
            )
        if name in {"bindings", "access_keys"}:
            columns.append(
                sa.Column("group_id", sa.String(128), sa.ForeignKey("groups.id"), nullable=False)
            )
        if name == "bindings":
            columns.extend(
                [
                    sa.Column("tool_id", sa.String(128), sa.ForeignKey("tools.id"), nullable=False),
                    sa.Column("profile_id", sa.String(128), sa.ForeignKey("config_profiles.id")),
                    sa.Column("exposed_name", sa.String(128), nullable=False),
                    sa.UniqueConstraint("group_id", "tool_id"),
                    sa.UniqueConstraint("group_id", "exposed_name"),
                ]
            )
        op.create_table(name, *columns)
    op.create_table(
        "admins",
        sa.Column("id", sa.String(128), primary_key=True),
        sa.Column("password_hash", sa.String(), nullable=False),
    )
    op.create_table(
        "artifact",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("fingerprint", sa.String(), nullable=False),
    )
    op.create_table(
        "audit",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("actor", sa.String(), nullable=False),
        sa.Column("action", sa.String(), nullable=False),
        sa.Column("resource", sa.String(), nullable=False),
        sa.Column("object_id", sa.String(), nullable=False),
    )


def downgrade():
    for name in (
        "audit",
        "artifact",
        "admins",
        "access_keys",
        "bindings",
        "groups",
        "config_profiles",
        "secrets",
        "auth_profiles",
        "tools",
    ):
        op.drop_table(name)
