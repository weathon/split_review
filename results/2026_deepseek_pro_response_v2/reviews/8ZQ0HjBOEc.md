Now I have enough comparison data. Let me write the final review.

---

## Summary

This paper analyzes the limiting behavior of the NTK for infinitely-wide fully-connected ReLU networks as depth increases, with data on the sphere. Proposition 4 and Theorem 2 provide a clean characterization showing the normalized NTK converges to the all-ones matrix (becoming singular). Theorem 3 — the paper's main claimed contribution — attempts to prove that despite this singularity, the closed-form predictor κ_x κ^{-1} converges to a well-defined, bounded, data-dependent limit, using rough differential equation machinery.

## Strengths

- **Proposition 4 and Theorem 2 provide a clean, interpretable characterization of how depth drives the NTK toward triviality.** The alternative recursion Θ̄_∞^{(L+1)} = (L/(L+1)) h'(ρ^{(L)}) Θ̄_∞^{(L)} + (1/(L+1)) h(ρ^{(L)}) (Proposition 4, line 149) exposes depth-dependence transparently through known functions h and h'. Combined with Lemma 1 (ρ^{(L)} → 1), Theorem 2 establishes that normalized kernel entries strictly increase to 1. These results are correctly proved and provide genuine insight.

- **The paper addresses a well-motivated gap in the NTK literature.** Prior work (Xiao et al., 2020) characterized the predictor limit only when the kernel decomposes into a constant plus an invertible matrix — an assumption Theorem 2 shows is violated when the NTK converges to the all-ones matrix. The paper correctly identifies this as an open problem, and the approach via rough differential equations is genuinely novel in this context.

- **The generalization criteria (Section 6, lines 239–241) are a useful synthesis.** The three conditions — diagonal dominance, eventual positive definiteness, and vanishing determinant — abstract the essential properties needed for the proof technique, and the η kernel example demonstrates these criteria are not vacuous.

## Weaknesses

### Fatal

None.

### Major

- **The proof of Theorem 3 contains a significant gap in the variation argument (the paper's main contribution).** The construction uses ψ_D(2t−1) with D = det(Θ̃_∞^{(L+1)})·det(Θ̃_∞^{(L)}) to interpolate between consecutive depths. The proof claims the derivative terms v_{i,j} converge to 0 in the 1-variation metric, relying on property (4) of ψ_d — that all derivatives converge to 0 pointwise as d→0+. However, as d→0+, ψ_d sharpens into a near-step function; its first derivative at z=0 blows up as ~1/(2d), and the total variation of ψ_d remains constant (≈2). Pointwise convergence of derivatives at each fixed z does not imply convergence in variation norm — the 1-variation of d/dt A_n^{(L+1)}(t) involves ∫|ψ'_D| which stays order-1. The subsequent determinant inequality chain (lines 219–223) then bounds a ratio that pairs the numerator's ψ'_D-dependent terms against the denominator's determinant product, without accounting for the 1/D growth of ψ'_D at t=1/2 competing with the ∼D decay in the denominator. As written, the proof does not establish that v_{i,j} → 0 in 1-variation. Since Theorem 3 is the paper's main claimed contribution, this gap substantially weakens the paper.

- **Even if the proof gap could be fixed, the significance of Theorem 3 is limited.** The theorem establishes existence of a limit for κ_x κ^{-1} and boundedness, but provides no characterization of what that limit is — no formula, interpretation, or connection to the learned function. For training points x_i ∈ X, the limit being e_i follows trivially from κ_{x_i} being the i-th row of κ at every finite L (line 228). For test points x ∉ X, the theorem says only that a bounded limit exists. This is a thin result to serve as the paper's central contribution.

### Minor

- **Empirical evidence is limited and does not directly validate Theorem 3.** The experiments run only to depth L=30 (Figure 1), while the paper itself notes kernel convergence is "logarithmic" and "extremely slow" (line 245–246). The third column of Figure 1 shows κ_x κ^{-1} values, but without a known limiting predictor to compare against, the plots cannot distinguish genuine convergence from slow drift. Only a single random dataset draw and MNIST are tested, with no variance across data draws reported. The hypothesis that moderate depths suffice for the solution limit (while the kernel requires much larger L) is plausible but not rigorously validated.

- **Property (4) of ψ_d is stated inaccurately for the specific function defined in Definition 6.** The claim that lim_{d→0+} d^k/dz^k ψ_d(z) = 0 for all k and z is false at z=0, where the first derivative is ~1/(2d) → ∞. The property holds pointwise for z ≠ 0 but fails at the midpoint of the interpolation, which is precisely where the interpolation matters most.

### Trivial

- **Notational inconsistency between Θ̃_∞ and Θ̄_∞.** Theorem 3 and Section 5–6 use Θ̃_∞ while Definition 4 defines Θ̄_∞. These appear to refer to the same normalized kernel.

- **The quantifier in property (4) of Proposition 5 has an unexplained variable:** "∀ j, k ∈ ℕ_0" where j does not appear in the limit expression d^k/dz^k ψ_d(z).

## Nice-to-Haves

- A direct asymptotic analysis of the eigendecomposition of Θ̃_∞^{(L)} — studying the rate at which the (n−1) small eigenvalues decay relative to the leading eigenvalue, and whether the projection of Θ̃_∞^{(L)}(x X^⊤) onto the small-eigenvalue subspace decays at a matching rate — could yield convergence conditions and an explicit characterization of the limiting predictor, rather than just existence.
- Running experiments to substantially larger L (hundreds) and quantifying the difference between the predictor at moderate depth vs. very large depth would better support the claim of fast solution convergence.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The entire rough-path apparatus appears unnecessary in principle. If one could genuinely establish that the difference between the solutions at depths L and L+1 goes to 0, this would follow from standard matrix perturbation bounds."** REMOVED. This is a judgment about proof strategy, not a verifiable error. The critic asserts an alternative proof exists without providing one; the claim that standard perturbation bounds suffice for nearly-singular matrices is not obvious and is not demonstrated.

- **Harsh Critic: "The paper never operationalizes the depth-to-width ratio condition (L ∈ o(min n_i)) in any concrete way."** REMOVED. The condition is stated as a scope delimiter distinguishing from Hanin & Nica (2020). The paper does not claim to derive results that depend quantitatively on this ratio; operationalizing it further is not required for the theoretical results presented.

- **Harsh Critic: "The claim that Xiao et al. (2020)'s proof 'would not apply' is somewhat circular."** REMOVED. The paper explains (line 228) that Theorem 2 shows the kernel converges to all-ones, which violates the decomposition assumption in Xiao et al. — this is a substantive point, not circular reasoning.

- **Harsh Critic: Critique about missing Proposition 8 and appendix.** REMOVED. The appendix is stripped by the parser; Proposition 8 exists in the original submission.

- **Harsh Critic: "The discussion of mean-field limits is speculative and underdeveloped."** REMOVED. This is a forward-looking remark (line 247), not a claimed result, and speculative remarks in a discussion section are appropriate.

- **Strength Finder: "Theorem 3 uses rough differential equation machinery to resolve the singular-kernel limit."** RETAINED in weakened form — the RDE approach is genuinely novel but the proof gap prevents this from being listed as an unqualified strength. The approach is noted as a strength of the paper's framing rather than its execution.

- **Strength Finder: "Empirical evidence disentangles slow kernel convergence from fast solution convergence."** PARTIALLY RETAINED as a Minor weakness rather than a strength — the evidence is suggestive but lacks rigor, as noted above.

## Novel Insights

The paper's key conceptual move — using rough path theory to handle the singular-kernel limit — is genuinely novel in the NTK literature, even though the execution is incomplete. The observation that the predictor can converge while the kernel becomes singular opens a direction distinct from prior phase-transition analyses (Xiao et al., 2020; Seleznova & Kutyniok, 2022) that required invertibility or a non-singular component. The distillation of necessary conditions (diagonal dominance, eventual positive definiteness, vanishing determinant) for the technique to generalize to other kernel sequences is a useful meta-contribution that could guide future work.

## Suggestions

- Fix the ψ_d construction or replace it with a bump function whose derivatives are actually controlled in variation norm as D→0. The current ψ_d has a derivative that blows up at the midpoint t=1/2 — this is the root cause of the proof gap. A mollifier or smooth step function whose variation is controlled in the small-parameter limit would be more appropriate.
- Provide a more explicit characterization of the limiting predictor, not just existence. An eigendecomposition analysis of Θ̃_∞^{(L)} could yield convergence rates and an explicit form for the limit, substantially strengthening the contribution.
- Run experiments to L in the hundreds and explicitly quantify the difference between the predictor at moderate vs. very large depth to validate the fast-solution-convergence hypothesis.

## Calibration Anchors

Round 1 (bracketing):
- fUz6Qefe5z (3.00) — NTK for derivative labels. Weaker: poor presentation, no real evaluation, limited significance.
- 2NwHLAffZZ (2.33) — Weak correlations for linearization. Much weaker.
- NbbsRnPBoS (2.33) — Depth in deep linear networks. Much weaker.
- G2Lnqs4eMJ (2.50) — Optimal NN approximation. Much weaker.
- VEJzjAvaIy (5.75) — NTK divergence in classification. Stronger: correct, complete proofs with clear contribution.
- 5EtSvYUU0v (6.00) — Connecting NTK and NNGP. Stronger: unifies two frameworks with correct proofs.
- WH9NhxOeu9 (5.00) — Sharp generalization bounds. Comparable: correct but somewhat incremental results, presentation issues.
- h7GAgbLSmC (7.00) — Sharper guarantees for gradient methods. Much stronger: multiple improved bounds, well-executed.
- 4xWQS2z77v (8.00) — Convex duality for regularized NNs. Much stronger.
- P7KIGdgW8S (8.00) — Hölder stability of GNNs. Much stronger.
- STUGfUz8ob (7.60) — Transformers reasoning. Much stronger.
- AoraWUmpLU (8.00) — Activation functions in Neural ODEs. Much stronger.

Round 1 bracket: **4.0 – 6.0**

Round 2 (narrowing):
- 3LLkES6nNs (4.25) — Infinitely deep ResNets as GPs. Our paper is more novel and ambitious, even with the proof gap.
- kOtFuzoA93 (4.00) — Novel kernel models beyond over-parameterized regime. Our paper has a more focused contribution.
- LNYL96VIsD (4.75) — Large learning rates and singularities. Our paper is comparable in ambition.
- YN4uWzcbtt (4.25) — Positive definiteness of NTK. Correct but incremental; our paper is more ambitious.
- 5EtSvYUU0v (6.00) — Already read in Round 1. Stronger than our paper.
- VEJzjAvaIy (5.75) — Already read in Round 1. Stronger than our paper.
- WH9NhxOeu9 (5.00) — Read in full. The closest comparator: correct but incremental results, some overstatement, presentation issues. Our paper is more novel but has a significant proof gap — comparable overall.

Final score determined by comparison with WH9NhxOeu9 (5.00): our paper has a more novel approach but an unproven main theorem, placing it at the same level — **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>