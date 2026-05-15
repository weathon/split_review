Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final review.

## Summary

This paper introduces GTBO, a method that adapts noisy adaptive group testing — traditionally designed for binary outcomes — to identify axis-aligned active dimensions in high-dimensional Bayesian optimization. GTBO operates in two phases: (1) a group testing phase that selects groups of variables via a mutual-information criterion and uses an SMC sampler to infer which dimensions are active, followed by (2) a standard BO phase with lengthscale priors informed by the discovered active set. The paper provides theoretical grounding for extending group testing to continuous function evaluations and demonstrates strong empirical performance on both synthetic and real-world benchmarks.

## Strengths

- **Novel adaptation of group testing to continuous, real-valued black-box functions.** The paper extends noisy adaptive group testing — which historically requires binary test outcomes — to continuous function evaluations with Gaussian observation noise. This is achieved by modeling the difference in function values under the null (inactive) and alternative (active) hypotheses as two Gaussians differing only in variance (Assumptions 1–2, Section 3), enabling the use of mutual information as a group selection criterion. This theoretical extension is the core contribution and is clearly novel within the BO literature.

- **Remarkably accurate identification of active dimensions with an extremely low false-positive rate.** On four noisy synthetic benchmarks (Figure 2), GTBO correctly identifies all active dimensions in every run (0% false negatives) across ten repetitions, while misclassifying only 6 out of 1,180 inactive variables (0.05% false positive rate). This empirically demonstrates that the group testing machinery can reliably recover the axis-aligned active subspace under its assumed conditions.

- **Strong empirical optimization performance against multiple state-of-the-art methods.** On real-world benchmarks (Figure 5), GTBO shows a sharp performance improvement immediately after the group testing phase on Mopta08 (124D), outperforming TuRBO, SAASBO, HeSBO, BAXUS, CMA-ES, and ALEBO. On synthetic benchmarks (Figure 4), GTBO consistently achieves lower log regret than all competitors over 100 iterations. The performance jump after the group testing phase on Mopta08 provides direct evidence that the identified dimensions are genuinely relevant.

- **Scalable inference via Sequential Monte Carlo.** The SMC sampler with M particles and a Gibbs kernel (Section 3) avoids the intractable exact summation over 2^D possible activity states, enabling the method to scale to problems with hundreds of dimensions (e.g., 180D LassoDNA).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The variance estimation procedure (Section 3) is ad-hoc and lacks robustness guarantees.** The method uses only ~2√D evaluations to estimate both the noise variance σ_n² and the function-value variance σ²: dimensions are split into √D bins, and the √D largest bin differences are attributed to signal variance while the rest are attributed to noise. This assumes at most √D active dimensions — an assumption the authors acknowledge (line 158) and test in the sensitivity analysis (Figure 6, 32 active with √100=10). However, the procedure has no theoretical error bounds, no safeguard against contamination when the assumption is violated, and no ablation showing how sensitive downstream group-testing accuracy is to these estimates. While the paper does test the violated-assumption case (32 active dims) and shows expected degradation, the estimation procedure itself remains a fragile heuristic. This does not invalidate the method but limits its reliability in settings where the ≤√D-active-dimension assumption is uncertain.

2. **Missing ablation against simpler feature-selection baselines.** The experiments compare GTBO against SOTA BO methods (TuRBO, SAASBO, HeSBO, BAXUS, CMA-ES, ALEBO) but not against a simpler baseline that, e.g., performs a small number of one-at-a-time perturbations per dimension and thresholds differences to decide activeness, or uses Lasso-type screening before BO. Without such an ablation, it is unclear whether the sophisticated SMC-based group-testing machinery provides substantial benefits over a simple heuristic, or whether the gains come primarily from the two-phase structure (screening + focused BO) rather than the specific group-testing mechanism.

3. **Batch evaluation capability is claimed but not experimentally validated.** Section 3 describes how GTBO can select multiple near-optimal groups in parallel by re-running the forward-backward algorithm excluding already-chosen groups. However, no experiment in Section 4 tests batch evaluation. This claim remains unsubstantiated in the current paper.

4. **Sensitivity analysis is limited in scope.** Figure 6 ablates noise, total dimensionality, and number of active dimensions, but only on a single function (Levy4 extended to 100D) with a single base noise level (σ=0.1). Results may not generalize across different function classes, especially those with different smoothness or correlation structures. Expanding the ablation to at least one additional function class would strengthen the conclusions about robustness.

5. **The zero-mean assumption for the active-group likelihood (Assumption 2) could be better justified.** The paper states that this assumption "follows from a GP prior assumption on f" (line 155-156). Under a zero-mean GP prior, the difference f(x_t)−f(x_def) is indeed zero-mean Gaussian, making this mathematically sound as a modeling choice. However, the paper does not clearly connect this to the actual estimation procedure (where ĝ is used, not a GP posterior), nor does it discuss what happens when the function has a strong global trend that violates the implicit stationarity assumption. The assumption is reasonable for the purpose of distinguishing signal from noise via variance differences (σ² > σ_n²), but a brief discussion of when it might fail would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- Extending the sensitivity analysis to multiple function classes beyond Levy4.
- Adding an ablation comparing GTBO against one-at-a-time perturbation screening or Lasso-based screening followed by BO.
- Reporting which dimensions GTBO identifies as active on real-world benchmarks (Mopta08, LassoDNA) and discussing whether these align with domain knowledge, to further substantiate the interpretability claim.
- Clarifying whether ĝ denotes a GP posterior mean or a noisy observation, and resolving the minor factor-of-2 discrepancy in the noise variance under the null (if ĝ is a noisy observation, Z_t ~ N(0, 2σ_n²) rather than N(0, σ_n²) when no active dims are present).

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"The core likelihood model is fundamentally flawed (zero-mean assumption invalid)"** — The critic claims that the zero-mean assumption for active groups (Assumption 2) is unjustified because perturbing active variables systematically shifts the function value. However, this assumption follows directly from a zero-mean GP prior (line 155-156), which is a standard modeling choice in Bayesian optimization. Under this prior, the difference f(x_t)−f(x_def) is indeed zero-mean Gaussian. The critic conflates the model's prior assumption with a claim about the true function. The method requires only that σ² > σ_n² to distinguish active from inactive groups, not that the mean is exactly zero. This criticism reflects a misunderstanding of the Bayesian modeling framework rather than a genuine flaw.

2. **"The convergence threshold 5×10³ is a typo"** — This is a parser artifact. The original submission likely uses a different notation (e.g., 5×10⁻³). Parser-induced formatting issues are explicitly excluded from consideration.

3. **"No statistical significance testing"** — The paper reports mean values with standard error shading (line 279), which is standard practice in this community. Requesting formal hypothesis tests goes beyond typical norms for empirical BO papers.

4. **"The definition of active/inactive is qualitative"** — The paper defines inactive dimensions as those where "the function value changes only marginally" (line 55). This is an inherent property of the axis-aligned subspace assumption and is standard in the literature (cited works include Eriksson et al. 2021, Nayebi et al. 2019, etc.). For synthetic benchmarks, ground truth is known; for real benchmarks, the ambiguity is acknowledged and is a feature of the problem setting, not a flaw in the method.

5. **"Griewank benchmark gives unfair advantage to projection methods"** — The paper explicitly acknowledges this (line 318) and mitigates it by using a non-standard default point for GTBO. The critic's claim that this is "not mitigated beyond choosing a non-standard default" is factually wrong — that IS the mitigation the paper describes.

## Novel Insights

None beyond the paper's own contributions. The reviewer critiques and strengths largely align with the paper's self-described claims and limitations. The most interesting observation emerging from the cross-review analysis is that the paper's clean synthetic results (0% false negatives, 0.05% false positives) serve as a best-case validation of the approach, while the real-world results (particularly the sharp drop on Mopta08 at iteration 300) provide the most compelling evidence that the group testing phase genuinely accelerates optimization. The tension between these two modes of evidence — perfect recovery under idealized synthetic conditions versus clearly visible but less perfectly controlled gains on real problems — is characteristic of a method whose assumptions are reasonable but not universally satisfied, and the paper would benefit from more directly discussing this gap.

## Suggestions
- Add an ablation experiment comparing GTBO against a simpler screening baseline (e.g., thresholding per-dimension perturbations or Lasso-based feature selection followed by BO). This would directly address whether the sophisticated SMC/group-testing machinery is necessary or if simpler heuristics suffice.
- Provide theoretical or empirical analysis of how errors in the variance estimates (σ_n², σ²) propagate into group-testing accuracy, and consider a more robust variance estimation procedure that does not assume ≤√D active dimensions.
- Include a brief discussion of when the zero-mean GP prior assumption (Assumption 2) is most likely to fail (e.g., functions with strong monotonic trends) and how such failures would manifest in practice.

## Score and Decision

**Originality:** High. The adaptation of group testing to continuous BO is genuinely novel and connects two previously disconnected literatures.

**Importance of research question:** High. High-dimensional BO is a practically important problem, and explicit identification of active dimensions provides both optimization gains and interpretability.

**Claims supported:** Mostly yes, though the "batch evaluation" claim is unsupported and the benefits of group testing over simpler screening are not fully isolated.

**Soundness of experiments:** Good. Comparisons against many SOTA methods, multiple synthetic and real benchmarks, and a sensitivity analysis. Could be strengthened by ablations.

**Clarity of writing:** Good. The method is clearly explained and the motivation is well-established.

**Value to community:** Significant. The group testing framework provides a new tool for interpretable dimension reduction in BO, and the empirical results suggest practical gains.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>