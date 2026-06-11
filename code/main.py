import argparse
import asyncio
import csv
import json
import random
import re
import logging
import os
import sys
import time
from collections import defaultdict
from pathlib import Path
from pydantic import BaseModel


def _extract_cli_arg(flag: str) -> str | None:
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return None


_cli_calibration_set = _extract_cli_arg("--calibration_set")
if _cli_calibration_set:
    os.environ["CALIBRATION_SET"] = _cli_calibration_set

if "--position" in sys.argv:
    os.environ["POSITION_MODE"] = "1"

_POSITION_MODE = os.environ.get("POSITION_MODE", "").strip().lower() in ("1", "true", "yes")

from paths import prompt_path, RESULTS_DIR
from tools import CALIBRATION_REVIEW_DIR, read_file, read_file_full, grep_file, search_file, _search_file_impl  # glob_files removed (unused)
import weave
weave.init("openai-agents")

from agents import Agent, OpenAIChatCompletionsModel, OpenAIResponsesModel, Runner, function_tool
from agents.model_settings import ModelSettings

_OPENROUTER_PROVIDER = os.environ.get("OPENROUTER_PROVIDER", "deepseek").strip()
# _MODEL_SETTINGS = ModelSettings(extra_body={"effort": "xhigh"})
_MODEL_SETTINGS = ModelSettings(extra_body={"provider": {"only": [_OPENROUTER_PROVIDER]}, "effort": "max"})
import dotenv
dotenv.load_dotenv()
os.environ["OPENAI_DEFAULT_MODEL"] = os.getenv("OPENAI_DEFAULT_MODEL", "z-ai/glm-5.1")
HARSH_MODEL = os.environ.get("HARSH_MODEL", "gpt-5.4")
NEUTRAL_MODEL = os.environ.get("NEUTRAL_MODEL")
MERGER_MODEL = os.environ.get("MERGER_MODEL", "ollama:glm-5.1:cloud")
SUBAGENT_MODEL = os.environ.get("SUBAGENT_MODEL", MERGER_MODEL)  # calibration_search subagent (OpenAI merger path)
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1/")
FEATHERLESS_BASE_URL = os.environ.get("FEATHERLESS_BASE_URL", "https://api.featherless.ai/v1")
# MERGER_MODEL = "claude_sdk:claude-sonnet-4-6" # use dash instead of dot in claude sdk
# MERGER_MODEL = "claude-sonnet-4.6"
from openai import AsyncOpenAI
from agents import set_default_openai_client, set_tracing_export_api_key

custom_client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

# OpenRouter usage accounting — inject {"usage": {"include": true}} into every
# chat completion and accumulate the per-response `cost` field returned by OR.
# https://openrouter.ai/docs/cookbook/administration/usage-accounting
_OR_COST_TOTAL = {"usd": 0.0, "calls": 0}


def _install_openrouter_cost_hook(client: AsyncOpenAI) -> None:
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

    client.chat.completions.create = create_with_usage  # type: ignore[assignment]


_install_openrouter_cost_hook(custom_client)
set_default_openai_client(custom_client)
tracing_api_key = os.environ["OPENAI_API_KEY"]
set_tracing_export_api_key(tracing_api_key)
# Suppress SDK's internal error logging — we handle errors in run_agent_with_retry
# logging.getLogger("openai.agents").setLevel(logging.CRITICAL) # this should be commented out in production to handle unexpected errors
from helpers import _detect_leakage


_error_log_path = Path(__file__).parent / "error.log"
_error_logger = logging.getLogger("gpt_agent_sdk.errors")
_error_logger.setLevel(logging.ERROR)
_error_handler = logging.FileHandler(_error_log_path, mode="a")
_error_handler.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
_error_logger.addHandler(_error_handler)

HUMAN_REVIEW_DIR = CALIBRATION_REVIEW_DIR
CONCURRENCY = int(os.environ.get("CONCURRENCY", 1))
print(f"Calibration review dir: {HUMAN_REVIEW_DIR}")

# ── Agent-level retry ────────────────────────────────────────────────
MAX_RETRIES = 5
RETRY_DELAY = 10


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


# ── Prompt loading ───────────────────────────────────────────────────
with open(prompt_path("timeline.md"), "r") as f:
    timeline = f.read().replace("{{CURRENT_DATE}}", time.strftime("%Y-%m-%d"))


PAPER_ACCESS_INJECTION = "The full paper text is included in the user message. Use it to verify reviewer claims directly."
PAPER_ACCESS_FILE = "The paper path is provided in the user message. Use read_file to read the paper (it reads the whole file by default — do not pass start_line/end_line unless you specifically need a slice) and verify reviewer claims directly."
PAPER_ACCESS_CHUNKED = """The paper path is provided in the user message. The paper is NOT included inline — read it from disk in sequential chunks using read_file with start_line/end_line, and use grep_file to locate specific claims or sections.

Read the paper progressively, one chunk at a time. After each chunk, before reading the next one, pause and reason: think through what this part of the paper claims, whether the method/evidence/argument in it holds up, and note any concerns or strengths it surfaces. Build your assessment incrementally as you go — do not dump the whole paper into context and review it all at the end. Only move to the next chunk once you have thought through the current one. Choose reasonable chunk sizes (e.g. a section or a few hundred lines at a time)."""

with open(prompt_path("cal_with.md"), "r") as _f:
    CAL_INSTRUCTION_WITH = _f.read()

with open(prompt_path("cal_without.md"), "r") as _f:
    CAL_INSTRUCTION_WITHOUT = _f.read()


def load_prompts(path, paper_access: str = PAPER_ACCESS_INJECTION, no_cal: bool = False):
    with open(prompt_path(path), "r") as f:
        raw_lines = f.readlines()
    kept_lines = []
    for lineno, line in enumerate(raw_lines, start=1):
        if line.lstrip().startswith("&&"):
            print(f"WARNING: ignoring commented line {lineno} in prompts/{path}: {line.rstrip()}")
            continue
        kept_lines.append(line)
    content = "".join(kept_lines)
    content = content.replace("{{PAPER_ACCESS_INSTRUCTION}}", paper_access)
    cal_instruction = CAL_INSTRUCTION_WITHOUT if no_cal else CAL_INSTRUCTION_WITH
    content = content.replace("{{CALIBRATION_INSTRUCTION}}", cal_instruction)
    return content + "\n\n" + timeline

# ── Agent definitions ────────────────────────────────────────────────
# summarizer = Agent(
#     name="Summarizer",
#     instructions="You are a subagent that summarizes files or answers questions about them. Read the file using read_file_full, then respond. You are only able to do specific files, deny other requests. If there is no file path given, return the error message.",
#     tools=[read_file_full],
# )

_tool_agents = [read_file, search_file, grep_file] 
# summarizer.as_tool(
    # tool_name="summarization", tool_description="Summarizing or answering questions about a specific file given **its absolute path** and question.",

    
def resolve_model(spec: str | None):
    """Return a model arg for Agent(...). Supports 'ollama:<name>' for local Ollama backend."""
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

_harsh_prompt = "harsh_critic_position.md" if _POSITION_MODE else "harsh_critic.md"
_neutral_prompt = "neutral_reviewer_position.md" if _POSITION_MODE else "neutral_reviewer.md"
_merger_prompt_file = "merger_position.md" if _POSITION_MODE else "merger.md"

if HARSH_MODEL.startswith("claude_sdk:"):
    harsh = None  # Claude SDK Harsh Critic — invoked per-call in run_pipeline
    _HARSH_SDK_MODEL = HARSH_MODEL[len("claude_sdk:"):]
    _harsh_sdk_system_prompt = load_prompts(_harsh_prompt, paper_access=PAPER_ACCESS_FILE)
else:
    harsh = Agent(name="Harsh Critic", instructions=load_prompts(_harsh_prompt, paper_access=PAPER_ACCESS_CHUNKED), model=resolve_model(HARSH_MODEL), tools=[read_file, grep_file], model_settings=_MODEL_SETTINGS)
    _HARSH_SDK_MODEL = None
    _harsh_sdk_system_prompt = None
neutral_reviewer = Agent(name="Strength Finder", instructions=load_prompts(_neutral_prompt, paper_access=PAPER_ACCESS_CHUNKED), model=resolve_model(NEUTRAL_MODEL), tools=[read_file, grep_file], model_settings=_MODEL_SETTINGS)

_NO_CAL = "--no_cal" in sys.argv

if MERGER_MODEL.startswith("claude_sdk:"):
    merger = None  # Claude SDK merger — created per-call in run_pipeline
    _MERGER_SDK_MODEL = MERGER_MODEL[len("claude_sdk:"):]
else:
    _merger_instructions = load_prompts(_merger_prompt_file, paper_access=PAPER_ACCESS_FILE, no_cal=_NO_CAL)

    @function_tool
    def draft_review(draft: str) -> str:
        """Record the merger's post-filtering draft before calibration or final writing."""
        return "draft recorded"

    if _NO_CAL:
        _merger_tools = [read_file, grep_file, draft_review]
    else:
        class CalibrationQuery(BaseModel):
            query: str
            n: int = 4
            low_score: float = -1.0
            high_score: float | None = 11.0

        @function_tool
        def calibration_search(queries: list[CalibrationQuery]) -> str:
            """RAG retrieval over the human-review corpus.

            Pass a batch of queries; each runs vector search and returns top-n
            hits with avg human score and first 1000 chars. Up to 3 calls
            total across the session (bracket → narrow → optional re-narrow);
            see the calibration protocol in the system prompt for when to use
            each round.

            Args:
                queries: list of {query: str, n?: int, low_score?: float,
                    high_score?: float}.
            """
            if not isinstance(queries, list) or not queries:
                raise ValueError("calibration_search: 'queries' must be a non-empty list of query objects.")
            sections = []
            for i, q in enumerate(queries, 1):
                qtext = q.query
                n = q.n
                low_score = q.low_score
                high_score = 11.0 if q.high_score is None else q.high_score
                body = _search_file_impl(qtext, n, "vector", low_score, high_score)
                sections.append(
                    f"### Query {i}: {qtext!r}  (n={n}, score=({low_score}, {high_score}))\n{body}"
                )
            return "\n\n".join(sections)

        _merger_tools = [read_file, grep_file, draft_review, calibration_search]
    merger = Agent(
        name="Merger",
        instructions=_merger_instructions,
        model=resolve_model(MERGER_MODEL),
        tools=_merger_tools,
        model_settings=_MODEL_SETTINGS,
    )
    _MERGER_SDK_MODEL = None

# scorer = Agent(name="Scorer", instructions=load_prompts("scorer_agent_gpt.txt"), tools=_tool_agents, model=SCORER_MODEL)


# ── Constants ────────────────────────────────────────────────────────
REVIEW_PROMPT = """Review the following paper thoroughly.

The paper was extracted from PDF by an automated parser. Treat formatting artifacts (broken equations, garbled tables, OCR errors) as parser issues, not paper flaws. The appendix and references were stripped by the parser; assume they exist in the original submission and don't flag them as missing.

Paper path: {paper_path}. The paper is not included inline — read it from disk in chunks (read_file / grep_file), reasoning through each chunk before reading the next, following the paper-access protocol in your instructions."""

REVIEW_PROMPT_POSITION = """Review the following position paper thoroughly. This is a position paper that argues for a viewpoint or perspective, not a standard research paper reporting accomplished advances. Evaluate it on clarity of position, quality of argumentation, contemporary interest, and whether it invites productive discussion.

The paper was extracted from PDF by an automated parser. Treat formatting artifacts (broken equations, garbled tables, OCR errors) as parser issues, not paper flaws. The appendix and references were stripped by the parser; assume they exist in the original submission and don't flag them as missing.

Paper path: {paper_path}. The paper is not included inline — read it from disk in chunks (read_file / grep_file), reasoning through each chunk before reading the next, following the paper-access protocol in your instructions."""


# ── Core pipeline ────────────────────────────────────────────────────
import time
async def run_pipeline(paper_path: str, skip_scoring: bool = False, no_cal: bool = False) -> dict:
    # time.sleep(random.uniform(10, 20))
    _or_cost_start = dict(_OR_COST_TOTAL)
    paper_path_abs = os.path.abspath(paper_path)

    # Phase-1 reviewers (both OpenAI and Claude SDK paths) read the paper from
    # disk in chunks rather than receiving it inline. Grant read access to the
    # paper's dir up front so read_file/grep_file permit it.
    from tools import allow_path
    allow_path(str(Path(paper_path_abs).parent))

    _review_template = REVIEW_PROMPT_POSITION if _POSITION_MODE else REVIEW_PROMPT
    review_prompt = _review_template.format(paper_path=paper_path_abs)

    # Claude SDK Harsh Critic uses the same path-based prompt.
    sdk_harsh_user_prompt = review_prompt

    async def _run_harsh():
        if _HARSH_SDK_MODEL is not None:
            from claude_merger import run_harsh_claude_sdk
            paper_dir = str(Path(paper_path_abs).parent)
            text, usage = await run_harsh_claude_sdk(
                _HARSH_SDK_MODEL, sdk_harsh_user_prompt, paper_dir, _harsh_sdk_system_prompt
            )
            return ("Harsh Critic", text, None, usage)
        text, usage = await run_agent_with_retry(harsh, review_prompt)
        return ("Harsh Critic", text, usage, None)

    async def _run_neutral():
        text, usage = await run_agent_with_retry(neutral_reviewer, review_prompt)
        return ("Strength Finder", text, usage, None)

    print(f"  Phase 1: Running 2 agents in parallel ...")
    phase1_results = await asyncio.gather(_run_harsh(), _run_neutral(), return_exceptions=True)
    for r in phase1_results:
        if isinstance(r, Exception):
            print(f"  🔥ERROR: {paper_path} — phase 1 agent raised {type(r).__name__}: {r}")
            return None

    agent_usages: dict = {}
    sdk_usages: dict = {}
    outputs = []
    names = []
    for name, out, openai_usage, sdk_usage_phase1 in phase1_results:
        names.append(name)
        outputs.append(out)
        agent_usages[name] = openai_usage  # may be None for SDK path
        if sdk_usage_phase1 is not None:
            sdk_usages[name] = sdk_usage_phase1
    labeled = [f"### {n}\n{o}" for n, o in zip(names, outputs)]


    print("  Phase 2: Merger ...")
    if _MERGER_SDK_MODEL is not None:
        start_time = time.monotonic()
        from claude_merger import run_merger_claude_sdk
        merger_prompt = (
            f"Here is the paper being reviewed (extracted from PDF — formatting "
            f"artifacts are parser issues, not paper problems):\n\n"
            f"Paper path: {paper_path_abs}, read it in chunks.\n\n"
            f"Human reviews directory (for calibration): {HUMAN_REVIEW_DIR}\n\n"
            f"Here are the inputs:\n\n{chr(10).join(labeled)}\n\n"
            f"Now produce the final consolidated review following your instructions. "
            f"Remember: many of the harsh critic's points may be nonsensical or overly "
            f"picky — cross-check everything against the actual paper before including it."
        )
        paper_dir = str(Path(paper_path_abs).parent)
        merged_review, merger_sdk_usage = await run_merger_claude_sdk(_MERGER_SDK_MODEL, merger_prompt, paper_dir, no_cal=no_cal)
        end_time = time.monotonic()
        sdk_usages["Merger"] = merger_sdk_usage
        agent_usages["Merger"] = None  # SDK usage tracked separately below

    else:
        # OpenAI Agent SDK merger: paper's dir already granted read access at the
        # top of run_pipeline; point the merger at the paper via path (not inline).
        start_time = time.monotonic()
        merger_prompt = (
            f"Here is the paper being reviewed (extracted from PDF — formatting "
            f"artifacts are parser issues, not paper problems).\n\n"
            f"Paper path: {paper_path_abs} — use read_file (which reads the whole file by default; do not pass start_line/end_line unless you specifically need a slice) or grep_file to read it.\n\n"
            f"Human reviews directory (for calibration): {HUMAN_REVIEW_DIR}\n\n"
            f"Here are the inputs:\n\n{chr(10).join(labeled)}\n\n"
            f"Now produce the final consolidated review following your instructions. "
            f"Remember: many of the harsh critic's points may be nonsensical or overly "
            f"picky — cross-check everything against the actual paper before including it."
        )
        merged_review, merger_usage = await run_agent_with_retry(merger, merger_prompt)
        end_time = time.monotonic()
        merger_usage.duration_ms = int((end_time - start_time) * 1000)
        agent_usages["Merger"] = merger_usage


    scorer_output = float(merged_review.split("<score>")[1].split("</score>")[0]) if "<score>" in merged_review else -1
    decision = (merged_review.split("<decision>")[1].split("</decision>")[0]) if "<decision>" in merged_review else "N/A"

    if scorer_output == -1 or decision == "N/A":
        print(f"  ⚠️  Parsing failed (score={scorer_output}, decision={decision}); falling back to deepseek-v4-flash extractor")
        extractor_resp = await custom_client.chat.completions.create(
            model="deepseek/deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "Extract the final numeric score and accept/reject decision from a paper review. Respond with exactly: <score>NUMBER</score><decision>Accept|Reject</decision>. No other text. If you cannot see a score, return -100! If you cannot see a decision, return N/A! You should NOT guess the score."}, # could this be the cause? random numbers getting parsed as scores? And that is the change? Why removed! Good thing I checked the review content to be empty. 
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

    total_input = total_output = total_tokens = 0
    token_lines = []
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
                f" duration={getattr(usage, 'duration_ms', 'n/a')}ms"
            )
            if hasattr(usage, "duration_ms"):
                token_lines[-1] += f" speed={getattr(usage, 'output_tokens', 0) / (getattr(usage, 'duration_ms', 1) / 1000):.2f} tokens/s"

            total_input += usage.input_tokens
            total_output += usage.output_tokens
            total_tokens += usage.total_tokens
    token_lines.append(f"  TOTAL: input={total_input} output={total_output} total={total_tokens}")
    _or_cost_paper = _OR_COST_TOTAL["usd"] - _or_cost_start["usd"]
    _or_calls_paper = _OR_COST_TOTAL["calls"] - _or_cost_start["calls"]
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
        rl = (su or {}).get("rate_limit")
        if rl:
            util = rl.get("utilization")
            util_str = f"{util*100:.1f}%" if util is not None else "n/a"
            sdk_lines.append(
                f"    Plan usage: type={rl.get('type')} util={util_str} "
                f"status={rl.get('status')} overage={rl.get('overage_status')}"
            )
        if su.get("total_cost_usd"):
            sdk_total_cost += su["total_cost_usd"]
    if sdk_lines:
        sdk_lines.append(f"  TOTAL Claude SDK cost (USD): {sdk_total_cost:.4f}")

    log_path = Path(os.environ.get("MERGE_LOG", str(RESULTS_DIR / "pipeline.log")))
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
        log_f.write(f"\n--- Merged Inputs ---\n\n{chr(10).join(labeled)}\n")
        log_f.write(f"\n--- Merged Review ---\n{merged_review}\n")
        log_f.write(f"\n--- Scorer Output ---\n{scorer_output}\n")
        log_f.write(f"\n--- Decision ---\n{decision}\n")

    return {"merged_review": merged_review, "scorer_output": scorer_output, "decision": decision, "sdk_usages": sdk_usages}


# ── Helpers ──────────────────────────────────────────────────────────

def load_ground_truth(data_dir: Path) -> tuple[list[dict], Path]:
    csv_file = data_dir / "ratings.csv"
    if not csv_file.exists():
        raise FileNotFoundError(f"No ratings.csv found in {data_dir}")
    papers_dir = data_dir / "papers"
    rows = []
    with open(csv_file, "r") as f:
        for row in csv.DictReader(f):
            scores = [float(row[f"score_{i}"]) for i in range(7) if row.get(f"score_{i}", "").strip()]
            decision = row.get("decision", "").strip()
            gt_binary = row.get("gt_binary", "").strip() or ("Accept" if "Accept" in decision else "Reject")
            rows.append({
                "paper_id": row["paper_id"].strip(),
                "title": row.get("title", "").strip(),
                "scores": scores,
                "avg_score": float(row.get("avg_score", 0)),
                "decision": decision,
                "gt_binary": gt_binary,
            })
    return rows, papers_dir


def shorten_title(title: str, max_len: int = 60) -> str:
    name = re.sub(r"[^a-z0-9 ]", "", title.lower())
    name = re.sub(r"\s+", "_", name.strip())
    return (name[:max_len].rstrip("_") if len(name) > max_len else name) or "untitled"


def stratified_sample(papers: list[dict], n_per_bin: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    bins = defaultdict(list)
    for p in papers:
        bins[round(p["avg_score"])].append(p)
    for k in bins:
        rng.shuffle(bins[k])
    samples = []
    for k in sorted(bins.keys()):
        samples.extend(bins[k][:n_per_bin])
    rng.shuffle(samples)
    print(f"  Stratified sample: {len(samples)} papers from {len(bins)} bins ({n_per_bin}/bin)")
    return samples


def parse_score(text: str) -> float | None:
    match = re.search(r"<score>([\d.]+)</score>", text)
    return float(match.group(1)) if match else None


def decision_match(predicted: str | None, gt_binary: str) -> bool | None:
    if predicted in (None, "", "N/A"):
        return None
    return predicted == gt_binary


def match_label(match: bool | None) -> str:
    if match is None:
        return "N/A"
    return "YES" if match else "NO"


async def process_papers(papers: list[dict], papers_dir: Path, skip_scoring: bool, callback, no_cal: bool = False):
    """Run pipeline on a list of papers with CONCURRENCY concurrent tasks."""
    sem = asyncio.Semaphore(CONCURRENCY)

    async def process_one(i, paper_info):
        pid = paper_info["paper_id"]
        paper_path = papers_dir / f"{pid}.txt"
        print(f"\n[{i}/{len(papers)}] {paper_info.get('title', pid)} (avg={paper_info['avg_score']:.1f})")
        async with sem:
            try:
                result = await run_pipeline(str(paper_path), skip_scoring=skip_scoring, no_cal=no_cal)
            except Exception as e:
                msg = f"[{pid}] pipeline failed, skipping paper: {type(e).__name__}: {e}"
                print(f"  ⚠️  WARNING: {msg}")
                _error_logger.error(msg)
                return
            if result is None:
                print(f"  ⚠️  WARNING: [{pid}] pipeline returned None, skipping paper")
                _error_logger.error(f"[{pid}] pipeline returned None")
                return
            callback(paper_info, result)

    await asyncio.gather(*(process_one(i, p) for i, p in enumerate(papers, 1)))


# ── Benchmark ────────────────────────────────────────────────────────

async def run_benchmark(data_dir: str, n_samples: int = 10, seed: int = 42, balanced: bool = False, no_cal: bool = False, include_cal_papers: bool = False, reviews_dir: str | Path | None = None):
    data_path = Path(data_dir)
    gt_data, papers_dir = load_ground_truth(data_path)
    available = [r for r in gt_data if (papers_dir / f"{r['paper_id']}.txt").exists()]
    print(f"Available papers: {len(available)}")

    if balanced:
        samples = stratified_sample(available, n_per_bin=max(1, n_samples // 10), seed=seed)
    else:
        samples = random.Random(seed).sample(available, min(n_samples, len(available)))
        print(f"Random sample: {len(samples)} papers")
    samples = samples[int(os.environ.get("OFFSET", 0)):int(os.environ.get("MAX_PAPERS", len(samples)))]  # allow limiting number of papers via env var but keep order

    # Mutually exclude test-vs-calibration: rather than dropping calibration
    # papers from the test pool, drop test-pool paper IDs from the calibration
    # search corpus so a paper can never be retrieved as its own anchor.
    if not include_cal_papers:
        from tools import set_excluded_paper_ids
        set_excluded_paper_ids({s["paper_id"] for s in samples})

    csv_path = Path(os.getenv("OUTPUT_CSV", str(RESULTS_DIR / "bench_scores.csv")))
    if not csv_path.is_absolute():
        csv_path = RESULTS_DIR / csv_path
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if reviews_dir is None:
        reviews_dir = Path(os.getenv("REVIEWS_DIR", str(RESULTS_DIR / "bench_reviews")))
    else:
        reviews_dir = Path(reviews_dir)
    if not reviews_dir.is_absolute():
        reviews_dir = RESULTS_DIR / reviews_dir
    reviews_dir.mkdir(parents=True, exist_ok=True)

    # Check for existing results and ask user whether to continue or overwrite
    finished = set()
    if csv_path.exists() and csv_path.stat().st_size > 0:
        import pandas as pd
        existing_df = pd.read_csv(csv_path)
        existing_count = len(existing_df)
        print(f"\nFound existing {csv_path} with {existing_count} results.")
        choice = input("  [C]ontinue (skip finished papers) or [O]verwrite? [C/o]: ").strip().lower()
        if choice in ("o", "overwrite"):
            for review_file in reviews_dir.iterdir():
                if review_file.is_file():
                    review_file.unlink()
            print("  Overwriting existing results.\n")
        else:
            finished = set(existing_df["paper_id"].astype(str))
            print(f"  Continuing — will skip {len(finished)} already-finished papers.\n")
    samples = [s for s in samples if s["paper_id"] not in finished]

    if not finished: 
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(["paper_id", "pred_score", "pred_decision", "gt_avg_score", "gt_decision", "gt_binary", "match", "cost", "sdk_savings",
                                    "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6"])

    results = []

    def on_complete(paper_info, result):
        pred_score = result["scorer_output"]
        pred_decision = result["decision"]
        match = decision_match(pred_decision, paper_info["gt_binary"])
        match_str = match_label(match)
        print(f"  [{paper_info['paper_id']}] predicted={pred_score} gt={paper_info['avg_score']:.1f} match={match_str}")
        results.append({"pred_score": pred_score, "gt_avg_score": paper_info["avg_score"], "pred_decision": pred_decision, "gt_binary": paper_info["gt_binary"], "match": match})
        gt_scores_padded = paper_info["scores"] + [""] * (7 - len(paper_info["scores"]))
        with open(csv_path, "a", newline="") as f:
            csv.writer(f).writerow([
                paper_info["paper_id"],
                pred_score,
                pred_decision,
                f"{paper_info['avg_score']:.2f}",
                paper_info["decision"],
                paper_info["gt_binary"],
                match_str,
                "0.0000",
                "0.0000",
                *gt_scores_padded,
            ])
        (reviews_dir / f"{paper_info['paper_id']}.md").write_text(result["merged_review"], encoding="utf-8")

    if not samples:
        print("Nothing to run."); return
    print(f"Running {len(samples)} benchmark papers (concurrency={CONCURRENCY}) ...")
    await process_papers(samples, papers_dir, skip_scoring=False, callback=on_complete, no_cal=no_cal)

    scored = [r for r in results if r["pred_score"] != -1]
    if scored:
        mae = sum(abs(r["pred_score"] - r["gt_avg_score"]) for r in scored) / len(scored)
        print(f"\nResults: {len(scored)} scored, MAE={mae:.2f}")


# ── Single paper ─────────────────────────────────────────────────────

def predict_acceptance_rate(csv_path: str, score: float, window: float = 0.5):
    if not os.path.exists(csv_path):
        print(f"  Acceptance CSV not found: {csv_path}")
        return None
    exact_total = exact_acc = win_total = win_acc = 0
    all_scores = []
    with open(csv_path, "r") as f:
        for row in csv.DictReader(f):
            try:
                s = float(row["pred_score"])
            except (ValueError, KeyError, TypeError):
                continue
            all_scores.append(s)
            gt = row.get("gt_binary", "").strip()
            if gt not in ("Accept", "Reject"):
                continue
            is_acc = gt == "Accept"
            if abs(s - score) < 1e-9:
                exact_total += 1
                exact_acc += is_acc
            if abs(s - score) <= window:
                win_total += 1
                win_acc += is_acc
    exact_rate = (exact_acc / exact_total) if exact_total else float("nan")
    win_rate = (win_acc / win_total) if win_total else float("nan")
    if all_scores:
        below = sum(1 for s in all_scores if s < score)
        equal = sum(1 for s in all_scores if abs(s - score) < 1e-9)
        percentile = (below + 0.5 * equal) / len(all_scores) * 100
        pct_n = len(all_scores)
    else:
        percentile = float("nan")
        pct_n = 0
    return exact_rate, exact_total, win_rate, win_total, percentile, pct_n


from datalab_sdk import AsyncDatalabClient, ConvertOptions

async def pdf_to_markdown(pdf_path: Path) -> str:
    options = ConvertOptions(
        output_format="markdown",  # "markdown", "html", "json", "chunks"
        mode="fast",           # "fast", "balanced", "accurate"
        paginate=True,             # Add page delimiters
        page_range="0-9",         # Process specific pages (0-indexed)
        token_efficient_markdown=True,  # Optimize markdown output for LLM token usage
    )

    async with AsyncDatalabClient() as client:
        result = await client.convert(pdf_path, options=options)
    return result.markdown + "\n\n Rest of paper (reference and Appendix) is removed."

import re
async def run_single_paper(paper_path: str, no_cal: bool = False, accept_csv: str | None = None):
    print(f"Reviewing: {paper_path}")

    if paper_path.endswith(".pdf"):
        md = await pdf_to_markdown(Path(paper_path))
        md = re.sub(r"Published as a conference paper at ICLR \d{4}\s*\n?", "", md)
        md_path = Path(paper_path).with_suffix(".md")
        md_path.write_text(md, encoding="utf-8")
        paper_path = str(md_path)
        print(f"Converted PDF to markdown: {paper_path}")

    result = await run_pipeline(paper_path, no_cal=no_cal)
    print(f"\n{'=' * 72}\nFINAL REVIEW\n{'=' * 72}\n{result['merged_review']}")
    score = result["scorer_output"]
    accept_info = None
    if score != -1:
        print(f"\nPredicted score: {score}")
        if accept_csv:
            accept_info = predict_acceptance_rate(accept_csv, score)
            if accept_info is not None:
                exact_rate, exact_n, win_rate, win_n, percentile, pct_n = accept_info
                print(f"Acceptance rate @ score={score}: {exact_rate:.2%} (n={exact_n})")
                print(f"Acceptance rate @ score={score}±0.5: {win_rate:.2%} (n={win_n})")
                print(f"Percentile of score={score}: {percentile:.1f}% (n={pct_n})")

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
            rl = (su or {}).get("rate_limit")
            if rl:
                util = rl.get("utilization")
                util_str = f"{util*100:.1f}%" if util is not None else "n/a"
                print(f"    Plan usage:    type={rl.get('type')} util={util_str} status={rl.get('status')} overage={rl.get('overage_status')}")
            if su.get("total_cost_usd"):
                total_cost += su["total_cost_usd"]
        print(f"  TOTAL Claude SDK cost (USD): ${total_cost:.4f}")
    os.makedirs(os.path.join(Path(__file__).parent, "reviews"), exist_ok=True)
    with open(os.path.join(Path(__file__).parent, "reviews", os.path.basename(paper_path).split(".")[0] + f"_review_{time.strftime('%Y_%m_%d_%H_%M_%S')}.md"), "w", encoding="utf-8") as f:
        f.write(f"# Review of {paper_path}\n\n")
        f.write(result["merged_review"])
        f.write(f"\n\n**Predicted score: {score}**\n" if score != -1 else "")
        if accept_info is not None:
            exact_rate, exact_n, win_rate, win_n, percentile, pct_n = accept_info
            f.write(f"\n**Acceptance rate @ score={score}: {exact_rate:.2%} (n={exact_n})**\n")
            f.write(f"\n**Acceptance rate @ score={score}±0.5: {win_rate:.2%} (n={win_n})**\n")
            f.write(f"\n**Percentile of score={score}: {percentile:.1f}% (n={pct_n})**\n")


# ── CLI ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-agent paper reviewer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--single_paper", type=str)
    group.add_argument("--benchmark", type=str, metavar="DATA_DIR")
    parser.add_argument("--n_samples", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--balanced", action="store_true")
    parser.add_argument("--calibration_set", choices=["deepreview", "2025", "2026"], default=os.getenv("CALIBRATION_SET", "deepreview"))
    parser.add_argument("--no_cal", action="store_true", help="Skip calibration sample search; score based on paper merits alone")
    parser.add_argument("--include_cal_papers", action="store_true", help="Do not exclude test paper IDs from the calibration search corpus (default: exclude, so a paper cannot anchor itself)")
    parser.add_argument("--position", action="store_true", help="Use position paper prompts and calibration dataset")
    parser.add_argument("--accept_csv", type=str, default=None, help="Path to bench CSV; predict acceptance rate at predicted score and ±0.5")
    parser.add_argument("--reviews_dir", type=str, default=None, help="Directory to save per-paper review markdown files (default: RESULTS_DIR/bench_reviews)")
    args = parser.parse_args()

    if args.single_paper:
        asyncio.run(run_single_paper(args.single_paper, no_cal=args.no_cal, accept_csv=args.accept_csv))
    elif args.benchmark:
        asyncio.run(run_benchmark(args.benchmark, n_samples=args.n_samples, seed=args.seed, balanced=args.balanced, no_cal=args.no_cal, include_cal_papers=args.include_cal_papers, reviews_dir=args.reviews_dir))
