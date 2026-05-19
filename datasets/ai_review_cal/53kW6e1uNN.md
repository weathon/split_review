- Decision: Reject
- Avg Score: 6.50
- Scores: 8, 5, 5, 8
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper identifies feature over-correlation as a distinct and underexplored problem in GNN-based collaborative filtering, separate from the commonly studied over-smoothing issue. The authors provide empirical evidence that over-correlation is widespread in four GNN-CF models, theoretically prove a proportional relationship between row (node) and column (feature) correlation under double standardization, and propose AFDGCF — a model-agnostic framework that adaptively penalizes feature correlation per layer. Experiments on four base models across four datasets show statistically significant improvements in Recall, NDCG, and MAP, with additional benefits of faster convergence.

## Strengths
1. **Novel and well-motivated problem identification**: The paper draws a clear distinction between feature over-correlation (column-wise) and over-smoothing (row-wise), correctly noting that existing GNN-CF research has focused almost exclusively on the latter. The empirical demonstration in Figure 2 (Corr and SMV trends for LightGCN, GCCF, HMLET, NGCF) convincingly shows that over-correlation is a genuine, unaddressed problem in these models.

2. **Theoretical connection between over-correlation and over-smoothing**: Theorem 1 proves that under double standardization, \(\frac{1}{m}\|\mathbf{P_R}\|_F = \frac{1}{n}\|\mathbf{P_C}\|_F\), establishing a formal proportional relationship between row correlation (a proxy for smoothness) and column correlation (feature correlation). This provides a principled foundation that motivates why addressing feature de-correlation can simultaneously mitigate over-smoothing.

3. **Consistent and substantial empirical gains**: Table 2 reports statistically significant improvements (paired t-test, \(p<0.05\)) across all four base models and all four datasets, with gains as high as 12.31% Recall on Yelp (AFD-GCCF). The pattern is consistent — no model suffers degradation — which strongly supports the method's effectiveness.

4. **Training efficiency benefit**: Table 3 shows that AFDGCF not only improves accuracy but also reduces the number of epochs to reach optimal performance, sometimes by nearly half (e.g., LightGCN on Amazon-book: 742→360 epochs). This is a practical advantage beyond accuracy.

## Weaknesses

### Fatal
None.

### Major
- **Gap between theoretical result and evaluation metrics**: Theorem 1 proves a relationship between the Frobenius norms of the row-correlation matrix \(\mathbf{P_R}\) and column-correlation matrix \(\mathbf{P_C}\) under double standardization. However, the experimental metrics are SMV (normalized Euclidean distance between rows, Eq. 6) and Corr (average absolute Pearson correlation between columns, Eq. 4). The paper states that row correlation "can be considered as a proxy for measuring smoothness" (line 172), and column correlation "correspond[s] to the feature correlation" (line 135), but never formally connects \(\|\mathbf{P_R}\|_F\) to SMV or \(\|\mathbf{P_C}\|_F\) to Corr. The double standardization assumption is also acknowledged to be a simplification (line 137) but its impact on the result is not characterized. These gaps mean the theoretical contribution is more suggestive than the "pivotal connection" claimed in the abstract. Importantly, the empirical evidence (Figure 2) independently confirms the claimed relationship, so this weakness does not invalidate the core contribution — it is a gap between the paper's theoretical framing and the strength of what is actually proven.

### Minor
- **Adaptive weighting mechanism under-analyzed**: The adaptive strategy (Eq. 10, inversely proportional to per-layer correlation) is empirically validated in Table 4 (adaptive consistently outperforms fixed \(1/L\) weighting). However, the choice of *inverse* weighting (assigning lower penalties to deeper, higher-correlation layers) is not fully justified — one could equally ask why not penalize high-correlation layers *more* (proportional weighting). The paper does not analyze how the adaptive weights evolve during training, whether they converge, or provide insight into the mechanism by which constraining early-layer correlations propagates through the GNN. The \(1/L\) fixed baseline is also a weak comparator; per-layer tuned fixed weights would be stronger.

- **Standardized configuration may inflate some improvement magnitudes**: The paper standardizes all GNN models to 3 layers and 128-dim embeddings, and explicitly notes (line 311) that this configuration makes HMLET "contrary to its original design" unable to outperform LightGCN on most datasets. While standardizing is defensible and the pattern of improvements is consistent across all four base models, the absolute gains reported for HMLET (e.g., 12.03% on Yelp) may partly reflect running the base model in a suboptimal regime. An additional experiment showing AFDGCF at HMLET's originally recommended depth would clarify this.

### Trivial
None.

## Nice-to-Haves
- The paper could provide practical guidance for selecting \(\alpha\), since the ideal value spans several orders of magnitude across datasets (\(1e^{-5}\) to \(1e^{-2}\)) and large values cause training collapse.
- A brief wall-clock overhead analysis of the de-correlation loss computation would be useful, though Table 3 (epochs/second) already suggests ~10–15% overhead.

## Removed Points
- **Missing related works**: Not checked — I do not have external sources to confirm.
- **Speculative reproducibility concerns**: Any claim that cited models/tools "may not exist" or "cannot be independently verified" is removed. The paper uses RecBole, a well-known framework; the baselines are properly cited.
- **Request for sparser datasets**: The paper already uses datasets with densities \(8.4e^{-4}\) to \(3.8e^{-2}\); requesting an even sparser (<10 interactions threshold) dataset is scope creep.
- **"Theoretical analysis is the paper's weakest point" phrased as fatal**: The harsh critic's framing of this as potentially undermining the paper was disproportionate; it is a gap between framing and proof strength, not a fatal error, and the empirical evidence compensates.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Tighten the theoretical claim**: Acknowledge explicitly that Theorem 1 proves a relationship between \(\|\mathbf{P_R}\|_F\) and \(\|\mathbf{P_C}\|_F\), while SMV and Corr are the metrics used in practice. Either derive a bound connecting these pairs, or temper the language (e.g., "suggest a connection" rather than "establish a pivotal connection") and clearly let the empirical evidence carry the argument.
2. **Add a brief analysis of adaptive weight dynamics**: Even a single figure tracking per-layer \(\lambda\) values during training for one model-dataset pair would greatly improve understanding of why inverse weighting works.
3. **Run one additional experiment for HMLET**: Show AFDGCF results with HMLET at its original recommended depth to confirm the improvement is not an artifact of the standardized configuration.
