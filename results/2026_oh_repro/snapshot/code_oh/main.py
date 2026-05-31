"""Multi-agent paper reviewer — OpenHarness-only port of code/main.py.

Uses the oh_agent_sdk shim (which wraps OpenHarness with the Claude Agent SDK
surface). The harsh critic, neutral reviewer, and merger are all driven via
ClaudeSDKClient — no openai-agents, no claude-agent-sdk.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import os
import pickle
import random
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(_REPO_ROOT / "code"))

import numpy as np
import dotenv
from rank_bm25 import BM25Okapi
from openai import OpenAI

from paths import DATASETS_DIR, RESULTS_DIR, ensure_hf_file, prompt_path
from oh_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    RateLimitEvent,
    ResultMessage,
    TextBlock,
    create_sdk_mcp_server,
    tool,
)

dotenv.load_dotenv()

# ── Configuration ────────────────────────────────────────────────────
_POSITION_MODE = os.environ.get("POSITION_MODE", "").strip().lower() in ("1", "true", "yes")
HARSH_MODEL = os.environ.get("HARSH_MODEL", "claude-sonnet-4-5")
NEUTRAL_MODEL = os.environ.get("NEUTRAL_MODEL", HARSH_MODEL)
MERGER_MODEL = os.environ.get("MERGER_MODEL", HARSH_MODEL)
CONCURRENCY = int(os.environ.get("CONCURRENCY", 1))

if _POSITION_MODE:
    HUMAN_REVIEW_DIR = str((DATASETS_DIR / "neurips_position_human_review").resolve())
    _EMB_FILE = "human_reviews_embeddings_position.pkl"
    _IDX_FILE = "human_review_score_index_position.pkl"
else:
    HUMAN_REVIEW_DIR = str((DATASETS_DIR / "deepreview_13k_calibration").resolve())
    _EMB_FILE = "human_reviews_embeddings_deepreview.pkl"
    _IDX_FILE = "human_review_score_index_deepreview.pkl"

_or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

# ── Prompt loading ───────────────────────────────────────────────────
with open(prompt_path("timeline.md"), "r") as _f:
    _TIMELINE = _f.read().replace("{{CURRENT_DATE}}", time.strftime("%Y-%m-%d"))
with open(prompt_path("cal_with.md"), "r") as _f:
    _CAL_WITH = _f.read()
with open(prompt_path("cal_without.md"), "r") as _f:
    _CAL_WITHOUT = _f.read()

_PAPER_ACCESS_FILE = (
    "The paper path is provided in the user message. Use read_file to read the paper "
    "(it reads the whole file by default — do not pass start_line/end_line unless you "
    "specifically need a slice) and verify reviewer claims directly."
)


def load_prompt(path: str, no_cal: bool = False) -> str:
    with open(prompt_path(path), "r") as f:
        raw = f.readlines()
    kept = [line for line in raw if not line.lstrip().startswith("&&")]
    text = "".join(kept)
    text = text.replace("{{PAPER_ACCESS_INSTRUCTION}}", _PAPER_ACCESS_FILE)
    text = text.replace("{{CALIBRATION_INSTRUCTION}}", _CAL_WITHOUT if no_cal else _CAL_WITH)
    return text + "\n\n" + _TIMELINE


# ── Calibration index ────────────────────────────────────────────────
_CAL_INDEX: dict = {}


def _ensure_indexes() -> None:
    if _CAL_INDEX:
        return
    print(f"Indexing calibration corpus from {HUMAN_REVIEW_DIR} ...")
    start = time.time()
    docs, paths = [], []
    for root, _, files in os.walk(HUMAN_REVIEW_DIR):
        for fname in files:
            if fname.endswith(".txt") or fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", errors="replace") as fh:
                    content = fh.read()
                if content.strip():
                    docs.append(content)
                    paths.append(fpath)
    _CAL_INDEX["bm25"] = BM25Okapi([d.split(" ") for d in docs])
    _CAL_INDEX["bm25_paths"] = paths

    emb_path = ensure_hf_file(_EMB_FILE)
    idx_path = ensure_hf_file(_IDX_FILE)
    with open(emb_path, "rb") as f:
        db = pickle.load(f)
    _CAL_INDEX["filenames"] = list(db.keys())
    _CAL_INDEX["vectors"] = np.array(list(db.values()))
    with open(idx_path, "rb") as f:
        _CAL_INDEX["score_index"] = pickle.load(f)
    print(f"Indexing complete in {time.time() - start:.2f}s")


_EXCLUDED_PAPER_IDS: set[str] = set()


def set_excluded_paper_ids(ids) -> None:
    _EXCLUDED_PAPER_IDS.clear()
    _EXCLUDED_PAPER_IDS.update(ids)
    print(f"  [calibration] excluding {len(_EXCLUDED_PAPER_IDS)} test paper id(s)")


# ── MCP tools (shim form) ────────────────────────────────────────────
def _build_review_mcp(paper_dir: str, no_cal: bool):
    if not no_cal:
        _ensure_indexes()
    allowed = [os.path.abspath(paper_dir), os.path.abspath(HUMAN_REVIEW_DIR)]

    def _check(path: str) -> str | None:
        resolved = os.path.abspath(path)
        if any(resolved.startswith(ap) for ap in allowed):
            return None
        return f"ERROR: Access denied. '{resolved}' not under any allowed directory: {allowed}"

    @tool(
        "read_file",
        "Read lines from a file. Returns lines numbered start_line to end_line (1-based). end_line=0 reads to EOF.",
        {"abs_path": str, "start_line": int, "end_line": int},
    )
    async def _read_file(args: dict) -> dict:
        abs_path = args["abs_path"]
        start_line = args.get("start_line") or 1
        end_line = args.get("end_line") or 0
        print(f"  [oh:read_file] {abs_path} lines {start_line}-{end_line or 'EOF'}")
        err = _check(abs_path)
        if err:
            return {"content": [{"type": "text", "text": err}], "is_error": True}
        try:
            with open(abs_path, "r", errors="replace") as fh:
                lines = fh.readlines()
        except FileNotFoundError:
            return {"content": [{"type": "text", "text": f"ERROR: File not found: {abs_path}"}], "is_error": True}
        selected = lines[max(0, start_line - 1): end_line if end_line > 0 else len(lines)]
        text = "".join(f"{start_line + i}: {line}" for i, line in enumerate(selected))
        return {"content": [{"type": "text", "text": text}]}

    @tool(
        "grep_file",
        "Search a single file for a substring/regex pattern. Returns matching lines with line numbers.",
        {"pattern": str, "abs_path": str},
    )
    async def _grep_file(args: dict) -> dict:
        pattern = args["pattern"]
        abs_path = args["abs_path"]
        print(f"  [oh:grep_file] '{pattern}' in {abs_path}")
        err = _check(abs_path)
        if err:
            return {"content": [{"type": "text", "text": err}], "is_error": True}
        if not os.path.isfile(abs_path):
            return {"content": [{"type": "text", "text": f"ERROR: '{abs_path}' is not a file."}], "is_error": True}
        matches = []
        with open(abs_path, "r", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                if re.search(pattern, line):
                    matches.append(f"{i}: {line.rstrip()}")
        text = "\n".join(matches) if matches else "No matches found."
        return {"content": [{"type": "text", "text": text}]}

    def _vector_query(query: str, n: int, low_score: float, high_score: float) -> str:
        score_index = _CAL_INDEX["score_index"]
        vectors = _CAL_INDEX["vectors"]
        filenames = _CAL_INDEX["filenames"]
        mask = np.array([
            (low_score < score_index.get(fn, -1.0) < high_score)
            and fn.rsplit(".", 1)[0] not in _EXCLUDED_PAPER_IDS
            for fn in filenames
        ])
        if not mask.any():
            return "No files in that score range."
        emb = _or_client.embeddings.create(
            model="google/gemini-embedding-001", input=query, encoding_format="float"
        )
        qv = np.array(emb.data[0].embedding)
        sims = vectors @ qv.T
        masked = np.where(mask, sims, -np.inf)
        top = masked.argsort()[-n:][::-1]
        out = []
        for idx in top:
            if not np.isfinite(masked[idx]):
                break
            fn = filenames[idx]
            fpath = os.path.abspath(os.path.join(HUMAN_REVIEW_DIR, fn))
            with open(fpath, "r", errors="replace") as fh:
                content = fh.read()
            out.append(
                f"{fpath}\navg_score: {score_index.get(fn, -1.0):.2f}  sim: {sims[idx]:.2f}\n"
                f"first 1000 chars:\n{content[:1000]}\n"
            )
        return "\n---\n".join(out) if out else "No relevant files found."

    @tool(
        "calibration_search",
        "RAG retrieval over the human-review corpus. Pass a list of queries; each runs vector search "
        "and returns top-n hits with avg human score and first 1000 chars. Up to 3 calls total per session.",
        {
            "type": "object",
            "properties": {
                "queries": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "n": {"type": "integer"},
                            "low_score": {"type": "number"},
                            "high_score": {"type": "number"},
                        },
                        "required": ["query"],
                    },
                }
            },
            "required": ["queries"],
        },
    )
    async def _calibration_search(args: dict) -> dict:
        queries = args.get("queries")
        if not isinstance(queries, list) or not queries:
            return {"content": [{"type": "text", "text": "ERROR: 'queries' must be a non-empty list."}], "is_error": True}
        sections = []
        for i, q in enumerate(queries, 1):
            qtext = str(q["query"])
            n = int(q.get("n", 4) or 4)
            low = float(q.get("low_score") if q.get("low_score") is not None else -1.0)
            high = float(q.get("high_score") if q.get("high_score") is not None else 11.0)
            print(f"  [oh:calibration_search] q{i}='{qtext}' n={n} score=({low}, {high})")
            body = _vector_query(qtext, n, low, high)
            sections.append(f"### Query {i}: {qtext!r}  (n={n}, score=({low}, {high}))\n{body}")
        return {"content": [{"type": "text", "text": "\n\n".join(sections)}]}

    tools_list = [_read_file, _grep_file]
    if not no_cal:
        tools_list.append(_calibration_search)
    return create_sdk_mcp_server(name="review_fs", version="1.0.0", tools=tools_list)


# ── Agent driver ─────────────────────────────────────────────────────
async def _run_agent(
    *,
    label: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    paper_dir: str,
    allowed_tool_names: list[str],
    no_cal: bool,
    max_turns: int,
) -> tuple[str, dict]:
    print(f"  [{label}] starting OpenHarness agent ({model}) ...")
    server = _build_review_mcp(paper_dir, no_cal=no_cal)
    options = ClaudeAgentOptions(
        model=model,
        system_prompt=system_prompt,
        allowed_tools=[f"mcp__review_fs__{n}" for n in allowed_tool_names],
        mcp_servers={"review_fs": server},
        permission_mode="bypassPermissions",
        max_turns=max_turns,
        cwd="/tmp",
    )

    text = ""
    usage_payload: dict = {
        "model": model,
        "session_id": None,
        "total_cost_usd": None,
        "num_turns": None,
        "duration_ms": None,
        "duration_api_ms": None,
        "usage": None,
        "rate_limit": None,
    }
    async with ClaudeSDKClient(options=options) as client:
        await client.query(user_prompt)
        async for msg in client.receive_response():
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock):
                        text += block.text
            elif isinstance(msg, RateLimitEvent):
                rl = msg.rate_limit_info
                usage_payload["rate_limit"] = {
                    "status": rl.status,
                    "type": rl.rate_limit_type,
                    "utilization": rl.utilization,
                    "resets_at": rl.resets_at,
                    "overage_status": rl.overage_status,
                }
            elif isinstance(msg, ResultMessage):
                usage_payload["session_id"] = msg.session_id
                usage_payload["total_cost_usd"] = msg.total_cost_usd
                usage_payload["num_turns"] = msg.num_turns
                usage_payload["duration_ms"] = msg.duration_ms
                usage_payload["duration_api_ms"] = msg.duration_api_ms
                usage_payload["usage"] = msg.usage

    if not text.strip():
        raise RuntimeError(f"[{label}] OpenHarness agent returned empty output")
    print(f"  [{label}] done")
    return text, usage_payload


# ── Pipeline ─────────────────────────────────────────────────────────
_REVIEW_TEMPLATE = """Review the following paper thoroughly.

The paper was extracted from PDF by an automated parser. Treat formatting artifacts (broken equations, garbled tables, OCR errors) as parser issues, not paper flaws. The appendix and references were stripped by the parser; assume they exist in the original submission and don't flag them as missing.

Paper path: {paper_path}. Use read_file (which reads the whole file by default) to read the paper end-to-end before reviewing."""


async def run_pipeline(paper_path: str):
    """Yield (variant_name, variant_result) as each merger finishes, so callers
    can flush per-variant outputs incrementally instead of waiting for both
    mergers to complete."""
    paper_abs = os.path.abspath(paper_path)
    paper_dir = str(Path(paper_abs).parent)

    review_user_prompt = _REVIEW_TEMPLATE.format(paper_path=paper_abs)

    harsh_system = load_prompt("harsh_critic_position.md" if _POSITION_MODE else "harsh_critic.md")
    neutral_system = load_prompt("neutral_reviewer_position.md" if _POSITION_MODE else "neutral_reviewer.md")

    print("  Phase 1: harsh + neutral in parallel ...")
    harsh_task = _run_agent(
        label="Harsh Critic",
        model=HARSH_MODEL,
        system_prompt=harsh_system,
        user_prompt=review_user_prompt,
        paper_dir=paper_dir,
        allowed_tool_names=["read_file"],
        no_cal=True,
        max_turns=15,
    )
    neutral_task = _run_agent(
        label="Strength Finder",
        model=NEUTRAL_MODEL,
        system_prompt=neutral_system,
        user_prompt=review_user_prompt,
        paper_dir=paper_dir,
        allowed_tool_names=["read_file"],
        no_cal=True,
        max_turns=15,
    )
    (harsh_text, _harsh_usage), (neutral_text, _neutral_usage) = await asyncio.gather(harsh_task, neutral_task)

    labeled = f"### Harsh Critic\n{harsh_text}\n\n### Strength Finder\n{neutral_text}"

    merger_user = (
        f"Here is the paper being reviewed (extracted from PDF — formatting artifacts are parser issues).\n\n"
        f"Paper path: {paper_abs}, read it in chunks.\n\n"
        f"Human reviews directory (for calibration): {HUMAN_REVIEW_DIR}\n\n"
        f"Here are the inputs:\n\n{labeled}\n\n"
        f"Now produce the final consolidated review following your instructions. "
        f"Cross-check every claim against the actual paper."
    )

    for variant_name, no_cal in (("cal", False), ("no_cal", True)):
        merger_system = load_prompt(
            "merger_position.md" if _POSITION_MODE else "merger.md",
            no_cal=no_cal,
        )
        allowed = ["read_file", "grep_file"] + ([] if no_cal else ["calibration_search"])

        print(f"  Phase 2 [{variant_name}]: merger ...")
        merged, merger_usage = await _run_agent(
            label=f"Merger ({variant_name})",
            model=MERGER_MODEL,
            system_prompt=merger_system,
            user_prompt=merger_user,
            paper_dir=paper_dir,
            allowed_tool_names=allowed,
            no_cal=no_cal,
            max_turns=30,
        )
        score = float(merged.split("<score>")[1].split("</score>")[0]) if "<score>" in merged else -1
        decision = merged.split("<decision>")[1].split("</decision>")[0] if "<decision>" in merged else "N/A"
        yield variant_name, {
            "merged_review": merged,
            "scorer_output": score,
            "decision": decision,
            "merger_usage": merger_usage,
        }


# ── Ground truth + benchmark ─────────────────────────────────────────
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
    print(f"  Stratified sample: {len(samples)} papers from {len(bins)} bins")
    return samples


_VARIANTS = ("cal", "no_cal")


def _bench_output_paths(reviews_dir: str | None) -> dict[str, tuple[Path, Path]]:
    """Return {variant_name: (csv_path, reviews_dir)} for the two merger variants.

    Relative OUTPUT_CSV / REVIEWS_DIR are resolved under RESULTS_DIR to match
    code/main.py — otherwise launcher scripts that export e.g.
    OUTPUT_CSV="$SWEEP_NAME/scores.csv" silently land files in cwd."""
    base_csv = Path(os.getenv("OUTPUT_CSV", str(RESULTS_DIR / "bench_oh_scores.csv")))
    if not base_csv.is_absolute():
        base_csv = RESULTS_DIR / base_csv
    base_rdir = Path(reviews_dir) if reviews_dir else Path(
        os.getenv("REVIEWS_DIR", str(RESULTS_DIR / "bench_oh_reviews"))
    )
    if not base_rdir.is_absolute():
        base_rdir = RESULTS_DIR / base_rdir
    out: dict[str, tuple[Path, Path]] = {}
    for v in _VARIANTS:
        csv_p = base_csv.with_name(f"{base_csv.stem}_{v}{base_csv.suffix}")
        rdir = base_rdir.with_name(f"{base_rdir.name}_{v}")
        out[v] = (csv_p, rdir)
    return out


async def run_benchmark(
    data_dir: str,
    n_samples: int = 10,
    seed: int = 42,
    balanced: bool = False,
    include_cal_papers: bool = False,
    reviews_dir: str | None = None,
):
    data_path = Path(data_dir)
    gt_data, papers_dir = load_ground_truth(data_path)
    available = [r for r in gt_data if (papers_dir / f"{r['paper_id']}.txt").exists()]
    print(f"Available papers: {len(available)}")

    if balanced:
        samples = stratified_sample(available, n_per_bin=max(1, n_samples // 10), seed=seed)
    else:
        samples = random.Random(seed).sample(available, min(n_samples, len(available)))

    samples = samples[: int(os.environ.get("MAX_PAPERS", len(samples)))]

    if not include_cal_papers:
        set_excluded_paper_ids({s["paper_id"] for s in samples})

    outputs = _bench_output_paths(reviews_dir)
    for v, (csv_p, rdir) in outputs.items():
        csv_p.parent.mkdir(parents=True, exist_ok=True)
        rdir.mkdir(parents=True, exist_ok=True)
        with open(csv_p, "w", newline="") as f:
            csv.writer(f).writerow([
                "paper_id", "pred_score", "pred_decision",
                "gt_avg_score", "gt_decision", "gt_binary", "match",
                "cost", "sdk_savings",
                "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3",
                "gt_score_4", "gt_score_5", "gt_score_6",
            ])
        print(f"  [{v}] csv={csv_p}  reviews={rdir}")

    sem = asyncio.Semaphore(CONCURRENCY)

    async def process_one(i: int, info: dict):
        async with sem:
            pid = info["paper_id"]
            paper_path = papers_dir / f"{pid}.txt"
            print(f"\n[{i}/{len(samples)}] {info.get('title', pid)} (avg={info['avg_score']:.1f})")
            gt_scores_padded = info["scores"] + [""] * (7 - len(info["scores"]))
            try:
                async for v, r in run_pipeline(str(paper_path)):
                    pred = r["scorer_output"]
                    dec = r["decision"]
                    match = "N/A" if dec in (None, "", "N/A") else ("YES" if dec == info["gt_binary"] else "NO")
                    print(f"  [{pid}][{v}] pred={pred} gt={info['avg_score']:.1f} match={match}")
                    csv_p, rdir = outputs[v]
                    with open(csv_p, "a", newline="") as f:
                        csv.writer(f).writerow([
                            pid, pred, dec,
                            f"{info['avg_score']:.2f}", info["decision"], info["gt_binary"], match,
                            "0.0000", "0.0000",
                            *gt_scores_padded,
                        ])
                    (rdir / f"{pid}.md").write_text(r["merged_review"], encoding="utf-8")
            except Exception as exc:
                print(f"  ⚠️  [{pid}] failed: {type(exc).__name__}: {exc}")
                return

    await asyncio.gather(*(process_one(i, p) for i, p in enumerate(samples, 1)))


async def run_single_paper(paper_path: str) -> None:
    print(f"Reviewing: {paper_path}")
    out_dir = Path(__file__).parent / "reviews"
    out_dir.mkdir(exist_ok=True)
    stem = Path(paper_path).stem
    ts = time.strftime("%Y_%m_%d_%H_%M_%S")
    async for v, r in run_pipeline(paper_path):
        print("\n" + "=" * 72 + f"\nFINAL REVIEW [{v}]\n" + "=" * 72)
        print(r["merged_review"])
        if r["scorer_output"] != -1:
            print(f"\nPredicted score [{v}]: {r['scorer_output']}  decision: {r['decision']}")
        out_path = out_dir / f"{stem}_{v}_review_{ts}.md"
        out_path.write_text(f"# Review of {paper_path} ({v})\n\n{r['merged_review']}\n", encoding="utf-8")
        print(f"Saved [{v}]: {out_path}")


# ── CLI ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-agent reviewer (OpenHarness)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--single_paper", type=str)
    group.add_argument("--benchmark", type=str, metavar="DATA_DIR")
    parser.add_argument("--n_samples", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--balanced", action="store_true")
    parser.add_argument("--include_cal_papers", action="store_true")
    parser.add_argument("--reviews_dir", type=str, default=None)
    args = parser.parse_args()

    if args.single_paper:
        asyncio.run(run_single_paper(args.single_paper))
    else:
        asyncio.run(run_benchmark(
            args.benchmark,
            n_samples=args.n_samples,
            seed=args.seed,
            balanced=args.balanced,
            include_cal_papers=args.include_cal_papers,
            reviews_dir=args.reviews_dir,
        ))
