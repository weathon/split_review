- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have everything I need. Let me compile the final review.

## Summary
COAT proposes a memory-efficient FP8 training framework that compresses both optimizer states (via Dynamic Range Expansion using a power-law transformation) and activations (via mixed-granularity quantization) into FP8 format. It achieves 1.54× memory reduction and 1.43× end-to-end speedup over BF16 training across LLM pretraining, fine-tuning, and VLM training, while maintaining nearly lossless accuracy.

## Strengths
- **Dynamic Range Expansion (Sec. 4.2, Eq. 4, Table 1):** The paper identifies a genuine, non-obvious problem: FP8's representation range is severely underutilized when quantizing optimizer states (especially second-order momentum, whose dynamic range is typically <1e1 vs. FP8's ~2×10⁵). The proposed power-law expansion \(f(x)=\operatorname{sign}(x)|x|^k\) with group-wise computed \(k\) is simple, principled, and demonstrably effective — reducing the MSE of the effective update term \(m/\sqrt{v}\) by 1.63× (from 20.10 to 12.31 in the E4M3 setting, Table 1). This is the paper's clearest novel contribution.

- **Mixed-Granularity Activation Quantization with memory decomposition (Sec. 5, Table 1):** The paper decomposes activation memory by operator type and reveals that non-linear layers (RMSNorm, activation functions) account for ~50% of the activation footprint in Llama models — a factor previous FP8 frameworks (TE, FP8-LM) leave in higher precision. COAT's per-group (1×16) quantization for non-linear layers achieves a measured 1.65× activation memory reduction per layer (Table 1), closely matching the theoretical 1.69×. The motivation (Figure 3a) showing that per-token-axis quantization incurs higher error than per-group quantization at the same granularity grounds this design choice experimentally.

- **Strong end-to-end efficiency results across realistic distributed settings (Table 5):** COAT enables full-parameter training of Llama-2-7B on a single H100 GPU (where BF16 and TransformerEngine both OOM), reduces peak memory by 1.54× for Llama-2-13B on 4 GPUs (35.6 GB vs. 55.1 GB BF16), and achieves 1.45× speedup (11,257 vs. 7,730 tok/s per GPU). These numbers directly support the paper's core efficiency claims and demonstrate practical value.

- **Broad validation scope:** The paper evaluates across LLM pretraining (OLMo-1B/7B), LLM fine-tuning (math corpus), and VLM training (VILA1.5-7B) — three distinct regimes — with consistent near-lossless performance (perplexities and accuracies within <0.5% of BF16 baseline on average).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by evidence.

### Minor
- **No statistical uncertainty reported.** All accuracy/perplexity results are point estimates from single runs without standard deviations, confidence intervals, or multiple seeds. The OLMo-1B loss difference between COAT (3.008) and BF16 (2.995) is 0.013, which is small but could represent a systematic shift. While single-run evaluation is common in large-scale training papers, the "nearly lossless" claim would be strengthened by reporting variability, even for just one setting (e.g., OLMo-1B with 3 seeds).

- **Computational overhead of Dynamic Range Expansion unquantified.** The expand function requires per-group per-step computation of \(k = \log_{R_X}(R_{\text{E4M3}})\) and per-element exponentiation \(|x|^k\) during quantization, followed by the inverse operation \(x^{1/k}\) during dequantization. The paper claims this is efficient but provides no profiling data (e.g., fraction of optimizer step time, cost relative to the optimizer update itself). This is a minor gap since the end-to-end speedups are reported, but the overhead of the expansion itself versus the rest of the FP8 flow is not isolated.

- **OLMo-7B continue-pretraining is short (4B tokens).** The paper acknowledges this is due to resource constraints. The training curve aligns well with the baseline, but 4B tokens is insufficient to assess convergence stability or whether systematic drift would emerge over longer training. The OLMo-1B experiment (22B tokens) partially mitigates this concern.

- **DE8 compatibility shown only at quantization error level (Table 7).** The ablation demonstrates that Dynamic Range Expansion reduces quantization error for DE8 by 1.41×, but no end-to-end training results are provided for this combination. The claim of "broad applicability" would be stronger with at least one training run.

- **Missing experimental comparison with prior FP8 training works.** The paper compares against BF16 and TransformerEngine, but does not include FP8-LM (Peng et al., 2023) or Fishman et al. (2024) as end-to-end baselines. While the quantization error analysis in Table 1 partially addresses this (showing E4M3 vs. E4M3+Expand, E5M2 vs. E5M2+Expand), direct training comparisons would more cleanly isolate the value of Dynamic Range Expansion over prior approaches that also quantize optimizer states (e.g., FP8-LM's first-order momentum quantization, Fishman et al.'s E5M2 second-order momentum).

### Trivial
None.

## Nice-to-Haves
- **Separate speedup decomposition:** The end-to-end speedup numbers (Table 5) conflate FP8 computation speedup with the benefit of larger feasible batch sizes. Reporting COAT's speedup at the *same* micro-batch size as BF16/TE, alongside the additional gain from batch size doubling, would provide a more transparent breakdown. This is not a flaw — the practical benefit is real either way — but it would sharpen the analysis.
- **Ablation on \(k\) update frequency:** The paper computes \(k\) per-group per-step. An ablation exploring whether a fixed or less-frequently updated \(k\) suffices would be informative and potentially reduce overhead.

## Removed Points
- **"Overstated and poorly contextualized quantization error reduction":** REMOVED. The paper states "Our Dynamic Range Expansion can effectively reduce the MSE by 1.63×," comparing worst-case (no expansion, 20.10) to best-case (expansion on both, 12.31). All 16 entries are shown in Table 1, so there is no hiding of less favorable comparisons. The 1.63× is the total system improvement, which is a standard and transparent way to report the headline benefit. Not cherry-picked.
- **"Activation quantization contribution is incremental":** This is a subjective opinion, not a concrete weakness. The paper provides specific, evidence-backed claims about activation memory decomposition and the quantization strategy, which the strength finder correctly identifies as well-supported.
- **"Section 5 title should be a method note, not a contribution":** Purely a formatting/presentation nitpick. REMOVED per style nitpick rule.
- **"The speedup numbers conflate batch size increases":** MOVED to Nice-to-Haves. The end-to-end speedup numbers reflect genuine practical benefits. Requesting a same-batch-size breakdown is a refinement suggestion, not a weakness of the presented results.

## Novel Insights
None beyond the paper's own contributions. The key insight — that FP8's representation range is underutilized for optimizer states and that a simple power-law expansion can align the dynamic range — is the paper's own contribution and is well-articulated.

## Suggestions
1. Add at least one experiment with 3 seeds (e.g., OLMo-1B) and report mean ± std for downstream metrics to quantify variability and support the "nearly lossless" claim.
2. Profile the Dynamic Range Expansion overhead: report the fraction of optimizer step time consumed by the \(k\) computation and per-element exponentiation/dequantization.
3. Include FP8-LM as a direct baseline in at least one setting (e.g., quantization error comparison, or a small-scale training run) to isolate the benefit of Dynamic Range Expansion over prior FP8 optimizer quantization.
4. Add a same-batch-size speedup comparison alongside the maximum-batch-size comparison to separate FP8 compute gains from batch-size-driven gains.

**Originality:** 7/10 — Dynamic Range Expansion is genuinely novel; activation quantization is well-engineered but less novel.
**Importance of research question:** 8/10 — Memory-efficient training for large models is a timely and practically important problem.
**Claims well-supported:** 7/10 — Core efficiency claims are well-supported; accuracy claims would benefit from uncertainty quantification and more comprehensive baselines.
**Soundness of experiments:** 7/10 — Broad scope, clean methodology, but single-seed reporting and missing FP8-LM comparison weaken completeness.
**Clarity of writing:** 8/10 — Clear motivation, well-structured, good visual aids.
**Value to community:** 8/10 — Practical framework with real efficiency gains; the Dynamic Range Expansion idea may transfer to other low-precision settings.
