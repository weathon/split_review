Now I have a thorough understanding of the paper and can produce a consolidated review.

## Summary

This paper proposes quantum Frank-Wolfe algorithms for projection-free sparse convex optimization. For the vector domain (ℓ₁-ball, simplex, group norm constraints), it achieves a query complexity of \(O(\sqrt{d}/\varepsilon)\) using a function-value oracle — a \(\sqrt{d}\) factor improvement over the classical \(O(d)\) per iteration — by combining finite-difference gradient estimation with Grover-based maximum finding. For the matrix domain (nuclear norm constraints), it proposes two quantum subroutines for top-singular-vector extraction (QTSVE and a quantum power method) that reduce the per-iteration update cost's dimension dependence relative to the classical power method, albeit with a worse \(\varepsilon\)-dependence. A further claim about \(O(1/\varepsilon)\) query complexity via Jordan's gradient estimation for Lipschitz functions is deferred to the appendix.

## Strengths

1. **Clean quadratic speedup for ℓ₁-ball and simplex constraints (Theorem 1, Theorem 2, Table 1).** The quantum algorithm achieves \(\tilde{O}(\sqrt{d}/\varepsilon)\) query complexity per iteration versus the classical \(O(d)\), using only a function-value oracle. The construction — finite-difference gradient circuit (Lemma 3) + approximate quantum maximum finding (Lemma 4) — is technically sound under standard assumptions, and the error analysis for how gradient approximation errors and maximum-finding errors propagate through Frank-Wolfe iterations is worked out. This is the paper's strongest and most defensible contribution.

2. **First quantum treatment of the Frank-Wolfe matrix case (Theorems 3 and 4, Section 4).** The paper introduces two quantum subroutines (QTSVE and QPM) for the nuclear-norm-constrained linear subproblem and provides explicit complexity expressions. The QTSVE approach (Algorithm 3) simplifies prior top-\(k\) singular vector extraction methods by replacing repeated sampling and threshold search with quantum maximum finding. The QPM approach (Algorithm 4) provides an alternative that reduces rank dependence at the cost of greater sensitivity to other parameters. The paper acknowledges and compares against an independent concurrent work on quantum power method.

3. **Novel subroutine for latent group norm constraints (Theorem 6, Table 1).** The paper develops a quantum subroutine that computes dual norms coherently across all groups in superposition and identifies the dominant group via quantum maximum finding. This extends the methodology beyond simple ℓ₁/sparsity constraints to a more general atomic set, with a clean \(O(\sqrt{|\mathcal{G}|})\) speedup.

4. **Non-uniform initial state analysis for quantum maximum finding (Lemma 4).** The paper explicitly handles the case where the initial amplitude distribution is non-uniform, providing a query complexity of \(O(1/\sqrt{p})\) where \(p\) is the probability of the maximum component. This is necessary for the matrix-domain algorithms (where the state after QSVE has non-uniform singular-value weights) and is correctly integrated into the overall complexity analysis.

## Weaknesses

### Major

1. **Matrix-case speedup claim is misleading when compared against the best classical method.** The abstract and introduction state "reducing at least a factor of \(O(\sqrt{d})\) over the best classical algorithm" for the matrix case. However, examining Table 2:

   - The classical **Lanczos method** (which is the better of the two classical alternatives) has complexity \(O\left(\frac{\sqrt{\sigma_1(M)}d}{\sqrt{\sigma_1(M)-\sigma_2(M)}\varepsilon}\right)\) — **linear in \(d\)**.
   - QTSVE (Table 2) has complexity \(\tilde{O}\left(\frac{\sigma_1^2(M)d}{(\sigma_1(M)-\sigma_2(M))\varepsilon^2}\right)\) — also **linear in \(d\)**.
   - So against the Lanczos method, there is **no dimension speedup at all**, and the quantum method has worse \(\varepsilon\)-dependence (\(\varepsilon^{-2}\) vs \(\varepsilon^{-1}\)) and worse spectral-gap dependence.

   The claimed \(\sqrt{d}\) speedup only holds against the power method (which is \(O(d^2)\)), not against the Lanczos method, which the paper itself acknowledges as the better classical approach. The abstract does not qualify this trade-off, and a reader cannot determine the regimes in which the quantum methods actually outperform the best classical alternative.

2. **Untenable inconsistency between complexity expressions in Table 2 and Theorem statements.** The formulas in Table 2 and the theorems do not match:

   - **QTSVE**: Table 2 has \(\tilde{O}(\sigma_1^2 d / ((\sigma_1-\sigma_2)\varepsilon^2))\); Theorem 3 states \(\tilde{O}(r\sigma_1^3 d / ((\sigma_1-\sigma_2)\varepsilon^2))\). The table omits the rank factor \(r\) and uses \(\sigma_1^2\) instead of \(\sigma_1^3\).
   - **QPM**: Table 2 has \(\tilde{O}(\sqrt{\sigma_1^2 d} / ((1-\sigma_1\gamma'_{\min})\varepsilon^3)) = \tilde{O}(\sigma_1\sqrt{d} / ((1-\sigma_1\gamma'_{\min})\varepsilon^3))\); Theorem 4 states \(\tilde{O}(\sqrt{r}\sigma_1^4 d / ((1-\sigma_1)^3 \gamma_{\min}^{2.5}))\) (with \(\varepsilon\)-dependence subsumed in parameter choices). These differ in the power of \(\sigma_1\), the presence of \(r\), the denominator structure, and even the dimensional dependence (\(d\) vs \(\sqrt{d}\)).

   These are not minor simplifications; they change the claimed speedup relative to classical methods. A reader cannot reliably assess which expression is correct or which speedup factors are real.

3. **Unsupported claim of \(O(1/\varepsilon)\) query complexity via Jordan's algorithm (Abstract, Theorem 5, Appendix A.1).** The abstract advertises that "the query complexity can be reduced to \(O(1/\varepsilon)\)" for Lipschitz functions. The main text (Section 3.1) mentions this only in one sentence referring to Appendix A.1, which was stripped from the available manuscript. No details are given about how Jordan's gradient estimation integrates with the Frank-Wolfe linear subproblem, what oracle model it requires, or how errors propagate through multiple iterations. Given that the standard finite-difference approach uses \(O(\sqrt{d})\) queries, a claim of \(O(1)\) queries per iteration is extraordinary and cannot be evaluated without the supporting argument. Placing this in the abstract and introduction without sufficient support in the main body overstates the contribution.

### Minor

4. **Strong assumptions for the matrix case are not fully acknowledged (Assumption 4, Section 4).** The algorithms assume precomputed quantum access to the gradient matrix \(M = \nabla f(X_t)\) via a specific data structure (Assumption 4). The paper states it "assumes that the gradient has been pre-computed and stored in the memory (Remark 3), following the classical convention of excluding gradient evaluation time." While the paper does add \(T_\nabla\) in the complexity tables, the cost of constructing the quantum-accessible representation of the gradient is not discussed. For a fair comparison, the overhead of preparing this representation from a function-value oracle (which the vector case uses directly) should be accounted for, especially since the title promises a "projection-free" advantage.

5. **The QPM complexity depends on a poorly characterized parameter \(\gamma'_{\min}\) (Lemma 9, Theorem 4, Table 2).** The quantum matrix-vector multiplication subroutine (Lemma 8) requires \(\|Mz\| \geq \gamma'\) for its success probability, and the power method's complexity contains a factor \(1/(\gamma'_{\min})^{2.5}\). The paper does not discuss how to estimate, guarantee, or lower-bound \(\gamma'_{\min}\) without prior knowledge of the gradient matrix and the random initial vector. The classical power method has no such parameter — it succeeds with high probability from a random start without extra assumptions. This asymmetry makes the claimed speedup difficult to interpret.

6. **Discrepancy between Table 2 and Theorem 4 in denominator structure for QPM.** Table 2 shows denominator \((1-\sigma_1(M)\gamma'_{\min})\) while Theorem 4 shows \((1-\sigma_1(M_t))^3\). These are structurally different expressions, not just simplified notation. Since \(\sigma_1(M)\) could be close to 1 (which violates the assumption \(\sigma_{\max} \leq 1\) in Lemma 8), the denominator could approach zero, dramatically inflating complexity — but the two versions of the formula would behave very differently in this regime.

### Trivial

7. The quantum gradient circuit description (Section 3.1) sketches the state preparation for \(|x^{(t)}\rangle\) informally. The claim that state preparation costs \(O(t)\) gates is plausible but no circuit construction or gate-count analysis is provided. This does not invalidate the results but reduces reproducibility.

## Nice-to-Haves

- The matrix-case analysis would be significantly strengthened by including a comparison table showing total runtime (including gradient access costs) for representative regimes (e.g., \(\varepsilon = 10^{-2}, 10^{-4}\)), rather than presenting only asymptotic expressions.
- The paper would benefit from explicitly bounding the linear subproblem accuracy \(\delta_t\) in terms of the gradient precision \(\sigma_t\) and tomography precision \(\delta_t\) in the main text, rather than deferring this to the appendix.

## Removed Points

These points were raised by the harsh critic or strength finder but are excluded from the main review for the reasons stated:

- **"Section 3.2 extensions are straightforward and duplicate analysis"**: The value of extensions is in showing broad applicability; reiterating a similar argument for different constraints is standard practice for a systematic paper. Removed as a generic complaint about scope.
- **"No discussion of how to coherently prepare \(|x^{(t)}+\sigma e_i\rangle\) for all \(i\) in superposition"**: The paper sketches the approach and cites Lemma 3 for the gradient circuit; the state preparation for a sparse |x⟩ updated incrementally is routine. Removed as a technical nitpick that is standard in the quantum algorithm literature.
- **"The derivation of QTSVE complexity from QSVE bound is not shown in the main text"**: This derivation is properly deferred to the appendix (which was stripped). Removed per the rule about missing appendix content.
- **"Comparisons mix query complexity (vector case) and time complexity (matrix case)"**: The paper clearly separates these in Tables 1 and 2 with different column heads. Removed as the paper is transparent about this.
- **Strength about "novel error propagation analysis using Hölder's inequality"**: This is listed as a strength but the main text does not actually show this analysis — it's deferred to the appendix. Kept removed as unverifiable from the available text.
- **"The matrix completion example might allow further acceleration via quantum sparse matrix multiplication"**: Criticized as an "afterthought" in conclusions, but the conclusion section is meant for future work. Removed as a content nitpick about concluding-section scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Revise the abstract and introduction** to accurately characterize the matrix-case speedup. Instead of a blanket "at least \(O(\sqrt{d})\) speedup," state the trade-off explicitly: e.g., "a speedup in the dimension dependence from \(d^2\) to \(d\) relative to the power method, at the cost of \(\varepsilon^{-2}\) vs \(\varepsilon^{-1}\) precision dependence; against the Lanczos method the dimension dependence is comparable but the \(\varepsilon\)-dependence is worse." This would give readers an honest picture.

2. **Resolve the inconsistencies between Table 2 and Theorem 3/4** so that readers have a single, self-consistent set of expressions.

3. **Either move the Jordan's algorithm argument into the main body** with a clear statement of the oracle model and error propagation, or remove the \(O(1/\varepsilon)\) claim from the abstract. An extraordinary claim requires in-text support, not just an appendix pointer.

4. **Add a discussion of the \(\gamma'_{\min}\) parameter** in the QPM analysis: how it relates to standard spectral properties, whether it can be efficiently estimated, and what its typical magnitude is.

**Round 1 bracket:** Based on initial calibration (papers in scoring bands <3.5, 3.5–7.5, >7.5), this paper sits in the 3.5–7.5 band — stronger than rejected papers scoring ~3.0 (which had no clear algorithmic contribution) but weaker than the clean near-optimal quantum optimization papers scoring 6.0+. My narrowest plausible range after round 1: **4.5 to 5.5**.

**Round 2 narrowing:** I compared against anchors at scores 4.80 (sparse online learning, Reject), 5.25 (Catalyst/QLSP, Reject), 5.33 (quantum LP/Gibbs, Reject), and 6.00 (minimizing maximal loss, Accept). The paper under review has stronger contribution than the 4.80 anchor (which had a questionable speedup regime of \(d > O(T^5)\) and no empirical validation) because the vector-case speedup here works for all dimensions and is cleaner. But it is weaker than the 5.25 and 5.33 anchors in terms of internal consistency (those papers have no contradictory formulas between tables and theorems), and significantly weaker than the 6.00 anchor (which provides matching lower bounds and a complete theoretical picture). The inconsistency between Table 2 and the theorem statements is a concrete flaw that the 5.25 and 5.33 papers avoided.

**Final score:** Placing the paper just below the 5.25 anchor due to the table/theorem inconsistency and the unsupported Jordan's algorithm claim.

## Score and Decision

<score>5.0</score>
<decision>Reject</decision>

**Comparison details for all anchors retrieved:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| hqxzi4d3Ws | 3.00 | 1 (weak) | Noise-resilient PQC training; much weaker paper with no optimization contribution |
| CrMyHiUttz | 3.00 | 1 (weak) | Bilinear zero-sum games; weaker paper on a classical-only algorithm |
| 0T8vCKa7yu | 3.00 | 1 (weak) | LLM compression; unrelated topic, no quantum contribution |
| wgnMdxS2nZ | 3.40 | 1 (weak) | Quantum federated learning; weaker paper with more speculative results |
| XABvLUXQ45 | 4.80 | 1 (middle), 2 (narrow) | Sparse online learning, Reject; similar type of quantum speedup paper but with impractical regime (\(d > O(T^5)\)); this paper's vector-case speedup is cleaner |
| pB1FeRSQxh | 6.00 | 1 (middle), 2 (narrow) | Minimizing maximal loss, Accept; cleaner results with matching lower bounds; this paper is weaker due to inconsistencies and overclaiming |
| IQi8JOqLuv | 6.33 | 1 (middle) | Quantum-driven graph learning; higher-scored paper with broader scope and more complete evaluation |
| XaARrKTNh3 | 5.25 | 1 (middle), 2 (narrow) | Catalyst/QLSP, Reject; similar level of contribution (meta-algorithm with limitations), but internally consistent; this paper is slightly weaker due to formula inconsistencies |
| rUx0zQFwD1 | 5.33 | 2 (narrow) | Quantum LP/Gibbs, Reject; solid technical improvement but poor presentation; comparable overall quality but this paper has more internal inconsistency |
| tDIL7UXmSS | 6.50 | 2 (narrow) | Quantum D²-sampling, Accept; cleaner results with practical application; this paper is weaker |
| dLrhRIMVmB | 8.00 | 1 (strong) | Topological data analysis; far stronger paper with end-to-end implementation |
| 5t57omGVMw | 8.00 | 1 (strong) | Learning to relax solvers; stronger with empirical validation |
| fMTPkDEhLQ | 8.00 | 1 (strong) | Tight lower bounds; stronger theoretical paper |
| TTrzgEZt9s | 8.00 | 1 (strong) | Distributionally robust optimization; stronger with experiments |