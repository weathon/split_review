Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper presents SpQR (Sparse-Quantized Representation), a hybrid compression format for LLM weight quantization that identifies and isolates outlier weights causing disproportionate quantization error, stores them in 16-bit precision, and compresses remaining weights to 3-4 bits using grouped quantization with very small groups (enabled by bilevel quantization of the statistics themselves). The method achieves near-lossless compression (<1% perplexity increase) at ~4.6 bits per parameter for LLaMA and Falcon models up to 65B, and outperforms GPTQ and RTN baselines at matched bit-widths. A custom GPU inference kernel yields 20-30% speedup over fp16 inference and fits 33B+ models on a single 24GB consumer GPU.

## Strengths

- **Near-lossless compression demonstrated across model scales.** SpQR achieves relative perplexity increases under 1% for both LLaMA 7B–65B and Falcon 7B–40B at ~4.4–4.7 bits per parameter (Tables 1–2, excluding the Falcon 3.92-bit anomaly). This is the first weight-only quantization method to reach this accuracy at these bit-widths, directly fulfilling the paper's central claim.

- **Clear improvements over GPTQ and RTN at matched bit-widths.** At ~4 bits, SpQR halves the perplexity gap to the 16-bit baseline compared with GPTQ (e.g., LLaMA-7B Wiki2: SpQR 5.87 vs. GPTQ 6.13 vs. RTN 6.43; LLaMA-65B Wiki2: SpQR 3.68 vs. GPTQ 3.83 vs. RTN 3.87). The margin is as large as the gain from GPTQ over RTN, establishing a new state of the art.

- **Novel structural analysis of weight quantization sensitivity.** Section 3 provides a fine-grained sensitivity analysis revealing previously undocumented outlier patterns in LLM weights: row outliers, attention-head stripes, rotary-embedding periodicity, and unstructured individual outliers. This analysis motivates the two-pronged design (small quantized groups + unstructured sparse outliers) and goes beyond prior work focused only on activation/column outliers.

- **Bilevel quantization of group statistics is empirically validated as effective.** Ablations (Table 3) show that quantizing scales/zero-points to 3 bits within groups of 16 yields better perplexity than storing them in 16-bit precision at the same average bit-width (e.g., 3.74 vs. 3.84 Wiki2 PPL for LLaMA-65B). This directly addresses the concern that small groups are impractical due to metadata overhead.

- **Controlled ablations isolate the contribution of each component.** Section 5 compares unstructured vs. row vs. column outlier strategies (Figure 5) and examines the impact of quantized zero-points and activation order. The evidence clearly shows that both unstructured outliers and small quantized groups are independently necessary for the reported gains.

## Weaknesses

### Fatal
None.

### Major

- **The Falcon-7B 3.92-bit PTB perplexity of 19.114 is clearly erroneous and must be corrected.** The uncompressed Falcon-7B baseline is 9.90; GPTQ 4-bit is 10.33; even the poor RTN 4-bit is 13.76. A value of 19.114 far exceeds all baselines (including the worst one) and is completely inconsistent with the near-lossless claim, especially since the same row's Wiki2 and C4 values (6.74, 9.70) are reasonable. This is either a data-entry error (e.g., transposed digits) or a corrupted evaluation run. The presence of such an error undermines trust in the Falcon experiments and contravenes the caption's claim that "SpQR reaches performances within 1% of the perplexity" for the Falcon table. The authors must explain or correct this data point.

- **Inference speed experiments lack a comparison against competitive quantized methods at the same bit-rate.** Table 4 compares SpQR against fp16 inference and against its own PyTorch (cuSPARSE) baseline. The relevant deployment question for a practitioner is whether SpQR's sparse outlier handling overhead is worthwhile compared to a simpler quantized method (e.g., GPTQ 4-bit with an efficient kernel). Showing that SpQR is 20–30% faster than fp16 is expected given 4× fewer weights to load; this does not isolate the cost of the sparse format. Without a quantized baseline, the reader cannot assess whether the accuracy benefit of SpQR comes at a speed penalty relative to simpler quantization.

### Minor

- **Zero-shot accuracy results are only shown in a figure (Figure 1, right panel), with no tabulated numeric values.** The text references these results qualitatively but provides no precise numbers for reproducibility or fine-grained comparison. A table would allow readers to verify that perplexity gains translate to task-level improvements.

- **The outlier detection algorithm (Alg. 1, `outliers()` subroutine) is under-specified.** The subroutine appears to select outlier columns (not individual weights) within a group by comparing leave-one-out error differences to τ, but the connection to the per-weight outlier storage (CSR format) is not clearly explained. The paper also does not discuss how the global threshold τ is calibrated across layers with potentially very different sensitivity profiles, nor report the resulting outlier counts per layer.

- **The sensitivity analysis focuses primarily on one layer (the output projection of the last self-attention layer of LLaMA-65B).** While the caption notes that the rightmost subfigures are "taken from other weight matrices," the paper does not quantify how representative the shown patterns are across layers (e.g., what fraction of layers exhibit each pattern). This limits the generality of the motivation for the design choices.

- **The paper acknowledges but does not address the lack of generative quality evaluation.** The limitation section (Section 6) states this honestly, but for a method claiming "near-lossless" compression, a side-by-side generation comparison (even qualitative examples or a small-scale human eval) would substantially strengthen the claim.

### Trivial
None.

## Nice-to-Haves

- A head-to-head inference speed comparison against GPTQ 4-bit (or RTN 4-bit) with an efficient kernel at the same bit-width and hardware would isolate the cost/benefit of SpQR's sparse outlier handling and make the speed results more actionable for practitioners.
- Reporting the number of outliers per layer and the range of τ values used across models would improve reproducibility and provide insight into how outlier density varies across architectures.
- A brief intuitive explanation of *why* quantized zero-points and the removal of the "max positive, min negative" constraint help (beyond the ablation numbers) would improve readability of Section 4.

## Removed Points

- **"Sensitivity analysis only on LLaMA-65B one layer" overstated severity:** The reviewer claimed the analysis was performed "only on LLaMA-65B and only on one attention layer." The paper's caption explicitly notes that the rightmost subfigures show patterns from "other weight matrices," and the text discusses patterns across attention Q/K/V projections and MLP weights. The criticism is valid in that systematic quantification is missing, but the severity was slightly overstated. Kept as minor rather than major.

- **"Outlier detection unclear (column vs weight)" — kept as minor but not major:** The reviewer framed this as a significant clarity gap. The paper's text explains that outliers are per-weight decisions based on the sensitivity criterion, and the algorithm operates group-by-group. The mapping is adequate for a research paper audience; the reviewer's confusion is understandable but the algorithm is functional. Downgraded from the reviewer's implied severity.

- **"Global τ threshold may not work across layers" — moved from implied major:** This is a reasonable methodological question but is standard practice in quantization (one threshold, tuned to achieve a target sparsity/outlier ratio). The paper states τ is chosen "to obtain the desired number of outliers across the whole model." This is a minor design choice note, not a structural flaw.

- **"Falcon PTB anomaly is a typo — fixable triviality":** The reviewer briefly entertains this might be a typo but treats it as undermining the entire Falcon evaluation. I agree with the reviewer — this is correctly identified as a major issue, not a triviality. Kept as major.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation: the Falcon 19.114 anomaly is not just a local error — it directly contradicts the paper's claim of "within 1%" for the Falcon table, meaning anyone citing those Falcon results as supporting the near-lossless claim would be relying on a data point that is almost certainly wrong. This underscores the importance of systematic error-checking in quantitative ML submissions where dozens of numbers are reported across multiple models and datasets. The reviews also correctly identify that SpQR's main strength (accuracy at near-lossless levels) and its main experimental gap (missing quantized speed baseline) are orthogonal concerns — the paper is stronger on accuracy evidence than on practical deployment evidence.

## Suggestions

1. **Fix the Falcon 7B 19.114 data point immediately.** Re-run the experiment or correct the typo. If the typo is confirmed, provide a corrected table.
2. **Add a table of zero-shot accuracy numbers** for the same model/method configurations as the perplexity tables, to allow direct quantitative comparison.
3. **Add an inference speed comparison against GPTQ 4-bit** (or RTN 4-bit) at the same bit-width on the same hardware, to contextualize whether SpQR's accuracy benefit carries a speed cost. Even a brief paragraph or supplementary table would significantly strengthen the deployment argument.

## Score and Decision

The paper presents a novel, well-motivated, and carefully ablated method that advances the state of the art in LLM weight quantization. The core technical contributions — sensitivity-aware outlier isolation combined with bilevel quantization of group statistics — are sound and clearly demonstrated across multiple model scales. The near-lossless claim is well-supported for the LLaMA family, and the ablations effectively isolate the contribution of each design component.

However, two issues prevent unconditional acceptance: (1) the Falcon 7B PTB value of 19.114 is clearly erroneous and must be corrected before the results can be trusted; (2) the inference speed evaluation lacks a comparison against competitive quantized methods, leaving a gap in the deployment evidence. Both are addressable — the first is a correction, the second is an addition that strengthens an already good paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>