Now I will write the final consolidated review.

## Summary

The paper studies conformal prediction for surrogate models of time-dependent PDEs, where exchangeability is violated because the solution distribution drifts with time. It proves that in function space, distributions at different times are mutually singular (TV distance = 1), precluding standard CP. The paper then proposes a weighted conformal prediction method based on the observation that after spatial discretization, the solution of a linear PDE with Gaussian initial condition is Gaussian, so the density ratio between test and calibration times can be computed in closed form. Experiments on synthetic linear PDEs and a thermography dataset are presented.

## Strengths

1. **Theorem 4.1 establishes a genuine impossibility result.** The proof that for the heat equation with Gaussian initial condition the TV distance between solution distributions at any two distinct times is maximal (d_TV = 1) is a nice theoretical observation. It cleanly justifies why standard CP cannot work in the function-space setting and motivates the discretized approach that follows.

2. **Principled handling of excessive distribution shift.** When the distributional dissimilarity between calibration and test times is too large for finite bands, the method returns infinite bands (reported as n_∞). This ensures coverage is never violated (trivially 100% coverage for those samples), a safer behavior than the systematic undercoverage produced by baselines (Table 1, Section 5).

3. **Computational efficiency.** The paper reports that WCP and naïve CP require seconds for 5000 test samples, while LSCI takes ≈40 minutes on the same hardware (Section 5). This practical benefit is noted alongside the coverage results.

## Weaknesses

### Fatal
None. The core idea (using the Gaussian structure of discretized linear PDEs for weighting) is not fundamentally impossible; the problem is that the paper does not properly establish the theoretical connection to weighted conformal prediction.

### Major

1. **No theorem establishing the coverage guarantee of the proposed method.** This is the most critical gap. The paper claims "exact coverage guarantees through reweighting calibration scores" (Abstract), "formal coverage guarantees" (Section 4.4), and that WCP "is the only method providing formal guarantees" (Section 5). Yet the paper contains **no theorem** stating the coverage guarantee of the weighted CP procedure. The only theoretical results are Theorem 4.1 (function-space impossibility, interesting but not about the CP guarantee) and Theorem 4.2 (the discretized solution is Gaussian, a standard result for linear ODEs). The link between the proposed weights and any coverage guarantee is asserted without proof. Remark 4.5 gestures at "asymptotic — and in some cases even non-asymptotic — guarantees" but provides neither a statement nor a proof. For a paper whose central claim is providing "exact coverage guarantees," this is a fundamental omission.

2. **The weighting scheme's validity for weighted CP is not established.** The paper proposes weights w_i ∝ N(u_i; μ_{t+δ}, Σ_{t+δ}) / N(u_i; μ_t, Σ_t), which is the likelihood ratio of the marginal densities of the solution field u_t. The data are described as pairs (u_0, u_t) in Section 4.1, and the score function (maximum absolute error over space from Diquigiovanni et al., 2022) depends on both u_0 (through the surrogate model) and u_t (the true solution). The paper never clarifies what the "data point" is for CP purposes nor justifies why the marginal ratio of u_t equals the required likelihood ratio for the joint distribution of the data that determines the score. Because u_t = S_t(u_0) is a deterministic transformation of u_0 (for a deterministic PDE), and the mapping from u_0 to u_t changes between calibration (time t) and test (time t+δ), the score function itself changes — it is a different function of u_0 at different times. Weighting the marginal distribution of u_t does not directly address this. The paper provides no argument that the proposed weights satisfy the weighted exchangeability condition or yield valid coverage. This is a structural gap in the core contribution.

3. **Ambiguity in the CP problem formulation.** The paper oscillates between different formulations. Section 4.1 describes data as pairs (u_{0,i}, u_{t,i}) from a pushforward measure; Section 4.4 weights u_i alone; the score from Diquigiovanni et al. (2022) is defined on functional data; the baselines are applied to residuals of a surrogate model that takes u_0 as input. It is never clearly stated what the conformal predictor takes as input, what the score is a function of, and what distribution the coverage guarantee covers (marginal over u_0, conditional on u_0, or marginal over u_t). This ambiguity makes it impossible to determine whether the method could be valid under some interpretation.

4. **Coverage drops below the nominal level in several experimental settings.** In Table 1, WCP reports coverage of 0.88 (a=-0.0075, timestep 10), 0.84 (a=-0.0075, timestep 15), 0.88 (a=-0.01, timestep 10), and 0.85 (a=-0.005, timestep 20) — below the 90% target. The paper attributes this to stochastic noise from small remaining sample sizes after excluding infinite-band samples, but this is precisely where the "exact coverage guarantee" should hold. The issue is compounded by reporting coverage only on non-infinite-band samples; overall coverage (including infinite bands) would be higher, but the practical utility of bands that are either trivially covering (infinite) or undercovering (finite) is unclear.

### Minor

5. **Parameter estimation is not discussed.** The method requires the exact parameters μ_t, Σ_t of the Gaussian solution distribution. Theorem 4.2 provides formulas in terms of the PDE operator A and initial distribution parameters μ_0, Σ_0, but the paper does not discuss how these are obtained in practice, whether they can be estimated from data, or how estimation error affects coverage. This is a practical concern that limits applicability.

6. **Theorem 4.1 is presented as more central than it is.** The function-space impossibility result is interesting but tangential to the main method. The paper moves from this result to the discretized setting, and the weighting scheme does not depend on it. A more concise treatment would suffice.

### Trivial
None.

## Nice-to-Haves

- The paper would benefit from a formal theorem stating the coverage guarantee under clearly stated assumptions, following the standard template of weighted conformal prediction (Tibshirani et al., 2019; Barber et al., 2023).
- An "oracle" baseline using the correct joint likelihood ratio (if computable) would clarify whether the marginal weighting is sufficient.
- Sensitivity analysis on the estimation of μ_t and Σ_t would strengthen the practical claims.
- Reporting overall coverage including infinite-band samples (which trivially cover) alongside the conditional coverage would give a more complete picture.

## Removed Points

- **"Invalid weighting for conformal prediction (structural) — fatal"** (Harsh Critic). The critic claimed the weighting is fundamentally invalid because it uses marginal instead of joint density. This is downgraded from "fatal" to "major" because there might be a valid interpretation under which the score depends only on u_t (if u_0 is determined by u_t), and the paper could potentially justify this with additional clarification. The issue as presented is a major gap, not an impossibility proof. Placed in Major weakness #2.

- **"Theorem 4.2 is standard/not novel"** (Harsh Critic). This is true but is a statement about contribution novelty more than a weakness. The paper's novelty lies in applying this known result to enable weighted CP, so the observation is not a weakness per se. Removed as noise.

- **"Theorem 4.1 is tangential"** (Harsh Critic). The critic's judgment about what should be in the paper is a matter of authorial choice, not a concrete weakness. Removed as opinion.

- **"Section-by-section notes about abstract/introduction claiming unsupported guarantees"** (Harsh Critic). This is subsumed by Major weaknesses #1 and #2.

- **"Missing appendix with real-world details"** (Harsh Critic). The appendix is stripped by the PDF parser; this is a known artifact, not the authors' fault. Removed per hard rules.

- **Strength Finder generic strengths** (e.g., "principled treatment," "computational efficiency" kept; "Strong empirical validation" demoted because coverage drops below nominal in some settings — the experiments don't fully support the claim. Removed the conditional/overclaimed parts of the strength about empirical validation.)

- **Strength Finder "Theorem 4.2 provides exact Gaussian form"** — this is a standard result; removed as an overclaimed strength.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's insight about the joint vs. marginal likelihood ratio is a known requirement of weighted CP (Barber et al., 2023; Tibshirani et al., 2019), and the paper's failure to address it is a gap, not a novel observation.

## Suggestions

1. **Provide a theorem and proof for the coverage guarantee.** State clearly what the conformal data points are (are they (u_0, u_t) pairs or just u_t?), what the score is, and prove that the proposed weights yield the claimed coverage under stated assumptions. Without this, the central claim of the paper is unsupported.
2. **Clarify the CP formulation.** Specify the relationship between the surrogate model, the score function, and the data points used in the CP procedure. Explain how the score distribution relates to the marginal distribution of u_t.
3. **Discuss the parameter estimation issue.** Either show how μ_t and Σ_t are computed from known PDE quantities, or analyze the effect of estimation error on coverage.
4. **Report coverage including infinite-band samples** (which trivially achieve 100% coverage) alongside the conditional coverage, so readers can assess the overall reliability.

## Score and Decision

**Round 1 bracket**: [3.0, 4.5]. The most comparable anchor is "Calibrated Physics-Informed Uncertainty Quantification" (4.50, Reject), which was criticized for lacking theoretical support for its CP guarantees. The paper under review has a more central problem — not just lacking a theoretical result, but having an unsubstantiated weighting scheme whose connection to CP theory is not established. Weakness-anchored papers ("Adapting Prediction Sets to Distribution Shifts Without Labels," 3.67, Reject) that lacked theoretical guarantees and were deemed heuristic further confirm the bracket.

**Narrowing**: The paper under review shares the failures of the low-band and weakness-anchored reject papers: claiming coverage guarantees without providing a theorem or rigorous justification. The paper has genuine strengths (Theorem 4.1, infinite-band handling, computational efficiency) but the core contribution — the weighted CP method with claimed exact coverage — is not properly established. The experimental results show coverage below nominal in several settings, further weakening the claim.

**Final score**: 3.0 — The paper identifies an important problem and makes interesting observations, but the central methodological contribution is unsupported. The missing coverage theorem and the unjustified weighting scheme mean the paper does not deliver on its core promise of "exact coverage guarantees." This is a fundamental issue as defined by the evaluation criteria (the central claim is unsupported by the evidence presented).

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>