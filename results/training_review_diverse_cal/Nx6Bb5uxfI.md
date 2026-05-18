Here is my final consolidated review:

## Summary

This paper proposes E3D, a two-stage training strategy for sparsely-supervised 3D object detection that leverages Large Multimodal Models (LMMs) to generate pseudo-labels. It consists of three components: a Confident Points Semantic Transfer (CPST) module that extracts semantic seed points from LMM-generated masks with a boundary-constrained shrink operation; a Dynamic Cluster Pseudo-label Generation (DCPG) module that adaptively clusters these seed points to fit bounding boxes; and a Distribution Shape (DS) score that evaluates pseudo-label quality without ground truth. The detector is first trained on these pseudo-labels, then fine-tuned on sparse annotations.

## Strengths

- **Clear problem motivation and sensible high-level direction**: Using LMMs to bridge the 2D-to-3D semantic gap under extreme annotation scarcity is a well-motivated research direction. The paper identifies a real bottleneck (insufficient feature discrimination when labels are extremely limited) and proposes a concrete strategy to address it.

- **Specific technical innovations to address known issues**: The CPST module's boundary-constrained mask shrink (Eq. 3) directly targets the projection noise problem that arises from 2D-3D calibration errors — a known issue in cross-modal label transfer. The DS score's combination of a distribution constraint and a meta-shape constraint is a novel way to rank pseudo-labels without ground-truth IoU.

- **Claimed quantitative gains under extreme sparsity**: The paper reports that E3D improves CoIn++ by an average of 11.63% under 2% annotation rates and improves CoIn by 36.92% at 0.1% and 14.89% at 2% on KITTI (Table 1). The two-stage strategy (pseudo-label pre-training + sparse fine-tuning) is a well-structured approach that is compatible with existing detectors.

- **Generalization across detector architectures**: Results with VoxelRCNN, CenterPoint, and CasA (Table 2) suggest the approach is not tied to a single detector design, which strengthens the claim of practical utility.

## Weaknesses

### Major

- **Unvalidated and underspecified core component of the DS score**: The distribution constraint score assumes distances from interior points to the bounding box boundary follow a Gaussian N(0.8, 0.2) (Section 3.4). While citing Luo et al. 2024, the paper provides **no empirical validation** that this prior holds for KITTI LiDAR point clouds. The choice of μ=0.8 and σ=0.2 is presented as given, with no justification or sensitivity analysis. Additionally, the "normalized KL divergence function" Φ_KL(·) in Eq. 6 is named but never defined — the reader cannot assess what normalization is applied or how the meta-shape templates B_c are derived (e.g., from KITTI training set statistics, which would leak information into the first stage). Since the DS score is the mechanism for filtering pseudo-labels, these gaps make it difficult to evaluate how much the method truly contributes versus the specific unvalidated priors.

- **Zero-shot claims are made but the experimental presentation is incomplete**: The abstract and contributions state that "we have verified our E3D in the zero-shot setting" and that "without fine-tuning on labeled data, our E3D has shown superior performance compared to zero-shot methods." However, the text in Section 4 describes only Table 1 (sparsely-supervised comparison at 100%, 20%, 2%) and Table 2 (fully-supervised baselines at 2%). Neither table description mentions a zero-shot evaluation or comparison against zero-shot methods. While the embedded tables are images that cannot be fully verified through text extraction, the textual framing of the experiments does not clearly support this claimed result. The paper should dedicate a specific subsection or table to the zero-shot setting with a clear definition of what "zero-shot" means here and which methods it is compared against.

- **Claimed comparison with cross-modal weakly-supervised methods is not visible in the presented experiments**: The paper states (Section 4, Baselines) that it "compared with cross-modal weakly-supervised methods (Qin et al., 2020; Liu et al., 2022b)." Neither Table 1 nor Table 2 are described as including these methods. Since the tables are embedded as images, this gap cannot be fully confirmed, but the text descriptions of the experiments do not mention these comparisons. This omission (if real) would prevent the reader from determining whether E3D's gains come from the LMM pipeline specifically or from injecting any 2D semantic information.

### Minor

- **No ablation study of the three components**: The paper does not isolate the contribution of CPST, DCPG, and the DS score. It is unclear which component drives the improvement. A simple ablation (e.g., full pipeline vs. w/o DS score, w/o DCPG) would substantially strengthen the empirical case.

- **No analysis of pseudo-label quality**: The paper reports no statistics on the pseudo-labels themselves — precision/recall against ground truth, number generated per frame, number filtered by the DS score, or quality distribution. The mechanism of improvement remains a black box without this analysis.

- **Non-standard DBSCAN usage without discussion**: DCPG's dynamic radius (Eq. 4) assigns a per-seed-point clustering radius that increases linearly with the seed point index within an instance. DBSCAN typically uses a fixed ε per cluster; applying a varying ε within a single cluster during clustering is non-standard and could produce inconsistent cluster membership. The paper does not discuss this design choice or its implications.

### Trivial

- **Naming inconsistency**: The figure caption (Fig. 3, line 67) and line 79 refer to "CSPT" instead of "CPST" (Confident Points Semantic Transfer). This is a consistent typo in the figure that should be corrected.

- **Meta-shape template source not defined**: The paper mentions B_c as the meta-shape for each category but does not explain how these values are obtained — whether from KITTI statistics or external data. This should be clarified even if briefly.

## Nice-to-Haves

- A comparison against a simpler baseline: projecting 2D masks from a standard 2D detector (without LMM) onto point clouds and using the resulting points directly as supervision. This would disentangle the benefit of the LMM from the benefit of the pseudo-label generation pipeline.
- Hyperparameter sensitivity analysis for γ (shrink factor), r_initial, δ, and the DS score weights λ₁, λ₂. These are set to specific values (γ=0.3, r_initial=1, δ=0.1, λ₁=λ₂=0.5) without discussion of robustness.
- Qualitative visualizations of generated pseudo-labels vs. ground truth to illustrate where CPST/DCPG succeed or fail.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Numerical inconsistency claim (Harsh Critic Issue 1, sub-point)**: The reviewer claims the 14.89% improvement over CoIn at 2% does not match Table 1 values. However, the reviewer compares against CoIn++ values (AP 68.56 → 71.69), while the paper claims improvement over **CoIn** (the baseline method, not CoIn++). The abstract separately reports 11.63% improvement over CoIn++. These are different baselines and not inconsistent. This criticism reflects a misunderstanding of which method is the baseline for each claim.

- **Criticism that the 0.1% annotation rate results are absent**: The paper claims 36.92% improvement at 0.1% in the contributions. The tables are embedded as images in the text extraction; the parser may not have captured all table content. The text near Table 2 (line 168-169, though garbled) references "41.95% 36.92% higher than CoIn," suggesting 0.1% results are discussed. The reviewer's claim cannot be fully verified due to parser limitations.

- **Criticism about Gaussian support on bounded data**: The reviewer notes that distances bounded in [0, max_dist] cannot be "truly" Gaussian. This is technically correct but is a standard approximation used widely in the literature (cited from Luo et al. 2024) and does not undermine the practical utility of the approach. The real concern is the lack of empirical validation, which is already captured in the Major weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews identify specific gaps (missing validation of the DS score prior, incomplete experimental descriptions) but do not surface a fundamentally new perspective on the paper's approach or its position in the field.

## Suggestions

1. **Provide a dedicated zero-shot evaluation table** with a clear definition of the setting (e.g., no fine-tuning on any labeled data) and comparison against methods such as SAM3D.
2. **Validate the DS score's Gaussian prior on KITTI data**: compute empirical distributions of point-to-boundary distances for ground-truth boxes and show whether N(0.8, 0.2) is a reasonable fit. If not, propose a data-driven alternative.
3. **Define the "normalized KL divergence function"** and specify how meta-shape templates B_c are obtained (e.g., from KITTI training set statistics, external datasets, or canonical values). If from KITTI, discuss potential information leakage.
4. **Add an ablation study** comparing the full E3D pipeline against variants without the DS score, without DCPG, and using simpler mask projection baselines.
5. **Include pseudo-label quality statistics**: precision/recall against ground truth, number of proposals generated and retained after DS score filtering.
6. **Fix the CSPT/CPST naming inconsistency** in Figure 3.
7. **Include the comparison with cross-modal weakly-supervised methods** in the main tables, or explain why such comparison is excluded despite being claimed.

## Score and Decision

This paper addresses a relevant problem and proposes a multi-component pipeline with reasonable technical ideas. The core direction — using LMMs to generate pseudo-labels for sparsely-supervised 3D detection — is timely and well-motivated. However, the experimental presentation has significant gaps: the zero-shot results claimed in the abstract and contributions are not clearly presented in the described experiments; the DS score relies on unvalidated priors and an undefined normalization; key comparisons with cross-modal methods are claimed but not visible; and no ablation study isolates the contribution of individual components. These gaps prevent the paper from being accepted in its current form. The methodological ideas are interesting and the approach has potential, but the empirical backing is insufficient to support the stated claims. A major revision with the missing evidence would substantially strengthen the paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>