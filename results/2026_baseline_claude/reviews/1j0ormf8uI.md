## Summary
The paper proposes *Conformalized Survival Counterfactual Prediction*, a method for constructing lower predictive bounds (LPBs) for counterfactual survival time under different treatments in the general right-censored setting. The central contribution is a reweighting scheme that converts the counterfactual prediction problem into a weighted conformal prediction problem on the uncensored sub-sample, achieving exact marginal coverage (rather than PAC-type) guarantees. The method is also shown to be doubly robust against misspecification of either the weight or quantile regression model.

---

## Strengths

- **Closes a clearly identified gap.** Prior works (Gui et al., 2024; Davidov et al., 2025) provide only PAC-type coverage for survival LPBs. The paper is the first to achieve exact marginal coverage under general right-censoring *and* counterfactual treatment settings. The distinction is substantive: marginal coverage is a guarantee over the whole population (including rare cases), which matters in clinical decision-making.

- **Technically sound reweighting derivation.** The chain in Equation (1) is non-trivial. The key step—that conditioning on $\{e=1\} = \{T < C\}$ stochastically lowers $T$ (under conditional independence of $T$ and $C$ given $X$), making $\mathbb{P}(T \leq c' \mid e=1, X, W=w) \geq \mathbb{P}(T \leq c' \mid X, W=w)$—is valid and provides a genuine upper bound that enables application of Lei & Candès (2021)'s weighted conformal framework.

- **Double robustness (Theorem 4.2).** Asymptotic exact coverage holds if either (A1) the weight function converges or (A2) the conditional quantile converges with mild regularity. This mutual-compensation property is a strong practical guarantee and is carefully stated.

- **Comprehensive experiments.** Six synthetic settings mimic realistic clinical censoring and treatment imbalance. Robustness to outliers (Figure 3) is specifically tested, where the proposed method maintains coverage while PAC-type methods (Focus, Fused) break down. The real-world NSCLC dataset (541 patients, 124 features) is directly clinically relevant, and the LPB ordering across VMAT vs. IMRT, and across chemotherapy regimens, is consistent with independent clinical literature.

- **LPB optimization.** The proposal to select $\tau^*$ to maximize the LPB test-point-wise (Section 4.1) is practically useful. Table 1 shows the resulting improvement over the naive $\tau = \alpha$ choice is modest but consistent.

---

## Weaknesses

### Fatal
None.

### Major

1. **Coverage guarantee for the $\tau^*$-optimized LPB is not established.** Theorems 4.1 and 4.2 guarantee coverage for any *fixed* $\tau$. The optimized $\tau^*(x) = \arg\max_\tau (\hat{q}_\tau^{(w)}(x) - c_{1-\alpha}^{(w)}(\tau))$ is computed from the same calibration data used to form $c_{1-\alpha}^{(w)}(\tau)$. Since $\hat{L}(\tau^*) \geq \hat{L}(\tau)$ for all $\tau$, choosing $\tau^*$ raises the bound, making the event $\{T(w) \geq \hat{L}(\tau^*)\}$ a strict subset of $\{T(w) \geq \hat{L}(\tau)\}$. Thus, $\mathbb{P}(T(w) \geq \hat{L}(\tau^*)) \leq \mathbb{P}(T(w) \geq \hat{L}(\tau))$, and the per-$\tau$ guarantee does **not** automatically transfer to the data-adaptive $\tau^*$. A uniform-over-$\tau$ coverage argument or a formal treatment of this selection step is missing.

2. **Undiscussed coverage violation in Setting 6.** The paper acknowledges the empirical coverage falls below $1-\alpha$ in Setting 6 and attributes this to weight estimation error, but does not characterize *when* this occurs, how large the shortfall is, or how it relates to the theoretical error term in Theorem 4.1. For a method claiming "exact" coverage, this setting deserves a detailed diagnostic.

### Minor

1. **"Exact" guarantee is asymptotic and weight-estimation-dependent.** Theorem 4.1 gives $\mathbb{P}(\cdot) \geq 1 - \alpha - \frac{1}{2}\mathbb{E}[|\tilde{\omega}(X) - \omega(X)|]$, while Theorem 4.2 is fully asymptotic. The paper's headline claim of "exact" coverage is technically accurate in the marginal sense but is conditional on vanishing estimation error; this nuance should be stated clearly in the introduction and abstract.

2. **No sensitivity analysis for ignorability violations.** Assumption 3.1 ($\{T(1),T(0)\} \perp (W,C) \mid X$) is the paper's core untestable assumption. The Discussion acknowledges the limitation but provides no partial sensitivity analysis (e.g., Rosenbaum-style $\Gamma$-sensitivity or confounding magnitude bounds). Given the clinical motivation, some empirical stress-testing (e.g., deliberately omitting an important covariate) would strengthen the practical claims.

3. **Extreme-weight instability not discussed.** In settings with imbalanced treatment proportions or high censoring rates, $\hat{\gamma}(x) \approx 0$ for some $x$, making $\hat{\omega}(x) = 1/\hat{\gamma}(x)$ very large. This variance inflation in the weighted quantile can lead to uninformative (conservative) LPBs. The paper notes the issue qualitatively in the Discussion but provides no clipping strategy or empirical evaluation of this regime.

### Trivial
- Step (ii) in Equation (1) is labeled as following from the "tower property" but is actually a trivial $\times 1$ insertion of $p(e=1|x,W=w)/p(e=1|x,W=w)$; the substantive inequality is at step (iii). The labeling is slightly misleading but does not affect correctness.

---

## Nice-to-Haves

- A formal coverage guarantee for the $\tau^*$-selected LPB (even an asymptotic one under mild conditions) would significantly strengthen the paper.
- A comparison against doubly robust survival function estimators (e.g., AIPW-based methods) in terms of LPB quality would situate the contribution more broadly.
- A simulation quantifying how coverage degrades as a function of treatment/censoring imbalance would help practitioners calibrate expectations.

---

## Novel Insights

The central novel insight is a tight connection between the correlation structure induced by censoring and the validity of the conformal coverage reduction. Specifically, under conditional independence of $T$ and $C$ given $X$ (a standard non-informative censoring assumption), the event $\{T < C\}$ stochastically lowers $T$—making the conditional CDF $\mathbb{P}(T \leq c \mid e=1, X, W=w)$ an upper bound on $\mathbb{P}(T \leq c \mid X, W=w)$. This inequality, combined with the Radon-Nikodym reweighting between $\mathbb{P}_X$ and $\mathbb{P}_{X|W=w,e=1}$, allows a clean reduction to the covariate-shift weighted conformal framework of Lei & Candès (2021) on the observable uncensored sub-sample—without any asymptotic approximation in the reduction step itself. This insight applies more broadly to any setting where an informative selection event biases outcomes in a monotone direction.

---

## Suggestions

- Provide a formal coverage guarantee for the $\tau^*$-optimized LPB, e.g., by establishing uniform-in-$\tau$ coverage or analyzing the selection step explicitly.
- Quantify in simulations how far coverage falls below $1-\alpha$ in Setting 6 and identify the data characteristics (censoring rate, covariate dimension, weight estimation accuracy) that predict this failure.
- Add a brief sensitivity analysis (e.g., withholding a known confounder from $X$) on the NSCLC dataset to illustrate robustness to ignorability violations.
- Clarify in the abstract/introduction that "exact" means marginal rather than PAC-type coverage, and that residual error depends on weight estimation quality.

---

## Score and Decision

The paper addresses a genuine and important gap—first-ever exact marginal coverage for survival counterfactual LPBs under general right-censoring. The core technical machinery (reweighting + weighted conformal reduction) is elegant and sound. The experiments are thorough and clinically grounded. The primary gap is the missing theoretical treatment of the $\tau^*$ optimization step, which leaves the most practically useful output (the optimized LPB) without a formal coverage guarantee. This is a real but fixable issue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>