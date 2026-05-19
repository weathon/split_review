- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have all the information needed. Let me construct the final consolidated review.

## Summary
This paper introduces 3D Gaussian Splatting (3DGS) into 3D Object Detection (3DOD) for the first time, proposing two lightweight strategies—Boundary Guidance (overlaying 2D object boundaries on training images to improve Gaussian blob spatial distribution) and Box-Focused Sampling (using 2D bounding boxes to construct 3D probability spaces for probabilistic sampling). Both strategies add zero learnable parameters. The full method (3DGS-DET) achieves +5.6 mAP@0.25 over a basic 3DGS pipeline on ScanNet and outperforms the NeRF-based NeRF-Det by +6.6 mAP@0.25 on ScanNet and +31.5 on ARKITScenes.

## Strengths
1. **First integration of 3DGS into 3DOD.** The paper is explicit about being the first to use 3DGS as a representation for 3D object detection (Abstract, Section 1), and the related work confirms no prior work has done this. This is genuine novelty.

2. **Clean, parameter-free strategies with verified gains.** Boundary Guidance improves the basic pipeline by +2.4 mAP@0.25 (54.3→56.7), and Box-Focused Sampling adds another +3.2 (56.7→59.9), both without introducing any learnable parameters. The ablation table (lines 253-290) provides clear evidence of each component's contribution.

3. **Ablation comparing different priors is informative.** The paper compares boundary guidance against center point guidance (54.4) and mask guidance (54.9) under identical settings (Table 1, lines 259-268), with a reasoned explanation for why boundaries work best—they preserve surface texture while providing shape cues (Fig. 4, lines 303-311).

4. **Strong results against NeRF-based methods.** On ScanNet, 3DGS-DET outperforms NeRF-Det by +6.6 mAP@0.25 and +8.1 mAP@0.5. The basic pipeline alone (54.3) already surpasses NeRF-Det (53.3), suggesting the explicit 3DGS representation offers structural advantages for detection.

## Weaknesses

### Major
1. **No controlled comparison against raw point clouds with the same detector.** The paper uses FCAF3D (a point-cloud detector) as its backbone but never reports what FCAF3D achieves when trained directly on raw ScanNet point clouds under the same conditions. The paper's comparison table (Section 4.2) includes point-cloud-based methods in a "first block," but these use different architectures, preprocessing, and training regimes—not an apples-to-apples comparison that isolates whether the 3DGS representation itself is beneficial, neutral, or detrimental compared to the original sensor data. This weakens the paper's core narrative that "introducing 3DGS into 3DOD" is a valuable contribution.

2. **ARKITScenes result (+31.5) reported on an uncharacterized subset.** The paper follows NeRF-Det's subset of ARKITScenes (described only as "low-resolution images") but does not specify the number of scenes, frames, or object instances in this subset. The +31.5 margin over NeRF-Det is extreme and needs more analysis—e.g., is NeRF-Det essentially broken on this subset, or is the subset very small and high-variance? The paper provides no discussion of this.

3. **No statistical variance reported.** All results are single numbers. The ablation gains of +2.4 and +3.2 mAP@0.25 are modest, and 3DGS training is stochastic (random initialization, densification). Without error bars or multiple runs, these improvements may fall within run-to-run variance.

### Minor
1. **Key hyperparameters unspecified.** (a) The sampling size M is only given as "M < N" (line 119), never the actual number used. (b) The background probability p_bg=0.01 (line 200) is set without ablation. Both directly affect the method's behavior and reproducibility.

2. **No runtime comparison despite using speed as motivation.** The paper repeatedly motivates 3DGS by "faster rendering speeds" (lines 5, 26-27, 56-57) compared to NeRF, but provides no training or inference time measurements whatsoever in the context of the detection pipeline.

3. **No discussion of limitations.** The paper ends with a purely positive conclusion (lines 333-336). Obvious limitations worth acknowledging include: reliance on pre-trained 2D models (Grounded SAM, Grounding DINO), assumption that 2D boundaries are good proxies for 3D object boundaries, and the requirement for multi-view posed images (same as NeRF-Det).

### Trivial
- None beyond what the parser artifacts caused (broken table references, etc.), which are not author errors.

## Nice-to-Haves
- A sensitivity analysis on p_bg (the background probability threshold) and the number of sampled Gaussians M would strengthen the Box-Focused Sampling story.
- A quantitative analysis of how many Gaussians fall inside vs. outside ground-truth bounding boxes before and after Box-Focused Sampling (rather than just qualitative visualization) would make the mechanism's effectiveness more rigorous.
- A breakdown of per-category results on the ARKITScenes subset would help contextualize the +31.5 improvement.

## Removed Points
These points from the reviewers are excluded with justification:
- **Garbled table references ("\tabref{tab:main_result_0.")** — This is a parser artifact from LaTeX extraction, not an author error. Removed per hard rules.
- **Concern that "zero additional learnable parameters" is misleading** — The paper clearly states it uses pre-trained 2D models (Grounded SAM, Grounding DINO); "zero additional" refers to parameters beyond the existing pipeline. The paper is not claiming self-supervision. Removed as a misreading.
- **"No formal argument" about boundary guidance spatial distribution** — The paper provides ablation (+2.4 points) and qualitative visualizations showing the effect; this is appropriate empirical evidence for a systems paper. The demand for formal proof is disproportionate to the paper's scope.

## Novel Insights
None beyond the paper's own contributions. The two-reviewer synthesis confirmed the paper's technical soundness and genuine novelty, while also surfacing that the evaluation is weaker than the method itself deserves. The most interesting structural observation is that the paper is caught between two comparison regimes: it wants to claim "3DGS is a great representation for 3DOD" but only benchmarks against the closest view-synthesis competitor (NeRF-Det), not against the raw point-cloud input that the same detector natively consumes. Closing this gap would sharpen the paper's thesis considerably.

## Suggestions
1. **Add FCAF3D-on-point-clouds as a controlled baseline.** Run the same detector (FCAF3D) with the same hyperparameters and training schedule on raw ScanNet point clouds. This directly answers whether 3DGS representation helps, hurts, or is neutral for detection. If 3DGS is worse but offers other benefits (novel view synthesis), make that trade-off explicit.
2. **Report variance.** At minimum, report 3-run means and standard deviations for the main results and key ablations. The +31.5 on ARKITScenes especially needs verification.
3. **Characterize the ARKITScenes subset.** State the number of scenes, frames, and object instances in the NeRF-Det subset, and discuss why the gain is so large.
4. **Report M and add p_bg ablation.** Specify the actual number of sampled Gaussians and show sensitivity to the background probability threshold.
5. **Add a limitations paragraph.** Acknowledge reliance on 2D pre-trained models, the multi-view requirement, and potential failure cases.
