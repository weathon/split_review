Now I have thoroughly verified the paper content against all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper studies activation sparsity in decoder-only Transformer LLMs (0.1B–1.2B parameters). It proposes PPL-p% sparsity, a metric that links sparsity to a controlled perplexity increase, and uses it to empirically characterize how sparsity scales with training data, activation function (ReLU vs. SiLU), width-depth ratio, and parameter count. The paper identifies opposite sparsity trends for ReLU (increasing sparsity with more data) and SiLU (decreasing sparsity), a width-depth ratio bottleneck, and weak correlation between limit sparsity and model scale.

## Strengths

- **Novel performance-aware sparsity metric (PPL-p% sparsity).** The metric adaptively determines layer-wise thresholds by binary-searching a CETT value that causes exactly a p% increase in perplexity, making it usable across arbitrary activation functions. Figure 3 demonstrates it consistently achieves a better PPL–sparsity trade-off than Top-k, FAT-ε, and straightforward ReLU baselines across multiple model scales.

- **First quantitative functional forms for activation sparsity scaling in decoder-only LLMs.** The paper derives a convergent power-law (SiLU, Eq. 5) and a decreasing logspace power-law (ReLU, Eq. 4) relating activation ratio to training data. These are fitted across five model scales (0.1B–1.2B) with ≥80× data-to-parameter ratios, going beyond prior qualitative work (Li et al., 2022).

- **Empirical evidence for scale-insensitivity of activation patterns.** Figures 9 and 10 show that neuron activation frequency distributions (per dataset) and token-wise activation ratios are nearly indistinguishable across models from 0.1B to 1.2B, supporting the non-obvious finding that limit sparsity is weakly correlated with parameter scale.

- **Rigorous training setup for reliable limit estimation.** Each model is trained on no less than 80× its non-embedding parameter count (up to 190× for some experiments), with hyperparameters following the well-tested MiniCPM recipe, lending confidence that observed sparsity limits are near-converged values.

## Weaknesses

### Major

- **Unsubstantiated claim that ReLU and SiLU have "comparable performance."** The paper repeatedly states that ReLU and SiLU achieve "comparable performance" (abstract, Section 4.2, line 134) — this is the linchpin of the recommendation to prefer ReLU over SiLU. Yet the paper presents **no evidence** comparing the two activation functions on any performance metric: no validation loss, no perplexity, no downstream task accuracy. Table 1 evaluates only SiLU models at different p% values. Figure 4 plots activation ratios (sparsity), not performance. Without this evidence, the central practical recommendation ("replace SiLU with ReLU") is unsupported. The observation that ReLU yields higher sparsity stands, but the claim that this comes without performance cost is an assertion, not a finding.

### Minor

- **Scaling "laws" are descriptive per-scale fits, not validated predictive laws.** Each model scale gets its own fitted curve with independent parameters (Eq. 4–5). No unified law predicts sparsity as a joint function of data and parameter count. No cross-scale validation is performed (e.g., predicting sparsity for a held-out 1.0B model from smaller-scale fits). The contribution is observational rather than predictive, which the title "Sparsing Law" and discussion overclaim.

- **Width-depth ratio experiments are limited to a single configuration (0.1B ReLU).** The quantitative findings (bottleneck at ~114, optimal interval 74–282) are derived from one model scale and one activation function. No evidence is provided that these values transfer to other scales or SiLU, limiting their utility as general architectural guidelines.

- **"Limit activation ratio" computation is not explicitly described for the width-depth and scale experiments.** The paper does not specify how the limit is estimated for models at different width-depth ratios (Section 4.3) — e.g., whether separate training runs were performed for each ratio, how convergence to the limit was determined, or whether the limit is the A₀ asymptote from Eq. 4/5 fits. This omission affects reproducibility of a key quantitative claim.

- **Goodness-of-fit and uncertainty are not reported for the fitted power laws.** Figure 4 shows qualitative fits, but no R², standard errors on parameters, or confidence intervals are reported for Eq. 4 and Eq. 5. The claim that these forms were found "after careful attempts" (line 113) suggests possible overfitting.

### Trivial

- **Validation dataset used for PPL measurement is insufficiently described** (line 83: "a tiny validation dataset" — no size, source, or composition specified).
- The combinatorial argument for why smaller models converge faster (Eq. 6 and surrounding text) is a heuristic that mixes combinatorics with training dynamics in an unverified way; it should be presented as speculation rather than "deduction."

## Nice-to-Haves

- **Generalize width-depth ratio experiments** to at least one other model scale and to SiLU to check whether the bottleneck point changes.
- **Report goodness-of-fit metrics** (R², confidence intervals) for the fitted power laws in Section 4.2.
- **Visualize convergence speed** directly (e.g., tokens to reach 90% of limit sparsity) rather than through derivatives in Figure 8.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that 80× data ratio is "weak" vs. Chinchilla's 20×**: The reviewer misreads the paper. 80× is far more conservative than 20× — the paper uses excess data to ensure near-saturation, which is a strength, not a weakness. **Removed: factually wrong.**

- **Criticism about MoE comparison being "tangential" and "not explained":** The MoE comparison is a brief motivational illustration (Figure 2), not a core part of the paper's contribution. The paper clearly scopes itself to intrinsic sparsity, not MoE. **Removed: scope creep.**

- **Criticism about "no statistical significance" for Table 1 downstream scores:** Single-run benchmark evaluation is the community standard for this type of study. **Removed: unreasonable request.**

- **Criticism about PPL-1% not being "unimpaired" due to a 65.0→63.5 drop:** The paper claims PPL-1% is "reliable performance-unimpaired" and Table 1 shows the actual scores. A 1.5-point drop on reading comprehension is noticeable but the paper does describe it ("reading comprehension performance is considerably impaired"). **Removed: the paper already addresses this.**

- **Criticism that models ≤1.2B is not "comprehensive":** The paper covers 5 scales, 2 activation functions, and 9 width-depth ratios. Training larger models is a resource constraint, not a methodological flaw. The scope is clearly stated. **Removed: scope creep.**

- **Strength Finder claim "ReLU yields higher sparsity than SiLU without sacrificing performance":** The "without sacrificing performance" part reflects the paper's own unsubstantiated assertion, not a verified strength. The verified strength is that ReLU yields higher sparsity — the performance claim is the weakness. **Moved here: conflicts with verified weakness.**

## Novel Insights

The reviewer who raised the "comparable performance" unsubstantiated claim and the reviewer who noted the per-scale, non-predictive nature of the fitted "laws" each identified distinct but related gaps: the paper makes strong prescriptive claims (prefer ReLU, use these quantitative relationships for design) without the cross-validation or controlled comparison that would support them. The remaining three reviewers' observations essentially corroborate these points at different granularity. The most valuable insight from the review process is that the paper's empirical contributions (the metric, the identified functional forms, the scale-insensitivity observation) are genuinely interesting and well-supported, but the paper over-interprets them into practical recommendations that require additional evidence.

## Suggestions

1. **Provide the missing ReLU vs. SiLU performance comparison.** Add a table or figure reporting validation perplexity (or loss) for both activation functions at matched model scales — this single addition would either validate or force a retraction of the paper's main practical recommendation.
2. **Tone down the "scaling law" framing.** The fitted relationships are descriptive and per-scale. Either rename them (e.g., "empirical scaling relationships") or add cross-scale validation to turn them into predictive laws.
3. **Explicitly describe how limit sparsity is estimated** for the width-depth experiments (method for fitting curves, convergence criterion).
4. **Report goodness-of-fit statistics** for the power-law fits in Figure 4.
5. **Add a caveat** that width-depth findings are demonstrated only for 0.1B ReLU models, and acknowledge that generalization requires further study.

## Score and Decision

**Originality:** 6/10 — The metric is novel, but the core findings (sparsity changes with data, width, depth) extend prior qualitative work.

**Importance of research question:** 7/10 — Activation sparsity is practically relevant for inference efficiency and interpretability; quantitative understanding is useful.

**Claims well supported:** 4/10 — The central claim of comparable ReLU/SiLU performance is entirely unsupported; other claims are adequately supported sparsity-wise but lack performance validation.

**Soundness of experiments:** 6/10 — Generally well-conducted (extensive training, multiple scales), but missing key comparisons and methodological details.

**Clarity of writing:** 6/10 — Generally clear, though some methodological steps are under-specified.

**Value to community:** 6/10 — The metric and empirical trends are useful; the unsubstantiated performance claim reduces confidence in the recommendations.

The paper makes genuine empirical contributions (a sensible metric, interesting sparsity trends, and the scale-insensitivity observation) but is undermined by an unsubstantiated central claim about "comparable performance" between ReLU and SiLU that drives its strongest practical recommendation. This gap can be addressed with additional experiments, but as submitted the evidence does not support the full set of conclusions drawn.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>