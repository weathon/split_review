import asyncio
import json
import os
import pickle
import random
import re
import sys

import numpy as np
import pandas as pd
import dotenv
from openai import AsyncOpenAI
from datasets import Dataset

dotenv.load_dotenv()

N_REVIEWS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
FULL_RUN = N_REVIEWS >= 300
RUNS_PER_PAIR = 3
JUDGE_CONCURRENCY = 30
EMBED_CONCURRENCY = 10
FOLDER = "results/2026_deepseek_train_balanced"
OUT_JSONL = "results/zto_samples.jsonl" if FULL_RUN else "results/zto_samples_test.jsonl"
HUB_REPO = "weathon/kto_review_2"
JUDGE_MODEL = "deepseek/deepseek-v4-flash"

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


def gt_answer_for(input_gt: float, anchor_gt: float) -> str:
    diff = input_gt - anchor_gt
    if abs(diff) < 1:
        return "tie"
    return "0" if diff > 0 else "1"


pids = [pid for pid in gt_by_pid if os.path.exists(f"{FOLDER}/reviews/{pid}.md")]
sampled = random.Random(42).sample(pids, min(N_REVIEWS, len(pids)))
print(json.dumps({"event": "batch_start", "n_reviews": len(sampled), "runs_per_pair": RUNS_PER_PAIR, "out": OUT_JSONL}))

embed_sem = asyncio.Semaphore(EMBED_CONCURRENCY)
judge_sem = asyncio.Semaphore(JUDGE_CONCURRENCY)
cost_total = {"usd": 0.0, "calls": 0}


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
    input_gt = gt_by_pid[pid]
    ai_review = strip_ai_review(raw)
    pairs = []
    for b in range(10):
        mask = (cal_bins == b) & (cal_files != f"{pid}.md")
        masked = np.where(mask, sims, -np.inf)
        idx = int(masked.argmax())
        anchor_fn = str(cal_files[idx])
        anchor_gt = float(cal_scores[idx])
        with open(f"datasets/deepreview_13k_calibration/{anchor_fn}", errors="replace") as f:
            anchor_review = strip_human_review(f.read())
        pairs.append({
            "paper_id": pid,
            "anchor_id": anchor_fn,
            "bin": b,
            "input_gt": input_gt,
            "anchor_gt": anchor_gt,
            "similarity": float(sims[idx]),
            "gt_answer": gt_answer_for(input_gt, anchor_gt),
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Review 1:\n\n{ai_review}\n\n---\n\nReview 2:\n\n{anchor_review}"},
            ],
        })
    print(json.dumps({"event": "sample_start", "paper_id": pid, "n_pairs": len(pairs)}))
    return pairs


async def judge(pair: dict, run_idx: int) -> dict | None:
    async with judge_sem:
        for attempt in range(3):
            try:
                resp = await client.chat.completions.create(
                    model=JUDGE_MODEL,
                    messages=pair["prompt"],
                    extra_body={"reasoning": {"enabled": True, "effort": "high"}, "usage": {"include": True}},
                )
                msg = resp.choices[0].message
                reasoning = msg.model_extra["reasoning"]
                answer_raw = (msg.content or "").strip()
                break
            except Exception as e:
                print(f"judge error {pair['paper_id']} bin={pair['bin']} run={run_idx} (attempt {attempt + 1}/3): {e}")
                await asyncio.sleep(5 * (attempt + 1))
        else:
            print(json.dumps({"event": "sample_skipped", "paper_id": pair["paper_id"], "anchor_id": pair["anchor_id"], "run_idx": run_idx}))
            return None
    cost = (resp.usage.model_extra or {}).get("cost")
    if cost is not None:
        cost_total["usd"] += float(cost)
        cost_total["calls"] += 1
    answer = answer_raw.lower().strip(".")
    label = answer == pair["gt_answer"]
    return {
        "prompt": pair["prompt"],
        "completion": [{"role": "assistant", "content": f"<think>\n{reasoning}\n</think>\n\n{answer_raw}"}],
        "label": bool(label),
        "reasoning": reasoning,
        "answer": answer_raw,
        "gt_answer": pair["gt_answer"],
        "paper_id": pair["paper_id"],
        "anchor_id": pair["anchor_id"],
        "bin": pair["bin"],
        "input_gt": pair["input_gt"],
        "anchor_gt": pair["anchor_gt"],
        "similarity": pair["similarity"],
        "run_idx": run_idx,
    }


async def main():
    finished = set()
    if os.path.exists(OUT_JSONL):
        with open(OUT_JSONL) as f:
            for line in f:
                r = json.loads(line)
                finished.add((r["paper_id"], r["bin"], r["run_idx"]))
        print(json.dumps({"event": "resume", "n_finished": len(finished)}))

    pair_lists = await asyncio.gather(*(build_pairs(pid) for pid in sampled))
    all_pairs = [p for pl in pair_lists for p in pl]
    print(json.dumps({"event": "pairs_built", "n_pairs": len(all_pairs)}))

    out_f = open(OUT_JSONL, "a")
    rows = []
    done = {"n": 0}
    todo = [(p, k) for p in all_pairs for k in range(RUNS_PER_PAIR) if (p["paper_id"], p["bin"], k) not in finished]
    total = len(todo)

    async def judge_and_save(pair, run_idx):
        row = await judge(pair, run_idx)
        done["n"] += 1
        if row is None:
            return
        out_f.write(json.dumps(row) + "\n")
        out_f.flush()
        rows.append(row)
        print(json.dumps({"event": "sample_done", "i": done["n"], "total": total, "paper_id": row["paper_id"], "bin": row["bin"], "run_idx": run_idx, "answer": row["answer"][:20], "gt": row["gt_answer"], "label": row["label"], "cost_usd": round(cost_total["usd"], 4)}))

    await asyncio.gather(*(judge_and_save(p, k) for p, k in todo))
    out_f.close()

    with open(OUT_JSONL) as f:
        rows = [json.loads(line) for line in f]
    n_pos = sum(r["label"] for r in rows)
    print(json.dumps({"event": "batch_done", "n_samples": len(rows), "n_positive": n_pos, "n_negative": len(rows) - n_pos, "total_cost_usd": round(cost_total["usd"], 4)}))

    ds = Dataset.from_list(rows)
    if FULL_RUN:
        ds.push_to_hub(HUB_REPO)
        print(f"pushed {len(ds)} samples to {HUB_REPO}")
    else:
        print(f"test run: not pushing to hub, samples in {OUT_JSONL}")


asyncio.run(main())
