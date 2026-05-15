Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

## Summary

This paper proposes ClusComp, a model compression paradigm that replaces quantization with weight clustering. Weight matrices are decomposed into codes (indices into a codebook) stored as 16-bit integers and FP16 centroids, keeping all values in high precision while achieving compression. The method adds block-wise reconstruction error minimization and can be extended with codebook-only finetuning for recovery or downstream adaptation. Compression results at 2–4 bits are strong across Llama models and a multimodal model, consistently outperforming quantization-based baselines.

## Strengths

- **Novel and well-motivated compression direction**: The paper identifies growing outlier frequency in Llama-3 weight matrices (via kurtosis analysis, Figure 2) as a fundamental challenge for uniform quantization, and proposes clustering as an alternative that avoids quantizing outliers. This motivation is concrete, data-driven, and timely given the trend toward larger models with more extreme weight distributions.

- **Consistent and substantial improvement across 2–4 bit compression**: In language modeling (Table 2), ClusComp achieves the lowest perplexity in 9 of 12 cases at 4-bit and dominates all baselines at lower bit-widths. At 2-bit the gaps are very large (e.g., Llama-2-7B WikiText2: 8.74 PPL vs 29.43 for GPTQ). Zero-shot accuracy results (Figure 4) show the same pattern. These results are the paper's strongest evidence.

- **Transparent and clean formulation**: The method is straightforward — K-means clustering, 16-bit integer codes, FP16 codebooks — and the bpp formula (Equation 3) analytically separates code bits from codebook overhead. The adapted linear layer is simple (Listing C.1). The code-fixed design during block-wise training is justified with clear overfitting and mode-collapse arguments.

- **Broad applicability demonstrated**: Results span Llama-1/2/3 (7B–70B) and LLaVA-Next-8B (Table 3), where ClusComp retains meaningful performance at 2-bit while GPTQ/AWQ produce degenerate outputs. This suggests robustness beyond pure language models.

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental evidence for two of the three claimed contributions.** The abstract and introduction claim ClusComp "(2) pushes the compression limit to the 1‑bit level" and "(3) facilitates seamless and efficient finetuning...rival[ing] full finetuning." However, Section 4.2 (1‑bit results) contains only two introductory sentences with no data, tables, or figures, and Section 4.3 (finetuning experiments) is entirely absent from the extracted text. The numbers cited in the introduction (e.g., 51.4 accuracy for 1-bit Llama-3-70B) are unverifiable. The paper's core contribution (compression at 2–4 bits) is supported, but the scope of claimed contributions goes beyond what can be evaluated.

- **Effective bit-budget not precisely reported for comparisons.** ClusComp's stated bit-width reflects primarily the code bits, but the codebook adds overhead (Equation 3: ~0.25 bpp for a large layer at g=4). Table 2 and Figure 4 label configurations as "4-bit," "3-bit," "2-bit" without reporting the exact effective bits-per-parameter for each model/layer configuration. While the bpp formula is provided, the reader cannot verify whether ClusComp's advantage persists when total bit budgets are equalized. This is a presentation gap that can be fixed, but it tempers the headline quantitative claims.

- **No ablation of the code-fixed design.** The paper justifies fixing codes during block-wise training with overfitting and mode-collapse arguments (Section 3.2.3), which are reasonable. But no experiment compares training both codes+codebooks vs. codebooks-only on reconstruction error or final perplexity. This leaves the design choice empirically unvalidated.

### Minor

- **Expressiveness of codebook finetuning is somewhat overstated.** The paper claims that updating the codebook is "analogous to adapting the entire high‑rank weight matrix" (Section 3.2.4). While updating a centroid does affect all weight vectors assigned to it, the number of free parameters per layer is only n×g (e.g., ~262K for a 16M-parameter layer), which is much smaller than full weight finetuning. The update is more expressive than LoRA in principle (no low-rank bottleneck), but the claim of "full‑rank" adaptation is misleading. The missing finetuning experiments (Weakness #1) make it impossible to assess whether this expressiveness translates to practical gains over LoRA/QLoRA.

- **Clustering runtime not reported.** K-means on every linear layer of a 70B model is non-trivial, but no runtime or peak memory figures are given. This matters for practical deployment assessment.

- **Kurtosis–quantization difficulty link is asserted rather than causally demonstrated.** The pilot study shows correlation between kurtosis and quantization difficulty, but does not test whether methods robust to outliers degrade less. The connection to the choice of clustering is plausible but not directly validated.

### Trivial
- Figure/table references to appendices (Table C.1, C.2, C.3, C.4) point to content stripped by the parser, which is not the authors' fault but makes some details unreachable in the extracted version.

## Nice-to-Haves
- Reporting exact effective bpp per configuration in the main comparison tables and, ideally, constructing an equal-budget comparison by adjusting codebook size.
- An ablation on training both codes vs. codebooks-only for the block-wise minimization step.
- Reporting clustering wall time and peak GPU memory for the largest model (70B).

## Removed Points

- **Memory-efficiency criticism about activation memory (Harsh Critic, Section-by-Section §3.2.4).** The paper's memory-efficiency claims are specifically about model loading and optimizer states, not activation memory. The critic's "conflation" accusation misreads the paper; removed as factually incorrect.
- **Criticism about missing Section 2.2 content.** Section 2.2 appears as a heading without content — this is a parser artifact. Removed per hard rules.
- **"Missing related works" consideration.** Per instructions, I do not comment on missing related works.
- **Strength #2 and #3 from Strength Finder** (1-bit claim, finetuning claim). These conflict with the verified weakness that the corresponding experimental sections are absent. Dropped as unsupported in the extracted text.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review is that the paper exposes a fundamental tension in the field: quantization-based compression is hitting diminishing returns on modern LLMs due to growing weight outliers, but replacing quantization with clustering introduces a new axis of overhead (codebook storage) that the field lacks standard methodology for accounting fairly. The fact that ClusComp still dominates at 2-bit even with this overhead suggests that the bottleneck is genuinely the rigid quantization grid, not the total bit budget per se. This is an insight worth further investigation.

## Suggestions

1. Report exact effective bpp for every ClusComp configuration in the main tables and add a controlled experiment where ClusComp is restricted to the same total bpp as the baselines (e.g., by reducing n or increasing g).
2. Provide the missing 1-bit and finetuning experimental results — these are essential to support the paper's full set of claims.
3. Add an ablation comparing codebook-only vs. joint code+codebook training during block-wise minimization, validating the overfitting/mode-collapse claims.
4. Report clustering runtime/memory for the 70B model.
5. Tone down the "entire high-rank weight matrix" phrasing for codebook finetuning — or provide evidence (e.g., effective rank analysis) to substantiate it.

## Score and Decision

The paper presents a novel, clean, and well-motivated compression method with strong empirical support for its primary contribution (2–4 bit compression). The missing experimental sections for the 1-bit and finetuning claims are a significant gap in the extracted text, and the bit-budget reporting is imprecise. However, the core method is sound, the main results are impressive and unlikely to be fully explained by the bit-budget discrepancy, and the identified weaknesses are addressable. This is a solid paper with a clear contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>