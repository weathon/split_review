import json
import pickle
from pathlib import Path
import time

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.linear_model import ElasticNetCV, LinearRegression, RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

SCORES_CSV = Path("results/final_deepreview_cal/scores.csv")
EMBEDDINGS_NPZ = Path("results/final_deepreview_cal/ml_qwen8b_openrouter_embedding/embeddings.npz")
OUT_DIR = Path("results/final_deepreview_cal/ml_qwen8b_openrouter_residual")
OUT_DIR.mkdir(parents=True, exist_ok=True)
RANDOM_STATE = 7
N_SPLITS = 5

print("loading scores and embeddings")
scores = pd.read_csv(SCORES_CSV)
saved = np.load(EMBEDDINGS_NPZ)
paper_ids = saved["paper_ids"].astype(str)
if list(scores["paper_id"].astype(str)) != list(paper_ids):
    raise ValueError("score rows and embedding rows are not aligned")

embeddings = saved["embeddings"].astype(float)
pred_scores = scores["pred_score"].to_numpy(dtype=float)
gt_scores = scores["gt_avg_score"].to_numpy(dtype=float)

pca_candidates = [16, 32, 64, 128]
pca_max = min(embeddings.shape[1], embeddings.shape[0] - N_SPLITS)
pca_candidates = [d for d in pca_candidates if d <= pca_max]
if not pca_candidates:
    raise ValueError("not enough samples for PCA candidates")

feature_variants = {
    "pca_only": lambda x, s, b: x,
    "pca_pred_sq": lambda x, s, b: np.hstack([x, s[:, None], (s * s)[:, None]]),
}

models = {
    "residual_ridge": lambda: make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-4, 4, 17))),
    "residual_elastic_net": lambda: make_pipeline(
        StandardScaler(),
        ElasticNetCV(
            l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9],
            alphas=np.logspace(-3, 3, 13),
            cv=3,
            max_iter=20000,
            random_state=RANDOM_STATE,
        ),
    ),
    "residual_svr_rbf": lambda: make_pipeline(StandardScaler(), SVR(C=3, gamma="scale", epsilon=0.05)),
    "residual_gradient_boosting": lambda: GradientBoostingRegressor(
        n_estimators=120,
        learning_rate=0.03,
        max_depth=2,
        min_samples_leaf=4,
        random_state=RANDOM_STATE,
    ),
    "residual_extra_trees": lambda: ExtraTreesRegressor(
        n_estimators=300,
        min_samples_leaf=3,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    ),
}

kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=RANDOM_STATE)
rows = []
best_score = -10.0
best_spec = None

baseline_oof = np.zeros(len(gt_scores), dtype=float)
for train_idx, val_idx in kf.split(embeddings):
    base = LinearRegression()
    base.fit(pred_scores[train_idx, None], gt_scores[train_idx])
    baseline_oof[val_idx] = base.predict(pred_scores[val_idx, None])
baseline_corr = pearsonr(gt_scores, baseline_oof).statistic
baseline_rmse = float((np.mean((gt_scores - baseline_oof) ** 2) ** 0.5))
print("baseline pred_score linear oof pearson", baseline_corr, "rmse", baseline_rmse)

for model_name, build_model in models.items():
    for pca_dim in pca_candidates:
        for feature_name, feature_builder in feature_variants.items():
            print("config", model_name, "pca", pca_dim, "features", feature_name)
            fold_scores = []
            fold_rmse = []
            oof_pred = np.zeros(len(gt_scores), dtype=float)

            for train_idx, val_idx in kf.split(embeddings):
                fold_start = time.time()
                base = LinearRegression()
                base.fit(pred_scores[train_idx, None], gt_scores[train_idx])
                base_train = base.predict(pred_scores[train_idx, None])
                base_val = base.predict(pred_scores[val_idx, None])
                residual_train = gt_scores[train_idx] - base_train

                pca_dim_fold = min(pca_dim, len(train_idx) - 1)
                if pca_dim_fold < 1:
                    raise ValueError(f"invalid PCA dim {pca_dim_fold} for fold train size {len(train_idx)}")
                pca = PCA(n_components=pca_dim_fold, random_state=RANDOM_STATE)
                x_tr_pca = pca.fit_transform(embeddings[train_idx])
                x_va_pca = pca.transform(embeddings[val_idx])
                x_tr = feature_builder(x_tr_pca, pred_scores[train_idx], base_train)
                x_va = feature_builder(x_va_pca, pred_scores[val_idx], base_val)

                model = build_model()
                model.fit(x_tr, residual_train)
                pred = base_val + model.predict(x_va).astype(float)
                oof_pred[val_idx] = pred
                corr = pearsonr(gt_scores[val_idx], pred).statistic
                fold_scores.append(float(corr))
                fold_rmse.append(float((np.mean((gt_scores[val_idx] - pred) ** 2) ** 0.5)))
                print("  fold", len(fold_scores), "corr", round(corr, 4), "time", round(time.time() - fold_start, 2))

            mean_corr = float(np.mean(fold_scores))
            mean_rmse = float(np.mean(fold_rmse))
            rows.append(
                {
                    "model": model_name,
                    "pca_dim": int(pca_dim),
                    "feature_variant": feature_name,
                    "mean_pearson": mean_corr,
                    "mean_rmse": mean_rmse,
                }
            )
            if mean_corr > best_score:
                best_score = mean_corr
                best_spec = {
                    "model": model_name,
                    "pca_dim": pca_dim,
                    "feature_variant": feature_name,
                }

metrics = pd.DataFrame(rows).sort_values("mean_pearson", ascending=False).reset_index(drop=True)
if metrics.empty:
    raise ValueError("no residual model variants were evaluated")
if best_spec is None:
    raise ValueError("best residual configuration was not selected")

metrics_path = OUT_DIR / "cv_metrics.csv"
metrics.to_csv(metrics_path, index=False)

best = best_spec
best_model_builder = models[best["model"]]
best_feature_builder = feature_variants[best["feature_variant"]]

oof = np.zeros(len(gt_scores), dtype=float)
for train_idx, val_idx in kf.split(embeddings):
    base = LinearRegression()
    base.fit(pred_scores[train_idx, None], gt_scores[train_idx])
    base_train = base.predict(pred_scores[train_idx, None])
    base_val = base.predict(pred_scores[val_idx, None])
    residual_train = gt_scores[train_idx] - base_train
    pca_dim_fold = min(best["pca_dim"], len(train_idx) - 1)
    pca = PCA(n_components=pca_dim_fold, random_state=RANDOM_STATE)
    x_tr_pca = pca.fit_transform(embeddings[train_idx])
    x_va_pca = pca.transform(embeddings[val_idx])
    x_tr = best_feature_builder(x_tr_pca, pred_scores[train_idx], base_train)
    x_va = best_feature_builder(x_va_pca, pred_scores[val_idx], base_val)
    model = best_model_builder()
    model.fit(x_tr, residual_train)
    oof[val_idx] = base_val + model.predict(x_va).astype(float)

oof_pearson = pearsonr(gt_scores, oof).statistic
oof_rmse = float((np.mean((gt_scores - oof) ** 2) ** 0.5))
r2 = float(r2_score(gt_scores, oof))

predictions = pd.DataFrame(
    {
        "paper_id": scores["paper_id"],
        "gt_avg_score": gt_scores,
        "pred_score": pred_scores,
        "baseline_oof_pred": baseline_oof,
        "residual_oof_pred": oof,
    }
)
pred_path = OUT_DIR / "oof_predictions.csv"
predictions.to_csv(pred_path, index=False)

base_full = LinearRegression()
base_full.fit(pred_scores[:, None], gt_scores)
base_pred_full = base_full.predict(pred_scores[:, None])
residual_full = gt_scores - base_pred_full
final_pca = PCA(n_components=best["pca_dim"], random_state=RANDOM_STATE)
reduced = final_pca.fit_transform(embeddings)
final_x = best_feature_builder(reduced, pred_scores, base_pred_full)
final_model = best_model_builder()
final_model.fit(final_x, residual_full)

model_path = OUT_DIR / "best_model.pkl"
state = {
    "embedding_npz": str(EMBEDDINGS_NPZ),
    "scores_csv": str(SCORES_CSV),
    "method": "foldwise_pred_score_linear_baseline_plus_embedding_residual",
    "pca_components": best["pca_dim"],
    "feature_variant": best["feature_variant"],
    "best_model_name": best["model"],
    "n_splits": N_SPLITS,
    "random_state": RANDOM_STATE,
    "baseline_oof_pearson": float(baseline_corr),
    "baseline_oof_rmse": baseline_rmse,
    "best_cv_mean_pearson": float(best_score),
    "oof_pearson": float(oof_pearson),
    "oof_rmse": oof_rmse,
    "r2": r2,
}
with model_path.open("wb") as f:
    pickle.dump({"base_model": base_full, "pca": final_pca, "residual_model": final_model, "meta": state}, f)

with (OUT_DIR / "best_meta.json").open("w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print("best model:", best)
print("cv best pearson:", best_score)
print("baseline oof pearson:", baseline_corr)
print("residual oof pearson:", oof_pearson)
print("residual oof rmse:", oof_rmse)
print("r2:", r2)
print("metrics:", metrics_path)
print("predictions:", pred_path)
