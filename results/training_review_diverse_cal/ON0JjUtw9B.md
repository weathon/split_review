Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

WIN proposes a LiDAR upsampling method that decouples the range image into two geometric components—horizon-range (interpolating horizontal distance \(d\)) and vertical-range (interpolating vertical coordinate \(z\))—and fuses them via a probabilistic contrast selection module (CSM) that predicts per-point view confidence. The method is built on the implicit-function interpolation paradigm (ILN/LIIF) and adds only 0.4M parameters over ILN. Experiments on CARLA and KITTI show consistent MAE and IoU improvements over prior work, with gains growing at higher upsampling scales.

## Strengths

1. **Novel decoupling of range-view interpolation into complementary geometric components.** The paper is the first to recognize that interpolating different geometric quantities (\(d = \sqrt{x^2+y^2}\) vs. \(z\)) in the same image grid yields different behaviors for different surface orientations (vertical surfaces vs. flat ground). The ablation study (Table 4) confirms that this variable-view design alone significantly improves over the single-view baseline (ILN). This is a principled and lightweight idea.

2. **Probabilistic contrast selection module with a well-motivated loss.** Instead of forcing a binary "which view is better" classification, the CSM models view confidence as a Gaussian-derived probability and uses a margin-based loss (Eq. 10) that focuses training on regions where the two views disagree. Table 4 shows CSM improves MAE by ~2.4% and IoU by ~2.9% over either single view, and Figure 5 demonstrates that the proposed loss converges stably while binary cross-entropy diverges.

3. **State-of-the-art results with minimal parameter overhead.** On CARLA, WIN achieves +4.53% MAE and +7.01% IoU over ILN while adding only 0.4M parameters (1.7M total). The improvement is consistent across upsampling scales (4× to 16×, Table 2) and holds on real-world KITTI data for IoU. The method's margin over prior work grows with resolution, demonstrating the value of decoupled views at high scales.

4. **Flexibility for arbitrary upsampling scales.** As an implicit-function method, WIN can upsample to any factor with a single trained model. Table 2 shows this is not a hypothetical advantage—the method delivers at all tested scales.

5. **Clean ablation isolating each contribution.** Table 4 systematically ablates (i) the variable-view module alone, (ii) CSM alone, (iii) full WIN, and (iv) the probabilistic loss vs. binary cross-entropy. Each component is shown to contribute positively, and the design choices are empirically justified.

## Weaknesses

### Fatal
None.

### Major

1. **The downstream depth-completion experiment is critically underspecified.** Section 4.4 states "We use the reconstructed point cloud for depth completion and compare it with ground truth" but never names the depth-completion architecture, its training protocol, or how the upsampled point cloud is integrated. If the authors simply re-project the upsampled points into a depth image and compute RMSE/MAE, this is not a separate downstream task—it is an alternative evaluation of the upsampling itself, and the numbers in Table 3 would largely recapitulate Table 1's range-image metrics. If a learned depth-completion model (e.g., Sparse-to-Dense, GuideNet, NLSPN) was used, it must be named and the pipeline described. As written, this experiment is neither reproducible nor interpretable as evidence that WIN "has the greatest potential for application" (line 226). This is a significant gap because the downstream task is highlighted in the abstract, contributions, and conclusion.

### Minor

1. **The "orthogonal views" terminology is conceptually imprecise.** The paper calls HRV and VRV "orthogonal views" and suggests they are different geometric projections. In reality, Eq. 3 shows that both are interpolated in the *same* range-image grid, just on different target quantities (\(d\) or \(z\)), which are then converted back to range \(r\) via \(\cos v\) or \(\sin v\). This is a target-value substitution in a fixed grid, not a re-projection to different viewports. The method is correctly and fully specified in Eq. 3 (a careful reader can follow it), but the "orthogonal views" framing conflates a geometric re-projection with interpolating different coordinate components. The conceptual overclaim does not invalidate the method, but it creates unnecessary confusion and should be corrected to describe what is actually implemented.

2. **The hyperparameter \(\lambda\) in the CSM loss (Eq. 7–9) is neither specified nor ablated.** \(\lambda\) controls the sharpness of the Gaussian-derived confidence pseudo-label \(\hat{g}\). The paper states only that "\(\lambda\) is a constant" (line 133) but gives no value, range, or sensitivity analysis. While this is unlikely to be a fatal omission—the loss likely works across a reasonable range—its absence weakens the analysis of the probabilistic modeling contribution and leaves readers unable to reproduce the exact setup.

3. **No runtime or FLOP comparison is provided despite claims of lightweight efficiency.** The paper repeatedly emphasizes that WIN has minimal parameters and computational cost (abstract, Section 5), yet provides no inference-time or FLOP comparison to support this. A single table showing ms per point cloud and parameter counts across all methods would directly substantiate this claimed advantage.

4. **Details of the modified KITTI projection are deferred to supplementary material.** The paper adjusts the KITTI projection to handle non-unique projection centers (Section 4.2) and retrains all baselines under this setting. While this is good practice, the main text defers the specifics to supplementary material. Since the resulting numbers may differ from published results, a brief summary of the modification in the main text would help the reader evaluate fairness.

### Trivial

1. Figure 4 (qualitative point cloud comparison) lacks axis labels, scale information, and a legend, making it difficult to assess geometric claims from the visualization alone.
2. Figure 5 (loss curves) has an unlabeled y-axis.

## Nice-to-Haves

- An ablation study varying \(\lambda\) to demonstrate robustness or identify an optimal setting.
- A per-region analysis quantifying where HRV vs. VRV excels (e.g., accuracy on vertical surfaces vs. ground), which would validate the motivation stated in Section 1.
- Comparison against IPN (Park et al. 2023), which is discussed in related work but not evaluated. This would strengthen the SOTA claim for the implicit-function category.

## Removed Points

- **"The HRV/VRV definition is so imprecise that the claimed advantage is not distinguishable from simply interpolating a different feature"** — This overstates the issue. While the "orthogonal views" framing is imprecise, the method is fully and correctly specified in Eq. 3, and the ablation study (Table 4) empirically validates that the decoupled interpolation provides a real benefit. The criticism is downgraded to Minor (point 1 above) because the experimental evidence clearly supports the method's advantage regardless of the conceptual framing.
- **"The resulting KITTI numbers differ from previously published results"** — This is speculation, not a verified weakness. The paper explicitly states that all methods were retrained under the same modified projection to ensure fair comparison, which is standard practice.
- **"The authors should add comparison against IPN"** — Moved to Nice-to-Haves. Not evaluating every related method is a reasonable scope decision, not a weakness.
- **"The paper should include per-region analysis of edges vs. ground"** — Moved to Nice-to-Haves. This would strengthen the analysis but is not a required experimental validation of the core claim.
- **"Figure 2: the dotted lines and red crosses in the figure indicate that the gradient is not returned here"** — This is already explained in the paper (line 158: "we interrupt the propagation of gradients at \(\mathcal{R}_d\) and \(\mathcal{R}_z\)"). The reviewer misread the caption.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the geometric description of HRV and VRV.** Replace the "orthogonal views" framing with precise language: these are interpolations of different geometric components (\(d\) vs. \(z\)) within the same range-image grid, which are then converted back to range values. A diagram explicitly showing Eq. 3's computation path (pixel → interpolate \(d\) or \(z\) → divide by \(\cos v\) or \(\sin v\) → range) would eliminate ambiguity.

2. **Fully specify the depth-completion experiment.** Name the depth-completion architecture, describe how the upsampled point cloud is fed into it, and state the training protocol. If no learned model is involved and this is simply a re-projection evaluation, rename the experiment accordingly (e.g., "Depth-map reconstruction from upsampled point clouds").

3. **Report the value of \(\lambda\)** used in experiments and ideally include a brief sensitivity analysis showing performance over a range (e.g., \(\lambda \in \{0.01, 0.05, 0.1, 0.5\}\)).

4. **Add a runtime/parameter comparison table** to substantiate the claimed lightweight efficiency.

## Score and Decision

**Originality:** Good. Decoupling the range image into separate geometric components for interpolation is a novel and well-motivated idea. The probabilistic confidence modeling for view fusion is also a non-trivial contribution.

**Importance:** The problem of LiDAR upsampling from low-cost sensors is practically relevant. The method's ability to improve geometric accuracy with minimal overhead addresses a real need.

**Claims:** The core claims (SOTA accuracy, complementary views help, CSM improves fusion) are well-supported by Tables 1, 2, and 4. The downstream-task claim is weakened by experimental underspecification.

**Soundness:** The methodology is sound. The ablations are clean. The main weakness is the underspecified depth-completion experiment, which prevents full verification of the downstream claim.

**Clarity:** The paper is generally readable, but the "orthogonal views" framing creates unnecessary confusion about what the method actually does. Key hyperparameters (\(\lambda\)) are missing. The downstream experiment description is insufficient.

**Value:** The core technical contribution—decoupled geometric interpolation with probabilistic fusion—is a lightweight, effective improvement to LiDAR upsampling that the community can build on. The weaknesses are presentation and documentation gaps, not fundamental flaws in the approach.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>