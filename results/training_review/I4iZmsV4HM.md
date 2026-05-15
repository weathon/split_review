Now I have thoroughly verified the paper content against the reviewer claims. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper studies model inversion attacks on voxel-based 3D point cloud feature extractors. It identifies two key challenges unique to 3D: (1) semantic ambiguity of zero-padded voxels (empty vs. points at the origin), and (2) exponential dispersion of non-empty voxels (VoI) across downsampling layers. The proposed ConcreTizer addresses these via Voxel Occupancy Classification (VOC, converting regression to binary occupancy classification) and Dispersion-Controlled Supervision (DCS, partitioning the feature extractor at downsampling layers and training inversion blocks with intermediate masking).

## Strengths
- **First systematic analysis of inversion challenges specific to 3D point cloud data (Section 3, Figure 3).** The paper identifies two non-obvious failure modes: zero-padded voxels being mistaken for valid points at the origin, and VoI dispersion during downsampling. This analysis is clear, well-visualized, and provides a principled foundation for the method.
- **ConcreTizer consistently and substantially outperforms baselines across all metrics and both datasets (Table 1).** At the deepest layer on KITTI, ConcreTizer achieves CD of 35.19 vs. 45.90 for the generative model (23.4% improvement) and F1 of 43.8 vs. 31.4 (12.4% improvement). Results are similarly strong on Waymo. The performance gap is large and consistent across all layers.
- **Restored scenes preserve meaningful task-relevant information (Table 2).** ConcreTizer's restored point clouds yield 75.4–86.7% of original 3D object detection AP on KITTI and 62.6–75.7% on Waymo, while the generative model collapses on Waymo and point regression produces unusable output. This demonstrates that the restoration goes beyond visual plausibility.
- **Ablation study cleanly isolates each component's contribution (Figure 7).** Switching from regression to VOC (BCE) enables basic restoration; adding Focal loss helps with label imbalance; only DCS prevents point clustering at deep layers. The step-by-step progression makes the design choices transparent and validated.
- **Defense analysis provides a balanced view of the privacy-utility trade-off (Section 5.6, Table 3, Figure 9).** The paper quantitatively shows that common perturbation defenses (rotation, scaling, sampling, Gaussian noise) degrade both restoration quality and detection accuracy, highlighting the challenge of defending against this attack without crippling utility.

## Weaknesses

### Fatal
None. The paper's core technical claims are supported by the evidence presented.

### Major
- **Limited generative baseline.** Only one generative model (UltraLiDAR, adapted by modifying its encoder) is compared against. The paper provides no details about hyperparameter tuning, training duration, or convergence criteria for this adaptation. Given that UltraLiDAR was designed for unconditional LiDAR generation, its adaptation to conditional inversion may not be well-optimized. The large gap (23.4% in CD) could partly reflect insufficient adaptation effort rather than a fundamental limitation of generative approaches. An additional simple baseline—e.g., a symmetric upsampling network with regression-only and post-processing to remove origin-clustered points—would help isolate the benefit of VOC and DCS over a thoughtfully designed non-classification alternative.

### Minor
- **Privacy framing overreaches the evaluation.** The introduction motivates the work with specific privacy risks (facial recognition, person re-identification, activity inference, location identification via SLAM), and the abstract states the attack "raise[s] serious privacy concerns." However, the evaluation measures only point cloud similarity and 3D object detection accuracy. No experiment tests whether any of the invoked privacy risks (re-identification, activity recognition, license plate reading) actually materialize from restored point clouds. While standard in model inversion papers to evaluate restoration fidelity and downstream task accuracy, the paper's language implies a stronger privacy validation than what is provided. The paper would benefit from either (a) a concrete re-identification or classification experiment on restored data, or (b) tempering the privacy claims to match the scope of the evaluation (e.g., "raises concerns about the feasibility of privacy attacks on 3D features" rather than claiming specific privacy risks are realized).
- **Architectural generality is not demonstrated.** Only two backbones are tested (VoxelBackbone, VoxelResBackbone), both from OpenPCDet with similar voxelization strategies and downsampling patterns. The paper claims "general applicability to representative 3D feature extractors" but does not test on architectures with different voxel resolutions, different downsampling ratios, or alternative voxelization approaches. This limits the evidence for robustness across the full range of deployed 3D backbones.
- **DCS training procedure is under-specified.** The paper states DCS "trains each segment individually" (line 28), but does not clarify whether blocks are trained sequentially or independently with frozen predecessors. If sequential, error propagation across blocks could be significant; the partitioning analysis (Figure 8) shows performance degradation with 10 DCS blocks, but the mechanism (error accumulation vs. something else) is not analyzed quantitatively.

### Trivial
- The role of channel regression (L2 loss) in intermediate DCS blocks is briefly explained ("normalization is applied, so both classification and regression on the channel values are required") but could be clarified further—specifically why the masked feature values cannot simply be set to a fixed value derived from the occupancy classification.

## Nice-to-Haves
- A per-block error accumulation plot (CD and F1 for the 4-DCS configuration across all blocks) to quantify how restoration degrades with depth.
- Hyperparameter sensitivity analysis for SF loss parameters (α, γ) and the regression weight β.
- Failure case analysis: example scenes where ConcreTizer struggles (distant objects, extreme sparsity, occlusion), to inform future work on limitations.
- A simple tailored defense that exploits the same zero-padding insight (e.g., controlled noise in empty voxel regions only) would complete the attack-defense analysis.
- Extending the method to non-voxel representations (projection-based, point-set) is noted as future work but would broaden the impact.

## Removed Points
- **"Voxel sizes in KITTI are ~0.1m, which cannot support facial recognition or license plate reading"** — The paper does not specify exact voxel sizes, and this claim introduces external assumptions not verifiable from the paper's content. Removed.
- **"Missing experiments: PointPillars baseline"** — The paper explicitly scopes its contribution to voxel-based feature extractors. PointPillars uses 2D pillars, not 3D voxels, making this a scope-creep request. Removed.
- **"Error propagation analysis needed"** — Already listed as a Nice-to-Have above; the harsh critic's version was too demanding for a paper of this length. Moved.
- **"Missing appendix, missing proofs in appendix, absent references"** — The parser strips these sections; they exist in the original submission. Removed.
- **Various formatting/typo nitpicks** — Parser artifacts, not author errors. Removed.
- **"Impact of voxel size on restoration fidelity"** — Reasonable suggestion but not a core weakness; moved to Nice-to-Haves.
- **Strength Finder point about "privacy-compromising data"** — The strength about detection accuracy being evidence of privacy-compromising data slightly overclaims; the detection accuracy demonstrates task utility preservation, which is strong evidence of restoration quality but the direct privacy link is the same overclaim identified in weaknesses. Kept as evidence of restoration quality but removed the privacy-compromising characterization.

## Novel Insights
The reviews reveal an interesting tension: the harsh critic identifies a gap between the privacy motivation and the actual evaluation, while the strength finder correctly notes that detection accuracy preservation is strong evidence of restoration fidelity. The deeper insight here is that for 3D point cloud inversion—unlike 2D image inversion where visual recognizability alone is the standard—the "right" evaluation for privacy is genuinely ambiguous. Point cloud resolution (governed by voxel size) may inherently limit certain privacy threats (e.g., facial recognition) while enabling others (vehicle re-identification, scene classification, location inference). The paper's evaluation falls in a middle ground: it shows the attack recovers task-relevant structure without proving specific privacy harms, which is standard for the literature but leaves the practical threat level unclear. The community may benefit from establishing a concrete privacy benchmark for 3D inversion attacks that goes beyond reconstruction metrics and downstream task accuracy.

## Suggestions
- **Reconcile the privacy framing with the evaluation.** Either add a concrete privacy experiment (e.g., re-identification of vehicles/pedestrians from restored clouds, or scene-level location matching) or recalibrate the claims in the abstract/introduction to match the reconstruction-focused evaluation. The latter is simpler and does not diminish the technical contribution.
- **Strengthen the baseline comparison.** Add a simple but well-tuned regression baseline that uses the same symmetric architecture as ConcreTizer but replaces VOC/DCS with regression + post-processing. This would directly isolate the benefit of the proposed components and address concerns about insufficient comparison.
- **Clarify the DCS training protocol.** Specify whether blocks are trained sequentially (with earlier blocks frozen during later block training) or jointly, and discuss how error propagation is (or is not) managed.

## Score and Decision

The paper makes a clearly identified, technically sound contribution to an underexplored problem. The core ideas (VOC and DCS) are well-motivated by the analysis, the experiments are rigorous on two large-scale datasets, and the results are strong. The main issues are overclaimed privacy framing and a thin baseline comparison, neither of which invalidates the technical contribution. These are addressable in revision.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>