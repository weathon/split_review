Now let me write the review based on my thorough reading of the paper.

---

## Summary

ELMUR is a transformer architecture augmented with structured, per-layer external memory for long-horizon decision-making under partial observability. Each layer maintains a bounded set of memory embeddings that are read via bidirectional cross-attention (mem2tok / tok2mem), updated through a Least-Recently-Used (LRU) management block using either full replacement or convex blending, and temporally grounded by relative positional biases. Evaluated on T-Maze (up to 10⁶ steps), MIKASA-Robo robotic manipulation, and 48 POPGym tasks, ELMUR achieves 100% success on T-Maze at corridor lengths 100,000× the attention window, ranks first on 21/23 MIKASA-Robo tasks, and achieves the top aggregate score on POPGym.

---

## Strengths

- **Compelling T-Maze result.** Achieving 100% success at corridor length 10⁶ with only L=10 context (S=3 segments during training) is a striking demonstration of long-horizon retention. The extrapolation heatmap (Figure 4) further supports that the learned policy generalizes bidirectionally in sequence length.
- **Broad and diverse evaluation.** The paper tests on three qualitatively different benchmarks — a synthetic memory probe (T-Maze), diverse puzzle/control tasks (POPGym-48), and visual manipulation (MIKASA-Robo) — providing a comprehensive picture of the method's scope.
- **Principled theoretical analysis.** Propositions 1–2 and the derived effective-horizon formula H(ε) = M·L·ln(ε)/ln(1−λ) give a closed-form understanding of how retention scales with M, L, and λ. This connects cleanly to the ablation results showing M ≥ N as a critical threshold.
- **Thorough ablation study.** The ablations in Figure 6 and Table 3 independently vary M, λ, σ, segmentation, the relative bias, LRU removal, shared vs. per-layer memory, and MoE vs. MLP, establishing the contribution of each component.
- **Efficiency gains over stronger baselines.** ELMUR's per-step inference time (6.8 ms) is faster than RATE (7.2 ms) and DT (10.7 ms) despite a larger parameter count, because bounded memory decouples complexity from sequence length.

---

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent baseline coverage across benchmarks.** RMT and TrXL appear prominently in Figure 3 (T-Maze) and are among the closest relevant baselines, yet they are absent from Tables 1 and 2 (MIKASA-Robo and POPGym). There is no stated reason — neither task incompatibility nor a failure-to-converge observation. This asymmetry makes it unclear whether the improvements over the most related memory-augmented models hold outside T-Maze.

2. **One memory slot updated per segment is a hard structural bottleneck.** The LRU module writes exactly one slot per segment, regardless of how many salient events occur. On tasks with multiple important events within a segment, the model cannot selectively retain more than one piece of new information per write cycle. Neither the theoretical analysis nor the experiments address multi-event segments, and this limit could significantly constrain applicability on richer tasks not covered by the benchmarks.

3. **MoE-FFN default is unjustified by the ablation.** Table 3 shows that swapping MoE → MLP achieves identical performance (1.00 ± 0.00) while "improving computational efficiency." If MLP is both simpler and more efficient and matches MoE performance, the motivation for using MoE as the default reported architecture is unclear. Reporting results with the strictly more complex component while noting that the simpler one equals it undercuts the design narrative.

### Minor

1. **RememberColor5/9 gains are marginal.** In Table 1, improvements on RememberColor5-v0 (0.15→0.19) and RememberColor9-v0 (0.17→0.23) are modest and overlap with the best baselines' error bars. The paper's headline claim of "nearly doubles performance" relies heavily on TakeItBack and RememberColor3; a per-category breakdown would be more informative.

2. **M requires task-specific tuning.** The ablation (Figure 6c) shows that M < N causes sharp performance collapse, but the paper does not provide guidance for setting M in practice when N (number of required segments) is unknown — a common situation in real deployments. Whether there is a safe, task-agnostic default is not discussed.

3. **POPGym reactive task gains are negligible.** On the reactive subtask (15 tasks), ELMUR scores 9.2 vs. DT 9.3 and RATE/BC-LSTM 9.1 — all within noise. The headline "ELMUR achieves the top score on 24 of 48 POPGym tasks" encompasses these reactive tasks where differences are not meaningful.

### Trivial

- The contributions section opens "Our contributions are twofold" but lists three bullets.

---

## Nice-to-Haves

- An experiment where multiple salient events occur within a single segment would directly test whether the one-write-per-segment constraint becomes a bottleneck.
- Reporting the aggregate MIKASA-Robo success across all 23 tasks in the main paper (rather than just 4) would make the "21 of 23" and "~70% improvement" claims directly verifiable without the appendix.
- A comparison of inference wall-clock time for ELMUR vs. RMT and TrXL (not just DT and RATE) would round out the efficiency story.

---

## Novel Insights

ELMUR surfaces a meaningful practical insight: that a per-layer, slot-limited external memory with LRU replacement provides **bounded-capacity long-horizon retention that is strictly decoupled from sequence length**, and that this decoupling is achievable within the transformer's standard layer structure rather than as an external module. The formal connection between the convex blending factor λ, slot count M, and segment length L — yielding a closed-form effective horizon H(ε) = M·L·ln(ε)/ln(1−λ) — is a useful design tool. The empirical finding that M ≥ N (the number of task-critical segments) is a near-binary threshold for success, and that this threshold is consistent across different hyperparameters once M is correctly set, provides actionable guidance for memory sizing in long-horizon POMDP applications.

---

## Suggestions

- Add RMT and TrXL to MIKASA-Robo and POPGym tables or explicitly state why they could not be evaluated on those benchmarks.
- Provide a practical heuristic or ablation showing how to choose M when N is unknown.
- Either justify the MoE default with a task where it outperforms MLP, or switch the default to MLP and present MoE as a scalability option.
- Test a setting where multiple key events occur within a single segment to expose any limitation of the one-write-per-segment design.

---

## Score and Decision

ELMUR addresses a clear and important problem (long-horizon partial observability in sequential decision-making), makes a coherent architectural contribution (per-layer LRU-managed external memory with bidirectional cross-attention), provides both theoretical and empirical support, and demonstrates strong results — most notably, 100% T-Maze success at 10⁶ steps with a context window of 10. The concerns about baseline inconsistency (RMT/TrXL missing from main tables) and the unjustified MoE default are real but not contribution-invalidating. The method is clearly described, the ablations are informative, and the experimental breadth is appropriate. This is a solid paper above the ICLR bar.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>