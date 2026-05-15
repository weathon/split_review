Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper studies how a conservative decision-maker should act when given forecasts that satisfy only weak ("partial") calibration guarantees, rather than the intractable full calibration. The authors formalize this as a minimax optimization problem over an ambiguity set of distributions consistent with $\mathcal{H}$-calibration, derive a closed-form dual characterization of the optimal robust policy (Theorem 3.1), and prove a striking "sharp transition" result: once the test class $\mathcal{H}$ contains the decision-calibration indicators, the minimax-optimal policy collapses to the simple plug-in best response (Theorems 4.1–4.2). Practical instantiations are given for self-orthogonality from squared-loss training and for bin-wise calibration, with experiments on two regression datasets.

## Strengths

1. **Clean theoretical framework with a surprising collapse result.** The paper provides the first systematic characterization of minimax-optimal decision policies under $\mathcal{H}$-calibration. Theorem 3.1 gives a closed-form dual solution, and Theorems 4.1–4.2 show that decision calibration—a tractable condition requiring only $|\mathcal{A}|$ test functions—suffices for the plug-in best response to be minimax optimal. This "sharp transition" is genuinely striking and reframes the debate about what calibration guarantees are needed for trustworthy decision-making.

2. **General and principled characterization.** Theorem 3.1 shows that for any finite-dimensional $\mathcal{H}$, the optimal robust policy is a best response to an adversarially tilted belief $q^*(v)$, efficiently computable via a finite-dimensional concave maximization plus pointwise convex minimization. This provides a unifying lens that interpolates between full conservatism (empty $\mathcal{H}$) and plug-in best response (full calibration), with all intermediate cases controlled by the richness of $\mathcal{H}$.

3. **Practical bridge to standard training pipelines.** Proposition 4.4 establishes that any model with a linear head trained to stationarity under squared loss automatically satisfies a self-orthogonality calibration condition. This means the robust policy is immediately available for a huge class of regression models without any algorithmic intervention—a genuine practical contribution.

4. **Simultaneous optimality across multiple decision problems.** Corollary 4.3 shows that a single decision-calibrated forecaster simultaneously yields minimax-optimal plug-in best response for any collection of downstream decision problems, a practically valuable property that goes beyond per-task calibration.

## Weaknesses

### Fatal
None.

### Major

1. **Experiments lack baselines and basic statistical rigor.** The empirical evaluation (Table 1) compares only the robust policy against the plug-in best response, with no baselines: not a constant minimax action, not a bin-wise calibrated policy (despite Proposition 4.5 developing exactly this), not an approximate full-calibration best-response. The reported numbers are single runs with no standard errors, confidence intervals, or results over multiple train/calibration/test splits. The observed utility differences (0.01–0.02) are small enough to be within noise, yet the reader has no way to assess this. For a paper that claims "practical value" and evaluates on "real-world applications," this level of empirical evidence is insufficient to substantiate those claims.

2. **Limited experimental scope.** The experiments test only the self-orthogonality class ($\mathcal{H} = \{h(v)=v\}$) on two regression datasets with a single utility specification each. The paper's own Proposition 4.5 provides a clean closed-form robust policy for bin-wise calibration, yet this is not tested. Decision calibration—the paper's headline theoretical result—is not directly tested either (it would require constructing a decision-calibrated forecaster). The "qualitative conclusions remain the same under other reasonable parameters" is stated but not demonstrated.

3. **Adversarial construction is underspecified.** The paper describes the adversarial distributions as "a worst case tailored to the plug-in policy" and "a worst case induced by the robust dual," but gives no algorithmic details about how these are actually constructed from data. This severely impairs reproducibility and makes it difficult for readers to interpret what the adversarial evaluation actually tests.

### Minor

1. **The experiments validate theoretical predictions rather than stress-test the method.** The adversarial distributions are derived from the same dual optimization used to derive the robust policy. While this is a natural verification of the saddle-point property (and the paper is upfront about this), the evaluation would be strengthened by testing against distribution shifts that preserve calibration constraints but are not adversarially constructed from the dual. The current setup cannot reveal situations where the robust policy might behave poorly under plausible but non-adversarial shifts.

2. **Utility parameter choices feel arbitrary.** The action sets and utility parameters ($\alpha$, $C(a)$) are stated without justification for why these particular values are meaningful for the respective decision problems. A sensitivity analysis would help establish that the conclusions are not artifacts of a particular choice.

3. **The paper tests only 1-d regression outcomes ($d=1$).** The framework applies to multiclass ($d>1$) settings, and the decision-calibration collapse result is most relevant for higher-dimensional outcomes where full calibration is intractable. Adding even a simple multiclass experiment (e.g., with decision regions for a concrete utility) would substantially strengthen the empirical contribution.

### Trivial
None.

## Nice-to-Haves

- **Approximate $\mathcal{H}$-calibration in the main text.** The paper mentions approximate calibration in Appendix B, but for practical credibility, the main text should explicitly state how the results degrade under $\varepsilon$-violations of the calibration constraints.
- **Visualization of the adversarial tilt $q^*(v)$.** Plotting $q^*(v)$ versus $v$ would clarify when the robust policy actually deviates from plug-in and how large the correction is.
- **Extension to infinite-dimensional $\mathcal{H}$.** The finite-dimensional assumption in Theorem 3.1 is reasonable but a brief discussion of the challenges for infinite-dimensional classes would help.

## Removed Points

These points are removed per the review guidelines; they should be treated with caution:

1. **"Theorem 3.1 proof relies entirely on the appendix"** – Removed because the appendix is stripped by PDF parsing; it exists in the original submission.
2. **Criticism that Theorem 3.1 is "insufficient for reviewers to assess correctness"** – Same reason; the proof is present in the original submission.
3. **Complaints about missing supplementary material or references** – Removed per hard rules about cited references and appendix availability.
4. **Formatting/style nitpicks** – Removed per hard rules.
5. **"Could be stronger with more datasets" framed as a fatal flaw** – The paper's primary contribution is theoretical; the limited experiments are a weakness but not a fatal one. Moved to Major.
6. **Strength Finder's claim that "empirical validation of theoretical predictions on real datasets" is a core strength** – This conflicts with verified weaknesses (no error bars, no baselines). The experiments do not convincingly validate the predictions, so this claimed strength is dropped.

## Novel Insights

The most insightful observation across the reviews is that the sharp transition result (Theorems 4.1–4.2) has implications that go beyond what the paper itself develops. The fact that the plug-in best response is minimax optimal for *any* downstream decision-maker once the forecaster satisfies decision calibration for their action set means that a single forecaster can be certified as "universally trustworthy" for a collection of decision problems without per-problem robustness engineering. This reframes the practical target: instead of asking forecasters to be "accurate," we can ask them to be decision-calibrated for the relevant action sets, and the decision-maker's job becomes trivial. The paper identifies this target but does not fully explore its implications for multi-stakeholder settings, which could be a fruitful direction.

## Suggestions

1. **Add baselines to the experiments.** At minimum, compare against: (a) the constant minimax action $\arg\max_a \min_y u(a,y)$, (b) the bin-wise calibrated policy (Proposition 4.5 with a small number of bins), and (c) a policy that best-responds to the globally calibrated mean. Report results over 10–20 random train/calibration/test splits with standard errors.

2. **Provide algorithmic details for the adversarial construction.** Describe explicitly how the worst-case distributions are computed: is it a reweighting of the test set? A parametric perturbation? Which dual variables are used? Without this, the experiments cannot be reproduced or properly interpreted.

3. **Test bin-wise calibration and decision calibration.** Even a simple experiment with histogram-binned forecasts (post-hoc recalibration) would validate Proposition 4.5 and demonstrate the framework's breadth beyond self-orthogonality.

4. **Clarify what "practical value" claim the paper makes.** The abstract and introduction promise "real-world applications" and "practical decision-making." If the contribution is primarily theoretical (which is perfectly acceptable), the framing should reflect that, and the experiments should be presented as illustrative sanity checks rather than definitive validation.

## Score and Decision

**Calibration anchors** (retrieved from human-review corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/vAU1fo1zRV.md` | 7.00 (Accept Poster) | Related topic (decision calibration); strong theory without experiments. This paper's theory is comparably strong and it adds (weak) experiments, but vAU1fo1zRV's results are more technically involved (lower bounds + algorithms). Slightly weaker overall. |
| `/home/wg25r/review_agent/human_reviews_2026/bt4Ahpemmi.md` | 6.50 (Accept Oral) | Conformal robustness control with strong experiments but weaker theory. This paper's theory is stronger but experiments much weaker. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/m5zdEywl57.md` | 6.00 (Reject) | Persuasive prediction; no empirical evaluation noted as key weakness. This paper has stronger theory and at least some experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/xRjOrcj08o.md` | 5.00 (Accept Poster) | CREDO; good balance of theory and experiments. This paper's theory is notably stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/jwv2Lsh8Wo.md` | 4.00 (Reject) | Purely theoretical calibration paper with clarity issues. This paper is substantially stronger in both theory and presentation. |
| `/home/wg25r/review_agent/human_reviews_2026/NNqi3tBcZr.md` | 3.00 (Withdrawn) | Missing proofs dominated evaluation. This paper is much stronger. |

The paper makes a genuine theoretical contribution: the characterization of minimax-optimal policies under $\mathcal{H}$-calibration and the sharp transition at decision calibration are novel and significant results. The writing is clear, the framework is principled, and the practical connections (self-orthogonality, bin-wise calibration) are well-motivated. However, the experimental evaluation is substantially weaker than what the paper's framing promises—lacking baselines, error bars, and coverage of the method's own breadth (no bin-wise or decision-calibration experiments). The theory stands on its own and merits acceptance, but the empirical claims need significant strengthening. Relative to the calibration anchors, the paper sits between the strong theory-only work (vAU1fo1zRV at 7.00) and the weaker-evaluation rejected work (m5zdEywl57 at 6.00).

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>