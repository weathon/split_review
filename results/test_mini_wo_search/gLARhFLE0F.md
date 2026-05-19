Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces LUT-GEMM, a GPU kernel for weight-only quantized matrix multiplication that operates directly on binary-coding quantized (BCQ) weights using lookup tables, thereby avoiding the dequantization step required by prior methods such as OPTQ and AWQ. The authors extend BCQ with a bias term to support both non-uniform and uniform quantization formats, and validate the kernel's efficiency through kernel-level and end-to-end latency measurements, showing 2.1× speedup over OPTQ for 3-bit OPT-175B on a single GPU.

## Strengths

- **Eliminates dequantization overhead with measured speedup.** Table 1 shows LUT-GEMM (INT3*) at 0.225 ms vs. OPTQ (INT3) at 0.359 ms for the same FFN layer (1.6× kernel speedup). Table 4 extends this end-to-end: 51.6 ms per token vs. OPTQ's 106.5 ms for OPT-175B 3-bit (2.1× improvement), with the gap attributable to the elimination of on-the-fly dequantization.

- **Extended BCQ format broadens applicability.** Section 3.3 introduces a bias term (Equation 5) enabling the BCQ representation to cover both non-uniform quantization (multiple scaling factors) and uniform quantization (single scale with zero-point). Figure 3 illustrates both cases, and Tables 5–6 demonstrate compatibility with OPTQ and AWQ quantization pipelines.

- **Well-supported latency–accuracy trade-off via group-wise quantization.** Section 3.4 and Figure 4 show that group size \(g\) can be varied independently of bit-width \(q\), and the paper establishes that latency scales with memory footprint (Equation 6). Table 5 concretely illustrates this trade-off for OPT-175B across different \((q,g)\) configurations.

- **Reduces GPU count for large-model inference.** Table 2 shows LUT-GEMM (q=2) on one GPU achieving 4.85× speedup over FP16 cuBLAS on one GPU while cutting total energy to 0.27×. Table 4 demonstrates that OPT-175B, which requires 8 GPUs in FP16, can run on a single GPU with LUT-GEMM 3-bit while delivering comparable latency (51.6 ms vs. 42.4 ms for 8-GPU FP16), eliminating inter-GPU communication overhead.

## Weaknesses

### Fatal

None.

### Major

- **Missing experimental validation that BCQ-converted uniform weights reproduce the original outputs.** The paper claims LUT-GEMM can execute uniform quantization (AWQ, OPTQ) via the extended BCQ format, but provides zero experimental evidence that the BCQ representation yields identical numerical outputs. All perplexity numbers in Table 3 (LLaMA with AWQ) and Table 6 (OPT-175B with OPTQ) are cited from prior work, not measured using LUT-GEMM. Table 3's caption does not clarify the source of the perplexity values. Without a direct comparison (e.g., logit difference or perplexity measured end-to-end on the LUT-GEMM kernel), the claim of generality to uniform quantization is unsubstantiated. This gap affects Contribution 1 ("verify that BCQ is capable of representing both uniform and non-uniform weight quantization").

### Minor

- **Conversion from uniform quantization to extended BCQ is not described.** The paper states that uniform quantization can be reformulated as BCQ (Section 3.3, Figure 3) but provides no algorithm or pseudocode for converting integer weights (with scale and zero-point) into the form \(\hat{w} = \sum_i \alpha_i b_i + z\). The mapping is mathematically straightforward but the absence of any description — even a brief sketch — hurts reproducibility, especially for practitioners wishing to apply LUT-GEMM to pre-quantized checkpoints.

- **Key kernel hyperparameters not reported for experiments.** The paper specifies \(t_h = 2048\) as "a practical number for large-scale LMs" (Section 3.2) and \(\mu = 8\) in the illustrative example (Figure 2 caption), but does not state the actual \(\mu\) and \(t_h\) values used in the latency measurements of Tables 1, 4, and 5. Since these parameters directly affect LUT construction cost and parallelism, their absence makes it hard to assess whether the reported configurations are near-optimal.

- **Batch-size sensitivity is acknowledged but not quantified.** The Limitations section (Section 6) correctly notes that performance degrades as batch size increases due to LUT construction overhead and shared-memory bandwidth, but no data is provided (e.g., a plot of latency vs. batch size 1, 2, 4, 8). This limits the reader's ability to assess the method's practical scope.

### Trivial

None.

## Nice-to-Haves

- A logit-difference or per-layer output comparison between LUT-GEMM (with BCQ-converted weights) and standard dequantization+GEMM for at least one uniform quantization method (e.g., AWQ 4-bit) would fully close the evidential gap identified above.
- A brief algorithmic description or pseudocode for converting uniform integer weights into the extended BCQ representation would strengthen reproducibility.
- A sensitivity plot showing latency vs. \(\mu\) and/or \(t_h\) for a representative layer would help validate the empirical choices.
- Quantifying the latency breakdown between LUT building and LUT reading (e.g., via a microbenchmark) would clarify where the method's bottlenecks lie.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Baseline comparison may not reflect best-configuration (Marlin, unspecified kernel versions).** The critic speculates about "more recent GPU kernels (e.g., Marlin)" — these postdate the paper's likely submission window. The paper does specify precision, group size, and GPU model for baselines (Table 1 caption). Without evidence of a specific misconfiguration, this is speculation.

- **Energy claim extrapolated from one layer.** The critic claims "total system energy for end-to-end inference... is not measured." The paper's text and table caption clearly scope the claim to "energy consumption for matrix multiplications" (Table 2 and surrounding text), not total system energy. The measurements are appropriate for the stated scope.

- **INT8* row is confusing.** The footnote in Table 1 explains that "* LUT-GEMM supports both non-uniform and uniform quantization." The row demonstrates LUT-GEMM's flexibility across bit-widths. This is a valid data point, not a weakness.

- **Complexity vs. latency conflation.** Early framing uses computational complexity to motivate the approach, but the paper's primary evidence is measured latency (Tables 1, 4, 5). The Limitations section explicitly notes the memory-bound nature of single-batch operations. This is a presentational preference, not a flaw.

- **Missing comparison with FP16 tensor parallelism at comparable inference latency.** The paper already includes this comparison in Table 2 (cuBLAS-1 vs. cuBLAS-8 vs. LUT-GEMM). The critic's proposed "cleaner" experiment (LUT-GEMM 1 GPU vs. cuBLAS 1 GPU) is impossible because the model does not fit, as the paper explicitly states.

- **Table 6 PPL cited from OPTQ.** The paper is transparent about this (footnote in Table 6: "PPL numbers are extracted from the OPTQ reference"). This is not a weakness.

## Novel Insights

The most insightful observation arising from this review is that the paper's core contribution (LUT-GEMM's acceleration from avoiding dequantization) is separable from its secondary contribution (generalizing BCQ to uniform quantization). The speedup results are strong and well-supported; the generality claim is mathematically sound but lacks empirical backing. This separation means the paper's practical value does not hinge on the unvalidated claim, but the authors should clarify this boundary in future versions.

## Suggestions

1. **Validate numerical equivalence**: Add a simple experiment comparing output logits (or final-layer outputs) from LUT-GEMM running on BCQ-converted AWQ 4-bit weights against the original dequantization+GEMM pipeline. Show that the difference is within machine epsilon.
2. **Document the conversion algorithm**: Provide a short algorithmic description (2–5 lines of pseudocode) showing how to decompose a uniformly quantized integer weight tensor into the \((\{\alpha_i\}, \{b_i\}, z)\) representation.
3. **Report hyperparameters used in experiments**: State the \(\mu\) and \(t_h\) values for each latency experiment in Tables 1, 4, and 5.
4. **Quantify batch-size sensitivity**: Add a figure or table showing LUT-GEMM latency at batch sizes 1, 2, 4, 8 for a representative model to delineate the method's regime of applicability.
5. **Clarify PPL sources in Table 3**: Add a footnote to Table 3 explicitly stating whether the perplexity values were measured using LUT-GEMM or reproduced from the AWQ reference, consistent with the practice in Table 6.

## Score and Decision

The paper presents a genuinely efficient kernel with well-measured speedups. The core contribution — accelerating weight-only quantized inference by avoiding dequantization with LUTs — is solid and empirically validated. The two main weaknesses (missing numerical equivalence validation for uniform-quantization support, and missing hyperparameter documentation) are real but fixable and do not invalidate the primary results.

**Evaluation across key axes**:
- **Originality**: Good — applying LUTs to avoid dequantization in LLM inference is a clever and practical idea.
- **Importance of research question**: High — efficient LLM inference is a critical problem.
- **Claims supported**: Partially — the latency speedup claims are well-supported; the uniform-quantization generality claim is mathematically reasoned but not empirically validated.
- **Soundness of experiments**: Solid for latency; incomplete for numerical accuracy of the uniform-quantization conversion.
- **Clarity of writing**: Generally clear; the missing conversion algorithm and ambiguous PPL sourcing in Table 3 are the main gaps.
- **Value to the community**: High — the kernel and the idea of LUT-based quantized multiplication are practical contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>