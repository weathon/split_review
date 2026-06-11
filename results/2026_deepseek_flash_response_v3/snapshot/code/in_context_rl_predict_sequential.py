import os
import re
import csv
import json
import argparse
from pathlib import Path

import pandas as pd
import dotenv
from openai import OpenAI

dotenv.load_dotenv("../.env")

REVIEW_DIR = Path("../results/test_mini_wo_search")
RATINGS_CSV = Path("../datasets/deepreview_13k_test_mini/ratings.csv")


def load_review(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"MY FINAL SCORE:\s*<score>[\d.]+</score>", "MY FINAL SCORE: <score>[HIDDEN]</score>", text)
    text = re.sub(r"MY FINAL DECISION:\s*<decision>[^<]+</decision>", "MY FINAL DECISION: <decision>[HIDDEN]</decision>", text)
    return text


def parse_score(text: str) -> float:
    m = re.search(r"<score>\s*([\d.]+)\s*</score>", text)
    if not m:
        return -100.0
    return float(m.group(1))


def parse_decision(text: str, score: float) -> str:
    m = re.search(r"<decision>\s*(Accept|Reject)\s*</decision>", text, re.IGNORECASE)
    if m:
        return m.group(1).capitalize()
    if score == -100.0:
        return "Error"
    return "Accept" if score >= 6.0 else "Reject"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, default="../results/in_context_rl_checkpoint.json")
    parser.add_argument("--output_csv", type=str, default="../results/in_context_rl_test_mini_sequential.csv")
    parser.add_argument("--model", type=str, default=None, help="override model from checkpoint")
    args = parser.parse_args()

    with open(args.checkpoint, "r") as f:
        ckpt = json.load(f)
    prefix_messages = ckpt["messages"]
    model = args.model or ckpt["model"]
    print(f"Loaded checkpoint with {len(prefix_messages)} prefix messages, model={model}")

    df = pd.read_csv(RATINGS_CSV).drop_duplicates(subset=["paper_id"]).set_index("paper_id")
    review_files = sorted(REVIEW_DIR.glob("*.md"))
    print(f"Predicting on {len(review_files)} papers sequentially with accumulating context")

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

    out_path = Path(args.output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as f:
        csv.writer(f).writerow([
            "paper_id", "pred_score", "pred_decision",
            "gt_avg_score", "gt_decision", "gt_binary", "match",
            "cost", "sdk_savings",
            "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6",
        ])

    running_messages = list(prefix_messages)
    appended_chars = 0
    MAX_APPENDED_CHARS = 300_000

    for idx, rf in enumerate(review_files, 1):
        pid = rf.stem
        if pid not in df.index:
            print(f"[{idx}/{len(review_files)}] {pid} not in ratings, skipping")
            continue
        row = df.loc[pid]
        gt_avg = float(row["avg_score"])
        gt_decision = str(row["decision"]).strip()
        gt_binary = str(row["gt_binary"]).strip()

        review = load_review(rf)
        user_msg = (
            f"Test paper (id={pid}).\n\n"
            f"Assisted review:\n\n{review}\n\n"
            "Predict the ground-truth average human score for this paper.\n\n"
            "IMPORTANT TASK NOTE: You are scoring a sequence of test papers in this same conversation. "
            "Your previous predictions (without ground truth) are visible above. "
            "Use them as a calibration reference so your scores are internally consistent across papers: "
            "a paper you judge stronger than a previous one should receive a higher score, and a weaker one a lower score. "
            "Maintain a stable, consistent scoring scale across the whole sequence rather than rescoring each paper in isolation."
        )
        messages = running_messages + [{"role": "user", "content": user_msg}]

        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                extra_body={"reasoning": {"enabled": False}, "provider": {"only": ["deepseek"]}},
            )
            out = resp.choices[0].message.content
            pred = parse_score(out)
            pred_decision = parse_decision(out, pred)
        except Exception as e:
            print(f"[{idx}/{len(review_files)}] {pid} API error: {e}")
            pred = -100.0
            pred_decision = "Error"
            out = None

        match_str = "N/A" if pred_decision in ("Error", "N/A") else ("YES" if pred_decision == gt_binary else "NO")
        print(f"[{idx}/{len(review_files)}] {pid} pred={pred} gt={gt_avg:.2f} match={match_str}")

        if out is not None and appended_chars < MAX_APPENDED_CHARS:
            running_messages.append({"role": "user", "content": user_msg})
            running_messages.append({"role": "assistant", "content": out})
            appended_chars += len(user_msg) + len(out)

        gt_scores = [row.get(f"score_{k}") for k in range(7)]
        gt_scores_padded = ["" if pd.isna(s) else f"{float(s):.1f}" for s in gt_scores]

        with open(out_path, "a", newline="") as f:
            csv.writer(f).writerow([
                pid, pred, pred_decision, f"{gt_avg:.2f}", gt_decision, gt_binary, match_str,
                "0.0000", "0.0000", *gt_scores_padded,
            ])

    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
