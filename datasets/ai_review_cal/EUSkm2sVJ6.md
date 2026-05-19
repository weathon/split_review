- Decision: Accept
- Avg Score: 7.60
- Scores: 8, 8, 8, 8, 6
Now I have all the information needed. Let me prepare the consolidated review.

---

## Summary

This paper introduces Dataset Usage Cardinality Inference (DUCI), shifting the data provenance problem from binary ("all-or-none" or "any-or-none") detection to estimating the exact proportion of a dataset used to train a model. The core technical contribution is a debiasing procedure that takes per-point membership inference guesses (from any MIA algorithm), corrects them using estimated dataset-wide TPR and FPR obtained from a small number of reference models, and aggregates them into an estimator of the usage proportion. Empirically, the method achieves maximum absolute error below 0.1 across multiple architectures and datasets, with as few as one reference model, representing a 630× computational savings versus the idealized MLE baseline.

---

## Strengths

1. **Novel and well-motivated problem formulation.** The paper formally defines DUCI (Section 3.1) and demonstrates concretely (Figure 1) that prior binary methods fluctuate erratically under partial dataset usage — e.g., classifying a model as "not using" the data at 60% usage after having classified it as "using" at 50%. This documents a real gap that the community had overlooked.

2. **Elegant debiasing framework with strong empirical performance.** The debiasing procedure (Equation 6) converts biased per-point MIA guesses into estimates that aggregate to a proportion estimator achieving max error < 0.1 (Figure 2). The method is MIA-agnostic ("applicable to any membership prediction technique," stated in Section 4), and the cost advantage over the idealized MLE baseline is quantified at 630× (Table 1) — a dramatic improvement.

3. **General applicability beyond image classification.** The method is validated on a practical book copyright infringement detection task using GPT-2 and the BookMIA dataset (Table 4), directly addressing the motivating use case of quantifying "amount and substantiality" under U.S. copyright law (Section 1). Extension to group-level estimation and non-uniform sampling (Table 2) is also demonstrated.

4. **Uncertainty quantification.** The paper provides confidence intervals for the estimated proportion (derived via Lyapunov CLT, validated in Figure 3), giving practitioners a principled way to assess estimate reliability — absent from prior heuristic threshold-based approaches.

---

## Weaknesses

### Fatal
None.

### Major

1. **The claim of an "unbiased estimator" is not adequately justified given the use of dataset-wide TPR/FPR.** The debiasing formula (Equation 6) applied per point requires that point's true TPR and FPR. The paper switches to dataset-wide estimates (Equation 7) with the justification that "the proportion p is a dataset-level statistic" (Section 4). This is not a formal justification: if per-point TPR/FPR vary across data points (which is known to happen — membership inference difficulty varies with proximity to decision boundary, outlier status, etc.), the aggregated estimator's unbiasedness is not guaranteed without additional conditions. The paper provides no theoretical analysis of this bias. The empirical results (max error < 0.1) suggest the practical impact may be small, but the theoretical claim of unbiasedness overreaches what is demonstrated. The authors should either provide a bias bound or reframe the contribution as an empirically effective method with approximately unbiased behavior under realistic conditions.

### Minor

2. **The Lyapunov CLT confidence interval derivation does not account for dependencies in model predictions.** The CLT argument requires weak dependence across per-point estimates $(\hat{m}_i - \text{FPR})/(\text{TPR}-\text{FPR})$, but these are all produced by the *same* target model $\theta$, introducing correlations. The paper says "independent data sampling" justifies this (footnote), but independence of data points does not imply independence of the model's predictions on those points. The paper validates the CIs empirically (Figure 3), which partially mitigates the concern, but the theoretical derivation as presented is incomplete. A bootstrap over training trials would be a cleaner approach.

3. **The paper conflates "error" and "bias" in Section 3.2.** The arguments cited from Kairouz et al. and Steinke et al. establish lower bounds on *error* for membership inference under indistinguishability constraints. The paper then claims these errors "accumulate and introduce biases" without formally connecting error to bias. This is a subtle distinction — systematic errors do tend to create bias — but the argument as presented is imprecise for a paper that stakes a claim on unbiasedness.

4. **No ablation of the number of reference models.** The paper states performance is achievable "with as few as one reference model" (contributions, Section 5.3) but does not show a curve of estimation error vs. number of reference models for different datasets/architectures. This is the most natural experiment to support the cost-effectiveness claim. The value of N used in Table 1 results is not stated in the visible text.

### Trivial

5. The language model case study (Table 4) is mentioned but not described in the available body text; even a brief summary of the setup is needed for self-containedness.

---

## Nice-to-Haves

- A bootstrap-based confidence interval (over model-training trials) would circumvent the theoretical concerns about the CLT independence assumption and provide more honest uncertainty quantification. The authors could compare CLT-based and bootstrap-based CIs empirically.
- A stronger "MIA Score" baseline could be constructed by calibrating confidence scores (e.g., via Platt scaling) before averaging, to test whether the debiasing step itself provides benefit beyond calibration.
- A brief complexity analysis of running MIA over the full target dataset would be helpful for practitioners applying this to large datasets.

---

## Removed Points

These points are either factually incorrect, addressed in the paper, or reflect reviewer knowledge gaps:

- **"MLE baseline comparison is unfair because no practitioner would use grid-search MLE."** — The paper explicitly frames MLE baselines as "idealized" and "computationally expensive" (Section 5.2). The comparison is fair on its own terms and the cost advantage (630×) is a genuine finding.
- **"The paper should report how many reference models the method uses."** — The paper states "as few as one" (contributions) and the method description (Section 4) discusses N reference models. The specific N used for Table 1 may be in an appendix, but the method's efficiency claim is clear.
- **"No discussion of the variance of $\hat{p}$ beyond the CI."** — The paper provides CIs precisely for this purpose.
- **"The paper assumes the dataset owner knows the training algorithm."** — This is stated explicitly in the problem formulation (Section 3.1).
- **"Missing related works."** — Cannot be verified without external sources.
- **Formatting/typo concerns.** — These are parser artifacts, not author errors.
- **Strength Finder strengths that are generic (e.g., "the problem is important").** — Dropped in favor of concrete, evidenced strengths only.

---

## Novel Insights

The reviews surface a genuine tension between the paper's theoretical framing and its empirical strength. The harsh critic correctly identifies that the "unbiased estimator" claim relies on an unexamined assumption (constant per-point TPR/FPR), yet the strength finder's evidence — max error < 0.1, 630× cost reduction, validation on language models — suggests the method works robustly in practice. The novel insight from this synthesis is that this tension is *resolvable*: the paper's practical contribution (a cheap, reliable proportion estimator) does not depend on strict unbiasedness. The empirical results are strong enough to stand on their own if the authors reframe the theoretical claims as approximate unbiasedness. The more fundamental concern — addressed by neither reviewer — is whether the method's performance degrades under *adversarial* data selection where the constant-TPR assumption would be most severely violated. The paper acknowledges this as a limitation but does not investigate the boundaries of its method's validity.

---

## Suggestions

1. **Reframe the theoretical claim.** Either (a) prove a bound on the bias from using global TPR/FPR in terms of the variance of per-point rates, or (b) honestly acknowledge that the estimator is approximately unbiased under realistic conditions and support this with a sensitivity analysis.
2. **Add an ablation of reference model count.** Show estimation error vs. N (number of reference models) for at least one dataset-architecture pair. This is the single most informative experiment for the method's claimed cost advantage.
3. **Replace or supplement the CLT confidence intervals** with a bootstrap over training trials (training multiple target models per proportion and computing empirical coverage). Report empirical coverage rates to verify the CIs are not overconfident.
4. **Include a stronger practical baseline:** a simple regression model trained on aggregated MIA statistics from the same number of reference models (e.g., average confidence score → proportion via linear regression) would better isolate the value of the debiasing procedure.

---
