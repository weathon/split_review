Now I'll write the final consolidated review.

## Summary
This paper introduces 3DTrajMaster, a framework for controlling multi-entity motions in 3D space for text-to-video generation, using user-specified 6DoF (location + rotation) pose sequences. The core contribution is a plug-and-play 3D-motion grounded object injector with gated self-attention that fuses entity text descriptions with their 3D trajectories. To address training data scarcity, the authors construct the 360°-Motion synthetic dataset (54,000 videos) using Unreal Engine with GPT-generated trajectories. A LoRA-based domain adaptor and annealed sampling strategy mitigate quality degradation from synthetic data. The paper reports state-of-the-art trajectory accuracy on human entities, with qualitative results on animals, cars, robots, etc.

## Strengths

1. **First to address multi-entity 6DoF motion control in video generation.** The paper clearly identifies a genuine gap: prior work uses 2D control signals (points, boxes, sketches) that cannot express 3D rotation or depth ordering. The 6DoF pose sequence representation (rotation matrix + translation vector per entity per frame) is a principled choice for this problem. The motivation is well-argued in Section 1.

2. **Well-designed injector architecture with gated self-attention.** The entity-wise addition of text and pose embeddings to form bonded correspondences (§3.2), combined with a gated self-attention layer initialized from the 2D spatial self-attention weights, is a clean design. The plug-and-play nature (inserted after existing self-attention, not modifying base model weights) is validated in the ablation (§4.6) showing that replacing it with cross-attention or placing it after 3D self-attention degrades performance.

3. **Constructed 360°-Motion Dataset.** The dataset construction pipeline (§3.3) is well-described: collecting 70 animated 3D assets, using GPT-4V for text descriptions and GPT for 6DoF trajectory templates, rendering with 12 cameras on diverse UE platforms (city, desert, forest, HDRIs). This addresses a genuine data bottleneck and enables the proposed training.

4. **Practical quality-preserving techniques.** The domain adaptor (LoRA module trained first, then frozen) and annealed sampling (Algorithm 1: trajectory injection early, drop-out late) are simple but effective. The ablation (Fig. 5, Tab. 3) shows clear quality degradation when either is removed, validating their utility.

5. **Honest limitation discussion.** The conclusion (§6) acknowledges that generalization to non-human entities lacks fine-grained editing capability, that the model is constrained to global motion patterns, and that only ≤3 entities are supported. This transparency is appreciated.

## Weaknesses

### Major

1. **Quantitative evaluation limited to human entities despite claimed generalization.** The paper claims "state-of-the-art in both accuracy and generalization for controlling multi-entity 3D motions" (abstract) and shows qualitative results on animals, cars, and robots (Fig. 5). However, §4.3 explicitly states: "Due to the absence of a pose estimator for open-world 4D objects, we limit our evaluation to only human objectives." The quantitative results (Tab. 2) are exclusively on human entities. While the paper acknowledges this limitation, the core claim of *generalization* to diverse entities remains unverified by trajectory accuracy metrics. The qualitative results, while visually appealing, do not measure whether generated non-human motions match the input 6DoF trajectories. This narrows the paper's contribution from "multi-entity 3D motion controller" to "human-entity 3D motion controller with promising generalization shown qualitatively."

2. **Method built on an unreproducible internal video backbone.** The method is trained on "our internal video diffusion model for research purposes" (§4.1) with ~1B parameters. No architectural details, training data, or pretrained weights are provided. This creates two problems: (a) the reported results cannot be independently verified or built upon, and (b) it is unclear whether performance comes from the proposed injector or the proprietary backbone. The paper claims a "plug-and-play" injector, but this is only demonstrated on a single non-public model. Reproducing results on a public backbone (e.g., Stable Video Diffusion, CogVideoX, Wan) would significantly strengthen the contribution.

### Minor

3. **Evaluation dataset is curated and limited in motion diversity.** The evaluation set consists of 100 pairs from 44 pose templates and 72 GPT-generated descriptions, all containing at least one human entity (§4.4). The training dataset uses only ~96 trajectory templates (§3.3). The paper does not analyze trajectory distribution (range of rotations, speeds, occlusion patterns), making it difficult to assess the difficulty or coverage of evaluation. A motion diversity analysis would help contextualize the quantitative results.

4. **Entity-trajectory binding not stress-tested.** The addition-based entity-trajectory binding (§3.2) is not tested for disambiguation when entities have similar descriptions (e.g., "a tall man" vs. "a short man") or when trajectories cross. An ablation swapping trajectories between entities would validate that the binding generalizes beyond the training distribution's implicit spatial separation.

5. **Comparison to 2D baselines, while reasonable, tests an inherently favorable setup.** The paper projects 3D trajectories to 2D for MotionCtrl, Direct-a-Video, and Tora (§4.5). This discards z-axis and orientation information that 3DTrajMaster explicitly exploits. The resulting quantitative advantage (Tab. 2) is expected and confirms that more informative input representations yield better control, but does not isolate architectural benefits. This is a valid comparison approach (it tests "is 3D input better than 2D input for 3D motion following?"), but the framing could more clearly acknowledge this asymmetry. A comparison on a 2D trajectory-following task where both representations can be fairly evaluated would be informative.

6. **Ablation differences for motion fusion design are small.** The ablation (Tab. 3) shows only minor differences between gated self-attention, cross-attention, and placement after 3D self-attention. While the gated variant is best, the small margin weakens the claim that the specific architectural choice is critical. The more impactful components (domain adaptor, annealed sampling) show clear benefits.

### Trivial

7. Key implementation details not fully specified: FPS, exact training prompt templates, and the architecture of the internal video backbone beyond "DiT-based, ~1B params" are missing.

8. The evaluation metric (GVHMR for human pose estimation on synthetic videos) may suffer from domain shift. The paper acknowledges this but does not report sensitivity to alignment choices or estimator variance.

## Nice-to-Haves

- Releasing the 360°-Motion dataset (or a representative subset) under a permissive license would substantially strengthen the dataset contribution.
- A diagnostic test swapping trajectories between entities would validate that the binding mechanism works beyond memorization.
- Reporting trajectory distribution statistics (speed range, rotation magnitude, occlusion frequency) for both training and evaluation sets would improve reproducibility.

## Removed Points

- **"Comparison baseline projection is unfair"** — Weakened and moved to Minor (#5). The comparison is a standard way to evaluate cross-modal methods: convert the same task to each method's input format. The advantage of 3D over 2D input is exactly what the paper aims to demonstrate. However, the framing should acknowledge the asymmetry.
- **"Domain adaptor/annealed sampling not critical" / "ablation differences are too small"** — Weakened and moved to Minor (#6). While the motion fusion design differences are small, the domain adaptor and annealed sampling show clear benefits, mitigating this concern.
- **"Framing suggests broader ambition than delivered"** — Removed. The limitations are honestly stated in §6. "Simulating authentic dynamics" is a reasonable ambition statement for a first work in this direction.
- **"The GVHMR metric concern"** — Moved to Trivial (#8). The paper acknowledges this concern and it is a practical limitation shared by many works using off-the-shelf estimators.

## Novel Insights

Reviewer 4 of the TGT paper (which referenced 3DTrajMaster as prior work) noted that 3DTrajMaster was published at ICLR 2025. Beyond the paper's own contributions, the reviews reveal a recurring pattern in controllable video generation evaluations: quantitative metrics are almost always limited to entities or objects for which off-the-shelf estimators exist (humans via SMPL-family methods). Papers consistently show impressive qualitative results on other categories but cannot produce trajectory accuracy numbers for them. This suggests the field would benefit from standardized benchmarks with ground-truth 6DoF annotations across diverse object categories, or from proxy metrics (e.g., based on optical flow consistency, depth alignment, or learned 3D object detectors) that could be applied more broadly. The 360°-Motion dataset, being synthetic with known ground truth, could be extended to serve this role if released.

## Suggestions

1. **Quantitative evaluation on non-human entities.** Even a proxy metric — using off-the-shelf 3D object detectors for rigid categories (cars), keypoint consistency for animals, or depth alignment — would substantially strengthen the claim of generalization. The synthetic evaluation videos have ground-truth 6DoF; establishing an evaluation pipeline using rendered ground truth (rather than estimated poses) would be even cleaner.

2. **Validate on a public video backbone.** Demonstrating the plug-and-play injector on a widely-used model (Stable Video Diffusion, CogVideoX, Wan, or AnimateDiff) — even at smaller scale or fewer steps — would address the reproducibility concern and convincingly show that the method generalizes beyond the internal backbone.

3. **Release the dataset.** The 360°-Motion dataset construction pipeline is a significant contribution. Releasing the dataset or a representative subset would enable follow-up work and community benchmarking.

4. **Add entity-swapping diagnostic.** As a simple sanity check, swap trajectories between entities in the evaluation set and verify that the generated motions swap accordingly. This would validate that the addition-based binding is effective.

5. **Report trajectory distribution statistics.** Characterize the evaluation set by motion speed, rotation magnitude, occlusion frequency, and entity count to help readers assess difficulty and coverage.

## Score and Decision

**Score:** 5.0

**Decision:** Reject

**Calibration anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| DiTraj (zWRmev5IQ4.md) | 4.50 | R1 | Weaker: single-object, 2D bounding-box trajectory only |
| TGT (qUwOlwao20.md) | 5.00 | R1 | Comparable: similar evaluation gap but addresses 2D point trajectories |
| FlexTraj (3fIBwnz4Tf.md) | 4.00 | R1 | Weaker: limited technical novelty, engineering-focused |
| RealisMotion (AvW39dAR8R.md) | 4.50 | R1 | Comparable: similar internal dataset/reproducibility issues |
| 3DScenePrompt (3XxoBwMusJ.md) | 5.00 | R2 | Comparable: similar evaluation fairness concerns, but accepted as poster |
| SteinsGate (8WS5nDWIWE.md) | 6.00 | R2 | Stronger: inference-time, public backbone, more principled method |
| MoCtrl4D (JT6hR0sNXZ.md) | 2.50 | R1 | Much weaker: poor results, missing baselines |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>