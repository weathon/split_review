- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5
Now I have all the information I need. Let me compile the final review.

## Summary
This paper studies differentially private (DP) optimization for nonsmooth nonconvex (NSNC) objectives and proposes two algorithms that return Goldstein-stationary points with improved sample complexity over the prior work of Zhang et al. (2023). The single-pass algorithm achieves a dimension-independent "non-private" term, and the multi-pass algorithm gives the first ERM result with sublinear dimension dependence for this setting. The paper further provides a generalization result linking empirical and population Goldstein-stationarity.

## Strengths
- **High-probability sensitivity bound for zero-order gradient estimators (Lemma 3.1):** The paper observes that the standard zero-order gradient estimator, when used with sufficiently many samples per query, concentrates near its expectation with high probability. This reduces the effective sensitivity from \(O(Ld/B)\) (worst-case) to \(O(L/B)\) under the high-probability event, enabling much less noise addition. This is the technical core of the improvement and is clearly explained (Section 3, around Eq. (1) vs. Eq. (2)).

- **Dimension-independent non-private term in the single-pass guarantee (Theorem 3.1, Remark 1):** The sample complexity includes a term \(\Phi L^2/(\alpha\beta^3)\) with no dependence on \(d\), which the prior work of Zhang et al. (2023) erroneously claimed impossible. This is a genuine conceptual advance for DP NSNC optimization.

- **First ERM algorithm with sublinear dimension-dependent sample complexity (Theorem 4.1, Table 1):** The multi-pass algorithm achieves sample complexity \(\widetilde{\Omega}(d^{3/4}/(\epsilon\alpha^{1/2}\beta^{3/2}))\), which is the first to break linear dimension dependence for private ERM in this nonsmooth nonconvex setting.

- **Generalization from empirical to population Goldstein-stationarity (Proposition 5):** The paper proves that an \((\alpha,\hat{\beta})\)-stationary point of the empirical loss is, with high probability, an \((\alpha,\beta)\)-stationary point of the population loss with \(\beta = \hat{\beta} + \widetilde{O}(L\sqrt{d/n})\). This is a necessary bridge for stochastic guarantees that was absent from prior work.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Privacy accounting for the \(\delta\) budget in the single-pass algorithm is not fully explicit.** Lemma 3.1 bounds the sensitivity with probability at least \(1-\delta/2\), and Lemma 3.2 states the algorithm is \((\epsilon,\delta)\)-DP. The proof (line 602-607) says "with probability at least \(1-\delta/2\), the sensitivity is bounded... Then the privacy guarantee follows from the Tree Mechanism." Standard reasoning requires splitting the \(\delta\) budget: \(\delta/2\) for the failure event and \(\delta/2\) for the Tree Mechanism's guarantee. This accounting is not spelled out. It can almost certainly be fixed straightforwardly, but as written the derivation is incomplete.

- **The generalization proof (Proposition 5) relies on a cited uniform convergence bound whose applicability to non-differentiable Lipschitz functions is not fully verified.** The proof (line 709) invokes "Theorem 1 of mei2018landscape" as "a gradient uniform convergence bound for Lipschitz objectives." While the mathematical logic of the proof (using the bound at differentiable points to control the Goldstein subdifferential) is sound, and the claimed rate \(\widetilde{O}(L\sqrt{d/n})\) is standard from empirical process theory, the paper does not justify why the specific cited theorem applies to functions that are only Lipschitz (almost-everywhere differentiable) rather than continuously differentiable. The authors should either confirm the cited theorem covers this case or provide a self-contained argument.

### Trivial
- The tree mechanism's noise vector \(\chi_t\) in the single-pass oracle (Algorithm 2) is mentioned only in the return statement but not shown in the algorithm description. Minor clarity issue.

## Nice-to-Haves
- The paper could briefly discuss the oracle complexity (function evaluations per data point) of the single-pass algorithm, since it uses \(m = \widetilde{O}(d^2 B_1^2 + d\alpha^2 B_2^2/D^2)\) evaluations, which can be large. A brief remark on the computational trade-off would be informative.
- A short sketch of how the parameter tuning in Theorems 3.1 and 4.1 leads to the claimed bounds (beyond the algebraic derivation already in the proof) would improve readability.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Concerns about dimension factors in variance bounds (Lemma 3.3):** The critic claims the term \(\frac{L^2 d D^2 \Sigma}{\alpha^2 B_2}\) has an "extra \(d\)." This is incorrect. The smoothness constant of \(F_\alpha\) is \(O(L\sqrt{d}/\alpha)\) (Fact 2), squaring gives \(L^2 d/\alpha^2\), times \(D^2\), divided by \(B_2\), summed over \(\Sigma\) steps, exactly yields the expression in the lemma. The proof (line 644: \(\frac{d L^2 D^2}{\alpha^2 B_2}\) per step) confirms this. The dimension factors are consistent.

- **Concerns about the multi-pass algebra (Theorem 4.1):** The critic questions the derivation from \(\Sigma = \widetilde{\Theta}(\alpha/(D\sqrt{d}))\) to \(G_0 = \widetilde{O}(L\sqrt{DT} d^{3/4}/(n\epsilon\sqrt{\alpha}))\). Substituting \(\Sigma = \alpha/(D\sqrt{d})\) into \(G_0^2\) from line 681 yields \(\frac{L^2 d T}{n^2\epsilon^2} \cdot \frac{D\sqrt{d}}{\alpha} + \frac{L^2 D^2 T d^2}{n^2\epsilon^2} \cdot \frac{\alpha}{D\sqrt{d}} = \frac{L^2 d^{3/2} DT}{n^2\epsilon^2\alpha} + \frac{L^2 D T d^{3/2}}{n^2\epsilon^2\alpha}\), so \(G_0 = \widetilde{O}(L\sqrt{DT} d^{3/4}/(n\epsilon\sqrt{\alpha}))\). The algebra is correct.

- **Claim that the generalization proof is "invalid":** The critic asserts an "invalid application" of the cited theorem. However, the paper explicitly states the theorem is for "Lipschitz objectives," and the mathematical logic of the proof is sound: it uses uniform convergence of gradients at differentiable points to bound the Goldstein subdifferential difference. The critic's claim that the theorem is "likely intended for smooth functions" is speculation about a paper the reviewer cannot verify. The result \(\widetilde{O}(L\sqrt{d/n})\) is standard and follows from generic empirical process theory for Lipschitz function classes. The concern is demoted to a minor weakness about insufficient justification, not invalidity.

- **Nitpicks about missing appendix content, reproducibility details, formatting:** These are parser artifacts or standard deferred material, not actual weaknesses.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Provide a clean accounting of the \(\delta\) budget in the single-pass privacy proof, explicitly showing the split between the high-probability sensitivity event and the Tree Mechanism's parameter.
- Add a brief verification that the cited uniform convergence theorem (or a standard alternative) indeed applies to Lipschitz (non-differentiable) functions, or provide a self-contained argument using standard empirical process theory.
