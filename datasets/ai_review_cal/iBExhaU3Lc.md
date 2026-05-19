- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes Adam-mini, a memory-efficient optimizer for LLM training that reduces Adam's second-moment buffer ($v$) by ≥99.9%, saving 50% of optimizer memory. The core idea is to partition model parameters into blocks based on the Hessian's near-block-diagonal structure, assign a single learning rate (computed as the average of Adam's $v$ within the block) per block, and otherwise follow Adam's update. Empirically, Adam-mini matches or slightly beats AdamW across LLMs from 39M to 13B parameters on pre-training, SFT, and RLHF, while enabling higher throughput (49.6% on Llama 2-7B with 2× A800-80GB GPUs) due to reduced memory pressure and communication overhead.

## Strengths

1. **50% memory reduction with on-par or better performance across scales.** Table 1 shows memory dropping from 53.92 GB to 26.96 GB for Llama 2-7B, and Figure 1 shows near-identical loss curves. This holds across GPT-2 (125M–1.5B), Llama 2 (20M–13B), and Llama 3 (8B). The central practical claim — that one can cut optimizer memory in half without degrading training — is convincingly demonstrated.

2. **Real throughput and wall-clock gains.** Table 2 reports 49.6% higher tokens/second for Adam-mini vs. AdamW on 2× A800-80GB GPUs, translating to 33.1% less wall-clock time for the same token budget. The advantage stems from two concrete mechanisms: larger per-GPU batch sizes enabled by lower memory, and reduced communication overhead.

3. **No hyperparameter retuning required.** The paper states and experimentally confirms that Adam-mini works well using *the same* hyperparameters (learning rate, β₁, β₂, ε) as AdamW across all experiments. This is a significant practical advantage over other memory-efficient optimizers like Adafactor, which the paper shows requires substantially more tuning effort (Section 4.5).

4. **Extensive Adafactor comparison.** Section 4.5 provides dedicated experiments with both original Adafactor and the Zhai-version, including hyperparameter sweeps on learning rate, β₂, ε, and warm-up steps for Llama 2-20M and 1B. Both Adafactor variants consistently underperform Adam-mini. The throughput comparison also shows Adam-mini is faster (40% higher throughput) due to cheaper row-wise vs. row+column operations.

5. **Consistent performance across diverse LLM tasks.** Adam-mini works for pre-training (GPT-2, Llama), supervised fine-tuning (Llama 2-7B, SFT perplexity), and RLHF (ReMax + MT-Bench scores 5.68 vs. 5.54). This breadth strengthens the claim that the optimizer is a practical drop-in replacement.

## Weaknesses

### Fatal

None.

### Major

None. The core claim — on-par performance with 50% less memory — is well-supported by the empirical evidence. The issues below are real but do not threaten the paper's central contribution.

### Minor

1. **Hessian-based partition principle is validated at very small scale, then extrapolated.** The Hessian visualizations (Figure 7) use a Transformer with vocab=8, dim=16, 4 heads — far from the scale of the models where Adam-mini is ultimately tested. The claim that the specific partition (query/key by heads, value/proj/MLP by output neurons, embeddings by tokens) corresponds to "the smallest dense sub-blocks" rests on visual inspection of this tiny model. The paper would be stronger with a quantitative measure (e.g., block-wise off-diagonal norm ratio) and/or Hessian approximations at moderate scale (e.g., 125M) to directly support the partition choice. However, this does not invalidate the method: the primary evidence that the partition works is the main empirical results up to 13B, and the paper's Principle 1 is presented as a heuristic motivated by analysis, not a proven theorem.

2. **Scaling law results lack uncertainty estimates.** Figure 6 (scaling law) shows single runs without standard deviations, error bars, or multiple seeds. The paper claims "Adam-mini reaches a lower final loss than AdamW for all models," but the gap appears small (~0.01–0.02 in loss). Without multiple runs, it is impossible to distinguish a genuine improvement from run-to-run noise. This is common practice in LLM pre-training papers (300 GPU hours are already reported for these experiments), but the claim of "better" should be softened to "comparable" or supported with variance estimates where feasible.

3. **SFT and RLHF results are from single runs on one base model (Llama 2-7B).** The MT-Bench improvements are marginal (e.g., 5.54 → 5.68 for RLHF) and no variance or significance is reported. This is a minor evidential limitation — the main claim of on-par performance is still supported.

### Trivial

None.

## Nice-to-Haves

- A Hessian proxy (e.g., Hutchinson trace estimate) at moderate scale (e.g., GPT-2-125M) to quantitatively validate that the partition captures dense sub-block structure.
- An ablation on partition granularity (e.g., partition by layer vs. by heads/neurons vs. full AdamW) for a 125M model to directly demonstrate the trade-off.
- Include a variant of AdamW with gradient checkpointing in the throughput comparison to rule out the possibility that the throughput advantage is partly an artifact of memory configuration (though the paper's results already show AdamW OOMs at batch size 2).

## Removed Points

These points were considered and removed with justification:

1. **"Comparison with other optimizers is not exhaustive enough"** (Harsh Critic Weakness 2). The paper provides extensive Adafactor comparison with hyperparameter sweeps on two model sizes, and includes CAME and SM3 baselines. The claim that Adafactor *cannot* perform well is never made; the paper says it "consistently underperforms" under their tuning setup, which is supported by the evidence shown. The suggestion to test downstream tasks with Adafactor is outside the scope of the Adafactor comparison section.

2. **"99.9% harmlessness claim is not directly tested"** (part of Harsh Critic Weakness 1). The harmlessness is demonstrated by the main empirical results (on-par performance at scale), not by the Hessian analysis alone. The Hessian analysis is a motivating framework, not a proof. The 99.9% refers to the *number of learning rates* cut, which is a straightforward counting claim (parameters vs. blocks), not a theoretical claim about performance guarantees.

3. **Missing non-LLM task results in main paper.** The non-LLM results (ResNet, diffusion, GNN) are mentioned but likely detailed in the appendix, which was stripped by the parser. The paper's primary claim is about LLM training.

4. **Generic strengths from Strength Finder** (e.g., "the paper addresses an important problem") — these are dropped as generic/superficial. Only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The core insight — that averaging Adam's $v$ within Hessian-motivated parameter blocks yields a memory-efficient optimizer matching AdamW — is well articulated by the authors. The synthesis of the two reviews does not surface a new observation not already present in the paper.

## Suggestions

1. Add a brief quantitative validation of the partition principle at moderate scale (e.g., GPT-2-125M using a Hessian approximation). At minimum, add a sentence clarifying that the Hessian analysis is a motivating schematic and the primary evidence for the partition comes from the full-scale training results.
2. Temper the "lower final loss" claim for the scaling law results to "comparable final loss" unless multiple runs or confidence intervals are provided.
3. Clarify in the throughput comparison whether gradient checkpointing or other techniques could let AdamW use a larger batch size.
4. Add a brief statement on whether the partition setup has any one-time computational overhead for new architectures, and note that it is hardcoded once per architecture.
