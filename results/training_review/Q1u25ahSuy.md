Here is my consolidated review, with all claims verified against the paper.

---

## Summary

This paper introduces SpQR (Sparse-Quantized Representation), a hybrid compression format for LLM weights that combines (1) identification and high-precision storage of outlier weights with (2) bilevel quantization of group statistics to enable very small quantization groups without the usual metadata overhead. The method is evaluated on LLaMA (7B–65B) and Falcon (7B, 40B) families, achieving perplexity within 1% of the 16-bit baseline at 4.6–4.7 bits per parameter, with a custom GPU kernel that yields 20–30% inference speedups over fp16.

---

## Strengths

- **Novel discovery of row-wise outlier patterns in weight sensitivity.** The paper identifies that outlier weights can occur along output hidden dimensions (rows), not only along input features (columns) as prior work assumed. Section 3.2 provides compelling visualizations of four distinct sensitivity structures (row outliers, column outliers, sensitive attention heads, rotary embedding patterns), and Section 5's ablation (Fig. outliers_fig) confirms that unstructured outlier handling outperforms both row-level and column-level alternatives.

- **Bilevel quantization of group statistics is clever and empirically effective.** By quantizing the per-group scales and zero-points themselves (3-bit over groups of 16) instead of storing them in 16-bit, SpQR makes very small group sizes (β₁=8–16) practical. The ablation in Table 3 directly supports this: the 3-bit statistics configuration at 3.63 avg bits (perplexity 3.74 on Wiki2) outperforms the 16-bit statistics configuration at 3.67 avg bits (perplexity 3.84) on LLaMA-65B — a clear win despite slightly fewer bits.

- **Practical GPU inference kernel with measured speedups.** The optimized SpQR kernel achieves 20–30% faster token generation than fp16 across LLaMA models (Table inference), while the fp16 baseline runs out of memory at 65B. The kernel handles the sparse outlier multiplies via a CSR-like scheme and the dense quantized multiplies in a combined pass, demonstrating that the format is engineering-feasible, not just a paper idea.

- **Consistent improvement over GPTQ at matched bit-width.** At comparable average bits (~4 bits), SpQR consistently halves the perplexity gap to the 16-bit baseline relative to GPTQ across model scales (e.g., LLaMA-7B Wiki2: SpQR 3.94 bits → 5.87 vs. GPTQ 4 bits → 6.13, reducing the 16-bit gap from 0.45 to 0.19).

---

## Weaknesses

### Fatal
None.

### Major

- **The abstract and introduction overclaim the compression ratio for near-lossless performance.** The abstract claims "3-4 bits per parameter" (line 8, line 31), and the introduction says the format "can compress accurate pretrained LLMs to 3-4 bits per parameter while staying near-lossless" (lines 31–33). However, the actual near-lossless results (within 1% perplexity) require **4.63–4.71 bits per parameter** for LLaMA models (Table: LLaMA-7B at 4.63 bits, 65B at 4.71 bits) and 4.44–4.46 for Falcon. The 3.9–4.0 bit configurations consistently exceed the 1% perplexity threshold (e.g., LLaMA-7B: 5.87 vs. 5.68 = +3.3%). The paper *is* transparent about these numbers in the results section, but the headline framing is misleading. This is not a fatal flaw — the method is still state-of-the-art — but the paper should honestly frame the contribution as "near-lossless at 4.5–4.7 bits with practical speedups at ~4 bits."

- **Unsubstantiated 33B model claim.** The abstract states that SpQR "makes it possible to run 33B parameter LLM on a single 24 GB consumer GPU without any performance degradation at 15% speedup" (line 9). No experiment in the paper evaluates a 33B model. The evaluated model sizes are LLaMA {7,13,30,65}B and Falcon {7,40}B. This claim appears to be extrapolation rather than a measured result, and it should either be supported with evidence or removed.

### Minor

- **No evaluation of generative quality (acknowledged by the authors).** The paper lists this as a limitation (Section 6), stating that only perplexity and zero-shot accuracy are measured. Perplexity is the standard evaluation metric in the LLM quantization literature (GPTQ, SmoothQuant, LLM.int8() all rely on it), so this is not a deviation from community norms. However, for a paper whose title includes "Near-Lossless," some evidence that generation quality is preserved (e.g., qualitative examples, diversity metrics, or human evaluation) would strengthen the claim. As-is, the paper is honest about this gap but it limits the strength of the "near-lossless" assertion.

- **No sensitivity analysis on the outlier threshold τ.** The paper states that τ is chosen to obtain ~1% outliers (line 204, line 369), but provides no ablation showing how performance varies with the outlier percentage or τ. Since outlier storage is expensive (32+ bits/outlier), the trade-off between outlier budget and perplexity is central to the method's practical use.

- **Table and figure presentation:** The zero-shot accuracy results are shown only as a small plot (Fig. 1 right) with no numerical table, making it difficult to read exact values. The paper should include a supplementary table with the raw accuracy numbers.

### Trivial

- The discussion section (line 547) says "less than 4.75 bits per parameter on average" — this is a different number from the "3-4 bits" in the abstract, creating an inconsistency that careful readers will catch.
- Table 3 uses "3.63 avg bits" for the 3-bit statistics row but the row-zero and w/o-act-order rows also show 3.63 bits, suggesting the minor variants don't change the bit count — this is correct but could be labeled more clearly.

---

## Nice-to-Haves

- An ablation of performance vs. outlier percentage / τ would help users understand the memory-quality trade-off and is a natural extension of the current experiments.
- Fixed-bit-rate comparison (SpQR, GPTQ, RTN all at exactly 4.0 bits and all at 4.5 bits) would cleanly separate whether SpQR's advantage comes from extra bits for outliers or from the representation itself. The paper already provides approximate comparisons (SpQR ~3.94 vs. GPTQ/RTN 4.0) which mostly address this, but a controlled experiment would be cleaner.
- Reporting the average bits for the SpQR models used in the inference speed test (Table inference) would help readers interpret the speedup relative to fp16.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Outlier detection algorithm may not correspond to the sensitivity analysis"** — The `outliers` function in Algorithm 1 uses a leave-one-out heuristic comparing quantization error with and without each weight. This is a reasonable approximation to the OBS-based sensitivity in Eq. 1, and the paper states it "implements a filtering technique based on the sensitivity criterion in Eq. (1)" (line 202). The reviewer's concern about a theoretical gap is overstated; the connection is adequately explained.
- **"Misleading comparison with baselines"** — Verified against the paper's own numbers: for LLaMA-7B Wiki2, the improvement of SpQR (3.94 bits) over GPTQ (4 bits) is 6.13 − 5.87 = 0.26, while GPTQ's improvement over RTN is 6.43 − 6.13 = 0.30. The claimed "gap being as large as" is approximately accurate (0.26 ≈ 0.30). The statement is a slight exaggeration but not a factual error.
- **"No code/reproducibility"** — The paper provides the algorithm (Alg. 1) and states hyperparameters (calibration data, group sizes, thresholds). Code release is standard but not required for publication; the method is described in sufficient detail for replication.
- **Strength Filter's claim: "Near-lossless compression at 3-4 bits per parameter"** — This repeats the paper's overclaim. The corrected formulation is used in the Strengths section above.

---

## Novel Insights

The most interesting observation from the reviews is the tension between the reviewers' characterization of the "3-4 bits" claim as potentially fatal vs. the paper's actual transparent reporting. The paper *does* show its near-lossless numbers at 4.6–4.7 bits and its ~4-bit numbers at ~4% perplexity degradation — the data is not hidden. The conflict is between the abstract's marketing and the paper's evidence. This is a framing flaw, not a methodological fraud, and the community discussion this reveals (how much compression "counts" as 3-4 bits) is itself a useful lesson for future quantization papers. The genuine algorithmic contributions — particularly bilevel quantization of statistics and the discovery of row outliers — are not challenged by any reviewer and stand as solid advances.

---

## Suggestions

1. **Revise the abstract and introduction** to accurately state the bit-rates: "near-lossless compression at 4.5–4.7 bits per parameter, with practical speedups and strong performance at ~4 bits."
2. **Add the 33B experiment or remove the claim** from the abstract. Since the method is evaluated on 30B and 40B models, a 33B result should be easy to produce.
3. **Add a table of zero-shot accuracy numbers** to supplement Figure 1 (right), enabling readers to see exact values.
4. **Include an ablation of outlier percentage vs. perplexity** to help practitioners select the τ threshold.

---

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>