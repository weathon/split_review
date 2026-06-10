## Summary

This paper proposes SANIA, a general optimization framework (Definition 1, Eq. SANIA) that unifies SGD, SPS, Preconditioned SGD, Cubic Regularized Newton, and SP2 as special cases of a single constrained minimization problem. Using this framework, the authors derive several new methods: a Stochastic Cubic Newton with Polyak step-size, SANIA Quasi-Newton (with step-size provably bounded by 1), scale-invariant variants of AdaGrad and Adam (AdaGrad-SQR, Adam-SQR) obtained by removing square roots from preconditioners, and a PCG-based Newton method for non-convex functions. The paper also provides a scale-invariance analysis showing that removing square roots from diagonal preconditioners yields invariance to diagonal basis transformations.

## Strengths

- **The SANIA framework reveals a previously unrecognized structural connection: SP2 is a Stochastic Cubic Newton with Polyak step-size (line 337).** This is a genuine insight that was not obvious from prior work and only emerges from the unified formulation. The paper cleanly derives how setting different parameters in Eq. SANIA recovers SGD, SPS, Preconditioned SGD, Cubic Regularized Newton, and SP2 (Sections "Existing methods" and "Proposed methods").

- **The scale-invariance analysis (Section 2.3) provides a principled explanation of why removing square roots from AdaGrad/Adam preconditioners yields invariance to diagonal transformations.** The paper formally shows (lines 418–427) that the standard preconditioners break scale invariance while the square-root-free variants (AdaGrad-SQR, Adam-SQR) restore it, with empirical confirmation in Figure 2 showing identical convergence on original and scaled data.

- **SANIA Quasi-Newton step-size λ_t is provably bounded by 1 (Eq. 367), strictly safer than the PSPS step-size from prior work.** The paper explicitly contrasts this improvement (line 369), showing a concrete analytical advantage over the existing PSPS method.

- **Figure 1 demonstrates remarkable step-size robustness across ~25 orders of magnitude on the colon-cancer dataset with logistic regression.** SANIA achieves 100% accuracy after 10 epochs for every learning rate in \([2^{-20}, 2^{5}]\), while Adam, AdaGrad, and AdaDelta degrade significantly at non-optimal rates.

- **The paper derives the first Stochastic Cubic Newton method with Polyak step-size** (Eqs. 326–335), bridging second-order optimization and Polyak step-size methods, and provides a practical SR-1/PCG construction for non-convex problems (Section "SANIA PCG for Newton method for non-convex functions").

## Weaknesses

### Major

- **Severe mismatch between the paper's framing and the experimental validation.** The abstract opens with "training Deep Neural Networks (DNNs)" and the introduction frames the contribution as addressing DNN training. The contributions list promises "comprehensive experiments encompassing a diverse range of scenarios, including both convex and non-convex settings" (line 109). However, the experiments are limited to logistic regression (convex) and non-linear least squares (a shallow non-convex model) on three tiny LibSVM datasets (colon-cancer, duke, leukemia) plus synthetic data. **There are zero experiments on any architecture that qualifies as a deep neural network.** The paper also claims "all presented variations of SANIA outperform other adaptive optimization methods" (line 460), but the baselines include only Adam, AdaGrad, and AdaDelta — no prior Polyak step-size methods (SPS, PSPS, mSPS, AdaSLS, SP2) are compared against, despite these being the most directly relevant baselines for a paper extending the Polyak step-size paradigm. Given that SANIA is presented as a generalization of SPS/PSPS/SP2, the absence of these comparisons makes it impossible to assess whether the framework yields practical benefit over existing Polyak methods.

- **No convergence theory for any of the proposed algorithms.** The paper introduces multiple new methods — Stochastic Cubic Newton Polyak, SANIA Quasi-Newton, SANIA AdaGrad-SQR, SANIA Adam-SQR, SANIA PCG — but provides **zero theorems, iteration complexity bounds, or convergence guarantees** for any of them. For the Cubic Newton variant (Eqs. 326–335), the update involves a case distinction requiring \(L_2\) (the Hessian Lipschitz constant, which is generally unknown) and a line-search when a condition fails, yet no analysis is given for convergence under misspecified \(L_2\). As the paper is proposing new optimization algorithms at a top venue, the complete absence of theoretical validation is a significant gap.

- **No numerical results, standard deviations, or variance reporting.** All results are presented as convergence curves with no tables of final accuracy/loss values, no multiple seeds, and no statistical significance measures. On datasets with fewer than 100 samples (colon-cancer, duke, leukemia), single-run results can be heavily influenced by data splits and initialization, making the evidence effectively anecdotal.

- **The "parameter-free" claim is overstated.** While SANIA eliminates the learning rate for several variants, the Cubic Newton Polyak method requires the Hessian Lipschitz constant \(L_2\) and a line-search (lines 283, 335). The AdaGrad-SQR and Adam-SQR methods still require momentum parameters \(\beta_1, \beta_2\). The paper does not discuss how to set these or test sensitivity to them.

### Minor

- **The framework, while conceptually interesting, is not clearly shown to yield practical benefit over deriving the same methods directly from PSPS or SP2.** The paper would benefit from sharper differentiation between what the framework adds versus what was already available from PSPS (Abdukhakimov et al. 2023) and SP2 (Li et al. 2022). The bounded step-size claim for SANIA Quasi-Newton over PSPS is a genuine improvement, but no empirical comparison to PSPS is provided.

- **Scale invariance experiments use only two scaling factors (k=2 in Figure 2, k=6 in Figures 3–4) and synthetic scaling.** The paper does not evaluate on naturally ill-conditioned problems where scale invariance would matter most.

- **Computational overhead of Hessian-based variants (Cubic Newton, PCG) is not discussed or measured.** The PCG method requires solving linear systems via conjugate gradient, which itself requires Hessian-vector products per iteration; the per-iteration cost relative to standard SPS or SGD is not analyzed.

- **The paper assumes the interpolation condition (Assumption 1) throughout but does not discuss its validity on the experimental datasets.** Logistic regression on datasets with d < n is not necessarily overparameterized, so interpolation may not hold, yet the analysis depends on it.

### Trivial

None.

## Nice-to-Haves

- Compare SANIA variants directly to SPS, PSPS, mSPS, AdaSLS, and SP2 to establish practical benefit.
- Add experiments on actual neural network architectures (even small-scale, e.g., an MLP on MNIST) to substantiate the DNN framing.
- Provide at least basic convergence theory for one method (e.g., linear convergence under interpolation for SANIA Quasi-Newton, which would follow from standard SPS theory with preconditioning).
- Report numerical results in tables with standard deviations over multiple seeds.
- Analyze the computational cost per iteration for the second-order variants (Cubic Newton, PCG).

## Removed Points

The following points from the harsh critic review are removed or demoted per the filtering rules:

- *"The framework does not clearly yield practical benefit over deriving the same methods directly"* — retained but demoted to Minor since the framework does reveal structural insights (SP2 = Cubic Newton) that are non-obvious.
- *"No discussion of when the implicit constrained subproblem has a closed-form solution"* — REMOVED. The paper explicitly acknowledges "the generality of this framework makes it difficult to propose an explicit step" (line 149) and then focuses on solvable cases.
- *"No experiments with mini-batches larger than 16"* — REMOVED as a generic request for more experiments beyond what is needed to support the paper's claims.
- *"No description of hyperparameter choices"* — REMOVED (per rule: nitpicks about reproducibility/undisclosed hyperparameters in a potentially stripped appendix). However, the broader concern about baseline fairness is retained in the Major weaknesses.
- *"Figures are not described with enough quantitative detail"* — REMOVED as a presentation nitpick.
- *"The paper does not discuss what happens when interpolation is violated"* — REMOVED as out-of-scope for a paper that explicitly operates under the interpolation assumption, though noted as a scope limitation.
- *"Demand for convergence theory for all methods"* — The core criticism about no theory is retained; the demand for complete theory for every method is softened to a suggestion.

## Novel Insights

The SANIA framework's discovery that SP2 is equivalent to a Cubic Newton method with Polyak step-size is the most novel finding in the reviews — it is a structural insight that only emerges from the unification that the framework provides. Additionally, the observation that removing square roots from AdaGrad/Adam restores scale invariance is a simple but non-obvious geometric insight that could inform future preconditioner design. The bounded step-size guarantee for SANIA Quasi-Newton (λ_t ≤ 1) over PSPS is a concrete, theoretically grounded improvement.

## Suggestions

1. **Rescope the claims.** Either remove the DNN framing and honestly state that the paper evaluates on convex and mildly non-convex problems with tabular data, or add neural network experiments to substantiate the DNN connection.
2. **Add direct comparisons to prior Polyak methods** (SPS, PSPS, mSPS, AdaSLS, SP2) in the experiments. Without these, it is impossible to judge whether SANIA variants improve upon existing methods.
3. **Add at least one convergence theorem** — e.g., linear convergence under interpolation for SANIA Quasi-Newton (which follows naturally from SPS theory with preconditioning).
4. **Report numerical results with standard deviations** over multiple random seeds.
5. **Discuss the cost of Hessian-based methods** relative to first-order alternatives and clarify the settings where the additional cost is justified.

## Score and Decision

**Score:** 5.0  
**Decision:** Reject

The paper's conceptual contributions — the SANIA framework, the SP2–Cubic Newton connection, and the scale-invariance insight — are genuine and interesting. However, the paper as submitted has a severe claim-evidence gap: it frames the work as relevant to DNN training and promises comprehensive experiments, yet evaluates only on three tiny tabular datasets with no comparison to the most relevant prior methods (existing Polyak step-size methods), no convergence theory for any proposed algorithm, and no numerical precision or variance reporting. These weaknesses collectively prevent acceptance at a top venue. The paper could become a strong submission with honest rescoping, proper baselines, and at least basic theory.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>