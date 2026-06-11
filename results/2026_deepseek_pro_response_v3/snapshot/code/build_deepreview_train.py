"""
Build datasets/deepreview_13k_train from the `train` split of
WestlakeNLP/DeepReview-13K, using the same on-disk structure as
datasets/deepreview_13k_test:

  ../deepreview_13k_train/
      papers/<paper_id>.txt        (raw paper content)
      human_reviews/<paper_id>.md  (formatted human reviews)
      ratings.csv                  (paper_id,title,decision,gt_binary,
                                    avg_score,score_0..score_5)
"""

import csv
import json
from pathlib import Path

import tqdm
from datasets import load_dataset

from paths import DATASETS_DIR
from build_deepreview import (
    coerce_scores,
    extract_abstract,
    extract_title,
    first_user_content,
    format_human_reviews_md,
    gt_binary_from_decision,
)

TRAIN_DIR = (DATASETS_DIR / "deepreview_13k_train").resolve()


def write_train(train_split):
    papers_dir = TRAIN_DIR / "papers"
    reviews_dir = TRAIN_DIR / "human_reviews"
    papers_dir.mkdir(parents=True, exist_ok=True)
    reviews_dir.mkdir(parents=True, exist_ok=True)
    ratings_path = TRAIN_DIR / "ratings.csv"

    print(f"Writing train set to {TRAIN_DIR} ({len(train_split)} papers)...")
    with open(ratings_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "paper_id", "title", "decision", "gt_binary", "avg_score",
            "score_0", "score_1", "score_2", "score_3", "score_4", "score_5",
        ])
        written = 0
        for ex in tqdm.tqdm(train_split):
            pid = ex["id"]
            scores = coerce_scores(ex["rating"])
            if not scores:
                continue
            avg = sum(scores) / len(scores)
            user_content = first_user_content(ex["inputs"])
            title = extract_title(user_content) or pid
            try:
                rc = json.loads(ex["reviewer_comments"]) if ex["reviewer_comments"] else []
            except json.JSONDecodeError:
                rc = []

            (papers_dir / f"{pid}.txt").write_text(user_content, encoding="utf-8")

            review_md_lines = [
                f"# {title}",
                "",
                f"- Decision: {ex['decision'] or ''}",
                f"- Scores: {', '.join(str(s) for s in scores)}",
                "",
                "## Abstract",
                extract_abstract(user_content),
                "",
                "## Human Reviews",
                "",
                format_human_reviews_md(rc),
            ]
            (reviews_dir / f"{pid}.md").write_text(
                "\n".join(review_md_lines).strip() + "\n", encoding="utf-8"
            )

            scores_padded = [str(s) for s in scores] + [""] * (6 - len(scores))
            w.writerow([
                pid, title, ex["decision"] or "", gt_binary_from_decision(ex["decision"] or ""),
                f"{avg:.2f}", *scores_padded[:6],
            ])
            written += 1
    print(f"  wrote {written} train paper+review pairs and ratings.csv")


def main():
    print("Loading WestlakeNLP/DeepReview-13K...")
    ds = load_dataset("WestlakeNLP/DeepReview-13K")
    print(ds)
    write_train(ds["train"])
    print("Done.")


if __name__ == "__main__":
    main()
