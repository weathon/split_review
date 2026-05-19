- Decision: Reject
- Avg Score: 5.83
- Scores: 5, 6, 5, 8, 6, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces **Gaussian flow**, a differentiable mapping from 3D Gaussian dynamics (translation, rotation, scaling) to 2D pixel velocities via splatting. By matching Gaussian flow to pre-computed optical flow on input video frames, the method directly supervises Gaussian motions during optimization. Experiments on 4D generation (Consistent4D) and 4D novel view synthesis (DyNeRF) show consistent improvements over prior methods, especially on dynamic regions with large motion.

## Strengths

1. **Novel analytical formulation bridging 3D Gaussian dynamics to 2D pixel flow.** The paper derives an explicit, differentiable mapping (Eq. 3) that connects a Gaussian's translation, scaling, and rotation to the pixel shifts it induces upon projection. This is the first direct bridge between 4D Gaussian Splatting and optical flow, enabling motion supervision without implicit temporal regularizers. (Section 3.2)

2. **State-of-the-art results on 4D generation.** On the Consistent4D dataset (Table 1), the method achieves the best mean LPIPS (0.14) and CLIP score (0.91) across all 7 scenes, outperforming DreamGaussian4D (0.16 LPIPS, 0.87 CLIP) and Consistent4D (0.16 LPIPS, 0.87 CLIP). Gains are consistent on every individual scene.

3. **State-of-the-art results on 4D novel view synthesis.** On the DyNeRF dataset (Table 2), the method achieves mean PSNR 32.30 vs. RT‑4DGS baseline 32.01. On dynamic regions (optical flow >1 pixel), the gain is larger: 28.99 vs. 28.00, directly demonstrating that motion supervision benefits moving content. (Section 4.3.2)

4. **Flow supervision demonstrably outperforms Local Rigidity Loss on challenging motions.** In the ablation (Fig. 6), the model with Local Rigidity Loss but no flow fails to split Gaussians for the opening skull mouth, while the flow-supervised version succeeds. This provides clear qualitative evidence that flow supervision is a stronger motion regularizer.

5. **Efficient and differentiable implementation.** The dynamics splatting is implemented as a CUDA extension of the tile-based 3DGS renderer, maintaining the efficiency of the original pipeline while adding only \(H\times W\times K\) tensors for per-pixel Gaussian indices and distances. (Section 4.1)

## Weaknesses

### Fatal

None.

### Major

1. **The core assumption underlying Gaussian flow is stated but not justified as a model of true scene motion.** The paper assumes (line 86–87) that a pixel's relative position within a Gaussian's local coordinate system remains constant across frames, which preserves the Gaussian probability density at the tracked pixel. While this is a geometrically self-consistent definition (it ensures the pixel receives the same radiance/opacity contribution from the Gaussian), the paper provides no argument—theoretical or empirical—that this quantity corresponds to the actual optical flow of scene points. Calling it an "analytical solution" (Conclusion) overstates the grounding: it is a well-defined but arbitrary mapping that *defines* how Gaussian dynamics translate to pixel motion, rather than being derived from physical correspondence. The method works empirically, and this is ultimately a modeling choice, but the conceptual framing would be stronger with a clear justification or a first-order analysis showing that, under small deformations, the Gaussian-relative coordinate tracking approximates true correspondence.

2. **Quantitative evaluation does not directly measure motion quality and lacks statistical rigor.** Table 1 uses LPIPS and CLIP—metrics that capture appearance and semantic similarity, not motion fidelity. While Table 2's dynamic-region PSNR (28.00→28.99) is the best evidence that flow supervision helps motion, improvements could partly reflect better static appearance or noise reduction. No direct motion metric is reported (e.g., warped-frame PSNR, scene flow end-point error, temporal consistency). Furthermore, no error bars, confidence intervals, or multi-seed statistics are provided for any quantitative result. Given that the method adds only a flow loss to an unchanged base representation, the ~0.3 dB full-scene PSNR gain could plausibly fall within run-to-run variation without significance testing.

### Minor

1. **Unclear which Gaussian flow formulation was used for the anisotropic RT‑4DGS experiments.** The paper presents the full form (Eq. 3) and a simplified form (Eq. 4) that assumes isotropy and small scale change (\(\mathbf{B}_{i,t_2}\mathbf{B}_{i,t_1}^{-1} \approx \mathbf{I}\)). The DyNeRF experiments use RT‑4DGS, which represents anisotropic Gaussians. The paper does not specify whether the full Eq. 3 or the approximate Eq. 4 was employed. If the simplified form was used despite anisotropy, the approximation error is unquantified.

2. **The optical flow estimator is not clearly specified in the implementation section.** The text refers generically to "off-the-shelf methods" (line 130). Later in Section 4.3.2, [shi2023videoflow] is cited for DyNeRF, and the Fig. 8 caption mentions autoflow [sun2021autoflow]. The implementation section (Section 4.1) should state the exact flow model, version, and any preprocessing used for each task to ensure reproducibility.

3. **No sensitivity analysis for key hyperparameters.** The flow loss weight \(\lambda_1\) and the number of top‑\(K\) Gaussians (\(K=20\)) are not ablated. The choice \(K=20\) is motivated by "balance speed and effectiveness" without showing how results vary with \(K\). Since gradient signals come only from the top‑\(K\) Gaussians, this could materially affect motion supervision.

4. **No discussion of failure cases or when flow supervision may hurt.** Optical flow estimates can be unreliable near occlusions, fast motion, or textureless regions. The paper does not analyze scenarios where flow supervision might degrade results or lead to artifacts.

### Trivial

None.

## Nice-to-Haves

- Comparison against a simpler flow supervision baseline (e.g., directly projecting each Gaussian's 3D mean velocity into 2D via the camera Jacobian) to isolate the benefit of the full composition over multiple Gaussians and deformation modeling.
- Robustness analysis: replacing the optical flow estimator with a different one to test sensitivity to flow quality.
- Long-term flow supervision across multiple frames (acknowledged as future work in the paper).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing comparison with flow-supervised dynamic NeRF"** (Harsh Critic, Critical Issue 3): The paper's scope is Gaussian-based representations, not NeRFs. Comparing against a NeRF+flow baseline would be off-scope — the relevant comparison (Ours vs. Ours without flow) is already provided.
- **"Missing code release"** (Harsh Critic, "Places to Improve"): Standard for non-camera-ready submissions; not a weakness of the paper's scientific contribution.
- **"Only short-term flow, no multi-frame coherence"** (Harsh Critic, Section-by-Section Notes): The paper explicitly acknowledges this as a limitation and discusses it as future work (Conclusion). Not a novel oversight.
- **"The central claim that Gaussian flow 'drastically improves' motion is not quantitatively demonstrated"** (Harsh Critic, Critical Issue 2): The dynamic-region PSNR (+0.99 dB in Table 2) does provide quantitative evidence of motion improvement, albeit indirectly. This phrasing overstates the gap.

## Novel Insights

None beyond the paper's own contributions. The key insight — defining Gaussian flow via normalized/unnormalized mappings through individual Gaussian coordinate systems and composing via alpha weights — is the paper's own contribution and is not an observation surfaced by the reviews.

## Suggestions

1. **Provide a brief justification for the core assumption.** Show that, under small inter-frame motion (which is the regime where dense optical flow is most reliable), the constant-relative-position assumption approximates linearized scene flow through the Gaussian representation. Even a short geometric intuition would substantially strengthen the paper.
2. **Add a direct motion metric.** Compute the warping error between consecutive rendered frames (warp using the predicted Gaussian flow, measure error against the actually rendered next frame). On synthetic data with known ground truth, report end-point error of Gaussian flow vs. true scene flow.
3. **Report error bars.** Run at least 3 seeds (or report standard deviation across the scenes) for the main quantitative results, especially the DyNeRF dynamic-region PSNR where the gains are most meaningful.
4. **Clarify Eq. 3 vs. Eq. 4 usage** for the RT‑4DGS experiments and specify the optical flow estimator(s) explicitly in Section 4.1.
5. **Add a failure case analysis** discussing when flow supervision might be unreliable (e.g., occlusions, textureless regions).
