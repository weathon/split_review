## Summary

This paper proposes FFN Token Pruning (FTP), a training-free method that accelerates the prefilling stage of LLM inference by pruning non-critical tokens before the Feed-Forward Network (FFN) in each layer. Token importance is determined by summing attention scores (from the last N queries across heads), and tokens below a cumulative threshold η are skipped — their FFN output is set to zero, so the residual connection leaves them unchanged. The first ℱ layers are fully preserved. Experiments on LongBench with Llama3-8B, Qwen2-7B, Qwen1.5-32B, and Qwen2-72B show TTFT speedups of 1.2–1.45× with generally small accuracy drops.

## Strengths

1. **Clear identification of FFN as the prefilling bottleneck.** Figure 3 shows that FFN accounts for >60% of per-layer walltime during prefilling (62.4% for Llama3-8B, 61.3% for Qwen2-7B). This directly motivates why targeting FFN (rather than attention) for token pruning is sensible — prior work on prefilling acceleration focused on attention, which flash attention has already made relatively efficient.

2. **Attention-based pruning is convincingly shown to be critical.** Table 3 compares FTP against a random-pruning variant that matches the same per-layer pruning count. Random pruning causes catastrophic accuracy collapse (e.g., Multi-Document QA on Llama3-8B drops from 34.85 to 7.56), while FTP preserves near-baseline performance. This is a clean and strong ablation.

3. **1.2–1.45× TTFT speedup with small accuracy drops on most configurations.** On Qwen2-7B-Instruct, FTP achieves 1.22–1.30× speedup with ≤2.25-point drops across six tasks. On Qwen1.5-32B and Qwen2-72B, speedups reach 1.31–1.45×, and certain tasks (e.g., Few-shot Learning on 32B) show slight accuracy increases.

4. **Training-free with reported overhead.** The method requires no fine-tuning. Section 4.6.1 reports that the extra attention-score computation adds 7–10ms (1–3% of TTFT) on Llama3-8B and 8–15ms (0.8–1.9%) on Qwen2-7B.

5. **Outperforms a comparable prefilling-acceleration baseline.** FTP consistently achieves higher accuracy and speedup than PyramidInfer (both its official PyTorch implementation and a flash-attention re-implementation). PyramidInfer* (official) suffers sub-1.0× speedup on Llama3-8B and OOM on Qwen2-32k.

6. **Scales to larger models with increased benefit.** Evaluation on Qwen1.5-32B and Qwen2-72B (Table 2) shows that deeper architectures with more total layers enable higher overall pruning rates and speedups.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained accuracy collapse on Llama3-8B Code Completion.** In Table 1, FTP drops the Code Completion score from 55.17 to 35.91 on Llama3-8B-Instruct — a 35% relative drop (19.26 points). This is not a minor degradation. The paper offers no discussion, hypothesis, or analysis of why this specific model/task combination fails so badly. Notably, the same task on Qwen2-7B (58.43→56.74), Qwen1.5-32B (46.97→46.63), and Qwen2-72B (69.05→68.35) shows much smaller drops. This suggests model-family or task-specific sensitivity that the authors should confront directly. The abstract's general claim of "negligible decrease in performance" is misleading when applied to this cell.

2. **Missing comparison to LazyLLM, a directly relevant prefilling-pruning method.** LazyLLM (Fu et al., 2024) is cited in Section 2.1 as a method that "drops tokens from the prefilling stage" — this is a direct competitor to FTP. Yet the experimental comparison includes only LLMLingua2 (prompt compression) and PyramidInfer (KV-cache compression). The omission weakens the empirical case: readers cannot assess whether FTP's design choices (pruning *before* FFN, using same-layer attention scores) are actually superior to an existing method that also prunes during prefilling.

### Minor

3. **Hyperparameter analysis is limited for P and N.** The paper sets P=100 (preserved initial tokens) and N=50 (queries used for attention scoring) based on prior work, but provides no ablation showing sensitivity to these choices in the context of FTP. Figure 7 does explore the accuracy-speedup trade-off by varying η and ℱ (the reserve ratio and number of preserved layers), which partially addresses hyperparameter robustness, but P and N are not examined. Given that these interact with the attention-score estimation, some characterization would strengthen the empirical claims.

4. **Overhead characterization would benefit from sequence-length scaling.** The paper reports overhead as a global percentage (1–3% of TTFT) for each model. It does not show how this cost scales with sequence length, which is important for deployment at the upper end of supported context windows (e.g., 32k). If the overhead grows quadratically (since it requires materializing attention weights), it could erode the speedup on very long sequences.

### Trivial
None.

## Nice-to-Haves

- Diagnosing the Llama3-8B Code Completion failure: e.g., comparing per-layer pruning ratios on that task, or checking whether code-specific patterns (indentation, brackets) cause uniform attention that undermines the selection strategy.
- A controlled comparison to LazyLLM on even a single task would clarify whether FFN-specific pruning is more effective than general prefilling pruning.
- Adding confidence intervals or standard deviations for the accuracy and speedup results (the LongBench datasets have fixed test sets, but variance across runs would be informative).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a paragraph discussing the Llama3-8B Code Completion failure — hypothesize why it occurs and whether it suggests a limitation of attention-based importance scoring for certain tasks or model families.
2. Include LazyLLM as a baseline in the experimental comparison, or justify its omission with specific evidence (e.g., on identical hardware, same settings).
3. Show overhead breakdown as a function of sequence length (e.g., 2k, 8k, 16k, 32k) to confirm sub-linear or constant scaling.
4. Add a brief hyperparameter sensitivity table for P and N in the main text or supplement.

## Removed Points

- **"Catastrophic accuracy degradation... is unreported and unexplained"** — KEPT in Major as explained above (it is a real issue); the "fatal" designation was downgraded to Major because the method still demonstrably improves upon random pruning (35.91 vs 16.28 on the same task), and the failure is specific to one model/task combination rather than invalidating the entire approach.
- **"Equation 2 appears garbled"** — Removed. This is a PDF-parser artifact; the original submission likely renders it correctly.
- **"No evidence that N=50 approximation works uniformly across tasks"** — Removed. The paper cites prior work (SnapKV, Li et al., 2024) that empirically justifies this design choice.
- **"Pure formatting/style nitpicks"** and **"Missing appendix"** — Removed per instructions (parser strips appendices from all submissions).
- **Strength Finder strength about "addressing an important problem"** — Removed as generic/superficial. The remaining strengths are concrete and evidence-backed.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/gcEhF4nuYI.md` | 3.00 | 1 | Weaker — rejected paper on token pruning; FTP has much stronger empirical validation |
| `/home/wg25r/review_agent/human_reviews/4QWPCTLq20.md` | 3.00 | 1 | Weaker — KV cache compression; narrow scope compared to FTP |
| `/home/wg25r/review_agent/human_reviews/n7iwmPacDt.md` | 3.00 | 1 | Weaker — speculative decoding theory; not comparable methodology |
| `/home/wg25r/review_agent/human_reviews/vw0NurJ7UX.md` | 3.00 | 1 | Weaker — quantization paper; different sub-area |
| `/home/wg25r/review_agent/human_reviews/9iN8p1Xwtg.md` (GemFilter) | 5.25 | 1, 2 | Comparable — both are training-free token pruning for prefilling. FTP has cleaner motivation (FFN bottleneck profiling), more models (up to 72B), and a stronger random-pruning ablation. GemFilter has higher claimed speedup (2.4×) but was rejected due to robustness concerns and missing baselines. FTP is slightly stronger overall. |
| `/home/wg25r/review_agent/human_reviews/G1fzW97QKR.md` | 4.75 | 1 | Weaker — intra-layer attention similarity; withdrawn paper with mixed reviews |
| `/home/wg25r/review_agent/human_reviews/QlvL6eEOC6.md` | 4.50 | 1 | Weaker — auxiliary model for KV prediction; introduces training cost unlike FTP |
| `/home/wg25r/review_agent/human_reviews/Hjk1tWIdvL.md` (HASA) | 5.00 | 2 | Weaker — requires fine-tuning a specialized branch; reported speedup is modest; FTP is training-free and cleaner |
| `/home/wg25r/review_agent/human_reviews/SYv9b4juom.md` (OrthoRank) | 5.25 | 2 | Comparable — token selection via sink tokens. Both show good results but have evaluation gaps. FTP has more comprehensive model scaling (32B, 72B). |
| `/home/wg25r/review_agent/human_reviews/ZTpWOwMrzQ.md` (Radar) | 6.60 | 1, 2 | Stronger — theoretical justification for token selection, accepted as poster. FTP lacks theoretical analysis and has an unexplained failure case. |
| `/home/wg25r/review_agent/human_reviews/yUC8pU508S.md` (APE) | 6.40 | 2 | Stronger — accepted poster, addresses a different problem (context-augmented generation) with thorough evaluation |
| `/home/wg25r/review_agent/human_reviews/vHO9mU87dc.md` (ShadowKV) | 6.75 | 2 | Stronger — system-level KV cache optimization with high throughput; different focus |

**Round-1 bracket:** Between 3.5 and 7.5 (clearly above weak 3.0 papers, clearly below 8.0 oral/spotlight papers).

**Round-2 narrowing:** FTP is stronger than the 5.0–5.25 rejected papers (GemFilter, HASA, OrthoRank) due to cleaner motivation, more comprehensive model scaling, and a strong random-pruning ablation. It is weaker than the 6.4–6.75 papers (Radar, APE, ShadowKV) which either provide theoretical guarantees, have more thorough experimental methodology, or have no unexplained failure cases. The unexplained Code Completion collapse on Llama3-8B and the missing LazyLLM baseline are substantive gaps that prevent this paper from reaching the 6+ level.

**Final score: 5.5** — A solid, well-motivated method with clean ablations and reasonable results on most model/task combinations, held back by an unaddressed failure case and an incomplete baseline comparison.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>