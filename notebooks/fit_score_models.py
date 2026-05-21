import json
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import ElasticNetCV, RidgeCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.svm import SVR


data_path = Path("notebooks/data.pkl")
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

with data_path.open("rb") as f:
    X, y = pickle.load(f)

X = np.asarray(X, dtype=np.float64)
y = np.asarray(y, dtype=np.float64)

test_size = 0.15
random_state = 7
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
    "pca50_ridge": make_pipeline(StandardScaler(), PCA(n_components=50, random_state=random_state), RidgeCV(alphas=alphas)),
    "pls25": make_pipeline(StandardScaler(), PLSRegression(n_components=25)),
    "elastic_net": make_pipeline(
        StandardScaler(),
        ElasticNetCV(
            l1_ratio=[0.05, 0.1, 0.25, 0.5, 0.75, 0.9],
            alphas=np.logspace(-4, 1, 20),
            cv=5,
            max_iter=20000,
            random_state=random_state,
        ),
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
    "random_forest": RandomForestRegressor(n_estimators=500, min_samples_leaf=3, random_state=random_state, n_jobs=-1),
    "extra_trees": ExtraTreesRegressor(n_estimators=500, min_samples_leaf=3, random_state=random_state, n_jobs=-1),
}

rows = []
preds = pd.DataFrame({"idx": idx_test, "y": y_test})

for name, model in models.items():
    print(f"fitting {name}")
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

metrics_path = results_dir / "embedding_score_fit_metrics.csv"
preds_path = results_dir / "embedding_score_fit_predictions.csv"
meta_path = results_dir / "embedding_score_fit_meta.json"

metrics.to_csv(metrics_path, index=False)
preds.to_csv(preds_path, index=False)
with meta_path.open("w") as f:
    json.dump(
        {
            "data_path": str(data_path),
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
print(f"saved {metrics_path}")
print(f"saved {preds_path}")
print(f"saved {meta_path}")
