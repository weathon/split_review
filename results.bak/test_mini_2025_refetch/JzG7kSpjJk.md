Now I have all the information I need. Let me compose the final review.

## Summary

This paper proposes per-input-channel (per-IC) weight quantization for LLMs, which groups weights along the input channel dimension rather than the conventional output channel dimension, to isolate the effect of activation outliers within a single quantization group. The authors further introduce AdaDim, an adaptive framework that selects per-IC or per-OC quantization per layer by minimizing reconstruction error with only two candidates to evaluate. Experiments show consistent improvements when AdaDim augments RTN and GPTQ across LLaMA base models (up to +4.7% MMLU on 7B), instruction-tuned models, and task-specific math/coding benchmarks (up to +10% on HumanEval).

## Strengths

- **Well-motivated and insightful core idea.** The observation that activation outliers affect specific input channels, and that per-IC grouping isolates these outliers within a single group (Figure 1), is clearly articulated and supported by a Fisher-information-based sensitivity analysis (Figure 2). The selective application study (Table 1) directly validates the intuition: applying per-IC only where outliers are present improves Wiki-2 perplexity from 9.22→9.09 and MMLU from 44.54→45.21 on LLaMA-V2-7B, while naive all-module per-IC hurts performance (44.38).

- **Consistent and often substantial empirical gains across diverse settings.** Figure 3 shows RTN-ada improving MMLU on LLaMA-V2-7B from ~37.5→~41.8 (4.7% absolute), and Table 4 demonstrates RTN-ada boosting HumanEval from 35.37→42.68 on WizardCoder-Python-7B. GPTQ-ada also shows gains, e.g., Vicuna-V1.3-33B MMLU from 55.68→57.08 (Table 3). The gains hold across INT3/INT4 and various group sizes (Figure 4), and across both general (MMLU, CSR) and task-specific (GSM8k, HumanEval) evaluations.

- **Mechanistic analysis strengthens the contribution.** Figure 6 shows that per-IC grouping concentrates GPTQ weight updates on a small subset of input channels rather than spreading them pervasively, providing a clear structural explanation for why per-IC reduces perturbation of the original weight distribution. Figure 5 links AdaDim's adaptive selection to up to 6× reduction in reconstruction error.

- **Practical kernel implementation with measurable speedups.** The per-IC LUT-GEMM kernel (Figure 7) achieves 1.44–4.34× speedup over cuBLAS across group sizes, demonstrating that the scheme is not only accurate but also practically viable (even if the cuBLAS comparison is not a quantized-GEMM baseline).

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency between GPTQ baselines across tables.** The "GPTQ w/o AdaDim" value for LLaMA-V2-13B in Figure 3 is ~50.5, but Table 2b reports the paper's chosen per-OC configuration ("reorder + static") as 51.32, and even the simplest per-OC GPTQ ("default, default") as 51.07. The ~0.8–1.0 point gap between the figure and the table is large enough to puzzle a careful reader: it is unclear whether Figure 3 uses the same configuration as Table 2b or a different one. The paper should (a) state the exact GPTQ configuration used for each main-table result, and (b) include the best-performing GPTQ variant (OC reorder without static, 52.18) alongside the hardware-efficient variant to contextualize the improvements. Without this, the headline improvements of GPTQ-ada over GPTQ may partly reflect a degraded baseline rather than the full benefit of the method.

2. **RTN-based dimension selection for GPTQ is not validated.** Section 3.3 states that the optimal dimension is searched with RTN, and GPTQ is then optionally applied in that dimension. But GPTQ's iterative Hessian-based updates can change the sensitivity landscape — a dimension that minimizes RTN reconstruction error may not be optimal after GPTQ's error compensation. The paper provides no ablation showing that the RTN-based selection remains optimal (or even beneficial) for GPTQ. This weakens the grounding of the adaptive mechanism specifically for GPTQ, although the method clearly works in practice as shown by overall results.

### Minor

1. **No variance or statistical significance reported.** All results are point estimates from single calibration-set draws. Some reported gains (e.g., ~0.2–0.5 MMLU points in several GPTQ-ada vs. GPTQ comparisons) could lie within run-to-run noise. Reporting means and standard deviations over multiple seeds would strengthen the reliability of the quantitative claims.

2. **Kernel comparison against cuBLAS, not against a quantized GEMM baseline.** The per-IC kernel speedups in Figure 7 are measured against cuBLAS (full-precision GEMM), not against the standard per-OC LUT-GEMM kernel that would be the practical alternative. The paper acknowledges this as preliminary, but a comparison against per-OC LUT-GEMM would be needed to substantiate the practical latency advantage claim.

### Trivial
None.

## Nice-to-Haves

- Validate that the RTN-based dimension choice transfers to GPTQ, e.g., by comparing GPTQ-ada with the RTN-chosen dimension vs. the opposite dimension for a few layers.
- Include variance estimates by running multiple calibration-set seeds.
- Compare the per-IC kernel against a per-OC LUT-GEMM kernel rather than cuBLAS.
- Report the best GPTQ variant (OC reorder without static) alongside the hardware-efficient baseline to clarify the headroom.

## Removed Points

- **"Comparison to QuIP is missing"** — Removed per instruction not to mention missing related works.
- **"AdaDim is incompatible with AWQ — appendix is absent"** — Removed because the appendix was stripped by the parser; the paper states incompatibility and cites the appendix.
- **"cuBLAS comparison has limited practical relevance"** — Retained as a Minor point but softened from the critic's stronger framing since the paper acknowledges this is preliminary.
- **"Ambiguous baseline: the reader cannot tell what configuration was used"** — The paper does specify the configuration ("static reordering for per-OC and reordering for per-IC"), so this specific claim is removed. However, the numerical inconsistency between Figure 3 and Table 2b is retained as Major weakness 1.
- **"Only LLaMA-family models tested"** — Retained as a limitation but not a core weakness since the paper's contribution is about the quantization dimension, not architecture generality. Moved to Nice-to-Have implicitly.
- **Various formatting/style nitpicks and speculation-based criticisms** — Removed.

## Novel Insights

The harsh critic identified a genuinely important inconsistency between the GPTQ baseline values reported in Figure 3 vs. Table 2b that the strength finder missed. Conversely, the strength finder correctly identified that the paper's real strength lies not just in the accuracy numbers but in the mechanistic analysis (Figures 2, 5, 6) which provides structural justification for why per-IC works. Beyond the paper's own contributions, a notable observation is that the core weakness (baseline ambiguity) is entirely fixable with better reporting, while the methodological gap (RTN-based selection for GPTQ) is empirically mitigated by the fact that GPTQ-ada consistently outperforms GPTQ in practice — the concern is about optimality, not about whether the method works.

## Suggestions

1. **Clarify the GPTQ baseline.** State explicitly which GPTQ configuration is used in each main experiment, and add a row for GPTQ with activation reordering (no static groups) alongside the hardware-efficient variant. This costs nothing and resolves the inconsistency.
2. **Add a small ablation validating the RTN→GPTQ dimension transfer.** For 2–3 layers of LLaMA-V2-7B, compare GPTQ applied in the RTN-chosen dimension vs. the opposite dimension. If the RTN choice is suboptimal, consider using GPTQ's own reconstruction error for selection.
3. **Report variance.** Even 3 seeds with mean ± std would substantially improve confidence in the results.
4. **Replace or complement the cuBLAS latency comparison** with a comparison against a per-OC LUT-GEMM kernel, which is the appropriate baseline for weight-only quantization.

## Score and Decision

**Bracketing pass (Round 1):** Retrieved 12 anchors across three bands. Weak anchors (scores <3.5): PrefixQuant (3.0), Scaling Laws Mixed Quant (3.0) — both rejected papers with limited novelty. Middle anchors (3.5–7.5): SpQR (6.5, accepted poster), Systematic Outliers (6.0, accepted poster), LRQ (5.25, rejected), FPTQ (4.0, rejected). Strong anchors (>7.5): CBQ (7.6, spotlight), Scaling Laws Precision (8.0, oral). **Initial bracket: 4.5–6.5.**

**Narrowing pass (Round 2):** Retrieved additional anchors in (4.5, 6.5) and (5.5, 7.5). OSTQuant (6.2, accepted poster), QERA (6.8, accepted poster), TesseraQ (5.0, rejected). Reading these in full: the paper under review is noticeably stronger than TesseraQ (5.0, rejected for incremental contribution and missing comparisons) and LRQ (5.25, rejected for marginal improvements). It is weaker than SpQR (6.5, accepted poster) which introduced a more fundamental sparse-quantized representation with near-lossless compression and a complete GPU kernel. The paper is comparable to OSTQuant (6.2) in overall quality — both have a clear, well-motivated idea and strong results, but OSTQuant has a more thorough theoretical framework. The present paper's main weakness relative to these anchors is the GPTQ baseline inconsistency and the missing validation of the RTN→GPTQ selection, which prevent it from reaching the 6+ level.

**Final score: 5.5** — a solid paper with a genuinely useful idea and strong empirical evidence, but with evaluation gaps (baseline transparency, missing ablation, no variance) that need to be addressed before it could be confidently accepted. The core contribution is valuable and the weaknesses are all fixable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>