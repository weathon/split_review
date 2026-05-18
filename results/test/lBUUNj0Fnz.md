Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes an active learning framework for semantic segmentation that uses binary (yes/no) queries about the presence or absence of a semantic class in an image, rather than requiring expensive pixel-level or region-level annotations. The authors formulate the selection of informative (image, class) pairs as a constrained optimization problem balancing class-presence uncertainty and image redundancy, and solve it via a linear programming relaxation. Experiments on FlickrLandscapes, Cityscapes, and PASCAL VOC12 show that the method achieves mIoU within ~0.5% of pixel-level methods while requiring roughly 100× less annotation time according to a small user study.

## Strengths

1. **Novel binary query formulation for segmentation AL.** The paper introduces the first active learning framework for semantic segmentation that poses binary (yes/no) queries about class presence, rather than requiring pixel-level or region-level annotations. This is a well-motivated and practically important idea — the abstract and contributions explicitly claim novelty, and the related work section correctly situates this against prior binary-query AL methods that address classification, not segmentation.

2. **Dramatic annotation time reduction with competitive accuracy.** The user study (Table 1) shows binary queries take ~4 seconds versus 37.5 minutes for pixel-level annotation on Cityscapes. Table 3 calculates ~5.56 hours total annotation time for the binary method versus ~750 hours for pixel-level methods. Despite this >100× reduction, Table 2 shows the binary method achieves mIoU within 0.5% of pixel-level methods (75.96 vs 76.21 on PASCAL VOC). This accuracy-efficiency trade-off is the paper's strongest empirical result.

3. **Principled optimization approach.** The batch selection is formulated as a constrained optimization problem (Equation 4) with a linear programming relaxation (Theorem 1), providing a systematic, non-heuristic method for selecting (image, class) pairs based on uncertainty and diversity criteria. The formulation with per-image class caps (C_max) is a sensible practical design choice.

4. **Multi-backbone validation.** Experiments with ResNet-101, Xception, and ResNet50 backbones (Section 4.7) show the binary method consistently outperforms the binary-level baselines (RR, EE) and remains competitive with pixel-level methods, demonstrating robustness to architecture choice.

5. **User study quantifying annotation burden.** The multi-annotator user study (Section 4.5) measures both time and perceived difficulty for pixel-level, region-level, and binary-level annotations across all three datasets, providing concrete evidence that the binary annotation mode is less burdensome in practice (binary queries received the highest ease rating of 10/10 consistently).

## Weaknesses

### Fatal

None.

### Major

- **The binary-level baselines (RR, EE) are too weak to properly validate the LP formulation's added value.** RR is random, and EE selects images by an unspecified entropy criterion and classes by prediction entropy. The paper does not compare against natural stronger baselines such as: (a) greedy per-class uncertainty sampling (selecting (image, class) pairs by class-presence entropy alone, ignoring redundancy), (b) uncertainty sampling with the LP objective but λ=0 (which would isolate the contribution of the redundancy term), or (c) random selection weighted by uncertainty scores. Because the paper's technical contribution is the LP-based selection algorithm, the absence of these comparisons leaves it unclear how much the LP formulation adds over simpler heuristics. The pixel-level and region-level comparisons demonstrate the value of the binary *modality* but do not validate the *selection algorithm* itself. This is the most significant weakness in the paper.

### Minor

- **No sensitivity analysis for key hyperparameters λ, C_max, and α.** All experiments use λ=1, C_max=5, α=1 with no ablation. Since λ governs the trade-off between uncertainty and redundancy, C_max determines query distribution across images, and α scales the confidence values, the sensitivity of results to these choices is unknown. For example, if the method's advantage over EE vanishes when C_max=10 or when λ=0, the contribution of the LP formulation would be substantially weaker. A sensitivity study on at least one dataset would meaningfully strengthen the paper.

- **User study lacks variance reporting and annotator details.** The study uses 10 images × 3 annotators (30 measurements per condition), which is a reasonable starting point, but no standard deviations or confidence intervals are reported for the annotation times. Without variance, it is impossible to judge whether the large differences (e.g., 37.5 min vs 4 sec) are statistically reliable or whether the multiplicative totals in Table 3 could be sensitive to outliers. Additionally, the paper does not describe whether annotators were experts or novices, or whether the pixel-level annotation task required labeling all classes or a subset.

- **The EE baseline is vaguely described.** The paper states EE selects images "based on the entropy of the underlying model" but does not specify whether this entropy is average pixel entropy (as used for pixel-level Entropy) or another definition. Similarly, "class prediction entropy" for class selection is not explicitly tied back to the H_ij formulation in Equation (1).

- **No analysis of the rounded LP solution quality.** The rounding procedure (selecting the B highest entries in M) is described briefly, but the paper does not analyze the optimality gap between the continuous LP solution and the rounded integer solution, nor the stability of the rounded solution across random seeds or AL iterations. While this is unlikely to be fatal, it would strengthen the technical contribution to show the rounding does not degrade solution quality substantially.

- **Cold-start issue not discussed.** The redundancy term uses cosine similarity on deep features from the current model. Early in AL when the model is trained on very few (initially 1) labeled images, these features may be poor, and the redundancy signal may be unreliable. The paper does not discuss this or whether the redundancy term helps or hurts in early iterations.

- **Computational overhead of LP solving not reported.** The paper mentions GPU-based parallel algorithms as future work but does not report actual LP solve times, which is relevant to practical feasibility.

### Trivial

- The rounding procedure description (line 100) has a step number gap (step 4 is missing between steps 3 and 5 in Algorithm 1).

## Nice-to-Haves

- A small-scale optimality check: for a tiny subset (e.g., 50 images, 10 classes, budget B=10), compute the exact integer solution via brute force or MILP and compare the LP+rounding solution's objective value, to ground the approximation.
- A time-budget-controlled comparison that re-analyzes the results using estimated annotation time on the x-axis instead of iteration number (using the user study estimates to convert queries to time, even acknowledging uncertainty).
- Report LP solve times to establish practical feasibility.
- Discuss how signals from binary responses are incorporated into model updates (referenced to Section F which was not in the provided text).

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The optimization problem ... contains the constraint v_i = min(1, (M.e)_i), which is non-linear and non-convex ... proof is relegated to the appendix (Section A, not provided). Without seeing the derivation, it is impossible to assess..."** — Removed per hard rules: the parser strips appendix sections; the proof exists in the original submission. Criticizing a missing appendix that was present in the original paper is not a valid weakness.
- **"The paper would be much stronger if it included a cost-benefit plot (mIoU vs. estimated time)"** — This is a reasonable suggestion (moved to Nice-to-Haves) but framed as a weakness rather than an enhancement.
- **"The paper does not discuss whether their framework reduces to standard image-level binary AL if one sets the segmentation model to a classifier"** — Asking the paper to address a hypothetical reduction to a different problem (classification vs. segmentation) is outside the paper's scope.

## Novel Insights

None beyond the paper's own contributions. The reviews align on the paper's core strengths (novelty of binary query modality for segmentation, dramatic efficiency gains) and converge on the same core weakness (the LP-based selection algorithm is not adequately validated against sufficiently strong binary-level heuristics). The primary tension is between admiring the practical promise of the idea and demanding stronger evidence for the technical contribution of the optimization formulation.

## Suggestions

1. **Add stronger binary-level baselines.** The most critical addition is to compare against a greedy baseline that simply selects (image, class) pairs by class-presence entropy alone (ignoring redundancy), and against the proposed LP objective with λ=0 (uncertainty only). This would isolate the contribution of the LP formulation and the redundancy term.

2. **Conduct a sensitivity study** for λ (e.g., {0, 0.1, 0.5, 1, 5, 10}) and C_max (e.g., {1, 3, 5, 10}) on at least one dataset (e.g., Cityscapes) to show the method's robustness to these choices.

3. **Report variance** (standard deviation or confidence intervals) for the user study annotation times. Even acknowledging the small sample size and describing annotator background would improve the credibility of the time estimates.

4. **Clarify the EE baseline** by explicitly stating how image-level entropy is computed for the EE method, tying it to the definitions used elsewhere in the paper.

5. **Briefly discuss the cold-start concern** for the redundancy term and whether features from early-model iterations remain useful.

6. Report approximate LP solve times for a typical AL iteration to establish practical feasibility.

## Score and Decision

**Score rationale:** The paper presents a genuinely novel and well-motivated idea — binary queries for segmentation AL — and provides compelling evidence that this query modality can achieve mIoU results close to pixel-level methods at a fraction of the annotation cost. These contributions are real and valuable. However, the technical contribution of the LP-based selection algorithm is not well-validated: the binary-level baselines are too weak to establish that the LP formulation adds value beyond simpler selection strategies. The lack of sensitivity analysis for key hyperparameters and the absence of variance reporting in the user study further weaken the empirical case. These issues are addressable but leave the paper in a borderline position.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>