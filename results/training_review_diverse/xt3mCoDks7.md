Now I'll construct the final consolidated review.

## Summary

This paper presents MolJO, a gradient-based framework for structure-based molecule optimization (SBMO) that jointly guides both continuous atom coordinates and discrete atom types. The key idea is to leverage the continuous Bayesian belief space of Bayesian Flow Networks (BFNs) as a medium for gradient guidance, circumventing the discrete-data guidance problem faced by prior diffusion-based methods. A backward correction sampling strategy is introduced, maintaining a sliding window of past history to trade off exploration and exploitation during optimization. On CrossDocked2020, MolJO achieves Success Rate 51.3%, Vina Dock -9.05, and SA 0.78 — substantially outperforming the prior gradient-based method TAGMol (12.6%) and approaching oracle-based methods. The framework is also extended to constrained settings including R-group optimization and scaffold hopping.

## Strengths

- **Joint gradient guidance over continuous and discrete modalities (validated by ablation).** The paper derives a principled form for guiding both atom coordinates (continuous) and atom types (discrete, through the latent y-space) within the BFN belief-space framework. The ablation in Figure 5 confirms that joint guidance consistently outperforms single-modality guidance across Vina Dock, QED, and SA, validating the core motivation that previous methods (TAGMol, guiding only coordinates) were insufficient because they lacked joint control.

- **Strong empirical performance on CrossDocked2020.** Table 1 shows MolJO achieving Success Rate 51.3%, the best among all categories (generative models, oracle-based methods, gradient-guided methods). The "Me-Better Ratio" analysis (Figure 1B) further shows MolJO produces roughly 2× the fraction of improved molecules compared to other 3D baselines, demonstrating practical optimization capability.

- **Backward correction strategy is empirically effective.** Table 4 shows that backward correction (k=130) improves both unguided sampling (37.9% → 42.8% Success Rate in the no-guidance condition) and gradient-guided sampling (42.8% → 51.3%). Figure 2 provides a clear visualization of how the window size k controls gradient alignment across steps, supporting the exploration-exploitation interpretation.

- **SE(3)-equivariance preservation is formally stated.** Proposition 4.4 correctly notes that when both the energy network and base generative model are SE(3)-equivariant and the complex is zero-centered, the guided sampling process preserves equivariance. This is a helpful theoretical guarantee for physical plausibility.

## Weaknesses

### Fatal
None.

### Major

- **The backward correction derivation involves an unacknowledged approximation that weakens its theoretical grounding.** In Eq. 7 (line 162), the derivation marginalizes out θ_{i-1} via p_U(θ_{i-1} | θ_{i-2}, 𝑥̂_i; α_{i-1}), replacing the *earlier* clean prediction 𝑥̂_{i-1} (which would come from p_O(·|Φ(θ_{i-2}, t_{i-1}))) with the *current* clean prediction 𝑥̂_i (from p_O(·|Φ(θ_{i-1}, t_i))). The additive accuracy property from Graves et al. (2023) applies when the same clean data point is used across merged steps, but here the network's prediction changes over time. The paper presents this derivation as following from additive accuracy without acknowledging the substitution or the approximation it introduces. This is not fatal — the empirical results in Table 4 suggest the heuristic works well — but the paper should either (a) provide a rigorous justification for the substitution, (b) explicitly label the backward correction as an approximation and analyze the associated error (e.g., comparing log-likelihood of the backward-corrected sampler vs. the standard BFN sampler), or (c) both. As written, the theoretical framing oversells the derivation's mathematical exactness.

- **Constrained optimization experiments lack sufficient methodological detail for verification or reproduction.** Section 5.3 (lines 278–289) reports results for R-group optimization and scaffold hopping, stating only that these are "achieved by infilling.2" (likely Appendix Section 2, now stripped). No algorithm, conditioning mechanism, or constraint-enforcement procedure is provided in the main text. The reader cannot determine: how is the scaffold or R-group fixed during generation? Does the backward correction interact with the constraint, and if so, how? Without these details, the strong results in Table 3 (near-100% validity, high Success Rate) are unverifiable. This undermines the paper's claim of "versatility" — the reader has no way to assess whether the method genuinely respects constraints or merely biases generation.

### Minor

- **The "4× improvement over gradient-based counterpart" conflates base model strength with guidance contribution.** MolJO builds on MolCRAFT (a strong BFN-based model with 42.1% unguided Success Rate), while TAGMol builds on DiffSBDD (a diffusion model with lower base performance). The 4× claim (12.6% → 51.3%) reflects improvement of the *entire system*, not just the guidance component. The paper does show guidance contributes meaningfully (42.1% → 51.3% from MolCRAFT's base), but the headline "4×" comparison is inflated by the base model gap. The paper should be more precise about what is being compared.

- **Limited information about the energy function(s) used for guidance.** The paper introduces E(θ, t) as a "time-dependent energy function" (line 74) but does not specify in the main text: what form does this network take (architecture, parameterization)? Is it a learned surrogate, and if so, how is it trained and on what data? For Vina, QED, and SA objectives, are these differentiable surrogates or direct formulas? These details are essential for reproducibility. (The critic also notes this; if an appendix exists, it should be moved to the main paper or clearly referenced.)

- **Gradient guidance fails with the vanilla (non-corrected) sampler, raising questions about robustness.** Table 4 shows that without backward correction (Vanilla and Vanilla MC), applying guidance *hurts* Success Rate (Vanilla: 8.1% with guidance vs... the caption shows the unguided values, but the relative improvement column shows non-positive numbers for Vanilla/Vanilla MC). The paper briefly notes (line 299) this is "probably due to the suboptimal history" but does not investigate why. If guidance works only in conjunction with the heuristic backward correction, this is a meaningful limitation that deserves analysis rather than a one-sentence dismissal.

### Trivial

- The gradient similarity analysis (Figure 2) provides an intuitive picture of the exploration-exploitation trade-off, but only measures cosine similarity for the first few steps; the connection to actual property improvement is suggestive rather than directly demonstrated.

- Table 4's caption uses green/black shading for "improvement under guidance" but the absolute scales and thresholds for Success Rate could be more clearly defined in the caption itself.

## Nice-to-Haves

- An ablation comparing guided sampling *without* backward correction to guided sampling *with* backward correction, specifically isolating the guidance contribution from the correction contribution, would strengthen the empirical claims.
- A brief "Limitations" section discussing failure cases (e.g., when does MolJO produce invalid molecules?) would improve the paper's completeness.
- A systematic analysis of the KL gap between the backward-corrected sampler and the exact sequential BFN sampler would calibrate the cost of the approximation.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **"Algorithm 1 line 10 is garbled (exp(yi)-(kz - k)i)"** — This is a PDF parser artifact, not an author error. The original submission would have the correct expression.
- **"Missing appendix or proofs in appendix"** — The parser strips appendix sections from all papers; they exist in the original submission.
- **"Definition of energy function is completely absent"** — The paper does state that E(θ, t) is a "time-dependent energy function" following Kong et al. (2024) and "predicts certain property" (line 74), though details are insufficient. This criticism was merged and downgraded to Minor rather than removed entirely, since the paper does provide a notational definition even if implementation details are thin.
- **"The paper should also cover more tasks / domains"** — This would turn the paper into a broader paper rather than a stronger version of its stated scope.
- **"Pure formatting/style nitpicks"** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core strengths (joint guidance, backward correction, strong results) and surface a real theoretical gap (the backward correction derivation masks a heuristic substitution) and a documentation gap (constrained optimization methodology is underspecified). The harsh critic's observation that guidance *fails* with the vanilla sampler (Table 4) is a particularly important point that the paper glosses over — this suggests the guidance may be less robust than claimed, or that the backward correction is doing more work than acknowledged.

## Suggestions

1. **Reframe the backward correction as a principled heuristic** with explicit acknowledgment of the approximation (substituting 𝑥̂_i for 𝑥̂_{i-1} in Eq. 7). Provide empirical validation (e.g., comparing KL divergence or sample quality of the backward-corrected sampler vs. the exact BFN sampler on held-out data) to calibrate the cost of the approximation.

2. **Provide full methodological details for constrained optimization** — describe how R-group/scaffold constraints are enforced during the backward-corrected sampling process. Include the algorithm or pseudocode in the main paper or a clearly referenced appendix.

3. **Clarify the experimental comparison framing.** Acknowledge that the "4×" improvement over TAGMol reflects overall system advantage (better base model + guidance), and isolate the guidance contribution explicitly (e.g., "MolJO on MolCRAFT improves Success Rate from 42.1% to 51.3% through joint guidance, a 22% relative gain; the additional gap over TAGMol's 12.6% partly reflects the stronger base generative model").

4. **Investigate why guidance hurts the vanilla sampler.** Table 4 shows guidance leads to non-positive improvement for Vanilla/Vanilla MC samplers. A brief analysis of this phenomenon would either reveal a meaningful limitation or help the reader understand the interaction between backward correction and guidance.

5. **Document the energy function** — architecture, training data, supervision signal, and whether the same function is used across all objectives or separate ones are trained.

## Score and Decision

This paper addresses an important problem with a novel approach and delivers strong empirical results on the primary unconstrained optimization benchmark. The joint guidance over continuous and discrete modalities via the BFN belief space is a genuinely new contribution, and the backward correction strategy, though heuristic, empirically improves performance. However, the paper has two significant issues: (1) the backward correction derivation presents a heuristic as an exact mathematical consequence without acknowledging the approximation, and (2) the constrained optimization experiments lack sufficient methodological detail for verification. These are fixable issues that do not invalidate the core contribution, but they meaningfully reduce the paper's current quality. The paper would benefit from a major revision that addresses theoretical clarity, documentation completeness, and more precise experimental framing.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>