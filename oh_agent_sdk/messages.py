"""Claude-Agent-SDK-shaped message classes, backed by OpenHarness."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TextBlock:
    text: str


@dataclass
class AssistantMessage:
    content: list[Any]


@dataclass
class RateLimitInfo:
    status: str | None = None
    rate_limit_type: str | None = None
    utilization: float | None = None
    resets_at: str | None = None
    overage_status: str | None = None
    overage_resets_at: str | None = None


@dataclass
class RateLimitEvent:
    rate_limit_info: RateLimitInfo


@dataclass
class ResultMessage:
    session_id: str | None = None
    total_cost_usd: float | None = None
    num_turns: int = 0
    duration_ms: int = 0
    duration_api_ms: int = 0
    usage: dict[str, int] | None = None
    stop_reason: str | None = None
    is_error: bool = False
    errors: list[str] = field(default_factory=list)
