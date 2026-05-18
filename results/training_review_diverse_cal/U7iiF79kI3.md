Now I have all the information needed. Let me compile the final review.

## Summary

This paper presents CALICO, a two-stage self-supervised contrastive pre-training framework for multimodal (camera + LiDAR) BEV perception. Stage 1 (PRC) uses DBSCAN-based semantic pooling followed by point-region contrast to pre-train the LiDAR backbone. Stage 2 (RAD) performs region-aware contrastive distillation from the LiDAR backbone to the camera backbone. Experiments on nuScenes and Waymo show improvements over existing self-supervised methods (PointContrast, ProposalContrast, SimIPU, BEVDistill) on 3D detection, BEV map segmentation, adversarial robustness, and corruption robustness.

## Strengths

- **PRC achieves state-of-the-art LiDAR-only results across data regimes**: PRC outperforms ProposalContrast (the previous SOTA) by 2.9% NDS at 5% data and 1.5% NDS at 10% data on nuScenes (Table 1), and by 2.3% AP on Waymo (Table 2). These gains persist at higher data fractions, demonstrating robust representation learning rather than merely benefiting from low-data regimes.

- **Full CALICO framework shows consistent improvements across diverse settings**: CALICO outperforms BEVDistill (the existing distillation method) at every data fraction on nuScenes 3D detection (Table 1: +0.4 NDS / +0.7 mAP at 5%, +0.3/0.3 at 10%, +0.3/0.4 at 20%, +0.4/0.5 at 50%), and achieves SOTA on Waymo with 71.6% AP (+3.2% over SimIPU). Gains are also shown on BEV map segmentation (Table for map segmentation: +1.1-5.7% mIoU across data fractions).

- **Robustness benefits are clearly demonstrated**: CALICO reduces adversarial attack success rates by 45.3% on average (Figure 1) and achieves the lowest mean corruption error at 78.2% (Figure 2) — a practical advantage for real-world deployment.

- **Architecture-agnostic**: PRC improves VoxelNet+TransFusion as well as PointPillars+CenterPoint (Figure 3), showing the method is not tied to a specific backbone or detection head.

- **Ablation of \(\alpha\) reveals principled trade-off**: The \(\alpha\) parameter in Eq. 2 cleanly balances region-level (PLRC) and scene-level (RAPC) learning, with \(\alpha=0.9\) best at 5% data (NDS 46.3) and \(\alpha=0.1\) best at 50% data (NDS 62.2), providing actionable guidance for practitioners (Table 5).

## Weaknesses

### Major

- **No direct evaluation of the semantic pooling quality.** The entire method rests on DBSCAN clustering (min\_pts=5, eps=0.75m) followed by heuristic filtering ("too large or high"). Yet the paper never reports: how many clusters are found per scene; what fraction capture actual objects vs. noise; how many false positives (e.g., parts of large structures) are introduced; or how sensitive downstream performance is to the DBSCAN hyperparameters. The clustering thresholds for the "too large or high" heuristic are not specified quantitatively ("simple yet effective heuristics," line 49), making the method partially irreproducible. While the downstream gains empirically validate the approach as a whole, the core claim that the pooling produces "object-level semantics" (line 15) remains an untested assumption. This is the most significant gap because the semantic pooling is the foundation of both PRC and RAD.

### Minor

- **Abstract oversimplifies the headline comparison.** The abstract states that CALICO "outperforms the baseline method by 10.5% and 8.6% on NDS and mAP." This compares the full CALICO (L+C) against the simplest LiDAR-only random initialization baseline (NDS 37.4→47.9, mAP 33.1→41.7). While the numbers are correct and the baseline is identifiable from Table 1, the comparison mixes modality differences (adding camera) with pre-training gains. The within-modality gain of RAD alone over "PRC+Rand. Init. (C)" is 1.8 NDS and 1.5 mAP. The introduction (line 16) provides better context by first reporting PRC's LiDAR-only gains, but the abstract alone could mislead a casual reader. The paper would benefit from stating the baseline explicitly in the abstract.

- **Two-stage design not ablated against a joint-training alternative.** The paper argues for two-stage training (PRC first, then RAD with frozen LiDAR backbone), criticizing SimIPU's joint training (lines 36, 159). However, SimIPU uses different losses and does not incorporate PRC or RAD. A direct ablation holding the loss functions constant and varying only the training schedule (joint vs. two-stage) is missing. Without this, the claimed benefits of two-stage optimization are plausible but unverified within the proposed framework.

- **RAD improvements over BEVDistill are small and unreplicated.** Across all data fractions in Table 1, RAD improves over BEVDistill by only 0.3–0.7 NDS and 0.3–0.7 mAP. No standard deviations or multi-run statistics are reported, so it is unclear whether these differences are statistically significant. The paper should acknowledge this and discuss whether the added complexity of RAD is warranted.

- **Several useful ablations are missing:**
  - DBSCAN hyperparameter sensitivity (eps, min\_pts) — especially important since clustering is the method's foundation.
  - Per-region normalization in RAD Eq. 3 — not ablated against an unnormalized variant.
  - Number of sampled points N=M=1024 — not varied to show robustness.
  - Reproducibility: the "too large or high" heuristic thresholds are not specified.

- **Inconsistency in robustness evaluation setup.** Adversarial attacks use models fine-tuned on 50% data (line 279) while corruption evaluation uses 10% data (line 281) with no rationale given. Consistency would strengthen the comparison.

### Trivial

- None that warrant listing separately — the paper is generally well-written and the presentation is clean.

## Nice-to-Haves

- An oracle experiment using ground-truth object boxes (instead of DBSCAN clusters) during pre-training would quantify how much is lost by relying on unsupervised clustering.
- A brief discussion of the transferability limitations observed in the cross-dataset experiment (Table 3: lower absolute numbers than in-dataset) would be helpful.
- Reporting mean and variance over 3 finetuning runs would address the statistical significance concern.

## Removed Points

These points from the reviewers were considered but removed or downgraded for the reasons below:

1. **"The improvements of RAD over BEVDistill are small... no standard deviations"** — Kept as Minor (above), not removed. This is a valid point.
2. **"The paper should also cover Y / domain Z"** — No such broad scope-creep demands were present.
3. **Any formatting/typo concerns** — Removed per instructions (parser artifacts, not author errors).
4. **Questioning existence/release of cited entities** — None found in the reviews.
5. **The reviewer's framing of Critical Issue 1 as "misleading" (overblown severity)** — Downgraded from "Critical/Major" to "Minor." The numbers are factually correct; the baseline is identifiable from Table 1 and is the simplest available baseline; the paper also reports within-modality comparisons (PRC+Rand.Init.(C) vs CALICO). The criticism is valid for presentation clarity but does not undermine the paper's claims.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known trade-offs in self-supervised learning (evaluation of unsupervised clustering quality, ablation of training schedules) but do not introduce a genuinely new perspective on the work.

## Suggestions

1. **Directly evaluate the semantic pooling**: Report precision/recall of DBSCAN clusters against ground-truth object boxes, distribution of cluster counts per scene, and a sensitivity analysis of DBSCAN hyperparameters on downstream performance. Specify the quantitative thresholds for the "too large or high" heuristics.
2. **Ablate the two-stage design**: Compare the current two-stage pipeline against a joint version that optimizes PRC and RAD simultaneously with gradients flowing to both backbones. This directly tests the paper's stated motivation.
3. **Correct the abstract**: Explicitly state the baseline being compared (e.g., "outperforms the random-initialization LiDAR-only baseline by 10.5% NDS and 8.6% mAP") so readers immediately understand the comparison.
4. **Add statistical significance**: Report results over multiple finetuning seeds (e.g., 3 runs) with mean and variance, especially for the RAD vs. BEVDistill comparison where the gaps are small.
5. **Consolidate the robustness evaluation**: Use the same data fraction for both adversarial and corruption experiments, or provide a rationale for the different choices.

## Score and Decision

This paper introduces a well-motivated framework with thorough experimental coverage across tasks, datasets, and robustness scenarios. The core weakness — lack of direct evaluation of the semantic pooling — is real but does not invalidate the contributions, as the downstream improvements are empirically demonstrated across many settings. The abstract framing concern and missing ablations are addressable in revision. On balance, the paper makes a solid empirical contribution to self-supervised multimodal BEV perception.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>