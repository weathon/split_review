from __future__ import annotations

import asyncio
import json
import traceback
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from deepreview.adapters.markdown_parser import build_page_index, parse_preparsed_text
from deepreview.config import get_settings
from deepreview.prompts.review_agent_prompt import build_review_agent_system_prompt
from deepreview.report.review_report_pdf import build_review_report_pdf
from deepreview.report.source_annotations import build_source_annotations_for_export
from deepreview.state import ensure_artifact_paths, fail_job, load_job_state, mutate_job_state, set_status
from deepreview.storage import append_event, write_json_atomic, write_text_atomic
from deepreview.tools.review_tools import ReviewRuntimeContext, build_review_tools
from deepreview.types import AnnotationItem, JobStatus


def _load_preparsed_paper_text(source_pdf_name: str):
    settings = get_settings()
    parsed_dir = Path(settings.parsed_papers_dir).expanduser()
    source_stem = Path(source_pdf_name).stem
    if not source_stem:
        raise RuntimeError('Source PDF name is required for pre-parsed paper lookup')
    parsed_path = parsed_dir / f'{source_stem}.txt'
    if not parsed_path.exists():
        raise RuntimeError(f'Pre-parsed paper text not found: {parsed_path}')
    parsed_text = parsed_path.read_text(encoding='utf-8')
    parse_result = parse_preparsed_text(parsed_text)
    return parse_result, parsed_path


def _sync_token_usage(job_id: str, usage: Any) -> None:
    requests = int(getattr(usage, 'requests', 0) or 0)
    input_tokens = int(getattr(usage, 'input_tokens', 0) or 0)
    output_tokens = int(getattr(usage, 'output_tokens', 0) or 0)
    total_tokens = int(getattr(usage, 'total_tokens', 0) or 0)

    def apply(job):
        job.usage.token.requests = requests
        job.usage.token.input_tokens = input_tokens
        job.usage.token.output_tokens = output_tokens
        job.usage.token.total_tokens = total_tokens

    mutate_job_state(job_id, apply)


def _build_claude_mcp_server(
    *,
    runtime: ReviewRuntimeContext,
    review_tools: list[Any],
    usage_totals: dict[str, int],
) -> tuple[dict[str, Any], list[str]]:
    from claude_agent_sdk import create_sdk_mcp_server, tool as sdk_tool

    sdk_tools = []

    def wrap_review_tool(review_tool):
        @sdk_tool(
            review_tool.name,
            review_tool.description,
            review_tool.params_json_schema,
        )
        async def invoke(args: dict) -> dict:
            print(f"  [claude:{review_tool.name}] {json.dumps(args, ensure_ascii=False)[:800]}")
            usage = SimpleNamespace(
                requests=usage_totals['requests'],
                input_tokens=usage_totals['input_tokens'],
                output_tokens=usage_totals['output_tokens'],
                total_tokens=usage_totals['total_tokens'],
            )
            ctx = SimpleNamespace(context=runtime, usage=usage, tool_name=review_tool.name)
            result = await review_tool.on_invoke_tool(ctx, json.dumps(args, ensure_ascii=False))
            if isinstance(result, str):
                text = result
            else:
                text = json.dumps(result, ensure_ascii=False, indent=2, default=str)
            return {'content': [{'type': 'text', 'text': text}]}

        return invoke

    for review_tool in review_tools:
        sdk_tools.append(wrap_review_tool(review_tool))

    server_name = 'deepreview_runtime'
    server = create_sdk_mcp_server(
        name=server_name,
        version='1.0.0',
        tools=sdk_tools,
    )
    allowed_tools = [f'mcp__{server_name}__{review_tool.name}' for review_tool in review_tools]
    return {server_name: server}, allowed_tools


def _apply_claude_usage(
    *,
    job_id: str,
    runtime: ReviewRuntimeContext,
    usage_totals: dict[str, int],
    result_message: Any,
) -> None:
    if result_message.usage is None:
        raise RuntimeError('Claude Agent SDK ResultMessage missing usage')
    usage = result_message.usage
    input_tokens = (
        int(usage.get('input_tokens') or 0)
        + int(usage.get('cache_creation_input_tokens') or 0)
        + int(usage.get('cache_read_input_tokens') or 0)
    )
    output_tokens = int(usage.get('output_tokens') or 0)
    usage_totals['requests'] += int(result_message.num_turns)
    usage_totals['input_tokens'] += input_tokens
    usage_totals['output_tokens'] += output_tokens
    usage_totals['total_tokens'] += input_tokens + output_tokens
    usage_payload = SimpleNamespace(**usage_totals)
    _sync_token_usage(job_id, usage_payload)
    runtime.sync_state_usage(usage_payload)


async def _run_claude_agent_turn(
    *,
    client: Any,
    prompt_text: str,
    job_id: str,
    runtime: ReviewRuntimeContext,
    usage_totals: dict[str, int],
    output_tag: str,
) -> str:
    from claude_agent_sdk import AssistantMessage, RateLimitEvent, ResultMessage, TextBlock

    await client.query(prompt_text)
    output_parts: list[str] = []
    result_message = None
    async for message in client.receive_response():
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    output_parts.append(block.text)
        elif isinstance(message, RateLimitEvent):
            info = message.rate_limit_info
            append_event(
                job_id,
                'claude_rate_limit',
                status=info.status,
                rate_limit_type=info.rate_limit_type,
                utilization=info.utilization,
                resets_at=info.resets_at,
                overage_status=info.overage_status,
            )
        elif isinstance(message, ResultMessage):
            result_message = message

    if result_message is None:
        raise RuntimeError('Claude Agent SDK ended without a ResultMessage')

    _apply_claude_usage(
        job_id=job_id,
        runtime=runtime,
        usage_totals=usage_totals,
        result_message=result_message,
    )
    append_event(
        job_id,
        'claude_agent_turn_completed',
        output_tag=output_tag,
        session_id=result_message.session_id,
        stop_reason=result_message.stop_reason,
        is_error=result_message.is_error,
        total_cost_usd=result_message.total_cost_usd,
        num_turns=result_message.num_turns,
        duration_ms=result_message.duration_ms,
        duration_api_ms=result_message.duration_api_ms,
        usage=result_message.usage,
    )
    result_errors = [str(item) for item in (result_message.errors or [])]
    reached_max_turns = any('Reached maximum number of turns' in item for item in result_errors)
    if result_message.is_error and not reached_max_turns and not runtime.final_markdown_text:
        raise RuntimeError(f'Claude Agent SDK run failed: {result_message.errors or result_message.stop_reason}')

    final_output_text = ''.join(output_parts).strip()
    if final_output_text:
        write_text_atomic(Path(runtime.job_dir / 'agent_final_output.txt'), final_output_text)
        write_text_atomic(
            Path(runtime.job_dir / f'agent_final_output_{output_tag}.txt'),
            final_output_text,
        )
    return final_output_text


def _token_usage_payload_from_state(state: Any) -> dict[str, int]:
    usage = getattr(state, 'usage', None)
    token = getattr(usage, 'token', None)
    return {
        'requests': int(getattr(token, 'requests', 0) or 0),
        'input_tokens': int(getattr(token, 'input_tokens', 0) or 0),
        'output_tokens': int(getattr(token, 'output_tokens', 0) or 0),
        'total_tokens': int(getattr(token, 'total_tokens', 0) or 0),
    }


def _render_report_pdf(
    *,
    job_id: str,
    job_title: str,
    source_pdf_name: str,
    final_md_path: Path,
    source_pdf_path: Path,
    report_pdf_path: Path,
    annotations: list[AnnotationItem] | list[dict[str, Any]],
    content_list: list[dict[str, Any]] | None,
    token_usage: dict[str, int],
    agent_model: str,
) -> dict[str, int]:
    final_report_markdown = final_md_path.read_text(encoding='utf-8')
    source_pdf_bytes = source_pdf_path.read_bytes() if source_pdf_path.exists() else None
    source_annotations = build_source_annotations_for_export(
        annotations=annotations,
        content_list=content_list,
    )

    report_pdf_bytes = build_review_report_pdf(
        workspace_title=job_title,
        source_pdf_name=source_pdf_name,
        run_id=job_id,
        status='completed',
        decision=None,
        estimated_cost=0,
        actual_cost=None,
        exported_at=datetime.now(timezone.utc),
        meta_review={},
        reviewers=[],
        raw_output=None,
        final_report_markdown=final_report_markdown,
        source_pdf_bytes=source_pdf_bytes,
        source_annotations=source_annotations,
        review_display_id=None,
        owner_email=None,
        token_usage=token_usage,
        agent_model=agent_model,
    )
    report_pdf_path.parent.mkdir(parents=True, exist_ok=True)
    report_pdf_path.write_bytes(report_pdf_bytes)

    export_stats = {
        'source_annotations_input_count': int(len(annotations)),
        'source_annotations_exported_count': int(len(source_annotations)),
        'content_list_count': int(len(content_list or [])),
        'report_pdf_size_bytes': int(len(report_pdf_bytes)),
    }
    append_event(job_id, 'pdf_export_rendered', **export_stats)
    return export_stats


async def run_job_async(job_id: str) -> None:
    settings = get_settings()
    job = load_job_state(job_id)
    if job is None:
        raise FileNotFoundError(f'Job not found: {job_id}')

    api_mode = 'claude_agent_sdk'
    append_event(
        job_id,
        'llm_api_mode_selected',
        api_mode=api_mode,
        model=str(settings.agent_model).strip(),
    )

    def apply_llm_mode(state):
        metadata = dict(state.metadata)
        metadata['llm_api_mode'] = api_mode
        state.metadata = metadata

    mutate_job_state(job_id, apply_llm_mode)

    artifacts = ensure_artifact_paths(job_id)
    source_pdf = Path(artifacts['source_pdf'])
    if not source_pdf.exists():
        raise RuntimeError(f'Source PDF missing: {source_pdf}')
    file_size = int(source_pdf.stat().st_size)
    if file_size <= 0:
        raise RuntimeError('Source PDF is empty.')
    if file_size > int(settings.max_pdf_bytes):
        raise RuntimeError(
            f'Source PDF too large: {file_size} bytes, max allowed {int(settings.max_pdf_bytes)} bytes.'
        )

    set_status(job_id, JobStatus.pdf_parsing, 'Loading pre-parsed paper text...')

    parse_result, parsed_paper_path = _load_preparsed_paper_text(job.source_pdf_name)

    write_text_atomic(Path(artifacts['mineru_markdown']), parse_result.markdown)
    if parse_result.content_list is not None:
        write_json_atomic(Path(artifacts['mineru_content_list']), {'content_list': parse_result.content_list})

    def apply_parsed(state):
        state.artifacts.mineru_markdown_path = str(artifacts['mineru_markdown'])
        state.artifacts.mineru_content_list_path = (
            str(artifacts['mineru_content_list']) if Path(artifacts['mineru_content_list']).exists() else None
        )
        state.artifacts.annotations_path = str(artifacts['annotations'])
        state.metadata['markdown_provider'] = parse_result.provider
        state.metadata['preparsed_paper_path'] = str(parsed_paper_path)

    mutate_job_state(job_id, apply_parsed)
    append_event(
        job_id,
        'preparsed_paper_loaded',
        path=str(parsed_paper_path),
        provider=parse_result.provider,
    )

    page_index = build_page_index(parse_result.markdown, parse_result.content_list)

    set_status(job_id, JobStatus.agent_running, 'Running review agent with tool loop...')

    paper_adapter = SimpleNamespace()
    paper_search_runtime_state = {
        'enabled': False,
        'started': False,
        'availability': 'disabled_for_offline_run',
        'provider': 'offline',
        'error': None,
    }
    append_event(
        job_id,
        'paper_search_runtime_state_resolved',
        enabled=paper_search_runtime_state.get('enabled'),
        started=paper_search_runtime_state.get('started'),
        availability=paper_search_runtime_state.get('availability'),
        base_url=paper_search_runtime_state.get('base_url'),
        health_url=paper_search_runtime_state.get('health_url'),
        error=paper_search_runtime_state.get('error'),
    )

    def apply_paper_search_state(state):
        metadata = dict(state.metadata)
        metadata['paper_search_runtime_state'] = dict(paper_search_runtime_state)
        state.metadata = metadata

    mutate_job_state(job_id, apply_paper_search_state)

    prompt = build_review_agent_system_prompt(
        source_file_id=job_id,
        source_file_name=job.source_pdf_name,
        ui_language=settings.ui_language,
        use_meta_review=False,
        paper_search_runtime_state=paper_search_runtime_state,
    )
    write_text_atomic(Path(artifacts['prompt_snapshot']), prompt)

    def apply_prompt(state):
        state.artifacts.prompt_snapshot_path = str(artifacts['prompt_snapshot'])

    mutate_job_state(job_id, apply_prompt)

    runtime = ReviewRuntimeContext(
        job_id=job_id,
        job_dir=Path(artifacts['source_pdf']).parent,
        page_index=page_index,
        source_markdown=parse_result.markdown,
        paper_adapter=paper_adapter,
        paper_search_runtime_state=paper_search_runtime_state,
        settings=settings,
    )

    requested_attempts = int(settings.agent_resume_attempts)
    max_attempts = max(1, min(2, requested_attempts))
    if requested_attempts != max_attempts:
        append_event(
            job_id,
            'agent_resume_attempts_capped',
            requested=requested_attempts,
            applied=max_attempts,
            reason='hard_cap_2',
        )
    usage_totals = {
        'requests': 0,
        'input_tokens': 0,
        'output_tokens': 0,
        'total_tokens': 0,
    }
    tools = build_review_tools(runtime)
    mcp_servers, allowed_tools = _build_claude_mcp_server(
        runtime=runtime,
        review_tools=tools,
        usage_totals=usage_totals,
    )
    from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient

    options = ClaudeAgentOptions(
        model=str(settings.agent_model).strip(),
        tools=[],
        system_prompt={'type': 'file', 'path': str(Path(artifacts['prompt_snapshot']).resolve())},
        mcp_servers=mcp_servers,
        strict_mcp_config=True,
        allowed_tools=allowed_tools,
        permission_mode='bypassPermissions',
        disallowed_tools=['Read', 'Glob', 'Grep', 'Bash', 'Edit', 'Write'],
        max_turns=max(1, int(settings.agent_max_turns)),
        cwd=str(runtime.job_dir),
    )
    append_event(job_id, 'claude_agent_configured', allowed_tools=allowed_tools)

    final_md_path = Path(artifacts['final_markdown'])
    for agent_stage_attempt in range(3):
        try:
            async with ClaudeSDKClient(options=options) as client:
                for attempt in range(1, max_attempts + 1):
                    if runtime.final_markdown_text:
                        append_event(
                            job_id,
                            'agent_run_skipped_after_final_write',
                            attempt=attempt,
                            reason='final_report_already_persisted',
                        )
                        break

                    turn_prompt = """Start the DeepReviewer job now. Follow the system prompt exactly and use the available MCP tools for status updates, paper inspection, annotations, and final report writing."""
                    if attempt > 1:
                        turn_prompt = f"""Resume the same review job from current state. Do not restart Phase 1 planning unless a hard gate is still unmet.
Current state: annotations={runtime.annotation_count}. External search/read services are disabled for this offline run.
If gates are met, go directly to final report assembly in section mode and call review_final_markdown_write(section_id=<required_section_id>, section_content=<section_markdown>) as soon as possible.
Mandatory: your next substantive action must be a section-mode tool call `review_final_markdown_write(...)`; plain chat markdown is invalid.
If a gate is unmet or the write tool returns an error, follow message/next_steps exactly, perform minimal remediation, then retry review_final_markdown_write.
Never end this run without a successful review_final_markdown_write."""

                    output_text = await _run_claude_agent_turn(
                        client=client,
                        prompt_text=turn_prompt,
                        job_id=job_id,
                        runtime=runtime,
                        usage_totals=usage_totals,
                        output_tag=f'attempt_{attempt}',
                    )

                    if runtime.final_markdown_text:
                        break

                    append_event(
                        job_id,
                        'agent_run_incomplete',
                        attempt=attempt,
                        max_attempts=max_attempts,
                        reason='no_final_report_persisted',
                        final_output_chars=len(output_text),
                    )

                    if attempt >= max_attempts:
                        append_event(
                            job_id,
                            'agent_forced_final_write_start',
                            attempt=attempt,
                            reason='max_attempt_reached_without_final_write',
                        )
                        forced_prompt = """MANDATORY ACTION NOW: Call review_final_markdown_write in section mode immediately. Submit exactly one required section per call using review_final_markdown_write(section_id=<required_section_id>, section_content=<section_markdown>). After each call, inspect completed_sections/missing_sections/next_required_section and submit the next required section right away until status=ok. Do not output plain-text final report. If the tool returns retry_required/error, follow message/next_steps and retry review_final_markdown_write."""
                        forced_output_text = await _run_claude_agent_turn(
                            client=client,
                            prompt_text=forced_prompt,
                            job_id=job_id,
                            runtime=runtime,
                            usage_totals=usage_totals,
                            output_tag=f'attempt_{attempt}_forced_final_write',
                        )
                        append_event(
                            job_id,
                            'agent_forced_final_write_result',
                            attempt=attempt,
                            final_output_chars=len(forced_output_text),
                            final_write_persisted=bool(runtime.final_markdown_text),
                        )
                        break

                    set_status(
                        job_id,
                        JobStatus.agent_running,
                        f"""Agent ended without final report write. Resuming review runtime (attempt {attempt + 1}/{max_attempts})...""",
                    )
        except (asyncio.CancelledError, Exception):
            if agent_stage_attempt == 2:
                raise
        if runtime.final_markdown_text and final_md_path.exists():
            break

    if not runtime.final_markdown_text or not final_md_path.exists():
        raise RuntimeError("""Agent finished without successful review_final_markdown_write. Final report gate was not satisfied.""")

    set_status(job_id, JobStatus.pdf_exporting, 'Rendering final markdown report into PDF...')

    report_pdf_path = Path(artifacts['report_pdf'])
    if not final_md_path.exists():
        raise RuntimeError(f'Final markdown not found: {final_md_path}')

    state_token_usage = _token_usage_payload_from_state(load_job_state(job_id))
    token_usage_for_pdf = {
        'requests': max(int(usage_totals.get('requests', 0)), int(state_token_usage.get('requests', 0))),
        'input_tokens': max(int(usage_totals.get('input_tokens', 0)), int(state_token_usage.get('input_tokens', 0))),
        'output_tokens': max(int(usage_totals.get('output_tokens', 0)), int(state_token_usage.get('output_tokens', 0))),
        'total_tokens': max(int(usage_totals.get('total_tokens', 0)), int(state_token_usage.get('total_tokens', 0))),
    }
    if token_usage_for_pdf['total_tokens'] <= 0:
        token_usage_for_pdf['total_tokens'] = (
            int(token_usage_for_pdf['input_tokens']) + int(token_usage_for_pdf['output_tokens'])
        )

    _render_report_pdf(
        job_id=job_id,
        job_title=job.title,
        source_pdf_name=job.source_pdf_name,
        final_md_path=final_md_path,
        source_pdf_path=source_pdf,
        report_pdf_path=report_pdf_path,
        annotations=list(runtime.annotations),
        content_list=parse_result.content_list,
        token_usage=token_usage_for_pdf,
        agent_model=str(settings.agent_model).strip(),
    )

    def apply_completed(state):
        state.status = JobStatus.completed
        state.message = 'Review pipeline completed.'
        state.error = None
        state.final_report_ready = True
        state.pdf_ready = report_pdf_path.exists()
        state.artifacts.final_markdown_path = str(final_md_path)
        state.artifacts.report_pdf_path = str(report_pdf_path)

    mutate_job_state(job_id, apply_completed)
    append_event(job_id, 'completed', report_pdf_path=str(report_pdf_path))


def run_job(job_id: str) -> None:
    try:
        asyncio.run(run_job_async(job_id))
    except Exception as exc:
        detail = ''.join(traceback.format_exception_only(type(exc), exc)).strip()
        stack = traceback.format_exc()
        append_event(job_id, 'pipeline_exception', error=detail, stack=stack)
        fail_job(
            job_id,
            message='Review pipeline failed.',
            error=detail,
        )
