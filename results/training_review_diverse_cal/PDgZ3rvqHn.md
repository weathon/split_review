I have thoroughly verified the paper's content against all reviewer claims. Let me now produce the final consolidated review.

---

## Summary

This paper proposes SDAR (Spatially Decoupled Action Repetition), a novel framework for continuous control RL that makes per-dimension act-or-repeat decisions rather than the whole-action binary switch used in prior methods like TAAC. SDAR operates via a two-stage process: a selection policy β decides which action dimensions to change, and an action policy π generates new values only for those selected dimensions. Experiments across classic control, MuJoCo locomotion, and manipulation tasks show that SDAR improves sample efficiency, final episode returns, and reduces action fluctuation compared to SAC, TAAC, TempoRL, UTE, and N-Rep baselines.

## Strengths

1. **Novel and well-motivated per-dimension action repetition.** The paper identifies a genuine limitation of prior action repetition methods — treating all action dimensions homogeneously — and proposes a principled solution. The qualitative evidence in Figure 4 and Table 3 directly demonstrates that different joints in Walker2d learn different repetition rates (e.g., leg joints repeat more than thighs/feet), which TAAC cannot achieve because it forces all dimensions to repeat or act simultaneously.

2. **Consistent empirical improvements across multiple domains.** Table 1 and Figure 3 show SDAR achieving the highest average normalized AUC in classic control, locomotion, and manipulation categories. The learning curves (Figure 3) confirm that SDAR (red) consistently climbs faster and reaches higher asymptotic returns than all five baselines, including the strongest prior closed-loop method TAAC, across challenging tasks like Humanoid and HalfCheetah.

3. **Simultaneous improvement in returns and action smoothness relative to vanilla RL.** Table 2 shows SDAR achieves a low action fluctuation rate (AFR) and high action persistence rate (APR) while maintaining superior episode returns — e.g., on Humanoid, SDAR attains AFR of 0.183 (SAC: 0.203) and episode return of 5538 (SAC: 4765). This combination is not achieved by N-Rep or open-loop methods, which obtain high APR at the cost of degraded returns.

4. **Thorough experimental scope.** The evaluation covers 11 continuous control tasks across three categories, compares against five baselines representing open-loop, closed-loop, and no-repetition approaches, and reports not only AUC/returns but also APR and AFR to characterize the persistence-diversity trade-off from multiple angles.

## Weaknesses

### Major

1. **The importance-sampling optimization for the selection policy is presented without validation, raising concerns about stability.** The paper's key optimization for scaling beyond tiny action spaces (Eq. 9) uses importance sampling with \(\beta_{\text{old}}\), but no empirical comparison to the exact enumeration variant (Eq. 8) is provided — even on a task like LunarLander (|A|=2) where exact enumeration is tractable. The paper states "sampling several \(b \in \mathcal{B}\)" without specifying how many samples are used, and provides no diagnostics (effective sample size, importance weight clipping, variance analysis) to establish that the gradient estimates are stable. This matters because the entire advantage of decoupling depends on the selection policy being reliably optimizable; if the importance-sampled gradients have high variance, the learned behavior could be erratic or biased. The paper's strong final results suggest the optimization works empirically, but without validation the reader cannot assess whether it is reliable or fragile.

2. **The claim of "reduced action fluctuation" from decoupling is confounded with different overall repetition rates.** In Table 2, SDAR achieves higher APR than TAAC, which mechanically lowers AFR (more repetition means fewer action changes per step). The paper interprets lower AFR as evidence that decoupling reduces unnecessary oscillations, but the comparison conflates the effect of decoupling with the effect of simply repeating actions more frequently. To isolate the benefit of per-dimension decisions, one would need to either (a) match APR across methods (e.g., by adjusting target entropies) and then compare AFR, or (b) compare SDAR to an ablation that uses a single scalar switch but is otherwise identical. Without such controls, the "reduced fluctuation" claim is weaker than presented.

3. **Missing ablation that directly isolates the value of per-dimension decoupling.** The paper compares SDAR to TAAC, but TAAC differs from SDAR in multiple ways beyond the per-dimension vs. whole-action design (e.g., the Mix operation, conditioning on \(a^-\), the two-stage architecture). The cleanest ablation would be a version of SDAR where β outputs a single scalar Bernoulli probability applied uniformly to all dimensions, keeping all other design choices and hyperparameters identical. This would directly measure whether per-dimension decisions provide benefit beyond the overall two-stage design. The current comparison to TAAC does not rule out the possibility that other aspects of SDAR's architecture (rather than decoupling per se) drive the improvements.

### Minor

4. **AUC normalization procedure is underspecified.** The paper states AUC scores are normalized into [0,1] where 0.0 = random policy performance and 1.0 = best method, but does not describe how the random-policy baseline is computed (e.g., average return over how many episodes, using what action distribution). Additionally, per-task normalization means that "0.9" on one task does not carry the same meaning as "0.9" on another, yet the scores are averaged across tasks in each category. Reporting raw AUC values alongside normalized ones would improve interpretability.

5. **Key hyperparameters are not reported.** The paper does not provide a table of hyperparameters (network sizes, learning rates, target entropies \(\mathcal{H}_\beta\) and \(\mathcal{H}_\pi\), policy delay, number of importance samples for Eq. 9) for SDAR or baselines. This makes it difficult to assess whether comparisons are fair or whether SDAR has been more carefully tuned than baselines.

6. **Computational cost is not discussed.** SDAR requires two forward passes per step (selection policy followed by action policy) versus a single pass for SAC and TAAC. The paper should at minimum report wall-clock time per environment step or note this overhead; real-time control applications may care about this.

### Trivial

- None that pass the filtering rules.

## Nice-to-Haves

- **Analyze whether β meaningfully conditions on the previous action \(a^-\).** The paper could inspect β's decisions when \(a^-\) is varied vs. fixed to assess whether the selection policy is actually making use of this information or whether the state alone would suffice.
- **Report the number of importance samples used in Eq. (9).** This is a specific detail that would help reproducibility.
- **Report whether importance weights in Eq. (9) are clipped** or otherwise stabilized to prevent large gradient updates.

## Removed Points

The following points from the reviews were found to be not valid or not applicable:

- **Environment choice criticism (manipulation tasks are "unusual" without HER).** Pusher, Reacher, and FetchReach are standard continuous control benchmarks in Gym/MuJoCo, used extensively in the RL literature. All methods (SDAR and baselines) are evaluated on the same tasks under the same conditions, so the comparison is fair. No method uses HER or goal relabeling, so this affects all methods equally and does not bias the comparison. Removed per rule: *REMOVE weaknesses that complain the paper does not use methods the reviewer prefers when the paper's own choices are defensible within its class.*
- **Strength Finder point about "Practical optimization for large action spaces."** This conflicts with verified Weakness #1 (unvalidated importance sampling). Per rules: *when a strength and weakness disagree, the weakness wins.* Dropped.

## Novel Insights

None beyond the paper's own contributions. One observation that emerges from cross-referencing the reviews: the paper's own Figure 4 and Table 3 provide the strongest qualitative support for its thesis (different joints need different repetition rates), and these are far more compelling as evidence than the confounded APR/AFR comparison. If the authors focus their revision on the controlled ablations (single-switch SDAR, matched-APR comparison) rather than on more tasks or baselines, the paper would be substantially stronger.

## Suggestions

1. **Run the single-switch ablation of SDAR.** Replace the per-dimension β with a scalar Bernoulli applied uniformly across all dimensions. Keep everything else identical (two-stage, Mix operation, same hyperparameters). This directly tests the core claim.
2. **Validate importance sampling on LunarLander (|A|=2).** Compare Eq. (8) (exact enumeration) vs. Eq. (9) (importance sampling) on a small task where both are feasible, reporting Q-values and policy performance over training.
3. **Control for repetition rate in the AFR comparison.** Either match APR across SDAR and TAAC by adjusting target entropies, or present a matched-comparison subset to show that decoupling itself reduces fluctuation beyond what more repetition alone achieves.
4. **Specify the AUC normalization procedure precisely** and consider reporting raw AUC values alongside normalized ones.
5. **Provide a full hyperparameter table** for all methods.

## Score and Decision

The paper proposes a genuinely novel and well-motivated approach to action repetition. The empirical results are consistent and impressive across diverse tasks. However, the experimental analysis has gaps that prevent full confidence in the mechanistic claims: the optimization of the selection policy is not validated, the fluctuation reduction claim is confounded, and an ablation isolating the decoupling contribution is missing. These are addressable weaknesses that strengthen rather than invalidate the work.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**