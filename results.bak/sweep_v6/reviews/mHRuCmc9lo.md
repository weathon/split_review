Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper studies how a decision maker should map ℋ-calibrated forecasts to actions in a minimax-optimal way. The authors characterize the optimal robust policy via duality (Theorem 3.1) and then prove a sharp transition result: when ℋ contains the decision-calibration indicators (just |𝒜| test functions), the optimal robust policy collapses to the simple plug-in best response — the same guarantee as full calibration but far more tractable (Theorem 4.1). Beyond decision calibration, the paper shows that self-orthogonality from squared-loss training (Proposition 4.4) and bin-wise calibration (Proposition 4.5) yield specific, efficiently computable robust policies. Experiments on two regression datasets illustrate the theoretical predictions.

## Strengths

- **Theorem 4.1 (decision calibration ⇒ plug-in best response optimality):** This is the paper's central theoretical result. It proves that under the tractable condition of decision calibration, the minimax-optimal robust policy coincides with the simple plug-in best response, upgrading previously known swap-regret guarantees to minimax optimality. The proof via invariance of the plug-in policy's expected utility is clean and insightful.

- **Theorem 3.1 (duality characterization of optimal robust policy):** Provides a closed-form, duality-based solution for the minimax decision rule under any finite-dimensional ℋ-calibration, showing the policy reduces to a best response to an adversarially tilted distribution. The characterization is elegant and the computational procedure (two-stage: optimize dual multipliers, then pointwise minimize) is clearly explained.

- **Sharp transition identification (Theorems 4.1–4.2):** The paper pinpoints decision calibration as the exact threshold at which the robust policy collapses to the plug-in rule. This is a crisp, non-obvious result — one might expect a gradual transition, but the paper shows a sharp one. Figure 2 clearly illustrates this.

- **Corollary 4.3 (simultaneous plug-in optimality):** Extends the result to multiple downstream decision problems, showing that a single decision-calibrated forecaster can serve many decision makers simultaneously — a practically important property.

- **Practical connectors bridging theory to practice:** Proposition 4.4 shows that any model with a linear last layer trained to stationarity under squared error automatically satisfies a useful ℋ-calibration condition (self-orthogonality). Proposition 4.5 gives a closed-form robust policy for bin-wise calibration. These show the framework connects to real training pipelines.

- **Clear conceptual framing:** The "robustness bridge" between fully conservative and fully aggressive extremes (Figure 1) is well-motivated and clearly presented, making the paper's contribution easy to understand.

## Weaknesses

### Fatal
None.

### Major
- **Insufficient experimental detail and no variance estimates:** The adversarial evaluation in Section 5 describes two types of worst-case distributions ("tailored to the plug-in policy" and "induced by the robust dual") at a high level but does not specify exactly how these test distributions were constructed from the dual solution or how the test-time Y values were generated. Additionally, no error bars, standard deviations, or confidence intervals are reported for any of the utility numbers in Table 1. Given the small differences between methods (e.g., 0.474 vs 0.463 under i.i.d. for Bike Sharing), the reader cannot assess whether these are statistically meaningful or within noise. This weakens the empirical validation — though the paper's main contribution is theoretical, the experiments are presented as supporting evidence and should be held to a higher standard.

### Minor
- **Population-level theory without finite-sample analysis:** The optimality guarantees (Theorems 3.1, 4.1, 4.2) are proven at the population level, assuming access to exact expectations. The paper mentions using a calibration split to estimate these quantities (Section 5, line 299: "We use the calibration data to substitute any population level expectation") but provides no discussion of sample complexity, convergence rates, or how estimation error in the dual multipliers affects the finite-sample performance of the robust policy. This is standard practice in theoretical ML papers, but a brief acknowledgment of the gap would strengthen the paper.

- **Only two datasets with simple action sets:** The experimental evaluation uses two regression datasets with 3 actions each. While reasonable for illustration, the scope is limited. The paper would benefit from at least one synthetic experiment precisely controlling the ℋ-calibration level to visually demonstrate the sharp transition predicted by theory (e.g., comparing ℋ = ∅, ℋ = ℋ_dec, and ℋ = full calibration for a binary outcome, two-action setup).

- **Missing characterization of the gap for ℋ strictly weaker than decision calibration:** The paper states a "sharp transition" at decision calibration but does not analyze what happens when ℋ is a proper subset of the decision-calibration indicators. Is there a monotonic decrease in worst-case utility as ℋ shrinks? A simple synthetic example would clarify the behavior.

### Trivial
None.

## Nice-to-Haves

- **Visualization of the learned q* function:** For the self-orthogonality case (ℋ = {h(v)=v}), plotting the estimated worst-case conditional expectation q*(v) as a function of the forecast v, overlaid with the 45° line, would visually confirm the "tilt" predicted by theory.
- **Approximate ℋ-calibration demonstration:** The paper mentions Appendix B on approximate calibration. An experiment showing how small calibration error (e.g., adding noise to forecasts) reduces the advantage of the robust policy would strengthen the practical claims.
- **Characterization of the monotonic gap for intermediate ℋ classes** between empty and decision calibration.

## Removed Points

- **"Does not specify whether the same adversarial q* was used for both policies":** The paper clearly states two distinct adversaries — "a worst case tailored to the plug-in policy" and "a worst case induced by the robust dual, tailored to the robust policy" (Section 5, lines 275–276). This criticism misunderstands the experimental design.
- **"Methodological gap — presupposes knowledge of marginal distribution":** The paper explicitly acknowledges using calibration data for estimation (line 299). The population-level framing is standard in theoretical ML and the finite-sample issue is common to essentially all theory papers of this type. This is not a genuine weakness.
- **Formatting/style nitpicks** from the harsh critic (not present in this review input).

## Novel Insights

The key insight that emerges across the reviews — and that goes beyond the paper's own explicit framing — is that the minimax lens exposes a fundamental structural property of calibration constraints: decision-calibration tests (indicator functions of best-response regions) are the *minimal* information needed to neutralize the adversary. This is reminiscent of how sufficient statistics capture all relevant information about a parameter, but here the "sufficiency" is about rendering adversarial tilt powerless. The paper's result that any ℋ containing these |𝒜| indicators collapses the robust policy to the plug-in rule means that forecasters do not need to be "correct in every detail" — they only need to be correct about which action is best, in expectation over each decision region. This reframes the practical goal of calibration from pointwise accuracy to decision-region accuracy, which is a substantially more achievable target.

## Suggestions

1. **In the experimental section, report standard deviations** (over multiple train/calibration/test splits) for all utility values. At minimum, describe the exact procedure used to construct the adversarial test distributions so the experiments are reproducible.

2. **Add a controlled synthetic experiment** demonstrating the sharp transition: construct a simple binary-outcome, two-action setting and show the robust policy's worst-case utility for ℋ = ∅, ℋ = {1_{R_a}} (decision calibration), and ℋ = {all functions} (full calibration). This would visually confirm the "collapse" predicted by Theorem 4.1.

3. **Include a brief discussion** acknowledging the population-level nature of the theoretical guarantees and how sample-based estimation of dual multipliers and conditional expectations affects finite-sample performance, even if formal sample complexity bounds are left for future work.

## Score and Decision

**Calibration anchors (all from `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`):**

- **TId1SHe8JG.md** (avg 7.50, Accept) "Provable Uncertainty Decomposition via Higher-Order Calibration" — Stronger experimental validation and similarly strong theory. This paper below due to weaker experiments.
- **uuPkll6i7m.md** (avg 6.75, Accept) "Certification of Uncertainty Calibration under Adversarial Attacks" — Comparable level. This paper has stronger theory but thinner experiments.
- **g6fYDGKeyB.md** (avg 6.00, Reject) "Addressing Misspecification in SBI" — Mixed reviews due to methodological concerns. This paper has cleaner theory and fewer assumptions.
- **X0epAjg0hd.md** (avg 5.67, Accept) "Reassessing Calibration of ML Models" — Useful meta-contribution, thin experiments (1 dataset). This paper has stronger theoretical depth.
- **XM7INBbvwT.md** (avg 4.67, Reject) "Does Calibration Affect Human Actions?" — Interesting but thin HCI study. This paper is clearly stronger theoretically.
- **34xYxTTiM0.md** (avg 5.50, Reject) "Optimizing Calibration by Gaining Aware of Prediction Correctness" — Incremental contribution. This paper more novel.
- **WoJzHQIIUk.md** (avg 1.50, Reject) "MinMax Bayesian Neural Networks" — Poorly written, no clear contribution. Not comparable.
- **92yrETgM6G.md** (avg 4.00, Reject) "Calibration Attack" — Limited framing. This paper significantly stronger.

The paper makes a genuine, theoretically significant contribution — the sharp transition at decision calibration is a novel and non-obvious result with practical implications. The duality framework is clean and well-presented. The main weakness is the thin experimental validation (no error bars, limited detail on adversarial construction), but the paper's core claims stand on their theoretical merits. Positioned relative to anchors: above methodology papers in the 5–6 range, slightly below the strongest calibration theory papers (7.5) due to weaker experiments.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>