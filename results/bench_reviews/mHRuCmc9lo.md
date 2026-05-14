## Summary

This paper studies how a decision-maker should optimally act when given forecasts that satisfy a partial (H-)calibration guarantee. The authors cast this as a minimax problem over conditional expectations consistent with the calibration constraints, characterize the optimal policy via convex duality (Theorem 3.1), and show a sharp transition: when H contains the decision-calibration indicators, the minimax-optimal policy collapses to the plug-in best response to the raw forecast (Theorems 4.1–4.2). This upgrades previously known swap-regret guarantees to full minimax optimality. Practical instantiations include self-orthogonality from squared-loss training and bin-wise calibration. Experiments on two regression datasets illustrate the approach.

## Strengths

- **Decision calibration recovers plug-in minimax optimality.** Theorem 4.1 is the paper's centerpiece: under decision calibration—a substantially weaker condition than full calibration—the minimax-optimal decision rule is the plug-in best response to the forecast. This upgrades swap-regret guarantees (Noarov et al., 2023) to minimax optimality over *all* forecast-to-action policies, not just action-remapping policies. This is a clean, genuinely useful conceptual result.

- **Sharp transition simplifies practical guidance.** Theorem 4.2 and Figure 2 show that once H contains the |A| decision-calibration indicators, the robust policy collapses to plug-in best response; any larger H gives the same policy. This gives a clear, actionable target for practitioners: if they can influence training, decision calibration suffices for minimax-optimal decision-making.

- **General duality characterization.** Theorem 3.1 provides a closed-form minimax optimal decision rule via dual variables that is pointwise computable and scales with the dimension of H. Instantiations for self-orthogonality from squared-loss training (Proposition 4.4) and bin-wise calibration (Proposition 4.5) connect theory to common pipelines without algorithmic modification.

- **Robustness to approximate calibration is quantified.** Appendix B (Theorem B.2) proves that even with ε-slack on decision-calibration constraints, the plug-in best response remains O(m L ε)-minimax optimal, bridging theory and practice.

## Weaknesses

### Major

1. **Experiments are far too thin to support the practical claims.** Only two regression datasets, a single H class (self-orthogonality from squared loss), and no baselines beyond the plug-in policy. Results are point estimates without standard errors or statistical tests—the utility differences are <0.02 on a [0,1] scale and likely within noise. The construction of the adversarial distributions used in the "worst-case" evaluations is not described (the paper only says they are "tailored to the plug-in policy" and "induced by the robust dual," with no algorithmic or procedural details), making the results unverifiable. There is no evaluation of sensitivity to calibration error (linking to Appendix B), training/calibration split, or network architecture. For a paper that claims to provide a "practical recipe," this experimental section does not meet the standard.

2. **The robust policy protects against uncertainty about the conditional outcome but not against covariate shift on f(X).** The ambiguity set Q (Equation 4) only varies the conditional expectation q(v)=E[Y|f(X)=v] while keeping the marginal distribution of f(X) fixed. However, the paper's stated goal is robustness over "all joint distributions over X×Y that are consistent with the promise that f is H-calibrated." In many deployment scenarios, the marginal of f(X) could shift, and the paper's framework does not address this. The decision-calibration collapse result (Theorems 4.1–4.2) also relies on this fixed-marginal structure. The paper does not acknowledge this as a limitation—the Conclusion mentions non-linear utilities but not this scope restriction.

3. **The theoretical techniques are standard.** Theorem 3.1 follows directly from convex duality (Sion's theorem + Lagrangian) given the convex-concave structure. Theorems 4.1–4.2 use Jensen's inequality and the fact that decision-calibration constraints fix the conditional mean within each decision region. The proofs are clean and correct but not technically surprising given the setup. The paper's primary value is in the *insight* (decision calibration ⇔ minimax optimality) rather than the technical machinery.

### Minor

4. **The adversarial distribution construction is underspecified.** The paper describes adversaries "tailored to the plug-in policy" and "induced by the robust dual" but gives no details about how these are computed or verified. For the self-orthogonality case, the worst-case distribution should derive from the dual: q*(v) = argmin_p [val(p) + λ* v p]—but whether this is actually what is used, and how λ* is estimated from finite data, is not stated. This is a reproducibility gap.

5. **The "tractability" of decision calibration depends on |A|.** The paper states that decision calibration is "far more statistically tractable" than full calibration because |H_dec| = |A|. This is true when |A| is small, but for many decision problems |A| could be large, and achieving decision calibration would then scale poorly. The paper does not discuss this caveat.

6. **Exact H-calibration is assumed in the main body.** While the paper relegates approximate calibration to Appendix B (and mentions it briefly in Section 2), the experiments do not test robustness to calibration error. The self-orthogonality property (Proposition 4.4) holds only at a first-order stationary point of expected squared loss; finite-data training and early stopping violate this exactly. The paper would be stronger if the main results and experiments discussed or tested sensitivity to calibration error.

### Trivial

7. **Figure 2 (sharp transition)** is referenced but appears to be a schematic figure with no actual data; its value is limited without quantitative backing.

## Nice-to-Haves

- Add standard errors or confidence intervals to Table 1, and describe the adversarial construction procedure explicitly.
- Compare to simple baselines such as the conservative minimax policy (argmax_a min_y u(a,y)).
- Test sensitivity to calibration error by synthetically perturbing forecasts, linking to Appendix B's theoretical guarantees.
- Plot robust policy decision boundaries on synthetic 2D data to illustrate how the adversarial tilt changes the decision rule.
- Analyze computational cost: how much slower is the robust policy than plug-in for the self-orthogonality case?

## Removed Points

These points are flagged to be removed, treat them with caution:

- "Theorem 3.1 is straightforward / not surprising" — This is a reviewer opinion about technical complexity, not a verifiable weakness. Clean results using standard techniques are a feature, not a bug.
- "Pointwise computability is only true once λ* is known" — This is how duality works for all such problems; not a weakness specific to this paper.
- "Missing related works" — Per instructions, I cannot confirm the existence of missing references.
- "Reproducibility concern about not-yet-released artifacts" — All cited entities are assumed to exist.
- "Theorems 4.2 only holds in minimax sense under fixed-marginal" — This is already subsumed under weakness #2 (fixed-marginal issue).
- Generic formatting/style nitpicks.
- "Self-orthogonality Proposition 4.4 only holds at stationary point" — This is explicitly stated in the proposition; the paper is clear about the assumption.

## Novel Insights

None beyond the paper's own contributions. The review process did not uncover unexpected interpretations or implications beyond what the paper already presents: the key insight is that the hierarchy of minimax-optimal robust policies collapses at decision calibration, a much weaker condition than full calibration.

## Suggestions

1. **Expand the experiments substantially.** Add at least one multi-class classification experiment with decision calibration (directly testing Corollary 4.3), include more baselines (conservative minimax, constant-mean policy), and report error bars. Most importantly, describe how the adversarial distributions are constructed—without this, Table 1 is uninterpretable.

2. **Acknowledge the fixed-marginal limitation explicitly.** The paper should clarify that the ambiguity set Q only perturbs the conditional expectation E[Y|f(X)] while keeping the marginal of f(X) fixed, and discuss when this is or is not a reasonable modeling choice. This would help readers understand the scope of the robustness guarantee.

3. **Test robustness to calibration error.** Run a sensitivity experiment where synthetic noise is added to the forecaster's outputs, and show how the robust policy's performance degrades as ε increases. This would connect the main results to Appendix B and address the concern that exact H-calibration is unrealistic.

4. **Improve presentation of adversarial evaluation.** Provide explicit formulas or pseudocode for constructing the worst-case distributions used in evaluation. This is essential for reproducibility.

## Score and Decision

**Anchor comparison:**

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| `vAU1fo1zRV` — Dimension-Free Decision Calibration for Nonlinear Loss Functions | 7.00 | Stronger technical contribution (dimension-free results, lower bounds). Current paper has cleaner conceptual message but more standard techniques. |
| `m5zdEywl57` — Persuasive Prediction via Decision Calibration | 6.00 | Similar level of theory, but that paper had no experiments. Current paper has thin experiments but still more than that paper. Both rejected in their venues. |
| `UkDte1jM2Q` — Non-Asymptotic Analysis of Efficiency in Conformalized Regression | 6.00 | Strong theory paper with limited experiments, accepted as poster. Current paper has similar theory-to-experiment ratio but the theory here is less technically novel. |
| `NNqi3tBcZr` — Conformal Risk-Averse Decision Making | 3.00 | Tanked by missing proofs. Current paper is substantially stronger. |
| `EYOwByRzU5` — Distributionally Robust Bayesian Optimization | 3.00 | Weak experiments with no baselines led to rejection. Current paper similarly lacks baselines but has stronger theory. |
| `YVzvi34qyc` — Making and Evaluating Calibrated Forecasts | 4.00 | Rejected/withdrawn. Current paper has clearer contribution. |

The paper makes a clean conceptual contribution (decision calibration ⇔ minimax optimality of plug-in) that is genuinely useful for practitioners and theorists working on calibration for decision-making. However, the experimental evaluation is far too thin to support the claimed practical significance (2 datasets, no error bars, underspecified adversarial construction, tiny effect sizes), and the fixed-marginal limitation of the framework is not acknowledged. The theoretical results, while correct and well-presented, rely on standard techniques (convex duality, Jensen). Relative to the anchors, this paper sits below the 7.0 theoretical paper that was accepted but above the 3–4 range papers that had fatal flaws. The closest comparator is m5zdEywl57 (avg 6.0, rejected) which had similar theoretical ambition but weaker experiments.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>