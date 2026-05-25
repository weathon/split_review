I now have enough information to write the consolidated review. Let me synthesize my findings.

---

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA), a method that trains a lightweight regression model (LightGBM) on pseudo-labeled diverse data to predict the cross-entropy loss of augmented views from their logit vectors. At test time, views with the lowest predicted loss are selected for ensembling. The key insight is that the true label cross-entropy loss is a much better view-selection criterion than entropy (as shown in ceiling experiments), and the paper attempts to approximate this using a learned regression mapping. Results are reported on ImageNet variants, cross-domain, and multi-label benchmarks.

## Strengths

1. **Empirical discovery of the ceiling TTA performance.** Tables 1-2 convincingly demonstrate that using true label cross-entropy loss for view selection dramatically outperforms entropy-based selection (e.g., ViT-B/16 on ImageNet-A: 90.2% with LCE vs. 64.3% with SE at 64 views). This is a striking finding and provides strong motivation for learning a regression mapping.

2. **Consistent improvements on ImageNet-variant benchmarks.** On ImageNet-1k, ImageNet-A, ImageNet-V2, ImageNet-R, and ImageNet-K (Table 3), RTA consistently outperforms prior TTA methods. For RN50, RTA achieves 49.24% OOD average vs. the next best 46.98%, and for ViT-B/16, 65.84% vs. 65.03%. These results are clean because all datasets share the same 1000-class space as the training data.

3. **Single offline training with negligible test-time cost.** The regression model is trained once on 1,000 samples from ImageVal-12k and applied without any per-instance updates. This contrasts with prior TTA methods that require per-instance tuning or cache maintenance. The LightGBM model is lightweight (max depth 5, 16 leaves) and adds minimal overhead.

4. **Ablation studies on design choices.** Figures 4 and 5 provide useful analysis of how performance varies with the number of augmented views and the number of regression training samples, showing saturation at practical values.

## Weaknesses

### Major

- **Undefined handling of class-count mismatch between training and test.** The regression decision tree is trained on 1000-dimensional logit vectors (from ImageNet's 1000 classes in ImageVal-12k). However, the cross-domain datasets in Table 4 have class counts ranging from 10 (EuroSAT) to 397 (SUN) and the multi-label datasets in Tables 5-6 have 20–81 labels. Algorithm 2 (lines 6–7) computes logits for *all* classes of the test dataset, which would produce vectors of dimension *L<sub>test</sub>* for datasets with other class counts. The paper never specifies how a regression model expecting 1000-dimensional inputs can process vectors of other sizes. This makes the cross-domain and multi-label experiments impossible to verify as reported, and these constitute the majority of the evaluation (13 of 18 total datasets). If the method uses ImageNet-class prompts for all datasets, this must be explicitly stated and the evaluation procedure justified.

- **Missing comparison against the trivial baseline: direct confidence-based selection.** The regression target ℒ<sub>CE</sub>(ŷ|s) = –log(max(softmax(s))) is a deterministic function of the logit vector that can be computed in closed form with a trivial operation. Training a LightGBM model to approximate this function adds approximation error and strays from the exact computation. The paper does not include any baseline that selects views by smallest –log(p<sub>max</sub>) (i.e., highest max-probability). Without this comparison, it is impossible to attribute the reported gains to the learned regression mapping rather than to the simple fact that max-probability is a different selection criterion than entropy. Tables 3–6 should include a row with direct max-probability selection under the same 64-view, 10% selection setup.

- **Multi-label adaptation is not described.** The method is defined entirely in terms of single-label cross-entropy loss (Eq. 4, Eq. 7, Algorithm 1). The paper evaluates on MS-COCO, VOC2007, and NUS-WIDE (Tables 5-6) but provides no description of: (a) how the regression loss target is defined for multi-label data (where binary cross-entropy or multi-label softmax would be required), (b) how pseudo-labels are assigned in the multi-label setting, or (c) how the regression tree (trained on single-label ImageNet data with 1000 classes) is applied to multi-label datasets with different label spaces. Without this specification, the multi-label results cannot be interpreted.

### Minor

- **Gap between ceiling and actual performance is not analyzed.** Tables 1-2 show huge improvements when using true labels (e.g., 89.0% on ImageNet with ViT-B/16 for LCE vs. 70.6% for SE at 64 views), but RTA achieves only 71.13% on ImageNet (Table 3). The paper conflates what is ideally possible with what is actually achieved, and does not analyze why the gap is so large or how pseudo-label noise contributes to it.

- **No analysis of pseudo-label quality.** The regression model is trained on samples with confidence ≥ 0.8, but the paper does not report how often these pseudo-labels are correct, how mistakes affect the regression targets, or how the 0.8 threshold was chosen. A sweep over thresholds (e.g., 0.7, 0.9, 0.95) would clarify sensitivity to this hyperparameter.

- **ImageVal-12k dataset is not defined.** The paper uses "ImageVal-12k" as the regression data source but does not specify its exact composition, size, or how it relates to the standard ImageNet validation set. This makes it difficult to assess the diversity of the training data.

### Trivial

- **Notation inconsistency in Eq. (8).** The test-time equation uses the superscript "reg" (regression set notation) when it should refer to test views, creating minor confusion.

## Nice-to-Haves

- Include a direct confidence-based selection baseline (smallest –log(p<sub>max</sub>)) in all main tables.
- Report Spearman's ρ between regression predictions and true label loss on a held-out labeled set to demonstrate that the learned mapping correlates with the true loss under distribution shift.
- Analyze pseudo-label accuracy on a labeled reference set to quantify the noise in the regression targets.
- Ablate the confidence threshold used for pseudo-label filtering.

## Removed Points

These points from the reviewers were considered but removed from the main weaknesses with justification:

- *"The ceiling experiments are misleading because they use true labels."* — The paper clearly and explicitly states that the ceiling results use true labels (Section 4.1: "using true labels"). This is not misleading; it is a stated upper bound.

- *"The t-SNE visualization does not demonstrate that a regression model trained on pseudo-labels can capture the correlation."* — This is a fair observation but applies to any visualization; the t-SNE is presented as supporting evidence alongside Spearman correlation, not as definitive proof. Demoting to a minor observation.

- *"The predicted loss may not be a reliable proxy under distribution shift."* — This is speculative without evidence; the paper should analyze this but it is not a verifiable flaw from the paper as written.

- *General reproducibility concerns about missing appendix or supplementary material.* — Parser-stripped content; cannot be evaluated.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's and strength finder's observations surface no genuinely novel synthesis that the paper did not already articulate regarding the regression relationship between logits and loss.

## Suggestions

1. **Clarify the dimension handling.** State explicitly whether the regression model receives logits from ImageNet-class prompts (dimension 1000) for all datasets or whether another mechanism is used. If the former, describe how the final prediction maps to non-ImageNet classes. If the latter, specify the procedure in Algorithm 2 and the experimental setup.

2. **Add the direct confidence baseline.** Replace the regression model with direct computation of –log(max(softmax(s))) for view selection under the same 64-view, 10% selection setup, and include this as a row in Tables 3–6. If performance is similar, the paper should reframe its contribution around the broader framework rather than the regression model.

3. **Describe the multi-label adaptation.** Specify how the loss target, pseudo-labels, and regression model are adapted for multi-label classification. At minimum, state whether the same regression model (trained on single-label 1000-class data) is applied directly and how the logits are computed.

4. **Analyze the ceiling-to-actual gap.** On a held-out labeled set, compare the regression model's predictions to the true label loss to quantify how well the learned mapping approximates the ideal.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>