import pickle
import numpy as np
from datasets import load_from_disk
from scipy.stats import pearsonr, spearmanr
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingRegressor

ds = load_from_disk("datasets/iclr2026_model_reviews_hf").filter(lambda x: x["review_model"] == "deepseek_flash")
gt = np.array(ds["gt_avg_score"], dtype=float)
pred = np.array(ds["pred_score"], dtype=float)
with open("deepseek_embeddings.pkl", "rb") as f:
    emb = np.array(pickle.load(f))
print(f"n={len(gt)}, emb={emb.shape}")

def score_feats(p):
    bins = np.array([2, 3, 4, 5, 6, 7])
    return np.column_stack([p, p ** 2, p ** 3, np.sqrt(p)] + [(p >= b).astype(float) for b in bins])

N_PCA = 50
N_SPLITS = 5
N_REPEATS = 5  # repeat CV over seeds to get a stable mean + spread

oof_corrs, base_corrs = [], []
oof_sp, base_sp = [], []
for seed in range(N_REPEATS):
    oof = np.zeros(len(gt))
    kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=seed)
    for tr, te in kf.split(emb):
        pca = PCA(n_components=N_PCA, random_state=0).fit(emb[tr])
        se = StandardScaler().fit(pca.transform(emb[tr]))
        sf = StandardScaler().fit(score_feats(pred[tr]))
        Xtr = np.hstack([se.transform(pca.transform(emb[tr])), sf.transform(score_feats(pred[tr]))])
        Xte = np.hstack([se.transform(pca.transform(emb[te])), sf.transform(score_feats(pred[te]))])
        m = GradientBoostingRegressor(random_state=0).fit(Xtr, gt[tr])
        oof[te] = m.predict(Xte)
    oof_corrs.append(pearsonr(gt, oof)[0])
    oof_sp.append(spearmanr(gt, oof)[0])
    base_corrs.append(pearsonr(gt, pred)[0])
    base_sp.append(spearmanr(gt, pred)[0])

oof_corrs, oof_sp = np.array(oof_corrs), np.array(oof_sp)
print(f"\n{N_REPEATS}x{N_SPLITS}-fold CV  (GradBoost, PCA={N_PCA} + expanded pred_score)")
print(f"BASELINE pred_score   pearson={base_corrs[0]:.3f}   spearman={base_sp[0]:.3f}  (fixed, full data)")
print(f"MODEL  oof            pearson={oof_corrs.mean():.3f}±{oof_corrs.std():.3f}   spearman={oof_sp.mean():.3f}±{oof_sp.std():.3f}")
print(f"Δ pearson = {oof_corrs.mean() - base_corrs[0]:+.3f}")
