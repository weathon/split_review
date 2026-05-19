## Summary
The paper proposes CasualHDR, a unified 3DGS-based framework for reconstructing HDR 3D scenes from casually captured videos that exhibit auto-exposure, unknown exposure times, and motion blur. The key innovation is a differentiable physical imaging model that jointly optimizes a continuous SE(3) B-spline camera trajectory, per-frame exposure times, a per-channel CRF (MLP), and the HDR 3D Gaussian scene representation. Experiments on synthetic Blender data and a newly captured real-world dataset (CasualVideo) show substantial improvements over prior HDR-NeRF, HDR-Plenoxels, Gaussian-W, and BAD-Gaussians baselines across NVS, deblurring, and pose estimation metrics.

## Strengths
- **Unified joint optimization of all variables in a single differentiable model.** The paper formulates a physical imaging model (Eq. 4–6) that couples exposure time, CRF, continuous SE(3) trajectory, and HDR 3DGS representation into one end-to-end optimizable pipeline. This is a clear departure from prior HDR-3D methods that assume known exposure times and static cameras, and the ablation (Table 6) quantifies each component's contribution: continuous trajectory (+24% PSNR), joint exposure+CRF optimization (+42%), and blur modeling (+9%).

- **Strong empirical results on a challenging new problem setting.** On real-world casually captured videos where baselines fail (HDR-NeRF fails entirely on all real scenes), CasualHDR achieves substantially higher PSNR/SSIM/LPIPS even with randomly initialized exposure times (Table 2). The ATE results (Table 4) on Vicon-ground-truth sequences show dramatic pose estimation improvements (5.1 cm vs. 32.7 cm for HLoc, 63.6 cm for DPV-SLAM, 11.0 cm for BAD-Gaussians), providing converging evidence that the joint optimization handles brightness variation and blur that break feature-based and SLAM methods.

- **Controlled ablation study validates each design choice.** Table 6 systematically ablates the continuous trajectory, exposure time optimization, CRF, and blur model components, demonstrating that all contribute meaningfully. Table 5 ablates the control-knot ratio for spline initialization. This gives the reader a clear picture of what each part of the model buys.

- **Release of a dedicated dataset (CasualVideo) for this task.** Section 4.1 describes both synthetic (Blender, 4 scenes) and real (RealSense + Smartphone, including Vicon ground truth) datasets, providing a resource for future work on this challenging problem.

## Weaknesses
### Fatal
None.

### Major

- **Optimized exposure times are never validated against ground truth.** The paper claims that "exposure time will be gradually optimized to the actual value" (line 111) and prominently states that ground-truth exposure times were recorded from camera hardware (line 145: "developed scripts to extract measured exposure times from the hardware as ground truth labels"). Yet no comparison between optimized and ground-truth exposure times is presented anywhere in the paper. This is a central claim of the method — that exposure-dependent motion blur and brightness jointly constrain the optimization to recover correct physical parameters — and it goes directly unvalidated. Without this check, one cannot distinguish between genuine physical parameter recovery and mere brightness compensation via the CRF while exposure time drifts arbitrarily. While the strong NVS and ATE results provide indirect evidence, a direct validation is straightforward (the data exists) and its absence is a significant evidential gap.

- **Real-world NVS evaluation protocol is underspecified.** The paper states: "Due to the fact that most images in real-world datasets are blurry, we select 5 to 10 sharp images for each sequence to evaluate metric" (line 168). It does not clarify whether these sharp frames were held out from training or were also used during training (for blur modeling). If they are training frames, the reported numbers measure reconstruction/deblurring quality on seen views, not novel view synthesis. If they are genuinely held out, the paper should state this explicitly and describe how the train/test split was constructed from the video sequence (e.g., temporal skipping). The ambiguity undermines the NVS claims on real data.

- **No variance reporting across multiple runs.** All quantitative results (Tables 1–4, 6) are reported as single numbers with no error bars. 3DGS-based methods have known variance from random initialization, adaptive density control, and stochastic optimization. While the reported PSNR gaps are very large (e.g., ~6 dB on Factory) and likely significant, the absence of any statistical characterization makes it impossible to assess whether smaller improvements would be reliable. This is a standard expectation for rigorous experimental evaluation.

### Minor

- **N=10 virtual poses is fixed without ablation.** The number of virtual latent sharp images used to approximate the blur integral (Eq. 5) is set to 10 with no sensitivity analysis showing that this is sufficient and how performance varies with N.

- **No sensitivity analysis on the exposure-normalized loss weight.** The hyperparameter λ_exp=0.25 is fixed in all experiments with no ablation showing sensitivity to this choice.

- **Limited limitations/failure cases discussion.** The paper does not discuss scenarios where the method might fail (e.g., very fast camera motion violating the constant-velocity assumption, scenes heavily saturated in most frames, rolling shutter effects). A limitations paragraph would improve credibility.

- **Missing learning rates for non-Gaussian components.** The paper states the learning rate for Gaussian primitives is consistent with gsplat but does not specify learning rates for the spline control knots, CRF MLPs, and per-frame exposure time parameters, which is helpful for reproducibility.

### Trivial
None.

## Suggestions
- **Validate exposure time recovery.** For the RealSense and Smartphone sequences where ground-truth exposure times were recorded (line 145), report a comparison (e.g., mean absolute error or correlation) between the optimized and ground-truth values. This directly confirms the paper's core claim.
- **Clarify the real-world evaluation protocol.** State explicitly whether the 5–10 sharp images selected per sequence were excluded from training. If they were, describe the hold-out procedure (e.g., temporal skipping). If not, reframe the evaluation as reconstruction/deblurring quality rather than NVS, or redo the evaluation with genuinely held-out views.
- **Add error bars.** Run the method and at least the top-2 baselines with 3 different random seeds and report mean ± std for all metrics. This is the minimum standard for claiming improvements over stochastic methods.
- **Include an ablation on N (virtual poses).** Vary N (e.g., 1, 5, 10, 20) to demonstrate that the chosen value is sufficient and not a performance bottleneck.

## Score and Decision

The paper presents a well-motivated, elegantly unified framework addressing a practically important and previously under-explored problem. The core methodology is sound and the ablations convincingly attribute performance to each design component. The weaknesses are evidential rather than methodological — they require additional experiments and clearer documentation, not a redesign of the approach. With the suggested validations (especially exposure time recovery and protocol clarification), the paper would be a strong contribution worthy of acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
