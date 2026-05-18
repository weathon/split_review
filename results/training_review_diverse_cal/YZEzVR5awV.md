Now I have a clear picture of the paper content and can verify claims directly. Let me construct the final consolidated review.

---

## Summary

ClusComp introduces a simple compression paradigm for LLMs that replaces weight quantization with K-means clustering: weight matrices are reshaped into low-dimensional vectors, clustered into codebooks, and reconstructed via code indices stored in 16-bit integers. A code-fixed block-wise error minimization step (training only the codebook while keeping assignment codes frozen) reduces compression error using only 128 calibration samples. Because all values remain in FP16, compressed models support standard gradient-based training, enabling efficient recovery finetuning (ClusComp⁺) for ultra-low-bit compression and parameter-efficient downstream finetuning via codebook updates alone. Experiments on Llama-1/2/3 (7B–70B) show strong perplexity and zero-shot performance at 2–4 bits, 1-bit results via recovery training, and extension to multimodal LLaVA-Next.

## Strengths

- **Competitive compression results across LLM families and bit-widths.** In Table 2, ClusComp achieves the lowest perplexity in 9/12 cases at 4-bit and consistently outperforms RTN, GPTQ, AWQ, OmniQuant, QuIP, and GPTVQ at <4-bit, maintaining perplexity <13 on WikiText2 at 2-bit. The zero-shot accuracy curves (Figure 4) show a flatter degradation slope, demonstrating robustness to lower bit-widths. These results are well-documented across Llama-1/2/3 (7B–70B).

- **Well-motivated design grounded in an observation about outlier trends.** The pilot study (§3.1) shows rising weight kurtosis from Llama-1 to Llama-3, correlating with increasing quantization difficulty. Clustering avoids the outlier problem by keeping all values in FP16. This motivation is clean and directly supports the core design choice.

- **Code-fixed block-wise tuning prevents overfitting and mode collapse.** By fixing assignment codes during block-wise distillation (§3.2.3), ClusComp achieves effective compression with only 128 calibration samples. The uniform code distribution (Figure 3) confirms balanced centroid utilization. This is a principled solution to a real problem in vector-quantized compression.

- **Zero-shot multimodal results at ultra-low bits.** Table 3 shows ClusComp compressing the Llama-3-8B backbone of LLaVA-Next-8B to 2-bit without collapse, while GPTQ and AWQ fail to produce correct outputs. This demonstrates generality beyond pure language modeling.

## Weaknesses

### Fatal
None.

### Major

- **No controlled re-evaluation of baselines; numbers are borrowed from original works.** The paper states (line 143) that "all baseline results are directly borrowed from the original works or their follow-up works" without re-evaluation. While this is common practice in the compression literature, the perplexity differences in Table 2 are often small (0.1–0.5 ppl at 4-bit), and different evaluation pipelines (calibration data, sequence length, evaluation harness version) can produce systematic shifts of this magnitude. The paper would benefit from running a subset of baselines under identical conditions to confirm the margin of superiority, especially for the <4-bit results where differences are larger and more meaningful.

- **No wall-clock runtime or throughput measurements for the clustering step.** K-means on weight matrices of 70B models with codebook sizes up to 2¹⁶ centroids is computationally non-trivial. The paper reports only memory usage (2GB for ClusComp⁻, line 91) and notes the process can be accelerated with more GPUs, but gives no runtime numbers. For a method positioned as "simple" and "efficient," the practical overhead matters. Without runtime data, a practitioner cannot assess whether the compression-quality trade-off is worth the computational cost.

### Minor

- **The code-fixed design trade-off is not discussed.** The paper correctly motivates why fixing codes prevents mode collapse and enables data-efficient training (§3.2.3). However, an acknowledged limitation is that freezing assignments prevents the model from reorganizing which weight vectors share a centroid during finetuning. While the paper claims updating codebooks modifies "all parameters" (§2.3), the effective degrees of freedom are bounded by the number of centroids. This is a genuine trade-off (which may be a strength or weakness depending on the task) and should be discussed explicitly rather than framed one-sidedly as an advantage.

- **Recovery finetuning results in the parsed text lack experimental context.** In the abstract, the paper reports specific accuracy numbers for 1-bit/2-bit recovery (e.g., "51.4 vs 75.4 for the 1-bit Llama-3-70B"). The parsed Section 4.2 (lines 158–162) is only three sentences and does not specify the evaluation task, number of training steps, training data, or which ClusComp variant was used. The paper references Appendix §B for details, but even in the main text the context for these headline numbers is insufficient for a reader to interpret them.

- **Kurtosis analysis is correlational, not causal.** The pilot study (§3.1) shows rising kurtosis across Llama versions and notes it correlates with quantization difficulty. This is reasonable motivation, but the paper does not establish a causal link. The framing as a "pilot study" is slightly overstated given the evidence.

### Trivial
None.

## Nice-to-Haves

- A runtime comparison (GPU-hours or wall-clock time) for the full ClusComp pipeline vs. baseline methods (GPTQ, AWQ, OmniQuant) would strengthen the practical claims.
- An ablation study systematically varying group size `g` and number of clusters `n` (beyond what is shown in Table 1) to map the performance-compression Pareto frontier would be informative.
- The paper would benefit from acknowledging that vector quantization is a form of quantization (retaining codebooks in FP16 is a design choice, not a categorical distinction) and clearly stating the novel combination as: VQ + block-wise code-fixed tuning + codebook-only finetuning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Section 4.3 (finetuning experiments) is missing and the finetuning claims are unsupported.** The parsed text jumps from Section 4.2 to Section 5 (Conclusion), and Section 4.3 is absent. However, the paper extensively references §4.3 in the abstract and introduction with specific claims. This is a parser truncation issue — the section exists in the original submission. The finetuning methodology is described in §3.2.4. Removed per rule: parser-stripped content should not be held against the authors.

- **Criticism that the 1-bit/recovery results are "isolated numbers without context."** The parsed Section 4.2 is truncated (3 sentences). The original contains additional details deferred to Appendix §B. Removed per rule: weaknesses about missing appendix content.

- **Criticism about clustering not being "real compression" / the bits-per-parameter framing.** The paper explicitly defines its bit calculation (Equation 3) and states "no quantization is applied" (line 103). This is a deliberate design choice, not a weakness. Removed as factually understood by the paper.

- **Criticism about comparing across different bit-width calculations between methods.** The bit-per-parameter formula is clearly defined and standard. Removed as not a substantive weakness.

- **"The paper would benefit from acknowledging VQ is quantization."** This is a generic stylistic suggestion that doesn't affect the paper's claims or contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Re-run the most important baselines (GPTQ, AWQ, OmniQuant at 2–4 bit) under the same evaluation harness (same lm-eval version, sequence length, calibration data) for at least one model size (e.g., Llama-2-7B and Llama-3-8B) to confirm the reported margins, particularly for the sub-4-bit regime.
2. Report wall-clock time for the K-means clustering pass across model sizes (7B, 13B, 70B) and codebook configurations, so practitioners can assess the practical overhead.
3. Add a brief discussion of the code-fixed design's trade-offs — namely that while it prevents mode collapse and enables balanced training, it also prevents the model from reassigning weight vectors to different centroids, potentially limiting adaptation flexibility in finetuning.
4. Provide minimal experimental context for the recovery finetuning results directly in Section 4.2 (task, training steps, data source) rather than exclusively in the appendix.

## Score and Decision

The paper proposes a clean, well-motivated compression framework with strong empirical results across multiple LLM families and bit-widths. The core ideas — clustering to avoid outlier degradation, code-fixed block-wise tuning, and codebook-only finetuning — are principled and have genuine practical appeal. The compression results in Table 2 and Figure 4 are the main body of evidence, and they are convincingly presented. The two substantive concerns (borrowed baselines without re-evaluation, and missing runtime data) are common limitations in this field and do not undermine the core contribution. The missing finetuning experimental section (parser artifact) is not the authors' fault. The paper makes a solid contribution worthy of acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>