Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper studies preference optimization for Large Reasoning Models (LRMs) that generate intermediate reasoning traces. The authors identify that the standard trace-based gradient estimator suffers from high variance, while marginalizing over all traces is intractable. They propose BVPO, which forms a convex combination of the trace-based gradient and an "empty-trace" gradient (obtained by disabling reasoning trace generation via a prompt modification). The paper provides theoretical analysis showing variance reduction, MSE optimality with a closed-form mixing weight, and improved SGD convergence bounds. Experiments on Arena-Hard, AlpacaEval 2, and six math reasoning benchmarks across three LRMs (1.5B–8B) show consistent improvements over DPO and SimPO in both alignment and reasoning.

---

## Strengths

1. **Identifies a genuinely new and important problem.** The paper is the first to systematically study the unique challenge of trace-induced gradient variance in LRM alignment. The problem framing — the gap between the intractable marginal preference objective and the high-variance single-trace proxy — is clearly articulated and well-motivated. This is a timely issue given the rapid adoption of reasoning models.

2. **Proposes a simple, principled, and drop-in solution.** BVPO's approach of mixing trace-based and empty-trace gradients via convex combination (Eq. 2) is elegant and directly addresses the identified bottleneck. The method is algorithm-agnostic (instantiated with DPO in experiments) and requires only appending `"