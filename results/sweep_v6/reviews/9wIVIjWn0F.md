Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA), a method that replaces entropy-based view selection in CLIP test-time adaptation with a regression model that maps logits to predicted pseudo-label cross-entropy loss. The key insight is that using true label cross-entropy loss for view selection (Ceiling TTA) dramatically outperforms entropy-based selection. The paper trains a LightGBM regressor once on diverse pseudo-labeled data (ImageNet validation set), then uses it to predict which augmented views are most reliable during TTA without any further adaptation. Experiments across single-label, multi-label, and cross-domain benchmarks with two CLIP backbones show consistent improvements over existing entropy-based TTA methods.

## Strengths
- **Powerful oracle experiment convincingly motivates the approach.** Tables 1 and 2 show that using true label cross-entropy (LCE) for view selection yields massive improvements over entropy-based selection — e.g., 90.2% vs. 64.3% on ImageNet-A (ViT-B/16, 64 views), a 25.9-point gap. This establishes a clear upper bound and provides strong motivation for learning a regression mapping from logits to loss.
- **Consistent SOTA results across a wide evaluation suite.** RTA outperforms all prior entropy-based TTA methods (TPT, DiffTPT, Zero, BCA, ML-TTA, etc.) on single-label ImageNet variants (Table 3), 10 cross-domain datasets (Table 4), and multi-label benchmarks (Tables 5-6), with two different CLIP backbones. For ViT-B/16, it achieves 65.84% OOD average vs. next-best 65.03%, and on MSCOCO it reaches 58.95% mAP vs. 57.52%.
- **Simple and practical framework.** The regression model is a lightweight LightGBM decision tree (depth 5, 16 leaves) trained once on 1,000 samples, then applied to any test distribution without per-instance or per-distribution updates. This eliminates the need for complex prompt tuning, diffusion models, or cache-based mechanisms used by existing TTA methods.
- **Good ablation analysis.** Figures 4 and 5 study the effect of number of augmented views and regression training samples, showing graceful scaling and clear saturation points, giving practitioners useful guidance.

## Weaknesses

### Major
- **Asymmetric data usage vs. baselines.** RTA trains its regression model on ImageVal-12k (the ImageNet validation set, 12,000 images), using 1,000 pseudo-labeled samples from it. Every baseline TTA method (TPT, DiffTPT, Zero, BCA, etc.) uses only the test data stream. This is an asymmetric comparison — RTA has access to a large, clean, diverse dataset that the baselines cannot use. The performance gains on ImageNet variants (Table 3) may partially reflect this data advantage rather than the regression formulation per se. The paper should either (a) provide a variant that trains the regressor using only the test stream (e.g., self-supervised on the first batch), or (b) acknowledge this limitation more transparently and discuss whether the gains persist on datasets far outside the training distribution. The strong results on cross-domain datasets (Table 4) partially mitigate this concern, but the experimental setup should be cleaner.

### Minor
- **No comparison to a direct confidence-based selection baseline.** The regression target is the negative log-probability of the pseudo-label class (i.e., essentially a monotonic function of CLIP's maximum softmax probability for that class). A natural baseline is to simply select views with the highest max-softmax probability (or lowest negative log of it) for each test instance — this requires no training at all. The paper does not report this baseline. If it achieves similar or superior performance, the added complexity of the regression framework is unnecessary. The authors should compare against this trivial alternative to isolate the value of the regression model.
- **No direct validation that the regressor predicts true-LCE better than entropy.** The paper's motivating argument is that LCE-based selection beats entropy-based selection, and that RTA approximates this. However, the paper never directly measures whether the regressor's predicted loss correlates with true label cross-entropy loss better than standard entropy does on a held-out set with ground-truth labels. The empirical results (RTA > entropy methods) provide indirect evidence, but a direct correlation analysis would substantially strengthen the central claim.
- **Weak justification for training on original images only.** The regressor is trained on original (unaugmented) images, with the justification that "the original image itself can actually be regarded as a view" (Section 4.2). Augmented views undergo cropping, color jitter, etc., producing logits in different regions of the space. The paper provides no analysis of whether the regressor generalizes from original-image logits to augmented-view logits. An experiment training on augmented views would test whether this is a limiting factor.
- **Training data bias toward high-confidence regions.** The regression training filters samples with CLIP confidence ≥ 0.8, selecting 1,000 out of 5,000 such samples. This biases the regressor toward high-confidence regions. Test instances with low confidence (common in distribution-shifted data) may have logit distributions the regressor never encountered. The authors should analyze how the regressor behaves on low-confidence examples.

### Trivial
- The t-SNE visualization (Figure 2) and Spearman correlation (Figure 3) in Section 4.1 are computed using true labels, while the method uses pseudo-labels. The paper should more clearly delineate this transition and acknowledge that t-SNE visualizations with pseudo-labels would be a fairer demonstration of what the regressor actually learns.

## Nice-to-Haves
- A variant that trains the regressor without any external data (using only the arriving test stream) would make the comparison with baselines perfectly fair and is the most direct way to address the data asymmetry concern.
- Analyzing failure cases where CLIP's argmax is incorrect — does the regressor still assign low predicted loss to views of confidently-wrong images?
- A scatter plot of predicted loss vs. true LCE for augmented views of individual test images would visually validate whether the regressor is learning meaningful structure.

## Removed Points
These points are flagged to be removed; treat them with caution.
1. **"Fundamental disconnect between motivation and method"** (Harsh Critic #1, first half) — The paper is transparent that Section 4.1 analyzes true LCE while Section 4.2 uses pseudo-labels. The Ceiling TTA establishes an upper bound, and the method transparently approximates it with pseudo-labels. This is standard research practice (oracle → surrogate). The paper does not claim the regressor learns true LCE; it explicitly states "pseudo-label cross-entropy loss."
2. **"Spearman analysis is ambiguous about true vs. pseudo labels"** — Section 4.1 is unambiguously about the Ceiling TTA with true labels (it is part of the "Discussion of the Regression Relationship" subsection, which follows from the Ceiling TTA exposition). The context makes this clear.
3. **"Regressor only trained on high-confidence samples, can't handle low-confidence test instances"** — While technically correct, the strong empirical results on diverse test sets (including challenging ones like ImageNet-A with many low-confidence instances) suggest this is not a practical problem. The ablation (Figure 5) also shows that increasing training data improves performance, consistent with the model benefiting from more coverage.
4. **Generic strengths from Strength Finder** — All strengths listed by the Strength Finder were concrete, specific, and verified against the paper, so none were removed.

## Novel Insights
None beyond the paper's own contributions. The reviewers' key observations converge with the paper's framing: the Ceiling TTA experiment is genuinely striking, the method is novel and simple, but the data asymmetry and missing baselines need attention.

## Suggestions
1. Add the direct max-softmax view selection baseline to Tables 3-6. This will either validate the regression model's added value or reveal that simpler alternatives suffice.
2. Report Spearman correlation between the regressor's predicted loss and true LCE on a held-out set, and compare it to entropy vs. true LCE. This directly addresses the central claim.
3. Provide a variant of RTA that trains the regressor on test-stream data only (e.g., pseudo-labeling the first few batches) to enable a fair comparison with online TTA baselines.
4. Clarify the transition from true LCE (Ceiling TTA motivation) to pseudo-label CE (method) in the paper's narrative to avoid any perception of a gap.

## Score and Decision

**Calibration anchors (from retrieval):**
- **RLCF** (`kIP0duasBb.md`, avg 6.67, Accept) — CLIP TTA using RL-based CLIP feedback. Slightly higher score due to cleaner comparison setup and broader task applicability, but RTA matches its empirical breadth with simpler machinery.
- **DOTA** (`yD2JMeKumt.md`, avg 6.00, Reject) — CLIP TTA with distribution estimation. Rejected due to multiple methodological gaps. RTA has clearer methodology and fewer open questions.
- **BAT-CLIP** (`z7PhIgVmZU.md`, avg 5.50, Reject) — Bimodal CLIP TTA. Fatal flaw of using ground-truth labels during test time. RTA does not have this issue.
- **L2C** (`TD3SGJfBC7.md`, avg 6.25, Accept) — Few-shot TTA for CLIP. Comparable novelty level and evaluation thoroughness. RTA's experiments are more comprehensive across task types.
- **Active TTP** (`pdzHpQbGrn.md`, avg 2.50, Reject) — Very weak paper with marginal improvements and unclear novelty. RTA is substantially stronger on all dimensions.
- **ROSITA** (`lF9QXpfNHm.md`, avg 4.67, Reject) — Open-world CLIP TTA with incremental contributions. RTA has clearer novelty and more thorough evaluation.
- **DOTA** (`yD2JMeKumt.md` — note duplicate in different band, avg 6.00) — Already discussed above.

RTA offers a genuinely novel approach to TTA view selection with compelling empirical evidence and conceptual simplicity. The main concerns are the asymmetric data comparison and missing baselines, which are addressable. Comparing to the calibration anchors, RTA sits above the 5.5 reject-tier papers (BAT-CLIP, Active TTP, ROSITA) and is competitive with the 6-6.67 accept-tier papers (RLCF, L2C) on novelty and breadth, though the data asymmetry concern pulls it slightly below the cleanest comparisons.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>