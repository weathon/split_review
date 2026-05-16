Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes three strategies to improve Mamba-based networks for point cloud understanding: **SAST** (Surface-Aware Spectral Traversing), which uses eigenvectors of the Random Walk Laplacian to define an isometry-invariant token traversal order for classification; **HLT** (Hierarchical Local Traversing), which recursively partitions tokens via multiple eigenvectors for segmentation; and **TAR** (Traverse-Aware Repositioning), which restores learnable MAE tokens to their original positions rather than appending them at the end, preserving spatial order for Mamba's directional processing. The paper evaluates these methods on ModelNet40, ScanObjectNN, ShapeNetPart, and few-shot benchmarks.

## Strengths

- **Principled spectral traversal addresses a real limitation of existing point-cloud Mamba methods.** The paper correctly identifies that 3D grid-based traversals (Point-Mamba, PCM) are view-dependent and fail to capture surface adjacency. SAST replaces this with a traversal ordered by low-frequency Laplacian eigenvectors, which is theoretically isometry-invariant and better respects the underlying manifold. The ablation in Fig. 4 (left) shows that SAST with 4 eigenvectors outperforms both Point-Mamba's grid traversal and an unordered baseline, confirming the importance of the ordering principle.

- **TAR is a clean, well-validated solution to a genuine problem.** The observation that MAE's learnable token placement (append-at-end) breaks Mamba's directional sensitivity is insightful and practically motivated. The ablation (Fig. 5) provides clear, interpretable numerical evidence: 91.05% vs. 90.11% SVM accuracy on ModelNet40 with vs. without TAR, and consistent improvement in downstream fine-tuning. This is a straightforward modification with measurable impact.

- **Systematic ablation studies guide key design choices.** The paper analyzes the number of eigenvectors (Fig. 4 left), the number of nearest neighbors for graph construction (Fig. 4 right), and the individual contribution of TAR (Fig. 5). These experiments isolate the benefit of each component and provide clear evidence for why 4 eigenvectors and 20 neighbors are optimal.

- **Strong motivation and problem formulation.** The introduction clearly articulates three distinct problems with existing point-cloud Mamba methods (view dependence of grid traversal, task-specific traversal requirements, MAE-Mamba incompatibility) and maps each to a proposed solution. The methodological narrative is coherent and well-structured.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation comparing HLT vs. SAST on the segmentation task.** The paper claims HLT is superior to SAST for segmentation (Section 3.4, line 109: "While effective for classification tasks, the SAST strategy considering each eigenvector in a separate traversal may not capture the precise relationship between patches needed for segmentation") and states in the results (line 218) that "In the 'Training from pretrained' setting, we further demonstrate the effectiveness of HLT strategy compared to SAST in the segmentation task." However, Section 4.3 (Ablation Studies) contains no experiment comparing HLT vs. SAST on ShapeNetPart — it only analyzes eigenvector count and K-neighbors on the *classification* task (ScanObjectNN) and the TAR strategy. The segmentation results in Table 2 (an image in the extraction) compare against SOTA methods, but without a direct SAST vs. HLT ablation, the source of the segmentation gain is confounded: it could come from the different traversal strategy, the pretraining, or other factors. This is the most significant experimental gap in the paper. The claim is plausible and well-motivated, but it lacks direct empirical validation.

### Minor

- **No empirical validation of isometry invariance.** The paper asserts (correctly, via spectral theory) that the Laplacian-based traversal is invariant to isometric transformations, but never tests this empirically. A simple experiment rotating test shapes and measuring traversal stability or prediction variance would directly validate a core motivation for SAST. This is not fatal — the mathematical property is well-established — but given that the paper argues robustness to viewpoint as a key advantage, some empirical demonstration would strengthen the paper.

- **Computational cost analysis deferred to supplement.** The paper states that "a comprehensive analysis of the computational efficiency, runtime, and memory usage of our SAST approach is provided in the Supplementary Material" (line 138). While deferring details to the supplement is standard, SAST's per-block feature concatenation multiplies the sequence dimension by 2s (e.g., 8x for 4 eigenvectors with forward/backward traversals), which is a non-trivial increase over Point-Mamba's 2 traversals. A brief statement of relative overhead in the main paper (e.g., "SAST adds approximately X% to the forward pass time") would help readers assess the practical trade-off.

- **Variance not reported for classification results.** Tables 1 and 4 report accuracy without standard deviation or confidence intervals. The few-shot results (Table 3) report mean and std from 10 runs, which is good practice. For the main classification benchmarks, especially the "Training from scratch" settings where differences between methods can be small, variance information would aid interpretation.

- **Canonicalization edge case.** The sign-flip rule (flip if the first element is negative) is a standard but not fully robust heuristic: if the first element is zero or near-zero, the sign remains ambiguous. This is a known limitation of such approaches and unlikely to cause problems in practice, but worth acknowledging.

### Trivial

None.

## Nice-to-Haves

- **Exploring TAR under varying masking ratios or token counts.** The current analysis (Fig. 5) fixes these hyperparameters. A brief study of whether TAR's benefit is consistent across different masking ratios would further strengthen the contribution.
- **Ablation of within-segment sorting strategy in HLT.** The paper uses random sorting within HLT segments to add stochasticity. Comparing this against sorting by the first eigenvector (which the paper mentions as an alternative) would clarify whether the randomness itself contributes to performance.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing numerical results from main tables"** — The tables (1–4) appear as image placeholders in the extracted text due to PDF parsing artifacts. The original submission contains these tables with numerical values. Per the parsing-artifact rule, this is not a paper weakness.
- **"Several cited works are only tangentially relevant"** — Subjective opinion about related work breadth. The paper's related work section is descriptively adequate for positioning the contributions.
- **"The paper should include a direct comparison of traversal order as the only variable"** — The ablation already compares SAST (with eigenvector traversal) against Point-Mamba's grid traversal and an unsorted baseline, which serves this purpose.
- **"The paper claims reproduction issues"** — No such claim is made by any reviewer in a justified manner. Removed as not present in verified evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key experimental gap (missing HLT vs. SAST ablation for segmentation) and the lack of empirical isometry testing, but do not identify fundamentally new angles beyond what the paper already presents.

## Suggestions

1. **Add a direct ablation comparing HLT vs. SAST on ShapeNetPart segmentation.** This is the most impactful addition the authors could make. Show performance (mIoU) for: (a) SAST traversal on segmentation, (b) HLT traversal on segmentation, (c) HLT with random within-segment sorting vs. sorted by v^(1). This would directly validate the central claim about HLT's advantage for per-point tasks.
2. **Add a simple isometry-invariance test.** Measure the stability of the SAST traversal order (e.g., Kendall tau or edit distance between orderings) under random rotations of the input point cloud, and report how prediction variance changes compared to grid-based traversal.
3. **Include a brief computational overhead statement in the main paper.** Even one line stating, e.g., "SAST with 4 eigenvectors adds approximately X ms to each forward pass (Y% overhead over the base Mamba backbone)" would address the efficiency concern.
4. **Report standard deviations for main classification results** (Tables 1 and 4) across multiple runs, to allow assessment of whether observed improvements are statistically significant.

## Score and Decision

The paper presents three well-motivated, clearly described contributions to an important problem (token traversal in point-cloud Mamba networks). SAST's spectral approach is theoretically grounded and supported by ablations; TAR is a simple but effective fix validated with clear numbers; HLT is conceptually appealing for segmentation but lacks a direct comparison to SAST on the segmentation task. The available evidence from ablations and the prose descriptions of full-benchmark results (which appear in table images removed during parsing) is predominantly positive. The missing HLT vs. SAST ablation is the most significant gap, but it weakens rather than invalidates an otherwise solid contribution.

The paper is original in applying spectral graph theory to Mamba traversal for point clouds, the research question is well-motivated, the claims are largely supported by the available evidence (with one notable gap), and the experiments cover the standard benchmarks for this area. Writing is clear. The value to the community lies in demonstrating that spectral traversal can improve Mamba-based point cloud processing, and in identifying the MAE-Mamba token-placement problem with a practical fix.

**Score: 7.0 / Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>