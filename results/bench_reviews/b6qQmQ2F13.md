## Summary

This paper studies memory–accuracy trade-offs for reasoning LLMs, where the KV cache dominates GPU memory due to long generations. Through over 1,700 configurations across Qwen3 (0.6B–32B), DeepSeek-R1-Distill, and OpenReasoning-Nemotron on four benchmarks (AIME25, GPQA-Diamond, LiveCodeBench, MATH500), the authors identify scale-dependent strategies: models with effective size below ≈8-bit 4B benefit from allocating memory to larger/higher-precision weights, while larger models benefit from longer token budgets and parallel scaling. The paper also reports task-dependent optimal weight precision (4-bit for knowledge tasks, 8-/16-bit for math/code) and a comparative analysis of KV cache eviction vs. quantization.

## Strengths

1. **Novel and practically important problem framing.** Shifting the unit of analysis from FLOPs to memory for reasoning models captures a real deployment constraint that prior work on test-time scaling and quantization has largely ignored. This reframing alone is a valuable contribution.

2. **Unusually thorough empirical design.** Over 1,700 configurations across three model families, four benchmarks, multiple quantization schemes (GPTQ, AWQ, FP8), and two KV compression families (eviction with R-KV/StreamingLLM, quantization with HQQ). The systematic Pareto-frontier mapping provides credible qualitative guidance. The paper also validates key results on multiple model families to test generalizability.

3. **Scale-dependent memory-allocation threshold.** The core finding — that the memory-optimal strategy reverses at different model scales — is clearly demonstrated in the Pareto-frontier analysis (Figures 1–2) and replicated across model families. The concrete examples (e.g., 1.7B 8-bit with 6k tokens outperforming 0.6B 8-bit with 18k tokens) make the abstract trade-off tangible.

4. **Task-dependent optimal weight precision.** The finding that 4-bit weights are memory-optimal for knowledge-intensive tasks (GPQA-Diamond) but suboptimal for math/code is non-obvious and practically valuable. The explicit comparison showing the 8B 8-bit model outperforming the 14B 4-bit model on AIME25 is striking.

5. **Honest treatment of limitations.** Section 7 candidly discusses the scope constraints (limited verifier comparison, single quantization family for KV compression, primary focus on Qwen3), which strengthens confidence in the results that are presented.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Capability ceiling confounds the threshold interpretation.** The central finding — that small models benefit more from weight allocation than longer generations — may partly reflect that small models saturate in accuracy with additional tokens because they lack the capacity to exploit long reasoning chains, rather than a pure memory-allocation effect. The paper acknowledges saturation (Section 4) but does not control for this confound. This does not invalidate the practical guidelines (the paper's value is pragmatic), but it limits confidence in the claimed generality of the threshold as a "law" of memory-optimal reasoning. The paper could strengthen this by including a within-model analysis that varies token budget for a fixed small model and comparing to a larger model at comparable memory.

2. **No statistical uncertainty reported.** Accuracy is averaged over 32 generations (Section 3), but no error bars, standard deviations, or significance tests are shown. Given that the Pareto frontiers involve comparing closely spaced configurations (e.g., 14B 4-bit vs. 8B 8-bit), it is impossible to assess whether differences are meaningful or noise. This is especially relevant for claims about 4-bit being suboptimal on math reasoning, where differences between 4-bit and 8-bit at comparable budgets appear small in some regions.

3. **The specific threshold value (8-bit 4B, ≈4.2 GB) is empirically contingent.** The threshold is derived from the Qwen3 family's available model sizes (0.6B, 1.7B, 4B, 8B, 14B, 32B). The paper acknowledges this and tests on other families, but the crisp number is a useful reference point rather than a universal constant. The qualitative pattern (scale-dependent reversal) is well-supported; the specific number should be interpreted with caution.

### Trivial
- The massive KV cache memory for 30k tokens × 16 samples on the 32B model (117 GB, Table 1) far exceeds a single GPU — the paper treats this regime theoretically, which is fine for Pareto analysis but could mislead practitioners about feasibility. The paper implicitly acknowledges this via the 80 GB VRAM constraint in latency experiments (Appendix C.1).

## Nice-to-Haves
- A within-model analysis separating capability ceilings from memory-allocation effects (e.g., for a fixed small model, show accuracy vs. token budget and weight precision, then compare to larger models at comparable total memory).
- Per-configuration Pareto-frontier labeling in key figures (e.g., Figure 5, Figure 8) showing which specific (model, precision, token budget) points dominate.
- Extension to mixture-of-experts models or other architecturally distinct reasoning models to test robustness of the threshold.

## Removed Points
- The criticism that the threshold "redefinition is post-hoc" (Harsh Critic's point 2, second paragraph): The paper identifies the transition at ~10 GB total memory (Figure 2a) and translates this to the effective size of an 8-bit 4B model as a convenient reference point. This is standard practice for communicating empirical findings and is not post-hoc in any damaging sense. The qualitative pattern is robust across model families.
- The criticism about missing comparison to KIVI, GEAR, SnapKV for KV compression: The paper cites these methods in related work and scopes its evaluation to a representative set. Requesting every possible baseline is scope creep; the paper's comparison is sufficient to support its claims.
- The claim that the PRM analysis (Section 4.1) is "anecdotally correct but not a general result": The paper tests a specific, large verifier (ActPRM-X, 7B, 13.28 GB) and explicitly acknowledges this limitation in Section 7. The finding is appropriately presented as a case study, not a universal law.
- The formatting/style nitpicks about figure labeling and readability: These are parser artifacts.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own contributions — is the interplay between two distinct "saturation" mechanisms that both produce the observed threshold. The paper shows that small models hit an accuracy ceiling with longer generations, while large models benefit from additional tokens. The reviews raise the possibility that this is driven by fundamentally different causes for small vs. large models (parameter capacity limit vs. genuine memory-allocation trade-off). Disentangling these would be a valuable direction for future work but does not diminish the paper's current contribution, which is pragmatic and empirically grounded.

## Suggestions
1. Add error bars or confidence bands to key Pareto-frontier figures (Figures 1, 3, 4) for at least a subset of configurations, to assess whether the frontier comparisons are statistically meaningful.
2. Include a controlled experiment that separates capability ceiling from memory allocation: e.g., for a fixed small model (1.7B), vary both weight precision and token budget, and plot the accuracy landscape to show where saturation occurs regardless of memory.
3. Soften the crisp threshold language slightly (e.g., "models with effective size comparable to or smaller than an 8-bit 4B model") to avoid giving the impression of a universal constant, while keeping the practical guidance intact.
4. Annotate the Pareto frontiers in Figures 5 and 8 with a few representative labeled points (e.g., "8B 8-bit, 22k tokens") to improve readability and allow direct verification of claims by readers.

---

## Score and Decision

**Calibration Anchors** (all from ICLR 2026 human-reviewed corpus listed by path):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/2za3iNkwXn.md` | 4.40 | Similar topic (compression + reasoning benchmarking). Our paper is more thorough (1700+ configs vs. limited scope) and has more novel findings. **Our paper is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/udgrpHqw4F.md` | 4.50 | Similar topic (KV cache compression on reasoning). Our paper is far more comprehensive and systematic. **Our paper is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/Vem6FQvRvq.md` | 4.67 | New KV cache quantization method. Our paper is a broader empirical study with comparable thoroughness. **Roughly comparable.** |
| `/home/wg25r/review_agent/human_reviews_2026/qK43vBvOZ7.md` | 5.00 | Empirical study about pruning + test-time scaling. Similar type of contribution; our paper is more comprehensive and less controversial (that paper had split 2/4/6/8 scores). **Our paper is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/aNVKROYpLB.md` | 5.50 | New KV cache compression method with strong results. Our paper is a different type (empirical study vs. new method) but comparable in quality and thoroughness. **Comparable.** |
| `/home/wg25r/review_agent/human_reviews_2026/HD7tuVakmR.md` | 6.40 | Strong method paper with novel PTQ framework for diffusion LLMs. Our paper does not propose a new method, so it is a different contribution type. **Our paper is less novel algorithmically but equally thorough empirically.** |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` | 8.00 | Top-tier oral paper with large-scale experiments and novel findings. Our paper does not match this level of impact. **Our paper is weaker.** |

The paper makes a genuine, well-executed empirical contribution with findings that are practically actionable and grounded in an unusually large number of configurations. The weaknesses identified (capability ceiling confound, lack of error bars, contingent threshold value) are minor concerns that do not threaten the core claims. None of the criticisms rise to the level of "Major" or "Fatal." The paper is stronger than the 4.4–5.0 average papers on related topics and comparable to the 5.5-level contributions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>