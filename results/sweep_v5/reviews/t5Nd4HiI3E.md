Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper studies preference optimization (DPO) for Large Reasoning Models (LRMs) where the ideal marginal probability over traces is intractable and single-trace Monte Carlo estimates produce high-variance gradients. The authors propose BVPO, which mixes a high-variance trace-based gradient with a low-variance empty-trace gradient (obtained by suppressing trace generation) via a convex combination. Theoretically, they prove conditional variance reduction, derive an MSE-optimal mixing coefficient with domination guarantees, and connect these results to SGD convergence bounds. Empirically, BVPO outperforms DPO and SimPO across three LRM sizes (1.5B–8B) on Arena-Hard and AlpacaEval 2 (gains up to 7.8 points), while also preserving or improving math reasoning performance.

## Strengths

1. **Well-motivated and clearly identified problem.** The paper formalizes a genuine challenge: the marginal preference objective for LRMs requires summing over an exponential number of reasoning traces, and the standard single-trace proxy injects substantial gradient variance. This problem framing is sound and timely.

2. **Consistent and substantial empirical gains.** BVPO outperforms both DPO and SimPO across all three model sizes (R1-Qwen-1.5B, 7B, R1-0528-Qwen3-8B) in both *Thinking* and *NoThinking* modes, with gains of up to 7.8 points on AlpacaEval 2 Win Rate and 6.8 points on Arena-Hard. The improvements are consistent across settings — not cherry-picked from isolated conditions.

3. **Reasoning ability is preserved and even improved.** Despite training exclusively on general conversational data (UltraFeedback), BVPO raises average math reasoning accuracy by up to 4.0 points over the base model across six benchmarks, demonstrating that the method does not trade reasoning quality for alignment.

4. **Simple and practical approach.** BVPO requires only appending `