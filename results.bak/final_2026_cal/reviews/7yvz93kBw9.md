Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper identifies two failure modes in sparse-view 3D Gaussian Splatting — near-field overfitting (excessive Gaussian density) and far-field underfitting (insufficient Gaussian coverage) — and proposes D²GS, a framework with two complementary modules: Depth-and-Density Guided Dropout (DD-Drop) that suppresses overfitting via adaptive per-Gaussian dropout probabilities, and Distance-Aware Fidelity Enhancement (DAFE) that strengthens supervision in distant regions using monocular depth masks. The paper also introduces an Inter-Model Robustness (IMR) metric to measure distributional stability across training runs. Experiments on LLFF and Mip-NeRF360 show consistent gains over prior 3DGS-based sparse-view methods.

## Strengths

- **Quantified spatial imbalance analysis.** Section 3.1 and Figure 1 provide concrete Gaussian counts showing the problem: near-field overfitting (11,450 vs. 6,112 Gaussians) and far-field underfitting (3,082 vs. 5,224 Gaussians) compared to dense-view training. This evidence goes beyond generic overfitting claims and directly motivates the two-pronged solution.

- **Additive gains from each sub-component validated.** The ablation in Table 4 progressively adds density score, depth score, depth-based layering, and DAFE, showing monotonic improvement from 19.22 to 21.35 PSNR with corresponding SSIM/LPIPS/IMR gains. This confirms that each design choice contributes positively and the components are complementary.

- **DAFE is robust across monocular depth estimators.** Table 6 shows consistent PSNR improvement over the DD-Drop baseline using MiDas (+0.04), DPT (+0.10), and DepthAnything V2 (+0.18). This demonstrates that DAFE's binary-mask-based far-field supervision is not tightly coupled to a specific depth predictor.

- **State-of-the-art results on two benchmarks.** On LLFF 1/8 resolution, D²GS outperforms LoopSparseGS by **+0.50 dB PSNR**, +0.029 SSIM, and −0.026 LPIPS. On Mip-NeRF360, it surpasses DropGaussian by **+0.35 dB PSNR** and +0.010 SSIM. These gains are consistent across resolution settings and metrics.

- **Thorough hyperparameter ablations.** Table 5 systematically explores dropout rate bounds, depth-density weighting coefficients, depth-mask ratio, and DAFE loss weight, giving confidence that the reported performance is not from coincidental tuning.

## Weaknesses

### Fatal

None.

### Major

- **The dropout mechanism's operational semantics are underspecified, hindering reproducibility.** The paper defines dropout scores \(S_i\) (Eq. 1) and dropout probabilities \(P_i\) (Eq. 2) and a time-dependent rate \(r(t)\) (Eq. 3), but never states what "dropping" a Gaussian means operationally. Are Gaussians permanently removed from the scene, or are they only masked from the current iteration's rendering/update (similar to DropGaussian's per-iteration subset selection)? The abstract says "adaptively masking" while Section 3.2 says "fraction of Gaussians discarded" and Figure 2's caption says "adaptively removes." These framings are inconsistent. Since 3DGS continuously densifies through cloning/splitting, whether dropout is permanent removal or temporary masking leads to very different training dynamics. The k in "k-nearest neighbors" density estimation is also unspecified. A clear algorithm description (pseudocode) is essential for reproducibility.

- **No variance reporting despite the paper's own emphasis on instability.** Figure 3 (left) highlights that baseline 3DGS PSNR can vary from 14.62 to 18.63 across 10 training rounds — a 4 dB range — and the paper motivates IMR precisely because of this instability. Yet Tables 1 and 2 report only single-point metrics without standard deviations, confidence intervals, or any measure of run-to-run variability. The claimed improvements (e.g., +0.50 dB over LoopSparseGS on LLFF 1/8) could partially lie within training noise. This is a critical inconsistency: the paper diagnoses instability as a problem but does not control for it in its own evaluation. While IMR partially addresses this at the distribution level, the image-quality metrics used for the main claims need variance reporting.

### Minor

- **DAFE's depth normalization is not discussed.** The paper uses monocular depth (DepthAnything V2, etc.) to define \(D_{\max}\) and \(\tau D_{\max}\) for the binary mask (Eq. 4). Monocular depth is typically affine-invariant (scale-and-shift ambiguous). The paper does not specify how the depth maps are normalized or whether \(D_{\max}\) is taken from raw relative depth. While the relative ordering of depth values is preserved (making the top-\(\tau\) mask meaningful even without metric depth), the lack of clarity is a presentation gap. The ablation on \(\tau\) (Table 5, top 5% best) is also tested only on LLFF, so its generalization is uncertain.

- **IMR metric is introduced but not validated.** IMR is presented as a contribution (Table 3), but the paper never demonstrates that lower IMR correlates with any meaningful property — higher image quality, lower PSNR variance, or better generalization. In fact, Table 3 shows CoR-GS has higher IMR than 3DGS on 6-view (3.270 vs. 3.234) while also having higher PSNR (from Table 1), suggesting IMR does not straightforwardly track quality. The metric is only reported on LLFF, not on Mip-NeRF360. Without validation, IMR remains an unsubstantiated auxiliary output.

- **k value for kNN density estimation unspecified.** Section 3.2 states density \(\rho_i\) is "estimated via k-nearest neighbors" but does not give the value of \(k\). This is a small but material missing detail for reproducibility.

- **Depth-mask ratio and IMR ablation tested only on LLFF.** All ablation studies (Tables 4–6) and IMR results (Table 3) are conducted on LLFF only, not on Mip-NeRF360. While this is common practice, it limits confidence in generalization.

### Trivial

None.

## Nice-to-Haves

- A pseudocode or training-loop description for DD-Drop showing how dropout scores are computed, when they are applied, and what happens to the Gaussian set.
- Reporting computational overhead (additional training time/memory) for DD-Drop's density estimation and DAFE's depth inference.
- Validating IMR by correlating it with PSNR variance or showing it captures meaningful differences beyond what image metrics already reflect.

## Removed Points

- **Missing related works / feed-forward baselines.** The harsh critic noted the paper doesn't compare with feed-forward methods (PixelSplat, MVSplat). The paper explicitly scopes itself to per-scene optimization (Section 2 discusses these methods but notes they are a different paradigm). This is not a weakness of the paper.
- **Claim that \(D_{\max}\) is "never defined."** The paper explicitly states "\(D_{\max}\) is the maximum depth value" in Eq. 4. The critic misread this.
- **Allegation that the method is "non-reproducible" / "irreproducible" due to missing appendix content.** The parser strips supplementary material from all papers. The core method description is reproducible with added pseudocode (noted as a real weakness above, but reframed as underspecification rather than irreproducibility).
- **Complaints about missing formatting/appendix stripping.** These are parser artifacts, not author errors.
- **Strength Finder's generic claim that "this paper addressed an important problem."** Removed for being generic and lacking specific evidence.

## Novel Insights

The most striking observation across the reviews is that the paper identifies a genuinely underexplored spatial asymmetry — near-field overfitting vs. far-field underfitting — and provides clean, per-Gaussian evidence for it (concrete counts of 11,450 vs. 6,112 and 3,082 vs. 5,224). This analysis is stronger than the typical "overfitting" hand-waving in sparse-view 3DGS papers. The DD-Drop design combining a local continuous score (Eq. 1) with a global discrete layering (Eq. 2) is also a principled way to handle the two scales at which spatial imbalance operates. The main gap is not in the idea but in the presentation of the mechanics and the statistical rigor of the evaluation.

## Suggestions

1. **Clarify the dropout operation.** Add pseudocode describing whether Gaussians are permanently removed or temporarily masked per iteration, how the per-Gaussian probability \(P_i\) is applied, and how dropout interacts with 3DGS's densification (cloning/splitting) process. Specify the value of \(k\) for kNN density estimation.

2. **Add variance reporting.** Report mean ± std over at least 5 independent training runs for the main metrics (PSNR, SSIM, LPIPS) in Tables 1 and 2. This is essential given the paper's own emphasis on training instability.

3. **Clarify DAFE depth normalization.** State how monocular depth maps are normalized (e.g., min-max scaling, percentile clipping) and confirm that \(D_{\max}\) refers to the maximum value of the normalized depth map, making \(\tau\) a percentile-like threshold.

4. **Validate or contextualize IMR.** Either show that IMR correlates with PSNR variance across runs (which would tie it back to the instability motivation) or explicitly describe IMR as a supplementary distributional metric whose interpretation is independent of image quality.

5. **Consider computing IMR on Mip-NeRF360** to show generalization beyond LLFF.

## Score and Decision

**Calibration report.** All anchors retrieved across rounds:

**Round 1 (bracketing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| BY8ATqW8vm (OGGSplat) | 3.00 | R1 weak | Weaker paper, withdrawn |
| 7mmnP3o1Hw (MatchGS) | 2.50 | R1 weak | Weaker paper, withdrawn |
| 3dNKozB8U7 (F4DGS) | 3.00 | R1 weak | Different topic, weaker |
| 3XGqsfKIIK (SplitGaussian) | 2.67 | R1 weak | Different topic, weaker |
| imblpbUryY (IPG-Rec) | 2.67 | R1 weak | Different topic, weaker |
| BpwRgbmTW9 (DRGSplat) | 4.67 | R1 mid | Depth-regularized 3DGS, similar approach; rejected for missing baselines; D²GS is stronger |
| Hmnh6UhDp6 (Layer-Based GS) | 5.50 | R1 mid | Different domain (CT), rejected |
| kdPmsMVhZf (G4Splat) | 5.00 | R1 mid | Sparse-view 3DGS with generative priors; accepted as poster; D²GS is somewhat stronger (cleaner pipeline) |
| MyKspTvxBl (GaussianTrim3R) | 5.50 | R1 mid | Feedforward pruning; rejected; not directly comparable |
| jdUAlrwppY (Gaussians on a Diet) | 4.50 | R1 mid | Memory-bound 3DGS; withdrawn |
| kI27Niy4xY (VIST3A) | 8.00 | R1 strong | Text-to-3D generation; accepted oral; different problem |
| DTQIjngDta (π³) | 8.00 | R1 strong | Feedforward geometry; accepted poster; different problem |

**Round 2 (narrowing within bracket 5.0–6.5):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| oapTMDy2Yh (Decouple Optimization) | 6.00 | R2 | 3DGS optimization analysis; accepted poster (6,6,6). Comparable quality — similar strengths (analysis, ablations) and similar weaknesses (no error bars, tuning complexity). D²GS ≈ this anchor. |
| 51JEkjP0gF (UBS) | 6.00 | R2 | Beta kernel generalization; accepted poster. Different contribution type. |
| v3ejhJxT1W (Splat the Net) | 6.00 | R2 | Neural primitives for 3DGS; accepted poster. Different contribution type. |
| WrEQFwWCdT (MoE-GS) | 6.00 | R2 | Dynamic 3DGS with MoE; accepted poster (6,6,2,10). Different problem. |
| egE7czf8qg (Path Matters) | 5.20 | R2 | Sparse-view 3DGS trajectory optimization; accepted poster (2,6,6,6,6). D²GS has clearer quantitative gains and less marginal improvements. |
| NvpVtGG6hk (Unified 3DGS Representation) | 5.50 | R2 | Gaussian representation learning; accepted poster (2,4,8,8). Different contribution type. |
| DavFcTeTbK (Signal Structure-Aware GS) | 6.50 | R2 | Large-scale scene 3DGS; accepted poster. Different problem domain. |

**Bracket and narrowing:** Round 1 bracket was 5.0–6.5. Round 2 identified the closest comparison as "Decouple Optimization" (6.00) and "Path Matters" (5.20, accepted). D²GS is stronger than Path Matters (clearer gains) and comparable to Decouple Optimization. The paper has two concrete major weaknesses (dropout underspecification, no variance) that prevent a higher score, but strong contributions and thorough ablations support a score near 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>