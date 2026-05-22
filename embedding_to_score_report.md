# DeepSeek review embeddings → gt_avg_score

**Question:** Can we predict a paper's ground-truth average score from the embedding of DeepSeek's review better than just reading the `pred_score` DeepSeek already wrote?

**Data:** 391 `deepseek_flash` rows from `datasets/iclr2026_model_reviews_hf`. Each `paper_review` embedded with `google/gemini-embedding-2-preview` via OpenRouter (3072-dim), cached in `deepseek_embeddings.pkl`.

**Baseline:** raw `pred_score` vs `gt_avg_score`.

## Scripts
- `embed_deepseek_tsne.py` — embed + cache + t-SNE plot (`deepseek_tsne.png`)
- `embed_to_score_ml.py` — single-split model sweep (PCA + expanded pred_score features)
- `cv_best_model.py` — repeated k-fold CV of the best config vs baseline

## What we tried, in order

1. **t-SNE of embeddings, colored by gt_avg_score** → no score structure; high/low scores fully mixed.
2. **Regressors on raw 3072-dim embedding** (Ridge/SVR/RF/GB/KNN/PLS) → best (SVR) 0.64 < baseline 0.71 on the seed-0 split. Embedding alone recovers less than the explicit score.
3. **Concat raw `pred_score` as one feature** → only tree models benefited (RF 0.76); scaled models still buried it among 3072 dims.
4. **Up-weight `pred_score`** → kernel/distance models (SVR/KNN) climbed to ~0.72 at high weight; Ridge plateaued ~0.61 (linear shrinkage).
5. **PCA(emb) + nonlinear expansion of pred_score** (p, p², p³, √p, cumulative score≥b bins) → balanced the dimension ratio; on the seed-0 split GradBoost@PCA50 hit 0.763, RF 0.759, even Ridge back to ~0.71.

## The catch: single splits lied

All numbers above are one n=98 test split (seed 0). The seed-0 baseline (0.709) was a lucky subset.

**5×5-fold CV on the best config (GradBoost, PCA=50 + expanded pred_score):**

| | Pearson | Spearman |
|---|---|---|
| BASELINE `pred_score` (full data) | **0.657** | **0.625** |
| Model (out-of-fold) | 0.617 ± 0.016 | 0.583 ± 0.018 |
| Δ | **−0.039** | −0.042 |

## Conclusion

**The embedding adds no usable signal beyond `pred_score`.** Under proper CV the best learned model is *systematically* ~0.04 below the baseline (tight ±0.016, so the gap is real, not noise). The seed-0 win was an artifact of the lucky split.

This is consistent with the t-SNE: the review text's semantic space is not organized by ground-truth quality. DeepSeek's own emitted scalar score is already the best distillation of its quality judgment; re-extracting that judgment from prose only dilutes it.
