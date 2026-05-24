Now I have sufficient calibration context. Let me write the final consolidated review.

My bracket: After comparing against PBFM (5.50, same subfield), SGFM (5.50, methodological neighbor), PIDDM (4.00), and CDC-FM (6.50), I place this paper at **5.5**. It has genuine novelty in the joint evolution formulation and scaled adjoint-matching, but the evaluation support for the "accurate recovery" claim is genuinely weak (only MMD, no per-sample accuracy), and the surrogate base flow's theoretical status is acknowledged as a construction but not analyzed. This is comparable to PBFM's reception (consensus ~4-6) and below CDC-FM's cleaner validation.

---

## Summary

This paper proposes a post-training fine-tuning framework for flow-matching generative models that enforces parameter-dependent PDE constraints using weak-form residuals, while jointly inferring latent physical parameters (e.g., permeability, Young's modulus, wavenumber) through an augmented state formulation. The core idea is to extend the adjoint-matching framework (Domingo-Enrich et al., 2025) to a joint state–parameter space, using a surrogate base flow for the parameters constructed from an inverse predictor, and introducing a scaled memoryless noise schedule for numerical stability. Experiments across four PDE families (Darcy flow, linear elasticity, Helmholtz, Stokes) and a natural-image recoloring task show that the method reduces PDE residuals while maintaining distributional fidelity (MMD).

## Strengths

- **Joint state–parameter evolution is a novel and well-motivated formulation.** Section 3.2 constructs a surrogate base flow for latent parameters \(\alpha\) via the inverse predictor \(\varphi\) and evolves both \(x\) and \(\alpha\) jointly through learned vector fields. This enables physics-constrained generation without requiring paired parameter–solution training data—a genuine advance over prior work (PBFM, PhyDA) that either requires paired data or does not model parameters explicitly.

- **Scaled memoryless noise schedule is a clean theoretical extension.** The introduction of \(\sigma^2(t) = (1-\kappa)2\eta_t\) (Section 3.3) retains the memoryless property required for adjoint-matching consistency (Lemma 1, Appendix D.4) while providing a practical "stabilisation knob" that mitigates blow-ups near \(t\to0\). This is a concrete, reusable contribution to the adjoint-matching literature.

- **Empirical results convincingly show simultaneous residual reduction and distributional fidelity preservation.** Table 1 (elasticity with BC misspecification) shows the method achieving BC error \(1.71\times10^{-6}\) vs \(6.98\times10^{-5}\) (FM) and \(\text{MMD}_x = 0.15\) vs \(0.24\) (FM). Table 2 (Helmholtz with model misspecification) shows the joint AM model attaining the lowest weak residual (\(4.3\times10^0\)) and lowest \(\text{MMD}_x\) (\(0.06\)) among all compared methods. These results support the core claim that the framework improves physical validity while preserving distributional fidelity.

- **Computational efficiency is a practical advantage.** Fine-tuning on noisy Darcy requires only 20 gradient steps and completes in under 15 minutes on a single L40S (Section 4.1), with inference cost equal to the base model—substantially cheaper than pre-training approaches like PBFM.

- **Weak-form PDE residuals with random local test functions provide a principled, stable learning signal.** The design in Section 3.1 using compactly supported polynomial kernels and integration-by-parts is well-motivated for the noisy, misspecified setting and enhances numerical robustness.

## Weaknesses

### Major

- **The parameter recovery claim ("accurate recovery of latent coefficients") is insufficiently supported.** The abstract and introduction claim accurate recovery of latent physical parameters, yet the experiments rely primarily on \(\text{MMD}_\alpha\) (a distributional metric) rather than per-sample accuracy metrics (e.g., mean absolute error, correlation, or relative \(L^2\) error against ground-truth parameters). In elasticity (Table 1), \(\text{MMD}_\alpha\) for the proposed method is *worse* than the base FM (0.12 vs 0.05). In Helmholtz (Table 2), \(\text{MMD}_\alpha\) is essentially equal across all methods (~0.03–0.05). Only in the Stokes problem does the joint model clearly improve \(\text{MMD}_\alpha\). Without per-sample accuracy measures, the claim of "accurate recovery" is overstated relative to the evidence provided. The qualitative Darcy results (Figure 2) are suggestive but not quantified.

- **The surrogate base flow for the latent parameters lacks theoretical analysis of its validity for adjoint matching.** Section 3.2 constructs the \(\alpha\)-flow as \(v_{t,\alpha}^{\text{base}}(\alpha_t) = (\hat{\alpha}_1 - \alpha_t)/(1-t)\) where \(\hat{\alpha}_1 = \varphi(\hat{x}_1)\), derived from the inverse predictor applied to a one-step estimate of \(x_1\). This is explicitly acknowledged as a surrogate construction, but the paper then applies the adjoint-matching framework (designed for processes with well-defined marginal distributions and Markov structure) to this joint process without analyzing whether the constructed base flow satisfies the conditions required for the theoretical guarantees (convergence to the tilted distribution). The paper would benefit from either: (a) a formal analysis of when this surrogate flow approximately satisfies the needed conditions, or (b) a clear statement that adjoint matching is used heuristically for the joint process and the theoretical guarantees apply only to the \(x\)-marginal.

### Minor

- **Baseline comparisons are uneven across tasks.** PBFM is included but for Stokes the paper only states it "fails to converge" and refers to the appendix for a single residual number (strong residual \(1.15\times10^1\pm0.05\)) with no visual comparison or discussion. FM+ECI is evaluated only on elasticity, where its zero BC error but extreme strong residual (\(2.49\times10^2\)) raises questions about whether the comparison is informative. More consistent baseline reporting across all tasks would strengthen the evaluation.

- **The evaluation of parameter recovery on Darcy is wholly qualitative.** Figure 2 shows heatmaps for a single seed with no quantitative accuracy metric. Given that Darcy is the primary denoising + parameter recovery showcase, a per-sample metric (e.g., relative \(L^2\) error of \(\alpha\) against a ground-truth reference where available) would substantially strengthen the evidence.

- **The practical trade-off between \(\lambda_f\) (regularization) and residual reduction is demonstrated but not guided.** Figure 3 shows the trade-off exists, but there is no methodology or heuristic for selecting \((\lambda_x, \lambda_\alpha, \lambda_f)\) in practice for a new PDE system. Given the sensitivity visible in the ablation, this is a practical gap.

### Trivial

- The paper's contribution list includes "THEORETICAL GROUNDING" in all caps for the adjoint-matching extension, which is somewhat overstated given the surrogate construction for \(\alpha\).

## Nice-to-Haves

- Per-sample parameter accuracy metrics (MAE, relative \(L^2\) error) on at least one problem would strongly support the inverse-problem claims.
- An analysis of when the surrogate base flow for \(\alpha\) is a reasonable approximation to a true generative process—even a simple 1D or 2D illustrative example—would address the theoretical concern about the joint adjoint-matching formulation.
- Reporting the PBFM Stokes results visually (even if poor) alongside the proposed method would make the comparison more transparent.

## Removed Points

- *"The joint state augmentation lacks theoretical justification (structural)"* — This was the harsh critic's point #1. I have retained a softened version as a Major weakness, downgraded from Fatal because: (1) the paper explicitly acknowledges the surrogate construction, (2) the practical method works empirically regardless of theoretical guarantees for the joint process, and (3) the paper does not claim that the joint adjoin-matching guarantees hold for the surrogate \(\alpha\)-flow; it claims to "leverage the adjoint-matching framework." The critic overstates the gap by calling it "structural" and "fatal."

- *"PBFM fails to converge to meaningful velocity-pressure fields" claim is unverifiable* — The paper reports the strong residual (\(1.15\times10^1\pm0.05\)) and references Appendix F. Given the parser stripped the appendix, this is a known artifact, not an author omission. Removed as a parser artifact consequence.

- *Pure formatting/style nitpicks, typos, etc.* — Removed per hard rules.

- *Missing related works* — Removed per hard rules (cannot verify external knowledge).

- *PBFM training cost not controlled* — The harsh critic notes PBFM is a pre-training method while the proposed method is post-training, implying unfair comparison. The paper acknowledges this distinction, and the comparison is informative even if the training paradigms differ. This is a minor point at best.

## Novel Insights

The key insight that emerges from the reviews is that the paper's most distinctive contribution—the joint state–parameter evolution—is also its weakest point in terms of validation. The method's ability to reduce PDE residuals while preserving distributional fidelity (the \(x\)-space claims) is well-supported across multiple PDEs. But the \(\alpha\)-space claims rest on a constructed flow whose theoretical status is unclear and on distributional metrics (MMD) that do not directly measure parameter recovery accuracy. Disentangling these two aspects—physics-constrained generation (well-supported) vs. joint parameter inference (less well-supported)—would allow the paper to better communicate what it actually achieves.

## Suggestions

1. Add per-sample parameter accuracy metrics (relative \(L^2\) error, correlation) on at least the Darcy and elasticity problems to directly support the inverse-problem claims.
2. Include a paragraph in Section 3.2 discussing the theoretical status of the surrogate base flow for \(\alpha\)—even an informal argument about why the adjoint-matching heuristic is reasonable—or explicitly scope the theoretical claim to the \(x\)-marginal.
3. Report the PBFM Stokes results more transparently (visual samples, even if poor) and include FM+ECI on at least one additional PDE for consistency.
4. Tone down the "accurate recovery" language in the abstract and introduction to match what MMD-based evaluation supports (e.g., "distributionally consistent recovery" or "plausible estimates").

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| tAf1KI3d4X (PBFM) | 5.50 | R1/R2 | Same subfield. Paper compares against PBFM. Current paper has broader scope (joint inference) but PBFM has cleaner evaluation. Comparable overall. |
| hW7P3x9W8A (PIDDM) | 4.00 | R1(R2) | Similar domain (post-training physics constraints). Current paper is stronger in formulation and scope. |
| nnRB90w2kv (Flow Marching) | 2.50 | R1(R2) | Similar domain but with major experimental flaws. Current paper is significantly stronger. |
| p56ZAQUCUr (SGFM) | 5.50 | R2 | Methodological neighbor (FM guidance). Current paper has broader experiments and application scope. Comparable quality. |
| psmrKQ5lJe (CDC-FM) | 6.50 | R2 | Cleaner theoretical framing and validation. Current paper is weaker in terms of clean claims-to-evidence alignment. |

**Round 1 bracket:** 4.5–6.5 (after reading PBFM at 5.50 and PIDDM at 4.00, with upper bound from CDC-FM at 6.50).

**Round 2 narrowing:** Reading SGFM (5.50) and CDC-FM (6.50) confirms the paper sits at the lower end of the bracket—the parameter recovery evidence gap and the unanalyzed surrogate flow prevent it from reaching the 6+ range, while the genuine novelty and solid x-space results clearly place it above the 4–5 range of PIDDM and the flawed Flow Marching paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>