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

METHODS = {
    "v1_DeepReviewer_7B_TXT": {
        "dir": BASELINE_DIR / "v1_DeepReviewer_7B_TXT_MD",
        "kind": "multi_reviewer",
    },
    "v1_DeepReviewer_14B_TXT": {
        "dir": BASELINE_DIR / "v1_DeepReviewer_14B_TXT_MD",
        "kind": "multi_reviewer",
    },
    "v2_API_DeepSeek_PDF": {
        "dir": BASELINE_DIR / "v2_API_DeepSeek_PDF",
        "kind": "single_report",
    },
    "v2_Local_Qwen_PDF": {
        "dir": BASELINE_DIR / "v2_Local_Qwen_PDF",
        "kind": "single_report",
    },
    "ours_wo_search": {
        "dir": ROOT / "results" / "test_mini_wo_search",
        "kind": "single_md",
    },
}

OUT_DIR = Path(__file__).parent / "hivemind_outputs"
OUT_DIR.mkdir(exist_ok=True)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

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


def load_review(method_name, pid, rng):
    cfg = METHODS[method_name]
    d = cfg["dir"]
    if cfg["kind"] == "multi_reviewer":
        candidates = sorted(d.glob(f"{pid}_reviewer*.md"))
        if not candidates:
            return None
        chosen = rng.choice(candidates)
        return chosen.read_text()
    if cfg["kind"] == "single_report":
        p = d / f"{pid}_report.md"
        return p.read_text() if p.exists() else None
    if cfg["kind"] == "single_md":
        p = d / f"{pid}.md"
        return p.read_text() if p.exists() else None


def judge(method, pid1, pid2, r1, r2):
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
            print(f"  retry {attempt}/{MAX_RETRIES} {method} {pid1}/{pid2}: {type(e).__name__}: {e}")
            time.sleep(RETRY_DELAY * attempt)
    items = [it.model_dump() for it in parsed.review1_weakness_items]
    total = len(items)
    matched = sum(1 for it in items if it["match_in_review2"])
    rate = matched / total if total else None
    usage = resp.usage.model_dump() if resp.usage else None
    return {
        "method": method,
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
    ap.add_argument("--n_base", type=int, default=30, help="number of base papers")
    ap.add_argument("--n_partners", type=int, default=3, help="partner papers per base")
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--out", type=str, default=str(OUT_DIR / "overlap_results.jsonl"))
    args = ap.parse_args()

    rng = random.Random(args.seed)

    method_papers = {m: list_papers(m) for m in METHODS}
    for m, s in method_papers.items():
        print(f"{m}: {len(s)} papers")
    common = set.intersection(*method_papers.values())
    print(f"common across all methods: {len(common)}")
    common_sorted = sorted(common)

    if len(common_sorted) < args.n_partners + 1:
        raise RuntimeError(f"need at least {args.n_partners + 1} papers in common")

    bases = rng.sample(common_sorted, min(args.n_base, len(common_sorted)))
    pairs = []
    for base in bases:
        pool = [p for p in common_sorted if p != base]
        partners = rng.sample(pool, args.n_partners)
        for partner in partners:
            pairs.append((base, partner))

    print(f"sampled {len(pairs)} paper pairs")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_f = open(out_path, "w")
    write_lock = threading.Lock()

    def run_one(method, pid1, pid2):
        reviewer_rng = random.Random((args.seed, method, pid1, pid2).__hash__())
        r1 = load_review(method, pid1, reviewer_rng)
        r2 = load_review(method, pid2, reviewer_rng)
        if r1 is None or r2 is None:
            print(f"  skip {method} {pid1} {pid2}: missing review")
            return
        try:
            rec = judge(method, pid1, pid2, r1, r2)
        except Exception as e:
            print(f"  err {method} {pid1} {pid2}: {type(e).__name__}: {e}")
            return
        with write_lock:
            out_f.write(json.dumps(rec) + "\n")
            out_f.flush()
        print(f"  done {method} {pid1}/{pid2}: {rec['n_matched']}/{rec['n_items_review1']} rate={rec['overlap_rate']}")

    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = []
        for pid1, pid2 in pairs:
            for method in METHODS:
                futures.append(ex.submit(run_one, method, pid1, pid2))
        for f in futures:
            f.result()
    out_f.close()

    print(f"\nwrote {out_path}")
    by_method = {}
    with open(out_path) as f:
        for line in f:
            r = json.loads(line)
            by_method.setdefault(r["method"], []).append(r)
    print("\n=== mean overlap rate (weakness, review1 -> review2) ===")
    for m in METHODS:
        rs = [r["overlap_rate"] for r in by_method.get(m, []) if r["overlap_rate"] is not None]
        if rs:
            print(f"  {m}: mean={sum(rs)/len(rs):.3f} n={len(rs)}")
        else:
            print(f"  {m}: no data")


if __name__ == "__main__":
    main()
