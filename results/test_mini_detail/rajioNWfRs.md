Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

TNT introduces a two-stage training paradigm for deep memory modules (models like Titans where a sub-network is updated online to memorize context). Stage 1 uses a hierarchical memory architecture: a global memory operating on large chunks for long-range context, and multiple parallel local memories with periodic state resets that break sequential dependencies, enabling context parallelism even for non-linear recurrences. A Q-K projection resolves a compression-retrieval domain mismatch. Stage 2 briefly fine-tunes the local memories to a smaller chunk size to improve inference. On 150M-parameter Titans models trained on 10B tokens, TNT reaches a target loss up to 17× faster than the most accurate Titans baseline while also improving perplexity and commonsense reasoning accuracy.

## Strengths

1. **Genuine innovation in parallelizing non-linear deep memory training.** The core idea—periodic resets of local memory states to a learned initial state, enabling shard-level parallelism while a global memory captures long-range context—is a clever and non-obvious solution to the long-standing challenge of parallelizing non-linear recurrences. Section 4.1.1 clearly articulates the mechanism (Eq. 6) and its motivation.

2. **Substantial training speedup with competitive or better quality.** Table 1 shows TNT reaches a target loss of 3.20 in 1.12 hours (C_L=64) versus 19.48 hours for Titans (C=8), a 17.37× speedup. Even with the same local chunk size (C_L=8 vs. C=8), TNT is 7.68× faster. Table 2 shows TNT Stage 1 achieves lower perplexity (23.13) and higher commonsense accuracy (41.0%) than the best Titans configuration (25.07 PPL, 39.0% acc) and vanilla Transformer (23.58 PPL, 38.3% acc).

3. **Q-K Projection is well-motivated and empirically validated.** Section 4.1.2 identifies a concrete domain mismatch (memory is trained on keys but queried with queries) and proposes a principled fix. The ablation in Table 3 shows removing Q-K projection increases perplexity from 21.04 to 22.01 (nearly 1 point), confirming its practical importance.

4. **Clear problem decomposition.** Section 3 systematically lays out three fundamental challenges (training inefficiency, compression-retrieval mismatch, chunk-size sensitivity), providing a clean narrative that structures the proposed solutions. This makes the paper's contributions easy to follow and evaluate independently.

## Weaknesses

### Fatal
None.

### Major

1. **Runtime scaling analysis is confounded by token-based batching and does not support the "linear scaling" claim.** Figure 4 and Section 5.2 fix *total tokens per batch* at 0.5M and vary sequence length. As the paper states: "keeping the number of tokens per batch fixed." When sequence length doubles, the number of sequences in the batch halves. Under this setup, a model whose per-sequence cost scales linearly would show *constant* total batch cost, not linear growth. TNT's near-flat runtime (~400ms across 2K–32K for C_L=16) is exactly what one would expect from this experimental design, not evidence of linear scaling. To meaningfully demonstrate scaling behavior, batch size (number of sequences) must be fixed while sequence length varies independently. The current presentation is misleading and undermines a headline claim. The comparative speed advantage over Titans is still valid (since Titans' runtime grows much faster), but the "linear scaling" narrative is not supported by the presented experiment.

2. **Only one deep memory architecture is evaluated despite claims of generality.** The paper states that "TNT is a general training paradigm applicable to any deep memory module" (Section 1, end of p.2) and the abstract claims "Evaluated on Titans and TTT models, TNT achieves a substantial acceleration..." However, the experiments instantiate TNT only on Titans. TTT (Sun et al., 2024) appears only as a baseline competitor (Table 2), not as a host model for TNT. The abstract's claim is factually incorrect about the scope of evaluation. Without demonstrating TNT on at least one other architecture (e.g., TTT or Atlas), the generality claim remains untested.

3. **Stage 2 fine-tuning delivers marginal improvements that do not convincingly resolve Challenge 3.** The best Stage 2 model (C_L={2,4,8,16}) achieves 23.09 PPL, only 0.04 lower than the best Stage 1 model (C_L={4,8,16,32}) at 23.13 PPL. No variance or multiple-seed results are reported, so it is impossible to assess whether this difference is meaningful. Furthermore, the C_L={1} configuration (which directly enables chunk-size-1 inference — the stated goal of Stage 2) achieves only 23.99 PPL, which is *worse* than the Stage 1 best. The paper needs to directly compare (a) Stage 1 evaluated at a smaller chunk size vs. (b) Stage 2 fine-tuned for that smaller chunk size, with error bars, to convincingly show that Stage 2 resolves the chunk-size mismatch rather than just providing a marginal boost.

4. **No statistical significance or variance reporting.** All experiments appear to be single runs with no reported standard deviations. Given the 150M parameter scale, the 10B token training budget, and the small differences in some comparisons (e.g., 0.04 PPL for Stage 2, fractional accuracy differences in Table 2), variance estimates are essential. This is especially important for the downstream commonsense reasoning results where differences are often within 1–2 percentage points.

### Minor

1. **Quality gains are partially confounded with architectural capacity, not just training efficiency.** TNT's hierarchical architecture (1 global memory + up to 4 local memories) is fundamentally different from the baseline Titans (single memory module). Table 3 shows monotonic perplexity improvement as more local memories are added (23.53 → 21.04 → 20.74 → 20.47 → 20.15). This is exactly what one would expect from increasing model expressiveness. Although parameter counts are matched (150M), the architectural change itself likely contributes to quality gains. The paper does not disentangle how much of the improvement comes from the training paradigm (resets, parallelism, Q-K projection) versus the memory multiplexing. This does not invalidate the results but weakens the attribution to "training efficiency innovations."

2. **Q-K projection's computational and memory overhead is not reported.** The Q-K projection maintains a running sum of d×d matrices per local memory module (Eq. 7). For d=512 and N=4 local memories, this is 4 × 512² ≈ 1M additional parameters and quadratic overhead during the projection computation. The ablation shows a significant quality impact (Table 3) but there is no corresponding runtime, FLOPs, or memory comparison. Given that speed is a central claim, the overhead should be quantified.

3. **Figure 2's sensitivity analysis is limited.** The figure showing inference chunk-size sensitivity only covers one model size (550M) and one training chunk size (64). Showing this pattern across multiple training chunk sizes would strengthen the claim that this is a general phenomenon (Challenge 3).

4. **Ablation training times are not reported.** Table 3 shows quality impacts of various components (w/o global memory, w/o Q-K projection) but does not report training time. The "w/o global memory" ablation likely loses the parallelism benefit of the global module, making it informative to know the speed impact.

### Trivial
None.

## Nice-to-Haves
- **Inference throughput comparison:** The paper motivates chunk-size-1 inference for autoregressive decoding but provides no inference speed (tokens-per-second) comparison between TNT, Titans, and Transformers.
- **Second deep memory host:** A small-scale TNT-on-TTT experiment (even on a single dataset) would substantially strengthen the generality claim.
- **Per-component runtime breakdown:** A FLOPs or wall-time breakdown showing how time is distributed across global memory, local memories, Q-K projection, and feed-forward layers.

## Removed Points
These points were flagged by the reviewers but are removed for the following reasons:
- *Missing related work* — Rule prevents including this (no external verification).
- *Typos/formatting artifacts* — These are parser errors, not author errors.
- *Reproducibility nitpicks (hyperparameters, implementation details)* — The paper provides sufficient training details (AdamW, cosine schedule, TPUv4 setup).
- *Strength/Superficial praise (e.g., "addresses an important problem")* — Dropped as generic/superficial without specific evidence.
- *"Misses comparison to concurrent work" (Guo et al. 2025, Zhang et al. 2025)* — These are cited in the paper (Section 1) and discussed qualitatively; an empirical comparison would strengthen the paper but the omission is not a weakness per se given that the paper positions TNT as complementary.

## Novel Insights

The reviews collectively surface two tensions not fully resolved in the paper itself. First, the "linear scaling" claim rests on a confounded experimental design (fixed total tokens), yet the comparative speedup over Titans at matched configurations is still real and valuable—the paper should decouple these two claims. Second, the Stage 2 fine-tuning results suggest a deeper issue: if adding more local memory modules (architectural expansion) drives most of the quality gain, the two-stage training paradigm may be less crucial than the hierarchical memory design itself. An ablation that applies the hierarchical memory to Titans' training pipeline (without the reset/parallelism benefit) would clarify this. Neither of these observations invalidates the paper's contributions, but they point to where the authors should focus their revision.

## Suggestions

1. Rerun the runtime scaling experiment with a fixed batch size (number of sequences) and varying sequence length to properly demonstrate linear scaling. Report results on a linear-linear plot (not log-scale) for clarity.
2. Conduct a small-scale TNT-on-TTT experiment (e.g., 150M, single dataset) to demonstrate generality, or adjust the abstract and claims to accurately reflect that only Titans was tested.
3. Report all key results (Table 2, Table 3) over 3 random seeds with standard deviations.
4. For Stage 2, directly compare the Stage 1 model evaluated at chunk size 1 (which Figure 2 predicts will be poor) against the Stage 2 model fine-tuned for chunk size 1, with variance estimates.
5. Add a column to Table 3 showing training time for each ablation to clarify the efficiency cost of each component.
6. Report the FLOPs and memory overhead of the Q-K projection mechanism.

## Score and Decision

**Calibration:** I performed a two-round calibration search over the human-review corpus.

*Round 1 (bracketing):*
- Weak band (avg ≤3.5) — papers scoring 1.5–3.0 on unrelated RNN/memory topics. TNT is clearly stronger.
- Middle band (3.5–7.5) — papers scoring 4.0–5.75 including RetNet (4.75, Reject), LightSeq (5.0, Reject), Efficient Long-range LM (5.75, Reject), Hierarchical Feature Sharing (5.75, Reject). Initial bracket: [4.5, 6.5].
- Strong band (≥7.5) — papers scoring 7.6–8.0 (oral/spotlight). TNT is clearly below these.

*Round 2 (narrowing):*
- TTT-Layer paper (avg 6.0, Reject) — Also about deep memory modules (TTT layers). Experiments up to 1.3B vs. TNT's 150M, but had novelty and missing-baseline concerns. TNT has clearer novelty but weaker experimental breadth and the confounded scaling analysis. TNT is slightly weaker → below 6.0.
- DS-LLM (avg 6.0, Accept Poster) — Different topic (analog hardware). Hard to compare directly but indicates acceptance threshold ≈ 6.0.
- Efficient Long-range LM (5.75, Reject) — Similar evaluation limitations (small models, single domain). TNT's speedup results are stronger, but the confounded analysis and marginal Stage 2 results pull it down. Comparable to this paper.

After reading 5 anchor papers in full (RetNet, LightSeq, Efficient Long-range LM, TTT-Layer, DS-LLM), the paper under review sits between RetNet (4.75) and TTT-Layer (6.0). It has clearer novelty than RetNet but shares similar overclaiming concerns (abstract claims evaluation on TTT models, runtime scaling claim poorly supported). The quality evidence is stronger than RetNet but the evaluation breadth is narrower than TTT-Layer. The most appropriate anchor is between LightSeq (5.0) and Efficient Long-range LM (5.75), closer to LightSeq.

**Final score:** 5.0 — marginally below the acceptance threshold. The core ideas (hierarchical memory with periodic resets) are novel and well-motivated, and the speedup/quality results are promising. However, the confounded scaling analysis, single-architecture evaluation, marginal Stage 2 evidence, and lack of variance reporting collectively prevent the paper from fully substantiating its central claims in the current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>