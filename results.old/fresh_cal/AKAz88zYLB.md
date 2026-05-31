Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes a methodology for generating prediction intervals for dose-response models with continuous treatments using weighted conformal prediction. The key insight is framing the evaluation of dose-response curves across all treatment values as a covariate shift (from the observational treatment distribution to a uniform interventional distribution) and using inverse propensity weighting to correct for this shift. The paper also extends this to a local variant using kernel functions, and provides a practical pipeline for estimating the propensity density via conformal predictive systems and kernel density estimation.

## Strengths

- **Principled derivation of propensity-weighted likelihood ratios for the dose-response setting.** Section 4.2 formally derives the weight $w_{g,p}(X_i, T_i) \propto \mathbbm{1}_{[t_L,t_U]}(T_i)/\pi(T_i|X_i)$ by decomposing the joint covariate-treatment distribution under the uniform interventional treatment assumption. This cleanly maps the dose-response UQ problem onto Tibshirani et al.'s weighted conformal prediction framework and is conceptually well-motivated.

- **Empirical demonstration that ignoring the covariate shift breaks coverage and propensity weighting restores it.** Figure 1 (Setup 3, Scenario 1) shows that standard conformal prediction and local-only weighting produce coverage well below nominal (e.g., ~60–70% for 90% target), while propensity-weighted methods (both oracle and estimated) recover coverage close to the nominal level. This directly supports the paper's central claim.

- **Novel synthetic benchmark (Setup 3) designed to stress-test confounding and limited overlap.** The design with four conditional dose-response functions and heavy confounding via $X_1, X_2$ (Table 1) creates a genuinely challenging test for UQ methods. This is a useful resource for the community.

- **Practical propensity estimation pipeline using CPS + KDE.** Section 5.2 describes a tractable approach for estimating the propensity density when the true GPS is unknown, combining a CatBoost propensity learner, split CPS calibration, and kernel density estimation. This moves the method beyond oracle-only idealization.

## Weaknesses

### Fatal

None. The core methodological approach (global propensity-weighted CP) is theoretically grounded in Tibshirani et al.'s weighted conformal prediction, and no fatal error invalidates the paper's central claims.

### Major

- **Results presented for only one of multiple experimental scenarios.** The paper describes three experimental setups (Setup 1 from Wu & Matching 2024, Setup 2 from Schröder et al. 2024, and Setup 3 with two scenarios), but the main text only presents detailed quantitative results for Setup 3, Scenario 1. Results for Setup 1, Setup 2, and Setup 3 Scenario 2 (the heteroscedastic case) are absent. While some results may reside in a stripped appendix, the main paper should at minimum summarize key findings across all setups to support the claimed generality. As presented, the empirical evidence rests on a single data-generating process, which is insufficient to substantiate the broad conclusions drawn.

- **"CatBoost with Uncertainty" baseline is undefined.** The paper mentions this method as a comparator (line 219) with a citation to Duan et al. (NGBoost), but never specifies what it actually is — e.g., whether it uses CatBoost's内置 variance estimates, a separate probabilistic model, or some other uncertainty quantification approach. The statement "The CatBoost with Uncertainty approach used the same underlying CatBoost model as the CADRF methods to ensure consistency" (line 221) does not clarify what uncertainty mechanism is employed. Without this, the baseline is uninterpretable, and the reader cannot assess whether the comparison is meaningful or a straw man.

- **No per-treatment-value coverage evaluation to support the "local coverage" claim.** The paper's abstract claims the method "approximates local coverage for every treatment value" and Section 5.3 claims "more conditional prediction intervals." However, the experiments only report coverage *averaged* over all 40 treatment values and all test samples (line 192: "coverage of all treatment values and all samples in the test set are aggregated to a single mean coverage"). Per-treatment-value coverage curves (coverage vs. $t$) are never shown. Without this evidence, there is no demonstration that coverage holds across the treatment range rather than merely on average, leaving the local coverage claim unsupported by the presented evaluation.

### Minor

- **The most relevant baseline (Schröder et al. 2024) is omitted with only a computational cost justification.** The paper states that a comparison "would require several years to complete the same experiments" (line 277). Even a reduced-scale comparison on a subset of treatment values or a single seed would provide useful calibration. The absence of any point of comparison against this closely related method weakens the empirical positioning.

- **No sensitivity analysis for the CPS+KDE propensity estimation pipeline.** The paper acknowledges (line 217) that the estimated propensity is approximate and KDE parameters introduce additional error, but provides no diagnostics (e.g., calibration of estimated densities, sensitivity to KDE bandwidth, comparison between estimated and oracle weights). The experiments only evaluate a setting where the true propensity is a simple normal distribution (Setup 3). How robust the method is to propensity estimation quality in more complex or high-dimensional scenarios remains unclear.

- **The local variant's theoretical status is heuristic.** The local propensity-weighted method (kernel + inverse propensity weighting) is presented without a proof or formal asymptotic argument that it yields coverage conditional on $T = t$. The paper cites Tibshirani et al.'s local coverage idea, which provides *marginal* coverage reweighted by a kernel — not conditional coverage for each $t$. The paper's hedging language ("approximates," "more conditional") is appropriate but does not fully resolve the gap between the problem definition (Eq. 1, requiring coverage for each $t$ individually) and what the method actually guarantees.

### Trivial

None.

## Nice-to-Haves

- Report minimum effective sample size for the local propensity method across treatment values, to help readers understand when intervals become uninformative.
- Include a runtime comparison (global vs. local method vs. standard CP).
- Add a structured limitations section, rather than scattering limitations across the results discussion.

## Removed Points

These points from the input reviews are flagged for removal — treat them with caution:

1. **"The paper is too short / missing sections"** — The parser strips appendix and reference sections from all papers; the original submission likely contains additional content. Removed per formatting instructions.
2. **"Typographical error in the kernel equation"** (reviewer's point about "$K((t-t/h))$") — This is a parser artifact mangling LaTeX, not an author error. Removed per formatting instructions.
3. **"Bandwidth parameter $h = 2 \cdot (0.$ is cut off"** — Parser truncation issue. Removed per formatting instructions.
4. **"Split CPS details mismatch with experiments"** (reviewer's note that split CPS is described but not used for main intervals) — The paper uses CPS for propensity estimation, not for the main prediction intervals; this is a separate use case and the background is still relevant context.
5. **"Section-by-section formatting/style nitpicks"** — Removed as non-substantive formatting observations.
6. **Strength Finder's generic strengths** — Generic framing about "addressing an important problem" and "targeting an interesting question" removed as they lack specific content tied to the paper.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface any genuinely novel observation about the work that the paper itself does not already convey.

## Suggestions

1. **Present results for all experimental setups in the main paper** — even as a summary table (mean coverage, interval width, coverage variance across seeds) for Setup 1, Setup 2, and Setup 3 Scenario 2. This is the single highest-priority addition.
2. **Add per-treatment-value coverage plots** for the local propensity method (coverage vs. treatment value $t$) to directly substantiate the "local coverage" claim.
3. **Define the "CatBoost with Uncertainty" baseline** clearly — specify the uncertainty mechanism, or replace it with a standard, well-understood baseline (e.g., conformalized CatBoost, or a Bayesian neural net).
4. **Include a reduced-scale comparison with Schröder et al.** (e.g., on a single seed with a coarser treatment grid) to give readers some calibration for the method.
5. **Add an ablation on KDE bandwidth** for the propensity estimation to demonstrate the method's sensitivity (or robustness) to this choice.
6. **Clarify the theoretical status of the local method** — either provide an asymptotic argument (e.g., under Lipschitz continuity of the density, the kernel-weighted method approximately achieves conditional coverage) or explicitly temper the claim to "heuristic approximation" and note the dependence on bandwidth and sample size.

## Score and Decision

**Originality:** Moderate. The key insight (framing dose-response evaluation as covariate shift + propensity weighting) is novel in the dose-response UQ context, though it applies existing machinery (weighted CP, CPS). **Quality of research question:** High. Uncertainty quantification for continuous-dose-response models is practically important and underexplored. **Claims support:** Weak. The main claim of generality is not supported because results are only shown for one of multiple experimental scenarios, and the local coverage claim lacks per-treatment evaluation. **Soundness of experiments:** Moderate — the one presented scenario is well-designed, but the evidential base is too narrow. **Clarity:** Adequate, though some key definitions are missing. **Value to community:** Potentially high, once the empirical foundation is strengthened.

**Score:** 5.5

**Decision:** Reject (pending major revisions addressing the incomplete empirical presentation and undefined baseline)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>