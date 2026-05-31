"""Tool registration that mirrors `claude_agent_sdk.tool` + `create_sdk_mcp_server`.

A `tool(name, description, params)` decorator wraps an async handler
`(args: dict) -> {"content": [{"type": "text", "text": ...}], "is_error": bool}`
into a `_ToolSpec`. `create_sdk_mcp_server` collects specs into a `_McpServer`.
At runtime the OpenHarness-backed client wraps each spec as a `BaseTool`.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Awaitable, Callable

from pydantic import BaseModel, ConfigDict

from openharness.tools.base import BaseTool, ToolExecutionContext, ToolResult


ToolHandler = Callable[[dict], Awaitable[Any]]


@dataclass
class _ToolSpec:
    name: str
    description: str
    input_schema: dict
    handler: ToolHandler


@dataclass
class _McpServer:
    name: str
    version: str
    tools: list[_ToolSpec]


_PY_TYPE_TO_JSON = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
}


def _python_to_jsonschema(value: Any) -> dict:
    if value is str or value is int or value is float or value is bool:
        return {"type": _PY_TYPE_TO_JSON[value]}
    if value is list:
        return {"type": "array"}
    if value is dict:
        return {"type": "object"}
    if isinstance(value, dict):
        return value
    raise TypeError(
        f"@tool: cannot derive a JSON schema for {value!r}. "
        "Use one of str/int/float/bool/list/dict, or pass a full JSON Schema dict."
    )


def _coerce_input_schema(params: Any) -> dict:
    if not isinstance(params, dict):
        raise TypeError(f"@tool params must be a dict, got {type(params).__name__}")
    if params.get("type") == "object" and "properties" in params:
        return params
    properties: dict[str, dict] = {}
    required: list[str] = []
    for key, value in params.items():
        properties[key] = _python_to_jsonschema(value)
        required.append(key)
    return {"type": "object", "properties": properties, "required": required}


def tool(name: str, description: str, params: Any):
    """Decorator that produces a `_ToolSpec`."""
    schema = _coerce_input_schema(params)

    def decorator(handler: ToolHandler) -> _ToolSpec:
        return _ToolSpec(name=name, description=description, input_schema=schema, handler=handler)

    return decorator


def create_sdk_mcp_server(*, name: str, version: str, tools: list[_ToolSpec]) -> _McpServer:
    return _McpServer(name=name, version=version, tools=list(tools))


class _PassthroughInput(BaseModel):
    model_config = ConfigDict(extra="allow")


class JsonSchemaTool(BaseTool):
    """Bridges a `_ToolSpec` into an OpenHarness `BaseTool`."""

    input_model = _PassthroughInput

    def __init__(self, *, full_name: str, spec: _ToolSpec) -> None:
        self.name = full_name
        self.description = spec.description
        self._input_schema = spec.input_schema
        self._handler = spec.handler

    def to_api_schema(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self._input_schema,
        }

    def is_read_only(self, arguments: BaseModel) -> bool:
        return True

    async def execute(self, arguments: BaseModel, context: ToolExecutionContext) -> ToolResult:
        args = arguments.model_dump()
        result = await self._handler(args)
        if not isinstance(result, dict):
            raise TypeError(
                f"@tool {self.name!r} returned {type(result).__name__}; "
                "handler must return {'content': [...], 'is_error': bool}."
            )
        if "content" not in result or not isinstance(result["content"], list):
            raise ValueError(
                f"@tool {self.name!r} return value missing list 'content' key."
            )
        text_parts: list[str] = []
        for block in result["content"]:
            if not isinstance(block, dict) or block.get("type") != "text":
                raise ValueError(
                    f"@tool {self.name!r} produced a non-text content block: {block!r}."
                )
            text_parts.append(block.get("text") or "")
        return ToolResult(output="".join(text_parts), is_error=bool(result.get("is_error", False)))
