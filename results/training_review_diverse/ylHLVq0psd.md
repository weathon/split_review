Now I have all the information I need. Let me synthesize the consolidated review.

---

## Summary

This paper rethinks noise schedules in diffusion models through two complementary lenses. In the training domain, it introduces the Weighted Signal-Noise-Ratio (WSNR), a frequency-domain metric that accounts for the power spectrum of natural images, and proposes WSNR-Equivalent training schedules that substantially improve FID at high resolutions (e.g., FFHQ-256: 11.49→7.89). In the sampling domain, it derives a data-driven heuristic for choosing the integration interval σ_max from ideal denoiser analysis, and proposes an NFE-guided dynamic scheme that switches between midpoint, Heun's, and 3rd-order methods depending on step size. The paper also provides an analysis of ODE discretization in σ-space vs. λ-space, suggesting advantages of σ-space solvers at large NFE.

## Strengths

- **Novel and well-motivated WSNR metric.** The paper identifies a genuine problem — that standard σ-based noise levels are resolution-dependent — and derives WSNR from power spectrum analysis as a principled solution. The metric is theoretically grounded (Eq. 2–3) and the observation that Gaussian noise has uniform power across frequencies while natural images concentrate power at low frequencies is insightful. Table 1 provides clean evidence that WSNR-Equivalent training schedules substantially improve FID at higher resolutions (FFHQ-256: 11.49→7.89), where both baseline and proposed models use the same architecture and training budget.

- **Clear theoretical analysis of the ideal denoiser leading to a data-driven σ_max heuristic.** The derivation from the ideal denoiser (Eq. 4–5) through Jensen's inequality (Eq. 6) and Chebyshev's inequality (Eq. 7) to propose σ_max = ||d|| is a well-structured chain of reasoning. Figure 6 verifies that the heuristic proxy covers >98% of data points. The insight that σ_max should be dataset-dependent rather than fixed is principled and practically relevant.

- **Informative empirical study of evaluation points (NEP) and method selection.** Table 4 systematically compares midpoint, Heun's, and 3rd-order methods under varying NEP, revealing that different methods dominate in different step-size regimes (midpoint better at large steps, Heun's at small steps). This observation is non-trivial and directly motivates the dynamic scheme.

- **Insightful λ-space vs. σ-space ODE analysis.** The Taylor expansion comparison (Eq. 9–10) formally identifies that λ-space solvers carry an exp(λ) factor in the truncation error that persists even when higher-order ϵ-derivatives vanish. Table 3 confirms that the proposed σ-space 3rd-order solver outperforms DPM-Solver at large NFE, providing evidence for the theoretical claim.

## Weaknesses

### Fatal
None.

### Major

- **Latent-space experiment (Table 2) confounds model capacity with noise schedule.** The comparison pits UViT-M (smaller model) with the WSNR schedule against UViT-L (more than double the parameters) with the EDM schedule. Since the paper does not include UViT-M with the EDM schedule (or UViT-L with the WSNR schedule), it is impossible to attribute the improved FID to the WSNR schedule rather than architectural differences between UViT-M and UViT-L. This is a structural flaw in experimental design that undermines the claim that WSNR benefits latent-space diffusion — a claim that is centrally featured in the abstract, contributions list, and conclusion.

- **No statistical significance reported for any experiment.** The paper reports single-run FID values without confidence intervals, multiple seeds, or any variance estimate. This is especially problematic for the headline CIFAR-10 improvement (1.92→1.89, a 0.03 difference) and FFHQ-64 improvement (2.45→2.25, a 0.20 difference) — both of which fall within typical run-to-run FID variance (±0.1–0.2) reported in the literature. Without replication, the reader cannot assess whether these improvements reflect genuine gains or noise. The same concern applies to Table 3 and Figure 7.

- **The WSNR-Equivalent training schedule lacks a precise, reproducible specification.** While Eq. 2 defines WSNR, the paper describes the WSNR-Equivalent schedule only verbally: "aligned with the p(WSNR) of the ImageNet dataset at 64x64 resolution in the RGB space under the EDM noise schedule" (line 87). The transformation from a reference p(WSNR) to a concrete σ(t) schedule is not given as an algorithm or pseudocode. Combined with the sensitivity of results to the choice of reference (only ImageNet-64 under EDM is tested, with no justification for why this reference is appropriate for FFHQ), this limits reproducibility.

- **The heuristic for σ_max lacks sensitivity analysis.** The paper chooses σ_max = ||d|| (line 158) based on the Chebyshev bound and the observation that p_ub decays slowly beyond this point. However, no experiment varies σ_max around this value to show that the heuristic point is near-optimal on the FID–NFE frontier. Figure 6 demonstrates coverage but not optimality for the generation quality–cost trade-off. A sweep varying σ_max by, e.g., ±20–50% would be needed to validate the heuristic.

- **The NFE-guided dynamic scheme's hyperparameter h_τ is unexplained.** The paper introduces h_τ as "the threshold for the step size" (line 168) but does not state its value, how it was chosen, or provide any principled derivation. The order-switching logic (midpoint when h > h_τ, Heun's/3rd-order otherwise) is similarly ad-hoc. Without a procedure for setting h_τ, the scheme is not a reproducible method but a post-hoc characterization.

### Minor

- **The σ-space vs. λ-space comparison (Table 3) confounds representation space with solver implementation.** The λ-space baseline is DPM-Solver, which has its own step-size schedule and is a specific 3rd-order implementation. The paper's σ-space solver may benefit from a different step-size schedule as much as from the choice of σ-space. A cleaner ablation would use the same step-size schedule (e.g., uniform in σ vs. uniform in log σ) with the same order of solver to isolate the effect of representation space.

- **Absolute FID values on FFHQ-256 are high (7.89 vs. baseline 11.49), suggesting models may not be fully converged after 780k iterations.** While the relative comparison between EDM and WSNR schedules is valid (same architecture, budget, and protocol), the high absolute scores raise questions about whether the improvements generalize to better-trained models.

- **Figure 2 shows only a single qualitative example to support the claim that same-WSNR images have perceptually similar noise.** A systematic study using a perceptual metric (e.g., LPIPS) across multiple images and resolutions would substantially strengthen this claim.

- **The paper's dynamic scheme is evaluated only on CIFAR-10 (Figure 7).** The approach is not tested on other datasets (e.g., FFHQ-64, ImageNet-64) which were used elsewhere in the paper, limiting evidence of generalization.

### Trivial

None.

## Nice-to-Haves

- A baseline that simply scales the EDM schedule's σ_max proportionally to image resolution (or to √pixels) would help isolate whether WSNR-Equivalence provides benefit beyond naive rescaling.
- Comparison against advanced solvers (DPM-Solver, DEIS) within the same NFE budget, using the authors' σ_max heuristic, would strengthen the sampling contributions. The paper acknowledges this limitation in the conclusion.
- An algorithmic pseudocode for computing the WSNR-Equivalent training schedule from a reference dataset would aid reproducibility.
- Discussion of the computational cost of computing WSNR for large datasets.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper's central empirical claims are largely unsupported"* — Overstated. Table 1 provides clean, well-controlled evidence for the training schedule contribution at high resolutions. The claim is partially supported but has specific gaps (addressed above).
- *"The WSNR metric's definition...is never explicitly written down"* — Incorrect. Eq. 2 explicitly defines WSNR. The WSNR-Equivalent *schedule* is not specified algorithmically (noted above as a major weakness).
- *"It is expected that a schedule that accounts for resolution differences would improve"* — Undermines the novelty of the method. The contribution is the WSNR-based method for principled adjustment, not the observation that adjustment helps.
- *"Thirty-five NFE is already a heavy budget"* — Partially genre-inappropriate. The paper's primary contributions are about noise schedule understanding, not extreme acceleration; 35 NFE is standard in the EDM framework.
- *"Missing comparison against state-of-the-art diffusion acceleration methods"* — The paper explicitly scopes this out in the limits section. Moved to Nice-to-Haves.
- *"Missing code or algorithmic pseudocode"* — Eq. 2 is explicit. The WSNR computation uses standard DFT operations. Moved to Nice-to-Haves as a reproducibility suggestion.
- *"The paper does not discuss the computational cost of computing WSNR"* — A minor omission, moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the latent-space experiment.** Add UViT-M trained with the EDM schedule as a baseline, so that UViT-M+EDM vs. UViT-M+WSNR isolates the effect of the schedule. This is the single most important experiment to add.
2. **Report statistical significance.** Run each experiment with at least 3 seeds and report mean ± std FID. This is essential before the CIFAR-10/FFHQ-64 sampling improvements (1.92→1.89, 2.45→2.25) can be considered credible.
3. **Provide an algorithmic specification of the WSNR-Equivalent schedule.** Include the transformation from reference p(WSNR) to the actual σ(t) used in training.
4. **Add σ_max sensitivity analysis.** Sweep σ_max around the proposed ||d|| value (e.g., 0.5× to 2×) on at least one dataset and show the FID–NFE curve to validate near-optimality.
5. **State and justify the h_τ threshold** used in the dynamic scheme, or derive it from a more principled error analysis.
6. **Extend the dynamic scheme evaluation** to FFHQ-64 and ImageNet-64 datasets, matching the scope of other experiments in the paper.

## Score and Decision

This paper presents a genuinely novel metric (WSNR) with a sound theoretical foundation, and provides clean evidence (Table 1) that WSNR-Equivalent training schedules improve generation quality at high resolutions. The analysis of λ-space vs. σ-space ODE discretization and the NEP study are also valuable contributions. However, the experimental validation has significant gaps: the latent-space claim rests on a confounded comparison, the headline sampling improvements are unreplicated and may fall within noise, the WSNR-Equivalent schedule is not precisely specified, and key hyperparameters (σ_max heuristic validation, h_τ in the dynamic scheme) are insufficiently tested. These issues collectively weaken but do not invalidate the core contributions. The paper would require substantial revisions — particularly fixing the latent-space experiment and providing statistical significance — before it could be accepted at a top-tier venue. In its current form, the contribution is promising but not yet fully supported.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>