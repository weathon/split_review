- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 5, 5, 6, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes BiC-Occ, a framework for vision-based 3D occupancy prediction that addresses the sparsity and ambiguity of voxel labels through two modules: (1) a Bi-directional View Transformer (Bi-VT) that approximates invertible transition matrices for self-consistent 2D-to-3D and 3D-to-2D transformations, and (2) a Circulated Interpolation Predictor (CIP) that aligns multi-scale BEV representations using local geometric structures. The method achieves state-of-the-art results on the Occ3d-nuScenes dataset (34.1% IoU, 13.8% mIoU).

## Strengths

1. **Novel bidirectional consistency framework for view transformation**: The Bi-VT module (§3.1) proposes a conceptually interesting approach to enforce self-consistency between 2D image features and 3D BEV representations via invertible transition matrix approximation — a genuine departure from the standard unidirectional projection pipelines. This is a creative formulation of the label sparsity problem.

2. **CIP module with geometric interpolation for multi-resolution alignment**: The Circulated Interpolation Predictor (§3.2) uses Geo-Gather and Geo-Scatter scores driven by 3D convolutions to propagate geometric structure information between high- and low-resolution BEV representations. The idea of using local neighborhood geometry to correct ambiguous voxel predictions is intuitive and well-motivated.

3. **Clear problem framing and well-structured ablation**: The paper clearly identifies two specific challenges (label sparsity and ambiguity) and ties each module to one challenge. The ablation study (Table 2) shows that both Bi-VT (+3.54% IoU, +3.66% mIoU) and CIP (+3.17% IoU, +3.93% mIoU) contribute meaningfully over the baseline, with a synergistic benefit when combined (+4.29% IoU, +5.02% mIoU). Parameter analyses for α and β (Tables 3–4) show sensitivity and provide guidance for optimal settings.

4. **Competitive results on a standard benchmark**: The method achieves the best published IoU (34.1%) and mIoU (13.8%) on the Occ3d-nuScenes validation set (Table 1), outperforming prior methods including COTR and UniTR.

## Weaknesses

### Fatal

None.

### Major

1. **Numerical inconsistency between main results and ablation results for the full method**: The ablation text reports the full method (baseline + Bi-VT + CIP) achieves a +4.29% IoU and +5.02% mIoU improvement over the baseline (28.89%/12.77%), implying absolute values of ≈33.18% IoU and ≈17.79% mIoU. However, Table 1 reports the same BiC-Occ framework as achieving 34.1% IoU and **13.8% mIoU**. The mIoU values differ by ~4 percentage points (17.79 vs 13.8). This is a large, unexplained discrepancy that directly affects the credibility of the reported results. The paper must reconcile these numbers or explain why the full method in the ablation differs from the one in the main comparison.

2. **Circular dependency in the Bi-VT module formulation**: The forward projection (Eq. 5) defines `A_BEV^fore = GAP(F_BEV)` and the backward projection (Eq. 8) defines `A_BEV^back = GAP(F_BEV)`. Both require `F_BEV` as input, yet `F_BEV` is the quantity the view transformer is supposed to produce as output (Eq. 10: `F_BEV = F_img · A_inv`). The paper does not explain how this circular dependency is resolved — whether `F_BEV` is initialized via a preliminary forward pass, whether the formulation describes an iterative procedure, or whether the equations are meant to represent a different computational flow than what they state. This is a significant gap in the method description.

3. **Unvalidated Kronecker factorization assumption (Assumption 1)**: The entire Bi-VT module rests on the claim that the view-transformation transition matrix can be factorized as `A_VT = A_img ⊗ A_BEV`. The paper provides intuitive motivation ("calculating the similarity score regarding each 2D pixel and 3D voxel") but **no empirical evidence** that this specific factorization captures the true view transformation with reasonable fidelity. Modern view transformations involve camera geometry, occlusion patterns, depth distributions, and attention mechanisms — these are not separable into independent 2D and 3D factors. While the assumption is labeled as such, the paper builds a substantial apparatus (VM decomposition, T-SVD, invertibility claims) on top of it without validation. The authors should at minimum measure the approximation error of the Kronecker factorization against a known full-rank transformation, or acknowledge this as a strong architectural design choice rather than a principled derivation.

4. **Tiny SOTA margins without controlled comparison or statistical significance**: The claimed improvement over the previous best method (COTR) is 0.5% IoU and 0.1% mIoU — margins that fall well within expected noise from random seeds and training variations. No confidence intervals, standard deviations, or multi-run statistics are reported. Furthermore, the paper does not specify which image backbones the compared methods in Table 1 use, nor whether all comparisons share the same input resolution (the paper resizes to 256×704 from 900×1600, a 4.7× pixel reduction). Without controlling for these factors or demonstrating statistical significance, the SOTA claim is unconvincing.

### Minor

1. **Truncated SVD rank `k` unspecified and unablated**: The invertible refinement (§3.1) relies on a truncation threshold `k` for the SVD, which controls the rank and invertibility of the approximation. The paper neither specifies the value used nor ablates its effect. This is a critical hyperparameter that should be reported.

2. **Computational cost not reported**: The paper introduces tensor factorization, truncated SVD (with eigendecomposition in the training graph), 3D convolutions, transpose 3D convolutions, and multi-resolution alignment — all of which add overhead. No inference speed, parameter count, or FLOPs are reported for BiC-Occ or any baseline. Given the marginal metric improvements, the practical value cannot be assessed without cost-performance trade-off data.

3. **Limited hyperparameter analysis scope**: The parameter analyses (Tables 3–4) only vary α and β. The number of VM decomposition components `i`, the SVD rank `k`, and the number of interpolation scales in CIP are not ablated.

4. **3D convolution specifications missing**: The CIP module uses 3DConv and T-3DConv layers (Eqs. 11, 13), but the paper does not specify kernel sizes, number of layers, or channel dimensions.

### Trivial

None.

## Nice-to-Haves

- The authors could validate the Kronecker factorization assumption experimentally, e.g., by computing the full transition matrix for a simplified setting (e.g., LSS with known depth) and measuring the approximation error of the Kronecker decomposition.
- Reporting means and standard deviations over 3 seeds for the key comparisons would strengthen the empirical claims.
- Clarifying the gradient propagation path through the truncated SVD (which can be non-trivial) would improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Missing related works on self-supervised methods"** — The harsh critic criticizes the related work section for not discussing self-supervised or consistency-based approaches. This is a scope-creep complaint; the paper focuses on supervised occupancy prediction with self-consistency as a regularizer, not self-supervised learning. Removed per the "do not mention missing related works" rule.

2. **"Ablation baseline is undefined/unclear"** — The harsh critic claims the ablation baseline "Huang & Huang (2022)" is undefined. The paper clearly names the reference. The method is identifiable. Removed because this is factually inaccurate — the paper does specify the baseline.

3. **"The paper claims unidirectional pipelines but many recent methods use depth supervision"** — The harsh critic says the paper overstates its critique of prior methods. The paper says "mostly adopt unidirectional pipelines supervised by annotated ground truth." Methods like BEVDepth use depth supervision but still have unidirectional image→BEV flow; the critique is about the direction of the pipeline, not the supervision signal. This is a misunderstanding.

4. **Strengths removed as generic/delusional**: "Thorough ablation and parameter analyses" — kept (it's specific). "Theoretical formulation of view transformation" — the strength is that the paper provides a formal framing, which is true but the framing rests on an unvalidated assumption (already raised as weakness), so this strength conflicts with a verified weakness. Moved here per the "when strength and weakness disagree, the weakness wins" rule.

5. **Strength removed**: "Addressing an important problem" — generic; applies to most papers in the area.

6. **"Missing parts-related reproducibility concerns"** (Harsh Critic's section on reproducibility details) — The harsh critic asks for unspecified 3D convolution parameters and other implementation details. These are common to defer, and the paper provides reasonable implementation details (batch size, learning rate, optimizer, augmentation). The specific 3D conv params are absent but this is more a minor missing detail than a reproducibility crisis. Kept as minor weakness (#4 in Minor).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine numerical discrepancy between the ablation and main results that the paper's own narrative overlooks — this is worth investigating but is an error, not a novel insight.

## Suggestions

1. **Reconcile the numerical discrepancy**: Clarify why the full-method IoU and mIoU differ between the ablation (Table 2) and the main results (Table 1). If different configurations were used, state this explicitly. If this is an error, correct it.
2. **Address the circular dependency in Bi-VT**: Clearly explain how `F_BEV` is initialized or how the equations should be interpreted. Provide a pseudo-code or explicit computational graph showing the flow.
3. **Either validate or de-emphasize the Kronecker assumption**: Provide an empirical approximation-error analysis, or reframe the Kronecker structure as an architectural design choice (not a formal assumption) and remove the invertibility claims that depend on it.
4. **Report computational cost**: Add a table with inference time, parameters, and FLOPs for BiC-Occ and at least the top-3 baselines.
5. **Specify k (SVD truncation rank) and ablate it**: This is a key hyperparameter for the core module.
6. **Add controlled comparison**: Report results with a common backbone (e.g., ResNet-50) and input resolution for all methods, or clearly document the settings each baseline uses.
