Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

The paper proposes CasualHDR, a one-stage method for reconstructing 3D HDR scenes from casually captured videos with auto-exposure, unknown exposure times, and motion blur. The method jointly optimizes a continuous-time SE(3) camera trajectory, per-frame exposure times, camera response function (CRF), and a 3DGS-based HDR scene representation within a differentiable physical imaging model. The approach enables three downstream applications: novel view synthesis, image deblurring, and HDR editing.

## Strengths

- **Physically motivated joint optimization over a genuinely challenging problem setup**: Section 3.3 (Eq. 4–6) presents a unified physical image formation model that couples exposure time, CRF, camera trajectory, and 3DGS scene representation. Unlike prior HDR-3D methods (HDR-NeRF, HDR-GS) which require known exposure times and static cameras, CasualHDR removes these constraints by treating exposure time as an optimizable quantity (stated explicitly: "we treat Δt as an optimizable quantity rather than a precisely known parameter"). This is a meaningful advance toward practical HDR 3D reconstruction with consumer-grade cameras.

- **Continuous SE(3) B-spline trajectory covering the full video**: Section 3.2 introduces a cumulative B-spline representation (Eq. 3) that models camera motion continuously over the entire capture period. This contrasts with prior deblurring works (e.g., BAD-NeRF) that estimate separate short splines per frame, and enables cross-frame motion constraints.

- **Ablation study isolates each component's contribution**: The paper reports (in text) that removing the continuous trajectory reduces PSNR by ~24%, removing exposure time optimization and CRF reduces PSNR by ~42%, and removing the deblur module reduces PSNR by ~9% (Table 6 / Section 4.6). These numbers directly support the claim that each module matters.

- **Multi-application capability from a single reconstruction**: The method demonstrates novel-view synthesis, image deblurring of training views, and HDR editing (Figure 3), showing practical versatility beyond methods that target only one task.

- **New challenging dataset**: Section 4.1 describes a dataset combining synthetic Blender scenes and real captures (CasualVideo) with severe brightness variation and motion blur, including ground truth poses from Vicon and measured exposure times.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Unclear evaluation protocol on real-world data**: The paper states "we select 5 to 10 sharp images for each sequence to evaluate metric" (Section 4.4) but does not clarify whether these sharp images are held out from training or used during training. If they are training views, the NVS evaluation measures reconstruction fidelity rather than novel view synthesis. If held out, the test set is very small (5–10 images). The paper should explicitly state the train/test split and whether test images were excluded from the input to the method. This ambiguity makes the reported real-world numbers harder to interpret.

- **Baseline comparisons are informative but asymmetrically disadvantaged**: Baselines such as HDR-NeRF, HDR-Plenoxels, and Gaussian-W were designed for settings with known exposure times and static cameras. The paper acknowledges that "HDR-NeRF failed in all scenes on the real dataset" and that many methods "struggle without ground-truth camera poses." While demonstrating that a new method works where prior ones fail is legitimate, the claim of "state-of-the-art performance" would be strengthened by including an adapted baseline variant (e.g., giving prior methods estimated exposure times or Oracle poses) to isolate whether the gains come from the joint optimization or simply from the differing problem setup.

- **Exposure time initialization and constraints are unspecified**: Section 3.3 states that Δt "can be assigned a random value" but does not specify the initialization range, whether bounds are imposed during optimization, or how the method avoids trivial/degenerate solutions. This detail affects reproducibility.

- **Sensitivity analysis for the number of virtual cameras N is missing**: The paper fixes N=10 without ablation. This parameter directly controls the fidelity of motion blur modeling and the computational cost. A brief analysis would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- Including a baseline variant where prior HDR methods are given ground-truth exposure times and poses would help quantify how much of the gain comes from the new problem formulation vs. the method itself.
- A failure analysis on real data (which scenes/conditions cause the method to struggle) would improve completeness.
- Additional tone-mapped qualitative comparisons against other HDR reconstruction methods would strengthen the visual evidence.

## Removed Points

- **Criticism about tables being images / quantitative results inaccessible**: The tables are present in the original PDF as embedded images — this is a parser limitation, not a paper flaw. Moreover, the paper does report key summary statistics in text (e.g., "~24% PSNR improvement," "~42% increase") for the ablation study. Removed per rules on parser artifacts.

- **Criticism that "no summary statistics outside tables"**: Factually incorrect — the paper reports the 24%, 42%, and 9% ablation numbers in plain text in Section 4.6.

- **Claim that the paper does not establish its contribution**: Overstated. The method is clearly described, the ablation study shows meaningful improvements, and the problem is well-motivated. The contributions are verifiable in principle even if the evaluation clarity could be improved.

- **Strength Finder claim about "SOTA quantitative results across multiple tasks"**: The exact numbers in tables are unverifiable from the text extraction, but the paper's textual claims and ablation percentages are legitimate. Kept as a qualified strength.

- **Strength Finder generic/superficial strengths**: Filtered out generic praise about "important problem" that lacked specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension typical of papers proposing a new, harder problem setting: the baselines are necessarily disadvantaged (they were not designed for this setting), which makes the claimed SOTA meaningful but also makes it hard to attribute how much of the gain comes from the method vs. the relaxed problem assumptions. An insightful ablation would be to give baselines Oracle exposure times and poses to isolate this.

## Suggestions

- **Clarify the train/test split for real-world sequences explicitly.** State whether the 5–10 sharp images used for evaluation are part of the input video or separate held-out captures. If they are part of the input, reframe the evaluation to distinguish reconstruction fidelity from novel view synthesis.
- **Add an ablation giving baselines (HDR-NeRF, HDR-Plenoxels, Gaussian-W) ground-truth exposure times and/or poses** to separate the effect of the harder problem setting from the method's joint optimization.
- **Report the initialization range and optimization bounds for exposure times** and include a brief sensitivity analysis for the virtual camera count N.

## Score and Decision

**Anchor comparisons:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/P4o9akekdf.md` (NoPoSplat) | 8.0 | Much stronger — feed-forward, no poses, broad generalization, tighter evaluation |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xPxHQHDH2u.md` (Ref-Gaussian) | 6.5 | Stronger — more rigorous evaluation and clearer baseline comparison, similar level of technical contribution |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dkrEoT68by.md` (Gaussian Splatting Lucas-Kanade) | 6.0 | Slightly stronger — evaluation is cleaner, but problem novelty is comparable |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/L3WnnnBRdu.md` (Hi-Gaussian) | 5.75 | Comparable — similar limitations in evaluation clarity and baseline fairness |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nkeF3iRJRo.md` (SCISplat) | 5.0 | Weaker — less problem novelty, more incremental |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fRXAQfHlmr.md` (studentSplat) | 4.25 | Much weaker — questionable contribution, poor evaluation |

The paper addresses a genuinely novel and well-motivated problem with a physically grounded solution. However, the evaluation has clarity issues (unclear train/test split for real data, unspecified exposure time initialization details) and the baseline comparisons are asymmetrically disadvantaged in a way that is acknowledged but not fully disentangled. The core contribution is real, but the paper does not present it as convincingly as it could. Compared to the anchors, it sits below Ref-Gaussian (6.5) and Gaussian Splatting Lucas-Kanade (6.0) but above SCISplat (5.0), in the 5.5 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>