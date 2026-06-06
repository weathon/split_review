---

## Summary

D²GS proposes a unified sparse-view 3D Gaussian Splatting framework addressing two complementary failure modes: near-field overfitting and far-field underfitting. The method introduces a Depth-and-Density Guided Dropout (DD-Drop) module that assigns each Gaussian a spatially-adaptive dropout probability based on local density and distance, a Distance-Aware Fidelity Enhancement (DAFE) loss applying targeted L1 supervision in monocular-depth-estimated far regions, and a novel Inter-Model Robustness (IMR) metric grounded in 2-Wasserstein distance and optimal transport to quantify training stability. Experiments on LLFF and Mip-NeRF360 show consistent improvements over DropGaussian and other 3DGS baselines.

---

## Strengths

- **Concrete, quantified failure mode analysis.** Section 3.1 provides direct evidence: near-field Gaussian count 11,450 (sparse) vs. 6,112 (dense) and far-field count 3,082 (sparse) vs. 5,224 (dense). These specific numbers ground the dual-module design.

- **Progressive ablation confirming complementary contributions.** Table 4 shows step-by-step gains: density score → 21.02 dB, +depth score → 21.17 dB, +DAFE → 21.35 dB, with consistent gains in SSIM, LPIPS, and IMR at each step. This is a credible, progressive validation rather than a global ablation.

- **DAFE robustness to depth estimator choice.** Table 6 shows all three tested estimators (MiDas, DPT, DepthAnything V2) yield improvements above the DD-Drop-only baseline (21.17 dB), confirming the module is not brittle to a single depth model.

- **IMR metric with principled theoretical grounding.** The metric formalizes 3DGS stability as a 2-Wasserstein distance between Gaussian mixture models, using closed-form Bures metric, Sinkhorn-solved entropic OT, and depth-stratified sampling for tractability (Eqs. 7–14). Numerically, D²GS achieves the lowest IMR in both 3-view (3.039) and 6-view (3.109) settings among all tested methods (Table 3).

- **Consistent multi-metric improvements on two datasets.** On LLFF (Table 1), D²GS leads on PSNR, SSIM, LPIPS, and AVGE at both 1/8 and 1/4 resolution. On Mip-NeRF360 (Table 2), it improves over the closest competitor (DropGaussian) by 0.35 dB PSNR with gains in all four metrics. The cross-metric, cross-dataset consistency provides moderate confidence in the gains.

---

## Weaknesses

### Fatal
None.

### Major

- **Single-run evaluation in the presence of demonstrated high training variance.** Figure 3 explicitly shows that repeated training of a prior method under identical settings yields PSNR ranging from 14.62 to 18.63 dB (a 4 dB spread) across 10 independent runs. The headline improvement over DropGaussian — 0.59 dB on LLFF (1/8 res.) and 0.35 dB on Mip-NeRF360 — is reported as a single number per method with no standard deviation, no averaging across runs, and no acknowledgment of this variance in the experimental section. This is internally inconsistent: the paper proposes IMR precisely because run-to-run variance is large enough to matter, yet then uses single-run metrics as the primary evidence of superiority. Notably, the data needed to report multi-run averages already exist (the authors ran 10 independent rounds per method to compute IMR). Even 3–5 run averages for Tables 1–2 would substantially strengthen the claim. The consistent improvement across multiple metrics (PSNR, SSIM, LPIPS, AVGE) on two datasets suggests the gains are real, but they cannot be confirmed at the reported margins without multi-run statistics.

### Minor

- **DD-Drop depth score design rationale is unexplained.** In Eq. 1, the local dropout score $S_i = \omega_\text{depth}\tilde{d}_i + \omega_\text{density}\tilde{\rho}_i$ uses normalized Euclidean distance to the camera, which is *larger* for farther Gaussians, meaning high $S_i$ flags far-field Gaussians for higher dropout. The paper states that "depth-and-density aware scores $S_i$ indicate regions prone to overfitting," but overfitting is identified as a *near-field* problem. The global attenuation in Eq. 2 ($\lambda_\text{far} = 0.3$) does partially counteract this by scaling down far-field dropout, but the paper never explains why the local depth term should point toward the far field in the first place — rather than, for instance, using inverse depth. The ablation (Table 4, row 2 vs. row 3) shows the depth score contributes positively, but the design logic is not stated. A reader trying to re-implement Eq. 1 from its stated motivation would likely invert the depth term. A brief explanation of why the local-then-attenuate design is preferred over using density alone with global attenuation would resolve this.

- **IMR lacks a validity correlation analysis.** IMR is introduced as a metric that "complements traditional image-space metrics," but the paper does not show that lower IMR correlates with higher rendering quality or lower PSNR variance across methods or scenes. The proposed log-ratio formulation in Eq. 14 ($\ln(\sum S_{ij}^2 / \sum S_{ij})$) is novel and penalizes large divergences by squaring the numerator, but the rationale for this specific formulation is not explained. A scatter plot or Spearman correlation between IMR and PSNR variance across the 10 runs would compactly establish the metric's discriminative validity.

- **Figure 2 / DAFE loss inconsistency.** The Figure 2 diagram caption (as extracted) specifies the DAFE loss as $L_\text{DAFE} = \lambda_\text{near} L_\text{near} + \lambda_\text{mid} L_\text{mid} + \lambda_\text{far} L_\text{far}$, while Eq. 5 defines a single binary far-field mask and one loss term, and Eq. 6 shows $L_\text{total} = L_1 + \lambda_\text{SSIM} L_\text{D-SSIM} + \lambda_\text{DAFE} L_\text{DAFE}$. The figure suggests a three-way decomposition that does not appear in the actual formulation. The paper should align the figure caption with the implemented loss.

- **LoopSparseGS omitted from Table 2 without explanation.** LoopSparseGS is included as a baseline in Table 1 but is absent from Table 2 (Mip-NeRF360). If it was not evaluated on Mip-NeRF360, that should be stated explicitly.

### Trivial

- **Framing in quantitative evaluation section.** The paper leads with "D²GS surpasses FSGS, CoR-GS, and LoopSparseGS by 0.92/0.9/0.5 dB PSNR" before reporting the 0.59 dB margin over DropGaussian, the most relevant predecessor. The ordering downplays the honest reference point.

---

## Nice-to-Haves

- An ablation removing the depth term from Eq. 1 entirely (leaving only density score + global attenuation) would directly test whether the depth component in $S_i$ contributes independently or whether its effect is fully absorbed by the global mechanism. This would clarify the design rationale discussed above.
- Reporting the approximate pixel fraction of the far-field mask $M_\text{dis}$ per LLFF scene (given $\tau = 5\%$) would confirm the supervision signal in DAFE is non-trivial and substantive.
- For Table 5, the τ sensitivity is nearly flat (21.25 at 5% vs. 21.26 at 10%); clarifying that all top-performing configurations converge to the same full model (21.35 dB, Table 4) would reduce potential reader confusion about the gap.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Leading with weaker baselines is a framing concern"** — The paper does compare against DropGaussian (the direct predecessor) with the honest 0.59 dB margin. The mention of larger gains over FSGS/CoR-GS is accurate and informative in context. Demoted to Trivial (ordering note) above.

- **"Depth τ = 5% table is internally inconsistent with claimed best"** — On closer inspection, Table 5 ablates individual DAFE parameters on top of DD-Drop only (reaching ~21.17 dB), while the full model with all components achieves 21.35 dB. The numbers are internally consistent; this is not a real inconsistency.

---

## Novel Insights

The most genuinely novel observation emerging from this review is the interplay between D²GS's stability improvement (measured by IMR) and the reliability of single-run evaluation: if D²GS substantially reduces training variance (as lower IMR across 10 runs suggests), its single-run performance may be a more reliable point estimate than its competitors'. This creates a somewhat paradoxical situation — the very metric the paper introduces to demonstrate stability could be used to argue that single-run comparisons are more defensible for D²GS than for its baselines. However, the paper never makes this argument, and it would require cross-method PSNR variance data to be convincing. The paper is positioned at an interesting boundary where 3D distribution-level stability (IMR) and image-level stability (PSNR variance) are being claimed as correlated but never verified to be so.

---

## Suggestions

1. **Report multi-run (≥5) PSNR/SSIM/LPIPS statistics in Tables 1–2.** The data already exists (10 rounds were run for IMR). This single change would address the most significant weakness and make the claimed improvements statistically credible.
2. **Add a correlation analysis for IMR:** scatter PSNR variance (std across 10 runs) vs. IMR across methods and/or scenes to establish that IMR captures what it claims to capture.
3. **Clarify the depth term in Eq. 1:** Add a sentence explaining that the local score increases with distance, and that the global attenuation (Eq. 2) is what ultimately keeps far-field dropout low. A simple visualization of $P_i$ as a function of depth would make the combined mechanism intuitive.
4. **Align Figure 2 caption with the actual DAFE formulation** (single far-field mask, not three-way near/mid/far decomposition).
5. **State explicitly why LoopSparseGS is absent from Table 2** (e.g., "LoopSparseGS was not run on Mip-NeRF360 due to dataset-specific training constraints").

---

## Score and Decision

**Originality:** The DD-Drop and DAFE are incremental extensions of DropGaussian, but the dual local-global design and the IMR metric based on OT/Wasserstein distance over Gaussian mixtures are genuinely novel formulations. The problem decomposition (near-field overfitting vs. far-field underfitting) is well-motivated and specific. *Score: 3/5*

**Importance of research question:** Sparse-view 3DGS stability is a practically important problem as sparse-view settings dominate real-world acquisition. The paper addresses a recognized failure mode with concrete solutions. *Score: 3/5*

**Claims well-supported:** The individual module contributions are well-supported through Table 4 ablations and Table 6 robustness checks. The headline SOTA claim in Tables 1–2 rests on single-run statistics despite demonstrated high variance — this is the main unsupported element. *Score: 3/5*

**Soundness of experiments:** Ablation structure is sound and comprehensive (Tables 4–6). Two datasets with multiple resolutions. Broad baseline set including NeRF and 3DGS methods. The single-run statistics issue is the primary soundness concern. *Score: 3/5*

**Clarity of writing:** Generally clear, with precise mathematical formulation of DD-Drop and IMR. The Figure 2 / DAFE formulation inconsistency and the depth score design rationale create localized clarity gaps. *Score: 3/5*

**Value to the research community:** The IMR metric with its OT-based formulation could have broader applicability beyond this specific method. The dual-mode failure analysis is transferable. The improvements, if confirmed under multi-run evaluation, are meaningful for the field. *Score: 3/5*

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>