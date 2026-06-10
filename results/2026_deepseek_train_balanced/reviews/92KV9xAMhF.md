Here is the final consolidated review:

## Summary

This paper provides the first theoretical analysis of the "conservativity" debate in diffusion models by deriving a gauge freedom condition from the Fokker-Planck equation. The core contributions are: (1) a necessary and sufficient condition (Eq. 6) under which a non-conservative vector field still yields exact sampling and density estimation, (2) an orthogonal decomposition of vector fields into conservative and gauge-satisfying components with implications for the score-matching loss, and (3) an analysis linking conservativity to correct intrinsic dimensionality estimation. The paper's central insight — that conservativity is not required for global tasks (sampling/density estimation) but is beneficial for local tasks (ID estimation) — is clearly stated and well-motivated.

## Strengths

1. **First analytical derivation of the gauge freedom condition for diffusion models.** The derivation from the Fokker-Planck equation (lines 90–103) is clean and correct: starting from the evolution of the marginal density, the paper shows that any remainder term r_θ satisfying ∇·r_θ + r_θ^T∇log p = 0 preserves exact sampling and density estimation. This is a genuine theoretical contribution to a question previously addressed only through contradictory empirical results (Salimans 2021, Chao 2023, Wenliang, etc.).

2. **Orthogonal decomposition of vector fields in L²(p) (Theorem 1).** The decomposition of any vector field into a conservative component and a gauge-satisfying component, with orthogonality in the L²(p) inner product, provides a new geometric interpretation of the score-matching loss (Eq. 10). This cleanly separates the loss into a term relevant for sampling/density estimation (the conservative part) and an irrelevant term (the gauge part).

3. **Explicit analytical counter-example (Section 4).** The 2D Gaussian construction (lines 141–166) is a rigorous mathematical proof, not an empirical observation: the anti-symmetric remainder R_t x_t is divergence-free, orthogonal to the score, and explicitly non-conservative (non-symmetric Jacobian). This directly disproves any assertion that conservativity is required for exact sampling/density estimation.

4. **Theoretical framing of the ID estimation problem (Theorem 2).** The connection between the Jacobian of the backward vector field, conservative structure, and intrinsic dimensionality is novel. The theorem identifies a specific scenario (conservative field + commutativity) under which the rank of exp(∇f̃_θ(x₀,0)) equals the true ID — providing a theoretical justification that prior work on diffusion-based ID estimation (Wenliang, Batzolis 2022) lacked.

## Weaknesses

### Fatal
None.

### Major

1. **The commutativity assumption in Theorem 2 is not adequately justified, creating a gap between theory and experiments.** The theorem requires [P_t(x₁), ∇f̃_θ(φ_t(x₁),t)] = 0 for all t ∈ [0,ε]. The Remark (lines 221–223) argues this is reasonable because the eigenvectors of both matrices "align with the normal and tangent space of the manifold." However, alignment with the same *subspaces* does not imply commutativity — two matrices commute iff they are simultaneously diagonalizable, which requires sharing the *same eigenvectors*, not merely spanning the same subspaces. If the tangent space is more than 1-dimensional, two matrices could have eigenvectors spanning it but in different bases, and they would not commute. The paper acknowledges this assumption is "strong" (line 249) and resorts to empirical validation, but this creates a logical tension: if the premise is violated in the experiments yet the experiments confirm the conclusion, the theorem does not actually *explain* the empirical results. The paper's claim in the introduction that "a conservative diffusion is guaranteed to make the right conclusions" (line 22) overstates what the theorem supports given this gap.

### Minor

2. **The ID experiments do not fully isolate conservativity as the causal factor.** The comparison is between a conservative model (s_θ = ∇‖ψ_θ‖², a constrained architecture requiring an additional backward pass) and a non-conservative model (s_θ = ψ_θ directly). These differ in parameterization, architecture, and optimization landscape — not only in the mathematical property of conservativity. The paper mentions (lines 228–229) that adding a symmetry penalty to the non-conservative model also fails, but the full results for this control are deferred to the supplementary material. For the main paper's central visual argument (Figure 2), the reader cannot assess whether the failure is due to non-conservativity *per se* or to architectural/optimization differences.

3. **The numerical computation of Y_t in the ID experiments is underspecified.** The paper describes Y_t through the sensitivity ODE (dY_t = ∇f̃ Y_t dt, line 205–207) and states that its singular values can be obtained from the eigenvalues of ∇f̃. But it does not explain how Y_t (or its singular values) is numerically approximated — whether by solving the augmented ODE, differentiating through the ODE solver, or computing the Jacobian of the solution map. Since the singular-value trajectories in Figure 2 are the primary visual evidence for the ID claims, some implementation detail is needed to assess numerical reliability.

4. **The gauge condition involves the unknown true score, limiting its practical force.** The condition ∇·r_θ + r_θ^T∇log p = 0 requires access to the very quantity (p(x,t)) the diffusion model is trying to learn. The paper acknowledges this (line 247) and suggests future work on penalty terms, but as a result, the paper's positive prescription ("the gauge freedom condition needs to be fulfilled," line 21) is not actionable for practitioners. This does not diminish the theoretical contribution but does limit its immediate practical impact.

### Trivial

None.

## Nice-to-Haves

- Presenting at least one additional singular-value trajectory plot (e.g., sphere or Swiss roll) in the main paper rather than deferring all but the Gaussian example to the supplementary would strengthen the paper's central visual argument.
- Clarifying the numerical procedure for computing Y_t / its singular values in the ID experiments would improve reproducibility.

## Removed Points

These points were flagged by the reviewers but are removed from the main weaknesses for the following reasons:

- **Grammar/typo artifacts (line 29 fragment, "figute" typo)**: Removed per instruction — these are PDF parsing artifacts, not present in the original submission.
- **"Only one sample's singular values shown"**: Removed — the paper explicitly notes "we observe the same behavior across different samples" (line 226), and this is a space constraint for a proof-of-concept experiment.
- **"Oscillating messaging" about whether non-conservative models could also estimate ID**: Removed — the paper is consistent on this point (line 249 clearly states the gauge-satisfying case would also work but is hard to achieve in practice).
- **Generic criticism about "the evaluation lacks rigor" without concrete anchor**: Removed — this is a sweep-level concern without a specific, verifiable anchor in the paper text.
- **Criticism about missing related works**: Removed per instruction — external verification of completeness is not possible.
- **Strength Finder strengths about "addressing an important problem"**: Removed — generic statements not specific to the paper's concrete contributions.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one insight: the gauge freedom condition (Eq. 6) can be viewed as a continuity equation constraint on the error field r_θ. The requirement that ∇·(r_θ p) = 0 means the error field induces no net probability flow in the Fokker-Planck picture. This geometric interpretation — that r_θ must be divergence-free in the *density-weighted* sense — connects the gauge condition to the broader literature on probability flow ODEs and might suggest alternative enforcement strategies (e.g., penalizing the divergence of (s_θ p̃) where p̃ is a learned or estimated density proxy) that differ from the suggested but unworkable direct penalty.

## Suggestions

1. **For Theorem 2**: Either (a) weaken the commutativity assumption to a more plausible spectral condition (e.g., that P_t and ∇f̃_θ share invariant subspaces at t=0, without requiring simultaneous diagonalizability for all t ∈ [0,ε]), or (b) reframe the ID experiments as heuristic validation of a conjecture rather than as direct support for the theorem. The paper's own Discussion already moves in this direction (line 249: "we hypothesize"), and the abstract/intro should be adjusted to match.

2. **For the ID experiments**: Include at minimum one full figure (in the main paper) showing the penalty-controlled non-conservative model's singular values alongside the conservative and unconstrained non-conservative results, to support the claim that the failure is due to non-conservativity rather than architecture.

3. **Tone calibration**: The introduction states that "a conservative diffusion is guaranteed to make the right conclusions" (line 22) about ID estimation. Given the commutativity gap, "guaranteed" overstates the result. Recommend softening to "can be expected to" or "is sufficient (under stated conditions) to."

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>