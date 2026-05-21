Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary
This paper proposes **CorreGen**, a generative framework for multi-view clustering under noisy correspondence (NC). It formulates correspondence learning as maximum likelihood estimation over latent cross-view alignments via an EM algorithm. The E-step infers soft correspondences by solving an entropy-regularized optimal transport problem with GMM-derived marginals and a virtual sample mechanism for outliers; the M-step updates the embedding network. Experiments on four datasets with synthetic and real noise show consistent improvements over seven baselines, with particularly large gains at high noise levels.

## Strengths

1. **Principled generative formulation for noisy correspondence in MVC.** The paper shifts from discriminative contrastive objectives to a generative maximum likelihood formulation (Eq. 3), solved via EM. The M-step objective (Eq. 8) directly maximizes the expected log-likelihood under inferred correspondences. **Proposition 2** further shows that standard InfoNCE emerges as a special case when marginals are uniform and the posterior degenerates — a clean theoretical unification of the generative and contrastive views.

2. **Clearly defined taxonomy of noise types.** The paper formalizes two distinct failure modes: *category-level mismatch* (Definition 1) and *sample-level mismatch* (Definition 2). These definitions are not merely taxonomic; they directly inform the method design — GMM-guided marginals handle category-level relations while the virtual sample mechanism absorbs unalignable outliers.

3. **Strong empirical results under extreme noise.** At MR=80% on Caltech101, CorreGen achieves ACC=64.74, outperforming the best baseline (CANDY, 54.17) by over 10 points. On UMPC-Food101 at MR=50%, the margin is even larger (ACC=42.57 vs. DIVIDE 25.21). These gains persist when both mismatch and corruption are present (Table 2, e.g., MR=0.5, CR=0.5 on Scene15: ACC=36.19 vs. CANDY 29.44). The method was evaluated on a real-world noisy dataset (UMPC-Food101) where web-crawled pairs contain natural noise, adding ecological validity.

4. **Empirical verification that the method discovers class-level correspondences.** Figure 3 tracks the estimated posterior distribution over training epochs, showing evolution from a sparse diagonal to a block-diagonal structure that progressively matches ground-truth category-level correspondences. This directly visualizes the method's core mechanism.

## Weaknesses

### Fatal
None.

### Major

1. **GMM marginal stability is not analyzed.** The GMM is fitted to the current encoder's embeddings, which are themselves being learned. The paper acknowledges a momentum update (line 185) and shows posterior evolution in Figure 3, but does not track GMM cluster purity over training or compare to an oracle-marginal variant. Since the GMM-derived marginals (Eq. 13–14) directly constrain the OT coupling, early unreliable marginals could in principle propagate errors. An ablation with uniform marginals would help isolate the GMM's contribution. This does not invalidate the results — the EM framework often tolerates poor early estimates — but the claimed benefit of GMM guidance is not fully substantiated.

### Minor

2. **Missing variance / standard deviations.** The paper reports "mean of five individual runs" (Table 1 caption) but does not include standard deviations or confidence intervals. Some improvements are modest (e.g., <1 ACC point on LandUse21 at MR=0%), making it difficult to assess statistical significance. Standard reporting practice for this community includes variance.

3. **The realignment strategy for baselines is underspecified.** The paper states "we apply a view realignment strategy to the learned representations following prior studies (Guo et al., 2024; Sun et al., 2025), where realignment is consistently performed within batches of 512" (Section 4.1). A brief description of what this strategy entails (clustering-based reassignment? reordering?) would improve reproducibility. It is cited to prior work, so this is not a fairness concern, but clarity would benefit readers.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the full method to a variant with uniform marginals (no GMM guidance) would directly demonstrate the value of the GMM component.
- A sensitivity analysis of the virtual sample parameter ρ (could be as simple as reporting its chosen value and showing that performance is stable over a reasonable range).

## Removed Points

- **Virtual sample parameter ρ not specified:** The paper defers hyperparameter analysis to Appendix E. Per policy, criticisms predicated on missing appendix content that exists in the original submission are removed.
- **Comparison fairness and base model attribution concerns:** The realignment strategy follows prior work and the base model (DIVIDE) is clearly stated. Criticisms that speculate about unfairness or question what is retained/changed from DIVIDE without evidence from the paper are removed.
- **Derivation denotation issues (correlation function s, entropy λ, constant A):** These are standard design choices in optimal transport formulations (cosine similarity for s, regularization for λ, padding constant for A). No substantive omission.
- **Missing related works:** Per policy, cannot be raised without external verification.
- **Reproducibility concerns about implementation details deferred to appendix:** Standard practice; removed per policy.
- **Generic scope-creep criticisms** (e.g., requesting theoretical convergence proofs for an empirical method, or analysis of non-Gaussian clusters): Removed as outside the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add standard deviations** to all tables to enable readers to assess the significance of the reported improvements.
2. **Include an ablation with uniform marginals** (i.e., removing GMM guidance) to isolate whether the GMM component is responsible for the gains or whether the OT+virtual sample mechanism alone drives performance.
3. **Briefly describe the realignment strategy** used for baselines, even if it follows prior work, to avoid ambiguity.
4. **State ρ explicitly** (or the heuristic used to set it) in the main text rather than deferring entirely to the appendix.

## Score and Decision

### Calibration Report

**Round 1 (bracketing):** Three queries spanning score bands `(-1, 3.5)`, `(3.5, 7.5)`, and `(7.5, 11)` on topics related to multi-view clustering, noisy correspondence, and generative clustering.

- Weak anchors (avg 3.0–3.4): Papers withdrawn or rejected with thin contributions. Clearly exceeded by the current paper.
- Middle anchors (avg 4.4–7.0): **Coresets for Clustering with Noisy Data** (avg 5.5, Reject — straightforward calculations, limited novelty); **M3C: Mixture Graph Matching and Clustering** (avg 7.0, Accept Poster — solid MM framework with convergence guarantees, narrower evaluation); **TDSM: Label-Noise Robust Diffusion Models** (avg 5.75, Accept Poster — similar empirical rigor, missing baselines criticism); **PRO-DSC: Deep Subspace Clustering** (avg 6.25, Accept Poster — strong theory, incremental novelty concerns).
- Strong anchors (avg 8.0+): Oral/spotlight papers with comprehensive experiments and novel theoretical or architectural contributions. The current paper does not reach this tier.

**Round 2 (narrowing):** Additional anchors from `(4.5, 6.5)`, `(6.0, 8.0)`, and `(5.0, 7.0)` bands: **Contrast with Aggregation** (avg 6.0, Reject — theoretical gaps); **U-NOT Barycenters** (avg 6.25, Accept Poster — novel but incremental); **Fair Clustering via Alignment** (avg 6.0, Reject); **Robust Barycenter Estimation** (avg 6.25, Accept Poster).

**Initial bracket: 5.5–7.0.** After narrowing: CorreGen is stronger than Coresets (5.5) and Contrast with Aggregation (6.0), comparable to PRO-DSC (6.25) and U-NOT Barycenters (6.25), and slightly below M3C (7.0) which had formal convergence guarantees. Its thorough evaluation across multiple noise settings and real-world data, combined with the clean theoretical unification with InfoNCE, place it squarely in the **6.0–6.5** range.

**Final score: 6.5** — a solid paper with a clear contribution, well-executed experiments, and one unresolved analytical gap (GMM stability) that does not threaten the core claim but would strengthen the paper if addressed.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>