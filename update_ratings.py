import csv
import os
from pathlib import Path

import openreview
from dotenv import load_dotenv

load_dotenv()

RATINGS_FILE = Path("datasets/deepreview_13k_test_refetch/ratings.csv")
RESULTS_FILE = Path("results/test_mini_2025_refetch.csv")

PIDS = [
    "WNxlJJIEVj", "O9NQLOjrdu", "u0L7djBiRw", "3ANoEa7roV", "nlHEfTRo0b",
    "luS9zeDpeO", "KlV5CkNQkl", "FBDtqWXfuq", "mHv6wcBb0z", "sllU8vvsFF", "leJWwts8P9",
]


def fetch_scores(client, pid):
    replies = [r.to_json() if hasattr(r, "to_json") else r for r in client.get_all_notes(forum=pid)]
    scores = []
    for r in replies:
        if not any(inv.endswith("/-/Official_Review") for inv in r.get("invitations", [])):
            continue
        v = r.get("content", {}).get("rating", {}).get("value", "")
        if isinstance(v, str) and ":" in v:
            scores.append(int(v.split(":")[0].strip()))
        elif isinstance(v, (int, float)):
            scores.append(int(v))
    return sorted(scores)


client = openreview.api.OpenReviewClient(
    username=os.environ["OPENREVIEW_USERNAME"],
    password=os.environ["OPENREVIEW_PASSWORD"],
    baseurl="https://api2.openreview.net",
)
truth = {pid: fetch_scores(client, pid) for pid in PIDS}
for pid, s in truth.items():
    print(pid, s, round(sum(s) / len(s), 2))

# ── ratings.csv: 6 score columns. For papers with >6 reviewers, keep existing
#    6 genuine scores (avg already correct). For the rest, overwrite scores+avg. ──
rows = list(csv.reader(open(RATINGS_FILE, newline="")))
header = rows[0]
for row in rows[1:]:
    pid = row[0]
    if pid not in truth:
        continue
    s = truth[pid]
    if len(s) > 6:
        continue  # 6-col schema can't hold it; avg already correct
    avg = sum(s) / len(s)
    row[4] = f"{avg:.2f}"
    padded = [str(x) for x in s] + [""] * (6 - len(s))
    row[5:11] = padded
with open(RATINGS_FILE, "w", newline="") as f:
    csv.writer(f).writerows(rows)
print(f"wrote {RATINGS_FILE}")

# ── results file: gt_score_0..gt_score_6 (7 slots). Overwrite gt scores, avg,
#    and recompute match (pred_decision vs gt_binary; gt_binary unchanged). ──
rrows = list(csv.reader(open(RESULTS_FILE, newline="")))
rheader = rrows[0]
gt_cols = [rheader.index(f"gt_score_{i}") for i in range(7)]
avg_col = rheader.index("gt_avg_score")
pred_dec_col = rheader.index("pred_decision")
gt_bin_col = rheader.index("gt_binary")
match_col = rheader.index("match")
for row in rrows[1:]:
    pid = row[0]
    if pid not in truth:
        continue
    s = truth[pid]
    assert len(s) <= 7, f"{pid} has {len(s)} reviewers, exceeds 7 columns"
    avg = sum(s) / len(s)
    row[avg_col] = f"{avg:.2f}"
    padded = [f"{x:.1f}" for x in s] + [""] * (7 - len(s))
    for col, val in zip(gt_cols, padded):
        row[col] = val
    row[match_col] = "YES" if row[pred_dec_col] == row[gt_bin_col] else "NO"
with open(RESULTS_FILE, "w", newline="") as f:
    csv.writer(f).writerows(rrows)
print(f"wrote {RESULTS_FILE}")
