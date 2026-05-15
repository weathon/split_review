Now I have a thorough understanding of the paper and have verified all reviewer claims against the text. Let me produce the final consolidated review.

## Summary

This paper proposes DM3D, a post-training weight pruning framework for 3D object detection that minimizes "detection distortion" (a weighted combination of bounding-box locality error and classification confidence error) via second-order Taylor approximation and Hessian-based layer-wise sparsity allocation. The method uses dynamic programming to allocate pruning ratios across layers and an efficient incremental Hessian update to avoid prohibitive computation. Experiments on KITTI, nuScenes, and ONCE across six detectors (PVRCNN, SECOND, CenterPoint, VoxelNeXT, Voxel R-CNN) show FLOPs reductions of 1.65×–3.89× with minimal mAP loss, and the approach is demonstrated to combine orthogonally with spatial pruning methods.

## Strengths

- **Novel distortion-minimization formulation for weight pruning.** The paper is the first to formulate weight pruning for 3D detection as an explicit Pareto optimization that jointly minimizes bounding-box localization distortion and classification confidence distortion (Eq. 4), rather than relying on spatial redundancy removal or hit-rate heuristics. This provides a principled objective for layer-wise sparsity allocation.

- **Efficient incremental Hessian computation.** The paper identifies that the incremental weight perturbation between consecutive pruning ratios is sparse, allowing an update rule (Eq. 14) that reduces Hessian-related complexity from \(O(N K D_i^4)\) to approximately \(O(\frac{1}{2}\sum_i D_i^2)\). This makes second-order pruning feasible for 3D detection models with large parameter counts.

- **Strong empirical results against spatial baselines across diverse settings.** DM3D achieves 3.89× FLOPs reduction on CenterPoint (ONCE) without mAP loss (Tab. 1), improves mAP by 2% on PVRCNN (Tab. 1), and obtains less performance drop than Ada3D at equivalent reduction levels on nuScenes (Tab. 2). The evaluation spans six detectors and three datasets, which is comprehensive for this domain.

- **Clear orthogonality and complementarity with spatial pruning.** Section 5.4 and Tab. 7 show that DM3D applied on top of SPSS-Conv (which already prunes 50% of voxels) further reduces FLOPs by 50.66% with only 0.30 mAP drop, boosting the overall speedup from 1.36× to 1.97×. This validates the plug-and-play claim and suggests practical value when combined with existing spatial pruning pipelines.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against weight pruning baselines.** The paper compares exclusively against spatial/voxel pruning methods (Multi et al. 2023, Ada3D Zhao et al. 2023, SPSS-Conv Liu et al. 2022a). Since the paper's contribution is a *weight* pruning method, the experiments must include standard weight pruning baselines — magnitude pruning, first-order Taylor pruning, random pruning, or other Hessian-based approaches (e.g., Optimal Brain Surgeon) applied to the same 3D detection models. Without this control, the claim that DM3D is "parameter-efficient and lossless" or superior to alternative weight pruning schemes is unsubstantiated. The existing comparisons against spatial methods only show that weight pruning can complement spatial pruning; they do not establish that the proposed distortion-minimization formulation outperforms simpler weight-only approaches.

- **Mathematical derivation of the distortion approximation is imprecise.** The paper attempts a second-order Taylor expansion of the *vector-valued* detection output \(\boldsymbol{y}\) (Eq. 6) and writes \(\boldsymbol{y} - \tilde{\boldsymbol{y}} = \sum_i \frac{1}{2}\Delta W^{(i)\top} H_i \Delta W^{(i)}\) as if \(H_i\) is a single matrix producing a scalar. For a vector-valued function, the second-order term involves a 3D Hessian tensor (a matrix per output dimension). The subsequent manipulation (Eq. 7→Eq. 9) also treats \(\frac{1}{2}\Delta W^\top H_i \Delta W\) as a scalar inside the norm with \(\lambda^\top\), without defining the dimensionality consistently. The intended correct derivation would expand the scalar \(\lambda^\top \boldsymbol{y}\) (a scalar function of weights), giving a proper matrix Hessian. The notation as written is mathematically unsupportable, though the empirical validation in Tab. 5 suggests the approximation works in practice. The derivation must be rewritten with proper rigor.

### Minor

- **"Linear time complexity" claim for the DP is incorrect.** The paper states Algorithm 1 runs with "linear time complexity relative to model parameter size" (line 131) and the conclusion repeats "linear complexity for layerwise sparsity search." However, the DP in Algorithm 1 loops over \(i\) (1 to \(l\)) and \(j\) (0 to \(T\)) with an inner minimization over \(k\) from 1 to \(j\), yielding \(O(l \cdot T^2)\) — quadratic in the number of weights to prune, not linear. The separate claim of "polynomial time complexity" is technically true but vacuous and does not correct the misstatement. The complexity analysis should be corrected.

- **"Lossless" claim insufficiently substantiated given fine-tuning.** The abstract claims "1.65× reduction **losslessly**" and "lossless 3D object detection" appears in the title. However, the paper performs post-pruning fine-tuning ("one round of finetuning," line 162). No comparison is shown between the pruned model *before* and *after* fine-tuning, making it impossible to determine how much of the recovery is due to the distortion-minimization objective versus the fine-tuning step itself. Fine-tuning is standard practice, but the "lossless" label should be qualified or accompanied by pre-fine-tuning results.

- **Key experimental details are not reported.** The paper does not specify the calibration set size \(N\), the Hessian dampening constant \(\kappa\), the fine-tuning hyperparameters (learning rate, number of epochs, optimizer), or the hardware used. The reproducibility statement is truncated by a parser artifact ("We pay attention to the reproducibility of this work.2.1)") and provides no specifics. These details are necessary for the community to build on this work.

- **First-order term discarded without justification specific to the output vector.** The paper discards the first-order Taylor term citing prior studies (line 85), but those studies justified the negligibility of first-order terms for the *loss* at a local minimum, not for the *output vector* \(\boldsymbol{y}\) directly. The gradient of \(\boldsymbol{y}\) w.r.t. weights is not zero at a minimum of the loss. While the paper uses first-order terms for intra-layer ranking (Sec. 3) and second-order for inter-layer allocation, the justification for discarding them in Eq. 6 needs to be argued specifically for the detection output.

- **Ablation on \(K\) (pruning granularity) shows a counterintuitive trend left unexplained.** Fig. 2 shows that detection scores drop slightly as \(K\) (the number of pruning steps / granularity) increases. Finer granularity should enable better allocation and produce at least equal results. This trend is not explained — possible causes (e.g., approximation error accumulation, optimization landscape) should be discussed.

### Trivial
None.

## Nice-to-Haves

- Wall-clock runtime of the Hessian computation and DP optimization would strengthen the efficiency claims beyond FLOPs arithmetic.
- Empirical validation of the assumption \(d_{i,k} \approx D_i/K\) used in the complexity analysis (Sec. 4.4).
- Variance statistics across multiple pruning runs or seeds to confirm that reported improvements are not noise.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about reproducibility statement being "incomplete ('We pay attention to the reproducibility of this work.2.1)')"** — The truncated fragment ending with "2.1)" is a parser artifact, not the original text. However, the underlying point (missing hyperparameters and experimental details) is retained as a Minor weakness above.
- **Criticism about Tables being "poorly formatted by the parser"** — Parser artifact, removed.
- **"First work" claim being too strong because He et al. (2022) prunes weights in 3D networks"** — He et al. works on 3D *segmentation*, not detection; the paper's qualifier "for 3D detection models in a distortion-minimized manner" narrows the claim sufficiently.
- **Criticism about "no comparison is shown between the pruned model before and after fine-tuning" being presented as a fatal flaw** — This is a valid Minor concern but not a fatal omission; fine-tuning after pruning is standard practice and many pruning papers do not show pre-fine-tuning numbers. Moved to Minor tier.
- **Strength Finder's claim that "Algorithm 1 runs in linear time w.r.t. total parameters"** — Conflicts with verified analysis showing quadratic complexity (see Minor weakness above).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's ambitious theoretical framing (second-order distortion minimization) and the incomplete experimental validation (missing weight pruning baselines, imprecise derivation). An interesting observation is that the incremental Hessian update (Eq. 14) leverages a form of "pruning incremental sparsity" that could generalize to other second-order pruning methods beyond 3D detection.

## Suggestions

1. **Fix the mathematical derivation.** Rewrite Sec. 4.2 by defining the scalar \(s(W) = \lambda^\top \boldsymbol{y}(W)\) and expanding \(s\) directly via second-order Taylor expansion (giving a proper matrix Hessian for each layer). This cleans up the notation and resolves the vector vs. scalar confusion without changing the actual algorithm.

2. **Add weight pruning baselines.** Compare against magnitude pruning, first-order Taylor pruning (using the loss gradient), and random pruning — each with the same layer-wise sparsity allocator (uniform or per-layer). Even if DM3D outperforms these, the comparison is essential to validate the distortion-minimization formulation.

3. **Correct the complexity analysis of Algorithm 1.** Replace the "linear time" claim with the correct \(O(l \cdot T^2)\) analysis, or clarify that linearity holds only under additional constraints (e.g., if \(T\) is treated as constant per layer rather than total).

4. **Report pre-fine-tuning performance** for at least one model/dataset to substantiate the "lossless" claim and isolate the pruning objective's contribution from fine-tuning recovery.

5. **Provide missing experimental details** (calibration set size \(N\), damping constant \(\kappa\), fine-tuning hyperparameters, hardware) in the main paper or supplement.

6. **Discuss the counterintuitive trend in Fig. 2** (performance drops with finer granularity \(K\)) — is this due to Hessian approximation drift, optimization landscape effects, or experimental noise?

## Score and Decision

The paper tackles a well-motivated and practically relevant problem — weight pruning for 3D object detection — with a novel distortion-minimization formulation and efficient Hessian approximation. The empirical results against spatial pruning methods and the orthogonality demonstration are valuable. However, the paper has two major weaknesses that prevent acceptance in its current form: (1) the mathematical derivation of the core objective is imprecisely handled and needs proper vector-valued or scalarized Taylor expansion, and (2) the experimental evaluation omits any weight pruning baselines, making the claimed "superiority" as a weight pruning method unsubstantiated. These issues are addressable through revision but are substantial. The incorrect complexity analysis, unqualified "lossless" claim, and missing experimental details further weaken the paper.

**Originality:** High — the distortion-minimization Pareto formulation for 3D detection weight pruning is novel.
**Importance of research question:** High — model compression for 3D detection is practically urgent.
**Claims support:** Low — claims about superiority over weight pruning alternatives are untested; the "lossless" and "linear complexity" claims are not adequately supported.
**Soundness of experiments:** Fair — evaluation is broad (6 models × 3 datasets) but lacks the critical baselines needed to validate the core contribution.
**Clarity of writing:** Fair — the derivation is unclear and mathematically imprecise; the experimental section lacks important details.
**Value to the community:** Moderate — the formulation and Hessian approximation techniques are useful, but the paper needs revision before these can be reliably adopted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>