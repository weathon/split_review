import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, auc, f1_score
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from itertools import combinations
import sys

SCALE = [1, 3, 5, 6, 8, 10]
# SCALE = [0, 2, 4, 6, 8, 10]

def round_to_scale(x):
    return min(SCALE, key=lambda v: abs(v - x))


def linear_regression_with_ci(x, y, confidence=0.95):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    fit = stats.linregress(x, y)
    n = len(x)
    t_crit = stats.t.ppf((1 + confidence) / 2, n - 2)
    slope_ci = (
        float(fit.slope - t_crit * fit.stderr),
        float(fit.slope + t_crit * fit.stderr),
    )
    intercept_ci = (
        float(fit.intercept - t_crit * fit.intercept_stderr),
        float(fit.intercept + t_crit * fit.intercept_stderr),
    )

    x_mean = np.mean(x)
    ssx = np.sum((x - x_mean) ** 2)
    y_hat = fit.intercept + fit.slope * x
    residual_std = np.sqrt(np.sum((y - y_hat) ** 2) / (n - 2))

    def mean_ci(xs):
        xs = np.asarray(xs, dtype=float)
        se_mean = residual_std * np.sqrt((1 / n) + ((xs - x_mean) ** 2) / ssx)
        center = fit.intercept + fit.slope * xs
        delta = t_crit * se_mean
        return center, center - delta, center + delta

    return {
        "slope": float(fit.slope),
        "intercept": float(fit.intercept),
        "rvalue": float(fit.rvalue),
        "pvalue": float(fit.pvalue),
        "stderr": float(fit.stderr),
        "intercept_stderr": float(fit.intercept_stderr),
        "slope_ci": slope_ci,
        "intercept_ci": intercept_ci,
        "mean_ci": mean_ci,
    }


def spearman_ci(r, n, confidence=0.95):
    """Fisher z-transform CI for Spearman correlation."""
    z = np.arctanh(np.clip(r, -0.9999, 0.9999))
    se = 1.0 / np.sqrt(n - 3)
    z_crit = stats.norm.ppf((1 + confidence) / 2)
    return (float(np.tanh(z - z_crit * se)), float(np.tanh(z + z_crit * se)))


def pearson_ci(r, n, confidence=0.95):
    """Fisher z-transform CI for Pearson correlation."""
    z = np.arctanh(np.clip(r, -0.9999, 0.9999))
    se = 1.0 / np.sqrt(n - 3)
    z_crit = stats.norm.ppf((1 + confidence) / 2)
    return (float(np.tanh(z - z_crit * se)), float(np.tanh(z + z_crit * se)))


def mae_ci(errors, confidence=0.95):
    """t-distribution CI for MAE (CLT-based)."""
    n = len(errors)
    mean = np.mean(errors)
    se = stats.sem(errors)
    t_crit = stats.t.ppf((1 + confidence) / 2, n - 1)
    return (float(mean - t_crit * se), float(mean + t_crit * se))


def auroc_ci(auroc, n_pos, n_neg, confidence=0.95):
    """Hanley-McNeil formula CI for AUROC."""
    q1 = auroc / (2 - auroc)
    q2 = 2 * auroc ** 2 / (1 + auroc)
    var = (auroc * (1 - auroc) + (n_pos - 1) * (q1 - auroc ** 2) + (n_neg - 1) * (q2 - auroc ** 2)) / (n_pos * n_neg)
    se = np.sqrt(var)
    z_crit = stats.norm.ppf((1 + confidence) / 2)
    return (float(np.clip(auroc - z_crit * se, 0, 1)), float(np.clip(auroc + z_crit * se, 0, 1)))


def max_f1_at_threshold(labels, scores):
    labels = np.asarray(labels, dtype=int)
    scores = np.asarray(scores, dtype=float)
    thresholds = np.sort(np.unique(scores))
    best_f1 = -1.0
    best_threshold = None

    for threshold in thresholds:
        preds = (scores >= threshold).astype(int)
        f1 = f1_score(labels, preds, zero_division=0)
        if f1 > best_f1:
            best_f1 = float(f1)
            best_threshold = float(threshold)

    return best_f1, best_threshold


def paired_bootstrap_ci(values, confidence=0.95):
    values = np.asarray(values, dtype=float)
    alpha = 1 - confidence
    return (
        float(np.quantile(values, alpha / 2)),
        float(np.quantile(values, 1 - alpha / 2)),
    )


def paired_bootstrap_pvalue(values):
    values = np.asarray(values, dtype=float)
    non_positive = np.mean(values <= 0)
    non_negative = np.mean(values >= 0)
    return float(min(1.0, 2 * min(non_positive, non_negative)))


def build_one_vs_rest_arrays_by_paper(df, gt_score_cols):
    pred = []
    gt_avg = []
    rest_means = []
    heldout_scores = []

    for _, row in df.iterrows():
        human = np.asarray([float(row[c]) for c in gt_score_cols if pd.notna(row[c])], dtype=float)
        if len(human) < 2:
            continue
        pred.append(float(row["pred_score"]))
        gt_avg.append(float(row["gt_avg_score"]))
        rest_means.append(np.asarray([(human.sum() - score) / (len(human) - 1) for score in human], dtype=float))
        heldout_scores.append(human.copy())

    if len(pred) < 2:
        return None

    return {
        "pred": np.asarray(pred, dtype=float),
        "gt_avg": np.asarray(gt_avg, dtype=float),
        "rest_means_by_paper": rest_means,
        "heldout_scores_by_paper": heldout_scores,
    }


def ai_vs_one_vs_rest(df, gt_score_cols, confidence=0.95, n_boot=2000, seed=0):
    """Compare AI vs human one-vs-rest with paired paper-level bootstrap."""
    paired_inputs = build_one_vs_rest_arrays_by_paper(df, gt_score_cols)
    if paired_inputs is None:
        return None

    pred = paired_inputs["pred"]
    gt_avg = paired_inputs["gt_avg"]
    rest_means_by_paper = paired_inputs["rest_means_by_paper"]
    heldout_scores_by_paper = paired_inputs["heldout_scores_by_paper"]
    rest_means = np.concatenate(rest_means_by_paper)
    heldout_scores = np.concatenate(heldout_scores_by_paper)

    ai_spearman = float(stats.spearmanr(pred, gt_avg).statistic)
    human_spearman = float(stats.spearmanr(rest_means, heldout_scores).statistic)
    ai_pearson = float(stats.pearsonr(pred, gt_avg).statistic)
    human_pearson = float(stats.pearsonr(rest_means, heldout_scores).statistic)
    ai_mae = float(np.mean(np.abs(pred - gt_avg)))
    human_mae = float(np.mean(np.abs(rest_means - heldout_scores)))
    ai_fit = stats.linregress(gt_avg, pred)
    human_fit = stats.linregress(heldout_scores, rest_means)

    delta_samples = {
        "spearman": [],
        "pearson": [],
        "mae": [],
        "slope": [],
        "intercept": [],
    }
    rng = np.random.default_rng(seed)

    for _ in range(n_boot):
        sample_idx = rng.integers(0, len(pred), len(pred))
        boot_pred = pred[sample_idx]
        boot_gt_avg = gt_avg[sample_idx]
        boot_rest_means = np.concatenate([rest_means_by_paper[idx] for idx in sample_idx])
        boot_heldout_scores = np.concatenate([heldout_scores_by_paper[idx] for idx in sample_idx])
        boot_ai_fit = stats.linregress(boot_gt_avg, boot_pred)
        boot_human_fit = stats.linregress(boot_heldout_scores, boot_rest_means)

        delta_samples["spearman"].append(
            float(stats.spearmanr(boot_pred, boot_gt_avg).statistic - stats.spearmanr(boot_rest_means, boot_heldout_scores).statistic)
        )
        delta_samples["pearson"].append(
            float(stats.pearsonr(boot_pred, boot_gt_avg).statistic - stats.pearsonr(boot_rest_means, boot_heldout_scores).statistic)
        )
        delta_samples["mae"].append(
            float(np.mean(np.abs(boot_pred - boot_gt_avg)) - np.mean(np.abs(boot_rest_means - boot_heldout_scores)))
        )
        delta_samples["slope"].append(float(boot_ai_fit.slope - boot_human_fit.slope))
        delta_samples["intercept"].append(float(boot_ai_fit.intercept - boot_human_fit.intercept))

    return {
        "spearman_diff": ai_spearman - human_spearman,
        "spearman_ci": paired_bootstrap_ci(delta_samples["spearman"], confidence),
        "spearman_p": paired_bootstrap_pvalue(delta_samples["spearman"]),
        "pearson_diff": ai_pearson - human_pearson,
        "pearson_ci": paired_bootstrap_ci(delta_samples["pearson"], confidence),
        "pearson_p": paired_bootstrap_pvalue(delta_samples["pearson"]),
        "mae_diff": ai_mae - human_mae,
        "mae_ci": paired_bootstrap_ci(delta_samples["mae"], confidence),
        "mae_p": paired_bootstrap_pvalue(delta_samples["mae"]),
        "slope_diff": float(ai_fit.slope - human_fit.slope),
        "slope_ci": paired_bootstrap_ci(delta_samples["slope"], confidence),
        "slope_p": paired_bootstrap_pvalue(delta_samples["slope"]),
        "intercept_diff": float(ai_fit.intercept - human_fit.intercept),
        "intercept_ci": paired_bootstrap_ci(delta_samples["intercept"], confidence),
        "intercept_p": paired_bootstrap_pvalue(delta_samples["intercept"]),
        "n_boot": n_boot,
    }


def split_half_baseline(df, gt_score_cols):
    """Estimate human reliability via all unique split-half partitions per paper."""
    half_a, half_b = [], []
    paper_decisions = []

    for _, row in df.iterrows():
        scores = [float(row[c]) for c in gt_score_cols if pd.notna(row[c])]
        if len(scores) < 2:
            continue

        mid = len(scores) // 2
        indices = range(len(scores))
        for combo in combinations(indices, mid):
            if len(scores) % 2 == 0 and 0 not in combo:
                continue
            left = [scores[i] for i in combo]
            right = [scores[i] for i in indices if i not in combo]
            half_a.append(float(np.mean(left)))
            half_b.append(float(np.mean(right)))
            paper_decisions.append(row["gt_binary"].strip().lower())

    if len(half_a) < 2:
        return None

    a = np.array(half_a)
    b = np.array(half_b)
    pearson, _ = stats.pearsonr(a, b)
    spearman, _ = stats.spearmanr(a, b)
    mae = float(np.mean(np.abs(a - b)))

    return {
        "n_pairs": len(half_a),
        "pearson": float(pearson),
        "spearman": float(spearman),
        "mae": mae,
        "half_a": half_a,
        "half_b": half_b,
        "paper_decisions": paper_decisions,
    }


def one_vs_rest_baseline(df, gt_score_cols):
    """Estimate human reliability via leave-one-reviewer-out predictions."""
    rest_means = []
    heldout_scores = []
    n_papers = 0
    paper_decisions = []

    for _, row in df.iterrows():
        human = [float(row[c]) for c in gt_score_cols if pd.notna(row[c])]
        if len(human) < 2:
            continue
        n_papers += 1
        for idx, heldout in enumerate(human):
            others = human[:idx] + human[idx + 1:]
            if not others:
                continue
            rest_means.append(float(np.mean(others)))
            heldout_scores.append(float(heldout))
            paper_decisions.append(row["gt_binary"].strip().lower())

    if len(rest_means) < 2:
        return None

    pearson, _ = stats.pearsonr(rest_means, heldout_scores)
    spearman, _ = stats.spearmanr(rest_means, heldout_scores)
    mae = float(np.mean(np.abs(np.array(rest_means) - np.array(heldout_scores))))

    return {
        "n_pairs": len(rest_means),
        "n_papers": n_papers,
        "pearson": float(pearson),
        "spearman": float(spearman),
        "mae": mae,
        "rest_means": rest_means,
        "heldout_scores": heldout_scores,
        "paper_decisions": paper_decisions,
    }

def analyze_and_plot(path):
    df = pd.read_csv(path)
    # remove -1 lines
    df = df[df["pred_score"] >= 0]
    gt_score_cols = [c for c in df.columns if c.startswith("gt_score_")]

    # Filter out rows where pred_score is missing (ERROR / failed papers)
    n_total = len(df)
    df = df.dropna(subset=["pred_score"])
    df = df.reset_index(drop=True)
    n_dropped = n_total - len(df)
    if n_dropped > 0:
        print(f"\n  WARNING: Dropped {n_dropped}/{n_total} papers with missing predictions (ERROR rows)")

    pred = df["pred_score"].values
    gt_avg = df["gt_avg_score"].values
    pred_rounded = np.array([round_to_scale(x) for x in pred])
    n = len(pred)

    sp_raw, sp_raw_p = stats.spearmanr(pred, gt_avg)
    pe_raw, pe_raw_p = stats.pearsonr(pred, gt_avg)
    sp_rnd, sp_rnd_p = stats.spearmanr(pred_rounded, gt_avg)
    sp_raw_ci = spearman_ci(sp_raw, n)
    pe_raw_ci = pearson_ci(pe_raw, n)
    sp_rnd_ci = spearman_ci(sp_rnd, n)
    mae_raw = float(np.mean(np.abs(pred - gt_avg)))
    mae_rounded = float(np.mean(np.abs(pred_rounded - gt_avg)))
    mae_raw_ci = mae_ci(np.abs(pred - gt_avg))
    mae_rounded_ci = mae_ci(np.abs(pred_rounded - gt_avg))
    bias_raw = np.mean(pred - gt_avg)
    raw_regression = linear_regression_with_ci(gt_avg, pred)
    one_vs_rest = one_vs_rest_baseline(df, gt_score_cols)
    split_half = split_half_baseline(df, gt_score_cols)
    ai_vs_human = None
    if one_vs_rest is not None:
        ai_vs_human = ai_vs_one_vs_rest(df, gt_score_cols)

    # Bin-based MAE summaries using GT score bins: [0,2), [2,4), [4,6), [6,8), [8,10]
    bin_edges = [0, 2, 4, 6, 8, 10.01]
    bin_labels = ["0-2", "2-4", "4-6", "6-8", "8-10"]
    bin_indices = np.digitize(gt_avg, bin_edges) - 1
    bin_indices = np.clip(bin_indices, 0, len(bin_labels) - 1)
    bin_counts = np.bincount(bin_indices, minlength=len(bin_labels))
    bin_maes_raw = [None] * len(bin_labels)
    bin_maes_rounded = [None] * len(bin_labels)
    nonempty_bin_maes_raw = []
    nonempty_bin_maes_rounded = []
    for i in range(len(bin_labels)):
        if bin_counts[i] == 0:
            continue
        bin_mask = bin_indices == i
        bin_mae_raw = float(np.mean(np.abs(pred[bin_mask] - gt_avg[bin_mask])))
        bin_mae_rounded = float(np.mean(np.abs(pred_rounded[bin_mask] - gt_avg[bin_mask])))
        bin_maes_raw[i] = bin_mae_raw
        bin_maes_rounded[i] = bin_mae_rounded
        nonempty_bin_maes_raw.append(bin_mae_raw)
        nonempty_bin_maes_rounded.append(bin_mae_rounded)

    mean_bin_mae_raw = float(np.mean(nonempty_bin_maes_raw))
    mean_bin_mae_rounded = float(np.mean(nonempty_bin_maes_rounded))

    # Weight = 1/count for each bin (0 if bin is empty)
    bin_weights = np.where(bin_counts > 0, 1.0 / bin_counts, 0.0)
    sample_weights = bin_weights[bin_indices]
    # Normalize so weights sum to 1
    sample_weights = sample_weights / sample_weights.sum()
    wmae_raw = np.sum(sample_weights * np.abs(pred - gt_avg))
    wmae_rounded = np.sum(sample_weights * np.abs(pred_rounded - gt_avg))

    pred_dec = df["pred_decision"].fillna("N/A").str.strip().str.lower()
    gt_dec = df["gt_binary"].str.strip().str.lower()
    accept_label = (gt_dec == "accept").astype(int).values

    # Accept-rate per 1-point score bin
    # This is a calibration-style summary at the paper level:
    # one (score, paper_accept) point per paper on both the pred side and the human side.
    # Human uses gt_avg here because the goal is to compare how smooth/close the acceptance
    # rate curves are, not to compare single-reviewer discrimination performance.
    unit_bin_edges = np.arange(0, 11)  # [0,1), [1,2), ..., [9,10]
    unit_bin_labels = [f"[{int(unit_bin_edges[i])},{int(unit_bin_edges[i+1])})" for i in range(len(unit_bin_edges) - 1)]
    unit_bin_labels[-1] = unit_bin_labels[-1].replace(")", "]")

    def accept_rate_by_bin(scores, labels):
        scores = np.asarray(scores, dtype=float)
        labels = np.asarray(labels, dtype=int)
        idx = np.digitize(scores, unit_bin_edges[1:-1])
        out = []
        for i in range(len(unit_bin_labels)):
            mask = idx == i
            n = int(mask.sum())
            rate = float(labels[mask].mean()) if n > 0 else None
            out.append((n, rate))
        return out

    accept_rate_pred = accept_rate_by_bin(pred, accept_label)
    accept_rate_human = accept_rate_by_bin(gt_avg, accept_label)

    # Mean within-bin z-score (mean standardized deviation from bin mean).
    # Bin by gt_avg in 1-point bins; within each bin, compute (t - mean)/std for
    # every point, then average. Report both signed mean and mean absolute z.
    def mean_within_bin_z(values, bin_by):
        values = np.asarray(values, dtype=float)
        bin_by = np.asarray(bin_by, dtype=float)
        idx = np.digitize(bin_by, unit_bin_edges[1:-1])
        signed = []
        absolute = []
        bin_rows = []
        for i in range(len(unit_bin_labels)):
            mask = idx == i
            n = int(mask.sum())
            if n < 2:
                bin_rows.append((n, None, None, None, None))
                continue
            v = values[mask]
            mu = float(v.mean())
            sd = float(v.std(ddof=1))
            if sd == 0:
                bin_rows.append((n, mu, sd, 0.0, 0.0))
                signed.append(0.0)
                absolute.append(0.0)
                continue
            z = (v - mu) / sd
            s_mean = float(z.mean())
            a_mean = float(np.abs(z).mean())
            signed.append(s_mean)
            absolute.append(a_mean)
            bin_rows.append((n, mu, sd, s_mean, a_mean))
        overall_signed = float(np.mean(signed)) if signed else None
        overall_abs = float(np.mean(absolute)) if absolute else None
        return overall_signed, overall_abs, bin_rows

    ai_z_signed, ai_z_abs, ai_z_rows = mean_within_bin_z(pred, gt_avg)
    # Human: use individual reviewer scores, binned by that paper's gt_avg
    human_scores_flat = []
    human_binby_flat = []
    for _, row in df.iterrows():
        ga = float(row["gt_avg_score"])
        for c in gt_score_cols:
            if pd.notna(row[c]):
                human_scores_flat.append(float(row[c]))
                human_binby_flat.append(ga)
    human_z_signed, human_z_abs, human_z_rows = mean_within_bin_z(human_scores_flat, human_binby_flat)
    valid_dec_mask = ~pred_dec.isin(["n/a", ""])
    dec_match = ((pred_dec == gt_dec) & valid_dec_mask).sum()
    dec_eval_mask = valid_dec_mask & pred_dec.isin(["accept", "reject"]) & gt_dec.isin(["accept", "reject"])
    dec_tn = int(((gt_dec == "reject") & (pred_dec == "reject") & dec_eval_mask).sum())
    dec_fp = int(((gt_dec == "reject") & (pred_dec == "accept") & dec_eval_mask).sum())
    dec_fn = int(((gt_dec == "accept") & (pred_dec == "reject") & dec_eval_mask).sum())
    dec_tp = int(((gt_dec == "accept") & (pred_dec == "accept") & dec_eval_mask).sum())

    match_any = 0
    within_1std = 0
    for _, row in df.iterrows():
        r = round_to_scale(row["pred_score"])
        human = [row[c] for c in gt_score_cols if pd.notna(row[c])]
        if r in [int(s) for s in human]:
            match_any += 1
        if len(human) >= 2:
            h_mean = np.mean(human)
            h_std = np.std(human, ddof=1)
            if abs(row["pred_score"] - h_mean) <= h_std:
                within_1std += 1
        elif len(human) == 1:
            # With only 1 reviewer, no std; count as match if exact
            if round_to_scale(row["pred_score"]) == int(human[0]):
                within_1std += 1

    border_mask = (gt_avg >= 4) & (gt_avg <= 6)
    n_border = border_mask.sum()

    # ── CLI Output ──
    print(f"\n  Papers: {len(df)}")
    print(f"  {'─'*45}")
    print(
        f"  Spearman (raw):        {sp_raw:.4f}  "
        f"(95% CI {sp_raw_ci[0]:.4f}, {sp_raw_ci[1]:.4f}; p={sp_raw_p:.4f})"
    )
    print(
        f"  Spearman (rounded):    {sp_rnd:.4f}  "
        f"(95% CI {sp_rnd_ci[0]:.4f}, {sp_rnd_ci[1]:.4f}; p={sp_rnd_p:.4f})"
    )
    print(
        f"  Pearson (raw):         {pe_raw:.4f}  "
        f"(95% CI {pe_raw_ci[0]:.4f}, {pe_raw_ci[1]:.4f}; p={pe_raw_p:.4f})"
    )
    print(
        f"  Regression slope:      {raw_regression['slope']:.4f}  "
        f"(95% CI {raw_regression['slope_ci'][0]:.4f}, {raw_regression['slope_ci'][1]:.4f})"
    )
    print(
        f"  Regression intercept:  {raw_regression['intercept']:.4f}  "
        f"(95% CI {raw_regression['intercept_ci'][0]:.4f}, {raw_regression['intercept_ci'][1]:.4f})"
    )
    print(
        f"  MAE (raw):             {mae_raw:.4f}  "
        f"(95% CI {mae_raw_ci[0]:.4f}, {mae_raw_ci[1]:.4f})"
    )
    print(
        f"  MAE (rounded):         {mae_rounded:.4f}  "
        f"(95% CI {mae_rounded_ci[0]:.4f}, {mae_rounded_ci[1]:.4f})"
    )
    print(f"  Mean bin MAE (raw):    {mean_bin_mae_raw:.4f}")
    print(f"  Mean bin MAE (rounded):{mean_bin_mae_rounded:.4f}")
    print(f"  Weighted MAE (raw):    {wmae_raw:.4f}")
    print(f"  Weighted MAE (rounded):{wmae_rounded:.4f}")
    print(f"  Bias (pred-gt):        {bias_raw:+.4f}")
    if one_vs_rest is not None:
        print(f"  {'─'*45}")
        print(f"  Human panel-to-reviewer consistency ({one_vs_rest['n_pairs']} held-out reviews):")
        print(f"    Note:                group-human baseline: mean(other reviewers) predicts the held-out reviewer, across all leave-one-reviewer-out splits")
        print(f"    Spearman:            {one_vs_rest['spearman']:.4f}")
        print(f"    Pearson:             {one_vs_rest['pearson']:.4f}")
        print(f"    MAE:                 {one_vs_rest['mae']:.4f}")
        print(f"    AI vs human (paired paper bootstrap, n={ai_vs_human['n_boot']}):")
        print(
            f"      Spearman Δ:        {ai_vs_human['spearman_diff']:+.4f}  "
            f"(95% CI {ai_vs_human['spearman_ci'][0]:+.4f}, {ai_vs_human['spearman_ci'][1]:+.4f}; "
            f"p={ai_vs_human['spearman_p']:.4f})"
        )
        print(
            f"      Pearson Δ:         {ai_vs_human['pearson_diff']:+.4f}  "
            f"(95% CI {ai_vs_human['pearson_ci'][0]:+.4f}, {ai_vs_human['pearson_ci'][1]:+.4f}; "
            f"p={ai_vs_human['pearson_p']:.4f})"
        )
        print(
            f"      MAE Δ:             {ai_vs_human['mae_diff']:+.4f}  "
            f"(95% CI {ai_vs_human['mae_ci'][0]:+.4f}, {ai_vs_human['mae_ci'][1]:+.4f}; "
            f"p={ai_vs_human['mae_p']:.4f})"
        )
        print(
            f"      Slope Δ:           {ai_vs_human['slope_diff']:+.4f}  "
            f"(95% CI {ai_vs_human['slope_ci'][0]:+.4f}, {ai_vs_human['slope_ci'][1]:+.4f}; "
            f"p={ai_vs_human['slope_p']:.4f})"
        )
        print(
            f"      Intercept Δ:       {ai_vs_human['intercept_diff']:+.4f}  "
            f"(95% CI {ai_vs_human['intercept_ci'][0]:+.4f}, {ai_vs_human['intercept_ci'][1]:+.4f}; "
            f"p={ai_vs_human['intercept_p']:.4f})"
        )
    if split_half is not None:
        print(f"  {'─'*45}")
        print(f"  Human subgroup-to-subgroup consistency ({split_half['n_pairs']} exact split pairs):")
        print(f"    Note:                group-human baseline: one reviewer subgroup predicts another reviewer subgroup on the same paper")
        print(f"    Spearman:            {split_half['spearman']:.4f}")
        print(f"    Pearson:             {split_half['pearson']:.4f}")
        print(f"    MAE:                 {split_half['mae']:.4f}")
    # Show bin breakdown
    print(f"  {'─'*45}")
    print(f"  Score bin weights (inverse freq):")
    for i, label in enumerate(bin_labels):
        if bin_counts[i] > 0:
            print(f"    [{label}]: n={bin_counts[i]:>3}, MAE={bin_maes_raw[i]:.4f}, Rounded MAE={bin_maes_rounded[i]:.4f}")
    print(f"  {'─'*45}")
    print(f"  Accept rate per 1-point score bin (pred vs human avg score):")
    print(f"    {'bin':<8} {'pred n':>7} {'pred rate':>12}     {'human n':>8} {'human rate':>12}")
    for i, label in enumerate(unit_bin_labels):
        pn, pr = accept_rate_pred[i]
        hn, hr = accept_rate_human[i]
        pr_str = f"{pr:.0%}" if pr is not None else "   -"
        hr_str = f"{hr:.0%}" if hr is not None else "   -"
        if pn == 0 and hn == 0:
            continue
        print(f"    {label:<8} {pn:>7d} {pr_str:>12}     {hn:>8d} {hr_str:>12}")
    print(f"  {'─'*45}")
    print(f"  Mean within-bin z-score (bin by gt_avg, 1-pt bins):")
    print(f"    {'bin':<8} {'AI n':>5} {'AI |z|':>8} {'AI z':>8}     {'Hum n':>6} {'Hum |z|':>8} {'Hum z':>8}")
    for i, label in enumerate(unit_bin_labels):
        an, _, _, asz, aaz = ai_z_rows[i]
        hn, _, _, hsz, haz = human_z_rows[i]
        if an == 0 and hn == 0:
            continue
        aaz_s = f"{aaz:.3f}" if aaz is not None else "   -"
        asz_s = f"{asz:+.3f}" if asz is not None else "   -"
        haz_s = f"{haz:.3f}" if haz is not None else "   -"
        hsz_s = f"{hsz:+.3f}" if hsz is not None else "   -"
        print(f"    {label:<8} {an:>5d} {aaz_s:>8} {asz_s:>8}     {hn:>6d} {haz_s:>8} {hsz_s:>8}")
    if ai_z_abs is not None:
        print(f"    Mean across bins — AI:    |z|={ai_z_abs:.4f}  signed z={ai_z_signed:+.4f}")
    if human_z_abs is not None:
        print(f"    Mean across bins — Human: |z|={human_z_abs:.4f}  signed z={human_z_signed:+.4f}")
    print(f"  {'─'*45}")
    if valid_dec_mask.any():
        valid_decisions = int(valid_dec_mask.sum())
        print(f"  Decision accuracy:     {dec_match}/{valid_decisions} = {dec_match/valid_decisions:.1%}")
        print(f"  Direct decision confusion matrix:")
        print(f"    {'':<12} {'Pred Reject':>12} {'Pred Accept':>12}")
        print(f"    {'GT Reject':<12} {dec_tn:>12} {dec_fp:>12}")
        print(f"    {'GT Accept':<12} {dec_fn:>12} {dec_tp:>12}")
    else:
        print("  Decision accuracy:     N/A (decision labels disabled)")
    print(f"  Within 1 human std:    {within_1std}/{len(df)} = {within_1std/len(df):.1%}")
    print(f"  Human match (rounded): {match_any}/{len(df)} = {match_any/len(df):.1%}")

    # AUROC: use predicted score to discriminate Accept vs Reject
    gt_binary = (gt_dec == "accept").astype(int)  # 1=Accept, 0=Reject
    n_pos, n_neg = gt_binary.sum(), len(gt_binary) - gt_binary.sum()
    if n_pos > 0 and n_neg > 0:
        auroc = roc_auc_score(gt_binary, pred)
        auroc_ci_val = auroc_ci(auroc, n_pos, n_neg)
        ai_f1_max, ai_f1_threshold = max_f1_at_threshold(gt_binary, pred)
        fpr, tpr, thresholds = roc_curve(gt_binary, pred)
        # Human baseline AUROC: use individual reviewer scores (not the average)
        # Each individual score is an independent prediction of the paper's accept/reject label
        human_indiv_scores = []
        human_indiv_labels = []
        for i, (idx, row) in enumerate(df.iterrows()):
            label = gt_binary[i]
            for c in gt_score_cols:
                if pd.notna(row[c]):
                    human_indiv_scores.append(float(row[c]))
                    human_indiv_labels.append(label)
        human_indiv_scores = np.array(human_indiv_scores)
        human_indiv_labels = np.array(human_indiv_labels)
        n_indiv_pos = human_indiv_labels.sum()
        n_indiv_neg = len(human_indiv_labels) - n_indiv_pos
        if n_indiv_pos > 0 and n_indiv_neg > 0:
            human_auroc = roc_auc_score(human_indiv_labels, human_indiv_scores)
            human_auroc_ci_val = auroc_ci(human_auroc, n_indiv_pos, n_indiv_neg)
            human_f1_max, human_f1_threshold = max_f1_at_threshold(human_indiv_labels, human_indiv_scores)
            human_fpr, human_tpr, _ = roc_curve(human_indiv_labels, human_indiv_scores)
        else:
            human_auroc = None
            human_auroc_ci_val = None
            human_f1_max, human_f1_threshold = None, None
            human_fpr, human_tpr = None, None
        print(
            f"  AUROC (score→A/R):     {auroc:.4f}  "
            f"(95% CI {auroc_ci_val[0]:.4f}, {auroc_ci_val[1]:.4f})"
        )
        print(f"  F1_max (score→A/R):    {ai_f1_max:.4f}  (threshold={ai_f1_threshold:.2f})")
        if human_auroc is not None:
            print(
                f"  AUROC (human indiv):   {human_auroc:.4f}  "
                f"(95% CI {human_auroc_ci_val[0]:.4f}, {human_auroc_ci_val[1]:.4f}; "
                f"{len(human_indiv_scores)} individual scores)"
            )
            print(f"  F1_max (human indiv):  {human_f1_max:.4f}  (threshold={human_f1_threshold:.2f})")
            print("  Note:                  high human baseline: each reviewer score is matched to that paper's final accept/reject label, humans get multiple within-paper chances while AI gets one score per paper, and the final decision is itself derived from human scores")
        # Find optimal threshold (Youden's J)
        j_scores = tpr - fpr
        best_idx = np.argmax(j_scores)
        best_thresh = thresholds[best_idx]
        print(f"  Optimal threshold:     {best_thresh:.2f} (TPR={tpr[best_idx]:.2f}, FPR={fpr[best_idx]:.2f})")
        # AUPRC
        precision, recall, _ = precision_recall_curve(gt_binary, pred)
        auprc = auc(recall, precision)
        baseline_rate = n_pos / len(gt_binary)
        print(f"  AUPRC (score→A/R):     {auprc:.4f}  (baseline={baseline_rate:.4f})")
    else:
        auroc = None
        auroc_ci_val = None
        auprc = None
        ai_f1_max, ai_f1_threshold = None, None
        human_auroc = None
        human_auroc_ci_val = None
        human_f1_max, human_f1_threshold = None, None
        fpr, tpr = None, None
        human_fpr, human_tpr = None, None
        print(f"  AUROC/AUPRC: N/A (only one class present: {n_pos} Accept, {n_neg} Reject)")

    if n_border > 0:
        b_mae = np.mean(np.abs(pred[border_mask] - gt_avg[border_mask]))
        print(f"  {'─'*45}")
        print(f"  Borderline (gt 4-6):   {n_border} papers")
        border_valid = valid_dec_mask[border_mask]
        if border_valid.any():
            b_dec_acc = ((pred_dec[border_mask] == gt_dec[border_mask]) & border_valid).sum()
            valid_border = int(border_valid.sum())
            print(f"    Decision accuracy:   {b_dec_acc}/{valid_border} = {b_dec_acc/valid_border:.1%}")
        else:
            print("    Decision accuracy:   N/A (decision labels disabled)")
        print(f"    MAE:                 {b_mae:.4f}")

    print(f"\n  {'─'*45}")
    print(f"  {'Paper ID':<20} {'Pred':>5} {'Rnd':>4} {'GT':>5} {'Human':<20} {'Match'}")
    print(f"  {'─'*45}")
    for _, row in df.iterrows():
        r = round_to_scale(row["pred_score"])
        human = [row[c] for c in gt_score_cols if pd.notna(row[c])]
        h_str = ",".join(str(int(s)) for s in human)
        m = "✓" if r in [int(s) for s in human] else "✗"
        print(f"  {row['paper_id']:<20} {row['pred_score']:>5.1f} {r:>4} {row['gt_avg_score']:>5.2f} [{h_str}]{'':<{16-len(h_str)}} {m}")

    # ── Plot ──
    colors = ["#e74c3c" if d.strip().lower() == "reject" else "#2ecc71" for d in df["gt_binary"]]
    legend_dots = [
        Line2D([0],[0], marker='o', color='w', markerfacecolor='#2ecc71', markersize=8, label='Accept'),
        Line2D([0],[0], marker='o', color='w', markerfacecolor='#e74c3c', markersize=8, label='Reject'),
    ]

    has_curves = auroc is not None
    fig, axes = plt.subplots(2, 3, figsize=(21, 12))

    # Top-left: raw
    ax = axes[0, 0]
    ax.scatter(gt_avg, pred, c=colors, s=80, edgecolors="white", linewidth=0.8, zorder=3)
    mn, mx = min(min(pred), min(gt_avg)) - 0.5, max(max(pred), max(gt_avg)) + 0.5
    ax.plot([mn, mx], [mn, mx], "k--", alpha=0.3)
    xs = np.linspace(mn, mx, 100)
    fit_center, fit_lower, fit_upper = raw_regression["mean_ci"](xs)
    ax.fill_between(xs, fit_lower, fit_upper, color="#3498db", alpha=0.15, zorder=1)
    ax.plot(xs, fit_center, color="#3498db", alpha=0.7, zorder=2)
    ax.set_xlabel("Human Average Score", fontsize=12)
    ax.set_ylabel("Agent Predicted Score", fontsize=12)
    ax.set_title("Raw Scores", fontsize=13)
    ax.set_xlim(mn, mx); ax.set_ylim(mn, mx); ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.text(0.05, 0.95, f"Spearman: {sp_raw:.3f} [{sp_raw_ci[0]:.3f}, {sp_raw_ci[1]:.3f}]\nPearson: {pe_raw:.3f} [{pe_raw_ci[0]:.3f}, {pe_raw_ci[1]:.3f}]\nSlope: {raw_regression['slope']:.3f} [{raw_regression['slope_ci'][0]:.3f}, {raw_regression['slope_ci'][1]:.3f}]\nMAE: {mae_raw:.3f} [{mae_raw_ci[0]:.3f}, {mae_raw_ci[1]:.3f}]\nBias: {bias_raw:+.3f}\nWithin 1 human std: {within_1std}/{len(df)} ({within_1std/len(df):.0%})\nn = {len(df)}",
            transform=ax.transAxes, fontsize=10, va="top",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="wheat", alpha=0.8))
    ax.legend(handles=legend_dots, fontsize=9, loc="lower right")

    # Top-right: human one-vs-rest baseline scatter or ROC baseline if unavailable
    ax2 = axes[0, 1]
    if one_vs_rest is not None and one_vs_rest.get("rest_means") and one_vs_rest.get("heldout_scores"):
        left = np.array(one_vs_rest["rest_means"])
        right = np.array(one_vs_rest["heldout_scores"])
        ovr_colors = [
            "#e74c3c" if decision == "reject" else "#2ecc71"
            for decision in one_vs_rest["paper_decisions"]
        ]
        jitter_rng = np.random.default_rng(42)
        left_jit = left + jitter_rng.uniform(-0.35, 0.35, size=len(left))
        right_jit = right + jitter_rng.uniform(-0.35, 0.35, size=len(right))
        ax2.scatter(left_jit, right_jit, c=ovr_colors, s=70, edgecolors="white", linewidth=0.8, alpha=0.9)
        mn2, mx2 = min(left.min(), right.min()) - 0.5, max(left.max(), right.max()) + 0.5
        ax2.plot([mn2, mx2], [mn2, mx2], "k--", alpha=0.3)
        if len(left) >= 2:
            m2, b2 = np.polyfit(left, right, 1)
            xs2 = np.linspace(mn2, mx2, 100)
            ax2.plot(xs2, m2 * xs2 + b2, color="#c0392b", alpha=0.7)
        ax2.set_xlabel("Mean of Other Reviewers", fontsize=12)
        ax2.set_ylabel("Held-Out Reviewer Score", fontsize=12)
        ax2.set_title("Human One-vs-Rest Baseline", fontsize=13)
        ax2.set_xlim(mn2, mx2); ax2.set_ylim(mn2, mx2); ax2.set_aspect("equal")
        ax2.grid(True, alpha=0.2)
        ax2.text(
            0.05, 0.95,
            f"Spearman: {one_vs_rest['spearman']:.3f}\n"
            f"Pearson: {one_vs_rest['pearson']:.3f}\n"
            f"MAE: {one_vs_rest['mae']:.3f}\n"
            f"Accept pairs: {sum(d == 'accept' for d in one_vs_rest['paper_decisions'])}\n"
            f"Reject pairs: {sum(d == 'reject' for d in one_vs_rest['paper_decisions'])}\n"
            f"{one_vs_rest['n_pairs']} held-out reviews",
            transform=ax2.transAxes, fontsize=10, va="top",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="wheat", alpha=0.8)
        )
        ax2.legend(handles=legend_dots, fontsize=9, loc="lower right")
    else:
        ax2.axis("off")

    # Bottom-left: ROC curve
    if has_curves:
        ax3 = axes[1, 0]
        ax3.plot(
            fpr,
            tpr,
            color="#3498db",
            lw=2,
            label=f"Agent (AUROC={auroc:.3f} [{auroc_ci_val[0]:.3f}, {auroc_ci_val[1]:.3f}])",
        )
        ax3.plot([0, 1], [0, 1], "k--", alpha=0.3, label="Random (0.500)")
        ax3.scatter([fpr[best_idx]], [tpr[best_idx]], color="#e74c3c", s=100, zorder=5,
                    label=f"Optimal threshold={best_thresh:.2f}")
        ax3.set_xlabel("False Positive Rate", fontsize=12)
        ax3.set_ylabel("True Positive Rate", fontsize=12)
        ax3.set_title("ROC Curve (Score → Accept/Reject)", fontsize=13)
        ax3.set_xlim(-0.02, 1.02); ax3.set_ylim(-0.02, 1.02)
        ax3.set_aspect("equal")
        ax3.grid(True, alpha=0.2)
        ax3.legend(fontsize=9, loc="lower right")

        # Bottom-right: Precision-Recall curve
        ax4 = axes[1, 1]
        ax4.plot(recall, precision, color="#9b59b6", lw=2, label=f"Agent (AUPRC={auprc:.3f})")
        ax4.axhline(y=baseline_rate, color="k", linestyle="--", alpha=0.3, label=f"Baseline ({baseline_rate:.3f})")
        ax4.set_xlabel("Recall", fontsize=12)
        ax4.set_ylabel("Precision", fontsize=12)
        ax4.set_title("Precision-Recall Curve (Score → Accept/Reject)", fontsize=13)
        ax4.set_xlim(-0.02, 1.02); ax4.set_ylim(-0.02, 1.02)
        ax4.set_aspect("equal")
        ax4.grid(True, alpha=0.2)
        ax4.legend(fontsize=9, loc="lower left")
    else:
        axes[1, 0].axis("off")
        axes[1, 1].axis("off")

    # Top-right: Split-half correlation scatter with jitter
    ax5 = axes[0, 2]
    if split_half is not None and split_half.get("half_a"):
        sh_a = np.array(split_half["half_a"])
        sh_b = np.array(split_half["half_b"])
        split_colors = [
            "#e74c3c" if decision == "reject" else "#2ecc71"
            for decision in split_half["paper_decisions"]
        ]
        jitter_rng = np.random.default_rng(99)
        sh_a_jit = sh_a + jitter_rng.uniform(-0.3, 0.3, size=len(sh_a))
        sh_b_jit = sh_b + jitter_rng.uniform(-0.3, 0.3, size=len(sh_b))
        ax5.scatter(sh_a_jit, sh_b_jit, c=split_colors, s=80, edgecolors="white", linewidth=0.8, alpha=0.85)
        mn5, mx5 = min(sh_a.min(), sh_b.min()) - 0.5, max(sh_a.max(), sh_b.max()) + 0.5
        ax5.plot([mn5, mx5], [mn5, mx5], "k--", alpha=0.3)
        if len(sh_a) >= 2:
            m5, b5 = np.polyfit(sh_a, sh_b, 1)
            xs5 = np.linspace(mn5, mx5, 100)
            ax5.plot(xs5, m5 * xs5 + b5, color="#2c3e50", alpha=0.7)
        ax5.set_xlabel("Half A Mean Score", fontsize=12)
        ax5.set_ylabel("Half B Mean Score", fontsize=12)
        ax5.set_title("Human Split-Half Correlation", fontsize=13)
        ax5.set_xlim(mn5, mx5); ax5.set_ylim(mn5, mx5); ax5.set_aspect("equal")
        ax5.grid(True, alpha=0.2)
        ax5.text(
            0.05, 0.95,
            f"Spearman: {split_half['spearman']:.3f}\n"
            f"Pearson: {split_half['pearson']:.3f}\n"
            f"MAE: {split_half['mae']:.3f}\n"
            f"Accept pairs: {sum(d == 'accept' for d in split_half['paper_decisions'])}\n"
            f"Reject pairs: {sum(d == 'reject' for d in split_half['paper_decisions'])}\n"
            f"{split_half['n_pairs']} exact split pairs",
            transform=ax5.transAxes, fontsize=10, va="top",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="wheat", alpha=0.8)
        )
        ax5.legend(handles=legend_dots, fontsize=9, loc="lower right")
    else:
        ax5.axis("off")

    # Bottom-right: Human PRC (individual scores)
    ax6 = axes[1, 2]
    if has_curves and human_auroc is not None:
        human_precision, human_recall, _ = precision_recall_curve(human_indiv_labels, human_indiv_scores)
        human_auprc = auc(human_recall, human_precision)
        human_baseline_rate = float(n_indiv_pos) / len(human_indiv_labels)
        ax6.plot(
            human_recall,
            human_precision,
            color="#f39c12",
            lw=2.5,
            label=f"Human Indiv (AUPRC={human_auprc:.3f})",
        )
        ax6.axhline(y=human_baseline_rate, color="k", linestyle="--", alpha=0.3, label=f"Baseline ({human_baseline_rate:.3f})")
        ax6.set_xlabel("Recall", fontsize=12)
        ax6.set_ylabel("Precision", fontsize=12)
        ax6.set_title("Precision-Recall Curve (Human Individual Scores)", fontsize=13)
        ax6.set_xlim(-0.02, 1.02); ax6.set_ylim(-0.02, 1.02)
        ax6.set_aspect("equal")
        ax6.grid(True, alpha=0.2)
        ax6.legend(fontsize=9, loc="lower left")
    else:
        ax6.axis("off")

    plt.tight_layout()
    out = path.replace(".csv", "_scatter.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"\n  Plot saved: {out}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "bench_scores.csv"
    analyze_and_plot(path)
