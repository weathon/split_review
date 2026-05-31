## Summary
This paper introduces Factorization Memory, a novel recurrent neural network architecture that maintains a 2-dimensional memory state with multiple "memory rows." It proposes both dense (all states updated) and sparse (only top-k states updated) memory update mechanisms. The model is designed to retain the training parallelization advantage of structured state-space models like Mamba‑2 while enabling larger memory capacity at bounded computational cost through selective updates. Experiments on language modeling show that Factorization Memory achieves comparable perplexity on short contexts, superior extrapolation to long contexts, and faster inference than both Transformer and Mamba‑2 baselines.

## Strengths
- **Novel sparse memory update mechanism for RNNs.** The idea of using the affinity scores as a router and updating only a subset of memory states (top‑k) is well motivated and directly addresses the capacity-efficiency tradeoff in recurrent models. The reuse of the same scores for read and write is elegant and enables the sparsity to reduce both computation and memory bandwidth.
- **Clear demonstration of long‑context extrapolation.** The loss‑so‑far plots (Figure 4) show that Factorization Memory maintains a stable loss far beyond its training context length (1024 tokens), while Transformer and Mamba‑2 degrade sharply. This result is consistent across two languages and multiple model sizes, providing strong evidence for the advantage of the proposed architecture.
- **Inference speed advantage.** The wall‑clock inference benchmarks (Figure 6) show a 35‑40% speed improvement over Mamba‑2, and drastically better scaling than the Transformer. This directly validates the practical efficiency gain promised by the sparse updates.
- **Systematic analysis of memory scaling.** The experiment in Section 4.1.3 exploring different numbers of memory states (m) and sparse update strategies provides good insight into how capacity and compute interact. The finding that proportional activation (25% of states) can match dense performance at large m is an important design insight.

## Weaknesses
### Fatal
None.

### Major
- **Downstream performance improvements are modest and lack statistical significance.** The average gain over Transformer on English tasks is 1.45 points (29.53 → 30.98) and over Mamba‑2 is 1.92 points. These differences are small and the paper does not report confidence intervals, multiple random seeds, or any statistical testing. The improvement on Japanese tasks is larger but still within a range that could be due to training variance.
- **Long‑context evaluation uses only a custom dataset.** The paper constructs a benchmark from web novels but does not evaluate on any standard long‑context benchmarks (e.g., LongBench, SCROLLS, RULER). This makes it difficult for the community to compare or reproduce the long‑context results directly.
- **The claim of being the “first RNN architecture that successfully combines sparse memory activation with competitive performance” is oversold.** There are prior works that introduce sparsity in RNN hidden state updates (e.g., Skip RNN, structurally sparse recurrent networks, or gating mechanisms that effectively zero out many states). The paper should better differentiate its contribution from these approaches with a more thorough related work discussion and clear evidence that prior sparse RNNs were not competitive.

### Minor
- **No training FLOPs comparison.** The paper only reports inference speed. For a method that claims efficiency, it would be informative to also compare the total training compute (FLOPs or wall‑time) against Mamba‑2 and Transformer under the same sequence length and model size.
- **Sensitivity to k is not explored.** The sparse experiments use only k=4 (fixed) and k=25% (proportional). A sweep over different k values would help understand the tradeoff between sparsity and accuracy more fully.
- **The role of the merge rate μ and update rate η feels under‑analyzed.** Both are sigmoid‑gated from the same input x_t, and it is plausible that one of them is redundant. An ablation showing the effect of each gate would strengthen the design justification.
- **The downstream evaluation benchmark includes only six English and four Japanese tasks.** While this is acceptable for a short submission, the set is small and some tasks (e.g., IFEval) have high variance. Expanding to more standard tasks (e.g., ARC, BoolQ, PIQA) would increase confidence.

### Trivial
- Figure 1 caption is duplicated in the main text.
- The table for Japanese tasks uses “xWino” but the reference cites “Wino‑X”; the naming should be consistent.

## Nice-to-Haves
- Include standard long‑context benchmarks (LongBench, RULER) to allow direct comparison.
- Report downstream results with error bars or over multiple seeds.
- Provide an analysis of the learned affinity scores α_t—e.g., how selective they become after training, and whether the heatmap shows clustering of tokens by state.
- Compare with a hybrid architecture (e.g., Hymba) to show where a pure recurrent approach stands relative to hybrid alternatives.

## Novel Insights
None beyond the paper’s own contributions.

## Suggestions
- Add confidence intervals or standard deviations to the downstream evaluation tables (Table 1 and Table 2 in appendix). At minimum, train each model with at least two random seeds to estimate variance.
- Include training time or training FLOPs in the efficiency comparison to give a complete picture of the method’s cost.
- Clarify the claim of “first RNN with sparse memory activation” by citing and contrasting with earlier sparse RNN variants (e.g., “Skip RNN: Learning to Skip State Updates” or “Self-normalizing Neural Networks” with sparse activations), or soften the claim.
- Evaluate on established long‑context datasets to increase the impact and reproducibility of the long‑context results.

## Score and Decision
**Score:** 6  
**Decision:** Accept

Explanation: The paper presents a clean, well‑motivated architectural innovation with strong empirical support for long‑context extrapolation and inference efficiency. The sparse memory update mechanism is a practical contribution. The main weaknesses—modest downstream gains without statistical validation and a somewhat narrow long‑context evaluation—prevent the paper from being a strong accept, but the core contributions are solid and of clear interest to the ICLR community working on efficient sequence models.

MY FINAL SCORE: <score>6</score>  
MY FINAL DECISION: <decision>Accept</decision>