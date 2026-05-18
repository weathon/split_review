## Summary

CasualHDR proposes a unified 3DGS-based framework for reconstructing HDR scenes from casually captured videos with auto-exposure, unknown exposure times, and motion blur. The method jointly optimizes a continuous SE(3) B-spline camera trajectory, per-frame exposure times, an implicit CRF, and an HDR 3D Gaussian scene representation within a differentiable physical imaging model. The paper also contributes a synthetic dataset (Blender) and a real-world dataset (CasualVideo) for evaluation.

## Strengths

- **A unified differentiable imaging model that jointly optimizes exposure time, CRF, continuous camera trajectory, and the HDR 3DGS scene.** This is the paper's core technical contribution. Rather than requiring known exposure times (as in HDR-NeRF) or treating blur and exposure as separate problems, the model couples them in a single optimization. The ablation (Table 6) shows that jointly optimizing exposure time + CRF yields a 42% PSNR improvement over the unprepared baseline, and the continuous trajectory module provides 24% improvement.

- **Simultaneous handling of motion blur and exposure variation in a single framework.** Prior methods address either blur (BAD-Gaussians, BAD-NeRF) or HDR (HDR-NeRF, HDR-GS), but not both with unknown exposure times. The paper's physical image formation model (Eq. 4–6) integrates both phenomena through the exposure time parameter that couples blur magnitude and brightness, which is a genuinely new capability.

- **Continuous SE(3) B-spline trajectory spanning the entire video, enabling cross-frame motion constraints.** Unlike prior multi-view deblurring methods (BAD-NeRF, BAD-Gaussians) that estimate short per-frame splines, CasualHDR uses a cumulative B-spline over the full video. The paper explains that this leverages temporal continuity and cross-frame constraints, which is methodologically sound and produces better pose estimates (Table 4).

- **Introduction of a new benchmark dataset with simultaneous blur and exposure variation.** The paper provides both a synthetic Blender dataset (with ground-truth exposure times and poses) and a real-world CasualVideo dataset (with Vicon ground truth for two sequences). This fills a gap — existing HDRI datasets use fixed-viewpoint multi-exposure captures — and provides a testbed that the community can use.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparisons are tested in a setting they were not designed for, which overstates the claimed "state-of-the-art" performance.** HDR-NeRF requires multi-exposure *static* images with known exposure times; HDR-Plenoxels and Gaussian-W do not handle blur; BAD-Gaussians assumes consistent exposure. The paper tests these methods on its own challenging data (unknown exposure, auto-exposure, motion blur) where they cannot function as intended. Reporting their failure is informative, but the paper frames this as "outperforming existing reconstruction methods" (contribution 3, Tables 1–2) rather than as demonstrating capability in a new setting where no prior work applies. A fairer evaluation would: (a) adapt baselines where possible (e.g., providing estimated exposure times to HDR-NeRF or selecting exposure-consistent subsets), and (b) test on standard HDR benchmarks (e.g., HDR-NeRF's dataset) to show the method does not sacrifice quality in simpler settings. Without this, the headline quantitative results do not fully support the "SOTA" claim.

2. **The ablation study (Table 6) does not isolate the contribution of the continuous trajectory from other components.** The baseline in Table 6 is vanilla 3DGS with none of the proposed modules. Adding the continuous trajectory to this unprepared baseline yields a 24% PSNR gain — a number the paper presents as evidence for the spline's importance. However, this gain may largely reflect compensating for the lack of exposure handling and deblurring in the baseline. A proper ablation would hold the other modules fixed (deblur + exposure opt + CRF) and compare per-frame pose optimization (as in BAD-Gaussians) against the continuous B-spline. Without this control, the paper cannot claim that the spline representation *per se* is the decisive factor.

3. **No comparison against the most closely related concurrent work ($I^2$-SLAM) is provided.** The paper acknowledges $I^2$-SLAM (Bae et al., 2024) as a concurrent work that also handles exposure inconsistencies and blur, but does not compare because it is not open-source. While this is understandable, it means there is no direct competitor validated in the exact same setting. The evaluation therefore relies entirely on comparisons to methods designed for different input assumptions.

### Minor

1. **The discretization in Eq. (5) assumes constant velocity and uniform sub-exposure durations during each frame's exposure interval.** This is a common assumption in deblurring literature, but casual hand-held videos can contain non-constant motion (e.g., quick pans, camera shake). The paper provides no analysis of how performance degrades under non-uniform motion or how sensitive the method is to the number of virtual sub-frames (N=10 was fixed across all experiments).

2. **Exposure time is "assigned a random value" initially, but the paper does not analyze convergence sensitivity.** The loss landscape with respect to exposure time Δt is highly non-convex (it affects both brightness scale and blur kernel width). No experiment reports convergence behavior, sensitivity to initialization, or accuracy of the estimated exposure times against ground truth (available on synthetic and RealSense sequences). Showing that Δt converges to reasonable values would directly support the paper's claim that "camera motion blur can serve as an indicator of the exposure time."

3. **The pose estimation comparison (Table 4) conflates different task scope.** The paper compares ATE against HLoc and DPV-SLAM (pure pose estimators) and BAD-Gaussians (joint reconstruction). CasualHDR optimizes poses within a full scene reconstruction framework with a continuous trajectory prior — this is a substantially different optimization landscape. While the comparison is not invalid, the paper over-interprets the result as demonstrating pose estimation "robustness" when the advantage may partly stem from the richer objective (render-consistency + smoothness prior) not available to pure pose estimators.

4. **The deblurring module's contribution appears modest.** In Table 6, adding deblurring yields only a ~9% PSNR improvement (approximately 1.14 dB), suggesting that exposure handling already accounts for most of the improvement on this data. The paper should discuss why deblurring is still presented as a major component when the gain is comparatively small.

### Trivial
- Table 5 varies the ratio of knots to images but reports only rendering quality, not pose accuracy (ATE). The spline's ability to model the underlying trajectory is directly relevant to pose quality, which the paper evaluates elsewhere.

## Nice-to-Haves
- Reporting estimated vs. ground-truth exposure times (available on synthetic and RealSense-Vicon data) to validate the key claim that exposure time can be recovered from blur and brightness.
- Show learned CRF curves compared against ground truth for synthetic scenes.
- Test on fully hand-held smartphone video (without gimbal stabilization) to demonstrate robustness to more challenging camera shake.
- Test the method on standard HDR datasets (e.g., HDR-NeRF's multi-exposure static captures) to show generality and that the method does not regress on simpler settings.

## Removed Points
- **"Main quantitative results are unverifiable (placeholder tables)"** — Parser artifact; tables exist in the original submission. Removed per formatting-artifact rule.
- **"No comparison against $I^2$-SLAM is a fatal flaw"** — The paper acknowledges $I^2$-SLAM is concurrent and not open-source. Not a flaw. But the absence of any direct competitor is a notable gap, moved to Major.
- **"Camera motion blur as indicator of exposure time is asserted without evidence"** — This is a well-established physical fact (longer exposure → more blur), used as motivation, not an evidence claim.
- **"MCMC sampling is non-standard"** — The paper uses an existing framework (gsplat with MCMC). Not a contribution claim that needs ablating.
- **"Dependency on pose initializer is a confound"** — The paper explains the choice (HLoc vs. DPV-SLAM) and it is standard practice to use initial poses from SfM/SLAM.
- **"Figures lack zoomed-in crops"** — Minor presentation nitpick; not a substantive weakness.
- **"$I^2$-SLAM not compared because not open-source"** — Not a weakness of the paper. Retained as note in Major because it means no direct competitor exists in the evaluation.

## Novel Insights
The key insight in the reviews that goes beyond the paper's own framing is that the paper's evaluation strategy (testing baselines in a setting they were not designed for) creates a tension: it simultaneously demonstrates a genuinely new capability (HDR reconstruction from casual video) while making it difficult to quantify *how well* the method actually works relative to what was previously possible. The paper would benefit from disentangling the claim into two parts: (1) "we are the first to handle this harder setting" (a contribution claim the evidence supports) and (2) "in controlled comparisons on standard benchmarks, our method is competitive" (which requires additional experiments). The current framing mixes these two claims, making the paper stronger in scope than in evidence.

## Suggestions
1. Add an ablation holding deblur + exposure opt + CRF fixed, comparing per-frame pose optimization vs. continuous B-spline, to isolate the spline's contribution.
2. Report estimated exposure time accuracy (vs. ground truth) on synthetic and RealSense sequences to validate the key claim that Δt is recoverable.
3. Test on a standard HDR benchmark (e.g., HDR-NeRF's dataset) to show the method generalizes to simpler settings.
4. Reframe the baseline comparisons as demonstrating a new capability rather than "outperforming" methods designed for different inputs. For baselines that partially apply (e.g., BAD-Gaussians), consider controlled subset experiments.
5. Analyze sensitivity to the constant-velocity assumption and the number of virtual sub-frames N.

## Score and Decision

**Calibration Anchors (from retrieval):**

| Anchor Path | Avg Score | How it compares |
|---|---|---|
| MoDGS (2prShxdLkX) | 6.75 (Accept) | Similar "casually captured" video setting; MoDGS has more rigorous controlled experiments and clearer isolation of contributions. This paper is weaker in evaluation rigor. |
| LVSM (QQBPWtvtcn) | 7.67 (Accept) | Much stronger paper across all dimensions: originality, thoroughness, and experimental validation. |
| HQGS (25Zlvl7JxW) | 6.50 (Accept) | Both handle degradation; HQGS has cleaner ablation studies. This paper tackles a more ambitious problem but with weaker evidence. |
| Video Deblurring (8DW3aSOnou) | 4.75 (Reject) | Marginal-innovation paper. This paper has stronger contributions (new problem framing, unified framework) but similar evaluation gaps. |
| Learn Dynamic 3DGS (xy9yv5siYQ) | 5.25 (Reject) | Similar "casual video" topic, rejected for limited novelty and evaluation gaps. This paper has better novelty but similar evaluation weaknesses. |
| Camera Pose Est. (lgf2LW7fOJ) | 4.50 (Reject) | Lower quality overall. |
| MOTIONFLOW (OBTmkKBmQW) | 4.00 (Reject) | Lower quality overall. |
| HIWE (NLRo4qhg6t) | 3.00 (Reject) | Much weaker. |
| Continuously Vol. Rendering (mYo9r0CwUf) | 2.33 (Reject) | Much weaker. |

The paper's core contribution — a unified framework for HDR 3D reconstruction from casual auto-exposure video — is genuinely novel and practically motivated. However, the experimental evaluation does not convincingly validate the headline claims. The baseline comparisons lack controlled adaptation, the ablation does not isolate the continuous trajectory contribution, and key analyses (exposure time convergence, non-constant motion sensitivity) are missing. Relative to the calibration anchors, the paper sits between the weaker accepted papers (~6.5) and the rejected papers (~4.75–5.25).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>