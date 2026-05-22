Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes RTA (Regression-based Test-time Adaptation), a method for CLIP-based image classification that replaces entropy-based view selection with a learned regression mapping that predicts each augmented view's cross-entropy loss directly from its logits. The key idea is that models trained on diverse pseudo-labeled data can learn a mapping from logits to loss that generalizes across domains, enabling confident view selection without needing true labels. Experiments are conducted on single-label (ImageNet variants + 10 cross-domain), multi-label (MSCOCO, VOC2007, NUSWIDE) benchmarks with RN50 and ViT-B/16 backbones.

## Strengths

1. **Clear and well-motivated Ceiling TTA finding.** Tables 1 and 2 convincingly show that using ground-truth label cross-entropy (LCE) to select views yields massive gains over entropy-based selection (e.g., ViT-B/16 with 64 views: LCE 89.0% vs. SE 70.6% on IN-1k, and 90.2% vs. 64.3% on IN-A). This provides a compelling motivation for learning a regression mapping from logits to loss.

2. **Novel departure from entropy-based selection.** The idea of learning a regression mapping from logits directly to cross-entropy loss is conceptually novel in the TTA literature. Instead of relying on the information bottleneck of a single instance's probability distribution, RTA leverages a pre-trained mapping from diverse data — a genuine conceptual shift.

3. **Consistent state-of-the-art results across many benchmarks.** RTA achieves the best or near-best results on most benchmarks. The gains are substantial on some datasets (e.g., RN50 on IN-A: 36.79% vs. DiTPT 31.06%, +5.73%; RN50 on MSCOCO: 53.25% mAP vs. ML-TTA 51.58%, +1.67%) and positive across essentially all settings.

4. **Practical training configuration.** The regression model (LightGBM) is trained once on only ~1,000 pseudo-labeled samples and applied to any test distribution without online updates. The ablation in Figure 5 shows the method is not brittle to training sample size.

## Weaknesses

### Major

1. **Dimensionality mismatch between training and test logit vectors is not addressed.** The regression tree is trained on logits from ImageNet's 1000 classes (Section 4.2, Algorithm 1). During test-time adaptation, Algorithm 2 computes logits for *L* classes of the **test dataset** (Equation 8, Algorithm 2 line 6). For cross-domain datasets like Aircraft (100 classes) or multi-label datasets like MSCOCO (80 classes), the input dimensionality to the LightGBM model changes. A decision tree trained on 1000 features cannot accept inputs with a different number of features. The paper provides no mechanism — padding, truncation, summary statistics, or otherwise — to align logit dimensions between training and inference for datasets with different class counts. This issue affects all cross-domain results in Table 4 and all multi-label results in Tables 5–6. The authors must clarify how this mismatch is handled; as written, the method description is incomplete on a point that is central to its applicability.

2. **No direct evaluation of regression quality.** The paper motivates RTA by showing that the Ceiling TTA (true-label-based selection) achieves near-saturated accuracy, then proposes RTA as a learned approximation. Yet no correlation metrics (Spearman's ρ, R², or similar) are reported between the *predicted* loss from the regression model and the *true* loss on held-out data. The t-SNE visualization (Figure 2) and Spearman analysis of individual features (Figure 3) demonstrate that logits and loss are related, but they do not show that the *trained regression model* predicts loss accurately. Without this evidence, it is unclear whether RTA's gains come from accurate loss prediction or from some other property of the learned mapping. Reporting prediction-vs.-ground-truth loss correlation on ImageNet-val and on cross-domain samples would substantially strengthen the paper.

### Minor

3. **Training on only high-confidence pseudo-labels (threshold ≥ 0.8).** The regression data is sampled from ImageNet-val examples where CLIP's confidence ≥ 0.8 (Section 5.1). This biases the training distribution toward easy, correctly classified examples. The model is then applied to predict loss for all views, including low-confidence ones where the logit–loss relationship may differ. While Figure 5 shows that performance improves with more data (suggesting some robustness), the paper lacks an analysis of regression accuracy broken down by confidence level. This is worth investigating but does not invalidate the results.

4. **Improvements on individual datasets are sometimes modest.** On several datasets, particularly for ViT-B/16, the gains over strong baselines like Zero and BCA are within 0.2–1.6 percentage points (e.g., Table 3 ViT-B/16 IN-1k: 71.13% vs. Zero 70.89%, +0.24%; IN-R: 81.05% vs. 80.82%, +0.23%; Table 4 ViT-B/16 average: 68.70% vs. BCA 68.59%, +0.11%). No confidence intervals or significance tests are reported. While the *average* trend across many benchmarks is positive, individual dataset differences should be interpreted cautiously.

### Trivial

5. Equation numbering inconsistency. Equation 8 uses the label "reg" in the superscript ($s_{ij}^{x_i^{\text{reg}}}$) but appears in the test-time Algorithm 2 section (4.3), which should refer to test instances $x^{\text{test}}$.

## Nice-to-Haves

- An ablation comparing the LightGBM tree trained with pseudo-labels vs. ground-truth labels (on a small labeled set) to isolate the effect of pseudo-label noise.
- Analysis of regression performance stratified by view quality (low vs. high confidence).
- A study of the sensitivity to tree hyperparameters (depth, number of leaves) — the paper uses fixed values of 5 and 16 respectively.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Ceiling TTA gap is enormous" (Harsh Critic point 2):** The gap between Ceiling TTA (using true labels) and RTA is not a weakness — Ceiling TTA is an oracle upper bound. No method achieves it. The relevant comparison is RTA vs. other TTA methods, where RTA shows consistent improvement. This criticism misunderstands the purpose of an upper-bound analysis.

- **"Free lunch claim understates offline training" (Harsh Critic section-by-section):** The paper explicitly describes the offline training stage in Sections 4.2 and 5.1. Calling it a "free lunch" refers to the fact that the same trained model applies to any test distribution without per-instance updates — a standard rhetorical framing. This is not a substantive weakness.

- **"Spearman and t-SNE analysis uses true labels" (Harsh Critic):** The analysis in Figures 2 and 3 is intended to demonstrate the *existence* of a structural relationship between logits and loss (which is a prerequisite for learning it), not to validate the trained model. The reviewer is demanding a different experiment than what these figures were designed to show.

- **Strength Finder's claim about "5.73% improvement over previous best DiTPT":** While factually correct for RN50 on IN-A, this is slightly misleading because TDA (CVPR 2024) at 30.29% and BCA (CVPR 2025) at 30.35% are also competitive on that benchmark. The core claim (RTA improves over baselines) remains valid.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core findings (the Ceiling TTA observation is compelling, the method is novel, the experiments are broad) while pointing to a significant gap in the method description (the dimensionality mismatch) that the authors need to resolve.

## Suggestions

1. **Clarify the dimensionality handling.** Describe explicitly how the regression model trained on 1000-class logits is applied to datasets with different numbers of classes. If there is a padding, truncation, or feature-selection mechanism, specify it. If the method only applies when the test dataset also has 1000 classes, state this limitation clearly and report results separately for datasets that satisfy this condition.

2. **Add regression quality metrics.** Report Spearman's ρ or R² between predicted loss and true loss on held-out ImageNet-val samples and on samples from at least one cross-domain dataset. This would directly validate that the regression tree learns the intended mapping.

3. **Report confidence intervals or significance tests** for the main results (Tables 3–6), or at minimum note the variance across multiple runs. This would help readers assess whether the observed improvements over strong baselines are statistically meaningful.

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| Multi-modal Reliability Bias (TPZRq4FALB) | 8.00 | Stronger: identifies a new challenge, constructs benchmarks, thorough validation. RTA has a more novel technical idea but a significant method description gap. |
| CLIP Reward TTA (kIP0duasBb) | 6.67 | Comparable: similar TTA-for-CLIP setting, broad evaluation. RTA has more extensive experiments but a more concerning methodological gap. |
| ML-TTA (75PhjtbBdr) | 6.25 | Comparable: multi-label TTA with clear motivation. RTA covers more settings but has the dimensionality issue ML-TTA does not. |
| BAT-CLIP (z7PhIgVmZU) | 5.50 | Similar tier: interesting CLIP adaptation idea with some gaps in presentation. RTA has more extensive experiments. |
| Active Test-Time Prompt Learning (pdzHpQbGrn) | 2.50 | Weaker: marginal improvements, poor novelty. RTA has clearer contributions and stronger empirical evidence. |
| IEL Ensemble TTA (4LiegvCeQD) | 2.50 | Weaker: missing baselines, unsubstantiated claims. RTA is much more thorough. |

The paper presents an interesting idea with strong Ceiling TTA motivation and consistent empirical improvements across many benchmarks. However, the unaddressed dimensionality mismatch between training (1000 classes) and test (variable classes) is a significant gap that prevents full verification of the method as described. The paper is clearly above the rejection-tier papers (2.5–3.3) in quality and scope, but below the top-tier anchors (6.67–8.00) due to this unresolved issue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>