Now I'll produce the final review.

## Summary
This paper proposes a hybrid RL algorithm (HAC/HNPG) that integrates off-policy Fitted Q-Iteration on offline data into an on-policy Natural Policy Gradient framework. The key theoretical contribution is a best-of-both-worlds guarantee: when Bellman completeness approximately holds and offline coverage is good, the bound depends on $\min\{C_{\text{npg}}, C_{\text{off}}^2\}$; when it does not, the bound defaults to the standard NPG rate. This is the first hybrid RL method with this doubly-robust property. Experiments on continuous combination lock tasks (including a CIFAR-100 variant) show HNPG outperforming both pure on-policy TRPO and the hybrid off-policy method RLPD.

## Strengths

1. **Novel doubly-robust theoretical guarantee.** Theorem 1 cleanly shows that HAC benefits from offline data when offline assumptions hold (bound scaling with $\min\{C_{\text{npg}}, C_{\text{off}}^2\}$) and falls back to standard NPG guarantees otherwise (Theorem 1, lines 180–190). This explicitly addresses a limitation of prior hybrid RL theory (e.g., HyQ) that provides no guarantee when offline assumptions fail.

2. **Clean algorithmic architecture.** The HPE subroutine (Eq. 5, lines 86–87) combines an off-policy TD loss (bootstrap-based) with an on-policy Monte Carlo regression loss (non-bootstrapped). The on-policy term requires no Bellman backup, so even when the off-policy term fails due to model misspecification, the on-policy term still provides a valid signal. This is a principled design difference from prior hybrid methods that mix data and run a single off-policy algorithm.

3. **Principled extension to parameterized policies.** HNPG (Algorithm 3, lines 106–124) extends the approach to neural-network-based policies via compatible function approximation, fitting a linear critic under both online and offline data. The Fisher information matrix interpretation (line 103: "exactly the fisher information matrix computed using both online and offline data") is a natural generalization of NPG to the hybrid setting, and Theorem 2 provides matching guarantees.

4. **Empirical demonstration on challenging exploration tasks.** On both the continuous combination lock (horizon 50) and the CIFAR-100 image-based variant (horizon 30), HNPG solves substantially harder horizons than RLPD, which fails at horizons 15 and 10 respectively (Figure 2, lines 298, 328). The diagnostic loss curves (Figure 3, lines 320–331) provide evidence that RLPD's online TD loss explodes while HNPG's supervised-style loss remains stable, consistent with the theoretical motivation.

## Weaknesses

### Fatal
None.

### Major

1. **Limited experimental evaluation constrains the empirical claims.** The paper tests only one family of tasks (combination lock variants) with a single hybrid baseline (RLPD). The "continuous" action space (line 296) is a 10-dimensional vector passed through softmax — a reparameterized discrete choice rather than a truly continuous control problem, making the setting quite specialized. No ablation is provided of the critical hyperparameter $\lambda$ (line 99: "chosen via hyperparameter tuning" with no sensitivity study), which controls the on-policy/off-policy trade-off and is central to the algorithm's design. The offline dataset contains 32–36% optimal trajectories (line 292), which is a relatively strong signal, and no test with weaker offline data is conducted. These gaps mean the paper's empirical claims about "significantly outperforming" hybrid RL rest on a narrower foundation than ideal for a top conference.

2. **Theory–experiment gap.** The theoretical analysis (Section 5, Theorem 1) is developed for a discounted infinite-horizon MDP with softmax tabular policies. The experiments use HNPG with neural-network-parameterized policies on a *finite-horizon* episodic environment, adapting the discount-based evaluation to the finite horizon (line 281: "instead of a discounted setting policy evaluation, we adapt to the finite horizon setting"). While this adaptation is common in RL practice and the HNPG theory (Theorem 2, with smoothness and realizability assumptions) partially addresses the policy class gap, the finite-horizon vs. discounted discrepancy is not theoretically resolved. The paper does not verify whether the assumptions for Theorem 2 are satisfied by the experimental setup.

### Minor

1. **No ablation of $\lambda$.** The weight $\lambda$ governing the on-policy/off-policy balance is described only as "chosen via hyperparameter tuning" with "typically $\lambda \in [1, T]$" (line 99). Without any sensitivity analysis, it is unclear how robust the method is to this choice or whether careful tuning is required per setting.

2. **Loss curves rely on a single random seed.** The diagnostic loss curves in Figure 3 that underpin the explanation for RLPD's failure are from "one random run" (caption, line 323). This weakens the claim that the observed online critic loss explosion is systematic rather than incidental.

3. **Generalization claim partially confounded.** The paper attributes HNPG's better generalization partly to RLPD's higher updates-to-data ratio (line 330–331), which it acknowledges. This confound makes it unclear whether the advantage stems from the on-policy vs. off-policy distinction per se or from different training dynamics.

4. **No test with weaker offline data.** With 32–36% of offline trajectories already optimal (line 292), testing with noisier data would better stress-test the hybrid benefit.

### Trivial
None.

## Nice-to-Haves
- **Ablation of $\lambda$** across multiple horizons would substantially strengthen the empirical evaluation.
- **Comparison with $\lambda{=}0$ (pure on-policy) and $\lambda{\to}\infty$ (pure off-policy FQI)** would directly isolate the hybrid design's contribution.
- **Wall-clock computation time** comparison would help practitioners assess the trade-off given HNPG's Monte Carlo rollouts.
- **Testing on a standard continuous-control benchmark** would connect the method to the broader RL literature, though this is outside the paper's stated focus on hard exploration.

## Removed Points
These points were flagged during processing and are excluded from the main review:
- "No code release is mentioned": Per policy, reproducibility nitpicks about code/artifact availability are not retained.
- "The theoretical results for HNPG are deferred to the appendix": Appendix content is stripped by the parser and exists in the original submission; the main-review version defers this to the appendix, which is standard.
- "Hyperparameters for RLPD are said to be tuned but no details are provided": The paper references the appendix for hyperparameter details; this does not affect the core evaluation.

## Novel Insights
The most interesting cross-cutting observation is that the paper's core design insight — combining a non-bootstrapped on-policy regression loss with a bootstrapped off-policy TD loss — has a precise theoretical payoff that prior hybrid methods lack. The on-policy term provides a "safety net" that preserves NPG-style guarantees when the off-policy term fails due to Bellman incompleteness. This mechanism manifests empirically in the CIFAR-100 experiment, where RLPD's online TD loss explodes while HNPG's supervised loss stays stable. The unresolved issue is whether this robustness generalizes beyond the specific combination lock family.

## Suggestions
1. **Ablate $\lambda$** across multiple horizons (5, 15, 30) to demonstrate robustness to this critical hyperparameter.
2. **Include a weaker offline data regime** (e.g., random data with $<5\%$ optimal trajectories) to stress-test the hybrid benefit.
3. **Either** run a small-scale tabular experiment that directly validates Theorem 1, **or** explicitly discuss which assumptions are satisfied/violated in the finite-horizon experimental setup and how the gap affects interpretation.
4. **Clarify whether the generalization advantage** in the CIFAR-100 experiment persists when controlling for the updates-to-data ratio.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>