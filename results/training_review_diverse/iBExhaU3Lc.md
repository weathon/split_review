Here is my consolidated meta-review.

---

## Summary

This paper proposes Adam-mini, a memory-efficient optimizer that reduces Adam's per-parameter learning rates (the $v$ state) to a single scalar per Hessian-derived parameter block, cutting optimizer memory by ~50%. The authors analyze the near-block-diagonal Hessian structure of neural networks (especially Transformers) to derive a partition principle, then use the arithmetic mean of $v$ within each block as the learning rate. Empirically, Adam-mini matches or improves upon AdamW on LLMs from 39M to 13B parameters across pre-training, SFT, and RLHF, while achieving 49.6% higher throughput on Llama 2-7B due to memory savings enabling larger per-GPU batch sizes and reduced communication overhead.

## Strengths

- **50% memory reduction with on-par performance across LLM scales (39M–13B).** Table 1 concretely documents 50% savings (e.g., Llama 2-7B: 53.92 GB → 26.96 GB). Loss curves in Figures 2, 5, and 6 consistently match AdamW on GPT-2, Llama 1/2/3 pre-training, SFT, and RLHF. The scaling-law experiments (Figure 5) show consistent behavior from 39M to 1B, lending credibility that the method scales.

- **Novel Hessian-structure-based partition principle for Transformers.** The paper identifies that Transformers' smallest dense Hessian sub-blocks correspond to heads (query/key), output neurons (value, attn.proj, MLP), and tokens (embed/output layers). This partition is shown to be necessary—the PyTorch default partition causes training instability at 1B scale (Figure 6i). The leave-one-out experiment (Figure 3) directly supports that a single well-chosen learning rate per block can match or beat Adam's per-parameter rates.

- **Thorough comparison against memory-efficient baselines.** The paper includes Adafactor (two versions), CAME, and SM3 across multiple LLM scales, including hyperparameter sweeps over LR, β₂, ε, and warmup (Section 4.4). Adam-mini consistently outperforms or matches baselines while using the same hyperparameters as AdamW—a practical advantage over methods requiring extensive tuning.

- **Practical throughput gains are honestly documented.** The 49.6% throughput improvement over AdamW on 2× A800-80GB GPUs (Table 2) is attributed to two explicitly stated factors: reduced per-step computation *and* memory savings enabling larger per-GPU batches. The paper does not claim this gain is purely algorithmic.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Gap between the optimal-LR motivation and the averaging heuristic.** The paper's central narrative (Section 3.1) shows that a *grid-searched optimal* single learning rate per dense block can outperform Adam per-parameter rates. However, the actual Adam-mini algorithm uses the *arithmetic mean of $v$* within each block, without validating that this mean approximates the optimal per-block LR or measuring the gap. The paper acknowledges this is "not optimal" (lines 420–422) and provides an intuitive row-wise BP-error argument (lines 358–361), but the connection between motivation and implementation remains at the level of plausibility rather than evidence. A direct comparison on the same small Transformer used in the leave-one-out experiment would close this gap. This does not invalidate the method—the empirical results stand—but weakens narrative coherence.

- **No error bars or multiple seeds on main experiments.** All pre-training, scaling law, SFT, and RLHF results (Figures 2, 5, 6, 7, Table 2) appear to be single runs without variance estimates. The scaling law plots claim Adam-mini achieves "slightly lower loss" (caption of Figure 5); without error bars it is unclear whether this difference is significant or within noise. This is standard practice to flag but not unusual for large-scale optimizer papers.

- **"Generic principle" claim rests primarily on Transformers.** The paper proposes Principle 1 (partition by smallest dense Hessian sub-blocks) as a generic rule, but non-Transformer tasks (ResNet, diffusion models, GNNs) use the PyTorch default partition rather than a Hessian-derived one (line 287). For those architectures the principle is not actually applied—the partition is architecture-agnostic. This narrows the demonstrated scope of the claimed general principle, even though the paper does show non-LLM results.

- **Throughput benefit is not disentangled.** The 49.6% throughput gain is measured at *different per-GPU batch sizes* (4 for Adam-mini vs. 1 for AdamW). While the paper transparently states both contributing factors (algorithmic efficiency and memory-driven batch-size increase), the reported gain conflates them. The *algorithmic* speedup from fewer sqrt/division operations is not separately isolated. A same-batch-size comparison would clarify this and strengthen the paper.

### Trivial

- The condition number analysis (Figure 4) uses a static proxy $g = H_b x$ with random Gaussian $x$ rather than actual training dynamics. The paper frames this as a numerical exploration, but its relevance to practice remains suggestive rather than definitive.

## Nice-to-Haves

- A concise pseudocode box for Adam-mini in the main paper would improve accessibility (the complete algorithm is relegated to the appendix).
- Explicitly state that the Hessian analysis is performed once per architecture and hardcoded, so readers understand the workflow for novel architectures.
- The leave-one-out experiment on a 4-layer Transformer could be extended to a slightly larger model to increase confidence in the motivation.

## Removed Points

- **Non-LLM results "relegated to appendix" criticism:** The parser strips appendix content. The original submission includes these results. However, the substantive point that non-LLM tasks use a different (default) partition is retained above as a scope issue.
- **Missing algorithm pseudocode in main paper:** Relegated to appendix; the parser strips this content. Retained as a nice-to-have above.
- **Criticism that throughput "inflates algorithmic contribution":** The paper explicitly names both factors (lines 349–355). The criticism overstates the problem; the concern is retained in weakened form as a suggestion to disentangle.
- **Typo/formatting/grammar nitpicks:** Parser artifacts, not author errors.
- **Missing related works:** Cannot verify without external sources.
- **"99.9% harmlessly removed" should be qualified:** The abstract already qualifies: "if we (1) carefully partition... (2) assign a single but good learning rate."

## Novel Insights

None beyond the paper's own contributions. The reviews surface the motivation–implementation gap as the central unresolved tension, but this is a gap the paper itself partially acknowledges.

## Suggestions

1. **Validate the averaging heuristic against the optimal per-block LR.** On the same small Transformer used in the leave-one-out experiment, compute the grid-searched optimal LR per dense block and compare it to the average-of-$v$ LR used by Adam-mini. Report both the values and the resulting loss. This directly bridges the motivation and the method, and the required experiment is cheap (the infrastructure already exists in the paper).

2. **Add variance estimates.** Run at least 2–3 seeds for the primary pre-training experiments (GPT-2 125M, Llama 1B) and report final loss variance. For scaling law plots, add confidence bands.

3. **Disentangle the throughput gain.** Report throughput at the same per-GPU batch size (e.g., batch size 1 for both optimizers) to isolate the algorithmic speedup, then separately report the combined effect at the maximum feasible batch sizes. This clarifies the source of the 49.6% improvement.

4. **Acknowledge the scope of the generic principle more precisely.** State explicitly that the Hessian-based partition has been applied and validated on Transformers, while non-Transformer architectures use a simpler default partition that works in practice but has not been derived from Hessian analysis.

## Score and Decision

This paper makes a clear and useful empirical contribution: a 50% memory reduction with matching performance across a wide range of LLM scales, backed by a novel Hessian-based partition analysis for Transformers. The weaknesses (motivation–implementation gap, lack of error bars, scope of the generic principle) are real but do not threaten the core empirical finding that Adam-mini works. They are addressable in revision and do not justify rejection. The paper delivers on its central claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>