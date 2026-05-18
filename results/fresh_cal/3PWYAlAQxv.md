Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proves that neural networks trained exclusively by permuting (reordering without changing) their initialized weights are universal approximators for one-dimensional continuous functions. The proof constructs step-function approximators via a novel four-pair basis-function design and eliminates unused parameters through a linear-reorganization method — both techniques tailored to the extreme constraint that weight values are fixed and only their order can change. Numerical experiments validate the predicted n^{-1/2} convergence rate and demonstrate the approach across equidistant, pairwise-random, and fully-random initializations.

## Strengths

- **First theoretical guarantee for permutation training.** Prior work (Qiu & Suda, 2020) only showed empirical evidence. This paper provides the first proof that permutation-trained ReLU networks are universal approximators — a genuinely novel theoretical contribution. The four-pair construction (Eq.~\ref{eq:coefficients_step}) and linear-reorganization method (Lemma~\ref{th:Leibniz}) are explicitly designed for the permutation constraint and are absent from standard UAP proofs that freely choose weights.

- **Clever constructive proof techniques.** The four-pair basis-function design creates a step approximator where the coefficient–bias mapping is one-to-one and uses exactly the fixed values {±b_i}. The linear reorganization cancels the effect of unused parameters while respecting the permutation constraint. The pseudo-copy technique (Theorem 2) further removes the need for learnable scaling factors. These constructions are novel and non-trivial.

- **Numerical validation confirms the predicted convergence rate.** Experiments (Fig.~\ref{fig:1D}) show the L^∞ error scales as roughly n^{-1/2} with network width n, matching the theoretical estimate. The paper covers equidistant, pairwise-random, and fully-random initializations, demonstrating the UAP is not an artifact of a special initialization.

- **Clear and well-organized exposition.** The proof is structured in three clearly delineated steps (piecewise constant approximation, step-matching construction, unused-parameter elimination), and the four-pair construction is illustrated with helpful figures.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The proof of Theorem 3 (random initialization) is presented at a lower level of rigor than Theorems 1 and 2.** The argument proceeds by showing that, with high probability, a randomly initialized network contains a subnetwork whose biases and coefficients are within Δr of an equidistant network's parameters. The existence of such a subnetwork is established via an inclusion–exclusion probability calculation over disjoint intervals, which guarantees distinct indices. The reasoning is structurally valid — the intervals are chosen to be non-overlapping (line 604: "Δr small enough such that these intervals have no overlap"), ensuring that finding one parameter in each interval yields a valid matching. However, the presentation is compressed: the probability bound is stated in terms of the exact inclusion–exclusion formula, the relationship between the subnetwork's parameters and the required permutation is not spelled out step-by-step, and mixing expectation with high-probability statements (lines 623-624) is informal. A direct high-probability bound (e.g., via a union bound or maximal-gap concentration) would be cleaner. This does not invalidate the result but means the proof is less polished than the equidistant case. The equidistant-case proofs (Theorems 1 and 2) are rigorous and well-constructed.

- **The proof of Lemma 1 (piecewise constant approximation) contains a sloppy argument.** The proof states "According to the Stone–Weierstrass theorem, we assume f^* to be a polynomial function for simplicity" and then constructs step locations s_j where f^*(s_j) = (k_j+0.5)Δh. For an arbitrary continuous function, such points may not exist (the function may not attain these exact values). The lemma itself is standard and true, and the fix is straightforward (partition the domain into small subintervals and bound the error by the modulus of continuity). This is a presentation flaw in a supporting lemma, not a gap in the main results.

- **The L^∞ error bound for step-function approximation is called "trivial" by the paper itself** (line 239: "It is obvious that the L^∞ error has the following trivial bound"). This is correct — the bound h only needs to be small after scaling — but the paper could note that tighter bounds exist in L^2 (which it later derives in Section 3.5).

### Trivial

- The error accumulation argument in Theorem 1 (step b) asserts E_use ≤ h (line 379) without explicitly stating that the supports of different step approximators are disjoint. The paper does state that the index sets K_j have empty intersection (line 353), which implies disjointness, but a brief clarifying sentence would help the reader.

## Nice-to-Haves

- A comparison with traditional (non-permuted) training of the same architecture would strengthen the practical claims. The current experiments only compare across initialization strategies within the permutation-training regime.
- The discussion relating the proof to the lottery ticket hypothesis (LTH) could be elaborated, since both involve structured weights, but this is outside the paper's stated scope.

## Removed Points

- **Criticism about w_i = ±1 lacking justification.** REMOVED: The paper explicitly justifies this via positive homogeneity of ReLU (line 93: "Since ReLU activation is positively homogeneous... we consider a homogeneous case with w_i = ±1"). This is standard.

- **Criticism about disjoint-support assumption not being "explicitly argued."** REMOVED: The paper states "{K_j}_{j=1}^J has empty intersection" (line 353), which directly addresses this.

- **Criticism that the error bound in Eq.~(\ref{eq:fs_error}) is trivial.** REMOVED: The paper itself calls it "the following trivial bound" (line 239). The critic is restating a self-acknowledged fact, not identifying a flaw.

- **Request for detailed LTH comparison or algorithmic permutation-search discussion.** REMOVED as scope creep. The paper's contribution is an existence proof, not an algorithm analysis.

- **Strength about "permutation-active patterns" as a major strength.** WEAKENED: This observation is interesting but preliminary and qualitative. It is a supporting observation, not a core contribution of the paper.

## Novel Insights

The key insight that emerges from the reviews — beyond the paper's own contributions — is that the permutation-trained UAP problem exposes a fundamental tension in approximation theory: the same weight values must serve two competing purposes simultaneously (constructing the desired function and canceling out unused parameters). The paper's linear-reorganization and constant-matching techniques resolve this tension in 1D, but the reviewers correctly identify that the random-initialization case (Theorem 3) introduces a third layer of difficulty — matching random continuous values to discrete required positions — that is handled less cleanly than the deterministic constructions. None of the reviewers raised issues that fundamentally undermine the core contribution; the paper's main results (Theorems 1 and 2) stand on solid ground.

## Suggestions

1. Tighten the proof of Theorem 3 by replacing the inclusion–exclusion argument with a simpler union bound (or explicit high-probability bound on maximal gaps of uniform points), and step through the permutation construction more explicitly. This would address the main rigor concern without changing the result.

2. Rewrite the proof of Lemma 1 using a standard partition-of-domain argument (e.g., divide [0,1] into M equal subintervals, set the constant value to f^* at the left endpoint, bound error by modulus of continuity). This avoids the questionable existence of points where f^* attains half-integer values.

3. Add a one-sentence clarification that the index sets K_j having empty intersection implies the supports of the step approximators are disjoint, so the sup-norm error of the sum is the maximum (not sum) of individual errors.

## Score and Decision

**Calibration anchors:**

| Path | Avg Human Score | Comparison |
|------|----------------|------------|
| dpDw5U04SU (Min width for UAP) | 7.00 | More rigorously polished proofs but incremental over prior work; the current paper has more novelty but slightly less polish |
| 34STseLBrQ (Polynomial width for set rep.) | 7.25 | Stronger theoretical rigor and wider scope; the current paper has more novelty in problem setting |
| 5xwx1Myosu (Random weights, learned biases) | 6.50 | Similar "constrained training" UAP paper; comparable quality and contribution |
| FwdN0KovFp (Stable PCN) | 3.75 | Fundamental issues with experiments and novelty; the current paper is clearly stronger |
| j0sq9r3HFv (LLM param extraction) | 2.50 | Preliminary work with weak results; the current paper is in a different tier entirely |
| P7KIGdgW8S (Hölder stability of GNNs) | 8.00 | More comprehensively developed theory and experiments; the current paper is notably less polished |

The paper makes a genuine theoretical contribution to a novel problem, with clever constructive proofs. The main results (Theorems 1 and 2) are rigorous. Theorem 3 has some presentational informality but is not fundamentally flawed. The paper is well-written, the experiments validate the theory, and the limitations (1D, specific initializations) are honestly discussed. Relative to the calibration anchors, it sits firmly in the mid-range — more novel than the incremental minimum-width paper but less polished than the top-tier GNN stability paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>