import argparse
import json
import os
import random
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import dotenv
from openai import OpenAI
from pydantic import BaseModel


class WeaknessItem(BaseModel):
    text: str
    match_in_review2: str | None


class OverlapResult(BaseModel):
    review1_weakness_items: list[WeaknessItem]


dotenv.load_dotenv(Path(__file__).parent.parent / ".env")

ROOT = Path(__file__).parent.parent
BASELINE_DIR = ROOT / "baselines" / "consolidated_reviews_2025"
HUMAN_DIR = Path("/home/wg25r/review_agent/deepreview_13k/human_reviews")

# methods used in hivemind.py — we mirror their paper sets to recover the same common-paper pool
METHODS = {
    "v1_DeepReviewer_7B_TXT": {"dir": BASELINE_DIR / "v1_DeepReviewer_7B_TXT_MD", "kind": "multi_reviewer"},
    "v1_DeepReviewer_14B_TXT": {"dir": BASELINE_DIR / "v1_DeepReviewer_14B_TXT_MD", "kind": "multi_reviewer"},
    "v2_API_DeepSeek_PDF": {"dir": BASELINE_DIR / "v2_API_DeepSeek_PDF", "kind": "single_report"},
    "v2_Local_Qwen_PDF": {"dir": BASELINE_DIR / "v2_Local_Qwen_PDF", "kind": "single_report"},
    "ours_wo_search": {"dir": ROOT / "results" / "test_mini_wo_search", "kind": "single_md"},
}

OUT_DIR = Path(__file__).parent / "hivemind_outputs"
OUT_DIR.mkdir(exist_ok=True)

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
JUDGE_MODEL = "deepseek/deepseek-v4-flash"
MAX_RETRIES = 5
RETRY_DELAY = 5

PROMPT = """You are comparing two paper reviews written by the SAME reviewer agent on TWO DIFFERENT papers. Identify each item in the WEAKNESS section of review 1 and, for each one, decide whether review 2 contains a SIMILAR weakness item — the same kind of methodological/presentation complaint applied to the other paper (e.g. "missing ablation", "no statistical significance", "overclaimed novelty", "writing/typos", "weak baselines").

Two items match if they describe the SAME KIND of problem, even when applied to different content. They do NOT match merely because both mention the same topic.

For each weakness item in review 1, output the item text and either the matching item summary from review 2, or null if there is no match.

=== REVIEW 1 (paper {pid1}) ===
{r1}

=== REVIEW 2 (paper {pid2}) ===
{r2}
"""


def list_papers(method_name):
    cfg = METHODS[method_name]
    d = cfg["dir"]
    if cfg["kind"] == "multi_reviewer":
        ids = set()
        for f in d.iterdir():
            m = re.match(r"^(.+)_reviewer(\d+)\.md$", f.name)
            if m:
                ids.add(m.group(1))
        return ids
    if cfg["kind"] == "single_report":
        return {f.name[: -len("_report.md")] for f in d.iterdir() if f.name.endswith("_report.md")}
    if cfg["kind"] == "single_md":
        return {f.stem for f in d.iterdir() if f.suffix == ".md"}
    raise ValueError(cfg["kind"])


def split_human_reviewers(md_text):
    parts = re.split(r"^## Human Reviewer \d+\s*$", md_text, flags=re.MULTILINE)
    return [p.strip() for p in parts[1:] if p.strip()]


def load_human_review(pid, rng):
    p = HUMAN_DIR / f"{pid}.md"
    if not p.exists():
        return None
    reviewers = split_human_reviewers(p.read_text())
    if not reviewers:
        return None
    return rng.choice(reviewers)


def judge(pid1, pid2, r1, r2):
    prompt = PROMPT.format(pid1=pid1, pid2=pid2, r1=r1, r2=r2)
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.chat.completions.parse(
                model=JUDGE_MODEL,
                messages=[{"role": "user", "content": prompt}],
                response_format=OverlapResult,
                extra_body={"reasoning": {"enabled": True}},
            )
            parsed = resp.choices[0].message.parsed
            break
        except Exception as e:
            if attempt == MAX_RETRIES:
                raise
            print(f"  retry {attempt}/{MAX_RETRIES} {pid1}/{pid2}: {type(e).__name__}: {e}")
            time.sleep(RETRY_DELAY * attempt)
    items = [it.model_dump() for it in parsed.review1_weakness_items]
    total = len(items)
    matched = sum(1 for it in items if it["match_in_review2"])
    rate = matched / total if total else None
    usage = resp.usage.model_dump() if resp.usage else None
    return {
        "method": "human",
        "paper1": pid1,
        "paper2": pid2,
        "n_items_review1": total,
        "n_matched": matched,
        "overlap_rate": rate,
        "items": items,
        "usage": usage,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n_base", type=int, default=30)
    ap.add_argument("--n_partners", type=int, default=3)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--out", type=str, default=str(OUT_DIR / "human_overlap_results.jsonl"))
    args = ap.parse_args()

    rng = random.Random(args.seed)

    method_papers = {m: list_papers(m) for m in METHODS}
    common = set.intersection(*method_papers.values())
    common_sorted = sorted(common)
    print(f"common across all methods: {len(common_sorted)}")

    have_human = {p.stem for p in HUMAN_DIR.iterdir() if p.suffix == ".md"}
    missing = [p for p in common_sorted if p not in have_human]
    if missing:
        print(f"WARNING: {len(missing)} common papers missing human reviews; e.g. {missing[:5]}")

    bases = rng.sample(common_sorted, min(args.n_base, len(common_sorted)))
    pairs = []
    for base in bases:
        pool = [p for p in common_sorted if p != base]
        partners = rng.sample(pool, args.n_partners)
        for partner in partners:
            pairs.append((base, partner))

    print(f"sampled {len(pairs)} paper pairs (same seed/scheme as hivemind.py)")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_f = open(out_path, "w")
    write_lock = threading.Lock()

    def run_one(pid1, pid2):
        reviewer_rng = random.Random((args.seed, "human", pid1, pid2).__hash__())
        r1 = load_human_review(pid1, reviewer_rng)
        r2 = load_human_review(pid2, reviewer_rng)
        if r1 is None or r2 is None:
            print(f"  skip human {pid1} {pid2}: missing review")
            return
        try:
            rec = judge(pid1, pid2, r1, r2)
        except Exception as e:
            print(f"  err human {pid1} {pid2}: {type(e).__name__}: {e}")
            return
        with write_lock:
            out_f.write(json.dumps(rec) + "\n")
            out_f.flush()
        print(f"  done human {pid1}/{pid2}: {rec['n_matched']}/{rec['n_items_review1']} rate={rec['overlap_rate']}")

    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = [ex.submit(run_one, a, b) for a, b in pairs]
        for f in futures:
            f.result()
    out_f.close()

    print(f"\nwrote {out_path}")
    rs = []
    with open(out_path) as f:
        for line in f:
            r = json.loads(line)
            if r["overlap_rate"] is not None:
                rs.append(r["overlap_rate"])
    if rs:
        rs_sorted = sorted(rs)
        mean = sum(rs) / len(rs)
        med = rs_sorted[len(rs)//2] if len(rs) % 2 else (rs_sorted[len(rs)//2 - 1] + rs_sorted[len(rs)//2]) / 2
        print(f"human: n={len(rs)} mean={mean:.3f} median={med:.3f}")
    else:
        print("human: no data")


if __name__ == "__main__":
    main()
