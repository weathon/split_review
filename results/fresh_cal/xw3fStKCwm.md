Here is my final consolidated review:

---

## Summary

The paper proposes using tensor-train (TT) low-rank decomposition to compress large point clouds, combined with a probabilistic training objective (Sliced Wasserstein + nearest-neighbor losses) that makes compression invariant to point ordering. It further exploits an implicit hierarchical structure in the TT representation to enable efficient approximate nearest-neighbor (ANN) search. The method is evaluated on MVTec anomaly detection (outperforming coreset subsampling at high compression ratios) and as a proof-of-concept ANN index on Deep1B.

## Strengths

- **Probabilistic training removes sensitivity to row ordering.** The paper identifies that standard TT decomposition is sensitive to the arbitrary enumeration of points in the matrix. By reinterpreting compression as density estimation and using the Sliced Wasserstein loss (Eq. 6) with gradient descent, the method becomes invariant to this ordering. This is a principled solution to a known limitation (Sec. "Sliced Wasserstein Loss").

- **Implicit hierarchical structure enables efficient ANN beam search.** The paper reveals that the TT format yields a natural hierarchical clustering tree, where centroids at any suffix of indices can be computed rapidly. This insight is leveraged for a beam-search ANN algorithm (Sec. 3.5), a genuinely novel connection between TT decomposition and efficient search.

- **Superior OOD detection at high compression ratios on MVTec.** At 100× and 1000× compression, the TT point cloud achieves better pixel-level precision-recall metrics than coreset subsampling, with the gap widening at higher compression (Table 1). This is the primary empirical evidence that the compressed representation preserves the distribution well for OOD detection.

- **Better bucket distribution for ANN indexing than GNO-IMI.** On the Deep1B subset, the TT-based index yields roughly 6× fewer empty buckets and a lower expected bucket size (at rank 32, only 21% of GNO-IMI's value), as shown in Figures 5–6. This demonstrates more uniform database coverage, a desirable property for second-stage search.

- **Memory complexity analysis.** The paper derives the parameter count as O(D·N₁·r + k·r²·N_max), contrasting with O(ND) for the full dataset, providing theoretical justification for the potential exponential memory savings.

## Weaknesses

### Fatal

None.

### Major

- **ANN evaluation is too preliminary to support claims of practical advantage.** The paper explicitly calls this a "proof-of-concept" (line 190), uses only a 10M subset of Deep1B, reports no end-to-end query latency or throughput, and compares only to GNO-IMI (2016) without modern baselines (FAISS IVF, HNSW). While the bucket-distribution analysis is informative, it does not establish that TT indexing can compete with or outperform existing ANN methods in practice. The contribution to ANN therefore remains suggestive rather than demonstrated.

- **No ablation isolating the source of improvement in OOD detection.** The comparison matches memory/parameter count, but not point count — at 1% subsampling, TT encodes ~65K virtual points (with N₁=1024, N₂=64) while coreset stores roughly 1K original vectors. Without controlling for point count (e.g., comparing TT to a coreset with the same number of points, or to K-means centroids at the same memory budget), it is unclear whether the gains stem from the TT representation quality, the training losses, or simply denser coverage of the space. This limits attribution of the improvement.

### Minor

- **No per-dataset breakdown or variance for MVTec.** The paper reports only aggregate metrics (mean across 15 sub-datasets). Given the known difficulty variation across MVTec sub-datasets (e.g., hazelnut vs. carpet), per-dataset results and confidence intervals (over multiple seeds or splits) would substantially strengthen the evaluation and help assess robustness.

- **Hierarchical search algorithm is underspecified.** Section 3.5 describes the tree structure but provides no details on how the K candidates are selected at each level, what beam width is used, or the computational complexity of the search. This limits reproducibility.

- **No ablation on sensitivity to TT rank r or factorization (N₁, N₂).** The paper fixes these hyperparameters across all MVTec datasets (good practice for avoiding overfitting), but does not explore how performance varies with these choices, which would help guide practitioners applying the method to new domains.

- **No comparison with other tensor decomposition formats (Tucker, CP) to motivate the choice of TT.** The paper states TT was chosen for "efficiency and computational synergies" (line 44) but provides no comparative evidence.

### Trivial

None.

## Nice-to-Haves

- Report inference time per query for OOD detection (TT vs. coreset) to clarify the practical speed trade-off of having more virtual points.
- For ANN evaluation, provide end-to-end recall vs. queries-per-second curves with a modern baseline (FAISS IVF).
- Sensitivity analysis of the loss-balancing hyperparameter α (Eq. 10).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unfair comparison due to unequal point counts"** — REMOVED. Matching memory/parameter count is the standard and meaningful compression benchmark. TT's ability to encode more synthetic points within the same memory budget is a feature, not an artifact. The inference-time concern is moved to Nice-to-Haves.
- **"Missing training details (learning rate, optimizer, α value)"** — REMOVED. These details likely resided in the appendix, which was stripped during parsing per venue format.
- **"Baseline GNO-IMI setting unverified"** — REMOVED. The paper (lines 209–211) explicitly describes adapting the index size from 2¹⁴ to 2¹⁰ for the 10M subset, a reasonable scaling.
- **"Expected bucket size metric is crude"** — REMOVED. This is a standard proxy metric for indexing evaluation; the paper uses it appropriately.
- **"Advantage could be artefact of bucket assignment strategy"** — REMOVED. Speculative, no evidence provided.
- **"Comparison to random subsampling, K-means centroids"** — This was mentioned in a criticism but is redundant with the ablation concern already listed as a Major weakness above; the core point (need for controlled baseline) is merged there.

## Novel Insights

The most insightful observation that emerges from reading the reviews against the paper is that the hierarchical structure of TT decomposition has a novel dual role: it is at once the mechanism for compression (through low-rank factorization) and the mechanism for efficient search (through the implicit multi-level cluster centroids). Most prior work on TT in ML treats it purely as a parameterization device; this paper's recognition that the factorization yields a usable clustering hierarchy is a genuinely fresh perspective. The probabilistic reformulation (SW loss) to dodge the ordering sensitivity is also a clever adaptation that could be applied to other matrix-compression problems where row permutation is arbitrary.

## Suggestions

1. **Strengthen the OOD evaluation by adding an ablation.** Compare TT against: (a) a coreset with the same number of points (not just same memory) as the TT cloud; (b) K-means centroids at equal memory; (c) random subsampling at equal memory. This would cleanly isolate whether TT's advantage comes from representation quality, training losses, or point density.

2. **Provide per-dataset results for MVTec** (at least as a supplementary table) to demonstrate that the improvement holds across the diverse sub-datasets.

3. **Either substantially strengthen the ANN evaluation** (add FAISS IVF baseline, queries-per-second vs. recall curves, larger dataset fraction) **or scope the ANN contribution down** to a "preliminary observation about bucket distributions" to avoid over-claiming.

4. **Specify the hierarchical search algorithm** (beam width, candidate selection mechanism, complexity analysis) to improve reproducibility.

5. **Add a brief sensitivity study** showing how performance varies with rank r and factorization hyperparameters (N₁, N₂) on one representative MVTec sub-dataset.

## Score and Decision

**Originality:** Strong — the probabilistic reinterpretation of TT compression and the hierarchical structure insight are both novel.

**Importance of research question:** High — efficient point cloud storage and retrieval is central to many ML applications.

**Claims supported:** Partially — the OOD detection claims are reasonably supported, but the attribution of improvement is incomplete, and the ANN claims are too preliminary to be convincing.

**Soundness of experiments:** Moderate — the MVTec comparison is well-designed (matching memory, fixed hyperparameters across datasets) but lacks ablations and per-dataset detail. The ANN evaluation is a proof-of-concept with limited evidence.

**Clarity of writing:** Clear — the method is well-motivated and the key ideas are explained effectively, though the hierarchical search section is underspecified.

**Value to community:** Moderate positive — the core idea is likely to inspire further work on TT-based point cloud representations, even if the current evaluation is incomplete.

**Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>