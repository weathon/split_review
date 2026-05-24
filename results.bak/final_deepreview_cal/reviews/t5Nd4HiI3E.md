## Summary

This paper identifies a real and timely problem: aligning Large Reasoning Models (LRMs) with human preferences is destabilized by the high variance of gradient estimates that arises from sampling stochastic reasoning traces. The authors propose BVPO, which mixes a standard trace-based gradient estimator \(g_t\) with a low-variance empty-trace estimator \(g_e\) (obtained by disabling trace generation) via a convex combination. Theoretically, they derive a closed-form MSE-optimal mixing weight and connect MSE reduction to tighter SGD convergence bounds. Empirically, BVPO shows consistent improvements over DPO and SimPO across three LRM sizes on Arena-Hard (up to 5.1 points), AlpacaEval 2 (up to 7.8 points), and six math reasoning benchmarks (up to 4.0 points average).

## Strengths

1. **Well-motivated and timely problem.** The paper clearly identifies trace-induced gradient variance as a key bottleneck for LRM alignment—a problem that existing DPO-based methods do not address. The contrast between the intractable marginal loss \(\mathcal{L}_m\) and the practical trace-based proxy \(\mathcal{L}_t\) is clearly articulated (Section 3.2).

2. **Non-trivial theoretical contribution (Theorem 2).** The closed-form MSE-optimal mixing weight \(\alpha^*\) and the domination guarantee \(\text{MSE}(g_c(\alpha^*)) \leq \min\{\text{MSE}(g_t),\text{MSE}(g_e)\}\) is a genuine theoretical result that goes beyond prior DPO-based methods. The connection to SGD convergence via Theorem 3–4, while adapted from standard analyses, is cleanly presented and provides a principled link between statistical and algorithmic optimality.

3. **Clean, practical, drop-in method.** BVPO requires only appending `