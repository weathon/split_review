import json
import os
import pickle
import re
from pathlib import Path
import time

import dotenv
import numpy as np
import pandas as pd
from openai import OpenAI
from scipy.stats import pearsonr
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.linear_model import ElasticNetCV, RidgeCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

MODEL_NAME = "qwen/qwen3-embedding-8b"
REVIEWS_DIR = Path("results/final_deepreview_cal/reviews")
SCORES_CSV = Path("results/final_deepreview_cal/scores.csv")
OUT_DIR = Path("results/final_deepreview_cal/ml_qwen8b_openrouter_embedding")
OUT_DIR.mkdir(parents=True, exist_ok=True)
BATCH_SIZE = 16
RANDOM_STATE = 7
N_SPLITS = 5
TASK_PROMPT = """Instruct: Encode this machine-learning paper review for predicting the paper's final ground-truth average review score on the 0-8 scale. Focus on the reviewer's assessment of novelty, correctness, experimental evidence, clarity, severity of weaknesses, calibration against anchor papers, and final recommendation. The first-round numeric prediction is supplied separately as a tabular feature, so do not infer it from metadata.
Query: """


def read_review(file_path):
    text = Path(file_path).read_text(encoding="utf-8")
    if "<score>" in text:
        text = text.split("<score>")[0]
    text = re.sub(r"MY FINAL SCORE:.*", "", text, flags=re.DOTALL)
    text = re.sub(r"MY FINAL DECISION:.*", "", text, flags=re.DOTALL)
    return text.strip()


dotenv.load_dotenv()
print("loading scores")
scores = pd.read_csv(SCORES_CSV)
scores["paper_id"] = scores["paper_id"].astype(str)
files = sorted(REVIEWS_DIR.glob("*.md"))

if len(files) < len(scores):
    raise ValueError(f"not enough review files {len(files)} for score rows {len(scores)}")

file_index = {p.stem: p for p in files}
missing_from_files = sorted(set(scores["paper_id"]) - set(file_index))
if missing_from_files:
    raise ValueError(f"missing review files: {missing_from_files}")

review_texts = [read_review(file_index[p]) for p in scores["paper_id"]]
pred_scores = scores["pred_score"].to_numpy(dtype=float)
gt_scores = scores["gt_avg_score"].to_numpy(dtype=float)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

embeddings = []
print(json.dumps({"event": "batch_start", "model": MODEL_NAME, "samples": len(review_texts)}, ensure_ascii=False))
for start in range(0, len(review_texts), BATCH_SIZE):
    batch = [TASK_PROMPT + text for text in review_texts[start : start + BATCH_SIZE]]
    print(json.dumps({"event": "sample_start", "start": start, "batch_size": len(batch)}, ensure_ascii=False))
    response = client.embeddings.create(
        extra_headers={
            "HTTP-Referer": "https://openrouter.ai/",
            "X-OpenRouter-Title": "split_review",
        },
        model=MODEL_NAME,
        input=batch,
        encoding_format="float",
    )
    embeddings.extend([item.embedding for item in response.data])
    print(json.dumps({"event": "sample_done", "start": start, "batch_size": len(batch)}, ensure_ascii=False))

print(json.dumps({"event": "batch_done", "model": MODEL_NAME, "samples": len(review_texts)}, ensure_ascii=False))

embeddings = np.asarray(embeddings, dtype=float)
np.savez_compressed(
    OUT_DIR / "embeddings.npz",
    paper_ids=scores["paper_id"].to_numpy(dtype=str),
    embeddings=embeddings,
    pred_scores=pred_scores,
    gt_scores=gt_scores,
)

if embeddings.shape[0] != len(gt_scores):
    raise ValueError("embedding count does not match score rows")
if embeddings.shape[1] < 2:
    raise ValueError("embedding dimension is too small to run PCA")

pca_candidates = [16, 32, 64, 128]
pca_max = min(embeddings.shape[1], embeddings.shape[0] - N_SPLITS)
pca_candidates = [d for d in pca_candidates if d <= pca_max]
if not pca_candidates:
    raise ValueError("not enough samples for PCA candidates")

pred_variants = {
    "pred_raw": lambda s: s[:, None],
    "pred_dup2": lambda s: np.column_stack([s, s]),
    "pred_sq": lambda s: np.column_stack([s, s * s]),
}

models = {
    "ridge": lambda: make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-4, 4, 17))),
    "elastic_net": lambda: make_pipeline(
        StandardScaler(),
        ElasticNetCV(
            l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9],
            alphas=np.logspace(-3, 3, 13),
            cv=3,
            max_iter=20000,
            random_state=RANDOM_STATE,
        ),
    ),
    "svr_rbf": lambda: make_pipeline(
        StandardScaler(),
        SVR(C=10, gamma="scale", epsilon=0.1),
    ),
    "random_forest": lambda: RandomForestRegressor(
        n_estimators=300,
        min_samples_leaf=2,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    ),
    "extra_trees": lambda: ExtraTreesRegressor(
        n_estimators=300,
        min_samples_leaf=2,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    ),
}

kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=RANDOM_STATE)
rows = []
best_score = -10.0
best_spec = None

for model_name, build_model in models.items():
    for pca_dim in pca_candidates:
        for pred_name, pred_builder in pred_variants.items():
            print("config", model_name, "pca", pca_dim, "pred", pred_name)
            fold_scores = []
            oof_pred = np.zeros(len(gt_scores), dtype=float)
            fold_mae = []

            for train_idx, val_idx in kf.split(embeddings):
                fold_start = time.time()
                x_tr = embeddings[train_idx]
                x_va = embeddings[val_idx]
                y_tr = gt_scores[train_idx]
                y_va = gt_scores[val_idx]
                pca_dim_fold = min(pca_dim, x_tr.shape[0] - 1)
                if pca_dim_fold < 1:
                    raise ValueError(f"invalid PCA dim {pca_dim_fold} for fold train size {x_tr.shape[0]}")
                pca = PCA(n_components=pca_dim_fold, random_state=RANDOM_STATE)
                x_tr_pca = pca.fit_transform(x_tr)
                x_va_pca = pca.transform(x_va)
                pred_tr = pred_builder(pred_scores[train_idx])
                pred_va = pred_builder(pred_scores[val_idx])
                x_tr_cat = np.hstack([x_tr_pca, pred_tr])
                x_va_cat = np.hstack([x_va_pca, pred_va])
                reg = build_model()
                reg.fit(x_tr_cat, y_tr)
                pred = reg.predict(x_va_cat).astype(float)
                oof_pred[val_idx] = pred
                corr = pearsonr(y_va, pred).statistic
                fold_scores.append(float(corr))
                mse = mean_squared_error(y_va, pred)
                fold_mae.append(float(mse**0.5))
                print("  fold", len(fold_scores), "corr", round(corr, 4), "time", round(time.time() - fold_start, 2))

            mean_corr = float(np.mean(fold_scores))
            mean_rmse = float(np.mean(fold_mae))
            rows.append(
                {
                    "model": model_name,
                    "pca_dim": int(pca_dim),
                    "pred_variant": pred_name,
                    "mean_pearson": mean_corr,
                    "mean_rmse": mean_rmse,
                }
            )
            if mean_corr > best_score:
                best_score = mean_corr
                best_spec = {
                    "model": model_name,
                    "pca_dim": pca_dim,
                    "pred_variant": pred_name,
                }

metrics = pd.DataFrame(rows).sort_values("mean_pearson", ascending=False).reset_index(drop=True)
if metrics.empty:
    raise ValueError("no model variants were evaluated")

if best_spec is None:
    raise ValueError("best configuration was not selected")

metrics_path = OUT_DIR / "cv_metrics.csv"
metrics.to_csv(metrics_path, index=False)

best = best_spec
best_model = models[best["model"]]()
best_pred_fn = pred_variants[best["pred_variant"]]

final_pca = PCA(n_components=best["pca_dim"], random_state=RANDOM_STATE)
reduced = final_pca.fit_transform(embeddings)
full_x = np.hstack([reduced, best_pred_fn(pred_scores)])
full_model = best_model.fit(full_x, gt_scores)

oof = np.zeros(len(gt_scores), dtype=float)
for train_idx, val_idx in kf.split(full_x):
    final_pred = best_pred_fn(pred_scores)
    pca_dim_fold = min(best["pca_dim"], len(train_idx) - 1)
    if pca_dim_fold < 1:
        raise ValueError(f"invalid PCA dim {pca_dim_fold} for OOF fold train size {len(train_idx)}")
    pca_cv = PCA(n_components=pca_dim_fold, random_state=RANDOM_STATE)
    x_tr = embeddings[train_idx]
    x_va = embeddings[val_idx]
    x_tr_pca = pca_cv.fit_transform(x_tr)
    x_va_pca = pca_cv.transform(x_va)
    pred_tr = final_pred[train_idx]
    pred_va = final_pred[val_idx]
    tr_x = np.hstack([x_tr_pca, pred_tr])
    va_x = np.hstack([x_va_pca, pred_va])
    tr = models[best["model"]]()
    tr.fit(tr_x, gt_scores[train_idx])
    oof[val_idx] = tr.predict(va_x)

best_pearson = pearsonr(gt_scores, oof).statistic
best_mae = float((np.mean((gt_scores - oof) ** 2) ** 0.5))
r2 = float(r2_score(gt_scores, oof))

predictions = pd.DataFrame(
    {
        "paper_id": scores["paper_id"],
        "gt_avg_score": gt_scores,
        "pred_score": pred_scores,
        "oof_pred": oof,
    }
)
pred_path = OUT_DIR / "oof_predictions.csv"
predictions.to_csv(pred_path, index=False)

model_path = OUT_DIR / "best_model.pkl"
state = {
    "model_name": MODEL_NAME,
    "scores_csv": str(SCORES_CSV),
    "pca_components": best["pca_dim"],
    "pred_variant": best["pred_variant"],
    "best_model_name": best["model"],
    "n_splits": N_SPLITS,
    "random_state": RANDOM_STATE,
    "best_pearson": best_pearson,
    "best_mae": best_mae,
    "r2": r2,
}
with model_path.open("wb") as f:
    pickle.dump({"pca": final_pca, "model": full_model, "meta": state}, f)

with (OUT_DIR / "best_meta.json").open("w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print("best model:", best)
print("best pca dim:", best["pca_dim"])
print("best pred variant:", best["pred_variant"])
print("cv best pearson:", best_score)
print("oof pearson:", best_pearson)
print("oof rmse:", best_mae)
print("r2:", r2)
print("metrics:", metrics_path)
print("predictions:", pred_path)
