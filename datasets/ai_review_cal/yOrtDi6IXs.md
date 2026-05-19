- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies safe linear bandits (instantaneous hard constraints) in non-convex and discrete feature spaces. The authors identify a "non-convexity bias" that causes standard safe bandit algorithms (designed for convex/star-convex spaces) to suffer linear regret when the feature space is non-convex. They propose NCS-LUCB, which uses a more optimistic bonus term parametrized by local geometric parameters ε and ι, achieving regret \(\tilde{\mathcal{O}}(d(1+\frac{1}{\tau\epsilon\iota})\sqrt{T})\). They also provide a matching lower bound of \(\Omega(\max\{d\sqrt{T}, 1/(\epsilon\iota^2)\})\) and validate the approach with a simple numerical experiment.

## Strengths

- **First sublinear regret bound for safe linear bandits in non-convex feature spaces**: Theorem 1 gives \(\tilde{\mathcal{O}}(d(1+\frac{1}{\tau\epsilon\iota})\sqrt{T})\) regret under the Local Point Assumption (Assumption 3), showing star-convexity is not necessary for near-optimal performance. This is the first such upper bound in the literature.
- **Information-theoretic lower bound with matching parameters**: Theorem 2 provides \(\Omega(\max\{d\sqrt{T},\frac{1}{\epsilon\iota^2}\})\), confirming that the same geometric parameters ε and ι in the upper bound are unavoidable and that Assumption 3 cannot be further relaxed without affecting regret.
- **Novel bonus term that provably resolves non-convexity bias**: The bonus \(g_t^\nu(a)\) in Eq. (4) is designed to be sufficiently optimistic in non-convex spaces. Lemma 2 establishes the optimism property, and Lemma 4 bounds the bonus's contribution to regret, ensuring sublinearity.
- **Explicit toy example isolating the failure mode**: Section 5.2 presents a concrete 4-point non-convex action set and shows step-by-step why star-convex bonus design leads to linear regret, while the corrected bonus enables expansion toward the optimal action. This clarifies the technical challenge and the paper's solution cleanly.
- **Extension to discrete/finite action spaces without degrading the bound**: The method handles discrete action sets while maintaining the same regret bound, unlike prior safe bandit methods that require continuous convex/star-convex sets.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **ι and ε not specified in the numerical experiment**: The experiment (Section 6) reports a discrete 5-action problem with τ=0.9 and T=900,000, but does not state what values of ι and ε were used or how the key parameter ν = (τ+ι)/ι was instantiated. Since the regret bound scales as 1/(ει), the experimental result cannot be fully assessed without this information. The paper should disclose these values.
- **Single, simple empirical evaluation**: The experiment uses only one synthetic problem with 5 discrete actions and no confidence intervals across trials (though 10 trials are averaged in Fig. 1). While acceptable as illustration for a theory paper, the empirical support for the claims would be strengthened by a second problem instance (e.g., a continuous non-convex set or a different geometry).

### Trivial

- **Lower bound presentation mismatch**: The abstract states the lower bound as \(\Omega(\max\{d\sqrt{T}, 1/(\epsilon\iota^2)\})\) while Theorem 2 gives \(\max\{d/(8e^2)\sqrt{T}, (1-2\varepsilon)/\varepsilon\cdot((1-\iota)/\iota)^2\}\). These are equivalent to leading order, but the discrepancy in form (particularly the constant second term vs. the function form in the abstract) is momentarily confusing. The authors should unify the presentation.

## Nice-to-Haves

- The paper acknowledges the Bandits-over-Bandits approach (Cheung et al., 2019) for unknown ι as future work. A brief discussion of how ι relates to the geometry of specific problem classes (e.g., for discrete sets ι is the smallest distance from φ(a*) to the safe set along the direction of φ(a*)) would make the assumptions more actionable for practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Assumption 3 incomplete in main text** (from Harsh Critic — weakness about missing conditions after "either of the following conditions holds"): The extracted text has "Then, either of the following conditions holds:" followed by no visible conditions. However, the paper consistently uses ι throughout, discusses the "ι-neighborhood" intuitively, and the formal mathematical conditions were almost certainly present in the original LaTeX and lost during PDF parsing. Per the formatting-artifact rule, this criticism is removed.
- **Argmax step intractability in continuous non-convex spaces** (from Harsh Critic): The paper explicitly acknowledges this limitation in the conclusion as future work. This is a known scope limitation, not an unaddressed weakness.
- **Lack of proof details in main body** (from Harsh Critic): Standard for page-limited conference submissions; lemmas are stated and proof sketches provided. Not a genuine weakness.
- **Real-world motivation with venture-capital analogy** (from Strength Finder): This is a didactic illustration, not a core technical strength. Removed as superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Disclose ι and ε values used in the experiment**, or explain how ν was chosen for the 5-action discrete set. This is essential for the experimental result to validate the theory.
- **Add a short remark clarifying** that the two forms of the lower bound (abstract vs. Theorem 2) are equivalent to leading order in ε and ι, to avoid confusion.
- **Consider a second experiment** on a continuous non-convex set (e.g., points on a circle segment) to demonstrate generality beyond the discrete 5-action case, even if only as a proof-of-concept.
