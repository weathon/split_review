Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

## Summary
This paper introduces 3DTrajMaster, a framework for controlling multi-entity 3D motions in text-to-video generation using 6DoF pose sequences (location and rotation). The core technical contribution is a plug-and-play 3D-motion grounded object injector with gated self-attention that associates each entity description with its corresponding 3D trajectory while preserving the video diffusion prior. To address training data scarcity, the authors construct a 360°-Motion Dataset (54K synthetic UE videos with 70 assets and 96 trajectory templates), and employ a LoRA-based domain adaptor plus annealed sampling to mitigate the synthetic-to-real domain gap.

## Strengths
- **Novel problem formulation and first use of 6DoF for multi-entity motion control in video generation.** The paper correctly identifies that 2D control signals (points, boxes, trajectories) cannot fully represent 3D motion properties like rotation and z-ordering. Using entity-specific 6DoF pose sequences as the control representation is a natural and underexplored direction. Table "control_level" confirms that 3DTrajMaster is the only method capable of controlling both location and orientation in 3D, while all 2D baselines lack z-dimension awareness.

- **Well-designed gated self-attention injector that preserves the video diffusion prior.** The entity-trajectory injection mechanism (Sec. 3.2) uses entity-wise addition to establish correspondence and gated self-attention (initialized from spatial self-attention weights, with a trainable gating parameter β) for motion fusion. The ablation (Table "ablation_main") demonstrates that replacing gated self-attention with cross-attention or placing the injector after 3D self-attention degrades motion accuracy and video quality, confirming the design choices are empirically grounded.

- **Strong quantitative results on human pose trajectory accuracy with large margins.** On trajectory accuracy, 3DTrajMaster achieves RotErr of 0.305 and TransErr of 0.082, compared to the next best baseline (MotionCtrl) at 1.455 and 0.786 — roughly 5× to 10× improvement. While this evaluation is limited to human entities (the only category with a reliable pose estimator), the margin is substantial and the metric follows established protocols from CameraCtrl.

- **Practical mitigation of synthetic-to-real domain shift.** The LoRA domain adaptor (trained on synthetic data, then attenuated during inference with reduced α) and the annealed sampling strategy (trajectory injection in early steps, drop-out in later steps) are thoughtfully designed. The ablation (Fig. "ablation") shows that removing either component visibly degrades video quality (reverting to UE-style rendering) while preserving most motion accuracy, indicating a favorable trade-off.

## Weaknesses

### Major
- **Quantitative trajectory evaluation is limited exclusively to human entities, leaving the core claim of "multi-entity" control partially unvalidated.** The paper's headline contribution is controlling motions across diverse entity types (human, animal, car, robot, natural force), yet Table 2's RotErr/TransErr metrics apply only to human entities. The authors acknowledge this on line 182 ("Due to the absence of a pose estimator for open-world 4D objects"), which is an honest admission of a genuine practical obstacle. However, the consequence is that the central claim — that 3DTrajMaster accurately controls 3D motions of non-human entities — rests entirely on qualitative examples. While qualitative evidence (Fig. "diverse_entity_bg") is suggestive, it does not establish that, e.g., the lion or zebra quantitatively follows its input 6DoF trajectory with the same accuracy as human entities. The paper would be substantially strengthened by at least one proxy quantitative signal for non-human entities (e.g., 3D bounding box IoU, or even human-annotated success/failure counts on direction matching).

- **Evaluation set is entirely synthetic/in-distribution, so generalization to real-world videos is unmeasured.** The model is trained on the synthetic 360°-Motion Dataset (UE renders), and the evaluation set (Sec. 4.4) uses novel GPT-generated pose templates and descriptions — still synthetic and in-distribution. The domain adaptor (LoRA) + annealed sampling are designed to handle synthetic-to-real shift, and qualitative results on real-world-like backgrounds are shown, but there is no systematic quantitative evaluation on in-the-wild real videos (e.g., using DAVIS-tracked objects). Without this, the claim of generalization to "diverse entities and backgrounds" remains supported by anecdotal evidence only.

### Minor
- **The comparison with 2D baselines, while the best available, inherently favors the proposed method.** MotionCtrl, Tora, and Direct-a-Video are designed for 2D control signals. The authors project their 3D trajectories onto 2D to feed these baselines (line 218). While this is the only feasible comparison (no existing 3D multi-entity motion control baselines exist), the 3D-to-2D projection discards information (rotation, z-depth) that is central to the paper's argument. The large margin in Table 2 is therefore partly attributable to the control representation rather than the architecture alone. A complementary baseline — e.g., adapting a 3D-capable camera control method like MotionCtrl (camera pose mode) to serve as a 3D spatial awareness lower bound — would help disentangle the contributions of the 3D representation from the injector architecture.

- **No metric explicitly measures multi-entity interaction quality (depth ordering, inter-entity separation).** The paper emphasizes handling 3D occlusions and entity-specific correspondence in multi-entity scenarios (the man-walking-in-front-of-zebra example), but no quantitative metric assesses whether the relative depth ordering of multiple entities matches the z-values in their input trajectories, or whether entity A's trajectory influences entity B's generated motion. The current evaluation aggregates per-entity metrics independently. A simple depth-order accuracy measure or inter-entity trajectory deviation check would strengthen this aspect.

- **"Domain adaptor" terminology is somewhat misleading.** The LoRA module is described as a "video domain adaptor" to mitigate the "MatrixCity style" of the training data. However, a true domain adaptor would adapt from synthetic to *real* distributions; in practice, the LoRA is trained on the synthetic data itself and then attenuated during inference. This is more accurately described as a method to prevent overfitting to the synthetic training domain rather than adaptation to a different target domain. This distinction is important for understanding the method's generalization properties.

### Trivial
- None.

## Nice-to-Haves
- **Evaluate trajectory accuracy for at least one non-human category** (e.g., animal) using an off-the-shelf keypoint tracker or 3D bounding box overlap, even if less precise than GVHMR for humans.
- **Include a controlled experiment** comparing against a version of MotionCtrl that receives camera poses only (to isolate the object-motion-control contribution of the injector architecture from the benefit of 3D awareness).
- **Report oracle/precision bounds** for GVHMR on the synthetic test videos to contextualize the reported RotErr/TransErr (i.e., how accurate is GVHMR itself on UE renders where ground truth is known?).
- **Ablate the number of entities** systematically (N=1,2,3,4+) to quantify performance degradation as entity count grows, rather than only reporting aggregated results.
- **Provide success/failure rate** on qualitative real-world-style generations (e.g., how often does the model produce a lion that follows its 3D trajectory plausibly?).

## Removed Points
These points were identified by reviewers or the strength finder but are not included as weaknesses/strengths in the main review, for the reasons stated below:
- **Strength Finder generic/superficial strengths removed:** The strength "Fine-grained editing of human entity descriptions" is a feature demonstration rather than a core contribution. It's retained as observable capability but not emphasized.
- **"Unfair comparison" criticism (Harsh Critic point 2) weakened and moved to Minor:** The claim that comparing 2D baselines (given 2D-projected trajectories) is "fundamentally unfair" overstates the case. There are no existing 3D multi-entity motion control methods to compare against; projecting to 2D is the standard way to compare across representation spaces. The asymmetry does not invalidate the comparison — the baselines receive their native input format. The remaining concern (that the control representation advantage confounds the architecture advantage) is included as a Minor weakness.
- **"No quantitative assessment of multi-entity motion accuracy" (Harsh Critic point 4) moved to Minor/Nice-to-Have:** The evaluation does measure per-entity trajectory accuracy in multi-entity scenarios (each multi-entity pair includes at least one human entity whose trajectory is evaluated). The request for depth-ordering metrics is reasonable but not a core flaw.
- **"Synthetic dataset generalization concern" (Harsh Critic point 3) retained as Major weakness but reframed:** The concern is valid but the paper does provide a domain adaptor design and annealed sampling specifically to address it, plus qualitative results. The weakness is that no *quantitative* real-world evaluation exists, not that the method ignores the problem.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a novel perspective that the paper itself does not articulate.

## Suggestions
1. **Provide quantitative trajectory accuracy for at least one non-human entity category.** Even a coarse proxy (e.g., 3D bounding box center deviation computed from depth maps, or human-annotated trajectory-direction correctness rates for animals/cars) would significantly strengthen the core claim of multi-entity control beyond humans.

2. **Include a small-scale real-world video evaluation.** Select 20-30 real-world video prompts (e.g., from DAVIS or tracked internet videos), generate with 3DTrajMaster, and report human-judged success rates for trajectory following. This would directly address the generalization concern.

3. **Add depth-order accuracy as an explicit metric** for multi-entity scenarios, measuring whether the z-ordering of generated entities matches the input trajectories' z-values.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison to 3DTrajMaster |
|---|---|---|
| Ctrl-Adapter (ny8T8OuNHe) | 7.00 | Stronger evaluation breadth and depth; broader framework contribution. 3DTrajMaster has more specific novelty but weaker empirical support. |
| CameraCtrl (Z4evOUYrk7) | 6.50 | Thorough evaluation on real data with clear ablations. 3DTrajMaster tackles a harder problem (multi-entity object motion vs. camera) but with weaker evaluation. |
| CamTrol (KI1zldOFz9) | 5.80 | Training-free camera control, accepted. Weaker technical contribution but stronger real-data evaluation. Comparable overall quality. |
| ReMoCo (LnN5UdhcjT) | 5.00 | Region-wise 2D motion control, rejected. 3DTrajMaster addresses a more challenging problem with a more novel approach and stronger results. |
| MotionFlow (OBTmkKBmQW) | 4.00 | Camera-trajectory video generation. 3DTrajMaster is significantly stronger in novelty, technical design, and results. |
| CCM-DiT (15lk4nBXYb) | 3.00 | Simple camera-pose control, rejected. Much weaker paper in all dimensions. |
| Single Motion Diffusion (DrhZneqz4n) | 7.50 | Motion animation synthesis with extensive evaluation. Different subfield but 3DTrajMaster's evaluation is substantially weaker. |

**Reasoning:** The paper addresses a genuinely novel and important problem (multi-entity 3D motion control in video generation) with a technically sound design. However, the structural limitation that quantitative trajectory accuracy is only measured for human entities, and the evaluation set is entirely synthetic/in-distribution, prevents the paper from fully establishing its central claims. The paper is stronger than rejected papers at the ~5.0 level (ReMoCo, MotionFlow) but does not reach the thoroughness of accepted papers at the ~6.5 level (CameraCtrl). It sits at the borderline where the technical contribution warrants consideration but the evaluation gaps are material. A revised version with at least one form of non-human quantitative evaluation and a systematic real-world test could reach the 6.5+ tier.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>