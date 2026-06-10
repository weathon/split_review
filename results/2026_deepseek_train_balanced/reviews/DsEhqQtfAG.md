Here is my final consolidated review.

## Summary
This paper proposes Decomposed Diffusion Sampling (DDS), which replaces the manifold-constrained gradient (MCG) update in diffusion-based inverse problem solvers with conjugate gradient (CG) iterations on the Tweedie-denoised estimate. The core idea is to perform multi-step CG data consistency updates within DDIM sampling, avoiding the costly backpropagation required by DPS/MCG. The method is evaluated on multi-coil MRI reconstruction (several masks/acceleration factors, including noisy and non-Cartesian settings) and 3D CT reconstruction (sparse-view and limited-angle), achieving state-of-the-art or near-SOTA reconstruction quality with 19–99 NFE compared to 4000 NFE for prior DIS methods, yielding 80–200× inference speedup.

## Strengths
- **Consistently strong empirical results across diverse medical imaging tasks.** Tables 1–3 and the CT table show DDS (VP) achieving the best or near-best PSNR/SSIM across virtually all settings, including outperforming supervised methods (E2E-Varnet, U-Net) on 2D subsampling patterns where supervised methods collapse. For example, on uniform 1D ×4 acceleration, DDS VP (99 NFE) achieves 34.88 PSNR vs. Score-MRI (4000 NFE) at 33.25 PSNR — better quality at <1/40th the NFE. This is supported by standard deviations and multiple repetitions.

- **Novel conceptual link between diffusion solvers and Krylov subspace methods.** Proposition 1 establishes that under an affine subspace assumption, the MCG Jacobian equals an orthogonal projection onto the clean manifold. Building on this, the paper shows a connection: if the tangent space at the denoised sample forms a Krylov subspace, then CG updates are guaranteed to stay in that subspace, providing a multi-step alternative to single-step MCG. This theoretical connection, even if conditional, is new and provides a framework for understanding why iterative solvers can replace backprop-based updates in DIS.

- **Practical advantages that address real limitations of prior DIS.** DDS avoids expensive backpropagation through the score network (required by DPS/MCG), handles measurement noise via a proximal formulation without computing SVD (which is non-trivial for medical imaging forward operators), and works with both VE and VP parameterizations. The method is also the first diffusion-based inverse solver demonstrated on non-Cartesian MRI (involving NUFFT).

- **Ablation isolating the CG contribution.** Table 2 (ablation on DC strategy) compares Score-MRI's gradient-based DC, DDNM's null-space projection, and DDS with varying CG iterations, keeping the DDIM sampling strategy fixed. This shows DDS (5 CG iterations) at 34.61 PSNR vs. Score-MRI at 26.48 and DDNM at 31.36, confirming that the CG update itself provides substantial improvement independent of other changes.

## Weaknesses

### Fatal
None.

### Major
- **The core theoretical claim depends on an unverified and unargued condition, making it essentially vacuous as a justification.** The paper's central insight (lines 247–259) is that CG updates preserve the tangent space, eliminating the need for expensive MCG. However, this is conditioned on the assumption that the tangent space at the denoised sample equals a Krylov subspace of the forward operator (line 252: "Suppose... that there exists the l-th order Krylov subspace such that T_t = \hat{x}_t + K_{t,l}"). The paper provides no argument, evidence, or even heuristic reasoning that this condition holds for natural image manifolds — it is simply stated as a supposition. The tangent space of a learned image manifold is determined by the score function and data statistics, while the Krylov subspace Span(b, Ab, A²b, …) is determined entirely by the forward operator A and the current residual. There is no known reason these should coincide. The abstract and introduction frame this as the paper's key theoretical contribution ("we prove that if… then…"), which is technically accurate but highly misleading, since the antecedent is never addressed. The method works well empirically — the real contribution is the practical algorithm — but the claimed theoretical rationale does not hold up. The paper would be substantially stronger if it reframed this as motivation rather than proof.

### Minor
- **The headline speedup claims (80–200×) partly conflate the effect of the CG update with the switch from VE to VP parameterization.** The paper's lead comparison contrasts DDS VP (19–49 NFE) against Score-MRI (VE, 4000 NFE). While the paper does provide VE ablations showing that DDS with the same VE model outperforms Score-MRI (Section "Improvement on VE"), the largest gains combine VE→VP switching with CG, and these are not fully disentangled in the headline framing. The DDS VE (99) results in the CT table achieve 33.43 PSNR vs. DiffusionMBIR (VE, 4000 NFE) at 33.49 — comparable but not a clear win — while DDS VP (49) jumps to 33.86. A cleaner disentanglement would strengthen the paper's claims about the CG contribution specifically.

- **The CT experiments combine CG with ADMM-TV without ablating the individual contributions.** For 3D CT, DDS uses a hybrid strategy: CG iterations followed by ADMM-TV with a CG solver. The paper states this combination is "crucial" (line 476) but does not report results for CG-only or ADMM-TV-only variants on the CT tasks. Given that DiffusionMBIR also uses a form of TV regularization, it is unclear how much of the CT improvement comes from the proposed CG-based DC update versus the ADMM-TV optimization component.

- **The claim of being "free from the cumbersome step-size tuning process" is overstated.** While the CG update itself has no step size, the overall method still requires tuning the stochasticity parameter η (values set differently for 19, 49, 99 NFE via grid search, line 349) and the proximal weight γ for noisy reconstruction (found through grid search, line 423). These are presented as fixed hyper-parameters rather than tuned quantities, which downplays the tuning burden.

### Trivial
- **The DPS (DDIM) baseline achieves surprisingly low PSNR (30.56 vs. DDS at 34.88 for uniform 1D ×4 in Table 1), but the paper does not discuss whether this is because DPS was designed for ancestral DDPM sampling rather than DDIM.** Since the paper uses DPS with DDIM specifically to "show that the strength of DDS not only comes from the DDIM sampling strategy" (line 348), a brief discussion about whether this DDIM variant of DPS is well-configured would help readers assess the fairness of this comparison.

## Nice-to-Haves
- A sensitivity analysis for the number of CG iterations M across different forward operators and acceleration factors (the ablation in Table 2 is for one MRI setting only).
- Reporting of statistical significance for comparisons where standard deviations overlap (e.g., DDS 49 vs. DDS 99 for several settings in Table 1).

## Removed Points
*These points were flagged for removal during consolidation. They are preserved here for reference but should not be treated as active weaknesses.*

- Criticism about the proof being "relegated to the appendix" — removed per rule about missing appendix content (appendix content is stripped by the parser).
- Criticism about rejection sampling "not being explained" — removed because the paper states "Further experimental details can be found in Sec. exp_details" (line 353), i.e., the details are in the appendix.
- Criticism about "no statistical significance testing" — demoted to Nice-to-Have; not standard practice for this type of benchmark paper.
- The "double gap" criticism about Proposition 1's affine subspace assumption — absorbed into the main Major weakness about the theoretical framing.
- Strength Finder's claim about "freedom from step-size tuning" — kept with caveat (the related weakness is retained as Minor).
- Various section-by-section notes about framing, presentation, and speculation about what "might" be happening — removed for lacking a specific, verifiable anchor in the paper.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- **Reframe the theoretical contribution.** Acknowledge plainly that the tangent space of a natural image manifold is not generally a Krylov subspace of the forward operator, and present the CG update as a fast-converging empirical heuristic motivated by the analogy, not as a theoretical guarantee. The empirical results are strong enough to stand on their own.
- **Disentangle the VE→VP confound** in the headline presentation. Report the best VE-based DDS results alongside the VP results in the main comparison tables, or clearly state how much of the gain is attributable to the parameterization change vs. the CG update.
- **Ablate the ADMM-TV component** in the CT experiments to show the standalone contribution of the CG-based DC update.
- **Discuss the DPS (DDIM) baseline's performance** to help readers assess whether the comparison is fair to DPS.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>