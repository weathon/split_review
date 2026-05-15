Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes representing high-dimensional point clouds via tensor-train (TT) low-rank decomposition, trained with a probabilistic interpretation using Sliced Wasserstein and nearest-neighbor distance losses to achieve ordering-invariant compression. The authors discover that TT-compressed point clouds naturally form a hierarchical structure (tree of centroids) that enables efficient approximate nearest-neighbor search via beam search. They demonstrate the method on MVTec AD for OOD detection (replacing coreset subsampling in PatchCore) and on a subset of Deep1B for ANN search (comparing against GNO-IMI). The core idea — treating TT compression as density estimation to sidestep the ordering problem — is conceptually clean and the hierarchical structure observation is original.

## Strengths

- **Probabilistic re-interpretation of TT compression that eliminates ordering dependence.** The paper clearly identifies that standard TT-SVD/TT-cross approximations are highly sensitive to arbitrary row ordering in the point-cloud matrix (Section 2.1). By reframing compression as distribution matching via Sliced Wasserstein and NN-distance losses (Section 2.2–2.3), training becomes invariant to vector ordering — a genuine improvement over direct low-rank approximation of the matrix. This is well-motivated and cleanly presented.

- **Discovery that TT point clouds encode an inherent hierarchical clustering structure useful for ANN search.** The observation that TT format allows rapid computation of mean vectors along multi-index suffixes (forming a tree of centroids at different levels, Section 2.5) is original and leads naturally to a beam-search-style traversal. This structural insight is the paper's most distinctive contribution and could be valuable beyond the specific experiments shown.

- **OOD detection results show clear improvement over coreset subsampling at matched parameter counts.** On MVTec AD (15 subdatasets), at 100× and 1000× compression ratios, pixel-level metrics "heavily favor" TT compression over PatchCore's coreset subsampling, with the gap widening at higher compression rates (Section 3.2). The use of fixed hyperparameters across all 15 datasets demonstrates robustness.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated by any single issue.

### Major

- **The OOD comparison lacks baselines needed to attribute the advantage to TT structure.** The paper compares TT compression only against coreset subsampling at matched parameter count. The critic correctly notes this conflates two variables: (1) the TT decomposition structure and (2) the ability to place centroids at arbitrary positions (rather than only selecting from existing points). Baselines like k-means centroids, random subsampling, or product-quantization centroids at equal memory would be needed to establish that TT decomposition specifically — rather than any method with flexible centroid placement — is responsible for the improvement. The existing comparison is informative but insufficient to support the broader claim that TT compression is uniquely beneficial.

- **The ANN evaluation does not directly measure search efficiency, even as a proof-of-concept.** The paper reports only proxy metrics (expected bucket size, empty buckets, recall vs. short-list length R) but provides no wall-clock time, number of distance computations, or query throughput for the full pipeline (hierarchical beam search + exhaustive second stage). The paper acknowledges this limitation (Section 3.3: "focus on indirect characteristics"), but the claims of "efficient" ANN search and "advantages over GNO-IMI" are not supported by the evidence presented. The delta-recall curve (Fig. 8, referenced at line 237) shows TT's advantage is largest at low recall, with GNO-IMI overtaking near recall=1 — a regime the paper dismisses as a "small period" without justification. Until the search cost is directly measured, the practical advantage remains unclear.

- **The claim of "unbiased estimation" for the NN loss is technically incorrect.** The paper states (line 114) that subsampling the original point cloud for the NN loss yields an "unbiased estimation." However, computing the minimum over a random subset does **not** produce an unbiased estimate of the minimum over the full set, because the min operation is nonlinear. This is not acknowledged. While many papers use such approximations in practice, labeling it as unbiased is inaccurate and should be corrected.

### Minor

- **Training details are critically underspecified for reproducibility.** The paper does not report: number of Monte Carlo projections for the Sliced Wasserstein loss, learning rate, optimizer, schedule, number of iterations, batch size for the NN loss, initialization scheme for TT cores, or the specific value of α in Eq. 5. These details are standard to require and their absence makes it difficult to reproduce or build upon the method.

- **No statistical rigor (error bars, multiple seeds) reported for any experiment.** All results (MVTec, ANN) are presented as point estimates without variance. Given that TT core initialization and random subsampling for the NN loss introduce stochasticity, multi-run statistics with mean and standard deviation are necessary to assess reliability.

- **The expected bucket size heuristic (p_i = N_i/N) is unvalidated.** The analysis in Section 3.3 (Eq. 8) assumes the probability that a query's nearest neighbor falls in a bucket is proportional to the bucket's size. This is a heuristic and is not empirically verified against the actual distribution of nearest-neighbor assignments, which weakens the quantitative claims about expected search cost.

- **The "potential exponential memory advantage" claim is overstated for the experimental regime.** The paper states TT offers a "potential exponential memory advantage" (line 66) depending on hyperparameters. In practice, the experiments use moderate ranks (up to 96) and few factors (2–3 cores), yielding at best linear compression. This theoretical potential is technically correct but risks misleading readers about the method's practical savings.

### Trivial
- None that are not parser-induced artifacts.

## Nice-to-Haves
- Additional OOD baselines (k-means, product quantization, Faiss IVF) at equal memory would strengthen attribution of the advantage.
- End-to-end timing benchmarks for ANN search (wall-clock queries per second, number of distance computations) would elevate the proof-of-concept to a practical demonstration.
- Ablation of the loss components (SW only, NN only, with/without inverse NN, varying α) to understand their individual contributions.
- Sensitivity analysis of TT-rank and sample dimensions on both OOD and ANN performance.
- Validation of the p_i = N_i/N assumption by empirically measuring nearest-neighbor bucket assignments.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The central motivation (ordering invariance) is solved trivially without TT"** — Removed: strawman. The paper does not claim TT is the only way to achieve permutation invariance. The contribution is about *making TT compression work* for point clouds despite the ordering issue, not about solving permutation invariance in general. TT is the representational choice, and the distributional training is the solution to a TT-specific problem.

2. **"OOD comparison is structurally asymmetrical / unfair"** — Weakened/repackaged. The comparison at matched parameter count is a standard and valid experimental design. The critic's framing that coreset is "structurally disadvantaged" is incorrect — coreset has the advantage of preserving the exact empirical distribution; TT has the advantage of flexible centroid placement. Both are valid approaches and comparing them at equal memory is informative. The real issue (which we keep as a major weakness) is the lack of *additional* baselines to isolate the source of improvement.

3. **"ANN evaluation is misleading"** — Weakened. The paper explicitly calls it a "proof-of-concept" (three times: lines 190, 196, 288). The critic's charge of "misleading" is too harsh given these disclaimers. The core issue (no direct timing measurements) is kept as a major weakness but the framing is softened.

4. **"Hyperparameter selection contradiction"** — Removed. The paper says hyperparameters are chosen to match parameter count *and* the same hyperparameters are used across MVTec datasets. For a fixed subsample factor c, the authors can pick representative N1, N2, r that work across the range of N values. This is not a contradiction, just an underspecified detail.

5. **Claims about Figure/Table references not being shown** — Removed: parser artifact. The original submission includes these figures and tables; they are stripped during text extraction.

6. **"The hierarchical beam search is described in one paragraph with no algorithm/beam width"** — Kept as part of the training details underspecified weakness but downgraded. It's a minor exposition issue.

## Novel Insights

The reviews surface a key tension that the paper does not fully address: the probabilistic interpretation of TT compression is elegant and the hierarchical structure is genuinely novel, but the experimental evaluation consistently stops short of directly testing the claimed benefits. The OOD experiment shows improvement over a single (well-chosen) baseline but lacks the ablative controls to attribute that improvement to TT decomposition per se. The ANN experiment identifies an interesting structural property (implicit hierarchical centroids) but does not measure the actual search cost that this property is supposed to reduce. The paper's strongest contribution — the structural observation — is also its least empirically validated. This gap between the conceptual contribution and the experimental support is the paper's most salient weakness across both reviews.

## Suggestions

1. **Expand baselines for OOD:** Add k-means centroids and product-quantization centroids at equal memory budgets to isolate the source of TT's advantage over coreset subsampling.
2. **Measure actual ANN search cost:** Report wall-clock queries-per-second (or number of distance computations) for the full TT-based pipeline vs. GNO-IMI, including the cost of the hierarchical beam search itself.
3. **Add multi-run statistics:** Report all results with at least 5 random seeds (mean ± std) for both OOD and ANN experiments.
4. **Clarify training details:** Provide learning rate, optimizer, schedule, number of Monte Carlo projections, α values, initialization scheme, and batch size — ideally in a table in the appendix.
5. **Correct the "unbiased" claim** for the NN loss approximation and clarify the nature of the estimation bias.

## Score and Decision

The paper introduces a genuinely novel conceptual framing (probabilistic TT compression via distributional losses) and identifies an interesting structural property (hierarchical centroids in TT representations). These are real contributions. However, the experimental evaluation is significantly incomplete: the OOD comparison lacks the baselines needed to isolate the source of improvement, and the ANN evaluation stops short of measuring actual search performance, relying instead on proxy metrics. The training procedure is critically underspecified for reproducibility. These gaps are sizable but not fatal — the core ideas are sound and the paper's honest self-assessment (proof-of-concept, limitations section) mitigates some concerns. With major revisions — particularly additional baselines, direct timing measurements, and full training details — the paper could provide a solid contribution. In its current form, the evidence supports the conceptual claims only partially.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>