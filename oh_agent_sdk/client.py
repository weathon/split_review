"""`ClaudeSDKClient` — driven by OpenHarness's `run_query` engine.

Mirrors the surface used by code/claude_merger.py and DeepReviewer-v2/runner.py:

    async with ClaudeSDKClient(options=opts) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage): ...
            elif isinstance(message, ResultMessage): ...
            elif isinstance(message, RateLimitEvent): ...
"""

from __future__ import annotations

import os
import time
import uuid
from pathlib import Path
from typing import Any, AsyncIterator

from openharness.api.client import AnthropicApiClient
from openharness.api.openai_client import OpenAICompatibleClient
from openharness.config.settings import PermissionSettings
from openharness.config import load_settings as _oh_load_settings
from openharness.ui.runtime import _resolve_api_client_from_settings as _oh_resolve_api_client
from openharness.engine.messages import ConversationMessage
from openharness.engine.messages import TextBlock as _OHTextBlock
from openharness.engine.query import QueryContext, run_query
from openharness.engine.stream_events import (
    AssistantTurnComplete,
    ErrorEvent,
)
from openharness.permissions.checker import PermissionChecker
from openharness.permissions.modes import PermissionMode
from openharness.tools.base import ToolRegistry

from oh_agent_sdk.messages import (
    AssistantMessage,
    RateLimitEvent,
    ResultMessage,
    TextBlock,
)
from oh_agent_sdk.options import ClaudeAgentOptions
from oh_agent_sdk.tools import JsonSchemaTool, _McpServer


def _build_api_client():
    """Pick an API client. By default, defer to OpenHarness's own settings/
    profile resolution (so `oh auth codex-login`, `claude-login`, etc. just
    work). Set OH_API_KIND=openai|anthropic to force a path that reads env
    vars directly instead."""
    kind = (os.environ.get("OH_API_KIND") or "").strip().lower()
    if kind == "openai":
        api_key = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
        base_url = (
            os.environ.get("OPENROUTER_BASE_URL")
            or os.environ.get("OPENAI_BASE_URL")
            or "https://openrouter.ai/api/v1"
        )
        return OpenAICompatibleClient(api_key=api_key, base_url=base_url)
    if kind == "anthropic":
        return AnthropicApiClient(
            api_key=os.environ.get("ANTHROPIC_API_KEY"),
            base_url=os.environ.get("ANTHROPIC_BASE_URL"),
        )
    return _oh_resolve_api_client(_oh_load_settings())


def _resolve_system_prompt(spec: Any) -> str:
    if spec is None:
        return ""
    if isinstance(spec, str):
        return spec
    if isinstance(spec, dict) and spec.get("type") == "file":
        path = spec.get("path")
        if not path:
            raise ValueError("system_prompt={'type':'file'} requires a 'path'")
        return Path(path).expanduser().read_text(encoding="utf-8")
    raise TypeError(f"Unsupported system_prompt: {spec!r}")


def _resolve_permission_mode(mode: str) -> PermissionMode:
    norm = (mode or "default").lower()
    if norm in ("default",):
        return PermissionMode.DEFAULT
    if norm in ("bypasspermissions", "full_auto", "auto"):
        return PermissionMode.FULL_AUTO
    if norm == "plan":
        return PermissionMode.PLAN
    raise ValueError(
        f"Unknown permission_mode {mode!r}; expected one of "
        "'default', 'bypassPermissions', 'plan'."
    )


class ClaudeSDKClient:
    """OpenHarness-backed client with the Claude-Agent-SDK surface."""

    def __init__(self, options: ClaudeAgentOptions) -> None:
        self._options = options
        self._api_client = None
        self._registry: ToolRegistry | None = None
        self._permission: PermissionChecker | None = None
        self._messages: list[ConversationMessage] = []
        self._pending_prompt: str | None = None
        self._session_id = f"oh-{uuid.uuid4().hex[:16]}"

    async def __aenter__(self) -> "ClaudeSDKClient":
        self._api_client = _build_api_client()

        registry = ToolRegistry()
        for server_key, server in (self._options.mcp_servers or {}).items():
            if not isinstance(server, _McpServer):
                raise TypeError(
                    f"mcp_servers[{server_key!r}] must come from create_sdk_mcp_server(...)"
                )
            for spec in server.tools:
                full_name = f"mcp__{server_key}__{spec.name}"
                registry.register(JsonSchemaTool(full_name=full_name, spec=spec))

        if self._options.allowed_tools:
            allowed = set(self._options.allowed_tools)
            kept = [t for t in registry.list_tools() if t.name in allowed]
            registry = ToolRegistry()
            for t in kept:
                registry.register(t)

        self._registry = registry
        self._permission = PermissionChecker(
            PermissionSettings(mode=_resolve_permission_mode(self._options.permission_mode))
        )
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._api_client is not None and hasattr(self._api_client, "close"):
            await self._api_client.close()
        self._api_client = None
        self._registry = None
        self._permission = None

    async def query(self, prompt: str) -> None:
        self._pending_prompt = prompt

    async def receive_response(self) -> AsyncIterator[Any]:
        if self._pending_prompt is None:
            return
        prompt = self._pending_prompt
        self._pending_prompt = None

        assert self._api_client is not None
        assert self._registry is not None
        assert self._permission is not None

        system_prompt = _resolve_system_prompt(self._options.system_prompt)
        cwd = Path(self._options.cwd or os.getcwd()).resolve()

        self._messages.append(ConversationMessage.from_user_text(prompt))

        ctx = QueryContext(
            api_client=self._api_client,
            tool_registry=self._registry,
            permission_checker=self._permission,
            cwd=cwd,
            model=self._options.model,
            system_prompt=system_prompt,
            max_tokens=self._options.max_tokens,
            max_turns=self._options.max_turns,
            tool_metadata={},
        )

        accumulated_input = 0
        accumulated_output = 0
        turns = 0
        errors: list[str] = []
        stop_reason: str | None = None
        start = time.monotonic()

        async for event, usage in run_query(ctx, self._messages):
            if isinstance(event, AssistantTurnComplete):
                turns += 1
                text_blocks = [
                    TextBlock(text=b.text)
                    for b in event.message.content
                    if isinstance(b, _OHTextBlock) and b.text
                ]
                if text_blocks:
                    yield AssistantMessage(content=text_blocks)
                if usage is not None:
                    accumulated_input += int(usage.input_tokens or 0)
                    accumulated_output += int(usage.output_tokens or 0)
            elif isinstance(event, ErrorEvent):
                errors.append(event.message)

        duration_ms = int((time.monotonic() - start) * 1000)
        yield ResultMessage(
            session_id=self._session_id,
            total_cost_usd=None,
            num_turns=turns,
            duration_ms=duration_ms,
            duration_api_ms=duration_ms,
            usage={
                "input_tokens": accumulated_input,
                "output_tokens": accumulated_output,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
            },
            stop_reason=stop_reason,
            is_error=bool(errors),
            errors=errors,
        )
