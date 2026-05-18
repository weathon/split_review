Now I have a solid understanding of both the paper and the calibration anchors. Let me produce the final consolidated review.

## Summary

This paper proves, for the first time, that neural networks trained solely by permuting their initial weights (without altering weight values) satisfy the universal approximation property for one-dimensional continuous functions. The authors develop a constructive proof using a novel four-pair step-function approximator, a linear reorganization method to eliminate unused parameters, and a pseudo-copy technique to remove dependence on a trained output layer. Numerical experiments validate the predicted O(n^{-1/2}) convergence rate and demonstrate approximation behavior for 1D, 2D, and 3D regression tasks.

## Strengths

- **First theoretical guarantee for permutation training**: The paper establishes the first theoretical foundation for a method that previously relied entirely on empirical evidence (Qiu & Suda 2020). The UAP proof is genuinely novel and addresses a nontrivial constraint — every parameter must be used exactly once, and weight values cannot change.

- **Novel four-pair step-function approximator designed for the permutation constraint**: The construction in Eq. (5) uses exactly the set of allowed coefficients {±b_i} to build a step function approximator, which is fundamentally different from the standard two-ReLU construction (Remark after Eq. 6) that would require coefficient values not available under permutation.

- **Linear reorganization and Leibniz's-test lemma provide a clean solution to a problem specific to permutation training**: The fact that every parameter must be used (none can be discarded) is a distinctive challenge. Lemma 1 and the subsequent slope-control argument give an elegant way to render the unused portion harmless by rewriting it as a linear function with bounded slope.

- **Numerical verification of the predicted O(n^{-1/2}) convergence rate**: Figure 2 shows that the L∞ error scales as ∼ n^{-1/2} for both equidistant and pairwise random initializations, matching the theoretical estimate derived in Section 3.4. The experiments also systematically explore initialization strategies and identify cases where common choices (Xavier, He) fail under permutation constraints.

## Weaknesses

### Major

- **Experiments do not isolate the power of permutation from gradient-based guidance**: The LaPerm algorithm interleaves Adam gradient updates (which temporarily change weight values) with periodic permutations. The theory proves existence of a permutation achieving approximation, but the experiments rely on gradient information to guide the search. No experiment tests whether a purely permutation-based search (e.g., random permutation search, greedy swapping without Adam) can find a good permutation. The paper states "our proof does not rely on any specific algorithmic implementations" (Sec. 5.3), which is true for the theory, but the experiments then do not actually test the existential claim — they test a hybrid algorithm. A simple control experiment (e.g., enumerating random permutations for small n without any gradient steps) would directly test the theoretical claim.

- **Random initialization guarantee (Theorem 3) is non-constructive**: The inclusion-exclusion probability bound requires n to be extremely large, and no concrete scaling is provided. The numerical experiments show that moderate widths work well for pairwise random initialization, suggesting a large gap between the theoretical guarantee and practical performance. While non-constructive existence proofs are standard in UAP theory, the paper positions itself as a foundation for practical training (mentioning hardware accelerators, photonic tensor cores), and the lack of a concrete width estimate weakens this connection.

### Minor

- **The main result covers only a restricted architecture**: The theorems apply to one-hidden-layer ReLU networks with first-layer weights fixed to ±1 and only the second-layer coefficients permuted. While the paper is explicit about this setting, the title and framing ("Neural Networks Trained by Weight Permutation are Universal Approximators") suggest a broader generality. The paper does discuss extensions to deeper networks (Sec. 8 in the appendix) and leaky-ReLU (Sec. 7), but these are sketched rather than proven. A paper with a more precise title (e.g., "One-Hidden-Layer ReLU Networks...") would better match the actual scope.

- **Error analysis of pseudo-copy construction relies on approximations treated as small without a rigorous bound**: The pseudo-copy analysis in Section 3.4 treats the mismatch Δs_l as O(d) and uses this to argue that e_{s,p_l} ∼ O(d^{5/2}). The error accumulation over L ∼ O(d^{-2}) copies is then bounded by L·O(d^{5/2}) = O(d^{1/2}). While the conclusion is likely correct, the argument that the Δs_l-dependent terms remain O(d) without blowing up as L increases is handled by estimation rather than a strict bound. A rigorous inequality chain would strengthen this part.

- **No free-training baseline in the 1D regression experiments**: Without comparing to a standard fully-trained network of the same width, the reader cannot judge whether the approximation error shown is competitive or poor. The 1/2 convergence rate is compared to the theory, but a practical baseline would contextualize the results.

- **The 2D and 3D experiments show degraded convergence rates (1/2 → 1/6)** and the paper honestly admits this, but these results highlight that the theoretical proof does not extend to higher dimensions in a straightforward way. The paper's core claim about UAP is for 1D functions, and the multi-dimensional experiments are exploratory.

### Trivial

- None beyond standard parser artifacts.

## Nice-to-Haves

- A purely permutation-based search experiment (e.g., random permutations or greedy coefficient swapping for small n, without any gradient updates) would directly test the existential claim of the theory.
- A free-training baseline for the 1D regression tasks would help contextualize the achievable accuracy.
- A more precise title clarifying the architectural scope would better match the paper's content.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The network has a trained scaling factor γ and bias α"** — The paper explicitly states in Section 2.1 that "this layer is not essential for achieving UAP, it does simplify the proof and offer practical value," and Theorem 2 removes them entirely. The paper addresses this concern directly.

- **"Initial weights change with n"** — Standard in all UAP constructive proofs (width scales with accuracy). This reflects a misunderstanding of how UAP theorems work, where the network is designed for a given ε.

- **"Pure formatting/style nitpicks" and "typos/spelling/grammar"** — These are parser artifacts, not author errors per the instructions.

- **Strength from Strength Finder about "permutation-active patterns linking to pruning and continual learning"** — This is speculative and qualitative. Dropped as a strength since it does not directly support the core UAP claim.

- **"Missing related works"** — Per instructions, I cannot confirm existence of missing citations.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a small-scale permutation-search-only experiment (n ≤ 20, enumerate random permutations without gradient steps) to directly validate the existential claim of Theorem 1.
2. Include a free-training baseline (unconstrained Adam on the same architecture) for the 1D regression tasks so readers can calibrate the achieved accuracy.
3. Either sharpen the title to reflect the actual architectural scope or add a more explicit caveat in the abstract about the architectural restrictions.
4. For the random initialization bound (Theorem 3), provide at least a heuristic scaling estimate connecting n, ε, and δ, even if not tight.

## Score and Decision

**Calibration Anchors** (all from the provided corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `dpDw5U04SU` (Min width for UAP) | 7.00 | Accepted ICLR paper settling a tight open problem. Technically sharper and more general than the current paper, but addresses a more mature problem. The current paper is more novel (first proof for permutation training) but narrower in applicability. |
| `QjO0fUlVYK` (Star domain) | 6.00 | Accepted. Empirical paper with a theoretical conjecture. Comparable significance but the current paper has stronger theoretical content. |
| `YN4uWzcbtt` (NTK positivity) | 4.25 | Rejected. Incremental improvement to existing results. The current paper is more novel and addresses a problem with no prior theory. |
| `V6JRkfj9dU` (How many samples) | 4.67 | Rejected. Interesting but overclaimed scope. The current paper is cleaner and more honest about its limitations. |
| `G2Lnqs4eMJ` (Optimal NN approx.) | 2.50 | Rejected. Poorly written and incremental. The current paper is substantially stronger in both writing and contribution. |
| `IqaQZ1Jdky` (KANs) | 2.50 | Rejected. Marginal improvements over baselines. The current paper has a fundamentally novel contribution. |
| `tKFZ53nerQ` (Topic/Description Gen.) | 2.00 | Rejected. Unrelated topic, poor quality. Not comparable. |

The paper is a solid theoretical contribution with genuine novelty (first UAP result for permutation training), clever proof techniques, and reasonable experiments. Its limitations — narrow architecture, non-constructive random-initialization bound, and the experiment-theory gap (gradient-guided search vs. existential permutation claim) — prevent it from being a strong accept but do not undermine its core contribution. Relative to the anchors, the paper sits above the rejection-tier papers (2.5–4.67) and near the lower end of the acceptance-tier papers (5.5–7.0).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>