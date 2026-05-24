Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes **CasualHDR**, a unified 3DGS-based framework for reconstructing HDR 3D scenes from casually captured videos with auto-exposure, motion blur, and unknown exposure times. The key idea is a differentiable physical imaging model that jointly optimizes continuous camera trajectory (SE(3) B-spline), exposure times, camera response function (CRF), and a 3DGS HDR scene representation. Experiments on synthetic and real datasets show large and consistent improvements over existing baselines in novel view synthesis, deblurring, and pose estimation tasks.

## Strengths

- **Novel unified formulation for a practical problem.** The paper integrates exposure time optimization, CRF estimation, continuous-time camera motion, and HDR 3DGS into a single differentiable framework (Sec. 3.3, Eq. 4–6). This is a genuinely new contribution — prior work either requires multi-exposure sharp images with known exposure times (HDR-NeRF, HDR-GS, HDR-Plenoxels) or handles blur without exposure variation (BAD-Gaussians). The insight that motion blur can serve as an indicator for exposure time is well-motivated and novel.

- **Strong, consistent empirical results.** On synthetic datasets (Table 1), CasualHDR-random (random exposure initialization) achieves 30.25 PSNR on Factory vs. 24.36 for the next best baseline (HDR-Plenoxels) — a ~6 dB margin. On real data (Table 2), it reaches 30.87 PSNR on Toufu-vicon vs. 26.38 for Gaussian-W. These margins hold across NVS, deblurring (Table 3), and pose estimation (Table 4), providing strong evidence that the joint optimization works in practice.

- **Demonstrated downstream applications.** The paper shows that the reconstructed HDR representation supports exposure editing and image deblurring (Figure 3, Table 3), which are practical use cases that go beyond standard NVS evaluation.

- **New benchmark datasets.** The paper generates synthetic Blender data and captures a real-world CasualVideo dataset with ground-truth exposure times and Vicon poses (Sec. 4.1), filling a gap for evaluating HDR reconstruction from casual videos.

- **Clear ablation isolating each module's contribution.** Table 5 on the control knot ratio and the textual description in Sec. 4.6 (quantifying ~24% PSNR improvement from continuous trajectory, ~42% from joint exposure+CRF optimization, ~9% from motion blur modeling) provide useful insight into which components matter most.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Figure 2 shows an "STM" (Spatial-Temporal Module) that is never mentioned in the method text.** The figure caption describes STM as producing virtual sharp images, but Section 3.3 describes this process as straightforward rendering from 3DGS at virtual camera poses (Eq. 5) without naming any separate module. While the pipeline *is* specified in the text, the discrepancy between the figure label and the text is confusing. Readers may wonder if a learned module (STM) exists and is omitted from the description. Align the figure with the text or remove the STM label.

- **Ablation table (Table 6) formatting obscures per-configuration interpretation.** The parsed table shows identical checkmarks across all rows (a parser artifact), and while the accompanying text provides the key quantitative findings (~24%, ~42%, ~9% improvements), the table itself does not clearly label which row corresponds to which configuration variant. This makes it unnecessarily hard to verify the individual contributions from the table alone. Clear row labels (e.g., "gsplat", "BAD-Gaussians", "Ours w/o CRF", "Ours full") should be added.

- **Exposure time optimization lacks direct validation.** The paper claims that Δt can be initialized randomly and converge to correct values via joint optimization, but no direct evidence is provided: no plots of estimated vs. ground truth exposure times, no discussion of identifiability (exposure time, CRF, and scene irradiance have inherent scale ambiguities), and no failure cases. The ablation comparison (CasualHDR-random ≈ CasualHDR-gt in Tables 1–4) suggests the optimization works but does not confirm that the estimated exposure times themselves are meaningful. A convergence analysis would strengthen this claim.

- **CRF MLP architecture details are omitted.** The paper states "we adopt separate MLP for each channel" (Sec. 3.3) for tone mapping but gives no information about the number of layers, hidden dimensions, activation functions, or input/output ranges. Similarly, exposure time Δt is treated as an optimizable parameter initialized randomly, but no mechanism for enforcing positivity (e.g., exp/softplus parameterization) is mentioned. These details are needed for reproducibility.

- **Baseline comparison framing could be more precise.** The paper compares against methods designed for different input settings (multi-exposure sharp LDR for HDR-NeRF/HDR-Plenoxels, blur-only for BAD-Gaussians, appearance variation for Gaussian-W) and reports "state-of-the-art performance across all datasets." Since no existing method targets the *combined* setting (auto-exposure video with blur), the comparison is inherently a demonstration that existing methods fail on this new task. The paper should be more explicit upfront that the task setting itself is new, rather than framing the large numerical margins solely as "outperforming" prior work.

### Trivial

- **The constant-velocity assumption during exposure (Sec. 3.3)** could be clarified: the paper states the camera moves with constant velocity during exposure (used for uniform discretization of the blur integral), but the SE(3) B-spline globally can represent non-constant velocity. A sentence noting that the constant-velocity assumption applies only within each exposure interval (for discretization) would improve clarity.

- **The choice λ_exp = 0.25 is not ablated or justified.** While this is a reasonable default, a brief ablation or reference justifying this value would strengthen the paper.

- **Pose initialization for baselines is not fully specified.** The paper states that HLoc/DPV-SLAM are used for initializing the proposed method's poses, but does not explicitly state whether baselines received the same pose initialization. If baselines received worse initial poses (e.g., from COLMAP), this could confound the comparison.

## Nice-to-Haves
- Include a plot or table showing estimated vs. ground truth exposure times for synthetic and real scenes, with discussion of when the estimation succeeds/fails.
- Add a short summary of ScanNet results to the main paper (currently in supplementary).
- Note whether the ATE differences in Table 4 are statistically significant given the overlapping standard deviations.
- Discuss potential domain gap from synthetic data: the synthetic data uses the same tone-mapping function as HDR-NeRF, which may favor the proposed method.

## Removed Points
These points are flagged to be removed; treat them with caution:

- Harsh critic's point #1 calling the STM issue a "structural" and "serious gap" that "undermines reproducibility" — the pipeline IS described in Section 3.3 (Eq. 4–6: render sharp HDR → average → CRF). The STM is a figure label for a process that is textually specified. The harsh critic overstates the severity. Demoted from "Critical/Fatal" to Minor.
- Harsh critic's point #2 calling the ablation "nearly useless" and "uninterpretable" — the text around the table (Sec. 4.6) clearly explains the findings with percentages (24%, 42%, 9% improvements). The table formatting is suboptimal but the results are interpretable. Demoted from "Critical" to Minor.
- Strength Finder's generic strength about "addressing an important problem" — too generic to retain.
- Strength Finder's claim about "introducing a publicly useful benchmark dataset" — partially kept as a genuine strength but trimmed.
- References to missing appendix content — parser strips appendices from all papers.
- Formatting nitpicks and typos — parser artifacts, not author errors.

## Novel Insights

The reviews surface an interesting observation not fully developed in the paper: the harsh critic correctly notes that the paper's key insight — motion blur as an indicator of exposure time — creates automatic coupling between the trajectory optimization and the radiometric calibration. This is potentially the most novel aspect of the work, but the paper does not explore its implications: for example, what happens when scenes have very little texture (motion blur is hard to estimate) or when exposure times are extremely short (negligible blur)? The ablation suggests the exposure optimization contributes ~42% PSNR improvement, but the mechanism by which the geometry and exposure constraints interact to resolve the inherent scale ambiguity between scene radiance, exposure time, and CRF remains undertheorized.

## Suggestions

1. **Align Figure 2 with the text.** Either remove the "STM" label or explain in Section 3.3 that this refers to the process of rendering sharp HDR images from 3DGS at N virtual camera poses (Eq. 5).
2. **Add exposure time validation.** Show a plot of estimated vs. ground truth Δt for synthetic scenes and discuss cases where the estimation succeeds/fails.
3. **Specify CRF architecture.** Provide MLP depth, width, activations, and the parameterization used to keep Δt positive.
4. **Reformat ablation table (Table 6)** with explicit row labels (e.g., "gsplat", "BAD-Gaussians", "Ours w/o CRF", "Ours w/o Conti. Traj.", "Full Ours") so each configuration is self-explanatory.
5. **Temper the superiority narrative.** Add a sentence in the introduction/experiments stating that this is a new task setting and existing methods are not designed for it, rather than implying they are simply inferior on a shared task.

## Score and Decision

**Calibration anchors:**

| Paper (Path) | Avg Human Score | Round | Comparison |
|---|---|---|---|
| VideoDiT (lvgsPjRtLM) | 2.50 | R1 bracketing | Unrelated topic (video generation); much weaker |
| Real-time CV on low-end boards (w73feIekdO) | 3.25 | R1 bracketing | Unrelated topic; much weaker |
| DepthSplat (IcPkW3QNW2) | 5.00 | R1 middle, R2 | Similar subfield (3DGS); less original contribution, withdrawn |
| Graph-Guided Scene Recon (56vHbnk35S) | 6.00 | R2 narrowing | Similar domain (3DGS scene reconstruction); comparable quality, accepted poster |
| SHARE (EAT5Jpa4ws) | 5.50 | R2 narrowing | Related (pose-free 3DGS); slightly lower |
| 3D Vision-Language GS (SSE9myD9SG) | 6.40 | R2 narrowing | Different subfield (semantic 3DGS); comparable novelty level, accepted poster |
| NVS-Solver (zDJf7fvdid) | 6.00 | R2 narrowing | Unrelated technique (diffusion); comparable rigor, accepted poster |
| Reflective Gaussian (xPxHQHDH2u) | 6.50 | R1 middle | Related (3DGS extension); similar contribution level, accepted poster |
| Lightweight Pred. 3DGS (PbheqxnO1e) | 7.00 | R1 middle | Different contribution (compression); stronger practical impact |
| LVSM (QQBPWtvtcn) | 7.67 | R1 upper | Major impact paper; stronger than this work |

**Round-1 bracket:** 5.0–7.0 (clearly above weak paper band, clearly below top-impact band).

**Round-2 narrowing:** Compared to the 6.0–6.5 anchors (Graph-Guided Scene Recon, NVS-Solver, 3D Vision-Language GS, Ref-Gaussian), this paper has comparable originality and stronger quantitative results, but also a few more presentation/reproducibility gaps. It is clearly stronger than DepthSplat (5.0) and SHARE (5.5). I place it at **6.0** — a solid paper with genuine contribution and convincing results, but whose completeness is held back by the STM figure-text inconsistency, missing CRF details, and lack of exposure time validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>