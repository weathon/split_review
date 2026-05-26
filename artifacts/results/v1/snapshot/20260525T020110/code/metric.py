from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, roc_auc_score


BOOTSTRAP_N = 10000
RANDOM_SEED = 0


csv_path = Path(sys.argv[1])
output_dir = csv_path.parent / "metrics"
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv_path)
score_columns = [column for column in df.columns if column.startswith("gt_score_")]
score_value_columns = ["pred_score", "gt_avg_score"] + score_columns
negative_mask = (df[score_value_columns].astype(float) < 0).any(axis=1)
filtered_negative_rows = int(negative_mask.sum())
df = df[~negative_mask].reset_index(drop=True)
human_score_frame = df[score_columns].astype(float)

paper_indices = np.arange(len(df))
pred_score = df["pred_score"].astype(float).to_numpy()
gt_avg_score = df["gt_avg_score"].astype(float).to_numpy()
decisions = df["gt_binary"].astype(str).to_numpy()
labels = (decisions == "Accept").astype(int)

human_scores = []
human_targets = []
human_labels = []
human_paper_indices = []

human_pair_x = []
human_pair_y = []
human_pair_decisions = []
human_pair_paper_indices = []

human_rest_x = []
human_rest_y = []
human_rest_decisions = []
human_rest_paper_indices = []

for paper_index in paper_indices:
    paper_scores = human_score_frame.iloc[paper_index].dropna().to_numpy(dtype=float)

    for score_index, score in enumerate(paper_scores):
        rest_scores = np.delete(paper_scores, score_index)
        human_scores.append(float(score))
        human_targets.append(float(rest_scores.mean()))
        human_labels.append(int(labels[paper_index]))
        human_paper_indices.append(int(paper_index))

    for left_index in range(len(paper_scores)):
        for right_index in range(left_index + 1, len(paper_scores)):
            human_pair_x.append(float(paper_scores[left_index]))
            human_pair_y.append(float(paper_scores[right_index]))
            human_pair_decisions.append(decisions[paper_index])
            human_pair_paper_indices.append(int(paper_index))

    for score_index in range(len(paper_scores)):
        rest_scores = np.delete(paper_scores, score_index)
        human_rest_x.append(float(paper_scores[score_index]))
        human_rest_y.append(float(rest_scores.mean()))
        human_rest_decisions.append(decisions[paper_index])
        human_rest_paper_indices.append(int(paper_index))

human_scores = np.asarray(human_scores, dtype=float)
human_targets = np.asarray(human_targets, dtype=float)
human_labels = np.asarray(human_labels, dtype=int)
human_paper_indices = np.asarray(human_paper_indices, dtype=int)

human_pair_x = np.asarray(human_pair_x, dtype=float)
human_pair_y = np.asarray(human_pair_y, dtype=float)
human_pair_decisions = np.asarray(human_pair_decisions)
human_pair_paper_indices = np.asarray(human_pair_paper_indices, dtype=int)

human_rest_x = np.asarray(human_rest_x, dtype=float)
human_rest_y = np.asarray(human_rest_y, dtype=float)
human_rest_decisions = np.asarray(human_rest_decisions)
human_rest_paper_indices = np.asarray(human_rest_paper_indices, dtype=int)

ai_corr = float(pearsonr(pred_score, gt_avg_score).statistic)
human_pair_corr = float(pearsonr(human_pair_x, human_pair_y).statistic)
human_rest_corr = float(pearsonr(human_rest_x, human_rest_y).statistic)

ai_calibrated = np.empty(len(df), dtype=float)
for paper_index in paper_indices:
    train_mask = paper_indices != paper_index
    model = LinearRegression()
    model.fit(pred_score[train_mask].reshape(-1, 1), gt_avg_score[train_mask])
    ai_calibrated[paper_index] = model.predict(pred_score[[paper_index]].reshape(-1, 1))[0]
ai_calibrated = np.clip(ai_calibrated, 0, 10)

human_calibrated = np.empty(len(human_scores), dtype=float)
for paper_index in paper_indices:
    train_mask = human_paper_indices != paper_index
    test_mask = human_paper_indices == paper_index
    model = LinearRegression()
    model.fit(human_scores[train_mask].reshape(-1, 1), human_targets[train_mask])
    human_calibrated[test_mask] = model.predict(human_scores[test_mask].reshape(-1, 1))
human_calibrated = np.clip(human_calibrated, 0, 10)

ai_calibrated_corr = float(pearsonr(ai_calibrated, gt_avg_score).statistic)

plot_rng = np.random.default_rng(RANDOM_SEED)
fig, axes = plt.subplots(2, 2, figsize=(11, 10), dpi=160)
plot_specs = [
    (
        axes[0, 0],
        gt_avg_score,
        pred_score,
        decisions,
        "AI raw vs human mean",
        "Human mean score",
        "AI raw score",
        ai_corr,
    ),
    (
        axes[0, 1],
        gt_avg_score,
        ai_calibrated,
        decisions,
        "AI calibrated vs human mean",
        "Human mean score",
        "AI calibrated score",
        ai_calibrated_corr,
    ),
    (
        axes[1, 0],
        human_pair_x,
        human_pair_y,
        human_pair_decisions,
        "Human 1 vs 1",
        "Human score",
        "Other human score",
        human_pair_corr,
    ),
    (
        axes[1, 1],
        human_rest_x,
        human_rest_y,
        human_rest_decisions,
        "Human 1 vs rest",
        "Human score",
        "Rest mean score",
        human_rest_corr,
    ),
]
colors = {"Accept": "#2a9d8f", "Reject": "#d65a31"}
for ax, x_values, y_values, plot_decisions, title, x_label, y_label, corr_value in plot_specs:
    x_jitter = x_values + plot_rng.uniform(-0.2, 0.2, size=len(x_values))
    y_jitter = y_values + plot_rng.uniform(-0.2, 0.2, size=len(y_values))
    for decision, color in colors.items():
        mask = plot_decisions == decision
        ax.scatter(
            x_jitter[mask],
            y_jitter[mask],
            s=42,
            alpha=0.72,
            color=color,
            label=decision,
            edgecolors="white",
            linewidths=0.45,
        )

    line_min = min(float(x_values.min()), float(y_values.min()))
    line_max = max(float(x_values.max()), float(y_values.max()))
    line_x = np.linspace(line_min, line_max, 100)
    model = LinearRegression()
    model.fit(x_values.reshape(-1, 1), y_values)
    ax.plot(line_x, line_x, color="#666666", linestyle="--", linewidth=1.2, label="y=x")
    ax.plot(
        line_x,
        model.predict(line_x.reshape(-1, 1)),
        color="#111111",
        linewidth=1.7,
        label="fit",
    )
    ax.set_xlim(line_min - 0.4, line_max + 0.4)
    ax.set_ylim(line_min - 0.4, line_max + 0.4)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(f"{title}\nr={corr_value:.3f}")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(alpha=0.25)

axes[1, 1].legend(frameon=False, loc="best")
fig.tight_layout()
corr_plot_path = output_dir / "corr_plots.png"
fig.savefig(corr_plot_path)
plt.close(fig)

ai_abs_error_by_paper = np.abs(ai_calibrated - gt_avg_score)
human_abs_error = np.abs(human_calibrated - human_targets)
human_abs_error_by_paper = np.asarray(
    [human_abs_error[human_paper_indices == paper_index].mean() for paper_index in paper_indices],
    dtype=float,
)

ai_auroc = float(roc_auc_score(labels, pred_score))
human_single_auroc = float(roc_auc_score(human_labels, human_scores))

human_pair_x_by_paper = [
    human_pair_x[human_pair_paper_indices == paper_index] for paper_index in paper_indices
]
human_pair_y_by_paper = [
    human_pair_y[human_pair_paper_indices == paper_index] for paper_index in paper_indices
]
human_rest_x_by_paper = [
    human_rest_x[human_rest_paper_indices == paper_index] for paper_index in paper_indices
]
human_rest_y_by_paper = [
    human_rest_y[human_rest_paper_indices == paper_index] for paper_index in paper_indices
]
human_scores_by_paper = [
    human_scores[human_paper_indices == paper_index] for paper_index in paper_indices
]
human_labels_by_paper = [
    human_labels[human_paper_indices == paper_index] for paper_index in paper_indices
]

rng = np.random.default_rng(RANDOM_SEED)

corr_pair_deltas = np.empty(BOOTSTRAP_N, dtype=float)
for bootstrap_index in range(BOOTSTRAP_N):
    sampled_papers = rng.integers(0, len(df), size=len(df))
    ai_boot_corr = float(pearsonr(pred_score[sampled_papers], gt_avg_score[sampled_papers]).statistic)
    human_boot_x = np.concatenate(
        [human_pair_x_by_paper[paper_index] for paper_index in sampled_papers]
    )
    human_boot_y = np.concatenate(
        [human_pair_y_by_paper[paper_index] for paper_index in sampled_papers]
    )
    human_boot_corr = float(pearsonr(human_boot_x, human_boot_y).statistic)
    corr_pair_deltas[bootstrap_index] = ai_boot_corr - human_boot_corr

corr_pair_observed_delta = ai_corr - human_pair_corr
corr_pair_p_value = 2 * min(
    float((corr_pair_deltas <= 0).mean()),
    float((corr_pair_deltas >= 0).mean()),
)

corr_rest_deltas = np.empty(BOOTSTRAP_N, dtype=float)
for bootstrap_index in range(BOOTSTRAP_N):
    sampled_papers = rng.integers(0, len(df), size=len(df))
    ai_boot_corr = float(pearsonr(pred_score[sampled_papers], gt_avg_score[sampled_papers]).statistic)
    human_boot_x = np.concatenate(
        [human_rest_x_by_paper[paper_index] for paper_index in sampled_papers]
    )
    human_boot_y = np.concatenate(
        [human_rest_y_by_paper[paper_index] for paper_index in sampled_papers]
    )
    human_boot_corr = float(pearsonr(human_boot_x, human_boot_y).statistic)
    corr_rest_deltas[bootstrap_index] = ai_boot_corr - human_boot_corr

corr_rest_observed_delta = ai_corr - human_rest_corr
corr_rest_p_value = 2 * min(
    float((corr_rest_deltas <= 0).mean()),
    float((corr_rest_deltas >= 0).mean()),
)

mae_deltas = np.empty(BOOTSTRAP_N, dtype=float)
for bootstrap_index in range(BOOTSTRAP_N):
    sampled_papers = rng.integers(0, len(df), size=len(df))
    mae_deltas[bootstrap_index] = (
        mean_absolute_error(gt_avg_score[sampled_papers], ai_calibrated[sampled_papers])
        - human_abs_error_by_paper[sampled_papers].mean()
    )

ai_mae = float(mean_absolute_error(gt_avg_score, ai_calibrated))
human_single_mae = float(human_abs_error_by_paper.mean())
mae_observed_delta = ai_mae - human_single_mae
mae_p_value = 2 * min(
    float((mae_deltas <= 0).mean()),
    float((mae_deltas >= 0).mean()),
)

positive_papers = paper_indices[labels == 1]
negative_papers = paper_indices[labels == 0]
auroc_deltas = np.empty(BOOTSTRAP_N, dtype=float)
for bootstrap_index in range(BOOTSTRAP_N):
    sampled_papers = np.concatenate(
        [
            rng.choice(positive_papers, size=len(positive_papers), replace=True),
            rng.choice(negative_papers, size=len(negative_papers), replace=True),
        ]
    )
    ai_boot_auroc = float(roc_auc_score(labels[sampled_papers], pred_score[sampled_papers]))
    human_boot_scores = np.concatenate(
        [human_scores_by_paper[paper_index] for paper_index in sampled_papers]
    )
    human_boot_labels = np.concatenate(
        [human_labels_by_paper[paper_index] for paper_index in sampled_papers]
    )
    human_boot_auroc = float(roc_auc_score(human_boot_labels, human_boot_scores))
    auroc_deltas[bootstrap_index] = ai_boot_auroc - human_boot_auroc

auroc_observed_delta = ai_auroc - human_single_auroc
auroc_p_value = 2 * min(
    float((auroc_deltas <= 0).mean()),
    float((auroc_deltas >= 0).mean()),
)

delta_names = ["corr 1v1", "corr 1vRest", "MAE", "AUROC"]
delta_values = np.asarray(
    [
        corr_pair_observed_delta,
        corr_rest_observed_delta,
        mae_observed_delta,
        auroc_observed_delta,
    ],
    dtype=float,
)
delta_cis = np.asarray(
    [
        np.percentile(corr_pair_deltas, [2.5, 97.5]),
        np.percentile(corr_rest_deltas, [2.5, 97.5]),
        np.percentile(mae_deltas, [2.5, 97.5]),
        np.percentile(auroc_deltas, [2.5, 97.5]),
    ],
    dtype=float,
)
delta_p_values = [
    corr_pair_p_value,
    corr_rest_p_value,
    mae_p_value,
    auroc_p_value,
]

lines = []
lines.append(f"file: {csv_path}")
lines.append(f"papers: {len(df)}")
lines.append(f"filtered negative rows: {filtered_negative_rows}")
lines.append(f"human scores: {len(human_scores)}")
lines.append(f"human pairs: {len(human_pair_x)}")
lines.append(f"bootstrap: {BOOTSTRAP_N}")
lines.append(f"corr plot: {corr_plot_path}")
lines.append("")
lines.append("Correlation")
lines.append("-----------")
lines.append(f"{'metric':<22} {'value':>10}")
lines.append(f"{'-' * 22} {'-' * 10}")
for name, value in [
    ("AI raw vs human mean", ai_corr),
    ("AI cal vs human mean", ai_calibrated_corr),
    ("Human 1 vs 1", human_pair_corr),
    ("Human 1 vs rest", human_rest_corr),
]:
    lines.append(f"{name:<22} {value:>10.4f}")

lines.append("")
lines.append("Leave-one-out calibrated MAE")
lines.append("----------------------------")
lines.append(f"{'metric':<22} {'value':>10}")
lines.append(f"{'-' * 22} {'-' * 10}")
mae_values = [
    ("AI", ai_mae),
    ("Human single", human_single_mae),
]
for name, value in mae_values:
    lines.append(f"{name:<22} {value:>10.4f}")

lines.append("")
lines.append("AUROC for final decision")
lines.append("------------------------")
lines.append(f"{'metric':<22} {'value':>10}")
lines.append(f"{'-' * 22} {'-' * 10}")
for name, value in [
    ("AI", ai_auroc),
    ("Human single", human_single_auroc),
]:
    lines.append(f"{name:<22} {value:>10.4f}")

lines.append("")
lines.append("Bootstrap paired test: delta = AI - Human")
lines.append("-----------------------------------------")
lines.append(
    f"{'metric':<14} {'delta':>10} {'ci_low':>10} {'ci_high':>10} {'p_value':>10}"
)
lines.append(f"{'-' * 14} {'-' * 10} {'-' * 10} {'-' * 10} {'-' * 10}")
for name, value, ci, p_value in zip(delta_names, delta_values, delta_cis, delta_p_values):
    left = float(ci[0])
    right = float(ci[1])
    lines.append(
        f"{name:<14} {value:>10.4f} {left:>10.4f} {right:>10.4f} {p_value:>10.4g}"
    )

report = "\n".join(lines) + "\n"
report_path = output_dir / "metric_report.txt"
report_path.write_text(report)
print(report)
print(f"saved {report_path}")
