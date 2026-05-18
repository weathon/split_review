Now I have thoroughly verified the paper content against all reviewer claims. Let me compose the final consolidated review.

## Summary

CasualHDR proposes a unified differentiable physical imaging model that jointly optimizes exposure time, camera response function (CRF), a continuous-time SE(3) camera trajectory via cumulative B-splines, and a 3DGS-based HDR scene representation. The target application is recovering HDR 3D scenes from casually captured auto-exposure videos that simultaneously exhibit motion blur and brightness variation — a practical scenario where existing methods (which assume known exposure times, sharp images, or static cameras during exposure) fail. The paper demonstrates the method on synthetic Blender data and real-world handheld sequences, reporting improvements over HDR-NeRF, HDR-Plenoxels, Gaussian-W, BAD-Gaussians, and vanilla 3DGS.

## Strengths

1. **Novel unified formulation tackling a genuine practical gap**: The joint optimization of exposure time, CRF, continuous-time camera trajectory, and HDR 3DGS scene in a single differentiable model is a meaningful integration. The key insight — that motion blur and brightness are both tied to exposure time, so one can constrain the other — is well-motivated and leads to a method that does not require known exposure times or static multi-exposure captures. (Abstract, Section 3.3, Eq. 4–6)

2. **Strong quantitative results on challenging data**: CasualHDR consistently outperforms all baselines across synthetic and real datasets in novel-view synthesis (Tables 1–2), image deblurring (Table 3), and pose estimation (Table 4). Notably, even with randomly initialized exposure times (CasualHDR-random), the method exceeds prior work, and HDR-NeRF fails entirely on real data — demonstrating that existing approaches simply are not designed for this regime.

3. **Continuous SE(3) B-spline over the full video**: Unlike prior multi-view deblurring works that estimate separate short splines per frame, this paper uses a single cumulative B-spline spanning the entire video. This enforces cross-frame motion constraints and yields smooth, physically plausible trajectories. Ablation results confirm this contributes ~24% PSNR improvement. (Section 3.2, Table 6)

4. **Practical applications demonstrated**: After training, the model supports novel-view synthesis, deblurring of input frames, and HDR editing (adjusting exposure time to control brightness), illustrating the flexibility of the recovered representation. (Abstract, Figure 3)

5. **Dataset contribution**: The paper creates and describes both synthetic Blender data with controlled motion blur/exposure variation and a real-world CasualVideo dataset with Vicon ground truth, providing a standardized testbed for this challenging setting. (Section 4.1)

## Weaknesses

### Fatal
None.

### Major

1. **Ablation study uses cumulative additions, not independent isolation**: The ablation in Table 6 adds components sequentially (+Deblur, +ContiTraj, +ExpOpt+CRF). This means the 42% improvement attributed to "Exp. Opt. + CRF" is a cumulative gain on top of all previously added components, not an isolated measurement of either exposure optimization or CRF individually. The paper also reports only relative PSNR improvements rather than absolute values, making it impossible to assess saturation or compare against other methods' absolute numbers. An ablation that independently removes single components (e.g., w/o CRF but with exposure opt) would be more informative. (Section 4.6, Table 6)

2. **Exposure time parameterization is underspecified**: The paper states Δt is initialized "randomly" and optimized, but provides no detail on the parameterization needed to enforce positivity (e.g., log-space, softplus, or clamped values). Since exposure time directly scales both integrated irradiance and the number of virtual cameras, an unconstrained parameter could produce degenerate solutions (near-zero exposure minimized blur, compensated by extreme CRF scaling). This gap affects both reproducibility and the reader's ability to assess optimization soundness. (Section 3.3)

### Minor

3. **CRF MLP architecture not specified**: The paper uses "separate MLP for each channel" for tone mapping but gives no details on depth, width, activation functions, input representation, or how the output is constrained to a valid range. While architectural specifics are commonly deferred to supplementary material, the current paper does not provide them. (Section 3.3, line 111)

4. **Baseline comparison fairness is uneven**: The paper uses HLoc/DPV-SLAM for its own pose initialization but does not state what initialization baselines (3D-GS, BAD-Gaussians) received. If baselines used standard COLMAP while CasualHDR used learning-based SfM more robust to brightness changes, the pose-quality gap inflates the apparent advantage. Additionally, comparing HDR-NeRF (designed for fixed-viewpoint multi-exposure captures with known exposure times) on casual video where those assumptions are violated is an expected failure rather than a demonstration of superiority. The paper should clarify initialization protocol or adapt baselines where possible.

5. **Pose estimation results lack supporting analysis**: The reported ATE values (0.36 cm, 0.42 cm) on handheld Vicon-captured sequences are strikingly small. The paper does not discuss scene scale, Vicon-to-camera coordinate alignment, or whether the ATE is computed over the continuous trajectory at frame timestamps versus discrete Vicon markers. There is no analysis of potential overfitting — the trajectory could adapt to render training views correctly without reflecting true camera motion. (Table 4, Section 4.4)

6. **Selection criteria for test images not stated**: The paper selects 5–10 "sharp" images per real sequence for evaluation but does not specify the selection criteria. If test views are chosen as those least affected by blur or exposure changes, the evaluation could be biased in the method's favor. (Section 4.4)

7. **No ablation on the number of virtual cameras N**: N=10 is set for "balance between performance and efficiency," but no experiment varies N (e.g., 1, 3, 5, 10, 20) to show convergence behavior or quantify the error from the discrete velocity-constant approximation. (Section 4.2, Eq. 5)

8. **MCMC densification choice not discussed**: The implementation uses MCMC-based densification (Kheradmand et al., 2024) rather than the standard 3D-GS adaptive density control. This could significantly affect reconstruction quality under blur and should be ablated or at least discussed. (Section 4.2)

9. **Runtime and memory not reported**: Using 10 virtual camera renders per input image multiplies computational cost compared to standard 3DGS. The paper does not report training time, VRAM usage, or convergence speed relative to baselines.

### Trivial
None.

## Nice-to-Haves

- An analysis showing that randomly initialized exposure times converge to physically plausible values across frames (rather than being absorbed by the CRF or scene representation).
- Testing whether the learned B-spline trajectory generalizes to intermediate timestamps not used in training, to check for overfitting.
- A discussion of failure cases: extreme motion blur poorly approximated by N=10 discrete samples, or scenes with large depth variation violating the constant-velocity assumption.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The datasets are not released (no link provided)"** — Removed per hard rule: questioning release status/availability of paper-cited entities is not permissible.
- **"Ablation studies that rigorously quantify component contributions"** (Strength Finder) — Removed: conflicts with verified weakness that the ablation is cumulative and does not isolate individual components. A strength and verified weakness disagree; the weakness wins.
- **"The related work section is somewhat encyclopedic"** — Removed per soft rule: this is a style judgment, not a substantive weakness. The paper does clearly position itself relative to the most relevant prior work (BAD-NeRF, HDR-Plenoxels, BAD-Gaussians) in Sections 2.2–2.3.
- **"The paper claims a dataset contribution, but the datasets are not released"** — Duplicate of first point; removed.

## Novel Insights

The most interesting observation to emerge from the reviews is that the paper's core strength — coupling motion blur and exposure time in a single constraint — is also the source of its most significant specification gap. The claim that "motion blur can serve as an indicator of exposure time" is evocative, but without showing that the jointly estimated exposure times converge to ground truth values or are at least physically plausible and well-separated from the learned CRF, it remains a plausible intuition rather than a demonstrated fact. The reviews collectively suggest that the method's main innovation is sound but its experimental validation would benefit from sharper isolation (component-level ablations, trajectory generalization checks) rather than broader coverage.

## Suggestions

1. **Restructure the ablation**: Report absolute PSNR/SSIM/LPIPS for at least: (a) standard 3DGS with fixed poses, (b) + continuous trajectory optimization, (c) + deblur model with fixed exposure times, (d) + exposure optimization without CRF, (e) + CRF only, (f) full model. This would isolate individual contributions and reveal whether the 42% gain requires both exposure optimization and CRF together.
2. **Specify the CRF architecture and exposure time parameterization**: Provide MLP depth/width/activations and explain how Δt positivity is enforced (log-space, softplus, or clamping). This is essential for reproducibility.
3. **Clarify baseline initialization**: State explicitly whether baselines received the same pose estimates as CasualHDR (via HLoc/DPV-SLAM) or used a different pipeline (COLMAP).
4. **Add analysis of trajectory estimation**: Compare learned continuous poses to Vicon ground truth at frame timestamps. Show that the trajectory does not overfit training views by evaluating at held-out timestamps.
5. **Document test image selection criteria**: Specify how "sharp" images were identified for evaluation to rule out selection bias.
6. **Report absolute PSNR in ablation and runtime/memory**: These are standard reporting requirements for a systems paper.

## Score and Decision

**Score: 5.5**

This paper addresses a timely and practically important problem with a well-motivated unified formulation. The core idea — jointly optimizing exposure time, CRF, continuous trajectory, and HDR 3DGS — is a genuine contribution that moves beyond existing methods that handle these degradations separately. The experimental results are consistently positive across multiple datasets and tasks.

However, the paper is held back by a set of interconnected rigor issues: the ablation design is cumulative rather than isolating, leaving the individual contribution of each component unclearly quantified; several key implementation details (exposure time parameterization, CRF architecture) are missing, hampering reproducibility; the baseline comparisons could be fairer; and the pose estimation results lack supporting analysis. None of these are fatal — they can be addressed with additional experiments and specification — but in their current form, they prevent a confident accept.

The contribution warrants acceptance conditional on substantial revision. A stronger version of this paper, with the suggested ablations and clarifications, would be a solid accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>