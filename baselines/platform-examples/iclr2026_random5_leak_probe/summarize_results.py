from pathlib import Path
import csv


root = Path("/home/wg25r/split_review/baselines/platform-examples/iclr2026_random5_leak_probe")
rows = []
with open(root / "selected.csv", newline="", encoding="utf-8") as f:
    selected = list(csv.DictReader(f))

for row in selected:
    paper_id = row["paper_id"]
    raw_path = root / "raw_original_submit" / "output" / f"{paper_id}__ICLR_main_2026_2.md"
    edited_path = root / "edited_submit" / "output" / f"{paper_id}__ICLR_main_2026_2.md"
    out = dict(row)
    for prefix, path in [("raw", raw_path), ("edited", edited_path)]:
        meta = {}
        for line in path.read_text(encoding="utf-8").splitlines()[1:]:
            if line == "---":
                break
            if ": " in line:
                key, value = line.split(": ", 1)
                meta[key] = value
        out[f"{prefix}_status"] = meta["status"]
        out[f"{prefix}_main_score_norm"] = meta["main_score_norm"]
        out[f"{prefix}_paper"] = meta["paper"]
        out[f"{prefix}_job_id"] = meta["job_id"]
    rows.append(out)

fieldnames = [
    "paper_id",
    "avg_score",
    "decision",
    "scores",
    "title",
    "new_title",
    "raw_main_score_norm",
    "edited_main_score_norm",
    "raw_status",
    "edited_status",
    "raw_job_id",
    "edited_job_id",
]
with open(root / "summary.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow({key: row[key] for key in fieldnames})

for row in rows:
    print(
        row["paper_id"],
        row["avg_score"],
        row["decision"],
        row["raw_main_score_norm"],
        row["edited_main_score_norm"],
        row["title"],
    )
