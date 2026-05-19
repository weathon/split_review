Now I have a thorough understanding of the paper. Let me construct the final consolidated review, carefully verifying each claim against the actual paper text.

---

## Summary

The paper presents a pipeline for estimating 6D object poses from a single RGB image without knowing the object's exact CAD model, by (i) retrieving a similar mesh from a large database (Objaverse-LVIS + GSO), (ii) aligning it via view-matching with DINOv2 features, and (iii) grounding absolute scale using monocular depth prediction and an LLM (GPT-4). The estimated per-frame poses are then refined into smooth trajectories using dense point tracking and retargeted to a robotic manipulator via trajectory optimization. Quantitative results on YCB-V and HOPE-Video show substantial improvements over MegaPose, GigaPose, and FoundPose when all methods are given retrieved (approximate) meshes. Qualitative demonstrations on Internet videos, EPIC-KITCHENS, and a real robot are provided.

## Strengths

- **Strong quantitative results on standard pose estimation benchmarks with unknown meshes**: On YCB-V and HOPE-Video, the proposed method achieves significantly higher mean AR across all metrics than MegaPose, GigaPose, and FoundPose when all methods use the same retrieved (non-ground-truth) meshes (Table 1). This provides clear evidence that the pipeline's design choices (FFA-based retrieval + view alignment + scale grounding) are better suited to approximate meshes than existing methods developed for known meshes.

- **Training-free pose estimation for objects without known 3D models**: The method requires no fine-tuning or per-object training. It combines open-set detection, foundation model features (DINOv2), an LLM, and off-the-shelf components into a single pipeline. This zero-shot property is a genuine advantage over category-level methods that require canonical-frame assumptions and model-free methods that need multi-view onboarding.

- **LLM-based scale estimation demonstrably improves over naive scaling**: Table 3 (referenced in text) shows a 55% improvement in average Chamfer distance recall over a constant 10cm baseline. Even though this baseline is weak, the ablation provides evidence that the LLM component contributes positively to final pose quality.

- **Detection of objects outside the annotated ground-truth set**: Figures 3 and accompanying text show the method detecting and aligning a chair and a keyboard in YCB-V scenes that are not among the dataset's annotated objects. This highlights a practical advantage over methods restricted to a fixed object list.

- **End-to-end system demonstration from Internet video to robot execution**: Figure 6 and Section 3.2 show the complete pipeline applied to instructional Internet videos, with the extracted trajectories executed on a real Franka Emika Panda robot. This demonstration combines multiple components (pose estimation, tracking, trajectory optimization) into a working system.

## Weaknesses

### Fatal

None. No verified weakness invalidates the paper's core claims.

### Major

- **Tracking and robot manipulation — claimed in the title and contributions — are evaluated only qualitatively.** Section 4.2 is explicitly titled with "Qualitative results" and the robot demonstration is shown as a single video example (Figure 6, "shaking a jug"). The paper's title foregrounds "Pose Tracking" and "Robotic Manipulation," and the contribution list (Section 1, bullet 2) claims "extract[ing] smooth 6D object trajectories" and retargeting them to a robot. Yet neither the tracking quality (e.g., trajectory error, temporal smoothness, success rate across videos) nor the robot success (e.g., task completion over multiple trials) is measured. The quantitative evaluation in Section 4.1 is exclusively on single-frame pose estimation. This creates a significant gap between what the paper claims and what it measures. While qualitative demonstrations are valuable for an emerging pipeline, the absence of any tracking metric or structured robot evaluation weakens the support for two of the paper's four claimed contributions.

- **The scale estimation ablation compares against an unreasonably weak baseline.** Table 3 reports that the proposed LLM-based scale estimation improves average Chamfer distance recall by 55% over a "constant model scaling" of 10cm (lines 131–132). A universal 10cm is a strawman — many objects in YCB-V (e.g., a banana, a cracker box, a mustard bottle) are not 10cm in any dimension. Beating this baseline does not demonstrate that the LLM-based scale is accurate; it only shows it is better than a default guess. A meaningful baseline would be using the mean metric size of the *retrieved* CAD model (if scale metadata exists in Objaverse/GSO) or a category-mean size from a static lookup table. As written, the 55% figure is not informative about the absolute quality of the scale estimates.

### Minor

- **The scale estimation method is not fully specified.** The text (line 81) states: "We assign relative scale r_i to every object i as distance between the furthest object points along object's principal axis as computed from the point cloud obtained from the monocular depth predictor (Bhat et al.)." The specific monocular depth model (a reference truncated by the parser; the superscript "2" suggests a footnote) and the procedure for determining the "principal axis" from the point cloud are not described. The GPT-4 prompt is not provided, and no sensitivity analysis to prompt wording or LLM version is included. While individual components are standard, their combination is novel and the lack of detail hinders reproduction.

- **No direct analysis of retrieval quality or its impact on downstream performance.** Table 2 compares retrieval methods (OpenShape, CLS token, FFA) but only reports final pose metrics, not retrieval accuracy (e.g., top-1/5 recall of correct category or geometry-similarity scores). Without knowing whether the 44% improvement over OpenShape comes from better retrieval or better robustness to imperfect retrieval, the contribution of the retrieval component is conflated with the alignment component. Additionally, because YCB-V and HOPE-Video contain common household items that are well-represented in Objaverse-LVIS and GSO, the results may overestimate performance on genuinely novel objects. Characterizing when retrieval succeeds or fails would significantly strengthen the paper.

- **No variance or error bars reported for main results.** Table 1 reports single numbers without confidence intervals, standard deviations, or multiple-run statistics. For a pipeline with stochastic components (view sampling, segmentation, LLM queries), the stability of results is unclear.

- **The finding about ground-truth masks producing worse scale estimates lacks statistical support.** The paper states (lines 133–134): "the scale estimation error in this case is worse than using our method to obtain the masks. This can be explained by the fact our method detects additional objects in the background, such as chairs, that are not in the ground truth masks but help with the scale estimation." This is an interesting claim but no sample size or statistical test is given, and it implies scale estimation degrades in scenes with few objects — a limitation that should be stated explicitly rather than presented as a strength of the method.

### Trivial

- None.

## Nice-to-Haves

- Reporting what MegaPose/GigaPose achieve with ground-truth meshes on the same datasets would provide a useful upper-bound reference, though the comparison is already fairly framed as within the unknown-mesh setting.
- A runtime breakdown by pipeline stage (detection, retrieval, alignment, scale estimation, tracking) would help readers assess practical applicability.
- Direct validation of scale estimation accuracy (comparing estimated metric sizes to ground-truth object dimensions from YCB-V) would be more informative than the current downstream-only ablation.
- Reporting retrieval recall (e.g., top-5 category accuracy) on the test datasets would help isolate the retrieval bottleneck.
- For a paper claiming "Pose Tracking," a simple quantitative tracking metric (e.g., trajectory end-point error, or temporal consistency measured via acceleration penalty on HOPE-Video's sequences) would meaningfully support the claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that the baseline comparison is insufficient because the paper doesn't report ground-truth-mesh performance.** *Reason for removal:* The paper (line 115) explicitly states "This simulates the in-the-wild scenario where no ground-truth meshes are available," and both baselines are given the same retrieved meshes "for a fair comparison" (line 119). The comparison is fairly scoped to the unknown-mesh setting; requesting ground-truth-mesh numbers is a scope-creep concern. Moved to Nice-to-Haves.

- **"No analysis of impact of DINOv2 feature choice" and "how many rendered views are used" and "which specific patch features."** *Reason for removal:* These are standard implementation details that are likely specified in the appendix (stripped by the parser). The paper explicitly states using patch-level feature maps from DINOv2 with FFA aggregation and the viewpoint sampler of Alexa (2022). This level of detail is adequate for a conference paper.

- **Criticism about the "monocular depth predictor (Bhat et al.)" being a missing reference.** *Reason for removal:* The superscript "2" suggests a footnote that was stripped by the PDF parser. Per the hard rule, parser artifacts are not author errors. The broader concern about method underspecification is retained (Minor weakness #1), but the specific complaint about a missing reference is removed.

- **"No open-set detection evaluation" and "No timing or computational cost."** *Reason for removal:* These are additional experiments that would strengthen the paper but are beyond the stated scope. Moved to Nice-to-Haves.

- **Strength: "LLM-based scale estimation yields 55% improvement over constant scaling."** *Reason for removal:* This strength conflicts with the verified weakness that the constant 10cm baseline is a strawman. The improvement is real but uninformative; citing it as a "strength" overstates its evidential value. The underlying observation that the LLM contributes positively is kept implicitly through the ablation discussion in weaknesses.

- **Strength Finder claims about the paper addressing an "important problem" or being "a significant step."** *Reason for removal:* Generic/superlative framing without specific evidence. Concrete strengths (quantitative results, training-free property, etc.) are retained above.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely reframe or contextualize what the paper already presents, without identifying an unrecognized implication or contradiction that advances understanding.

## Suggestions

1. **Add quantitative tracking evaluation.** At minimum, compute trajectory error (e.g., average translation/rotation error vs. ground-truth poses) on HOPE-Video's video sequences, or report temporal smoothness (e.g., reduction in per-frame jitter from tracking refinement vs. running the single-frame pipeline independently on each frame).

2. **Strengthen the scale estimation ablation.** Replace or supplement the "constant 10cm" baseline with a more meaningful competitor: (a) the metric size of the retrieved CAD model if scale metadata exists, or (b) a fixed category-level size lookup table (e.g., from WordNet or common dimensions). If possible, also report the estimated scale directly against ground-truth object sizes (available in YCB-V).

3. **Report retrieval accuracy directly.** Add a column in Table 2 showing top-1 or top-5 retrieval recall on the test datasets. Stratify the pose results by whether the retrieved model is visually/geometrically similar to the ground-truth object to clarify when the method works.

4. **Report variance/error bars.** Run the main experiment (Table 1) multiple times or report bootstrap confidence intervals to establish result stability.

5. **Clarify the scale estimation details.** Specify the monocular depth model used, describe how the "principal axis" is determined from the point cloud, and include the GPT-4 prompt either in the main text or an accessible supplementary.

## Score and Decision

The paper makes a real contribution: a training-free pipeline for 6D pose estimation without known CAD models that demonstrably outperforms existing methods on standard benchmarks under this challenging setting. The pose estimation results (Table 1) are the paper's strongest evidence. However, the paper's title and contribution list make claims about *pose tracking* and *robotic manipulation* that are only supported by qualitative demonstrations, and the scale estimation ablation uses a baseline too weak to be informative. These are significant gaps that prevent the evidence from matching the scope of the claims. With targeted revisions — particularly adding tracking metrics, strengthening the scale ablation, and reporting retrieval quality — the paper could become a strong contribution.

**MY FINAL SCORE:** <score>5.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>