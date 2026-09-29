import asyncio

import typer
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .auth import passwords
from .catalog import Catalog
from .credentials import PASSWORD_MIN_LENGTH, AdminCredentials, LoginBody
from .models import AdminUser, AuditEvent
from .settings import Settings

app = typer.Typer(no_args_is_help=True)
plugins = typer.Typer(no_args_is_help=True)
app.add_typer(plugins, name="plugins")


@plugins.command("check")
def check(path: str = "plugins"):
    catalog = Catalog(path)
    typer.echo(f"OK: {len(catalog.tools)} tools; fingerprint={catalog.fingerprint}")


@plugins.command("sync")
def sync():
    async def run():
        settings = Settings()
        engine = create_async_engine(settings.database_url)
        try:
            async with async_sessionmaker(engine)() as db, db.begin():
                catalog = Catalog(settings.plugins_path)
                await catalog.sync(db)
                from .service import Service

                await Service(settings, catalog).validate_all(db)
                db.add(
                    AuditEvent(
                        actor="cli", action="sync", resource="tools", object_id=catalog.fingerprint
                    )
                )
                typer.echo(f"Synced {len(catalog.tools)} tools")
        finally:
            await engine.dispose()

    asyncio.run(run())


def save_admin(username: str, password: str, *, reset: bool = False):
    try:
        if reset:
            # Allow recovery of legacy IDs without changing their identity.
            LoginBody(username=username, password=password)
            if len(password) < PASSWORD_MIN_LENGTH:
                raise typer.BadParameter("Password must contain at least 12 characters")
        else:
            AdminCredentials(username=username, password=password)
    except ValidationError as exc:
        errors = exc.errors(include_input=False, include_context=False, include_url=False)
        raise typer.BadParameter(
            "; ".join(f"{'.'.join(map(str, e['loc']))}: {e['msg']}" for e in errors)
        ) from None

    async def run():
        engine = create_async_engine(Settings().database_url)
        try:
            async with async_sessionmaker(engine)() as db, db.begin():
                user = await db.get(AdminUser, username)
                if reset:
                    if not user:
                        raise typer.BadParameter("Administrator does not exist")
                    user.password_hash = passwords.hash(password)
                else:
                    if user:
                        raise typer.BadParameter("Administrator already exists")
                    db.add(AdminUser(id=username, password_hash=passwords.hash(password)))
                db.add(
                    AuditEvent(
                        actor="cli",
                        action="reset-password" if reset else "create",
                        resource="admins",
                        object_id=username,
                    )
                )
        except IntegrityError:
            raise typer.BadParameter("Administrator already exists") from None
        finally:
            await engine.dispose()

    asyncio.run(run())


@app.command("admin-create")
def admin_create(
    username: str,
    password: str = typer.Option(..., prompt=True, hide_input=True, confirmation_prompt=True),
):
    """Create an administrator (username is case-sensitive; email is not required)."""
    save_admin(username, password)
    typer.echo("Administrator created")


@app.command("admin-reset-password")
def admin_reset_password(
    username: str,
    password: str = typer.Option(..., prompt=True, hide_input=True, confirmation_prompt=True),
):
    """Reset an administrator password and invalidate their existing sessions."""
    save_admin(username, password, reset=True)
    typer.echo("Password reset; existing sessions invalidated")
