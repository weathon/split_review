"""`ClaudeAgentOptions` — the shape the existing code uses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ClaudeAgentOptions:
    model: str = ""
    system_prompt: Any = None  # str | {"type": "file", "path": str} | None
    allowed_tools: list[str] = field(default_factory=list)
    disallowed_tools: list[str] = field(default_factory=list)
    mcp_servers: dict[str, Any] = field(default_factory=dict)
    max_turns: int = 30
    cwd: str = ""
    permission_mode: str = "default"  # "default" | "bypassPermissions" | "plan"
    tools: list[Any] = field(default_factory=list)
    strict_mcp_config: bool = True
    agents: Any = None
    max_tokens: int = 16384
