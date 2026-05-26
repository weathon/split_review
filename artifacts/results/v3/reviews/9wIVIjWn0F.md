Now I will write the final consolidated review.

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA), which learns a mapping from CLIP image logits to cross-entropy loss using gradient-boosted decision trees (LightGBM) trained on pseudo-labeled data. During test time, RTA generates augmented views of each test image, predicts the CE loss for each view using the pre-trained regression model, and ensembles the views with the smallest predicted losses. The key claimed advantage is that this regression relationship is learned offline on diverse data and can then be applied to any test distribution without online updates.

## Strengths

1. **The LCE ceiling experiments (Tables 1–2) provide compelling evidence that view selection via true-label cross-entropy loss dramatically outperforms entropy-based selection.** For example, with ViT-B/16 and 64 views on ImageNet-A, LCE achieves 90.2% vs. SE's 64.3% — a gap of ~26 percentage points. This observational finding is a genuine empirical contribution that motivates the core idea.

2. **Consistent accuracy improvements across a wide evaluation suite.** RTA outperforms prior TTA methods on single-label OOD (e.g., OOD average 65.84% vs. Zero's 65.03% with ViT-B/16, Table 3), cross-domain (68.70% vs. BCA's 68.59%, Table 4), and multi-label benchmarks (e.g., MSCOCO mAP 53.25% vs. ML-TTA's 51.58%, Table 5). The improvements are modest but consistent across nearly all datasets and both backbones (RN50 and ViT-B/16).

3. **Practical one-time offline training with no per-instance adaptation overhead.** The LightGBM model is trained once on 1,000 samples and applied to all test distributions without online prompt tuning, memory banks, or per-instance optimization. This is a genuine practical advantage over methods that require per-instance prompt updates (e.g., TPT, RLCF) or dynamic cache management (e.g., TDA).

## Weaknesses

### Major

1. **The trained regression model's predictive quality is never directly evaluated.** The core of the method is a LightGBM model that predicts cross-entropy loss from logits, yet the paper reports no metrics on how well this model actually predicts loss — no MSE, no Spearman correlation between predicted and actual loss, no ranking accuracy for view selection on held-out data. The paper only provides t-SNE visualization (Figure 2) and Spearman correlation analysis (Figure 3) of the *general* logits-loss relationship, not of the *trained* regression model. Without this evaluation, it is unclear whether the regression model is learning the intended LCE mapping, capturing a coarse proxy (e.g., max logit), or working for some other reason. This is a significant evidence gap for a paper whose central claim is that regression-based view selection works.

2. **Unaddressed gap between the motivating LCE ceiling and the actual pseudo-label implementation.** The paper convincingly shows (Tables 1–2) that true-label LCE is dramatically better than entropy, but the actual method uses pseudo-labels obtained by thresholding CLIP confidence at 0.8. The regression model is trained on *pseudo-label* CE, not true LCE. The gap between the oracle LCE ceiling and what the pseudo-label regression achieves is never quantified. Moreover, the regression model is trained on logits from *original* (unaugmented) images but applied to logits from *augmented* views during TTA — a distribution shift that is neither analyzed nor discussed. Without bridging these gaps, the motivational link between the ceiling experiments and the proposed method remains unsubstantiated.

3. **Questionable fairness of some baseline comparisons.** The paper states that "the TTA process follows the settings of Zero and ML-TTA" for its own method, but does not clarify whether all baseline numbers were obtained under identical conditions (same augmentation set, same view count, same ensemble protocol). Several baseline numbers appear to be taken from original publications that may use different protocols. Most concerning: RLCF — a single-label method — is included in the multi-label comparisons (Tables 5–6) where it performs far below even unadapted CLIP (36.87% vs. 47.53% on MSCOCO, RN50), suggesting inappropriate configuration rather than meaningful comparison. This undermines the claimed superiority, particularly for the multi-label results where RTA's gains are largest.

### Minor

4. **Overclaim of generalization to "arbitrary test distributions."** The abstract and conclusion state that RTA "can directly adapt to test instances with arbitrary distributions," but the evaluation is limited to ImageNet variants and 10 cross-domain natural-image datasets. While this set includes some diversity (EuroSAT satellite imagery, DTD textures), it does not approach "arbitrary" — no medical images, no sketch/tactile domains, no non-image sensor data. This claim should be qualified.

5. **No error bars or significance tests.** None of the main results (Tables 3–6) include standard deviations, confidence intervals, or statistical significance tests. Given that some improvements are marginal (e.g., cross-domain ViT-B/16 average: 68.70% vs. 68.59% for BCA, a 0.11% gain), the absence of variance estimates makes it impossible to assess whether these differences are meaningful or within noise. This is a widespread issue in this benchmark area but remains a weakness.

6. **Undocumented "logit-based equal-interval" sampling strategy.** The paper mentions this sampling method in Section 5.1 without any explanation of what it entails or what bias it might introduce. Given that the regression training set is small (1,000 samples from 5,000 high-confidence candidates), the sampling strategy could significantly affect the trained model's coverage and quality.

### Trivial

- None beyond formatting artifacts that are parser issues.

## Nice-to-Haves

- Direct evaluation metrics (MSE, Spearman ρ, ranking accuracy) for the trained LightGBM model's loss predictions on held-out data from both the training source and target domains.
- An ablation of the pseudo-label confidence threshold (0.8) to assess robustness to pseudo-label noise.
- A controlled re-evaluation of all baselines under the same augmentation and ensemble protocol, or at minimum a clear statement of which numbers are from original papers versus re-implemented.
- Inclusion of at least one genuinely out-of-domain test set (e.g., medical or sketch) and retraction of the "arbitrary distributions" claim if it fails there.
- Error bars (3+ seeds) for the main results.

## Removed Points

These points were removed from the main weaknesses during filtering:

1. **Criticism that the paper's central motivation is "severed" by pseudo-labels (from Harsh Critic).** While the pseudo-label gap is real, the motivation chain is not severed — the method still outperforms entropy-based methods, which provides indirect validation. I have preserved this concern in Major #2 but downgraded the framing from "severed" to "unaddressed gap."

2. **Criticism that the LightGBM model's capacity is too limited (max depth 5, 16 leaves) for 1,000-dim logits.** This is speculative — Figure 5 shows diminishing returns with more training data, and a decision tree with limited capacity may actually improve generalization. The paper could justify this choice better, but calling it a capacity problem without evidence is unsupported.

3. **Criticism about "RTA (81.05%) is nearly identical to Zero (80.82%) on ImageNet-R."** This is an overstatement — the 0.23% gap could be noise, but it's only one data point among many, and the overall OOD average (65.84% vs. 65.03%) is larger. This has been incorporated into Minor #5 (no error bars).

4. **Strength from Strength Finder about "thorough analysis of key factors" (Figures 4–5).** The analysis in these figures is basic (varying view count and training sample size) and does not constitute a thorough analysis of the method's components. Moved here.

## Novel Insights

None beyond the paper's own contributions. The observation that LCE-based view selection is an oracle upper bound (Tables 1–2) is genuine, but no reviewer surfaced a novel perspective not already in the paper.

## Suggestions

1. Add a direct evaluation of the trained regression model: report Spearman correlation between predicted and actual (pseudo-label) CE loss on held-out source data and on target domain samples. This is the single most important thing to strengthen the paper.

2. Quantify the gap between the LCE oracle ceiling and RTA's actual performance. Report true-label LCE accuracy alongside RTA's accuracy on the same test sets to show how much of the ceiling is recovered.

3. Re-run all baselines under the same protocol (same augmentations, same view count, same filtering ratio) or clearly state which numbers are from original papers and flag any configuration mismatches. At minimum, remove or re-evaluate RLCF for multi-label.

4. Add error bars (at least 3 random seeds) to the main tables. Without them, marginal improvements cannot be interpreted.

5. Replace "arbitrary test distributions" with a more accurate qualifier (e.g., "diverse natural-image distributions") to avoid overclaiming.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>