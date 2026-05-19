- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6
## Summary

This paper proposes ActSafe, a model-based RL algorithm for safe exploration. The algorithm learns a probabilistic dynamics model, uses epistemic uncertainty as an intrinsic reward to expand a pessimistic safe set of policies, and then transitions to exploiting extrinsic reward. The paper provides theoretical guarantees (safety during all episodes and finite sample complexity to near-optimality) under RKHS/GP assumptions, and presents a practical variant using RSSM ensembles that scales to high-dimensional vision-based control tasks. Experiments on Safety Gym and related benchmarks show that ActSafe incurs lower cumulative costs than prior methods while achieving competitive reward.

## Strengths

1. **First theoretical guarantees for both safety and finite sample complexity in continuous-space model-based safe RL.** Theorem 1 proves that ActSafe maintains safety during all episodes and provides a sample-complexity bound for reaching an $\epsilon$-optimal policy within the reachable safe set. The paper explicitly positions this claim relative to prior safe exploration literature (Berkenkamp et al., Baumann et al., Sukhija et al.), which either focuses on low-dimensional policy spaces or lacks optimality guarantees. The claim is well-supported by the paper's framing and the related-work analysis. (Lines 32–33, 86–87, 229)

2. **The pessimistic safety margin is empirically validated to be necessary.** In the GP experiments (Section 5.1, Figure 1), ActSafe with pessimism incurs zero cost on Pendulum/Cartpole, while a variant without pessimism and the unsafe Opax algorithm violate constraints. This clean ablation ties the theoretical insight directly to empirical safety behavior and is correctly interpreted by the authors. (Lines 305–308)

3. **Scaling to high-dimensional vision-based control while maintaining safety.** Figure 3 shows that ActSafe's practical variant (using RSSM ensembles) achieves substantially lower cumulative costs than LAMBDA, BSRP-Lag, and CPO on Safety Gym vision tasks, while remaining competitive in reward. This demonstrates that the principles of pessimistic constraint satisfaction and intrinsic exploration can be instantiated in a deep-RL setting. (Lines 324–331)

4. **Intrinsic exploration demonstrably helps in hard exploration tasks with sparse rewards.** Figures 4–5 show that ActSafe significantly outperforms greedy, uniform, and optimistic baselines on sparse-reward navigation and Cartpole tasks, validating the claim that epistemic-uncertainty-driven exploration is crucial for both safety and sample efficiency in challenging exploration settings. (Lines 333–347)

## Weaknesses

### Major

1. **Unclear whether the offline data advantage is controlled across baselines in vision experiments.** The paper states (line 321) that ActSafe uses 200K steps of offline data collected with a random policy for model initialization. For the baselines LAMBDA, BSRP-Lag, and CPO, the paper says only that "we use the same experimental setup from Safety Gym and [as2022constrained]" — but this does not clarify whether the baselines also received the same offline pretraining. If they did not, ActSafe's substantially lower costs (Figure 3) could partly reflect a data-quantity advantage rather than the algorithm's safety mechanism. The paper should either (a) explicitly state that all baselines received the same offline data (with citation to each baseline's pretraining protocol), (b) run an ablation without offline data, or (c) acknowledge the asymmetry and discuss its potential impact on the comparison. This is the single most important experimental gap.

2. **The practical variant's safety claims depend on unverified uncertainty calibration.** The theoretical guarantees (Theorem 1) assume GP dynamics and exact calibration. The practical variant (Section 4.4) replaces the GP with an RSSM ensemble, using heuristic pessimism via worst-case ensemble cost and claiming (line 247) that the conservative safe set $\widehat{\mathcal{S}}_n \subseteq \mathcal{S}_n$ "still preserves the safety guarantees." However, this argument depends on the RSSM ensemble providing a well-calibrated statistical model (Definition 1), which is not proven or empirically validated. The paper acknowledges using "approximate Bayesian inference" (line 278), but the gap between approximation and the well-calibrated model assumption is not bridged. This leaves the safety properties of the vision experiments on weaker ground than the paper's framing suggests. A calibration study (e.g., reliability diagrams or empirical coverage of ensemble predictive intervals) would substantially strengthen the empirical claims.

### Minor

1. **Safety metrics are not reported for the sparse-reward experiments.** Figure 4 ("Performance on hard safe exploration tasks") and Figure 5 (Cartpole) show only reward curves. The paper mentions in text (line 334) that ActSafe "violat[es] the constraint only once," but no cost curves or tables are shown. Since the paper's central claim is about *safe* exploration, reporting cost trajectories for these tasks would significantly strengthen the evidence.

2. **The sample-complexity bound (Equation 12) is not instantiated or discussed in relation to any environment.** The bound involves $\gamma_{n^*}(k)$, $\beta_{n^*}^4(\delta)$, $T^6$, $C^4$, and a term with $\sigma_0^2 / \log(1 + \sigma^{-2}\sigma_0^2)$, but no approximate value is computed even for the simple Pendulum environment. The theorem's value is primarily existential—which is acceptable—but the paper could note the bound's limitations or discuss which terms dominate.

3. **The choice of $n^*$ (episodes to switch from intrinsic to extrinsic reward) is not ablated or given a principled rule.** The paper uses a fixed $n^*$ for each domain but does not discuss sensitivity to this hyperparameter or provide guidance on how to set it in practice.

### Trivial

- 5 seeds with standard error (Figure 3) is on the low end for safety-critical evaluation; showing individual runs or IQR would be more informative.
- The GP experiments run only 10 episodes — reasonable for GP efficiency, but a brief comment on whether safety is maintained over longer horizons would clarify.

## Nice-to-Haves

- A comparison with model-based safe RL methods (Koller 2018, Curi 2022) on the GP tasks would help position ActSafe within the existing model-based safe RL literature.
- A brief discussion of computational cost (ensemble of RSSMs + constrained optimization per episode) for real-time feasibility.

## Removed Points

These points from the reviews are removed with justification:

1. **"Definition 2 (safe set) is unintuitive and the paper does not discuss how $D$ might be computed"** — The paper explicitly connects $D(\pi,\pi')$ to similar distance metrics in prior work (cite Foster 2024, line 191) and acknowledges (line 197) that the expansion operator is "difficult to evaluate in continuous spaces" but provides key insights. The practical variant replaces this definition with a tractable surrogate. This is an understood design choice, not a weakness.

2. **"10 episodes for GP experiments is very short"** — GP-based safe exploration methods are sample-efficient by design (e.g., Berkenkamp et al. use comparable episode counts). This is a generic critique that does not account for the setting.

3. **"Variance reporting: standard error with 5 seeds is unreliable"** — 5 seeds is standard practice in deep RL papers and does not constitute a methodological error. The paper also reports median (robust to outliers). This is a formatting/presentation nitpick.

4. **"Missing empirical comparison with Koller 2018 and Curi 2022"** — The paper already compares against LAMBDA, BSRP-Lag, and CPO, which are state-of-the-art safe vision RL methods. Adding more GP-MPC baselines beyond what is standard in the deep safe RL evaluation protocol is a scope-expansion request.

5. **Strength Finder's claim that "[Practical implementation] is directly linked to the theoretical algorithm"** — This conflicts with the verified weakness (Major #2) about unverified calibration. The link is claimed by the authors but not fully substantiated. Demoted from core strength.

6. **"The paper should not imply that the theoretical guarantees justify the vision results"** — The paper does not claim that the GP-based theorem directly applies to the vision experiments. It explicitly calls the theoretical version "idealized" (line 85) and the practical variant "heuristic" (line 366). The paper says the practical variant "preserves the safety guarantees" (line 247) — this is too strong a claim given the unverified calibration, but the critic's framing overstates how much the paper relies on theoretical justification for the vision results.

## Novel Insights

The two-stage design (intrinsic exploration for safe-set expansion, then extrinsic exploitation) combined with *both* optimism (for epistemic exploration) and pessimism (for constraint satisfaction) is a clean synthesis of ideas from safe Bayesian optimization and model-based RL. The key insight — that the same uncertainty estimates that drive exploration can simultaneously serve as a pessimistic safety margin — is intuitive but elegantly operationalized. The paper's main gap is that the practical instantiation (RSSM ensembles) does not come with a guarantee of well-calibrated uncertainty, so the safety properties in high-dimensional settings are empirically demonstrated but not theoretically grounded. This is a common situation in deep RL theory-to-practice transitions and does not invalidate the empirical contribution.

## Suggestions

1. **Clarify the offline data protocol for all baselines.** The simplest fix is to explicitly state either that all baselines received the same 200K offline pretraining steps, or conduct an ablation of ActSafe *without* offline data to isolate the algorithm's own safety mechanism. This is the most impactful thing to address.

2. **Add a calibration study for the RSSM ensemble uncertainty** on the vision tasks — e.g., reliability diagrams or empirical coverage of predictive intervals. This would directly address the theory-practice gap and strengthen the safety claims.

3. **Include cost curves in the sparse-reward experiments.** Showing cumulative cost alongside reward for Figures 4–5 would make the safety evaluation complete.

4. **Add a sensitivity analysis or discussion of the $n^*$ hyperparameter.** Even a one-sentence rule of thumb (e.g., "we set $n^*$ to the number of episodes needed for the safe set to cover the reachable region, which we monitor via ensemble disagreement dropping below a threshold") would make the method more actionable.
