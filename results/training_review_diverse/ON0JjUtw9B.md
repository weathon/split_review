Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes WIN, a LiDAR upsampling network that decouples the standard range view (RV) into two orthogonal virtual views — Horizon Range View (HRV) and Vertical Range View (VRV) — to overcome the geometric limitations of single-view interpolation. A Contrast Selection Module (CSM) with probabilistic confidence modeling fuses the two views. The method is evaluated on CARLA and KITTI against explicit and implicit baselines, and tested on a downstream depth completion task. WIN achieves consistent improvements (+4.53% MAE, +7.01% IoU on CARLA) with only 1.7M parameters.

## Strengths

- **Variable-view decoupling addresses a genuine limitation of range-view interpolation.** The paper identifies that a single range view cannot accurately represent complex local geometry (e.g., object edges, ground surfaces) and proposes decoupling into HRV and VRV. This is well-motivated by concrete examples in Figure 1, and the quantitative results (Table 1: +4.53% MAE, +7.01% IoU on CARLA over ILN) directly validate the core claim.

- **Contrast Selection Module with probabilistic confidence modeling is novel and effective.** Instead of a hard binary view classifier, the CSM models view fusion as a confidence prediction problem using a Gaussian-based loss (Eq. 9) and a custom margin loss (Eq. 10). Ablation results (Table 4) show CSM contributes ~2.4% MAE and ~2.9% IoU improvement. The probabilistic supervision is shown to outperform binary cross-entropy (Figure 5).

- **Consistent improvements across datasets, scales, and downstream tasks.** WIN outperforms both explicit (TULIP, LiDAR-SR) and implicit (ILN, LIIF) methods on single-scale (Table 1), multi-scale (Table 2), and downstream depth completion (Table 3: 20mm RMSE reduction over ILN) on both synthetic CARLA and real KITTI data, all while adding only +0.4M parameters over ILN.

- **Thorough ablation study.** Table 4 systematically removes variable-view interpolation, the CSM, and the confidence loss, demonstrating that each component is necessary for the reported gains. The binary classification baseline provides a clear comparison point.

## Weaknesses

### Fatal
None.

### Major

- **Non-standard KITTI evaluation protocol undermines comparability with prior work.** The paper adjusts the KITTI projection (referencing Fan et al. 2021), citing non-unique projection centers in the standard KITTI setup, and retrains all methods under this adjusted setting. While this ensures within-paper fairness (all methods compared under identical conditions), the deviation from the de facto standard means the results in Table 1 are not directly comparable with any previously published numbers. The paper should report results under **both** the standard KITTI projection and its adjusted projection, or provide a stronger justification for why the adjustment is necessary. This is the most significant evidential concern — it does not invalidate the core contribution, but it requires the reader to trust the modified protocol without being able to cross-reference against the literature.

### Minor

- **Methodology description for virtual views is underspecified.** The paper explains that HRV interpolates horizontal distances (z ignored) and VRV interpolates heights (x,y ignored), and Eq. 3 gives the interpolation formulas with divisions by cos v and sin v. However, the forward mapping from 3D points to HRV/VRV "grids" is never formally defined — the description focuses on what values are interpolated rather than the coordinate transformation. A reader familiar with LiDAR spherical projection can reconstruct the mechanism (d_t = sqrt(x²+y²), cos v/sin v convert back to range), but the paper should provide explicit forward/inverse projection equations for both virtual views. This does not prevent reproducibility (the mechanism is inferable) but is a clarity gap that should be addressed.

- **No point-level geometric metrics despite the paper's central claim about geometric accuracy.** The paper emphasizes that single-view interpolation fails to capture local geometry, yet evaluates only MAE on range images and voxel IoU at 0.1 m. These are standard metrics, but adding Chamfer distance, point-to-mesh distance, or surface normal consistency (especially on CARLA where ground truth is clean) would directly substantiate the geometric accuracy claim. The downstream depth completion task partially addresses this, but not at the point level.

- **Hyperparameter λ (Gaussian standard deviation scale) is neither reported nor ablated.** The probabilistic loss in Eq. 9 depends on λ, which controls the width of the confidence distribution. The paper states λ is a constant but never specifies its value or studies its sensitivity. Given that the probabilistic loss is a key novelty, a sensitivity analysis or at least a stated value is needed.

- **Depth completion pipeline details are insufficient.** The downstream experiment (Section 4.4) does not state which specific depth completion method is used, whether it is trained from scratch or uses a pre-trained model, or whether the same completion model is applied to all upsampling outputs. These details are needed for reproducibility and to rule out confounding factors.

- **No runtime or FLOPs reported.** The paper claims "minimal memory and computation time" but reports only parameter counts (1.7M). Given that WIN adds two interpolation branches and a CSM, inference time or FLOPs would substantiate this claim.

- **No statistical significance reported.** Standard deviations or confidence intervals are absent from all main tables. Given the limited test samples in KITTI, variance could be non-trivial.

### Trivial

- Figure 5 shows loss curves which are informative but do not directly prove better point cloud quality — this is a presentation choice, not a flaw in the experiments.

## Nice-to-Haves

- A geometric analysis grouped by surface orientation (ground vs. wall vs. pole) showing where HRV vs. VRV excels would provide direct evidence for the claimed complementarity, going beyond the qualitative examples in Figure 4.
- Reporting both standard and adjusted KITTI results would resolve the comparability concern without adding much experimental burden.
- The λ sensitivity analysis would strengthen the probabilistic contribution.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Methodology is structurally flawed/non-reproducible"** (Harsh Critic, Critical Issue 1): This characterization is too severe. The paper communicates the core mechanism — interpolation weights are predicted from shared range-view features, HRV interpolates d_t values, VRV interpolates z_t values, and divisions by cos v/sin v convert to range. While the description could be clearer, it is inferable and not a structural flaw. Removed per rules about downgrading overblown severity and because the paper's description, though compact, conveys the essential design.

- **"Uncertain fairness — reader cannot assess whether retrained baselines are optimal"** (Harsh Critic, Critical Issue 2, second part): The paper retrains all methods under the same setting, which ensures within-paper fairness. The concern about optimality of retrained baselines is standard for any reproduction effort and applies equally to all methods. The paper references Supplementary Material for details. Kept as the non-standard projection issue (Major), but the more general "uncertain fairness" framing is removed as it implies asymmetry that does not exist.

- **"The evaluation does not test the authors' own claim"** (Harsh Critic, Critical Issue 3, framing): The evaluation does test the claim — MAE on range images and voxel IoU are geometry-sensitive metrics, and the downstream depth completion task directly measures geometric accuracy. The request for additional metrics is valid (kept as Minor), but the claim that the evaluation does not test the paper's own claims is incorrect. Softened.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the paper itself does not already articulate clearly.

## Suggestions

1. **Provide explicit forward/inverse projection equations** for HRV and VRV in the methodology section (or supplementary), clarifying how 3D points map to each virtual view and how interpolated values are converted back.
2. **Report results under both the standard KITTI projection and the adjusted projection** side-by-side, or provide a more detailed justification for the adjustment that addresses why the standard protocol is unsuitable.
3. **Add a point-level geometric metric** (Chamfer distance or point-to-mesh distance) on CARLA, where clean ground truth is available, to directly support the geometric accuracy claim.
4. **Report λ value and include a sensitivity analysis** over a reasonable range.
5. **Add runtime/FLOPs inference** and **statistical significance** (standard deviations across multiple runs or test splits) to the main tables.
6. **Specify the downstream depth completion method** (which specific model, training protocol, whether shared across all upsampling outputs) in the main text.

## Score and Decision

**Score: 6.5 / 10**

The paper proposes a well-motivated and clever idea — decoupling the range view into two orthogonal views for LiDAR upsampling — and supports it with consistent experimental improvements across multiple settings. The CSM with probabilistic loss is a genuine methodological contribution. The weaknesses are addressable: the primary concern is the non-standard KITTI projection, which limits comparability with prior work but does not invalidate within-paper comparisons. The clarity gaps in the methodology description are minor and fixable. The addition of geometric metrics and efficiency numbers would further strengthen an already solid submission.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>