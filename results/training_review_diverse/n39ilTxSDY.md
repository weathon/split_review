Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes Ditto, a framework for quantization-aware secure inference of Transformer models using secure multi-party computation (MPC). The key technical contributions are: (1) incorporation of MPC-friendly static dyadic quantization with layer-wise precision and quantization-aware distillation to maintain model utility, (2) novel MPC primitives (UpCast and DownCast) for type conversions between different rings that are essential in mixed-precision quantized inference, and (3) integration into a compiler with dynamic ring support and automatic type conversion. Empirical results on BERT and GPT2 models show 3.14–4.40× speedup over MPCFormer and 1.44–2.35× over PUMA with negligible accuracy degradation on GLUE benchmarks and Wikitext-103.

## Strengths

1. **Novel UpCast protocol enabling mixed-precision secure inference.** The UpCast protocol (Algorithm 1) converts shares between rings of different sizes (e.g., ℤ₂³² → ℤ₂⁶⁴) with only 3ℓ+ℓ′ bits of communication in 3 rounds. This primitive is essential for supporting the layer-wise fixed-point quantization that the framework relies on and fills a genuine gap identified in prior work (Section 4.2.1).

2. **Significant and well-measured empirical speedups.** In both LAN and WAN settings (Figure 3), Ditto achieves 3.14–4.40× faster runtime than MPCFormer and 1.44–2.35× faster than PUMA across BERT-base, BERT-large, GPT2-base, and GPT2-medium. These gains are substantial and clearly documented.

3. **Negligible utility degradation with evidence of careful design.** On GLUE benchmarks (Table 1), Ditto with Quad approximation maintains accuracy within ±0.5 points of the full-precision baseline for most tasks, and perplexity on Wikitext-103 degrades by less than 1 point. The quantization-aware distillation using layer-wise MSE loss is a sensible design choice that demonstrably recovers accuracy.

4. **Ablation studies cleanly isolate sources of improvement.** Table 3 separates the effect of quantization alone (1.41–1.56× speedup) from the combined effect of quantization + GeLU approximation (1.74–2.09×), showing that quantization is the primary driver of efficiency gains.

## Weaknesses

### Fatal
None.

### Major

1. **The UpCast protocol's range assumption lacks validation.** The core UpCast protocol relies on a "positive heuristic trick" (lines 261–264): it assumes the input value x lies in the range [−2^(ℓ−2), 2^(ℓ−2)−1], i.e., half the signed ring range. The paper explicitly states this as a "heuristic" and says "supposing" the condition holds. **However, the paper provides no analysis, proof, or empirical validation** that intermediate values in the quantized pipeline actually satisfy this constraint. While the accuracy results in Table 1 implicitly suggest the protocol works correctly (otherwise accuracy would degrade), the paper should either: (a) prove that the range condition is always satisfied given the quantization choices (FXP32^8 with layer-wise normalization), or (b) provide explicit empirical validation by measuring the distribution of values entering each UpCast operation across all layers and inputs. This is the most significant gap in an otherwise well-executed paper.

### Minor

2. **Distillation setup is under-specified.** The quantization-aware distillation is described only as using layer-wise MSE loss (line 196). No hyperparameters (learning rate, batch size, number of epochs, optimizer, dataset used for distillation, temperature if applicable) are provided. This affects reproducibility, though the distillation procedure itself is standard and the results demonstrate its effectiveness.

3. **Compiler overhead and dynamic ring support are not evaluated.** The paper describes dynamic ring support and automatic type conversion in the compiler (Section 4.3.2) but reports no measurements of their overhead (e.g., cost of dispatching between rings, tracking types). Given that the paper's focus is end-to-end efficiency, showing that this overhead is negligible would strengthen the contribution.

4. **Speedup comparison against PUMA conflates two sources of gain.** The headline speedup over PUMA (1.44–2.35×) combines the effects of quantization and the cheaper Quad GeLU approximation, since PUMA uses a more accurate (and more expensive) Poly approximation. The ablation study (Table 3) partially addresses this, but the paper's main efficiency figure and narrative could more clearly distinguish the two sources.

### Trivial
None.

## Nice-to-Haves
- A breakdown of communication overhead (what fraction goes to type conversion vs. matrix multiplication vs. non-linear functions) would strengthen the efficiency analysis.
- Discussion of scalability to deeper/wider transformers (e.g., would the range assumption in UpCast become a concern with deeper layers?).
- The paper frames itself as "the first framework that supports MPC execution of quantization-aware secure inference" — this is defensible but could be more precise by highlighting that the novelty is specifically in supporting **mixed-precision type conversions** for quantization-aware inference, since SecureQ8 also performed int8 quantization.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"The paper does not treat the UpCast range assumption as a heuristic"**: The paper explicitly says "positive heuristic trick" and "supposing" (lines 260–264). The paper does acknowledge this is a heuristic. The valid concern is about *validation*, not about acknowledgment.
- **"Security implications of the upcast heuristic could be exploited by adversary"**: The paper operates in the semi-honest honest-majority model (line 126), where parties follow the protocol. A correctness failure (wrong output due to violated assumption) is distinct from a security failure (privacy leakage). This concern conflates the two.
- **"Downcast is trivial"**: The paper correctly presents DownCast as a straightforward right-shift and modulo (line 207). This is not a weakness of the paper.
- **"Quad approximation is not novel"**: The paper attributes it to MPCFormer (line 180). The novelty is in the quantization-aware inference framework, not the approximation itself.
- **"Missing related works"**: Cannot be verified without external sources.

## Novel Insights
The most interesting observation from the reviews is that the UpCast protocol's range assumption, while presented as a "heuristic trick," is actually quite natural for quantized inference. The paper uses FXP32^8 (32-bit representation with 8 fractional bits), meaning the actual numeric values are bounded by roughly ±2^23. The assumption requires values to stay within half the signed range [−2^30, 2^30−1], which is dramatically looser than the actual quantization range. This suggests the heuristic is very likely safe in practice — but the paper should still validate this explicitly rather than leaving readers to infer it.

## Suggestions
1. **Validate the UpCast protocol's range assumption.** Add an experiment measuring the distribution of values entering each UpCast operation across all layers and model configurations, confirming they satisfy |x| ≤ 2^(ℓ−2). A brief analysis of why the quantized pipeline guarantees this bound (due to fixed-point arithmetic with truncation after each multiplication and the bounded nature of normalized Transformer activations) would also be valuable.
2. **Provide distillation hyperparameters** (learning rate, batch size, optimizer, number of epochs, training dataset) in the final version.
3. **Include a brief evaluation of the compiler overhead** for dynamic ring support and automatic type conversions.
4. **Present the speedup sources more clearly** by explicitly separating the quantization-only comparison (Ditto_w/o{a} vs. PUMA with equivalent non-linear functions) from the combined effect.

## Score and Decision
The paper addresses a real and important problem — bridging ML quantization with MPC for secure Transformer inference — and proposes a practical solution with impressive empirical results. The main weakness is the lack of explicit validation of the UpCast protocol's range assumption, though the empirical accuracy results provide implicit validation and the paper does acknowledge the heuristic nature. With the suggested revisions (particularly validation of the range assumption and filling in reproducibility details), this would be a solid contribution to the field.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>