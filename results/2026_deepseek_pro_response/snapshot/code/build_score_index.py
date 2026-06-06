"""
One-shot: parse `- Scores:` line in each ../human_reviews/*.md, compute avg,
prepend `- Avg Score: X.XX` after the title line, and save score index pickle.

Idempotent: skips files already containing an `- Avg Score:` line.
"""
import os
import pickle
from paths import DATASETS_DIR

REVIEW_DIR = str(DATASETS_DIR / "deepreview_13k_calibration")
INDEX_PATH = str(DATASETS_DIR / "human_review_score_index_deepreview.pkl")


def parse_scores(line: str) -> list[float]:
    prefix = "- Scores:"
    body = line[len(prefix):].strip()
    out = []
    for tok in body.split(","):
        tok = tok.strip()
        if not tok:
            continue
        out.append(float(tok))
    return out


def main():
    score_index: dict[str, float] = {}
    updated = 0
    skipped = 0
    missing = 0

    for name in sorted(os.listdir(REVIEW_DIR)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(REVIEW_DIR, name)
        with open(path, "r", errors="replace") as f:
            text = f.read()

        lines = text.splitlines()
        score_line = next((ln for ln in lines if ln.startswith("- Scores:")), None)
        if score_line is None:
            missing += 1
            continue

        try:
            scores = parse_scores(score_line)
        except ValueError:
            missing += 1
            continue
        if not scores:
            missing += 1
            continue

        avg = sum(scores) / len(scores)
        score_index[name] = avg

        if any(ln.startswith("- Avg Score:") for ln in lines):
            skipped += 1
            continue

        # Insert `- Avg Score:` right before `- Decision:` (if present) else
        # right before `- Scores:`.
        new_lines: list[str] = []
        inserted = False
        avg_line = f"- Avg Score: {avg:.2f}"
        for ln in lines:
            if not inserted and (ln.startswith("- Decision:") or ln.startswith("- Scores:")):
                new_lines.append(avg_line)
                inserted = True
            new_lines.append(ln)
        if not inserted:
            new_lines.insert(0, avg_line)
        with open(path, "w") as f:
            f.write("\n".join(new_lines) + ("\n" if text.endswith("\n") else ""))
        updated += 1

    with open(INDEX_PATH, "wb") as f:
        pickle.dump(score_index, f)

    print(f"Index: {len(score_index)} files -> {INDEX_PATH}")
    print(f"  updated: {updated}")
    print(f"  already had Avg Score (skipped): {skipped}")
    print(f"  no parseable Scores line: {missing}")


if __name__ == "__main__":
    main()
