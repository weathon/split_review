Now I have all the information I need. Let me produce the consolidated review.

## Summary

The paper proposes P3DTrack, a 2D MOT method that learns a 3D object representation from pseudo-3D labels generated via Structure-from-Motion (SfM) and 2D tracking labels, without requiring LiDAR or depth sensor supervision. The 3D representation is jointly learned with a GNN-based association module and used in an online tracker with a 3D Kalman Filter. The core idea—lifting 2D association to 3D space via learnable 3D features from pseudo labels—is conceptually interesting and different from prior depth-based approaches.

## Strengths

- **Novel pseudo-3D label generation pipeline from 2D tracklets and SfM.** The paper designs (Sec. 3.1, Fig. 2) a method to extract 3D object centroids by reconstructing static scene points via SfM, then applying intra-frame and inter-frame point clustering from 2D bounding boxes with identity. This generates 3D supervision without LiDAR, depth sensors, or human-annotated 3D labels, which is the paper's primary novelty.

- **Joint learning of 3D representation and object association.** The 3DRL module (Sec. 3.2) is trained jointly with the GNN-based association module, sharing the detection backbone. This contrasts with prior depth-based MOT methods that keep depth estimation and association separate. The ablation (Table 3) shows that adding association learning + 3D representation yields +4.2 MOTA and +3.8 IDF1 over the baseline.

- **Strong KITTI results on association metrics.** On the KITTI test set (Table 2), P3DTrack achieves the highest AssA (66.7) and the lowest ID switches (247) among methods without extra pre-trained models or 3D ground truth, a meaningful improvement of +3.0 AssA over the next best method.

- **Computational efficiency is reasonable.** Table 8 reports only +12 ms (5.5%) inference latency increase, +1 GB training memory, and +3.5 M parameters over the baseline, showing the approach does not introduce prohibitive overhead.

- **Clear motivation and positioning.** Section 1 clearly articulates three limitations of off-the-shelf depth models (temporal inconsistency, camera-intrinsic generalization, lack of joint optimization) and explains how learnable 3D representation from pseudo labels addresses them.

## Weaknesses

### Fatal
None.

### Major

- **No direct validation that the learned 3D representation generalizes to moving objects.** The pseudo labels are generated only for static objects (SfM filters moving objects during RANSAC). The paper asserts (line 105) that "the network can easily make the 3D position prediction of the moving object" and claims generalization in Table 5, but provides no direct evidence—no comparison of predicted vs. LiDAR ground-truth 3D positions for moving objects, no ablation separating static vs. moving object performance, and no qualitative visualization of predicted 3D trajectories. The overall tracking metrics (which include moving objects) provide only indirect support. For a paper whose value proposition is lifting 2D association to 3D space, this gap weakens the central claim considerably.

- **Missing coordinate transformation details for pseudo labels.** The pseudo 3D labels are generated in the *global* frame from SfM (line 67: "3D position of each keypoint P_i in the global frame"), but the 3D representation learning module predicts the object's position in the *camera* frame (line 91: "3D position of the object center in the camera frame"), and the loss (Eq. 2) is computed between them. The paper states the target barycenter is "in the camera frame" (line 78, garbled by parser) but never explains *how* the global SfM coordinates are transformed to camera-frame coordinates. SfM (COLMAP) does recover camera poses as part of bundle adjustment, making this transformation technically standard, but the paper omits this step entirely. This omission makes the pipeline difficult to reproduce and leaves an unverified link in the learning chain.

- **Ablation does not isolate the 3D representation from the GNN association module.** Table 3 shows a combined improvement of +4.2 MOTA from "association learning + 3D representation" over a baseline that already includes ByteTrack-style low-score matching. However, this increment bundles the GNN association head *together with* the 3D representation learning. The paper never ablates the GNN association module *without* the 3D representation. Table 4 partially addresses this by comparing "3D representation + 3D KF" vs. "appearance only" on the FRONT camera subset (+1.1 MOTA), but this comparison uses a different setup (FRONT camera only) and does not control for the GNN component. The reader cannot tell how much of the 4.2 gain comes from the GNN architecture itself versus the 3D representation specifically.

- **WOD results are marginal and inconsistent.** On Waymo (Table 1), P3DTrack achieves 49.0 MOTA vs. 48.7 for QDTrack (+0.3), while IDF1 is *lower* (42.8 vs. 44.0). The paper attributes this to a weaker detector (DLA-34 vs. Faster-RCNN) causing lower ID Recall, which is a valid explanation, but the overall result does not constitute a clear SOTA claim on this dataset. ID switches are not reported separately on WOD, which is the metric most directly tied to the paper's motivation of improving association quality. The KITTI results are stronger, but the paper's "state-of-the-art" claim is overstated given the WOD numbers.

### Minor

- **The SfM pseudo-label generation description is somewhat vague on edge cases.** The matching strategy (line 73: "assign the cluster to the tracklet whose 2D bounding box can involve the maximum number of the reprojected points") does not discuss how ambiguous cases are handled (e.g., overlapping bounding boxes, partial occlusions, or clusters projecting into multiple tracklets equally).
- **ID switches not reported separately on WOD.** This metric most directly reflects the method's claimed benefit (reducing wrong associations) and is available from the evaluation protocol. Its absence makes it harder to assess the 3D representation's impact on association quality on the larger dataset.
- **How alternative 3D representations (SfM positions, MiDaS depth) are integrated into the tracking pipeline is not fully specified.** The paper discusses their limitations (Table 5) but does not describe the integration mechanics (e.g., raw SfM coordinates fed into 3D KF directly? MiDaS relative depth converted to metric?).

### Trivial
None.

## Nice-to-Haves

- Reporting ID switches on WOD would strengthen the association-focused evaluation.
- A controlled ablation with "GNN + appearance only" vs. "GNN + appearance + 3D representation" would cleanly isolate the 3D representation's contribution.
- A qualitative visualization of predicted 3D positions overlaid on LiDAR point clouds would help validate the method's core claim.

## Removed Points

These points were considered but removed after verification against the paper:

- **"Missing algorithm pseudo-code in appendix"** — The paper references "Alg." (line 65), which the parser likely truncated from the appendix. Per policy, parser-stripped appendix content is not a valid weakness.
- **"Frozen appearance model advantages the 3D representation"** — Freezing the appearance model is a design choice, not a source of unfair advantage. If anything, it limits the association module's representational power. This criticism misidentifies the direction of the effect.
- **"Table 5 comparisons not explained"** — The paper *does* explain these comparisons (lines 214–215): SfM positions fail on moving objects; MiDaS lacks temporal consistency. The integration details could be more precise, but the comparison is not unexplained.
- **"Cross-validation of thresholds"** — Sensitivity analysis (Tables 6–7) is standard practice for threshold selection in tracking papers; demanding formal cross-validation is outside the norms for this setting.
- **Request for more recent 2D MOT baselines on WOD** — Without external knowledge of whether ByteTrack/OC-SORT have published WOD results under comparable settings, this cannot be evaluated as a weakness.
- **"Preprocessing cost of pseudo-label generation"** — The paper's inference latency comparison is about online runtime, which is the relevant metric for an online tracker. The offline preprocessing cost is a one-time expense and is standard to exclude.
- **Strength Finder claim of "comprehensive ablation isolating each component"** — The ablation does not isolate GNN from 3D representation, so this strength conflicts with a verified weakness. It is removed per the conflict rule.

## Novel Insights

None beyond the paper's own contributions. The reviews add useful specificity about what is missing (coordinate transformation details, moving-object validation) but do not surface a fundamentally new perspective on the work itself.

## Suggestions

1. **Validate 3D predictions on moving objects.** Use the LiDAR ground truth available in Waymo/KITTI to compute per-object 3D position error (e.g., L1 distance in camera frame between predicted 3D point and ground-truth object center), reported separately for static and moving objects. This is the single most impactful experiment to support the paper's central claim.

2. **Clarify the global-to-camera coordinate transformation.** Add a sentence or figure explaining that SfM recovers camera poses as part of bundle adjustment, and that the global barycenter is transformed to each camera frame using the corresponding camera-to-world pose. If metric scale is ambiguous, explain how it is resolved.

3. **Add an ablation with GNN but without 3D representation.** Train a variant where the association head uses only appearance features in the GNN (no 3D feature). Compare this to the full method on the same setup to isolate the 3D representation's independent contribution.

4. **Report ID switches on WOD.** This metric directly supports the paper's motivation.

## Score and Decision

**Originality:** The pseudo-3D label generation from 2D tracklets + SfM is a novel contribution. The overall paradigm of learning 3D representation for 2D association is creative but builds on known ideas (SfM, 3D KF, GNN association). **7/10**

**Importance:** Addressing the 2D-to-3D lift for MOT is an important problem. The approach avoids expensive 3D annotations, which is practically valuable. **7/10**

**Claims supported:** The core claim that 3D representation improves association is partially supported (KITTI results are strong; WOD results are marginal). The claims about generalization to moving objects and SOTA status are not fully supported by the evidence presented. **5/10**

**Soundness:** The methodology is generally sound but has gaps (coordinate transformation unexplained, no direct moving-object validation, ablation conflates GNN and 3D representation). **5/10**

**Clarity:** The paper is clearly written and well-structured. The pipeline figures are helpful. Some technical details are omitted. **6/10**

**Value to community:** The pseudo-label generation pipeline could be useful to other researchers, and the results on KITTI are competitive. The code release would further increase value. **6/10**

The paper has a genuinely interesting core idea and shows meaningful results on KITTI. However, three issues prevent acceptance in current form: (1) the generalization to moving objects is asserted without any direct evidence, (2) the ablation conflates the 3D representation with the GNN architecture, and (3) the WOD results are marginal with lower IDF1. These are addressable in a revision but are structural gaps, not just presentation issues.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>