import hashlib
import importlib.util
import sys
from pathlib import Path

from gateway_sdk import ToolPackage
from sqlalchemy import select, text

from .models import Artifact, ToolDefinition


class Catalog:
    def __init__(self, root: str):
        path = Path(root).resolve()
        if not path.is_dir():
            raise ValueError(f"Plugin directory missing: {path}")
        self.tools = {}
        digest = hashlib.sha256()
        for source in sorted(path.rglob("*.py")):
            digest.update(str(source.relative_to(path)).encode())
            digest.update(source.read_bytes())
        self.fingerprint = digest.hexdigest()
        sys.path.insert(0, str(path.parent))
        packages = set()
        for entry in sorted(path.glob("*/plugin.py")):
            name = f"{path.name}.{entry.parent.name}.plugin"
            try:
                spec = importlib.util.spec_from_file_location(name, entry)
                module = importlib.util.module_from_spec(spec)
                sys.modules[name] = module
                spec.loader.exec_module(module)
                package = module.package
                if not isinstance(package, ToolPackage):
                    raise TypeError("Entry must export a ToolPackage as package")
                if package.id in packages:
                    raise ValueError(f"Duplicate package ID: {package.id}")
                packages.add(package.id)
                for key, tool in package.tools.items():
                    if key in self.tools:
                        raise ValueError(f"Duplicate tool ID: {key}")
                    self.tools[key] = tool
            except Exception as exc:
                raise ValueError(f"Plugin {entry}: {exc}") from exc

    async def sync(self, session):
        await session.execute(text("SELECT pg_advisory_xact_lock(671923)"))
        existing = {t.id: t for t in (await session.scalars(select(ToolDefinition))).all()}
        for key, spec in self.tools.items():
            row = existing.pop(key, None)
            data = {
                "available": True,
                "enabled": True if row is None else row.data["enabled"],
                "package_version": spec.version,
                "parameters": spec.tool.parameters,
                "config_schema": spec.config_model.model_json_schema(),
                "description": spec.tool.description,
                "fingerprint": self.fingerprint,
            }
            if row:
                row.data = data
                row.version += 1
            else:
                session.add(ToolDefinition(id=key, data=data))
        for row in existing.values():
            row.data = {**row.data, "available": False}
            row.version += 1
        artifact = await session.get(Artifact, 1)
        if artifact:
            artifact.fingerprint = self.fingerprint
        else:
            session.add(Artifact(id=1, fingerprint=self.fingerprint))

    async def verify(self, session):
        artifact = await session.get(Artifact, 1)
        if not artifact or artifact.fingerprint != self.fingerprint:
            raise RuntimeError(
                "Plugin artifact mismatch; run gateway plugins sync before starting all workers"
            )
