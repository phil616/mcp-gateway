"""Trusted plugin contract. No database or server application imports."""

import inspect
import re
from contextvars import ContextVar
from dataclasses import dataclass
from typing import TypeVar

from fastmcp.dependencies import Depends
from fastmcp.tools import Tool
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


@dataclass(frozen=True)
class ToolRuntime:
    group: str
    call_id: str
    _config: BaseModel

    def config(self, model: type[T]) -> T:
        if not isinstance(self._config, model):
            raise TypeError("Configuration model mismatch")
        return self._config


_runtime: ContextVar[ToolRuntime] = ContextVar("gateway_runtime")


def current_runtime() -> ToolRuntime:
    return _runtime.get()


class EmptyConfig(BaseModel):
    model_config = {"extra": "forbid"}


@dataclass(frozen=True)
class ToolSpec:
    id: str
    version: str
    tool: Tool
    config_model: type[BaseModel]
    timeout: float


class ToolPackage:
    def __init__(self, id: str, version: str):
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", id) or not version:
            raise ValueError("Invalid package ID or version")
        self.id, self.version = id, version
        self.tools: dict[str, ToolSpec] = {}

    def tool(
        self,
        *,
        id: str,
        config_model: type[BaseModel] = EmptyConfig,
        description: str | None = None,
        timeout: float = 30,
    ):
        def register(fn):
            if not re.fullmatch(r"[a-z][a-z0-9_-]*", id) or timeout <= 0:
                raise ValueError("Invalid tool ID or timeout")
            key = f"{self.id}.{id}"
            if key in self.tools:
                raise ValueError(f"Duplicate tool ID: {key}")
            if not issubclass(config_model, BaseModel):
                raise TypeError("config_model must be a Pydantic model")
            signature = inspect.signature(fn)
            if signature.return_annotation is inspect.Signature.empty or any(
                p.annotation is inspect.Parameter.empty for p in signature.parameters.values()
            ):
                raise TypeError(f"{key}: all parameters and return value need type annotations")
            config_model.model_json_schema()
            tool = Tool.from_function(fn, name=key, description=description, run_in_thread=True)
            self.tools[key] = ToolSpec(key, self.version, tool, config_model, timeout)
            return fn

        return register


__all__ = ["Depends", "ToolPackage", "ToolRuntime", "current_runtime"]
