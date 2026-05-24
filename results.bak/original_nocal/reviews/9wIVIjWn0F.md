Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes RTA (Regression-based Test-time Adaptation), a method that trains a lightweight regression decision tree on pseudo-labeled data from ImageNet to predict the cross-entropy loss of augmented views for CLIP-based classification. At test time, the tree selects the top-k views with the lowest predicted loss, replacing entropy-based view selection in standard TTA pipelines. The key insight is establishing a learnable regression mapping from logits to loss that transfers across distributions. RTA achieves consistent improvements over prior TTA methods on single-label (ImageNet variants), cross-domain (10 datasets), and multi-label benchmarks for both RN50 and ViT-B/16 backbones.

## Strengths

- **Compelling Ceiling TTA finding (Tables 1 and 2):** The paper clearly demonstrates that selecting views by ground-truth label cross-entropy loss produces near-saturated accuracy (e.g., 90.2% on ImageNet-A, 94.4% on ImageNet-R with ViT-B/16, 64 views), far exceeding entropy-based selection. This finding strongly motivates the regression approach and is cleanly presented.

- **Consistent SOTA results across diverse benchmarks (Tables 3–6):** RTA outperforms prior TTA methods on single-label (e.g., +5.73% on ImageNet-A for RN50 over DiTPT), cross-domain (best average on both RN50 and ViT-B/16), and multi-label (e.g., +1.67% mAP on MSCOCO for RN50 over ML-TTA) settings. The evaluation is broad, covering 5+ single-label datasets, 10 cross-domain datasets, and 3 multi-label datasets with two backbones.

- **Lightweight and practical design:** The regression model is a shallow LightGBM tree (max depth 5, 16 leaves) trained once offline on 1,000 samples, with negligible inference overhead. Unlike online TTA methods that require per-instance optimization or dynamic memory, RTA adds no cost during adaptation beyond the tree forward pass.

- **Supporting analyses (Figures 2, 3, 4, 5):** The t-SNE visualizations show structural clustering of logits by loss value, Spearman correlations confirm statistically significant monotonic relationships, and the scaling experiments (number of views, number of regression samples) demonstrate robustness of the approach.

## Weaknesses

### Fatal
None.

### Major

- **Multi-label adaptation is underspecified (Section 4 vs. Tables 5, 6):** The method description (Section 4) defines the regression tree on single-label cross-entropy loss (Eq. 4) with ImageNet's 1000 classes. For multi-label benchmarks (MSCOCO, VOC2007, NUSWIDE), the paper states it "follow[s] ML-TTA" settings but does not specify how the regression tree — trained on 1000-class logits — is applied to multi-label datasets with different class counts (e.g., 80 for MSCOCO). The logit dimensionality mismatch between training (1000) and test-time multi-label prediction is not addressed. Without this explanation, the multi-label results cannot be fully interpreted from the paper alone. The authors should clarify whether (a) the regression tree is retrained per dataset, (b) a common logit representation is used across datasets, or (c) some other adaptation mechanism is applied.

### Minor

- **No comparison against a simple max-softmax-probability baseline:** The regression tree predicts low loss for high-confidence pseudo-labels. A baseline that simply selects views by maximum softmax probability (directly related to what the tree approximates) is not included. The comparisons are to entropy-based methods (which are related but not identical). Adding this baseline would clarify whether the regression tree adds value beyond a straightforward confidence measure. For context, the pseudo-label generation already uses a confidence threshold of 0.8, so a "select top-k by max probability" baseline is a natural control.

- **Regression model trained only on high-confidence samples (threshold ≥ 0.8):** The training data for the regression tree consists of 1,000 samples from ImageNet validation with CLIP confidence ≥ 0.8. This means the tree never sees logits corresponding to low-confidence, ambiguous samples during training. At test time, it must evaluate all augmented views — including low-confidence ones where extrapolation is required. The paper does not analyze how well the tree's predictions generalize to these unseen logit regimes. An ablation varying the training confidence threshold (e.g., 0.7, 0.9) would help establish robustness.

- **Regression model trained on original images only, not augmented views:** The paper justifies this (line 184) by noting "the original image itself can actually be regarded as a view," but augmented views can have systematically different logit distributions (e.g., lower confidence on random crops). Training on augmented views (using the same augmentation pipeline as test time) would be a cleaner design. The paper does not ablate this choice.

- **No error bars or statistical significance reported:** All results are single numbers. Given small gaps on some comparisons (e.g., 68.70 vs. 68.59 average on cross-domain for ViT-B/16), variance could affect the reported rankings. Adding standard deviations over multiple runs or bootstrap significance tests would strengthen the empirical claims.

### Trivial
None.

## Nice-to-Haves

- A scatter plot of the trained regression tree's predicted loss vs. true cross-entropy loss on OOD test sets (e.g., ImageNet-A examples) would directly validate the mapping's calibration.
- An analysis of which logit features the tree uses most frequently for splitting (feature importance from LightGBM) could reveal whether the regression relies on global confidence patterns or class-specific signals.
- A comparison of training the regression tree on augmented views vs. original images.

## Removed Points

These points from the reviewers are removed with justification:

1. **"Regression model generalization to OOD is unsubstantiated"** — This claim ignores the empirical evidence in Tables 3 and 4, where RTA demonstrably improves accuracy on OOD datasets (ImageNet-A, ImageNet-R, cross-domain). The method works in practice even if a formal theoretical analysis is absent. The speculation that gains "could arise from the ensembling mechanism itself" has no supporting evidence.

2. **"-0.33% on average for RN50" (factually incorrect)** — The harsh critic claims RTA is -0.33% worse than BCA on average for RN50. The actual Table 4 shows RTA achieves 61.78% vs. BCA's 61.44%, i.e., **+**0.34% better. The cross-domain results also show RTA outperforms BCA on average for both backbones (RN50: +0.34; ViT-B/16: +0.11).

3. **"Ceiling TTA to pseudo-label CE gap is not justified"** — The paper clearly explains that Ceiling TTA demonstrates the upper bound achievable with true labels, and the regression approach aims to approximate this bound using pseudo-labels. This is a standard motivational framing, not a claim of equivalence.

4. **"Not comparing against Kim et al.'s method adapted to CLIP"** — Kim et al.'s loss predictor requires training within each target domain using target-domain labels, which is a fundamentally different (and more demanding) setup. The paper explicitly discusses this difference in the related work. A fair adaptation would require significant re-engineering.

5. **"The claim of strong generalization is overstated"** — While the cross-domain improvements are sometimes modest, RTA achieves the best average over 10 datasets for both backbones, which is a legitimate empirical claim of strong generalization. Criticizing the magnitude of improvement is a matter of opinion, not a flaw in the evidence presented.

6. **Generic area-of-concern sweeps from the harsh critic's filtering instruction** (e.g., "evidence is weak for the claims," "the evaluation lacks rigor" without concrete anchors) are removed per the filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The two reviews did not surface any additional novel interpretation of the results that the paper itself does not already articulate.

## Suggestions

1. **Clarify multi-label adaptation:** Specify how the regression tree trained on 1000-class logits is applied to multi-label datasets with different class counts. This is the single most important clarification needed.
2. **Add a max-softmax-probability baseline** to Table 3/4 comparisons to isolate the regression tree's added value.
3. **Report error bars** (at least 3 runs with standard deviation) for the main comparisons, especially where gaps are small.
4. **Ablate the confidence threshold** used for training data selection (e.g., 0.7, 0.9) to test sensitivity.
5. **Ablate training on augmented views** vs. original images to validate the design choice.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>