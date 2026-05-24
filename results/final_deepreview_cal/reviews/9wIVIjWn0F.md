Now I have a thorough understanding of both the paper and the calibration landscape. Let me write the consolidated review.

## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA), which trains a lightweight decision tree (LightGBM) offline on pseudo-labeled diverse data to predict per-view cross-entropy loss from CLIP logits, then uses this predictor at test time to select confident augmented views. The core insight—motivated by a compelling ceiling analysis showing that true label-cross-entropy loss selection vastly outperforms entropy-based selection—is that a regression mapping between logit patterns and loss generalizes across distributions. RTA requires no online model updates and consistently outperforms state-of-the-art TTA methods across single-label, multi-label, and cross-domain benchmarks.

## Strengths

- **Compelling ceiling TTA analysis (Tables 1–2):** The demonstration that using ground-truth LCE for view selection yields 20–30% absolute accuracy gains over entropy selection on distribution-shifted benchmarks (e.g., ViT-B/16 on IN-A: 90.2% LCE vs. 64.3% SE at 64 views) provides strong motivation and sets a clear target for the regression approach.

- **Well-evidenced logits-loss relationship (Figures 2–3):** The t-SNE visualizations reveal clear clustering of view logits by LCE value across multiple datasets, and the Spearman correlation analysis confirms statistically significant monotonic relationships between top logit features and loss. This directly supports the feasibility of learning a regression mapping.

- **Broad and consistent empirical validation (Tables 3–6):** RTA outperforms recent TTA methods (TPT, DiffTPT, TDA, Zero, BCA, ML-TTA, etc.) across 15+ datasets spanning single-label ImageNet variants, 10 cross-domain datasets, and multi-label benchmarks (MSCOCO, VOC, NUSWIDE) on both RN50 and ViT-B/16 backbones. The gains are modest but consistent.

- **Practical efficiency:** The regression model (LightGBM tree, max depth 5, 16 leaves) is trained once on only 1,000 pseudo-labeled samples and requires no per-instance gradient updates, prompt tuning, or cache maintenance at test time—a genuine practical advantage over competing TTA methods.

## Weaknesses

### Fatal

None.

### Major

- **Undisclosed regression set composition hinders fairness assessment:** The paper states only that it uses "ImageVal-12k as the regression mapping data" (Section 5.1) with no description of what this dataset contains, how it was constructed, or its relationship to the test benchmarks. While the cross-domain results (Table 4) provide evidence that the learned mapping generalizes beyond any single domain, the paper's central claim that the regression mapping is learned from "diverse data independent of downstream tasks" cannot be fully evaluated without transparency about the regression set. This is addressable through clarification.

### Minor

- **No direct quantification of predicted-loss vs. true-loss correlation on test sets:** The paper establishes a ceiling with true LCE (Tables 1–2) and shows final RTA accuracy (Tables 3–6), but never reports how well the tree's predicted pseudo-loss correlates with true label cross-entropy loss on the test benchmarks. Reporting Spearman correlation between f(logits) and true LCE would directly validate the core mechanism.

- **"Arbitrary distributions" claim is overstated (Section 1, Abstract):** The paper claims RTA "can adapt to test instances with arbitrary distributions" and "directly adapt to test instances with arbitrary distributions," but the empirical evidence covers specific benchmark distribution shifts, not truly arbitrary ones. The language should be tempered.

- **No explicit limitations section:** The paper would benefit from discussing when RTA might fail—e.g., when CLIP's pseudo-label confidence is poorly calibrated on a target domain, or when the regression set's logit distribution differs substantially from test logits.

### Trivial

- The method description in Section 4.3 uses inconsistent notation: Equation 8 refers to $s_{ij}^{x_i^{\text{reg}}}$ but the surrounding text describes test-time adaptation ($\mathbf{x}^{\text{test}}$). This is a minor copy-paste error that does not affect understanding.

## Nice-to-Haves

- An experiment training the regression tree on a clearly distinct dataset (e.g., LAION or Conceptual Captions subset) to directly demonstrate that the logits-to-loss mapping transfers across dataset boundaries would strengthen the independence claim.
- Reporting the correlation between predicted loss and ground-truth LCE on test sets.
- A brief discussion of scenarios where the approach may underperform (e.g., domains where CLIP has poor zero-shot calibration).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Unfair experimental advantage due to domain-overlapping regression set" (from Harsh Critic):** The claim that this amounts to a "structural flaw invalidating main experimental results" is speculative. The paper does not describe ImageVal-12k's composition, so whether it overlaps with test distributions cannot be verified from the text. Moreover, the regression tree learns a mapping from logits to pseudo-CE loss—a function of CLIP's own prediction behavior—not from images to class labels. The consistent gains on cross-domain benchmarks (Cars, Aircraft, etc., Table 4), which are far from ImageNet, provide affirmative evidence that the mapping generalizes. Demoted from "fatal" to an acknowledged limitation about transparency.

- **"The baseline TTA methods operate purely on the test instance without any offline data" (from Harsh Critic):** This mischaracterizes several baselines. TDA and BCA maintain caches of test samples, and Zero uses a theoretically derived entropy threshold—none are purely single-instance in the sense implied. The criticism exaggerates the asymmetry.

- **"The leap from ground-truth loss to pseudo-loss predictor is not adequately justified" (from Harsh Critic):** The paper dedicates Section 4.1 entirely to this justification with visualizations (Figure 2), correlation analysis (Figure 3), and the ceiling experiments. The justification exists; the reviewer may want more, but the claim that it is absent is incorrect.

- **Strength Finder's generic statement about "addressing an important problem":** Removed as generic. Replaced with specific, evidence-backed strengths.

## Novel Insights

The paper's most genuinely novel observation is that a simple regression model trained once on diverse pseudo-labeled data can learn a logits-to-loss mapping that transfers across distribution shifts, enabling confident view selection without any per-instance adaptation. This inverts the standard TTA assumption that confidence estimation must be derived from the test instance alone, and the ceiling TTA experiment provides a crisp, quantified upper bound that prior work had not established.

## Suggestions

- Clarify the composition and construction of ImageVal-12k. If it overlaps with any test set, disclose this and ideally re-run key experiments with a disjoint regression set. If it does not overlap, state this explicitly.
- Report the Spearman or Pearson correlation between the tree's predicted pseudo-loss and true LCE on each test set—this would directly validate whether the regression mechanism works as claimed.
- Tone down claims about "arbitrary distributions" to match the empirical scope ("diverse benchmark distribution shifts" would be accurate).
- Add a brief limitations paragraph discussing dependence on CLIP's pseudo-label quality.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| ML-TTA (BEM) | 75PhjtbBdr | 6.25 | R1/R2 | RTA surpasses ML-TTA on shared benchmarks and has broader evaluation; clearly stronger |
| RLCF | kIP0duasBb | 6.67 | R2 | Comparable in novelty and execution; RLCF extends to more tasks (retrieval, captioning) while RTA is more focused and efficient within classification |
| TTE | 4wk2eOKGvh | 6.50 | R2 | RTA has more novel core mechanism; TTE has cleaner methodology description |
| DeYO | 9w3iw8wDuE | 7.00 | R1/R2 | DeYO has deeper theoretical grounding and equally strong experiments; RTA is below this level |
| DOTA | yD2JMeKumt | 6.00 | R1 | RTA is significantly stronger in experimental breadth and methodological clarity |
| BAT-CLIP | z7PhIgVmZU | 5.50 | R2 | RTA is clearly stronger across all dimensions |
| Weak anchors | various | 2.50 | R1 | Not comparable—these are rejected papers with fundamental flaws |

**Bracket from Round 1:** 5.5–7.0. Round 2 narrowed this by placing RTA above ML-TTA (6.25) and TTE (6.50), comparable to RLCF (6.67), and below DeYO (7.0). The paper's core innovation (regression-based loss prediction for TTA), compelling ceiling analysis, and comprehensive evaluation merit a score near RLCF but with a slight deduction for the undisclosed regression set and missing loss-correlation analysis. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>