Now let me produce the final consolidated review.

## Summary

This paper presents a large-scale empirical study comparing Bayesian neural network surrogates against standard Gaussian processes for Bayesian optimization. It evaluates finite-width BNNs with four approximate inference methods (HMC, SGHMC, deep ensembles, LLA), deep kernel learning, and infinite-width BNNs across synthetic and real-world benchmarks with varying dimensionality, stationarity, and input types. Key findings: (i) the ranking of methods is highly problem-dependent; (ii) HMC is the most reliable approximate inference method for fully stochastic BNNs; (iii) full stochasticity may be unnecessary as DKL is competitive; (iv) deep ensembles perform relatively poorly; (v) infinite-width BNNs are particularly effective in high dimensions.

## Strengths

1. **Comprehensive and well-scoped evaluation.** The paper systematically compares standard GPs, finite-width BNNs with four inference methods (HMC, SGHMC, ensembles, LLA), DKL, and infinite-width BNNs across 6 synthetic + 6 real + 3 high-dimensional problems (Section 4, Figures 3–5). This fills a clear gap in the literature where prior work studied only one or two BNN variants in specialized settings.

2. **Clear evidence that HMC is the most reliable inference method for fully stochastic BNNs.** On synthetic benchmarks HMC consistently achieves higher rewards than SGHMC, deep ensembles, and LLA, while those alternatives often plateau or fail (Figure 3). On real-world benchmarks HMC also generally outperforms other finite-width BNN inference methods (Figure 4). This finding is well-supported by the data.

3. **Novel result: infinite-width BNNs excel in high-dimensional settings.** In high-dimensional polynomial, neural-network function draw, and knowledge distillation tasks (d=20, 100, 31), I-BNNs clearly outperform all other surrogates including GPs (Figure 5, Section 4.3). This is a non-obvious finding with practical implications, and the paper provides a reasonable post-hoc explanation (non-Euclidean similarity metric combined with no data-hungry hyperparameters).

4. **The surprising weakness of deep ensembles is a noteworthy empirical contribution.** Given ensembles' success in other domains, the finding that they consistently underperform on BO tasks (plateauing on BraninCurrin, DTLZ1, etc.) is valuable (Figure 3). The paper also provides nuance by noting that ensembles improve with more queries (Section 4.4).

5. **Valuable sensitivity and ablation studies.** The architecture sensitivity study (Figures 1–2), the hybrid model ablation separating mean and uncertainty quality (Section 4.4), and the investigation of standard GP assumptions (Section 4.6) all provide practical guidance beyond the main comparison.

## Weaknesses

### Fatal
None.

### Major

1. **The analysis is predominantly descriptive rather than explanatory.** The paper shows *that* rankings vary across problems but does not systematically analyze *why*. With 15+ problems varying in dimensionality, stationarity, discrete/continuous inputs, and output multiplicity, the study has rich data to test hypotheses about which problem characteristics predict which surrogate will work best (e.g., regressing performance against effective dimensionality, degree of non-stationarity, or sample size). Without such analysis, the finding that "the ranking of methods is highly problem dependent" (stated as a core takeaway) amounts to a restatement of the results rather than an explanation that advances scientific understanding. This limits the paper's contribution relative to what a study of this scope could deliver.

2. **Limited explanatory depth for the I-BNN high-dimensional result.** The paper attributes I-BNNs' success in high dimensions to a "non-Euclidean similarity metric" and "no hyperparameters for learning" (Section 4.3), but these explanations are offered post-hoc. A deeper analysis—e.g., comparing the effective length-scales learned by GPs vs. the neural-network-induced kernel, or quantifying how the I-BNN prior concentrates in high dimensions—would substantially strengthen the scientific contribution.

### Minor

3. **The GP baseline is a single configuration, and the paper's own analysis shows this matters.** The main experiments use Matérn-5/2 with hyperparameter marginalization as "standard GPs," which is a reasonable default. However, Section 4.6 demonstrates that RBF vs. Matérn and marginalization vs. optimization produce meaningfully different results depending on the problem. Since the paper does not test whether the main rankings would change with a different (potentially better-suited) GP specification, there is a gap between the evidence and the strength of the claim that "standard GPs are relatively competitive." The paper partially addresses this through Section 4.6, but does not connect that sensitivity analysis back to the main comparison.

4. **Computational cost is acknowledged but not integrated into the primary analysis.** The paper correctly notes (Runtime subsection) that in BO the objective query typically dominates cost. However, HMC can be orders of magnitude more expensive than alternatives as the dataset grows during the BO loop. The paper presents HMC results without caveating their practical cost implications in the main ranking analysis (Figure 6), which may mislead practitioners who cannot afford gold-standard MCMC. The runtime subsection (line 330–333) is brief and disconnected from the central conclusions.

5. **Some claims would benefit from stronger statistical support.** The paper uses 10 trials with mean ± 1 SE, which is standard practice in BO. However, the claim that deep ensembles perform "consistently" worse (e.g., on Ackley 10d, Pest Control, where differences are within one SE) is a strong one that merits paired comparisons or rank-based tests across trials. The core qualitative findings are unlikely to change, but the confidence in fine-grained comparisons could be improved.

### Trivial
None.

## Nice-to-Haves
- A cost-adjusted comparison (performance vs. wall-clock time) or at minimum a prominent caveat that all HMC results reflect a method whose practical applicability depends on computational budget.
- A brief discussion of the acquisition function choice: MC-EI is used for all surrogates, which is fair but means GP-quality predictive distributions are not exploited via closed-form EI. This asymmetry is unlikely to change results but is worth noting.
- Extension of the architecture sensitivity study to inference methods beyond HMC (e.g., whether deeper networks affect SGHMC differently), though the paper's focus on HMC as gold standard is defensible.

## Removed Points
- **Weakness 5 (I-BNN framing blurs BNN vs. GP distinction):** Removed. The paper is fully transparent — it explicitly states (line 25) that I-BNNs "correspond to GPs with fixed non-stationary kernels derived from a neural network architecture" and (line 130–131) that they "cannot do representation learning and instead has a fixed covariance function." No blurring or deception occurs.
- **General formatting/style nitpicks:** Removed per instructions.
- **Missing related work complaints:** Removed per instructions (cannot verify external completeness).

## Novel Insights
The most interesting cross-perspective insight from the reviews is that the paper's grouping of models by "stochasticity" (fully stochastic BNNs vs. partially stochastic DKL vs. fixed-kernel I-BNN) is less informative than an alternative grouping by representation-learning capability: methods that learn a kernel/distance metric (finite BNNs, DKL) vs. methods with fixed kernels (standard GPs, I-BNNs). The paper's own finding — that I-BNNs (fixed kernel) outperform learned-kernel methods in high dimensions — gains sharper framing when viewed through this lens: when data is scarce in high dimensions, a strong fixed prior beats representation learning. This reframing could elevate the paper's central insight beyond what the authors currently articulate.

## Suggestions
1. Turn the current ranking analysis (Figure 6) into a predictive analysis: for each problem, measure interpretable characteristics (effective dimensionality, degree of non-stationarity, data size, number of discrete inputs) and test whether they predict which surrogate works best. This would transform the paper's main descriptive finding into an explanatory one.
2. Include at least one alternative GP configuration (e.g., RBF + optimization) in the main comparison to verify that the relative rankings are robust to GP specification. The data from Section 4.6 can almost certainly support this with minimal additional computation.
3. Add a brief caveat to the HMC results in the ranking figure and discussion noting that HMC's computational cost may be prohibitive in many practical BO settings, especially as dataset size grows.
4. Add pairwise rank-based comparisons or effect sizes for the deep ensembles claim across the full benchmark suite to strengthen statistical support where error bars overlap.

## Score and Decision
This is a solid, timely empirical study addressing an important and underexplored question. Its contributions—the comprehensive head-to-head comparison, the finding that I-BNNs excel in high dimensions, and the surprising weakness of deep ensembles—are genuine and useful to the community. The weaknesses are real but addressable: the analysis is more descriptive than explanatory (the most significant limitation), and some methodological choices (single GP specification, cost not integrated) could be tightened. The paper does not contain fatal errors, and its central claims are supported by the evidence. Given the scope and value of the evaluation, the paper merits a weak accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>