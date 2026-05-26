Now I have a thorough understanding of the paper. Let me cross-check the reviewer claims against the actual paper content and produce the final consolidated review.

## Summary

TNT introduces a two-stage training paradigm for deep memory modules (Titans, TTT) that decouples training efficiency from inference quality. Stage 1 uses a hierarchical memory architecture — a global module with large chunks for long-range context and parallel local modules with periodic state resets to enable context parallelism. Stage 2 is a brief fine-tuning phase that adapts the local modules to smaller, high-resolution chunk sizes. The paper reports up to **17.37× training speedup** over the standard Titans baseline while simultaneously improving perplexity and downstream accuracy.

## Strengths

1. **Massive training speedup with concurrent quality improvement.** Table 1 shows TNT (C_L={64}) reaches the target loss in 1.12 hours vs. 19.48 hours for the best Titans baseline — a 17.37× speedup. Table 2 shows this faster training does not sacrifice quality: TNT Stage 1 achieves 23.13 avg. PPL vs. 25.07 for the best Titans model, and also improves commonsense reasoning accuracy (41.0% vs. 39.0%). This directly validates the paper's central claim.

2. **Empirically verified linear scaling to long sequences.** Figure 4 provides clear runtime evidence: TNT's runtime stays nearly flat (~400–550 ms) as sequence length grows from 2K to 32K, whereas standard Titans scaling degrades sharply from ~400 ms to ~4000 ms. At 32K, TNT (C_L=128) even outperforms FlashAttention, directly confirming that the periodic-reset mechanism enables effective context parallelism for non-linear RNNs.

3. **Structured, informative ablation.** Table 3 quantifies the contribution of each design choice. Removing the global memory increases PPL by 4.56 (21.04→25.60), confirming its role in compensating for the lost long-range context from local resets. Removing Q-K Projection increases PPL by 0.97 (21.04→22.01), providing concrete evidence for Challenge 2. The progressive addition of local modules (1→4) shows consistent PPL improvements (21.04→20.15), validating the multi-resolution approach.

4. **Precise diagnosis of the train-test chunksize mismatch.** Figure 2 is striking: inference perplexity is minimized *only* when the chunk size exactly matches the training chunk size (C=64), and degrades sharply at smaller or larger sizes. This evidence-driven identification of Challenge 3 is a clear contribution, and Stage 2 provides a targeted solution.

5. **Generality of the framework.** The paper explicitly frames TNT as "a general training paradigm applicable to any deep memory module rather than a specific architecture" (Section 4) and instantiates it on both Titans and TTT. The core ideas — hierarchical global/local memory with periodic resets and decoupled fine-tuning — are architecture-agnostic.

## Weaknesses

### Fatal
None.

### Major

1. **Parameter count matching is not explicitly discussed.** All models in Tables 1–2 are labeled "150M params," but TNT replaces a single memory module (Titans) with a hierarchy containing 1 global memory + up to 4 local memories. Each memory module carries its own fast-weight parameters. The paper does not explain how total parameter counts are held constant across these different architectural configurations (e.g., whether hidden dimensions were reduced to accommodate the additional memory modules). While the speedup claims are unaffected by this (they derive from parallelism, not parameters), the quality comparisons in Table 2 are potentially confounded if TNT has greater representational capacity through additional memory parameters. The authors should state explicitly how the 150M count is maintained, or acknowledge the capacity difference and discuss its implications for the quality comparisons.

### Minor

2. **Multi-local-memory combination mechanism is deferred to the appendix.** The main text (Section 4.1.1) explicitly states "For clarity of illustration, we will assume the simplest case where N = 1. We defer the generalized formulation of TNT to Appendix E." While the appendix presumably contains the full description, a brief sketch of the combination rule (e.g., are local memory outputs summed, gated, or hierarchically combined?) in the main text would aid readability and reproducibility. The experimental results in Table 2 use up to 4 local modules, so the reader should not have to consult the appendix to understand how they interact.

3. **Stage 2 evidence is not as informative as it could be.** The Stage 2 PPL improvements over Stage 1 are small (0.03–0.11 points), and no variance or confidence intervals are reported, making it difficult to assess statistical reliability. More importantly, the paper compares Stage 1 (evaluated at its *training* chunk size) against Stage 2 (evaluated at the *fine-tuning* chunk size). The more compelling comparison would be: Stage 1 evaluated at the Stage 2 chunk size (where Figure 2 predicts catastrophic degradation) vs. Stage 2 evaluated at that same chunk size. That would directly demonstrate the recovery from train-test mismatch that Stage 2 is designed to address. The paper briefly mentions that Stage 2 requires 5% of pre-training compute (citing Table 4 in the appendix) but does not reproduce this figure in the main text.

4. **No training variance reported.** The paper reports single-seed runs throughout. For the Stage 2 differences (as small as 0.03 PPL) and the commonsense accuracy figures (which fluctuate irregularly across configurations, e.g., 40.2% for {4,8,16} vs. 40.6% for {4,8,16,32}), the absence of variance estimates is a meaningful gap. This is standard practice for large-scale training but should be acknowledged, and the risk of over-interpreting small differences should be noted.

5. **The reset interval S_L is not ablated.** The paper introduces S_L (set to 2048 or 4096 in experiments) as a critical hyperparameter that controls the parallelism-performance tradeoff: shorter S_L increases parallelism but truncates local context. The lack of any sensitivity analysis for this parameter is a notable omission, as it directly affects the practical applicability of the method.

6. **Q-K operation terminology and cost analysis.** Describing the sum-of-outer-products operation as "projecting the query onto the subspace spanned by previously observed keys" is slightly imprecise — it produces a vector in the span of the keys, but the cumulative sum of rank-1 projections onto potentially non-orthogonal directions is not itself a projection operator (not idempotent). More importantly, the O(d²) memory cost of maintaining the running sum matrix per local memory is mentioned obliquely ("constant-size state") but not analyzed. For a 150M model (d ≈ 768), this is about 2.4 MB per local memory per chunk — modest but worth quantifying, especially for the 4-local-memory configuration.

### Trivial
None.

## Nice-to-Haves

- An ablation where S_L (the reset interval) is varied to show the tradeoff between parallelism and quality would be a useful addition.
- Including a comparison at 1B+ scale would strengthen the scaling claims, though the paper's scope (150M) is reasonable for a methods paper.
- A comparison against Zhang et al. (2025) — which the paper discusses in Section 1 as related work combining large chunks with local attention — would contextualize the runtime gains.

## Novel Insights

The review process surfaces one novel insight the paper itself does not emphasize: the periodic reset mechanism (Eq. 6) effectively turns the non-linear recurrence into a set of independent sub-problems that can be parallelized across the sequence length. This is conceptually similar to how Mamba's parallel scan linearizes SSM recurrence — but here the "trick" works for arbitrary non-linear updates because the paper does not linearize the recurrence; it simply breaks it with resets. The tradeoff is explicit: the global memory must compensate for the lost cross-segment information. This clean design point — breaking recurrence to enable parallelism, then compensating with a second hierarchical module — could be applicable beyond the specific deep-memory setting.

## Suggestions

1. **Address the parameter count concern explicitly.** Add a sentence in Section 5.1 explaining how the 150M parameter count is maintained across configurations (e.g., by reducing the base model hidden dimension to accommodate additional memory modules), or acknowledge the capacity difference and discuss its implications.

2. **Add a brief description of the N > 1 combination mechanism in the main text.** Even one sentence (e.g., "Multiple local memory outputs are combined via [summation/gating]") would significantly improve clarity without requiring readers to consult the appendix.

3. **Restructure the Stage 2 comparison.** Show a table (or extend Table 2) comparing: (a) Stage 1 model evaluated at its training chunk size, (b) Stage 1 model evaluated at the Stage 2 chunk size (showing degradation), and (c) Stage 2 model evaluated at its fine-tuning chunk size. This would make the benefit of Stage 2 much more transparent.

4. **Include variance estimates or at least acknowledge the single-seed limitation.** For the key comparisons (especially the 0.03–0.11 PPL improvements in Stage 2), noting that these differences may not be statistically significant without repeated runs would increase scientific honesty.

5. **Quantify the O(d²) memory overhead of Q-K projection.** A brief sentence like "This adds 2.4M parameters per local memory at d=768" would help readers assess the practical cost.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>