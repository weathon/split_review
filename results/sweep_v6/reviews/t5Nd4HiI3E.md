Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper studies preference optimization for Large Reasoning Models (LRMs), where the intractable marginal objective (summing over all reasoning traces) is typically replaced by a single-trace Monte Carlo approximation, introducing high gradient variance. The authors propose BVPO, which forms a convex combination of the high-variance trace-based gradient \(g_t\) and a low-variance "empty-trace" gradient \(g_e\) (obtained by disabling reasoning trace generation). Theoretically, they prove variance reduction (Theorem 1), derive an MSE-optimal mixing weight (Theorem 2), and connect MSE optimality to tighter SGD convergence bounds (Theorems 3–4). Empirically, BVPO outperforms DPO and SimPO on AlpacaEval 2 and Arena-Hard across three LRM scales (1.5B, 7B, 8B) and also shows modest improvements on math reasoning benchmarks.

## Strengths

- **Well-motivated and timely problem.** The paper identifies a genuine gap: aligning LRMs with human preferences introduces trace-induced gradient variance that existing preference optimization methods (designed for conventional LLMs without explicit reasoning traces) do not address. This framing is both novel and practically relevant.

- **Clean, self-contained theoretical framework.** Theorem 1 proves that the conditional variance (w.r.t. trace sampling) of the combined estimator \(g_c\) is strictly less than that of \(g_t\) for any \(\alpha \in (0,1)\). Theorem 2 gives a closed-form MSE-optimal mixing weight with the guarantee \(\text{MSE}(g_c(\alpha^*)) \leq \min\{\text{MSE}(g_t), \text{MSE}(g_e)\}\). Theorem 4 formally connects MSE optimality to SGD convergence error when \(\eta L = 1\). The theory is presented concisely and is internally consistent.

- **Consistent empirical gains across alignment benchmarks.** Table 1 shows that BVPO outperforms both DPO and SimPO across all three model sizes in both *Thinking* and *NoThinking* modes on Arena-Hard and AlpacaEval 2, with gains of up to 7.8 points (AlpacaEval 2 win rate) and 6.8 points (Arena-Hard).

- **Interesting incidental finding.** The observation that preference alignment on general conversational data (UltraFeedback) not only preserves but slightly improves math reasoning (Table 2) is a non-obvious and valuable result.

## Weaknesses

### Major

1. **The choice of the mixing coefficient \(\alpha\) in experiments is not disclosed.** The paper never states what value(s) of \(\alpha\) were used in the experiments or how \(\alpha\) was selected (e.g., grid search, validation set, heuristic). Theorem 2's optimal \(\alpha^*\) depends on biases, variances, and covariances relative to the unknown \(\mu\), quantities that are not available in practice. Without specifying how \(\alpha\) was set, the empirical results cannot be reproduced, and it is unclear whether the reported gains actually stem from the claimed bias–variance optimization or from a differently tuned hyperparameter.

2. **No error bars, confidence intervals, or multiple seeds.** All results in Tables 1 and 2 are reported as point estimates with no measure of uncertainty. Given the stochastic nature of trace sampling, preference dataset construction, and fine-tuning, single-run results could be within the noise range. This undermines the statistical significance of the empirical claims, especially the modest reasoning improvements (e.g., +0.3 on AMC for R1-0528-Qwen3-8B, +0.2 on MATH-500 for the same model).

3. **Limited baseline comparisons.** The paper compares only against DPO and SimPO. Several other preference optimization methods exist (KTO, R-DPO, TGDPO, ORPO, etc.) that are mentioned in the related work section but not evaluated. Since the core claim is that BVPO improves upon "standard" preference optimization for LRMs, a broader comparison would substantially strengthen the empirical case.

### Minor

4. **The "empty-trace" construction is heuristically motivated.** Appending `