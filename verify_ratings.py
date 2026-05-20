import csv
import os
from pathlib import Path

import openreview
from dotenv import load_dotenv

load_dotenv()

RATINGS_FILE = Path("datasets/deepreview_13k_test_refetch/ratings.csv")


def get_client():
    return openreview.api.OpenReviewClient(
        username=os.environ["OPENREVIEW_USERNAME"],
        password=os.environ["OPENREVIEW_PASSWORD"],
        baseurl="https://api2.openreview.net",
    )


def parse_scores(replies):
    """Same logic as fetch_iclr.parse_note: pull rating ints from Official_Review replies."""
    scores = []
    for reply in replies:
        invitations = reply.get("invitations", [])
        if not any(inv.endswith("/-/Official_Review") for inv in invitations):
            continue
        rc = reply.get("content", {})
        rating_val = rc.get("rating", {}).get("value", "")
        if isinstance(rating_val, str) and ":" in rating_val:
            scores.append(int(rating_val.split(":")[0].strip()))
        elif isinstance(rating_val, (int, float)):
            scores.append(int(rating_val))
    return scores


def main():
    rows = list(csv.DictReader(open(RATINGS_FILE, newline="")))
    print(f"{len(rows)} papers in ratings.csv")

    client = get_client()
    mismatches = []
    errors = []

    for i, row in enumerate(rows):
        pid = row["paper_id"]
        try:
            replies = client.get_all_notes(forum=pid)
            replies = [r.to_json() if hasattr(r, "to_json") else r for r in replies]
        except Exception as e:
            errors.append((pid, str(e)))
            print(f"[{i}] {pid} FETCH ERROR: {e}")
            continue

        fetched = sorted(parse_scores(replies))

        csv_scores = []
        for k in ["score_0", "score_1", "score_2", "score_3", "score_4", "score_5"]:
            v = row[k].strip()
            if v != "":
                csv_scores.append(int(float(v)))
        csv_scores = sorted(csv_scores)

        csv_avg = float(row["avg_score"])
        fetched_avg = sum(fetched) / len(fetched) if fetched else None

        ok = (fetched == csv_scores) and (
            fetched_avg is not None and abs(fetched_avg - csv_avg) < 0.01
        )
        if not ok:
            mismatches.append((pid, csv_scores, fetched, csv_avg, fetched_avg))
            print(f"[{i}] {pid} MISMATCH csv={csv_scores}(avg {csv_avg}) fetched={fetched}(avg {fetched_avg})")

    print("\n" + "=" * 60)
    print(f"Total: {len(rows)}  OK: {len(rows)-len(mismatches)-len(errors)}  "
          f"Mismatch: {len(mismatches)}  Errors: {len(errors)}")
    if mismatches:
        print("\nMISMATCHES:")
        for pid, c, f, ca, fa in mismatches:
            print(f"  {pid}: csv={c}(avg {ca})  fetched={f}(avg {fa})")
    if errors:
        print("\nERRORS:")
        for pid, e in errors:
            print(f"  {pid}: {e}")


if __name__ == "__main__":
    main()
