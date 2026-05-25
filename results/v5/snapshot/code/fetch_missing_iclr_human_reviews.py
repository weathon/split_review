import csv
import sys
from pathlib import Path


REVIEW_AGENT_DIR = Path("/home/wg25r/review_agent")
SKIPPED_CSV = Path("datasets/iclr2026_model_reviews_hf_skipped.csv")
OUT_DIR = REVIEW_AGENT_DIR / "iclr2026_new" / "human_reviews"

sys.path.insert(0, str(REVIEW_AGENT_DIR))

from fetch_iclr import fetch_human_reviews, format_human_reviews, get_or_client


paper_ids = []
with SKIPPED_CSV.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        pid = row["paper_id"]
        if pid not in paper_ids:
            paper_ids.append(pid)

OUT_DIR.mkdir(parents=True, exist_ok=True)
client = get_or_client()

saved = 0
already_done = 0
empty = 0
for index, paper_id in enumerate(paper_ids, start=1):
    out_path = OUT_DIR / f"{paper_id}.md"
    if out_path.exists() and out_path.stat().st_size > 0:
        already_done += 1
        print(f"[{index}/{len(paper_ids)}] exists {paper_id}")
        continue

    reviews = fetch_human_reviews(client, paper_id)
    if not reviews:
        empty += 1
        print(f"[{index}/{len(paper_ids)}] no reviews {paper_id}")
        continue

    out_path.write_text(format_human_reviews(reviews).strip() + "\n", encoding="utf-8")
    saved += 1
    print(f"[{index}/{len(paper_ids)}] saved {paper_id} ({len(reviews)} reviews)")

print(f"saved={saved} already_done={already_done} empty={empty} total={len(paper_ids)}")
