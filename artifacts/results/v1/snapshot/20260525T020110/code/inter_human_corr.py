"""Inter-human (reviewer-to-reviewer) correlation for ratings.csv.

Uses the same baselines as code/metric.py (one_vs_rest_baseline and
split_half_baseline) but adapts the deepreview ratings.csv schema:
  score_0..score_5  -> gt_score_0..gt_score_5
  avg_score         -> gt_avg_score
  decision          -> gt_binary (already present)
"""
import sys
import pandas as pd

from metric import one_vs_rest_baseline, split_half_baseline


def main(path: str) -> None:
    df = pd.read_csv(path)
    rename = {f"score_{i}": f"gt_score_{i}" for i in range(6) if f"score_{i}" in df.columns}
    rename["avg_score"] = "gt_avg_score"
    df = df.rename(columns=rename)
    gt_score_cols = [c for c in df.columns if c.startswith("gt_score_")]

    if "gt_binary" not in df.columns:
        raise KeyError("ratings.csv must contain 'gt_binary' column")

    print(f"Papers: {len(df)}")
    print(f"GT score cols: {gt_score_cols}")
    print("─" * 60)

    ovr = one_vs_rest_baseline(df, gt_score_cols)
    if ovr is None:
        raise RuntimeError("one_vs_rest_baseline returned None — not enough multi-reviewer papers")
    print(f"One-vs-rest (mean of other reviewers vs held-out reviewer):")
    print(f"  n_papers : {ovr['n_papers']}")
    print(f"  n_pairs  : {ovr['n_pairs']}")
    print(f"  Spearman : {ovr['spearman']:.4f}")
    print(f"  Pearson  : {ovr['pearson']:.4f}")
    print(f"  MAE      : {ovr['mae']:.4f}")
    print("─" * 60)

    sh = split_half_baseline(df, gt_score_cols)
    if sh is None:
        raise RuntimeError("split_half_baseline returned None — not enough multi-reviewer papers")
    print(f"Split-half (mean of subgroup A vs mean of subgroup B):")
    print(f"  n_pairs  : {sh['n_pairs']}")
    print(f"  Spearman : {sh['spearman']:.4f}")
    print(f"  Pearson  : {sh['pearson']:.4f}")
    print(f"  MAE      : {sh['mae']:.4f}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "datasets/deepreview_13k_test/ratings.csv"
    main(path)
