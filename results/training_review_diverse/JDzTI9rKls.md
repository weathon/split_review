Now I have all the evidence I need. Let me synthesize the final review.

---

## Summary

This paper proposes Vlearn, an off-policy RL method that learns only a state-value function (V-function) as the critic, entirely avoiding the Q-function. The core technical contribution is a weighted importance sampling (WIS) loss for deep V-function learning — Theorem 1 shows this loss is an upper bound on the naive importance-weighted Bellman error and shares the same minimum. Combined with trust-region projection layers (TRPL), twin value networks, importance weight clipping, and advantage normalization, Vlearn demonstrates strong empirical performance on high-dimensional continuous control tasks (Ant-v4, Humanoid-v4, DMC dog with 38-D actions, MyoSuite hand with 39-D actions), outperforming SAC, MPO, PPO, TRPL, and V-trace.

## Strengths

- **Novel V-function-only off-policy method that circumvents the curse of dimensionality in action spaces.** The paper provides Theorem 1 proving that the WIS loss upper-bounds the naive Bellman error with the same minimum, enabling deep V-function learning from off-policy data without a Q-function. Empirical results show this design pays off: a 25% improvement over SAC on Humanoid-v4 (17-D actions), and reliable learning on DMC dog tasks (38-D) and MyoSuite hand tasks (39-D) where SAC and MPO fail to learn consistent policies (Figures 2, 3).

- **Mechanistic analysis of why WIS placement matters vs. V-trace.** Figure 1 provides clear intuition: as the importance ratio ρ → 0, V-trace shifts its optimum toward the target network (stalling learning), while Vlearn simply scales down the sample's influence. The bandit analysis in Section 3.2 further shows the WIS loss yields a self-normalized importance weighting estimator, whereas V-trace yields a squared self-normalized estimator. This analysis is supported by empirical results where V-trace fails or suffers performance drops in the fully off-policy setting while Vlearn remains stable.

- **Comprehensive and well-controlled empirical evaluation.** All methods are evaluated with 10 seeds, 95% bootstrapped confidence intervals per Agarwal et al. (2021), uniform network architectures and hyperparameters across methods. The ablation study (Figure 4, right) cleanly disentangles the contribution of each component (IS, TRPL vs. PPO, weight clipping, twin networks), showing all are necessary for the method's success.

- **Principled use of TRPL for off-policy policy updates.** The paper adapts trust-region projection layers (Otto et al., 2021) for the off-policy setting, providing per-state exact trust region enforcement rather than heuristic clipping. The ablation confirms that substituting TRPL with PPO clipping degrades performance, especially on Ant-v4.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Limited analysis of bias in the off-policy advantage estimator.** The policy gradient (Eq. 5) uses a one-step advantage estimate A = r + γV(s') − V(s) computed from the WIS-learned V-function. The paper does not analyze how errors in the off-policy V-function (learned via a weighted squared-Bellman-error objective) propagate to the policy gradient, nor how this differs from the bias of a Q-function-based advantage. While this level of analysis is absent in most actor-critic papers and the empirical results suggest the bias is manageable, the paper's core claim about the WIS loss's superiority would benefit from at least acknowledging this gap.

- **The V-trace comparison uses one-step returns, which differs from V-trace's typical multi-step usage.** The paper is transparent about this choice (Section 4: "we want to eliminate any external factors … and thus do not use n-step returns for both V-trace and Vlearn"), and the comparison successfully isolates the importance weight placement. However, this means the conclusion "V-trace underperforms Vlearn" is specific to this one-step, fully-off-policy configuration. V-trace's multi-step variant might yield different results, and the paper's framing of V-trace's failure should be read with this caveat in mind.

- **The bandit variance analysis provides intuition but does not directly transfer to the full RL setting.** The paper acknowledges this ("evaluating the variance of the importance sampling estimator is generally intractable… we consider a stateless MDP"), yet the section's framing ("Variance Analysis of Importance Sampling Estimators of the Bellman Error") could be read as claiming stronger theoretical support than the simplified bandit derivation actually provides. The empirical results convincingly demonstrate the practical advantage, but the theoretical claim remains suggestive rather than definitive.

- **The abstract's claim about sample complexity is somewhat overbroad.** The abstract states the approach "improves sample complexity as well as final performance." For high-dimensional tasks this holds, but on low-dimensional tasks (e.g., HalfCheetah-v4, Figure 5) Vlearn converges more slowly than SAC and achieves a lower final return. The paper acknowledges this in the conclusion ("sample efficiency remains a challenge"), creating a tension with the abstract's wording.

### Trivial
- The paper's claim that Twin Value Networks are used "to avoid an optimization bias" (abstract) is slightly misleading since the paper later explains overestimation bias is not a direct problem for V-functions, and the twin networks instead act as regularization via a small ensemble.

## Nice-to-Haves
- An empirical measurement of gradient variance during training (e.g., variance of TD errors or gradient norms for Vlearn vs. V-trace on a representative task) would substantiate the variance argument beyond the bandit abstraction.
- A simple MDP analysis (e.g., two-state, two-action chain) comparing the gradient bias/variance of Vlearn, V-trace, and a Q-function method would strengthen the theoretical motivation for the design.

## Removed Points

These points from the reviewers were considered but removed per policy:
- **Criticism about missing comparison to AWR/CRR** — The paper cites Peng et al. (2019) in related work. Adding these baselines would broaden the paper's scope into offline/off-policy hybrid territory. The paper's existing baseline set (SAC, MPO, PPO, TRPL, V-trace) is already substantial and appropriate for its stated scope. Removed per Rule 4 (missing related works) and Rule 16 (scope creep).
- **Criticism about V-trace comparison being "unfair"** — The paper transparently explains it uses one-step returns for both methods to isolate the importance weight placement. This is a methodologically sound choice for the comparison's stated purpose. The underlying concern about V-trace's multi-step potential is kept above in Minor weaknesses, but the framing as an "unfair" comparison is removed.

## Novel Insights

The two most interesting observations emerge from the interaction between the reviewer critiques and the paper's own evidence. First, the paper reveals a subtle but important failure mode for V-trace that is rarely discussed: in the fully off-policy regime with one-step returns, V-trace's interpolation toward the target network for small importance ratios does not just add bias — it actively stalls learning by shifting the optimum away from the Bellman target. This is distinct from the standard narrative that V-trace's importance weight truncation merely controls variance. Second, the ablation showing that TRPL (principled trust region) significantly outperforms PPO clipping in the off-policy setting suggests that the benefits of exact trust region enforcement are amplified when the policy and data distributions diverge — a finding that could inform other off-policy actor-critic designs beyond the V-function-only setting.

## Suggestions
1. Soften the abstract's sample complexity claim to reflect the paper's own evidence, or qualify it as applying primarily to high-dimensional tasks.
2. Add a brief paragraph in Section 3.3 acknowledging the potential bias from using the learned V-function in the advantage estimate, and note why the empirical results still support the approach (or provide a simple diagnostic experiment).
3. Clarify the scope of the V-trace comparison (one-step, fully off-policy) in the conclusion to avoid readers extrapolating beyond the tested regime.

## Score and Decision

The paper presents a clean, well-executed method that makes a genuine practical contribution to off-policy RL in high-dimensional action spaces. The empirical evidence is strong, thorough, and reproducible. The theoretical framing provides useful intuition even if not fully rigorous in the deep RL setting. No fatal or major weaknesses threaten the core claims; the issues raised are addressable and typical of a solid conference paper.

**Originality**: Good — adapting WIS for deep V-functions with TRPL is a novel combination that the field has overlooked.  
**Importance**: Good — high-dimensional action spaces are a real bottleneck for Q-function methods.  
**Claims**: Well-supported for high-dimensional tasks; the sample complexity claim in the abstract is slightly overbroad.  
**Soundness**: Strong — 10 seeds, bootstrapped CIs, ablation study, uniform hyperparameters.  
**Clarity**: Well-written with clear figures and intuitive explanations.  
**Value**: Useful contribution — a practical algorithm that works where SAC and MPO struggle.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>