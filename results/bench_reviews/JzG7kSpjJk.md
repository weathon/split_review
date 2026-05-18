Now I have all the data I need. Let me write the consolidated review.

## Summary

This paper proposes per-input-channel (per-IC) quantization for weight-only LLM quantization, which groups weights along the input-channel direction rather than the conventional output-channel direction to isolate the effect of activation outliers. Building on this, the authors introduce AdaDim, a lightweight framework that adaptively selects per-IC or per-OC grouping per layer by minimizing reconstruction error on a calibration set. AdaDim is shown to improve Round-To-Nearest (RTN) and GPTQ consistently across MMLU, commonsense reasoning, GSM8k, and HumanEval for LLaMA-V2 base and instruction-tuned models at 3-bit and 4-bit precision.

## Strengths

- **Novel and well-motivated quantization grouping direction.** The per-IC scheme is a clean, intuitive idea directly motivated by the geometry of activation outliers. The paper shows convincingly (Figure 1) that per-OC grouping spreads the outlier effect across all groups, while per-IC isolates it to a single group. This is a genuinely new design axis in weight-only quantization, distinct from prior work that exclusively uses per-OC grouping.

- **AdaDim's adaptive per-layer selection outperforms heuristic fixed schemes.** Table 2 shows that the optimization-based (reconstruction error minimization) choice of per-IC vs. per-OC yields higher MMLU scores than heuristic-based fixed assignment (e.g., 44.38 vs. 44.23 for 13B). This validates that a one-size-fits-all grouping strategy is suboptimal and that the adaptive framework captures layer-specific sensitivity patterns.

- **Consistent accuracy gains across model scales, tasks, and precisions.** AdaDim improves RTN and GPTQ across 7B–70B models on MMLU, CSR, GSM8k, and HumanEval. The improvements are amplified by using task-specific calibration sets (up to +10.3% on HumanEval for WizardCoder-Python, Table 4). Figure 4 shows strict perplexity improvements across INT3/INT4 with various group sizes, demonstrating generality beyond a single setting.

- **Analysis of weight sensitivity patterns motivates the adaptive approach (Figure 2).** The correlation of activation outliers with sensitive weights, combined with the observation that the dominant sensitivity dimension (row vs. column) can switch across layers, provides principled motivation for adaptive grouping rather than a fixed scheme.

- **Demonstration that per-IC localizes GPTQ weight updates (Figure 6).** The qualitative visualization that per-IC concentrates weight updates to a few input channels (while per-OC spreads them pervasively) offers mechanistic insight into why per-IC benefits GPTQ.

## Weaknesses

### Fatal
None.

### Major
- **Insufficiently documented AWQ baseline.** The paper claims that AdaDim+RTN "surpasses AWQ" by up to 4.7% on MMLU (Figure 3, Section 4.2) and refers to this as a headline result, but provides no specific details on how AWQ was configured — no group size, calibration set size, or hyperparameter choices are reported beyond citing the original paper and stating "following the settings." The paper also shows AWQ results in Table 4 without specifying precision/configuration. While AWQ is a known method with public code, the absence of even basic configuration details (precision setting, group size, calibration data size) means a reader cannot verify whether the AWQ comparison is operating under comparable conditions. This is the single most significant weakness because it undermines the strongest comparative claim. *The core contribution does not depend on beating AWQ — the improvements over RTN and GPTQ are already meaningful — but the paper elevates this comparison as a headline result.*

- **Kernel speedup comparison confounds quantization with grouping direction.** Section 4.5 and Figure 7 compare the per-IC LUT-GEMM kernel against cuBLAS FP16 matmul. This measures the well-known speedup of quantized vs. full-precision computation, not the speedup attributable to per-IC vs. per-OC grouping. A controlled comparison would require an equivalently optimized per-OC quantized kernel. The paper acknowledges the kernel is "not fully optimized" but still claims the comparison indicates "measurable speedups in inference latency" from per-IC quantization. The kernel section is preliminary and does not support the claim that per-IC specifically leads to latency advantages.

### Minor
- **Precision specification is inconsistent across experiments.** The preliminary study (Table 1) uses INT4 w128, base model results (Figure 3) use INT3 w128, and instruction-tuned experiments (Tables 3, 4) do not explicitly state the bit width — the text says "we use the same settings as the base model" which refers to INT3, but this is ambiguous and requires cross-referencing. The paper would benefit from stating precision explicitly in each table caption for clarity.

- **Reconstruction error analysis (Figure 5) partially validates the optimization objective rather than downstream improvement.** Showing that AdaDim reduces reconstruction error (up to 6×) confirms the optimization is working as designed, which is useful but expected. The downstream accuracy improvements (Figures 3, 4; Tables 3, 4) are the proper validation. The paper could strengthen this by analyzing whether dim choices from reconstruction error correlate with better MMLU at the layer level.

- **GPTQ update analysis (Figure 6) is qualitative.** The claim that per-IC "minimally perturbs the weight distribution" is supported only by visual inspection of weight update patterns. Quantitative statistics (e.g., L2 norm of updates, variance across channels) would strengthen this analysis.

- **GPTQ ablation (Table 2) is limited in scope.** The paper states it "thoroughly ablate[s] GPTQ's most up-to-date design parameters" but only tests reorder vs. static groups. Other parameters known to affect GPTQ quality (dampening factor, block size, calibration set size) are not explored. This is a relatively minor concern since the main contribution (AdaDim) is orthogonal to these choices.

### Trivial
- The claim "activation outliers do not dictate quantization difficulty" (abstract) could be more precisely stated — the paper's own analysis shows outliers *do* create sensitive rows, but they do not *solely* determine difficulty because inherent weight sensitivity also matters.
- The paper does not specify which calibration set size was used, only that it used a "small" calibration set from The Pile.

## Nice-to-Haves

- A layer-wise visualization showing which layers are assigned per-IC vs. per-OC, overlaid with activation outlier presence (e.g., indicator of outlier channels), would ground the adaptive decisions in the motivational analysis of Figure 2.
- Testing AdaDim with more recent quantization methods (e.g., QuIP, SpQR, QuaRot) beyond RTN and GPTQ would demonstrate generality.
- Analyzing whether the per-IC vs. per-OC decision per layer remains stable across different calibration sets would address potential overfitting concerns.

## Removed Points

- *AWQ citation/release status concerns*: The Harsh Critic claimed AWQ results "cannot be verified" due to insufficient citation detail. Since the paper cites Lin et al. 2023 (a published, peer-reviewed paper), AWQ exists as a method. The concern about *configuration* details is kept as a Major weakness; the concern about whether AWQ even exists or can be reproduced at all is removed as a reviewer knowledge gap.
- *"Activation outliers do not dictate quantization difficulty claim contradicts paper's own analysis"*: This criticism misreads the paper. The paper explicitly states "activation outliers cause sensitive rows but does not necessarily dictate the overall sensitivity" (line 69-71), which is consistent with the claim in the abstract. Removed as factually wrong.
- *"Figure 5 reconstruction error is tautological"*: Removed as a strawman — showing that the optimization objective is met is standard practice. The paper separately validates downstream improvements.
- *"Missing related work"*: Removed per policy — I cannot verify the existence of missing references.
- *"Figure 2 and Figure 9 missing from text"*: These are figure references the parser stripped; they exist in the original submission. Removed.
- *Formatting/style nitpicks about tables/figures*: Removed per policy.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves do not already articulate. The insight that per-IC grouping can be a cheap "plug-in" to existing quantizers (RTN, GPTQ) is the paper's own framing.

## Suggestions

1. **Document the AWQ baseline configuration in full.** Specify the precision, group size, calibration dataset size, and any other hyperparameters used. This is essential for the headline comparison to be credible. Consider running AWQ with its official implementation under identical conditions.

2. **Reframe the kernel comparison.** Either (a) add a comparison against an equivalently optimized per-OC quantized kernel to isolate the effect of grouping direction, or (b) clearly state that the cuBLAS comparison demonstrates quantization speedup (not per-IC-specific speedup) and position this as preliminary evidence that the per-IC approach does not preclude efficient inference.

3. **State precision explicitly in all table captions** (especially Tables 3 and 4) to avoid ambiguity.

4. **Add quantitative metrics to the GPTQ update analysis** (Figure 6), such as L2 norm or variance of updates under per-IC vs. per-OC, to substantiate the "localized updates" claim with numbers.

5. **Consider adding a correlation analysis** between the per-IC/per-OC decision from reconstruction error (Eq. 1) and downstream task accuracy at the layer level to confirm that minimizing reconstruction error is a good proxy.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| `wg1PCg3CUP.md` — Scaling Laws for Precision | 8.0 | Much stronger paper — fundamental theoretical contribution with extensive validation. Our paper is an applied method paper and does not match this level. |
| `E4Fk3YuG56.md` — Cut Your Losses | 8.5 | Much stronger — clear practical impact, well-engineered solution to a well-defined problem. Our paper has a less direct practical impact. |
| `ISqx8giekS.md` — LeanQuant | 5.17 | Comparable — both are quantization method papers with similar evaluation scope. Our paper has a more novel core idea (per-IC grouping) but similar presentation issues. Slightly stronger. |
| `ZBlfjXubgG.md` — Pyramid VQ for LLMs | 5.0 | Weaker paper — less clear contribution and suffered from novelty/writing concerns. Our paper is stronger in both contribution clarity and experimental validation. |
| `0Ag8FQ5Rr3.md` — The Super Weight in LLMs | 4.6 | Similar topic (outliers in LLMs). Our paper has a more novel technical contribution and stronger experiments. Clearly stronger. |
| `6Mdvq0bPyG.md` — EfficientQAT | 3.0 | Much weaker — limited novelty, unfair comparisons, strongly rejected. Our paper is substantially stronger. |
| `0T8vCKa7yu.md` — LLM Compression with Convex Optimization | 3.0 | Much weaker. Our paper is substantially stronger. |

**Positioning:** Our paper sits between the 5.0–6.0 quantization method papers. It has a genuinely novel and well-motivated idea, solid experiments across multiple scales and tasks, and addresses an important problem. However, the poorly documented AWQ comparison and misleading kernel evaluation prevent it from reaching the top of the quantization method tier.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>