I've now read the full paper and verified all reviewer claims against the actual content. Let me now construct the consolidated final review.

---

## Summary

This paper introduces Super Floating-Point (SuFP), an 8-bit custom data type for quantizing deep neural networks. SuFP combines (a) multi-region piecewise quantization — three representations with different exponent baselines and mantissa allocations to cover dense near-zero values and outliers — with (b) a tensor-wise scalable bias (5-bit, −16 to +15) that adjusts the exponent range per tensor via a single integer addition. A custom Processing Element designed for SuFP uses only integer arithmetic units and a 6-bit multiplier. Experiments evaluate accuracy across vision (ResNet, ViT, EfficientNet-v2), language (BERT), text-to-image (Stable Diffusion), and LLMs (Llama 2 on MMLU), alongside memory footprint and hardware efficiency results.

## Strengths

1. **Novel multi-region piecewise quantization design within a fixed 8-bit budget.** The idea of dedicating 2 encoding bits to select among three representations — one subnormal (all mantissa), one intermediate, one wide-range — is a thoughtful way to pack both high-precision near-zero and coarse outlier coverage into a single 8-bit format. This is structurally different from prior block-floating-point approaches (MSFP, BSFP) that use shared exponents at the block level. (Section 3, Algorithm 1, Figure 3.)

2. **Hardware efficiency from integer-only PE with a 6-bit multiplier.** The SuFP PE uses only integer ALUs and shifters, and employs a 6-bit multiplier (vs MSFP's 7-bit). The results in Figure 6 show 9.00× throughput-per-area over FP32 and up to 7.20× over MSFP/BSFP, and 17.04× energy efficiency over FP32. These hardware comparisons are on synthesized PEs at the same technology node (28nm, 500MHz), making the comparison concrete. (Section 4.4, Figure 6, lines 100–101, 151–153.)

3. **Tensor-wise scalable bias as a lightweight alternative to block-level scaling.** The bias applies at the tensor level (rather than per block), requires only a single integer addition per tensor, and extends the exponent range by −16 to +15. This is cleaner than BSFP's per-subword scaling factors and does not incur the memory overhead of smaller block sizes. (Section 3, lines 74–78.)

4. **Evaluation across four distinct model families.** The paper tests on vision CNNs (ResNet, EfficientNet), vision transformers (ViT), BERT, Stable Diffusion, and Llama 2 — giving breadth to the claim of broad applicability. (Section 4.2, Tables 2–4.)

## Weaknesses

### Fatal
None. The core ideas are coherent and the paper presents a complete method, hardware design, and experimental suite. No single error invalidates the entire contribution.

### Major

1. **Unfair and opaque baseline comparisons undermine the accuracy claims.** In Table 2 (vision models), MSFP is configured as **MSFP16** (1+7+8 = 16 bits, per the table footnote on line 114), while SuFP is 8 bits. Comparing 8-bit SuFP's accuracy drop (0.06%) against 16-bit MSFP's drop (0.17%) or 7+bit BSFP's drop (0.2%) is not an apples-to-apples comparison — MSFP is operating at twice the bit budget. The paper then states "SuFP outperforms MSFP and BSFP" implicitly from this table. In Tables 3 and 4 (language, text-to-image, LLMs), the bit-widths of MSFP and BSFP are *not specified at all* (line 120, line 135), making it impossible to assess whether the comparison is fair. The paper does compare against FP8 E4M3 (an 8-bit format) in those tables, which is appropriate, but the overall presentation suggests SuFP surpasses MSFP/BSFP without disclosing that the MSFP baseline in the accuracy evaluation uses twice the bits. **This is the most consequential weakness in the paper.**

2. **The SuFP data format is underspecified and not reproducible.** The paper describes a sign bit, an "encoding field," and a "data field" (line 64), but never states the exact bit counts for each field. From the example positions `b5` and `b4` (line 70) and the 8-bit total, one can deduce 2 encoding bits and 5 data bits — but this deduction is never confirmed. More critically, for representations ② and ③, which "divide the data field into exponent and mantissa sections" (line 70), the paper never specifies how many bits are allocated to exponent vs. mantissa in each representation. Without this, the claimed granularities (2⁻⁴ for the dense region, 26 for outliers on line 72) cannot be derived. Additionally, the algorithm for determining the per-tensor bias is described only as "predetermined" (line 78) with no method given. These omissions mean the method cannot be independently reimplemented or fully evaluated on paper.

3. **No ablation studies isolate the contribution of each component.** The paper attributes success to two main design choices: multi-region piecewise quantization and tensor-wise scalable bias. Neither is ablated. There is no experiment showing accuracy with a single region (effectively a fixed 8-bit floating-point format with no encoding field), or with a fixed bias (no tensor-wise adjustment). Without this, the reader cannot tell whether the complexity of the encoding scheme is warranted, or whether a simpler approach — e.g., a single region with a well-chosen per-tensor bias — would achieve similar results.

### Minor

1. **INT8 quantization is not included as a baseline.** INT8 uniform quantization is the most standard 8-bit inference format and is discussed in the related work (line 43–45), but never compared experimentally. Since SuFP is an 8-bit format, omitting INT8 leaves a natural reference point unaddressed.

2. **Accuracy results are point estimates with no variance or statistical significance reported.** All values in Tables 2–4 are single numbers. Given the normalization to FP32 for EfficientNet-v2 (line 116), which itself indicates variance across implementations, reporting standard deviations or multiple runs would strengthen confidence.

3. **LLM evaluation is limited to a single benchmark (MMLU).** Table 4 shows only MMLU for Llama 2. While MMLU is a standard benchmark, evaluating on perplexity (WikiText-2) or a second LLM (e.g., OPT) would better substantiate the claim about outlier handling, as those settings are known to stress quantization schemes. The paper acknowledges SuFP targets outliers but does not directly measure outlier-handling quality.

4. **Hardware results lack absolute numbers.** Figure 6 shows throughput-per-area and operations-per-watt normalized to FP32, but the actual area (μm²) and power (mW) values are not reported. Absolute numbers would allow readers to verify the conclusions and compare against other published designs.

5. **Rounding mode is not specified.** The paper does not state whether it uses round-to-nearest, truncation, stochastic rounding, or another scheme. This is a standard detail for quantized inference.

### Trivial
- The resolution operations-per-watt in the abstract (line 4) says "up to 2.06×" for BSFP, while the conclusion (line 160) says "up to 8.27×" — these are about different things (energy efficiency vs. computational capability?), but the relationship should be clarified.

## Nice-to-Haves
- Analyze the overhead of computing the per-tensor bias (e.g., does it require calibration data? a forward pass? What is the time/memory cost?).
- Compare against an 8-bit variant of MSFP, if one exists in the literature, to create a matched bit-width comparison.
- Provide quantization error distributions across layers for one vision model and one LLM to visually demonstrate the claimed benefit of multi-region coverage.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Accuracy tables are absent" / "Table 1 is not visible"* — The tables exist as embedded images in the original submission. The parser extracted image placeholders, but in the submitted PDF they are present and readable. REMOVED (factually incorrect given the submission format).
- *"No discussion of 4-bit regimes"* — The paper proposes an 8-bit format; criticizing it for not covering 4-bit is scope creep. REMOVED.
- *"No comparison to MSFP8"* — The critic asserts MSFP8 exists as a known variant, but this is not established in the paper nor verifiable from its references. The valid underlying concern (lack of a matched 8-bit MSFP comparison) is captured in Major Weakness #1. REMOVED.
- *"No comparison to adaptive float formats or micro-exponent designs"* — Generic criticism without specific missing works named. REMOVED.
- *Strengths about "importance of the problem" or "addressing an important question"* — Generic and not specific to this paper's evidence. REMOVED.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an interpretation of the data or method that the authors themselves missed.

## Suggestions
1. **Specify the format completely.** State explicitly: total bits = 8; sign = 1 bit; encoding = 2 bits; data field = 5 bits. For each of the three representations, give the exact number of exponent bits and mantissa bits within those 5 data bits. Provide the decoding table (encoding → exp bits, mant bits, exponent baseline). Describe the bias selection algorithm.
2. **Fix the baseline comparisons.** In all accuracy tables, specify the total bit-width of every baseline. Add a fair comparison where MSFP is configured at 8-bit if possible, or acknowledge the bit-width disparity and compare SuFP primarily against other 8-bit formats (FP8 E4M3/E5M2, INT8). Reframe claims about "surpassing MSFP/BSFP" to specify whether this refers to accuracy (at matched bits) or hardware.
3. **Add ablation experiments.** Compare SuFP against: (a) a version with a single representation (no encoding field, a fixed 8-bit float-like format), and (b) a version with fixed bias (no tensor-wise adjustment). Show the accuracy impact of each component.
4. **Add INT8 comparison** for at least one vision model and one LLM.
5. **Report absolute hardware numbers** (area in μm², power in mW) alongside normalized ratios.

## Score and Decision

The paper presents a creative data type design that is conceptually well-motivated, and the hardware PE results are promising. However, the accuracy evaluation is compromised by comparing 8-bit SuFP against 16-bit MSFP without disclosure, the format specification is incomplete to the point of irreproducibility, and the lack of ablations makes it impossible to attribute performance to the proposed mechanisms. These are fixable issues, but in their current form they prevent acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>