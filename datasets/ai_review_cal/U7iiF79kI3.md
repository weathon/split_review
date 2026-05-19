- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6
## Summary

This paper introduces CALICO, a self-supervised contrastive pretraining framework for multimodal BEV perception. It operates in two stages: (1) Point-Region Contrast (PRC) on LiDAR, which combines point-level region contrast (PLRC) with region-aware point contrast (RAPC) to balance region- and scene-level learning, and (2) Region-Aware Distillation (RAD), which distills knowledge from the self-pretrained LiDAR backbone to the camera backbone. Extensive experiments on nuScenes and Waymo for 3D object detection and BEV map segmentation show substantial gains in low-data regimes (e.g., +10.5 NDS points at 5% data) and consistent if smaller improvements at higher data fractions, along with measurable robustness benefits against adversarial spoofing and common corruptions.

## Strengths

- **Large improvements in low-data regimes are unambiguous and well-substantiated.** At 5% labeled data, CALICO achieves NDS 47.9 and mAP 41.7 versus random initialization at NDS 37.4 and mAP 33.1 (Table I) — absolute gains of 10.5 and 8.6 points, respectively. These margins are far too large to be explained by variance, making the low-data claim solid even without error bars.

- **Consistent gains across two tasks, two datasets, and cross-dataset transfer.** The method improves both 3D object detection (Table I) and BEV map segmentation (Table V), on both nuScenes and Waymo (Table II), and transfers from Waymo pretraining to nuScenes fine-tuning (Table III, +2.6 NDS over ProposalContrast). This breadth strengthens the claim of general applicability.

- **Well-designed ablation study of the α hyperparameter** (Table VI). The analysis shows a clear trade-off: α=0.9 (emphasizing PLRC) performs best at 5% data (NDS 46.3) but worst at 50% (NDS 60.8), while α=0.1 (emphasizing RAPC) reverses this pattern. α=0.5 is shown to be a reasonable default. This gives practitioners actionable guidance.

- **Novel robustness analysis adds practical value.** The 45.3% average reduction in LiDAR spoofing attack success rate and the best mCE (78.2%) against corruptions demonstrate that the pretraining yields more balanced multimodal representations, not just better clean accuracy.

## Weaknesses

### Fatal

None.

### Major

- **No statistical significance or variance reporting for any result.** All metrics are reported as single-run point estimates. The improvements at the 50% data setting are 1–2 NDS/mAP points (e.g., Table I, 50%: CALICO vs. PRC+BEVDistill gives +0.4 NDS, +0.5 mAP). Without error bars, confidence intervals, or multiple-seed experiments, it is impossible to determine whether these small high-data gains are real or within the noise floor. While the low-data improvements are large enough that this concern does not undermine the paper's core contribution, it weakens the claim of consistent advantage across all data amounts. This is the single most impactful issue to fix.

### Minor

- **Key preprocessing detail is underspecified.** The "ground removal" step (Section 3.2) is mentioned but its method is not described at all — no mention of plane-fitting RANSAC, height thresholding, or any other concrete algorithm. Since the entire semantic pooling stage (and thus the quality of region assignments) depends on this step, the omission hurts reproducibility. The DBSCAN parameters are given (eps=0.75m, min_samples=5), but a brief sensitivity analysis of these choices would increase trust in the method's robustness.

- **Percentage-vs.-percentage-point ambiguity in headline claims.** The abstract and conclusion state that CALICO "outperforms the baseline method by 10.5% and 8.6% on NDS and mAP" — these are absolute percentage-point differences (37.4→47.9 NDS, 33.1→41.7 mAP). While this convention is not uncommon in the autonomous driving literature, it risks misleading readers unfamiliar with the convention. Rephrasing as "10.5 points and 8.6 points" would be clearer.

### Trivial

None.

## Nice-to-Haves

- A convergence analysis of the pretraining stage (the paper uses 20 epochs for both PRC and RAD without showing whether performance saturates) would be informative.
- Reporting the computational overhead of the added projectors (parameter counts, training time) would help practitioners assess the practical cost of the method.
- The naming "PRC+Rand. Init. (C)" in Table I is explained in the caption but remains somewhat awkward; a cleaner label would improve readability.

## Removed Points

- **PLRC positive-pair definition insufficiently explained** (Harsh Critic, Critical Issue 3 sub-point): The paper states clearly that points sharing the same region ID across two augmented views form positive pairs (lines 55–56, "We use $r_i = r_j$ to show that point $i$ and $j$ belong to the same region"). The sampling strategy (N semantic-rich + M semantic-less points) and the loss formulation in Equation (1) are adequately specified. Removed because the paper already addresses this.

- **Naming confusion about "PRC+Rand. Init. (C)"** (Harsh Critic, §4.2): The table caption explicitly defines this notation. Removed because the paper already explains it.

- **Waymo table only showing 20%** (Harsh Critic, Waymo results): Showing a single representative data fraction is common practice. Not a weakness.

- **Cross-dataset comparison clarity** (Harsh Critic, §Table III): The comparison is valid and the caption is reasonably clear. The paper compares Waymo-pretrained+nuScenes-finetuned against scratch-trained on nuScenes — a standard cross-dataset protocol. Removed.

- **Robustness metrics insufficiently described** (Harsh Critic, §4.5): The text states the attack uses 60/100/200 spoof points, reports average ASR reduction, and describes the mCE calculation with the scratch model as baseline. The description is adequate for the venue. Removed.

- **Generic strengths** (Strength Finder): All five strengths are concrete, specific, and backed by evidence from specific tables/figures. None are generic or superficial; all are retained.

## Novel Insights

Beyond the paper's own contributions, the most notable takeaway from the review process is that the two-stage design (first LiDAR-only pretraining, then camera distillation from the frozen LiDAR backbone) is empirically validated as superior to joint multimodal contrastive learning (SimIPU). This is a non-obvious finding — one might expect joint training to produce better aligned representations — but the paper demonstrates that the implicit pixel-to-BEV transformation makes joint training unstable. The ablation showing that PLRC without RAPC overfits at high data fractions (Table VI) is also a useful design insight: region-level contrast helps in low data but hurts with abundant data, so explicit balancing is necessary. These findings are actionable for future work on multimodal BEV pretraining.

## Suggestions

- Report all main results as mean ± std over 3–5 random seeds, especially for the 20% and 50% data settings where gains are modest. If computational cost is prohibitive, at minimum run 3 seeds for the key comparison tables (Tables I and V).
- Specify the ground removal algorithm used in semantic pooling (e.g., RANSAC plane fitting with a height threshold), and add a brief sensitivity analysis of DBSCAN parameters in the appendix.
- Recast the headline percentage claims as "X points" (e.g., "10.5 NDS points") to avoid ambiguity.
- Consider adding pretraining convergence curves (NDS vs. pretraining epoch for PRC and RAD) to justify the 20-epoch choice.
