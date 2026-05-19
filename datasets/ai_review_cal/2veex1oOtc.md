- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have a thorough understanding of the paper. Let me synthesize my final review.

---

## Summary

MQuant is a post-training quantization (PTQ) framework for multimodal large language models (MLLMs). It addresses three identified challenges — visual token explosion causing slow inference, distribution mismatch between visual and text tokens, and sensitivity to outlier clipping — through modality-specific per-tensor static quantization with token reordering (MSQ+AIFS), a Post-LN to RMSNorm transformation enabling Hadamard rotation in vision encoders, and Rotation Magnitude Suppression (RMS) to mitigate Hadamard-induced weight outliers. Experiments on five MLLMs at W4A8 show near-floating-point accuracy with reported speed and memory improvements.

## Strengths

1. **Well-motivated problem identification backed by evidence.** The paper identifies three concrete, MLLM-specific obstacles to quantization — visual token count exploding with image resolution (Fig. 1a), divergent activation distributions across modalities (Fig. 1b), and disproportionate accuracy loss from clipping visual outliers (Table 1). These diagnostics are specific, measured, and directly inform the design choices.

2. **MSQ+AIFS delivers a practical solution to a real tension between speed and accuracy.** MSQ applies separate per-tensor quantization scales to visual and text tokens, while AIFS reorders mixed-modality tokens so that per-tensor GEMM operations become possible without irregular memory accesses. Table 4 shows this combination matches per-tensor static latency (0.032s) while maintaining near-FP accuracy (64.42 vs 64.46 on TextVQA), compared to a 62.90 drop from naive static quantization.

3. **Post-LN→RMSNorm transformation extends rotation-based smoothing to vision encoders.** Prior rotation methods (SliceGPT, Quarot) assumed Pre-LN architectures common in LLMs. Section 4.2 derives an arithmetic equivalence (Eq. 10) that converts Post-LN to RMSNorm, enabling Hadamard rotation in vision encoders. The ablation in Table 5 isolates a clean gain (OCRBench 62.90→63.08) from adding this step.

4. **RMS is a simple, effective fix for rotation-induced weight outliers.** The paper provides a statistical argument (Eq. 12‑13) that only the first input channel after Hadamard rotation can produce outsized values, validates this empirically (Fig. 4b), and proposes a clean separation of that channel. Table 5 shows RMS boosts OCRBench from 63.08 to 63.56, approaching the FP model at 63.69.

5. **Systematic ablation isolates each component.** Table 5 starts from a static baseline and progressively adds AIFS+MSQ, LN2RN, and RMS, with clear incremental improvements on both OCRBench and MME. This provides direct evidence that each technique contributes.

6. **Evaluation spans five diverse MLLMs.** InternVL2-8B, Qwen-VL-Chat-9.6B, MiniCPM-V 2.6-8B, Qwen2-VL-7B, and GLM-4V-9B cover different architectures, model sizes, and vision encoders. Table 2 shows the accuracy gains are consistent rather than model-specific.

## Weaknesses

### Fatal

None.

### Major

1. **Memory savings metric is reported in a non-standard way that inflates the numbers.** The paper reports "Memory Saving vs PyTorch (↑)" with values exceeding 100% (e.g., 152.92%). Under the conventional definition (baseline − ours)/baseline × 100%, savings cannot exceed 100%. These values are most consistent with the formula (baseline − ours)/ours × 100%, which is non-standard and makes the savings appear larger. For example, a 152.92% value by this formula corresponds to roughly 60.5% conventional savings — still impressive, but the "over 100%" framing in the text is misleading. The paper must either report raw memory consumption in GB, use the conventional (baseline − ours)/baseline formula, or explicitly define the computation. This directly affects a headline quantitative claim.

2. **Speedup comparison lacks a dynamic per-token quantization baseline at the same bit-width.** The paper's efficiency motivation is that per-token dynamic quantization is slow for large numbers of visual tokens. However, Table 3 compares MQuant (W4A8 static) against PyTorch BF16 and AWQ (W4 weight-only) — neither is a dynamic W4A8 baseline. Without measuring a per-token dynamic variant at the same W4A8 setting, the reader cannot attribute the speedup to static-vs-dynamic quantization versus other optimizations in the pipeline. This is the most direct test of the paper's central efficiency claim.

### Minor

3. **"First" language is overclaimed in parts of the paper, and inconsistently qualified.** The abstract and contribution list include "to the best of our knowledge, the first quantization solution for MLLMs" (lines 5, 35), which is appropriately qualified. However, the conclusion (line 450) states "the first accurate and efficient post-training quantization solution for multimodal large language models" *without* the qualifier, and contribution 1 claims "the first comprehensive analysis of quantization issues in MLLMs" (line 32) also without qualification. The qualifier should be applied consistently, and the "first comprehensive analysis" claim should be softened to avoid overreach — the community may have prior empirical observations about these challenges, even if no full PTQ solution existed.

4. **Benchmark coverage is limited to OCR and one general QA benchmark.** The evaluation uses TextVQA, DocVQA, OCRBench (all OCR-heavy), and MME (perception + cognition). No standard VQA benchmarks (e.g., VQAv2, GQA) or hallucination-focused evaluations (POPE) are included. This narrows the generality claim, especially since vision-language reasoning beyond OCR is a core use case for MLLMs.

5. **RMS theoretical analysis is a heuristic statistical argument, not a rigorous proof.** Section 4.3 assumes i.i.d. normally distributed weights and uses the expected maximum (σ√(2 ln n)) to characterize the other channels. The paper acknowledges this with "assuming" language, which is appropriate, but the framing ("revealed the root issues through theoretical analysis") overstates the rigor. This does not diminish the empirical effectiveness of RMS (Table 5 is clear), but the theoretical language should be softened to "statistical argument" or "empirically motivated heuristic."

6. **Ablation baseline is a non-standard configuration.** Table 5 starts from a "Static" baseline described as "GPTQ with online Hadamard transformation." GPTQ is a weight-only method, so the activations and the interaction between weight quantization and Hadamard rotation in this baseline are unclear. Starting from a cleaner baseline (e.g., RTN with per-tensor static weight+activation quantization) would better isolate each component's contribution.

### Trivial

7. **No variance or confidence intervals reported.** Only single numbers are reported across all tables. Given the calibration set size (256 samples), reporting variance across multiple calibration draws would strengthen reproducibility.

8. **Table numbering inconsistency.** The text references "Table 10" for the speedup/memory results (lines 180, 350), but the table caption reads "Table 3" (line 407). While likely a parser artifact, this should be corrected.

## Nice-to-Haves

- A comparison against a dynamic per-token W4A8 variant in the speedup table would directly test the central efficiency claim.
- A broader set of benchmarks (VQAv2, GQA, POPE) would strengthen the generality claim.
- Quantifying the overhead of RMS (fraction of layer time added by separating the first channel and running a separate GEMV) would address the "minimal overhead" claim with concrete numbers.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"First quantization solution" as an unsubstantiated claim** — The reviewer stated this claim lacks evidence and the paper's literature review does not establish the gap. However, the paper includes "to the best of our knowledge" qualifiers in the abstract and contributions, and the related work section explicitly states "dedicated quantization methods for MLLMs... remain under-explored" (line 42). The claim is appropriately qualified. The conclusion drops the qualifier (point 3 in Minor Weaknesses above addresses this), but the core concern as originally framed is overstated.

2. **AIFS cannot handle multiple interleaved text-visual segments** — The reviewer suggested the token reordering assumes a single contiguous block of visual tokens and would break with multiple interleaved blocks. However, AIFS "rearranges the visual tokens to the front of the sequence and places the textual tokens at the end" (line 165) — this handles *any* number of interleaved blocks by moving all visual tokens to the front. The adjusted causal mask (Eq. 9) accounts for all visual-then-text relationships. The method explicitly applies "regardless of the input order" (line 165).

3. **Missing related works (OmniQuant, AffineQuant)** — The paper mentions OmniQuant (line 43: "OmniQuant (Shao et al., 2023) optimizes performance by training quantization parameters"). Beyond this, the instruction explicitly prohibits faulting papers for missing related works since external sources cannot be verified.

4. **Missing appendix/proofs** — The instruction states appendix content is stripped by the parser; these exist in the original submission.

5. **Pure formatting/style nitpicks** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same strengths and weaknesses. The most notable observation not fully developed in either review is that the paper's three contributions (MSQ+AIFS, LN→RMSNorm, RMS) are modular and independently ablated, which is good scientific practice but also means the paper is best viewed as a combination of three fairly simple ideas that together solve a practical problem, rather than a single breakthrough. The Harsh Critic's observation about the non-standard memory savings formula is the single most actionable novel finding for the authors.

## Suggestions

1. **Clarify the memory savings formula.** State explicitly whether you report (baseline − ours)/baseline × 100% or (baseline − ours)/ours × 100%, and better yet, provide raw memory usage in GB alongside the percentages. The quantitative claims are still strong under standard reporting conventions — choose that convention.

2. **Add a dynamic per-token W4A8 baseline to the speedup table** (Table 3/Table 10). Run Quarot or your own method with dynamic per-token activation quantization at W4A8 and compare latency directly. This is the most direct test of your core efficiency claim.

3. **Use the qualifier "to the best of our knowledge" consistently** every time "first" appears in connection with MQuant. Soften "first comprehensive analysis" to a more precise description of what the paper contributes.

4. **In the ablation (Table 5), include a cleaner starting baseline** — RTN with static per-tensor weight+activation quantization (no GPTQ). This would make the incremental gains of each component easier to interpret.

5. **Report raw memory numbers** (e.g., peak memory in GB) alongside the derived savings percentages.

6. **Expand the benchmark set** in a revision to include at least one non-OCR visual reasoning benchmark (VQAv2 or GQA) to demonstrate generality beyond document understanding.

7. **Ensure all claims about theoretical analysis use measured language** ("statistical argument suggests" rather than "revealed the root issues").
