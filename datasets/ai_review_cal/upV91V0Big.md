- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6
Now I have everything I need. Let me compose the final consolidated review.

---

## Summary

This paper introduces CompoFormer, a structure-based continual transformer for offline reinforcement learning that adaptively composes prior policies via semantic attention over task descriptions (S-BERT). When a new task arrives, the method evaluates whether an attention-weighted combination of existing policies suffices; if not, new parameters are added via LoRA ("Grow") or pruning ("Prune"). The paper also contributes the Offline Continual World (OCW) benchmark, a 10-task manipulation suite with offline datasets and a pre-computed transfer matrix. On OCW10 and OCW20, CompoFormer consistently and substantially outperforms 12 baselines spanning regularization-based, structure-based, and rehearsal-based continual learning methods, demonstrating a strong plasticity-stability tradeoff.

## Strengths

- **Introduction of the Offline Continual World benchmark (Sec 5.1).** The paper extends the online Continual World to an offline setting with 10 manipulation tasks, a pre-computed transfer matrix, and corresponding offline datasets. This provides a standardized, controlled testbed for CORL research that was previously lacking.

- **Comprehensive empirical evaluation (Table 1).** The paper compares 12 baselines across three metrics (Average Performance, Forgetting, Forward Transfer) on both OCW10 and OCW20. This is the most systematic multi-metric comparison of continual learning methods in offline RL to date. Regularization- and rehearsal-based methods catastrophically forget (Forgetting >0.50), while structure-based methods are better but still suboptimal — establishing a clear baseline for the field.

- **CompoFormer consistently and substantially outperforms all baselines (Table 1).** CompoFormer-Prune achieves 0.69 (OCW10) and 0.73 (OCW20) Average Performance, substantially above the next best method (PackNet: 0.64 and 0.57 respectively). It also achieves the lowest forgetting scores (−0.01 to 0.00) across settings.

- **Attention mechanism demonstrably captures semantic task correlations (Figure 4a).** The paper visualizes attention scores and shows, for example, that tasks 2 and 4 share a "pushing the puck" primitive, and the model assigns higher attention from task 4 to task 2. This provides direct interpretability evidence that the mechanism works as intended.

- **Ablation validates the attentive selection design (Figure 4b).** Attentive-Selection clearly outperforms Layer-Sharing and Direct-Addition variants for both CompoFormer-Grow and CompoFormer-Prune, confirming that the selective composition mechanism — not just policy-level sharing — is responsible for the performance gain.

- **Robustness to task order (Table 2).** CompoFormer-Prune achieves nearly identical average performance (~0.69) across four random task orders, while structure-based LoRA varies from 0.35 to 0.54. This demonstrates the method's advantage is not an artifact of a specific sequence.

- **Better plasticity-stability tradeoff than prior structure-based methods (Figure 7/Fig 5).** Per-task success rates after full sequential learning show CompoFormer retains higher performance on most tasks relative to single-task training, compared to PackNet and LoRA.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Threshold η is left undefined and unanalyzed (Algorithm 1, lines 182–214).** The threshold that determines whether the composed policy from prior tasks suffices or whether new parameters are needed is never given a concrete value, nor is its sensitivity discussed. Since this threshold directly controls when the algorithm adds new capacity, its setting is important for understanding the method's behavior. The paper should at minimum state the value used and discuss how it was chosen.

- **No analysis of why CompoFormer-Prune consistently outperforms CompoFormer-Grow.** On OCW10, Prune scores 0.69 vs. Grow's 0.60; on OCW20, 0.73 vs. 0.61. The paper presents both variants but does not explain this gap. Is it because pruning reuses existing capacity more efficiently (no rank constraint), because the Grow variant's LoRA bottleneck limits expressivity, or because of the specific architecture of the base DT model? An analysis of parameter utilization (e.g., number of active parameters per task for each variant) would inform readers.

- **Low forward transfer (FWT) values are acknowledged but not analyzed (Table 1, line 278).** All methods, including CompoFormer, show near-zero or small FWT values. The paper notes this as a limitation for future work but offers no analysis of whether this reflects a limitation of the task sequence, the offline setting, or the method itself. Understanding this would strengthen the contribution.

- **Attention analysis is purely qualitative (Figure 4a).** The visualization of attention scores is informative, but the paper does not quantify the correlation between attention weights and ground-truth task similarity (e.g., using a task-similarity matrix from the benchmark's transfer matrix or from human annotation). A quantitative measure would strengthen the causal claim that the model is doing what the paper argues.

- **Computational cost is mentioned but not quantified (Conclusion, line 416).** The paper acknowledges that storing and computing attention over all previous policies is a limitation, but provides no data on how memory or inference time scales with the number of tasks K (e.g., for K=20). A brief analysis would help readers assess practical feasibility.

- **OCW20 description is ambiguous (line 272).** The paper states the second set of tasks is "identical to the first set" — it is unclear whether this means the *same tasks in the same order* or the *same task definitions* (with newly collected or reused data). This should be clarified.

### Trivial
None.

## Nice-to-Haves
- A correlation analysis between attention weights and ground-truth task similarity (e.g., using the pre-computed transfer matrix) would tighten the causal story.
- Discussing the setting of threshold η and its sensitivity across different task sequences would strengthen the method's reproducibility.
- A quantitative comparison of parameter counts between Grow and Prune variants would help explain the performance gap.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Missing comparison with diffusion- and prompt-based CORL methods."** The cited methods (hu2024continual, hu2024prompt) are rehearsal-based approaches using diffusion models, with different experimental settings, evaluation protocols, and base architectures, as the paper itself notes (line 78: "these efforts often differ in their experimental settings, evaluation metrics"). The paper's baseline set of 12 methods spanning regularization-based, structure-based, and rehearsal-based categories is comprehensive and appropriate for a DT-based method. This criticism constitutes scope creep.

2. **"Missing detail on offline dataset construction in the main text."** The appendix (stripped by the parser) likely contains these details. The main text appropriately states the benchmark construction approach, and full dataset specifications in the appendix are standard practice.

3. **"Missing hyperparameter reporting (LoRA rank, pruning fraction, I_wp, I_tb)."** Per the review guidelines, nitpicks about undisclosed hyperparameters that are standard implementation details are explicitly excluded. These values are presumably in the appendix.

4. **"Reliance on task descriptions and known task boundaries as limitations."** The paper already states these as standard assumptions adopted from prior work (lines 98–100), not as overlooked limitations. Every paper in this subfield makes these assumptions.

## Novel Insights

The most insightful observations from the reviews go beyond the paper's own framing. (1) The consistent performance gap between Grow and Prune (large on OCW20: 0.61 vs 0.73) suggests that the LoRA bottleneck in the Grow variant may be a genuine limitation in capacity for longer task sequences. This points toward a design tradeoff that future work could investigate: whether the flexibility of pruning (which can reuse any subset of existing weights) fundamentally outperforms low-rank adaptation when task count grows. (2) The near-zero forward transfer across all methods, including CompoFormer, is itself a notable finding that merits deeper analysis. It suggests that in offline RL, the distribution shift between successive tasks may dominate any positive transfer effects — a challenge that may require fundamentally different mechanisms than the composition strategy proposed here. Neither of these points undermines the paper's contributions, but they suggest productive directions.

## Suggestions

- **Add a sensitivity analysis for threshold η** — describe how it is set (e.g., based on warmup performance, a fixed success rate, or relative to single-task performance) and show results with at least one alternative value.
- **Analyze the Grow vs. Prune gap** — report per-task parameter counts or effective capacity for each variant, and discuss whether the rank r of LoRA limits expressivity on later tasks.
- **Quantify the attention-similarity correlation** — compute a Spearman correlation between attention weights and the benchmark's transfer matrix entries (or a simple task-feature overlap metric) to ground the qualitative claim.
- **Add a brief computational cost table** — show inference time per step and memory per policy for K={5,10,20}.
- **Clarify the OCW20 description** — explicitly state whether the second set of 10 tasks reuses the same task definitions and whether data is re-collected or the same datasets are used.
