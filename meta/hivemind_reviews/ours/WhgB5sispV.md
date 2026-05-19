## Summary
This paper proposes 4D Gaussian Splatting (4DGS), extending 3D Gaussian Splatting to dynamic scenes by treating space and time as a unified 4D volume. The representation uses 4D Gaussian primitives with 4D rotations (parameterized by two quaternions) and 4D Spherindrical Harmonics (4DSH) for time-evolved view-dependent appearance, combined with a splatting-based rasterizer. The method achieves state-of-the-art rendering quality on the Plenoptic Video and D-NeRF benchmarks while being the only evaluated method to deliver real-time rendering speeds.

## Strengths
1. **Unified 4D Gaussian formulation with interpretable motion modeling**: The coherent 4D covariance matrix with 4D rotation (decomposed into left/right quaternions \(L(q_l)R(q_r)\)) provides a principled way to model spatiotemporal correlations. The conditional distribution \(\mu_{xyz|t}\) yields a natural linear trajectory per primitive without requiring an explicit deformation field or tracking. This is a conceptually clean extension of 3DGS. (Evidence: Section 3.2, Eqs. 6–8.)

2. **State-of-the-art rendering quality with real-time speed**: On the Plenoptic Video dataset, 4DGS achieves the highest PSNR/SSIM/LPIPS among all compared methods while being the only one to run at real-time frame rates. The combination of high fidelity and efficiency is a significant practical contribution. (Evidence: Table 1 [\input{table/sota_dynerf}], Section 4.3.)

3. **4D Spherindrical Harmonics provide a compact temporal appearance model**: Extending SH with Fourier-series time basis functions enables each Gaussian to model time-varying view-dependent color without duplicating primitives. The ablation study confirms this component improves rendering quality. (Evidence: Section 3.2 "4D spherindrical harmonics," Eq. 9; Table 3 ablation row.)

4. **Ablation validates each component**: Systematic removal of 4D rotation, 4DSH, and temporal densification each degrades performance on held-out scenes, demonstrating that all three innovations contribute meaningfully. (Evidence: Table 3 [\input{table/ablation_main}], Section 4.4.)

5. **Generalization across dataset types**: The method performs well on both multi-view real-world scenes (Plenoptic Video) and monocular synthetic scenes (D-NeRF), showing the representation is not tied to a specific supervision setup. (Evidence: Tables 1 & 2, Sections 4.3.)

## Weaknesses
### Fatal

None.

### Major

1. **Overclaimed generality of motion modeling**: The paper repeatedly claims the ability to "capture complex dynamic scene motions" and "scene intrinsic motion" (abstract, Sec. 3.2, conclusion) without qualifying that each individual 4D Gaussian assumes linear translation with a **time-invariant spatial covariance** (Eqs. 7–8: \(\mu_{xyz|t}\) is linear in \(t\); \(\Sigma_{xyz|t}\) is independent of \(t\)). Per-primitive, the model cannot represent acceleration, shape deformation, or rotation of the ellipsoid over time. While a mixture of Gaussians can approximate non-linear motion piecewise, the paper never discusses this structural limitation or characterizes what class of motions the representation supports. This omission affects how researchers assess the method's applicability to scenes with non-rigid or accelerating motion.

### Minor

1. **Motion capture claim lacks quantitative support**: The optical flow visualization (Fig. 4) is presented as evidence that "optimizing rendering loss alone can lead to the emergence of coarse scene dynamics," but no quantitative evaluation (e.g., endpoint error, warping error against ground truth flow) is provided. This weakens the motion-capture narrative; the claim would be substantially stronger with a numerical benchmark.

2. **No limitations section**: The paper does not discuss failure cases, representational limitations, or scenarios where the method would struggle. Given the strong assumptions noted above (linear per-primitive motion, time-invariant covariance, cosine-only 4DSH), the absence of an honest limitations discussion reduces scientific completeness.

3. **GPU hardware not specified alongside FPS claims**: The paper reports achieving the only real-time rendering among competing methods but does not state the GPU model used for these speed measurements, making the speed claim difficult for practitioners to contextualize or reproduce.

### Trivial

1. **Ablation limited to two scenes**: The ablation study (Table 3) is conducted on only two representative scenes rather than the full dataset. While two scenes are sufficient to demonstrate trends, full-dataset ablations would rule out scene-specific effects.

## Suggestions
1. Add a limitations section that explicitly states the per-primitive linear-motion / fixed-shape assumption, along with examples of scene types where the method would struggle (e.g., fast non-rigid deformation, topological changes).
2. Either add a quantitative optical flow evaluation (e.g., average endpoint error on Plenoptic Video where multi-view stereo can provide ground truth) or tone down the motion-capture framing.
3. Specify the GPU hardware used for all FPS measurements.
4. Consider running the ablation study on the full Plenoptic Video dataset to improve statistical reliability.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
