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
weave.init("rescore-agents")

from agents import Agent, OpenAIChatCompletionsModel, OpenAIResponsesModel, Runner, function_tool
from agents.model_settings import ModelSettings
from openai import AsyncOpenAI
from agents import set_default_openai_client, set_tracing_export_api_key

RESCORE_MODEL = os.environ.get("RESCORE_MODEL", "deepseek-v4-flash")
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


# ── Prompt loading ────────────────────────────────────────────────────

PAPER_ACCESS_FILE = "The paper path is provided in the user message. Use read_file to read the paper (it reads the whole file by default — do not pass start_line/end_line unless you specifically need a slice) and verify reviewer claims directly."

with open(prompt_path("timeline.md"), "r") as f:
    timeline = f.read().replace("{{CURRENT_DATE}}", time.strftime("%Y-%m-%d"))

with open(prompt_path("cal_without.md"), "r") as f:
    CAL_INSTRUCTION_WITHOUT = f.read()

SUBSCORES_ENDING = """IMPORTANT: At the very end of your response, you MUST write exactly these lines:
MY FINAL SCORE: <score>score</score>
MY FINAL DECISION: <decision>Accept/Reject</decision>

Then immediately output 6 subscores (integers 0–5) in this exact XML format:
<subscores>
<originality>X</originality>
<importance>X</importance>
<claims_supported>X</claims_supported>
<soundness>X</soundness>
<clarity>X</clarity>
<community_value>X</community_value>
</subscores>"""

ORIGINAL_ENDING = """IMPORTANT: At the very end of your response, you MUST write exactly this line (using a score XML tag):
MY FINAL SCORE: <score>score</score>
MY FINAL DECISION: <decision>Accept/Reject</decision>"""


def load_merger_prompt_with_subscores():
    with open(prompt_path("merger.md"), "r") as f:
        raw_lines = f.readlines()
    kept_lines = []
    for lineno, line in enumerate(raw_lines, start=1):
        if line.lstrip().startswith("&&"):
            continue
        kept_lines.append(line)
    content = "".join(kept_lines)
    content = content.replace("{{PAPER_ACCESS_INSTRUCTION}}", PAPER_ACCESS_FILE)
    content = content.replace("{{CALIBRATION_INSTRUCTION}}", CAL_INSTRUCTION_WITHOUT)
    content = content.replace(ORIGINAL_ENDING, SUBSCORES_ENDING)
    return content + "\n\n" + timeline


# ── Agent definitions ─────────────────────────────────────────────────

@function_tool
def draft_review(draft: str) -> str:
    """Record the merger's post-filtering draft before calibration or final writing."""
    return "draft recorded"


if RESCORE_MODEL.startswith("claude_sdk:"):
    rescore_agent = None
    _SDK_MODEL = RESCORE_MODEL[len("claude_sdk:"):]
else:
    _SDK_MODEL = None
    rescore_agent = Agent(
        name="Rescorer",
        instructions=load_merger_prompt_with_subscores(),
        model=resolve_model(RESCORE_MODEL),
        tools=[read_file, grep_file, draft_review],
        model_settings=_MODEL_SETTINGS,
    )


# ── Log parsing ───────────────────────────────────────────────────────

SUBSCORE_DIMS = ["originality", "importance", "claims_supported", "soundness", "clarity", "community_value"]


def parse_pipeline_log(log_path: str) -> list[dict]:
    with open(log_path, "r") as f:
        log = f.read()
    seen = {}
    for seg in log.split("=" * 60)[1:]:
        if "--- Merged Inputs ---" not in seg:
            continue
        paper_line = seg.split("Paper: ")[-1].split("\n")[0].strip() if "Paper: " in seg else None
        if not paper_line:
            continue
        cached_inputs = seg.split("--- Merged Inputs ---")[-1].split("--- Merged Review ---")[0].strip()
        if not cached_inputs:
            continue
        paper_id = Path(paper_line).stem
        seen[paper_id] = {
            "paper_id": paper_id,
            "paper_path": paper_line,
            "cached_inputs": cached_inputs,
        }
    return list(seen.values())


def parse_subscores(text: str) -> dict:
    subscores = {}
    for dim in SUBSCORE_DIMS:
        match = re.search(rf"<{dim}>\s*(\d+)\s*</{dim}>", text)
        subscores[dim] = int(match.group(1)) if match else -1
    return subscores


# ── Claude SDK path ───────────────────────────────────────────────────

async def run_rescore_claude_sdk(paper_path_abs: str, cached_inputs: str, paper_dir: str) -> tuple[str, dict]:
    from claude_merger import _make_merger_mcp_server, _run_claude_sdk_query

    system_prompt = load_merger_prompt_with_subscores()
    mcp_server = _make_merger_mcp_server(paper_dir, no_cal=True)

    user_prompt = (
        f"Here is the paper being reviewed (extracted from PDF — formatting "
        f"artifacts are parser issues, not paper problems).\n\n"
        f"Paper path: {paper_path_abs} — use read_file to read it.\n\n"
        f"Here are the inputs:\n\n{cached_inputs}\n\n"
        f"Now produce the final consolidated review following your instructions. "
        f"Remember: many of the harsh critic's points may be nonsensical or overly "
        f"picky — cross-check everything against the actual paper before including it."
    )

    return await _run_claude_sdk_query(
        label="Rescorer",
        model_id=_SDK_MODEL,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        allowed_tools=[
            "mcp__merger_fs__read_file",
            "mcp__merger_fs__grep_file",
            "mcp__merger_fs__draft_review",
        ],
        mcp_servers={"merger_fs": mcp_server},
        max_turns=30,
    )


# ── Core pipeline ────────────────────────────────────────────────────

async def run_rescore_pipeline(paper_path: str, cached_inputs: str) -> dict:
    _or_cost_start = dict(_OR_COST_TOTAL)
    paper_path_abs = os.path.abspath(paper_path)
    paper_dir = str(Path(paper_path_abs).parent)
    allow_path(paper_dir)

    user_prompt = (
        f"Here is the paper being reviewed (extracted from PDF — formatting "
        f"artifacts are parser issues, not paper problems).\n\n"
        f"Paper path: {paper_path_abs} — use read_file (which reads the whole file by default; "
        f"do not pass start_line/end_line unless you specifically need a slice) or grep_file to read it.\n\n"
        f"Here are the inputs:\n\n{cached_inputs}\n\n"
        f"Now produce the final consolidated review following your instructions. "
        f"Remember: many of the harsh critic's points may be nonsensical or overly "
        f"picky — cross-check everything against the actual paper before including it."
    )

    sdk_usages = {}
    agent_usages = {}

    if _SDK_MODEL is not None:
        merged_review, sdk_usage = await run_rescore_claude_sdk(paper_path_abs, cached_inputs, paper_dir)
        sdk_usages["Rescorer"] = sdk_usage
        agent_usages["Rescorer"] = None
    else:
        start_time = time.monotonic()
        merged_review, usage = await run_agent_with_retry(rescore_agent, user_prompt)
        end_time = time.monotonic()
        usage.duration_ms = int((end_time - start_time) * 1000)
        agent_usages["Rescorer"] = usage

    scorer_output = float(merged_review.split("<score>")[1].split("</score>")[0]) if "<score>" in merged_review else -1
    decision = (merged_review.split("<decision>")[1].split("</decision>")[0]) if "<decision>" in merged_review else "N/A"

    if scorer_output == -1 or decision == "N/A":
        print(f"  Parsing failed (score={scorer_output}, decision={decision}); falling back to extractor")
        extractor_resp = await custom_client.chat.completions.create(
            model="deepseek/deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "Extract the final numeric score and accept/reject decision from a paper review. Respond with exactly: <score>NUMBER</score><decision>Accept|Reject</decision>. No other text."},
                {"role": "user", "content": merged_review},
            ],
            extra_body={"reasoning": {"enabled": False}},
        )
        extracted = extractor_resp.choices[0].message.content or ""
        if scorer_output == -1 and "<score>" in extracted:
            scorer_output = float(extracted.split("<score>")[1].split("</score>")[0])
        if decision == "N/A" and "<decision>" in extracted:
            decision = extracted.split("<decision>")[1].split("</decision>")[0]
        print(f"  [extractor] score={scorer_output} decision={decision}")

    subscores = parse_subscores(merged_review)

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

    log_path = Path(os.environ.get("RESCORE_LOG", str(RESULTS_DIR / "rescore_pipeline.log")))
    if not log_path.is_absolute():
        log_path = RESULTS_DIR / log_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as log_f:
        log_f.write(f"\n{'='*60}\n")
        log_f.write(f"Paper: {paper_path}\n")
        log_f.write(f"Timestamp: {time.strftime('%Y-%m-%dT%H:%M:%S')}\n")
        log_f.write(f"\n--- Token Usage ---\n" + "\n".join(token_lines) + "\n")
        if sdk_lines:
            log_f.write(f"\n--- Claude SDK Usage ---\n" + "\n".join(sdk_lines) + "\n")
        log_f.write(f"\n--- Cached Inputs ---\n\n{cached_inputs}\n")
        log_f.write(f"\n--- Merged Review ---\n{merged_review}\n")
        log_f.write(f"\n--- Scorer Output ---\n{scorer_output}\n")
        log_f.write(f"\n--- Decision ---\n{decision}\n")
        log_f.write(f"\n--- Subscores ---\n")
        for dim in SUBSCORE_DIMS:
            log_f.write(f"  {dim}: {subscores[dim]}\n")

    return {
        "merged_review": merged_review,
        "scorer_output": scorer_output,
        "decision": decision,
        "subscores": subscores,
        "sdk_usages": sdk_usages,
    }


# ── Batch mode ────────────────────────────────────────────────────────

CSV_HEADER = [
    "paper_id", "pred_score", "pred_decision",
    "originality", "importance", "claims_supported", "soundness", "clarity", "community_value",
]


async def run_rescore_batch(log_path: str, papers_dir: str | None = None):
    entries = parse_pipeline_log(log_path)
    print(f"Parsed {len(entries)} papers from {log_path}")

    if papers_dir:
        for entry in entries:
            entry["paper_path"] = str(Path(papers_dir) / Path(entry["paper_path"]).name)

    csv_path = Path(os.getenv("OUTPUT_CSV", str(RESULTS_DIR / "rescore_scores.csv")))
    if not csv_path.is_absolute():
        csv_path = RESULTS_DIR / csv_path
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    reviews_dir = Path(os.getenv("REVIEWS_DIR", str(RESULTS_DIR / "rescore_reviews")))
    if not reviews_dir.is_absolute():
        reviews_dir = RESULTS_DIR / reviews_dir
    reviews_dir.mkdir(parents=True, exist_ok=True)

    finished = set()
    if csv_path.exists() and csv_path.stat().st_size > 0:
        import pandas as pd
        existing_df = pd.read_csv(csv_path)
        finished = set(existing_df["paper_id"].astype(str))
        print(f"Skipping {len(finished)} already-finished papers")

    entries = [e for e in entries if e["paper_id"] not in finished]
    if not entries:
        print("Nothing to run.")
        return

    if not finished:
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(CSV_HEADER)

    print(f"Running {len(entries)} papers (concurrency={CONCURRENCY}) ...")
    sem = asyncio.Semaphore(CONCURRENCY)

    async def process_one(i, entry):
        paper_id = entry["paper_id"]
        paper_path = entry["paper_path"]
        if not os.path.exists(paper_path):
            print(f"  [{paper_id}] paper file not found: {paper_path}, skipping")
            return
        print(f"\n[{i}/{len(entries)}] {paper_id}")
        async with sem:
            try:
                result = await run_rescore_pipeline(paper_path, entry["cached_inputs"])
            except Exception as e:
                print(f"  [{paper_id}] pipeline failed: {type(e).__name__}: {e}")
                return
            if result is None:
                print(f"  [{paper_id}] pipeline returned None, skipping")
                return

        (reviews_dir / f"{paper_id}.md").write_text(result["merged_review"], encoding="utf-8")

        subscores = result["subscores"]
        with open(csv_path, "a", newline="") as f:
            csv.writer(f).writerow([
                paper_id,
                result["scorer_output"],
                result["decision"],
                subscores["originality"],
                subscores["importance"],
                subscores["claims_supported"],
                subscores["soundness"],
                subscores["clarity"],
                subscores["community_value"],
            ])
        print(f"  [{paper_id}] score={result['scorer_output']} decision={result['decision']} subscores={subscores}")

    await asyncio.gather(*(process_one(i, e) for i, e in enumerate(entries, 1)))
    print(f"\nDone. Results in {csv_path}")


# ── CLI ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Re-score from cached merger pipeline log")
    parser.add_argument("log_path", type=str, help="Path to the pipeline merge.log file")
    parser.add_argument("--papers_dir", type=str, default=None,
                        help="Override papers directory (remap paths from the log)")
    args = parser.parse_args()

    asyncio.run(run_rescore_batch(args.log_path, papers_dir=args.papers_dir))
