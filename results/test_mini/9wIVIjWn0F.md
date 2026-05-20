Now I have all the information I need. Let me compose the final consolidated review.

## Calibration Anchors

Let me list all anchor papers from the retrieval batch:

1. **HeGMugkCOH** (avg 3.00, rejected) — "Continuous TTA of VLMs." Had mismatch between claimed setting and experiments. RTA has more systematic experiments but a more fundamental methodological flaw.

2. **nErnNhJx2o** (avg 4.00, withdrawn/rejected) — "SOBA: training-free TTA via geometric transformation." Poorly motivated, limited analysis. RTA is better motivated and has broader experiments, but its core method is mathematically redundant.

3. **CLUvRxQXtf** (avg 4.67, rejected) — "CLIP-TTA: dual regularization." Incremental but solid experiments. RTA has broader experiments but a more severe methodological issue.

4. **dHj8hC081K** (avg 4.50, accepted poster) — "ADTE: Adaptive Debiasing Tsallis Entropy." Modest gains, some ad-hoc design, but accepted. RTA has similar experimental scope but a more fundamental issue (redundant computation).

5. **S90g7NE88b** (avg 5.00, accepted poster) — "FGA: Flatness-Guided Adaptation." Novel idea, some theoretical concerns. RTA is less novel and has a more serious methodological issue.

6. **7kLNGaAHaw** (avg 5.50, accepted poster) — "PEA: Architecture-Agnostic TTA." Well-motivated, strong analysis. RTA is weaker in motivation and analysis.

7. **1c6Ao3CpKt** (avg 6.80, accepted poster) — "Specialization after Generalization." Strong theory paper. RTA doesn't compare at this level.

The accepted papers in this area (scores 4.50–5.50) have issues like modest gains, ad-hoc components, or incomplete analysis — but none have a core mechanism that reduces to computing a known closed-form function without acknowledging it. RTA's flaws are more fundamental than those in the accepted papers but less severe than the purely rejected ones.

---

## Final Consolidated Review

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA) for CLIP-based image classification. The core idea is to train a LightGBM decision tree on ImageNet validation data to predict pseudo-label cross-entropy loss from logits, then use this tree at test time to select confident augmented views (those with lowest predicted loss) for ensembling. The method trains once offline and then applies to arbitrary test distributions without updates. Experiments span single-label, multi-label, and cross-domain benchmarks, showing consistent improvements over entropy-based TTA methods like Zero and BCA.

## Strengths

- **Comprehensive evaluation across diverse settings.** RTA is evaluated on single-label (ImageNet variants + 10 cross-domain datasets), multi-label (MSCOCO, VOC2007, NUSWIDE), and two architectures (RN50, ViT-B/16). The consistent improvements over a large set of baselines (Tables 3–6) suggest the underlying selection criterion is effective.

- **Ceiling TTA analysis (Tables 1, 2) provides a clean upper bound.** The observation that selecting views with ground-truth cross-entropy loss yields massive gains (e.g., 90.2% on ImageNet-A with ViT-B/16 and 64 views vs 64.3% for entropy) cleanly motivates the pursuit of better selection criteria.

- **Practical efficiency.** The regression model uses LightGBM trained on only 1,000 samples (max depth 5, 16 leaves) with negligible inference overhead. The once-trained, never-updated paradigm is appealing for deployment.

- **Strong results on multi-label benchmarks.** Improvements of +1.43–1.67 mAP over ML-TTA on MSCOCO and +1.47–1.58 on VOC2007 are the largest gains in the multi-label setting, which is less explored in prior TTA work.

## Weaknesses

### Fatal
None. The method is not fundamentally broken, but its presentation suffers from significant overclaim.

### Major

- **The regression model is trained to approximate a function that can be computed exactly in closed form.** The regression target (pseudo-label cross-entropy loss, Eq. 4) is exactly ℒ = −log(max_k softmax(s_k)) — a deterministic function of the logits. The pseudo-label is the argmax (obtained by high-confidence filtering), so the loss is simply the negative log of the maximum softmax probability. A decision tree that approximates this function can only be *worse* than computing it directly. The paper never acknowledges this redundancy. The method should be compared against the trivial baseline of directly computing −log(max softmax) for each view and selecting the top-k. Without this comparison, the claimed gains over entropy-based methods may simply reflect that max-softmax confidence is a better selection criterion than entropy — a finding that has nothing to do with the regression machinery and would make the paper's framing as a "regression" contribution misleading.

- **The method cannot, as described, handle datasets with different class label sets.** The regression tree is trained on 1000-dimensional logit vectors (ImageNet-1k classes). The experiments include datasets with entirely different class counts: Pets (37), Flowers (102), Aircraft (100), DTD (47), EuroSAT (10), Cars (196), Food (101), SUN (397), and Caltech (256), as well as multi-label datasets MSCOCO (80), VOC2007 (20), and NUSWIDE (various). The paper never specifies how a tree trained on 1000-dim features processes logit vectors of different dimensionality. If the tree is retrained per dataset, the claim of "trains once and adapts to any test distribution without updates" is false. If it is applied directly to mismatched-dimensionality inputs, the procedure is undefined. This makes the cross-domain (Table 4) and multi-label (Tables 5, 6) results unverifiable under the described procedure.

- **The paper omits the most important baseline: direct confidence-based (max softmax) view selection.** Since the regression target is deterministically computable from logits, RTA should be compared against simply computing −log(max softmax) for each view and selecting the top-k. This baseline is computationally cheaper (O(L) vs. a tree traversal), mathematically exact, and would isolate whether the contribution is (a) the regression model itself, or (b) the discovery that max-softmax confidence beats entropy for view selection. If (b), the paper is about a different contribution than claimed, and the regression model is unnecessary overhead.

### Minor

- **No error bars, standard deviations, or statistical significance tests.** Many reported improvements are small (e.g., +0.24% on IN-1k for ViT-B/16 over Zero, Table 3; many cross-domain deltas under 1%). Without error bars, it is unclear whether these differences are meaningful or within noise.

- **The Ceiling TTA analysis uses true-label loss, but the regression is trained on pseudo-label loss.** The t-SNE visualization (Figure 2) and Spearman correlation (Figure 3) use ground-truth label cross-entropy loss, not pseudo-label loss. The gap between the two is not analyzed, so the visualization does not directly support the regression model's target.

- **The regression model is trained only on high-confidence samples (confidence ≥ 0.8) but evaluated on all views, including low-confidence ones during TTA.** The paper does not analyze how the regression tree behaves on out-of-distribution or low-confidence logits.

- **The Spearman correlation analysis (Figure 3) only examines the top 10 logit features**, but the regression tree takes all L logits as input. The analysis does not show that the remaining L−10 features are uninformative, nor does it justify the tree's ability to capture relationships across the full logit vector.

### Trivial
None.

## Nice-to-Haves

- An ablation that replaces the regression tree with the exact computation of −log(max softmax) and compares performance. If results are identical, the tree is superfluous. If the tree performs worse, it is harmful.
- An analysis of how the regression model's prediction error varies across OOD views (e.g., views from ImageNet-A when trained on ImageNet-1k).
- A quantification of the gap between true-label LCE (used in Ceiling TTA) and pseudo-label LCE (used in RTA) to better connect the motivation to the method.

## Removed Points

- **Criticism about framing of Figure 1/Introduction.** The harsh critic claims the framing is "misleading" because the regression is "a complex way of approximating a simple closed-form computation." This is a restatement of the redundancy issue already listed as a major weakness, not a separate point.
- **Criticism about Section 4.2 (distribution shift between original images and augmented views).** While the paper does not analyze this, the claim that the regression may not transfer is speculative without evidence. Weakness removed as insufficiently substantiated.
- **Complaint about "no error bars."** Moved to Minor (it is listed there), as this is a common limitation in this line of work and not unique to this paper.
- **Strength Finder's claim that "state-of-the-art performance" is a core strength.** This is a restatement of experimental results, not an independent strength. However, kept in spirit under the comprehensive evaluation point.
- **Strength Finder's generic claim about "computational efficiency."** Already subsumed under the practical efficiency strength.
- **Strength Finder's claim about "ablation studies provide practical insights."** This is a minor supporting detail, not a core strength, and conflicts with the missing ablation (direct confidence baseline).

## Novel Insights

The reviews surface a central tension: the paper's empirical contribution (showing that max-softmax confidence works better than entropy for view selection in CLIP TTA) may be valid and useful, but it is presented as a "regression" contribution that is mathematically redundant. The harsh critic correctly identifies that the regression target is a closed-form function of the input, making the decision tree an unnecessary approximation of a known quantity. The missing baseline (direct confidence selection) is not a minor oversight — it is the linchpin for interpreting every experiment in the paper. Meanwhile, the strength finder correctly notes the breadth and consistency of the empirical results. The resolution requires either (a) adding the missing baseline and honestly reframing the contribution as "confidence-based view selection for CLIP TTA" (in which case the regression tree should be removed in favor of direct computation), or (b) demonstrating that the regression tree provides some robustness or generalization benefit that direct computation does not — a claim the paper currently makes no attempt to support.

## Suggestions

1. **Add the missing baseline**: Compare RTA against directly computing −log(max softmax) for each view and selecting the top-k. This is the single most important experiment and should be the top priority.
2. **Address the cross-domain label space issue**: Either (a) describe how the regression tree handles variable-dimensional logits (e.g., by zero-padding, retraining per dataset, or using per-logit features), or (b) retract the claim of "trains once, adapts to any distribution" and report the cost of per-dataset retraining.
3. **Reframe the contribution honestly**: If direct confidence selection works as well as RTA, the paper should be repositioned as an analysis paper showing that max-softmax confidence outperforms entropy for CLIP TTA view selection, with the regression model removed or presented only as an implementation detail.
4. **Add error bars** for the main results, especially where improvements are <1%.
5. **Analyze the gap between true-label LCE and pseudo-label LCE** to better connect the Ceiling TTA motivation to the actual method.

## Score and Decision

MY FINAL SCORE: 4.0
MY FINAL DECISION: Reject