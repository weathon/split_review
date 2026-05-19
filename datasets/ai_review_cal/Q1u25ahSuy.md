- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

SpQR introduces a hybrid sparse-quantized representation for LLM weight compression that isolates outlier weights (stored in 16-bit precision) while compressing the remaining weights to 3-4 bits using small-group quantization with bilevel quantization of the statistics. The method achieves near-lossless perplexity (~within 1% of the 16-bit baseline) at ~4.5-4.7 bits per parameter, outperforming GPTQ and RTN at matched bit budgets, and provides a custom GPU kernel achieving 20-30% speedup over fp16 inference.

## Strengths

1. **Novel and well-motivated hybrid format.** The sensitivity analysis (Section 3) identifies multiple outlier patterns (row, column, attention head, rotary embedding, unstructured) in LLM weights — going beyond prior observations of only input-feature outliers. This analysis directly motivates the hybrid sparse-quantized design, which is a genuine conceptual contribution.

2. **Clear empirical advantage over GPTQ and RTN.** At controlled ~4 bits per parameter, SpQR consistently halves the perplexity gap to the 16-bit baseline compared to GPTQ (e.g., LLaMA-7B Wiki2: SpQR 3.94 bits → 5.87 vs. GPTQ 4 bits → 6.13, vs. RTN 4 bits → 6.43). The improvement margin is comparable to GPTQ's improvement over RTN (Table 1), and the pattern holds across LLaMA and Falcon families (Tables 1 and 2).

3. **Strong ablation studies.** Each design component is validated independently: bilevel quantization with 3-bit statistics outperforms 16-bit statistics at similar memory (3.74 vs. 3.84 Wiki2 ppl, Table 4), and unstructured outliers reduce perplexity faster than row or column outlier alternatives (Figure 4). This confirms the design choices.

4. **Practical GPU inference kernel.** The optimized CSR-based sparse multiplication achieves 20-30% speedup over fp16 inference for models that fit in GPU memory (e.g., LLaMA-30B: 22 vs. 19 tok/s for scratch generation) and enables running LLaMA-65B (12 tok/s) where fp16 runs out of memory on an A100 (Table 5).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The "less than 1% relative perplexity" claim is violated for one of twelve tested model-dataset pairs.** For LLaMA-65B on WikiText2, the SpQR (4.71 bits) perplexity is 3.57 vs. the 16-bit baseline of 3.53, a relative increase of 1.13% — exceeding the advertised 1% threshold. The other 11 model-dataset pairs are within 1%, so the issue is not a systematic failure, but the abstract and introduction state the threshold as an unqualified achievement (lines 9, 32-33). The authors should either specify that this applies across most settings or adjust the claim to "within approximately 1%."

2. **The abstract's claim about running a "33B parameter LLM on a single 24 GB consumer GPU" is extrapolation beyond the paper's experimental scope.** No 33B model is tested, and all GPU experiments use an A100 (40/80 GB), not a consumer card. While the 30B LLaMA results (4.69 avg bits) make the memory arithmetic plausible (~17.6 GB for weights), the "consumer GPU" specific claim — with different memory bandwidth and compute characteristics — is unsupported by any actual measurements. The paper's contribution is strong enough without this extrapolation; it should be removed or substantiated with measurements on a 24 GB consumer GPU.

3. **No experimental comparison to SparseGPT** (Frantar et al., 2023), a directly competing method that also combines sparsity and quantization. SparseGPT is discussed in related work (line 87) but not included in any benchmark. A head-to-head comparison at comparable average bits would strengthen the evaluation. However, given that both works are approximately concurrent and share authors, the omission is understandable; the authors should at minimum explain why a comparison was not feasible.

### Trivial

1. **The pseudocode in Algorithm 1 has a missing comma** on line 232 (between the last two arguments to `outliers()`). The logic is still clear from context, but it could confuse readers.

2. **The "near-lossless" rows in Tables 1 and 2** are visually distinguished only by a midrule. A more explicit labeling (e.g., a separate "near-lossless" row marker) would improve readability.

## Nice-to-Haves

- A concrete description of how the sensitivity threshold $\tau$ is set globally (the paper says "the algorithm aims to pick a sensitivity threshold $\tau$ to obtain the desired number of outliers... around 1% of weights" on line 204, which is underspecified). A brief heuristic or binary search strategy would improve reproducibility.
- Including a generative quality metric (e.g., MT-Bench) would strengthen the claim that perplexity improvements translate to generation quality, as the authors acknowledge in their limitations section. This is not required for acceptance but would add value.

## Removed Points

- **Pseudocode errors about `outliers()` not returning O and S not being initialized**: Factually wrong. Line 284 explicitly returns `W, O`, and line 230 initializes `S := ∅`. The critic misread the pseudocode.
- **Various requests for comparisons outside paper's scope** (activation quantization methods like SmoothQuant, other inference engines like AutoGPTQ/llama.cpp): Scope creep. The paper clearly targets weight-only quantization and compares against the standard baselines (fp16, PyTorch sparse, GPTQ).
- **Complaint about zero-shot results shown as figures not tables**: A presentation preference, not a weakness. Figures are standard for showing trends across model sizes.
- **Missing statistical significance for perplexity**: Perplexity on fixed test sets is deterministic given the same model and calibration data. This is not a meaningful concern.
- **No generative evaluation**: The paper explicitly acknowledges this limitation (Section 6, lines 548-549). Not a hidden flaw.
- **Complaints about missing appendix/proofs/deferred content**: Parser artifact; these sections are present in the original submission.

## Novel Insights

The reviews collectively surface one observation not foregrounded in the paper: the 1% relative perplexity threshold is violated for LLaMA-65B on WikiText2 (1.13%), which creates a minor but real discrepancy between the paper's strongest advertised claim and its own data. The harsh critic correctly identifies this, and the strength finder's claim that "SpQR achieves <1% relative perplexity increase across all tested LLaMA and Falcon models" is technically imprecise for this one case. No other genuinely novel observation emerges beyond the paper's own contributions.

## Suggestions

1. **Tighten the "1% relative error" claim.** Either add "for most settings" / "approximately 1%" qualifiers to the abstract and introduction, or explicitly note that the LLaMA-65B Wiki2 case slightly exceeds the threshold but remains within 1.2%.
2. **Remove or substantiate the consumer GPU claim.** Either delete the unsupported "24 GB consumer GPU" claim from the abstract, or add a small set of measurements on an RTX 3090/4090 with a compressed 30B or 65B model.
3. **Add a brief discussion of SparseGPT compatibility.** Even without a direct comparison, explaining why a head-to-head comparison was not attempted (concurrent work, incompatible granularity, etc.) addresses the gap transparently.
4. **Clarify the tau-threshold selection** in the algorithm description by adding a short sentence on how the global threshold is determined.
