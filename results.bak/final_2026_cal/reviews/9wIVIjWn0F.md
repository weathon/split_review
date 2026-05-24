Now I'll write the final consolidated review.

## Summary

This paper proposes RTA (Regression-based Test-Time Adaptation), which replaces the standard entropy-based view selection in TTA for CLIP with a learned regression mapping. The key insight is that true label cross-entropy loss (LCE) is a far superior signal for selecting confident augmented views than entropy, as shown by a compelling ceiling analysis (Tables 1-2). The method trains a lightweight LightGBM decision tree on pseudo-labeled ImageNet validation data to predict cross-entropy loss from logits, then selects views with the smallest predicted loss at test time. Experiments on ImageNet variants, 10 cross-domain datasets, and multi-label benchmarks show consistent improvements over existing entropy-based TTA methods.

## Strengths

- **Ceiling TTA analysis revealing the potential of loss-based view selection (Tables 1-2).** The paper convincingly demonstrates that using ground-truth label cross-entropy loss (LCE) for view selection yields enormous gains over entropy-based selection (SE). For ViT-B/16 with 64 views, LCE achieves 90.2% on ImageNet-A vs. SE's 64.3% — a 25.9-point gap. This quantitative evidence is the strongest contribution of the paper and provides clear motivation for the regression approach.

- **Consistent SOTA results across multiple benchmarks (Tables 3-6).** RTA outperforms existing TTA methods (Zero, BCA, ML-TTA, etc.) on ImageNet variants, cross-domain datasets, and multi-label classification. For instance, on multi-label MSCOCO with RN50, RTA achieves 53.25% mAP vs. the next best 51.58% (ML-TTA). These results suggest genuine practical value.

- **Computational efficiency with lightweight one-time training.** The use of a small LightGBM model (max depth 5, 16 leaves, trained on 1,000 samples for 100 rounds) means the regressor adds negligible overhead at test time. The method requires no per-instance backpropagation or online parameter updates, making it practical for deployment.

- **Novel perspective on view selection.** Replacing entropy (which is computed from the current instance's probability distribution alone) with a regression model trained on diverse data is a conceptually interesting departure from the dominant TTA paradigm. The t-SNE visualization (Figure 2) and Spearman correlation analysis (Figure 3) provide supporting evidence that a learnable logit-to-loss mapping exists.

## Weaknesses

### Major

- **The paper does not explain how the regression model handles test datasets with different numbers of classes (logit dimensionality mismatch).** The regression model is trained on logit vectors from ImageNet's 1000 classes (L=1000). At test time, for ImageNet and its variants (IN-1k, IN-A, IN-V2, IN-R, IN-S) the logit dimensionality is also 1000, so there is no issue there. However, for cross-domain datasets (e.g., Pets with 37 classes, Aircraft with 100 classes, DTD with 47 textures) and multi-label datasets (e.g., MSCOCO with 80 labels), the logit dimensionality differs from 1000. The paper states "the TTA process follows the settings of Zero and ML-TTA" which use dataset-specific class prompts. Neither the main text nor the algorithms explain how a regression model trained on 1000-dimensional inputs can process inputs of different dimensionality. This is not a speculative concern — it follows unambiguously from the paper's own description. The cross-domain (Table 4) and multi-label (Tables 5-6) results cannot be verified without this explanation. This is the single most critical issue in the paper.

- **The regression model is trained exclusively on high-confidence predictions (CLIP confidence ≥ 0.8) from a single source distribution (ImageNet), but the paper claims adaptation to "arbitrary test distributions."** The training data is constructed by filtering 5,000 ImageNet validation samples to those with CLIP confidence ≥ 0.8, then sampling 1,000 from those. This means the regressor learns only from examples where CLIP is already confident on ImageNet-like data. The paper's motivation (§1) emphasizes that existing TTA methods "struggle to estimate reliable entropy for outliers," yet the regressor's training data explicitly excludes the uncertain or out-of-distribution examples that constitute "outliers." The cross-domain experiments in Table 4 are all natural-image classification datasets (not medical images, satellite imagery, or genuinely novel class taxonomies), so the "arbitrary distributions" claim is overstated relative to the evidence.

- **No validation of the core assumption: that the regressor's predicted loss correlates with true label loss on test instances.** The ceiling experiment (Tables 1-2) uses ground-truth labels and establishes that LCE is a powerful selection signal. However, the actual method replaces LCE with a regressor trained to predict *pseudo-label* cross-entropy loss from CLIP's own high-confidence predictions. The paper never directly measures whether the regressor's predictions correlate with true LCE on held-out test views from any domain. The t-SNE visualization (Figure 2) and Spearman analysis (Figure 3) show structural relationships between logits and *true* loss, but these use ground-truth labels, not the pseudo-label loss the regressor is trained on. Without this validation, it is unclear whether the method's gains come from approximating LCE (as claimed) or from exploiting a different signal.

### Minor

- **Missing baseline: max-softmax-probability view selection.** The simplest alternative for view selection is to pick the top-*k* views with the highest maximum softmax probability (max-prob). The paper compares against entropy-based methods but not max-prob. Since the pseudo-label generation in RTA already uses a CLIP confidence threshold (≥ 0.8), a comparison to max-prob view selection would directly test whether the learned regression adds value beyond CLIP's own confidence signal. Without this, the claim that the regression relationship is the key driver of improvement is not fully substantiated.

- **Limited analysis of the regressor's internal behavior.** The training uses 1,000 samples with up to 1,000 features (logit dimensions). While LightGBM with max_depth=5 and 16 leaves is heavily regularized, the paper reports no held-out validation metrics for the regressor (e.g., R², Spearman ρ between predicted and true pseudo-loss, or cross-validation error). Figure 5 only shows downstream accuracy as a function of training data size, not regressor quality.

- **The confidence threshold (0.8) controlling training data quality is not ablated.** The threshold determines the size and quality of the pseudo-labeled training set. A different threshold would change training data quantity and pseudo-label accuracy, but its impact on downstream performance is not explored.

- **Scope of "one-time training on diverse data" claim.** The claim that regression training data is "diverse" and "independent of downstream tasks" is partially contradicted by the use of ImageVal-12k — a single dataset with a fixed 1000-class ImageNet label space. While the method generalizes to cross-domain datasets in practice, the training data is not particularly diverse in terms of label taxonomy or visual domain variation.

### Trivial

- Algorithm 1 uses the notation $\mathbf{y}^{\text{reg}}$ for labels without explicitly stating these are pseudo-labels from CLIP (though this is clarified in the text).
- "ImageVal-12k" is not formally defined; it likely refers to the ImageNet validation set (~12k images).

## Nice-to-Haves

- A direct correlation analysis (Spearman ρ or R²) between the regressor's predicted loss and the true label loss on held-out test views from multiple domains would strongly validate the method's core assumption.
- Testing on genuinely out-of-distribution scenarios (medical images, satellite imagery, or datasets with completely different class taxonomies) would better support the "arbitrary distributions" claim.
- An analysis of the regressor's failure cases — when does RTA select the wrong views and how do these differ from entropy-based selection errors?

## Removed Points

These points are flagged to be removed; treat them with caution:
- **Criticism about regressor overfitting (1000 samples × 1000 features):** Removed because LightGBM with max_depth=5 and max_leaves=16 is heavily regularized — 16 leaf values cannot overfit 1000 features to a meaningful degree. This criticism does not account for the strong regularization constraints stated in the paper.
- **"Training data is not independent of downstream tasks because it uses ImageNet class set":** Partially removed because this conflates the label space with the task. The regression model predicts loss scalar from logits regardless of what the labels mean, so the same training can apply to different downstream class sets *if the dimensionality issue is resolved* — which is a separate problem noted above.
- **Claim that Spearman correlation analysis in Figure 3 is per-instance and hard to interpret:** Removed because per-instance analysis is exactly the right granularity for a per-instance view selection task, and the figure's presentation is standard.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the dimensionality mismatch as the central concern but do not add an independent analytical perspective beyond what reading the paper reveals.

## Suggestions

1. **Clarify the dimensionality handling.** State explicitly how the regression model (trained on 1000-dim ImageNet logits) is applied to test datasets with different class counts. If the same 1000 ImageNet class prompts are used for all datasets even during TTA (so logits are always 1000-dim), state this and discuss how a 1000-class view selection signal can work for a 37-class downstream task. If the regressor is applied per-dataset with its class-specific logit dimensionality, explain how this is done (e.g., training per-dataset regressors, or using dimension-agnostic features such as only the top-*k* logits/softmax values).

2. **Validate the regressor directly.** Report the Spearman correlation or R² between the regressor's predicted loss and (a) the pseudo-label loss on held-out samples and (b) the true label loss on a small labeled set from one or two test distributions. This would close the gap between the ceiling experiment and the actual method.

3. **Include the max-softmax-probability baseline** for view selection to isolate whether the learned regression adds value beyond CLIP's own confidence.

4. **Tone down the "arbitrary distributions" claim** or expand experiments to include test distributions beyond natural image classification (e.g., medical, satellite, sketch).

## Score and Decision

**Calibration details:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| S90g7NE88b (FGA) | 5.00 | R1-middle | Stronger theory, comparable experiments, no dimensionality gap |
| dHj8hC081K (ADTE) | 4.50 | R1-middle | Clearer presentation, less novel idea, fully specified method |
| CLUvRxQXtf (CLIP-TTA) | 4.67 | R1-middle | More complete experiments but incremental; similar scope |
| DxGPQECIJB (D-TPT) | 4.50 | R2 | Well-executed but incremental; RTA more novel but has serious gap |
| HeGMugkCOH (C-TTA) | 3.00 | R1-low | Weak method, poor results; RTA clearly stronger in results |
| vJV22Ig8YG (TE-VLM) | 3.00 | R1-low | Distillation paper, not directly comparable |

**Round-1 bracket:** 3.0 – 5.5  
**Round-2 narrowing:** Compared against ADTE (4.50, Accept), CLIP-TTA (4.67, Reject), D-TPT (4.50, Reject), and FGA (5.00, Accept). RTA has a more novel core idea than ADTE/CLIP-TTA/D-TPT but suffers from an unaddressed methodological gap (logit dimensionality handling) that prevents verification of a significant fraction of the experimental results. It is clearly stronger than the ~3.0 withdrawn papers. The gap in the paper is more severe than the weaknesses of the accepted-poster anchors.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>