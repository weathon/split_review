import argparse
import asyncio
import csv
import json
import os
import re
import time
from pathlib import Path

import dotenv
dotenv.load_dotenv()

import numpy as np
from scipy.optimize import minimize_scalar

from paths import prompt_path, RESULTS_DIR
from tools import (
    read_file,
    grep_file,
    allow_path,
    CALIBRATION_REVIEW_DIR,
    _score_index,
    _search_file_impl,
)

import weave
weave.init("pairwise-score-agents")

from pydantic import BaseModel
from agents import Agent, OpenAIChatCompletionsModel, OpenAIResponsesModel, Runner, function_tool
from agents.model_settings import ModelSettings
from openai import AsyncOpenAI
from agents import set_default_openai_client, set_tracing_export_api_key

RESCORE_MODEL = os.environ.get("RESCORE_MODEL", "claude_sdk:claude-sonnet-4-6")
PAIRWISE_MODEL = os.environ.get("PAIRWISE_MODEL", "claude_sdk:claude-sonnet-4-6")
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1/")
FEATHERLESS_BASE_URL = os.environ.get("FEATHERLESS_BASE_URL", "https://api.featherless.ai/v1")

custom_client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

OR_COST_TOTAL = {"usd": 0.0, "calls": 0}


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
                OR_COST_TOTAL["usd"] += float(cost)
                OR_COST_TOTAL["calls"] += 1
        except Exception as e:
            print(f"  [openrouter] cost extraction failed: {e}")
        return resp

    client.chat.completions.create = create_with_usage


install_openrouter_cost_hook(custom_client)
set_default_openai_client(custom_client)
set_tracing_export_api_key(os.environ["OPENAI_API_KEY"])

CONCURRENCY = int(os.environ.get("CONCURRENCY", 5))
PAIRWISE_CONCURRENCY = int(os.environ.get("PAIRWISE_CONCURRENCY", 20))
MAX_RETRIES = 5
RETRY_DELAY = 10
MERGER_MODEL_SETTINGS = ModelSettings(extra_body={"effort": "xhigh"})


# ── Score bands ──────────────────────────────────────────────────────

BAND_EDGES = [(-1.0, 2.0), (2.0, 4.0), (4.0, 6.0), (6.0, 8.0), (8.0, 11.0)]
ANCHORS_PER_BAND = int(os.environ.get("ANCHORS_PER_BAND", 40))
BT_BETA = float(os.environ.get("BT_BETA", 1.0))


# ── Custom calibration instruction for 5-band bracketing-only retrieval ─

CALIBRATION_INSTRUCTION_PAIRWISE = f"""Use `calibration_search` to bracket the paper against human-reviewed anchors across the full score range, then select the genuinely comparable anchors per band. The final score is computed externally via pairwise comparison against the anchors you SELECT — so the selected set must be topically comparable to the paper under review, not just papers that happen to fall in a score band.

## Retrieval (5 bracketing calls, one per band)

Make exactly 5 `calibration_search` calls — one per score band — each with `n={ANCHORS_PER_BAND}` and the score filter set for that band. Pick a query string per band that captures the paper's topic/method/contribution; you may use different queries per band if a different angle is more discriminating in that range.

Bands (use these exact bounds):
- Band 1 (weak): low_score=-1, high_score=2, n={ANCHORS_PER_BAND}
- Band 2: low_score=2, high_score=4, n={ANCHORS_PER_BAND}
- Band 3 (middle): low_score=4, high_score=6, n={ANCHORS_PER_BAND}
- Band 4: low_score=6, high_score=8, n={ANCHORS_PER_BAND}
- Band 5 (strong): low_score=8, high_score=11, n={ANCHORS_PER_BAND}

Before any `calibration_search` call, finish filtering inputs into a draft review and call `draft_review` exactly once with that draft.

## Selection (per band, up to 5)

For each band, inspect candidates using `read_file` (read snippets/full reviews as needed) and select UP TO 5 anchors per band that are genuinely topically comparable to the paper under review (same problem area, related method family, comparable claims surface, etc.). If fewer than 5 candidates in a band are actually comparable, return fewer — do not pad with topically-irrelevant papers just to hit 5. If zero are comparable in a band, return zero for that band.

Do NOT use the selected anchors to set your final review score — the final score is computed externally via pairwise comparison.

## Output

At the very end of your review (after the score line), include a section titled `# Selected Anchors` followed by a single line of the form:

<related>["paperidA", "paperidB", ...]</related>

containing only the anchors you SELECTED across all 5 bands (use the file basename without the `.md` extension). De-duplicate the list."""


# ── Agent setup ──────────────────────────────────────────────────────

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


PAPER_ACCESS_FILE = "The paper path is provided in the user message. Use read_file to read the paper (it reads the whole file by default — do not pass start_line/end_line unless you specifically need a slice) and verify reviewer claims directly."

with open(prompt_path("timeline.md"), "r") as f:
    timeline = f.read().replace("{{CURRENT_DATE}}", time.strftime("%Y-%m-%d"))


def load_merger_prompt_pairwise():
    with open(prompt_path("merger.md"), "r") as f:
        raw_lines = f.readlines()
    kept_lines = [line for line in raw_lines if not line.lstrip().startswith("&&")]
    content = "".join(kept_lines)
    content = content.replace("{{PAPER_ACCESS_INSTRUCTION}}", PAPER_ACCESS_FILE)
    content = content.replace("{{CALIBRATION_INSTRUCTION}}", CALIBRATION_INSTRUCTION_PAIRWISE)
    return content + "\n\n" + timeline


class CalibrationQuery(BaseModel):
    query: str
    n: int = ANCHORS_PER_BAND
    low_score: float = -1.0
    high_score: float | None = 11.0


@function_tool
def calibration_search(queries: list[CalibrationQuery]) -> str:
    """5-band bracketing retrieval. Pass a batch of queries with score filters.

    Args:
        queries: list of {query: str, n?: int, low_score?: float, high_score?: float}.
    """
    if not isinstance(queries, list) or not queries:
        raise ValueError("calibration_search: 'queries' must be a non-empty list of query objects.")
    sections = []
    for i, q in enumerate(queries, 1):
        body = _search_file_impl(q.query, q.n, "vector", q.low_score, 11.0 if q.high_score is None else q.high_score)
        sections.append(f"### Query {i}: {q.query!r}  (n={q.n}, score=({q.low_score}, {q.high_score}))\n{body}")
    return "\n\n".join(sections)


@function_tool
def draft_review(draft: str) -> str:
    """Record the merger's post-filtering draft before calibration."""
    return "draft recorded"


if RESCORE_MODEL.startswith("claude_sdk:"):
    merger_agent = None
    SDK_MERGER_MODEL = RESCORE_MODEL[len("claude_sdk:"):]
else:
    SDK_MERGER_MODEL = None
    merger_agent = Agent(
        name="Merger",
        instructions=load_merger_prompt_pairwise(),
        model=resolve_model(RESCORE_MODEL),
        tools=[read_file, grep_file, calibration_search, draft_review],
        model_settings=MERGER_MODEL_SETTINGS,
    )


# ── Pairwise judge ───────────────────────────────────────────────────

PAIRWISE_PROMPT = """You will be given two reviews for two different papers. Decide which paper is better based on the reviews. You MUST pick one — ties are NOT allowed.

Return -1 if the FIRST paper is better, or 1 if the SECOND paper is better.

Note that you are not comparing the reviews, you are comparing the papers based on the reviews. The review tone may not reflect the actual quality of the paper, so read carefully and understand the content of the reviews.

At the very end of your response, output exactly one line of the form:
<result>-1</result>
or
<result>1</result>

Nothing else after that tag."""


if PAIRWISE_MODEL.startswith("claude_sdk:"):
    pairwise_agent = None
    SDK_PAIRWISE_MODEL = PAIRWISE_MODEL[len("claude_sdk:"):]
else:
    SDK_PAIRWISE_MODEL = None
    pairwise_agent = Agent(
        name="PairwiseJudge",
        instructions=PAIRWISE_PROMPT,
        model=resolve_model(PAIRWISE_MODEL),
        tools=[],
        model_settings=ModelSettings(),
    )


async def run_agent_with_retry(agent, prompt: str, max_turns: int = 30) -> tuple[str, object]:
    agent_name = agent.name
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            result = await Runner.run(agent, prompt, max_turns=max_turns)
            output = result.final_output
            if not output or not output.strip():
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_DELAY + attempt * 5)
                    continue
                raise RuntimeError(f"[{agent_name}] empty response after {MAX_RETRIES} attempts")
            return output, result.context_wrapper.usage
        except Exception as e:
            if attempt < MAX_RETRIES:
                wait = RETRY_DELAY * attempt
                print(f"  [{agent_name}] error (attempt {attempt}/{MAX_RETRIES}), waiting {wait}s ... {e}")
                await asyncio.sleep(wait)
            else:
                raise RuntimeError(f"[{agent_name}] {e}") from e
    raise RuntimeError(f"[{agent_name}] failed after {MAX_RETRIES} attempts")


# ── Merger via Claude SDK with custom cal instruction ────────────────

async def run_merger_pairwise_claude_sdk(paper_path_abs: str, cached_inputs: str, paper_dir: str) -> tuple[str, dict]:
    from claude_merger import _make_merger_mcp_server, _run_claude_sdk_query

    system_prompt = load_merger_prompt_pairwise()
    mcp_server = _make_merger_mcp_server(paper_dir, no_cal=False)

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
        label="Merger",
        model_id=SDK_MERGER_MODEL,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        allowed_tools=[
            "mcp__merger_fs__read_file",
            "mcp__merger_fs__grep_file",
            "mcp__merger_fs__draft_review",
            "mcp__merger_fs__calibration_search",
        ],
        mcp_servers={"merger_fs": mcp_server},
        max_turns=30,
    )


# ── Pairwise via Claude SDK ───────────────────────────────────────────

async def run_pairwise_claude_sdk(review_1: str, review_2: str) -> tuple[str, dict]:
    from claude_merger import _run_claude_sdk_query

    user_prompt = f"Review 1:\n{review_1}\n\nReview 2:\n{review_2}"
    return await _run_claude_sdk_query(
        label="PairwiseJudge",
        model_id=SDK_PAIRWISE_MODEL,
        system_prompt=PAIRWISE_PROMPT,
        user_prompt=user_prompt,
        allowed_tools=[],
        mcp_servers={},
        max_turns=2,
    )


async def pairwise_compare(review_under_test: str, anchor_review: str) -> int:
    """Returns -1 if anchor better, +1 if under-test better. No ties."""
    user_prompt = f"Review 1:\n{anchor_review}\n\nReview 2:\n{review_under_test}"
    if SDK_PAIRWISE_MODEL is not None:
        text, _ = await run_pairwise_claude_sdk(anchor_review, review_under_test)
    else:
        text, _ = await run_agent_with_retry(pairwise_agent, user_prompt, max_turns=2)

    m = re.search(r"<result>\s*(-?1)\s*</result>", text)
    if not m:
        raise RuntimeError(f"pairwise judge missing <result>: {text[:200]}")
    val = int(m.group(1))
    if val not in (-1, 1):
        raise RuntimeError(f"pairwise judge returned invalid value {val}")
    # Map: from judge's POV review_1 = anchor, review_2 = under-test.
    # judge returns -1 if review_1 (anchor) is better, +1 if review_2 (under-test) is better.
    # We want: +1 if paper-under-test wins, -1 if anchor wins.
    return val


# ── Score & decision parsing ──────────────────────────────────────────

RELATED_RE = re.compile(r"<related>\s*(\[.*?\])\s*</related>", re.DOTALL)


def parse_related(text: str) -> list[str]:
    m = RELATED_RE.search(text)
    if not m:
        return []
    ids = json.loads(m.group(1))
    return [str(x).removesuffix(".md") for x in ids if isinstance(x, str)]


class RelatedList(BaseModel):
    related: list[str]


async def extract_related_deepseek(merged_review: str) -> list[str]:
    resp = await custom_client.chat.completions.parse(
        model="deepseek/deepseek-v4-flash",
        messages=[
            {"role": "system", "content": "Extract every retrieved/anchor paper ID mentioned in this review (look for a Related Reviews / Retrieved Anchors section, or paths like /.../paperid.md). Return a JSON object with field 'related' as a list of paper IDs (no .md extension)."},
            {"role": "user", "content": merged_review},
        ],
        response_format=RelatedList,
        extra_body={"reasoning": {"enabled": False}},
    )
    return [str(x).removesuffix(".md") for x in resp.choices[0].message.parsed.related]


def remove_scores_and_ratings(text: str) -> str:
    text = re.sub(r"(?m)^- (?:Avg Score|Scores):.*\n", "", text)
    text = re.sub(r"(?m)^- Decision:.*\n", "", text)
    rating_sections = ("Rating", "Rating Number", "Confidence", "Soundness", "Presentation", "Contribution")
    names = "|".join(re.escape(name) for name in rating_sections)
    text = re.sub(rf"(?ms)^### (?:{names})\n.*?(?=^### |^## |^---$|\Z)", "", text)
    return text


# ── Bradley-Terry fit ────────────────────────────────────────────────

def bradley_terry_fit(observations: list[tuple[float, int]]) -> float:
    """observations: list of (anchor_score, win) where win=1 if under-test won, 0 otherwise.
    Returns MLE of theta in [0, 10]."""
    if not observations:
        raise RuntimeError("BT: no observations")
    s_arr = np.array([s for s, _ in observations])
    w_arr = np.array([w for _, w in observations], dtype=float)

    def neg_ll(theta):
        z = BT_BETA * (theta - s_arr)
        # log(sigmoid(z)) and log(1 - sigmoid(z)) numerically stable
        log_p = -np.logaddexp(0.0, -z)
        log_1mp = -np.logaddexp(0.0, z)
        return -float(np.sum(w_arr * log_p + (1.0 - w_arr) * log_1mp))

    res = minimize_scalar(neg_ll, bounds=(0.0, 10.0), method="bounded", options={"xatol": 1e-3})
    return float(res.x)


# ── Log parsing ───────────────────────────────────────────────────────

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


# ── Ground truth ──────────────────────────────────────────────────────

def load_ground_truth(data_dir: str) -> dict[str, dict]:
    csv_file = Path(data_dir) / "ratings.csv"
    rows = {}
    with open(csv_file, "r") as f:
        for row in csv.DictReader(f):
            scores = [row[f"score_{i}"] for i in range(7) if row.get(f"score_{i}", "").strip()]
            decision = row.get("decision", "").strip()
            gt_binary = row.get("gt_binary", "").strip() or ("Accept" if "Accept" in decision else "Reject")
            rows[row["paper_id"].strip()] = {
                "scores": scores,
                "avg_score": float(row.get("avg_score", 0)),
                "decision": decision,
                "gt_binary": gt_binary,
            }
    return rows


# ── Per-paper pipeline ───────────────────────────────────────────────

async def run_paper(paper_id: str, paper_path: str, cached_inputs: str, reviews_dir: Path, log_path: Path) -> dict:
    paper_path_abs = os.path.abspath(paper_path)
    paper_dir = str(Path(paper_path_abs).parent)
    allow_path(paper_dir)

    user_prompt = (
        f"Here is the paper being reviewed (extracted from PDF — formatting "
        f"artifacts are parser issues, not paper problems).\n\n"
        f"Paper path: {paper_path_abs} — use read_file (which reads the whole file by default; "
        f"do not pass start_line/end_line unless you specifically need a slice) or grep_file to read it.\n\n"
        f"Here are the inputs:\n\n{cached_inputs}\n\n"
        f"Now produce the final consolidated review following your instructions."
    )

    if SDK_MERGER_MODEL is not None:
        merged_review, _ = await run_merger_pairwise_claude_sdk(paper_path_abs, cached_inputs, paper_dir)
    else:
        merged_review, _ = await run_agent_with_retry(merger_agent, user_prompt)

    anchor_ids = parse_related(merged_review)
    if not anchor_ids:
        print(f"  [{paper_id}] no <related> tag, extracting via deepseek")
        anchor_ids = await extract_related_deepseek(merged_review)
    anchor_ids = [a for a in dict.fromkeys(anchor_ids) if a != paper_id]

    review_under_test_stripped = remove_scores_and_ratings(
        merged_review.split("## Score and Decision")[0]
        if "## Score and Decision" in merged_review else merged_review
    )

    sem = asyncio.Semaphore(PAIRWISE_CONCURRENCY)
    observations: list[tuple[float, int]] = []
    pair_log: list[dict] = []

    async def one_pair(aid: str):
        anchor_path_md = os.path.join(CALIBRATION_REVIEW_DIR, f"{aid}.md")
        anchor_path_txt = os.path.join(CALIBRATION_REVIEW_DIR, f"{aid}.txt")
        if os.path.exists(anchor_path_md):
            anchor_file = anchor_path_md
            key_for_score = f"{aid}.md"
        elif os.path.exists(anchor_path_txt):
            anchor_file = anchor_path_txt
            key_for_score = f"{aid}.txt"
        else:
            print(f"  [{paper_id}] anchor {aid} not found, skipping")
            return
        if key_for_score not in _score_index:
            raise RuntimeError(f"anchor {aid} missing from _score_index")
        anchor_score = float(_score_index[key_for_score])
        with open(anchor_file, "r", errors="replace") as f:
            anchor_review = remove_scores_and_ratings(f.read())

        async with sem:
            try:
                result = await pairwise_compare(review_under_test_stripped, anchor_review)
            except Exception as e:
                print(f"  [{paper_id}] pairwise failed for anchor {aid}: {e}")
                return
        win = 1 if result == 1 else 0
        observations.append((anchor_score, win))
        pair_log.append({"anchor_id": aid, "anchor_score": anchor_score, "result": result})

    await asyncio.gather(*(one_pair(aid) for aid in anchor_ids))

    if not observations:
        raise RuntimeError(f"[{paper_id}] no successful pairwise observations")

    bt_score = bradley_terry_fit(observations)

    n_wins = sum(1 for _, w in observations if w == 1)
    n_losses = sum(1 for _, w in observations if w == 0)

    (reviews_dir / f"{paper_id}.md").write_text(merged_review, encoding="utf-8")

    with open(log_path, "a") as log_f:
        log_f.write(f"\n{'='*60}\n")
        log_f.write(f"Paper: {paper_path}\n")
        log_f.write(f"Timestamp: {time.strftime('%Y-%m-%dT%H:%M:%S')}\n")
        log_f.write(f"\n--- Cached Inputs ---\n\n{cached_inputs}\n")
        log_f.write(f"\n--- Merged Review ---\n{merged_review}\n")
        log_f.write(f"\n--- Anchor IDs ---\n{json.dumps(anchor_ids)}\n")
        log_f.write(f"\n--- Pairwise Results ---\n")
        for row in pair_log:
            log_f.write(f"  {row['anchor_id']} score={row['anchor_score']:.2f} result={row['result']}\n")
        log_f.write(f"\n--- BT Score ---\n{bt_score:.4f}\n")
        log_f.write(f"--- Counts ---\nwins={n_wins} losses={n_losses} n={len(observations)}\n")

    return {
        "merged_review": merged_review,
        "bt_score": bt_score,
        "n_anchors": len(observations),
        "n_wins": n_wins,
        "n_losses": n_losses,
    }


# ── Batch ─────────────────────────────────────────────────────────────

CSV_HEADER = ["paper_id", "pred_score", "pred_decision", "gt_avg_score", "gt_decision", "gt_binary",
              "match", "cost", "sdk_savings",
              "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6"]


async def run_batch(log_path: str, data_dir: str, papers_dir: str | None = None):
    entries = parse_pipeline_log(log_path)
    print(f"Parsed {len(entries)} papers from {log_path}")
    gt = load_ground_truth(data_dir)

    if papers_dir:
        for entry in entries:
            entry["paper_path"] = str(Path(papers_dir) / Path(entry["paper_path"]).name)

    csv_path = Path(os.getenv("OUTPUT_CSV", str(RESULTS_DIR / "pairwise_scores.csv")))
    if not csv_path.is_absolute():
        csv_path = RESULTS_DIR / csv_path
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    reviews_dir = Path(os.getenv("REVIEWS_DIR", str(RESULTS_DIR / "pairwise_reviews")))
    if not reviews_dir.is_absolute():
        reviews_dir = RESULTS_DIR / reviews_dir
    reviews_dir.mkdir(parents=True, exist_ok=True)

    pair_log_path = Path(os.environ.get("PAIRWISE_LOG", str(RESULTS_DIR / "pairwise_pipeline.log")))
    if not pair_log_path.is_absolute():
        pair_log_path = RESULTS_DIR / pair_log_path
    pair_log_path.parent.mkdir(parents=True, exist_ok=True)

    finished = set()
    if csv_path.exists() and csv_path.stat().st_size > 0:
        import pandas as pd
        existing = pd.read_csv(csv_path)
        finished = set(existing["paper_id"].astype(str))
        print(f"Skipping {len(finished)} already-finished papers")

    entries = [e for e in entries if e["paper_id"] not in finished]
    if not entries:
        print("Nothing to run.")
        return

    if not finished:
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(CSV_HEADER)

    print(f"Running {len(entries)} papers (concurrency={CONCURRENCY}, pairwise_concurrency={PAIRWISE_CONCURRENCY}) ...")
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
                result = await run_paper(paper_id, paper_path, entry["cached_inputs"], reviews_dir, pair_log_path)
            except Exception as e:
                print(f"  [{paper_id}] pipeline failed: {type(e).__name__}: {e}")
                return

        gt_row = gt[paper_id] if paper_id in gt else None
        gt_avg = f"{gt_row['avg_score']:.2f}" if gt_row else ""
        gt_decision = gt_row["decision"] if gt_row else ""
        gt_binary = gt_row["gt_binary"] if gt_row else ""
        gt_scores = gt_row["scores"] if gt_row else []
        gt_scores_padded = list(gt_scores) + [""] * (7 - len(gt_scores))

        with open(csv_path, "a", newline="") as f:
            csv.writer(f).writerow([
                paper_id,
                f"{result['bt_score']:.4f}",
                "N/A",
                gt_avg,
                gt_decision,
                gt_binary,
                "N/A",
                "0.0000",
                "0.0000",
                *gt_scores_padded,
            ])
        print(f"  [{paper_id}] bt_score={result['bt_score']:.3f} n={result['n_anchors']} wins={result['n_wins']} losses={result['n_losses']}")

    await asyncio.gather(*(process_one(i, e) for i, e in enumerate(entries, 1)))
    print(f"\nDone. Results in {csv_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pairwise-score papers from cached merger pipeline log via Bradley-Terry")
    parser.add_argument("log_path", type=str, help="Path to the pipeline merge.log file")
    parser.add_argument("--data_dir", type=str, default=os.environ.get("DATA_DIR", "/home/wg25r/split_review/datasets/iclr2026_new"),
                        help="Dataset directory containing ratings.csv (for gt columns)")
    parser.add_argument("--papers_dir", type=str, default=None,
                        help="Override papers directory (remap paths from the log)")
    args = parser.parse_args()

    asyncio.run(run_batch(args.log_path, data_dir=args.data_dir, papers_dir=args.papers_dir))
