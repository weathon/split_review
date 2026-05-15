Now I have a thorough understanding of the paper and all the review components. Let me compose the consolidated review.

---

## Summary

This paper introduces LoQA (Low-Rank Quantization Adaptation), a method for fine-tuning quantized LLMs by using two LoRA-style adapters to update both the scale (**S**) and zero-point (**Z**) quantization parameters simultaneously. The two key components are HQ-LoRA (which enables learning both S and Z via separate low-rank modules) and QBAS (which adjusts the LoRA scaling factor by bit-width). Experiments on LLaMA models (7B–30B) across MMLU and commonsense reasoning benchmarks show consistent improvements over QA-LoRA (which only tunes Z), and the method matches or surpasses higher-precision 4+16-bit approaches while maintaining a fully quantized format.

## Strengths

- **Addresses a genuine limitation of QA-LoRA.** QA-LoRA restricts learnable parameters to zero-points only, capping performance. LoQA's key insight—jointly fine-tuning both scale and zero-point via separate low-rank modules—is a well-motivated and natural extension. The ablation study (Table 6) confirms both components contribute, and Table 7 shows LoQA achieves higher accuracy than QA-LoRA with fewer trainable parameters, indicating the improvement comes from better optimization rather than more parameters.

- **Consistent empirical gains across models and settings.** LoQA outperforms QA-LoRA on LLaMA-7B (+2.2% on Flan v2 MMLU), LLaMA-13B (+1.4%), and LLaMA-30B (+1.7%), maintains the advantage on Alpaca (Table 3), and works on LLaMA2/LLaMA3 families. The 2-bit results (Table 2) show LoQA surpassing the 2+16-bit SOTA IR-QLoRA by 4.7% on MMLU. These gains are consistent across model scales, bit-widths, and fine-tuning datasets.

- **Low training overhead.** Training time is reported as ~1.3× QA-LoRA (vs. QLoRA's ~2×), making the method practical for resource-constrained settings. The merged weights are compatible with standard inference frameworks (MLC-LLM, AWQ, Marlin), preserving the quantized format for deployment.

## Weaknesses

### Fatal
None.

### Major

- **Mathematical presentation error in the forward pass for group size > 1 (Equation 6).** The third term is written as `s·(W^Int ⊙ f(B'A', g)) x'`. Here, `W^Int ⊙ f(B'A', g)` has shape *D_out × D_in*, but `x'` (obtained via average pooling) has shape *(D_in/g) × 1*. Multiplying a *D_out × D_in* matrix by a *(D_in/g) × 1* vector is dimensionally invalid. For the second term, `s·BA x'` works dimensionally (`BA` is *D_out × (D_in/g)*, `x'` is *(D_in/g) × 1*), but produces a different result from the merged-weight forward pass (`f(BA, g) x`) by a factor of *g* when average pooling is used. The correct training forward pass should use the full-dimensional `x` (not `x'`) for the scale-related term, and the zero-point term should use `f(BA, g) x` (not `BA x'`) to match the merged inference path.

**Why this matters:** The paper's core contribution is HQ-LoRA, yet its defining equation contains a dimensional inconsistency. The merge equations (8, 10) are correct, and the g=1 special case (Equation 7) is correct, which suggests the implementation likely uses the correct formulation and Equation 6 has a notation error. However, as written, the paper's mathematics is imprecise for the practical g>1 setting. This must be clarified and corrected. It is a major presentation flaw that obscures the method and raises uncertainty about whether the training procedure matches the described inference-time behavior.

- **Misleading claim about surpassing 16-bit performance.** The paper states that "2-bit LoQA surpasses the original 16-bit model by 3.8%." The 16-bit model receives no downstream fine-tuning, while LoQA is fine-tuned on Flan v2. The observed gain almost certainly reflects the benefit of fine-tuning itself, not the quantization method. A proper baseline—16-bit model fine-tuned with standard LoRA on the same data—is absent. This comparison inflates the apparent contribution. The main claim of outperforming QA-LoRA and other quantized methods is unaffected, but the 16-bit-surpassing narrative should be removed or properly contextualized.

- **Critical experimental details unspecified.** (a) The paper does not state which PTQ method is used to obtain the initial quantized weights (e.g., RTN, GPTQ, or another scheme). This matters because different PTQ starting points could affect relative comparisons. (b) The group size used in the main experiments (Tables 1–3, 5) is not reported. Group size is integral to the method's correctness (see above) and directly affects the scale/zero-point granularity. A separate experiment (Table 8) uses group size 128, but the main tables do not specify. (c) No statistical variance (multiple seeds, confidence intervals) is reported. While single-run MMLU evaluation is the norm in this field, given the modest improvements over QA-LoRA (1–2%), some indication of stability would strengthen the results.

### Minor

- **QBAS motivation and derivation.** The QBAS scaling factor `s = α / (r · 2^{N-1})` uses `2^{N-1}` as the normalization constant. For unsigned N-bit quantization (range [0, 2^N-1]), the maximum value is `2^N-1`, not `2^{N-1}`. While this constant can be absorbed into the hyperparameter α and does not functionally harm the method, the paper's justification is imprecise. Additionally, QBAS's effect could be partially replicated by tuning α per bit-width, though the paper's ablation (Table 6) does show empirical benefit, which is the stronger argument.

- **LLaMA3 results undercut generality claims.** The paper honestly reports that LoQA's better data fitting on LLaMA3 does not translate to MMLU gains, and attributes this to dataset/training limitations. While transparency is commendable, this finding weakens the claim that LoQA "consistently achieves performance gains across a wide range of models."

- **Training time claim lacks implementation detail.** "1.3 times the training time of QA-LoRA" is stated without specifying GPU hardware, batch size, sequence length, or whether the measurement is per-step or total. This makes the claim difficult to verify or reproduce.

### Trivial
- The paper contains numerous garbled/broken formatting artifacts (equations running into text, misplaced image references, truncated sentences) that are parser errors rather than author errors. These do not affect evaluation.

## Nice-to-Haves
- A full-precision LoRA fine-tuning baseline on Flan v2 (16-bit model + LoRA) to isolate the effect of quantization from fine-tuning, and to properly contextualize the "surpassing 16-bit" claim.
- Reporting group size explicitly alongside each table of main results.
- Multiple-seed runs with mean ± std for at least the 4-bit experiments.
- Clarification of which PTQ scheme initializes the quantized weights.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Tables 1 and 2 are images with poor resolution" — This is a PDF extraction artifact, not an author error. The original submission contains proper tables.
- "The paper does not discuss methods that fine-tune scale parameters (e.g., LSQ, PACT)" — Missing related works is not a valid weakness as the reviewer cannot confirm what is or is not discussed; the paper adequately covers QA-LoRA, QLoRA, IR-QLoRA, PEQA, and EfficientQAT.
- "The claim of mathematical equivalence to the original operator (Section 3.2) is contradicted by the pooling operation introduced for group size > 1" — The claim refers to the quantization operator itself being compatible with LoRA, not to the correctness of the pooled forward pass. This is a misreading.
- "QBAS's effect could equivalently be absorbed into the learning rate" — While technically true, this ignores that QBAS automates cross-bit-width scaling to avoid separate tuning, which is a practical benefit. The ablation shows empirical value.
- Various typos/formatting nits — These are parser artifacts.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the paper's authors have not already addressed or that cannot be inferred from reading the paper directly.

## Suggestions

1. **Fix Equation 6.** Replace `x'` with `x` in the third term (scale update), and replace `BA x'` with `f(BA, g) x` in the second term (zero-point update). Verify that the implementation matches the corrected equation and comment on whether average vs. sum pooling is used. Clarify the training-inference consistency.

2. **Remove or contextualize the "surpassing 16-bit" claim.** Add a full-precision LoRA baseline or explicitly state that the 16-bit model receives no fine-tuning and the comparison is illustrative rather than competitive.

3. **Report group size for all experiments** and specify the PTQ method used for weight initialization. Add a line to the experimental setup describing these choices.

4. **Provide implementation details for training time claims** (GPU type, batch size, whether measured per-step or end-to-end).

5. **Consider running at least 2–3 seeds** for the main 4-bit experiments to establish stability, given the modest improvements over QA-LoRA.

---

## Score and Decision

**Score:** 5.0

**Decision:** Reject

**Rationale:** The paper identifies a worthwhile problem (extending QA-LoRA to learn scale in addition to zero-point) and provides consistent experimental evidence that the approach works. However, the core mathematical presentation of HQ-LoRA for group size > 1 (Equation 6) contains a dimensional error, which — until clarified or corrected — undermines confidence in the method's technical correctness. Combined with a misleading headline claim (surpassing 16-bit without proper baseline) and omitted experimental details (PTQ method, group size for main results), the paper requires substantial revision before it can be accepted. The underlying idea has merit, and the empirical trends are promising; a corrected and more precise exposition would make a stronger submission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>