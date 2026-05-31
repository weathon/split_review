So the paper never mentions cross-fitting or sample splitting in its nuisance estimation on the test set. It says:

- Line 214: "unlike (Gao, 2025), our proposed methodology does not require sample splitting. The key derivation in Section 4.1, as well as the proofs of Theorem 1 and Proposition 2 in this section, are conducted using the full dataset without sample splitting."

This is a genuine concern because they estimate nuisance parameters on the same test dataset used for evaluation. In semiparametric inference, this can cause first-order bias if the nuisance estimation is not Neyman-orthogonal. They claim the moment conditions (Eq. 4) handle this, but the theoretical justification is thin.

Now let me write the full review:

---

## Summary

This paper proposes a relative error-based evaluation framework for heterogeneous treatment effect (HTE) estimators. The key insight is to relax the requirement that outcome regression models be consistently estimated, which is problematic in the presence of covariate shift between treatment and control groups. By deriving orthogonality conditions on the nuisance parameters (propensity score and outcome model), the authors design a weighted least squares loss and a soft-constraint regularizer embedded in a Dragonnet-inspired neural network. The resulting relative error estimator achieves $\sqrt{n}$-consistency and valid confidence intervals even with misspecified outcome models, provided the propensity score is correctly specified. An associated HTE learning method that aggregates pairwise nuisance estimates is also proposed. The evaluation covers IHDP and Twins semi-synthetic datasets with coverage and selection accuracy metrics.

## Strengths

- **Theoretical relaxation of nuisance parameter requirements** — The paper derives explicit moment conditions (Equation 4) that allow the relative error estimator to maintain $\sqrt{n}$-consistency and asymptotic normality (Theorem 1, Proposition 2) even when outcome regression models are misspecified, as long as the propensity score is correctly specified. This addresses a genuine gap over Gao (2025), which requires all nuisance estimators to converge at $n^{-1/4}$ rates.
- **Practical loss design with soft constraint relaxation** — The weighted least squares loss $\mathcal{L}_{\text{wls}}$ (Section 4.2) and the soft-margin balance regularizer $\mathcal{L}_{\text{const}}$ transform an over-constrained system of moment conditions into a tractable optimization. The ablation study (Table 5) shows that removing $\mathcal{L}_{\text{const}}$ causes significant drops in both coverage and selection accuracy, validating the design.
- **Empirical gains in both evaluation and learning** — The method achieves near-nominal 90% coverage rates (Figures 1–2), selection accuracy exceeding 0.80 (Table 2), and outperforms baselines across PEHE and ATE metrics on IHDP and Twins (Table 1). The ablation and sensitivity analyses (Tables 4–5) are thorough.

## Weaknesses

### Fatal
None.

### Major

- **Notation in the Taylor expansion is ambiguous or self-cancelling** — Equation (3) on page 6 reads as $\Delta_\gamma^\top (\tilde{\gamma} - \tilde{\gamma}) + \Delta_{\beta_0}^\top (\tilde{\beta}_0 - \tilde{\beta}_0) + \dots$ where the differences appear to involve the same symbol on both sides, which would make them identically zero. The intended distinction is between the empirical estimator (hat: $\hat{\gamma}$) and its probability limit (bar: $\bar{\gamma}$), but the paper uses `\tilde` and `\bar` inconsistently throughout Sections 4.1–4.3. The same issue affects the absolute error estimator on page 3 where $\{\hat{\tau}(X_i) - \hat{\tau}(X_i)\}^2$ also collapses to zero. While these may be rendering artifacts (the original PDF distinguishes tilde from bar), as presented in the text these expressions are unverifiable. This is not merely cosmetic: readers cannot confirm the validity of the core expansion (from which Eq. 3 follows) if the symbols cannot be disambiguated.
  
- **The rate argument for $o_\mathbb{P}(n^{-1/2})$ remainder is incomplete** — Theorem 1 requires nuisance estimators to converge "faster than $n^{-1/4}$" and the paper claims this is "readily satisfied" by citing Chernozhukov et al. (2018) and Semenova & Chernozhukov (2021). However, the rate justification is superficial. (1) The paper works with misspecified outcome models where nuisance parameters converge to probability limits rather than true values; the convergence properties of empirical gradients at these limits are different and not analyzed. (2) The paper does not establish concrete regularity conditions (e.g., Donsker properties, entropy bounds, or smoothness of the learned representation $\Phi(X)$) that would guarantee the required rates when the nuisance estimators are neural networks. Without this, Theorem 1's stated conditions are not verified for the proposed architecture.

- **"No sample splitting" claim lacks justification** — The paper asserts (line 214) that "unlike Gao (2025), our proposed methodology does not require sample splitting" and that "the proofs ... are conducted using the full dataset without sample splitting." However, the nuisance parameters ($\tilde{\gamma}, \tilde{\beta}_0, \tilde{\beta}_1$) are estimated via neural networks on the same test dataset used for computing the relative error estimator. In the semiparametric inference literature, estimating high-dimensional nuisance parameters on the same sample used for inference typically requires cross-fitting to avoid first-order bias, unless the estimating equation is Neyman-orthogonal *and* the nuisance estimator is sufficiently regular. The paper's claim that the moment conditions (Eq. 4) eliminate the need for sample splitting only guarantees that the *expectation* of the gradient terms is zero; it does not automatically control the empirical bias from evaluating the influence function and nuisance model on the same data. This is a significant gap in the theoretical argument, especially since cross-fitting is standard practice (Chernozhukov et al., 2018).

- **Evaluation on semi-synthetic data is circular** — The paper's core claim is robustness to *realistic* misspecification where ground truth is unavailable. Yet the experiments validate evaluation quality (coverage, selection accuracy) on IHDP and Twins—semi-synthetic datasets where "ground truth" treatment effects are known by construction. The selection accuracy metric (Table 2) explicitly requires knowing which candidate estimator is truly better, which is determined by the artificially imposed data-generating process. This means the evaluation validates whether the method correctly ranks estimator pairs that were already designed to differ in a specific way. The paper acknowledges this limitation implicitly by relegating the Jobs dataset (truly observational) to the appendix, and the real-data results are not discussed for the evaluation framework.

### Minor

- **The HTE learning method is under-motivated** — Section 5 introduces pairwise aggregation of nuisance estimates into a final HTE estimator using simple uniform averaging. The paper admits the method "surprisingly" outperforms baselines but provides no theoretical analysis of why this aggregation works, no variance analysis of the averaged estimator, and no principled weighting scheme. The conclusion (line 349) itself acknowledges this is a "simple uniform averaging scheme" that "may underutilize the heterogeneous strengths of individual estimators."

- **Experimental scope is limited to two datasets for primary results** — The main HTE results (Table 1) cover only IHDP and Twins. The Jobs dataset (truly observational) and the ablation analysis are in the appendix. The sensitivity analysis for propensity score perturbation (Table 6) uses simulated data, not real data with known misspecification structure.

- **Table 5 ablation variant "wls + ce" comparison to Gao is unclear** — The paper states this variant "degenerates to TARNet used in Gao's framework," but Gao's method and the proposed neural network differ in nuisance estimation protocols and training objectives. A direct equivalence claim needs more careful justification.

## Nice-to-Haves

- Consider providing a minimal proof sketch or lemma showing that the empirical gradient terms $\Delta_\gamma, \Delta_{\beta_0}, \Delta_{\beta_1}$ satisfy the required $O_\mathbb{P}(n^{-1/2})$ concentration under the proposed neural network architecture, at least under stated regularity conditions.
- Include a sensitivity analysis that manipulates the degree of distributional shift between treatment and control groups, then measures how coverage degrades compared to baselines, to directly test the robustness-to-extrapolation claim.
- Provide at least a variance comparison between the uniform pairwise aggregation and individual candidates, to support the HTE learning results in Section 5.
- Consider clarifying whether the representation $\Phi(X)$ is shared between the propensity score head and the outcome heads during training, as this affects the misspecification analysis.

## Removed Points

- **"Unclear notation undermines the theoretical argument" (framed as fatal)** — The reviewer correctly identifies that tilde/bar/hat notation is confusingly rendered, making derivations hard to follow. However, the underlying mathematical idea (expanding around probability limits of nuisance parameters) is standard in semiparametric inference. This is a major presentation issue, not a fundamental methodological flaw. Downgraded to major and kept as the first Main weakness.
  
- **"The experiments do not adequately test the paper's core claim" (framed as fatal)** — The circular evaluation concern is valid, as the semi-synthetic benchmarks require known ground truth for evaluating selection accuracy. However, this is the standard validation protocol in the HTE literature (PEHE and selection accuracy both require semi-synthetic ground truth). While it limits generalizability claims, it does not invalidate the results. Kept as major but rephrased.
  
- **"The 'no sample splitting' claim conflicts with experimental setup" (framed as fatal)** — The concern is substantive but depends partly on the reviewer's interpretation of standard practice. The paper's moment conditions provide theoretical justification for why sample splitting might be unnecessary. This is a genuine gap, not a clear error. Kept as major.
  
- **"HTE learning method is under-motivated" (framed as fatal)** — This is a fair criticism but the authors themselves acknowledge in the conclusion that the aggregation is simple and that better weighting strategies are future work. The method's performance is still empirically strong. Demoted to minor.
  
- **"{\hat{τ}(X_i) - \hat{τ}(X_i)}^2 is identically zero" (absolute error formula)** — This appears in the absolute error estimator on page 3 (line 78). It could be a parser artifact where tilde and hat render identically. The absolute error estimator is not the paper's main contribution (it is used only for motivation). Demoted to trivial presentation issue, not repeated in main weaknesses.
  
- **Missing convergence rate conditions for misspecified models** — Merged into the rate argument major weakness.
  
- **Missing analysis of constraint satisfaction quality** — The ablation (Table 5) and Appendix F.4 address this sufficiently for a minor concern. Dropped.
  
- **$\bar{\tau}$ vs $\hat{\tau}$ notation inconsistency** — Merged into the main notation weakness.

## Novel Insights

The paper's core theoretical contribution — that the relative error estimator's orthogonality conditions on nuisance parameters can be *learned into* the estimation procedure via a weighted loss rather than requiring consistent nuisance estimation — is a genuine insight. If the nuisance parameters are trained to satisfy $\mathbb{E}[\Delta_\gamma] = \mathbb{E}[\Delta_{\beta_0}] = \mathbb{E}[\Delta_{\beta_1}] = 0$, the debiased influence function automatically compensates for outcome model misspecification. This is more ambitious than standard double-robustness (where one model must be correct), but it shifts the burden to the constraint-satisfaction quality of the optimization. The question of whether soft-constraint relaxation with neural networks actually achieves sufficient constraint satisfaction in finite samples — rather than merely having the right asymptotic property — is an open empirical question that the paper partially addresses through ablation but does not fully resolve.

## Suggestions

- Add a notation table/appendix explicitly mapping hat ($\hat{\cdot}$), bar ($\bar{\cdot}$), and tilde ($\tilde{\cdot}$) symbols to their mathematical meaning (empirical estimator, probability limit, reference estimator).
- State explicit regularity conditions (e.g., entropy integral bounds on $\Phi(X)$, boundedness of the representation) that guarantee the convergence rates claimed in Theorem 1.
- Provide a brief discussion or experiment comparing the method with and without cross-fitting to empirically validate (or disconfirm) the no-sample-splitting claim.
- Clarify the equivalence claim between the "wls + ce" ablation variant and Gao (2025)'s method in Table 5, since they differ in training protocol.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>