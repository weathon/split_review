## Summary

This paper studies the Kernel Density Estimation (KDE) problem for the Gaussian kernel in high dimensions. The core contribution is the first query-time vs. space tradeoff for KDE data structures, achieved by replacing symmetric LSH (used in prior work by Charikar et al., 2020) with asymmetric LSH (Andoni et al., 2017; Razenshteyn, 2017) in the level-set recovery reduction. The resulting optimization problem (Equation 10) is solved numerically to yield two headline results: query time $1/\mu^{0.051}$ at space $1/\mu^{4.15}$, and query time $1/\mu^{0.1865}$ at linear space $1/\mu$—the latter improving over the previous data-independent bound of $1/\mu^{0.25}$ with a simpler analysis.

---

## Strengths

1. **First query-time vs. space tradeoff for KDE (Theorem 16, Figure 1):** The paper establishes a parametric tradeoff curve $\xi(\delta)$ over the full range $\delta \geq 0$, which is a qualitatively new contribution relative to all prior work. No previous result showed how to trade space for improved query time in KDE data structures.

2. **Explicit analytic formulation of the optimization problem (Equation 10):** The query-time exponent $\xi(\delta, x)$ is derived as a closed-form min-max expression over the asymmetric LSH parameters $\rho_q, \rho_s$ and the density-constraint collision probabilities. This is the technical core of the improvement, not just a black-box claim.

3. **Linear-space result matches the data-dependent bound closely with a substantially simpler scheme:** The $1/\mu^{0.1865}$ result at linear space beats the data-independent prior of $1/\mu^{0.25}$ and comes within 0.013 of the best known data-dependent bound ($1/\mu^{0.173}$). The paper correctly acknowledges it does not surpass 0.173, but the simplicity advantage is real.

4. **Analytic identification of the constant-query-time barrier (Section 1.2):** The paper demonstrates that even setting $\rho_q = 0$ (minimum ANN query exponent) still produces an overhead of $\approx 1/\mu^{0.09}$ from intermediate-scale collisions (Equations 6–7), and shows this is reduced to $\approx 1/\mu^{0.05}$ by optimizing $\rho_q$. The plateau in Figure 1 is thus not a numerical artifact but is grounded in the structure of the optimization.

5. **Rigorous and modular reduction:** The asymmetric ANN construction (Theorem 7) is carefully integrated into the Level-$j$ Recovery framework via Lemma 15, with explicit threshold functions $\theta(\delta)$ separating constant-query and polynomial-query regimes (Definition 14). The reduction is clean and generalizes the Charikar et al. 2020 framework in a principled way.

---

## Weaknesses

### Fatal
None.

### Major

- **Numerically derived headline exponents with no analytic characterization or bracketing:** Both key values—$0.051$ (Theorem 17, regime 1) and $0.1865$ (Theorem 17, regime 2)—are obtained by numerically solving the optimization in Equation (10). The paper explicitly states: *"The exact optimum does not seem simple to obtain analytically, and we therefore resort to numerics."* For a theory paper whose central claims are stated to four significant figures, the absence of any analytic bound that brackets the true optimum is a real gap. Even a weak analytic lower bound confirming that no parameter choice in the current framework can improve beyond 0.173 at linear space would substantially strengthen the claim. As it stands, readers cannot verify the headline numbers without running the same numerical solver. The paper should at minimum report the numerical precision (tolerance, solver used) in Appendix D so the reproducibility of the central claims is clear.

### Minor

- **Abstract framing obscures the space cost of the headline result:** The abstract calls the $1/\mu^{4.15}$ space requirement "somewhat higher" relative to the $1/\mu$ prior art. In the regime $\mu = n^{-\Theta(1)}$, this is $\Theta(n^{4.15})$, which far exceeds the dataset itself. The paper is fully transparent about this in Section 5, but the abstract framing may mislead readers into thinking the headline improvement is a strict advance over Charikar et al. 2020's main result. The tradeoff curve (Theorem 16 / Figure 1) is actually the paper's most significant contribution and deserves to be foregrounded more clearly in the abstract.

- **Plateau phenomenon deserves formal treatment:** The paper identifies numerically that $\xi(\delta)$ plateaus at $\approx 0.05$ for $\delta \gtrsim 3.15$, and attributes this to the limits of current ANN technology. Section 1.2 gives a compelling informal argument. However, this is not formalized anywhere in the paper as a conditional lower bound: *"given the Andoni et al. ANN tradeoff constraint (Equation 8), no parameter choice in this framework achieves $\xi < 0.05$ regardless of space."* Making this a formal theorem would turn the numerical plateau into a characterization of the framework's inherent limits, which is a significant insight that the current presentation underutilizes.

### Trivial

- **Remark 12 duplicates "in expectation":** Line reads: *"contains, in expectation, only a constant number of points in expectation."* The phrase appears twice.

---

## Nice-to-Haves

- Even an analytic bound on $\xi(0)$ (the linear-space optimum) would be valuable: it would clarify whether the 0.013 gap between 0.1865 and 0.173 is a limitation of the data-independent approach or of the specific ANN construction being used.
- The motivation from fast attention computation (last paragraph of introduction) is asserted but unconnected to the technical results. A sentence explaining how the KDE query complexity translates into an attention speedup, or explicitly scoping this out, would improve the introduction.
- A proof sketch for Lemma 31 (the core technical lemma) in the main body would help readers evaluate the key departure from Charikar et al. 2020—namely, the analysis of asymmetric LSH collision probabilities from intermediate distance scales under density constraints.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Definition 10 exponent issue ($2^{J+n}$ vs. $2^{j \cdot n}$):** The harsh critic flagged this as a possible mathematical inconsistency. Verified against the paper: this is a PDF-extraction artifact. The surrounding context (sampling rate $p_j = (1/\mu)^{1-x_j} / n$ from Equation 3, expected dataset size $m_j = (1/\mu)^{1-x_j}$) is internally consistent throughout Section 3 and Section 4, confirming that the displayed formula in Definition 10 is a parser error, not an author error. Removed per parser-artifact rule.

- **Theorem 7 space formula appearing to use $\rho_q$ instead of $\rho_s$:** In the extracted text, Theorem 7 states space $n^{1+\rho_q+o(1)}$. However, Section 1.2 (line 73) explicitly says "space $n^{1+\rho_s+\alpha(1)}$ and query time $n^{\rho_q+\alpha(1)}$," and Equation 9 correctly constrains $\rho_s$ for the space requirement. The inconsistency is a parser artifact; the rest of the paper is internally consistent with standard asymmetric LSH conventions. Removed per parser-artifact rule.

- **Lemma 31 proof sketch absent from main body:** The harsh critic raised this as undermining self-containedness. Per the hard rule, criticisms about absent appendix content or missing proofs in appendix are removed, as the parser strips those sections from all papers.

- **Comparison to data-dependent Charikar et al. 2020 (0.173 vs. 0.1865) framed as a weakness:** The paper is transparent about this and explicitly notes the simpler analysis as compensation. Removed because the paper addresses this honestly, and the comparison asymmetry (the prior's 0.173 uses data-dependent techniques while this paper is data-independent) means this is not a straightforward deficit.

- **Missing related work citations:** Removed per the hard rule against citing missing related works.

- **Strength: "addresses an important problem":** Too generic; removed per filtering rule on non-specific strengths.

---

## Novel Insights

The most genuinely novel insight in this paper—not fully articulated by either reviewer—is the structural observation that the KDE query-time problem under the level-set recovery reduction is *harder* than the underlying ANN sub-problem it invokes: even the best ANN sub-routine (with $\rho_q = 0$) still incurs a $1/\mu^{0.09}$ overhead from intermediate-scale collisions. This gap between ANN complexity and KDE complexity is explained by the density-constrained collision analysis (Equations 6–7) and is a conceptual contribution that goes beyond the specific exponent improvements. It suggests that KDE is "harder" than ANN in a precise sense, and that closing the gap further would require either new ANN primitives or a different reduction framework—an interesting open problem that the paper gestures toward but does not fully formalize.

---

## Suggestions

1. Report the numerical solver details and optimization tolerance in Appendix D so that the precision of the headline exponents (0.051, 0.1865) is verifiable.
2. Attempt an analytic characterization, even a weak one, of $\xi(0)$—the linear-space optimum. Even bounding it away from 0.173 analytically would add significant theoretical value.
3. Formalize the plateau result as a conditional lower bound: "Given the Andoni et al. 2017 ANN constraint (Equation 8), no choice of parameters in this framework achieves query exponent below $0.05$ for any polynomial space." This is already argued informally in Section 1.2 but deserves a theorem.
4. Revise the abstract to foreground the tradeoff curve (Theorem 16) as the main result rather than the extreme-space point (Theorem 17, regime 1), which is of limited practical relevance.

---

## Score and Decision

**Originality:** High. The use of asymmetric LSH in the Charikar et al. reduction is a clear conceptual advance, and the resulting time-space tradeoff is the first of its kind for KDE.

**Importance:** Moderate-to-high for the TCS community; moderate for ICLR. The practical impact of $1/\mu^{4.15}$ space is limited, but the tradeoff curve and the 0.1865 linear-space result are meaningful theoretical advances.

**Claims well-supported:** The framework and reductions are rigorous. The headline exponents are numerically derived and stated to four significant figures without analytic validation, which is a real gap for a theory paper, but does not invalidate the core claims.

**Soundness:** The mathematical framework is correct and clearly argued. The numerical optimization is a standard and accepted methodology in TCS.

**Clarity:** Good technical overview (Section 1.2 is particularly well-written). Some framing issues in the abstract. Proofs in appendix (stripped) are necessary for full evaluation.

**Community value:** Genuine contribution to the algorithmic theory of KDE, with some connections to ML applications.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>