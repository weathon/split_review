Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies ℓ₁-regularized inverse optimal transport (iOT) for recovering a sparse ground cost from samples drawn from an entropic optimal transport coupling. Its core theoretical contribution is a sufficient condition for sparsistency — a generalization of the Lasso's irrepresentability condition to the iOT setting — along with a sample complexity bound. For the Gaussian case, the paper derives a closed-form Hessian enabling explicit certificate computation, and shows that as the entropic regularization ε varies, the iOT problem interpolates between a classical Lasso (ε→∞) and a graphical Lasso (ε→0). Numerical experiments on synthetic graphs illustrate the behavior of the certificate.

## Strengths

1. **First rigorous sparsistency analysis for inverse OT.** The paper derives a sufficient "irrepresentability-type" condition (Definition 1, Eq. C) for ℓ₁-regularized iOT that generalizes the classic Lasso condition to the non-quadratic Fenchel-Young loss of iOT. This provides a novel theoretical foundation for support recovery in continuous state spaces, going beyond prior discrete-space analyses (e.g., Chiu et al. 2022, Dupuy & Galichon 2014).

2. **Explicit sample complexity bound.** Theorem 1 provides a sample complexity rate of n^{-1/2} under the non-degenerate certificate condition, together with a bound quantifying the influence of the entropic regularization ε and the true cost magnitude via a factor exp(C‖A_soln‖₁/ε). While this bound is loose (see Weaknesses), it is the first such bound for the iOT problem and identifies the relevant problem parameters.

3. **Closed-form Hessian and limiting-case analysis for Gaussians.** Lemma 3 provides a general formula for ∇²W(A) under Gaussian distributions, enabling explicit computation of the certificate. Propositions 5 and 6 show concretely that the iOT certificate reduces to the Lasso certificate (ε→∞) and the graphical Lasso certificate (ε→0, under stated restrictions), establishing a concrete connection between iOT and two well-studied sparse estimation problems. This gives practical intuition for the role of ε.

4. **Numerical evidence supporting the theory.** Figures 1–2 demonstrate on circular, planar, and Erdős–Rényi graphs that the certificate's non-degeneracy improves with larger ε and that recovery performance matches theoretical predictions: sparsistency is achieved only when the certificate is non-degenerate.

## Weaknesses

### Fatal
None.

### Major

1. **Unaddressed gap between population and empirical centering.** Assumption 1(iii) centers the cost basis using the true marginal distributions α, β (∫ cost_k(x,y) dβ(y) = 0, ∫ cost_k(x,y) dα(x) = 0). Section 2.3 states that the finite-sample problem uses empirical centering (∑_i cost_k(x_i,y_j)=0, ∑_j cost_k(x_i,y_j)=0). The certificates z_∞ and z_n in Proposition 4 are defined with respect to different bases (Φ and Φ_n respectively), but the paper does not explain how centering error propagates through the bound on ‖z_∞ − z_n‖_∞. Since the centering transformations differ between population and empirical levels, the comparison between z_∞ and z_n requires an additional argument. Without addressing this, the claim that z_n inherits the non-degeneracy of z_∞ is not fully justified. This is a genuine gap in the theoretical argument for Theorem 1.

2. **Exponential factor in the bound is not contextualized or reconciled with experiments.** The sample complexity and error bounds contain a factor exp(C‖A_soln‖₁/ε) with an unspecified constant C>0. For small ε (e.g., ε=0.1, used in the experiments) or moderate ‖A_soln‖₁, this factor is astronomically large, yet the numerical experiments with n=80 and ε=0.1 show successful recovery (albeit only for large enough λ). The paper does not discuss whether this exponential is an artifact of the proof technique or a genuine barrier, and does not attempt to reconcile the theoretical bound with the practical performance. Since the whole contribution rests on this guarantee, the looseness significantly weakens the practical relevance of the result.

### Minor

1. **The irrepresentability condition is hard to verify in practice.** The certificate in Eq. (C) depends on ∇²W(A_soln), which in turn depends on the unknown true cost and the coupling it generates. While the Gaussian case provides a closed-form Hessian (Lemma 3), for general settings there is no way to check whether the condition holds without already knowing the answer. The paper frames this as a "far reaching generalization of the Lasso's irrepresentability condition," but the Lasso condition is testable from the observed design matrix, whereas here the design involves unknown quantities. The paper does not discuss how a practitioner might validate the condition.

2. **Limiting-case analysis requires restrictive assumptions and parameter rescaling.** The ε→0 limit (Proposition 6) requires symmetric positive-definite A, Σ_α=Σ_β=I, and an explicit A≽0 constraint. Both limits also require rescaling λ by ε (λ₀/ε for ε→∞, λ₀·ε for ε→0) to obtain a non-trivial limit. The paper is transparent about these choices, but the "interpolation" claim is more limited than the abstract's language suggests, and the rescaling is externally imposed rather than emerging naturally from the iOT objective.

3. **Numerical experiments do not directly validate the sample complexity bound.** The recovery performance plots (Figure 2) show the number of wrongly estimated positions as a function of λ for three ε values, but n is fixed at 80 throughout. There is no experiment varying n to verify the claimed n^{-1/2} rate or the exp(C‖A_soln‖₁/ε) scaling, weakening the connection between theory and experiments.

### Trivial

- The adjoint operator Φ^* is used in the certificate and Proposition 2 without explicit definition. While standard in functional analysis, defining it explicitly would improve readability.
- The constant C>0 in Theorem 1 and Proposition 4 is never identified or bounded; a remark on its dependence (or lack thereof) on problem dimensions would be helpful.

## Nice-to-Haves

- A discussion of strategies to tighten or potentially remove the exponential factor (e.g., regimes where ‖A_soln‖₁ is bounded uniformly in dimension, or where ε is large) would significantly strengthen the paper.
- A brief quantitative comparison of the bound to known results in compressed sensing or generalized linear models would help calibrate expectations.
- Explicitly noting that the empirical centering converges to population centering at rate O_p(n^{-1/2}) and sketching how this error can be absorbed into the existing bounds would resolve the centering gap.

## Removed Points

- **"Proof of the sample complexity bound is deferred to the appendix."** The parser strips appendix content from all papers; proofs exist in the original submission. Deferring proofs to an appendix is standard for conferences and does not constitute a weakness.
- **"The paper should also cover Y / domain Z / additional tasks."** Demands for breadth outside the paper's stated scope (e.g., covering non-Gaussian settings beyond what is analyzed, or adding entirely new classes of experiments) are scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper that the authors do not already make themselves.

## Suggestions

1. **Address the centering gap explicitly.** The simplest fix is to note that the empirical centering converges to the population centering at rate O_p(n^{-1/2}), and sketch how the bound in Proposition 4 can accommodate this additional error term. Alternatively, show that the whole analysis can be carried out in the population-centered basis, with the finite-sample estimator constrained to obey population centering (which is feasible when α, β are known or well-approximated).

2. **Contextualize the exponential factor.** Add a paragraph discussing whether exp(C‖A_soln‖₁/ε) is a proof artifact or a genuine barrier. Consider showing that in regimes where ε is large relative to ‖A_soln‖₁, the bound becomes meaningful, and explain how the small-ε regime (where the graphical Lasso connection lives) may require a different analytical approach.

3. **Add experiments varying n.** A simple plot of recovery probability vs. n for fixed ε and λ would directly validate the sample complexity claim and strengthen the empirical section considerably.

4. **Clarify the verifiability of the condition.** For the Gaussian case, explicitly state the conditions on Σ_α, Σ_β, and the graph structure under which the irrepresentability condition is guaranteed to hold (e.g., diagonally dominant Hessian). This would make the abstract condition more interpretable.

## Score and Decision

The paper tackles a genuinely difficult and important problem — providing recovery guarantees for inverse OT with sparse structure. The core ideas (generalized irrepresentability condition, certificate convergence, Gaussian case analysis) are novel and represent a meaningful theoretical step. However, the unaddressed centering mismatch creates a gap in the proof of the main result, and the exponential factor in the sample complexity bound is not contextualized, making it hard to assess the practical relevance of the guarantee. These issues are fixable but need to be addressed before the contribution stands as complete and trustworthy. I recommend a borderline decision: the paper has merit and should not be rejected outright, but requires major revision to close the centering gap and to provide a more honest assessment of the bound's limitations.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>