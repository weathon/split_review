Now I have a thorough understanding of the paper and can verify each claim. Let me synthesize the final review.

**Verification of key criticisms against the paper text:**

1. **2-bit vs 16-bit comparison**: The paper says "surpasses the original 16-bit model by 3.8%" (line 244). The "original 16-bit model" is the base pre-trained LLaMA, while LoQA 2-bit is fine-tuned on Flan v2. This is indeed an apples-to-oranges comparison. However, the primary claim (beating IR-QLoRA 2+16-bit by 4.7%) is between two fine-tuned methods and is fair.

2. **PTQ method**: The paper describes uniform quantization in Eq. 3 (line 74-76) with round-to-nearest and specifies group sizes. The PTQ method IS implicit in the equations — standard uniform quantization / RTN. The critic's claim that it's completely unspecified is inaccurate; it's described through the quantization formula.

3. **QBAS justification**: The paper's motivation (line 135) states "magnitude of W_int varies with quantization bit-width" — this is correct. The choice of maxq = 2^(N-1) is not ablated vs alternatives. Valid minor concern.

4. **Missing EfficientQAT**: The paper mentions EfficientQAT in related work (line 43) as "improves upon PEQA by replacing the simple RTN method" but never compares to it. Valid concern — EfficientQAT is the most relevant missing baseline.

5. **One-dimensional average pooling**: The paper says (line 117) "apply one-dimensional average pooling with the corresponding group size to x" — kernel size IS the group size. The critic's claim that kernel size/stride is unspecified is incorrect.

6. **Column duplication operator**: The paper (line 78) says "the column duplication operator, which repeats the matrix V column-wise r times" — clearly specified. Critic's claim that it's unclear is wrong.

7. **PEQA discussion**: PEQA IS discussed in related work (line 43) AND included in experiments (line 152). Removed criticism.

8. **Confidence intervals**: Not standard in MMLU reporting for quantized LLMs. Move to Nice-to-Haves.

9. **Code release**: Rule says to remove reproducibility nitpicks about hyperparameters and trivial details. But a general "no code available" is a practical limitation — I'll keep it as a minor point.

Now let me produce the consolidated review.

---

Let me re-read the rules carefully:

"REMOVE criticisms that are factually wrong or misunderstand the paper."
→ The PTQ method IS specified (uniform quantization/RTN with equations). The column duplication operator IS clarified. The pooling kernel size IS given. Remove these.

"REMOVE weaknesses that amount to 'the paper should also cover Y / domain Z / additional tasks' when doing so would turn the paper into a different, broader paper"
→ The missing baseline (EfficientQAT) is a reasonable request within the paper's scope. Keep it.

"REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references."
→ Not applicable here.

"REMOVE pure formatting/style nitpicks."
→ "Tables are presented as images" is a parser issue. Remove.

"REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details"
→ Remove the "code not released" if it's treated as a nitpick. I'll keep it as a minor practical limitation since the rule says "trivial implementation details" and code release is a broader concern.

Actually, re-reading: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details, or large artifacts impractical to include in a submission (e.g., complete training logs)." - Code release is different from hyperparameters. I'll keep it but classify it appropriately.

Let me finalize and write the review.Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper introduces LoQA (Low-rank Quantization Adaptation), a two-stage method for fine-tuning quantized LLMs while preserving the quantized format. The core technical contributions are (1) HQ-LoRA, which uses two separate LoRA modules to jointly fine-tune both the scale (S) and zero-point (Z) of a uniform quantizer, and (2) QBAS, a bit-width-aware scaling factor for the LoRA update. Experiments on LLaMA, LLaMA2, and LLaMA3 models show consistent improvements over QA-LoRA (which only tunes zero-points) and competitive results with higher-precision methods.

## Strengths

- **HQ-LoRA enables joint fine-tuning of both scale and zero-point, consistently outperforming QA-LoRA.** The paper shows that by aligning LoRA granularity with quantization group size, two LoRA modules can naturally merge into S and Z after fine-tuning (Eqs. 8–10). Results across LLaMA-7B/13B/30B on MMLU (Table 1) show LoQA outperforming QA-LoRA by 1.4–2.2 percentage points under identical settings. The ablation (Table 6) confirms HQ-LoRA alone provides 1.1–1.6 points improvement over the baseline.

- **Consistent gains across multiple model families, datasets, and downstream tasks.** The paper evaluates on LLaMA, LLaMA2, LLaMA3 using both Flan v2 and Alpaca datasets, and on six commonsense reasoning benchmarks (Table 5). LoQA outperforms QA-LoRA in nearly every configuration, demonstrating robustness beyond a single setting.

- **Parameter efficiency: LoQA achieves better performance with fewer trainable parameters than QA-LoRA.** Table 7 shows LoQA with rank 4 (half the parameters of QA-LoRA rank 8) still outperforms QA-LoRA (e.g., 46.7% vs 45.8% on LLaMA-7B), suggesting the improvement comes from architectural design rather than sheer parameter count.

- **Ultra-low-bit results are genuinely strong.** The 2-bit LoQA beats the 2+16-bit SOTA IR-QLoRA by 4.7% (Table 2) — a fair comparison since both are fine-tuned on Flan v2. This is the strongest empirical result in the paper and demonstrates that joint scale+zero-point fine-tuning is particularly valuable under extreme compression.

- **Post-fine-tuning merging preserves inference efficiency.** The method is designed so that LoRA parameters can be merged back into S and Z (Eqs. 8–9), maintaining the original quantized format without FP16 LoRA residuals. The paper explicitly states compatibility with MLC-LLM, AWQ, BitBLAS, and Marlin toolkits.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence presented, and no single flaw invalidates the central contribution.

### Minor

- **The comparison of 2-bit LoQA against the "original 16-bit model" is confounded by fine-tuning.** The paper claims (Section 4.1, line 244) that 2-bit LoQA "surpasses the original 16-bit model by 3.8%." However, LoQA is fine-tuned on Flan v2 while the "original 16-bit model" is the base pre-trained LLaMA (no fine-tuning). The observed gain conflates fine-tuning with quantization. This claim appears in the abstract and introduction as a headline result. The primary claim (beating IR-QLoRA 2+16-bit by 4.7%) is between two fine-tuned methods and is fair, but the 16-bit comparison should be clarified or removed. A proper baseline would be a 16-bit model fine-tuned with the same LoRA on the same data.

- **Missing comparison against EfficientQAT.** The paper discusses EfficientQAT (Chen et al., 2024) in related work (line 43) as a method that "improves upon PEQA by replacing the simple RTN method," but EfficientQAT is not included in any experiment. Since EfficientQAT also fine-tunes scale parameters within a quantized model (and maintains the quantized format), it is the most natural missing baseline. Adding it would substantiate the claim that joint scale+zero-point tuning is uniquely beneficial.

- **The choice of maxq = 2^(N-1) in QBAS is not empirically justified against alternatives.** QBAS sets s = α/(r·maxq) with maxq = 2^(N-1). The paper motivates this by noting that W_int magnitude varies with bit-width (line 135), which is reasonable. However, no ablation compares this specific formula against alternatives such as s = α/(r·(2^N-1)), s = α/r with separate learning rates per bit-width, or a tuned constant. The ablation in Table 6 only shows that QBAS (as a whole) helps, not that this particular formulation is optimal or necessary. Since the effect could be absorbed into hyperparameter tuning of α, the paper would benefit from a targeted justification.

- **PTQ initialization is not explicitly stated.** The method section (line 50) says "a limited amount of calibration data to perform efficient post-training quantization (PTQ)" but never names the specific PTQ algorithm. The quantization formula in Eq. 3 describes standard round-to-nearest (RTN) uniform quantization, which is what the paper appears to use. However, explicitly stating "we use RTN" (or specifying if GPTQ/AWQ is used for initialization) would improve reproducibility.

- **The paper lacks a discussion of limitations.** Several practical considerations are not acknowledged: (a) after merging, the fine-tuned S and Z remain in FP16, so the quantization parameters themselves are not low-bit — this increases memory relative to pure integer quantizers; (b) whether the method's gains hold under activation quantization is not discussed; (c) the paper does not discuss settings where LoQA might underperform or fail.

### Trivial

- **Notation inconsistency in Equation (6):** The forward formula uses both `x` and `x'` but the relationship between them (average pooling with group-size kernel) could be stated more cleanly. The paper does clarify this in the surrounding text (line 117), but the equation alone is confusing on first read.

- **Training time claim is vague.** Section 4.3 mentions "LoQA demands 1.3× the training time of QA-LoRA" without reporting absolute wall-clock times or hardware details.

## Nice-to-Haves

- **Include confidence intervals or error bars for MMLU results.** Single-run MMLU evaluations are the norm in this literature, so this is not a flaw, but reporting variance would strengthen the paper's reliability claims.
- **Release code and evaluation scripts** to aid reproducibility, particularly since the method's success depends on the interaction between the two LoRA modules and the choice of rank/α.
- **Ablate the QBAS formula** against alternatives (e.g., s = α/r, s = α/(r·(2^N-1))) on a small model to empirically justify the specific choice of 2^(N-1).
- **Compare against EfficientQAT** in at least one setting to contextualize the joint scale+zero-point approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"PTQ method unspecified"** (as a major gap): The paper does specify its quantization via Eq. 3 (standard round-to-nearest uniform quantization with group size). The critic's framing as completely unspecified is inaccurate — the quantization formula is given. I have kept a softened version as a minor reproducibility note.
- **"f(V,r) column duplication operator is unclear"**: The paper explicitly says "the column duplication operator, which repeats the matrix V column-wise r times" (line 78). The critic misread this.
- **"Average pooling kernel size/stride unspecified"**: The paper says "apply one-dimensional average pooling with the corresponding group size to x" (line 117) — kernel size is the group size. Sufficiently specified.
- **"PEQA discussion is insufficient"**: PEQA is discussed in related work (line 43) AND used as a baseline in experiments (line 152). The critic's concern is unfounded.
- **"Tables presented as images"**: This is a PDF parsing artifact, not a paper flaw.
- **"No confidence intervals"**: Not standard practice for MMLU evaluations in this subfield. Moved to Nice-to-Haves.
- **Various formatting/typo complaints**: These are parser artifacts, not present in the original submission.
- **Strength from Strength Finder about "2-bit LoQA surpassing 16-bit model"**: This strength conflicts with the verified weakness about the unfair comparison. The primary result (beating IR-QLoRA) remains valid, but the 16-bit comparison is confounded by fine-tuning.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses surface the predictable tension between the paper's claimed generality and its limited baseline coverage, but no reviewer identified a structural insight that changes how the contribution should be framed.

## Suggestions

1. **Clarify or remove the "outperforms original 16-bit model" claim** in the abstract, introduction, and Section 4.1. Replace with a comparison against a 16-bit model fine-tuned with the same LoRA on the same data, or clearly state that the gain includes fine-tuning effects.
2. **Add EfficientQAT as a baseline** in at least the main 4-bit MMLU table to contextualize the benefit of joint scale+zero-point tuning versus scale-only tuning.
3. **Explicitly state the PTQ method** used (round-to-nearest uniform quantization) in Section 3.
4. **Add a Limitations section** acknowledging that (a) fine-tuned S and Z remain FP16, (b) the method is demonstrated only on weight-only uniform quantization, and (c) settings where LoQA might not help.
5. **Provide a targeted ablation** comparing QBAS's maxq=2^(N-1) against simpler alternatives on a small model to justify the specific design choice.

## Score and Decision

The paper makes a solid contribution: HQ-LoRA is a clean extension of QA-LoRA that enables joint fine-tuning of both quantization parameters, and the results consistently show meaningful gains. The weaknesses identified (the confounded 16-bit comparison, missing EfficientQAT baseline, insufficient QBAS justification) are real but addressable — none invalidate the core contribution. The 2-bit result against IR-QLoRA is the strongest evidence and is unaffected by these concerns.

The paper does what it sets out to do: propose and validate a method for fine-tuning both scale and zero-point while preserving the quantized format. The empirical evaluation is reasonably thorough across models and datasets. With the suggested revisions, this would be a clean contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>