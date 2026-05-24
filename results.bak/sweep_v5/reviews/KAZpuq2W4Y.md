Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that extends attention-based MIL by computing both first-order (attention-weighted mean) and second-order (scatter/covariance) moments of patch/cluster features, combined with DBSCAN-based adaptive clustering to reduce computational cost. The method is evaluated on CAMELYON16 and TCGA-NSCLC, reporting improvements over nine baselines.

## Strengths

- **Clear statistical motivation and principled framing**: The paper reframes ABMIL's attention-weighted pooling as first-order moment estimation (Section 3.1) and identifies the missing second-order statistics (feature covariance) as a natural extension. This framing is well-motivated and distinguishes the work from heuristic aggregation approaches. The statistical analogy provides a clear intellectual basis for the method.

- **Ablation study confirms incremental contribution of each component**: The ablation (Table 3) cleanly separates the contributions of clustering (CM) and second-order moments (SOM). The full model reaches ACC 96.98% vs. 95.98% without SOM and 95.72% without CM, demonstrating that both components add measurable value. The runtime reduction from 530s (w/o CM) to 310s (full) validates the efficiency claim for clustering.

- **Computational efficiency is demonstrated with clear numbers**: HOMIL's total 5-fold runtime on CAMELYON16 (310s) is substantially lower than most strong baselines (TransMIL 5175s, MambaMIL 7200s, HMIL 10800s), and this advantage is achieved alongside the highest reported metrics. On TCGA-NSCLC, HOMIL (3685s) is roughly 7× faster than MambaMIL (25200s).

## Weaknesses

### Fatal
None.

### Major

- **Baseline implementations produce anomalously low results, undermining SOTA claims**: Several baseline numbers are inconsistent with published performance, strongly suggesting implementation or tuning issues in the "unified codebase." On TCGA-NSCLC (Table 2), TransMIL achieves AUC 90.76% — far below Mean Pooling's 96.85%. On CAMELYON16 (Table 1), HMIL achieves AUC 94.44% while ABMIL and CLAM-SB both exceed 98%, and the ACC/AUC gap (96.19% vs. 94.44%) is atypical. These discrepancies indicate the baselines were not properly tuned, making it impossible to conclude that HOMIL achieves state-of-the-art results. The paper's central claim of "significant improvement over SOTA" is unsupported without credible baselines.

- **Covariance compression via 1D convolution lacks any validation**: The paper compresses a 512×512 covariance matrix into a 512-d vector using row-wise 1D convolution with T=4 kernels of size m=64 followed by two sequential max-pooling operations (Section 4.3.3). No ablation compares this to any alternative (e.g., flatten+linear projection, eigenvalue decomposition/pooling, diagonal-only features, spectral methods). Without such comparisons, there is no evidence that second-order information actually survives this compression — the pipeline could be destroying or distorting the signal. The parameter choices (m=64, T=4) are stated without justification.

- **No validation of the clustering module's core diagnostic claim**: The paper asserts that DBSCAN "adaptively forms large clusters for abundant normal tissues and small clusters for rare pathological regions" (Section 1, 4.2), but provides zero supporting evidence. There is no analysis of cluster size distributions, no visualization of which patches fall into which clusters, no quantification of cluster purity against tissue types, and no sensitivity analysis for DBSCAN's ε and minPts beyond a single heuristic. This foundational assumption — that clustering preserves diagnostic information — is unverified, and if clusters mix pathological and normal patches, the mean-pooling within clusters could destroy the signal second-order moments are meant to capture.

### Minor

- **The second-order representation's independent contribution is modest**: The ablation (Table 3) shows that removing the second-order moment module drops ACC from 96.98% to 95.98% (~1%) and F1 from 96.54% to 94.94% (~1.6%). While nonzero, this improvement is relatively modest given the substantial architectural complexity added (covariance computation, compression pipeline, second attention stream). The fusion weight analysis (Figure 2b) shows α⁽²⁾ ≈ 0.4–0.45, consistent with the second-order stream receiving less weight.

- **"Attention-weighted covariance" is a naming imprecision**: The covariance formula in Section 4.3.3 computes C = Σₖ (𝐠ₖ − 𝐯⁽¹⁾)(𝐠ₖ − 𝐯⁽¹⁾)ᵀ where 𝐯⁽¹⁾ = Σₖ aₖ·𝐠ₖ. The centering uses attention weights, but the sum itself gives every cluster equal weight regardless of attention score. Calling this an "attention-weighted covariance matrix" is imprecise — it is technically a scatter matrix centered at the attention-weighted mean. This does not invalidate the method (the computed quantity is still a valid second-order statistic), but the terminology mismatch between Sections 3.2 (which sets up the expectation-weighted formula) and 4.3.3 (which omits the weights) is confusing.

- **No statistical significance tests**: All comparisons report means ± standard error across 5-fold CV, but no significance tests (paired tests, bootstrapped differences, confidence intervals) are provided. Several comparisons have overlapping error bars (e.g., CAMELYON16 AUC: HOMIL 99.23±0.62 vs. S4MIL 99.02±0.87), making it unclear whether the claimed improvements are statistically reliable.

### Trivial

- The DBSCAN ε parameter is described as "the 65th percentile of nearest neighbor distances" — it would benefit from specifying which nearest neighbor (1st? k-th?) and the distance metric used.

## Nice-to-Haves

- Validate clustering quality empirically: report cluster size distributions, visualize cluster assignments on WSIs, analyze sensitivity to DBSCAN parameters.
- Provide a runtime breakdown to explain why HOMIL (310s) is faster than ABMIL (455s) despite additional operations (clustering, covariance computation, second stream).
- Compare the covariance compression method against alternatives (eigenvalue pooling, flatten+linear projection, diagonal-only features).
- Diagnose what the compressed second-order vector captures: compute cosine similarity between v⁽¹⁾ and v⁽²⁾ to check for redundancy vs. complementarity.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The covariance computation is fundamentally flawed" (Harsh Critic's Point 1)**: The critic claims the formula is "not a proper covariance matrix" and scales with the number of clusters. In fact, the paper computes a scatter matrix (sum of outer products), which is proportional to the unnormalized covariance. This is a standard quantity in multivariate statistics. The centering at the attention-weighted mean is unconventional but mathematically valid. The critic overstates this as "fatal"; it is best characterized as a naming imprecision (Minor).

2. **"The clustering efficiency claim rests on an assumption" (Harsh Critic's framing as a fatal issue)**: While the clustering validation is indeed missing (kept as a Major weakness above), the paper's efficiency claim is partially supported by the ablation — removing CM increases runtime from 310s to 530s, which empirically demonstrates the computational benefit regardless of cluster purity.

3. **Strength Finder's generic strengths about "importance of the problem" and "good motivation"**: These are not specific to the paper's execution and are dropped per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a key pattern common in WSI MIL papers: a methodologically interesting core idea whose evaluation is undermined by insufficiently validated baselines. The tension between the paper's clean statistical framing (moments of patch features) and the ad-hoc engineering choices (1D convolution compression, unverified clustering assumptions) is a recurring theme that the authors would need to resolve.

## Suggestions

1. **Fix the baseline implementations**: Verify that TransMIL, HMIL, and other baselines produce results consistent with their original publications (within expected variance). Report hyperparameter search ranges and selection criteria for every baseline. If the "unified codebase" produces different results, explain why.

2. **Add an ablation comparing covariance compression methods**: Compare the proposed 1D convolution against flatten+linear projection, eigenvalue pooling (e.g., sum of top-k eigenvalues), and diagonal-only features. This is essential to show that the second-order signal survives compression.

3. **Validate clustering empirically**: Include t-SNE/UMAP visualization of cluster assignments, cluster size distributions, and a WSI with patches colored by cluster label to confirm that DBSCAN separates pathological from normal regions.

4. **Include statistical significance tests**: Report bootstrapped AUC differences or paired tests for HOMIL vs. each baseline.

5. **Fix the covariance terminology**: Clarify that the scatter matrix uses unweighted outer products centered at the attention-weighted mean. If the intention was truly an attention-weighted covariance, correct the formula.

6. **Provide runtime breakdown**: Report per-component runtime (clustering, first-order aggregation, second-order computation, classification) to explain HOMIL's efficiency advantage.

## Score and Decision

**Calibration anchors** (all from deepreview_13k_calibration):

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0yVP49SDg0.md` (Mamba-HMIL, avg 3.25): Similar WSI MIL paper with baseline comparison concerns. The current paper has a stronger core idea (statistical motivation for second-order moments) but similar experimental weaknesses, making it slightly stronger (~0.25 pts).
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6xrDPHhwD3.md` (MFC, avg 6.00): Stronger paper with more novel multi-scale causal methodology and more thorough evaluation. The current paper is clearly weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/q1t0Lmvhty.md` (Covariance Pooling Theory, avg 6.00): Rigorous theoretical treatment of second-order features. The current paper is more applied and less rigorous.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YCdag94iZs.md` (MILCA, avg 3.50): Comparable quality — interesting core idea undermined by experimental/implementation issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/trj2Jq8riA.md` (VLSA, avg 5.67): Better-structured paper with more thorough evaluation. Current paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8vUcEqFGE1.md` (Bag-level MIL distance, avg 3.50): Similar tier of methodological interest with moderate experimental support.

The paper has a well-motivated core idea and clean ablation results, but the experimental evaluation is substantially weakened by baseline comparisons that are not credible (TransMIL AUC below Mean Pooling, HMIL AUC anomalies). The compression scheme and clustering claims lack necessary validation. Positioned relative to the anchors, this paper sits in the 3.0–4.0 range.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>