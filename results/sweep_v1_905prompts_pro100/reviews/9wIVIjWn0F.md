Now I have enough evidence to write the final review. Let me compile everything.

---

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA), a method for improving CLIP's test-time performance by training a lightweight regression model (LightGBM decision tree) to predict the cross-entropy loss of augmented views directly from their logit vectors. The key insight — demonstrated convincingly through a "ceiling TTA" analysis — is that ground-truth label cross-entropy loss correlates strongly with view quality across diverse distributions, and that this relationship can be learned from pseudo-labeled data and exploited during inference for better view selection than entropy-based methods. The paper reports improvements over existing TTA methods across ImageNet variants, cross-domain datasets, and multi-label benchmarks.

## Strengths

- **Compelling ceiling analysis (Tables 1–2):** Using ground-truth cross-entropy loss to select views pushes accuracy dramatically higher than entropy-based selection (e.g., ViT-B/16 on ImageNet-A: 47.8% → 90.2% with 64 views). This directly establishes that a learnable view–loss relationship exists and that exploiting it could significantly advance TTA. This is the paper's strongest contribution.

- **Consistent empirical gains across broad benchmarks:** RTA delivers improvements over a wide range of TTA baselines on single-label ImageNet variants (Table 3), 10 cross-domain datasets (Table 4), and multi-label benchmarks (Tables 5–6), across both RN50 and ViT-B/16 backbones. The breadth of evaluation is commendable.

- **Lightweight and practical design:** The regression model is a shallow LightGBM tree (depth 5, 16 leaves) trained on only 1,000 samples, making the overhead negligible relative to the base CLIP inference cost. This practical efficiency is a genuine advantage over methods requiring per-instance optimization.

- **Well-motivated analysis of logit-loss structure:** The t-SNE visualizations (Figure 2) and Spearman correlation analysis (Figure 3) provide plausible evidence that a structural, learnable relationship exists between logit vectors and loss values, lending credibility to the regression approach beyond the ceiling results alone.

## Weaknesses

### Fatal

None.

### Major

- **Class-space mismatch across datasets is unexplained, undermining the "train once, adapt anywhere" claim:** The regression tree is trained on ImageNet logits (1000-dimensional). During TTA, Algorithm 2 computes logits over the test set's L classes (e.g., 196 for Stanford Cars, 100 for Aircraft). A decision tree trained on 1000-D inputs cannot process 196-D inputs. The paper never explains how this dimensionality mismatch is resolved for the cross-domain experiments in Table 4. This is a critical methodological gap: the central claim that RTA "only needs to be trained once … and then it can directly adapt to test instances with arbitrary distributions" (line 82–83) cannot be evaluated without knowing how the regressor handles varying class counts. There are plausible resolutions (e.g., always computing logits over the 1000 ImageNet classes regardless of the downstream task), but none is described.

- **Multi-label methodology is entirely undocumented:** The paper reports multi-label results (Tables 5–6) with substantial gains over ML-TTA. However, Section 4 describes only single-label softmax cross-entropy (Equation 4). There is no discussion of how the regression mapping — which predicts a scalar loss derived from a softmax over L classes — is extended to multi-label problems where predictions involve independent binary decisions per class. This omission leaves the multi-label results unsubstantiated.

### Minor

- **ImageVal-12k as regression data creates a label-space overlap with ImageNet variants:** For ImageNet-1k and its variants (IN-A, IN-V2, IN-R, IN-Sketch), the regression training data (ImageVal-12k) shares the same 1000-class label space as the test data. While the image distributions differ, the regressor has seen logit patterns from the same 1000-class structure. This is disclosed but not discussed as a potential confound. The paper's claim that the regression mapping is "independent of downstream tasks" (line 388) is slightly overstated for these datasets, though the cross-domain results (if correctly implemented) partially address this.

- **No analysis of pseudo-label noise impact:** The regression model is trained on pseudo-labels filtered by a confidence threshold (≥0.8). There is no ablation studying how sensitive the method is to pseudo-label errors (e.g., varying the threshold), which matters because the regression target values are derived from potentially incorrect pseudo-labels.

- **Sampling procedure is imprecisely described:** The paper mentions "sampling by logit-based equal-interval from 5,000 samples with threshold ≥ 0.8" (line 390–391) but does not explain what "logit-based equal-interval" means or how the 5,000 initial samples relate to ImageVal-12k. This impairs reproducibility.

### Trivial

- The "free lunch" framing (line 13, 78) is rhetorical overreach — training the regressor requires 12k images, pseudo-labeling, and a training step, which is a modest but real cost.

## Nice-to-Haves

- An ablation comparing regression data sources (in-domain vs. strictly out-of-domain, e.g., a non-ImageNet source) would clarify whether the gains derive from the regression mapping itself or from the specific data distribution.
- Reporting results with different regressor architectures (e.g., linear regression, MLP) would help characterize how much of the performance depends on the specific tree-based model.
- Discussing the relationship to Kim et al. (2020), which the paper cites as closely related, with a more detailed comparison of assumptions and performance trade-offs.

## Removed Points

These points were raised in the input reviews but are removed after verification against the paper:

- **"Undisclosed use of in-distribution data" (Harsh Critic #1):** The paper explicitly discloses using ImageVal-12k (line 390). The word "undisclosed" is factually incorrect. The concern about shared label space is downgraded to Minor above, not because it's invalid, but because it's disclosed and the cross-domain experiments (with different label spaces) partially address it. The harsh critic's framing that this makes comparisons "unfair" is also tempered by the fact that the regressor learns a logit→loss mapping from CLIP's own representations, which have some domain invariance.

- **"Class-space mismatch means separate regressors were trained" (Harsh Critic #2, speculative conclusion):** The harsh critic asserts that "the only plausible resolution is that separate regressors were trained per dataset." This is speculation — the paper doesn't say this, and there are other plausible resolutions. The underlying concern (class-space mismatch is unexplained) is kept as a Major weakness, but the speculative conclusion is removed.

- **Harsh Critic's claim that "more data can yield higher performance is not empirically validated":** Figure 5 shows accuracy increasing from 1k to 50k regression samples for both ImageNet and its variants, with significant early gains and a plateau. The claim is empirically validated; the harsh critic's "only marginal improvements after 5k" is contradicted by the figure which shows continued (if slower) improvement.

- **Strength Finder's "training-once, generalise-anywhere property":** This strength directly conflicts with the verified Major weakness about class-space mismatch. Removed as unsupported.

- **Strength Finder's "lightweight and computationally practical":** Kept as a genuine strength.

- **Strength Finder's generic framing about "important problem" and "timely":** These are generic strengths without concrete anchors; removed as superficial.

## Novel Insights

The ceiling TTA analysis (Tables 1–2) is genuinely insightful and goes beyond the paper's own method contribution. By showing that ground-truth loss-guided view selection can push CLIP accuracy to near-saturation (e.g., 90.2% on ImageNet-A), it establishes an empirical upper bound for what TTA methods could achieve with perfect view selection. This is a useful reference point for the entire TTA community and suggests that the gap between current entropy-based methods and what is possible is much larger than previously appreciated. The regression approach is a natural consequence of this observation.

## Suggestions

- **Resolve the class-space ambiguity:** Either (a) describe the protocol used for cross-domain datasets — e.g., always compute logits over the 1000 ImageNet classes and use those as fixed-dimensional features for the regressor — or (b) if separate regressors were trained per dataset, retract the "train once, adapt anywhere" claim and reframe accordingly. This is essential for the paper to be evaluable.

- **Document the multi-label extension:** Explain how the regression loss prediction is adapted for multi-label problems. At minimum, specify what loss function is used as the regression target during training and how the predicted loss guides view selection when multiple labels can be positive.

- **Add a pseudo-label sensitivity ablation:** Vary the confidence threshold for pseudo-labeling (e.g., 0.7, 0.8, 0.9, 0.95) and report how regression quality and downstream TTA performance change. This would address concerns about the method's robustness to label noise.

- **Clarify the sampling procedure:** Explain the "logit-based equal-interval" sampling method explicitly, including how the 5,000 initial samples are selected from ImageVal-12k.

## Score and Decision

I evaluated RTA against the calibration anchors. The paper's strongest asset is the ceiling TTA analysis, which is novel and well-executed. Its empirical evaluation is broad, and the regression approach is intuitively appealing. However, the paper has two major methodological gaps: (1) the class-space dimensionality mismatch across cross-domain datasets is never explained, which makes the central "train once, adapt anywhere" claim impossible to verify, and (2) the multi-label extension is entirely undocumented despite reported results. These gaps place RTA below well-described TTA methods like RLCF (6.67) and DeYO (7.00), and below the more completely specified ML-TTA (6.25). It is comparable to DOTA (6.00), which was rejected for unclear methodology, but the gaps in RTA are arguably more severe since they involve missing descriptions rather than merely unclear ones. I place RTA at 5.5, comparable to BaFTA (5.50).

**Anchor comparison:**
- BaFTA (KNtcoAM5Gy, 5.50, round 1): Similar level of missing methodological detail; RTA has stronger motivation but similar incompleteness.
- DOTA (yD2JMeKumt, 6.00, round 2): All reviewers gave 6; rejected for unclear methodology. RTA's gaps are comparably severe.
- ML-TTA (75PhjtbBdr, 6.25, rounds 1–2): More complete methodology than RTA; accepted.
- RLCF (kIP0duasBb, 6.67, rounds 1–2): Stronger methodological completeness; accepted.
- DeYO (9w3iw8wDuE, 7.00, round 1): Stronger theoretical grounding and methodological clarity.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>