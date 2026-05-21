import json
import os
import pickle
from pathlib import Path

import dotenv
import numpy as np
import pandas as pd
from openai import OpenAI
from scipy.stats import pearsonr, spearmanr
from sklearn.decomposition import PCA
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import ElasticNet, RidgeCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.svm import SVR


dotenv.load_dotenv(".env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

review_dir = Path("results/fresh_cal")
csv_path = Path("results/fresh_cal.csv")
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

model_name = "google/gemini-embedding-2-preview"
n_samples = 1024
batch_size = 64
test_size = 0.15
random_state = 7

embedding_path = results_dir / "fresh_cal_gemini_embedding_2_preview_1024.pkl"
metrics_path = results_dir / "fresh_cal_embedding_score_fit_1024_metrics.csv"
preds_path = results_dir / "fresh_cal_embedding_score_fit_1024_predictions.csv"
meta_path = results_dir / "fresh_cal_embedding_score_fit_1024_meta.json"

df = pd.read_csv(csv_path).head(n_samples).copy()
if len(df) != n_samples:
    raise ValueError(f"expected {n_samples} rows in {csv_path}, found {len(df)}")
if df["gt_avg_score"].isna().any():
    raise ValueError("gt_avg_score has missing values")

contents = []
for paper_id in df["paper_id"]:
    path = review_dir / f"{paper_id}.md"
    if not path.exists():
        raise FileNotFoundError(path)
    contents.append(path.read_text())

if embedding_path.exists():
    with embedding_path.open("rb") as f:
        payload = pickle.load(f)
    if payload["model"] != model_name:
        raise ValueError(f"embedding cache model mismatch: {payload['model']}")
    if payload["paper_ids"] != df["paper_id"].tolist():
        raise ValueError("embedding cache paper_ids do not match current CSV slice")
    X = np.asarray(payload["embeddings"], dtype=np.float64)
else:
    embeddings = []
    for start in range(0, len(contents), batch_size):
        end = min(start + batch_size, len(contents))
        print(f"embedding {start}:{end}", flush=True)
        response = client.embeddings.create(
            model=model_name,
            input=contents[start:end],
            encoding_format="float",
        )
        batch_embeddings = [item.embedding for item in response.data]
        if len(batch_embeddings) != end - start:
            raise ValueError(f"embedding batch {start}:{end} returned {len(batch_embeddings)} embeddings")
        embeddings.extend(batch_embeddings)

        tmp_path = embedding_path.with_suffix(f".partial.{end}.pkl")
        with tmp_path.open("wb") as f:
            pickle.dump(
                {
                    "model": model_name,
                    "paper_ids": df["paper_id"].tolist()[:end],
                    "embeddings": embeddings,
                },
                f,
            )

    with embedding_path.open("wb") as f:
        pickle.dump(
            {
                "model": model_name,
                "paper_ids": df["paper_id"].tolist(),
                "embeddings": embeddings,
            },
            f,
        )
    X = np.asarray(embeddings, dtype=np.float64)

y = df["gt_avg_score"].to_numpy(dtype=np.float64)
all_idx = np.arange(len(y))
X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(
    X,
    y,
    all_idx,
    test_size=test_size,
    random_state=random_state,
)

alphas = np.logspace(-4, 4, 25)

models = {
    "mean": DummyRegressor(strategy="mean"),
    "ridge": make_pipeline(StandardScaler(), RidgeCV(alphas=alphas)),
    "ridge_l2_norm": make_pipeline(Normalizer(), RidgeCV(alphas=alphas)),
    "pca100_ridge": make_pipeline(StandardScaler(), PCA(n_components=100, random_state=random_state), RidgeCV(alphas=alphas)),
    "elastic_net": make_pipeline(
        StandardScaler(),
        ElasticNet(alpha=0.01, l1_ratio=0.1, max_iter=5000, random_state=random_state),
    ),
    "svr_rbf": make_pipeline(
        StandardScaler(),
        GridSearchCV(
            SVR(kernel="rbf"),
            param_grid={"C": [0.3, 1, 3, 10], "gamma": ["scale", 0.001, 0.01]},
            cv=5,
            scoring="neg_mean_absolute_error",
        ),
    ),
    "kernel_ridge_rbf": make_pipeline(
        StandardScaler(),
        GridSearchCV(
            KernelRidge(kernel="rbf"),
            param_grid={"alpha": [0.01, 0.1, 1, 10], "gamma": [0.0001, 0.001, 0.01]},
            cv=5,
            scoring="neg_mean_absolute_error",
        ),
    ),
    "random_forest": RandomForestRegressor(
        n_estimators=120,
        min_samples_leaf=3,
        max_features="sqrt",
        random_state=random_state,
        n_jobs=-1,
    ),
    "extra_trees": ExtraTreesRegressor(
        n_estimators=120,
        min_samples_leaf=3,
        max_features="sqrt",
        random_state=random_state,
        n_jobs=-1,
    ),
}

rows = []
preds = pd.DataFrame({"idx": idx_test, "paper_id": df.iloc[idx_test]["paper_id"].to_numpy(), "y": y_test})

for name, model in models.items():
    print(f"fitting {name}", flush=True)
    model.fit(X_train, y_train)
    pred = np.asarray(model.predict(X_test), dtype=np.float64).reshape(-1)
    preds[name] = pred
    rows.append(
        {
            "model": name,
            "mae": mean_absolute_error(y_test, pred),
            "rmse": mean_squared_error(y_test, pred) ** 0.5,
            "r2": r2_score(y_test, pred),
            "pearson": pearsonr(y_test, pred).statistic,
            "spearman": spearmanr(y_test, pred).statistic,
        }
    )

metrics = pd.DataFrame(rows).sort_values("mae")
metrics.to_csv(metrics_path, index=False)
preds.to_csv(preds_path, index=False)
with meta_path.open("w") as f:
    json.dump(
        {
            "csv_path": str(csv_path),
            "review_dir": str(review_dir),
            "embedding_model": model_name,
            "embedding_path": str(embedding_path),
            "n_samples": int(len(y)),
            "n_features": int(X.shape[1]),
            "test_size": test_size,
            "random_state": random_state,
            "train_n": int(len(y_train)),
            "test_n": int(len(y_test)),
            "test_indices": idx_test.tolist(),
        },
        f,
        indent=2,
    )

print(metrics.to_string(index=False))
print(f"saved {embedding_path}")
print(f"saved {metrics_path}")
print(f"saved {preds_path}")
print(f"saved {meta_path}")
