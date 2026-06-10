## Summary

This paper adapts Evidential Deep Learning (EDL) to BEV-based 3D object detection by replacing the standard heatmap head with one that outputs Beta distribution parameters (α, β) per class per BEV cell, enabling single-pass uncertainty estimates. A custom loss function (Eq. 3) combines EDL's Bayes risk with GFL-style weighting factors and a spatial discounting term to address class imbalance. The method is evaluated on three downstream tasks (OOD detection, bounding-box quality assessment, missed-object detection) and an auto-labeling pipeline across two architectures and two sensor configurations.

## Strengths

- **Sampling-free uncertainty at BEV level with low overhead**: The method requires only a single forward pass (versus 5 passes for MC-Dropout, Deep Ensembles, etc.) while matching or exceeding sampling-based methods on downstream tasks. This is a genuine practical advantage for real-time autonomous driving applications.

- **Novel EDL loss adapted to 3D detection's class imbalance**: Equation (3) integrates GFL-style modulation $(1 - \alpha/(\alpha+\beta))^\gamma$ and spatial discounting $(1-\hat{y})^\eta$ into the EDL Bayes risk. This addresses a real problem: vanilla EDL loss fails on detection tasks due to the extreme foreground-background imbalance, and the proposed modifications are well-motivated.

- **Comprehensive baseline comparison**: The paper evaluates against 6 uncertainty baselines (Entropy, MC-Dropout, Deep Ensembles, BatchEnsemble, Masksembles, Packed-Ensembles) across 2 architectures (FocalFormer3D, DeformFormer3D) and 2 sensor configurations (LiDAR-only, LiDAR+Camera), demonstrating architectural generality.

- **Uncertainty-driven auto-labeling pipeline**: Section 4.5 integrates all three uncertainty tasks into a pipeline where uncertainty scores guide human verification of pseudo-labels, showing measurable mAP/NDS improvements in a practical downstream application.

## Weaknesses

### Fatal
None.

### Major

- **Base detection performance of the EDL-modified detector is not reported**. The paper replaces the heatmap head architecture and uses a different loss function, yet never reports the mAP or NDS of the EDL model on nuScenes validation. Without this information, readers cannot assess whether the uncertainty benefits come at a cost to detection accuracy. If the EDL modification degrades base mAP from, say, 55% to 50%, the practical value of the uncertainty estimates is substantially diminished. The auto-labeling experiment reports mAP/NDS for a *downstream* detector trained with corrected labels, not for the EDL detector itself.

- **Key hyperparameters γ and η in the proposed loss (Eq. 3) are never specified**. The paper introduces two parameters that directly control the loss landscape — γ modulates the focusing factor (analogous to focal loss) and η controls the spatial discounting near object centers. Only λ = 10⁻⁴ is given (line 144). A method paper that proposes a novel loss function but omits critical hyperparameters is not reproducible on its own terms, and does not meet the standard for acceptance.

- **No variance, error bars, or multi-seed results for any experiment**. All results are reported as single points. The claimed improvements are modest (1% mAP for auto-labeling, 5–8% AUC for downstream tasks). Deep Ensembles and MC-Dropout are stochastic methods with nontrivial variance; without any measure of dispersion, the reader cannot assess whether the improvements are statistically meaningful.

### Minor

- **The missed-object detection evaluation (Sec. 4.4) does not specify how baseline uncertainty methods were incorporated** into the separately trained $\mathcal{M}^{\text{miss}}$ head. The description focuses on feeding EDL's uncertainty $\mathbf{u}_i$ along with $\mathbf{e}_i$ and $\mathbf{p}_i$ into the head. It is unclear whether the same architecture was applied to baseline methods with their respective uncertainty estimates plugged in, or whether a different procedure was used. This omission makes the comparison difficult to interpret.

- **No calibration evaluation** (expected calibration error, reliability diagrams). The paper only measures the *discriminative* quality of uncertainty (AUC for ranking tasks). For a method that claims to quantify uncertainty, calibration is at least as important as ranking quality. This is a notable gap.

- **Abstract claims "10–20% on average" improvement, but per-task numbers in the introduction are 5–8%** (8% OOD, 7% box quality, 5% missed objects). The box quality section itself says "5–10%" (line 166). The "10–20%" headline figure in the abstract does not clearly correspond to numbers stated in the body, which is misleading.

- **The min-aggregation for assigning uncertainty to a bounding box** ($u_b = \min_i \hat{u}^i_b$, Sec. 4.3) is stated without justification or ablation. Why the minimum rather than mean, max, or learned aggregation? This design choice could significantly affect results and is compared against baselines that may use different aggregation strategies.

- **Missing ablation of the standard EDL loss without GFL adaptation**. The paper claims vanilla EDL is unsuitable for detection (line 88–89) but never runs this ablation to demonstrate that the GFL weighting and spatial discounting are actually necessary.

### Trivial
None.

## Nice-to-Have

- Ablation of the $\mathcal{M}^{\text{miss}}$ head without the uncertainty input $\mathbf{u}_i$ to isolate the contribution of uncertainty features.
- Ablation of the individual loss components: removing GFL weighting, regularization, or spatial discounting separately.
- Sensitivity analysis of γ and η over a small grid.
- Near-OOD evaluation (e.g., nuScenes night vs. day) in addition to the cross-dataset (nuScenes vs. Waymo) OOD setting.

## Removed Points

These points were raised in the input reviews but are removed here with justification:

- *"Missing related work on uncertainty in object detection (e.g., Bayesian YOLO, EDL for 2D detection)"* — Removed per rule: DO NOT mention missing related works, as external sources to confirm their existence cannot be verified.
- *"CenterPoint-Voxel vs FocalFormer3D architecture confusion"* — Removed: the paper clearly states "For the LiDAR backbone, we use CenterPoint-Voxel as the feature extractor for point clouds" within the FocalFormer3D framework. This is standard and unambiguous.
- *"Independent Beta distributions instead of Dirichlet is a technical concern"* — Removed: the paper explicitly frames the problem as multi-label classification per BEV cell (Sec. 3.1), where independent Beta distributions are the standard EDL formulation. This is a deliberate modeling choice, not an error.
- *"Auto-labeling experiment uses asymmetric comparison"* — Removed: the comparison is actually conservative (Nk-U uses N−1 thousand initial labeled scenes vs. Nk-P's N thousand), so any asymmetry disadvantages the proposed method, not the baselines. A fairer baseline design is noted as a nice-to-have but not a genuine weakness.
- *"The paper does not report whether EDL degrades base detection performance... if EDL reduces mAP from 55% to 53%, the claimed uncertainty benefits come at a real cost"* — The underlying concern (missing base detection metrics) is kept as Major. The hypothetical example is removed as speculation.

## Novel Insights

The strongest insight that emerges from the reviews is that the paper's core contribution — adapting EDL to 3D detection via a specialized loss — is sensible and well-motivated, but the evaluation as presented contains an evidential gap: the EDL-modified detector's own detection performance is treated as a black box. This is compounded by the omission of two key hyperparameters (γ, η) that are introduced as part of the method's novelty. Together, these gaps mean the reader cannot determine whether the proposed loss function works as intended (maintaining detection accuracy) or reproduce it. The reviews collectively suggest that the paper's practical claim rests on an assumed premise (that the EDL head does not degrade the base detector) that is never verified.

## Suggestions

1. **Report the base mAP and NDS of the EDL-modified detector** on the nuScenes validation set alongside the original detector's numbers. This single piece of evidence would either validate the practical contribution or reveal whether the uncertainty estimates come at a cost.
2. **Specify γ and η**, and ideally include a sensitivity analysis over a small grid (e.g., γ ∈ {0.5, 1.0, 2.0}, η ∈ {1.0, 2.0, 4.0}).
3. **Add error bars** (standard deviation over ≥3 random seeds) to the main results, particularly the auto-labeling experiment where the claimed gain is only 1% mAP.
4. **Clarify the missed-object evaluation protocol** for baselines: specify whether the $\mathcal{M}^{\text{miss}}$ head was retrained for each baseline method with their uncertainty features, or whether a different procedure was used.
5. **Add calibration metrics** (expected calibration error or reliability diagrams) to characterize the quality of the uncertainty estimates beyond ranking-based AUC.
6. **Run an ablation** of (a) the standard EDL loss without GFL modifications, and (b) the min-aggregation for box uncertainty vs. other strategies.
7. **Align the abstract's "10–20%" claim** with the per-task numbers (5–8%) stated in the body.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>