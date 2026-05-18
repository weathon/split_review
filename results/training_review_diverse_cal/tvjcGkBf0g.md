Now I have all the information needed. Let me compose the final consolidated review.

## Summary

DM3D proposes a post-training weight pruning framework for 3D object detection, formulating pruning as a distortion-minimization problem (balancing bounding-box locality and classification confidence) via second-order Taylor expansion and Hessian-based layer-wise sparsity allocation solved by dynamic programming. Experiments span 6 models across 3 datasets (KITTI, nuScenes, ONCE) and demonstrate substantial FLOPs reductions (e.g., 3.89× on CenterPoint/ONCE) with minimal or no accuracy loss, and compatibility with spatial pruning methods.

## Strengths

1. **Principled formulation grounded in distortion minimization.** The paper explicitly frames pruning as a Pareto optimization over both detection locality and confidence distortion (Eq. 4), using Hessian-based second-order Taylor approximation (Eq. 5–10). This goes beyond the hit-rate or magnitude heuristics used in prior 3D pruning work (He et al. 2022, Zhao et al. 2021) and provides a clear objective to minimize.

2. **Strong empirical results with large FLOPs reductions across diverse settings.** On CenterPoint, DM3D achieves 3.89× FLOPs reduction on ONCE while matching/outperforming the dense model; on PVRCNN on ONCE, a 1.65× lossless reduction is demonstrated. Gains generalize across architectures (PVRCNN, SECOND, CenterPoint, VoxelNeXT, Voxel R-CNN) and datasets, consistently matching or exceeding spatial-sparsity baselines (Multi, Ada3D, SPSS-Conv).

3. **Orthogonality and composability with spatial pruning.** Table 7 shows that DM3D can be stacked on top of SPSS-Conv: speedup increases from 1.36× to 1.97× on KITTI with negligible AP loss, confirming that weight pruning fills a complementary role to voxel-level sparsification.

4. **Empirical validation of the Hessian approximation.** Table 5 compares the proposed second-order distortion estimate against the true network-output distortion on the calibration set and finds no significant difference (e.g., Car Mod. 81.07 vs. 81.08), supporting the fidelity of the core approximation.

5. **Robustness to the Lagrangian multiplier \(\lambda\).** Table 6 ablates \(\lambda\) across a wide range (0.5 to 4) with negligible impact, and the paper fixes \(\lambda=[1,1]^\top\) for all experiments — a useful property for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparisons against weight pruning baselines.** The experimental comparison is almost entirely against *spatial sparsity* methods (Multi, Ada3D, SPSS-Conv). The only weight pruning baseline discussed (He et al. 2022) targets 3D segmentation and is never evaluated. Meanwhile, the paper mentions Zhao et al. (2021) — a weight pruning method for 3D detection — in the related work but does not compare against it. Without baselines such as global magnitude pruning (Han et al. 2015), uniform-per-layer first-order Taylor pruning (Molchanov et al. 2019), or the layerwise allocation from Zhao et al. (2021), it is impossible to determine whether the Hessian-based distortion-minimization formulation provides a meaningful advantage over simpler schemes. This gap weakens the paper's claim of "state-of-the-art" among weight pruning approaches. *(Note: the paper's comparison against spatial sparsity SOTA is valid for showing that weight pruning outperforms voxel pruning; the gap is in isolating the *weight pruning methodology* itself.)*

2. **Critical i.i.d. perturbation assumption (Assumption 1) is unvalidated.** The reduction from Eq. 6 to Eq. 9 — which decomposes the objective into independent per-layer terms and makes DP feasible — rests entirely on Assumption 1 (zero covariance of weight perturbations across layers). This is a strong claim: pruning one layer alters downstream gradients, creating correlations. The paper provides no empirical check (e.g., measuring the magnitude of the cross-terms in Eq. 6 relative to the diagonal terms), no sensitivity analysis, and no theoretical justification beyond citing Zhou et al. (2018). While Table 5 validates the *overall second-order approximation* against true distortion, it does not isolate the independence assumption. If cross-terms are nontrivial, the DP allocates sparsity according to a proxy that may diverge from the true objective.

3. **Unexplained performance gains on the ONCE dataset.** On ONCE with PVRCNN, DM3D raises mAP from 68.81 to 70.69 (+1.88) while simultaneously reducing FLOPs by 1.65×. Such a large accuracy improvement under compression is unusual and is described but not analyzed. The paper does not investigate whether the dense baseline is undertrained, whether pruning acts as a regularizer, or whether calibration set selection introduces bias. Without a plausible explanation, it is difficult to distinguish between a genuine discovery of redundant parameters and an artifact of the experimental setup. This directly affects confidence in the "lossless" framing.

### Minor

1. **DP complexity claim is imprecisely stated.** Algorithm 1 is described as having "linear time complexity relative to model parameter size" (line 131). As written, the algorithm loops over \(i \in [1,l]\) and \(j \in [0,T]\) with an inner minimization over \(k \in [1,j]\), which is \(O(l \cdot T^2)\). The paper later adopts \(K=1000\) discrete pruning ratios per layer (Section 5.3), making the DP \(O(l \cdot K^2)\) — essentially linear in layers with \(K\) constant, which matches the paper's intent. However, this transition from \(T\) (total weights) to \(K\) (discrete steps) is not clearly signaled in Algorithm 1 or its description, creating unnecessary confusion that the reviewer correctly flagged. A precise statement of complexity and a clean notation distinguishing \(T\) from \(K\) are needed.

2. **Incremental Hessian update notation is hard to follow.** The derivation in Section 4.4 introducing \(\operatorname{sp}(\sigma_{i,k})\), \(H_i'\), and the update rule (Eq. 14) uses notation that is not fully concretized (e.g., the figure referenced to illustrate the update appears to be missing, and the indexing of submatrices is ambiguous). Reproducing this computation from the description alone would require significant guesswork.

3. **No wall-clock latency measurements.** The paper reports FLOPs reductions but provides no actual inference latency benchmarks. For unstructured weight pruning, FLOPs counts do not directly translate to speedups on standard hardware without specialized sparse kernels. While this does not invalidate the contribution, a single latency benchmark or a discussion of the practical speedup barrier would significantly strengthen the practical relevance claims.

### Trivial
- The paper says "linear time complexity" in one place (line 131) and "polynomial time complexity" in another (line 25, line 221) for the overall approach — these should be harmonized.

## Nice-to-Haves
- **Oracle-based layerwise allocation comparison.** A small-scale experiment (e.g., on KITTI) comparing the DP allocation against the oracle allocation that minimizes true distortion (by exhaustively evaluating sparsity configurations on a held-out set) would strongly validate the optimization.
- **Per-component sparsity levels.** Table 4 reports FLOPs reductions from pruning different components (3D backbone, 2D backbone, head) but does not report the achieved sparsity percentages. Reporting the percentage of zeros per component would give insight into where redundancy concentrates.
- **Ablation:** Compare the full method against a variant using the same DP framework but with magnitude-based scores instead of Hessian-based scores, to isolate the benefit of the Hessian.

## Removed Points

- **Criticism about Hessian of head outputs w.r.t. backbone weights being non-obvious:** This is standard backpropagation and does not represent a weakness. The gradient \(\nabla_W y\) is well-defined via the chain rule regardless of which module's output is used as the objective.
- **Claim that the method is compared against the wrong class of methods:** The paper's main comparison is against spatial sparsity SOTA, which is appropriate for establishing where weight pruning stands in 3D detection compression. The missing weight pruning baselines (kept as a Major weakness) are a separate issue.
- **Generic or infeasible asks from the harsh critic:** Full human studies, pretraining from scratch, and multi-seed runs at $100k+ cost per experiment are not standard asks for this class of paper.

## Novel Insights

Beyond the paper's own contributions, the cross-review analysis surfaces two observations. First, the unexplained accuracy gains under compression (ONCE/PVRCNN) may point to a broader phenomenon in 3D detection: the dense model's capacity may be under-utilized due to the highly imbalanced nature of LiDAR data (many empty voxels, a few informative foreground points), and pruning could be implicitly regularizing the model away from overfitting to sparse foreground patterns. Second, the tension between the i.i.d. assumption (Assumption 1) and the overall empirical success is worth deeper investigation — if the cross-layer correlations turn out to be small in practice for 3D detection backbones (which are often shallow compared to image classifiers), the field would benefit from understanding *why* the independence assumption holds better than expected.

## Suggestions

1. **Add weight pruning baselines.** At minimum: global magnitude pruning, uniform-per-layer Taylor pruning, and the Bayesian-optimization-based method from Zhao et al. (2021). Run on one dataset (e.g., KITTI) to isolate the benefit of the Hessian-based allocation.
2. **Empirically validate Assumption 1.** On a small model (e.g., SECOND on KITTI), compute the full cross-layer terms in Eq. 6 and report the ratio of cross-term magnitude to diagonal-term magnitude. If small, the assumption is supported; if not, discuss the implications for the DP solution.
3. **Investigate the ONCE performance gains.** Run the dense model through the same fine-tuning procedure without pruning to check if the improvement persists. Report per-class AP to see if gains concentrate on certain categories.
4. **Clarify the DP complexity.** Rename the input \(T\) in Algorithm 1 to \(K\) (number of discrete pruning steps), state the complexity as \(O(l \cdot K^2)\), and explicitly note that \(K=1000\) is used (already mentioned in Section 5.3 but needs to be linked back to the algorithm).
5. **Improve notation in Section 4.4.** Provide a clear small example or a diagram of the subvector/submatrix indexing to make the incremental Hessian update reproducible.
6. **Add a latency benchmark** on at least one hardware configuration, even if using an off-the-shelf sparse inference library, to ground the FLOPs claims in practical speed.

## Score and Decision

The paper introduces a principled weight pruning framework for 3D detection, backed by extensive experiments across diverse models and datasets. The core ideas (distortion-minimization formulation, Hessian-based DP allocation, orthogonality to spatial pruning) are novel and practically relevant. However, three major weaknesses — missing weight pruning baselines, an unvalidated theoretical assumption, and unexplained accuracy gains — prevent the paper from fully substantiating its claims in its current form. These are all addressable with additional experiments and analysis. I recommend acceptance conditional on the authors addressing these gaps in a revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>