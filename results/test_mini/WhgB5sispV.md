Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper proposes representing dynamic scenes with full 4D Gaussians that treat space and time as a unified 4D volume. The key technical innovations are: (1) parameterizing each Gaussian's covariance via a full 4D rotation (using two quaternions), which enables joint spatiotemporal modeling rather than treating space and time independently, and (2) 4D Spherindrical Harmonics (4DSH) for time-evolved view-dependent appearance. The method is trained end-to-end on entire videos without frame-by-frame optimization and achieves real-time rendering (145+ FPS on Plenoptic Video).

## Strengths

- **Conceptually clean and well-motivated representation.** Treating space and time symmetrically via a full 4D Gaussian with 4D rotation (two quaternions, Eqs. 153-177) is mathematically elegant. The derivation of the conditional 3D Gaussian from the 4D Gaussian (Eqs. 183-185) and the rendering equation (Eq. 4) are sound. The ablation against the "No-4DRot" baseline (space-time independence) confirms that the full 4D rotation is empirically beneficial.

- **4D Spherindrical Harmonics are a natural extension of SH to dynamic scenes.** The combination of spherical harmonics (for view dependence) with Fourier series (for time evolution) in Eq. 204 forms an orthonormal basis that is interpretable and ablated cleanly — removing 4DSH degrades PSNR, validating its concrete contribution.

- **Real-time rendering with strong visual quality.** On the Plenoptic Video dataset, the method achieves the highest metrics among the methods included in the comparison (PSNR 30.78, SSIM 0.975, LPIPS 0.067) while rendering at 145+ FPS — an order-of-magnitude speed advantage over prior MLP/grid-based approaches, most of which require seconds per frame.

- **End-to-end training on entire videos.** Unlike frame-by-frame or multi-stage optimization used by some dynamic Gaussian methods, the pipeline trains on whole videos in a single stage (Section 3.3), with temporal batch sampling to mitigate flicker.

- **Emergent optical flow without motion supervision.** The conditional mean of the 4D Gaussian naturally yields scene flow (Figure 4), demonstrating that the representation captures coarse dynamics purely from photometric loss.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against the most relevant dynamic Gaussian baselines.** The paper claims state-of-the-art performance yet compares only against non-Gaussian methods (TiNeuVox, K-Plane, HexPlane, NeRFPlayer, etc.). The following methods that also extend 3DGS to dynamic scenes are cited in the related work but not included in any quantitative experiment: Luiten et al. "Dynamic 3D Gaussians," Yang et al. "Deformable 3DGS," Wu et al. "4D Gaussian Splatting," and Kratimenos et al. "DyMF." These are the paper's closest competitors — they operate on the same datasets (Plenoptic Video, D-NeRF) and share the Gaussian splatting paradigm. Without this comparison, the paper's core claims of superiority are unsubstantiated. The "first ever" claim for real-time high-fidelity dynamic scene synthesis (Conclusion) cannot be evaluated. This is not a minor omission; it requires re-running experiments against these baselines. (Verified: the paper cites all four methods at lines 59-64 but includes none in Tables 1-2.)

- **An unacknowledged and restrictive prior: constant spatial covariance over time.** From the conditional distribution of a 4D Gaussian (Eq. 184): Σ_{xyz|t} = Σ_{1:3,1:3} − Σ_{1:3,4} Σ_{4,4}^{-1} Σ_{4,1:3}. This expression is independent of t. Each Gaussian can only translate with constant velocity (μ_{xyz|t} moves linearly with t, Eq. 183), and its spatial shape/orientation cannot change over time. This is a strong assumption that the paper never discusses. On datasets with non-rigid or articulated motion (e.g., D-NeRF jumping jack, rotating head), this limits expressiveness. The ablation of "No-4DRot" vs. full 4D rotation does not isolate whether the benefit comes from enabling linear translation or from something else. The paper should analyze this limitation and, if possible, show that densification compensates for it (e.g., tracking Gaussian count across scenes with varying motion complexity).

### Minor

- **Lack of quantitative analysis of temporal stability.** The paper acknowledges "temporal flickering and jitter" in challenging scenes and describes a "straightforward batch sampling in time" solution (lines 215-216), but provides no ablation or metric (e.g., warp-based temporal consistency, per-frame PSNR variance) demonstrating its effectiveness. The reader cannot assess whether the reported results are representative or cherry-picked.

- **The ablation isolates only the presence/absence of components, not why they help.** The "No-4DRot" baseline (block-diagonal covariance) is compared against the full model, but there is no finer-grained ablation (e.g., allowing 4D rotation only in spatial dimensions vs. full 4D, or allowing only translational coupling without rotational coupling). Similarly, the densification-in-time ablation (last two rows of the ablation table) could be better isolated from spatial densification.

### Trivial

- None (the paper is generally well-written and the parser artifacts are not author errors).

## Nice-to-Haves

- A direct numerical characterization of the expressivity of the 4D Gaussian: what types of motion (e.g., non-linear trajectories, non-rigid deformation) require more Gaussians to approximate, and at what cost?
- Including temporal consistency metrics (e.g., inter-frame PSNR, LPIPS over time, or flow warping error) would strengthen the evaluation.

## Removed Points

**From Harsh Critic:**
- The critic's framing that missing comparisons "fundamentally undermines the contribution" is too absolute — the core representation contribution (4D Gaussian with 4D rotation) is novel and independently interesting regardless of whether it beats every concurrent method. The missing comparison remains a major weakness, but it does not invalidate the methodology itself.

**From Strength Finder:**
- Several "supporting strengths" (e.g., "end-to-end training on entire videos," "emergent optical flow") are retained as they are concrete and verified.
- The claim that the method "achieves state-of-the-art" is kept but caveated — the evidence supports SOTA against the included baselines, but the omission of dynamic Gaussian baselines makes the broader SOTA claim unverifiable.

## Novel Insights

The reviews reveal a tension not fully addressed in the paper: the 4D Gaussian representation imposes a *constant-spatial-covariance* prior that is neither discussed nor analyzed. This is a genuinely novel observation about the paper's limitations that goes beyond what the authors reported. The missing baseline comparison, while important, is a standard experimental gap; the constant-covariance issue is a deeper methodological insight that could inform future work on 4D primitives for dynamic scenes.

## Suggestions

1. **Include direct quantitative comparisons against Luiten et al. (Dynamic 3D Gaussians), Yang et al. (Deformable 3DGS), Wu et al. (4D-GS), and Kratimenos et al. (DyMF) on both Plenoptic Video and D-NeRF datasets.** This is the single most important revision — without it, the paper's central claims cannot be properly evaluated.

2. **Add a discussion of the constant-covariance limitation** (Eq. 184). Analyze what types of motion the 4D Gaussian can and cannot represent, and show empirically whether densification compensates (e.g., track the number of Gaussians on scenes with different motion complexity, or compare the method's performance on articulated vs. rigid-motion scenes).

3. **Provide a quantitative evaluation of temporal consistency** — either standard metrics (inter-frame PSNR, LPIPS across time) or a simple comparison of the batch-sampling strategy vs. alternatives (e.g., random time sampling).

4. **Soften the "first ever" claim** in the introduction and conclusion, or qualify it carefully with respect to the specific combination of properties (real-time + high-fidelity + end-to-end on complex real-world scenes) rather than claiming primacy broadly.

## Score and Decision

**Calibration anchors (all from the provided human-review corpus):**

| Path | Avg Human Score | Comparison |
|------|----------------|------------|
| SplineGS (tMG6btjBfd) | 6.00 | Accepted. Similar topic (dynamic GS), compared against dynamic Gaussian baselines but had novelty concerns. Current paper has cleaner novelty but weaker experimental validation. |
| GaussianFlow (okD9dbifxa) | 5.83 | Rejected. Added flow supervision to 4DGS but missing comparisons. Current paper has more original core representation. |
| GSLK (dkrEoT68by) | 6.00 | Accepted. Analytical formulation with relevant baselines. Stronger empirical validation than current paper. |
| ReflectiveGS (xPxHQHDH2u) | 6.50 | Accepted. Well-evaluated on reflective scenes. Stronger experimental thoroughness. |
| KG4D (wKOoWTBMZe) | 3.67 | Rejected. Poorly written with unclear contributions. Current paper is far stronger. |
| HIWE (NLRo4qhg6t) | 3.00 | Rejected. Unrelated topic, weak contribution. |
| NoPoSplat (P4o9akekdf) | 8.00 | Accepted. Exceptionally strong submission with clean evaluation. |

The paper's core representation contribution is original and well-motivated. However, the omission of the most relevant dynamic Gaussian baselines from the experimental comparison is a significant gap that prevents verification of the central SOTA claims. This is the same class of issue that led to rejection of GaussianFlow (5.83). The paper is stronger than GaussianFlow in its core methodological novelty but weaker than SplineGS (6.00) in experimental thoroughness. With the required comparisons, it could be a solid contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>