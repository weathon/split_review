Here is my consolidated review:

## Summary

This paper resolves the open problem of optimal sample complexity for learning the optimal policy in uniformly ergodic average-reward MDPs (AMDPs) under a generative model. The main contribution is achieving \(\widetilde O(|S||A|\tau_{\mathrm{mix}}\epsilon^{-2})\) sample complexity, matching the lower bound of Jin & Sidford (2021). The approach combines an improved analysis of Li et al.'s perturbed model-based planning algorithm for discounted MDPs (yielding optimal DMDP complexity with a low minimum sample size) with a reduction to the AMDP setting.

## Strengths

- **First optimal sample complexity for uniformly ergodic AMDPs**: The paper resolves an acknowledged open problem by achieving \(\widetilde \Theta(|S||A|\tau_{\mathrm{mix}}\epsilon^{-2})\), matching the lower bound from Jin & Sidford (2021). Table 1 clearly shows that all prior upper bounds had strictly worse dependencies on \(\tau_{\mathrm{mix}}\) or \(\epsilon\). This is the first algorithm and analysis to reach the lower bound.

- **Novel combination achieving both optimal complexity and low minimum sample size**: The key technical innovation is a refined analysis of the perturbed model-based planning algorithm (Li et al. 2020) under mixing assumptions. This yields the optimal DMDP rate \(\widetilde \Theta(|S||A|\tau_{\mathrm{minor}}(1-\gamma)^{-2}\epsilon^{-2})\) while maintaining a minimum sample size of only \(\widetilde \Omega(|S||A|(1-\gamma)^{-1})\) — far smaller than the Wang et al. (2023) baseline's \(\widetilde \Omega(|S||A|(1-\gamma)^{-3})\). This improvement is essential for the AMDP reduction to work, and is of independent theoretical interest for uniformly ergodic DMDPs.

- **Clear positioning against existing literature**: The paper provides two detailed tables (Tables 1 and 2) cataloguing existing upper and lower bounds. Section 1.1 explains why prior reduction-based methods (Jin & Sidford 2021, Wang 2022) obtained \(\epsilon^{-3}\) rates, and Section 3.1 explains how the new DMDP analysis overcomes this. The structured exposition makes the contribution well-motivated.

- **Supporting numerical experiments**: The experiments on the hard MDP instance from Wang et al. (2023) demonstrate a \(-0.5\) slope (optimal \(\epsilon^{-2}\) dependence) versus \(-0.33\) for Jin & Sidford (2021), and validate the linear \(\tau_{\mathrm{minor}}\) dependence. These results concretely show the theoretical guarantees translating into practice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Numerical experiments are somewhat limited in scope**: The experiments use only a single family of hard instances (from Wang et al. 2023). The \(\tau_{\mathrm{minor}}\) dependence verification (Figure 1b) is indirect — it fixes sample size proportional to \(\tau_{\mathrm{minor}}\) and checks that error remains constant, rather than directly measuring the sample size needed to achieve a fixed error across varying \(\tau_{\mathrm{minor}}\). Additionally, no confidence intervals or error bars are reported for the regression slopes, making it impossible to assess the statistical significance of the claimed slopes. These are genuine limitations, though they do not undermine the paper's primary theoretical contribution (the paper is first and foremost a theoretical contribution, with experiments as supporting validation).

### Trivial

- The discussion of \(H\) vs \(\tau_{\mathrm{mix}}\) (paragraph before Section 1.1) correctly notes that \(H \leq 8\tau_{\mathrm{mix}}\) and that \(H\) depends on the reward while \(\tau_{\mathrm{mix}}\) does not. The zero-reward example is precise, but the text could briefly clarify why this asymmetry matters for lower bounds (i.e., that \(\tau_{\mathrm{mix}}\) is a more conservative/complexity measure that does not collapse when the reward is degenerate). This is a very minor expositional issue.

## Nice-to-Haves

- A brief sketch in the main text connecting Theorem 3.1 (DMDP error bound) to Theorem 4.2 (AMDP result) — showing how the reduction approximation error and the DMDP estimation error combine under the chosen parameterization — would help the reader follow the flow of the argument without needing to consult the appendix.
- The experiments would be strengthened by including error bars (e.g., shaded regions from multiple replications) and a direct plot of required sample size vs \(\tau_{\mathrm{minor}}\) for a fixed error target.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Missing reduction lemma (Structural)"** — The reviewer states the reduction lemma is never stated and the reader cannot verify how the DMDP error bound translates to the AMDP bound. However, the paper clearly states it follows the reduction methodology of Jin & Sidford (2021) and provides specific parameter choices in Algorithm 2. The full derivation is part of the proof appendix; the parser strips appendix content from all submissions. Per the hard rules, this criticism is removed as it concerns material that exists in the original submission's appendix.

2. **"Theorem 3.1 error bound contains a circular definition"** — The reviewer claims \(\eta_\delta^* = \zeta\delta(1-\gamma)/(9|S||A|^2)\) creates a circular dependency because \(\beta_\delta\) is evaluated at \(\eta_\delta^*\). This is factually incorrect: \(\eta_\delta^*\) is simply a specific numerical value defined in terms of input parameters, and plugging it into \(\beta_\delta\) is standard function composition — there is no circularity. This is a standard practice in theoretical CS/ML for defining log factors in sample complexity bounds. The criticism reflects a misunderstanding of the notation.

3. **"The claim that the DMDP algorithm from Li et al. 2020 can be analyzed to replace \((1-\gamma)^{-1}\) factors with \(\tau_{\mathrm{minor}}\) is stated without any sketch"** — This is a request for more exposition in the main text. The full analysis would be in the appendix (now stripped). The paper correctly identifies the technical challenge and states the result.

4. **"The constant 486 suggests a specific concentration inequality, but without any context, the bound seems ad hoc"** — This is a presentational nitpick about a constant that arises naturally from the analysis (specifically from Bernstein-type inequalities and union bounds). Constants like 486 are standard in sample complexity bounds and reflect the specific concentration arguments used.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add error bars or confidence bands to the experimental figures (with 300 replications, standard errors are readily computable) to strengthen the empirical validation.
- Include a brief sketch in the main text (even 2-3 sentences) showing how the AMDP reduction error and the DMDP estimation error from Theorem 3.1 combine under the parameter choices in Algorithm 2 to yield the final AMDP bound. This would improve readability without requiring the full appendix.

## Score and Decision

The paper makes a significant theoretical contribution by resolving an open problem in RL theory — achieving the optimal sample complexity for uniformly ergodic AMDPs. The technical approach (improved DMDP analysis under mixing + reduction) is sound and clearly motivated. The surviving weaknesses are minor and do not threaten the core claims. The paper is well-written, well-positioned against prior work, and the experiments, while limited, support the theory. This is a strong, publishable paper.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>