import json
from collections import defaultdict
from pathlib import Path

OUT_DIR = Path(__file__).parent / "hivemind_outputs"
SOURCES = [
    OUT_DIR / "overlap_results.jsonl",
    OUT_DIR / "human_overlap_results.jsonl",
]
OUT_MD = Path(__file__).parent / "overlap_results.md"


def stats(values):
    vs = sorted(values)
    n = len(vs)
    mean = sum(vs) / n
    median = vs[n // 2] if n % 2 else (vs[n // 2 - 1] + vs[n // 2]) / 2
    return n, mean, median


def main():
    rates = defaultdict(list)
    items = defaultdict(list)
    for src in SOURCES:
        if not src.exists():
            print(f"missing: {src}")
            continue
        with open(src) as f:
            for line in f:
                r = json.loads(line)
                m = r["method"]
                items[m].append(r["n_items_review1"])
                if r["overlap_rate"] is not None:
                    rates[m].append(r["overlap_rate"])

    rows = []
    for m in sorted(rates, key=lambda k: stats(rates[k])[1]):
        n, mean, median = stats(rates[m])
        mean_items = sum(items[m]) / len(items[m])
        rows.append((m, n, mean, median, mean_items))

    lines = [
        "# Weakness Overlap Results",
        "",
        "Each row reports the rate at which weakness items in review-of-paper-A reappear as similar items in review-of-paper-B, with both reviews written by the same agent (or same-style human reviewer). Lower = more paper-specific, less templated.",
        "",
        "| method | n_pairs | mean_overlap | median_overlap | mean_items |",
        "|---|---:|---:|---:|---:|",
    ]
    for m, n, mean, median, mean_items in rows:
        lines.append(f"| {m} | {n} | {mean:.3f} | {median:.3f} | {mean_items:.2f} |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines))
    print(f"wrote {OUT_MD}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
