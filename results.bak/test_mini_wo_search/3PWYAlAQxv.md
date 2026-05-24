Now I have all the information needed. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
- suggestion

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Here is my final review:

## Summary

This paper proves the universal approximation property (UAP) for one-hidden-layer ReLU networks whose second-layer weights are trained solely by permuting a fixed initial vector, without changing their values. The constructive proof uses a novel four-pair step-function approximator and a linear-reorganization method to eliminate unused parameters. Results cover equidistant initialization (Theorems 1–2), random initialization (Theorem 3), and are supported by numerical experiments on 1D regression.

## Strengths

1. **First theoretical guarantee for permutation training.** The paper proves UAP for networks trained by weight permutation only, a method previously supported only empirically (Qiu & Suda, 2020). This is stated in the abstract and substantiated by Theorems 1–3. The construction is non-trivial: unlike standard UAP proofs, every parameter must be used because permutation training cannot discard weights.

2. **Novel four-pair construction respecting the permutation constraint.** The step-function approximator (Section 3.1) uses exactly four pairs of basis functions with coefficients matched one-to-one to the biases {±b_i}, ensuring each coefficient is used exactly once. This directly addresses the key difficulty that the proof "must utilize every parameter, rather than just pick up the desired parameters and discard the rest" (Section 2.4).

3. **Linear reorganization and Leibniz-test elimination of unused weights.** Lemma 4 provides a method to bound the residual linear function from unused parameters using an alternating-sum construction, which is essential because permutation training cannot discard parameters. This technique is applied in Theorem 1 to control the slope of the unused part and bound the approximation error.

4. **Probabilistic extension to random initialization.** Theorem 3 extends the result to uniformly random biases and pairwise-random weights, giving a probability bound for sufficiently wide networks. The extension strategy—finding a close-to-equidistant subnetwork in the random network—is sound.

5. **Numerical validation of key claims.** Experiments in Section 4 show convergence behavior consistent with the theoretical results, including an L^∞ error rate of approximately n^{−1/2} for equidistant and pairwise random initializations, matching the theoretical L² rate from Section 3.5.

## Weaknesses

### Fatal
None.

### Major

1. **Probability conjunction in Theorem 3 is not properly justified.** The proof claims P_sub ≥ √(1−δ) (subnetwork approximation) and P_un ≥ √(1−δ) (unused-part bound), then concludes that the conjunction of both events holds with probability ≥ 1−δ. The paper provides no justification for how the conjunction probability follows from these individual bounds. Since the two events are not independent (they occur on the same random draw), the natural approach is a union bound, which would give P[both] ≥ P_sub + P_un − 1 ≥ 2√(1−δ) − 1. This does not generally equal 1−δ (e.g., δ = 0.05 gives 2√0.95 − 1 ≈ 0.949, not 0.95). The proof would need P_sub ≥ 1−δ/2 and P_un ≥ 1−δ/2 for the union bound to yield 1−δ, or a different coupling argument. This gap is fixable but needs to be addressed for the theorem to be convincing. (Section 3.5, proof of Theorem 3, steps c–e)

2. **The existence of r₀ and the continuity argument in Theorem 3 are asserted without justification.** The proof states "for sufficiently small Δr < r₀, the subnetwork f_sub^NN will approach f_equi^NN" (line 585) without establishing how r₀ depends on the network size or the function, and without a continuity argument connecting the perturbation of parameters to the output error. While the claim is plausible (the network output is continuous in its parameters), the proof simply asserts existence. For a theorem claiming a precise probability bound, the dependence between parameter perturbation and approximation error needs to be quantified. (Section 3.5, proof of Theorem 3, step b)

### Minor

3. **The bound Δb ≤ 2/(γ\hat n) in Theorem 1 is presented without sufficient algebraic derivation.** The paper states (line 390) that d = 1/(n−1) < 1/(γ\hat n) ensures Δb ≤ 2/(γ\hat n). While the inequality chain is correct given the parameter choices (n = L(ĥn−1)+1 with L ≥ γ), the derivation of d < 1/(γ\hat n) and its relationship to Δb is too terse. A reader cannot immediately verify the bound without reconstructing the relationships among n, L, ĥn, γ, and d. This step is central to the unused-part error bound; the paper would benefit from an explicit inequality chain. (Section 3.3, proof of Theorem 1, step c)

4. **Scope framing slightly overstates the generality of the results.** The title "Neural Networks Trained by Weight Permutation are Universal Approximators" does not specify the one-dimensional input setting, which is a genuine restriction of the proof (w_i = ±1, pairwise ±b_i initialization, 1D domain [0,1]). The abstract and introduction do state "one-dimensional continuous functions," and the paper is explicit about its scope in the technical sections, but the title and the third "main finding" (permutation training as a tool for describing learning behavior, which is supported only by qualitative observations) risk misleading readers about what is rigorously established.

5. **The pseudo-copy error bound in Theorem 2 uses a loose triangle inequality that is not fully discussed.** Eq. (16) bounds the pseudo-copy error as Lh + Δh = 2Δh, relying on the sum of L per-copy errors each bounded by h. This is tight only if all pseudo-copy errors align in the same direction. The bound is conservative enough for a UAP result but merits explicit acknowledgement. (Section 3.4, proof of Theorem 2, step b)

6. **The analysis of permutation-active patterns (Section 4.6) is observational and lacks statistical validation.** The four-stage classification of permutation behavior and the hypothesized ribbon-like patterns are interesting observations but are not supported by quantitative evidence or statistical tests. The paper appropriately describes this as a "preliminary attempt," but including it as a "main finding" in the introduction inflates what is rigorously established.

### Trivial
None.

## Nice-to-Haves

- A theoretical L^∞ convergence bound (even a loose one) would strengthen the paper beyond the current L² estimate.
- The adaptation from domain [0,1] (used in proofs) to [−1,1] (used in experiments) could be explicitly noted for reproducibility.
- A brief positioning of permutation training relative to other constrained training approaches (weight-sharing, sign-constrained networks) would help contextualize the novelty.

## Removed Points

The following criticisms from the input reviews were removed with justification:

1. **"The elimination of unused parameters is not fully rigorous" as a methodological gap.** The harsh critic claimed the bound Δb ≤ 2/(γ\hat n) is insufficiently justified. Verifying the actual inequalities (d = 1/(n−1) = 1/(L(ĥn−1)) ≤ 1/(γ(ĥn−1)) < 1/(γ\hat n), and Δb ≤ 2d < 2/(γ\hat n)) shows the bound is correct. The presentation could be clearer (kept as Minor weakness #3 above), but it is not a methodological gap. **Downgraded from "methodological gap" to Minor.**

2. **"The four-pair construction depends on coefficient availability that is not verified" (Critical Issue 4).** The harsh critic argued that residual biases in Theorem 2 cannot be guaranteed to be small enough. However, for the equidistant initialization used in Theorem 2, the smallest bias in the remaining pool is at most O(1/n), which can be made arbitrarily small by increasing n. The paper's argument is valid for its stated setting. **Removed entirely.**

3. **Various nitpicks about missing derivations, proof details, and formatting** from the section-by-section notes that either misunderstand the paper or request depth beyond what is standard for UAP proofs. **Filed here as minor presentational concerns, not substantive weaknesses.**

4. **Strength Finder #3 (linear reorganization as a core strength)** is genuine but subsumed by strength #1 above. **Merged.**

## Novel Insights

The most interesting observation that emerges from the reviews but is not made by the paper itself is the asymmetry in difficulty between the equidistant case (solid, clean proofs) and the random-initialization case (where the probabilistic machinery has gaps). This suggests that the core technical contribution is the deterministic construction and the Leibniz-test elimination, while the extension to randomness requires a substantially different or more careful probabilistic framework than currently provided. The paper's value rests primarily on the equidistant construction (Theorems 1–2), which is genuinely novel and well-executed.

## Suggestions

1. Fix the probability handling in Theorem 3: replace the qualitative "sufficiently large n" with a union-bound argument. Specifically, show that for a given δ, one can choose n large enough so that P_sub ≥ 1 − δ/2 and P_un ≥ 1 − δ/2, then the conjunction has probability ≥ 1 − δ by union bound. Alternatively, provide explicit rates using Chernoff or concentration inequalities.

2. Justify the existence of r₀ in Theorem 3. Provide a continuity argument or modulus-of-continuity bound showing how the network output changes under parameter perturbations of size Δr.

3. Add an explicit inequality chain for the Δb bound in Theorem 1, step (c), showing how d < 1/(γ\hat n) follows from n = L(ĥn−1)+1 and L ≥ γ, and how this implies Δb ≤ 2/(γ\hat n).

4. Adjust the title and framing to accurately reflect the 1D scope, or temper the claim in the third "main finding" (learning-behavior description) to match its observational nature.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>