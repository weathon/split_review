Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper diagnoses why multiple-choice QA benchmark performance is hard to predict with scale. The authors show that standard metrics (Accuracy, Brier Score, probability over available choices) are computed from log-likelihoods via a sequence of transformations that progressively degrades the correlation between per-sample scores and pretraining compute. The mechanism is that these metrics depend not only on probability mass on the correct choice, but on how mass is distributed among specific incorrect choices — which fluctuates unpredictably. The paper provides empirical evidence from five model families and twelve benchmarks.

## Strengths

- **Identifies a concrete, well-articulated mechanism for unpredictability.** The paper shows exactly where and why the breakdown occurs: the transformation from $p_{\theta}^{\text{Vocab}}(\text{Correct Choice})$ to $p_{\theta}^{\text{Choices}}(\text{Correct Choice})$ introduces dependence on incorrect choices, which is where correlation with compute degrades most sharply. This is supported by a consistent ordering of correlation distributions across families and benchmarks (Figure 3).

- **Provides striking visual evidence that incorrect-choice dependence breaks predictability.** Figure 4 demonstrates that once metrics incorporate incorrect choices, knowing the correct choice's probability mass provides almost no information about the downstream metric — any value of one can map to nearly any value of the other. Figure 5 shows that incorrect-choice masses can vary by orders of magnitude for a fixed correct-choice mass. These figures are the paper's strongest evidence.

- **Offers a principled explanation for why pretraining loss scales predictably while individual benchmarks do not.** Pretraining loss does not depend on comparing correct outputs against specific incorrect alternatives; multiple-choice metrics do. The paper connects this structural difference to the observed correlation degradation, which is a clean and pedagogically valuable explanation.

- **Provides practical, actionable takeaways.** The Takeaway boxes (especially the recommendation to consider $p_{\theta}^{\text{Vocab}}(\text{Correct Choice})$ as a smoother surrogate and the warning that continuous metrics are not a panacea) are grounded in the empirical analysis and give concrete guidance for evaluation design.

## Weaknesses

### Major

1. **Correlation with compute is a proxy for predictability, but the paper does not connect it to actual extrapolation performance.** The paper equates "predictability" with "correlation with compute" (line 132: "To quantify how this sequence of transformations affects predictability of performance, we measured how per-sample scores correlate with pretraining compute"). However, the relevant notion of predictability in the scaling literature is the ability to extrapolate a fitted functional form forward to unseen compute budgets. A metric could have high rank correlation with compute but still be impossible to extrapolate (if the relationship is not well-approximated by a simple parametric family), or could have lower correlation and still be extrapolatable (with a suitable functional form capturing saturation). The paper acknowledges it does not perform backtesting (Direction 2, lines 229–232), but never bridges the gap between the correlation evidence and the title's question about *prediction*. This weakens the paper's central empirical argument: the correlation degradation is real, but its practical importance for prediction is asserted rather than demonstrated.

2. **The paper does not directly test whether incorrect-choice probabilities themselves are predictable with scale — a stated premise of the claimed mechanism.** The paper identifies that downstream metrics depend on $p_{\theta}^{\text{Vocab}}(\text{Incorrect Choice})$ for each incorrect choice, and argues that these fluctuate with scale. However, the only analysis of incorrect-choice probabilities is Figure 5, which shows how $p_{\theta}^{\text{Vocab}}(\text{incorrect})$ co-varies with $p_{\theta}^{\text{Vocab}}(\text{correct})$ across compute, colored by compute level — not how $p_{\theta}^{\text{Vocab}}(\text{incorrect})$ directly correlates with compute. Computing per-sample correlations between each incorrect choice's probability and compute would directly test whether the premises of the mechanism actually hold. Without this, the mechanism is asserted rather than fully demonstrated. (The paper's Section 5 concludes by noting this is left to future work, which is honest but leaves a gap in the present contribution.)

### Minor

3. **Limited compute points per model family (7–13) with no uncertainty quantification on correlation estimates.** Per-sample Spearman correlations over 7–13 points have wide confidence intervals. While the consistent pattern across families and benchmarks makes it unlikely that the observed ordering is entirely spurious, the paper does not report any measure of uncertainty (e.g., bootstrapped intervals or significance tests). Given that the argument rests heavily on distribution shifts of correlations, this omission reduces confidence in the quantitative precision of the findings.

4. **Title is broader than the paper's actual scope.** The title asks about "predicting downstream capabilities of frontier AI models" but the paper studies only log-likelihood-based multiple-choice benchmarks. The abstract and body scope the work to multiple-choice QA, and the limitations are clearly stated (Direction 1). Nevertheless, the title overclaims and should be narrowed to reflect the paper's actual contribution.

### Trivial

None.

## Nice-to-Haves

- **Test whether incorrect-choice probabilities correlate with compute.** This would be the most impactful addition: computing per-sample correlation between $p_{\theta}^{\text{Vocab}}(\text{Incorrect Choice}_i)$ and compute for each incorrect choice would directly verify a premise of the mechanism and fits naturally within the existing methodology.

- **Demonstrate the connection to extrapolation for a single case.** Fitting a standard parametric scaling law to log-likelihoods, then using it to predict $p_{\theta}^{\text{Vocab}}(\text{Correct Choice})$ and $p_{\theta}^{\text{Choices}}(\text{Correct Choice})$ at the largest compute point, would directly tie the observed correlation degradation to practical prediction difficulty.

- **Analyze whether the degradation varies with the number of answer choices.** The mechanism predicts that benchmarks with more choices should exhibit worse predictability (more incorrect choices to fluctuate). A breakdown by number of choices would strengthen the causal argument.

- **Soften or caveat Takeaway #3** (recommending $p_{\theta}^{\text{Vocab}}(\text{Correct Choice})$ as a scaling-predictable metric). The paper shows this metric has high correlation with compute, but does not test whether it actually extrapolates well. The recommendation is premature without validation.

- **Better situate the contribution relative to prior work on metric artifacts** (e.g., Schaeffer et al., Hu et al., who show that emergent abilities can arise from metric choice). The paper cites this work but does not clarify whether the current finding is a restatement, a deeper mechanistic explanation, or a distinct factor.

## Removed Points

These points were considered but removed for the following reasons:

- **Criticism about the paper not engaging with "metrics as the culprit" work at sufficient depth** — The paper does cite Schaeffer et al. and Hu et al. (line 23). Per the guidelines, demanding deeper engagement with specific related work risks scope creep; moved to Nice-to-Haves as a suggestion rather than a weakness.

- **"The paper should quantify how much variance in $p_{\theta}^{\text{Choices}}$ is explained by $p_{\theta}^{\text{Vocab}}$ alone"** — This is a reasonable extension but not a weakness of the current analysis. It is reframed as a Nice-to-Have.

- **Any complaint about the appendix/related work being relegated to the appendix** — Parser-stripped content; the original submission contains these sections.

## Novel Insights

The most interesting insight that emerges from synthesizing the reviews is that the paper's core contribution is structural and diagnostic rather than predictive: it identifies a *necessary condition* for a metric to be predictable with scale (independence from specific incorrect choices) and shows that common multiple-choice metrics violate this condition. The paper's evidence is strongest when it is descriptive (Figures 4 and 5 showing the non-deterministic mappings) and weakest when it tries to be predictive (correlation as a proxy for extrapolation). The reviews collectively suggest the paper would be better served by embracing its diagnostic framing more explicitly rather than reaching toward the prediction question in the title.

## Suggestions

1. Narrow the title to reflect the paper's actual scope, e.g., "Why Predicting Multiple-Choice QA Performance with Scale Remains Elusive: The Role of Incorrect-Choice Probability Mass."
2. Directly compute per-sample correlations between $p_{\theta}^{\text{Vocab}}(\text{Incorrect Choice})$ and compute for each incorrect choice to verify the mechanism's premise.
3. Add a small-scale extrapolation experiment (even for one family and benchmark) bridging the gap between correlation and prediction.
4. Include uncertainty estimates (bootstrapped confidence intervals) on the correlation distribution statistics.
5. Soften Takeaway #3 with a caveat that $p_{\theta}^{\text{Vocab}}(\text{Correct Choice})$ has not been validated for actual extrapolation.

## Score and Decision

**Originality:** Good — the paper identifies a specific structural factor (dependence on incorrect-choice probability mass) that is underappreciated in the scaling literature. **Importance of research question:** High — understanding why downstream metrics behave unpredictably is practically important for evaluation design. **Claims support:** Moderate — the mechanism is well-illustrated and plausible, but the central quantitative argument (correlation with compute) is not directly connected to the claimed contribution (predictability/extrapolation), and a premise of the mechanism is not tested. **Soundness:** Moderate — the experimental design is reasonable and the evidence is consistent, but the correlation-extrapolation gap and missing test of incorrect-choice predictability weaken the argument. **Clarity:** Good — the paper is well-written, the transformation pipeline is clearly explained, and the figures are effective. **Value:** The core insight about incorrect-choice dependence is valuable and worth publishing, but the paper overreaches in its title and central claim relative to the evidence.

The paper makes a real contribution: identifying and demonstrating that dependence on specific incorrect choices breaks the monotonic relationship between model scale and performance on multiple-choice metrics. The scatter plots (Figure 4) are genuinely convincing. However, two gaps are significant: (1) the paper equates correlation with predictability without connecting to actual extrapolation, and (2) it asserts a mechanism without directly testing whether its premise (incorrect-choice probabilities fluctuate unpredictably with scale) holds. These are fixable but non-trivial gaps.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>