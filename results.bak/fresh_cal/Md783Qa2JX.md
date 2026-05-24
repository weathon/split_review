Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper studies the problem of computing near-optimal regularizers for Follow-the-Regularized-Leader (FTRL) in online linear optimization. The authors propose an algorithm that, given oracle access to convex symmetric action and loss sets, computes a regularizer such that FTRL achieves regret within a universal constant factor of the minimax optimal rate. The approach combines a Gaussian-smoothing technique to obtain a smooth regularizer, quasi-quadratic approximation of this regularizer over a discretized point set, and a convex program whose solution yields the desired regularizer. The paper also proves that the log T factor from prior work (Srebro et al., 2011) can be removed via a sharper martingale estimate, and gives an exponential lower bound for verifying strong convexity against an arbitrary norm.

## Strengths

1. **First algorithmic construction for computing near-optimal regularizers.** Theorem 1 presents a concrete cutting-plane algorithm that, given a linear optimization oracle for the loss set and a membership oracle for the action set, outputs a regularizer guaranteeing regret within a constant factor of the minimax rate. The runtime (dR/r)^(O(d^2)) is independent of the horizon T, and the approach provides the first explicit algorithmic handle on this problem. (Lines 176–185, Theorem 1)

2. **Removal of the logarithmic factor from prior universality results.** Theorem 4 (stated at line 191) improves over Srebro et al. (2011) by showing that there exists an FTRL regularizer achieving O(Rate·√T) without the log T factor present in the earlier analysis, attributed to a sharper martingale-type estimate. (Lines 190–195)

3. **Gaussian-smoothing technique that preserves strong convexity while adding derivative smoothness.** Theorem 3 (line 217) constructs a smooth regularizer whose Hessian is Lipschitz, yet the regret bound remains O(Rate·√T). This smoothness is essential for the quasi-quadratic approximation and is a non-trivial extension of the non-smooth regularizer from Srebro et al. (Lines 208–227)

4. **A convex program that reduces the search over regularizers to a finite-dimensional optimization.** The program defined in Section 7 (lines 300–309) encodes the regularizer's value, gradient, and Hessian at a finite discretization set, and any feasible solution yields a regularizer with bounded range and near-optimal strong convexity. (Lines 259–309, Lemmas 2–4)

5. **Exponential lower bound for verifying strong convexity w.r.t. an arbitrary norm.** Theorem 5 (line 380) proves that even checking whether the quadratic regularizer f(x)=||x||₂² is α-strongly-convex with respect to the dual norm requires exponentially many membership queries, partially justifying the exponential runtime of the algorithm. (Lines 374–391)

## Weaknesses

### Fatal
None.

### Major

1. **Per-round runtime claim is inconsistent with the regularizer representation.** The regularizer g^(inst)(x) = max_{i∈[N]} g_i(x) is defined as a maximum over N = exp(Θ(d² log d)) quasi-quadratic functions (lines 262–269, Theorem 1). Evaluating this at a single query point — as required by each iteration of the cutting-plane method used to run FTRL — naively requires computing the maximum over all N pieces. The paper claims a per-round running time of O(d² ln^{O(1)}(dRT)) (line 185), but provides no mechanism (data structure, spatial lookup, or other) for evaluating or separating over this max in time sub-exponential in d. Without such a mechanism, the per-round runtime necessarily includes a factor of exp(Θ(d²)), contradicting the stated bound. The abstract's claim that the algorithm "can be run efficiently online" is therefore unsupported by the paper as written.

2. **Constants in the convex program depend on quantities not computable from the given oracles.** The convex program (lines 300–309) involves constants c₀, c₂, L, U₂, whose values in Theorem 6 (line 360) are specified in terms of properties (c̃₁, c̃₂, L̃, U) of the *unknown* smooth regularizer that the algorithm is trying to construct. The algorithm is given only a membership oracle for X and a linear optimization oracle for L (plus the radii r and R), yet the paper does not explain how these constants are determined solely from this input. For instance, L = Rate·d^{3/4}/r³ (line 234) depends on Rate, which is not known a priori. Without a method for setting these constants (e.g., via conservative bounds using only r, R, d, or via a search procedure), the convex program cannot be instantiated. This is a significant gap in the algorithmic specification.

### Minor

3. **Standard FTRL regret bound (Fact 1) contains an inverted α dependence.** Fact 1 (line 164) states the regret as O(C√(αT)). Standard FTRL analysis (e.g., Hazan 2016, Theorem 5.2, which the paper cites) gives regret O(√(D/α)·√T) for a regularizer with range D and strong convexity α. With D = C², this yields O(C/√α·√T), not O(C√α·√T). The α is in the numerator when it should be in the denominator. While the paper ultimately uses α = 1 so this error does not propagate to the main results, it is a mathematical error in a basic formula that should be corrected.

4. **Key foundational claims have proofs deferred to the (stripped) appendix.** The existence of the smooth regularizer (Theorem 3), the removal of the log T factor (Theorem 4), the locality lemma (Lemma 4), and the main feasibility theorem (Theorem 6) all state results crucial to the paper's construction but provide no proof sketches in the main text. For a paper whose algorithmic construction rests on these claims, the absence of even a brief sketch of the central technical arguments makes independent assessment difficult.

5. **The separation oracle for strong convexity constraints relies on an argument not present in the main text.** The constraint v^T Σ_{x_i} v ≥ α for all v ∈ L^c (line 306) is an infinite family of constraints. The paper states that finite discretization of L suffices (referencing Section 7 for details), but the required analysis of discretization error, how it couples with ε-locality, and why the resulting approximate separation oracle does not degrade the constant-factor optimality guarantee is absent from the main text. Since Theorem 7 shows exact verification is NP-hard, the reader cannot verify from the main text that the proposed approximate oracle is sound.

### Trivial
None.

## Nice-to-Haves

- The per-round runtime issue could be addressed by acknowledging that evaluating g at a query point requires time proportional to N (which is exponential in d) and revising the runtime claim accordingly, or by developing a data structure that exploits the locality property to find the maximizing discretization point in sub-exponential time (e.g., via approximate nearest-neighbor search over the discretization grid).
- The constants problem could be resolved by showing that the smooth regularizer's parameters (c̃₁, c̃₂, L̃, U) can be bounded in terms of r, R, d alone, using the fact that Rate can be bounded geometrically. The paper should either derive such bounds or describe a search procedure.
- The learning rate η = 1/√T assumes T is known ahead of time; a doubling trick (standard in the literature) would address this.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The existence of a smooth regularizer... is not established in the main text"** — The paper states the result (Theorem 3) and sketches the Gaussian-smoothing construction (lines 208–227), then references the detailed proof. Deferring proofs to the appendix is standard for conference papers. The critique about insufficient evidence is more about completeness than a genuine flaw.
- **"The separation oracle is not convincingly described"** — The main text references Section 7 for the detailed construction. Since the appendix is stripped by the paper-parsing pipeline, the authors' full argument is not accessible for evaluation. This is a limitation of the review process, not necessarily a paper flaw.
- **"Missing oracle specification: How does the algorithm obtain L?"** — This is subsumed by Weakness 2 (the constants issue).
- **"Dependence on T: η = 1/√T assumes T known"** — This is a standard issue with a standard fix (doubling trick) and does not affect the paper's core contribution.
- **"Comparison with Srebro et al. 2011: log factor removal not substantiated"** — The paper claims a sharper martingale estimate (line 195) and defers the proof. This is subsumed by Weakness 4.
- **"Clarity of notation: L^c and L used interchangeably"** — A presentation nitpick that does not affect the technical content.
- **Strengths dropped from the Strength Finder:** None of the five listed strengths are generic or superficial; all correspond to concrete, verified contributions in the paper. No strengths were dropped.

## Novel Insights

The reviews surface one genuinely novel observation that goes beyond the paper's own contributions: The tension between the paper's two main complexity claims — that the regularizer is represented by an exp(O(d²))-dimensional vector and that the per-round FTRL runtime is only O(d² ln^{O(1)}) — highlights a non-trivial open question about whether the max-of-quasi-quadratics representation can be evaluated efficiently using the locality property (Definition 5). If the locality property could be leveraged to give exp(O(d)) evaluation (e.g., by only checking O(1/ε^{d}) nearby centers), it would bridge the gap. Conversely, if no such efficient evaluation exists, the per-round runtime would be exponential, making the "efficient online" claim incorrect. The reviewers' cross-examination reveals this as a blind spot the paper does not address.

## Suggestions

1. **Revise the per-round runtime claim.** Either (a) acknowledge that evaluating g requires time proportional to the discretization size N (which is exponential in d), making the per-round runtime also exponential; or (b) describe a concrete data structure (e.g., a spatial tree over the discretization points, or exploiting the locality property to only evaluate quasi-quadratic functions at centers within a bounded radius) that permits faster evaluation, and back it with analysis.

2. **Specify how the convex program constants are set from the given input.** Derive upper bounds on c̃₁, c̃₂, L̃, U (the smooth regularizer's Lipschitz constants) in terms of r, R, d alone — since the algorithm only has access to these quantities plus oracles. Alternatively, describe a search procedure over possible values of these constants.

3. **Correct the α dependence in Fact 1** or add a clarifying note about the normalization convention used.

4. **Include brief proof sketches** in the main text for the smooth regularizer existence (Theorem 3), the log-factor removal (Theorem 4), and the feasibility theorem (Theorem 6), since these are foundational to the algorithmic construction.

5. **Provide the discretization error analysis** for the strong-convexity constraint's separation oracle in the main text, or at minimum state the discretization density required and how it couples with the ε-locality guarantee.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>