Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper presents FLARE, a method for fine-tuning ReLU activations and FIRE relative position encodings into pre-trained Softmax-based transformer models. The core contributions are: (1) showing that fine-tuning ReLU from a Softmax checkpoint yields better loss than training ReLU from scratch, (2) identifying that the specific sequential recipe "FIRE first, then ReLU" is necessary for length generalization, (3) the FLARE fused algorithm that exploits ReLU sparsity to skip 98.9% of FIRE addition operations, and (4) a custom CUDA kernel and hardware PPA analysis demonstrating efficiency gains.

## Strengths

- **Fine-tuning ReLU into a Softmax-pretrained model yields lower validation loss than training ReLU from scratch.** Figure 2 compares these approaches over the same total iterations (30k), and the fine-tuned model reaches better loss. Section 4.1 also reports a 29% reduction in total training time (12h vs 17h), a concrete practical advantage.

- **Only the sequential recipe "FIRE first, then ReLU" imparts length generalization.** Figure 5 compares four fine-tuning recipes at context lengths 2048 and 4096 (2× and 4× the training length of 1024). The FIRE-then-ReLU recipe maintains nearly flat validation loss at extended lengths, while the other three recipes and RoPE baselines show large degradation. This is the first demonstration that fine-tuning order determines whether a ReLU-based attention model achieves length generalization.

- **The FLARE fused algorithm enables skipping 98.9% of FIRE addition operations.** Section 5 reports that the ReLU probability matrix is 98.9% zeros in the lower triangle for causal attention. The FLARE algorithm's branch condition (f<sub>ij</sub> ≤ -a<sub>ij</sub>) holds 98.9% of the time, so the addition can be omitted — a direct computational saving derived from the fusion.

- **Hardware synthesis on 130nm CMOS shows ReLU achieves 8× higher frequency, 0.1% of the power, 0.11% of the energy per cycle, and 1% of the silicon area compared to Softmax** (Table 1, Section 6.2). These are concrete, measured PPA numbers demonstrating dramatic hardware-level improvements.

- **The custom ReLUFlashAttention CUDA kernel achieves an average 3.8× speedup over FlashAttention for context lengths 512–4096** (Figure 8, Section 6.1), confirming the practical inference-time benefit of ReLU in a modern GPU implementation.

- **Detailed analysis of ReLU input/output statistics during fine-tuning** (Figures 6, 7) shows stabilization after ~3k iterations and that only 1.1% of outputs are non-zero, providing insight into how the model adapts to ReLU.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No variance or error bars on the length generalization experiment.** Figure 5 presents single-run validation loss comparisons at extended context lengths. The claim that only the FIRE-then-ReLU recipe imparts length generalization is a central result, and the paper would benefit substantially from multiple runs with error bars or at least some indication of statistical reliability. Without this, the observed differences (~0.1 loss units between recipes) could potentially be noise.

- **Sparsity measurement protocol is underspecified.** The 98.9% sparsity figure (Sections 4.3 and 5) is a key result motivating the FLARE algorithm, but the paper does not specify the measurement details: over how many tokens, which layers, which attention heads, or which sequences in the validation set. The claim that "on average only 1.1% of outputs are non-zero" needs a clear protocol (e.g., "averaged over 500 validation examples across all 12 layers and 12 heads") to be reproducible and trusted.

- **The NopE and RoPE baselines in Figure 5 are not described in the methods section.** These appear only in the figure caption. Their training procedures are not specified, which makes it difficult to assess whether the comparison is fair or what they represent as controls.

- **Hardware PPA comparison could be more transparent.** The Softmax baseline (Stevens et al., 2021) and the ReLU design are not described in enough detail (precision, pipeline depth, support logic) to assess whether the comparison is apples-to-apples. The claimed 0.11% energy per cycle is striking but undersupported — the paper should clarify what exactly is being compared (standalone activation modules vs. full attention units) and how these savings translate to end-to-end accelerator performance.

- **The 3.8× CUDA kernel speedup over FlashAttention lacks sufficient profiling context.** The paper does not describe the GPU model (A100 is mentioned for training but not for kernel profiling), whether FlashAttention is from the official implementation, what tiling configurations are used, or how the speedup breaks down across operations (QK<sup>T</sup> matmul, ReLU, V projection). Replacing just the Softmax with ReLU would not alone explain a 3.8× end-to-end speedup.

- **No empirical comparison to enhanced ReLU variants from prior work.** The paper cites Wortsman et al. (2023), Shen et al. (2023), and Zhang et al. (2021) who proposed learned divisors and additional normalization for ReLU attention. The paper claims prior work "had not explored fine-tuning," which is correct, but does not compare against those methods — leaving unclear whether fine-tuning alone matches or exceeds their results without extra operations.

- **Uncertainty about the final quality relative to the original Softmax model.** Experiment 1 (Figure 2) shows fine-tuned ReLU beats ReLU from scratch, but does not explicitly state how the fine-tuned ReLU model's loss compares to the original Softmax model's loss at the start of fine-tuning. The figure suggests the model recovers to approximately the Softmax checkpoint loss, but the paper does not state this comparison, which would help readers evaluate whether the ReLU replacement is "free" in terms of quality.

### Trivial
None.

## Nice-to-Haves

- Add a control experiment where the Softmax model is trained for an additional 10k iterations (without switching to ReLU) to show that the benefit is not simply "more training helps."
- Profile the FLARE fused vs. unfused version to quantify whether the branch comparison overhead outweighs the saved additions in wall-clock time.
- Evaluate on at least one task-based long-context benchmark (e.g., a subset of LongBench or RULER) to validate that the validation loss improvements at extended lengths translate to actual task performance.
- Report per-layer sparsity statistics to show whether the 98.9% figure is uniform or varies across the network.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The core comparison is confounded by an unfair starting point"** (Harsh Critic Point 1): This criticism claims Experiment 1 is confounded because the fine-tuned model starts from a better checkpoint. However, the paper's claim is specifically scoped to comparing *fine-tuning ReLU vs. training ReLU from scratch* — exactly what Figure 2 shows. The requested control ("continue training Softmax for 10k more iterations") answers a different question (ReLU fine-tuning vs. continued Softmax training) that the paper does not claim to address. The criticism misunderstands the intended comparison. A softened version of this (wondering how the final ReLU model compares to the original Softmax model) is kept as a Minor weakness above.

2. **"Abstract claim is misleading"**: The abstract says "shave 98.9% of FIRE operations," which the critic claims is ambiguous. The body of the paper (Section 5) clearly explains that this refers to skipping FIRE additions via the FLARE branch condition. The abstract is adequately precise.

3. **"Table 1 numbers difficult to parse"**: This is a parser artifact (image rendering), not a paper problem.

## Novel Insights

The most interesting finding is that **fine-tuning order matters** for whether a ReLU-based attention model inherits the length generalization property from FIRE. The fact that simultaneous fine-tuning or ReLU-first sequential fine-tuning fails to impart length generalization — while FIRE-first-then-ReLU succeeds — suggests that FIRE must be "baked in" while the model still has Softmax attention's dense probability distribution before ReLU sparsity collapses the signal pathways. This interaction between the order of architectural changes and the resulting model behavior is a non-obvious insight that goes beyond the individual contributions of ReLU or FIRE in isolation.

## Suggestions

- Run the length generalization experiment (Figure 5) with at least 3 random seeds and report error bars.
- Specify the sparsity measurement protocol precisely: number of tokens, layers, heads, sequences, and whether the statistic is per-head or aggregated.
- Include a brief sentence in Experiment 1 stating the final loss of the fine-tuned ReLU model relative to the original Softmax model's loss at 20k iterations.
- Describe the NopE and RoPE baselines' training procedures in Section 3.3.3.
- Add profiling details for the CUDA kernel comparison: GPU model, FlashAttention version, tiling configuration, and a breakdown of where the 3.8× speedup originates.
- Compare against at least one enhanced ReLU baseline (e.g., Wortsman et al.'s softmax-free attention) on the same fine-tuning setup.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>