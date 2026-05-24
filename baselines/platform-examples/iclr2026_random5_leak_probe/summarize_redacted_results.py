from pathlib import Path
import csv


root = Path("/home/wg25r/split_review/baselines/platform-examples/iclr2026_random5_leak_probe")
selected = list(csv.DictReader(open(root / "selected.csv", newline="", encoding="utf-8")))

rows = []
for row in selected:
    paper_id = row["paper_id"]
    out = dict(row)
    for prefix, path in [
        ("raw", root / "raw_original_submit" / "output" / f"{paper_id}__ICLR_main_2026_2.md"),
        ("redacted", root / "redacted_original_submit" / "output" / f"{paper_id}__ICLR_main_2026_2.md"),
    ]:
        meta = {}
        for line in path.read_text(encoding="utf-8").splitlines()[1:]:
            if line == "---":
                break
            if ": " in line:
                key, value = line.split(": ", 1)
                meta[key] = value
        out[f"{prefix}_status"] = meta["status"]
        out[f"{prefix}_main_score_norm"] = meta["main_score_norm"]
        out[f"{prefix}_desk_reject"] = meta["desk_reject"]
        out[f"{prefix}_paper"] = meta["paper"]
        out[f"{prefix}_job_id"] = meta["job_id"]
    rows.append(out)

fieldnames = [
    "paper_id",
    "avg_score",
    "decision",
    "scores",
    "raw_main_score_norm",
    "redacted_main_score_norm",
    "raw_desk_reject",
    "redacted_desk_reject",
    "title",
    "new_title",
    "raw_job_id",
    "redacted_job_id",
]
with open(root / "summary_redacted.csv", "w", newline="", encoding="utf-8") as f:
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
        row["redacted_main_score_norm"],
        row["raw_desk_reject"],
        row["redacted_desk_reject"],
    )
