Now I have all the evidence needed. Let me produce the final consolidated review.

---

## Summary

This paper tackles the problem of sparse-view 3D Gaussian Splatting (3DGS), identifying two specific failure modes: near-field overfitting (excessive Gaussian density near the camera) and far-field underfitting (insufficient Gaussian coverage in distant areas). It proposes D²GS, a unified framework with two complementary modules: **(1)** a Depth-and-Density Guided Dropout (DD-Drop) that assigns spatially adaptive dropout probabilities to Gaussians based on local density and depth, combined with a global depth-based layering scheme; and **(2)** a Distance-Aware Fidelity Enhancement (DAFE) loss that uses monocular depth priors to construct a binary mask and amplify supervision in far-field regions. The paper also introduces an Inter-Model Robustness (IMR) metric based on 2-Wasserstein distance and optimal transport to quantify the stability of learned 3D Gaussian distributions across independent training runs. Experiments on LLFF and Mip-NeRF360 show consistent improvements over prior methods including DropGaussian, LoopSparseGS, and CoR-GS.

## Strengths

1. **Clear problem decomposition into two distinct failure modes.** The paper provides a concrete, quantitative analysis in Figure 1 showing that under sparse views, near-field regions accumulate an excess of Gaussians (11,450 vs. 6,112 for dense views in DropGaussian) while far-field regions suffer from a deficit (3,082 vs. 5,224). This spatial imbalance is a well-motivated and underappreciated challenge, and it directly informs the two-module design.

2. **DD-Drop outperforms uniform dropout with a clearly validated design.** The ablation (Table 4) progressively adds density score, depth score, and depth-based layering to the 3DGS baseline, improving PSNR from 19.22 to 21.17. Each component contributes positively, and the full DD-Drop outperforms the uniform-dropout baseline (DropGaussian) by 0.59 dB on LLFF 1/8 and 0.35 dB on MipNeRF360 (Tables 1, 2). The hyperparameter sensitivity analysis (Table 5) further tests dropout rates, score weights, mask thresholds, and loss weights, supporting the design choices.

3. **DAFE module provides a targeted solution to far-field underfitting with consistent depth-estimator robustness.** Adding DAFE on top of the full DD-Drop improves PSNR from 21.17 to 21.35 and IMR from 3.088 to 3.039. Table 6 shows DAFE works with three different monocular depth estimators (MiDas, DPT, DepthAnything V2), all outperforming the baseline, demonstrating robustness to the choice of depth prior.

4. **Comprehensive comparisons across two benchmarks with multiple competitive baselines.** Tables 1–2 compare against 6 NeRF-based methods and 6 3DGS-based methods, including recent strong baselines (LoopSparseGS, DropGaussian, CoR-GS). D²GS achieves the best PSNR, SSIM, LPIPS, and AVGE across both datasets and both evaluated resolutions.

5. **Novel IMR metric for measuring 3D representation stability.** The IMR metric (Section 3.4) provides a principled way to evaluate the dispersion of independently trained Gaussian point clouds using optimal transport, going beyond image-space metrics. The paper shows that D²GS achieves the lowest IMR (3.039 vs. 3.205 for DropGaussian on LLFF 3-view, Table 3), supporting the claim of improved robustness.

## Weaknesses

### Fatal
None.

### Major

None.

### Minor

1. **No error bars or variance reporting on the main quantitative results.** The PSNR improvements over DropGaussian are 0.59 dB (LLFF 1/8) and 0.35 dB (MipNeRF360). Without standard deviations or multiple-run statistics, it is unclear whether these gains are statistically significant. This is a common limitation in the 3DGS literature, but it weakens the evidence, especially given the modest margins. While the paper does report IMR across 10 runs (Table 3), the core PSNR/SSIM/LPIPS numbers in Tables 1–2 are single-run.

2. **The IMR metric, while principled in its formulation, lacks empirical validation.** The paper defines IMR formally (Eq. 7–14) and shows its values across methods (Table 3), but does not establish what the metric practically means: e.g., does lower IMR correlate with lower variance in test-set PSNR? Is IMR measuring something that PSNR variance alone would not capture? The values are close across methods (3.039–3.234), and without a validation study the metric's added value over simpler dispersion measures (e.g., variance of PSNR across runs) is not demonstrated. This does not weaken the method's core contributions, but it means the "novel metric" claim is not fully substantiated.

3. **All ablation studies are conducted only on LLFF, not on MipNeRF360.** Tables 4–6 show component ablations, parameter sweeps, and depth-estimator comparisons exclusively on the LLFF dataset. While the main results on MipNeRF360 (Table 2) show the full method works, the lack of ablations on the unbounded indoor/outdoor scenes of MipNeRF360 limits understanding of how sensitive the design choices are to scene type.

4. **The k-nearest neighbors implementation for local density estimation is underspecified.** The paper states that local density ρᵢ is "estimated via k-nearest neighbors" (Section 3.2) but does not specify the number of neighbors k or whether the search is conducted in 3D position space. This is a detail that would typically appear in an appendix, but the parsing of the paper removed that section. As written, this detail is missing from the main text.

5. **The DAFE gain is small and the hard threshold could be fragile.** The improvement from DAFE over the full DD-Drop is 0.18 dB PSNR (21.17→21.35, Table 4). The binary mask (Eq. 4) uses a hard cutoff at the top τ% of depth values. While the paper ablates τ (Table 5, τ=5% works best), a hard threshold could introduce boundary artifacts and may be scene-dependent. The small gain suggests the contribution is real but marginal.

6. **The dropout mechanism could benefit from a clearer description of its interaction with 3DGS's adaptive density control.** The paper describes dropout probabilities P_i and a time-dependent global rate r(t), but does not discuss how dropout interacts with 3DGS's densification and pruning operations. If dropped Gaussians are re-densified in subsequent steps, the effective regularization behavior may differ from the stated intention. This is a reasonable question that the paper could address.

### Trivial

- The "k-nearest neighbors" detail for density estimation should specify k (currently absent from the main text; may be in the stripped appendix).

## Nice-to-Haves

- A softer (continuous-weight) version of the DAFE mask could be explored and compared to the hard threshold.
- An empirical validation of IMR — e.g., correlating IMR values with variance in PSNR across runs, or with the reproducibility of rendered views — would strengthen the metric's practical utility.
- A sensitivity analysis of the tertile-based layering thresholds (D_near, D_middle) would clarify how critical this specific choice is.

## Removed Points

These points from the reviews are flagged for removal — treat with caution if they appear in discussion:

- **"Dropout mechanism is critically underspecified / irreproducible"** — The paper specifies dropout probabilities P_i (Eq. 2), a time-dependent rate r(t) (Eq. 3), and builds on DropGaussian. The mechanism is sufficiently clear for reproducibility; the reviewer's claim that "the method may not function as intended" is speculative and unsupported by the text.
- **"IMR has no justification"** — The paper explicitly states: "To specifically penalize model pairs with large divergence, we use a weighted formulation that amplifies the impact of inconsistent models" (text preceding Eq. 14). The squaring in the numerator and the log transform serve this stated purpose.
- **"Figure 1 numbers are confusing / 565 vs. 6,112 is unclear"** — The paper's explanation is clear: DropGaussian overfits (11,450 > 6,112 dense-view reference), while D²GS suppresses overfitting (565). The qualitative results (Figure 4) confirm D²GS produces better renderings with fewer Gaussians.
- **"Ablation starts from 3DGS not DropGaussian"** — This is standard ablation design (start from simplest baseline and build up). The direct comparison to DropGaussian is already provided in Tables 1 and 2.
- **"Missing related works"** — Per instructions, this cannot be verified without external sources.
- **"Missing appendix / missing proofs"** — The parser strips appendix content; these exist in the original submission.
- **Formatting/style nitpicks, typos, and parser artifacts** — These are parser errors, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report standard deviations** for the main PSNR/SSIM/LPIPS results across at least 3–5 runs. This is the most impactful improvement for the paper's credibility, especially given the modest margins over DropGaussian.
2. **Add a validation experiment for IMR:** e.g., show that IMR across 10 runs correlates with the variance in per-run PSNR, or that a lower IMR predicts better view-consistency. This would turn IMR from a definition into a useful tool.
3. **Include at least the component ablation on MipNeRF360** (e.g., the same rows as Table 4 but on MipNeRF360) to verify that the design choices transfer to unbounded scenes.

## Score and Decision

This paper presents a well-motivated, cleanly designed solution to a genuine problem in sparse-view 3DGS. The modular design is clearly validated through ablation, and the method achieves consistent (if modest) gains over strong baselines across two benchmarks and multiple metrics. The primary weaknesses are the lack of variance reporting, limited validation of the IMR metric, and ablations restricted to a single dataset. These are addressable limitations, not fatal flaws. The paper's contributions are solid and incremental.

**MY FINAL SCORE: <score>7.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**