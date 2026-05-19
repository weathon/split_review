- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the information I need to produce the consolidated review. Let me synthesize everything.

## Summary

This paper proposes DDOT, a diffeomorphic mesh deformation framework for cortical surface reconstruction. Instead of the standard Chamfer distance loss (which suffers from local minima and quadratic complexity), the authors use sliced Wasserstein distance (SWD) on probability measures representing meshes, including a richer oriented varifold representation. The method is evaluated on ADNI, OASIS, and TRT datasets against DeepCSR, Vox2Cortex, CFPP, and CortexODE. The paper reports improvements in geometric accuracy, self-intersection ratio (<10⁻⁴%), and consistency.

## Strengths

- **Dimension-independent sample complexity bound (Theorem 1).** The paper proves that the Monte Carlo SWD estimation error between empirical measures on sampled point-clouds and the true SWD between continuous mesh surfaces decays as O(m⁻¹/²) + O(L⁻¹/²), where the m⁻¹/² rate does not depend exponentially on dimension. This is a strictly better rate than the standard Wasserstein convergence rate of O(m⁻¹/ᵈ) and supports the claim that SWD is scalable to meshes with high-dimensional features.

- **Consistent state-of-the-art geometric accuracy and near-zero self-intersection.** On both ADNI and OASIS (Table 1), DDOT achieves the best EMD, SWD, ASSD, and Chamfer normals across most categories, while reducing self-intersection to <10⁻⁴% — over 100× better than CortexODE (e.g., 0.013% on ADNI left WM). The ablation study (Table 4) confirms that the combination of SWD + varifold representation drives this improvement.

- **Empirically validated computational efficiency.** Figure 2 shows SWD loss scaling approximately linearly with the number of supports and consistently outperforming Chamfer distance (with or without regularization), especially for high-dimensional varifold representations. This confirms the theoretical O(m log m) time and O(m) memory complexity of SWD.

- **Ablation study isolates the contribution of each design choice.** Table 4 compares SWD on point sampling, CD on varifold, Sinkhorn on varifold, and SWD on varifold — all on the same initial surface and number of supports. SWD on varifold dominates all alternatives, providing strong internal evidence that both the metric (SWD) and the representation (varifold) matter.

- **Consistency on test-retest data.** On the TRT dataset (Table 2), DDOT achieves the best EMD and ASSD among learning-based methods (Vox2Cortex, CortexODE), demonstrating robustness to intra-subject scan variability.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled initial surface across baseline comparisons confounds cross-method results.** DDOT initializes via Marching Cubes from a predicted segmentation mask (which already approximates the target shape), while baselines such as CortexODE and CFPP typically start from a spherical template. The paper states that baselines were reproduced "using their official implementations and recommended experimental settings" (line 201), but does not specify whether the initial surface is held constant. This is especially problematic for interpreting the self-intersection (SI) results: an initial surface already close to the target will naturally yield fewer self-intersections during deformation. While the ablation study (Table 4) controls for initial surface *within* DDOT variants and convincingly shows the benefit of SWD+varifold, the cross-method headline comparisons in Table 1 conflate initialization differences with loss function differences. The authors should either run a controlled experiment with a shared initial surface or explicitly discuss the impact of different initializations.

### Minor

- **Several key metrics show overlapping standard deviations without significance testing.** On ADNI left WM, DDOT's SWD (0.420±0.273) and CortexODE's (0.436±0.403) have overlapping standard deviations; on ADNI right WM, DDOT's Chamfer normals (0.938±0.012) are slightly *below* CortexODE (0.939±0.019); on OASIS, EMD (0.418±0.192 vs 0.425±0.193) and SWD (0.779±0.055 vs 0.785±0.047) means are very close with overlapping SDs. Without paired significance tests or confidence intervals, the claim of "outperforming" on these specific metrics is not fully supported. The strongest evidence lies in ASSD and SI, where differences are larger. The paper should either report statistical significance or qualify the claims appropriately.

- **Theoretical analysis does not directly cover the varifold representation used in practice.** Theorem 1 bounds the error between SWD on i.i.d. sampled empirical measures and SWD on continuous surface measures. However, the primary loss used in the method is SWD on *oriented varifolds* — discrete measures on face barycenters and normals with area weights, which are a deterministic quadrature rather than i.i.d. samples. The paper states that "leveraging the scaling property and the approximation of varifold to mesh... we can represent meshes as discrete measures" (lines 133–134), but does not develop how Theorem 1's convergence rate carries over to the varifold case. The bound's variance term also depends on the uncharacterized quantity Var[Wₚᵖ(θ♯μ̂ₘ, θ♯ν̂ₘ)], which may itself have dimension dependence, making the claim of dimension-independent convergence partially incomplete. A brief discussion (or extension of the bound) connecting the two would substantially strengthen the paper.

- **Runtime analysis covers only loss computation, not total training or inference time per subject.** Figure 2 shows loss computation time scaling, which is useful, but practitioners would benefit from knowing total training time and per-subject inference time for the full pipeline.

- **No ablation on the number of SWD projections L.** Theorem 1 shows that error decays as O(L⁻¹/²), and L is a hyperparameter of the method, but the paper does not ablate over L to confirm that results are stable with respect to this choice.

- **Sinkhorn regularization parameter not reported.** The paper uses entropic regularization and the Sinkhorn algorithm to estimate EMD for evaluation (line 204) and in the ablation (Table 4), but does not state the regularization strength (ε) used, which affects approximation quality.

### Trivial
None.

## Nice-to-Haves

- Controlled experiment with a shared initial surface across all baselines (e.g., running CortexODE from the marching-cubes surface) to isolate the loss function effect.
- Paired significance tests or bootstrap confidence intervals for metrics with overlapping standard deviations.
- An experiment on a non-medical shape deformation task (even small-scale) to demonstrate broader transferability.
- Ablation study varying the number of SWD projections L.
- Reporting the regularization parameter (ε) used for Sinkhorn-based EMD estimation.

## Removed Points

*These points were flagged by reviewers but are removed per the filtering rules. They should be treated with caution if encountered elsewhere.*

1. **"Theorem 1 is stated without proof (relegated to appendix)"** — Removed per the rule that weaknesses about missing appendix content are invalid (the parser strips appendices; proofs exist in the original submission).

2. **"Missing training hyperparameters (learning rate schedule, batch size, etc.) from main text"** — Removed per the rule removing nitpicks about reproducibility (undisclosed hyperparameters are standard to place in appendix/supplement).

3. **"Claim of generalizability is not supported by experiments"** — Removed because the paper explicitly scopes itself in the Limitations section ("within the context of this paper, we only focus on this task"), so criticizing its absence is scope creep.

4. **"Differentiability of varifold representation not stated"** — Removed because computing barycenters and normals from differentiable vertex positions is a standard and straightforward differentiable operation in any geometry processing library; this does not require special discussion.

5. **"CD uses O(m²) implementation; optimized CD with kd-trees can approach O(m log m)"** — Removed because the paper compares against the standard CD implementation used in practice by the baselines, and the comparison is conducted on the methods as they actually operate.

6. **Strengths from Strength Finder that were removed as generic or conflicting:** None of the strengths were removed — all six are concrete, specific, and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The reviews largely affirm the paper's stated contributions (novel combination of varifold representation with SWD for mesh deformation, dimension-independent convergence bound for empirical SWD) while raising concerns about confounded cross-method comparisons and a theory-practice gap. No genuinely new observations about the paper emerged that the authors themselves do not already discuss.

## Suggestions

1. **Address the initial-surface confound explicitly.** Either run at least one baseline (CortexODE or CFPP) from the same marching-cubes initialization as DDOT, or provide a detailed paragraph explaining each method's initialization and its likely impact on results, especially SI.
2. **Add significance tests or confidence intervals** for the metrics where DDOT's mean is best but standard deviations overlap with CortexODE (SWD on ADNI, EMD/SWD on OASIS). This will strengthen the "outperforming" claim considerably.
3. **Bridge the theory-practice gap** by adding a brief remark or proposition connecting Theorem 1's bound to the varifold case — e.g., noting that the varifold quadrature converges to the continuous varifold measure as mesh resolution increases, and that the SWD estimation error then inherits the same rate up to a discretization error.
4. **Report the Sinkhorn regularization parameter** used for EMD estimation, and ablate L (number of SWD projections) to confirm stability.
