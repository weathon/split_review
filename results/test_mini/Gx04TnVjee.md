Here is my consolidated final review.

---

## Summary

3DTrajMaster introduces a method for controlling multi-entity 6DoF (location + rotation) motion in text-to-video generation. The core contribution is a plug-and-play object injector that establishes entity-wise correspondence between text descriptions and 3D pose sequences via additive fusion and gated self-attention. The method is trained on a custom synthetic dataset (360°-Motion, 54k videos) rendered in Unreal Engine with GPT-generated trajectories. Experiments demonstrate large improvements in trajectory accuracy and video quality over 2D-based baselines (MotionCtrl, Tora, Direct-a-Video), with ablation studies validating the design choices.

## Strengths

1. **Novel problem formulation.** The paper is the first to tackle 6DoF multi-entity *object* motion control in 3D space for video generation. Prior work focuses on camera control or 2D object trajectories. The paper's Related Work section clearly surveys the landscape and establishes this gap (Section 2), and the task formulation (Section 3.1) precisely defines the multi-entity 3D control problem.

2. **Clean, well-motivated architecture.** The entity-wise additive fusion of frozen text embeddings with learnable pose embeddings, followed by gated self-attention initialized from the 2D spatial self-attention weights, is a simple and principled design. The ablation (Table 3) confirms that gated self-attention outperforms cross-attention fusion (RotErr 0.277 vs. 0.310, TransErr 0.201 vs. 0.307), validating this architectural choice.

3. **Strong quantitative results on trajectory accuracy.** On the human subset (where evaluation is feasible), the method achieves RotErr=0.277 and TransErr=0.201, substantially outperforming MotionCtrl (2.482/1.322), Direct-a-Video (2.092/0.960), and Tora (1.814/1.213). The margins are large and consistent across metrics.

4. **Qualitative generalization to diverse entities.** Figures 5 and 6 show the method controlling motions for humans, animals, cars, robots, and abstract natural forces, and supporting fine-grained editing of human attributes (hair, clothing, figure size). This demonstrates that the injector preserves the base model's prior and generalizes beyond the 70 training assets, as claimed.

## Weaknesses

### Fatal
None.

### Major

1. **Quantitative evaluation is limited to humans and to synthetic data from the same pipeline.** The paper explicitly states (§4.3): "Due to the absence of a pose estimator for open-world 4D objects, we limit our evaluation to only human objectives." All quantitative trajectory accuracy results are on humans only. The evaluation dataset (§4.4) is constructed from GPT-generated poses and synthetic backgrounds from the same UE platforms used for training. There is no evaluation on real-world videos, real motion capture data, or any distribution outside the synthetic pipeline. The paper's central quantitative claim ("state-of-the-art accuracy in controlling 3D entity motions") is therefore supported by evidence from a narrow subset (humans) within the training distribution. For non-human entities, only qualitative results are provided.

2. **The domain adaptor and annealed sampling are critical for reasonable quality, but their necessity raises questions about robustness.** The ablation (Table 3, Figure 4) shows that without the LoRA domain adaptor, FVD rises from 128.3 to 175.5, and without annealed sampling, FVD rises to 155.1, with clear visual degradation (UE-style artifacts). This means the base model, when trained only on synthetic data, does not naturally produce high-quality video; it requires inference-time modulations to suppress the synthetic style. The sensitivity of the LoRA scalar α is not analyzed (the paper only says "set α to a small value"), and the annealed cutoff timestep Tc is similarly untreated. These are free parameters whose tuning requirements are unexplored.

### Minor

1. **Baseline comparisons conflate 3D representation advantage with architectural advantage.** The paper projects its 3D trajectories onto 2D for MotionCtrl, Tora, and Direct-a-Video (§4.2). This comparison primarily demonstrates that 3D control > 2D control, which is expected given the experimental setup. The paper would be strengthened by an ablative baseline that uses the same architecture but with 2D-only trajectories (e.g., dropping rotation and z-axis translation) to isolate the specific benefit of 3D representation from the benefit of the injection architecture. The paper does not include this ablation.

2. **The pose encoder design is not ablated.** The pose encoder is described as "a linear layer and a downsampler" with a note that "we also tried several sequential one-dimensional convolution layers but achieved similar results" (§3.2). No quantitative comparison between encoder variants is provided. While this is unlikely to change the paper's conclusions, a proper ablation would strengthen the method section.

3. **The evaluation limitation is not acknowledged as an evidential weakness.** The Conclusion/Limitations section discusses the inability to edit animals with fine granularity and the ≤3 entity constraint, but does not acknowledge that the quantitative results are restricted to humans and synthetic data. This omission means readers could over-interpret the quantitative claims.

### Trivial
None.

## Nice-to-Haves
- A proxy for non-human motion accuracy (e.g., optical flow consistency, 2D reprojection error from detection) to extend quantitative evaluation beyond humans.
- A small-scale real-world validation set (e.g., human motion capture with real background videos) to test generalization beyond the synthetic pipeline.
- Sensitivity analysis of the LoRA scalar α and the annealed timestep Tc.
- An ablative 2D-only trajectory variant of the proposed method to isolate the 3D representation benefit from the architecture benefit.

## Removed Points
- **"The paper does not survey whether any prior work achieves partial such control"** — The paper *does* survey prior work in Section 2, explicitly stating that "none address the customization of object motion in 3D space." This criticism is factually wrong.
- **"Comparison with SynCamMaster/CameraCtrl is insufficiently contrasted on the object-control axis"** — The paper clearly distinguishes camera-control methods from its object-motion-control task. Requesting deeper contrast on an axis where these methods are not designed to operate is scope creep.
- **"The central claim 'first to customize 6DoF multi-entity motion' is overstated"** — The literature review supports this claim; the paper identifies a genuine gap. This criticism is not evidence-based.
- Various pure formatting/writing nitpicks from the section-by-section notes — parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions. The reviewers' observations converge on a standard pattern: the paper addresses a well-motivated, novel problem with a clean method, but the experimental validation is narrower than the claims warrant. The domain adaptor/annealed sampling dependency is the most interesting nuance — the method relies on inference-time domain suppression to achieve quality, which is a pragmatic engineering choice but limits confidence in its robustness to distribution shift. The calibration comparison reveals that this pattern (novel problem + clean method + imperfect evaluation) is common in this rapidly moving area, and the paper's contribution is comparable to accepted camera-control papers.

## Suggestions
1. **Expand quantitative evaluation beyond humans.** The most impactful revision would be to provide a proxy metric for non-human entities. Options include: (a) optical flow consistency between generated frames and rendered reference trajectories, (b) 2D bounding box IoU between detected objects and projected 3D trajectories, or (c) a human evaluation study on trajectory adherence for non-human entities.
2. **Add a small real-world test set.** Even 5–10 real-world prompts with hand-drawn 3D trajectories would substantially strengthen the generalization claim. The current all-synthetic evaluation is the paper's biggest vulnerability.
3. **Add an ablative 2D-trajectory variant of 3DTrajMaster.** By dropping the rotation and z-translation components, the paper could directly measure the value of full 3D representation vs. 2D within the same architecture, making the baseline comparison more informative.
4. **Report α and Tc sensitivity.** The paper should state the specific α value used and show how quality/accuracy vary with α and Tc over a small grid.
5. **Acknowledge the evaluation limitation explicitly in the Limitations section.** This would improve the paper's scientific candor.

## Score and Decision

**Calibration anchors (all from the same review corpus):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| CCM-DiT (15lk4nBXYb.md) | 3.00 | Rejected. Poor presentation, limited experiments, marginal novelty. 3DTrajMaster is substantially stronger in all dimensions. |
| MotionFlow (OBTmkKBmQW.md) | 4.00 | Rejected. Camera control with limited evaluation. 3DTrajMaster has a cleaner method and more novel problem formulation. |
| Ctrl-V (n6To2wAOKL.md) | 4.00 | Rejected. Bounding-box control for driving. Narrower scope, weaker results. |
| CamTrol (KI1zldOFz9.md) | 5.80 | Accepted. Training-free camera control. Comparable quality — both have clear methods and reasonable-but-imperfect evaluations. |
| VD3D (0n4bS0R5MM.md) | 6.20 | Accepted. Camera control for DiTs. Stronger evaluation (RealEstate10K benchmark), but less novel problem (incremental over CameraCtrl). |
| I2VControl-Camera (AcAD4VEgCX.md) | 6.50 | Accepted. Camera control with motion strength. Similar evaluation concerns (small dataset). |
| CameraCtrl (Z4evOUYrk7.md) | 6.50 | Accepted. Camera control for T2V. Well-executed but incremental. |

**Assessment:** The paper compares favorably to the low-scoring anchors (3–4) in all dimensions. Relative to mid-scoring anchors (5–6), it has a more novel problem formulation but a weaker evaluation (entirely synthetic + humans only). Relative to high-scoring anchors (6+), it has a more ambitious scope but less thorough validation. The core architectural contribution is clean and well-justified. The main weaknesses (synthetic-only quantitative evaluation, domain adaptor dependency) are significant but not fatal — they are addressable in revision and do not invalidate the core contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>