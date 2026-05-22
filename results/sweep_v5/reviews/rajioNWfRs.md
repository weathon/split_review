Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary

This paper introduces TNT (Two-stage Non-linear Training), a training framework for deep memory modules (e.g., Titans) that combines: (1) a hierarchical memory architecture with periodic state resets enabling context parallelism, (2) a Q-K projection mechanism to resolve compression-retrieval mismatch, and (3) a two-stage procedure (efficiency-focused pre-training with large chunks, then performance-focused fine-tuning with small chunks). Experiments on 150M-parameter models show up to 17× training speedup over Titans baselines while maintaining or improving perplexity and reasoning accuracy, with linear runtime scaling at long sequences.

## Strengths

- **Periodic state resets for context parallelism (Eq. 6) is a genuine technical innovation.** The paper identifies that sequential dependencies in non-linear deep memory modules prevent effective parallelization, and proposes breaking them by resetting local memory states to a learnable initial state at fixed intervals. This enables massive parallelism across sequence shards—a non-trivial solution to a long-standing challenge that prior work (Zhang et al., 2025; Guo et al., 2025) did not resolve for deep memory modules.

- **Q-K Projection (Eq. 7) with running-sum implementation is a clean, practical fix for the compression-retrieval mismatch.** The ablation in Table 3 confirms its effect: removing it increases perplexity from 21.04 to 22.01 (+0.97 PPL). The constant-memory running-sum formulation makes it deployment-friendly.

- **Strong end-to-end speedup results.** Table 1 shows TNT with C_L={64} reaches target loss 3.20 in 1.12 hours vs. 19.48 hours for the most accurate Titans baseline (C=8). Even controlling for chunk size (C_L={8} vs. Titans C=8), TNT achieves 7.68× speedup. Figure 4 demonstrates linear runtime scaling: at 32K tokens, TNT (550ms) is ~7× faster than Titans (C=16) at ~4000ms and slightly faster than FlashAttention.

- **Clean ablation study.** Table 3 systematically isolates the contribution of each component: adding local memories progressively improves PPL from 23.53 (Titans) to 20.15 (4 local modules); removing the global memory causes a 4.56 PPL penalty; removing Q-K projection causes a 0.97 PPL penalty; Stage 2 fine-tuning provides further improvement.

- **Clear problem identification.** Section 3 articulates three concrete challenges (training inefficiency, compression-retrieval mismatch, chunk-size sensitivity) with empirical validation in Figure 2 showing the over-specialization to training chunk size.

## Weaknesses

### Major

- **Abstract overclaims evaluation on TTT.** The abstract states "Evaluated on Titans and TTT models," but the experiments (Section 5) only instantiate TNT on the Titans architecture. TTT appears solely as a baseline in Table 2 (PPL 27.62). This is a factual discrepancy between the scope advertised in the abstract and what the experiments actually demonstrate. While the paper claims TNT is "a general training paradigm applicable to any deep memory module" (line 43), this generality claim is untested beyond a single architecture.

- **The "general training paradigm" framing outstrips the evidence.** TNT bundles architectural changes (hierarchical memory with global + local modules, periodic resets, Q-K projection) with a training procedure (two-stage pre-training then fine-tuning). The experiments compare this bundled system against the original Titans architecture. The paper does not test whether applying only the training procedure (periodic resets + two-stage, without the global memory or Q-K projection) to the original Titans architecture yields speedups. Without this control, it is unclear whether the claimed speedup is attributable to the procedural contribution, the architectural additions, or their combination. The framing as a "training paradigm" rather than a "system" overstates what is isolated.

### Minor

- **Stage 2 fine-tuning gains are very small.** The perplexity improvements from Stage 1 to Stage 2 range from 0.03 to 0.11 PPL (e.g., 23.13 → 23.09 for the best configuration). The paper claims Stage 2 "consistently lowers perplexity," which is technically true, but the magnitudes are near the noise floor. No confidence intervals or multiple-seed results are reported to establish statistical significance. The claim that this resolves Challenge 3 is weakened by the tiny improvements.

- **No parameter budget breakdown.** All models are reported as 150M parameters, but TNT adds a global memory module and up to 4 local memory modules, each containing a neural sub-network. The paper does not explain how the parameter budget is distributed across components (e.g., whether hidden dimensions were reduced in TNT to compensate for additional memory modules). Without this, comparisons against Titans and Transformers are not fully controlled for effective model capacity, though this is standard practice in the field and is a transparency issue rather than a validity issue.

- **Ablation "w/o global memory" (PPL 25.60) is worse than baseline Titans (PPL 23.53).** This shows that the local memory with periodic resets, on its own, underperforms the original Titans. The result is consistent with the paper's design rationale (the global memory compensates for lost cross-chunk information), but it does reveal that the reset mechanism alone is harmful without the global memory—this nuance is under-discussed.

### Trivial

- None.

## Nice-to-Haves

- A controlled experiment applying TNT's Stage 1 training procedure (periodic resets + two-stage) to the original Titans architecture (single memory, no global memory, no Q-K projection) to directly measure the training paradigm's isolated effect.
- A small-scale demonstration on a second deep memory module (e.g., TTT) to substantiate the "generality" claim, even at reduced model size.
- Confidence intervals or multiple-seed runs for the perplexity and accuracy results, especially for the Stage 2 gains.
- A breakdown of how the 150M parameter budget is distributed across components (global memory, local memories, Q-K projection, feed-forward layers).

## Removed Points

- **Harsh critic's point about the 17× speedup being biased toward a headline number.** The paper clearly states it compares against the "most accurate baseline configuration" (Titans C=8), which is standard practice. The paper also reports speedups against Titans C=64 (4.18/1.12 ≈ 3.7×) and TNT C_L={8} vs Titans C=8 (7.68×). The headline is appropriately caveated.

- **Harsh critic's point about "global memory is doing most of the heavy lifting."** This is a misinterpretation of the ablation: the "w/o global memory" condition removes the component specifically designed to compensate for information lost due to periodic resets. The paper's design is that global + local work together, and the ablation confirms this. It does not undermine the contribution.

- **Strength Finder's generic strengths** (e.g., "systematic identification of three fundamental challenges" as a standalone strength; "Stage 2 fine-tuning with minimal overhead" claimed as a strength despite tiny gains) — these were either generic or conflicted with verified weaknesses and were removed.

- **Criticisms about missing appendix content or unreleased code/data.** These are parser artifacts or violate the "hard rules" about questioning the existence of cited entities.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension in the paper's framing—that TNT is presented as a "training paradigm" but the evaluation never separates the procedural contribution from the architectural one. This is a genuine insight that the authors should address, but it does not invalidate the paper's substantial empirical results.

## Suggestions

1. **Correct the abstract overclaim.** Either remove "and TTT models" from the abstract, or add a small-scale TTT-based experiment (even at a smaller parameter count) to support the generality claim.
2. **Add a controlled experiment** that applies only the training paradigm (resets + two-stage, without global memory or Q-K projection) to the original Titans architecture to isolate the procedural contribution. This would substantially strengthen the "general training paradigm" framing.
3. **Report confidence intervals or multiple seeds** for the Stage 2 fine-tuning results to establish whether the small PPL improvements are statistically meaningful.
4. **Provide a parameter distribution table** showing how the 150M budget is allocated across components for each model configuration.
5. **Tone down the "general training paradigm" language** in favor of "system" or "framework" unless additional architectures are tested.

## Score and Decision

**Calibration Anchors** (all from the deepreview_13k_calibration set):

| Path | Avg Score | Comparison to This Paper |
|------|-----------|-------------------------|
| KZJehvRKGD.md (Depthwise Hyperparameter Transfer) | 7.50 | Stronger: solid theory + experiments with clear framing. TNT has stronger speedup results but weaker framing and no theoretical grounding. |
| xwKt6bUkXj.md (Emergent Mechanisms for Long Timescales) | 6.75 | Comparable empirical quality but better-scoped claims. TNT has more impactful results but more claim-evaluation gaps. |
| pCEgna6Qco.md (Two-stage LLM Fine-tuning) | 6.75 | Similar two-stage framing with cleaner evaluation. TNT has more novel technical components but weaker claim substantiation. |
| TvGPP8i18S.md (MELODI Memory Compression) | 6.25 | Comparable: both propose hierarchical memory for long contexts. TNT has stronger speedup results and ablations. |
| GQGNLEHmdl.md (AutoChunk) | 6.33 | Similar practical contribution with memory efficiency. TNT has more architectural novelty. |
| 1SO93f7sVf.md (Parallel Low-Rank Adapters) | 4.25 | Weaker: TNT has more thorough experiments, cleaner ablations, and more impactful results. |
| mSSi0zYkEA.md (Layer-wise Learning Rate) | 3.75 | Much weaker: TNT has clearer motivation, stronger experiments, and more novel contributions. |

Relative to these anchors, TNT is a solid paper with genuine technical contributions and impressive speedup results. Its main weakness is a gap between the claimed scope ("general training paradigm," "evaluated on Titans and TTT") and what is actually demonstrated (a single-architecture system with architectural changes bundled into the training procedure). This is significant but not fatal. The paper belongs in the upper-middle band of the reviewed papers.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**