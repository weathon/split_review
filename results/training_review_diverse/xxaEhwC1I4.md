Now I have all the information needed to produce the consolidated review. Let me construct it carefully.

---

## Summary

This paper provides a unified analysis framework for the last-iterate convergence of Composite Stochastic Mirror Descent (CSMD). It establishes convergence rates across a broad spectrum of settings: general (possibly unbounded) domains, composite objectives, non-Euclidean norms, Lipschitz and smooth functions, convex and strongly convex cases, and both in-expectation and high-probability regimes. Extensions cover heavy-tailed noises (finite \(p\)-th moment, \(p\in(1,2)\)) and sub-Weibull noises. The core technical contribution is Lemma 4.1, a general recursion from which all results (Theorems 3.1–3.5, 5.1–5.2, 6.1–6.2) are derived by plugging in specific step-size choices.

## Strengths

- **First high-probability last-iterate convergence for general domains under sub-Gaussian noises without compact-domain or bounded-noise assumptions.**  
  Theorems 3.2 and 3.4 provide high-probability bounds for convex and strongly convex objectives under \((L,M)\)-smooth functions on arbitrary closed convex sets, whereas all prior high-probability results (Harvey et al., 2019; Gorbunov et al., 2020) required either a compact domain or almost surely bounded noises. The paper states this explicitly (Section 3.1, lines 460–475) and the claim is supported by the analysis.

- **Unified analysis framework that simultaneously handles composite objectives, non-Euclidean norms, Lipschitz/smoothness, and (strong) convexity.**  
  Lemma 4.1 (core-general) is the single technical device that specializes to both the in-expectation bound (Lemma 4.2) and the high-probability bound (Lemma 4.3). The paper convincingly demonstrates that all settings are covered by plugging different step sizes into these lemmas (Section 4, lines 636–740). No prior work provides such a unified treatment.

- **First last-iterate rates for smooth (strongly) convex optimization with general domains.**  
  Theorem 3.1 gives an expected rate \(\widetilde{O}(L/T + \sigma/\sqrt{T})\) for smooth convex functions, improving the prior best \(O(1/T^{1/3})\) from Moulines and Bach (2011). Theorem 3.3 gives the first high-probability last-iterate bound for smooth and strongly convex problems (Section 3.2, lines 404–423, 567–577).

- **First last-iterate convergence guarantees under heavy-tailed noises and sub-Weibull noises.**  
  Theorem 5.1 provides the first expected last-iterate rate under heavy-tailed noises (finite \(p\)-th moment), nearly matching the lower bound \(\Omega(T^{1/p-1})\). Theorem 6.1 provides the first high-probability last-iterate bound under sub-Weibull noises. The paper explicitly claims these as firsts (Section 5.3, lines 880–882; Section 6.3, lines 1006–1007).

- **Optimal \(O(1/\sqrt{T})\) last-iterate rate for non-smooth Lipschitz convex problems without compact domain.**  
  Theorems 3.3 and 3.4 remove the extra \(\log T\) factor for the non-smooth case using the step-size schedule \(\eta(T-t+1)/T^{3/2}\) from Zamani & Glineur (2023), improving over Shamir (2013) who required a compact domain and Harvey et al. (2019) who required bounded noises.

- **Simpler high-probability proof technique based on basic sub-Gaussian properties rather than complex martingale inequalities.**  
  The high-probability analysis uses only Lemma 2.2 (the elementary property of sub-Gaussian random vectors), in contrast to previous work that relied on the generalized Freedman's inequality. This is clearly stated (lines 469–472) and represents a genuine methodological simplification.

## Weaknesses

### Fatal
None.

### Major
None. The paper makes substantive theoretical contributions; no weakness undermines its core claims.

### Minor

- **Missing discussion of lower bound context for smooth convex problems.**  
  The paper discusses lower bounds for Lipschitz problems (Section 1.2) but does not compare its smooth convex rate \(\widetilde{O}(L/T + \sigma/\sqrt{T})\) against known lower bounds for smooth optimization. A brief statement acknowledging that the optimal last-iterate rate under smoothness is not fully characterized (and that the result improves the only prior bound \(O(T^{-1/3})\)) would add useful context.

- **Step-size definition for heavy-tailed case when \(L=0\).**  
  In Theorem 5.1 (lines 864–866), the step size uses \(\eta_* = \Theta([D_\psi]^{(2-p)/p} / L)\), which is undefined when \(L=0\). While Theorem 5.2 separately handles the non-smooth (\(L=0\)) heavy-tailed case, the paper does not explicitly note that for \(L=0\) the condition \(\eta_t \leq 1/(2L)\) is vacuous and the step size in Theorem 5.1 simply reduces to \(\eta/t^{1/p}\). A clarifying remark would prevent confusion.

- **The \(\sqrt{\log T}\) gap relative to the optimal averaged rate for smooth convex problems.**  
  The paper achieves \(\widetilde{O}(L/T + \sigma/\sqrt{T})\) for smooth convex functions while the optimal averaged rate is \(O(L/T + \sigma/\sqrt{T})\). The paper mentions this gap (lines 415–418) but offers no discussion of whether the \(\sqrt{\log T}\) factor is fundamental or an artifact. A brief comment on this would strengthen the presentation.

### Trivial

- No summary table of all convergence rates is provided. The rates are spread across multiple theorem statements; a table would improve readability. This is a presentation convenience, not a technical flaw.

## Nice-to-Haves

- A short proof sketch for Lemma 4.1 in the main text (even 2–3 equations showing how convexity of \(F\) is used to bound \(F(x^{T+1}) - F(z^T)\)) would help readers assess the proof without consulting the appendix. The current conceptual explanation (using \(w_t, v_t, z_t\)) is informative but schematic.
- A discussion of whether the \(\log T\) factors in the smooth case are an artifact of the analysis or reflect a genuine gap.
- The paper could note more explicitly that the step-size schedule \(\eta(T-t+1)/T^{3/2}\) for the improved non-smooth case is decreasing in \(t\) and trivially satisfies \(\eta_t \leq 1/(2L)\) when \(L=0\).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Reliance on deferred proofs (methodological gap)"** — Removed per rule: criticisms about missing proofs in the appendix are not valid because the parser strips appendix sections from all submissions; they exist in the original paper. The main text provides intuition and sketches for Lemmas 4.1–4.3, which meets the standard for a theory paper under space constraints.

2. **"Sub-Weibull analysis requires boundedness condition on Z (Lemma 6.1)"** — Removed per rule: the paper states (lines 957–963) that a different technique (from Ivgi et al. 2023 and Liu et al. 2023) is used to ensure this condition holds. The detailed verification is in the appendix, which was stripped by the parser. The existence of the boundedness condition is stated honestly; the paper's claim to address it is explicit.

3. **"The word 'simple' might be an overstatement"** — Removed: a style/subjective comment, not a substantive weakness.

4. **"\(\eta=1.5\) is arbitrary"** — Removed: the paper already acknowledges this (line 544: "the constant \(\eta=1.5\) is chosen without any special reason") and notes that any \(\eta\) satisfying \(\eta+\kappa_f > 1\) works. This is not a weakness.

5. **General comments about lemma ordering and connections** — The critic notes that Lemma 4.1 is the most general and Lemmas 4.2–4.3 are specializations. This is already clear from the text (lines 716–718, 731–736) and is a description, not a weakness.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the simplification of the high-probability proof technique (using only basic sub-Gaussian concentration rather than the generalized Freedman's inequality) is a methodological contribution in itself, as it makes the analysis accessible to a broader audience and separates the probabilistic machinery cleanly from the optimization structure. The reviews also correctly note that the paper's honest acknowledgment of its limitations (e.g., the non-continuous dependence on \(p\) in the sub-Weibull case, the extra \(\log T\) factors) strengthens its credibility, though this is more a meta-observation about presentation than a technical insight.

## Suggestions

1. Add a brief remark in Theorem 5.1 clarifying that when \(L=0\), the term involving \(\eta_*\) vanishes and the step size reduces to \(\eta/t^{1/p}\).
2. Add a short discussion (2–3 sentences) comparing the smooth convex last-iterate rate to known lower bounds, even if only to note that the optimal rate for this setting is not yet characterized.
3. Consider adding a summary table of convergence rates for quick reference (optional but helpful).

## Score and Decision

This is a strong theoretical paper that makes significant progress on several open problems in last-iterate convergence of stochastic gradient methods. The unified analysis framework (Lemma 4.1) is a genuine contribution that yields new results across multiple settings simultaneously. The paper is well-structured, assumptions are clearly stated, and the claims are appropriately scoped. The remaining weaknesses are minor and do not affect the core contribution. The paper meets the standards of a strong theory contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>