Now let me finalize the review with the calibration complete.

## Calibration Summary

**Round 1 anchors (bracketing):**
- `rWIrdAo2xC` (avg 5.20, but with scores of 3,10,5,5,3 — actually mid-band, retrieved as weak due to 3s): Single-view 3D human rendering. Weaker motivation and less thorough ablation than D²GS.
- `VpGsy4hKMc` (avg 5.00, FreeSplatter): Pose-free sparse-view 3DGS. Criticized as GS-LRM + PnP, limited novelty. D²GS has clearer motivation and more thorough ablation.
- `R9lgWYE508` (avg 5.75, RAIN-GS): Relaxing 3DGS initialization. Criticized for limited novelty, many hyperparameters. D²GS comparable or slightly better.
- `P4o9akekdf` (avg 8.00, NoPoSplat): Pose-free 3DGS, all 8s. Clearly stronger — simpler design, stronger results, better generalization. D²GS is clearly below this tier.

**Round 1 bracket: 5.0–6.5**

**Round 2 anchors (narrowing):**
- `c4Nh4A8Xn5` (avg 5.00, Geo-3DGS): All 5s. Criticized as incremental, lacking novelty. D²GS clearly stronger.
- `25Zlvl7JxW` (avg 6.50, HQGS): 3DGS under degraded scenes. Praised for novel contribution, thorough ablation, convincing improvements. D²GS somewhat weaker (IMR validation gap, modest gains).
- `BzsjHiBfLk` (avg 6.75, FDS): Flow distillation for 3DGS. Praised for simple intuitive idea. D²GS somewhat weaker (less novel core idea, more gaps).

**Final score: 6.0** — between RAIN-GS (5.75) and HQGS (6.50). D²GS has stronger problem diagnosis and ablation than 5.x papers, but the IMR validation gap, missing variance reporting, and modest quantitative gains prevent it from reaching 6.5+.

---

## Summary
This paper proposes D²GS, a framework for improving sparse-view 3D Gaussian Splatting (3DGS) by addressing two diagnosed failure modes: near-field overfitting and far-field underfitting. The method introduces Depth-and-Density Guided Dropout (DD-Drop), which adaptively prunes redundant near-field Gaussians using depth and local density signals, and Distance-Aware Fidelity Enhancement (DAFE), which amplifies supervision in under-fitted far regions using monocular depth priors. A third contribution, the Inter-Model Robustness (IMR) metric, uses Wasserstein-distance-based optimal transport to measure stability across independently trained 3DGS models. Experiments on LLFF and Mip-NeRF360 show consistent improvements over prior sparse-view methods.

## Strengths
- **Empirically grounded problem diagnosis (Section 3.1):** The paper quantifies sparse-view failure modes with specific Gaussian counts — near-field regions produce 11,450 primitives vs. 6,112 in dense-view, while far-field regions produce only 3,082 vs. 5,224. This concrete evidence directly motivates the dual overfitting/underfitting strategy.

- **Systematic component ablation (Table 4):** Starting from vanilla 3DGS (PSNR 19.22), each added module — density score, depth score, depth-based layering, and DAFE — monotonically improves both rendering quality (to 21.35 PSNR) and distributional robustness (IMR from 3.162 to 3.039). This cleanly demonstrates that the overfitting and underfitting interventions are complementary.

- **Dual local-global dropout design validated:** The DD-Drop module combines per-Gaussian scoring (Eq. 1) with global depth-based layering (Eq. 2). Table 4 confirms that adding layering on top of local scores improves PSNR from 21.10 to 21.17, validating that the global mechanism contributes beyond local scoring alone.

- **Thorough hyperparameter sensitivity analysis (Table 5):** Dropout rate bounds, score weights, depth threshold, and DAFE loss weight are systematically varied. Performance remains stable across configurations (PSNR range 21.04–21.30), indicating the method is not brittle.

- **Depth-estimator agnosticism demonstrated (Table 6):** Three different monocular depth models (MiDas, DPT, DepthAnything V2) all yield improvements over the baseline, showing the approach is not tied to a specific depth prior.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **IMR metric lacks validation and interpretability:** The paper devotes substantial space to developing IMR (Section 3.4, Eqs. 7–14) and lists it as a contribution, yet provides no analysis to help readers interpret the metric. There is no correlation study between IMR and rendering-quality variance (the very instability IMR is meant to capture), no ablation on the depth-stratified sampling size (10k from scenes up to 310k), and no error analysis for the first-order Taylor approximation in Eq. 11. The anomalous values in Table 3 — DropGaussian (3.205) having worse IMR than vanilla 3DGS (3.162) at 3-view, and 3DGS at 6-view (3.234) being worse than at 3-view (3.162) — are left undiscussed. These gaps make the third claimed contribution more preliminary than established.

- **No variance estimates reported for any metric:** The paper's own motivation highlights training instability (Figure 3 left shows PSNR varying by ~4 dB across runs for a baseline). Yet Tables 1–2 report PSNR/SSIM/LPIPS as point estimates with no standard deviations, confidence intervals, or per-scene breakdowns. Given that PSNR gains over DropGaussian are modest (0.35–0.59 dB), the reader cannot assess whether these margins exceed run-to-run noise. This is a notable omission for a paper whose theme is robustness.

- **λ_far and λ_middle not ablated:** These attenuation factors (0.3 and 0.7) are central to the global layering mechanism in DD-Drop (Eq. 2) but are set "based on experimental experience" (line 76) without any sensitivity analysis. Table 5 ablates ω, r, τ, and λ_DAFE but not these λ values. This is a gap in the otherwise thorough hyperparameter study.

- **No per-scene results:** Given the method's scene-dependent motivation (near/far imbalance varies by scene geometry), per-scene breakdowns would reveal whether gains are concentrated in specific scene types or are uniformly distributed. Their absence limits insight into when the method helps most.

- **No computational overhead discussion:** The method adds KNN density estimation across up to 310k Gaussians, monocular depth inference, and Sinkhorn iterations on 10k×10k cost matrices. Wall-clock time or memory comparisons against DropGaussian and other baselines would contextualize the practical cost of the improvements.

### Trivial

- The abstract claims "significantly improves both visual quality and robustness," which slightly overstates the modest quantitative margins (0.35–0.59 dB PSNR over the closest baseline).

## Nice-to-Haves
- The IMR formula (Eq. 14) uses squared distances in the numerator and linear in the denominator, which amplifies outlier model pairs. A justification or alternative normalization would strengthen the metric.
- A controlled ablation replacing DD-Drop with uniform dropout at equivalent rates within the D²GS framework (rather than relying on the cross-experiment DropGaussian comparison in Table 1) would more directly test the adaptivity claim.
- Clarifying the interaction between the per-Gaussian dropout probability P_i (Eq. 2) and the global progressive rate r(t) (Eq. 3) — whether r(t) thresholds, scales, or independently controls dropout — would improve reproducibility.

## Removed Points

These points were considered and removed (treat with caution):

- **KNN k, Sinkhorn ε, and normalization domain unspecified:** These are implementation details that would appear in the appendix (the paper references Appendix B for implementation details). Per review policy, these are not valid criticisms of the main text.
- **Demand for IMR-to-PSNR correlation as proof of validity:** The paper frames IMR as a complementary metric measuring distribution-level robustness, not as a proxy for rendering quality. Requiring it to correlate with PSNR variance misunderstands its stated purpose as a different evaluation dimension. However, the metric still needs interpretability support.
- **Criticism that DD-Drop vs uniform dropout is not ablated:** Table 1 directly compares D²GS against DropGaussian (uniform dropout baseline), and Table 4 isolates DD-Drop's contribution over no dropout. While a within-framework uniform-dropout ablation would be cleaner, the existing evidence reasonably supports the adaptivity claim.
- **Claim that gains come from depth prior rather than dropout:** Table 4 shows DD-Drop alone (no DAFE, no depth prior) improves PSNR from 19.22 to 21.17, confirming that the dropout strategy itself provides substantial gains independent of monocular depth.
- **"Significantly improves" language in abstract:** This is a minor rhetorical choice, not a substantive flaw. Moved to Trivial.

## Novel Insights
The paper's most insightful observation is that sparse-view 3DGS failure is spatially structured rather than random: near-field regions systematically overfit (producing nearly 2× the Gaussians of dense-view models) while far-field regions systematically underfit (producing only ~60% as many). This spatial diagnosis is more actionable than generic "sparse views cause instability" framings, and it motivates the dual dropout+enhancement design in a principled way. The idea of using optimal transport over Gaussian mixture distributions as a 3D-level robustness metric is also genuinely novel, even if its practical validation remains preliminary.

## Suggestions
- Validate IMR by reporting its empirical relationship to rendering-quality variance across the training runs from Table 3. A simple scatter plot of IMR vs. PSNR std-dev across methods would immediately show whether IMR captures what practitioners care about.
- Add per-scene PSNR/SSIM breakdowns and standard deviations across test views to strengthen the quantitative claims, especially given the modest margins.
- Discuss the anomalous IMR values in Table 3 (DropGaussian > 3DGS at 3-view; 3DGS worse at 6-view than 3-view) or investigate their causes.
- Ablate λ_far and λ_middle to justify the heuristic values.
- Report training time or GPU memory comparisons against DropGaussian and other baselines.

## Calibration Anchors Referenced

| Paper | Avg Score | Round | Comparison to D²GS |
|---|---|---|---|
| `rWIrdAo2xC` (Human-DAD) | 5.20 | R1 | Weaker motivation, less thorough ablation |
| `lT7Wq8qEvT` (DRO surface recon.) | 3.00 | R1 | Clearly weaker — different domain, less coherent |
| `VpGsy4hKMc` (FreeSplatter) | 5.00 | R1,R2 | Similar tier; D²GS has clearer motivation and ablation |
| `R9lgWYE508` (RAIN-GS) | 5.75 | R1,R2 | Close comparator; D²GS has stronger ablation, additional IMR contribution |
| `P4o9akekdf` (NoPoSplat) | 8.00 | R1 | Clearly stronger — simpler design, better results, broader impact |
| `c4Nh4A8Xn5` (Geo-3DGS) | 5.00 | R2 | D²GS clearly stronger — better motivation, more thorough ablation |
| `25Zlvl7JxW` (HQGS) | 6.50 | R2 | D²GS somewhat weaker — HQGS has stronger reviewer reception, more comprehensive validation |
| `BzsjHiBfLk` (FDS) | 6.75 | R2 | D²GS somewhat weaker — FDS has more novel core idea, higher reviewer scores |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowed:** D²GS sits between RAIN-GS (5.75) and HQGS (6.50). The IMR validation gap, missing variance reporting, and modest quantitative gains prevent it from reaching the 6.5+ level, but the strong motivation, thorough ablation, and dual-mechanism design place it above the 5.0–5.5 tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>