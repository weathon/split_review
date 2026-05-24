Now I have a clear picture of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA), a method that replaces entropy-based view selection in CLIP test-time adaptation with a learned regression tree. The tree is trained once offline on pseudo-labeled ImageNet data to predict cross-entropy loss from logit vectors, then used at test time to select the most confident augmented views. The key insight — that a learnable mapping exists between logit patterns and true loss, and that this mapping can be exploited for view selection — is well-motivated by ceiling experiments and t-SNE/Spearman analyses. RTA achieves consistent improvements over entropy-based TTA methods across single-label, cross-domain, and multi-label benchmarks with negligible online cost.

## Strengths

- **Ceiling TTA provides compelling motivation (Section 4.1).** Tables 1 and 2 demonstrate that using ground-truth label cross-entropy loss for view selection yields massive gains over entropy (e.g., ViT-B/16 on ImageNet-A: 64.3% entropy → 90.2% label loss with 64 views). This directly motivates the regression-based approximation and establishes a clear upper bound.

- **The regression relationship is empirically grounded.** t-SNE visualizations (Figure 2) reveal structural correlation between logit distributions and normalized label loss. Spearman's rank analysis (Figure 3) shows statistically significant monotonic relationships between top logit features and loss. This provides rigorous support for using a regression model.

- **RTA achieves consistent, state-of-the-art improvements on standard benchmarks.** On ImageNet variants (Table 3), RTA sets new OOD average records for RN50 (49.24% vs. 46.98% BCA) and ViT-B/16 (65.84% vs. 65.03% Zero). On cross-domain datasets (Table 4), it attains the highest average accuracy for both backbones (RN50 61.78%, ViT-B/16 68.70%). The gains are particularly pronounced on RN50.

- **The method is lightweight and practical.** Training requires only ~1,000 pseudo-labeled samples (Figure 5), uses a small decision tree (LightGBM, max depth 5, 16 leaves), and requires no online adaptation or gradient computation. This makes RTA genuinely easy to deploy compared to methods requiring per-sample prompt optimization.

## Weaknesses

### Major

- **Class-dimension mismatch for cross-domain and multi-label settings is unresolved.** The regression tree is trained on 1,000-dimensional ImageNet logits (Section 5.1: "ImageVal-12k as the regression mapping data"), but at test time it must receive logit vectors computed over the test task's class set — which differs in size and semantics for cross-domain (e.g., 37 Pet classes, 102 Flower classes) and multi-label datasets. The paper claims the mapping is "independent of any downstream classification task" (line 388) but never explains how a tree expecting 1,000-dimensional input operates on differently-sized vectors. This is not a minor omission: it is a structural description gap that makes the cross-domain (Table 4) and multi-label (Tables 5–6) results uninterpretable as presented. The most plausible resolution (computing ImageNet-class logits for view selection while classifying over target-class logits) is reasonable but must be stated and justified, since the predicted loss would then be a proxy for view quality on a *different classification task* — an assumption that requires validation.

- **Multi-label adaptation is not described.** The regression target is softmax cross-entropy loss of a single pseudo-label (Eq. 4), which assumes mutually exclusive classes. Multi-label classification (Tables 5–6) has no single ground-truth class and uses mAP, not softmax cross-entropy. The paper states it "follows ML-TTA" settings but does not explain how the single-label regression framework is adapted. Without this explanation, the multi-label results — while empirically positive — cannot be assessed for validity.

### Minor

- **Gains on ViT-B/16 are modest relative to the oracle ceiling.** On ViT-B/16 ImageNet-1k, RTA achieves 71.13% vs. Zero's 70.89% (a 0.24% gain), while the oracle ceiling is 89.0% (Table 2). The gap between RTA and the oracle (17.9%) dwarfs the gain over entropy (0.24%). This raises the question of how much of the regression signal is genuinely capturing view-loss structure versus serving as a slightly improved entropy proxy. The paper would benefit from an analysis of where the regressor agrees/disagrees with the oracle.

- **Training on original images, testing on augmented views.** Section 4.2 argues that "the original image itself can actually be regarded as a view" to justify training the regressor on unaugmented images only. However, TTA augmentations include substantial color, spatial, and geometric transformations that can shift the logit distribution. While the empirical results suggest the transfer works, the paper offers no analysis of this distribution shift or an ablation with augmented-view training.

- **The "free lunch" framing is somewhat misleading.** The regression mapping requires an external dataset (ImageVal-12k) and pseudo-label filtering, which involves design choices (confidence threshold ≥ 0.8, logit-based equal-interval sampling) that are not cost-free. The baselines (TPT, Zero, BCA) operate on the test stream alone without auxiliary data. While the offline nature of the regression training makes this a reasonable design, the paper overstates the "freeness" of the approach.

- **Limited analysis of regression failures.** The large gap between RTA and the oracle ceiling (Tables 1–2 vs. Table 3) is never discussed. Understanding where the regression tree fails (e.g., which types of views or classes it confuses) would substantially strengthen the paper and help contextualize the modest ViT-B/16 gains.

### Trivial

- Table 4 lists "TDA [CVPR 2024]" twice with different numbers for ViT-B/16, likely a typographical duplication.
- The "logit-based equal-interval" sampling procedure for selecting the 1,000 regression samples is not defined.
- No limitations section is included, which would be appropriate given the reliance on an external regression set and the unresolved class-set questions.

## Nice-to-Haves

- Analyze where the regressor disagrees with the oracle label loss to characterize failure modes and explain the ceiling gap.
- Ablate the regression model choice (LightGBM vs. linear regression vs. MLP) to understand whether the decision tree structure is essential.
- Study the effect of the pseudo-label confidence threshold (0.8) on the learned mapping.
- Train the regressor on augmented rather than original images and compare.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Fatal mismatch" claimed as fatal (Harsh Critic Issue 1):** The class-dimension concern is valid and kept as Major, but the critic's framing as "fatal" and "structurally unusable" is too strong. A straightforward resolution exists (computing ImageNet-class logits for view selection separately from target-class logits for classification), and the empirical results across cross-domain datasets suggest the method does work. The paper's failure to describe this is a significant weakness, not a fatal flaw.

- **"Unfair comparison with prior TTA methods" (Harsh Critic Issue 2):** REMOVED. The regression tree is trained offline on pseudo-labeled data using CLIP's own predictions — this is analogous to how all methods benefit from CLIP's pre-training on 400M image-text pairs. The tree is applied as a fixed function at test time with no further updates. Demanding that baselines receive the same external data misunderstands that RTA's offline training is part of its method design, not an unfair advantage. The "free lunch" language is overclaimed (kept as Minor) but the comparison itself is fair.

- **Spearman analysis showing varying correlation directions (Harsh Critic note):** REMOVED. The paper correctly reports that different features show positive and negative correlations — this is expected and does not undermine the regression approach, which can model both.

- **"TDA listed twice" as evidence of carelessness:** Kept as Trivial only. This is a table formatting issue, not a methodological concern.

- **Strength Finder claim that "RTA effectively handles multi-label classification":** PARTIALLY REMOVED. The results show improvement, but the mechanism is undescribed (see Major weakness). The strength is demoted from supporting evidence to an empirical observation that requires methodological justification.

- **Strength Finder's "the regression relationship is grounded in empirical evidence" from t-SNE:** Kept but qualified — the t-SNE and Spearman evidence is valid for ImageNet-class spaces but does not directly validate cross-class-set generalization.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a regression mapping between logits and loss can be learned offline and applied for view selection — is genuinely novel within the TTA-for-VLMs literature, which has been dominated by entropy-based approaches.

## Suggestions

- **Explicitly describe the class-set handling for cross-domain and multi-label settings.** If ImageNet-class logits are computed for regression-tree input while target-class logits are used for final classification, state this clearly and discuss why the predicted loss transfers. If a different mechanism is used, describe it.
- **Add a limitations paragraph** acknowledging the reliance on an external regression set, the class-set dependency, and the gap to the oracle ceiling.
- **Analyze regressor-oracle agreement** to understand where and why the regression approach falls short of the ceiling.
- **Define the "logit-based equal-interval" sampling** used to select the 1,000 regression samples.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison to RTA |
|---|---|---|---|
| DOTA (yD2JMeKumt) | 6.00 (Reject) | R2 | RTA has a more novel core idea (regression vs. distribution estimation) and stronger results, but shares a significant methodological description gap. RTA is comparable or slightly stronger. |
| ML-TTA (75PhjtbBdr) | 6.25 (Accept) | R1 | RTA's regression paradigm is more novel than extending entropy to multi-label, and RTA has broader evaluation. But ML-TTA has clearer method description. RTA is comparable. |
| L2C (TD3SGJfBC7) | 6.25 (Accept) | R2 | Different setting (few-shot TTA), but similar novelty level and empirical strength. RTA has a cleaner method; L2C has fewer description gaps. Comparable. |
| RLCF (kIP0duasBb) | 6.67 (Accept) | R1 | RLCF has broader task applicability (3 tasks) and cleaner description. RTA is more lightweight but limited to classification. RTA is somewhat weaker. |

**Round 1 bracket:** 5.5–6.67. RTA sits clearly above the low-band rejects (2.0–3.5) and below the high-band analysis papers (8.0). Within the middle band, it is closest to DOTA, ML-TTA, and RLCF.

**Round 2 narrowing:** DOTA (6.00, rejected for methodological gaps), ML-TTA (6.25, accepted), L2C (6.25, accepted), RLCF (6.67, accepted). RTA has a more novel core contribution than DOTA and ML-TTA but a significant unresolved description gap (class-dimension mismatch, multi-label adaptation). RTA is stronger than DOTA (6.00) but weaker than RLCF (6.67). It is comparable to ML-TTA (6.25) — a slightly more novel idea offset by a less complete method description.

**Final score: 6.0.** The paper introduces a genuinely novel and well-motivated regression-based view selection paradigm for TTA, supported by strong ceiling analysis and solid empirical results. However, the failure to explain how the regression tree handles class-set mismatches for cross-domain and multi-label settings is a significant gap that undermines the central claim of task-independence. This is addressable in rebuttal but cannot be ignored in its current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>