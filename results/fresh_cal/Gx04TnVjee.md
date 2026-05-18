Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

3DTrajMaster tackles multi-entity 3D motion control in text-to-video generation — the first method to use 6DoF pose sequences (location + rotation) as control signals for multiple entities. The core technical contribution is a plug-and-play 3D-motion grounded object injector with gated self-attention that associates entity descriptions with their trajectories. To handle the lack of training data, the authors construct a 54,000-video synthetic dataset (360°-Motion Dataset) using UE, GPT-generated trajectories, and 12-camera capture. They also introduce a video domain adaptor (LoRA-based) and an annealed sampling strategy to mitigate quality degradation from synthetic-domain training. Qualitative results show compelling 3D motion (e.g., 180° turns, occlusion handling) across diverse entities.

## Strengths

1. **First to tackle multi-entity 6DoF motion control in video generation** — No prior work handles 3D location, rotation, and z-depth for multiple entities simultaneously. The paper correctly identifies that 2D control signals (points, bboxes) cannot express 3D rotation or resolve 3D occlusions. This opens a new and meaningful direction for controllable video generation (Section 1, Table "Control Level").

2. **Well-designed architecture with clear ablation support** — The gated self-attention mechanism for entity-trajectory fusion (Section 3.2) is validated against cross-attention alternatives in the ablation study. The two-stage training (domain adaptor first, then object injector) and the annealed sampling strategy (Algorithm 1) are each ablated, with qualitative evidence (Figure 3) showing that removing the domain adaptor reverts to "purely UE-style appearance" and removing annealed sampling degrades video quality.

3. **Substantial dataset construction effort** — The 360°-Motion Dataset (54,000 videos, 70 3D assets, 12 cameras, 4 platform types) is a nontrivial engineering contribution that enables supervised training for a task where real-world paired 6DoF trajectory-video data does not exist (Section 3.3). The dataset construction pipeline is clearly described and reproducible.

4. **Compelling qualitative results** — Figures 4 and 5 demonstrate visually convincing 3D motion control for humans, animals, cars, and robots, including 180° turns, 3D occlusions (man walking in front of zebra), and fine-grained entity editing (hair, clothing, figure size). The gap with 2D baselines is visually stark.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated.

### Major

1. **Quantitative evaluation is restricted to human entities only** — The paper states (Section 4.3): *"Due to the absence of a pose estimator for open-world 4D objects, we limit our evaluation to only human objectives."* This means that for the majority of claimed controllable entities (animals, cars, robots), there is zero quantitative evidence that their 3D motions are correctly generated. While the paper acknowledges this limitation, the title claims "Mastering 3D Trajectory for Multi-Entity Motion" — and the quantitative evidence only supports the "human entity" subcase. Given that multi-entity control is the paper's central selling point, this is a significant evidential gap.

2. **Evaluation dataset shares distribution with training data** — The 100 evaluation pairs use 44 GPT-generated pose templates (same GPT pipeline as training), GPT-generated entity descriptions, and UE-rendered backgrounds from the same platforms used in training (Section 4.4). No real-world videos or out-of-distribution trajectories are used for testing. While the paper claims "novel" pose templates, these come from the same generative process, creating a risk of overfitting to the synthetic domain. The claim of "generalization" (title, Section 4.5) is not convincingly supported by evaluation on synthetic data that shares distribution with the training set.

### Minor

1. **No confidence intervals or variance reported** — No metric in the paper has confidence intervals, standard deviations, or significance tests. This is particularly concerning for the ablation study where the claimed improvements are modest (e.g., gated self-attention vs. cross-attention shows a 0.012 RotErr difference and a ~2-point FVD change). Without variance estimates, it is impossible to determine whether these differences are statistically significant, weakening the ablation's conclusions.

2. **Baseline comparisons are inherently asymmetric** — The three baselines (MotionCtrl, Direct-a-Video, Tora) all operate with 2D control signals. The paper correctly notes that 2D signals cannot express 3D motion, so it is unsurprising that a 3D method outperforms them. The paper would be strengthened by clearly framing the contribution as establishing a new task and benchmark rather than implying SOTA on an existing one. This does not diminish the contribution but would better calibrate reader expectations.

3. **No sensitivity analysis for key hyperparameters** — The LoRA scaler α and annealed timestep Tc are described as "chosen" (Section 3.4) but no range, grid, or trade-off analysis is provided. The paper mentions "more experiments in supplementary" for choosing suitable values, but the main text lacks even a simple plot showing the accuracy-quality trade-off as these parameters vary.

4. **Failure cases are not discussed** — The paper does not analyze scenarios where the model fails to follow a trajectory, produces implausible entity intersections, or degrades in quality. Including failure examples and analyzing their causes would increase trustworthiness and provide directions for improvement.

### Trivial

- Inference speed, GPU memory usage, and parameter counts relative to baselines are not reported.
- The pose encoder downsampler is described as using "interval sampling" with the note that "1D convolution achieved similar results" but no ablation is shown.
- The paper does not report video quality metrics for baselines *with their own 2D controls* as a reference point for the quality cost of 3D injection.

## Nice-to-Haves

- A small user study on motion plausibility (e.g., comparing 3DTrajMaster outputs against baselines on the same text prompts) would partially address the synthetic-evaluation concern without requiring real-world pose estimation.
- A proxy evaluation for non-human entities (e.g., tracking 2D object centers across frames and comparing against projected 3D trajectories) would provide at least some quantitative signal for animals/cars.
- Reporting analysis of the 360°-Motion Dataset's diversity (unique trajectory count, entity category distribution, motion speed distribution, trajectory completion rates).

## Removed Points

- **GLIGEN attribution (critic point)**: The reviewer noted the gated self-attention "closely follows GLIGEN without stating the adaptation." However, the paper explicitly writes *"Inspired by [li2023gligen], we employ a gated self-attention layer"* (Section 3.2). GLIGEN is correctly cited and the adaptation is clear. This criticism is a misreading.
- **"No direct comparison to any 3D motion method" framed as an evidential gap**: This is a consequence of the paper opening a new task. The authors correctly compare against the closest existing approaches (2D motion control methods). This is a framing nuance, not a weakness of the method, and it is already acknowledged by the reviewer as such. Moved to minor weakness above as a positioning suggestion.
- **Strength Finder claim about "state-of-the-art on both motion accuracy and video quality"**: The large margins (RotErr 0.277 vs 0.382+) are partly an artifact of comparing 2D and 3D methods on a 3D task. The numbers are reported accurately but the framing as "SOTA" is misleading without this context. I have instead noted the results as supporting evidence for the method's effectiveness on its own terms.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces the key tension in the paper: it has a genuinely novel and well-motivated technical approach to an important open problem, but the evaluation infrastructure for its own task is underdeveloped (no open-world 4D pose estimators for non-human entities, no real-world benchmark). This pattern — strong method on a new task with weak evaluation due to missing infrastructure — recurs in many early-stage controllable generation papers. The field would benefit from standardized real-world evaluation protocols for 3D motion control and broader-coverage pose estimation methods.

## Suggestions

1. **Add a real-world validation experiment, however small.** Even 10-20 examples with human-annotated motion plausibility ratings (e.g., "does the car in the generated video follow the specified 3D trajectory?") would significantly strengthen the generalization claim. Alternatively, use a proxy metric like 2D IoU trajectories for non-human entities estimated by an open-vocabulary tracker (e.g., SAM-track).

2. **Report confidence intervals or run ablations with multiple seeds.** At minimum, report standard deviations for the key metrics (RotErr, TransErr, FVD) over multiple runs or bootstrapped samples from the 100 evaluation pairs.

3. **Include a hyperparameter sensitivity plot** showing how varying α (LoRA scaler) and Tc (annealed timestep) trade off pose accuracy vs. video quality.

4. **Explicitly reframe the contribution** as establishing a new benchmark for 3D multi-entity motion control, rather than "state-of-the-art" relative to 2D methods. This would be more accurate and preempt the unfair-comparison criticism.

5. **Add a failure analysis section** with 2-3 representative failure cases (e.g., trajectory deviation for a non-human entity, implausible occlusion, quality degradation). This would make the paper more scientifically credible.

## Score and Decision

**Calibration anchors** (from batch retrieval):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0n4bS0R5MM.md` (VD3D) | 6.20 | Camera control for video transformers; cleaner evaluation on real-world data (RealEstate10K), comparable novelty. 3DTrajMaster tackles a harder problem (multi-entity 3D motion) but has weaker evaluation (synthetic-only). Roughly comparable overall. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AcAD4VEgCX.md` (I2VControl-Camera) | 6.50 | Camera/subject motion control with strong quantitative and qualitative evaluation. 3DTrajMaster has more technical novelty but less thorough evaluation. Slightly weaker than this anchor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uQjySppU9x.md` (SG-I2V) | 5.60 | Zero-shot trajectory control with cleaner evaluation but simpler technical contribution. 3DTrajMaster tackles a harder problem with more technical depth. Slightly stronger than this anchor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OBTmkKBmQW.md` (MotionFlow) | 4.00 | Camera trajectory control with presentation and clarity issues. 3DTrajMaster is notably stronger in both contribution and execution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/n6To2wAOKL.md` (Ctrl-V) | 4.00 | Bounding-box control for driving scenes with limited generalizability. 3DTrajMaster is stronger in both scope and novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/15lk4nBXYb.md` (CCM-DiT) | 3.00 | Camera control for DiT with limited results. 3DTrajMaster is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LbEWwJOufy.md` (TANGO) | 8.50 | Co-speech gesture video reenactment with thorough evaluation. 3DTrajMaster tackles a different (arguably harder) problem but does not approach this level of evaluation rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rzF0R6GOd4.md` (Neural SDF Flow) | 8.00 | Dynamic 3D reconstruction with strong mathematical framing. Not directly comparable. |

The paper's core contribution (first to do multi-entity 3D motion control in video generation) is genuine and well-motivated, and the technical approach is sound. However, the evaluation — restricted to human entities on a synthetic test set that shares distribution with training data, without variance estimates — does not fully support the claimed scope. This places it between the weaker controllable-generation papers (SG-I2V at 5.60) and the stronger ones (VD3D at 6.20, I2VControl-Camera at 6.50).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>