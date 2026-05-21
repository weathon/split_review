Now I have all the calibration data needed. Let me write the final consolidated review.

**Round 1 bracket:** The paper is clearly stronger than the weak-band anchors (~3.0: C-TTA, REACT, VLBO — papers with misleading positioning, unfair comparisons, or marginal contributions) and comparable to the middle-band anchors (~4.33–5.50: ADTE, BITTA, FGA, PEA — solid papers with some weaknesses). The strong-band anchors (8.0) are on entirely different topics and not comparable. **Initial bracket: 4.0–6.0.**

**Round 2 narrowing:** Compared to ADTE (4.50, Accept Poster): RTA has a more novel approach and larger empirical gains. Compared to FGA (5.00, Accept Poster): RTA is comparably novel with similarly strong results but has a significant clarity gap. Compared to PEA (5.50, Accept Poster): Both are solid contributions; RTA is slightly lower due to the unresolved methodological description gap. **Final score: 5.0**, positioned between ADTE (4.50) and PEA (5.50), alongside FGA (5.00).

---

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA) for vision-language models. The key insight is that a regression model (LightGBM) can be trained offline on pseudo-labeled data to predict the cross-entropy loss of augmented views directly from their logits, enabling more accurate view selection during TTA compared to standard entropy-based approaches. RTA is trained once on ImageNet validation data and applied without updates to any downstream distribution. Experiments across single-label (ImageNet variants), multi-label (MSCOCO, VOC2007, NUSWIDE), and cross-domain (10 datasets) benchmarks show consistent improvements over prior TTA methods.

## Strengths

1. **Novel and well-motivated approach**: The paper identifies a genuine limitation of entropy-based view selection (reliance on individual instance probability distributions, which struggle with outliers) and proposes a fundamentally different solution — learning a regression mapping from logits to loss. The ceiling analysis in Tables 1-2 (showing 19–35 point gaps between entropy-based and ground-truth-loss-based view selection, e.g., +23.9 points on IN-1k for RN50 with 64 views) provides strong empirical motivation for the approach.

2. **State-of-the-art results across multiple settings**: RTA consistently outperforms prior TTA methods. On ImageNet variants (Table 3), RTA achieves 49.24% OOD average (RN50) vs. next-best 46.98% (BCA) and 65.84% (ViT-B/16) vs. 65.03% (Zero). On multi-label (Tables 5-6), RTA surpasses the dedicated multi-label method ML-TTA on all three datasets for both backbones. On cross-domain (Table 4), RTA achieves the highest average accuracy on 10 diverse datasets for both architectures.

3. **Offline training with no test-time updates**: The regression model is trained once on 1,000 pseudo-labeled samples and then frozen. This makes RTA computationally efficient at inference (no backpropagation, no prompt tuning, no memory bank) and avoids catastrophic forgetting issues that affect online TTA methods.

4. **Structural correlation evidence**: The t-SNE visualization (Figure 2) shows clear color gradients in the logit space across multiple datasets, and the Spearman rank-correlation analysis (Figure 3) quantifies monotonic relationships between individual logit features and label loss. These analyses provide direct statistical support for the claim that a regression function can reliably map logits to loss.

## Weaknesses

### Fatal
None.

### Major
1. **Unspecified handling of variable label spaces**: The regression model is trained on logit vectors produced using ImageNet-1k class prompts (Section 4.2, Algorithm 1). At test time, the paper evaluates on datasets with widely varying numbers of classes: Pets (37), Flowers (102), Aircraft (100), DTD (47), EuroSAT (10), MSCOCO (80), VOC2007 (20), NUSWIDE (81), etc. The paper is completely silent on how a LightGBM decision tree trained on fixed-length 1000-dimensional logit vectors processes logit vectors of different dimensionalities. This is a structural gap in the methodological description — the experiments cannot be reproduced without knowing whether (a) the same 1000 ImageNet class prompts are used to produce fixed-length logits for the regression model at test time (while final predictions use the test dataset's actual classes), (b) the model is retrained per dataset, or (c) some other mechanism is employed. *(Verified: the paper contains no mention of how this dimensionality mismatch is resolved in Algorithms 1-2 or anywhere else.)*

### Minor
2. **Missing ablation isolating regression benefit**: The paper compares RTA against full TTA methods (TPT, DiffTPT, BCA, Zero, etc.) that involve parameter updates, prompt tuning, or other complexity. However, there is no direct comparison of RTA against a simple, parameter-free entropy-based view selection baseline using the *same* augmentation pipeline, view count, and ensemble strategy. Tables 1-2 compare entropy (H_SE) vs. ground-truth loss (H_LCE) for the ceiling analysis, but Table 3 compares RTA against full methods — not against a "entropy-only view selection" baseline with identical pipeline. Since the reported gains over entropy on some datasets are modest (e.g., 0.5–1.3 points on ImageNet-1k in Tables 1 vs. Table 3), a controlled ablation would clarify the regression mapping's added value.

3. **Data-access asymmetry with baselines**: RTA uses an offline training phase on ImageNet validation data (ImageVal-12k, subsampled to 1,000 pseudo-labeled examples). The baselines (TPT, DiffTPT, Zero, BCA, etc.) perform test-time adaptation using only the current test instance with no additional data. The paper does not discuss this as a limitation or attempt to ablate what information the offline training contributes. While this is a practical design choice, it deserves acknowledgment for fair comparison.

4. **No statistical significance or error bars**: None of the tables report variance or confidence intervals. Many results are close (e.g., RTA vs. BCA on ViT-B/16 cross-domain: 68.70 vs. 68.59; RTA vs. Zero on ViT-B/16 ImageNet-R: 81.05 vs. 80.82). Without variance estimates, it is unclear whether RTA reliably outperforms baselines in these tight comparisons.

### Trivial
5. **Typo in Equation (8)**: The superscript reads `x_i^{reg}` instead of `x_i^{test}`.

## Nice-to-Haves
- A controlled comparison of RTA against entropy-based view selection using identical augmentation counts, ensemble strategy, and no parameter updates would cleanly isolate the benefit of the regression mapping.
- Discussion of the gap between RTA and the ceiling (H_LCE) on each dataset. For example, on ImageNet-A with RN50, the ceiling is 70.9% but RTA achieves 36.79% — a gap of ~34 points that is not analyzed.

## Removed Points
- **"Unfair comparison with respect to data access" (from Harsh Critic)**: Retained but downgraded to Minor (Weakness #3). The data-access difference is real, but it reflects a design choice (offline training on generic data for a one-time cost) rather than an unfair comparison. The paper frames RTA's offline training as a practical advantage, not a hidden source of test-set information.
- **"No experiments on truly non-ImageNet distributions (medical images, satellite imagery)"**: Removed. Scope creep — the paper evaluates on 16+ standard datasets across single-label, multi-label, and cross-domain settings, which is comprehensive for a TTA paper.
- **"Limited ablation on regression model choice (only LightGBM)"**: Removed. LightGBM is a reasonable choice for tabular regression; additional model comparisons would be nice but are not required.
- **"No discussion of computational cost of LightGBM"**: Removed. The paper provides implementation details (100 rounds, max depth 5, 16 leaves) and states "negligible additional cost." The cost of tree inference is trivially low.
- **"Missing related works"**: Removed per instructions — cannot verify without external sources.
- **Strength Finder's generic strengths** (e.g., "addressing an important problem"): Removed as not paper-specific.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify the label-space handling**: In Section 4.2 or Algorithm 2, explicitly state how the regression model processes logit vectors from test datasets with different class counts. If the same 1000 ImageNet class prompts are used to produce fixed-length logit vectors for the regression model at test time (while final predictions use the test dataset's actual classes), state this clearly.
2. **Add a controlled ablation**: Compare RTA vs. entropy-based view selection with identical augmentation pipeline (same N views, same k selection, same ensemble) and no parameter updates, to isolate the regression benefit.
3. **Report variances**: Add confidence intervals or standard deviations for the main results, especially for close comparisons.
4. **Discuss the ceiling gap**: Add a paragraph analyzing how close RTA gets to the ground-truth-loss ceiling on key datasets, to provide a realistic view of the regression model's limitations.

## Score and Decision

**Anchor papers used for calibration:**
- **C-TTA** (3.00, Weak): A training-free prototype-based continuous TTA method. The paper has misleading positioning (confusing "continuous TTA" with the well-established CTTA setting), unclear experimental setup, and small gaps. RTA is clearly stronger — more novel approach, larger gains, clearer positioning.
- **ADTE** (4.50, Accept Poster): Replaces Shannon entropy with Tsallis entropy for view selection. Modest gains (0.5–2%), ad-hoc min-max mapping for the q parameter, but a clean and well-motivated idea. RTA has a more novel approach and larger empirical gains, but the label-space clarity gap is a more significant weakness than ADTE's ad-hoc design.
- **BITTA** (4.33, Accept Poster): Bilateral learning/unlearning for TTA. Marginal gains (0.3–1.0 pp), incremental novelty, missing baselines. RTA is clearly stronger in novelty and results.
- **FGA** (5.00, Accept Poster): Flatness-guided adaptation requiring 16-shot labeled training data. Novel approach, strong results, but some theoretical and experimental concerns. RTA is comparable — similarly novel, similarly strong results, with a comparable weakness (offline data requirement + label-space clarity issue).
- **PEA** (5.50, Accept Poster): Backprop-free embedding alignment. Elegant geometric interpretation, strong efficiency, but requires source data access. RTA is slightly below PEA due to the unresolved label-space description gap.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>