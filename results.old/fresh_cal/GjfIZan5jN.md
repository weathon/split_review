Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes the Inherent Interpretability Score (IIS), a metric that quantifies representation interpretability by measuring the area under the curve of sparsity ratio vs. accuracy retention rate when predicting through sparse concept-based interpretations. Using IIS, the paper investigates the relationship between interpretability and classifiability in pre-trained vision representations across 12 model architectures, 4 datasets, and 4 concept library types. The central discovery is a consistent positive correlation between interpretability and classifiability, challenging the common assumption of an inherent conflict. Two applications are demonstrated: using interpretability maximization as a fine-tuning objective to improve classifiability, and using high-classifiability representations to produce interpretable predictions with accuracy competitive with or exceeding that of inherently interpretable models.

## Strengths

1. **Novel, annotation-free interpretability metric (IIS).** Unlike prior metrics that rely on human expectations (Bau et al., 2017) or ground-truth labels (Zarlenga et al., 2022), IIS measures interpretability automatically via the ability of a representation to retain accuracy when predictions are forced through sparse concept projections (Equation 7, area under the sparsity–ARR curve). This is a principled quantitative alternative.

2. **Discovery of a positive correlation between interpretability and classifiability, contradicting a widely assumed trade-off.** The paper systematically shows across four concept library types (Figure 3), four datasets (Figure 4), and 12+ models that representations with higher classification accuracy consistently achieve higher IIS. The trend is particularly clean within architecture families (ResNet, ViT). This challenges the long-held view from interpretability-oriented methods that these properties are inherently in conflict.

3. **Extensive and systematic experimental validation.** The study covers 12 pre-trained models (ResNet, ViT, ConvNeXt, Swin), four datasets (ImageNet, CUB-200, CIFAR-10, CIFAR-100), and four distinct concept library constructions (Prototype, Cluster, End2End, Text). All configurations consistently support the positive-correlation finding, lending robustness to the conclusion.

4. **Factor-level analysis connecting sparsity, ARR, and accuracy.** Section 3.3 dissects IIS into its constituent factors and shows that higher-accuracy representations maintain higher ARR at sparser interpretations (Figure 7). This provides mechanistic insight into why the positive correlation holds—better representations lose less task-relevant semantics when interpreted sparsely.

## Weaknesses

### Fatal
None.

### Major

1. **The causal direction in the "mutual promoting" claim is not isolated from alternative explanations.** The paper claims "improving interpretability can further improve classifiability" based on the fine-tuning experiment (Section 4.1). However, the fine-tuning objective (Equation 8) adds a cross-entropy loss on a sparsified concept subspace, and the paper itself describes the effect as "the regularization effect induced by the second terms" (line 179). The improvement (0.3–0.6 pp in Table 1) could be driven by general regularization rather than increased interpretability per se. No control experiment with an alternative regularization (e.g., dropout, weight decay, or feature-level noise) is run to attribute the gain specifically to interpretability. This does not invalidate the core correlational discovery, but the causal claim is not adequately supported as presented.

2. **The IIS metric's partial dependence on accuracy is not fully disentangled.** ARR = Acc(interpretation) / Acc(original). When Acc(original) is low (e.g., small or poorly trained models), the denominator is small and ARR can be inflated purely mechanically. The paper acknowledges this for early training phases (line 123) and provides a qualitative demonstration that models with similar accuracy can have different IIS (e.g., ViT-B vs. Swin-T in Figure 3), suggesting IIS captures something beyond accuracy. However, this demonstration is limited to a few points; a systematic residual analysis (e.g., regressing IIS on accuracy and examining residuals) or a formal decorrelation would significantly strengthen the evidence that the observed correlation is not a metric artifact.

### Minor

3. **Accuracy numbers are reported without error bars.** Tables 1–5 report point estimates of accuracy without standard deviations or confidence intervals. Given that the reported improvements in Section 4.1 are small (0.3–0.6 pp), the reader cannot assess whether these gains are statistically significant. Error bars would substantially improve the reliability of the claims.

4. **Reproducibility gaps in implementation details.** Several details needed to reproduce the experiments are missing: (a) the "pre-defined clustering methods" used for visual concept aggregation (Section 2.1) are not specified by name or hyperparameters; (b) the number of sparsity ratios evaluated and the training hyperparameters (learning rate, optimizer, epochs) for the linear classifiers $g_{cls}$ are not stated; (c) training details for the fine-tuning step in Section 4.1 are not provided. These gaps hinder reproducibility and should be addressed.

5. **No explicit discussion of IIS's limitations.** The paper does not include a limitations section. Important caveats—such as the metric's sensitivity to concept library quality, the impact of concept library size on cross-dataset IIS comparisons, and the reliance on the quality of the CLIP vision-language model for textual concept vectors—are not discussed.

6. **Comparison in Section 4.2 could be complemented by post-hoc baselines.** The paper compares interpretable predictions from pre-trained representations against inherently interpretable models trained from scratch (ECBM, etc.). While the paper is transparent about the training-cost asymmetry (only a linear classifier is trained for the proposed method vs. full-model training for baselines), the comparison would be more informative if it also included post-hoc concept-based interpretation methods (e.g., TCAV, post-hoc Concept Bottleneck) to establish the relative quality of the sparse concept interpretations within the same methodological family.

### Trivial
None.

## Nice-to-Haves

- **Residual analysis for IIS vs. accuracy.** A formal analysis regressing IIS on accuracy and examining whether the correlation holds on residuals would definitively address the metric confound concern.
- **Human evaluation.** A small-scale user study asking humans to judge whether sparse concept explanations from high-IIS models are more understandable than those from low-IIS models would strengthen the claim that IIS corresponds to human-perceived interpretability.
- **Analysis of when the correlation breaks.** The observation that models with similar accuracy can have different IIS (e.g., ViT-B vs. Swin-T) is interesting and merits deeper investigation into what architectural properties affect IIS beyond accuracy.
- **Error bars on all quantitative results.** Standard deviations across multiple runs or seeds for Tables 1–5.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about "differentiable alternatives" for sparsification.** The reviewer suggests mentioning differentiable alternatives to hard thresholding. This is a speculative preference, not a weakness of the current approach. **Reason:** Speculative/personal preference, not a specific flaw in the paper.
- **Criticism that the comparison in Section 4.2 is "unfair" / "staged."** The asymmetry in training cost favors the baselines (they train the full model; the proposed method trains only a linear classifier), and the paper is transparent about this. Per the filtering rules, criticisms about unfair comparison should be removed when the asymmetry favors the baseline. **Reason:** Asymmetry favors baselines, paper is transparent.
- **Criticism about missing appendix content or references.** The parser strips appendix sections; the original submission contains them. **Reason:** Parser artifact.
- **Criticism about "pure formatting/style nitpicks" and "grammar/spelling."** These are parser artifacts, not author errors. **Reason:** Parser artifact.
- **Criticism about "not yet released" models/tools.** The paper cites existing published methods and models. **Reason:** Violates hard rule about assuming cited entities exist.
- **"Could the metric be measuring a proxy?" type speculation.** The reviewer poses this as a general concern without specific evidence in the paper. **Reason:** Unanchored speculation.
- **Various generic weaknesses** such as "evaluation lacks rigor" without specific anchor. **Reason:** Lacks concrete anchor in the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's main strengths (novel metric, extensive correlation evidence) and its main limitations (causal claim not fully isolated, metric confound partially addressed, missing error bars). The most interesting observation from the synthesis is that the paper's factor-level analysis (Section 3.3) is actually its strongest piece of evidence—it shows the mechanism *why* higher-accuracy representations are more interpretable (they maintain higher ARR even at sparser interpretations)—but this is somewhat buried between the correlational discovery and the application sections.

## Suggestions

1. **Reframe the "mutual promoting" claim** as an empirical observation of positive correlation + suggestive evidence that IIS-regularized fine-tuning further improves accuracy, rather than a proven causal relationship. Drop the language implying proven causality unless controls (e.g., alternative regularizations) are added.

2. **Add a formal residual analysis** to demonstrate that the positive correlation between IIS and accuracy holds after controlling for accuracy itself. This would address the metric confound concern definitively.

3. **Report standard deviations or confidence intervals** on all accuracy tables (Tables 1–5). The improvements in Section 4.1 are small; error bars are essential for interpretation.

4. **Provide complete implementation details** in the appendix or supplement: clustering algorithm and hyperparameters for visual concepts, number of sparsity ratios evaluated, optimizer, learning rate, and training epochs for all linear classifiers and fine-tuning experiments.

5. **Add a limitations subsection** discussing IIS's dependence on concept library quality, the sensitivity to concept library size, and potential failure modes of the metric.

6. **Expand the comparison in Section 4.2** by including post-hoc concept-based interpretation methods (e.g., applying TCAV or Concept Bottleneck to pre-trained features) to better situate the approach within its own methodological family.

## Score and Decision

The paper makes a genuine contribution: a novel, practical metric for representation interpretability and a well-supported empirical discovery that contradicts a long-held assumption. The weaknesses are evidential and presentational, not structural—they do not undermine the core findings. The main claims (IIS as a metric, positive correlation) are well-supported; only the stronger causal interpretation needs reframing. With the suggested revisions, this would be a solid contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>