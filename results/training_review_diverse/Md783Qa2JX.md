Now I have a thorough understanding of the paper, the reviews, and the relevant rules. Let me compose the final consolidated review.

---

## Summary

This paper studies the problem of computing a regularizer for Follow-the-Regularized-Leader (FTRL) that is guaranteed to achieve regret within a universal constant factor of the minimax optimal rate $\Rate(\mathcal{X},\mathcal{L})\sqrt{T}$ for any symmetric convex action set $\mathcal{X}$ and loss set $\mathcal{L}$. The authors present an algorithm that, given oracle access to these sets, runs in $\exp(O(d^2))$ time and outputs such a regularizer. The approach involves (1) proving the existence of a *smooth* near-optimal regularizer (via Gaussian smoothing of the non-constructive regularizer from Srebro et al. 2011), (2) approximating it by a piecewise "quasi-quadratic" function defined on a finite discretization, (3) encoding the search for a good regularizer as a finite-dimensional convex program, and (4) solving it via cutting-plane methods with a separation oracle for strong convexity constraints. The paper also provides a query-complexity lower bound showing that checking strong convexity is exponentially hard.

## Strengths

1. **Removes the $\log T$ factor from the Srebro et al. (2011) universality result.** Theorem~3.1 (highlevelrate) proves that for any symmetric convex $\mathcal{X}, \mathcal{L}$, there exists an FTRL regularizer achieving regret $O(\Rate(\mathcal{X},\mathcal{L})\sqrt{T})$, improving on the earlier $O(\Rate(\mathcal{X},\mathcal{L})\log T \sqrt{T})$ bound. This is a clean theoretical improvement and forms the foundation for the algorithmic results.

2. **First algorithm to compute a near-optimal regularizer for arbitrary symmetric OLO instances.** Theorem~1 (maincomputebarrier) provides an explicit algorithm that, given oracle access to $\mathcal{X}$ and $\mathcal{L}$, outputs a regularizer $g$ for which FTRL achieves $O(\Rate(\mathcal{X},\mathcal{L})\sqrt{T})$ regret. The algorithm runs in $(dR/r)^{O(d^2)}$ oracle time, which is fully polynomial for constant dimension. Prior work (Srebro et al.) only gave non-constructive existence guarantees.

3. **Novel convex programming formulation for regularizer optimization.** Section~6 constructs a finite-dimensional convex program whose variables are the values, gradients, and Hessians of quasi-quadratic functions at a discretization set. The program enforces strong convexity via constraints $v^\top\Sigma_{x_i}v \geq \alpha$ for all $v\in\mathcal{L}$ and locality via inequality (eq:localitycondition). Theorem~6.3 (lem:lptobarrier) shows that any feasible solution yields an optimal regularizer and that the feasible region contains a Euclidean ball around the (discretization of the) smooth optimal regularizer — essential for cutting-plane methods.

4. **Locality analysis bridging finite-dimensional optimization and infinite-dimensional strong convexity.** Lemmas~6.1 (feasibilitytolocality) and~6.2 (sconvexity) show that feasible solutions to the convex program produce regularizers that are $\alpha/2$-strongly convex with respect to $\|\cdot\|_\mathcal{L}$ on the entire domain $\mathcal{X}$, not just at discretization points.

5. **Lower bound on query complexity.** Theorem~7.1 (lowerbound) proves that even checking whether the identity Hessian is $\alpha$-strongly-convex with respect to $\|\cdot\|_{\mathcal{L}}$ requires exponentially many membership queries to $\mathcal{L}$, providing some justification for the exponential-in-$d$ complexity of the algorithm.

## Weaknesses

### Fatal

None. The paper's core direction is well-motivated and the high-level approach is plausible.

### Major

1. **Abstract claims NP-hardness, but the only stated lower bound theorem is about membership-query complexity.** The abstract states: "even deciding whether a given regularizer is $\alpha$-strongly-convex with respect to a given norm is NP-hard." However, the sole lower bound in the paper body (Theorem~6.1 / thm:lowerbound) is about *membership-query complexity* — it proves an exponential query lower bound for distinguishing a convex body from the Euclidean ball under a specific distribution. Query-complexity lower bounds do **not** imply NP-hardness; they are different complexity notions. If an NP-hardness proof exists in the appendix, the main text does not state it as a theorem. This mismatch is misleading about the nature of the hardness result and must be corrected.

2. **The convex program requires constants $(L, c_0, c_2, \uppertwo)$ that depend on the smooth regularizer's properties, but no method is given to compute these from the input sets alone.** The constants are derived from the smooth barrier function $f_{\text{smooth}}$ whose existence is asserted (e.g., $L = \Rate(\mathcal{X},\mathcal{L})^2 \cdot d^{3/4}/r^3$, $c_0$ from the gradient bound, etc.). However, $\Rate(\mathcal{X},\mathcal{L})$ is defined as $\inf_{\text{alg}} \Rate(\text{alg})$ — it is not directly computable from $(\mathcal{X},\mathcal{L}, r, R, d)$. Theorem~6.3 (lem:lptobarrier) says "assume we are given a smooth barrier function $f$" and sets constants in terms of $f$'s properties, but the algorithm does **not** know $f$ a priori. Without explaining how to bound these constants (or $\Rate$) from the geometric parameters $(r,R,d)$ alone — or how to set them without knowledge of the unknown optimal regularizer — the convex program is not actually constructible from the input. This is a significant gap in the algorithm's specification.

### Minor

3. **The lower bound (Section~7) uses membership queries, but the algorithm assumes a linear optimization oracle for $\mathcal{L}$.** The paper describes the lower bound as showing the exponential running time is "in some sense necessary," yet the bound is proven for a *membership oracle* model, while the main algorithm uses a *linear optimization oracle* for $\mathcal{L}$ (plus a membership oracle for $\mathcal{X}$). The paper does not explicitly argue that the lower bound transfers to the linear-optimization oracle model, which is a different (and potentially stronger) oracle. This weakens the "necessity" claim, though it does not invalidate the algorithmic construction itself.

4. **The paper contains editorial artifacts (e.g., `\sj{...}` comments, unfinished parentheticals) indicating a draft-level polish.** While these do not affect technical correctness, they suggest the presentation is not in final form.

### Trivial

None.

## Nice-to-Haves

- Provide explicit worst-case bounds on $\Rate(\mathcal{X},\mathcal{L})$ in terms of $r,R,d$ so that the constants $L, c_0, c_2, \uppertwo$ can be computed purely from the input.
- Explicitly reconcile the abstract's "NP-hardness" claim with the actual query-complexity lower bound theorem.
- Include a brief discussion of whether (and how) the membership-query lower bound implies hardness for the linear-optimization oracle model used by the algorithm.

## Removed Points

The following points from the Harsh Critic are removed with justification:

- **Separation oracle description is incomplete (Critic's point #2):** The critic notes the separation oracle for the strong-convexity constraint is described only at a high level, and details about the $\epsilon$-net, Lipschitz constants, and net size are missing. **Removed because** these details belong to the appendix (Section~sec:separationoracle), which was stripped by the parser. The rule to remove weaknesses about missing appendix content applies.

- **Smoothing argument unsubstantiated (Critic's point #4):** The critic says the derivative bounds and regret-preservation of Gaussian smoothing lack derivation. **Removed because** the proofs are in the appendix (referenced via Theorem~thm:smoothbarrier). The rule to remove weaknesses about missing appendix content applies.

- **$\log T$ factor removal not supported (Critic's point #5):** The critic says the removal of the $\log T$ factor is claimed without proof. **Removed because** the claim is attributed to Theorem~thm:idealbarrier and a "more careful analysis of martingale types," whose detailed proof is in the appendix. The rule to remove weaknesses about missing appendix content applies.

- **Criticism about missing related work:** Not present in the reviews.

- **Formatting/style nitpicks about the paper's readability:** Removed per the formatting/style rule.

## Novel Insights

The most novel observation emerging from this review is that the paper's core technical innovation — encoding the search for a regularizer as a convex program with a separation oracle for strong convexity — is largely decoupled from the two most significant weaknesses (the abstract/theorem mismatch and the incomputable constants). The quasi-quadratic approximation and locality analysis (Lemmas~6.1–6.2) appear technically sound and are the paper's strongest contributions. The smoothing and $\log T$ removal, while important, are referenced to the appendix and cannot be fully evaluated from the main text. The separation oracle construction (the paper's main algorithmic hurdle) also resides in the appendix. This creates an unusual situation where the most interesting and novel part of the contribution (the convex program) is visible in the main text, but the pieces needed to verify its implementability (separation oracle, smoothing, feasibility analysis) are deferred.

## Suggestions

1. **Correct the abstract** to accurately describe the lower bound as a query-complexity result (e.g., "requires exponentially many membership queries") rather than NP-hardness, unless an actual NP-hardness proof is stated as a theorem in the main body.

2. **Provide explicit formulas** for the constants $L, c_0, c_2, \uppertwo$ in terms of the input parameters $(r,R,d)$, along with a brief derivation. Since $\Rate(\mathcal{X},\mathcal{L})$ can be bounded by known functions of $r,R,d$ for symmetric convex sets, this should be possible. Even a crude bound would make the algorithm constructible.

3. **Address the oracle-model mismatch** in the lower bound by either proving the bound transfers to the linear-optimization oracle model or tempering the "necessary" language.

## Score and Decision

The paper addresses an important open problem (computing instance-optimal regularizers for OLO) with a novel technical approach (convex programming over regularizers via quasi-quadratic approximation). The core algorithmic framework and the locality analysis are genuine contributions. However, the current version has two significant issues: (a) the abstract misrepresents the lower bound as NP-hardness when the stated theorem is about query complexity, and (b) the algorithm requires constants that depend on the unknown optimal regularizer, with no explanation of how to compute them from the input alone. These gaps prevent the paper from being accepted in its current form. With a major revision that corrects the abstract and provides explicit constant-setting procedures, the paper could be strong.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>