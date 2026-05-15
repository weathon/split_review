Now I have a thorough understanding. Let me write the final review.

## Summary

This paper studies the computability of approximating global optima of non-convex continuous functions in an oracle setting. It claims that ε-approximations to the global optimum (both value and point) are not computable with only oracle access (Theorem 2.6), gives a necessary and sufficient condition for approximability via a predicate framework (Section 3), presents an algorithm that converges when the basin of attraction of the global minimizer is known (Sections 4–5), and provides numerical experiments on benchmark functions (Section 6).

## Strengths

- **Clear differentiation from existing computability frameworks.** The paper correctly identifies that its oracle setting (where f is only known through finite-precision queries) is distinct from the computable-analysis setting of Pour-El & Richards (1989) and from the oracle model of Lee et al. (2023). It argues (correctly, in spirit) that its negative result would be stronger than those previously established. The distinction is meaningful and worth exploring.

- **Concrete algorithmic proposal.** The idea of combining grid search (with spacing determined by a known lower bound on the basin of attraction) with gradient descent is a reasonable instantiation of the paper's broader claim that additional global structural information enables approximability. The algorithm is simple and the intent is clear, even if the analysis has gaps.

## Weaknesses

### Fatal

- **The proof of the main negative result (Theorem 2.6) is not rigorous and the central claim is unsubstantiated.** Lemma 2.4 attempts to reduce the undecidable problem of deciding whether a continuous function is identically zero to the problem of deciding whether a point is an ε-approximation to the global optimum. The reduction is not properly established. The construction `f'(x) = max{0, f(x)+ε}` and the claim that this function "is identically zero if and only if the ε-approximation to the global minimal value is zero" is confusing and does not clearly connect to the decision problem. The paper never defines what "the ε-approximation to the global minimal value is zero" means in a way that enables the claimed reduction. Without a valid Lemma 2.4, Theorem 2.6 is unsupported. Since the paper's primary claimed contribution is this impossibility result, this is a fatal flaw.

### Major

- **Section 3 (global optima property) is essentially vacuous.** Theorem 3.4 states that the global optimum is approximable iff there exists a computable predicate Q such that P^f ⊂ Q, where P^f is the ordering predicate of f. This restates the definition of computability of the optimum in a disguised form — it does not provide a useful characterization. The "if" direction's proof invokes "the inverse of a surjective recursive function is recursive" without establishing any surjective function or connecting to the oracle setting. The "only if" direction constructs Q in terms of ||x*|| but Q still requires oracle access to f, so calling it "computable" is misleading. The subsequent claim that Lipschitz continuity is an example is also problematic: knowing an upper bound on the Lipschitz constant does not make the ordering predicate P^f computable — it enables a specific grid-search algorithm, which is a different statement.

- **Convergence proof contains a sign error and an incomplete argument.** In Theorem 5.4, the final inequality states:
  `f(x_k) - f(x*) ≤ ||x_M - x*||² / (2t(M-k))`
  For k > M, the denominator (M-k) is negative, making the RHS negative, while the LHS is non-negative (since x* is the global minimizer). The intended bound clearly should have (k-M) or (k-M+1) in the denominator. Additionally, the bound uses 1/k instead of 1/(k-M+1) when averaging from i=M to k. These are not minor typos — they appear in the stated theorem and its proof.

- **Lemma 5.2 does not establish convergence from arbitrary initialization.** The lemma proves that if iterates are inside B(x*,R), they stay there asymptotically. It does **not** prove that the algorithm's grid search will ever place an iterate inside this ball. The convergence theorem (Theorem 5.3) assumes the lemma guarantees eventual entry, creating a logical gap. The combination of grid search and gradient descent is not analyzed to show the grid will eventually find the basin.

- **Algorithm description is too vague to be reproducible.** The paper states: "The algorithm finds the point z_k where the function takes a minimum amongst all points at a distance of m from each other and does a gradient descent step from the point z_k." It does not specify how the grid is constructed, how it is maintained across iterations, how the grid search and gradient descent steps are interleaved, or how z_k is selected. This is insufficient for reproducibility.

- **Experiments do not support the paper's theoretical claims.** The experiments test benchmark functions with known global optima and known basin sizes. They never test the critical scenario where m (the basin lower bound) is unknown — which is precisely the setting of the paper's negative result. There are no comparisons to baselines (e.g., random search, multi-start gradient descent), no ablation of the m parameter, and no analysis of failure cases. The experiments merely show that gradient descent with basin-aware initialization works, which is a known fact.

### Minor

- **The oracle model is incompletely specified.** The paper says the oracle gives f(x) "up to any finite-precision" but does not specify the error model (absolute vs. relative error; whether the oracle can be adversarial within the precision). For a formal computability argument, this matters. The proof of Lemma 2.3 (undecidability of checking if a function is identically zero) is an informal sketch that would benefit from a cleaner connection to a standard undecidable problem.

- **Proof of Lemma 2.1 is sloppy.** The lemma (which is mathematically correct due to uniform continuity on a compact domain) has a proof that conflates the gap between finite-precision numbers with the continuity modulus. It states |x*_n - x*| < ε when it should establish |x*_n - x*| < δ for the continuity modulus δ. This does not make the lemma false, but the proof is imprecise.

- **Theorem 5.4 assumes convexity in B(x*,r) without justification.** This assumption is stated explicitly, but the paper never justifies why it should hold for the general non-convex functions the paper claims to address. It significantly weakens the contribution of the convergence rate result.

## Nice-to-Haves

- A comparison of the proposed algorithm against simple baselines (e.g., random grid search followed by gradient descent) would help contextualize its performance.
- An experiment that demonstrates failure when m is mis-specified or unknown would validate the necessity claimed by the theory.
- Clarifying the error model of the oracle (deterministic truncation vs. adversarial within precision) would strengthen the formal computability framework.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Lemma 2.1 is false."** — This is incorrect. Continuity on a compact domain implies uniform continuity, so the claim holds. The proof is sloppy but the lemma is valid. (Harsh critic error.)

2. **"The paper conflates NP-hard with not computable."** — The paper explicitly says: "We show more in this paper, that this set S is not computable. This is much stronger than saying it is intractable." This correctly distinguishes the two concepts. (Harsh critic error.)

3. **"The paper's claim about justifying NNs is a non-sequitur."** — The paper discusses supervised learning as a real-world motivation. Whether the justification is convincing is a matter of opinion, not a technical flaw in the paper's core claims.

4. **"Missing figures and image links are broken."** — These are parser extraction artifacts, not errors in the original submission.

5. **"The formalization of Turing machines is irrelevant."** — Many computability papers provide Turing machine formalization as background; this is not a weakness.

6. **"Lemma 2.1 proof conflates function values and inputs."** — As noted above, the lemma is correct and the proof, while sloppy, uses continuity in the standard way. The criticism is overstated.

## Novel Insights

None beyond the paper's own contributions. The predicate framework in Section 3 is a restatement rather than a genuine characterization, and the proof of the central impossibility result is too flawed to support the claimed insight. The algorithmic idea (basin-aware grid + gradient descent) is reasonable but not novel in the optimization literature.

## Suggestions

1. **Fix the proof of Lemma 2.4 / Theorem 2.6.** If the impossibility result is the main contribution, provide a proper reduction from a known undecidable problem (e.g., the halting problem via a function that encodes Turing machine states) with a clearly specified oracle model. The current "reduction" is insufficient.
2. **Either remove Section 3 or substantially rework it** to provide a non-trivial characterization. As it stands, it is a near-tautology that adds no insight.
3. **Correct the sign error in Theorem 5.4** and provide a proper convergence proof that addresses how the grid search and gradient descent interact to enter the basin of attraction.
4. **Provide a precise algorithmic description** with pseudocode, specifying how the grid is constructed, maintained, and searched.
5. **Expand the experiments** to include: (a) the case where m is unknown or mis-specified, (b) baseline comparisons, and (c) an ablation study showing the necessity of the basin-size knowledge.

## Score and Decision

The paper has a fatal flaw: the central impossibility result (Theorem 2.6), which is its primary claimed contribution, is not validly proven. The reduction in Lemma 2.4 is not properly established, and the oracle model lacks the precision needed for a formal computability argument. Additional major issues include a vacuous characterization in Section 3, a sign error in the convergence proof, an algorithm too vaguely described to reproduce, and experiments that do not test the paper's own claims. While the paper identifies a meaningful research direction, the execution is insufficient to support its conclusions.

MY FINAL SCORE: <pineapple>2.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>