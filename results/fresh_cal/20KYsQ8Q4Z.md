Now I have all the information. Let me construct the final consolidated review.

## Summary

This paper proposes GTBO, a method that adapts noisy adaptive group testing—originally designed for binary outcomes—to identify active (influential) dimensions in high-dimensional Bayesian optimization. The method models the difference between a perturbed evaluation and a default evaluation as a two-component Gaussian mixture, uses mutual information to select groups of variables to test via a forward-backward algorithm with SMC-based belief updates, then performs standard BO on the identified active subspace. Experiments on synthetic benchmarks (up to 100D with dummy dimensions) and real-world problems (124D and 180D) show strong optimization performance and near-perfect active-dimension identification (0.05% false positive rate).

## Strengths

- **Principled adaptation of group testing to continuous functions.** The paper provides a clean mathematical formulation (Assumptions 1–2, Eq. 6 for mutual information) that extends group testing—originally designed for binary test outcomes—to continuous, noisy function evaluations via a Gaussian mixture model. This provides a theoretical grounding for the method.

- **Near-perfect identification of active dimensions.** Figure 2 shows that across ten runs on four synthetic benchmarks, all active dimensions are correctly identified in every run, with only 6 out of 1180 inactive dimensions misclassified (false positive rate ~0.05%). This directly supports the claim that GTBO reliably discovers active variables.

- **Strong optimization performance against diverse baselines.** GTBO achieves competitive or superior performance against TuRBO, SAASBO, HEBO, BAxUS, CMA-ES, and ALEBO on both synthetic benchmarks (Branin2, Levy4, Hartmann6, Griewank8) and real-world benchmarks (Mopta08, LassoDNA). The performance jump after the group-testing phase (e.g., Mopta08 at iteration 300) provides direct evidence that identifying active dimensions accelerates optimization.

- **Sensitivity analysis characterizing robustness.** Section 4.4 systematically ablates noise level, dimensionality, and number of active dimensions, showing graceful degradation and explicitly documenting when the method breaks down (e.g., when active dimensions exceed √D). This gives readers a clear picture of the method's applicability domain.

## Weaknesses

### Fatal

None.

### Major

- **The zero-mean assumption for active-group differences is not validated.** The paper models $Z_t \sim \mathcal{N}(0, \sigma^2)$ when the tested group contains active dimensions (Assumption 2). The sole justification is "we assume this distribution to have mean zero" (line 156). If the function's active dimensions produce a systematic shift away from the default point (e.g., the optimum is far from the default and the function is not centered), the difference distribution would have non-zero mean, violating the model. The method's detection then relies on variance differences alone. The paper provides no empirical check of robustness to mean shifts (e.g., testing on functions with additive positive-only active effects). While the overall benchmark results suggest the assumption is not catastrophically wrong for the tested problems, this is a significant gap in validation for a claimed methodological contribution.

### Minor

- **Variance estimation heuristic assumes sparsity that may not hold.** The noise and function variances are estimated by dividing dimensions into bins and taking the $\sqrt{D}$ largest empirical variances as $\sigma^2$ and the rest as $\sigma_n^2$, which assumes at most $\sqrt{D}$ active dimensions. The paper acknowledges this (line 333) and the sensitivity analysis shows the method degrades when this bound is exceeded (32/100 active dimensions). This is a documented structural limitation rather than a flaw, but it is worth noting.

- **No ablation of the group-selection criterion against simpler alternatives.** The core MI-based group selection (forward-backward algorithm) is not compared against cheaper alternatives such as random groups of comparable size, variance-based heuristics, or one-at-a-time screening. Without this, it is unclear whether the group-testing machinery adds value beyond a simpler variable-identification phase. This does not invalidate the results but weakens the claim that the group-testing formalism is the source of the gains.

- **Convergence thresholds are unanalyzed.** The group-testing phase terminates when marginal probabilities converge to $[0, C_\text{lower}] \cup [C_\text{upper}, 1]$, with $C_\text{lower}=5\times10^{-3}$ (printed as $5\times10^3$, a typo) and $C_\text{upper}=0.9$. No sensitivity analysis is provided for these thresholds, which control how many evaluations the group-testing phase consumes (up to 112 in Figure 2).

- **The random perturbation $\bm{U}$ introduces uncontrolled variance.** Equation (1) perturbs active dimensions by $\bm{U}_{i,j}\sim\mathcal{U}(-0.5, 0.5)$, drawn independently per test. Two evaluations of the same group can yield very different $Z_t$ due to the random draw of $\bm{U}$. The paper does not discuss whether this variance could dominate the signal or how it interacts with the noise model.

- **Exact noise levels for synthetic benchmarks not reported.** The paper states "significant observation noise" but provides only the noise std for the sensitivity study (0.1). The actual noise level used in the main synthetic experiments (Figure 3) is not given, making it difficult to assess problem difficulty.

- **Real-world benchmark results lack interpretability details.** The paper does not report how many variables were deemed active by GTBO on the Mopta08 (124D) and LassoDNA (180D) problems. Since real-world benchmarks have "marginal impact" from all dimensions, reporting the discovered active set would help readers judge whether the subsequent BO phase is truly exploiting a low-dimensional subspace.

- **No limitations paragraph.** The Discussion (Section 5) is a single paragraph highlighting only positive aspects. Given the strong assumptions underlying the method, a brief discussion of limitations would improve completeness.

### Trivial

- $C_\text{lower}$ is printed as $5\times10^3$ (5000) rather than the intended $5\times10^{-3}$ (0.005).

## Nice-to-Haves

- An ablation where groups are chosen randomly (with matched size distribution) instead of by MI maximization would directly test whether the group-testing formalism contributes.
- A comparison against a simple screening baseline (e.g., perturb one dimension at a time and compare variance) would contextualize the method's cost-benefit trade-off.
- Reporting hardware usage consistency across methods would improve reproducibility transparency.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Batch evaluation paragraph is vague:** The reviewer claimed the batch evaluation method is unspecified. However, the paper explicitly states (line 231) that batches are generated "by simply running the forward-backwards algorithm again excluding already selected groups." This is specified. **Removed** — factual error by reviewer.

- **Figure 2 caption insufficient detail:** The reviewer claimed the caption does not specify the number of trials accumulated. The caption clearly states "across ten runs" and "once in ten runs across the benchmarks." **Removed** — already specified.

- **Random seed handling not mentioned:** Per review guidelines, undisclosed random seeds are a trivial implementation detail and not a valid criticism. **Removed**.

- **Criticism about "the paper should compare against a simple screening baseline that runs D evaluations":** This overlaps with the ablation concern above (same substantive point, different framing). Merged into the Minor weakness on ablation.

- **Formatting/style nitpicks about presentation:** Removed per guidelines.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the zero-mean assumption.** Test GTBO on synthetic functions where active dimensions produce a non-zero mean shift (e.g., a sum of positive-only terms) and report whether detection accuracy degrades. If it does, characterize the regime where the assumption holds.
2. **Add an ablation of the group-selection criterion.** Compare MI-based selection against random groups of matched size. This would isolate whether the mutual information criterion is necessary for the observed performance.
3. **Report the discovered active set on real-world benchmarks.** This would make the results on Mopta08 and LassoDNA more interpretable and support the claim that GTBO "aids in the discovery of active parameters."
4. **Report the exact observation noise level used in the synthetic benchmarks.**
5. **Add a brief limitations paragraph** discussing the zero-mean assumption, the √D sparsity bound, and the default-point dependency.

## Score and Decision

This paper introduces a creative and well-motivated adaptation of group testing to high-dimensional Bayesian optimization. The main claims—that the method reliably identifies active dimensions and achieves strong optimization performance—are supported by careful experiments with diverse baselines and sensitivity analysis. However, the lack of validation for the zero-mean modeling assumption and the absence of an ablation for the group-selection criterion leave open questions about the method's robustness and the source of its gains. These are addressable gaps rather than fatal flaws. The paper represents a solid contribution that would be strengthened by the suggested additions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>