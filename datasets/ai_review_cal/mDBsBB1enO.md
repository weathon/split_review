- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes LLM-QAT, a data-free quantization-aware training method for large language models. It generates training data from the pre-trained LLM itself via next-token generation with a hybrid sampling strategy, then uses logit distillation from the teacher (full-precision) to the quantized student. The method simultaneously quantizes weights, activations, and the KV cache down to 4 bits. Experiments on LLaMA-7B/13B/30B demonstrate large improvements over post-training quantization methods (RTN, SmoothQuant, GPTQ) in low-bit settings — e.g., LLaMA-30B at 4-8-4 achieves 69.9% average zero-shot accuracy vs. ~42% for PTQ methods, within 1.5 points of full-precision.

## Strengths

- **Data-free distillation is practical and effective**: The paper generates training data from the pre-trained model itself, eliminating dependence on the original (often inaccessible) training data. The ablation on data choice (Table 3/tab:ablation_data) shows that generated data with hybrid sampling (Generated data³) achieves 63.1% average zero-shot accuracy on LLaMA-7B, outperforming fine-tuning on C4 (61.5%), WikiText-103 (58.5%), or WikiText-2 (58.1%). This makes QAT feasible for any generative model regardless of data availability.

- **QAT dramatically outperforms PTQ at 4-bit precision**: The method enables 4-bit weights and KV cache with minimal accuracy loss where PTQ baselines collapse. The strongest evidence: LLaMA-30B at 4-8-4 (Table 1 rows 52–54) — LLM-QAT achieves 69.9% vs. 42.5% (RTN) and 40.7% (SmoothQuant), compared to 71.4% full-precision. Perplexity on WikiText-2 (Table 2 row 4) confirms the same pattern: LLM-QAT at 11.6 vs. >100 for PTQ methods.

- **Simultaneous KV cache quantization**: The paper extends QAT to the KV cache, which is a known throughput bottleneck for long-sequence generation. Results in Table 1 (e.g., 8-8-4 setting for LLaMA-30B, rows 67–69: LLM-QAT at 69.7% vs. SmoothQuant at 50.7%) show QAT preserves quality even with heavily quantized KV cache, where PTQ fails.

- **Systematic ablations provide actionable insights**: The paper ablates data choice, quantization function (symmetric MinMax vs. clipping-based methods like StatsQ/LSQ), and knowledge distillation variants (logit-only vs. adding attention/hidden supervision). These experiments validate design choices and give practitioners clear guidance: preserve outliers (don't clip), use logit-only distillation, and use hybrid sampling for data generation.

- **Compatibility with complementary techniques**: The method can be combined with SmoothQuant's activation-channel rescaling to improve the difficult W4A4 setting (Table 7: 39.5% for LLM-QAT alone → 49.2% with SmoothQuant on LLaMA-7B), demonstrating flexibility.

## Weaknesses

### Fatal
None.

### Major

- **The claim that generated data outperforms "subsets of the original training set" is overstated relative to the evidence**. The introduction (line 16) states the method "is better able to preserve the original model's output distribution, even compared to training on large subsets of the original training set," and Section 2 (line 32) repeats "superior performance compared to using subsets of the original pre-training data." However, the real-data baselines in the data-choice ablation (Table 3/tab:ablation_data) are WikiText-2, WikiText-103, and C4 — none of which is a representative, diverse sample of LLaMA's actual multi-source pre-training mixture (CommonCrawl, C4, Wikipedia, Books, etc.). C4 is one component of that mixture, but not a stratified sample. The experiment shows generated data beats these particular public corpora, which is practically useful, but the stronger linguistic claim about the "original training set" is not directly tested. This does not invalidate the core contribution (data-free QAT works well), but the narrative should be recalibrated to match what was actually compared.

### Minor

- **KV cache quantization is motivated as performance-critical but no throughput/memory measurements are provided**. The abstract and conclusion assert that KV cache quantization is "critical for increasing throughput" (line 4, 20), yet all evaluations are accuracy/perplexity only. The paper honestly acknowledges (line 375) that "4-bit quantization does not have hardware support out-of-the-box," but even analytical estimates (memory savings at various sequence lengths, simulated speedups) are absent. Including at least a back-of-envelope calculation or a reference to prior throughput benchmarks would ground this claimed benefit.

- **Missing training cost details**. The paper specifies learning rate (2e-5), optimizer (AdamW), batch size (1 per GPU), and maximum sequence length (1024), but does not report the number of training steps, total GPU-hours, or whether the same 100k generated sequences are reused across model sizes (the data is generated using LLaMA-7B — is the same data used for 13B and 30B?). These details help practitioners assess practical overhead.

- **No variance or statistical significance reported**. Zero-shot results are reported as single numbers without error bars or multi-seed runs. Given that QAT involves stochastic training and non-deterministic data generation, some measure of variance (even for a representative subset of settings) would strengthen close comparisons (e.g., rows 45–46 in Table 1 where RTN and SmoothQuant tie at 68.0). That said, single-run evaluation is standard for large-scale LLM experiments, so this is a minor concern.

### Trivial

- None that warrant mentioning — the paper is well-written with clear tables and figures. Minor formatting artifacts are parser-related, not author errors.

## Nice-to-Haves

- **Ablate the impact of data-generator size**: The data is generated using LLaMA-7B for all model sizes. Would using the same-size model as the student (e.g., LLaMA-30B to generate data for a 30B student) improve results? A quick ablation on LLaMA-13B comparing data from 7B vs. 13B generators would address this.
- **Explicit statement on GPTQ's scope**: GPTQ appears only in the 4-16-16 setting because it is a weight-only method. The paper already notes it compares to "the best PTQ result in each setting," but a sentence clarifying that GPTQ is excluded from settings with activation/KV quantization would prevent any impression of selective reporting.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"GPTQ should be included for the 4-8-16 setting"** (Harsh Critic, Missing Parts): The critic writes "including GPTQ for 4-8-16 would be a natural extension since activations are not quantized." This is factually incorrect — in 4-8-16, the "8" denotes 8-bit activation quantization. GPTQ does not handle activation quantization, so it is not applicable. Removed.

- **"No error bars" framed as a significant weakness**: The critic mentions this as a "missing part." While noted above as Minor, the critic's framing as a major evaluation gap would be disproportionate — single-run evaluation is standard practice at this scale. Removed from the main weakness set and downgraded to Minor.

## Novel Insights

None beyond the paper's own contributions. The two reviewers did not surface any unexpected interpretation or cross-cutting insight that the paper itself does not already articulate.

## Suggestions

1. **Tone down the claim about generated data vs. the original training set.** Replace phrases like "even compared to training on large subsets of the original training set" (Introduction) with "even compared to training on publicly available web-crawled corpora like C4." This aligns the narrative with what was actually tested and does not weaken the practical value of the method.
2. **Add a brief analytical estimate for KV cache memory savings.** Even a single paragraph computing the memory footprint of the KV cache at 16-bit vs. 4-bit for typical sequence lengths (e.g., 2048, 4096, 8192) would ground the claim that KV cache quantization is "critical for throughput."
3. **Report the number of training steps and approximate GPU-hours** for at least one configuration (e.g., LLaMA-7B W4A8) so practitioners can gauge computational cost.
4. **Explicitly state why GPTQ is excluded from activation-quantization settings** (Section 3) to avoid any appearance of cherry-picking.
