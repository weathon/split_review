Now I have enough calibration data. Let me finalize the review.

**Round 1 Bracket**: 5.0–7.5, based on comparison with FreeSplatter (5.00, reject) as a lower anchor and NoPoSplat (8.00, accept) as an upper anchor. GenCoGS has more thorough ablations than FreeSplatter but is less novel than NoPoSplat.

**Round 2 Narrowing**: 5.5–6.5. Comparing to Zero-shot NVS via Video Diffusion (6.00, accept) — GenCoGS has more thorough experiments and ablations but the misleading abstract is a concern. Comparing to MVDream (6.50, accept) — MVDream is more novel, GenCoGS is more comprehensive in evaluation but an engineering combination of existing components.

GenCoGS lands near the Zero-shot NVS paper (6.00): similar strengths in empirical results, similar weaknesses in evaluation concerns. Slightly above due to more thorough ablations, but offset by the misleading abstract. Final score: **6.0**.

---

## Summary

This paper proposes GenCoGS, a unified 3DGS-based few-shot novel view synthesis method combining two generative completion strategies: (1) GCGI, which uses a point cloud completion network (DGCNN + Transformer + FoldingNet) followed by kd-tree-based outlier filtering to produce a more complete initial point cloud; and (2) GCGO, which uses an image-to-video diffusion model with perturbed camera trajectories to generate pseudo views, plus a generative consistency loss to mitigate hallucination. Experiments on LLFF, DTU, and Shiny under 3, 6, and 9-view settings demonstrate improvements over existing methods.

## Strengths

- **Thorough ablation studies isolate each component's contribution.** Tables 4, 5, and 6 systematically decompose the method: GCGI adds +0.66 dB PSNR, GCGO adds +0.86 dB, combined achieves +1.34 dB over baseline. Table 5 separates perturbed trajectory from random sampling (+0.30 dB) and generative consistency loss (+0.54 dB). Table 6 shows CPG and CPF modules each contribute independently, including with degraded (1/4-sampled) point cloud input, demonstrating robustness.

- **Consistent SOTA results across three benchmark datasets and multiple view settings.** GenCoGS achieves best results on LLFF (3/6/9 views), DTU (3 views), and Shiny (3 views). Key gains: +2.40 dB PSNR on DTU vs. BinoGS (Table 2), +1.47 dB on Shiny vs. FSGS (Table 3), consistent improvements across PSNR/SSIM/LPIPS/AVGE on LLFF (Table 1).

- **Well-motivated generate-and-filter paradigm for point cloud completion.** The CPF module uses SfM points as high-confidence references in a kd-tree structure for outlier detection (Eqs. 5–8). Table 6 confirms CPF consistently improves results (+0.09 dB for full, +0.17 dB for 1/4 sampling), and Figure 3 visually demonstrates the outlier removal effect.

- **Generative consistency loss provides a principled mechanism to attenuate diffusion hallucination.** The two-term loss (Eqs. 16–18) combines a pixel-level adaptive confidence mask with a VGG-based structural loss. Table 5 confirms this contributes +0.54 dB PSNR and improves LPIPS from 0.181 to 0.164.

## Weaknesses

### Fatal

None.

### Major

- **Abstract headline improvement numbers are cherry-picked across different datasets with different baselines.** The abstract claims "improvements of up to 2.40 dB, 0.08 and 0.125 in PSNR, SSIM and LPIPS." Verification: PSNR 2.40 dB comes from DTU vs. BinoGS (23.11 − 20.71, Table 2); SSIM 0.080 from Shiny vs. FSGS (0.692 − 0.612, Table 3); LPIPS 0.125 from Shiny vs. FSGS (0.327 − 0.202, Table 3). No single comparison yields all three simultaneously. On DTU vs. BinoGS, SSIM improvement is 0.048 and LPIPS is 0.029. While the body text (lines 250, 279) correctly reports per-dataset improvements, the abstract's juxtaposition creates a misleading impression of magnitude and should be corrected.

- **Shiny dataset uses substantially weaker baselines than other datasets.** Table 3 compares only against RegNeRF, FreeNeRF, SparseNeRF, 3DGS, and FSGS. Strong methods evaluated on LLFF and DTU — BinoGS, CAT3D, ReconFusion, IPSM, ReconX — are absent. The 1.47 dB PSNR improvement is thus measured against the weakest baseline set, reducing the evidential weight of the Shiny results compared to LLFF and DTU.

### Minor

- **DTU and Shiny results only reported for 3-view setting.** LLFF has 3/6/9-view results (Table 1), but DTU (Table 2) and Shiny (Table 3) only have 3-view. This prevents assessment of whether GenCoGS's advantages persist beyond extreme few-shot settings.

- **No computational cost analysis.** The paper does not report training time, inference time, or memory usage. The I2V diffusion model is a computationally heavy component, and this practical concern is entirely absent.

- **AVGE metric used prominently but not defined in main text.** It appears in every results table and drives headline claims, but its definition is deferred to the appendix (line 246: "please refer to Appendix for details on Datasets and Evaluation Metrics").

- **Key hyperparameters set without systematic sensitivity analysis.** The perturbation amplitude A=2.0, loss weights α=10.0 and β=0.1, and transition iteration m=4000 are fixed without systematic study beyond the qualitative A=2.0 vs. A=3.0 comparison in Figure 8.

### Trivial

None.

## Nice-to-Haves

- Report honest single-comparison headline numbers in abstract (e.g., all metrics from DTU vs. BinoGS, which are actually strong).
- Add missing strong baselines to Shiny or explain why they cannot be included.
- Provide multi-view DTU/Shiny results to demonstrate generality beyond extreme few-shot.
- Brief computational cost comparison to address practical deployment concerns.
- Analysis of what fraction of pixels are masked by the confidence mask and whether masked regions correspond to actual hallucination vs. legitimate appearance changes.

## Removed Points

These points are flagged to be removed, treat them with caution:
- Sentence fragment at line 120 ("And, the complete point cloud P_f, which possesses enhanced structural information barely affected by outliers.") — removed as a grammar/formatting nitpick.

## Novel Insights

The paper's core insight — that generative completion can address the scene completeness limitation in few-shot 3DGS NVS through a two-pronged approach (init-time point cloud completion + optimization-time pseudo-view completion with hallucination mitigation) — is practically useful. The generate-and-filter paradigm for point cloud completion, using SfM points as a reference set for outlier detection via kd-tree, is a practical contribution that could generalize beyond this specific method.

## Suggestions

- Rewrite abstract to present per-dataset improvements honestly rather than cherry-picking the max from each.
- Discuss why strong baselines are absent from Shiny evaluation.
- Add a brief table or discussion of computational costs.
- Define AVGE in the main text given its prominence in all results tables.

## Calibration Report

**Retrieved anchors:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| GeoGS3D | 3.40 | 1 | GenCoGS is stronger: more thorough ablations, stronger results |
| Generalizable Monocular 3D | 2.83 | 1 | GenCoGS is stronger: better evaluation, clearer contribution |
| 360-InpaintR | 3.33 | 1 | GenCoGS is stronger: more complete evaluation |
| DC3DO | 3.00 | 1 | GenCoGS is stronger: better motivated and evaluated |
| FreeSplatter | 5.00 | 1 | GenCoGS is slightly stronger: more thorough ablations, more consistent SOTA |
| Hi-Gaussian | 5.75 | 1 | GenCoGS is slightly stronger: more comprehensive evaluation |
| studentSplat | 4.25 | 1 | GenCoGS is stronger: better evaluated, clearer method design |
| SCISplat | 5.00 | 1 | GenCoGS is stronger: more thorough experiments |
| NoPoSplat | 8.00 | 1 | GenCoGS is weaker: NoPoSplat is more novel, better received |
| TetSphere Splatting | 7.60 | 1 | GenCoGS is weaker: less novel representation innovation |
| STC-GS | 8.00 | 1 | GenCoGS is weaker: less novel, presentation issues |
| LVSM | 7.67 | 1 | GenCoGS is weaker: LVSM has broader impact |
| 3D-free meets 3D priors | 5.00 | 2 | GenCoGS is slightly stronger: more thorough evaluation |
| Zero-shot NVS via Video Diffusion | 6.00 | 2 | Comparable: similar evaluation quality, GenCoGS has better ablations but misleading abstract |
| ZERO-1-to-G | 5.50 | 2 | GenCoGS is slightly stronger: more comprehensive experiments |
| MVDream | 6.50 | 2 | GenCoGS is slightly weaker: less novel, misleading presentation |
| WildFusion | 7.00 | 2 | GenCoGS is weaker: WildFusion is more novel |
| Phidias | 6.20 | 2 | Comparable: similar strength levels |
| Controllable Sat-to-Street | 6.25 | 2 | Comparable: similar experimental rigor |

**Bracket**: Round 1: 5.0–7.5. Round 2: 5.5–6.5. Final: 6.0, comparable to Zero-shot NVS via Video Diffusion (6.00) — similar quality of empirical contribution with similar evaluation concerns.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>