Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

## Summary

This paper proposes Residual-MPPI, an online planning algorithm that combines Residual Q-Learning (RQL) with Model Predictive Path Integral (MPPI) to customize continuous-control policies at execution time without retraining. The method uses the prior policy's log-likelihood as a proxy for the unknown original reward during MPPI's trajectory evaluation, enabling zero-shot and few-shot policy customization. Experiments in MuJoCo show consistent improvements over baselines, and the paper demonstrates customization of the champion-level GT Sophy 1.0 racing agent in Gran Turismo Sport, reducing off-course steps by ~60% while maintaining competitive lap times with dramatically less data than RL-based alternatives.

## Strengths

- **Novel and practically motivated algorithmic integration**: Residual-MPPI bridges RQL (previously limited to discrete actions or requiring additional training) with MPPI's sampling-based MPC, enabling online continuous-control policy customization. The approach requires only access to the prior policy's action distribution and a dynamics model — no knowledge of the original reward, training data, or policy parameters. This is a clean and practical formulation.

- **Strong empirical results on a champion-level real-world agent**: The GTS experiments show Few-shot Residual-MPPI reduces GT Sophy 1.0's off-course steps from 93.13 to 36.60 per lap (a ~60% reduction) with only a 3-second lap time increase (117.77s → 120.75s), using only ~2,100 laps total. This is contrasted with Residual-SAC which required 80,000 laps and produced an overly conservative policy (130s lap time). The data efficiency advantage (40× less data) is a practically significant result.

- **Consistent zero-shot performance across diverse MuJoCo environments**: Table 1 shows Residual-MPPI outperforms both Guided-MPPI (which has full ground-truth reward) and Full-MPPI across all four environments (HalfCheetah, Swimmer, Hopper, Ant) on total reward and add-on task metrics, while maintaining similar basic reward levels to the prior policy. These results are computed over 500 episodes with standard errors reported.

- **Honest discussion of limitations**: Section 7 explicitly identifies that the method is bottlenecked by prior policy quality and dynamics model accuracy, and discusses directions for improvement (diffusion policies, world models, learned residual Q-functions). This appropriate scoping lends credibility to the contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Missing specification of the critical hyperparameter \(\omega'\).** The weight \(\omega'\) on the log-prior term appears in both the algorithm (line 114) and the evaluation function (Eq. 7), controlling the balance between maintaining prior behavior and satisfying the add-on objective. The paper never defines, discusses, or explains how \(\omega'\) is set — whether it is derived from the prior policy's temperature \(\alpha\), tuned as a hyperparameter, or has a principled relationship to any known quantity. This is not a trivial omission: without this information, the experimental results cannot be properly interpreted (they could reflect carefully hand-tuned weights rather than a robust method). This must be addressed for the paper to be evaluable.

2. **Theoretical gap between the RQL framework and the proposed Residual-MPPI evaluation function.** In the maximum-entropy RL framework, the optimal policy satisfies \(\pi(a|s) \propto \exp(Q(s,a)/\alpha)\), so \(Q(s,a) = \alpha \log \pi(a|s) + \alpha \log Z(s)\), where \(Z(s)\) is the state-dependent partition function. The paper's evaluation function \(S^{\text{aug}}(U) = \sum \gamma^t (r_R + \omega' \log \pi)\) uses only the \(\log \pi\) term without accounting for the state-dependent constant \(\alpha \log Z(x_t)\). Since different action sequences \(U\) produce different trajectories \(\{x_t\}\), these missing constants differ across sequences and can affect their relative ranking. The paper claims to "derive Residual-MPPI straightforwardly" from RQL, but the connection is incomplete: the evaluation function is a heuristic rather than a principled instantiation of the RQL framework. A formal statement with clear assumptions about when (or whether) the state-dependent constants cancel or can be absorbed would transform the current heuristic into a principled method.

### Minor

1. **The MuJoCo Guided-MPPI baseline comparison conflates two differences.** Guided-MPPI has access to the full ground-truth reward but is limited to a finite planning horizon, while Residual-MPPI replaces the unknown reward with \(\log \pi\) which encodes long-horizon value information from the trained prior policy. The paper attributes Guided-MPPI's worse performance to the finite-horizon limitation, but the comparison simultaneously varies both the evaluation function (true reward vs. \(\log \pi\)) and the source of long-horizon information. A cleaner ablation would augment Guided-MPPI with a learned terminal value function to isolate whether the advantage comes from the log-prior proxy specifically, or simply from having any long-horizon signal. This does not invalidate the results — the paper's explanation is plausible — but it weakens the strength of the causal claim.

2. **The dynamics training loss uses a discounted multi-step error \(\sum \gamma^t (s_t - \hat{s}_t)^2\), which weights near-term accuracy more heavily than long-term accuracy.** The paper states this is to "ensure accuracy over the long term," but discounting actually has the opposite priority. While prioritizing near-term accuracy is defensible in a receding-horizon planner (errors can be corrected at the next step), the mismatch between stated intent and actual design should be clarified or corrected.

### Trivial

- The algorithm initializes the nominal action sequence with \(\arg\max \pi(\cdot|x_t)\) and then uses this same sequence as a candidate for evaluation. This is equivalent to importance sampling with zero noise, which could benefit from a brief formal note in the weight calculation, though it does not affect the results.

## Nice-to-Haves

- **Sensitivity analysis for \(\omega'\).** Once \(\omega'\) is defined, reporting sensitivity over a range of values would demonstrate robustness.
- **Ablation with a degraded prior policy** (e.g., partially trained SAC) to quantify how inaccurate the prior can be before Residual-MPPI breaks down — especially given Section 7's acknowledgment that accuracy requirements are a bottleneck.
- **Planning horizon sensitivity analysis** for all MuJoCo methods to directly test the paper's claim that finite horizon limits Guided-MPPI.
- **Off-course distance distributions** for the GTS experiment (beyond the means and max values already reported on lines 293) would better characterize the safety improvement.

## Removed Points

- **Criticism about add-on task definitions being in the appendix**: Removed because the parser strips appendix content from all papers; these definitions exist in the original submission.
- **Claim that GTS safety improvement is "overstated"**: Removed. The paper reports a ~60% reduction in off-course steps (93→37) and quantifies reduced off-course distance severity (0.69m→0.37m avg, 3.21m→1.13m max). The critic's comparison to Residual-SAC ignores the 40× data efficiency advantage (80,000 vs 2,100 laps) which is a central part of the paper's contribution. The claim is well-supported.
- **Criticism about the "infinite variance" condition for Theorem 1 being a non-sequitur**: Removed. The paper hedges with "suggests" and "can well approximate" — it does not claim formal equivalence for finite variance. The framing is reasonable for a heuristic theoretical motivation.
- **Mischaracterization that the paper "claims to derive Residual-MPPI" from RQL**: The paper says "integrate RQL into the MPPI framework" (line 31), not "derive," and "derive straightforwardly" (line 148) refers to defining the evaluation function given the MPPI-max-entropy connection, not a formal derivation of the algorithm from first principles.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is that the paper's practical strength (demonstrated effectiveness on a champion-level real-world system) and its theoretical weakness (incomplete justification of the log-prior-as-reward proxy) are two sides of the same coin. The method works empirically despite the theoretical gap — and understanding *why* it works despite the missing state-dependent constants could itself be a valuable contribution. One hypothesis is that in MPPI's trajectory evaluation setting, the missing \(\log Z(x_t)\) terms are dominated by the add-on reward signal and the prior policy's own log-likelihood differences, making the approximation empirically tight. Another is that \(\omega'\) implicitly absorbs the missing constant when tuned. Either way, the gap between theory and practice here is not a bug to be fixed but a phenomenon worth investigating in future work.

## Suggestions

1. **Define \(\omega'\) explicitly.** Clarify whether \(\omega' = \alpha\) (the prior policy's entropy temperature), whether it is a tuned hyperparameter (report its value and sensitivity), or whether it can be derived. This is the single most important revision needed.
2. **Address the state-dependent constant issue.** Either provide a formal argument (Lemma/Proposition) showing that the missing \(\log Z(x_t)\) terms cancel or can be absorbed under MPPI's trajectory-level evaluation, or explicitly characterize the method as a heuristic approximation of RQL (which the experiments validate).
3. **Augment the Guided-MPPI baseline with a learned terminal value function** in MuJoCo to isolate the source of Residual-MPPI's advantage.
4. **Clarify the dynamics loss justification.** Either explain why discounted multi-step error is appropriate for a receding-horizon planner, or switch to undiscounted multi-step MSE.

## Score and Decision

This paper addresses a genuinely important problem — customizing continuous-control policies at execution time without retraining — and provides compelling experimental evidence, especially the GTS results with a champion-level agent. The method is novel, the problem is well-motivated, and the practical advantages (data efficiency, zero-shot capability, no access to original reward) are clearly demonstrated. However, the paper has two significant gaps that prevent it from being fully evaluable: the critical hyperparameter \(\omega'\) is never defined, and the theoretical connection to RQL is asserted without addressing the missing state-dependent constant in the log-prior-as-reward proxy. The remaining concerns (Guided-MPPI comparison, dynamics loss) are addressable. The core empirical contribution is real and worth publishing, but the paper must first be brought to a state where its claims can be properly assessed. I recommend acceptance contingent on addressing the major issues (especially \(\omega'\) and the theoretical gap) in a revised version.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>