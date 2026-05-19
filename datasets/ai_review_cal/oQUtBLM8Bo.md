- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3
Now I have a thorough understanding of the paper and all the reviewers' claims. Let me produce the final consolidated review.

---

## Summary

This paper extends the epigraph form technique from single-agent safe RL to the multi-agent setting, proposing EFMARL to solve the multi-agent constrained optimal control problem (MACOCP) with zero constraint violation. The method decomposes the problem into a centralized inner problem (trained with PPO using a GNN backbone) and a distributed outer problem solved via root-finding during execution, enabling CTDE. Experiments on MPE and Safe Multi-agent MuJoCo show EFMARL achieves near-100% safety and low cost with a single hyperparameter configuration across all tested environments, outperforming penalty-based and Lagrangian baselines that require per-environment tuning.

## Strengths

- **Addresses Lagrangian instability in zero-constraint-violation MARL**: The paper provides a clear theoretical motivation (Section 3.2) explaining why the Lagrangian multiplier never decreases and gradients scale with it, while the epigraph form's auxiliary variable $z$ does not multiply the cost function. The training curves in Figure 5 directly support this: EFMARL shows smoother, lower-variance training compared to MAPPO-Lagrangian.

- **Strong empirical results across multiple environments**: Figure 3 demonstrates that EFMARL with a single hyperparameter set consistently occupies the top-left region (low cost, near-100% safety) in all four environments (MPE Target, Spread, Formation, Safe MuJoCo HalfCheetah 2×3, Coupled HalfCheetah 4×3). Baselines require different hyperparameter choices to trade off safety vs. performance and vary considerably across environments.

- **Scalability to larger multi-agent systems**: Figure 6 shows EFMARL maintains its advantage (top-left region) when scaling to 5 and 7 agents, while baseline performance degrades or requires retuning.

- **Proposition 1 (dynamic programming for the total value function)**: The recursive update $V(x^k, z^k; \pi) = \max\{h(x^k), V(x^{k+1}, z^{k+1}; \pi)\}$ with $z^{k+1}=z^k - l(x^k, \pi(x^k))$ formalizes how $z$ acts as cost-upper-bound dynamics, making the inner problem tractable for standard RL algorithms like PPO.

- **Ablation studies validate practical design choices**: Table 1 shows that omitting $z_i$ communication (theoretically required) does not harm performance, supporting the method's simplicity. Table 2 systematically examines the safety margin $\xi$ and confirms that $\xi \approx \nu$ gives the best trade-off, providing practical guidance.

## Weaknesses

### Major

- **Theorem 1's relationship to $V^l$ is not clearly justified in the main text**: Theorem 1 states that the outer problem (which involves both $\max_i V_i^h \le 0$ and $V^l \le z$) can be solved as $z = \max_i z_i$ where each $z_i$ is computed from $V_i^h(o_i; \pi(\cdot, z')) \le 0$ — with no reference to $V^l$. The text preceding the theorem acknowledges that the outer problem "requires the centralized cost-value function $V^l$" and claims Theorem 1 eliminates this need, but the theorem statement as written does not explain *why* the $V^l \le z$ constraint is automatically satisfied when $z = \max_i z_i$. This is a substantive logical gap in the presentation. The proof may address this in the appendix (which is stripped by the parser), but the main text should be self-contained on this point. This does not invalidate the paper's contribution (the empirical results provide strong evidence the method works), but it weakens the claimed *theoretical* foundation for the distributed outer problem as presented in the main body.

### Minor

- **The "no hyperparameter tuning" claim is overstated**: The paper states it uses "a constant set of hyperparameters" and claims "without any hyperparameter tuning." While the same $(\nu, \xi) = (0.5, 0.4)$ values are indeed used consistently across environments, these are still hyperparameters that the authors had to choose. The $\xi$ ablation (Table 2) is conducted on only one environment (Line with $N=3$), so the sensitivity to this choice in other environments is not established. A sensitivity analysis of $\xi$ on one additional environment (e.g., from Safe MuJoCo) would significantly strengthen the hyperparameter-robustness claim. The core claim that EFMARL outperforms baselines with its chosen settings is well-supported; the concern is only about the scope of the zero-tuning narrative.

- **GNN architecture unspecified**: The paper states it uses a "graph neural network (GNN) backbone" for policy and value networks but does not specify the architecture (GCN, GAT, attention, etc.), number of layers, or hidden dimensions. While some of these details may be in the stripped appendix, the main text should summarize the key architectural choices for reproducibility, especially given that all baselines are reimplemented using the same backbone.

### Trivial

None beyond the presentation concerns already noted.

## Nice-to-Haves

- **Comparison with one additional safe MARL baseline** not derived from InforMARL (e.g., MACPO (Gu et al., 2023) with its original implementation) would further validate that EFMARL's gains are not solely due to the GNN backbone or implementation choices.
- **Formal hypothesis tests** (e.g., paired t-tests across seeds/environments) for the cost and safety rate comparisons would strengthen the statistical claims, though the visual separation in Figure 3 is already convincing.
- **Runtime overhead of the root-finding procedure** used in the distributed outer problem could be discussed, as this may matter for large-scale deployment.

## Removed Points

- The critic's characterization of Theorem 1 as a "structural flaw" that "undercuts the core theoretical contribution" is overly severe. The theorem may be fully correct with a proper proof in the appendix; the issue is that the main-text presentation does not explain how $V^l$ is resolved. Demoted from potential Fatal to Major.
- The critic's concern about the phrase "theories and algorithms for safe RL are still lacking for the multi-agent scenario" being too strong: the paper qualifies this with "to the best of our knowledge" and "especially when policies are executed in a distributed manner." Removed as not substantive.
- The critic's note about the safety rate definition conflating per-agent and overall safety is an observation, not a weakness. The definition is clearly stated. Removed.
- Various formatting/style nitpicks and requests for details likely present in the stripped appendix are removed per policy.
- Requests for comparisons with methods outside the paper's stated scope or for statistical tests that are not standard in this subfield are moved to Nice-to-Have.

## Novel Insights

The harsh critic flags a potentially significant gap in the presentation of Theorem 1 — the main text states a decomposition that appears to omit the $V^l$ coupling — while the strength finder identifies the same theorem as a core contribution. Merging these reveals that the paper's central theoretical claim is presented in an incomplete way in the main body, and that the real strength of the paper lies in its empirical demonstration that the epigraph form *works* for multi-agent safe RL, even if the theoretical justification for the distributed outer problem requires deeper justification than the main text provides. The paper's overall contribution is more strongly empirical than theoretical, and the review should reflect this calibration.

## Suggestions

1. **Clarify Theorem 1 in the main text**: Add an intuitive explanation of why the $V^l \le z$ constraint is automatically satisfied when $z = \max_i z_i$ under the optimal policy, or at least provide a sketch of the proof mechanism in the main body. If the theorem requires additional assumptions (e.g., that the inner-problem policy $\pi(\cdot, z)$ achieves $V^l(\pi(\cdot,z)) \le z$ whenever all $V_i^h \le 0$), state them explicitly.

2. **Broaden the $\xi$ ablation**: Add a similar sensitivity analysis for $\xi$ in at least one non-MPE environment (e.g., a Safe MuJoCo task) to strengthen the claim of hyperparameter robustness.

3. **Specify the GNN architecture**: Add a sentence summarizing the GNN type, number of layers, and hidden dimension choices in the main text for reproducibility.

4. **Soften the "no hyperparameter tuning" phrasing**: Acknowledge that $\nu$ and $\xi$ are problem-informed hyperparameters that were chosen and held constant, rather than claiming "no tuning," which invites unnecessary criticism.
