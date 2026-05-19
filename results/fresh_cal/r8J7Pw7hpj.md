I have all the information I need. Let me now write the final consolidated review.

---

## Summary

This paper introduces IPRO (Iterated Pareto Referent Optimisation), a decomposition-based multi-objective reinforcement learning algorithm that learns a Pareto front by iteratively querying a Pareto oracle with reference points and using each returned policy to shrink the remaining search space. The core theoretical contribution is a set of convergence guarantees: Theorem 4.1 provides an upper bound on the approximation error to the true Pareto front at each iteration, Theorem 4.2 guarantees convergence to a τ-Pareto front, and Corollary 4.2.1 ensures finite termination. The paper also presents practical oracle designs based on DQN, A2C, and PPO, and a specialized bi-objective variant IPRO-2D. Experiments on Deep Sea Treasure (2 objectives), Minecart (3 objectives), and MO-Reacher (4 objectives) demonstrate that IPRO can approximate the true Pareto front when known and is competitive with prior methods.

## Strengths

- **Provable convergence with an online error bound.** Theorem 4.1 gives an upper bound on the approximation error at every iteration, Theorem 4.2 proves convergence to a τ-Pareto front, and Corollary 4.2.1 guarantees finite termination for any positive tolerance. These results go beyond prior decomposition-based MORL methods (e.g., Van Moffaert et al., 2013), which lacked theoretical guarantees. The claim to being "the first algorithm" with this combination of guarantees is significant and well-supported by the theoretical development.

- **Handles non-convex Pareto fronts where convex-hull methods fail.** On Deep Sea Treasure, the true Pareto front contains concave regions that are unreachable by linear scalarisation. IPRO-2D with all three oracle implementations closely approximates the true hypervolume (Fig. 3a, 3d), whereas convex-hull algorithms such as GPI‑LS cannot recover all Pareto-optimal solutions. This directly demonstrates the advantage of the decomposition approach over convex-hull methods for deterministic policies.

- **Rigorous formalisation of Pareto oracles and their connection to ASFs.** Definitions 3.1 (weak Pareto oracle) and 3.2 (approximate Pareto oracle), together with Theorems 3.1 and 3.2, provide a clean theoretical framework linking Pareto oracles to order-representing and order-approximating achievement scalarising functions. This formalisation is principled and gives the algorithm a solid foundation.

- **Practical oracle designs from standard single-objective RL algorithms.** Section 3.2.1 provides concrete modifications of DQN, A2C, and PPO to serve as Pareto oracles by optimising the augmented Chebyshev scalarisation. The fact that all three yield competitive results on benchmarks with 2–4 objectives (Fig. 3) demonstrates that the framework can leverage established RL methods.

- **Specialised bi-objective variant IPRO-2D.** Section 4.3 introduces a simplified version for d=2 that represents the search space as isolated rectangles and uses a priority queue. This directly contributes to the strong performance on Deep Sea Treasure and is a thoughtful engineering contribution.

## Weaknesses

### Fatal
None.

### Major

- **Coverage decrease contradicts the claimed monotonicity with no explanation.** The paper states "In theory, the sequence of coverages is monotonically increasing" yet acknowledges that Fig. 3e shows coverage decreasing in certain iterations (Minecart). The paper flags this discrepancy but provides no analysis of why it occurs — whether it is due to a suboptimal oracle return, a violation of the bounding-box reduction, a computational artifact, or a genuine gap between the theoretical model and the practical implementation. Since coverage monotonicity is presented as a core property ("systematic reduction of the search space" per Section 4), this unexplained contradiction weakens the empirical support for the method's internal logic and should be resolved.

### Minor

- **Gap between oracle definitions used in theory and the practical instantiation.** The theoretical guarantees (Theorems 4.1, 4.2, Corollary 4.2.1) assume a Pareto oracle that satisfies precise definitions (weak or approximate, boundary-free). In practice, the oracle is implemented by optimising the augmented Chebyshev scalarisation via DQN/A2C/PPO with ρ > 0 (making it order-approximating rather than order-representing) and without the ε-shift required by Theorem 3.2 for the approximate variant. The paper acknowledges this gap (Section 3.2: "One potential drawback… A more practical alternative…") but does not analyze how the guarantees degrade under the heuristic oracle. The experiments thus operate as a heuristic approximation of the ideal algorithm, and the paper would benefit from a discussion of when the guarantees might be violated in practice.

- **Non-differentiability of the Chebyshev scalarisation for policy gradient methods.** The policy gradient derivation in Section 3.2.1 assumes a differentiable scalarisation function f (line 119: "For differentiable f"). However, the augmented Chebyshev function (Eq. 1) contains a min operator, making it non-differentiable at points where the minimum switches between objectives. The paper does not discuss how this is handled in practice — whether subgradients, smooth approximations, or empirical gradient estimates are used. This is a non-trivial implementation detail affecting both correctness and reproducibility.

- **IPRO-2D weighting modification lacks theoretical justification.** Section 4.3 states that "we normalise the ASF according to the distance between the lower and upper points that make up the isolated rectangle" rather than the standard weighting based on the ideal point. This is a heuristic change, and the paper does not discuss whether the theoretical guarantees (Theorems 4.1, 4.2) still hold under this modified weighting. Given the paper's emphasis on theory, this is a notable gap.

- **Limited evaluation scope.** Only three environments are tested, all of relatively modest scale (DST is small and deterministic; Minecart and MO-Reacher have continuous state spaces but simple dynamics). The paper does not evaluate on higher-dimensional or more challenging stochastic-control benchmarks. While this does not invalidate the results, it limits the generalisability claims that can be drawn from the empirical evaluation.

### Trivial
None.

## Nice-to-Haves

- An ablation study of the key knobs: the augmentation parameter ρ, the tolerance τ, and the oracle variant (DQN vs. A2C vs. PPO) would strengthen practical guidance.
- A controlled experiment on DST that uses known ground truth to measure how much the practical oracle heuristics degrade the theoretical bound (Theorem 4.1) would directly test the theory-practice gap.
- A brief characterisation of computational complexity (oracle calls, set-update cost, especially for d>2) would help readers assess scalability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Selective seeding ("five best seeds") on Minecart (and incorrectly claimed for MO-Reacher):** The paper uses the five best seeds for baselines PCN and GPI-LS on Minecart while averaging IPRO over all five seeds. The harsh critic's concern is that this inflates the baselines' apparent performance. Per the hard rule, asymmetry that *favors the baseline* (makes the author's method look relatively worse) is intentionally conservative and not a valid criticism. IPRO still achieves higher hypervolume than PCN under this asymmetry. Additionally, the harsh critic incorrectly extends this criticism to MO-Reacher, where the paper does not mention selective seeding.
- **Missing code or appendix:** The parser strips supplementary material; these exist in the original submission.
- **Critique that the bound is not empirically verified on realistic problems:** The bound is a theoretical statement (Theorem 4.1); the experiments serve a complementary purpose. The paper does not claim empirical verification of the bound's tightness on complex problems.
- **Critique that the paper should evaluate on MO-HalfCheetah, MO-Ant, etc.:** This is scope creep. The paper evaluates on three standard MORL benchmarks, which is a standard evaluation footprint for the field.

## Novel Insights

None beyond the paper's own contributions. The main novel insight—that iteratively querying a Pareto oracle with Chebyshev scalarised problems yields provable convergence with an online error bound—is the paper's own contribution, not something surfaced by the reviews. The reviews did identify the theory-practice gap in oracle implementation and the unexplained coverage decrease as issues that, if addressed, would strengthen the paper, but these are concerns about the paper's completeness rather than novel observations about the method.

## Suggestions

1. **Address the coverage decrease directly.** Either explain why coverage can decrease in practice despite the theoretical monotonicity claim (e.g., due to oracle suboptimality) and adjust the theory to allow non-monotonic coverage, or fix the computation/implementation and re-run experiments. A satisfactory explanation is necessary for the paper's internal claims to be coherent.

2. **Explicitly state how the non-differentiability of the Chebyshev min is handled in practice** in the policy gradient oracles (subgradient, smooth surrogate, or empirical gradient). This is important for reproducibility.

3. **Discuss the theory-practice oracle gap more thoroughly.** The paper already acknowledges the gap in Section 3.2. Adding a paragraph that identifies conditions under which the practical oracle approximately satisfies the theoretical definitions (e.g., small ρ, near-optimal RL optimisation) would strengthen the connection between theory and experiments.

4. **Clarify whether the IPRO-2D weighting modification preserves the theoretical guarantees,** or explicitly treat it as a heuristic with an empirical justification.

## Score and Decision

This paper makes a genuine theoretical contribution: the first MORL algorithm to offer an upper bound on approximation error at each iteration alongside convergence and finite-termination guarantees. The oracle framework and the IPRO-2D variant are well-designed. The empirical evaluation, while showing competitive results, has several gaps that prevent full validation of the theoretical claims in practice — in particular, the unexplained coverage decrease and the unanalyzed gap between the theoretical oracle model and the practical implementation. These are addressable in revision and do not undermine the paper's core theoretical contribution.

**Score:** 7.0 — A solid paper with a strong theoretical contribution; the empirical evaluation needs strengthening but the core ideas are sound and important.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>