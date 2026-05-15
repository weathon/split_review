Now I have a complete picture. Let me write the consolidated review.

## Summary

This paper tackles the problem of computing optimal regularizers for Follow-The-Regularized-Leader (FTRL) in online linear optimization (OLO). The authors present an algorithm that, given oracle access to convex symmetric action and loss sets, outputs a regularizer such that FTRL achieves regret within a universal constant factor of the minimax optimal rate. The main technical innovations are: (1) removing a logarithmic factor from the Srebro et al. (2011) universality result via a sharper martingale analysis; (2) smoothing the ideal regularizer via Gaussian convolution to obtain bounded derivatives; (3) approximating the smooth regularizer with piecewise "quasi-quadratic" functions over a finite discretization, encoded as a convex program; and (4) a lower bound showing that even verifying strong convexity requires exponentially many membership queries.

## Strengths

1. **Algorithmic regularizer computation for OLO.** Theorem 1.1 states a cutting-plane algorithm that, with oracle access to the loss set, computes a regularizer achieving regret $O(\Rate(\mathcal{X},\mathcal{Y}^*)\sqrt{T})$ — within a universal constant of the optimal rate. The runtime $(\frac{dR}{r})^{O(d^2)}$ is independent of the horizon $T$, which directly delivers on the paper's central claim of computing a near-optimal regularizer for any convex symmetric action and loss set.

2. **Removal of the $\log T$ factor from the Srebro et al. (2011) universality result.** The paper claims (Section 4) that a refined martingale norm-growth estimate yields a regularizer that is 1-strongly convex with respect to $\|\cdot\|_{\mathcal{Y}^*}$ and bounded by $O(\Rate(\mathcal{X},\mathcal{Y}^*)^2)$, implying regret $O(\Rate(\mathcal{X},\mathcal{Y}^*)\sqrt{T})$ without the $\log T$ factor that appeared in prior work. This is a genuine theoretical improvement over the state of the art.

3. **Connection between smoothing, quasi-quadratic approximation, and convex programming.** The construction of a smooth optimal regularizer via Gaussian convolution (Theorem 5.1), the quasi-quadratic approximation scheme (Eq.~4.3, Lemma 5.1), and the finite-dimensional convex program (Eq.~mainlp) form a coherent and technically interesting pipeline for reducing an infinite-dimensional optimization over functions to a finite-dimensional program. This is a clever methodological contribution.

4. **Explicit convex program with feasibility guarantees.** Theorem 6.1 shows that the convex program is feasible (the smoothed regularizer $\tilde{\mathcal{I}}$ is a feasible point), and any feasible solution yields a regularizer $g^{(\mathcal{I})}$ that is $\alpha/2$-strongly convex with respect to $\|\cdot\|_{\mathcal{Y}^*}$ with bounded range. The feasible region is sandwiched between Euclidean balls, enabling standard cutting-plane methods.

5. **Query complexity lower bound for verifying strong convexity.** Theorem 7.1 gives a distribution over convex bodies $\mathcal{Y}^*$ such that exponentially many membership queries are needed to distinguish the norm ball from the Euclidean ball, implying that verifying $\alpha$-strong convexity of even the identity Hessian requires exponentially many queries. This justifies the exponential complexity of the algorithm and clarifies the inherent difficulty of the problem.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Inconsistency between abstract and body regarding the lower bound.** The abstract states that "even deciding whether a given regularizer is $\alpha$-strongly-convex with respect to a given norm is NP-hard." However, Theorem 7.1 and the surrounding body text (lines 37, 203, 378) consistently describe a **query complexity** lower bound — a distribution over convex bodies such that an exponential number of membership oracle queries is needed. NP-hardness (a computational complexity concept) and exponential query complexity (an information-theoretic concept) are fundamentally different claims. The body does not provide an NP-hardness result or proof; Theorem 7.1 is explicitly an "Exponential lower bound" about membership oracle queries. This mismatch misrepresents the nature of the lower bound and needs correction. (*This is the most substantive weakness — it is a presentation error that does not undermine the core algorithmic contribution but does affect the accuracy of the paper's claims.*)

2. **Key theorems stated only by reference.** Theorem 4.2 (the "IdealBarrier" establishing existence of a 1-strongly convex regularizer with $O(\Rate(\mathcal{X},\mathcal{Y}^*)^2)$ bound) and Theorem 5.2 (smooth barrier via Gaussian convolution) are referenced in the body but their full statements and proofs are deferred to the appendix. Since these theorems are the foundation for the entire construction — the smooth regularizer's existence and properties directly determine the parameters of the convex program — the absence of their statements from the body makes the logical chain harder to follow. While deferring proofs to the appendix is standard practice, deferring the *statement* of key theorems is unusual and weakens the self-containedness of the main text.

3. **The algorithm's exponential dimension-dependence limits practical applicability.** The preprocessing time is $(\frac{dR}{r})^{O(d^2)}$, which becomes prohibitive for $d > 3$ or $4$. The paper acknowledges this and frames the contribution as a feasibility result for constant dimension, but the disconnect between the strong theoretical guarantee (within a constant factor of optimal for any instance) and the astronomical runtime even for moderate $d$ is worth noting. The paper could strengthen its case by demonstrating that the approach is implementable in any non-trivial setting.

### Trivial
- The paper uses both "barrier" and "regularizer" terminology somewhat interchangeably (e.g., "ideal barrier" vs. "regularizer"), which can cause confusion. Consistent terminology would improve readability.
- Several equations reference constants ($c_0, c_2, L, \alpha$) whose specific values in Theorem 6.1 are given in terms of other constants ($\tilde c_1, \tilde c_2, \tilde L$) that themselves depend on asymptotic bounds from Theorem 5.1; tracing the exact constant propagation is difficult without the appendix.

## Nice-to-Haves
- A small-scale worked example (e.g., $d=2$ with $\ell_2$ balls) illustrating the computed regularizer and comparing its regret to known optimal rates would help ground the theoretical claims. This is not standard for pure theory papers but would make the contribution more accessible.
- A brief proof sketch for Theorem 4.2 (IdealBarrier) in the body — even a paragraph explaining how the $\log T$ factor is removed — would significantly improve the paper's self-containedness without requiring the full proofs.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism about missing proofs and appendices** (*Removed* per instructions: the parser strips appendix/proof sections from all papers; they exist in the original submission. All lemmas and theorems stated in the body are present.)
- **Criticism about no experimental validation** (*Removed*: this is a theoretical paper in learning theory. Experiments are not standard for such contributions. Asking for experiments for a $\exp(O(d^2))$ algorithm is scope creep.)
- **Criticism about algorithm being described only at a high level** (*Removed*: the convex program, quasi-quadratic approximation, discretization scheme, and separation oracle approach are all described with explicit equations and citations. The detailed proofs are in the appendix, which is standard.)
- **Criticism about parameters $c_0,c_2,L$ being implicit** (*Removed*: these parameters are specified explicitly in Theorem 6.1 in terms of the smooth regularizer's properties from Theorem 5.1. The dependency is clearly documented.)
- **Strength: "the paper addressed an important problem"** (*Removed*: generic statement without specific evidence.)
- **Strength: "connects ideas from martingale type theory"** (*Removed*: this is a minor conceptual observation, not a concrete technical contribution.)

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface observations about the paper that the paper itself does not already articulate. The core insight — that a smooth optimal regularizer can be approximated by piecewise quasi-quadratic functions over a discretization, reducing regularizer search to a convex program — is already clearly stated.

## Suggestions
1. **Fix the abstract/body inconsistency.** Replace "NP-hard" in the abstract with a correct description of the lower bound, e.g., "requires exponentially many membership queries" or "has exponential query complexity." If an NP-hardness result exists in the full version, state it explicitly as a theorem in the body; otherwise, correct the abstract.
2. **Include statements of Theorems 4.2 and 5.2 in the body** (not just references), even if their proofs remain in the appendix. These are the linchpins of the technical argument and readers should be able to see their exact claims without consulting the supplementary material.
3. **Add a proof sketch** (1–2 paragraphs) in Section 4 explaining how the $\log T$ factor is removed from the Srebro et al. bound. This is a standalone improvement that deserves exposition in the main text.
4. **Standardize terminology** — choose either "barrier" or "regularizer" and use it consistently throughout.

## Score and Decision

**Originality:** Good. The convex-program-over-quasi-quadratics approach to regularizer computation is novel, and the removal of the $\log T$ factor is a genuine improvement.

**Importance of research question:** High. Computing optimal regularizers for OLO is a well-recognized open problem.

**Claims well supported:** Partially. The main algorithmic claims are stated as theorems but their proofs are deferred. The single most notable presentation issue is the NP-hardness claim in the abstract that does not match the body's query complexity result.

**Soundness of experiments:** Not applicable — this is a pure theory paper. The theoretical results are clearly stated.

**Clarity of writing:** Good overall. The progression from existence → smoothness → approximation → convex program → separation oracle → lower bound is logical. The abstract/body inconsistency and occasional terminology mixing slightly detract.

**Value to community:** Moderate to high. If the proofs are correct, this provides both a theoretical advance (removing the $\log T$ factor) and a concrete algorithmic framework for computing near-optimal regularizers in a general setting.

The paper has no fatal flaws. The only substantive weakness is the abstract/body inconsistency on the lower bound, which is a presentation error that can be corrected without changing the technical contribution. The core algorithmic contribution — a method for computing near-optimal regularizers via convex optimization over quasi-quadratic approximations — is well-motivated, technically interesting, and clearly described. I recommend acceptance with revisions to address the noted issues.

**Score: 7.0 / 10**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>