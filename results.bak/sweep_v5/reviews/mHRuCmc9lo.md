Now I have a thorough understanding of both the paper and the calibration landscape. Let me synthesize the final review.

## Summary

This paper develops a minimax-optimal framework for decision-making under ℋ-calibration, a family of weighted calibration conditions. It characterizes the optimal robust policy via duality (Theorem 3.1), and shows a striking collapse result: when ℋ contains the decision-calibration indicators (a tractable class of size |𝒜|), the minimax-optimal policy reduces to the simple plug-in best-response — matching the guarantee of intractable full calibration. The paper also derives robust policies for self-orthogonality (implied by squared-loss training) and bin-wise calibration, with experiments on two regression datasets.

## Strengths

1. **Decision-calibration collapse (Theorem 4.1/4.2) is a genuine theoretical insight.** The result shows that `|𝒜|` test functions suffice to recover the same decision-theoretic semantics as full calibration under the minimax criterion. This upgrades known swap-regret guarantees from decision calibration to full minimax optimality over all forecast-to-action policies — a strictly stronger statement. The stability under enrichment (Theorem 4.2) and the multi-decision-maker extension (Corollary 4.3) are natural and practically relevant.

2. **Clean duality characterization (Theorem 3.1).** The saddle-point characterization reduces policy computation to a finite-dimensional concave maximization (over dual multipliers λ) followed by pointwise minimization, providing structural insight into how the adversary tilts the belief as a function of the forecast v. This is a technically nontrivial advance over prior work that handled only binary outcomes and approximate full calibration (Rothblum & Yona, 2023).

3. **Self-orthogonality from squared-loss training (Proposition 4.4) bridges theory to practice.** Identifying that any model with a linear head trained to stationarity under squared loss automatically satisfies ℋ-calibration with ℋ = {h(v) = v_k} — without any algorithmic intervention — gives practitioners a concrete entry point. The resulting robust policy is tractable (one-dimensional dual maximization via bisection, small convex programs for d>1).

4. **Bin-wise calibration yields a simple closed-form robust policy (Proposition 4.5).** The piecewise-constant characterization (best-respond to the bin mean) is immediately usable by any practitioner who performs histogram binning or isotonic regression as post-hoc calibration.

## Weaknesses

### Fatal

None. The theoretical core is sound and the paper's central claims are supported by the mathematical framework.

### Major

1. **Finite-sample / estimation gap between theory and practice.** The theoretical framework (Theorem 3.1, the dual optimization for λ*, the pointwise minimization for q*) assumes knowledge of population-level expectations over f(X). The experiments handle this by substituting empirical estimates from a calibration set ("We use the calibration data to substitute any population level expectation"), but the paper provides no analysis of how this estimation error propagates: no sample complexity bounds, no guarantee that the empirically estimated policy is approximately minimax optimal, and no discussion of when 20% calibration split data suffices. This weakens the practical claims made in the abstract and introduction. The paper would benefit from at least a discussion of this gap and, ideally, a high-probability bound on the regret relative to the population minimax optimum.

2. **Experimental evaluation is thin for the strength of the empirical claims.** The experiments use only two datasets, both low-dimensional (d=1) regression problems with small action sets (3 actions each). No confidence intervals or standard errors are reported for the mean utilities in Table 1, making it impossible to assess whether the observed differences (e.g., 0.012 improvement on Bike Sharing under worst-case for plug-in) are statistically significant. The comparison includes only two policies (plug-in vs. robust) with no additional baselines — for example, the naive minimax policy (constant action), the unconditional-mean policy, or an oracle policy. While the experiments are presented as a validation of the theory rather than an exhaustive benchmark, the current presentation overclaims relative to the evidence provided.

### Minor

1. **The adversarial construction in the experiments is described only at a high level in the main text.** The paper states that adversarial distributions "respect the ℋ-calibration constraints" and are constructed via "a worst case tailored to the plug-in policy" and "a worst case induced by the robust dual," but the main text does not explain how these are algorithmically constructed — whether they are solved via the dual optimization on the calibration set, whether empirical or population constraints are enforced, etc. Details presumably reside in the appendix, but the main text should provide enough information for a reader to understand what was done.

2. **Limited scope of the experimental evaluation.** The utility functions and action sets are chosen arbitrarily (α=0.9, three hand-picked cost values). While the paper notes that "qualitative conclusions remain the same under other reasonable parameter choices," no sensitivity analysis is shown. The paper tests only the self-orthogonality case (ℋ={h(v)=v}); the decision-calibration collapse result (Theorem 4.1) is not tested experimentally, which would have been a natural next step.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis varying utility parameters (α, C(·)) over a wider range.
- Comparison with the naive minimax policy and the policy that best-responds to the unconditional mean 𝔼[Y].
- A figure visualizing the robust policy a_robust(v) vs. a_BR(v) for the self-orthogonality case, showing how conservatism varies with v.
- A brief note on how the finite-sample estimation of λ* and q* via the calibration set interacts with the saddle-point structure (e.g., rates of convergence).

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"General characterization (Theorem 3.1) does not translate into a practical algorithm"** — The paper explicitly describes the dual optimization as concave (easy), the pointwise minimization as a small convex program over [0,1]^d, and gives explicit forms for d=1 (bisection on a monotone subgradient). The claim that the solution is "efficiently computable" is adequately supported for the cases studied. For a theory paper, demanding full pseudocode and convergence analysis is scope creep.

2. **"Proposition 4.5 is not adequately supported"** — The proof is in the appendix (removed by parser). The claim that the worst-case belief is constant per bin under bin-wise calibration is standard by now (it follows from the constraints only fixing bin-averages and the objective decomposing per bin given linear utility). The main text's reasoning, while terse, points to the correct structure.

3. **"Missing standard errors and more baselines"** — Partly kept as a Major weakness (the thinness of experiments), but the harsh critic's framing that "the results in Table 1 are uninterpretable" and "the experimental evaluation is fundamentally flawed" is overblown. The systematic pattern across both datasets (robust outperforms plug-in under adversarial evaluation, slightly underperforms under i.i.d.) is consistent with the theory and interpretable even without error bars — though error bars would strengthen the claim.

4. **"Section-by-section notes about ℋ-calibration definition"** — These are clarifications, not substantive weaknesses.

5. **Strength Finder's claim about experimental validation being a strength** — While the experiments are supportive, they are too limited (2 datasets, no error bars, no baselines) to be listed as a core strength. The theoretical results are the paper's real strength.

## Novel Insights

The harsh critic and strength finder largely recapitulate the paper's own contributions rather than identifying genuinely novel observations beyond them. One subtle point that emerges from reading both reviews together: the paper shows that the decision-calibration collapse requires the utility to be linear in the outcome (Assumption 2.1). This is a real constraint — risk-averse utilities that depend on outcome variance are excluded. The paper acknowledges this in the conclusion but does not discuss whether the collapse result might degrade gracefully under mild nonlinearity. Understanding this frontier (how much nonlinearity can be tolerated before the robust policy diverges from plug-in) would be a natural next question that the paper's framework enables but does not address.

## Suggestions

1. Provide a finite-sample analysis or at minimum a rigorous discussion quantifying how the plug-in estimation of λ* and q* from calibration data degrades the minimax guarantee. This would significantly strengthen the practical applicability claims.

2. Add standard errors (or confidence intervals) to Table 1 and include at least one additional baseline (e.g., the minimax-constant policy and the unconditional-mean policy) to contextualize the improvements.

3. Add at least one experiment testing the decision-calibration collapse prediction (Theorem 4.1) — e.g., post-process a forecaster to satisfy decision calibration and verify that the robust and plug-in policies coincide.

4. Clarify in Section 5 how the adversarial test distributions are constructed (empirical optimization over the calibration set, solution of the dual, etc.) so the experiments are self-contained in the main text.

5. State the tie-handling assumption explicitly in the proof sketch for Theorem 4.1 (the paper implies ties have measure zero — making this explicit would resolve a reader's reasonable concern).

## Score and Decision

**Calibration anchors (all retrieved in my single batch call):**

| Path | Avg Score | Comparison to Current Paper |
|------|-----------|-----------------------------|
| TId1SHe8JG (Higher-Order Calibration) | 7.50 | Stronger on both theory depth and experiment rigor. Current paper's theory is comparably novel but experiments are weaker. |
| zavLQJ1XjB (Limitations of Temperature Scaling) | 6.67 | Strong alignment between theory and experiments. Current paper has cleaner theory but thinner experimental validation. |
| g6fYDGKeyB (Addressing Misspecification in SBI) | 6.00 | Similar experiment limitations, but current paper's theory is more complete and better motivated. |
| X0epAjg0hd (Reassessing Calibration) | 5.67 | Similar experiment scope (1-2 datasets), comparable contribution level. Current paper's theory results are more novel. |
| 5HpZZbgdeK (Efficient Calibration) | 5.00 | More applied, less theoretical depth. Current paper has stronger theoretical contributions. |
| 7BDUTI6aS7 (Risk Quadrangle) | 3.00 | Poorly organized, unclear contribution. Current paper is far clearer. |
| WoJzHQIIUk (MinMax BNN) | 1.50 | Very poor quality throughout. Current paper is incomparably better structured and substantiated. |

Relative to these anchors, the current paper sits between the 5.67 and 6.67 papers — it has stronger and more novel theoretical contributions than the former, but its experimental validation is thinner than the latter. The theoretical core (Theorems 3.1, 4.1, 4.2, Proposition 4.4) is solid, well-motivated, and clearly presented. The main limitation is the finite-sample gap and the limited experimental scope, which prevent a higher score but do not undermine the validity of the core theory.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>