# %%
"""
Standalone calibration agent: reads uncalibrated reviews from
results/original_nocal/reviews/*.md, runs the SAME calibration logic the merger
uses (calibration_search MCP tool + prompts/cal_with_sdk.md), and writes a new CSV
with a calibrated_score column. Review files are left untouched.

Deepreview calibration set only. Model via CAL_MODEL (default claude-opus-4-7).
"""
import os
import re
import csv
import asyncio
from pathlib import Path

import dotenv
dotenv.load_dotenv()

from paths import RESULTS_DIR, prompt_path
from claude_merger import _make_merger_mcp_server, _run_claude_sdk_query

REVIEW_DIR = Path(os.getenv("CAL_REVIEW_DIR", str(RESULTS_DIR / "original_nocal" / "reviews")))
OUT_CSV = Path(os.getenv("POST_HOC_CAL_CSV", str(RESULTS_DIR / "original_nocal" / "calibrated_scores.csv")))
GT_CSV = Path(os.getenv("POST_HOC_GT_CSV", os.path.expanduser("~/review_agent/iclr2026_new/ratings.csv")))
CAL_MODEL = os.getenv("CAL_MODEL", "claude-opus-4-7")
CONCURRENCY = int(os.getenv("CONCURRENCY", "10"))

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

CSV_HEADER = [
    "paper_id", "pred_score", "pred_decision",
    "gt_avg_score", "gt_decision", "gt_binary", "match", "cost", "sdk_savings",
    "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6",
]

with open(prompt_path("cal_with_sdk.md"), "r") as f:
    CAL_INSTRUCTION = f.read()

_gt_index = {}
with open(GT_CSV, "r", newline="") as f:
    for row in csv.DictReader(f):
        _gt_index[row["paper_id"].strip()] = row

if not OUT_CSV.exists() or OUT_CSV.stat().st_size == 0:
    with open(OUT_CSV, "w", newline="") as f:
        csv.writer(f).writerow(CSV_HEADER)

_logged_paper_ids = set()
with open(OUT_CSV, "r", newline="") as f:
    for row in csv.DictReader(f):
        _logged_paper_ids.add(row["paper_id"])

_csv_lock = asyncio.Lock()
_sem = asyncio.Semaphore(CONCURRENCY)

# The cal_with_sdk.md protocol drives calibration_search; here we ask the agent to
# score the given review (not a paper) and emit both score and decision tags.
USER_PROMPT = """\
You are calibrating an already-written paper review. Do NOT re-review the paper.
Read the review below, follow the calibration protocol in your instructions to
retrieve and read human-review anchors, then place this review's quality relative
to those anchors.

Human reviews directory (for calibration): {human_review_dir}

Review under calibration:

{review_body}

Output your final calibrated score as <score>X.X</score> (1-10 in 0.5 increments)
and your decision as <decision>Accept</decision> or <decision>Reject</decision>.
"""


async def cal_paper(review_filename: str):
    paper_id = review_filename.rsplit(".", 1)[0]
    if paper_id in _logged_paper_ids:
        print(f"  [{paper_id}] already logged — skipping")
        return

    with open(REVIEW_DIR / review_filename, "r") as f:
        full_review = f.read()

    raw_match = re.search(r"<score>\s*([\d.]+)\s*</score>", full_review)
    if not raw_match:
        print(f"  [{paper_id}] no <score> in input review — skipping")
        return
    pred_score = float(raw_match.group(1))

    # Strip the entire trailing "## Score and Decision" section so the first
    # agent's predicted score/decision can't bias calibration.
    review_body = re.split(r"\n#+\s*Score and Decision", full_review)[0].strip()

    if paper_id not in _gt_index:
        raise RuntimeError(f"[{paper_id}] not found in ground truth {GT_CSV}")
    gt = _gt_index[paper_id]
    gt_scores = [gt.get(f"score_{i}", "") for i in range(7)]
    gt_binary = gt.get("gt_binary", "").strip()

    from claude_merger import HUMAN_REVIEW_DIR
    mcp_server = _make_merger_mcp_server(
        paper_dir=HUMAN_REVIEW_DIR,
        no_cal=False,
        exclude_basenames={paper_id},
    )

    async with _sem:
        response_text, usage = await _run_claude_sdk_query(
            label=f"Cal {paper_id}",
            model_id=CAL_MODEL,
            system_prompt=CAL_INSTRUCTION,
            user_prompt=USER_PROMPT.format(human_review_dir=HUMAN_REVIEW_DIR, review_body=review_body),
            allowed_tools=["mcp__merger_fs__read_file", "mcp__merger_fs__calibration_search"],
            mcp_servers={"merger_fs": mcp_server},
            max_turns=30,
        )

    cal_match = re.search(r"<score>\s*([\d.]+)\s*</score>", response_text)
    if not cal_match:
        print(f"  [{paper_id}] no <score> tag in calibration response — skipping")
        return
    calibrated_score = float(cal_match.group(1))

    dec_match = re.search(r"<decision>(.*?)</decision>", response_text, re.DOTALL)
    pred_decision = dec_match.group(1).strip() if dec_match else "N/A"
    match_str = "N/A" if pred_decision in ("", "N/A") else ("YES" if pred_decision == gt_binary else "NO")

    cost = usage.get("total_cost_usd") or 0.0
    gt_scores_padded = gt_scores + [""] * (7 - len(gt_scores))

    async with _csv_lock:
        with open(OUT_CSV, "a", newline="") as f:
            csv.writer(f).writerow([
                paper_id,
                calibrated_score,
                pred_decision,
                f"{float(gt.get('avg_score', 0)):.2f}",
                gt.get("decision", "").strip(),
                gt_binary,
                match_str,
                f"{cost:.4f}",
                "0.0000",
                *gt_scores_padded,
            ])
        _logged_paper_ids.add(paper_id)
    print(f"  [{paper_id}] pred={pred_score} calibrated={calibrated_score} cost=${cost:.4f} — logged")


async def main():
    reviews = sorted(f for f in os.listdir(REVIEW_DIR) if f.endswith(".md"))
    limit = int(os.getenv("CAL_LIMIT", "0"))
    if limit > 0:
        reviews = reviews[:limit]
    await asyncio.gather(*(cal_paper(r) for r in reviews))


# %%
if __name__ == "__main__":
    asyncio.run(main())
