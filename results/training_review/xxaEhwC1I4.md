Now I have all the information I need. Let me compile the consolidated review.

---

## Summary

This paper provides a unified theoretical analysis framework for last-iterate convergence of Composite Stochastic Mirror Descent (CSMD). It establishes the first high-probability last-iterate bounds without requiring compact domains or bounded noises (resolving Q1), obtains near-optimal $\widetilde{O}(L/T + \sigma/\sqrt{T})$ rates for smooth convex problems and $\widetilde{O}(1/T)$ for smooth strongly convex problems in general domains (Q2), and delivers a unified proof that simultaneously covers composite objectives, non-Euclidean norms, Lipschitz/smooth/(strongly) convex function classes, and general domains (Q3). Extensions to heavy-tailed noises (first expected last-iterate results) and sub-Weibull noises (first high-probability last-iterate results) are also provided.

## Strengths

1. **First high-probability last-iterate bound without compact domains or bounded noises (Q1):** Theorems 3.2 and 3.5 provide high-probability convergence for CSMD under sub-Gaussian noises on general (possibly unbounded) domains, removing two restrictive assumptions that all prior works required. The paper explicitly states (after Theorem 3.2) that these are "the first to describe the high-probability behavior of Algorithm 1 for the wider (L,M)-smooth function class in a general domain even with sub-Gaussian noises."

2. **First optimal last-iterate rates for smooth convex and smooth strongly convex problems in general domains (Q2):** Theorem 3.1 gives $\widetilde{O}(L/T + \sigma/\sqrt{T})$ for smooth convex optimization, improving the previous best $O(1/\sqrt[3]{T})$ (Moulines & Bach 2011). Theorem 3.3 gives the first in-expectation last-iterate bound for smooth strongly convex functions ($\widetilde{O}(1/T)$). Both are extended to high-probability (Theorems 3.2 and 3.4). The paper notes (Section 3.2) that these are "the first convergence results for the last iterate of stochastic gradient methods with respect to the function value gap" for smooth strongly convex problems.

3. **Unified analysis covering composite objectives, non-Euclidean norms, and all considered function classes (Q3):** Lemma 4.1 (core lemma) is derived for general $(L,M)$-smoothness, $(\mu_f,\mu_h)$-strong convexity, and an arbitrary norm. From it, Lemmas 4.2 and 4.3 yield unified expected and high-probability bounds that apply simultaneously to all considered scenarios—covering composite objectives, non-Euclidean norms, Lipschitz/smooth/(strongly) convex functions, and sub-Gaussian stochastic oracles. The paper states (Section 4) that "this unified result for the expected last-iterate convergence can be applied to many different settings like composite optimization and non-Euclidean norms without any restrictive assumptions."

4. **First expected last-iterate convergence under heavy-tailed noises:** Theorem 5.1 provides rates $O(T^{-(1-1/p)})$ (up to log factors) that match the lower bound $\Omega(T^{-(1-1/p)})$ for convex functions.

5. **First high-probability last-iterate convergence under sub-Weibull noises:** Theorem 6.1 gives high-probability rates for convex functions under sub-Weibull noises (including sub-exponential as a special case).

6. **Improved non-smooth rates that remove logarithmic factors:** Theorems 3.3 and 3.4 achieve the optimal $O(1/\sqrt{T})$ rate (without $\log T$) for known $T$ under both expectation and high probability, using a step-size schedule from Zamani & Glineur (2023).

7. **Simpler high-probability proof technique:** The high-probability argument relies on the basic sub-Gaussian property (Lemma 2.1) rather than heavier tools like the generalized Freedman's inequality used in prior work, potentially offering new insights to the community.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **High-probability proof details rely on external techniques described concisely.** The paper borrows the $w_t$ weighting technique from Liu et al. (2023) for high-probability bounds, and the sub-Weibull section borrows a different technique from Ivgi et al. (2023) and Liu et al. (2023). While the main lemmas (Lemmas 4.3 and 6.x) are stated clearly, the paper defers detailed derivations to the appendix (stripped by the parser) and refers readers to the original works. A reader cannot fully verify the adaptation without cross-referencing those papers. This is standard practice in theory papers but worth noting—the paper would benefit from a more self-contained presentation of how these external techniques are adapted to the different step-size schedules.

2. **The sub-Weibull analysis requires a boundedness condition ($\|Z\| \leq 1/(2\sigma)$) and yields a discontinuity at $p=1$ that does not recover the sub-Gaussian dependence as $p\to2$.** The paper acknowledges both issues (lines 966-977 and 1011-1016) and correctly frames them as open problems. However, these are genuine limitations: the boundedness condition is non-trivial to verify for the specific sequences used in the analysis, and the discontinuity weakens the elegance of the claimed unification across noise types.

3. **Known-$T$ step-size schedules require horizon knowledge.** The paper provides both known-$T$ and unknown-$T$ schedules, but the known-$T$ schedules for the improved non-smooth rates (e.g., $\eta_t \propto (T-t+1)/T^{3/2}$) have a non-trivial dependence on $T$ that cannot be directly deployed in online/streaming settings. The paper does not discuss whether these can be converted to unknown-$T$ schedules (e.g., via doubling tricks) while preserving optimal rates. This somewhat limits the practical relevance of the improved results.

4. **The heavy-tailed analysis is restricted to $\mu_f=\mu_h=0$ (general convex).** The paper provides clear justification for this restriction (lines 812-835): strong convexity in the Euclidean norm would impose an undesirable uniform convexity condition, and combining uniform convexity with $(L,M)$-smoothness would force a compact domain. The restriction is principled, but it means the heavy-tailed results do not cover the strongly convex case, which may be important for some applications.

### Trivial

1. The step-size schedule $\eta_t \propto (T-t+1)/T^{3/2}$ used for improved non-smooth rates (Zamani & Glineur 2023) is unusual—it decreases linearly rather than like $1/\sqrt{t}$. The paper does not provide intuition for its shape or discuss whether it can be extended to smooth problems.

## Nice-to-Haves
- A synthetic experiment (e.g., logistic regression with controlled noise) demonstrating that the predicted rates are achievable under the proposed parameter choices would strengthen the paper. While not required for a theory paper, it would address concerns about the practical implementability of the various step-size schedules.
- A brief discussion of whether the known-$T$ schedules can be converted to unknown $T$ via the doubling trick, with explicit tracking of any extra logarithmic factors.
- Explicit examples of uniformly convex mirror maps for common non-Euclidean norms (e.g., $\ell_p$ norms) in the heavy-tailed section would be helpful.

## Removed Points
- **"First unified way" claim is overstated (Harsh Critic's Critical Issues, point 1):** The critic misreads the paper's claim. The abstract and contributions clearly state the unification is across *function classes and geometry* (general domains, composite objectives, non-Euclidean norms, Lipschitz/smooth/(strongly) convex), not across noise types. The heavy-tailed and sub-Weibull sections are presented as extensions, using similar proof ideas. The paper never claims a single lemma handles all noise types. This is a strawman criticism.

- **Step-size bound $\eta_t \leq 1/(2L)$ creates implicit restrictions (Harsh Critic's Critical Issues, point 4):** Factually wrong. The step size is defined as $\eta_t = \frac{1}{2L} \land \frac{\eta}{\sqrt{t}}$ (i.e., the minimum of $1/(2L)$ and $\eta/\sqrt{t}$). The constraint $\eta_t \leq 1/(2L)$ is satisfied by construction. There is no implicit restriction on $D_\psi$, $\sigma$, or $L$ beyond what the min operation enforces.

- **C($\delta$,$p$) discontinuity not discussed:** The paper explicitly discusses the discontinuity and the failure to recover the sub-Gaussian case (lines 1011-1016), calling it "an interesting problem." The critic claims it does not discuss this—factually wrong.

- **Missing examples of (L,M)-smooth functions not covered by existing frameworks:** The paper's goal is to unify, not to introduce new function classes. It correctly notes that L-smooth (M=0) and G-Lipschitz (L=0, M=2G) are subclasses.

- **Missing experiments:** Moved to Nice-to-Haves. A theory paper should not be penalized for lacking experiments.

- **Pure formatting/style nitpicks:** Removed per instructions.

## Novel Insights
None beyond the paper's own contributions. The key insight—using a carefully designed auxiliary sequence $z^t$ (a convex combination of past iterates and the target $x$) to convert an ergodic bound into a last-iterate bound—is clearly articulated in Section 4 and is genuinely useful. The extension of this idea to heavy-tailed and sub-Weibull settings is likewise novel.

## Suggestions
1. In a revision, explicitly verify (perhaps in the appendix) that the adaptation of the weighting technique from Liu et al. (2023) to the different step-size schedules used in the main theorems is valid. A brief note explaining why simpler approaches (e.g., directly applying Freedman's inequality) would not work would further strengthen the presentation.
2. Discuss the conversion of known-$T$ schedules to unknown $T$ via the doubling trick, even if only briefly, to address practical concerns.
3. Soften the "first unified way" phrasing slightly to make explicit that the unification is across function classes and geometry, while noting that the heavy-tailed and sub-Weibull extensions use similar proof ideas but require additional specialized assumptions.

## Score and Decision

This paper makes substantial theoretical contributions to the last-iterate convergence literature. The core claims are well-supported by rigorous analysis. The weaknesses identified are minor and do not threaten the main contributions. The paper is clearly written, thoroughly motivated, and positions its results carefully against a large body of prior work.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>