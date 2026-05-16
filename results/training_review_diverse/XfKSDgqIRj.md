Now I have a thorough understanding of the paper and can verify all reviewer claims directly. Let me write the final consolidated review.

## Summary

COAT proposes a memory-efficient FP8 training framework that quantizes both optimizer states (via Dynamic Range Expansion, DRE) and activations (via Mixed-Granularity Activation Quantization, MGAQ) to FP8 precision. The paper demonstrates 1.54× memory reduction and 1.43× end-to-end speedup vs. BF16 across LLM pretraining (OLMo-1B from scratch, OLMo-7B continued), finetuning (Llama-2-7B on math), and VLM training (VILA1.5-7B SFT), while maintaining nearly lossless accuracy.

## Strengths

1. **Significant and practically meaningful memory reduction (1.54× end-to-end) with consistent speedups (1.43× on average) across multiple model sizes (7B, 13B, 30B) and GPU counts.** The end-to-end results in Table 7 are the paper's strongest empirical contribution. COAT enables full-parameter training on fewer GPUs (e.g., Llama-2-7B on a single GPU where BF16 and TE OOM) and doubles batch size in distributed settings.

2. **Dynamic Range Expansion is well-motivated and independently verified through offline MSE analysis.** Table 5 (paper's Table 1) shows that DRE reduces quantization MSE on the effective weight-update term \(m/\sqrt{v}\) from 20.10 (E4M3 only) to 12.31 (E4M3+Expand), a 1.63× improvement. The observation that FP8's representation range is under-utilized for optimizer states (dynamic range < 1e4 for first-order, < 1e1 for second-order vs. E4M3's capacity of ~2×10^5) is clearly explained and visualized in Figure 2. The method is also shown to be compatible with and improve the DE8 format (Table 6), demonstrating generality.

3. **Mixed-Granularity Activation Quantization achieves near-optimal activation memory reduction (1.65× vs. theoretical 1.69×).** Table 2 decomposes activation memory across Llama-style layers, showing COAT reduces total activation memory from 22.66U (BF16) to 13.33U. The per-group (1×G) quantization for non-linear layers with per-tensor quantization for linear layers is a sensible design choice, and the Group Scaling method provides an efficient alternative to delayed scaling.

4. **Nearly lossless accuracy across diverse tasks and benchmarks.** COAT stays within ~0.1 perplexity or ~1% accuracy of BF16 on OLMo-1B pretraining (Wikitext, C4, Pile, COPA, ARC, SciQ, HellaSwag), math finetuning (MATH, SVAMP, NumGLUE, GSM8K), and VLM training (VideoMME, GQA, VQAv2, SEED, etc.). These results are consistent across the entire evaluation suite, not cherry-picked.

5. **Enables training configurations that are otherwise impossible.** COAT is the only method that can train Llama-2-7B on 1 GPU, Llama-2-13B on 2 GPUs, and Llama-30B on 8 GPUs — all configurations where both BF16 and TE OOM. This is a clear practical contribution for resource-constrained settings.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core empirical claims are supported by the data.

### Minor

1. **No training-level ablation isolates either claimed component (DRE or MGAQ).** The paper always combines both innovations. The only component-level evidence is (a) an offline MSE table for \(m/\sqrt{v}\) (Table 5) and (b) a forward-pass quantization-error plot (Fig. 5a). Neither guarantees that the error reduction translates to preserved training accuracy when used independently. A simple ablation — e.g., quantizing second-order momentum to E5M2 without DRE while keeping activations quantized, or keeping nonlinear-layer activations in BF16 while using COAT elsewhere — even on a short run (OLMo-1B for the same 22B tokens) would make the contribution of each component transparent. Without this, a reader cannot tell whether the simpler baselines would also succeed, which weakens the paper's methodological claims.

2. **Speed comparison at maximum batch size conflates memory savings with arithmetic speedup.** In Table 7, all speed comparisons use the maximum batch size each method supports. For example, COAT's 2.25× speedup on Llama-2-13B 4-GPU uses batch size 2 vs. BF16's batch size 1 and TE's batch size 1. The speedup is partly from doubling the batch (better hardware utilization), not purely from FP8 arithmetic. While this is the practically relevant comparison (larger batches are a real benefit), the paper should separate the two effects or at least acknowledge this conflation.

3. **OLMo-7B evidence is incomplete.** The 7B experiment is only a 1000-step continued pretraining (≈4B tokens) from an official checkpoint, with only a training loss curve and no perplexity or downstream accuracy numbers. The paper claims "nearly lossless" performance at this scale, but a few thousand steps on a small fraction of the model's total training cannot rule out accuracy drift over longer horizons. The 1B pretraining (22B tokens from scratch) is convincing for that scale, but the 7B claim is under-supported.

4. **Speed discrepancy with TransformerEngine on Llama-2-7B 8-GPU is not discussed.** The abstract and conclusion claim COAT "performs on par with or surpassing TransformerEngine's speedup." However, in the 7B 8-GPU setting, COAT achieves 1.36× vs. BF16 while TE achieves 1.42× — making COAT *slower* than TE. The paper does not comment on this discrepancy or analyze the overhead causing it (likely the additional quantization for non-linear layers). The claim is still roughly true (1.36× is close to 1.42×, and COAT beats TE in most other configurations), but the lack of discussion makes the presentation feel incomplete.

5. **The per-step computational cost of DRE's on-the-fly \(k\) computation is not discussed.** The optimal \(k\) is computed as \(\log_{\mathcal{R}_X}(\mathcal{R}_{\text{E4M3}})\), which varies from 1–15 across groups and steps and requires logarithm and power operations per group per step. The speedup numbers suggest this overhead is small, but the paper would benefit from acknowledging this cost.

### Trivial

- The MSE table (Table 5) appears to be computed from a single snapshot of optimizer states; variance across training steps is not reported.
- The group size choices (1×128 for optimizer states, 1×16 for activations) are given without justification or sensitivity analysis.
- The table caption structure in Table 7 ("Context Length = 2048" and "Maximum Batch Size, Context Length = 2048" columns) is somewhat hard to parse at first glance.

## Nice-to-Haves

- **Comparison with Jetfire (Xi et al., 2024):** Jetfire proposes INT8 data flow for activation quantization of both linear and non-linear layers and is cited in the related work. While Jetfire operates in a different precision ecosystem (INT8 vs. FP8), a brief discussion of how the approaches differ in terms of hardware requirements, memory reduction, and numerical accuracy would help position the contribution. Not a required comparison, but would strengthen the contextualization.

- **Limitations section:** The paper would benefit from a brief discussion of where COAT might struggle — e.g., very long context (where activation memory dominates), sensitivity to group size choices, potential runtime overhead from expand/inverse operations.

- **Statistical significance:** Accuracy numbers in Tables 3–5 are close or overlapping. Multiple-seed variance estimates would strengthen the "nearly lossless" claim, though single-run evaluation is the norm in this systems-oriented literature.

- **Comparison of Group Scaling vs. delayed scaling on an actual training run:** The claim that Group Scaling "is no worse, and could be even better" than delayed scaling is supported only by an error/timing plot (Fig. 5b), not by a convergence comparison.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about Jetfire comparison being a "methodological gap":** Jetfire uses INT8, which is a different precision ecosystem from FP8. Comparing across precisions would require a different hardware setup or software stack. The paper's baselines (BF16, TransformerEngine) are the standard FP8 comparisons. Removed as scope creep.

- **Criticism about nested column headers being hard to parse:** Pure formatting/style nitpick. Removed per formatting-nitpick rule.

- **Criticism about missing limitations section and missing hyperparameter sensitivity:** These are nice-to-haves, not weaknesses. Downgraded.

- **Criticism about statistical significance / lack of seed variance:** Single-run evaluation is standard in large-scale training papers of this type. Downgraded to nice-to-have.

## Novel Insights

None beyond the paper's own contributions. The key technical observations — that FP8's representation range is under-utilized for optimizer states (especially second-order momentum) and that non-linear layers dominate activation memory — are clearly made by the paper itself. The reviews do not surface any deeper insight not already in the paper.

## Suggestions

1. **Add a single training ablation** — even a short run on OLMo-1B toggling DRE on/off (e.g., quantize second-order momentum to E5M2 without expansion) and MGAQ on/off (e.g., keep nonlinear-layer activations in BF16). This would dramatically increase confidence in the claimed innovations.
2. **Discuss the 7B 8-GPU speed discrepancy** with TE explicitly, even if only to note that COAT's overhead for nonlinear quantization causes slightly slower throughput in that specific configuration.
3. **Report perplexity/downstream numbers for the OLMo-7B continued pretraining**, or explicitly caveat the "nearly lossless" claim for the 7B scale as preliminary.
4. **Separate the batch-size effect from the arithmetic speedup** — e.g., include a comparison at the same batch size alongside the max-batch-size comparison.

## Score and Decision

This is a solid systems paper with clear practical contributions. The weaknesses are real but fixable and do not invalidate the core results. The paper demonstrates meaningful memory reduction and speedup with near-lossless accuracy across a diverse evaluation suite. The missing training-level ablations and incomplete 7B reporting are the most notable gaps, but they are addressable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>