I now have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

## Summary

This paper introduces I2VControl-Camera, a camera control method for image-to-video generation that uses dense 2D point trajectories (derived from the linear term of a Maclaurin expansion of 3D point motion in the camera coordinate system) as the control signal, replacing the sparse extrinsic camera matrices used in prior work (MotionCtrl, CameraCtrl). The paper further introduces an explicit motion-strength parameter \(m_\lambda\) derived from the higher-order (nonlinear) trajectory components, which enables adjustable subject motion dynamics independently of camera motion. A data pipeline using metric depth estimation (UniDepth) and pixel tracking (SpatialTracker) extracts these control signals from raw RGB video, and an adapter architecture injects them into a frozen base model (Magicvideo-V2). Quantitative results on static (RealEstate10K) and dynamic test sets show improved RotErr/TransErr over retrained baselines, and the motion strength parameter is shown to modulate subject motion in a controllable way (MSC ranging from 18.96 at strength 0 to 47.70 at strength 600).

## Strengths

1. **Novel control signal design using dense point trajectories.** The paper replaces the standard camera extrinsic matrix (6-DoF per frame) with a dense 2D point trajectory \(\mathbf{T}_\lambda\) derived from the linear term of a Maclaurin expansion (Eqs. 3–8). This is a principled and well-motivated departure from prior work, and the results support its effectiveness: RotErr 0.53 vs. 1.26 (CameraCtrl) and 2.66 (MotionCtrl) on RealEstate10K (Table 1). The theoretical derivation linking the linear trajectory term to static-world rigid motion is clearly presented.

2. **Explicit, adjustable motion strength control via higher-order trajectories.** The motion strength \(m_\lambda\) (Eq. 9) is derived from the time derivative of the nonlinear residual \(\mathcal{G}(\mathbf{p},\lambda)\) — the component of the trajectory not explained by rigid camera motion. This provides a theoretically grounded mechanism for controlling subject dynamics. The quantitative evidence is convincing: MSC varies monotonically from 18.96 (strength 0) to 47.70 (strength 600) in Table 2, and the qualitative results (Fig. 6) visually confirm the effect.

3. **Fair and controlled comparison with baselines.** The paper retrains both MotionCtrl and CameraCtrl using the same base model (Magicvideo-V2) and the same experimental settings (Section 4.3). This addresses a common confound in prior camera-control evaluations where different base models and training data made comparisons unreliable.

4. **Practical data pipeline.** Section 3.3 describes a complete, automated pipeline (depth estimation + pixel tracking + iterative static/dynamic partitioning in Algorithm 1) that extracts \((\mathbf{T}_\lambda, m_\lambda)\) from raw RGB video without needing ground-truth 3D or camera pose annotations, making the approach scalable to 30K video clips.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation studies — cannot attribute gains to specific components.** The paper compares against MotionCtrl and CameraCtrl (retrained), but never isolates its own design choices. The key question — *which component drives the improvement?* — is unanswered. Specifically: (a) Is the gain from using point trajectories rather than camera matrices, or from the larger/more diverse training set (30K clips vs. RealEstate10K)? (b) Does the motion strength conditioning actually enable adjustable dynamics beyond what a baseline without \(m_\lambda\) would produce? (c) What does the iterative static/dynamic partition contribute versus a simpler threshold? An ablation that keeps training data identical and varies only the control signal (point trajectory vs. extrinsic matrix vs. Plücker embedding) would directly support the paper's central claims. Without it, the contribution is empirically underdetermined. This is the single most impactful weakness.

2. **Motion strength conditioning mechanism is underspecified.** The paper states that "the user can provide a scalar value for the motion strength control" (Section 3.4), and the network receives \(m_\lambda\) as a tensor of shape \((T, 1)\). But the mapping from the user-provided scalar to the per-frame \(m_\lambda\) sequence is never explained. During training, \(m_\lambda\) is computed from data (Eq. 13). During inference, is the user scalar broadcast to all T frames? Is it a multiplier on the data-derived \(m_\lambda\)? Does it replace \(m_\lambda\) entirely? The architecture description (Fig. 4 / Section 3.4) tiles and concatenates \(m_\lambda\) with \(\mathbf{T}_\lambda\), but how the scalar becomes a \((T,1)\) tensor is not stated. This is a reproducibility gap for the paper's second headline contribution.

### Minor

1. **FID reference set is unusual and poorly motivated.** The paper computes FID against "2000 random frames from WebVid" (Section 4.1). WebVid is a large-scale, highly diverse web-scraped dataset; using 2000 frames as the reference distribution is not standard practice for evaluating quality in camera-control generation. It is unclear what this FID measures — a comparison to natural image statistics? The reference distribution should be drawn from the domain of interest (e.g., the test set itself). While relative comparisons across methods are still informative (all use the same reference), the absolute FID values are difficult to interpret.

2. **No uncertainty quantification.** Tables 1 and 2 report only point estimates. No standard deviations, confidence intervals, or information about run-to-run variation is provided. Given that RotErr/TransErr can vary substantially across samples, this makes it impossible to assess whether the reported differences are statistically significant.

3. **Motion Strength Score (MSC) conflates multiple sources of residual motion.** MSC computes optical flow followed by 2D rigid alignment and reports the average \(L_2\) alignment error. This captures not only subject motion but also residual camera motion not removed by rigid alignment, non-rigid scene motion (water, foliage, cloth), and flow estimation errors. While MSC is a reasonable proxy and the trends in Table 2 are consistent, the paper should acknowledge these confounds.

4. **Training data description is sparse.** The 30K video clips are described only as "containing not only camera movements but also natural motion" (Section 4.1). No details about curation, resolution diversity, scene diversity, or how camera/subject motion are balanced are provided. This limits reproducibility.

### Trivial

1. **Vague architecture description.** The adapter uses "several convolutional layers" (Section 3.4) — specifying the exact number, kernel sizes, and channel dimensions would be helpful.

2. **No discussion of data-pipeline failure modes.** The pipeline relies on UniDepth (metric depth) and SpatialTracker (pixel tracking), both of which have known failure cases (e.g., reflective surfaces, thin structures, occlusion). A brief discussion of when the pipeline might break would strengthen the paper.

## Nice-to-Haves

- Adding confidence intervals or error bars to Tables 1 and 2.
- A limitations section that acknowledges the reliance on depth/tracking quality, the approximate nature of the static/dynamic partition, and the global (non-spatially-varying) nature of the motion strength scalar.
- Brief discussion or comparison with training-free approaches (Camtrol) and epipolar-constraint approaches (CamCo), even if limited in scope.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- *Harsh critic: "RotErr/TransErr estimation may be inaccurate on dynamic scenes, penalizing methods with more subject motion."* — This is speculative; the paper does not describe the pose estimation pipeline for generated videos, so the claim cannot be verified from the paper as written. Non-speculative versions of this concern (e.g., the need to describe how metrics are computed) are covered in weakness M3.
- *Harsh critic: "The higher-order term \(\mathcal{G}\) conflates scene dynamics and non-rigid camera motion (e.g., suspensions)."* — The paper acknowledges this implicitly in the data pipeline (the static/dynamic partition is data-driven). The expansion is presented as a first-order model, not a claim of perfect separation.
- *Harsh critic: "No analysis of convergence or sensitivity of Algorithm 1 parameters \(\epsilon, \alpha, N_{\text{max}}\)."* — This is a reasonable concern but minor; the algorithm is a straightforward iterative fitting procedure and these are typical implementation parameters.
- *Strength Finder: Generic/superlative strengths about "broad potential applications," "important problem," etc.* — These are not specific to the paper.
- *Harsh critic: "The paper does not compare to Camtrol or CamCo."* — Per filtering rules, missing related work citations are not included because the reviewer cannot verify their existence or relevance from external knowledge.
- *Harsh critic: "No limitations section."* — Per filtering rules, this is a format preference, not a substantive weakness. The conclusion does discuss future directions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add ablation studies (most critical).** Train variants of the method that differ only in the control signal type (point trajectory vs. extrinsic matrix vs. Plücker embedding) while holding the training data, base model, and adapter architecture fixed. Also compare a version with and without motion strength conditioning to isolate its effect. Two additional rows in each of Tables 1 and 2 would substantially strengthen the paper.

2. **Clarify the motion strength conditioning mechanism.** Add a short paragraph or explicit equation showing how the user-provided scalar becomes the \((T,1)\) tensor \(m_\lambda\) that enters the network.

3. **Justify or improve the FID reference.** Either use a more standard reference distribution (e.g., the test set's real frames) or explain the rationale for using 2000 WebVid frames and discuss the metric's limitations.

4. **Report confidence intervals** or standard deviations for the main metrics, even if from a small number of seeds.

## Score and Decision

**Calibration report:**

**Round 1 — Bracketing:** Three queries for "camera control video generation diffusion model" in bands (-∞, 3.5), (3.5, 7.5), (7.5, ∞). Low-band anchors (scores 1.5–3.25) are clearly weaker papers. Middle-band anchors include several relevant camera-control papers. High-band anchors (scores 7.6–8.5) are oral/spotlight papers on different diffusion topics — not comparable to this camera-control paper.

**Round 1 bracket:** [4.0, 6.5]

**Round 2 — Narrowing:** Queried inside (4.5, 6.5) and (5.0, 7.5) for trajectory control and adapter-based camera control papers. Anchors used for comparison:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CamTrol (KI1zldOFz9) — Training-free Camera Control | 5.80 | 1, 2 | Accepted (Poster). Training-free approach with similar ablation/metric weaknesses. I2VControl-Camera has stronger methodological novelty (point trajectory, motion strength) but CamTrol's training-free nature is a different selling point. Comparable quality of evidence. |
| Boosting Camera Motion Control (rDRCIvTppL) | 5.50 | 1, 2 | Rejected. Mostly analytical contribution with limited novelty. I2VControl-Camera has more novel technical content. |
| FreeTraj (CU7QfWJ6nC) — Tuning-Free Trajectory Control | 5.50 | 2 | Rejected. Criticized for limited technical contribution ("intuitive engineering work"). I2VControl-Camera has stronger theoretical grounding and more novel contributions. |

**Final score determination:** The paper sits between the 5.50 rejected anchors (FreeTraj, Boosting Camera Motion Control) and the 5.80 accepted anchor (CamTrol). Compared to the 5.50 anchors, I2VControl-Camera has stronger theoretical motivation and more novel technical contributions. Compared to CamTrol (5.80), it has comparable weaknesses (missing ablations, metric concerns) but makes a less universally applicable claim (requires training). The missing ablations are a significant issue that prevents clear attribution of gains. Given these trade-offs, the paper is closest to FreeTraj/Boosting Camera Motion Control in overall assessment score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>