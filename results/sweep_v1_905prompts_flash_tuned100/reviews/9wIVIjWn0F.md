Now I have enough information. Let me write the final consolidated review.

## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA) for CLIP image classification. The authors first observe that using ground-truth label cross-entropy loss (LCE) for view selection dramatically outperforms standard entropy-based selection (SE) — an 18.4% gap on ImageNet with ViT-B/16. They then train a LightGBM regression model on pseudo-labeled images from ImageVal-12k (1000 samples, with pseudo-labels from CLIP predictions ≥ 0.8 confidence) to predict pseudo-LCE from view logits, and select views with the lowest predicted loss during TTA. Experiments across single-label, multi-label, and cross-domain benchmarks show consistent improvements over prior TTA methods.

## Strengths

1. **Clear discovery of LCE superiority over entropy for view selection (Tables 1-2).** The ceiling TTA analysis demonstrates that using true labels for view selection yields 14-35% absolute gains over entropy-based selection across multiple datasets and both architectures. This is a well-motivated, clearly demonstrated finding that provides a strong upper bound and rationale for the regression approach.

2. **Consistent improvements across diverse benchmarks.** RTA outperforms prior methods on single-label (Table 3, e.g., RN50 OOD average 49.24% vs. BCA's 46.98%), cross-domain (Table 4, e.g., ViT-B/16 average 68.70% vs. BCA's 68.59%), and multi-label classification (Tables 5-6, e.g., RN50 MSCOCO 53.25% mAP vs. ML-TTA's 51.58%). The method is evaluated on 15+ datasets with two architectures, demonstrating breadth.

3. **Simple and practical method.** The approach is lightweight — training a single LightGBM model on 1,000 samples, with no per-instance optimization or test-time parameter updates. The inference overhead (tree prediction per view) is negligible compared to computing CLIP features. The one-time training / any-test-time-use paradigm is practically appealing.

4. **Ablation studies on design choices (Figures 4-5).** The paper studies the effect of the number of augmented views (saturating around 128) and the number of regression training samples (nearly saturating at 5k), providing practical guidance for deployment.

## Weaknesses

### Major

1. **The core regression mapping is not directly validated.** The entire method rests on the premise that a regression model trained on pseudo-label CE loss can reliably predict the true label CE loss for arbitrary test views. Yet the paper provides no direct quantitative evidence of this: no scatter plot of predicted vs. true loss, no aggregate R² or Spearman correlation coefficient between the model's predicted loss and actual loss on held-out data, and no per-view analysis comparing RTA's selected views to those selected by true LCE. The t-SNE visualization (Figure 2) is qualitative, and the Spearman analysis (Figure 3) examines individual logit features on only 2 examples per dataset, not the full regression model's predictions. Without this validation, the paper's central mechanism operates as a black box.

2. **The gap between Ceiling TTA and RTA is large and unacknowledged.** On ImageNet with ViT-B/16 (64 views): Ceiling LCE = 89.0%, vanilla SE = 70.6%, RTA = 71.13%. RTA recovers only ~0.5% of the 18.4% gap between SE and LCE. Similar patterns hold across datasets (e.g., IN-A: Ceiling 90.2%, RTA 65.65%, SE 64.3%). The paper never discusses why the regression approximation recovers so little of the LCE ceiling — is the issue pseudo-label noise, model capacity, or distribution mismatch? This is a critical diagnostic that should inform the reader about the method's fundamental limitations.

### Minor

3. **No variability or statistical significance estimates.** No standard deviations, confidence intervals, or significance tests are reported for any result. Given that many margins over the best prior methods are <1% (e.g., +0.24% on IN-1k, +0.23% on IN-R for ViT-B/16), it is impossible to assess whether these differences are meaningful.

4. **No comparison to a simple max-softmax baseline.** The paper compares against sophisticated methods (TPT, DiffTPT, Zero, BCA, etc.) but never includes the simplest view-selection baseline: pick views with the highest softmax confidence. This would help isolate whether the regression model adds value beyond trivial alternatives.

5. **Pseudo-label threshold not ablated.** The threshold of 0.8 for high-confidence CLIP predictions is not varied or analyzed. This choice introduces selection bias (training on only confident samples) that could limit regression quality in low-confidence regions where it is most needed.

### Trivial

6. Figure 4's y-axes have different ranges for IN-1k (69-71.5) and variant (63.5-66), which makes the relative performance comparison visually misleading.

## Nice-to-Haves

- Compare against a linear regression model to justify the need for non-linear tree models.
- Compare against alternative regressors (e.g., random forest, MLP).
- Report computational cost: training time for LightGBM and inference overhead per view.
- Ablate the pseudo-label confidence threshold (e.g., 0.7, 0.9, no filtering) and analyze its effect.
- Include a per-view analysis showing that RTA's selected views are closer to true LCE-selected views than entropy-selected views.

## Removed Points

- **"The experimental setting deviates from standard TTA, invalidating comparison with prior methods."** This is too strong. The paper clearly describes its offline training phase, and several prior TTA methods for VLMs (TDA, BCA) also use cache/memory mechanisms. The comparison is not invalidated; the setting is different and should be acknowledged, but it does not negate the results.

- **"Practical gains are marginal and not justified."** This is overstated. For RN50, gains are meaningful (+2.26% OOD avg, +5.73% on IN-A). For multi-label, gains are 1.43-3.18% mAP. The ViT-B/16 gains are modest but consistent across all datasets. The claim of "within noise" is speculative without variance estimates.

- **"ImageVal-12k is not diversely distributed — it's the same distribution as pre-training data."** ImageNet has 1000 diverse classes, and the cross-domain results show the regression generalizes well across distribution shifts (IN-A, IN-R, cross-domain sets). This is evidence of diversity, not a flaw.

- **"Why LightGBM over other regressors?"** This is an ablation the paper could run but doesn't need to justify in the main text — using a standard gradient-boosted tree is a reasonable engineering choice.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the regression directly.** On a held-out set, compute the Spearman rank correlation (or R²) between the LightGBM model's *predicted loss* and the *actual label cross-entropy loss*. Show a scatter plot. This is necessary to establish that the core mechanism works as claimed.

2. **Analyze the gap to Ceiling TTA.** Explain why RTA recovers so little of the LCE ceiling. Breakdown by prediction confidence bins (e.g., how does RTA perform on samples where CLIP is confident vs. uncertain?) to identify failure modes.

3. **Report standard deviations** for at least the key results in Table 3.

4. **Add a max-softmax baseline** as a simple sanity check for whether the regression provides value beyond the cheapest alternative.

## Score and Decision

**Bracket (Round 1):** I initially bracketed the paper between 3.5 and 7.5 — clearly stronger than broken/weak papers (avg <3.5) and clearly not at the level of outstanding papers (avg >7.5).

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ML-TTA (75PhjtbBdr) | 6.25 | 1,2 | Accepted. Solves a genuinely novel problem (multi-label TTA). RTA has broader experiments but a more conventional setting and weaker validation of core mechanism. RTA is weaker. |
| RLCF (kIP0duasBb) | 6.67 | 1,2 | Accepted. Novel RL+CLIP feedback framework across 3 tasks. Better validated core mechanism. RTA is weaker. |
| BaFTA (KNtcoAM5Gy) | 5.50 | 1,2 | Rejected. Similar level — simple method, comprehensive experiments, some methodological gaps. RTA is comparable but has a stronger empirical discovery (LCE ceiling tables). |
| DOTA (yD2JMeKumt) | 6.00 | 2 | Rejected despite good scores. Strong evaluation but concerns about core assumptions. RTA has a different (but comparable) profile of strengths/weaknesses. |
| ROSITA (lF9QXpfNHm) | 4.67 | 2 | Rejected. Incremental technical contribution, incomplete baseline comparisons. RTA is clearly stronger (more novel finding, broader evaluation). |
| BaFTA-style (G9Ea7mlqGO) | 3.80 | 2 | Rejected. Weak contribution, unclear methodology. RTA is substantially stronger. |

**Narrowing (Round 2):** After reading BaFTA (5.50, rejected) and DOTA (6.00, rejected) in full, I compared RTA against these. RTA is slightly weaker than DOTA (which had a more novel problem framing — continual distribution estimation) but comparable to BaFTA. However, RTA's missing validation of the core regression mapping is a more fundamental gap than BaFTA's issues (experimental setting mismatches, insufficient ablations). RTA is stronger than ROSITA (4.67). I place RTA between ROSITA (4.67) and BaFTA (5.50), closer to BaFTA.

**Final score:** 5.0. The paper has a genuinely interesting finding (LCE >> SE) and a practical method with broad experiments. However, the central mechanism — that a regression model can predict pseudo-LCE for view selection — is not directly validated, and the gap to the LCE ceiling is large and unanalyzed. These are significant gaps that prevent acceptance as written.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>