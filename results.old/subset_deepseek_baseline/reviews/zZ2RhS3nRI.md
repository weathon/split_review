## Summary

The paper proposes MIAU (Membership Inference Attack Unlearning Score), a metric that quantifies how closely an unlearned model approximates the privacy behavior of a fully retrained model. MIAU combines three MIA comparisons (Forget vs Test, Retain vs Forget, Retain vs Test) and normalizes them between a baseline model (trained on full data) and a retrained model (trained without the forget set), producing a bounded score from 0 to 100. The metric is intended as an offline auditing benchmark to select the most suitable unlearning method for a given model–dataset pair, avoiding retraining during deployment.

## Strengths

- **Clear motivation and problem identification.** The paper correctly identifies that existing MIA-based unlearning evaluations are often incomplete—relying on a single comparison and lacking proper baselines. The need for a more structured, interpretable metric is well argued.
- **Systematic integration of three MIA perspectives.** Combining Forget vs Test, Retain vs Forget, and Retain vs Test into a single score is a sensible way to capture different aspects of forgetting (residual memorization, removal effectiveness, generalization stability) and to rule out confounders like global degradation.
- **Extensive experimental setup.** The evaluation covers four datasets (MNIST, CIFAR-10, CIFAR-20, MUCAC), three architectures (ResNet-18, All-CNN, ViT), and four unlearning methods (Fine-tune, SSD, Amnesiac, Teacher), with multiple random seeds and statistical tests. This provides a broad view of the metric’s behavior.

## Weaknesses

### Fatal

- **The metric does not reliably reflect gradual forgetting, which is a core requirement for any unlearning evaluation metric.** The paper’s own gradual unlearning experiments (Figure 3, Figure 4, and the associated p-value heatmap) show that MIAU does not consistently increase as more of the forget set is preserved in retraining. For several dataset–architecture combinations, the expected monotonic progression (MIAU_25 < MIAU_50 < MIAU_75 < MIAU_full) fails, and many pairwise comparisons are not statistically significant (p > 0.05). This directly undermines the claim that MIAU “faithfully captures the extent of forgetting” and calls into question its practical utility as a reliable measure of unlearning quality.

### Major

- **High variance and instability across seeds.** The reported MIAU scores often have very large standard deviations (e.g., Table 1: Amnesiac 40.08 ± 23.37, Teacher 38.36 ± 20.35). Such high variance means that a single MIAU score is not a stable indicator; the ranking of methods could change substantially across runs. This limits the metric’s usefulness for method selection in practice.
- **The logistic transformation and the choice of α=13.8 are not convincingly justified.** The derivation in Appendix A.1 (not fully visible in the extracted text) is referenced but not explained in the main paper. The sensitivity of MIAU to this parameter is not explored, and the claim that α=13.8 ensures baseline ≈ 0 and retrain ≈ 100 is not empirically verified across all settings. The transformation also introduces a nonlinear mapping that may obscure meaningful differences in gap closure.
- **The metric inherits all limitations of the underlying MIA attacks.** The paper acknowledges that MIAs can be insensitive for well-generalized models and unstable across seeds, but these limitations are not addressed or mitigated in the MIAU formulation. The metric is only as good as the attack, and the paper’s own evidence shows that the attack itself is often unreliable.

### Minor

- The paper uses a simple logistic regression attack on softmax outputs. More sophisticated attacks (e.g., loss-based, gradient-based) might yield different results, and the sensitivity of MIAU to attack choice is not studied.
- The equal weighting (β=γ=δ=1/3) is a reasonable default, but the paper does not explore how different weightings affect the metric’s behavior or whether the optimal weighting is dataset-dependent.

### Trivial

- The paper states “Retain vs Forget” twice in the attack training protocol description (Section 5), which appears to be a minor copy-paste error.

## Nice-to-Haves

- A sensitivity analysis of MIAU to the choice of α and to the weighting coefficients would strengthen the paper.
- An ablation study showing the contribution of each MIA component to the final MIAU score would help interpretability.
- Testing MIAU with stronger or more diverse MIA attacks (e.g., loss-based, LiRA) would improve confidence in the metric’s robustness.

## Novel Insights

None beyond the paper’s own contributions. The paper’s main insight—that combining three MIA comparisons and normalizing against baseline and retrain provides a more complete picture—is sensible but not surprising. The more novel finding is the empirical demonstration that MIA-based metrics, including MIAU, can be unstable and fail to reflect gradual forgetting, which is a valuable cautionary result for the community.

## Suggestions

- Address the fatal weakness by either (a) providing a modified version of MIAU that demonstrably satisfies monotonicity under gradual forgetting, or (b) clearly reframing the paper as a critical analysis of MIA-based evaluation rather than a proposed solution, and discussing the conditions under which MIAU can and cannot be trusted.
- Reduce variance by using more robust MIA attacks (e.g., ensemble of attacks) or by aggregating over multiple attack models.
- Provide a more thorough justification for the logistic transformation and the choice of α, including empirical validation across all experimental settings.

## Score and Decision

**Score:** 3  
**Decision:** Reject

The paper addresses an important problem and proposes a well-motivated metric, but the empirical validation reveals a fatal flaw: MIAU does not consistently reflect gradual forgetting, which is a fundamental property for any unlearning evaluation metric. The high variance and non-significant statistical comparisons further undermine confidence in the metric’s reliability. While the paper is honest about these limitations, the proposed solution is not sufficiently supported to warrant acceptance.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>