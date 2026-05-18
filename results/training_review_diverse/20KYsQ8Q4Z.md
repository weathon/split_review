Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes Group Testing Bayesian Optimization (GTBO), a two-phase method for high-dimensional BO under the axis-aligned active subspace assumption. In phase one, GTBO adapts noisy adaptive group testing to continuous black-box functions by modeling the difference between a perturbed point and a default configuration as a Gaussian mixture, using an SMC-based mutual information criterion to select which groups of variables to test. In phase two, it runs BO with strongly informative lengthscale priors that focus optimization on the identified active dimensions. The paper demonstrates nearly perfect active-variable recovery (0.05% false positive rate) and competitive optimization performance on several synthetic and real-world benchmarks.

## Strengths

- **Novel and principled extension of group testing to continuous BO.** The paper adapts binary-outcome group testing to continuous, noisy function evaluations by modeling Z_t = f̂(x_t) − f̂(x_def) as a two-component Gaussian mixture (noise-only vs. signal+noise), and uses mutual information maximization to select groups. This is a genuine methodological contribution that goes beyond prior binary-outcome group testing work (Cuturi et al.). (Section 3, Equations for MI and likelihood updates)

- **Accurate and low-cost identification of active dimensions.** In synthetic benchmarks with 50–100 total dimensions, GTBO correctly classifies all active dimensions in every run within 39–112 tests, with a false-positive rate of only 0.05% (6 out of 1180 inactive variables, Figure 1). This is direct, strong evidence that the core group testing procedure works as intended under the assumed conditions.

- **Competitive optimization performance.** GTBO matches or outperforms state-of-the-art methods (TuRBO, SAASBO, HEBO, BAXUS, CMA-ES) on both noisy synthetic benchmarks (Figure 2) and real-world tasks (Figure 3). The sharp drop in incumbent value immediately after the group testing phase on Mopta08 confirms that identifying active dimensions translates into faster convergence.

- **Comprehensive sensitivity analysis.** The paper ablates performance under varying noise levels, total dimensionality, and number of active dimensions (Figure 4), providing practical guidance on where GTBO works and where it breaks down. This transparency is valuable and strengthens the credibility of the approach.

- **Scalable inference via SMC.** By using Sequential Monte Carlo with particles rather than enumerating the 2^D state space, GTBO scales to high dimensions (100+), and the empirical results confirm that this approximation is effective.

## Weaknesses

### Fatal
None.

### Major

- **The variance estimation procedure is ad-hoc and relies on an unverified sparsity assumption.** Estimating σ_n^2 and σ^2 by binning dimensions, evaluating each bin, taking the √D largest absolute differences as "signal" and the rest as "noise" (Section 3) is not derived from any principle and makes two strong assumptions: that at most √D dimensions are active, and that bins containing active dimensions reliably produce the largest differences. The sensitivity analysis confirms that the method degrades when the number of active dimensions exceeds √D (Figure 4, right panel). Since these variance estimates are fixed after initialization and never updated, early errors propagate through the entire group testing phase. While the approach is pragmatic, a more principled estimation scheme (e.g., learning variances via maximum likelihood during testing, or using repeated evaluations at a single point for noise) would substantially strengthen the method. This is the paper's single most significant methodological gap.

- **The zero-mean Gaussian assumption for active-containing groups is a strong simplification that is not empirically validated.** Assumption 2 models Z_t ~ N(0, σ^2) when the group contains active variables. While the normality of the difference follows from a GP prior, the zero-mean assumption is a modeling choice — the actual expected change when perturbing active variables could be systematically positive or negative depending on the geometry of f near the default point. The paper acknowledges this ("we assume this distribution to have mean zero") but provides no diagnostic experiment validating that this assumption is reasonable for the function classes tested. The method's empirical success suggests the assumption works in practice (because discrimination relies on variance differences, not mean differences), but a validation plot comparing empirical Z_t distributions to the assumed mixture would substantially increase confidence, especially for practitioners who might apply GTBO in settings where this assumption fails.

### Minor

- **Limited evaluation of robustness to default point placement.** The default point is fixed at the center of the search space. While the Griewank experiment (Section 4.2) runs GTBO with a non-standard default away from the optimum to avoid unfair advantage, there is no systematic study of how GTBO's performance degrades as the default point moves further from a well-behaved region (e.g., near the boundary, or in a region with strong gradient). This is relevant because Assumption 1 (inactive perturbations produce only noise-level changes) depends on the default being in a region where inactive dimensions genuinely don't move the function much.

- **Comparison with SAASBO and ALEBO is limited by different evaluation budgets.** The paper notes that SAASBO could only be run for 100 evaluations and ALEBO for 300 due to memory/scale constraints, while GTBO uses up to ~100 evaluations for group testing plus additional evaluations for BO. This asymmetry is acknowledged but not critically discussed — it conflates algorithmic design with computational scaling and means the comparison does not fully isolate sample efficiency.

- **Group testing observations are highly localized around the default point.** The paper mentions removing duplicate points before the BO phase (Section 3), but the resulting observation set remains clustered near x_def. This could make the GP surrogate poorly calibrated far from the default, potentially slowing optimization in regions the group testing phase never explored. The paper does not analyze or diagnose this effect.

- **No quantitative results table for real-world benchmarks.** Real-world results are shown only as incumbent plots (Figure 3). Reporting final best-found values and standard errors in a table would facilitate comparison with prior results.

- **Particle degeneracy for SMC is not discussed.** The paper uses 10,000 particles for a 2^D state space (D up to 180) but does not discuss whether this is sufficient or whether particle degeneracy occurs. The empirical success is reassuring, but a brief theoretical or diagnostic justification would strengthen this component.

### Trivial
None.

## Nice-to-Haves

- A diagnostic plot showing the empirical distribution of Z_t for groups with and without active variables on a simple synthetic function, overlaid with the assumed Gaussian mixture, would directly validate the core modeling assumption.
- A formal (information-theoretic) bound on the number of group tests needed to identify the active set with high probability, even under the paper's own assumptions, would strengthen the claim of sample efficiency.
- An ablation where GTBO is run with deliberately misspecified variances (e.g., swapping σ_n^2 and σ^2) would help characterize the method's robustness.
- A small-budget comparison (e.g., ≤100 total evaluations) between GTBO and methods that do not require a dedicated testing phase would provide a more symmetric efficiency comparison.

## Removed Points

- **"Conflates the marginal distribution of a GP at a point with the distribution of the difference":** This is factually incorrect. Under a GP prior, any linear combination (including the difference) of function values at two points is normally distributed. The paper's statement that f̂(x_t) is normally distributed and the difference is normally distributed is correct.
- **"ignores that magnitude and sign depend on which active variables are perturbed":** Overstated. The method uses random symmetric perturbations U(−0.5, 0.5) and relies on variance differences (σ^2 > σ_n^2) for discrimination, not mean differences. The sign cancels out under symmetric perturbation; the magnitude is captured by σ^2.
- **Criticism about not testing non-axis-aligned subspaces:** The paper explicitly scopes itself to the axis-aligned case (stated in the abstract, introduction, Section 2, and Section 3). Demanding evaluation on non-axis-aligned problems is scope creep — the paper's claims are conditioned on the axis-aligned assumption holding.
- **Generic formatting/style/presentation nitpicks:** Removed per instructions.

## Novel Insights

The reviews converge on an important tension: the paper's primary strength (a clever, practical adaptation of group testing to continuous BO) is also the source of its main weaknesses (simplified distributional assumptions and ad-hoc variance estimation). Neither reviewer identified a contradiction or fatal flaw; rather, both highlight that the method's reliability depends on assumptions that are reasonable but unvalidated. The most useful insight is that the variance estimation procedure — which seems like a secondary implementation detail — is actually structurally important: because the entire group testing phase hinges on correctly distinguishing σ_n^2 from σ^2, a misspecification early on can cascade. The paper's own sensitivity analysis partially addresses this, but an ablative study isolating the impact of variance misspecification would be the single highest-value addition.

## Suggestions

1. Replace or augment the ad-hoc variance estimation (binning + sqrt(D) threshold) with a more principled approach — for example, estimate σ_n^2 from repeated evaluations at the default point, and estimate σ^2 jointly during group testing via maximum likelihood or Bayesian inference. At minimum, show that the current procedure is robust when the sqrt(D) assumption is violated by including an ablation where the true number of active dimensions exceeds sqrt(D).
2. Add a diagnostic figure for a simple synthetic function (e.g., a quadratic with known active subspace) showing the empirical distribution of Z_t for active and inactive groups overlaid with the fitted Gaussian mixture. This would directly validate the core modeling assumption.
3. Include a table reporting final best-found values with standard errors for the real-world benchmarks.
4. Discuss the potential issue of SMC particle degeneracy (e.g., effective sample size over iterations) for high-dimensional settings, even if only briefly.

## Score and Decision

This paper makes a genuine contribution by bridging group testing and Bayesian optimization in a novel and practical way. The core idea is well-motivated, the algorithm is clearly described, and the empirical results convincingly demonstrate that GTBO works under its stated assumptions. The weaknesses are real but addressable: the variance estimation is ad-hoc (the main methodological gap), and the core distributional assumptions would benefit from direct validation. These are not fatal — they do not undermine the paper's central claim that group testing can be adapted for BO and yields strong empirical performance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>