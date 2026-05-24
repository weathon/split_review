Now I have a thorough understanding of the paper and all the reviews. Let me synthesize the final consolidated review.

## Summary

QUOKA is a training-free, hardware-agnostic sparse attention method for chunked prefill. It selects informative queries based on their cosine dissimilarity to the mean query (Step 1), then scores keys against these queries using cosine similarity with max-over-queries/mean-over-GQA-heads aggregation (Step 2-3), and feeds the resulting KV subset to a dense attention kernel. The paper reports strong empirical results: near-baseline accuracy at moderate sparsity, significant speedups (5× attention, 3× TTFT on A100, up to 7× on CPU), and consistent outperformance over seven baselines across five model families and four benchmarks.

## Strengths

1. **Novel geometric observation for query subselection.** The paper identifies that queries with low cosine similarity to the mean query attend more broadly and contribute more to attention logits. This is supported by a correlation of 0.737 between $S_q$ and $\max_k(A)$ in Figure 2c and a PCA visualization (Figure 2b) showing that high-$S_q$ queries lie closer to the key cluster. This insight directly enables the query subselection step that reduces the number of queries used for scoring, unlike prior multi-query methods that treat queries homogeneously (e.g., SampleAttention uniformly samples queries).

2. **Hardware-agnostic design using standard linear algebra.** QUOKA relies only on cosine similarity and top-k operations (Algorithm 1), avoiding custom kernels. This is demonstrated by consistent speedups across Nvidia A100 (5× attention, Figure 5a), Nvidia RTX 2080 (5–6×, Figure 5d), and Intel Xeon CPU (7×, Figure 5c). Prior methods dependent on CUDA kernels (e.g., pattern-based approaches) cannot achieve such portability.

3. **Empirically superior accuracy under high sparsity across models and architectures.** On RULER with $B_{SA}=1024$ (Table 1), QUOKA outperforms all seven baselines on every model and length, often by 10–20% (e.g., Llama3.2-3B at 16k: 70.90 vs. next best 48.59). On LongBench (Table 3), QUOKA achieves relative accuracy 0.945–0.986 at $B_{SA}=512$–2048, while the closest baseline (SampleAttention) reaches 0.738–0.947. Results extend across 6 model families including MoE and NoPE models (Table 2, Table 1), demonstrating generality.

4. **Well-designed aggregation strategy with empirical justification.** The max-over-queries and mean-over-GQA-heads aggregation is justified by the heavy-tailed distribution of attention scores across queries vs. heads (Figure 3). The paper notes that averaging over queries obscures rare but important interactions, while head-level importance is correlated, making the mean appropriate. The pre-aggregation trick (averaging normalized queries before computing the score) is a neat efficiency optimization.

5. **Thorough ablation study showing graceful degradation.** Ablations over $B_{SA}$, $B_{CP}$, and $N_Q$ (Tables 5, 6, 11, 12) show that accuracy degrades gradually with increasing sparsity, with less than 3% drop at 12% token retention. This allows practitioners to tune for different hardware constraints.

## Weaknesses

### Major

None. The core claims are well-supported by extensive empirical evidence.

### Minor

1. **Theorem 1 has a notational gap.** The theorem statement introduces $q_0$ in the premise but switches to $q^*$ in the inequality (line 151) without defining $q^*$. The intended meaning is clear enough (it refers to the query being evaluated), but this is sloppy and undermines the presentation. The theorem is also not essential to the paper's contribution — the empirical observation in Figure 2c is sufficient motivation. The authors should either fix the notation or remove the theorem.

2. **Missing ablation: random query selection vs. the geometric criterion.** The paper's core algorithmic innovation is the query subselection criterion (choosing queries with low cosine similarity to the mean). While the paper compares against SampleAttention (which uses uniform random query sampling) and shows QUOKA substantially outperforms it, a cleaner within-method ablation — replacing only the selection rule with random selection while keeping all other QUOKA components identical — would more directly isolate the benefit of the geometric criterion. This is a gap, though the cross-method comparison already provides meaningful evidence.

3. **"Near-baseline" framing is optimistic at the most aggressive sparsity settings.** On LongBench at $B_{SA}=512$, QUOKA achieves 0.945 normalized accuracy on Llama3.2-3B (5.5% drop) and 0.869 on Qwen2.5-3B (13.1% drop). These are not "near-baseline" in the practical sense. The paper's abstract and "88% fewer" claim correspond to the less aggressive sparsity settings (e.g., $B_{SA}=2048$, where degradation is 1–3%). The paper presents results transparently at all budgets, but the framing could be more precise about which budgets achieve "near-baseline" (e.g., <3% drop) and which do not.

4. **Math500 "surpasses dense attention" claim lacks variance reporting.** The paper states that QUOKA "in some cases surpasses the accuracy of dense attention" on Math500 (Table 8, in the removed appendix). Without confidence intervals or multiple-seed results, a 1-2% improvement on a 500-problem benchmark could be noise. The authors should report standard deviation or tone down the claim.

5. **Absolute latency numbers would be helpful.** The paper reports speedups relative to the dense baseline, which is useful for comparing methods. But absolute latency (e.g., ms per attention call) at a few key sequence lengths would help readers assess whether QUOKA's selection overhead is significant at shorter lengths, where speedup is barely above 1× for some methods (Figure 5a).

### Trivial

- The 88% figure in the abstract ("88% fewer key-value pairs") is stated without specifying the exact configuration (sequence length, $B_{SA}$). The paper's ablation section explains that this corresponds to <3% drop at 12% token retention, but the abstract alone is ambiguous.
- Algorithm 1 uses PyTorch-style dimension notation (`dim=2`, `dim=-1`) without prose explanation; this is fine for a specialist audience but could be clarified.

## Nice-to-Haves

- An ablation replacing QUOKA's cosine-dissimilarity query selection with random selection of the same number of queries, holding all other steps fixed. This would directly quantify the value of the geometric criterion.
- A visualization of the query subselection pattern across a sample of layers/heads (Figure 2 only shows layer 0, head 11), to increase confidence that the correlation generalizes.
- Comparison with a random key selection baseline (no scoring at all) to establish the lower bound.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Theorem 1 is garbled / circular"** (Harsh Critic): The notation issue ($q^*$ undefined) is real and kept as Minor weakness #1. However, the characterization of the theorem as "garbled" and the argument as "circular" is an overstatement — the theorem's intent is clear, its proof is in Appendix D (not available to us), and the paper's empirical evidence (Figure 2c) independently supports the claim. The circularity accusation is speculative.
- **"The paper's main contribution cannot be fully evaluated" without the random query ablation** (Harsh Critic): The paper already compares against SampleAttention (uniform random query sampling), which partially addresses this. The specific within-method ablation would be stronger evidence but is not a prerequisite for evaluating the contribution.
- **"Near-baseline framing is misleading"** (Harsh Critic): The paper transparently reports results at all budgets. The abstract highlights the best-case operating point, which is standard practice. The framing concern is kept as a minor weakness, not a critical issue.
- **"Missing related works"** and **"typo/formatting nitpicks"** (various): These are either outside the scope of this review or are parser artifacts rather than author errors.
- **Generic strengths from Strength Finder** (e.g., "the problem is well-motivated"): These are too generic and lack specific evidence anchoring.

## Novel Insights

The harsh critic's strongest framing — that the theoretical justification is "garbled" and the paper is "misleading" — significantly overstates the problems. The actual paper is well-written, the empirical results are clearly presented, and while Theorem 1 has a notation issue, the core method is sufficiently motivated by the empirical observations in Figure 2. The main value of the reviews is in identifying the missing random-query ablation, which is a clean experiment that would strengthen an already strong paper. The synthesizing insight is that QUOKA's empirical dominance over baselines (10-20% on RULER) is so clear that even removing the theorem entirely would not weaken the paper — the empirical evidence for the method stands on its own.

## Suggestions

1. Fix the notation in Theorem 1: replace $q^*$ with a properly defined variable (e.g., $q$ or $q_0$) and ensure the premise-to-conclusion logical flow is clear.
2. Add a within-method ablation replacing the cosine-dissimilarity query selection with random selection of the same $N_Q$ queries, keeping all other steps identical. This will directly demonstrate the value of the geometric criterion.
3. Add variance (standard deviation or confidence intervals) for the Math500 results, or qualify the "surpasses dense attention" claim.
4. Calibrate the "near-baseline" language: explicitly state which budgets achieve what degradation level (e.g., "<3% drop at $B_{SA} \geq 2048$").
5. Add a small table of absolute latency (ms) for attention at a few key sequence lengths to complement the speedup ratios.

## Score and Decision

**Round 1 bracket (initial):** Based on the three-band calibration search, I observed that papers in the low band (<3.5) had serious flaws in evaluation or novelty; papers in the 3.5–7.5 band had clear contributions but some gaps; and papers in the high band (7.5+) were exceptionally strong with novel contributions and thorough evaluation. QUOKA clearly sits in the upper-middle of the 3.5–7.5 band.

**Round 2 narrowing:** I compared QUOKA against four anchors in the 4.5–6.75 range:
- **SwiftKV (5.50, Reject):** Limited model testing (only Llama-3.1), requires distillation, evaluation gaps. QUOKA is notably stronger — it tests 6 model families, is training-free, and has more comprehensive evaluation.
- **Identify Critical KV Cache (5.75, Reject):** Strong theoretical framing but concerns about theorem correctness and incremental contribution. QUOKA has stronger empirical results (10-20% improvement vs. marginal improvements) and a more novel core idea.
- **Cascading KV Cache (6.00, Accept):** Simple idea, weak baselines (mostly StreamingLLM). QUOKA has stronger baselines, more model diversity, and clearer empirical dominance.
- **Radar (6.60, Accept):** Strong theoretical analysis and solid experiments. QUOKA has weaker theory but arguably stronger empirical dominance over baselines.

**Final calibration:** QUOKA is clearly stronger than SwiftKV (5.50) and the KV Cache paper (5.75), comparable to Cascading KV Cache (6.00), and slightly below Radar (6.60) due to weaker theoretical development. The paper's strengths — novel geometric insight, thorough multi-model multi-hardware evaluation, strong empirical dominance over baselines, practical hardware-agnostic design — outweigh the minor weaknesses (theorem notation, missing ablation, framing precision). The paper is a solid contribution to the sparse attention literature with clear practical value.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>