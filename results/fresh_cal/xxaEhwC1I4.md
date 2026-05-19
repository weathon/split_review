Now I have all the information needed to produce the final consolidated review.

## Summary

This paper provides a unified convergence analysis for the **last iterate** of Composite Stochastic Mirror Descent (CSMD), covering general (possibly unbounded) domains, composite objectives, non-Euclidean norms, and function classes spanning Lipschitz convex, smooth convex, and strongly convex objectives. The analysis yields both in-expectation and high-probability bounds. The paper extends these results to heavy-tailed noises (finite $p$-th moment, $p\in(1,2)$) and sub-Weibull noises ($p\in(0,2)$), establishing several first-of-their-kind last-iterate guarantees.

## Strengths

1. **First unified analysis framework for last-iterate convergence across diverse settings.** Lemma 3.1 (core-general) and its corollaries Lemma 3.2 (in-expectation) and Lemma 3.3 (high-probability) provide a single template that simultaneously covers general domains, composite objectives, non-Euclidean norms, Lipschitz/smooth/(strongly) convex functions, and both expectation and high-probability bounds. The paper is explicit about this claim (abstract, Section 1.1) and the lemmas are cleanly stated in the main text.

2. **First high-probability last-iterate bounds that remove both the compact-domain and bounded-noise assumptions.** Theorem 2.2 (convex) and Theorem 2.5 (strongly convex) prove high-probability rates for general domains under sub-Gaussian noises. The paper correctly identifies that "[prior works] only work for Lipschitz functions in a compact domain" (lines 460–464) and that the proof in Lemma 3.3 uses only the sub-Gaussian property, not domain compactness or bounded noise.

3. **First last-iterate convergence rates for smooth (non-strongly) convex optimization on general domains.** Theorem 2.1 gives an expected bound of $\widetilde{O}(1/\sqrt{T})$ and Theorem 2.2 gives a high-probability bound, improving on the prior non-asymptotic rate of $O(1/\sqrt[3]{T})$ by Moulines & Bach (2011). The paper explicitly calls this "the first improvement since the $O(1/\sqrt[3]{T})$ rate" (line 410), which is verified in the text.

4. **First last-iterate convergence under heavy-tailed noises (finite $p$-th moment, $p\in(1,2)$).** Theorem 4.1 matches the lower bound $\Omega(T^{1/p-1})$ up to logarithmic factors. The paper honestly restricts to convex objectives (explaining why strongly convex would force bounded domains) and notes that high-probability bounds would require clipping (left as future work).

5. **First high-probability last-iterate bounds under sub-Weibull noises.** Theorem 5.1 provides high-probability rates for $p\in(0,2)$ covering sub-exponential, etc. The paper transparently discusses the discontinuity as $p\to2$ where the bound does not recover the $\sqrt{\log(1/\delta)}$ dependence of the sub-Gaussian case (lines 1010–1016).

6. **Simpler high-probability proof technique.** Unlike prior works relying on generalized Freedman's inequality (Harvey et al. 2019), the paper's high-probability argument uses only the basic property of sub-Gaussian vectors (Lemma 2.1) and a weight sequence adapted from Liu et al. (2023). The paper notes this explicitly (lines 468–475).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Sub-Weibull results have a discontinuity at $p=2$ that prevents recovery of the optimal $\sqrt{\log(1/\delta)}$ dependence.** The $C(\delta,p)$ factor yields $O(\log(1/\delta))$ when $p\to2$, failing to recover the $\sqrt{\log(1/\delta)}$ factor from the sub-Gaussian case. While the paper acknowledges this limitation (lines 1010–1016), it is a genuine gap between the sub-Weibull analysis and the sub-Gaussian baseline. The paper does not speculate on whether a continuous dependence is achievable.

2. **Heavy-tailed results are restricted to the convex case; strongly convex is not covered.** The paper explains why (a uniformly convex mirror map combined with strong convexity would force the domain to be bounded, contradicting the paper's goal of a unified analysis on general domains; lines 812–835). The explanation is reasonable but the limitation is real and constrains the scope of the heavy-tailed contribution.

3. **The $\log T$ factor in the smooth convex unknown-$T$ bound is not discussed regarding optimality.** The paper achieves $\widetilde{O}(1/\sqrt{T})$ for smooth convex optimization, but the $\log T$ factor (present in the unknown-$T$ case) is not compared against any lower bound or analyzed for potential removal. The paper explicitly removes the $\log T$ factor for the non-smooth case with known $T$, making this silence noticeable for the smooth case.

4. **The assumption that the Bregman projection in Algorithm 1 is "efficiently solvable" (line 272) is stated without elaboration.** For a theory paper this is acceptable (the assumption is clear), but a brief remark on the conditions under which the projection is tractable (e.g., $\psi$ chosen so that the update has a closed form) would improve completeness.

### Trivial
None.

## Nice-to-Haves

- **Numerical illustration.** For an optimization theory paper, experiments are not required. However, a simple synthetic example (e.g., unconstrained least squares) demonstrating the predicted removal of the compact-domain requirement would strengthen the paper's message.
- **Explicit discussion of whether the $\log T$ factor in smooth convex bounds is removable or intrinsic.** The paper could state whether lower bounds exist or whether this is an analysis artifact.
- **A more self-contained intuition for the weight sequence $w_t$** used in high-probability bounds. The paper references Liu et al. (2023); a brief explanatory paragraph would improve readability.
- **Scope note on CSMD vs. other stochastic gradient methods.** The paper is about CSMD (of which SGD is a special case); noting explicitly that momentum or adaptive variants are not covered would manage reader expectations.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Reliance on unverified constants and deferred full statements"** — The appendix is stripped by the PDF parser; this is a formatting artifact, not a flaw in the paper as submitted. The paper repeatedly states "full version with general constants is deferred to the appendix," which exists in the original submission. (Hard rule: missing-appendix complaints are parser artifacts.)
- **"O(·) notation hides constants"** — The paper explicitly says full versions with any positive $\eta$ are in the appendix. Again a parser artifact. (Hard rule.)
- **"Missing related works"** — I cannot verify the existence or absence of related works without external sources. (Hard rule.)
- **"Algorithms beyond CSMD"** — The paper's scope is CSMD (which includes SGD as a special case). Criticizing a paper for not covering methods outside its stated scope is scope creep. (Soft rule.)
- **Pure formatting nitpicks or typos** — The paper text as provided has no evident typos; any apparent issues are parser artifacts. (Hard rule.)

## Novel Insights

The Harsh Critic's observation that the high-probability proof uses *only* the basic sub-Gaussian moment-generating function (Lemma 2.1) rather than a specialized tool like the generalized Freedman inequality is worth highlighting. This simplicity is a genuine selling point of the paper: it makes the proof accessible and suggests the framework could be adapted by other researchers more easily than prior work. The paper itself notes this (lines 468–475), but the contrast with the complexity of Harvey et al. (2019)'s approach deserves emphasis in a broader assessment. Beyond this, no genuinely novel insight emerges from the reviews beyond the paper's own well-articulated contributions.

## Suggestions

1. Add a brief discussion in Section 3 (or the conclusion) on whether the remaining $\log T$ factors in the smooth convex bounds (unknown $T$) are removable or known to be necessary from lower bounds.
2. In Section 6 (sub-Weibull), discuss the feasibility of obtaining a continuous dependence on $p$ that recovers the $\sqrt{\log(1/\delta)}$ sub-Gaussian factor as $p\to2$, or state it as a concrete open problem.
3. Include a short remark (1–2 sentences) after Algorithm 1 giving an example of a mirror map $\psi$ and composite term $h$ for which the projection step has a closed form, to ground the "efficiently solvable" assumption.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Accept</decision>