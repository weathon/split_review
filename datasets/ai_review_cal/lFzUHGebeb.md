- Decision: Reject
- Avg Score: 2.00
- Scores: 1, 1, 3, 3
Now I have all the evidence I need. Let me write the consolidated final review.

---

## Summary

This paper proposes Variable Forward Regularization (-kF), a generalization of Forward Regularization (-F) for online linear regression that introduces a multiplicative factor *k* to modulate the strength of the unsupervised forward penalty. The authors derive closed-form recursive updates and a regret bound for -kF, showing it subsumes both Ridge (-R, k=0) and Forward (-F, k=1) regularization as special cases. They further propose an adaptive variant (-kF-Bayes) that sets *k* dynamically from the data. Experiments on synthetic data, tabular continual learning benchmarks, and CIFAR-100/10 in CIL/OTCIL settings are presented.

## Strengths

1. **Principled generalization of Forward regularization.** The -kF framework (Theorems 1–3, Remark 1) subsumes -R (k=0) and -F (k=1) as special cases, providing a unified treatment with variable learning rates and closed-form recursive updates. This formalizes the intuitive idea of modulating the forward-penalty strength and is the paper's central conceptual contribution.

2. **Derivation of a regret bound for the generalized method.** Theorem 5 provides an explicit expected regret bound for -kF, and Remark 4 uses growth-rate analysis to show that choosing $0<k<1$ can yield a tighter bound than -F. This attempts to ground the method theoretically, going beyond a purely heuristic proposal.

3. **Adaptive -kF-Bayes removes the need for manual *k* tuning.** The adaptive variant (Theorem 6) sets $k_t$ automatically during online learning, which is practically valuable since the paper demonstrates (and acknowledges) that -kF with a fixed *k* is sensitive to this hyperparameter. Figures 2 and 4b visualize the adaptive *k* trajectories, confirming that the mechanism responds to data.

4. **Competitive empirical results on CL benchmarks.** In tabular and CIFAR-100/10 experiments, edRVFL-kF-Bayes achieves competitive or superior accuracy against a range of baselines (EWC, CRNet, DYSON, GEM, GSS, RanPAC, NICE) with notably lower standard deviations. The CIL and OTCIL evaluation across multiple datasets provides breadth.

## Weaknesses

### Fatal

None.

### Major

1. **Central motivation is contradicted by the paper's own experimental evidence.** The abstract and introduction assert that -F "cannot perform as expected in practice, even possibly losing to -R" and "could not perform as expected in experiments, even possibly failing to -R during OL." However, the numerical simulation (Section 4.1, Figure 1) shows -F *outperforming* -R with "cumulative error decreases significantly" — the paper's own words (line 225). The paper never demonstrates a single case where -F actually underperforms -R. This contradiction undermines the motivation for the entire paper. If -F already outperforms -R in the simplest testbed, the claimed "failure" needs concrete evidence, not just assertion.

2. **Regret bound in Theorem 5 has an unstated domain restriction.** The bound is 
   $$\frac{k}{2}Y_m^2 d\,\ln\!\left(1+\frac{T X_m^2}{\lambda+(k-1)X_m^2}\right)$$
   with only "$k>0$" as condition. For $0<k<1$, the denominator $\lambda+(k-1)X_m^2 = \lambda - (1-k)X_m^2$ can become zero or negative unless $\lambda > (1-k)X_m^2$ holds. When the denominator is zero, the argument is undefined; when negative and sufficiently large in magnitude, the argument of the logarithm becomes non-positive. The paper never states or discusses this condition. Since the paper emphasizes $0<k<1$ as the regime giving tighter bounds (Remark 4), the bound is not established for its claimed operating range without a nontrivial (and unstated) assumption about $\lambda$ relative to $X_m^2$.

3. **The -kF-Bayes adaptive update lacks derivation and justification.** Theorem 6 presents the update $k_{t+1}=k_t=x_t^T\eta_t x_t$ with the claim that it is "based on Bayesian learning and distribution estimation." However, no derivation, optimization principle, or link to the regret analysis connects this specific rule to Bayesian reasoning. The notation $k_{t+1}=k_t$ is confusing — it is unclear whether $k$ changes across steps or is constant within a step. Without a principled foundation, -kF-Bayes is a heuristic whose behavior is not predictable from the theory, weakening what the paper presents as a main contribution.

### Minor

1. **Theory-experiment gap in evaluation metrics.** The theoretical analysis concerns relative regret for online *linear regression* (cumulative squared-error loss relative to an offline expert). The CIL/OTCIL experiments report accuracy (%) and "regret" curves that are not clearly defined relative to the theoretical quantity in Theorem 5. No experiment measures the actual bound or verifies whether -kF's theoretical advantage (tighter bound) translates into practice. The connection between the theory and the empirical claims is loose.

2. **Uncontrolled tuning advantage in tabular experiments.** SMAC3 optimizes hyperparameters for all methods, but for -kF it additionally optimizes $k$ — a whole extra degree of freedom that -R and -F do not have. The paper acknowledges this (line 239: "Note the $k$ of $-k\mathrm{F}$ was optimized") and -kF-Bayes partially addresses it (no $k$ tuning needed), but the comparison between -kF (with optimized $k$) and -R/-F (without an equivalent tunable parameter) is not apples-to-apples. An ablation controlling this — e.g., testing -kF with fixed $k$ against -R/-F with optimized $\lambda$ — is missing.

3. **The -R bound in Equation (4) is stated without citation.** The bound $2Y_m^2 d\,\ln(\frac{T X_m^2}{\lambda}+1)$ is presented without reference to the standard result (e.g., Azoury & Warmuth, 2001). Since the paper's claim that -F is "4 times better than -R" depends critically on the constants in these bounds, the lack of citation for the -R bound is a scholarship gap. It is impossible for the reader to verify whether this bound, with its specific constant, is standard or derived under a non-standard setup.

### Trivial

None.

## Nice-to-Haves

- The paper would benefit from showing a concrete failure case where -F underperforms -R, even a simple synthetic one, to validate the motivating claim.
- A sensitivity analysis of -kF's performance across a range of $k$ values on real CL datasets would clarify how critical $k$ tuning is.
- Statistical significance tests (e.g., paired tests across folds) would strengthen the tabular experimental claims.
- Convergence or boundedness properties of the $k_t$ sequence in -kF-Bayes are not analyzed.

## Removed Points

- **"Theorem 3 contains several typos; $\eta_{t+1}^\dagger$ is used as both a matrix and its inverse."** — The notation is dense but internally consistent: $\eta_{t+1}^\dagger$ is always a matrix (the inverse of $\eta_0^{-1}+\sum x_i x_i^T$). The Woodbury-formula updates in lines 109–110 are correct. This criticism misunderstands the notation.
- **"The -kF-Bayes notation $k_{t+1}=k_t$ is incoherent."** — While confusing, the likely intended meaning is that $k$ is computed as $x_t^T\eta_t x_t$ and then used throughout step $t$. The notation is awkward but not incoherent; this is a presentation issue the paper can clarify. (This point is subsumed under the broader Major weakness about missing derivation.)
- **"Missing appendix/proofs."** — The parser strips these; they exist in the original submission. Removed per hard rules.
- **"The bound comparison in Remark 4 uses $\hat{X}_m$ and $\hat{Y}_m$ which are running maxima; the inequality is not rigorous."** — This is how running-parameter adversarial bounds work; it is standard practice. The criticism is not substantive.
- **Various formatting, typo, and grammar nitpicks.** — Parser artifacts, not author errors.

## Novel Insights

The reviews do not reveal genuinely novel observations beyond what the paper itself contributes. The contradiction between the paper's stated motivation and its own experimental evidence is the most salient meta-insight: it suggests the paper may have been motivated by anticipated failure modes of -F in long task streams or non-i.i.d. settings that the synthetic experiment in Figure 1 (i.i.d. Gaussian features) does not test. This pointing toward a potential mismatch between claimed and actual experimental scope is worth noting but does not constitute a new discovery.

## Suggestions

1. **Reconcile the motivation with the evidence.** Either provide a concrete example (synthetic or real) where -F underperforms -R, or moderate the claims about -F's failure to match what the paper actually demonstrates.
2. **Fix the regret bound.** State the condition $\lambda > (1-k)X_m^2$ required for the bound to be valid when $0<k<1$, or use a different bounding technique that avoids the denominator issue entirely.
3. **Derive or motivate the -kF-Bayes update.** Explain why $k_t = x_t^T\eta_t x_t$ follows from a Bayesian principle, or present it as a heuristic with empirical justification.
4. **Align theory and experiments more closely.** Measure the relative regret (as defined in Theorem 5) in the synthetic experiments to verify the bound is not vacuous and the trend matches the theory.
5. **Add a controlled comparison.** Compare -kF with a fixed *k* against -R and -F with optimized $\lambda$, to separate the benefit of the -kF formulation from the benefit of the extra tunable parameter.
