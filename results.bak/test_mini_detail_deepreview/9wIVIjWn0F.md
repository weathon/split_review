Now let me write the final consolidated review.

## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA) for CLIP-based image classification. The core idea is to pre-train a decision tree (LightGBM) that maps CLIP logits of augmented views to their pseudo-label cross-entropy loss, using a diverse pool of pseudo-labeled images from ImageVal-12k. At test time, the regression model predicts loss for each augmented view of a test instance, and the views with the smallest predicted loss are selected and ensembled for the final prediction. The method requires only one offline training session and then adapts to any test distribution without updates. Extensive experiments on single-label (ImageNet and variants, 10 cross-domain datasets) and multi-label benchmarks show consistent improvements over existing entropy-based TTA methods.

## Strengths

1. **Strong and well-motivated key observation**: The paper first demonstrates via "Ceiling TTA" experiments (Tables 1–2) that selecting views using ground-truth label cross-entropy (LCE) instead of Shannon entropy yields dramatically higher accuracy across all datasets (e.g., +23.9 points on IN-1k with RN50, 64 views). This provides a clear existence proof that the logit–loss relationship is exploitable, and motivates the regression approach convincingly. The t-SNE visualizations (Figure 2) and Spearman correlation analyses (Figure 3) further support the existence of a non-linear structural relationship between logits and loss.

2. **Consistent state-of-the-art performance across diverse benchmarks**: RTA achieves top average accuracy across single-label (Table 3, e.g., 66.90% avg with ViT-B/16 vs. 66.24% for Zero), cross-domain (Table 4, 68.70% avg with ViT-B/16 vs. 68.59% for BCA), and multi-label settings (Tables 5–6, e.g., 58.95% mAP on MSCOCO with ViT-B/16 vs. 57.52% for ML-TTA). These gains are consistent across both RN50 and ViT-B/16 backbones, demonstrating generalizability.

3. **Domain-agnostic one-shot training**: The regression model is trained once on 1,000 pseudo-labeled images from ImageVal-12k (5,000 after confidence filtering) and applied to all downstream tasks—including cross-domain datasets (Cars, Aircraft, EuroSAT, etc.) and multi-label datasets—without any retraining or per-task adaptation. This is a practical advantage over methods requiring per-instance prompt updates (TPT, DiffTPT) or memory-bank maintenance (BCA).

## Weaknesses

### Major

1. **No direct validation of the regression model's predictive quality.** The paper's entire contribution hinges on the regression decision tree accurately predicting cross-entropy loss for augmented views. Yet no direct regression quality metrics are reported: no MSE, Pearson/Spearman correlation between predicted and actual loss, or precision/recall of top-k view selection on a held-out set. The downstream accuracy results are indirect evidence, confounded by the pseudo-labeling pipeline, the view-count choice, and the ensemble protocol. Without a direct evaluation, it is impossible to tell whether the regression mapping is actually capturing the intended relationship or whether the improvements stem from some other property of the selection scheme (e.g., simply filtering out diverse views). This is the most significant gap in the paper.

2. **Training/test distribution mismatch for the regression model.** The decision tree is trained exclusively on *original (unaugmented) images* from ImageVal-12k, not on augmented views. The paper's justification ("the original image itself can actually be regarded as a view") ignores that augmentation (random crop, color jitter, rotation) systematically shifts the CLIP logit distribution. At test time, the tree is applied to augmented views that may fall outside its training distribution. The paper provides no analysis (e.g., logit distribution overlap, regression accuracy on augmented vs. original images) establishing that the learned mapping generalizes. This undermines confidence in the method's stated mechanism.

3. **Pseudo-label filtering biases training data toward low-loss regions, and the limited tree capacity raises concerns about extrapolation.** Training uses only samples with CLIP confidence ≥ 0.8 (1,000 of ~5,000), which means the regression model learns almost exclusively from logits that already produce low cross-entropy loss. At test time, the model must predict for views with potentially higher loss—exactly the ones worth rejecting. With only depth-5/16-leaf LightGBM, the piecewise-constant tree is forced to extrapolate in regions where it has no training data. The paper does not analyze leaf coverage (how many leaves have training data, what loss ranges they cover) or whether the tree is extrapolating in empty regions.

### Minor

4. **No variance or confidence intervals reported for any experimental result.** All results in Tables 3–6 are single point estimates. Given randomness in augmentation sampling and decision tree training (the tree is trained on a 1,000-sample subset), reporting standard deviations over multiple runs would improve statistical reliability. The community standard for TTA papers varies, but at minimum an ablation showing the method's stability would strengthen the empirical claims.

5. **Missing analysis of simpler baselines.** A natural competitor for RTA is selecting views based on maximum CLIP softmax confidence (highest predicted probability), which is effectively what the regression model approximates when the loss is low. Showing whether RTA outperforms this simple baseline would clarify whether the regression adds value beyond a trivial confidence measure.

6. **Limited justification for the decision tree's capacity (depth 5, 16 leaves).** The regression model maps from L-dimensional logits (L=1000 for ImageNet) to a scalar loss. No ablation is provided showing whether deeper/wider trees or alternative regressors (e.g., MLP, random forest) improve performance. The choice appears arbitrary and is not empirically motivated.

### Trivial

7. **Minor labeling ambiguity**: The "Ceiling TTA" label in Tables 1–2 uses ground-truth labels, which is clearly stated, but the term "Ceiling" could be misread as an achievable upper bound by a TTA method. The paper frames this correctly as an oracle analysis, but the terminology is worth clarifying.

## Nice-to-Haves

- Train the regression model on augmented views from the diverse data (generate 64 augmentations per training image) to eliminate the train/test distribution mismatch, then compare performance.
- Report direct regression metrics: predicted vs. actual loss correlation on held-out augmented views, and selection precision/recall for top-k views.
- Add an ablation of the confidence threshold (≥0.8) to show sensitivity of the pseudo-labeling pipeline.

## Removed Points

- **"The gap between oracle LCE and RTA is enormous and unaddressed"** — Removed because this is comparing RTA (no ground-truth labels) to an oracle using ground-truth labels. The gap is natural and expected; the paper uses the oracle only as motivation for the regression approach. The critic's framing as a weakness of RTA is a category error.

- **"RTA also operates on a single test instance"** — Removed because RTA pre-trains the regression model on diverse offline data, which is fundamentally different from per-instance methods that only use the current test sample. The criticism misunderstands the method's offline training stage.

- **Formatting/style nitpicks, missing appendix content** — Removed per parser issues.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide direct regression validation**: Add a small experimental section reporting Pearson/Spearman correlation between predicted and true loss on a held-out set of *augmented views* (from the same diverse data, but held out). Also report top-k selection recall (how often the k views with smallest predicted loss are actually among the k views with smallest true loss).

2. **Address the distribution mismatch**: Either train the regression on synthetically augmented versions of the diverse data (ablation to show whether it helps), or at minimum provide a scatter plot or histogram showing that the logit distributions of original training images and test-time augmented views overlap sufficiently.

3. **Analyze tree coverage**: Report the range of pseudo-label CE losses in the training set, the number of leaves that contain training samples, and what loss values the tree predicts for out-of-range inputs.

4. **Add variance estimates and the max-softmax baseline**: Report at least 3 runs with standard deviations for the main results, and add a "max softmax probability" baseline to Table 3.

5. **Tree capacity ablation**: Show RTA's performance with different tree depths (3, 5, 7, 10) and leaf counts to empirically justify the chosen architecture.

## Score and Decision

**Round-1 bracket**: After reading the paper, my initial assessment placed it in the (3.5, 7.5) range — clearly stronger than the low-anchor papers (avg 2.50–3.33, rejected for fundamental methodological flaws or unclear contributions) and clearly weaker than the high-anchor papers (avg 8.00, accepted based on rigorous execution and strong empirical validation).

**Round-2 anchors examined**:

- **DOTA (6.00, rejected)**: Solid method with clear motivation and extensive evaluation, but had several methodological gaps (unclear batch handling for distribution estimation, insufficiently motivated human-in-the-loop component, sensitivity to hyperparameters unexamined). The RTA paper has similar scope of evaluation but a more fundamental gap in the core mechanism validation.

- **ML-TTA / BEM (6.25, accepted)**: Clean multi-label TTA solution with good theoretical grounding (bound entropy minimization) and consistent gains. Stronger in terms of architectural justification and ablation. RTA is more ambitious in scope (single-label, multi-label, cross-domain) but less convincingly validated at the mechanism level.

- **BAT-CLIP (5.50, rejected)**: Mixed reviews (scores 3, 8, 5, 6). Interesting bimodal approach but concerns about practical efficiency and clarity of the adaptation mechanism. RTA is more extensive in evaluation coverage.

- **RLCF (6.67, accepted)**: Reinforcement learning with CLIP reward for TTA, applied to 3 tasks. Clean execution but concerns about incremental novelty over prior work. RTA is less polished in its evidence chain but proposes a more distinctive mechanism.

**Final score**: 5.5. The paper proposes a genuinely novel idea (regression-based view selection for TTA) and validates it extensively at the task-performance level. However, the missing direct validation of the regression model — the paper's core claimed mechanism — is a significant gap that prevents the paper from reaching the 6+ tier. The paper is clearly better than papers in the 3–4 range (which typically have fundamental flaws in their experimental design or lack clear contributions), but it does not match the evidential completeness of the top-tier papers in this space.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>