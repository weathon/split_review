import pandas as pd
from datasets import Dataset

folder = "results/2026_deepseek_train_balanced"
scores = pd.read_csv(f"{folder}/scores.csv").drop_duplicates("paper_id")

system_prompt = "Rewrite this review to be more aligned with real reviews on the severity of strengths and weaknesses, and give a better calibrated score. The original scores at the end of the review are kept for reference only."

reviewer_cols = [c for c in scores.columns if c.startswith("gt_score_")]

rows = []
skipped = []
for paper_id in scores["paper_id"]:
    path = f"{folder}/reviews/{paper_id}.md"
    try:
        with open(path) as f:
            review = f.read()
    except FileNotFoundError:
        skipped.append(paper_id)
        continue
    row = scores[scores["paper_id"] == paper_id].iloc[0]
    reviewers = [float(row[c]) for c in reviewer_cols if pd.notna(row[c])]
    rows.append({
        "review": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": review},
        ],
        "gt_scores": {"avg": float(row["gt_avg_score"]), "reviewers": reviewers},
    })

print(f"rows={len(rows)} skipped_no_review={len(skipped)}")

ds = Dataset.from_list(rows)
ds.push_to_hub("weathon/grpo_review")
