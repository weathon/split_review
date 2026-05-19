- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 5, 5, 3, 3
Now I have a thorough understanding of the paper and can cross-check all reviewer claims.

## Summary

The paper introduces the relative-translation invariant Wasserstein distances ($RW_p$), a family of metrics on the quotient space $\mathcal{P}_p(\mathbb{R}^n)/\!\sim$ under translation equivalence. For the quadratic case ($p=2$), it derives three properties — decomposability of the ROT optimization, translation-invariance of coupling solutions, and a Pythagorean relationship $W_2^2 = \|\bar{\mu}-\bar{\nu}\|_2^2 + RW_2^2$ — and leverages them to propose an $RW_2$ Sinkhorn algorithm that centers the source distribution before running standard Sinkhorn. The paper provides numerical stability and complexity analyses and validates the method on synthetic data, MNIST digit recognition under random translations, and a large-scale thunderstorm pattern detection task (205,848 radar images).

## Strengths

1. **Decomposability theorem (Theorem 2, Sec. 3.2).** The paper proves that the quadratic ROT problem separates into an independent classical OT problem (determining the coupling $P$) and a simple quadratic minimization in $s$ (yielding $s = \bar{\nu} - \bar{\mu}$). This decomposition is correctly derived and is the theoretical linchpin that enables the efficient algorithm.

2. **Pythagorean relationship (Corollary 2, Sec. 3.2).** The identity $W_2^2(\mu,\nu) = \|\bar{\mu}-\bar{\nu}\|_2^2 + RW_2^2(\mu,\nu)$ provides a clean interpretation of distribution shift as a sum of "bias" (mean difference) and "shape" ($RW_2$) terms. This is a principled decomposition that the paper puts to concrete use.

3. **Existence guarantee (Theorem 1, Sec. 3.1).** The proof that the outer minimization over $s$ can be restricted to a compact set $\{\|s\|_p \le 2\max_{ij}\|x_i-y_j\|_p\}$, ensuring a minimizer exists, grounds the ROT formulation rigorously and distinguishes it from a heuristic search.

4. **Numerical validation (Experiment 1, Sec. 5.1).** Controlled experiments on Gaussian and uniform distributions in $\mathbb{R}$ and $\mathbb{R}^{10}$ cleanly demonstrate that as translation grows, the $RW_2$ Sinkhorn algorithm yields lower error and faster runtime compared to standard Sinkhorn. The results confirm the complexity/stability analysis and show the method's practical benefit.

5. **Digit recognition under random translations (Experiment 2, Sec. 5.2).** On MNIST images embedded in larger grids with varying translation magnitudes (0–28 pixels), $RW_2$ achieves significantly higher nearest-neighbor classification accuracy than $L_1$, $L_2$, $W_1$, and $W_2$ as translation increases. The experiment uses two sample sizes ($N=100, 1000$) with 10 repeats and reports mean/std, establishing robustness empirically.

## Weaknesses

### Fatal
None.

### Major

1. **The thunderstorm pattern detection experiment (Sec. 5.3) is purely qualitative.** The paper shows two figures comparing retrieved snapshots/sequences using $RW_2$ vs. $W_2$, but provides no quantitative evaluation — no retrieval precision/recall, no mean average precision, no user study, no objective shape-similarity metric. The claim that "$RW_2$ focuses more on shape similarity while $W_2$ pays more attention to location similarity" is an expected consequence of the definitions, not an empirical finding. Given that the weather application is presented as the primary motivation (Introduction, first paragraph), the absence of quantitative evidence is a significant gap that weakens the paper's overall empirical support.

2. **Scope gap: the title and abstract claim a family $RW_p$, but the entire algorithmic and experimental contribution is limited to $p=2$.** The paper correctly defines $RW_p$ for general $p \ge 1$ and proves $RW_p$ is a metric on the quotient set. However, for $p \neq 2$ the ROT problem does not decompose as it does for $p=2$, and solving it would require a joint optimization over $s$ and $P$ that could be non-convex and computationally expensive. The paper does not discuss this difficulty, acknowledge that $p \neq 2$ is an open problem, or even state this limitation explicitly. A reader could reasonably assume the algorithm generalizes.

### Minor

3. **Experiment 2 (digit recognition) would be strengthened by an explicit centered-$W_2$ baseline.** Since $RW_2$ is mathematically equivalent to $W_2$ applied to centered distributions, a direct comparison against $W_2$ on pre-centered images would validate the theory and show that the benefit of $RW_2$ comes from its translation invariance, not from some other algorithmic artifact. The absence of this baseline does not invalidate the results, but it is a missed opportunity to make the experiment more informative.

4. **The numerical stability analysis (Sec. 4.3) uses the product of all entries of $K$ ($g(K)$) as a stability criterion, which is a heuristic.** The paper shows that centering maximizes $g(K)$ and argues this improves stability by pushing entries away from zero. While the intuition is reasonable, the actual numerical stability of Sinkhorn depends on the range of the entries and their interaction with the iterative scaling, not just the product. The analysis would be stronger with a direct validation of stability (e.g., condition numbers of the iteration matrices or convergence rates under varying translations).

5. **The RW$_2$ Sinkhorn algorithm (Algorithm 1) is centering + standard Sinkhorn.** The algorithm computes $s = \bar{\nu} - \bar{\mu}$, translates the source points, and runs standard Sinkhorn on the shifted cost matrix. This is a straightforward application of the decomposition theorem rather than a novel algorithmic technique. The contribution lies in recognizing and formalizing this reduction, which is valuable, but the paper should be clearer about this framing to avoid overclaiming algorithmic novelty.

### Trivial
None.

## Nice-to-Haves

- Adding a quantitative retrieval evaluation for the thunderstorm experiment (e.g., precision@k against human-annotated shape similarity, or using known temporal proximity as pseudo-ground-truth).
- A brief discussion of the challenges for $p \neq 2$ (non-convexity, potential approaches) to clarify the scope.
- An explicit experiment showing $RW_2 \equiv W_2$ on pre-centered data to validate the theory.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Novelty is significantly overstated; core ideas are elementary and well-known."** This criticism asserts that the Pythagorean decomposition is "routinely used in the OT literature" and that the paper presents it as a new discovery. The paper claims "we introduce a new family of distances" ($RW_p$) and "identify three useful properties of $RW_2$." The reviewer provides no citations to support the claim that this specific decomposition for general discrete distributions is well-known. Per the meta-review rules, I cannot verify the existence of this alleged prior art, and I should not penalize the paper for missing related works that may not exist. The decomposition is correctly derived and forms part of a coherent framework.

2. **"Motivation disconnected from evaluation."** The reviewer argues the paper does not show $RW_2$ improves downstream task performance (e.g., forecast accuracy). The paper's scope is to propose a distance metric and validate that it behaves as claimed (shape-focused retrieval). Requiring downstream weather prediction benchmarks is scope creep and goes beyond what the paper sets out to do.

3. **Strength: "Thunderstorm pattern detection experiment (Figures 6 and 7)."** This strength conflicts with the verified weakness that the experiment is purely qualitative. Following the rule that "when a strength and weakness disagree, the weakness wins," this claimed strength is removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add quantitative evaluation to Experiment 3.** For the thunderstorm retrieval task, compute precision@k, mean average precision, or a similar metric against a reasonable ground truth (e.g., human annotation of shape similarity, or temporal proximity under the assumption that consecutive storm images share similar shapes). Without numbers, the sole experiment tied to the paper's motivating application remains anecdotal.

2. **Acknowledge the $p \neq 2$ limitation explicitly.** Either narrow the paper's scope in the title/abstract to $RW_2$, or add a paragraph discussing why $p \neq 2$ is more challenging and what approaches might be explored (even if not solved). This would set honest expectations.

3. **Reframe the algorithm contribution.** Present Algorithm 1 as "a practical application of the decomposition theorem that enables efficient computation of $RW_2$ via standard OT solvers" rather than as a novel algorithmic variant. This accuracy would strengthen credibility.

4. **Add an explicit centered-$W_2$ baseline to Experiment 2.** Show that $RW_2$ and $W_2$ on centered images produce identical or near-identical classification accuracy, confirming the theoretical equivalence.

5. **Strengthen the numerical stability analysis.** Supplement the $g(K)$ heuristic with empirical validation (e.g., show condition numbers, convergence trajectories, or entropy values of the scaling vectors) to directly support the stability claim.
