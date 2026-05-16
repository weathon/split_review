Now I have all the evidence I need. Let me compile the final consolidated review.

## Summary

CALICO proposes a two-stage self-supervised contrastive pre-training framework for multimodal BEV perception: (1) Point-Region Contrast (PRC) for the LiDAR backbone, using DBSCAN-based semantic pooling and a balanced region+scene-level contrastive loss, and (2) Region-Aware Distillation (RAD) for the camera backbone via self-supervised contrastive distillation from the frozen LiDAR teacher. Evaluated on nuScenes and Waymo for 3D detection and BEV map segmentation, the method shows consistent improvements over existing pre-training approaches at multiple data fractions, along with notable gains in adversarial and corruption robustness.

## Strengths

- **Novel semantic pooling for unsupervised region definition.** The paper replaces the random anchor/ball-query heuristics used in ProposalContrast with DBSCAN clustering on ground-removed point clouds, producing object-aligned regions without labels. Table 1 shows PRC outperforms ProposalContrast by 2.9 NDS on 5% LiDAR data (46.0 vs 43.1) and by 1.1 NDS on 50% data (62.1 vs 61.0), directly attributable to this design.

- **Consistent gains across tasks, datasets, and data regimes.** At 5% labeled data, full CALICO improves over the random-initialization LiDAR-only baseline by 10.5 NDS and 8.6 mAP for detection (Table 1). Gains remain positive even at 50% data (62.7 vs 61.0 NDS for LiDAR-only random init). The method also transfers to Waymo (71.6 vs 63.2 AP, 20% data, Table 2), cross-dataset settings (Table 3), and BEV map segmentation (5.7 mIoU improvement at 5%, Table 4).

- **Robustness improvements under two threat models.** The paper evaluates adversarial LiDAR spoofing attacks and common corruptions, reporting a 45.3% reduction in attack success rate and the lowest mean corruption error (78.2%) among all compared methods. This is relatively underexplored in the self-supervised pre-training literature for BEV perception and adds practical value.

- **Two-stage design that avoids multimodal degradation.** The paper identifies that joint camera-LiDAR contrast (SimIPU) degrades in BEV settings due to implicit pixel-to-BEV transformation. CALICO's two-stage approach (pretrain LiDAR alone, freeze it during camera distillation) produces stable multimodal gains: PRC+random camera (46.1 NDS) already outperforms SimIPU (45.8 NDS) at 5% data (Table 1).

- **Ablation of the α trade-off reveals practical insight.** Table 5 shows that α=0.9 (more region-level focus) works best for scarce data (46.3 NDS at 5%), while α=0.1 works best for abundant data (62.2 NDS at 50%), providing actionable guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Headline improvement numbers mix LiDAR-only and multimodal comparisons.** The abstract and intro state "outperforms the baseline method by 10.5% and 8.6% on NDS and mAP." Looking at Table 1 at 5% data, this compares Rand. Init. (L, LiDAR-only, 37.4 NDS) to CALICO (L+C, multimodal, 47.9 NDS). The gain mixes LiDAR pre-training, camera pre-training, and multimodal fusion. The closest multimodal baseline (PRC+Rand. Init. (C)) gives a more modest 1.8 NDS improvement at 5% data. The paper should clearly distinguish cumulative gains from per-component gains and report the improvement over the closest comparable multimodal baseline.

- **No variance or uncertainty estimates.** All results appear to be single runs. For large benchmarks like nuScenes this is common practice, but given that several comparisons show small margins (e.g., 0.4 NDS difference between CALICO and PRC+BEVDistill at 50% data), error bars from multiple seeds would significantly strengthen confidence in the results.

- **RAD's contribution is not fully isolated.** The paper compares PRC+BEVDistill vs PRC+RAD (CALICO). However, RAD differs from BEVDistill in several ways (contrastive distillation design, region-wise normalization, self-supervised teacher). An ablation that isolates the region normalization (e.g., removing it or replacing it with uniform weighting) and/or comparing against a simpler L2 distillation baseline with the same architecture would clarify whether RAD's design choices are individually necessary. The margin over BEVDistill is 0.2–0.4 NDS across data regimes, making this isolation important.

- **Missing fully random multimodal baseline in detection.** Table 1 (detection) does not include a row for both backbones randomly initialized (L+C). The table has "Rand. Init." only for L (LiDAR-only). Including both-randomized baselines would allow readers to see the additive benefit of camera pre-training independently. (Note: the BEV map segmentation table does include this baseline.)

- **Semantic pooling details are underspecified.** The paper mentions "ground removal" and "filtering out clusters that are too large or high" but does not describe how ground removal is performed or quantify the heuristics (what thresholds define "too large or high"). Reporting clustering statistics (avg. number of regions per scene, fraction of points labeled semantic-rich, failure case analysis) would increase confidence in the robustness of this critical component.

- **α ablation does not include extreme values.** Table 5 varies α from 0.1 to 0.9 but does not include α=0 (RAPC only) or α=1 (PLRC only). Including these extremes would directly show whether combining both losses is strictly better than either in isolation.

### Trivial

- Missing details on the exact projection/interpolation from 3D points to the BEV feature map for point-wise feature extraction (bilinear interpolation is mentioned but the coordinate mapping is not fully specified).

## Nice-to-Haves

- Quantifying pre-training time and memory overhead relative to training from scratch and to baselines, since the paper acknowledges computational cost as a limitation.
- Reporting 100% fine-tuning results to show whether pre-training remains beneficial at full data.
- Including results at additional data fractions for Waymo and cross-dataset evaluations.

## Removed Points

These points were identified by reviewers but are either factually incorrect, misunderstandings, or strawman criticisms after cross-checking against the paper.

1. **SimIPU baseline comparison is unfair.** *Details from reviewer:* "The paper acknowledges SimIPU underperforms due to the implicit pixel-to-BEV transformation... This is essentially an architecture mismatch." *Reason for removal:* Comparing against a published method as-is, showing that it doesn't transfer well to a new architecture class, is legitimate scientific comparison. The paper's motivation is precisely that existing methods struggle in BEV settings. Claiming this is an "unfair comparison" misunderstands the paper's contribution: CALICO is designed to address this gap.

2. **BEVDistill comparison is not apples-to-apples.** *Details from reviewer:* "BEVDistill relies on ground-truth object masks for distillation... If it does [use GT masks], then the comparison is not apples-to-apples." *Reason for removal:* The paper explicitly states (Section 2.3): "Different from existing studies that generate center-based masks for groundtruth objects [BEVDistill citation], we treat every point in one region the same as the region assignments are from heuristics." This confirms BEVDistill uses GT masks (stronger supervision) while RAD is fully self-supervised. If RAD outperforms BEVDistill despite using weaker supervision, this *strengthens* the paper's claims, not weakens them.

3. **Missing related works.** *Reason for removal:* Per instructions, I do not have external sources to confirm whether missing works exist.

4. **Formatting/style nitpicks, figure quality complaints, typos.** *Reason for removal:* These are parser artifacts or presentational minutiae, not content issues.

5. **The paper overstates the gap about a missing unified framework.** *Reason for removal:* The paper acknowledges SimIPU and BEVDistill but shows specific limitations (SimIPU fails in BEV; BEVDistill uses GT masks). The claim that a unified *self-supervised* pre-training framework for multimodal BEV is missing is accurate given these limitations.

## Novel Insights

The most interesting observation across the reviews is the α-ablation trade-off: the same method behaves qualitatively differently in low-data vs high-data regimes, with region-level contrast (PLRC) dominating when data is scarce and scene-level contrast (RAPC) dominating when data is abundant. This is a genuinely useful design insight for practitioners building self-supervised pre-training pipelines for autonomous driving, and it is well-documented in the paper (Table 5). The robustness evaluation showing consistent benefits against both adversarial spoofing and natural corruptions is also notable, as most pre-training papers for 3D perception focus exclusively on accuracy metrics.

## Suggestions

1. **Clarify the headline numbers.** In the abstract and introduction, state the improvement over the best multimodal baseline (e.g., 1.8 NDS over PRC+Rand. Init. (C)) alongside the cumulative improvement over the LiDAR-only baseline, so readers can distinguish the specific contribution from camera pre-training.

2. **Add variance estimates** for at least the key comparisons (5% and 20% data fractions, 3 seeds) to assess whether the small-margin gains (0.2–0.4 NDS over BEVDistill) are statistically reliable.

3. **Ablate the region normalization in RAD** by comparing against (a) RAD without region-wise normalization and (b) a simple L2 distillation baseline, to isolate which design elements drive the improvement over BEVDistill.

4. **Provide clustering statistics** (average number of regions, point coverage, qualitative examples including failure cases) to demystify the semantic pooling step.

5. **Add a "Rand. Init. (L+C)" row to Table 1** for the detection task to match the BEV map segmentation table.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>