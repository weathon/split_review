from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
    )

    app_name: str = 'DeepReviewer-2.0 OSS Backend'

    data_dir: Path = Field(default=Path('./data'))

    # Claude Agent SDK runtime
    agent_model: str = 'claude-sonnet-4-6'
    agent_max_turns: int = 1000
    agent_resume_attempts: int = 2

    # Submit behavior
    submit_default_wait_seconds: int = 8
    submit_poll_interval_seconds: float = 1.0
    max_pdf_bytes: int = 50 * 1024 * 1024

    # Pre-parsed paper text directory. File stem must match submitted PDF stem.
    parsed_papers_dir: Path = Field(default=Path('~/review_agent/iclr2026_new/papers'))

    # External paper search/read service is disabled for offline review runs.
    paper_search_enabled: bool = False
    paper_search_provider: str = 'offline'

    # Gates aligned with offline DeepReviewer finalization logic
    min_paper_search_calls_for_pdf_annotate: int = 0
    min_paper_search_calls_for_final: int = 0
    min_distinct_paper_queries_for_final: int = 0
    min_annotations_for_final: int = 10
    min_english_words_for_final: int = 0
    min_chinese_chars_for_final: int = 0
    force_english_output: bool = True
    ui_language: str = 'en'

    # PDF export
    pdf_font_name: str = 'Helvetica'
    pdf_title_font_size: int = 15
    pdf_body_font_size: int = 10
    pdf_page_margin: int = 48

    @field_validator('agent_model')
    @classmethod
    def validate_agent_model(cls, value: str) -> str:
        model = str(value or '').strip()
        if not model:
            raise ValueError('AGENT_MODEL is required for Claude Agent SDK runs.')
        return model

    @field_validator('paper_search_enabled')
    @classmethod
    def validate_paper_search_disabled(cls, value: bool) -> bool:
        if bool(value):
            raise ValueError('PAPER_SEARCH_ENABLED must be false for offline review runs.')
        return False

    @field_validator('paper_search_provider')
    @classmethod
    def validate_paper_search_provider(cls, value: str) -> str:
        provider = str(value or '').strip().lower()
        if provider != 'offline':
            raise ValueError('PAPER_SEARCH_PROVIDER must be offline for offline review runs.')
        return provider

    @field_validator(
        'min_paper_search_calls_for_pdf_annotate',
        'min_paper_search_calls_for_final',
        'min_distinct_paper_queries_for_final',
    )
    @classmethod
    def validate_no_paper_search_gates(cls, value: int) -> int:
        count = int(value)
        if count != 0:
            raise ValueError('Paper-search gates must be 0 for offline review runs.')
        return count

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    (settings.data_dir / 'jobs').mkdir(parents=True, exist_ok=True)
    return settings
