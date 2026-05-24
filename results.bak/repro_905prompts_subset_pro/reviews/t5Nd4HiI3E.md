Now I have a thorough understanding of the paper and anchors. Let me write the consolidated review.

---

## Summary
This paper identifies trace-induced gradient variance as a key bottleneck when aligning Large Reasoning Models (LRMs) with human preferences via DPO. The authors propose BVPO, which forms a convex combination of the standard high-variance trace-based gradient estimator and a novel low-variance empty-trace estimator (obtained by disabling reasoning trace generation). Four theorems establish variance reduction, MSE optimality of the mixing weight, and tighter SGD convergence bounds. Experiments on three LRM variants show consistent alignment improvements over DPO and SimPO on AlpacaEval 2 and Arena-Hard, with the additional finding that reasoning ability is preserved and even improved after alignment.

## Strengths
- **Principled problem identification**: The paper clearly diagnoses trace-induced gradient variance as a unique challenge in LRM alignment that existing DPO variants (designed for standard LLMs) do not address. The trace-answer factorization and the intractability of the marginal objective are well motivated (Section 3.2).
- **Rigorous theoretical framework**: Four theorems provide a coherent chain from statistical estimation to algorithmic performance: Theorem 1 proves strict variance reduction for α∈(0,1); Theorem 2 derives the MSE-optimal α* with a domination guarantee (MSE(g_c(α*)) ≤ min{MSE(g_t), MSE(g_e)}); Theorems 3–4 connect MSE minimization to tighter SGD convergence bounds. The theory is self-contained and logically structured.
- **Strong, consistent empirical gains**: Table 1 shows BVPO outperforming the best baseline across all three LRMs (R1-Qwen-1.5B, 7B, R1-0528-Qwen3-8B) on both alignment benchmarks, with gains up to 7.8 points on AlpacaEval 2 and 6.8 on Arena-Hard. Results hold in both Thinking and NoThinking modes.
- **Reasoning preservation and improvement**: Table 2 shows BVPO not only preserves but improves math reasoning (up to +4.0 avg points over base model across six benchmarks), despite training only on general conversational data. This is a practically important finding not demonstrated by baselines.
- **Method simplicity**: BVPO requires only appending `