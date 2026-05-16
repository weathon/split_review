Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper re-evaluates two existing regularization methods for long-tailed trajectory prediction—contrastive loss (Makansi et al., 2021) and PLM re-weighting (Kozerawski et al., 2022)—on a probabilistic model (Trajectron++) using the NuScenes dataset for both pedestrian and vehicle classes. It evaluates using the KDE-NLL metric (which captures full predicted distributions rather than biased minADE/minFDE) and finds that while both methods improve pedestrian performance, neither reliably improves long-tailed vehicle prediction.

## Strengths

- **First evaluation of both pedestrian and vehicle classes in NuScenes for these methods**: As stated in the abstract and Section 4.2, prior work only reported results on one agent type. The paper provides separate quantitative results (Tables 1–4) for both categories, revealing that the methods do not reliably transfer to vehicles. This is a non-trivial negative finding that contradicts the implied generality of the original works.

- **Use of KDE-NLL metric to compare full trajectory distributions instead of biased minADE/minFDE**: Section 4.1 provides a clear motivation for using KDE-NLL over minADE/minFDE, which ignore likelihoods and are biased. This directly addresses the gap identified in the abstract and is the right evaluation choice for a probabilistic model like Trajectron++.

- **Demonstrates that PLM re-weighting can degrade long-tailed vehicle performance despite improving pedestrian performance**: The paper's analysis of Table 4 (Section 4.2.2) shows that PLM performs worse than the baseline on long-tail KDE metrics for vehicles, even while its most-likely FDE looks good. The paper correctly identifies that this is likely due to PLM collapsing to a "mean" trajectory rather than predicting a diverse multi-modal distribution—an insightful diagnosis.

- **Qualitative analysis linking model behavior to metric differences**: Section 4.3 and Figure 3 provide concrete examples showing that the contrastive model often produces higher-variance (more diverse) predictions than the PLM model, which tends to predict a "mean" trajectory. This connects the quantitative findings to model behavior and supports the diversity-collapse hypothesis for PLM on vehicles.

## Weaknesses

### Fatal

None.

### Major

- **Potentially incorrect claim about vehicle average KDE (Section 4.2.2)**: The paper states "Both long-tail techniques improve average performance by improving nonlong-tailed predictions" for vehicles. According to the Harsh Critic's reading of Table 4, the PLM method's *average* KDE for vehicles at 3s is worse than the baseline (-1.9 vs -2.2; note: more negative is better for KDE-NLL). If this reading is accurate, the claim that PLM improves average performance is factually wrong. While the paper's core conclusion (neither method is effective for vehicles) remains valid, this error in interpreting the paper's own results undermines trust in the analysis. The paper should correct this statement to only claim that non-long-tailed predictions improve (based on Figures 2c/2d showing more examples with KDE < 5) while noting that the average is pulled down by worsened long-tail examples.

### Minor

- **Missing ablation study (promised but absent)**: Line 91 states "we also perform an ablation study to see how applying more or less regularization might affect the model," but no ablation results appear anywhere in the paper. Since both methods use default hyperparameters from their original papers (tuned for a different base model and, for Makansi et al., a different dataset), the absence of this ablation leaves the vehicle results open to the question of whether different regularization strengths would change the conclusions. The default-parameters choice is defensible as a "portability test," but the promised-but-unreported ablation is a gap in the paper's own stated methodology.

- **No statistical significance or confidence intervals**: The reported performance differences between methods are modest (especially for pedestrians, and when comparing contrastive vs baseline on vehicles). Without confidence intervals or significance tests, it is difficult to assess whether the observed differences are reliable or within the noise of a single run.

- **Total loss function not explicitly specified**: The paper describes the CVAE architecture and states that the regularization terms are added (Figure 1), but does not give the overall loss equation (e.g., ℒ_total = ℒ_CVAE + λ·ℒ_contrastive or ℒ_PLM). The weighting between the CVAE loss and the regularization term is not stated. This weakens reproducibility.

- **Metric equivalence claim relies solely on a citation without explanation**: Section 4.1.1 states that the difficulty-score metric (Makansi et al.) and percentile metric (Kozerawski et al.) are equivalent "as shown by Thuremella & Kunze (2023b)." A brief explanation of why they are equivalent (e.g., a monotonic mapping between difficulty scores and error percentiles) would make the evaluation framework more self-contained and rigorous. As written, the reader must take the equivalence on faith.

### Trivial

None.

## Nice-to-Haves

- Add a quantification of prediction diversity (e.g., average prediction variance or number of distinct modes) to support the qualitative claim that PLM collapses to a "mean" trajectory for vehicles. This would strengthen the diagnosis in Section 4.2.2.
- Report training stability or convergence behavior—whether the regularizers affected the number of epochs needed or introduced training instability.
- The distinction between the regularization term and kurtosis term in Kozerawski et al. is already briefly explained at line 87, so no additional clarification is needed there.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The distinction between the two terms [regularization vs kurtosis] is not explained"** — Removed because the paper does explain this at line 87, stating the regularization term "improves performance slightly in average and rare cases" while the kurtosis term "significantly improves only the worst error."
2. **Various formatting/style nitpicks** — Removed per instructions as parser artifacts.
3. **Criticisms that question the existence/release status of cited works** — None were present in the original review; the Harsh Critic's review is clean on this front.
4. **The Harsh Critic's claim that "the paper should be rejected without changes" is softened** — The reviewer's own language recommends major revisions, not outright rejection, so no adjustment needed.

## Novel Insights

None beyond the paper's own contributions. The key insight—that long-tail regularization methods which work for pedestrians do not transfer to vehicles, likely because PLM collapses multi-modal distributions to a "mean" trajectory—is the paper's own finding and is well-supported by the evidence presented.

## Suggestions

1. **Correct the factual error** in Section 4.2.2 regarding PLM's average KDE for vehicles. If PLM does not improve average KDE, revise the text to say only that non-long-tailed vehicle predictions improve (based on histogram evidence), while average KDE is degraded by worsened long-tail performance.
2. **Report the ablation study** promised in Section 3.2.2. Even a brief paragraph showing a sweep over regularization weight for one condition would address the main threat to validity.
3. **Add confidence intervals** (e.g., bootstrapped) or report multiple seeds for the main experiments, particularly given the modest performance differences.
4. **Specify the total loss function** explicitly: ℒ_total = ℒ_CVAE + λ·ℒ_reg, with the value of λ.
5. **Briefly explain the metric equivalence** in Section 4.1.1. A single sentence describing the monotonic relationship between difficulty scores and error percentiles would suffice.

## Score and Decision

The paper addresses a well-motivated and under-explored question: whether long-tail regularization methods for trajectory prediction transfer to a probabilistic model and to multiple agent types. The choice of KDE-NLL as the evaluation metric is sound, and the finding that neither method works reliably for vehicles is a genuine contribution. However, the paper is weakened by a factual error in interpreting its own vehicle results (claiming PLM improves average KDE when the data appear to show the opposite), a promised-but-missing ablation study, and the absence of statistical significance testing. These issues are fixable but reduce the paper's credibility in its current form. The core contributions are real, but the presentational and evidential gaps prevent a confident acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>