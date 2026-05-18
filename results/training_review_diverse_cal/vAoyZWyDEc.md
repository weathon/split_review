I have verified all the key claims. Now I'll produce the final consolidated review.

---

## Summary

This paper studies the computability of approximating optima of non-convex functions in an oracle setting where function values are obtained via queries at finite-precision points. It claims three main results: (1) that computing an ε-approximation to the global optimum (both value and point) is not computable in this oracle setting, proven via reduction from the undecidable "identically zero" problem; (2) a necessary and sufficient characterization for when global optima can be approximated, based on a computable predicate Q; and (3) an algorithm that converges to the global optimum when a lower bound on the basin of attraction of the global minimizer is known, with convergence analysis and numerical experiments.

## Strengths

- **Algorithmic contribution with practical motivation**: The proposed algorithm interleaves grid search with gradient descent and does not require knowledge of the optimal value (unlike the prior work of D'Helon et al. 2007). When a lower bound on the basin of attraction is available, the grid-search-first-then-gradient-descent strategy is a sensible approach, and the paper makes an explicit attempt at convergence analysis (Theorem 5.3, Theorem 5.4).  
- **Experimental demonstration**: Numerical results on six standard benchmark functions (Ackley, Rastrigin, Rosenbrock, Booth, Beale, Sphere) show that the algorithm empirically converges to the optimum, supporting the practical viability of the approach in settings where basin information is known.  
- **Contextualization of the problem**: The paper correctly distinguishes its oracle setting from the computable-analysis setting of Pour-El & Richards (1989) and from prior optimization-specific computability results (Lee et al. 2023), and it surveys relevant real-world applications (portfolio optimization, neural network training, chemical process optimization) that motivate the problem.

## Weaknesses

### Fatal

- **Theorem 2.6 proof contains a logical error that invalidates the paper's core claim.** The proof attempts a reduction from the problem of finding an ε/2-approximate optimal point to the decision problem of whether a given point is ε-approximate. It states: for any point x_k ∈ C, "we can say it is ε close to optimum if |f(x_k) − f(x′_k)| < ε/2 else it is not." This is incorrect. The condition is sufficient but not necessary: a point x_k can be ε-close to the optimum while differing from x′_k by more than ε/2. For example, let f(x*)=0, f(x′_k)=0.4ε (ε/2-approximate), and f(x_k)=0.9ε. Then |f(x_k)−f(x*)|=0.9ε<ε (so x_k is ε-close), but |f(x_k)−f(x′_k)|=0.5ε≥ε/2, so the proposed procedure would incorrectly reject x_k. The claimed decision procedure does not work, the contradiction with Lemma 2.4 does not follow, and Theorem 2.6 is unproven. Since the paper's primary advertised contribution (contribution #2: "the problem of approximating both the minimal value and the minimizer... are not computable") rests on this theorem, the central claim collapses.

- **Lemma 2.4 is not convincingly established, and its proof is incoherent.** The lemma claims that deciding whether a point x_k is an ε-approximation to the global optimum is undecidable. The proof attempts a reduction from the undecidable "identically zero" problem by constructing f′(x)=max{0, f(x)+ε} and stating that this "is identically zero if and only if the ε-approximation to the global minimal value is zero." The mapping from the decision problem about a specific point x_k to this construction is never explained, and it is unclear what "the ε-approximation to the global minimal value is zero" even means in this context. Even if one suspects the decision problem is undecidable (which may be true in some formalization), the proof as written does not establish it. This further undermines Theorem 2.6, which relies on Lemma 2.4 for its contradiction.

### Major

- **No argument that the algorithm's grid-sampled point lies in the global minimum's basin.** The algorithm samples the grid of spacing m (the presumed basin size) and starts gradient descent from the point with the minimum function value. While the global minimum's basin of size m guarantees at least one grid point falls in that basin, the algorithm does not select it — it selects the grid point with minimum function value. If a deep local minimum exists, the grid point near it may have a lower function value, and gradient descent will converge to that local minimum instead. The convergence analysis (Theorem 5.3, Theorem 5.4) assumes without justification that the chosen grid point is in the global minimum's basin, which is a significant gap in the algorithm's validity.

- **Theorem 3.4 (the "necessary and sufficient condition") is too vague to constitute a useful contribution.** The condition requires existence of a computable predicate Q such that P^f ⊂ Q (i.e., Q(ζ,x,y) = [f(x) ≤ f(y)] for all x,y). This is essentially a restatement of the problem rather than a useful characterization: saying "the global optimum is approximable if there exists a computable predicate equivalent to comparing function values" does not provide constructive guidance. The proof relies on undefined concepts ("inverse of a surjective recursive function is recursive" without specifying the function) and does not establish a clear connection to the oracle model. Lipschitz continuity is offered as an example (Remark 3.5), but this is already a well-known sufficient condition, and the theorem adds no new insight beyond what is known from standard Lipschitz-based global optimization theory.

### Minor

- **Lemma 5.2's proof is incomplete.** The lemma attempts to show that iterates remain in a ball around the global minimum asymptotically. The proof shows that function values in the ball are lower than at any non-global local minimum, and that gradient descent decreases the function value. From this, it concludes iterates "can not move to another hypercube around some local minima." However, the proof does not rule out the iterates leaving the ball through non-minimum regions where the function might have lower values. Gradient descent dynamics can traverse points that are not local minima, and the proof provides no bounds on function values outside the ball to prevent such escape. The conclusion does not follow from the premises given.

- **The formal definition of "basin of attraction" (Section 4) is insufficient.** The paper defines it as the condition that ∇f(x)≠0 for all x≠x* in the basin region. This condition (non-zero gradient) does not guarantee that gradient descent initialized in the region converges to x* — it only guarantees the absence of other stationary points. Standard convergence results require additional structure (e.g., the Polyak–Łojasiewicz condition, strong convexity, or that the gradient points toward x*). While Assumption 5.1 (Lipschitz gradient) and the step-size condition provide some descent properties, the paper never establishes that these conditions together ensure convergence to x* specifically rather than to any stationary point.

- **Remark 2.8 (higher-order oracles preserved undecidability) is asserted without argument.** The remark claims that "the reduction from the problem of deciding if f is identically zero remains" for derivative oracles, but offers no justification. Given that derivative information provides strictly more information about the function, it is not obvious that the reduction is unaffected, and the paper should at minimum sketch why the argument carries through.

- **Lemma 2.3 (undecidability of identically zero) is only sketched.** The core idea — a Turing machine only sees finitely many points and an adversarial oracle can disagree elsewhere — is standard and "essentially correct" as the critic acknowledges, but the proof is too brief to be rigorous. In a paper whose central contribution is a non-computability result, this foundational lemma should be argued more carefully.

### Trivial

- The proof of Lemma 2.1 states |x_n*−x*| < ε but the conclusion needed is about function values, not distances. The continuity argument would require linking the precision gap ε/10 to a δ in continuity first, then to function values. As written, it conflates distance in domain with distance in range.
- Several mathematical typos and notation inconsistencies are present (e.g., "M−k" in the denominator of Theorem 5.4 should likely be "k−M"; misplaced subscript/superscript formatting throughout).

## Nice-to-Haves

- A comparison with the multi-start global optimization literature would help contextualize the algorithm's novelty relative to standard practices.
- Formalizing the oracle model in the language of computable analysis (e.g., the BSS model or Type-2 Theory of Effectivity) would strengthen the theoretical claims significantly.

## Removed Points

These points were flagged but removed upon verification:

- **Criticism about fairness of comparison with existing methods**: Not applicable — the paper provides no formal comparison with other methods beyond citing D'Helon et al. (2007), and no unfair comparison was claimed.
- **Strength Finder's claim that Theorem 2.6 "is a clear advance over prior results"**: This is removed because the proof of Theorem 2.6 is flawed; the paper does not actually establish this claimed result.
- **Strength Finder's claim about "necessary and sufficient condition" being "clean"**: Removed because, upon verification, Theorem 3.4 is too vaguely stated and the proof is insufficiently rigorous to count as a genuine strength.
- **Generic strength about "addressing an important problem"**: Removed per instructions (generic, lacks specific content).

## Novel Insights

None beyond the paper's own contributions. The algorithmic idea of interleaving grid search with gradient descent by spacing the grid according to a known basin size is sensible but closely related to prior work (D'Helon et al. 2007), and the theoretical impossibility claim — which would have been the novel insight — is not correctly proven.

## Suggestions

1. **Fix the core impossibility proof or remove the claim.** The proof of Theorem 2.6 needs a fundamentally different reduction. The current attempt fails because the "else it is not" direction of the decision procedure is unjustified. If a correct impossibility result can be established, it could salvage the paper's main contribution. If not, the paper should honestly acknowledge this and restructure itself around the algorithm and characterization alone, which would require significantly strengthening those parts.

2. **Provide a rigorous proof that the algorithm's grid-selected point lies in the global minimum's basin**, or modify the algorithm to guarantee this (e.g., by starting gradient descent from every grid point and keeping the best result — but this must be analyzed for correctness).

3. **Strengthen the algorithm's convergence analysis** by properly establishing that gradient descent iterates stay within the global minimum's basin, using standard Lyapunov or descent arguments that bound function values everywhere, not just at local minima.

4. **Clarify the formal model.** The mixing of Turing machine definitions, finite-precision representations, and oracle queries needs to be specified precisely. Readers familiar with computable analysis will find the current description ambiguous.

## Score and Decision

The paper's primary advertised contribution (a non-computability result for approximating global optima) is not correctly proven — Theorem 2.6 contains a clear logical error that invalidates the reduction. Lemma 2.4, on which the theorem depends, is also not convincingly established. The remaining contributions (the algorithm and its analysis) have independent merit but are significantly weakened by gaps in the convergence analysis and the absence of a guarantee that the grid-sampled point lies in the global minimum's basin. The characterization in Theorem 3.4 is too vague to constitute a useful contribution. Overall, the paper does not deliver on its core claims, and the remaining content does not compensate for this.  

**Recommendation: Reject.**

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>