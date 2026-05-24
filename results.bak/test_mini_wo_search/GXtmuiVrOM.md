Here is my consolidated final review:

## Summary

This paper proposes DORAEMON, a method for automatically shaping the distribution over dynamics parameters in Domain Randomization for RL-based sim-to-real transfer. The core idea is to maximize the entropy of the training distribution subject to a constraint on the estimated probability of success, using importance sampling to reuse training trajectories and a KL trust region to control distribution changes. The method is evaluated on six MuJoCo sim-to-sim tasks and a real robot PandaPush task.

## Strengths

- **Clean, theoretically motivated formulation.** The constrained optimization problem (maximizing entropy subject to a success-probability constraint, Eq. 3) is a natural and well-justified way to formalize the DR distribution-shaping problem. The toy inclined-plane example (Sec. 4.2) verifies that the converged entropy aligns with the true feasible dynamics range.

- **Consistent empirical advantage over baselines in sim-to-sim evaluation.** The paper reports that DORAEMON achieves higher or equal global success rate on the maximum-entropy uniform distribution compared to LSDR, AutoDR, and Fixed-DR across all six MuJoCo environments (Fig. 6, top row), with lower variance in most cases. This supports the claim that the method produces policies that generalize better over the full dynamics range.

- **Ablation and sensitivity analysis on the key hyperparameter α and the success threshold.** The paper analyzes the trade-off between in-distribution success rate α and final entropy (Fig. 8a) and shows the algorithm tracks different return thresholds reliably (Fig. 8b), demonstrating that DORAEMON is not overly sensitive to arbitrary threshold choices.

- **Sample-efficient algorithmic design.** The importance-sampling estimator (Eq. 5) reuses training trajectories to evaluate the success rate under candidate new distributions without additional rollout collection. The method updates all dimensions of φ simultaneously, unlike AutoDR which updates one dimension at a time. These design choices are clearly motivated.

- **Demonstration of zero-shot sim-to-real transfer.** The paper presents results on a real 7-DoF robotic arm pushing task with 17 randomized dynamics parameters (Tab.~\ref{tab:pandapush} in the original submission), providing concrete evidence that the method can narrow the reality gap. A project website with video evidence is referenced.

## Weaknesses

### Fatal
None.

### Major

- **The importance sampling estimator's reliability is not analyzed.** The estimator in Eq. 5 reweights trajectories collected under ν_{φ_i} to estimate success rates under ν_{φ_{i+1}}. As the distribution shifts, effective sample size can drop, especially in high-dimensional spaces (n_ξ=17 in the real experiment). The paper does not report the number of trajectories K per update, the variance of the estimator, or whether importance sampling weights become degenerate. The KL trust region mitigates abrupt shifts, but without any analysis, the constraint satisfaction signal that drives the entire distribution growth may be based on noisy estimates. This is a methodological gap that weakens confidence in the results.

- **The backup procedure (Eq. 7) is described as "crucial" but never ablated.** The paper states "We observed this addition to be crucial for recovering policy performance" (line 144) but provides no experiment showing what happens without it — how often it triggers, whether it always succeeds, or whether performance collapses in its absence. A central design element that is called crucial deserves empirical verification.

- **Best-performing policy tracking is asymmetric across methods.** The paper states "To mitigate this effect, we track the best-performing policy during training in terms of global success rate" (line 263) for DORAEMON in tasks where performance degrades (Walker2D, Swimmer). It is not clarified whether the same best-policy tracking is applied to baselines (LSDR, AutoDR). If not, the comparison may unfairly favor DORAEMON in tasks where policies destabilize during training.

- **Key hyperparameters (K, ε) are not specified.** Algorithm 1 lists K (trajectories per distribution update) and ε (KL trust region size) as input parameters, but their numerical values are never reported in the available text. ε in particular controls the pace of distribution growth and is critical for reproducibility and understanding the method's sensitivity.

### Minor

- **The evaluation uses a single metric (global success rate on ν_max) that aligns with DORAEMON's own objective.** While global success rate is the most relevant metric for the problem (generalization across dynamics), reporting additional complementary metrics — such as average return under the reference distribution (relevant to LSDR's objective) or performance near nominal dynamics — would provide a more complete picture of trade-offs. The paper acknowledges the success-rate vs. entropy trade-off but does not quantify what DORAEMON may sacrifice in performance near nominal dynamics for broader coverage.

- **The heatmap analysis (Fig. 7) shows only a 2D slice of the dynamics space.** The remaining parameters are fixed at nominal values, so the visualization does not demonstrate generalization across the full space. This is acknowledged implicitly but limits the strength of the evidence from that figure.

- **The method "only requires a binary rule for success" is somewhat oversold.** Defining a meaningful success function for complex tasks can be as nontrivial as tuning DR distributions. The paper does partially address this by studying sensitivity to the success threshold (Fig. 8b), which is good, but the framing in the introduction overstates the simplification.

### Trivial
None.

## Nice-to-Haves
- A direct sample-efficiency comparison (total environment interactions vs. global success rate) accounting for extra evaluation rollouts used by LSDR and AutoDR would substantiate the claimed efficiency advantage.
- Sensitivity analysis on the KL trust region size ε would strengthen the empirical evaluation.
- An ablation comparing the dynamics-conditioned critic (inherited from prior work) to an unconditional critic would isolate the contribution of entropy maximization from this technique.
- Statistical significance tests or confidence intervals for the sim-to-sim comparisons would clarify whether DORAEMON's advantage is significant across all tasks, given visible variance in some environments (e.g., Walker2D).
- A quantitative evaluation of the toy problem (e.g., measuring how well the converged distribution's shape matches the analytically computed feasible region) would strengthen the intuition.

## Removed Points

- **Real-world results not verifiable (Harsh Critic #2).** The criticism about the missing table is a parser artifact. The original submission includes Tab.~\ref{tab:pandapush} via `\input{03_tables/sim2real_results}`, which the parser could not resolve. The table exists in the original paper; the review should not penalize the paper for extraction failures.
- **Evaluation unfair because it conflates objectives (Harsh Critic #1, core framing).** The harsh critic argued that comparing DORAEMON with LSDR/AutoDR on global success rate is "stacked in favor of DORAEMON." This is not a valid fairness concern: global success rate on the full dynamics range is the correct metric for the problem these methods all address (producing policies that generalize across unknown dynamics). LSDR optimizes toward a reference distribution (set to ν_max here), and AutoDR expands based on boundary performance; evaluating on ν_max is a standard generalization test. Criticisms about missing additional metrics are retained as a minor weakness above.
- **Missing related works.** Cannot be confirmed without external sources. Removed per instructions.
- **Formatting and style nitpicks.** Parser artifacts, not author errors. Removed per instructions.

## Novel Insights

A genuinely novel observation emerges from reviewing the two assessments side by side: the paper's strongest contribution — the constrained entropy-maximization formulation — simultaneously enables and limits the evaluation. Because DORAEMON directly targets the entropy-coverage objective, it can be precisely measured against the desired goal (maximizing coverage while maintaining success). But this same precision makes it difficult to evaluate what the method sacrifices, because the natural evaluation metric (global success rate) is the one DORAEMON was designed to optimize, and standard baselines were designed for different objectives (average return to a reference, boundary-based expansion). The reviews thus surface a meta-level issue in the automatic DR literature: the field lacks a universally agreed-upon evaluation protocol that isolates generalization capability from training objective alignment. DORAEMON's empirical advantage across six environments is convincing, but establishing whether that advantage holds across diverse objectives and reward structures would require a more comprehensive evaluation framework than any single metric provides.

## Suggestions

1. **Report K and ε values.** Specify the number of trajectories per distribution update and the KL trust region size used in all experiments. Show that results are robust to ε.
2. **Ablate the backup procedure.** Provide an experiment comparing DORAEMON with and without the backup optimization to verify that it is indeed "crucial" as claimed.
3. **Analyze the importance sampling estimator's variance.** Report the effective sample size or weight diagnostics over training to demonstrate that the success rate estimates are reliable.
4. **Clarify best-policy tracking for baselines.** State explicitly whether LSDR and AutoDR also benefit from best-policy tracking in the Walker2D and Swimmer tasks; if not, provide a version of the results where all methods use the same evaluation protocol.
5. **Add complementary metrics.** Include average return under the nominal/reference distribution alongside global success rate to quantify the performance-coverage trade-off.

## Score and Decision

This is a solid paper with a clean, well-motivated formulation and consistent empirical support across multiple environments. The sim-to-sim results demonstrate clear advantages over baselines. The main weaknesses are analytical gaps (IS variance, backup ablation, missing hyperparameter values) rather than fundamental flaws. None of the verified weaknesses threaten the core claims; they are addressable with additional experiments and reporting.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>