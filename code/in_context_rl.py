import os
import re
import json
import random
import argparse
from pathlib import Path

import pandas as pd
import dotenv
from openai import OpenAI

dotenv.load_dotenv("../.env")

REVIEW_DIR = Path("../results/fresh_cal")
RATINGS_CSV = Path("../datasets/deepreview_13k_train/ratings.csv")

SYSTEM_PROMPT = """You are doing in-context reinforcement learning to learn how to score papers from assisted reviews.

Task:
- On every turn you receive a paper review written by an assistant reviewer.
- You must predict the ground-truth average human score for the paper (a number between 1 and 10, on a 0.5 grid).
- The review itself contains an assistant-predicted score at the very bottom; that prediction may be biased. Use the review CONTENT, not the assistant's score, as your primary signal, but you may use the assistant's score as one input.
- After each prediction we will tell you the ground-truth score and the signed error (predicted - ground_truth). Positive error => you over-predicted; negative error => you under-predicted.
- Use the running history of signed errors to recalibrate your future predictions. The goal is for the absolute error to improve over time.

Reasoning mode:
- Thinking mode is DISABLED at the API level. You must still reason explicitly inside your answer, but do it in a visible <reasoning>...</reasoning> XML block before your final score.
- After the <reasoning> block, output exactly one <score>X.X</score> tag with the predicted score. Nothing else after it.

Output format (strict):
<reasoning>
... your step-by-step calibration reasoning, referencing prior signed errors and the current review ...
</reasoning>
<score>NUMBER</score>
"""

def load_review(paper_id: str) -> str:
    text = (REVIEW_DIR / f"{paper_id}.md").read_text(encoding="utf-8")
    text = re.sub(r"MY FINAL SCORE:\s*<score>[\d.]+</score>", "MY FINAL SCORE: <score>[HIDDEN]</score>", text)
    text = re.sub(r"MY FINAL DECISION:\s*<decision>[^<]+</decision>", "MY FINAL DECISION: <decision>[HIDDEN]</decision>", text)
    return text


def parse_score(text: str) -> float:
    m = re.search(r"<score>\s*([\d.]+)\s*</score>", text)
    if not m:
        raise ValueError(f"no <score> tag in model output:\n{text[:500]}")
    return float(m.group(1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_steps", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--model", type=str, default="deepseek/deepseek-v4-flash")
    parser.add_argument("--checkpoint", type=str, default="../results/in_context_rl_checkpoint.json")
    args = parser.parse_args()

    df = pd.read_csv(RATINGS_CSV).drop_duplicates(subset=["paper_id"]).set_index("paper_id")

    rng = random.Random(args.seed)
    all_ids = sorted(f.stem for f in REVIEW_DIR.glob("*.md") if f.stem in df.index)

    strata = {}
    for pid in all_ids:
        bucket = round(float(df.loc[pid, "avg_score"]) * 2) / 2
        strata.setdefault(bucket, []).append(pid)

    buckets = sorted(strata.keys())
    per_bucket = args.n_steps // len(buckets)
    remainder = args.n_steps - per_bucket * len(buckets)
    paper_ids = []
    for b in buckets:
        ids = strata[b]
        k = min(per_bucket, len(ids))
        paper_ids.extend(rng.sample(ids, k))
    pool = [pid for b in buckets for pid in strata[b] if pid not in set(paper_ids)]
    if remainder and pool:
        paper_ids.extend(rng.sample(pool, min(remainder, len(pool))))
    rng.shuffle(paper_ids)

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    history = []

    for i, pid in enumerate(paper_ids, 1):
        review = load_review(pid)
        gt = float(df.loc[pid, "avg_score"])

        user_msg = f"Paper {i}/{args.n_steps} (id={pid}).\n\nAssisted review:\n\n{review}\n\nPredict the ground-truth average human score for this paper."
        messages.append({"role": "user", "content": user_msg})

        resp = client.chat.completions.create(
            model=args.model,
            messages=messages,
            extra_body={"reasoning": {"enabled": False}, "provider": {"only": ["deepseek"]}},
        )
        out = resp.choices[0].message.content
        pred = parse_score(out)
        signed_err = pred - gt
        history.append({"paper_id": pid, "pred": pred, "gt": gt, "signed_err": signed_err, "abs_err": abs(signed_err)})

        print(f"[{i}/{args.n_steps}] {pid} pred={pred} gt={gt:.2f} signed_err={signed_err:+.2f} abs_err={abs(signed_err):.2f}")

        messages.append({"role": "assistant", "content": out})
        messages.append({
            "role": "user",
            "content": f"Ground-truth score for paper {i} (id={pid}) was {gt:.2f}. Your signed error (pred - gt) was {signed_err:+.2f}. Use this to recalibrate future predictions.",
        })

    print("\n=== Summary ===")
    for h in history:
        print(f"  {h['paper_id']}: pred={h['pred']} gt={h['gt']:.2f} signed={h['signed_err']:+.2f} abs={h['abs_err']:.2f}")

    abs_errs = [h["abs_err"] for h in history]
    n = len(abs_errs)
    half = n // 2
    first_mae = sum(abs_errs[:half]) / half if half else float("nan")
    second_mae = sum(abs_errs[half:]) / (n - half) if (n - half) else float("nan")
    overall_mae = sum(abs_errs) / n
    print(f"\nMAE overall: {overall_mae:.3f}")
    print(f"MAE first half (1..{half}): {first_mae:.3f}")
    print(f"MAE second half ({half+1}..{n}): {second_mae:.3f}")
    print(f"Improvement (first - second): {first_mae - second_mae:+.3f}  (positive => improved)")

    ckpt_path = Path(args.checkpoint)
    ckpt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(ckpt_path, "w") as f:
        json.dump({
            "model": args.model,
            "n_steps": args.n_steps,
            "seed": args.seed,
            "system_prompt": SYSTEM_PROMPT,
            "messages": messages,
            "history": history,
        }, f, indent=2)
    print(f"\nSaved checkpoint to {ckpt_path}")


if __name__ == "__main__":
    main()
