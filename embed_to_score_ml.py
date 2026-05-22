import pickle
import numpy as np
from datasets import load_from_disk
from scipy.stats import pearsonr, spearmanr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

ds = load_from_disk("datasets/iclr2026_model_reviews_hf").filter(lambda x: x["review_model"] == "deepseek_flash")
gt = np.array(ds["gt_avg_score"], dtype=float)
pred = np.array(ds["pred_score"], dtype=float)

with open("deepseek_embeddings.pkl", "rb") as f:
    emb = np.array(pickle.load(f))
assert len(emb) == len(gt)
print(f"emb={emb.shape}, y={gt.shape}")

idx = np.arange(len(gt))
tr, te = train_test_split(idx, test_size=0.25, random_state=0)
ytr, yte = gt[tr], gt[te]

def report(name, yhat):
    r = pearsonr(yte, yhat)[0]
    rho = spearmanr(yte, yhat)[0]
    print(f"{name:30s} pearson={r:.3f}  spearman={rho:.3f}")
    return r

# method 2: expand the scalar pred_score into several nonlinear features,
# z-scored so they sit on the same scale as the PCA components.
def score_feats(p):
    bins = np.array([2, 3, 4, 5, 6, 7])  # cumulative "score >= b" indicators
    return np.column_stack([p, p ** 2, p ** 3, np.sqrt(p)] + [(p >= b).astype(float) for b in bins])

report("BASELINE raw pred_score", pred[te])

for n_pca in [20, 50, 100]:
    print("-" * 55, f"PCA dim = {n_pca}")
    pca = PCA(n_components=n_pca, random_state=0).fit(emb[tr])
    Ztr, Zte = pca.transform(emb[tr]), pca.transform(emb[te])

    sf = StandardScaler().fit(score_feats(pred[tr]))
    Str = sf.transform(score_feats(pred[tr]))
    Ste = sf.transform(score_feats(pred[te]))

    se = StandardScaler().fit(Ztr)
    Xtr = np.hstack([se.transform(Ztr), Str])
    Xte = np.hstack([se.transform(Zte), Ste])

    models = {
        "Ridge(a=10)": Ridge(alpha=10.0),
        "Ridge(a=100)": Ridge(alpha=100.0),
        "SVR(rbf)": SVR(C=10.0),
        "KNN(15)": KNeighborsRegressor(n_neighbors=15, weights="distance"),
        "RandomForest": RandomForestRegressor(n_estimators=400, random_state=0, n_jobs=-1),
        "GradBoost": GradientBoostingRegressor(random_state=0),
    }
    for name, m in models.items():
        m.fit(Xtr, ytr)
        report(name, np.ravel(m.predict(Xte)))
