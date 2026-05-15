Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper studies linear stochastic bandits with instantaneous hard safety constraints, specifically when the feature space is non-convex or discrete. The authors identify a novel "non-convexity bias": existing safe bandit algorithms (which assume star-convex feature spaces) can suffer linear regret in non-convex settings. They propose NCS-LUCB, which introduces a new optimism bonus term \(g_t^\nu\) designed to overcome this bias, and prove a high-probability regret bound of \(\tilde{\mathcal{O}}\big(d(1+\frac{1}{\epsilon\iota})\sqrt{T}\big)\) under a local assumption around the origin and the optimal point. They also provide a lower bound \(\Omega(\max\{d\sqrt{T}, 1/(\epsilon\iota^2)\})\) and a small empirical validation on a 5-action problem.

## Strengths

- **First algorithm for non-convex/discrete safe linear bandits with provably sublinear regret.** Theorem 1 gives a rigorous bound \(\tilde{\mathcal{O}}(d(1+\frac{1}{\epsilon\iota})\sqrt{T})\) that nearly matches star-convex benchmarks up to the \(1/(\epsilon\iota)\) factor, which is the cost of handling non-convexity. This is a genuinely novel theoretical contribution.

- **Clear identification and analysis of the non-convexity bias.** The paper cleanly demonstrates (Section 5.2, Figure 2a) why standard optimistic bonuses fail in non-convex settings: they measure distance to the safe-set boundary rather than to the nearest available action, biasing the agent toward suboptimal directions. This conceptual insight is well-articulated and likely to be useful beyond this specific algorithm.

- **Novel bonus term with principled analysis.** The design of \(g_t^\nu(a)\) (Eq. 4) and the choice \(\nu = (\tau+\iota)/\iota\) are theoretically grounded. Lemma 2 shows the bonus restores optimism, and Lemma 4 shows it converges to zero at a rate that yields sublinear regret. The proof structure (Lemmas 1-4 → Theorem 1) is clear.

- **Good motivation with real-world grounding.** The venture capital investment example (Figure 2b) and the discussion of DNN-based feature extractors provide concrete intuition for why non-convex/discrete feature spaces arise in practice and why star-convexity is too restrictive.

## Weaknesses

### Fatal

None.

### Major

- **The lower bound does not justify the claimed role of \(\epsilon\) and \(\iota\) in the upper bound as strongly as advertised.** Theorem 2 gives \( \max\{ \frac{d}{8e^2}\sqrt{T},\; \frac{1-2\epsilon}{\epsilon}(\frac{1-\iota}{\iota})^2 \}\). The second term is **constant in \(T\)**. For any fixed \(\epsilon,\iota\), as \(T\to\infty\) the bound reduces to \(\Omega(d\sqrt{T})\) with no \(\epsilon,\iota\) dependence in the leading-order term. The paper's abstract and contribution list state this lower bound "highlights the necessity of \(\epsilon\) and \(\iota\) in the upper bound," but the upper bound has \(\frac{1}{\epsilon\iota}\sqrt{T}\) as a multiplicative leading-order effect, while the lower bound's \(\epsilon,\iota\) term does not scale with \(T\). A constant additive lower bound does not demonstrate that a multiplicative \(\frac{1}{\epsilon\iota}\sqrt{T}\) factor is necessary — it only shows that extremely small \(\epsilon,\iota\) increase the problem's constant hardness. Remark 3 attempts to bridge this gap for a specific \(T = \lceil 1/(\epsilon\iota^2)\rceil\), but this does not resolve the asymptotic mismatch. The paper should either (a) qualify this claim more carefully or (b) derive a lower bound where \(\epsilon,\iota\) appear in a \(\sqrt{T}\)-scaled term.

### Minor

- **Assumption 3 is restrictive and its scope is narrower than the paper's rhetoric suggests.** The assumption requires that *every direction* present in the feature set \(\mathcal{F}\) has a representative point in the radial shell \([\epsilon, \tau/\sqrt{d}]\). This is a genuine constraint: many discrete sets (where certain directions only appear with large-norm feature vectors) or sparse sets would violate it. The paper motivates this with the VC example, which is reasonable, but the general class of "non-convex and discrete" problems satisfying this assumption is not systematically characterized. The paper would benefit from a formal comparison between Assumption 3 and other non-convexity notions (e.g., what concrete practically-motivated sets satisfy it but are not star-convex?).

- **Experiments are too thin to support the theoretical claims.** Only one simulation is presented: a 2D problem with 5 discrete actions, one baseline (LC-LUCB), and no variation of the key parameters \(d, \epsilon, \iota, \tau\). There is no experiment showing: (a) how regret scales with \(d\) beyond 2, (b) how changing \(\epsilon\) or \(\iota\) affects empirical performance, (c) a larger discrete action set, or (d) a continuous non-convex set. For a paper whose central claim is a new regret bound with explicit dependence on these parameters, experiments that verify even the qualitative scaling behavior would significantly strengthen the contribution. The presented experiment validates that the non-convexity bias exists and that NCS-LUCB can overcome it on one instance, but this is minimal.

- **Imprecision in stated regret bounds across sections.** The abstract states \(\tilde{\mathcal{O}}(d(1+\frac{\tau}{\epsilon\iota})\sqrt{T})\), while Theorem 1 gives the coefficient \((2\beta_1 + \frac{2\beta_2 L(\tau+\iota)}{\epsilon\iota\tau})\) which simplifies to approximately \(2\beta_1 + 2\beta_2 L(\frac{1}{\epsilon\iota} + \frac{1}{\epsilon\tau})\). The abstract's \(\tau/(\epsilon\iota)\) differs from the dominant term \(1/(\epsilon\iota)\) in the theorem. This is a minor imprecision but could confuse readers comparing the two statements.

- **No error bars or variance information in the experiment plots.** The paper mentions 10 trials but shows only mean regret without confidence intervals. Adding these would improve interpretability.

### Trivial

- Some garbled typesetting in the parsed text (e.g., "Algortihm" on line 146, "coeffecicient" on line 152). These do not affect technical content.
- The action history bar plots (Figures 4a/4b) are referenced but their actual images are not visible in the parsed text.

## Nice-to-Haves

- A larger-scale experiment (e.g., \(d=10\) or \(d=20\), 100+ actions) with regret plotted against the theoretical scaling in \(\epsilon\) and \(\iota\).
- Comparison on a star-convex problem to show NCS-LUCB does not degrade when star-convexity holds.
- A more precise characterization of the class of sets satisfying Assumption 3, ideally with formal examples and counterexamples.
- A time-series plot showing when the algorithm expands its safe set (switches from playing \(a_2\) to \(a_1/a_3\)) would help visualize the non-convexity bias mechanism.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Assumption 3 is incoherent or incompletely stated"* — The parser stripped the conditions following "either of the following conditions holds." The original submission contains these conditions; this is a parsing artifact, not a paper error.
- *"Lemma 2 and Lemma 4 are not proven in the main text"* — These proofs reside in the appendix, which the parser strips from all submissions. Standard practice for conference papers.
- *"Missing related works"* — Cannot be verified without external sources.
- *"Typos, formatting issues, capitalization"* — Parser artifacts, not author errors.
- *"The abstract/introduction form of the lower bound does not match Theorem 2"* — The abstract states \(\Omega(\max\{d\sqrt{T}, 1/(\epsilon\iota^2)\})\) and Theorem 2 gives \(\max\{d/(8e^2)\sqrt{T}, (1-2\epsilon)/\epsilon \cdot ((1-\iota)/\iota)^2\}\). For small \(\epsilon,\iota\) these are asymptotically equivalent (\((1-2\epsilon)/\epsilon \cdot ((1-\iota)/\iota)^2 \sim 1/(\epsilon\iota^2)\)), so they match.
- *"Non-convexity bias example is a strength"* from the harsh critic's strengths list — This is actually listed as a strength by the critic as well, not removed; included here for completeness only.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging from the reviews is the subtlety of the lower bound. The paper correctly identifies that \(\epsilon\) and \(\iota\) must be positive for sublinear regret to be possible, but the constant-in-\(T\) form of their dependence in the lower bound versus the \(\sqrt{T}\)-scaled form in the upper bound reveals an open question: can one prove a *tight* lower bound of \(\Omega(d\sqrt{T}/(\epsilon\iota))\), or is there a fundamental algorithmic reason the \(\epsilon,\iota\) dependence can be a constant (additive) rather than multiplicative (leading-order)? This gap — whether \(\epsilon,\iota\) truly amplify the regret-rate or merely the problem's constant hardness — is a non-trivial direction for future work that the paper does not fully acknowledge.

## Suggestions

1. **Qualify the lower bound claim.** Reword Contribution 2 to say "demonstrating that \(\epsilon\) and \(\iota\) must be strictly positive for sublinear regret to be possible, and that Assumption 3 cannot be relaxed to allow \(\epsilon=0\) or \(\iota=0\)" rather than claiming it "highlights the necessity" of the specific multiplicative form in the upper bound.
2. **Add at least one scaling experiment.** Even a simple 2D sweep over different values of \(\epsilon\) and \(\iota\) with a synthetic non-convex set would substantially strengthen the empirical case.
3. **Clarify the scope of Assumption 3.** Add a brief discussion of what classes of non-convex/discrete sets satisfy it and which do not. This would help readers assess the practical relevance.
4. **Harmonize the bound expressions** across abstract, introduction, and Theorem 1 to avoid confusion.

## Score and Decision

This paper makes a genuine contribution: it identifies a real problem (non-convexity bias in safe bandits), proposes a clean algorithmic fix with rigorous analysis, and provides a theoretical framework that extends beyond the star-convex setting. The upper bound is technically sound and represents the first result of its kind.

However, the paper suffers from two meaningful weaknesses. First, the lower bound is weaker than advertised — its \(\epsilon,\iota\) term is constant in \(T\) and does not match the multiplicative \(\sqrt{T}/(\epsilon\iota)\) form in the upper bound, making the claim about "necessity" somewhat overstated. Second, the experimental validation is minimal, consisting of a single 5-action toy problem with no parameter variation. The assumption (Assumption 3), while reasonable, is also more restrictive than the paper's rhetoric about handling arbitrary non-convex spaces suggests.

These weaknesses are real but not fatal; they can be largely addressed with better framing and additional experiments. The core theoretical contribution (the algorithm and its upper bound) is solid.

I recommend a borderline score. The paper should not be rejected outright, but it requires revisions to the presentation of the lower bound and preferably expanded experiments before it can be considered a strong accept.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Borderline</orange>