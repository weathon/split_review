## Summary
# Final Review Report

## Summary

This paper proposes CasualHDR, a unified 3D Gaussian Splatting-based framework for reconstructing high dynamic range (HDR) scenes from casually captured videos with auto-exposure and motion blur. The method jointly optimizes continuous-time camera trajectory (using SE(3) B-splines), exposure time, camera response function (CRF), and the 3DGS scene representation within a differentiable physical imaging model. By coupling motion blur and brightness variations through exposure time, the approach eliminates the need for ground truth exposure times and robustly handles pose estimation failures caused by exposure inconsistencies. Extensive experiments on synthetic and real-world datasets demonstrate superior performance in novel view synthesis, image deblurring, and pose estimation compared to existing methods. The paper also introduces a new dataset (CasualVideo) and provides ablation studies validating the contribution of each module.

## Strengths
1. **Novel Problem Setting and Practical Motivation:** The paper addresses a highly practical and underexplored problem: reconstructing 3D HDR scenes from casual videos with auto-exposure and motion blur. This setting significantly lowers the data acquisition barrier compared to prior HDR methods that require fixed poses and precise exposure times.
2. **Unified Joint Optimization Framework:** The proposed method elegantly couples continuous-time camera trajectory, exposure time, CRF, and 3DGS representation within a differentiable physical imaging model. The insight that motion blur and brightness variations are both indicators of exposure time provides a strong theoretical foundation for joint optimization.
3. **Robust Pose Estimation under Exposure Variation:** By leveraging SE(3) B-splines for continuous trajectory representation, the method effectively regularizes high-frequency pose noise caused by motion blur and exposure inconsistencies, outperforming traditional SfM and frame-wise deblurring baselines.
4. **Comprehensive Evaluation and Dataset Contribution:** The paper introduces a challenging new dataset (CasualVideo) and provides extensive experiments on both synthetic and real-world benchmarks. The ablation studies clearly isolate the contributions of each module, and the inclusion of pose estimation metrics (ATE) strengthens the validity of the trajectory optimization claims.

## Weaknesses
1. **Missing Variance Reporting for Rendering Metrics:** The quantitative results in Tables 1-3 report only mean values for PSNR, SSIM, and LPIPS. Without variance (mean ± std) over multiple seeds, the statistical reliability of the reported gains, especially against strong baselines like Gaussian-W and BAD-Gaussians, cannot be fully assessed.
2. **Optimization Stability and Initialization Details:** The method treats exposure time $\Delta t$ as an optimizable quantity initialized randomly. However, the paper does not discuss how the joint optimization avoids degenerate solutions (e.g., $\Delta t \to 0$ or $\infty$) or how the mutual constraints between blur, brightness, and trajectory ensure convergence stability. This limits reproducibility.
3. **Overstated Contribution Claims and Broad Wording:** Contribution 3 claims "state-of-the-art performance across all datasets" without specifying the evaluation tasks or comparison scope. Similarly, the conclusion repeats broad performance claims without bounding them to the evaluated benchmarks. Such wording can reduce scientific credibility.
4. **Incomplete Baseline Comparison:** The related work mentions HDR-HexPlane, which handles unknown exposure times for dynamic scenes, but it is not included in the quantitative baseline comparison. Additionally, the unavailability of I2-SLAM is noted but not framed as an evaluation limitation, reducing transparency.
5. **Misinterpretation of Logarithmic Metric Gains:** The ablation study interprets PSNR improvements as percentages (e.g., "24% improvement"), which is misleading since PSNR is a logarithmic metric. Absolute delta gains should be reported to accurately reflect perceptual and error reductions.

## Key Issues
1. **Statistical Reliability of Rendering Gains:** The absence of variance reporting for PSNR/SSIM/LPIPS metrics prevents readers from assessing the stability of the reported improvements. Given the complex joint optimization space, multi-seed variance is critical to confirm that gains are consistent and not seed-dependent.
2. **Optimization Convergence and Degeneracy Risks:** The joint optimization of exposure time, CRF, and trajectory introduces a high-dimensional, non-convex objective. Without explicit discussion of initialization strategies, regularization terms, or convergence diagnostics, there is a risk of degenerate solutions (e.g., trivial exposure times or overfitting CRF) that could undermine reproducibility.
3. **Claim-Evidence Alignment in Contributions and Conclusion:** The contribution list and conclusion use broad, unbounded language ("state-of-the-art across all datasets") that overextends the experimental evidence. Scientific claims should be precisely scoped to the evaluated tasks, datasets, and comparison baselines to maintain objectivity and defensibility.
4. **Missing Comparison with Relevant Concurrent Methods:** The exclusion of HDR-HexPlane from quantitative baselines, despite its relevance to unknown exposure times, weakens the completeness of the evaluation. Additionally, the unavailability of I2-SLAM should be explicitly framed as a limitation rather than a passing comment.

## Actionable Suggestions
1. **Add Variance Reporting:** Report mean ± std over at least 3 random seeds for PSNR, SSIM, and LPIPS in Tables 1-3. This will establish statistical reliability and strengthen confidence in the reported gains.
2. **Clarify Optimization Stability:** In Section 3.4, explicitly describe the initialization strategy for exposure time $\Delta t$ (e.g., random initialization within a physically plausible range) and explain how the mutual constraints between blur extent, brightness, and trajectory prevent degenerate solutions. Consider adding a brief convergence analysis or visualization.
3. **Bound Contribution and Conclusion Claims:** Revise Contribution 3 and the conclusion to explicitly mention the evaluated tasks (novel view synthesis, image deblurring, pose estimation) and datasets. Replace broad phrases like "state-of-the-art across all datasets" with precise, evidence-bound wording.
4. **Complete Baseline Comparison:** Include HDR-HexPlane in the quantitative comparison if feasible, or explicitly justify its exclusion based on setting differences. Move the I2-SLAM comment to a limitations paragraph and frame its unavailability as an evaluation constraint.
5. **Correct Metric Interpretation:** In the ablation study (Section 4.6), rephrase PSNR improvements as absolute delta gains (e.g., "+4.0 dB") rather than percentages. Add a note on the computational overhead (training time/memory) associated with increasing the spline knot ratio to justify the choice of ratio=3.0.
6. **Improve Introduction Motivation:** Explicitly link auto-exposure-induced brightness variations to the breakdown of photo-consistency in traditional SfM pipelines, clarifying why joint trajectory optimization is necessary. Correct the typo "impoving" to "improving".

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** 3D scene representations like NeRF and 3DGS have advanced novel view synthesis, yet most rely on low dynamic range (LDR) inputs, limiting detail capture in high-contrast environments.
- **S2 (Significance/Challenge):** Prior HDR reconstruction methods typically require time-consuming multi-exposure captures at fixed poses, restricting practical flexibility and robustness to motion blur.
- **S3 (Gap):** Auto-exposure in casual videos expands dynamic range but introduces unknown exposure times, brightness inconsistencies, and severe motion blur, breaking traditional SfM and HDR pipelines.
- **S4 (Method):** We propose CasualHDR, a unified differentiable physical imaging model that jointly optimizes continuous-time camera trajectory (SE(3) B-spline), exposure time, CRF, and 3DGS-based HDR scene representation.
- **S5 (Result & Implication):** Extensive experiments on synthetic and real-world datasets demonstrate superior performance in novel view synthesis, image deblurring, and pose estimation, enabling robust 3D HDR reconstruction from casual videos.

### Introduction Outline (Complete)
- **P1 (Big Picture):** Establish the importance of photo-realistic 3D reconstruction and NVS in VR/AR and embodied AI, highlighting the transition from NeRF to efficient 3DGS.
- **P2 (Problem & Value):** Explain the limitation of LDR inputs in capturing high-contrast scenes and the practical value of 3D HDR content for downstream tasks.
- **P3 (Prior Work & Gap):** Categorize existing 3D HDR methods (RAW-based vs. multi-exposure LDR) and explicitly identify the gap: strict input requirements, motion blur risks, and SfM failure due to exposure variations.
- **P4 (Challenges of Casual Videos):** Detail the specific challenges of using casual auto-exposure videos: unknown exposure times, brightness inconsistencies breaking photo-consistency, and coupled motion blur.
- **P5 (Core Intuition):** Introduce the key insight that motion blur and brightness variations are both indicators of exposure time, providing a constraint for joint optimization.
- **P6 (Proposed Method):** Present CasualHDR as a unified framework coupling physical imaging with continuous trajectory representation, eliminating the need for ground truth exposure times.
- **P7 (Contributions):** List precise, bounded contributions: (1) CasualHDR method, (2) CasualVideo dataset, (3) SOTA performance on specific tasks/datasets.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Add mean ± std over ≥3 seeds for PSNR/SSIM/LPIPS in Tables 1-3. | Establishes statistical reliability of rendering gains; critical for reviewer confidence. | Low |
| **P0** | Clarify initialization and convergence stability for exposure time $\Delta t$ in Section 3.4. | Addresses reproducibility and degeneracy risks; strengthens methodological rigor. | Medium |
| **P1** | Bound contribution and conclusion claims to specific tasks/datasets; remove "SOTA across all datasets". | Improves scientific objectivity and defensibility; aligns claims with evidence. | Low |
| **P1** | Include HDR-HexPlane in baselines or explicitly justify exclusion; frame I2-SLAM unavailability as limitation. | Completes evaluation transparency; strengthens related work positioning. | Medium |
| **P2** | Rephrase ablation PSNR gains as absolute deltas; add computational cost note for spline ratio. | Corrects metric interpretation; provides practical deployment context. | Low |
| **P2** | Explicitly link exposure variations to SfM photo-consistency failure in Introduction. | Sharpens motivation and problem-solution alignment. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | CasualHDR outperforms baselines in NVS under motion blur/exposure variation. | Synthetic (Blender) & Real (CasualVideo, ScanNet) | PSNR, SSIM, LPIPS | Superior rendering quality vs. HDR-NeRF, Gaussian-W, BAD-Gaussians. | C3 (Performance) | No variance reported; HDR-HexPlane missing. |
| E2 | CasualHDR accurately recovers camera trajectories. | RealSense sequences with Vicon GT | ATE (mean±std) | Lower ATE than HLoc, DPV-SLAM, BAD-Gaussians. | C1 (Trajectory Opt) | Limited to 2 sequences with GT. |
| E3 | Module contributions isolated. | Synthetic datasets (Pool, Factory, Cozyroom) | PSNR, SSIM, LPIPS | Continuous trajectory & joint Exp/CRF opt provide largest gains. | C1 (Method Design) | PSNR gains reported as percentages. |
| E4 | Spline knot ratio sensitivity. | Synthetic datasets | PSNR, SSIM, LPIPS | Performance saturates at ratio=3.0. | C1 (Hyperparameter) | Computational cost not discussed. |
| E5 | Deblurring quality on real data without sharp GT. | ScanNet | BRISQUE | Lower BRISQUE than BAD-Gaussians. | C3 (Deblurring) | No-reference metric limits direct comparison. |

### Research-Theme Gap Diagnosis
The core research-value claims (robust HDR reconstruction from casual videos) are well-supported by E1-E3. However, the lack of variance reporting (E1) and missing baseline (HDR-HexPlane) weakens the statistical and comparative rigor. The computational efficiency trade-off for trajectory regularization (E4) is underexplored, limiting practical deployment claims.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Gains are consistent across random seeds. | Run E1 with 3 seeds. | Same baselines. | PSNR±std, SSIM±std | Std < 0.5 dB | Low | Validates robustness of gains. |
| Optimization Stability | Joint opt avoids degenerate $\Delta t$. | Visualize $\Delta t$ convergence; test init sensitivity. | Fixed init vs random. | PSNR, $\Delta t$ error | Stable convergence | Low | Improves reproducibility trust. |
| Computational Efficiency | Ratio=3.0 balances quality and speed. | Measure training time/memory for ratios 1.0-4.0. | Baseline 3DGS. | Time, VRAM, PSNR | Pareto optimal | Low | Justifies hyperparameter choice. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper addresses a highly practical and underexplored problem with a well-motivated, unified optimization framework. The joint modeling of continuous trajectory, exposure time, and CRF is conceptually strong and demonstrates clear performance gains over relevant baselines. However, the score is moderated by the lack of variance reporting for rendering metrics, insufficient discussion of optimization stability/convergence, and overstated contribution claims that overextend the experimental evidence. The missing comparison with HDR-HexPlane and unframed I2-SLAM limitation further reduce evaluation completeness. With the suggested revisions (variance reporting, claim bounding, stability clarification), the paper would be significantly stronger.

**Post-Revision Target:** [7.5, 8.5]/10

**Page Coverage Audit:**
| Page | Annotation Count | Coverage Status | Skip Reason |
|---|---|---|---|
| 1 | 1 | Covered | |
| 2 | 1 | Covered | |
| 3 | 1 | Covered | |
| 4 | 1 | Covered | |
| 5 | 1 | Covered | |
| 6 | 1 | Covered | |
| 7 | 1 | Covered | |
| 8 | 1 | Covered | |
| 9 | 1 | Covered | |
| 10 | 1 | Covered | |
| 15 | 1 | Covered | |
| 16-19 | 0 | Skipped | Non-substantive/figure-only pages; claims covered in main text/appendix P15. |