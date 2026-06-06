import argparse
import asyncio
import csv
import os
import re
import time
from pathlib import Path

import dotenv
dotenv.load_dotenv()

from paths import prompt_path, RESULTS_DIR
from tools import read_file, grep_file, allow_path

import weave
weave.init("rebuttal-agents")

from agents import Agent, OpenAIChatCompletionsModel, OpenAIResponsesModel, Runner
from agents.model_settings import ModelSettings
from openai import AsyncOpenAI

REBUTTAL_MODEL = os.environ.get("REBUTTAL_MODEL", "gpt-5.4")
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1/")
FEATHERLESS_BASE_URL = os.environ.get("FEATHERLESS_BASE_URL", "https://api.featherless.ai/v1")

custom_client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

_OR_COST_TOTAL = {"usd": 0.0, "calls": 0}


def install_openrouter_cost_hook(client: AsyncOpenAI) -> None:
    orig_create = client.chat.completions.create

    async def create_with_usage(*args, **kwargs):
        extra_body = dict(kwargs.get("extra_body") or {})
        extra_body.setdefault("usage", {"include": True})
        kwargs["extra_body"] = extra_body
        resp = await orig_create(*args, **kwargs)
        try:
            usage = getattr(resp, "usage", None)
            cost = None
            if usage is not None:
                cost = getattr(usage, "cost", None)
                if cost is None and hasattr(usage, "model_extra"):
                    cost = (usage.model_extra or {}).get("cost")
            if cost is not None:
                _OR_COST_TOTAL["usd"] += float(cost)
                _OR_COST_TOTAL["calls"] += 1
                print(f"  [openrouter] call cost=${float(cost):.6f} cumulative=${_OR_COST_TOTAL['usd']:.4f} (n={_OR_COST_TOTAL['calls']})")
        except Exception as e:
            print(f"  [openrouter] cost extraction failed: {e}")
        return resp

    client.chat.completions.create = create_with_usage


install_openrouter_cost_hook(custom_client)

from agents import set_default_openai_client, set_tracing_export_api_key
set_default_openai_client(custom_client)
set_tracing_export_api_key(os.environ["OPENAI_API_KEY"])

CONCURRENCY = int(os.environ.get("CONCURRENCY", 5))
MAX_RETRIES = 5
RETRY_DELAY = 10
_MODEL_SETTINGS = ModelSettings(extra_body={"effort": "xhigh"})


async def run_agent_with_retry(agent, prompt: str, max_turns: int = 30) -> tuple[str, object]:
    agent_name = agent.name
    print(f"  [{agent_name}] starting ...")
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            result = await Runner.run(agent, prompt, max_turns=max_turns)
            output = result.final_output
            if not output or not output.strip():
                if attempt < MAX_RETRIES:
                    print(f"  [{agent_name}] empty response (attempt {attempt}/{MAX_RETRIES}), retrying ...")
                    await asyncio.sleep(RETRY_DELAY + attempt * 5)
                    continue
                raise RuntimeError(f"[{agent_name}] empty response after {MAX_RETRIES} attempts")
            print(f"  [{agent_name}] done")
            return output, result.context_wrapper.usage
        except Exception as e:
            if attempt < MAX_RETRIES:
                wait = RETRY_DELAY * attempt
                print(f"  [{agent_name}] error (attempt {attempt}/{MAX_RETRIES}), waiting {wait}s ... {e}")
                await asyncio.sleep(wait)
            else:
                raise RuntimeError(f"[{agent_name}] {e}") from e
    raise RuntimeError(f"[{agent_name}] failed after {MAX_RETRIES} attempts")


def resolve_model(spec: str | None):
    if spec is None:
        return None
    if spec.startswith("ollama:"):
        name = spec[len("ollama:"):]
        client = AsyncOpenAI(api_key="ollama", base_url=OLLAMA_BASE_URL)
        return OpenAIChatCompletionsModel(model=name, openai_client=client)
    if spec.startswith("featherless:"):
        name = spec[len("featherless:"):]
        client = AsyncOpenAI(api_key=os.getenv("FEATHERLESS_API_KEY"), base_url=FEATHERLESS_BASE_URL)
        return OpenAIChatCompletionsModel(model=name, openai_client=client)
    return OpenAIResponsesModel(model=spec, openai_client=custom_client)


PAPER_ACCESS_FILE = "The paper path is provided in the user message. Use read_file to read the paper (it reads the whole file by default — do not pass start_line/end_line unless you specifically need a slice) and verify claims directly."

with open(prompt_path("timeline.md"), "r") as f:
    timeline = f.read().replace("{{CURRENT_DATE}}", time.strftime("%Y-%m-%d"))


def load_prompt(path):
    with open(prompt_path(path), "r") as f:
        content = f.read()
    content = content.replace("{{PAPER_ACCESS_INSTRUCTION}}", PAPER_ACCESS_FILE)
    content = content.replace("{{CALIBRATION_INSTRUCTION}}", "")
    return content + "\n\n" + timeline


# ── Agent definitions ────────────────────────────────────────────────

_tool_agents = [read_file, grep_file]

if REBUTTAL_MODEL.startswith("claude_sdk:"):
    rebuttal_agent = None
    meta_review_agent = None
    _SDK_MODEL = REBUTTAL_MODEL[len("claude_sdk:"):]
else:
    _SDK_MODEL = None
    rebuttal_agent = Agent(
        name="Author Rebuttal",
        instructions=load_prompt("rebuttal.md"),
        model=resolve_model(REBUTTAL_MODEL),
        tools=_tool_agents,
        model_settings=_MODEL_SETTINGS,
    )
    meta_review_agent = Agent(
        name="Meta Reviewer",
        instructions=load_prompt("meta_review.md"),
        model=resolve_model(REBUTTAL_MODEL),
        tools=_tool_agents,
        model_settings=_MODEL_SETTINGS,
    )


# ── Claude SDK path ──────────────────────────────────────────────────

def make_rebuttal_mcp_server(paper_dir: str):
    from claude_agent_sdk import create_sdk_mcp_server, tool
    import random

    allowed_paths = [os.path.abspath(paper_dir)]

    def check_path(path: str) -> str | None:
        resolved = os.path.abspath(path)
        if any(resolved.startswith(ap) for ap in allowed_paths):
            return None
        return f"ERROR: Access denied. Path '{resolved}' is not under any allowed directory: {allowed_paths}."

    @tool(
        "read_file",
        "Read lines from a file. Returns lines numbered start_line to end_line (1-based). If end_line is 0, reads to EOF.",
        {"abs_path": str, "start_line": int, "end_line": int},
    )
    async def sdk_read_file(args: dict) -> dict:
        time.sleep(random.uniform(0.5, 1.5))
        abs_path = args["abs_path"]
        start_line = args.get("start_line", 1) or 1
        end_line = args.get("end_line", 0) or 0
        print(f"  [claude:read_file] {abs_path} lines {start_line}-{end_line or 'EOF'}")
        err = check_path(abs_path)
        if err:
            return {"content": [{"type": "text", "text": err}], "is_error": True}
        try:
            with open(abs_path, "r", errors="replace") as fh:
                lines = fh.readlines()
            selected = lines[max(0, start_line - 1):end_line if end_line > 0 else len(lines)]
            text = "".join(f"{start_line + i}: {line}" for i, line in enumerate(selected))
            return {"content": [{"type": "text", "text": text}]}
        except FileNotFoundError:
            return {"content": [{"type": "text", "text": f"ERROR: File not found: {abs_path}"}], "is_error": True}

    @tool(
        "grep_file",
        "Search a single file for a substring pattern. Returns matching lines with line numbers.",
        {"pattern": str, "abs_path": str},
    )
    async def sdk_grep_file(args: dict) -> dict:
        pattern = args["pattern"]
        abs_path = args["abs_path"]
        print(f"  [claude:grep_file] pattern='{pattern}' in '{abs_path}'")
        err = check_path(abs_path)
        if err:
            return {"content": [{"type": "text", "text": err}], "is_error": True}
        if not os.path.isfile(abs_path):
            return {"content": [{"type": "text", "text": f"ERROR: '{abs_path}' is not a file."}], "is_error": True}
        matches = []
        try:
            with open(abs_path, "r", errors="replace") as fh:
                for i, line in enumerate(fh, 1):
                    if re.search(pattern, line):
                        matches.append(f"{i}: {line.rstrip()}")
        except Exception as e:
            return {"content": [{"type": "text", "text": f"ERROR: {e}"}], "is_error": True}
        text = "\n".join(matches) if matches else "No matches found."
        return {"content": [{"type": "text", "text": text}]}

    return create_sdk_mcp_server(
        name="rebuttal_fs",
        version="1.0.0",
        tools=[sdk_read_file, sdk_grep_file],
    )


async def run_claude_sdk_agent(label: str, system_prompt: str, user_prompt: str, paper_dir: str) -> tuple[str, dict]:
    from claude_agent_sdk import (
        ClaudeSDKClient,
        ClaudeAgentOptions,
        AssistantMessage,
        TextBlock,
        ResultMessage,
        RateLimitEvent,
    )
    import random

    print(f"  [{label}] starting Claude Agent SDK ({_SDK_MODEL}) ...")

    mcp_server = make_rebuttal_mcp_server(paper_dir)
    options = ClaudeAgentOptions(
        model=_SDK_MODEL,
        allowed_tools=["mcp__rebuttal_fs__read_file", "mcp__rebuttal_fs__grep_file"],
        permission_mode="bypassPermissions",
        disallowed_tools=["Read", "Glob", "Grep", "Bash", "Edit", "Write", "WebSearch", "WebFetch"],
        mcp_servers={"rebuttal_fs": mcp_server},
        max_turns=30,
        cwd="/tmp",
    )

    full_prompt = f"{system_prompt}\n\n---\n\n{user_prompt}"

    result_text = ""
    sdk_usage = {
        "model": _SDK_MODEL,
        "session_id": None,
        "total_cost_usd": None,
        "num_turns": None,
        "duration_ms": None,
        "duration_api_ms": None,
        "usage": None,
        "rate_limit": None,
    }
    time.sleep(random.uniform(20, 40))

    async with ClaudeSDKClient(options=options) as sdk_client:
        await sdk_client.query(full_prompt)
        async for message in sdk_client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        result_text += block.text
            elif isinstance(message, ResultMessage):
                sdk_usage["session_id"] = message.session_id
                sdk_usage["total_cost_usd"] = message.total_cost_usd
                sdk_usage["num_turns"] = message.num_turns
                sdk_usage["duration_ms"] = message.duration_ms
                sdk_usage["duration_api_ms"] = message.duration_api_ms
                sdk_usage["usage"] = message.usage
            elif isinstance(message, RateLimitEvent):
                info = message.rate_limit_info
                sdk_usage["rate_limit"] = {
                    "status": info.status,
                    "type": info.rate_limit_type,
                    "utilization": info.utilization,
                    "resets_at": info.resets_at,
                    "overage_status": info.overage_status,
                    "overage_resets_at": info.overage_resets_at,
                }

    if not result_text.strip():
        raise RuntimeError(f"[{label}] Claude Agent SDK returned empty output")

    print(f"  [{label}] done — {_SDK_MODEL} (Claude Agent SDK)")
    return result_text, sdk_usage


# ── Core pipeline ────────────────────────────────────────────────────

async def run_rebuttal_pipeline(paper_path: str, review_path: str) -> dict:
    _or_cost_start = dict(_OR_COST_TOTAL)
    paper_path_abs = os.path.abspath(paper_path)
    review_path_abs = os.path.abspath(review_path)

    with open(review_path_abs, "r") as f:
        review_content = f.read()

    paper_dir = str(Path(paper_path_abs).parent)
    allow_path(paper_dir)

    # ── Phase 1: Author Rebuttal ──
    print("  Phase 1: Author Rebuttal ...")
    rebuttal_user_prompt = (
        f"Paper path: {paper_path_abs} — use read_file to read the paper.\n\n"
        f"--- REVIEW START ---\n{review_content}\n--- REVIEW END ---\n\n"
        f"Write a rebuttal addressing every weakness in this review. "
        f"Ground every claim in the paper text."
    )

    sdk_usages = {}
    agent_usages = {}

    if _SDK_MODEL is not None:
        rebuttal_system = load_prompt("rebuttal.md")
        rebuttal_text, rebuttal_sdk_usage = await run_claude_sdk_agent(
            "Author Rebuttal", rebuttal_system, rebuttal_user_prompt, paper_dir
        )
        sdk_usages["Author Rebuttal"] = rebuttal_sdk_usage
        agent_usages["Author Rebuttal"] = None
    else:
        rebuttal_text, rebuttal_usage = await run_agent_with_retry(rebuttal_agent, rebuttal_user_prompt)
        agent_usages["Author Rebuttal"] = rebuttal_usage

    # ── Phase 2: Meta Review ──
    print("  Phase 2: Meta Review ...")
    meta_user_prompt = (
        f"Paper path: {paper_path_abs} — use read_file to read the paper.\n\n"
        f"--- ORIGINAL REVIEW START ---\n{review_content}\n--- ORIGINAL REVIEW END ---\n\n"
        f"--- AUTHOR REBUTTAL START ---\n{rebuttal_text}\n--- AUTHOR REBUTTAL END ---\n\n"
        f"Evaluate the rebuttal against the paper. The author is biased — verify every claim "
        f"they make by reading the paper yourself. Then produce an updated review with a final score."
    )

    if _SDK_MODEL is not None:
        meta_system = load_prompt("meta_review.md")
        meta_text, meta_sdk_usage = await run_claude_sdk_agent(
            "Meta Reviewer", meta_system, meta_user_prompt, paper_dir
        )
        sdk_usages["Meta Reviewer"] = meta_sdk_usage
        agent_usages["Meta Reviewer"] = None
    else:
        meta_text, meta_usage = await run_agent_with_retry(meta_review_agent, meta_user_prompt)
        agent_usages["Meta Reviewer"] = meta_usage

    # ── Parse score/decision ──
    scorer_output = float(meta_text.split("<score>")[1].split("</score>")[0]) if "<score>" in meta_text else -1
    decision = (meta_text.split("<decision>")[1].split("</decision>")[0]) if "<decision>" in meta_text else "N/A"

    if scorer_output == -1 or decision == "N/A":
        print(f"  Parsing failed (score={scorer_output}, decision={decision}); falling back to extractor")
        extractor_resp = await custom_client.chat.completions.create(
            model="deepseek/deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "Extract the final numeric score and accept/reject decision from a paper review. Respond with exactly: <score>NUMBER</score><decision>Accept|Reject</decision>. No other text."},
                {"role": "user", "content": meta_text},
            ],
            extra_body={"reasoning": {"enabled": False}},
        )
        extracted = extractor_resp.choices[0].message.content or ""
        if scorer_output == -1 and "<score>" in extracted:
            scorer_output = float(extracted.split("<score>")[1].split("</score>")[0])
        if decision == "N/A" and "<decision>" in extracted:
            decision = extracted.split("<decision>")[1].split("</decision>")[0]
        print(f"  [extractor] score={scorer_output} decision={decision}")

    # ── Logging ──
    _or_cost_paper = _OR_COST_TOTAL["usd"] - _or_cost_start["usd"]
    _or_calls_paper = _OR_COST_TOTAL["calls"] - _or_cost_start["calls"]

    token_lines = []
    total_input = total_output = total_tokens = 0
    for agent_name, usage in agent_usages.items():
        if usage is None:
            token_lines.append(f"  {agent_name}: N/A (claude_sdk path)")
        else:
            cached = getattr(getattr(usage, "input_tokens_details", None), "cached_tokens", None)
            reasoning = getattr(getattr(usage, "output_tokens_details", None), "reasoning_tokens", None)
            token_lines.append(
                f"  {agent_name}: input={usage.input_tokens} (cached={cached}) "
                f"output={usage.output_tokens} (reasoning={reasoning}) "
                f"total={usage.total_tokens} requests={usage.requests}"
            )
            total_input += usage.input_tokens
            total_output += usage.output_tokens
            total_tokens += usage.total_tokens
    token_lines.append(f"  TOTAL: input={total_input} output={total_output} total={total_tokens}")
    token_lines.append(f"  OpenRouter cost (this paper): ${_or_cost_paper:.6f} over {_or_calls_paper} calls")

    sdk_lines = []
    sdk_total_cost = 0.0
    for sdk_name, su in sdk_usages.items():
        u = (su or {}).get("usage") or {}
        sdk_lines.append(f"  [{sdk_name}]")
        sdk_lines.append(f"    Model: {su.get('model')}")
        sdk_lines.append(f"    Session ID: {su.get('session_id')}")
        sdk_lines.append(f"    Cost (USD): {su.get('total_cost_usd')}")
        sdk_lines.append(f"    Turns: {su.get('num_turns')}")
        sdk_lines.append(f"    Duration: total={su.get('duration_ms')}ms api={su.get('duration_api_ms')}ms")
        sdk_lines.append(
            f"    Tokens: input={u.get('input_tokens')} output={u.get('output_tokens')} "
            f"cache_read={u.get('cache_read_input_tokens')} cache_creation={u.get('cache_creation_input_tokens')}"
        )
        if su.get("total_cost_usd"):
            sdk_total_cost += su["total_cost_usd"]
    if sdk_lines:
        sdk_lines.append(f"  TOTAL Claude SDK cost (USD): {sdk_total_cost:.4f}")

    log_path = Path(os.environ.get("REBUTTAL_LOG", str(RESULTS_DIR / "rebuttal_pipeline.log")))
    if not log_path.is_absolute():
        log_path = RESULTS_DIR / log_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as log_f:
        log_f.write(f"\n{'='*60}\n")
        log_f.write(f"Paper: {paper_path}\n")
        log_f.write(f"Review: {review_path}\n")
        log_f.write(f"Timestamp: {time.strftime('%Y-%m-%dT%H:%M:%S')}\n")
        log_f.write(f"\n--- Token Usage ---\n" + "\n".join(token_lines) + "\n")
        if sdk_lines:
            log_f.write(f"\n--- Claude SDK Usage ---\n" + "\n".join(sdk_lines) + "\n")
        log_f.write(f"\n--- Author Rebuttal ---\n{rebuttal_text}\n")
        log_f.write(f"\n--- Meta Review ---\n{meta_text}\n")
        log_f.write(f"\n--- Scorer Output ---\n{scorer_output}\n")
        log_f.write(f"\n--- Decision ---\n{decision}\n")

    return {
        "rebuttal_text": rebuttal_text,
        "meta_review": meta_text,
        "scorer_output": scorer_output,
        "decision": decision,
        "sdk_usages": sdk_usages,
    }


# ── Helpers (match main.py) ────────────────────────────────────────────

def load_ground_truth(data_dir: Path) -> dict[str, dict]:
    csv_file = data_dir / "ratings.csv"
    if not csv_file.exists():
        return {}
    index = {}
    with open(csv_file, "r") as f:
        for row in csv.DictReader(f):
            pid = row["paper_id"].strip()
            scores = [float(row[f"score_{i}"]) for i in range(7) if row.get(f"score_{i}", "").strip()]
            decision = row.get("decision", "").strip()
            gt_binary = row.get("gt_binary", "").strip() or ("Accept" if "Accept" in decision else "Reject")
            index[pid] = {
                "scores": scores,
                "avg_score": float(row.get("avg_score", 0)),
                "decision": decision,
                "gt_binary": gt_binary,
            }
    return index


def decision_match(predicted: str | None, gt_binary: str) -> bool | None:
    if predicted in (None, "", "N/A"):
        return None
    return predicted == gt_binary


def match_label(match: bool | None) -> str:
    if match is None:
        return "N/A"
    return "YES" if match else "NO"


CSV_HEADER = [
    "paper_id", "pred_score", "pred_decision", "gt_avg_score", "gt_decision",
    "gt_binary", "match", "cost", "sdk_savings",
    "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6",
]


# ── Batch mode ────────────────────────────────────────────────────────

async def run_rebuttal_batch(reviews_dir: str, papers_dir: str):
    reviews_path = Path(reviews_dir)
    papers_path = Path(papers_dir)

    csv_path = Path(os.getenv("OUTPUT_CSV", str(RESULTS_DIR / "scores.csv")))
    if not csv_path.is_absolute():
        csv_path = RESULTS_DIR / csv_path
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    reviews_out = Path(os.getenv("REVIEWS_DIR", str(RESULTS_DIR / "rebuttal_reviews")))
    if not reviews_out.is_absolute():
        reviews_out = RESULTS_DIR / reviews_out
    reviews_out.mkdir(parents=True, exist_ok=True)

    gt_index = load_ground_truth(papers_path.parent)
    if gt_index:
        print(f"Loaded ground truth for {len(gt_index)} papers")
    else:
        print("No ratings.csv found — CSV will have empty gt columns")

    review_files = sorted([f for f in reviews_path.iterdir() if f.suffix == ".md"])
    print(f"Found {len(review_files)} reviews in {reviews_dir}")

    finished = {f.stem for f in reviews_out.iterdir() if f.suffix == ".md"}
    review_files = [f for f in review_files if f.stem not in finished]
    if finished:
        print(f"Skipping {len(finished)} already-finished papers")
    if not review_files:
        print("Nothing to run.")
        return

    if not finished:
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(CSV_HEADER)

    sem = asyncio.Semaphore(CONCURRENCY)

    async def process_one(i, review_file):
        paper_id = review_file.stem
        paper_file = papers_path / f"{paper_id}.txt"
        if not paper_file.exists():
            print(f"  [{paper_id}] paper file not found: {paper_file}, skipping")
            return
        print(f"\n[{i}/{len(review_files)}] {paper_id}")
        async with sem:
            try:
                result = await run_rebuttal_pipeline(str(paper_file), str(review_file))
            except Exception as e:
                print(f"  [{paper_id}] pipeline failed: {type(e).__name__}: {e}")
                return
            if result is None:
                print(f"  [{paper_id}] pipeline returned None, skipping")
                return

        (reviews_out / f"{paper_id}.md").write_text(result["meta_review"], encoding="utf-8")

        gt = gt_index.get(paper_id, {})
        gt_scores = gt.get("scores", [])
        gt_scores_padded = gt_scores + [""] * (7 - len(gt_scores))
        gt_avg = gt.get("avg_score", "")
        gt_decision = gt.get("decision", "")
        gt_binary = gt.get("gt_binary", "")
        match = decision_match(result["decision"], gt_binary) if gt_binary else None
        match_str = match_label(match)

        with open(csv_path, "a", newline="") as f:
            csv.writer(f).writerow([
                paper_id,
                result["scorer_output"],
                result["decision"],
                f"{gt_avg:.2f}" if isinstance(gt_avg, float) else gt_avg,
                gt_decision,
                gt_binary,
                match_str,
                "0.0000",
                "0.0000",
                *gt_scores_padded,
            ])
        print(f"  [{paper_id}] pred={result['scorer_output']} gt={gt_avg} match={match_str}")

    await asyncio.gather(*(process_one(i, f) for i, f in enumerate(review_files, 1)))
    print(f"\nDone. Results in {reviews_out}")


# ── Single paper mode ─────────────────────────────────────────────────

async def run_single_rebuttal(paper_path: str, review_path: str, output_dir: str | None = None):
    print(f"Paper: {paper_path}")
    print(f"Review: {review_path}")

    result = await run_rebuttal_pipeline(paper_path, review_path)

    print(f"\n{'=' * 72}\nFINAL REVIEW\n{'=' * 72}\n{result['meta_review']}")
    score = result["scorer_output"]
    if score != -1:
        print(f"\nPredicted score: {score}")
    print(f"Decision: {result['decision']}")

    sdk_usages = result.get("sdk_usages") or {}
    if sdk_usages:
        print(f"\n{'=' * 72}\nClaude SDK Usage\n{'=' * 72}")
        total_cost = 0.0
        for name, su in sdk_usages.items():
            u = (su or {}).get("usage") or {}
            print(f"  [{name}]")
            print(f"    Model:         {su.get('model')}")
            print(f"    Session ID:    {su.get('session_id')}")
            print(f"    Cost (USD):    ${su.get('total_cost_usd')}")
            print(f"    Turns:         {su.get('num_turns')}")
            print(f"    Duration:      total={su.get('duration_ms')}ms api={su.get('duration_api_ms')}ms")
            print(f"    Input tokens:  {u.get('input_tokens')}")
            print(f"    Output tokens: {u.get('output_tokens')}")
            print(f"    Cache read:    {u.get('cache_read_input_tokens')}")
            print(f"    Cache create:  {u.get('cache_creation_input_tokens')}")
            if su.get("total_cost_usd"):
                total_cost += su["total_cost_usd"]
        print(f"  TOTAL Claude SDK cost (USD): ${total_cost:.4f}")

    if output_dir:
        out = Path(output_dir)
    else:
        out = Path(__file__).parent / "reviews"
    out.mkdir(parents=True, exist_ok=True)

    paper_stem = Path(paper_path).stem.split(".")[0]
    ts = time.strftime("%Y_%m_%d_%H_%M_%S")
    with open(out / f"{paper_stem}_review_{ts}.md", "w", encoding="utf-8") as f:
        f.write(result["meta_review"])
        f.write(f"\n\n**Predicted score: {score}**\n" if score != -1 else "")


# ── CLI ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rebuttal + meta-review pipeline")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--single", nargs=2, metavar=("PAPER_PATH", "REVIEW_PATH"),
                       help="Run rebuttal on a single paper + review pair")
    group.add_argument("--batch", nargs=2, metavar=("REVIEWS_DIR", "PAPERS_DIR"),
                       help="Run rebuttal on all reviews in a directory")
    args = parser.parse_args()

    if args.single:
        paper, review = args.single
        asyncio.run(run_single_rebuttal(paper, review))
    elif args.batch:
        reviews_dir, papers_dir = args.batch
        asyncio.run(run_rebuttal_batch(reviews_dir, papers_dir))
