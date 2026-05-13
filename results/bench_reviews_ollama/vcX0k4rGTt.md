Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes ACP-GN, an approximate full conformal prediction method for neural network regression that avoids both model retraining and grid search over candidate labels. By using Gauss-Newton influence (Eq. 12) to approximate retraining and network linearization (Eq. 15) to express residuals as piecewise-linear functions of the candidate label — recovering the same structure as conformalized ridge regression — the method produces closed-form prediction intervals from a single model fit. The paper also shows ACP-GN corresponds to conformalizing Linearized Laplace (Sec. 3.1) and proposes two practical variants: ACP-GN (split+refine) which restores coverage via sample splitting, and SCP-GN, a normalized split-CP method that retains the coverage guarantee while improving adaptivity.

## Strengths

- **Elegant derivation connecting GN influence to CRR piecewise-linear structure (Eqs. 13–14):** This is the paper's core insight — showing that the add-one-in residual takes the form |a_i + b_i y|, identical to conformalized ridge regression, thereby eliminating both the retraining loop and the exhaustive grid search. This is a genuinely novel and technically clean result that provides a principled computational shortcut for approximate full-CP. Algorithm 2 makes the procedure concrete and efficient.

- **Exact full-CP on the linearized network (Sec. 3.1):** The paper proves that ACP-GN corresponds to exact full conformal prediction on the linearized neural network (Eqs. 18–20), connecting the method to Linearized Laplace and the Conformal Bayes framework. This provides a clean theoretical grounding and places the method in proper context, distinguishing it from a purely heuristic approach.

- **SCP-GN normalization (Eq. 21) preserves the coverage guarantee while improving adaptivity:** This is a practical contribution — normalizing split-CP scores by the Linearized Laplace predictive standard deviation improves adaptivity at minimal computational cost and maintains valid coverage. The paper shows SCP-GN generally outperforms CRF across datasets.

- **Empirical validation on small datasets shows genuine efficiency gains:** On yacht, boston, and energy, ACP-GN produces the tightest intervals among well-calibrated methods across multiple confidence levels (Table 1), directly demonstrating the statistical efficiency advantage of using all training data.

## Weaknesses

### Fatal
None.

### Major

- **No theoretical bound on coverage violation for ACP-GN, and miscoverage confirmed empirically on larger datasets:** Full conformal prediction's defining feature is the distribution-free coverage guarantee (Eq. 2), which requires exchangeability of scores across all N+1 data points. The Gauss-Newton influence approximation (Eq. 12) and linearization (Eq. 15) both break this exchangeability. The paper establishes exact coverage only for the linearized network (Sec. 3.1), not the original DNN. While the paper honestly reports miscoverage on larger datasets (Table 1: protein, community, facebook 2), it provides no theorem, asymptotic result, or even qualitative discussion bounding when or how badly coverage can fail. The paper's conclusion states "we show that we can efficiently construct approximate full-CP predictive intervals...without retraining the model," which overstates what is established: the method is approximate in computation *and* approximate in coverage, and the degree of the latter is not characterized. For a method operating under the "conformal prediction" umbrella — where the guarantee is the core value proposition — this is a meaningful gap. Additionally, the pattern of miscoverage occurring on *larger* datasets (opposite of what one might expect if the GN approximation improves with data) is unexplained and potentially signals a systematic failure mode worthy of investigation.

- **Asymmetric framing in efficiency comparisons:** ACP-GN uses all N training points for both fitting and calibration, while split-CP uses N/2 for each. The resulting tighter intervals for ACP-GN are partly explained by this data advantage, but partly also by the absence of a coverage guarantee — one can always make intervals tighter by sacrificing coverage. The paper does report coverage numbers and marks miscovering methods, which makes the comparison transparent at the data level. However, the abstract's claim of constructing "prediction intervals...post-hoc without held-out data" and the framing around "statistical efficiency" obscures the fact that ACP-GN's efficiency advantage is not an apples-to-apples comparison with a guaranteed-coverage method. This is not a fatal flaw (coverage is reported), but the framing should more clearly acknowledge the trade-off between coverage validity and interval width.

### Minor

- **Application to bounding box task with L1 loss violates the method's theoretical basis:** The paper explicitly acknowledges (Sec. 5.2) that "with L1 loss, Eqs. (12) to (14) no longer hold" yet still applies ACP-GN. No justification is given for why the squared-loss derivation should approximately hold under L1 loss. While the empirical results in Table 2 show the method works reasonably well, this application extends the method beyond its verified theoretical scope without discussion.

- **The split+refine variant partially concedes the paper's stated motivation:** The introduction motivates the work as avoiding sample splitting's statistical inefficiency. Yet the split+refine variant reintroduces splitting to fix miscoverage. While the paper is transparent about this trade-off, the variant is presented as a remedy rather than acknowledged as a fundamental limitation of the approximation approach. Moreover, even this variant relies on the Gauss-Newton + linearization approximation within the calibration set, so its empirical (not guaranteed) coverage still depends on approximation quality.

- **Scalable approximations (KFAC, last-layer) relegated to appendix:** The paper uses only small networks (50 hidden units, 1–3 layers) in the main experiments, noting that GN matrix inversion scales cubically in parameters. Any practical deployment of ACP-GN would require KFAC or last-layer approximations, yet these results appear only in the appendix. Including key findings from App. H.1 in the main text would better reflect the method's practical scope.

## Nice-to-Haves

- **Coverage calibration curves across dataset sizes:** Plotting empirical coverage vs. N for synthetic data where ground truth is known would reveal how miscoverage scales and whether it diminishes asymptotically. Even an asymptotic coverage guarantee (e.g., coverage → 1−α as N → ∞ under specified conditions) would substantially strengthen the contribution.

- **Direct comparison to exact full-CP on small problems:** For the smallest datasets/models, exact full-CP via grid search is feasible. Comparing ACP-GN intervals to true full-CP intervals would directly measure the approximation quality that is the paper's central claim.

- **Visualization of parameter trajectory:** Plotting $\hat{\theta}_*^+(y)$ vs. actual $\theta_*^+(y)$ for small networks would reveal whether the GN step is a geometrically reasonable approximation.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic's claim that split+refine lacks formal coverage guarantee (Issue 2):** While technically true that split+refine doesn't have a *formal* guarantee beyond split-CP's, the split+refine variant does separate training and calibration sets, so it at minimum inherits the standard split-CP exchangeability argument. The GN approximation is used only within the calibration set for computing the CRR structure, but the coverage property depends on the conformalization of calibration scores, not on exactness of the GN approximation. This is more nuanced than the critic claims and partially addressed by the split structure.

- **Harsh critic's claim that the efficiency comparison is "not meaningful":** This overstates the issue. The paper reports both coverage AND width; readers can see that ACP-GN miscovers on some datasets. The comparison is informative as long as both metrics are visible. Downgraded from "not meaningful" to "asymmetric framing."

- **Harsh critic's request for "comparison against methods that also achieve valid coverage on the same datasets":** The paper does compare against SCP, CRF, and CQR — all of which achieve valid coverage — and marks which methods miscover. This request is essentially already addressed.

- **Harsh critic's claim that "the method cannot honestly be called 'conformal prediction'":** The paper uses "approximate full-CP" consistently, acknowledging the approximation. Additionally, the method IS exact full-CP on the linearized network (Sec. 3.1), providing a legitimate basis for the nomenclature.

- **Strength finder's claim about "tighter well-calibrated intervals in limited data regimes" as a separate strength from the derivation:** This is redundant with the core strength about the piecewise-linear structure and the empirical results already noted.

- **Strength finder's claim about "support for multiple nonconformity scores" as a supporting strength:** While the paper does discuss LOO/deleted/studentized variants, this is a standard feature of any CP framework and not a novel contribution of this paper.

## Novel Insights

The paper reveals an underappreciated structural parallel: just as conformalized ridge regression exploits the Sherman-Morrison rank-1 update to avoid retraining, the same piecewise-linear structure can be recovered for neural networks via the Gauss-Newton influence — effectively treating the Jacobian as a learned feature map that converts the DNN into a ridge regression problem at test time. The key tension is that this structural parallel is exact only for the linearized network; for the original DNN, the approximation error has an unpredictable effect on coverage, and critically, the paper's own experiments suggest this error grows (not shrinks) with dataset size, possibly because larger datasets lead to more complex loss landscapes where the linearized model is a poorer local approximation despite better training.

## Suggestions

- Provide even a qualitative discussion of conditions under which the GN + linearization approximation is expected to preserve coverage well (e.g., near a well-conditioned minimum, small residuals) and when it is expected to fail (e.g., flat loss landscapes, sharp curvature changes, undertrained networks).
- Investigate and explain the counterintuitive pattern of worse coverage on larger datasets — this could yield valuable insight into failure modes of the linearized Laplace approximation in general.
- If the split+refine variant is meant as a practical recommendation, prominently position it and clearly articulate its coverage properties (it inherits split-CP's guarantee, plus the GN approximation provides adaptivity).

## Score and Decision

The paper makes a genuine, elegant contribution — the derivation connecting GN influence to the CRR structure is novel and principled, enabling closed-form approximate full-CP intervals without grid search or retraining. The Linearized Laplace connection provides real theoretical grounding. However, the approximation breaks the conformal coverage guarantee without any bound on the resulting miscoverage, and the paper's own experiments confirm systematic miscoverage on larger datasets. The value proposition of conformal prediction is its guarantee; an approximate method must characterize how and when the approximation degrades that guarantee. Without this, the method sits in an awkward space: too approximate to carry the conformal guarantee, but positioned and framed as though it does. The SCP-GN variant, which does maintain the guarantee while improving adaptivity, is arguably the most practically reliable contribution but receives relatively less emphasis.

Originality: High — the GN influence → CRR piecewise-linear connection is novel and insightful.
Importance: Moderate — addresses a real computational bottleneck in full-CP, but the uncharacterized coverage gap limits applicability in the safety-critical settings the paper motivates.
Claims support: Partial — exact for linearized model, empirically validated on small datasets, but coverage violations on larger datasets are unexplained and unbounded.
Experiments: Adequate for small-scale, insufficient for characterizing failure modes.
Clarity: Good — clean exposition of the CRR background and the GN derivation.
Community value: Moderate — the derivation and SCP-GN are useful; ACP-GN itself needs more development before trustworthiness is established.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>