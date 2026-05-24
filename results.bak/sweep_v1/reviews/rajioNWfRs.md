Now I have all the information I need. Let me produce the final review.

## Summary

This paper introduces TNT (Two-stage Non-linear Training), a training paradigm for deep memory modules (e.g., Titans, TTT) that resolves the conflict between training throughput and inference accuracy caused by the chunk-size hyperparameter. Stage 1 uses a hierarchical memory architecture — a sequentially-updated global memory operating on large chunks and parallel local memories with periodic state resets — to enable context parallelism for inherently non-linear recurrences. Stage 2 fine-tunes only the local memories at a smaller chunk size with minimal additional compute. Experiments on 150M-parameter Titans models demonstrate up to 17× training speedup over the slowest Titans baseline while maintaining or improving perplexity.

## Strengths

- **Novel mechanism for parallelizing non-linear RNNs.** The hierarchical memory with periodic local-state resets (Eq. 6) is a clean and genuinely innovative solution to a real bottleneck. Unlike linear RNNs (where parallel scans apply), non-linear deep memory modules have lacked efficient parallelization; the paper provides a principled way to break sequential dependencies across sequence shards while preserving global context through the global memory module. This is the paper's strongest conceptual contribution.

- **Clear linear runtime scaling demonstrated.** Figure 4 shows TNT's per-step runtime grows linearly (~400–550ms) from 2K to 32K sequence length, while Titans (C=16) grows from ~400ms to ~4000ms. At 32K, TNT (C_L=128) is even faster than FlashAttention, confirming superior scalability for long contexts. This evidence is clean, visually compelling, and independent of parameter-count concerns.

- **Time-to-quality speedup is genuine and well-measured.** Table 1 compares time to reach the same target loss (3.20). TNT (C_L=64) reaches it in 1.12 hrs vs. 4.18 hrs for Titans (C=64) and 19.48 hrs for Titans (C=8). Even against the most natural baseline (C=64), the 4.67× speedup is substantial and practically meaningful. The paper explicitly acknowledges that TNT does not yet match FlashAttention-optimized Transformers, which is appropriate.

- **Q-K Projection is a well-motivated fix for the compression-retrieval mismatch.** Challenge 2 (Section 3) identifies a real issue — during compression the network maps keys→values but at retrieval it receives queries — and the Q-K projection (Eq. 7) is a computationally lightweight solution. The ablation (Table 3) shows its removal increases PPL from 21.04 to 22.01, validating the hypothesis.

## Weaknesses

### Major

- **Parameter count not controlled in quality comparison (affects core quality claims).** The TNT models with N local memories (Table 2, rows 264–267) have strictly more fast-weight sub-networks than the baseline Titans model (1 global + N local vs. 1 memory module). The paper states "150M parameter models" for all configurations but never reports per-configuration parameter counts or explains how the total parameter count is held constant when adding local modules. The perplexity improvements (e.g., 20.15 vs. 25.07) cannot be cleanly attributed to the hierarchical design vs. increased capacity. A controlled experiment — e.g., matching total parameters by scaling down per-module size, or comparing TNT N=1 against a Titans model with a similarly-sized single memory — is absent and would be necessary to support the quality claims. This is the most significant methodological gap.

### Minor

- **Generality claim is unverified.** The paper presents TNT as "a general training paradigm applicable to any deep memory module" (Section 1) and the abstract states "Evaluated on Titans and TTT models," but all TNT instantiations use Titans. TTT (Sun et al., 2024) appears only as a baseline, not as a model on which TNT is applied. Without at least one additional instantiation, the generality claim is unsupported.

- **Quality results lack statistical rigor.** Perplexity and accuracy numbers (Table 2) are single point estimates with no confidence intervals, error bars, or significance tests. The accuracy improvements over Transformers are small (e.g., 41.0% vs. 39.7%) and could be within noise range, especially at the 150M scale. The paper notes that perplexity is "more stable" for small models but still draws conclusions from the accuracy numbers.

- **Computational overhead of Q-K projection not analyzed.** The projection (Eq. 7) requires maintaining a running d×d matrix and performing a matrix-vector multiply per token. The paper claims it is "efficient" but provides no FLOP count, memory footprint, or runtime breakdown. Since the whole point of the method is efficiency, omitting this analysis is a notable gap.

### Trivial

- **"W/o global memory" ablation (Table 3) compares against a deliberately weakened variant.** Removing the global memory while keeping the local memories with resets produces a model with no cross-chunk information — this is expected to perform poorly (PPL 25.60). A cleaner comparison would contrast TNT against a standard chunkwise Titans model with matched parameters, isolating the effect of the reset mechanism.

## Nice-to-Haves

- A comparison of Stage 2 fine-tuning against the alternative of training from scratch with the small chunk size for the same compute budget would help contextualize the fine-tuning benefit.
- A runtime breakdown per component (global memory, local memories, overhead) would help identify where further optimizations are needed.
- Reporting absolute GPU-hours for Stage 2 (currently only given as "5%") would aid reproducibility.

## Removed Points

- **"Misleading speedup framing" (Critic's Point 2):** The abstract states "up to 17× faster than the **most accurate baseline configuration**" (Titans C=8, PPL 25.07). This is precise and not misleading. The paper also reports speedup against Titans C=64 (4.67×) and acknowledges TNT is slower than FlashAttention Transformers. Removed because the criticism misreads the paper's explicit framing.
- **"Challenge 1 is well-known" (Critic's Section-by-Section):** This is a subjective opinion about novelty framing, not an identifiable weakness. Removed.
- **"Challenge 3 contradiction is manufactured" (Critic's Section-by-Section):** The observation that models overfit to training chunk size is a valid empirical finding; whether it is "unsurprising" is a matter of interpretation, not a flaw. Removed.
- **Strength Finder generic strengths:** Several claimed strengths (e.g., "the paper addresses an important problem") are generic and not backed by specific evidence from the paper. Removed.

## Novel Insights

The most interesting interaction across the reviews is the tension between the paper's clearly demonstrated efficiency gains (linear scaling, 4–17× speedup) and the confounded quality comparison. The hierarchical memory with resets is a genuinely useful engineering contribution regardless of the quality claims — enabling non-linear RNN training that was previously forced to use tiny, hardware-inefficient chunks. The parameter-count issue would be straightforward to address in a revision (scale down per-module size to match totals) and the core speedup results would likely survive such a check. The unverified generality claim is a more open question: whether the reset mechanism hooks cleanly into architectures like TTT that use different update rules depends on details not explored in the paper. None of the reviews identified a fatal flaw; the most serious issues are about what the evidence supports, not about correctness.

## Suggestions

1. **Report parameter counts per configuration** and ideally run a controlled experiment where TNT (N=1) is compared to a Titans model with an equivalently-sized memory sub-network to isolate the effect of the hierarchical design from capacity.
2. **Tone down the generality claim** or add at least one additional instantiation (e.g., TNT on TTT with one local module) to demonstrate the framework is not Titans-specific.
3. **Add error bars or confidence intervals** to the quality results (Table 2), or at minimum run each configuration multiple times to establish variance, especially for the small accuracy differences.
4. **Report the FLOP/memory overhead of the Q-K projection** to substantiate the claim that it is efficient.

## Score and Decision

**Calibration anchors used (all queries combined):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/s1kyHkdTmi.md` (NAMM) | 7.00 | Stronger in experiment rigor but on a more mature topic (KV cache pruning); paper under review has more novel mechanism but weaker quality controls |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TvGPP8i18S.md` (MELODI) | 6.25 | Similar hierarchical memory theme; MELODI has better-controlled experiments but TNT tackles a harder parallelization problem |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IiagjrJNwF.md` (Memory Mosaics) | 6.25 | Both propose novel memory architectures; Memory Mosaics lacks ablation details while TNT has a parameter-count confound |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BI2int5SAC.md` (EM-LLM) | 5.75 | Both have overclaiming issues (EM-LLM on "human-like," TNT on generality); comparable evidence quality |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/h3wbI8Uk1Z.md` (RNNs≠Transformers) | 5.50 | Both address RNN limitations; RNNs≠Transformers is theoretical while TNT is empirical — TNT's evidence is stronger on efficiency but confounded on quality |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7iuFxx9Ccx.md` (SlimTTT) | 6.00 | Also uses test-time training but in vision; rejected despite decent score, mainly for incremental contribution concerns |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IhOeYKqnfp.md` (Continual Memory Neurons) | 4.25 | Less focused contribution with methodology gaps; paper under review is stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/N581Nje6fH.md` (Long Horizon Episodic) | 1.50 | Incomplete early work; substantially weaker than paper under review |

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**