Now I have a clear picture of the paper and can cross-check all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper extends the epigraph form technique from single-agent safe RL to multi-agent settings, targeting the zero-constraint violation problem that causes training instability in Lagrangian-based safe MARL methods. The key contribution is a CTDE framework: a centralized inner problem trains a z-conditioned policy using PPO with advantage decomposition, while a theoretically-derived distributed outer problem allows each agent to compute its own safety threshold online via one-dimensional root-finding. Experiments on MPE and Safe Multi-agent MuJoCo environments show that EFMARL, using constant hyperparameters across all tasks, consistently achieves near-perfect safety with low cost.

## Strengths

1. **Theoretical decomposition enabling distributed execution (Theorem 1)** — Theorem 1 proves that the outer problem of the epigraph form can be solved locally per agent via 1D root-finding, then aggregated by taking the maximum of per-agent values. This is the core intellectual contribution that fits the epigraph form into the CTDE paradigm, and the derivation cleanly removes dependence on the centralized cost-value function during execution.

2. **Demonstrated training stability over Lagrangian baselines** — Figure 5 shows EFMARL's cost and safety curves during training are substantially smoother than InforMARL-L (lr). Section 3.2 provides an intuitive theoretical explanation: unlike the Lagrangian method, where the policy gradient scales with the multiplier λ (causing divergent oscillations when the constraint threshold is zero), the epigraph form's gradient does not scale with the auxiliary variable z, and the empirical curves in Figure 5 validate this analysis.

3. **Consistent hyperparameter-robust performance across multiple environments** — In Figure 3, EFMARL uses a single fixed set of hyperparameters yet achieves near-100% safety and low cost across all four MPE environments and both Safe MuJoCo environments. No baseline variant (InforMARL with β=0.02/0.1/0.5, InforMARL-L with λ₀=1/5, or the high-lr variant) achieves this combination of safety and performance across all tasks. This result is quantified and clearly presented.

4. **Honest limitations section** — Section 6 candidly acknowledges that the theoretical optimality guarantee is lost without z-communication, that noise/disturbances are not considered, and that safety guarantees do not hold under inexact minimization. This transparency strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline hyperparameter grid is limited** — The paper claims EFMARL requires no hyperparameter tuning while baselines do, but only three penalty coefficients (β ∈ {0.02, 0.1, 0.5}) and two initial Lagrange multipliers (λ₀ ∈ {1, 5}) are tested. The values span orders of magnitude and the extremes clearly show the safety–performance tradeoff, so the core claim is supported. However, the reader cannot fully rule out that a denser sweep (e.g., β=0.3 or λ₀=2) might yield a configuration that gets closer to EFMARL's position in cost–safety space on some environments. Adding a few intermediate values would make the hyperparameter-robustness claim more bulletproof.

2. **Scalability evidence is thin** — Research Question 3 asks whether EFMARL maintains performance with increasing agents, but the experiments are limited to two MPE environments (Formation, Line) with only 5 and 7 agents. No results are shown for Safe Multi-agent MuJoCo with more agents, nor for larger agent counts (e.g., 10+). The paper's framing implies broader scalability, and while the evidence supports the claim for the tested scales, it would be strengthened by at least one higher-agent-count experiment or a MuJoCo scaling result.

3. **Training stability comparison is selective** — Figure 5 compares EFMARL only with InforMARL-L (lr), which is the most unstable baseline variant by design (increased λ learning rate). Showing the same stability plot for the standard InforMARL-L variants (λ₀=1, λ₀=5) would provide a fairer and more complete picture. As presented, the comparison stacks the deck in EFMARL's favor.

4. **zᵢ communication ablation is tested on only one environment** — Table 1 examines whether disabling zᵢ communication (a significant design approximation that sacrifices the theoretical guarantee) affects performance, but this is tested only on Line with N=3. Given that the paper then disables communication for all main experiments, this ablation should be confirmed on at least one additional environment (e.g., a MuJoCo task or a higher-agent MPE task) to support generalizability.

5. **Computational overhead of online root-finding is not discussed** — The method solves a 1D root-finding problem per agent at every execution step. The paper does not provide even a rough estimate of the additional computation relative to standard policy execution (e.g., number of NN evaluations per step, wall-clock overhead). This information would help practitioners assess practicality.

6. **No discussion of non-smoothness from the max operator in the inner problem** — The paper notes that the epigraph form avoids the gradient-scaling pathology of Lagrangian methods (Section 3.2), but does not acknowledge that the max operator inside the total value function V = max{Vᵢʰ, Vˡ − z} introduces non-smoothness when the active term switches during training. The empirical stability in Figure 5 mitigates this concern, but an explicit remark would strengthen the theoretical framing.

### Trivial

1. **Figure 3 caption ambiguously describes error bars** — The caption states "The error bar shows one standard deviation" without clarifying whether this applies to both cost (x-axis) and safety rate (y-axis) or only cost. Clarifying this would improve interpretability.

2. **Ablation tables (Tables 1, 2) do not report variance** — The paper trains with 3 random seeds but the tables appear to report only point estimates. Adding mean ± std would align with the rest of the paper's reporting standards.

## Nice-to-Haves

- A denser sweep of baseline hyperparameters (a few intermediate β and λ₀ values) to more rigorously demonstrate that no single baseline configuration approaches EFMARL's position in cost–safety space.
- A scalability experiment in Safe MuJoCo with more agents (e.g., HalfCheetah 6x3 or higher) to broaden the scaling evidence beyond MPE.
- A brief mathematical extension making the gradient-scaling analysis in Section 3.2 more precise (e.g., showing ‖∇_π J_λ‖ ∝ λ while ‖∇_π V‖ is bounded independently of z).
- Estimating the practical overhead of the online root-finding step (number of extra NN calls, wall-clock time per step) to help readers assess deployment cost.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing proofs in appendix (Proposition 1, Theorem 1):** The harsh critic notes these are deferred to the appendix. This is standard practice for conference papers; the appendix exists in the original submission and is only absent due to parser stripping.
- **GNN handling of variable agent counts:** The paper does not discuss this in detail, but this is a standard implementation detail that is unlikely to affect the paper's core claims.
- **"Error bars on safety rate are omitted":** The Figure 3 caption says "the error bar shows one standard deviation," which could apply to both axes. Insufficient information to confirm this as a genuine weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a few intermediate baseline hyperparameter values** (e.g., β=0.3, λ₀=2, λ₀=3) to Figure 3. If the pattern holds, this significantly strengthens the claim that no baseline configuration systematically reaches EFMARL's position. Even a post-hoc addition to the appendix would help.
2. **Extend the stability analysis** by showing training curves for at least one additional Lagrangian variant (e.g., InforMARL-L with λ₀=1) alongside Figure 5, so the comparison is not limited to the most unstable baseline.
3. **Ablate the z-communication decision on at least one more environment** (e.g., Formation with N=5, or a Safe MuJoCo task) to support the claim that disabling communication does not degrade performance.
4. **Add a sentence acknowledging the non-smoothness of the max operator** and explaining why its empirical effect is benign (citing Figure 5).

## Score and Decision

The paper makes a well-motivated and sound contribution: the first extension of the epigraph form technique to multi-agent safe RL, with a clean CTDE decomposition (Theorem 1), plausible theoretical grounding, and consistent experimental evidence across multiple environments. The weaknesses are evidential gaps and presentation issues that do not threaten the core claims. The paper is solid and deserves acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>