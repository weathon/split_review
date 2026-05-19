## Summary
# Final Review Report

## Summary
This paper addresses the challenge of rendering unbounded neural radiance fields (NeRFs) when camera poses are positioned far from the scene origin. The authors identify that existing coordinate transformations (e.g., inverted-sphere mapping in NeRF++, contract mapping in mip-NeRF 360) rely on fixed manifold shapes (cylindrical, paraboloidal) that allocate representation capacity statically. This leads to severe sampling distortion and capacity waste when the viewing volume shifts. To overcome this, the paper proposes: (1) a unified geometric analysis of prior mappings via stereographic projection, (2) a p-norm-based adaptive mapping function that deforms the embedding manifold according to scene geometry, with automatic p-value estimation via RANSAC on COLMAP point clouds, and (3) an angular ray parameterization that preserves relative distances in the distorted space. Experiments on mip-NeRF 360, Tanks and Temples, and a free-trajectory dataset demonstrate consistent performance gains across MLP-based and voxel-based backbones, particularly in far-camera scenarios. While the geometric intuition is compelling and the modular evaluation is practical, the manuscript requires tighter mathematical rigor (dimensionality consistency in angular parameterization), statistical reporting (variance across seeds), and bounded claim wording to improve scientific defensibility.

## Strengths
1. **Unified Geometric Analysis:** The paper provides a novel and insightful reinterpretation of existing unbounded NeRF mappings (inverted-sphere, contract) through the lens of stereographic projection. Revealing their implicit manifold shapes (cylindrical, paraboloidal) offers a clear geometric explanation for their static capacity allocation and sampling vulnerabilities.
2. **Scene-Adaptive Manifold Deformation:** The p-norm-based mapping function is a conceptually elegant solution that directly addresses the fixed-manifold limitation. The ability to continuously deform the embedding space curvature based on scene geometry is a meaningful methodological advance.
3. **Modular & General Evaluation:** The experimental design effectively isolates the mapping function's contribution by embedding it into diverse backbones (DVGO, TensoRF, iNGP, NeRF). This demonstrates the method's compatibility and practical utility without requiring full system retraining.
4. **Practical Far-Camera Focus:** The paper targets a realistic and under-explored failure mode (camera displacement far from the scene origin), which is highly relevant for free-trajectory rendering and wide-baseline applications. The angular ray parameterization directly addresses the resulting sampling distortion.

## Weaknesses
1. **Mathematical Rigor in Angular Parameterization:** Equation (10) contains a dimensionality inconsistency: the viewing direction $d$ is 3D, while the center of projection $Q=(0,0,0,1)$ is 4D. The expression $\angle(d-Q, o-Q)$ is mathematically invalid without explicit coordinate lifting or projection. This threatens reproducibility and requires immediate correction.
2. **Statistical Reporting & Variance:** Table 1 and Table 2 report only mean metrics without standard deviation or confidence intervals across random seeds. Given that some performance margins are small (<0.5 dB), the absence of variance prevents assessment of statistical reliability and result stability.
3. **RANSAC Heuristic Justification:** The automatic p-value estimation via RANSAC ("maximizing distance between two projected points") lacks statistical or theoretical justification. Maximizing pairwise distance does not directly optimize for even distribution or capacity utilization, and the method may be sensitive to SfM point cloud noise or outliers.
4. **Overconfident Claim Wording:** The abstract and conclusion repeatedly use "state-of-the-art" without variance or scope bounding. The limitation paragraph honestly admits failure at extreme distances, which partially contradicts the main claim of robust far-camera rendering. Claims should be bounded to tested conditions (e.g., 2-4× scene radius).
5. **Ablation Study Clarity:** Table 2 mixes mapping function and ray parameterization changes in confusing column headers ("p-norm & normalized", "contract & angular"), making it difficult to isolate the individual contribution of each component. The ablation needs restructuring to clearly separate component-wise gains.

## Key Issues
1. **Dimensionality Mismatch in Eq. (10):** The angular parameterization formula uses $\angle(d-Q, o-Q)$ where $d \in \mathbb{R}^3$ and $Q \in \mathbb{R}^4$. This is mathematically invalid. The authors must explicitly define the 4D lifting of the ray direction or clarify that the angle is computed in a 3D subspace.
2. **Missing Variance Reporting:** All quantitative tables (Table 1, Table 2, Appendix Tables 3-11) report only mean values. Without standard deviation across $\geq 3$ random seeds, the statistical significance of small performance gains cannot be verified.
3. **RANSAC Heuristic Sensitivity:** The p-value selection relies on maximizing the distance between two randomly projected points. This heuristic is statistically weak and potentially sensitive to SfM noise. The authors should clarify whether median/percentile-based selection is used and provide robustness analysis against point cloud sparsity/noise.
4. **Unbounded SOTA Claims vs. Admitted Limitations:** The conclusion claims "state-of-the-art" performance while the limitation section admits failure at extreme camera distances. This contradiction reduces credibility. Claims must be explicitly bounded to the tested operational range (e.g., $\times 2$ to $\times 4$ displacement).
5. **Ablation Component Isolation:** Table 2 does not cleanly separate the contribution of the p-norm mapping from the angular parameterization. The current setup makes it impossible to determine which component drives the majority of the performance gain in far-camera scenarios.

## Actionable Suggestions
1. **Fix Eq. (10) Dimensionality:** Explicitly define the 4D lifting of the ray origin $o$ and direction $d$, or clarify that the angle is computed in the 3D subspace orthogonal to the hyper-axis. Replace $\angle(A, B)$ with standard vector angle notation: $\arccos\left(\frac{A \cdot B}{\|A\|\|B\|}\right)$.
2. **Add Variance Reporting:** Report mean $\pm$ std over $\geq 3$ random seeds in all quantitative tables. Add a paired significance test (e.g., t-test) against the strongest baseline for key results.
3. **Clarify RANSAC Robustness:** Specify whether the p-value selection uses median or percentile-based distance to mitigate outlier sensitivity. Add a brief ablation showing p-value stability under noisy/sparse COLMAP point clouds (already partially in Appendix E, but needs explicit connection to main text).
4. **Bound SOTA Claims:** Replace "state-of-the-art" with bounded comparative wording (e.g., "consistent improvements over selected baselines under reported settings"). Integrate the limitation into the conclusion as a defined operational boundary (e.g., "effective within 2-4× scene radius").
5. **Restructure Ablation Table:** Separate Table 2 into clear component-wise ablations: (a) Baseline (contract + normalized), (b) + p-norm mapping, (c) + angular parameterization, (d) Full method (RANSAC p). Provide a concise textual breakdown of the delta contributed by each component.
6. **Explicit Contribution Enumeration:** Add a bulleted contribution list at the end of the introduction summarizing C1 (geometric analysis), C2 (p-norm mapping), and C3 (angular parameterization).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Estimating neural radiance fields (NeRFs) enables novel view synthesis, but unbounded scenes require coordinate transformations to compress infinite space into learnable domains.
- **S2 (Significance/Challenge):** Existing mappings (e.g., inverted-sphere, contract) rely on fixed manifold shapes that statically allocate representation capacity, leading to severe sampling distortion when cameras are positioned far from the scene origin.
- **S3 (Prior Gap):** This fixed capacity distribution cannot adapt to varying scene geometries or free-trajectory camera setups, causing under-sampling in distant regions and capacity waste in empty space.
- **S4 (Proposed Method):** We propose a p-norm-based adaptive mapping function that deforms the embedding manifold according to scene structure, with automatic parameter estimation via RANSAC, and an angular ray parameterization that preserves sampling uniformity in the distorted space.
- **S5 (Key Result & Bounded Implication):** Integrated into diverse NeRF backbones, our method yields consistent performance gains on challenging unbounded benchmarks, particularly in far-camera scenarios where conventional mappings fail.

### Introduction Outline (Complete)
- **P1 (Big Picture & Bounded Limit):** Establish NeRF success in bounded scenes, then explain why simply expanding the volume fails (exponential sample growth, positional encoding aliasing, memory overhead).
- **P2 (Gap: Fixed Mapping Failure):** Introduce coordinate transformations as the standard solution, but highlight their vulnerability: fixed manifold shapes enforce static capacity allocation, breaking down under camera displacement.
- **P3 (Solution Intuition: Adaptive Manifold):** Propose deforming the manifold shape to match scene geometry. Introduce stereographic projection as a unified lens to analyze prior mappings and motivate p-norm deformation.
- **P4 (Method Component 1: p-norm Mapping):** Explain how the p-parameter controls curvature (convex for near, concave for far) and how RANSAC automatically estimates optimal p from COLMAP point clouds.
- **P5 (Method Component 2: Angular Parameterization):** Address sampling distortion in deformed space by introducing angular parameterization, which preserves relative distances and prevents over/under-sampling.
- **P6 (Evidence & Contributions):** Preview experimental validation across backbones and datasets. Explicitly enumerate contributions: (1) unified geometric analysis, (2) scene-adaptive p-norm mapping, (3) angular ray parameterization.

## Priority Revision Plan
| Priority | Task | Effort | Expected Impact |
|---|---|---|---|
| **P0** | Fix Eq. (10) dimensionality mismatch & clarify angle notation | Low | Resolves mathematical validity threat; enables correct implementation. |
| **P0** | Add mean ± std variance reporting across ≥3 seeds in all tables | Medium | Establishes statistical reliability; critical for small-margin claims. |
| **P1** | Restructure Table 2 ablation to isolate p-norm vs angular contributions | Low | Clarifies component-wise value; strengthens methodological argument. |
| **P1** | Bound "state-of-the-art" claims & integrate limitation as operational scope | Low | Improves scientific defensibility; resolves contradiction with limitation. |
| **P2** | Clarify RANSAC robustness (median/percentile selection) & noise sensitivity | Medium | Strengthens automatic p-value justification; improves reproducibility. |
| **P2** | Add explicit contribution enumeration at end of Introduction | Low | Improves narrative clarity; helps readers quickly grasp novelty. |

**Execution Order:** 
1. **Immediate (Today):** Fix Eq. (10) notation, bound SOTA claims, add contribution list.
2. **This Week:** Run multi-seed experiments for variance reporting, restructure ablation table.
3. **Before Submission:** Add RANSAC robustness analysis, finalize limitation integration, polish abstract/intro storyline.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Modular mapping evaluation across backbones | DVGO, TensoRF, iNGP, NeRF on mip-NeRF 360, TNT, Free | PSNR, SSIM, LPIPS | Consistent gains, especially in ×2 far-camera | C2, C3 | No variance reported |
| E2 | Ablation of p-norm vs contract & angular vs normalized | Bicycle scene, ×1 to ×8 displacement | PSNR, SSIM, LPIPS | p-norm + angular outperforms fixed baselines | C2, C3 | Component isolation unclear |
| E3 | RANSAC p-value robustness to noise/sparsity | Synthetic noise/sparsity on COLMAP points | p-value stability, PSNR | Relatively insensitive to sparsity; noise affects p | C2 | Not integrated into main text |
| E4 | Iterative p-value refinement from trained NeRF | Rendered views, error thresholding, re-estimation | PSNR, SSIM | Converges to optimal p, improves quality | C2 | Appendix-only, not main claim |

### Research-Theme Gap Diagnosis
- **Statistical Reliability:** Missing variance across seeds prevents confidence assessment for small margins.
- **Component Isolation:** Ablation does not cleanly separate mapping deformation from sampling parameterization.
- **Operational Boundary:** Limitation admits extreme-distance failure but does not quantify the effective range.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| C2/C3 Validity | Variance does not overturn mean gains | Run ×3 seeds on all Table 1 setups | Contract mapping baseline | PSNR ± std | Std < 0.3 dB, p<0.05 | 2 days GPU | Statistical confidence |
| C2 Isolation | p-norm mapping drives majority of far-camera gain | Ablate: (a) Baseline, (b) +p-norm, (c) +angular, (d) Full | Contract + normalized | PSNR delta | Clear component hierarchy | 1 day GPU | Methodological clarity |
| Operational Scope | Performance degrades predictably beyond ×4 | Test ×1 to ×8 displacement on 3 scenes | Contract mapping | PSNR drop curve | Quantified effective radius | 1 day GPU | Bounded claim defensibility |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10  
**Rationale:** The paper presents a compelling geometric insight (unified stereographic analysis of unbounded mappings) and a practical solution (p-norm adaptive manifold + angular parameterization) that addresses a realistic failure mode (far-camera rendering). The modular evaluation across diverse backbones is a strong point. However, the score is reduced due to mathematical rigor issues (dimensionality mismatch in Eq. 10), missing statistical variance reporting, weak justification for the RANSAC heuristic, and overconfident SOTA claims that contradict admitted limitations. These issues are fixable but currently impact reproducibility and scientific defensibility.

**Post-Revision Target:** [7.5, 8.5]/10  
**Conditions for Target:** 
1. Fix Eq. (10) dimensionality and clarify angle notation.
2. Add mean ± std variance across ≥3 seeds in all tables.
3. Restructure ablation to isolate component contributions.
4. Bound SOTA claims and integrate limitation as operational scope.
5. Clarify RANSAC robustness against SfM noise.

If these revisions are fully executed, the paper will achieve strong mathematical rigor, statistical reliability, and defensible claim scoping, warranting a competitive acceptance score.