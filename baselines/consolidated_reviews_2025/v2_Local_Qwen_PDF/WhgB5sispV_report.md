## Summary
# Final Review Report

## Summary
This paper proposes 4D Gaussian Splatting (4DGS), a novel representation for dynamic scene reconstruction and real-time novel view synthesis. By treating space and time as a unified 4D volume, the method employs 4D Gaussian primitives with anisotropic ellipses and 4D rotations to capture intrinsic scene motion. Appearance evolution is modeled using 4D Spherindrical Harmonics (4DSH), extending traditional spherical harmonics with a temporal Fourier basis. The authors demonstrate that this coherent spatiotemporal formulation avoids the limitations of frame-by-frame or deformation-based approaches, achieving state-of-the-art visual quality and real-time rendering speeds (over 100 FPS) on both monocular (D-NeRF) and multi-view (Plenoptic Video) benchmarks. The work also includes an extension to urban scenes using LiDAR supervision. While the conceptual unification of 4D Gaussians is elegant and empirically effective, the manuscript requires tighter claim-evidence alignment, quantitative anchoring in the abstract/introduction, and more rigorous ablation and urban scene evaluations to fully substantiate its contributions.

## Strengths
1. **Conceptual Elegance and Unification:** The proposal to treat space and time as a unified 4D volume using 4D Gaussian primitives is conceptually clean and mathematically well-motivated. By leveraging 4D rotations and conditional distributions, the method naturally captures spatiotemporal correlations without relying on explicit deformation fields or frame-by-frame tracking.
2. **Strong Empirical Performance:** The method achieves state-of-the-art results on established dynamic scene benchmarks (Plenoptic Video and D-NeRF), significantly outperforming prior implicit and explicit representations in both visual quality (PSNR/SSIM/LPIPS) and rendering speed.
3. **Real-Time Rendering Capability:** The adaptation of the tile-based rasterizer to handle 4D Gaussians enables real-time synthesis at over 100 FPS, which is a substantial practical advantage for AR/VR and interactive applications.
4. **Interpretable Temporal Appearance Modeling:** The introduction of 4D Spherindrical Harmonics (4DSH) provides a compact, continuous basis for modeling time-evolving view-dependent appearance, avoiding the redundancy of per-frame color attributes.
5. **Practical Extension to Urban Scenes:** The appendix demonstrates the method's adaptability to large-scale urban environments by integrating LiDAR depth supervision and background modeling, highlighting its potential for autonomous driving applications.

## Weaknesses
1. **Unquantified and Overstated Claims:** The abstract and introduction make strong SOTA and "first-ever" claims without providing concrete metric anchors (e.g., specific PSNR gains or FPS numbers). Contribution (ii) uses vague qualitative descriptors ("useful and interpretable") instead of explaining the technical mechanism of 4DSH.
2. **Insufficient Implementation Details for Real-Time Claims:** The mathematical formulation of the 4D Gaussian conditional distribution (Eq. 9) does not address the computational cost or numerical stability of computing conditional covariances during the high-frequency rasterization loop. Without clarifying how these operations are optimized or cached, the real-time rendering claim lacks implementation-level credibility.
3. **Limited Ablation Scope and Qualitative Motion Analysis:** The ablation studies (Table 3) are evaluated on only two scenes, limiting statistical significance. Furthermore, the claim that the method captures "coarse scene dynamics" is supported only by qualitative optical flow visualizations, lacking quantitative motion error metrics (e.g., End-Point Error).
4. **Uneven Baseline Comparisons and Missing Hardware Specs:** Table 1 compares against a competing "4DGS" method evaluated on only a subset of scenes, creating an uneven comparison. The FPS metric lacks critical hardware and resolution specifications, hindering reproducibility and fair efficiency assessment.
5. **Purely Qualitative Urban Scene Evaluation:** The extension to urban scenes (Appendix D) demonstrates practical applicability but relies entirely on qualitative results. It lacks quantitative metrics, comparison against urban-specific baselines, and justification for deactivating the temporal coefficient of 4DSH.

## Key Issues
1. **Claim-Evidence Misalignment in Abstract/Intro:** The manuscript makes broad novelty and performance claims without quantitative backing in the opening sections. This forces readers to search the main text for validation and risks perceived overstatement.
2. **Computational Efficiency of 4D Conditioning:** The derivation of conditional 3D Gaussian parameters from the 4D covariance matrix is mathematically correct but computationally non-trivial. The absence of implementation details regarding matrix inversion, caching, or runtime optimization undermines the real-time rendering assertion.
3. **Ablation Statistical Rigor:** Evaluating core component ablations on only two scenes reduces the generalizability of the conclusions. Additionally, qualitative optical flow visualization is insufficient to validate emergent motion dynamics without quantitative error metrics.
4. **Fairness and Reproducibility of Baselines:** The comparison with the competing 4DGS method is uneven due to partial scene evaluation. Missing hardware specifications for FPS measurements prevent accurate efficiency benchmarking against prior work.
5. **Urban Scene Validation Depth:** The urban extension is promising but under-evaluated. Purely qualitative results and unexplained architectural modifications (deactivating 4DSH temporal coefficients) limit the scientific contribution of this application case.

## Actionable Suggestions
1. **Quantify Abstract and Contribution Claims:** Insert concrete metrics (e.g., average PSNR gain, rendering FPS) into the abstract and Contribution (iii). Rewrite Contribution (ii) to explicitly describe the 4DSH mechanism (e.g., Fourier-series temporal basis) rather than using vague adjectives.
2. **Clarify 4D Conditioning Implementation:** Add a concise implementation note in Section 3.2 explaining how the conditional mean and covariance (Eq. 9) are computed efficiently during rasterization. Mention precomputing $\Sigma_{4,4}^{-1}$, caching cross-covariance terms, or leveraging block-matrix structures to avoid runtime bottlenecks.
3. **Expand Ablation Scope and Add Motion Metrics:** Extend Table 3 ablation results to include averages across all Plenoptic Video scenes. Complement Figure 4 optical flow visualizations with a quantitative metric (e.g., End-Point Error or AUC) to rigorously validate emergent motion dynamics.
4. **Standardize Baseline Comparisons and Hardware Specs:** Rename the competing method to "4DGS-Wu" to avoid confusion. Explicitly state the GPU model, rendering resolution, and whether FPS includes preprocessing. Provide per-scene breakdowns to ensure fair apples-to-apples comparisons.
5. **Strengthen Urban Scene Evaluation:** Add quantitative metrics (e.g., depth error, PSNR) for the Waymo urban scenes. Briefly justify deactivating 4DSH temporal coefficients (e.g., stable daylight conditions). If feasible, include a comparison with a recent urban Gaussian baseline to contextualize performance.
6. **Balance Conclusion with Limitations:** Append a brief statement in the conclusion acknowledging current constraints (e.g., background reconstruction, initialization sensitivity) and outlining concrete future directions (e.g., adaptive background modeling, streaming updates).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Reconstructing dynamic 3D scenes from 2D images remains challenging due to complex spatiotemporal correlations and temporal dynamics.
- **S2 (Significance/Challenge):** Existing neural implicit models struggle with either inadequate scene structure or impractical deformation modeling, limiting real-time applicability.
- **S3 (Prior Gap):** Methods that explicitly model motion often lack scalability, while plenoptic function learners suffer from parameter coupling and interference.
- **S4 (Proposed Method):** We approximate the underlying spatio-temporal 4D volume using a collection of 4D Gaussian primitives, parameterized by anisotropic ellipses with arbitrary 4D rotations and time-evolved appearance via 4D spherindrical harmonics.
- **S5 (Key Result & Bounded Implication):** Experiments on monocular and multi-view benchmarks demonstrate state-of-the-art visual quality (e.g., +X.X PSNR on Plenoptic Video) and real-time rendering at over 100 FPS, significantly outperforming prior dynamic scene representations.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Establish the importance of dynamic novel view synthesis for AR/VR and autonomous driving. Highlight the fundamental challenge of preserving spatiotemporal correlations while minimizing interference between unrelated locations.
- **P2 (Prior Work Limitations):** Categorize existing methods into plenoptic function learners (lack flexibility, parameter coupling) and explicit motion/deformation models (reduced scalability, complex tracking). Emphasize the trade-off between temporal correlation and spatial interference.
- **P3 (Proposed Solution & Intuition):** Introduce the core idea of treating spacetime as a unified 4D volume. Explain how 4D Gaussians with 4D rotations naturally fit the 4D manifold and capture intrinsic motion without explicit tracking.
- **P4 (Technical Components):** Briefly describe the 4D Gaussian formulation, conditional 3D projection for rasterization, and 4D Spherindrical Harmonics for continuous temporal appearance evolution.
- **P5 (Evidence & Contributions):** Preview key empirical outcomes (SOTA quality, real-time speed) and list explicit, quantified contributions. Bound claims to evaluated benchmarks and provide concrete metric anchors.

## Priority Revision Plan
| Priority | Task | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Quantify abstract/intro claims with concrete PSNR/FPS metrics. | Improves claim-evidence alignment and initial reader impact. | Low |
| **P0** | Clarify 4D conditioning implementation efficiency (caching/precomputation). | Validates real-time rendering claim and addresses computational concerns. | Low |
| **P0** | Expand ablation to all scenes and add quantitative optical flow metrics (EPE). | Strengthens statistical rigor and motion dynamics validation. | Medium |
| **P1** | Standardize baseline naming ("4DGS-Wu") and add hardware specs for FPS. | Ensures fair comparison and reproducibility. | Low |
| **P1** | Add quantitative metrics and justify 4DSH modification for urban scenes. | Deepens application validation and scientific contribution. | Medium |
| **P2** | Balance conclusion with explicit limitations and future directions. | Enhances scientific credibility and roadmap clarity. | Low |

**Execution Strategy:** Begin with P0 text revisions to immediately tighten claim-evidence alignment. Proceed to P0/P1 experimental clarifications by extracting existing logs or running lightweight ablations. Finally, address P2 narrative adjustments to ensure a balanced, professional closing.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Multi-view real scenes SOTA comparison | Plenoptic Video (6 scenes) | PSNR, DSSIM, LPIPS, FPS | Outperforms baselines in quality and speed | Real-time high-fidelity synthesis | Uneven baseline evaluation (4DGS-Wu on 3 scenes) |
| E2 | Monocular synthetic scenes comparison | D-NeRF (8 scenes) | PSNR, SSIM, LPIPS | Surpasses all competing methods | Effective monocular dynamic reconstruction | Lacks variance/multi-seed reporting |
| E3 | Component ablation (4DRot, 4DSH, Time split) | Flame Salmon, Cut Beef | PSNR, SSIM | Full model superior to ablated variants | Validates core design choices | Limited to 2 scenes; lacks statistical averaging |
| E4 | Emergent motion dynamics validation | Plenoptic Video test views | Qualitative optical flow | Rendered flow matches GT trends | 4D rotation captures underlying motion | Purely qualitative; no quantitative error metric |
| E5 | Urban scene applicability | Waymo Open Dataset segments | Qualitative RGB/Depth | High-fidelity dynamic/static rendering | Adaptable to large-scale sparse scenes | Purely qualitative; missing metrics/baselines |

### Research-Theme Gap Diagnosis
The core research value lies in the unified 4D representation and real-time capability. However, the evidence for motion dynamics (E4) and urban generalization (E5) is weakly supported due to qualitative-only evaluation. Statistical reliability (multi-seed variance) is also missing, which limits reproducibility confidence.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Motion Dynamics | 4D Gaussians implicitly learn accurate 3D trajectories. | Compute rendered optical flow vs GT flow across all scenes. | VideoFlow GT | EPE, AUC | EPE < X pixels | Low | Quantitative validation of emergent motion |
| Ablation Robustness | Component gains are consistent across diverse dynamics. | Run ablation on all 6 Plenoptic scenes. | Full model | PSNR, SSIM | Consistent delta | Low | Statistical significance of design choices |
| Urban Generalization | Method generalizes to unbounded outdoor dynamics. | Evaluate on Waymo with depth/RGB metrics. | StreetGaussian/VGGT | Depth L1, PSNR | Competitive metrics | Medium | Stronger application validation |
| Reproducibility | Results are stable across random seeds. | Train 3 seeds on Plenoptic/D-NeRF. | Default run | Mean±Std | Std < 0.2 PSNR | Medium | Establishes statistical reliability |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a conceptually elegant and empirically strong method for dynamic scene representation. The unified 4D Gaussian formulation and real-time rendering capability are significant contributions. However, the score is moderated by unquantified claims in the abstract/introduction, insufficient implementation details regarding computational efficiency, limited ablation scope, and purely qualitative urban scene evaluation. Addressing these issues would substantially strengthen the manuscript's scientific rigor and reproducibility.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Quantifying all SOTA and efficiency claims, clarifying the 4D conditioning runtime optimization, expanding ablations to full datasets with quantitative motion metrics, and adding baseline comparisons/metrics for urban scenes will resolve the core validity and reproducibility concerns, elevating the paper to a strong acceptance standard.