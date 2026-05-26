import csv
import json
import shutil
from pathlib import Path

from datasets import Dataset


OUT_DIR = Path("datasets/iclr2026_model_reviews_hf")
SKIPPED_CSV = Path("datasets/iclr2026_model_reviews_hf_skipped.csv")
PAPER_DIR = Path("/home/wg25r/review_agent/iclr2026_new/papers")
HUMAN_REVIEW_DIR = Path("/home/wg25r/review_agent/iclr2026_new/human_reviews")
ALL_NOTES_PATHS = [
    Path("/home/wg25r/review_agent/iclr2026_new/all_notes.json"),
    Path("/home/wg25r/review_agent/iclr2026_unbalanced/all_notes.json"),
    Path("/home/wg25r/review_agent/iclr2026_balanced/all_notes.json"),
]

RUNS = [
    {
        "review_model": "deepseek_flash",
        "scores_csv": Path("results/sweep_v1_905prompts/scores.csv"),
        "review_dir": Path("results/sweep_v1_905prompts/reviews"),
    },
    {
        "review_model": "opus",
        "scores_csv": Path("results/2026_opus.csv"),
        "review_dir": Path("results/2026_opus"),
    },
]


def format_human_reviews(reviews):
    sections = []
    for i, review in enumerate(reviews, start=1):
        parts = [f"## Human Reviewer {i}"]
        for key in [
            "summary",
            "strengths",
            "weaknesses",
            "questions",
            "limitations",
            "soundness",
            "presentation",
            "contribution",
            "rating",
            "confidence",
        ]:
            value = review.get(key)
            if value not in ("", None):
                parts.append(f"### {key.replace('_', ' ').title()}\n{value}")
        sections.append("\n\n".join(parts))
    return "\n\n---\n\n".join(sections).strip() + "\n"


def load_human_review_index():
    by_id = {}
    for path in ALL_NOTES_PATHS:
        notes = json.loads(path.read_text(encoding="utf-8"))
        for row in notes:
            by_id.setdefault(row["paper_id"], row)
    return by_id


def read_human_review(paper_id, notes_by_id):
    md_path = HUMAN_REVIEW_DIR / f"{paper_id}.md"
    if md_path.exists():
        return md_path.read_text(encoding="utf-8")
    note = notes_by_id[paper_id]
    if "human_reviews" not in note:
        return None
    return format_human_reviews(note["human_reviews"])


def gt_scores(row):
    scores = []
    for i in range(7):
        value = row.get(f"gt_score_{i}", "").strip()
        if value:
            scores.append(float(value))
    return scores


def build_rows():
    notes_by_id = load_human_review_index()
    rows = []
    skipped = []
    seen = set()
    for run in RUNS:
        with run["scores_csv"].open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                paper_id = row["paper_id"].strip()
                key = (run["review_model"], paper_id)
                if key in seen:
                    print(f"skip duplicate {run['review_model']} {paper_id}")
                    continue
                seen.add(key)

                paper_path = PAPER_DIR / f"{paper_id}.txt"
                review_path = run["review_dir"] / f"{paper_id}.md"
                if not paper_path.exists():
                    raise FileNotFoundError(paper_path)
                if not review_path.exists():
                    raise FileNotFoundError(review_path)
                if paper_id not in notes_by_id and not (HUMAN_REVIEW_DIR / f"{paper_id}.md").exists():
                    raise KeyError(f"missing human review for {paper_id}")
                human_review = read_human_review(paper_id, notes_by_id)
                if human_review is None:
                    skipped.append({
                        "review_model": run["review_model"],
                        "paper_id": paper_id,
                        "reason": "missing human review text",
                    })
                    print(f"skip missing human review {run['review_model']} {paper_id}")
                    continue

                rows.append({
                    "paper_id": paper_id,
                    "paper_content": paper_path.read_text(encoding="utf-8"),
                    "paper_review": review_path.read_text(encoding="utf-8"),
                    "review_model": run["review_model"],
                    "pred_score": float(row["pred_score"]),
                    "gt_avg_score": float(row["gt_avg_score"]),
                    "gt_scores": gt_scores(row),
                    "pred_decision": row["pred_decision"],
                    "gt_decision": row["gt_decision"],
                    "human_review": human_review,
                })
    return rows, skipped


rows, skipped = build_rows()
if OUT_DIR.exists():
    shutil.rmtree(OUT_DIR)
dataset = Dataset.from_list(rows)
dataset.save_to_disk(str(OUT_DIR))
with SKIPPED_CSV.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["review_model", "paper_id", "reason"])
    writer.writeheader()
    writer.writerows(skipped)
print(f"wrote {len(dataset)} rows to {OUT_DIR}")
print(f"skipped {len(skipped)} rows -> {SKIPPED_CSV}")
print(dataset)
