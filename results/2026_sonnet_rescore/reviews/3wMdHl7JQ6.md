---

## Summary

This paper proposes eliminating two components of the Chin et al. (2015) spectral algorithm for community detection in the two-community SBM: (1) the degree-based vertex deletion preprocessing step, and (2) the downstream Correction step. The central claim is that the simplified Spectral Partition alone achieves the inverse-logarithmic error bound of Theorem 1.3 (previously attributed to the full two-step algorithm), representing both a theoretical improvement and an algorithmic simplification. The paper supports this claim via Chernoff-bound analysis, normal approximations, Monte Carlo simulation, and empirical regression on dense-regime graph experiments.

---

## Strengths

- **Structural insight on the looseness of Theorem 3.2 (Section 3.2):** The paper correctly identifies that the adversarial vector achieving $\gamma = \sin^2\theta$ has a specific pathological structure — zeros in the middle entries, flat positive/negative entries at the extremes — that spectral eigenvectors do not possess. This is the conceptually strongest and most original observation in the paper, and Section 3.2 establishes it cleanly with a clean adversarial construction and a valid reduction to the optimization problem in Equation 9.

- **Chernoff-based convex optimization framework (Section 3.4, Figure 4a):** The paper constructs a set of optimization constraints derived from Chernoff concentration inequalities on the binomial-difference distribution of eigenvector entries (the constraint set immediately below Equation 11). Numerically solving this constrained optimization (blue points in Figure 4a) gives substantially tighter $\gamma$-vs-$\sin\theta$ values than the original quadratic bound, and the theoretical prediction of Equation 11 closely matches the numerically optimized values. This is a concrete methodological contribution.

- **Empirical observation that Spectral Partition achieves inverse-log behavior (Figure 5, orange points):** Across $n \in \{500, \ldots, 1000\}$ with $a = 0.06n, b = 0.04n$, the modified algorithm (no degree deletion, no correction) achieves error rates that track the fitted curve $\sin\theta = C/\sqrt[3]{\log(2/\gamma)}$ rather than the quadratic baseline. The convergence of orange and green points as $n$ grows (Section 4.1) is consistent with the claimed $O(1/\sqrt{n})$ approximation error.

---

## Weaknesses

### Fatal

- **The main theorem is not proven — and the proof sketch has an algebraic gap.** The paper's entire theoretical edifice is meant to culminate in establishing Theorem 1.3 for the simplified algorithm. The claimed bridge is stated in Section 4: "The functional form in Equation 13, combined with the claims of Theorems 2.2 and 3.1, *directly yields* the final result stated in Theorem 1.3." This is an unsubstantiated assertion, not a derivation. When the algebra is actually carried out: Equation 13 inverts to $\gamma \leq 2\exp(-(C/\sin\theta)^3)$; substituting Theorem 3.1's bound $\sin\theta \leq C_2\sqrt{\sqrt{a+b}/(a-b)} = C_2(a+b)^{1/4}/(a-b)^{1/2}$ yields $$\gamma \leq 2\exp\!\Bigl(-C' \frac{(a-b)^{3/2}}{(a+b)^{3/4}}\Bigr),$$ which is *not* equivalent to the required form $\gamma \leq 2\exp(-C(a-b)^2/(a+b))$ in Theorem 1.3. The exponents differ structurally, and the paper never reconciles this. This is not a matter of a missing appendix passage — the combination of Theorems 2.2/3.1 with Equation 13 simply does not produce the stated conclusion. The paper cannot be accepted with this gap unresolved.

- **Equation 13 is a curve-fit, not a derived relationship, yet it is used as the pivotal theoretical step.** Section 4 explicitly states that the functional form $\sin\theta = C/\sqrt[3]{\log(2/\gamma)}$ is "fit… using OLS regression." The cube-root-of-log form is unusual and no theoretical derivation or intuition is offered for it. Using an empirically-fitted regression equation as the key step in a claimed mathematical proof is not a valid proof strategy for a theory paper. The entire argument from Sections 3.4–3.5 builds analytic constraints (Equations 11–12) that bound $\gamma$ given $\sin\theta$, but never derives the inverse direction $\sin\theta = f(\gamma)$ analytically.

### Major

- **The experimental regime ($a = 0.06n, b = 0.04n$) is categorically different from the theoretical setting.** The SBM defined in Section 1 and analyzed in Sections 2–3 has edge probabilities $a/n$ and $b/n$ where $a, b = O(1)$ are constants independent of $n$ (the sparse regime, with $O(n)$ edges total). But Section 4 sets $a = 0.06n$ and $b = 0.04n$, making the edge probabilities $0.06$ and $0.04$ — constants, not $O(1/n)$. This is the dense regime with $\Theta(n^2)$ edges. In this regime degree concentrates strongly, the motivation for the degree-deletion step (controlling sparse-graph outlier degrees) is largely absent, and the parameter $(a-b)^2/(a+b)$ grows as $\Theta(n)$ rather than being $O(1)$. Empirical results in the dense regime do not validate the theoretical claims made for the sparse regime. The paper does not acknowledge this inconsistency anywhere.

### Minor

- **Equation 11 is also OLS-fitted.** Section 3.4 describes Equation 11 as a "theoretical prediction," but the caption of Figure 4a states it is "fitted to the optimization data using ordinary least squares (OLS) regression to account for the unit normalization." This ambiguity between analytical bound and fitted curve should be clarified throughout the exposition.

- **The proof of Theorem 2.2 in Appendix A.1 is incomplete for the high-probability statement.** The argument establishes that $\mathbb{E}[\lambda_1(M)] = O(\sqrt{a+b})$ (from Equation 15) and asserts the result "with probability $1 - o(1)$," but no concentration argument around the expectation is provided. For the Füredi–Komlós result, the $O(n^{1/3}\log n)$ correction term in Equation 15 can be non-negligible for moderate $n$; a complete high-probability bound requires exponential concentration (e.g., from Krivelevich–Vu), which is cited but not invoked for the tail probability statement.

### Trivial

- None worth noting beyond the items above.

---

## Nice-to-Haves

- **Experiments in the theoretically analyzed regime.** Running the simplified algorithm at, say, $a = 6, b = 4$ (sparse SBM) for increasing $n$ would check whether the claimed inverse-log behavior holds in the setting the theory is actually about. This is not just a nice-to-have for completeness — it is necessary to make the experimental section coherent with the theoretical one.
- **Analytical derivation of Equation 13.** The Chernoff and normal-approximation bounds in Sections 3.4–3.5 bound $\cos\theta$ as a function of $\gamma$. Inverting these analytically (rather than by regression) would replace the pivotal OLS-fitted equation with a rigorous lemma and would clarify whether the resulting exponent matches Theorem 1.3's form or some other near-optimal rate.
- **Quantification of constants in Theorem 2.2.** The paper states that Theorem 2.2 holds without deletion "with only modest increases in the constants $C_1, C_2$." Quantifying these increases matters for the regime applicability of the result.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Preservation of statistical independence" as a core strength (Strength Finder):** The independence claim (Section 2.1) is stated as a motivation for removing the deletion step, but is not developed into any concrete theorem or proof in the main text. It is flagged as useful for future work. As a present contribution it is too speculative to list as a concrete strength.

- **Strength about scalability/convergence (Strength Finder):** The convergence of orange-to-green gap with $n$ (Figure 5, Section 4.1) is cited as a strength. However, this convergence occurs in the dense regime ($a/n = 0.06$) and therefore primarily reflects the $O(1/\sqrt{n})$ quality of the distributional approximation, not a theoretical statement about sparse-SBM performance. Given the regime mismatch weakness, this cannot stand as a clean strength.

- **Harsh Critic claim on Appendix A.1 / Füredi–Komlós application:** The critic suggests the constants need to "match precisely" and that the paper "glosses over" this. The appendix proof does in fact bound $\sigma^2 \leq (a+b)/n$ (Equation 14) and invokes Füredi–Komlós to get $\mathbb{E}[\lambda_1(M)] = O(\sqrt{a+b})$ correctly. The concern about constant precision is real but minor — it is already listed under Minor above. The stronger version of this criticism ("the proof is invalid") is not supported by the text.

---

## Novel Insights

The paper's most original observation — that the adversarial vector achieving $\gamma = \sin^2\theta$ is structurally dissimilar to actual spectral eigenvectors — explains *why* Theorem 3.2 is not tight for the algorithm's output and provides the right conceptual lens for eventually proving a tighter bound. The Chernoff-based constrained optimization in Section 3.4 is a concrete instantiation of this insight and gives numerically tighter bounds. If the cube-root-of-log functional form of Equation 13 could be derived analytically from the distributional constraints, this would close the gap and constitute a genuine theoretical advance. As it stands, the insight is present and the framework is laid, but the proof is absent.

---

## Suggestions

1. **Prove or remove the claim in Theorem 1.3.** The paper's title and abstract assert that the simplified algorithm achieves information-theoretic bounds. This requires either: (a) analytically deriving the functional form of $\sin\theta$ as a function of $\gamma$ from the constraints in Section 3.4, checking whether the exponent matches Theorem 1.3, and writing this as a complete proof; or (b) honestly reframing the contribution as empirical evidence that the Correction step is unnecessary, with a rigorous proof deferred to future work.

2. **Conduct experiments in the sparse SBM regime.** Replace or supplement the dense-regime ($a = 0.06n, b = 0.04n$) experiments with the sparse regime ($a, b$ small constants) that the theory actually concerns.

3. **Clarify the status of Equations 11, 12, and 13.** Clearly distinguish between quantities that are analytically derived vs. those that are OLS-fitted. Both can appear in a paper, but conflating them as "theoretical predictions" when they are regression fits is misleading.

---

## Assessment on Key Axes

- **Originality:** Moderate. The observation about eigenvector structure in Section 3.2 is the paper's most novel element. The algorithmic simplification idea is plausible but not novel on its own.
- **Importance:** The research question (can the Correction step be eliminated?) is meaningful and practically relevant. If proved, it would be a clean result.
- **Claims supported:** Weak. The central claim (Theorem 1.3 holds for the simplified algorithm) is not proven. The empirical support is in a different regime than the theory.
- **Soundness:** Weak. The main theoretical argument has an algebraic gap, and the pivotal step is a regression fit misrepresented as a theoretical derivation.
- **Clarity:** Moderate. Writing is generally readable, but the boundary between "proved" and "empirically observed" is systematically blurred.
- **Community value:** Limited in current form. The insight in Section 3.2 has value; the rest requires substantial revision before it would serve as a reliable reference.

---

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>1</claims_supported>
<soundness>1</soundness>
<clarity>2</clarity>
<community_value>2</community_value>
</subscores>