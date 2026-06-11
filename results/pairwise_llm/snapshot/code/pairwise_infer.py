import asyncio
import csv
import json
import os
import pickle
import random
import re

import numpy as np
import pandas as pd
import dotenv
from openai import AsyncOpenAI
from scipy.stats import pearsonr, spearmanr

dotenv.load_dotenv()

N_PAPERS = 30
N_SHOTS = 15
KTO_SEED_N = 300
CONCURRENCY = 10
FOLDER = "results/2026_deepseek_train_balanced"
SAMPLES_JSONL = "results/zto_samples.jsonl"
JUDGE_MODEL = "deepseek/deepseek-v4-pro"
OUT_CSV = "results/pairwise_infer_scores.csv"
OUT_JSONL = "results/pairwise_infer_judgments.jsonl"

SYSTEM_PROMPT = """You are given two reviews of two different papers. Your job is to determine which paper is better, judging from its review — evaluate the papers themselves, not the quality of the reviews. The first review is AI generated and the second one is human written; the AI reviewer can sometimes be too nice, account for that. Answer with a single token: 0 if the first paper is better, 1 if the second paper is better, or tie if they are about equally good (within 1 point on a 10-point scale)."""

client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

scores = pd.read_csv(f"{FOLDER}/scores.csv").drop_duplicates("paper_id")
gt_by_pid = dict(zip(scores["paper_id"], scores["gt_avg_score"].astype(float)))

with open("datasets/human_reviews_embeddings_deepreview.pkl", "rb") as f:
    emb_db = pickle.load(f)
with open("datasets/human_review_score_index_deepreview.pkl", "rb") as f:
    score_index = pickle.load(f)

cal_files = np.array(list(emb_db.keys()))
cal_vectors = np.array(list(emb_db.values()))
cal_scores = np.array([score_index[fn] for fn in cal_files])
bin_edges = np.linspace(0.5, 8.0, 11)
cal_bins = np.clip(np.digitize(cal_scores, bin_edges) - 1, 0, 9)


def strip_ai_review(text: str) -> str:
    text = text.split("## Score and Decision")[0]
    text = re.sub(r"^MY FINAL (SCORE|DECISION):.*$", "", text, flags=re.M)
    text = re.sub(r"<score>[^<]*</score>", "", text)
    text = re.sub(r"<decision>[^<]*</decision>", "", text)
    return text.strip()


def strip_human_review(text: str) -> str:
    text = re.sub(r"^- (Decision|Avg Score|Scores):.*\n", "", text, flags=re.M)
    text = re.sub(
        r"^### (Rating Number|Rating|Confidence|Soundness|Presentation|Contribution)\s*\n(?:(?!#).*\n?)*",
        "", text, flags=re.M,
    )
    return text.strip()


def elo_estimate(anchor_ratings: list[float], outcomes: list[float]) -> float:
    s_obs = sum(outcomes)
    lo = min(anchor_ratings) - 800
    hi = max(anchor_ratings) + 800
    expected = lambda r: sum(1 / (1 + 10 ** ((ra - r) / 400)) for ra in anchor_ratings)
    if expected(lo) >= s_obs:
        return lo
    if expected(hi) <= s_obs:
        return hi
    for _ in range(100):
        mid = (lo + hi) / 2
        if expected(mid) < s_obs:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


pids = [pid for pid in gt_by_pid if os.path.exists(f"{FOLDER}/reviews/{pid}.md")]
kto_pids = set(random.Random(42).sample(pids, KTO_SEED_N))
eval_pool = [pid for pid in pids if pid not in kto_pids]
eval_pids = random.Random(0).sample(eval_pool, N_PAPERS)

with open(SAMPLES_JSONL) as f:
    sample_rows = [json.loads(line) for line in f if line.endswith("\n")]
positives = [r for r in sample_rows if r["label"]]
random.Random(0).shuffle(positives)
shots = []
seen_papers = set()
for r in positives:
    if r["paper_id"] in seen_papers:
        continue
    seen_papers.add(r["paper_id"])
    shots.append(r)
    if len(shots) == N_SHOTS:
        break
assert len(shots) == N_SHOTS, f"only found {len(shots)} few-shot papers"
fewshot_turns = []
for r in shots:
    fewshot_turns.append({"role": "user", "content": r["prompt"][1]["content"]})
    fewshot_turns.append({"role": "assistant", "content": r["gt_answer"]})
print(json.dumps({"event": "shots_picked", "n": len(shots), "answers": [r["gt_answer"] for r in shots]}))

embed_sem = asyncio.Semaphore(5)
judge_sem = asyncio.Semaphore(CONCURRENCY)
cost_total = {"usd": 0.0, "calls": 0}
out_f = open(OUT_JSONL, "w")


async def build_pairs(pid: str) -> list[dict]:
    with open(f"{FOLDER}/reviews/{pid}.md") as f:
        raw = f.read()
    async with embed_sem:
        for attempt in range(3):
            try:
                resp = await client.embeddings.create(
                    model="google/gemini-embedding-001", input=raw, encoding_format="float"
                )
                break
            except Exception as e:
                print(f"embed error {pid} (attempt {attempt + 1}/3): {e}")
                await asyncio.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f"embedding failed for {pid} after 3 attempts")
    query = np.array(resp.data[0].embedding)
    sims = cal_vectors @ query
    ai_review = strip_ai_review(raw)
    pairs = []
    for b in range(10):
        mask = (cal_bins == b) & (cal_files != f"{pid}.md")
        masked = np.where(mask, sims, -np.inf)
        idx = int(masked.argmax())
        anchor_fn = str(cal_files[idx])
        with open(f"datasets/deepreview_13k_calibration/{anchor_fn}", errors="replace") as f:
            anchor_review = strip_human_review(f.read())
        pairs.append({
            "paper_id": pid,
            "anchor_id": anchor_fn,
            "bin": b,
            "anchor_gt": float(cal_scores[idx]),
            "user_content": f"Review 1:\n\n{ai_review}\n\n---\n\nReview 2:\n\n{anchor_review}",
        })
    return pairs


async def judge(pair: dict, mode: str) -> float:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if mode == "fewshot":
        messages += fewshot_turns
    messages.append({"role": "user", "content": pair["user_content"]})
    async with judge_sem:
        for attempt in range(3):
            try:
                resp = await client.chat.completions.create(
                    model=JUDGE_MODEL,
                    messages=messages,
                    extra_body={"reasoning": {"enabled": True, "effort": "high"}, "usage": {"include": True}},
                )
                cost = (resp.usage.model_extra or {}).get("cost")
                if cost is not None:
                    cost_total["usd"] += float(cost)
                    cost_total["calls"] += 1
                answer = (resp.choices[0].message.content or "").strip().strip(".").lower()
                if answer not in ("0", "1", "tie"):
                    print(f"unparseable answer {pair['paper_id']} bin={pair['bin']} mode={mode} (attempt {attempt + 1}/3): {answer!r}")
                    continue
                break
            except Exception as e:
                print(f"judge error {pair['paper_id']} bin={pair['bin']} mode={mode} (attempt {attempt + 1}/3): {e}")
                await asyncio.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f"judge failed for {pair['paper_id']} bin={pair['bin']} mode={mode} after 3 attempts")
    outcome = {"0": 1.0, "tie": 0.5, "1": 0.0}[answer]
    out_f.write(json.dumps({"paper_id": pair["paper_id"], "anchor_id": pair["anchor_id"], "bin": pair["bin"], "anchor_gt": pair["anchor_gt"], "mode": mode, "answer": answer, "outcome": outcome}) + "\n")
    out_f.flush()
    return outcome


async def main():
    print(json.dumps({"event": "batch_start", "n_papers": len(eval_pids), "model": JUDGE_MODEL}))
    pair_lists = await asyncio.gather(*(build_pairs(pid) for pid in eval_pids))
    print(json.dumps({"event": "pairs_built", "n_pairs": sum(len(pl) for pl in pair_lists)}))

    results = {}

    async def score_paper(pid, pairs, mode):
        print(json.dumps({"event": "sample_start", "paper_id": pid, "mode": mode}))
        outcomes = await asyncio.gather(*(judge(p, mode) for p in pairs))
        ratings = [p["anchor_gt"] * 100 for p in pairs]
        est = elo_estimate(ratings, list(outcomes)) / 100
        results[(pid, mode)] = est
        print(json.dumps({"event": "sample_done", "paper_id": pid, "mode": mode, "est": round(est, 3), "gt": gt_by_pid[pid], "wins": sum(outcomes), "cost_usd": round(cost_total["usd"], 4)}))

    await asyncio.gather(*(score_paper(pid, pl, mode) for pid, pl in zip(eval_pids, pair_lists) for mode in ("zeroshot", "fewshot")))
    out_f.close()

    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["paper_id", "gt_avg_score", "est_zeroshot", "est_fewshot"])
        for pid in eval_pids:
            w.writerow([pid, gt_by_pid[pid], results[(pid, "zeroshot")], results[(pid, "fewshot")]])

    gt = np.array([gt_by_pid[pid] for pid in eval_pids])
    for mode in ("zeroshot", "fewshot"):
        est = np.array([results[(pid, mode)] for pid in eval_pids])
        print(json.dumps({
            "event": "correlation", "mode": mode,
            "pearson": round(float(pearsonr(gt, est)[0]), 4),
            "spearman": round(float(spearmanr(gt, est)[0]), 4),
        }))
    print(json.dumps({"event": "batch_done", "total_cost_usd": round(cost_total["usd"], 4), "calls": cost_total["calls"]}))


asyncio.run(main())
