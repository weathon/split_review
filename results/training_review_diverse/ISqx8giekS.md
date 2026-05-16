Now I have a complete picture. Let me write the final consolidated review.

---

## Summary

This paper proposes LeanQuant, a post-training quantization method for LLMs that builds on the iterative loss-error-based framework (OBQ/GPTQ). The key insight is that the standard min-max affine quantization grid is suboptimal because it treats all weights equally, whereas weights corresponding to small values of the inverse Hessian diagonal (i.e., those with high loss-error risk) need finer precision. LeanQuant learns loss-error-aware grids — via weighted k-means for non-uniform quantization and a discrete search over shrinking intervals for affine quantization — and integrates them into the GPTQ iterative update loop. A fused GPU kernel makes the affine-grid search tractable (50× speedup), enabling quantization of Llama-3.1 405B on two 48GB GPUs in 21 hours. Experiments show favorable perplexity and zero-shot accuracy vs. GPTQ, AWQ, OmniQuant, and SqueezeLLM, with especially large gains at 3-bit.

## Strengths

1. **Clear diagnosis of a real limitation in existing iterative quantization.** The paper correctly identifies that the standard min-max affine grid in GPTQ/OBQ does not account for per-weight differences in loss-error sensitivity. The loss-error expression (Eq. 6: εᵢ ∝ (Δwᵢ)² / H⁻¹ᵢᵢ) shows that weights with small H⁻¹ᵢᵢ contribute disproportionately to the total error. Figure 2 directly validates that LeanQuant's grids reduce accumulated loss error relative to GPTQ — this is the most direct evidence for the core claim.

2. **Scalability to 405B parameters with modest hardware.** Quantizing Llama-3.1 405B on two 48GB GPUs in 21 hours and Mistral-Large 123B on a single 48GB GPU in 4.2 hours (Table 4) is a strong engineering result. Memory consumption is drastically lower than OmniQuant (OOM at 70B) and SqueezeLLM (OOM at 8B), making the method accessible for models that competing accurate methods cannot handle.

3. **Substantial zero-shot accuracy improvements in the challenging 3-bit regime.** At 3-bit, LeanQuant_aff improves average zero-shot accuracy over OmniQuant by 17.18% (Llama-3-8B) and 14.14% (Mistral-7B), and over GPTQ by 18.38% and 9.16% respectively (Section 4.1). These margins are large by PTQ standards and are backed by explicit numerical claims in the text.

4. **Versatility across quantization formats.** The method works for both affine (group-wise and row-wise) and non-uniform quantization, meaning quantized models are directly compatible with existing high-performance inference kernels (Marlin, LUT-GEMM) without requiring custom data types or specialized codebooks.

5. **Practical fused kernel for grid learning.** The 50× speedup from the fused GPU kernel (Table 5: 15.1 hrs → 0.27 hrs for Llama-3-8B) transforms the affine-grid search from impractical to efficient, which is critical for scaling to 100B+ models.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficient analysis of the extraordinary 3-bit gains over OmniQuant.** The paper reports that LeanQuant_aff improves average zero-shot accuracy over OmniQuant by ~17% at 3-bit (Llama-3-8B) and ~14% (Mistral-7B). OmniQuant *also* learns scaling factors via gradient descent with a smooth quantization surrogate, so the reader needs to understand why its learned scaling cannot approximate the same effect. The paper provides no analysis — e.g., whether OmniQuant's optimization gets stuck in poor local minima at very low bitwidths, whether the exhaustive discrete search in LeanQuant finds a better range than gradient-based learning, or whether baseline hyperparameters are aligned. Without this explanation, the magnitude of the claimed gains appears implausible and invites skepticism about the baseline configuration. This is the most significant gap in the paper's evidence.

2. **The non-uniform variant's improvement over SqueezeLLM is not properly isolated.** LeanQuant_nu differs from SqueezeLLM in *two* ways: (a) loss-error-aware weighting in the k-means objective, and (b) the iterative GPTQ-style weight update (SqueezeLLM does not perform iterative updates). The paper lacks an ablation that isolates (a) — e.g., comparing GPTQ + standard (unweighted) k-means vs. GPTQ + weighted k-means (LeanQuant_nu) within the same iterative framework. Without this, improvements could be driven primarily by the iterative update rather than the weighted grid. The loss-error comparison in Figure 2 partially addresses this concern for the affine case, but the non-uniform variant specifically needs this ablation.

### Minor

3. **Confusing narrative around "inverse Hessian diagonal outliers."** The paper states (line 125) that it examines the distribution of 1/H⁻¹ᵢᵢ, yet the figure caption refers to "inverse Hessian diagonals" containing "outliers that can cause high loss errors." The loss error εᵢ ∝ 1/H⁻¹ᵢᵢ, so it is *small* H⁻¹ᵢᵢ (which produce *large* values in the 1/H⁻¹ᵢᵢ distribution) that cause high loss error. The text and figure caption conflate the two quantities. The method itself is correct — the weighting (H⁻¹ᵢᵢ)⁻ᵖ correctly downweights large H⁻¹ᵢᵢ and upweights small H⁻¹ᵢᵢ — but the narrative should be clarified to avoid confusing readers.

4. **No variance or confidence intervals reported.** Quantization results can be sensitive to the random calibration subset. Reporting mean ± std over multiple calibration draws (even 3 runs) would strengthen the evidence, especially for the dramatic 3-bit results.

5. **Bitwidth notation for the 405B experiment (4.25) is not explained.** The paper reports "4.25 bits" for group-size-128 quantization but does not explain how this is calculated (e.g., overhead from storing zero-points and scaling factors). This should be clarified for reproducibility.

### Trivial

6. **Storage overhead of learned grids for non-uniform quantization is not discussed.** Each row stores 2ᵇ grid points; this is negligible but should be stated for completeness.

7. **GPTQ's memory usage is missing from the efficiency comparison.** Table 4 (peak GPU memory) compares LeanQuant to OmniQuant and SqueezeLLM but omits GPTQ, which is the most direct baseline. Including GPTQ's memory would make the efficiency advantage clearer.

## Nice-to-Haves

- An ablation showing GPTQ + standard k-means vs. GPTQ + weighted k-means (LeanQuant_nu) within the same iterative framework, to isolate the effect of the Hessian-aware weighting for the non-uniform variant.
- A brief analysis of why OmniQuant underperforms at 3-bit: e.g., comparing the learned affine ranges from both methods and showing that OmniQuant's gradient-based optimization converges to a wider (closer to min-max) range while LeanQuant's discrete search finds a tighter range.
- Sensitivity analysis for the search granularity T (currently fixed at 2048) to show whether a coarser grid would suffice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The harsh critic's note about "the main results table (tbl:accu) is not present in the snippet" — this is a parser artifact; the table is an `\input{}` in the original submission.
- The harsh critic's mention that "The paper does not discuss the storage overhead of the learned grids" — kept as trivial weakness above since it's a genuine (if small) omission, but downgraded from the critic's framing.
- Strength Finder's claim about "Large accuracy gains" — kept but the corresponding weakness about insufficient justification is noted above.
- The suggestion to "add an ablation that replaces the weighted grid with a standard (unweighted) non-uniform grid inside GPTQ" — kept as Major Weakness #2 but reframed.
- The note about "no multiple seeds or confidence intervals" — kept as Minor Weakness #4.
- The note about the 4.25 bitwidth — kept as Minor Weakness #5.

## Novel Insights

The reviews collectively highlight an interesting tension: the paper's core diagnostic insight (min-max grids are suboptimal due to varying loss-error sensitivity across parameters) is principled and well-supported by the loss-error analysis, yet the extraordinary empirical gains at 3-bit over a strong baseline (OmniQuant) that also learns scaling factors remain unexplained. This gap suggests either that the discrete search space in LeanQuant is critical (the grid search avoids poor local minima that gradient descent falls into at very low bitwidths) or that there is a configuration asymmetry. A controlled experiment that retrofits the LeanQuant grid-search strategy into OmniQuant's pipeline would directly test this hypothesis and would be a valuable contribution beyond the present paper. Additionally, the fact that LeanQuant's memory efficiency comes from avoiding gradient computation (unlike OmniQuant and SqueezeLLM) while still outperforming these methods suggests that the iterative GPTQ update + learned grid combination may be a Pareto-optimal design point that the community has overlooked.

## Suggestions

1. **Clarify the outlier terminology.** Replace "outliers in inverse Hessian diagonals" with precise phrasing: "weights with small H⁻¹ᵢᵢ (large 1/H⁻¹ᵢᵢ) incur high loss error and need finer quantization." Ensure the figure caption matches what is actually plotted (1/H⁻¹ᵢᵢ, not H⁻¹ᵢᵢ).
2. **Provide an analysis of the 3-bit OmniQuant comparison.** Show a side-by-side comparison of the learned affine ranges from both methods at 3-bit to explain why OmniQuant underperforms.
3. **Add the non-uniform ablation** (GPTQ + unweighted k-means vs. GPTQ + weighted k-means) to isolate the effect of the loss-error-aware weighting.
4. **Report variance** for at least the 3-bit results (3 runs with different calibration subsets).
5. **Explain the 4.25 bits** calculation for group-wise quantization in the 405B case.

## Score and Decision

The paper makes a solid contribution: it identifies a genuine limitation of existing iterative quantization methods, proposes a well-motivated fix (loss-error-aware grids), demonstrates scalability to 405B parameters that competing accurate methods cannot reach, and provides a practical fused kernel. The weaknesses are real but addressable. The main concern is the insufficient analysis of the very large 3-bit gains over OmniQuant, which undermines the credibility of the strongest claimed results. However, the core contribution does not depend on these specific numbers — the loss-error reduction (Figure 2) and scalability results stand independently.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>