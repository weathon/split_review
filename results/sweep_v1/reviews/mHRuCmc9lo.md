Now let me write the consolidated review.

## Summary

The paper develops a minimax-optimal decision-making framework for acting on ℋ-calibrated forecasts — predictions that satisfy only partial calibration guarantees defined by a finite-dimensional test class ℋ. The core contributions are: (i) a duality-based characterization of the optimal robust policy (Theorem 3.1), (ii) the result that decision calibration — a tractable condition significantly weaker than full calibration — is sufficient for the plug-in best response to be minimax optimal (Theorems 4.1–4.2), and (iii) identification of ℋ-classes that arise naturally from standard training pipelines (self-orthogonality under squared loss, bin-wise calibration) with their associated closed-form robust policies. Experiments on two regression datasets support the theoretical predictions.

## Strengths

1. **Novel and principled theoretical framing (Theorems 3.1, 4.1–4.2).** Casting the decision problem as a minimax optimization over distributions consistent with ℋ-calibration provides a clean connection between weak calibration guarantees and actionable policies. Theorem 3.1 gives a general duality-based characterization for any finite-dimensional ℋ; Theorems 4.1–4.2 prove that decision calibration (only |𝒜| test functions) is sufficient for plug-in optimality, recovering the same semantics as full calibration. This upgrades previously known swap-regret guarantees to full minimax optimality and identifies a crisp, attainable target for forecaster design.

2. **Sharp transition insight (Figure 2, Theorem 4.2).** The paper shows that the minimax-optimal policy collapses from fully conservative to plug-in best response exactly when ℋ contains the decision-calibration indicators, with no gradual enrichment possible. This is a clean and non-obvious result.

3. **Practical ℋ-classes from training pipelines (Propositions 4.4–4.5).** The identification of self-orthogonality from squared-loss stationarity and bin-wise calibration from post-hoc recalibration means the framework applies without requiring custom calibration algorithms. These results are concrete and directly usable.

4. **Empirical support for the predicted pattern (Table 1).** On both Bike Sharing and California Housing, the robust policy outperforms the plug-in best response under adversarial distributions respecting the ℋ-calibration constraints, while maintaining competitive nominal performance. The qualitative pattern across all six columns matches the theory's predictions.

## Weaknesses

### Fatal
None.

### Major
1. **The "worst-case for plug-in" adversary is not described.** The paper describes two adversarial evaluations: (i) a worst-case tailored to the robust policy (which comes from the dual q* in Theorem 3.1) and (ii) a worst-case tailored to the plug-in best response. The construction of adversary (ii) is not specified — it cannot be the same q* (which solves min_p{val(p) + ...} for the robust policy's val(p)). Without knowing how the plug-in-tuned adversary is computed, the reader cannot verify whether it correctly solves min_{q∈Q} E[u(a_BR(f(X)), q(f(X)))], and therefore cannot assess the central empirical claim that the robust policy outperforms plug-in under this adversary. This gap undermines the interpretability of the experimental results in Table 1.

2. **No measures of uncertainty for any experimental result.** Table 1 reports mean utilities without confidence intervals, standard errors, or significance tests. The utility differences under the robust adversary are small (0.402 vs 0.410 on Bike Sharing; 0.160 vs 0.164 on California Housing), and without uncertainty quantification it is impossible to determine whether these differences are meaningful or simply noise from finite test samples.

### Minor
3. **No empirical verification of how well the self-orthogonality conditions hold.** Proposition 4.4 gives exact moment conditions at a population-level stationary point. The two-layer MLP is trained on finite data, so the conditions hold only approximately. The paper does not report the empirical moment errors (e.g., ∥E[f(X)(Y−f(X))]∥ on the calibration split) or analyze how approximation quality affects the robust policy's performance. This makes it unclear whether the experimental setup satisfies the assumptions of the theory to a reasonable degree.

4. **The sensitivity of results to utility parameters is claimed but unsubstantiated.** The paper states (line 297) that "qualitative conclusions ... remain the same under other reasonable parameter choices" without providing any supporting evidence (e.g., results under alternative α or C(·) values).

5. **Missing architectural and training details.** The two-layer MLP's hidden size, activation function, learning rate, optimizer, number of epochs, and other hyperparameters are not reported. Sample sizes for the train/calibration/test splits are not given. While these omissions are common for theoretically-oriented papers, they hinder reproducibility of the experimental component.

6. **The claim that decision calibration is "substantially weaker and more tractable" (vs. full calibration) is not quantified.** The paper correctly states that the test class size is |𝒜| (which may be small), but a sample complexity comparison or reference to known rates would ground this claim more solidly.

### Trivial
None.

## Nice-to-Haves

- An experiment with a forecaster that is explicitly decision-calibrated (e.g., via the methods of Noarov et al., 2023) would directly validate Theorem 4.1's headline result.
- A visualization showing a_robust(v) vs. a_BR(v) as functions of v for the one-dimensional regression setting would illustrate how the robust policy deviates from plug-in when calibration constraints are weak.
- An experiment with bin-wise calibration (Proposition 4.5) would provide another test of the framework beyond self-orthogonality.
- Discussion of computational tractability when ℋ is larger (beyond the small-dimensional cases studied) would be helpful for practitioners.

## Removed Points
These points were raised by reviewers but are removed after verification against the paper:

- **"Self-orthogonality only extracts d of the d^2 conditions provided by Proposition 4.4."** — Factually incorrect. The ℋ-calibration definition (Eq. 2) uses h(f(X)) as a scalar times the d-dimensional vector (Y−f(X)), so each of the d test functions h_j(v)=e_j^⊤ v produces d equations, yielding d^2 constraints total, which match the matrix equation.
- **"No experiment with a decision-calibrated forecaster."** — The paper's experiments are explicitly scoped to the self-orthogonality case (Proposition 4.4), which is a different contribution from Theorem 4.1. Asking for a decision-calibration experiment is scope creep.
- **"No experiment with bin-wise calibration."** — Same scope-creep reasoning.
- **"Missing related works."** — Removed per policy; external verification is not possible.
- **"The adversarial evaluation procedure is completely unspecified."** — Overstated. The robust-tuned adversary is described (derived from the dual q* in Theorem 3.1). Only the plug-in-tuned adversary's construction is missing. The stronger claim ("completely unspecified") is incorrect.
- Pure formatting/style criticisms and missing appendix/proof references — parser artifacts, removed per policy.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the construction of both adversarial distributions.** For the plug-in-tuned adversary, describe the optimization problem and how it is solved (e.g., does it use a similar dual with val_BR(p) = u(a_BR(·), p)?). Providing the objective and algorithm would make Table 1 interpretable.
2. **Add confidence intervals or error bars to Table 1**, e.g., via bootstrapping the test set. This is essential given the small magnitude of some utility differences.
3. **Report empirical moment errors on the calibration split** (e.g., the norm of the empirical average of f(X)(Y−f(X))), to verify that the self-orthogonality condition approximately holds.
4. **Provide a brief sensitivity analysis** showing results under at least one alternative set of utility parameters (α, C(·)), or remove the unsubstantiated claim of robustness.

## Score and Decision

**Anchor comparison for calibration:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Provable Uncertainty Decomposition via Higher-Order Calibration | 7.50 | Stronger theory + experiments than current paper's experiments. Current paper's theory is comparably strong but experiments are less thorough. |
| Towards Certification of Uncertainty Calibration under Adversarial Attacks | 6.75 | Both have decent theory + experiments. Current paper has richer theory; anchor has more rigorous experiments. Roughly comparable. |
| Reassessing How to Compare and Improve Calibration | 5.67 | Accepted but experiments limited to one dataset. Current paper has stronger theoretical contributions and two datasets — better overall. |
| Does Calibration Affect Human Actions? | 4.67 | Rejected — a user study with weak methodology. Current paper's theory is far more rigorous. |
| MinMax Bayesian Neural Networks | 1.50 | Rejected — unclear contribution, poor presentation. Not comparable to current paper. |

The paper makes a strong theoretical contribution: a clean duality characterization for robust decisions under ℋ-calibration, and the non-trivial finding that decision-calibration suffices for plug-in optimality. The experiments support the theory but have concrete gaps — the main one being that the construction of one of the two adversarial evaluators is not described, and the results lack any uncertainty quantification. These are addressable in a revision. Relative to the anchor set, the paper's theoretical depth is at the level of the 7.50 and 6.75 accept papers, while the experimental rigor lags behind both. A score of 6.5 reflects this balance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>