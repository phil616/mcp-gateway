import asyncio

import typer
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .auth import passwords
from .catalog import Catalog
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


@app.command("admin-create")
def admin_create(
    username: str,
    password: str = typer.Option(..., prompt=True, hide_input=True, confirmation_prompt=True),
):
    if len(password) < 12:
        raise typer.BadParameter("Password must contain at least 12 characters")

    async def run():
        engine = create_async_engine(Settings().database_url)
        try:
            async with async_sessionmaker(engine)() as db, db.begin():
                if await db.get(AdminUser, username):
                    raise typer.BadParameter("Administrator already exists")
                db.add(AdminUser(id=username, password_hash=passwords.hash(password)))
                db.add(
                    AuditEvent(actor="cli", action="create", resource="admins", object_id=username)
                )
        finally:
            await engine.dispose()

    asyncio.run(run())
    typer.echo("Administrator created")
