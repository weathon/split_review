Now I have sufficient information. Let me write the final consolidated review.

## Summary

The paper establishes a first-order duality between activation steering and influence functions, proving that any steering vector can be represented as an influence weighting over training data and vice versa. It introduces Influence-Aligned Steering (IAS), an alignment diagnostic γ that quantifies when steering can faithfully replace influence, spectral optimality for principled steering direction selection, and generalization bounds for low-rank interventions. The core idea — connecting two previously separate interpretability toolkits under a unified geometric framework — is genuinely novel and interesting.

## Strengths

1. **Novel theoretical connection between activation steering and influence functions (Theorem 4.2, Lemma 4.1).** The paper establishes a two-way mapping that bridges two previously disconnected research threads. This is a genuinely original conceptual contribution that many in the interpretability community will find interesting, as it provides a unified language for discussing activation-space and weight-space interventions.

2. **Alignment diagnostic γ (Theorem 5.1, Equation 3).** The cosine of the smallest principal angle between the Jacobian subspaces of the layer and the parameters provides a rigorous, computable bound on the residual error when matching an influence update with a steering vector. This gives practitioners an actionable feasibility check that costs only two SVDs. The empirical validation of γ's monotonic increase across layers (Figure 2, 0.64 → 0.94) cleanly corroborates the theory.

3. **No-free-lunch impossibility result (Theorem 6.2).** When γ is bounded below 1, every activation perturbation is provably limited to at most a fraction γ of the logit movement achievable by a parameter-space perturbation. This gives a clear, principled criterion for when to skip steering entirely — a practically useful decision rule that emerges naturally from the theory.

4. **Spectral optimality principle (Theorem 5.3).** The paper shows that under an ℓ₂ budget, the direction maximizing first-order logit change is the top eigenvector of a Fisher-influence matrix Σ, replacing ad-hoc steering vectors with a principled spectral recipe. The ImageNet experiment (Figure 3, p=0.00498) suggests this direction is statistically distinguishable from random.

## Weaknesses

### Major

1. **Equation (2) contains an algebraic error in a central derivation.** The dual program derivation states Δh* = J_{h→y}ᵀ J_{θ→y} Δθ (line 88). Solving the Lagrangian correctly gives Δh* = J_{h→y}ᵀ (J_{h→y}J_{h→y}ᵀ)† J_{θ→y} Δθ = J_{h→y}† J_{θ→y} Δθ — the pseudoinverse factor (J_{h→y}J_{h→y}ᵀ)† is missing. Theorem 5.2 later states the correct formula Δh* = J_{h→y}† J_{θ→y} Δθ, which is reassuring, but the inconsistency in Equation (2) is a real error in a formula that the paper explicitly calls foundational. A reader trying to follow the dual derivation will be confused about whether the paper is claiming Δh* = J_{h→y}ᵀ J_{θ→y} Δθ (which is dimensionally inconsistent if m ≠ d and generally incorrect) or the pseudoinverse expression. This needs to be fixed.

2. **Theorem 6.1 (generalization bound) is not clearly connected to activation steering.** The theorem models the perturbed model as f̃ = f_θ + αUVᵀ — a weight-matrix perturbation. But IAS as defined throughout the paper is an activation-space perturbation: it adds a vector to the hidden state during inference, not a matrix to the weights. The sketch claims "IAS changes only a rank-k submatrix of the layer weight" without establishing the mapping from activation steering to an equivalent low-rank weight update. Unless the authors provide a constructive argument showing how adding αs to the hidden state is equivalent to a rank-k modification of the weight matrix (which would require additional analysis involving the downstream layers), this bound is not clearly relevant to the proposed method. The bound itself is a minor extension of existing Rademacher-complexity results and does not contribute new insight to the paper's central thesis.

3. **Unexplained scaling discrepancy in the central experimental validation (Figure 1).** The theory predicts that the slope between predicted and actual logit shifts should be 1.0 in the linear regime. The paper reports a slope of 1.50 — a 50% systematic deviation. The cosine of 0.978 shows good directional alignment, but the scale error is large and unexplained. The paper mentions using Tikhonov damping λ for stability (line 56), which could introduce systematic scaling; the effect of λ on the slope should be analyzed and reported. Without this analysis, the single experiment that directly tests the claimed first-order equivalence is inconclusive. The text describes the result as "consistent with the expected linear regime," but slope ≠ 1 for a first-order claim requires explanation, not hand-waving.

### Minor

4. **The promised "data provenance" workflow is never demonstrated.** The abstract and introduction promise a workflow: "steer first, trace provenance, edit weights only when the geometry demands it" and "a constructive algorithm for mapping undesired behaviors back to causal training examples." Yet no experiment uses IAS to map a steering vector back to training examples, nor does any experiment compare an influence-based data re-weighting with the IAS-induced change. The detoxification experiment (Table 1) compares IAS with CAA on toxicity metrics without specifying what target influence the IAS vector was constructed to match, making it unclear what the comparison tests. This gap between the ambition of the narrative and the scope of the experiments weakens the paper's practical claims.

5. **Theorem 4.2 states existence of ρ_s but does not construct it explicitly in the main text.** The paper's central theorem asserts the existence of a signed measure ρ_s with ‖ρ_s‖₁ = |α|, but the main text provides only conceptual intuition ("weighted by how well their gradients correlate with s") rather than an explicit formula for ρ_s in terms of s and the training data. While a full proof may exist in the (stripped) appendix, a reader of the main text cannot see how ρ_s is actually computed. Coupled with the strong affine-independence assumption in Corollary 1, this makes the practical payoff ("ρ_s pinpoints the fewest training examples") feel ungrounded.

6. **The feasibility condition Im(J_{θ→y}) ⊆ Im(J_{h→y}) is stated as a core assumption (Section 2) but is almost never satisfied in practice.** The parameter–logit Jacobian has rank up to P (billions), while the activation–logit Jacobian has rank at most d (layer width, typically thousands). The paper acknowledges this via the γ diagnostic and residual bounds, but the main theorems (4.2, 5.2) are stated under this assumption, with qualifications deferred to subsequent discussion. This creates a disconnect between the crisp theory and the approximate regime where it actually applies. While this is common in first-order analyses, the paper could more honestly front-load the conditional nature of its central claims.

### Trivial

7. Lemma 5.4 contains redundant notation: √(1−(1−γ₁²)) is simply γ₁. The expression is unnecessarily complicated. Some references to equations are ambiguous (e.g., "bound equation 3" on line 210 could be clearer about which equation is meant).

## Nice-to-Haves

- **Add a targeted duality experiment:** Pick a training example, compute its influence on a test output via the standard influence function, then compute the IAS vector that matches that influence. Verify that the steering intervention produces the same logit shift with slope ≈ 1. Then show that the signed measure ρ_s recovered from the steering vector puts high weight on that training example. This would directly confirm the claimed connection and address the paper's biggest experimental gap.
- **Report confidence intervals or quantiles for the γ diagnostic** (Figure 2 currently shows only median).
- **Analyze the effect of Tikhonov damping λ on slope scaling** in Figure 1, and report λ values used in experiments.
- **Clarify the mapping from activation steering to low-rank weight updates** if Theorem 6.1 is to be retained, or remove Section 6 and focus on the core duality contributions.

## Removed Points

These points were flagged in the inputs but removed after verification against the paper:

- **Claim that "Theorem 4.2 does not bound the residual when the span condition is violated":** REMOVED — the paper explicitly bounds the residual immediately after Theorem 4.2 (Equation 3 and surrounding text): "the irreducible residual obeys ‖(I − P_h)J_{θ→y}Δθ‖₂ ≤ √(1−γ(x)²) ‖J_{θ→y}Δθ‖₂."
- **Claim that the paper does not characterize when ρ_s exists:** REMOVED — the paper states "The result holds exactly if the set {ℐ(z→x)} spans Im(J_{h→y}); otherwise Eq. (4) holds up to a residual."
- **Criticism about missing proofs in the appendix:** REMOVED per hard rule — the parser strips appendix content; proofs likely exist in the original submission.
- **Formatting/typo nitpicks:** REMOVED per hard rule — these are parser artifacts.
- **"No discussion of the computational cost for the spectral direction":** REMOVED — the paper provides a clear cost model (two JVPs per input, rank-d pseudoinverse, small SVD) and a practical power-iteration recipe.
- **Criticism that detoxification comparison is "uninformative":** WEAKENED to Minor weakness #4 — the comparison has a useful purpose (showing IAS is competitive with CAA) but the absence of the target influence specification is a real limitation, not a fatal flaw.
- **Strength finder's claim about Corollary 1 being a major strength:** REMOVED — the strength is contingent on affine independence (a very strong assumption the paper itself acknowledges), and the proof idea is circular as written.
- **Strength finder's claim about generalization bounds:** REMOVED — as discussed in Major weakness #2, the bound is not clearly connected to activation steering.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not already make.

## Suggestions

1. **Fix Equation (2):** Replace Δh* = J_{h→y}ᵀ J_{θ→y} Δθ with Δh* = J_{h→y}ᵀ (J_{h→y}J_{h→y}ᵀ)† J_{θ→y} Δθ (or equivalently Δh* = J_{h→y}† J_{θ→y} Δθ) and ensure consistency throughout all derivations.
2. **Clarify or remove Theorem 6.1:** Either provide a rigorous argument showing how activation steering is equivalent to a low-rank weight perturbation, or remove the section and focus on the core duality contributions.
3. **Explain the slope discrepancy in Figure 1:** Analyze how Tikhonov damping, pseudoinverse truncation, or finite-step nonlinearities affect the scaling. Report λ values and show how the slope changes with λ.
4. **Add a direct duality experiment:** As described in Nice-to-Haves — this is the single most impactful experiment the paper could add.
5. **Provide an explicit formula for ρ_s** in the main text (or a sketch that makes the construction clear), so readers can understand how to compute it from s and the training data.
6. **Front-load the conditional nature of the claims:** State in the abstract/introduction that the equivalence holds to first order and is approximate when the subspace inclusion condition is violated, which is the typical case.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>