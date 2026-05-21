## Summary

This paper proposes quantum Frank-Wolfe (FW) algorithms for projection-free sparse convex optimization in both vector domains (ℓ₁-ball, simplex, latent group norms) and matrix domains (nuclear norm). For vector constraints, it achieves O(√d/) query complexity per iteration (vs. classical O(d)) using a function-value oracle. For matrix constraints, it presents two algorithms with time complexities Õ(rd/ε²) and Õ(√(rd)/ε³) for the update-direction computation. The vector results are sound and demonstrate a clear query-complexity speedup. The matrix results are novel in scope but are undermined by an unaddressed cost of constructing the quantum data structure each iteration — a gap that prevents the claimed time-complexity advantage from being convincingly established.

## Strengths

1. **First systematic quantum treatment of FW for both vector and matrix constraints.** The paper is the first to extend quantum acceleration to the matrix-domain (nuclear norm) FW linear subproblem, proposing two complementary algorithms (QTSVE and QPM) with different tradeoffs between rank dependence and precision sensitivity. This goes significantly beyond the prior work of Chen & de Wolf (2023), which only addressed a specific linear-regression setting.

2. **Provable O(√d) query-complexity speedup for vector-domain FW.** Theorem 1 (ℓ₁-ball) and Theorem 2 (simplex) establish a clean query-complexity reduction from O(d) to O(√d) per iteration using only a function-value oracle. The error analysis is carefully controlled: the gradient-approximation parameter σ_t is set to C_t/(√d L(t+2)) so that the FW convergence guarantee is preserved (Appendix B.3). This is the paper's strongest contribution.

3. **Generalization to latent group norm constraints (Theorem 6).** The paper extends the quantum FW framework beyond simple ℓ₁ and simplex constraints to latent group sparsity, achieving query complexity Õ(√(|𝒢|)·|𝒢|_max) and an O(√(|𝒢|)) speedup. The dual-norm computation across groups in quantum superposition is a non-trivial technical extension.

4. **Rigorous error propagation analysis throughout.** For both the vector and matrix algorithms, the paper traces how approximation errors from quantum subroutines (finite-difference gradient estimation, singular value estimation, state tomography) propagate into the FW convergence bound, and sets parameters to absorb these errors into the standard O(1/t) convergence rate. This is done carefully (e.g., δ_t, ε_t choices in Theorems 3 and 4).

## Weaknesses

### Fatal
None.

### Major

1. **Unaccounted cost of quantum data structure preparation for the matrix algorithms.** The matrix algorithms (Theorems 3 and 4) rely on Assumption 4 (quantum access to matrix M) to enable fast singular value estimation and quantum power iteration. This assumption requires a tree-based QRAM data structure supporting queries in Õ(1) time. The gradient matrix M_t = ∇f(X_t) changes every FW iteration, but the paper does not discuss the cost of constructing or updating this data structure. Even assuming the gradient is pre-computed classically (Remark 3), building the QRAM for a dense d×d matrix costs Ω(d²). The claimed per-iteration complexities — Õ(rd/ε²) and Õ(√(rd)/ε³) — are asymptotically smaller than d² for large d (since r ≤ d), so this overhead would dominate and eliminate the claimed speedup. Without a discussion of how quantum access is obtained at an acceptable cost in this iterative setting, the matrix-domain complexity bounds are not credible as stated.

2. **Overclaimed speedup for the matrix domain.** The abstract claims the matrix algorithms "reduc[e] at least a factor of O(√d) over the best classical algorithm." However, comparing the complexities in Table 2 gives a speedup that depends on ε, r, and spectral gaps in ways that do not straightforwardly yield O(√d). For QTSVE vs. classical power method: ratio ≈ dε/r (not √d). For QPM vs. Lanczos: ratio ≈ √(d/r)·ε^(2.5). The claimed √d factor in the abstract is not supported by the paper's own complexity expressions. This overclaiming should be corrected.

### Minor

3. **Incomplete success probability analysis for the matrix algorithms.** The matrix subroutines (QSVE, tomography, quantum maximum finding) each succeed with probability 1−1/poly(d). The paper states that "the success probability can be improved by repeating it logarithmic times and then taking the average" but does not incorporate the necessary overhead into the stated complexity bounds of Theorems 3 and 4. While the poly(d) failure probability likely covers the T = O(1/ε) iterations via a union bound, this is not made explicit, and the cost of constant-factor boosting for high-probability guarantees is not quantified. This is addressable but should be clarified.

4. **State preparation overhead partially masks the √d speedup in the vector case.** The paper acknowledges that the incremental state-preparation cost for |x^(t)⟩ is O(t) per iteration, and total T = O(1/ε), making the cumulative cost O(1/ε²). Table 1 lists gate complexity as O(√d), which focuses only on the maximum-finding circuit. While this is disclosed in the text, the presentation (especially Tables 1–2 and the abstract) emphasizes the √d factor without clearly separating it from the ε-dependent overhead. A more balanced presentation would help.

### Trivial

5. **ℓ₂ vs ℓ∞ gradient error bound not made explicit.** Lemma 2 gives an ℓ₂ error bound for the finite-difference gradient, but Lemma 4 (maximum finding) needs an ℓ∞ bound (per-component). The parameter choice σ_t = C_t/(√d L(t+2)) controls the per-component error, but the reasoning connecting ℓ₂ to ℓ∞ is left implicit. The paper would benefit from an explicit statement.

## Nice-to-Haves

- A discussion of whether the quantum data structure for the gradient matrix could be updated incrementally across FW iterations (e.g., if the gradient changes are low-rank or admit sparse updates).
- A comparison with Chen & de Wolf (2023) that quantitatively contrasts the oracle models and complexity regimes.
- A dedicated limitations section discussing the dependence on eigenvalue gaps, the parameter γ'_min in the quantum power method, and the practical feasibility of the QRAM assumption.

## Removed Points

The following points from the input reviews were removed:

- **Table 2 T_∇ inconsistency**: The harsh critic claimed classical rows include T_∇ while quantum rows do not. This is factually wrong — all four rows in Table 2 include "+ T_∇" and are internally consistent. (Source: Table 2, lines 90–93.)
- **Criticism about missing related works**: Removed per instruction (cannot verify existence of external references).
- **Formatting/style nitpicks and typo flags**: Removed per instruction (parser artifacts, not author errors).
- **Missing appendix / missing proofs**: Removed per instruction (parser strips these from all papers).
- **Generic "evaluation lacks rigor" / "baselines may not be fair" sweeps without concrete anchors**: Removed.
- **Several strengths from the Strength Finder that were generic or sycophantic**: Removed (e.g., generic statements about "Careful error control" without specific evidence were moved here; the substantive error analysis point is retained as strength #4 above).

## Novel Insights

None beyond the paper's own contributions. The two reviews identify the same core issues in complementary ways: the harsh critic correctly identifies the QRAM data-structure gap in the matrix section and the overclaimed √d speedup; the strength finder correctly identifies the soundness of the vector results and the novelty of the group-norm extension. No reviewer offers a fundamentally new observation about the paper's approach that goes beyond what the paper itself articulates.

## Suggestions

1. **Address the QRAM data-structure cost for the matrix algorithms.** Either propose a method to compute the gradient directly into a quantum-accessible form (so that the data structure is built in one pass), analyze the incremental update cost (showing it does not asymptotically dominate, e.g., for sparse or low-rank gradient changes), or explicitly characterize the regime where the data-structure overhead does not negate the speedup.

2. **Correct the overclaimed speedup factors.** Revise the abstract and introduction to state the matrix speedup using the actual expressions from Table 2 with explicit dependence on ε, r, and spectral gaps, rather than claiming a generic O(√d) factor.

3. **Rigorize the success probability analysis.** Provide a union bound over T iterations, state the total success probability, and verify that the cost of boosting (if needed) does not affect the asymptotic bounds.

4. **Split or restructure the paper.** The vector contributions are self-contained and defensible; the matrix contributions need substantial revision. Consider splitting into two papers, or reworking the matrix section as a separate algorithms section with caveats about the access model.

## Score and Decision

**Bracket.** Round 1 (bracketing): This paper sits between weak anchors near score 3 (e.g., the noise-resilient PQC paper at 3.0) and strong anchors above 7.5 (e.g., topological data analysis at 8.0). The plausible range after round 1 was 4–6.

**Narrowing.** Round 2 targeted papers in (3.5, 5.5) and (5.5, 7.5). The closest anchors are:
- *Catalyst Framework for QLSP* (5.25, Reject): a meta-algorithm with a novel idea but incremental overall, similar to this paper's vector section. The present paper is comparable in technical quality but more ambitious in scope. The matrix section's unaddressed data-structure issue is a larger gap than the catalyst paper's main weakness (single-iteration limitation).
- *Quantum Speedups in Linear Programming* (5.33, Reject): technically strong but poor presentation. The present paper is better written but has a more central technical gap.
- *Quantum Sparse Online Learning* (4.80, Reject): a straightforward application of quantum subroutines to a known algorithm. The present paper is more comprehensive and has more rigorous error analysis, so it is slightly stronger.
- *Near-Optimal Quantum Algorithm for Minimizing Maximal Loss* (6.00, Accept): cleaner results with matching lower bounds, tighter exposition. The present paper is weaker by comparison.

Compared against these anchors, the paper sits between 4.80 and 5.33 — closer to 5.0. The vector results are solid but incremental (applying finite-difference + quantum maximum finding to FW is a relatively direct combination). The matrix results are more novel but carry a significant unaddressed flaw. A score of 5.0 reflects that the paper makes genuine but incomplete contributions, and the matrix section requires substantial revision before its claims can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>