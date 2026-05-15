Now I have all the information needed. Let me produce the consolidated review.

## Summary

The paper proposes P3DTrack, a 2D MOT framework that learns a 3D object representation from monocular video without LiDAR or pre-trained depth estimators. The key idea is to generate pseudo-3D object labels by combining Structure-from-Motion scene reconstruction with 2D bounding box tracklets, then jointly learn a 3D representation and a graph-based association module. The method is evaluated on KITTI and Waymo Open Dataset, with the KITTI results being particularly strong (3.0 AssA improvement, lowest ID switches among methods without extra annotations).

## Strengths

- **Novel pseudo-3D label generation from monocular video without extra supervision (Section 3.1, Figure 2).** The idea of using SfM reconstruction + 2D tracklet IDs to generate 3D pseudo-labels is creative. It eliminates the need for LiDAR, pre-trained depth estimators, or manually annotated 3D labels, which is a genuine departure from prior depth-based MOT methods. This is the paper's strongest conceptual contribution.

- **Strong association results on KITTI (Table 2).** On the KITTI test set, P3DTrack achieves a 3.0-point improvement in AssA (association metric) over prior methods without additional annotations, and achieves the lowest number of ID switches (111). This directly supports the paper's central claim that the learned 3D representation aids association.

- **Architectural integration is clean and computationally efficient.** The 3DRL module adds only 12 ms (~5.5%) to inference latency with modest increases in training memory and parameters (Table 8), making the approach practical for real-world deployment.

- **Ablation studies show the 3D representation provides real value beyond appearance.** Table 4 demonstrates that adding the learned 3D representation on top of appearance features improves MOTA by 1.1 and IDF1 by 1.6, and combining it with a 3D KF motion model yields clear gains over 2D KF alternatives. Table 7 shows a 5.1 MOTA / 13.9 IDF1 gap between α=0 (appearance only) and the best α setting.

## Weaknesses

### Fatal
None. The paper's core approach is valid and the experiments show real (if uneven) improvements.

### Major

- **The 3D representation is trained only on static objects; generalization to moving objects is asserted without evidence (Section 3.1, lines 73; Section 3.2, line 105).** The paper states "we only label static objects" because SfM cannot reconstruct moving objects. The claim that "the network can easily make the 3D position prediction of the moving object" because "the network does not distinguish the object movement in one frame" is a non-sequitur that is not experimentally validated. The paper provides no analysis of performance on static vs. moving objects, no qualitative examples of predicted 3D trajectories for moving objects, and no comparison against methods that explicitly handle moving objects. Since the majority of objects in autonomous driving scenes are moving, this gap undermines confidence in the core mechanism. This is the single most important issue to address.

- **On Waymo Open Dataset, the paper's own most-prioritized association metrics worsen (Table 1).** The paper states "the number of mismatches is the most important to evaluate the data association performance" (Section 4.1), yet P3DTrack increases ID switches vs. QDTrack (3427 vs. 3318, +109) and decreases IDF1 (71.7 vs. 73.0, –1.3). The MOTA improvement (+0.3, 66.6 vs. 66.3) is driven by drastically fewer false positives (FP 32911 vs. 51851) at the cost of many more false negatives (FN 71151 vs. 56014) — a pattern consistent with a different detector architecture and threshold choices rather than better association. The paper's explanation (line 192) attributes this to the CenterNet detector's lower recall vs. QDTrack's FasterRCNN, but the headline narrative of "improved association" is not supported by the WOD evidence.

- **Limited baselines, especially on Waymo.** On WOD, only a single contemporary baseline (QDTrack) is compared. Recent camera-based 3D MOT methods (e.g., PF-Track, MUTR3D) are cited in related work but not compared, even though they also leverage 3D information. The paper scopes itself to methods "without any additional human annotations and pre-trained models" (Section 4.3), but this exclusion is not applied consistently — some baselines in Table 2 use pre-trained models, and the claim of "state-of-the-art" requires a broader comparison. On KITTI, baselines are from 2020-2021 and no transformer-based trackers are included.

### Minor

- **Ambiguous "joint learning" claim (Section 4.2, line 176).** The paper repeatedly claims that the 3D representation and association module are "jointly learned," but the training procedure describes staged training: 6 epochs for detection, 1 additional epoch for 3D representation learning, then 4 additional epochs for the association module. It is never stated whether gradients from the association loss backpropagate into the 3D representation head, or whether the 3D head is frozen during association training. If the latter, the term "joint" is misleading, and the claimed advantage over depth-based methods ("joint optimization," line 14) is not realized. This must be clarified.

- **No sensitivity analysis for SfM thresholds and no quantification of data loss (Section 3.1).** The clustering thresholds δ=0.5 and κ=30 are introduced without ablation or sensitivity analysis. The paper notes that videos with "low speed of ego-motion" are filtered, and "not all scenes can be reconstructed well," but the number/percentage of discarded sequences is never reported. This makes it difficult to assess the method's applicability range.

- **Components are conflated in the main ablation (Table 3).** The transition from row 2 (+low-score matching) to row 3 (+association learning with GNN and jointly learning 3D representation) bundles two architectural changes — the GNN association module and the 3D representation — into a single experimental step. Table 4 partially disentangles this for the 3D representation vs. motion model comparison, but the individual contribution of the GNN alone (without 3D) is never isolated.

- **No HOTA on WOD.** The paper uses HOTA as a primary metric on KITTI (correctly), but reports only CLEAR metrics and IDF1 on WOD. Since HOTA separates detection and association contributions, its absence on WOD makes it harder to determine whether the MOTA gain on WOD comes from improved association or detection differences.

### Trivial
None.

## Nice-to-Haves

- A static vs. moving object breakdown on WOD to validate the claim of generalization to moving objects.
- An analysis of the quality of pseudo-3D labels (e.g., comparison against LiDAR ground truth on WOD for static objects).
- An ablation of the uncertainty σ² output — does it correlate with prediction error and does it help the association?
- Reporting results on the WOD test set via the leaderboard would strengthen the SOTA claim.

## Removed Points

*These points were flagged for removal and should be treated with caution:*

1. **"The improvement from α=0 to best is modest" (Critic, Section 4.4).** Removed as factually wrong. The paper reports a 5.1 MOTA and 13.9 IDF1 decrease from best to α=0 (Table 7), which is substantial, not modest.

2. **"The 'appearance only' baseline does not use any KF, so it is not a fair comparison with methods that use 2D KF" (Critic, Section 4.4).** Removed as a misreading. Table 4 includes separate baselines for "+2D KF" and "+3D KF (w/o 3D repr)," so the comparison is fair — the "appearance only" row is just one of several points of comparison.

3. **"α=1 means no appearance, but detection and 3D KF still rely on image features" (Critic, Section 4.4).** This is an inherent property of the design (the 3D representation is learned from image features, which is the point of representation learning), not a weakness of the paper.

4. **Criticism that the paper should compare with camera-based 3D MOT methods that use manually annotated 3D ground truth.** The paper explicitly scopes itself to 2D MOT without 3D labels (Section 2.1, line 35). This is scope-creep.

5. **"The network can easily make the 3D position prediction of the moving object" labeled as a non sequitur.** The underlying concern (lack of evidence) is valid and kept in Major Weakness 1, but the dismissive framing as a logical fallacy is removed. The paper's reasoning about per-frame prediction is plausible but unvalidated — this is a missing-experiment issue, not a logical error.

## Novel Insights

The reviews surface a tension that the paper does not fully wrestle with: the method's pipeline uses SfM (which fundamentally requires static scenes) to generate the only 3D supervision signal, but then applies the learned representation to dynamic scenes. Even if the per-frame prediction argument (Section 3.2) is theoretically sound, the paper never tests it, leaving the core claim in a vulnerable position. Separately, the WOD results reveal a pattern where the method trades away recall for precision (low FP, high FN), which produces a modest MOTA gain but degrades association metrics — a trade-off that the paper's own narrative of "better association" does not predict. This mismatch between claimed mechanism and observed behavior is the central weakness that a revision must address.

## Suggestions

1. **Critically, provide a breakdown of performance on static vs. moving objects on WOD.** This single experiment would either validate or refute the paper's most important unsubstantiated claim. Show MOTA, IDF1, ID Sw for each subset, and ideally visualize predicted 3D trajectories for moving objects.

2. **Acknowledge and discuss the IDF1/ID Sw regression on WOD head-on** rather than attributing it entirely to detector differences. Report HOTA on WOD to separate detection and association contributions. If the 3D representation is mainly helping precision (reducing FP) rather than association, state this clearly.

3. **Clarify the training procedure**: does the association loss backpropagate into the 3D representation head? If yes, state it explicitly. If no, stop calling it "joint learning."

4. **Add a direct comparison with a 2D-only variant that uses the same association module (GNN + quadratic matching) without the 3D representation**, to isolate the contribution of the GNN from the 3D representation. Table 3 conflates these.

5. **Quantify SfM data loss**: report how many WOD sequences are discarded due to low ego-motion, and how many tracklets receive pseudo-3D labels vs. how many do not.

6. **Ablate SfM thresholds** δ and κ to show performance sensitivity.

## Score and Decision

The paper makes a genuine conceptual contribution — generating pseudo-3D labels from SfM + 2D tracklets for 2D MOT is novel and the KITTI results are strong. However, the WOD evidence is mixed and undermines the central narrative, and the most important claim (generalization of the 3D representation to moving objects) is unvalidated. The paper is not fatally flawed — the approach has merit — but it requires substantive revision to close the gap between claims and evidence. In its current form, it falls below the acceptance threshold.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>