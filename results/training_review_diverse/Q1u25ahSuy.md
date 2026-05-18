Now I have all the evidence I need. Let me synthesize the final review.

## Summary

This paper introduces SpQR (Sparse-Quantized Representation), a hybrid compression format for LLMs that identifies and isolates outlier weights (stored in 16-bit) while compressing the remaining weights to 3–4 bits using small-group quantization with bilevel quantization of statistics. The method achieves substantially lower perplexity degradation than GPTQ and round-to-nearest at similar or lower average bitwidths across LLaMA (7B–65B) and Falcon (7B, 40B) model families, and provides a GPU inference kernel that is 20–30% faster than fp16 baselines.

## Strengths

1. **Novel structural insight into weight sensitivity patterns.** The paper provides a sensitivity analysis (Eq. 1) that goes beyond the previously known column/input-feature outliers to identify row outliers, sensitive attention heads, rotary embedding patterns, and unstructured outliers in weight matrices (Fig. 2, Section 3). This structural taxonomy motivates the hybrid sparse-quantized representation and is a genuine contribution to understanding quantization error in LLMs.

2. **Bilevel quantization of statistics enabling very small groups without overhead.** By quantizing groupwise scales/zero-points to 3-bit (Alg. 1, `fit_statistics`), SpQR uses groups of 8–16 weights — contrary to prior recommendations against small groups — while maintaining accuracy. The ablation (Table 3) shows that 3-bit statistics at 3.63 avg bits outperform 16-bit statistics in perplexity (e.g., Wiki2: 3.74 vs. 3.84), demonstrating that the metadata overhead concern is effectively addressed.

3. **Clear accuracy improvements over GPTQ and RTN at similar bitrates.** Across all model sizes, SpQR consistently achieves lower perplexity than both baselines. At 4 bits per parameter, SpQR roughly halves the error relative to the 16-bit baseline compared to GPTQ (e.g., LLaMA-7B: SpQR 5.87 vs GPTQ 6.13 on Wiki2), and the gap is often as large as the improvement of GPTQ over naive RTN. Results generalize across the LLaMA and Falcon families.

4. **Practical GPU inference faster than fp16.** The custom sparse-matrix multiplication for outliers combined with quantized dense multiplication achieves 20–30% speedup over fp16 inference (Table 4, e.g., LLaMA-7B: 57 vs. 47 tokens/s; LLaMA-65B fits on an A100 where fp16 does not). This demonstrates practical feasibility for deployment.

5. **Thorough ablation isolating design choices.** The paper separately evaluates bilevel quantization vs. 16-bit statistics (Table 3), outlier type comparison (unstructured vs. row vs. column, Fig. 3), activation order effects, and the impact of rounding zero-points — providing clear evidence for each design decision.

## Weaknesses

### Major

1. **Near-lossless claim is not consistently met on the paper's own definition.** The paper adopts the MLCommons standard of ≤1% relative perplexity increase (line 368–369) and states that SpQR "approaches the non-quantized models with at most 1% margin of error for all models" (line 376). However, in Table 1, LLaMA-65B with SpQR at 4.71 bits shows Wiki2 perplexity of 3.57 vs. 16-bit 3.53 — a relative increase of **1.13%**, exceeding the stated threshold. The abstract similarly claims "relative accuracy losses of less than 1%" (line 9). This is not a cosmetic issue: the 1% threshold is the paper's own definition of near-lossless, and the headline result for the largest model violates it on one of three datasets. The authors should either correct the claim to reflect the actual worst-case behavior or provide justification for why this small exceedance is acceptable.

2. **Speed evaluation lacks a quantized baseline.** Table 4 compares SpQR (optimized kernel) to fp16 and to SpQR using PyTorch's cuSPARSE outlier handling. There is no comparison to a similarly compact quantized format without outliers (e.g., GPTQ 4-bit with a kernel). Since any quantized format would be faster than fp16 due to reduced memory bandwidth, the reader cannot determine whether SpQR's speed advantage comes from the sparse-quantized format itself or merely from quantization. Additionally, the abstract states "15% speedup" (line 9) while the main text reports "20–30%" (lines 47, 541); these should be reconciled.

### Minor

3. **No generative quality evaluation.** The paper evaluates only perplexity and zero-shot accuracy. As the authors acknowledge (line 548), this leaves the "near-lossless" claim for actual open-ended generation unvalidated. Perplexity and multiple-choice accuracy do not guarantee fluency, coherence, or factual consistency in generated text, especially for smaller models where quantization errors may compound differently during autoregressive generation. The paper would be stronger with even a small-scale generative evaluation (e.g., MT-Bench, AlpacaEval, or human ratings on 100–200 samples).

4. **Pseudocode has unresolved ambiguities.** In Algorithm 1, the `outliers` subroutine passes the set $\mathcal{O}$ as an argument but never uses it — the `error` function only takes $W$ and $H^{\text{ic}}$, not $\mathcal{O}$. The description states that outliers are detected before statistics are fit, and `fit_statistics` correctly zeroes outliers before computing stats, but the detection itself computes quantization error on the full group including weights that will later be marked as outliers. While this is a standard leave-one-out detection (not a circular dependency as the reviewer claimed — the detection is *by design* based on comparing error with and without each weight), the unused $\mathcal{O}$ argument in `error` creates confusion about whether the pseudocode faithfully represents the implementation. These issues are presentation-level but hinder exact reproducibility.

5. **Falcon 7B at 3.92 bits shows a suspicious PTB value.** The PTB perplexity for Falcon 7B SpQR at 3.92 bits is listed as 19.114 (Table 2, line 454), which is dramatically higher than the 16-bit baseline of 9.90 and even far above RTN 4-bit (13.76). This appears to be a typo (possibly 10.114 rendered incorrectly). The authors should clarify or correct this value.

6. **The ablation comparing outlier types (Fig. 4) shows perplexity vs. number of outliers, not vs. bits spent on outliers.** The paper claims unstructured outliers "reduce perplexity significantly faster … even after accounting for the different memory footprint" (line 483), but the figure does not normalize by the memory cost per outlier type (unstructured: ~32 bits; row: much higher). The claim about memory footprint accounting is not supported by the presented axis.

### Trivial

- Abstract says "15% speedup" while main text says "20–30%." The speed data in Table 4 shows 15.8–21.3% speedup across models where fp16 fits (7B–30B), so 15% is a conservative floor but inconsistent with the text's range.
- Computation cost of the leave-one-out outlier detection per group is not discussed, though the reported 4.5 hours for 65B on A100 is acceptable for a one-time cost.

## Nice-to-Haves

- A comparison of inference speed against a 4-bit GPTQ kernel (even without a custom kernel) would contextualize the speed claims and help isolate the benefit of the sparse-quantized format.
- An ablation varying group sizes $\beta_1$ and $\beta_2$ would strengthen the understanding of bilevel quantization's behavior.
- A principled criterion for picking $\tau$ (e.g., analyzing when the perplexity gain per additional outlier saturates) would make the method less heuristic than "choose τ to get ~1% outliers."

## Removed Points

- **"O argument is passed but unused in the error function"** → The reviewer claimed this creates a "circular dependency" between outlier detection and statistics fitting. This is a misunderstanding: the detection step computes error with all weights (leave-one-in) vs. without each weight (leave-one-out) to identify which weights are most impactful. This is a standard approach, not a circular dependency. The unused $\mathcal{O}$ is a genuine pseudocode presentation issue (kept in Minor), but the claim of a circular dependency is removed as factually incorrect.
- **Demand for SparseGPT comparison** → The paper already cites SparseGPT in related work. A comparison between a 4-bit + sparsity method and a 4-bit + outlier method would be interesting but is scope-expanding beyond what the paper targets; moved to Nice-to-Haves.
- **"The paper does not analyze sensitivity to group sizes β₁, β₂"** → Moved to Nice-to-Haves as it is a reasonable suggestion but not a flaw in the presented results.
- **Certain Strength Finder strengths that conflict with verified weaknesses** → The claim of "near-lossless compression" as an unconditional strength is qualified in the strength description above.

## Novel Insights

The structural taxonomy of weight sensitivity patterns (row outliers, column outliers, sensitive attention heads, rotary embedding patterns, unstructured outliers) is the paper's most under-exploited insight. The observation that outlier weights include not just large-magnitude weights but also weights that GPTQ uses to compensate errors from many other weights (line 209) adds a nuanced dimension to outlier detection that distinguishes SpQR from prior work like LLM.int8(). The bilevel quantization of statistics — treating quantization metadata with the same quantization algorithm as weights — is a practical trick that may generalize beyond this specific setting.

## Suggestions

1. **Correct the near-lossless claim.** Either acknowledge that LLaMA-65B Wiki2 is at 1.13% (above the 1% threshold) and relax the claim accordingly, or provide justification for maintaining the 1% threshold (e.g., showing that the average across all three datasets stays within 1%).
2. **Add a quantized speed baseline.** Even reporting GPTQ 4-bit speed with PyTorch's native quantized matmul would let readers contextualize SpQR's speed advantage.
3. **Run a small generative evaluation.** 100–200 generation samples with automated metrics (MAUVE, perplexity of continuations) would substantially strengthen the "near-lossless for deployment" claim.
4. **Fix the Falcon 7B PTB suspicious value (19.114 → likely 10.114).**
5. **Clean up the pseudocode:** ensure `error` either takes $\mathcal{O}$ as an argument and uses it, or clarify in text that outlier detection is based on a leave-one-out comparison that does not require pre-excluding outliers from statistics.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>