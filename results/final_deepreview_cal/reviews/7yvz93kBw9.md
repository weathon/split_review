Now I have all the information I need. Let me synthesize the final review.

## Calibration Report

**Round 1 (bracketing):** Three queries covering weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands:
- Weak band anchors: GeoGS3D (3.40), 360-InpaintR (3.33), Distributionally Robust Surface Reconstruction (3.00), HIWE (3.00)
- Middle band anchors: RAIN-GS (5.75), FreeSplatter (5.00), IBGS (5.75), Geo-3DGS (5.00)
- Strong band anchors: NoPoSplat (8.00), STC-GS (8.00), TetSphere Splatting (7.60), LVSM (7.67)

**Round 1 bracket:** (4.5, 6.5) — the paper is clearly stronger than the weak-band papers but not at the strong-band level.

**Round 2 (narrowing):** Queried within (4.5, 6.0) and (6.0, 7.5):
- (4.5, 6.0): Hi-Gaussian (5.75), FreeSplatter (5.00), SCISplat (5.00), RAIN-GS (5.75)
- (6.0, 7.5): Ref-Gaussian (6.50), FDS (6.75), Lightweight Predictive 3DGS (7.00), HQGS (6.50)

Read in full: RAIN-GS (5.75, Reject), IBGS (5.75, Reject), HiSplat (6.00, Accept), Ref-Gaussian (6.50, Accept), FDS (6.75, Accept).

**Final score position:** The paper is substantively similar to RAIN-GS (5.75) — both propose simple-but-effective improvements to 3DGS with thorough ablations and consistent gains. D²GS has a clearer problem motivation (spatial imbalance analysis with concrete Gaussian counts), but it also has two substantive weaknesses that RAIN-GS does not: the DD-Drop interaction between P_i and r(t) is underspecified, and the IMR metric is claimed as a contribution without validation. I place the paper at 5.5 — slightly below RAIN-GS due to these gaps.

---

## Summary

This paper identifies two failure modes in sparse-view 3D Gaussian Splatting — near-field overfitting and far-field underfitting — and proposes D²GS, a framework with two complementary modules: a Depth-and-Density Guided Dropout (DD-Drop) mechanism that adaptively prunes overfitted Gaussians using local density and depth cues, and a Distance-Aware Fidelity Enhancement (DAFE) module that amplifies supervision in far-field regions via monocular-depth-derived masks. The paper also introduces an Inter-Model Robustness (IMR) metric based on optimal transport between Gaussian mixtures to quantify training stability. Experiments on LLFF and Mip-NeRF360 show consistent improvements over prior 3DGS-based methods.

## Strengths

- **Well-motivated diagnosis of sparse-view failure modes.** Section 3.1 provides concrete quantitative evidence (Gaussian counts: 11,450 vs. 6,112 for near-field; 3,082 vs. 5,224 for far-field) showing spatial imbalance under sparse views. This diagnosis directly motivates the two-module design and is backed by numbers, not just visual speculation.

- **Comprehensive ablation study isolating each component's contribution.** Table 4 incrementally adds density score, depth score, depth-based layering, and DAFE — each step improves PSNR, SSIM, LPIPS, and IMR. Table 5 ablates key hyperparameters (dropout rates, depth-density weights, DAFE threshold and loss weight), and Table 6 shows DAFE works with multiple monocular depth estimators. This level of component-level validation is strong evidence that the gains are not coincidental.

- **Consistent quantitative gains across two datasets.** D²GS outperforms DropGaussian by 0.59 dB (LLFF 1/8), 0.55 dB (LLFF 1/4), and 0.35 dB (Mip-NeRF360), and surpasses CoR-GS and LoopSparseGS by 0.9 dB and 0.5 dB respectively on LLFF. The gains are modest but consistent across settings.

## Weaknesses

### Major

1. **DD-Drop mechanism: interaction between per-Gaussian dropout probability \(P_i\) and global rate \(r(t)\) is underspecified, creating a reproducibility gap.** Equation (2) defines \(P_i\) as the "dropout rate" of each Gaussian, and Equation (3) introduces \(r(t)\) as a time-dependent global rate that "progressively increases the fraction of Gaussians discarded." The paper never states how these combine. Does \(r(t)\) set the fraction of Gaussians to drop, with \(P_i\) determining which ones (e.g., sort by \(P_i\) and drop the top \(r(t)\) fraction)? Or is \(P_i\) the actual dropout probability scaled by \(r(t)\)? Without this detail, the method cannot be reliably re-implemented. The ablation on \(r_{\min}\) and \(r_{\max}\) in Table 5 (bottom-left panel) shows performance varies with these values, reinforcing that the mechanism matters. This is fixable but requires explicit clarification or pseudocode.

2. **The IMR metric is presented as a contribution (third bullet in the contributions list) but lacks validation that it measures what it claims.** IMR is defined as \(\ln(\sum S_{ij}^2 / \sum S_{ij})\) — the log of a ratio of moments of pairwise mixture-Wasserstein distances between independently trained models. The paper provides no evidence that lower IMR actually correlates with meaningful robustness (e.g., correlation with run-to-run PSNR variance, or consistency across scenes). Table 3 only shows D²GS achieves the lowest IMR, but this is a circular argument if the metric favors the authors' method by construction. Without a validation experiment — for instance, showing that IMR ranks methods consistently with their rendering variance — the metric remains an unsubstantiated auxiliary claim. The authors should either validate IMR or de-emphasize it from a main contribution to a supplementary analysis.

### Minor

3. **Missing implementation details.** (a) The value of \(k\) in "estimated via k-nearest neighbors" (Sec. 3.2) is not stated, nor is the feature space (3D positions only?). (b) The depth score \(\tilde{d}_i\) uses "Euclidean distance to the camera" — in a multi-view setting, each Gaussian has a different distance to each camera; which distance is used (minimum, per-view averaged, gradient-weighted)? (c) The importance sampling for IMR (Sec. 3.4) mentions oversampling far-field Gaussians but does not specify the oversampling factor.

4. **No variance or confidence intervals on main rendering results.** Tables 1 and 2 report single numbers per method. Since the paper's central motivation is about robustness and training variance (Figure 3 left explicitly shows PSNR fluctuating across runs from 14.62 to 18.63), reporting mean ± std over multiple seeds for all compared methods would directly substantiate the stability claim.

5. **IMR is only reported on LLFF, not on Mip-NeRF360.** If IMR is a general-purpose robustness metric, it should be computed on both datasets. Its absence on Mip-NeRF360 weakens the claim of generality.

### Trivial

6. The phrase "previous methods generated 11,450 Gaussian primitives" (Sec. 3.1) should specify which method (DropGaussian, from the figure caption).

## Nice-to-Haves

- Reporting final Gaussian count distributions across depth would directly validate that DD-Drop actually rebalances spatial allocation (the paper's core claim).
- An ablation on the depth tertile thresholds (currently fixed at the first and second tertiles) would strengthen the global layering mechanism.
- A comparison with feed-forward methods (PixelSplat, MVSplat, HiSplat) on a subset of data would help situate the contribution in the broader sparse-view landscape.

## Removed Points

Points from the inputs that were filtered:

- **Harsh critic's claim that "the paper does not compare with most recent feed-forward methods"** — Retained in Nice-to-Haves but demoted because the paper explicitly scopes itself as an optimization-based method (built on DropGaussian), and the feed-forward vs. optimization distinction is a different paradigm; the paper's comparisons are appropriate for its category.

- **Strength Finder's claim that IMR is a strength** — Removed because the metric is unvalidated (see Weakness #2). A claimed contribution that lacks validity evidence cannot be listed as a strength.

- **Harsh critic's claim about "no analysis of the number of Gaussians after training"** — Placed in Nice-to-Haves. The paper motivates from Gaussian counts but doesn't close the loop by showing DD-Drop's effect on final distributions, which is a reasonable future direction.

- **Criticism about "the values \(\lambda_{\text{far}}=0.3, \lambda_{\text{middle}}=0.7\) are given as fixed"** — The paper explicitly states "based on experimental experience" and provides ablation on \(r_{\min}, r_{\max}\) in Table 5. This is standard practice; removing.

- **Criticism about "the IMR formula (Equation 14) is unusual and appears arbitrary"** — This is a judgment call, not a factual error. The formula is a specific design choice (log of ratio-of-moments). The real issue is lack of validation (covered in Major weakness #2), not the formula's aesthetics.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Provide a precise algorithmic description or pseudocode clarifying how \(P_i\) and \(r(t)\) interact in the dropout step.
- Either validate IMR with a correlation experiment (IMR vs. run-to-run PSNR variance across methods) or reframe it as a secondary analysis rather than a core contribution.
- Specify \(k\), the feature space for kNN density estimation, and how per-Gaussian depth is computed in the multi-view setting.
- Report mean ± std for the main PSNR/SSIM/LPIPS results across multiple seeds for all methods.

## Score and Decision

**Anchors used in calibration:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| I86z54CL2y (GeoGS3D) | 3.40 | 1 (weak) | Much weaker; method unclear, confuses feed-forward and optimization |
| R9lgWYE508 (RAIN-GS) | 5.75 | 1, 2 | Similar tier: simple modifications to 3DGS, clear ablations, but RAIN-GS had stronger empirical results and fewer reproducibility gaps |
| vkj5ARRCeY (IBGS) | 5.75 | 1 | Similar tier: geometry-focused, thorough ablation, some missing details (k sensitivity) |
| SBzIbJojs8 (HiSplat) | 6.00 | 2 | Slightly stronger: feed-forward method with clear motivation, accepted despite modest gains |
| xPxHQHDH2u (Ref-Gaussian) | 6.50 | 2 | Stronger: more novel technical contribution (PBR + inter-reflection), accepted |
| BzsjHiBfLk (FDS) | 6.75 | 2 | Stronger: novel use of matching priors, accepted despite limited evaluation scope |

**Round 1 bracket:** (4.5, 6.5) — the paper is clearly stronger than weak-band papers (3.0–3.5) but not at the strong-band level (7.5+).

**Round 2 narrowing:** Comparing against RAIN-GS (5.75) as the closest anchor, D²GS has a clearer problem motivation (spatial imbalance analysis with concrete counts) and more comprehensive ablations, but also has two substantive weaknesses that RAIN-GS does not: the DD-Drop implementation ambiguity and the unvalidated IMR metric claim. Score of 5.5 reflects that the paper has real contributions held back by gaps that would need to be resolved before the work can be fully trusted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>