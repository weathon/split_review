Now let me write the final consolidated review.

## Summary

This paper studies preference optimization for Large Reasoning Models (LRMs), where the statistically correct marginal objective (summing over all reasoning traces) is intractable and practical single-trace approximations introduce high gradient variance. The authors propose **BVPO**, which mixes a high-variance trace-based gradient estimator with a low-variance "empty-trace" estimator (obtained by disabling reasoning generation) via convex combination. Theoretical analysis proves variance reduction, derives an MSE-optimal mixing coefficient, and connects MSE minimization to tighter SGD convergence bounds. Empirically, BVPO outperforms DPO and SimPO on AlpacaEval 2 and Arena-Hard across three LRM sizes, while also improving math reasoning performance despite being trained only on general conversational data.

## Strengths

1. **Well-motivated problem with a clean, principled solution.** The paper identifies a genuine and timely issue: trace-sampling variance in LRM preference optimization, which existing methods (designed for conventional LLMs without explicit reasoning traces) do not address. The proposed solution—mixing trace-based and empty-trace gradients—is conceptually simple, theoretically grounded, and easy to implement as a drop-in replacement for existing DPO pipelines. Section 3.3 makes clear that BVPO is algorithm-agnostic and can be instantiated with any preference optimization objective.

2. **Consistent and non-trivial empirical gains across alignment benchmarks.** Table 1 shows BVPO improving over the best baseline (DPO/SimPO) by up to 7.8 points on AlpacaEval 2 and 6.8 points on Arena-Hard, across three model sizes (R1-Qwen-7B, R1-Qwen-1.5B, R1-0528-Qwen3-8B) and in both *Thinking* and *NoThinking* evaluation modes. The gains are systematic rather than cherry-picked: BVPO leads on all 18 reported metrics (6 metrics × 3 models).

3. **Reasoning improvement despite general-domain training data.** Table 2 shows that BVPO improves average performance on six math reasoning benchmarks by up to 4.0 points (R1-Qwen-7B: 60.5→62.3; R1-Qwen-1.5B: 44.7→48.7; R1-0528-Qwen3-8B: 74.7→76.1). This is notable because the training data (UltraFeedback) is general conversational, not math-specific, demonstrating that the proposed alignment method does not degrade—and can strengthen—reasoning capability.

4. **Formal link between bias-variance trade-off and SGD convergence.** Theorems 2–4 connect the MSE-optimal mixing weight to the per-step error floor in SGD convergence bounds. While Theorem 4's result (MSE = Bias² + Var under ηL=1) is straightforward, the overall framework provides a principled statistical justification for why mixing improves training stability, beyond heuristic variance reduction.

5. **Practical simplicity.** The method only requires appending `