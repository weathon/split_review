- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 8, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes STBLLM, a post-training framework for LLM compression that pushes below 1-bit precision by combining N:M structured sparsity with binarization. The contributions are: (1) a Standardized Importance (SI) metric for gradient-free pruning, (2) adaptive layer-wise N:M ratio assignment based on per-layer L2-norm importance, (3) a three-region (sparse/intermediate/dense) non-salient quantization via trisection search, and (4) a specialized CUDA kernel leveraging 2:4 sparse tensor cores. Experiments span LLaMA-1/2/3, OPT, and Mistral families. The headline result: STBLLM achieves perplexity 31.72 at 0.55 bits on LLaMA-1-7B while BiLLM at the same N:M setting yields 688.73.

## Strengths

1. **First demonstration of structured binarization below 1-bit in LLMs, with large verified perplexity improvements**: Figure 2 and Table 2 show STBLLM at 0.55 bits achieves 31.72 perplexity on LLaMA-1-7B Wikitext2, compared to BiLLM's 688.73 at the same 4:8 setting — a >20× improvement. The paper is honest about the bit-width accounting, including the 2-bit group-identification overhead. This is, to the best of the evidence available, the first method to push structured LLM binarization substantially below the 1-bit threshold with non-trivial performance.

2. **Each component is individually validated through controlled ablations**: Table 5 shows SI (27.21) outperforms Magnitude (29.18), Wanda (28.11), and SparseGPT (27.71) within the same STBLLM framework on LLaMA-1-7B 4:8. Table 6 shows adaptive layer-wise assignment (27.21) beats Uniform (29.30) and Sin-shaped (28.80). Table 8 shows the three-region non-salient quantization (9.49) outperforms BiLLM's bell-shaped split (12.34) on LLaMA-2-7B. These ablations establish the individual contribution of each proposed technique.

3. **Extensive evaluation across model families and sizes**: Results cover LLaMA-1 (7B–65B), LLaMA-2 (7B–70B), LLaMA-3 (8B), OPT (1.3B–30B), and Mistral-7B, with consistent trends across all architectures. Zero-shot evaluations across 7 tasks on LLaMA-1-30B (Table 4) confirm that STBLLM at 0.55 bits (51.78%) substantially outperforms BiLLM (43.72%) in task accuracy, not just perplexity.

4. **Efficient post-training pipeline without fine-tuning**: The process takes 1.8 hours for a 7B model and 2.8 hours for 13B on a single GPU, making it practical relative to QAT-based approaches.

## Weaknesses

### Fatal
None.

### Major
- **Hardware speedup comparison lacks appropriate baselines**: The paper reports a 17.85× speedup over ABQ-LLM's 2-bit dense kernel (Section 4.3). This comparison conflates two advantages: lower bit-width (1-bit vs 2-bit) and structural sparsity (2:4 vs dense). The paper does not compare against a 1-bit dense kernel (e.g., BiLLM's own kernel) or a 2-bit 2:4 sparse baseline, so the speedup cannot be attributed to the specific contribution of structural binarization. The reported 79.74% of RTX4090 2:4 sparse tensor core peak utilization is useful as an absolute measure, but the headline speedup claim is inflated by comparing against a strictly slower baseline.

### Minor

1. **The BiLLM baseline comparison confounds the pruning metric with the framework — but the confound is largely bounded by the ablation data**: The BiLLM N:M baseline uses Wanda for pruning (stated on line 138), while STBLLM uses SI. The critic's concern that "gains could come from the metric alone" is the right instinct, but when cross-referenced with Table 5, it is clear the confound is bounded: Wanda within the STBLLM framework achieves 28.11 perplexity on LLaMA-1-7B 4:8 (vs SI's 27.21), while BiLLM (with Wanda) at the same setting yields 688.73. The ~0.9 perplexity gap from the metric is trivial compared to the ~660 perplexity gap from the framework. Nevertheless, a direct BiLLM+SI baseline in Tables 2/3 would have been the cleanest experimental design and would preempt this concern entirely. The current cross-table inference is unnecessary work for the reader.

2. **The adaptive layer-wise assignment uses L2-norm of weights as a proxy for layer importance without empirical validation that this correlates with pruning sensitivity**: The formula α_i = ω_i / ω_total is a crude heuristic. The ablation (Table 6) only compares against Uniform and Sin-shaped allocations — not against other principled layer importance measures (e.g., per-layer perplexity impact, Hessian trace). While the results show the heuristic works, its external validity (e.g., whether it generalizes to other model families or compression ratios) is not established.

3. **Perplexity results are only reported on Wikitext2 in the main tables**: The paper mentions C4 and PTB as evaluation datasets (line 136), but Tables 2 and 3 report only Wikitext2 perplexity. Table 7 (which compares metrics across multiple datasets) may address this, but its image is not visible in the text extraction. Including C4 results directly in the main comparison tables would strengthen robustness claims.

### Trivial
- No Algorithm 2 pseudocode is present in the extracted text (presumably deferred to an appendix stripped by the PDF parser). The trisection search procedure is described verbally but could benefit from a clear step-by-step in the main paper.
- The paper uses "GTPQ" (line 138) — presumably a typo for "GPTQ."

## Nice-to-Haves
- Provide a breakdown of computational overhead for the SI metric and trisection search (calibration data requirements, wall-clock time per component).
- Compare the three-region non-salient quantization against a two-region split at the same effective bit-width (controlling for the 2-bit group identification overhead) to verify Pareto-superiority.
- Discuss failure cases or model scales where the method degrades more rapidly (e.g., does sub-1-bit compression work equally well on smaller models like OPT-1.3B vs larger ones? The data suggests yes, but a targeted discussion would help).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Construction of N:M BiLLM baseline is unclear (methodological gap)"** — The paper states (line 138): "We perform an N:M sparse pattern on pre-trained LLMs and then conduct the same procedure as BiLLM to report the results." This is unambiguous: pruning first (using Wanda), then BiLLM binarization. The critic's speculation about saliency distribution interactions between pruning order and binarization is not grounded in any evidence from the paper and does not rise to a verifiable flaw.

- **"Three-region quantization adds 2 bits... should explicitly compute effective bit-width"** — The paper already computes this at line 114 ("introduces an additional 2 bits for group identification") and line 116 (N_storing = 2 + 1/b_size). This concern is already addressed.

- **"Trisection search (Algorithm 2, not shown)"** — This is a parser artifact; the appendix is stripped from all papers.

- **"No discussion of computational overhead for SI or trisection search"** — The paper reports end-to-end runtime (1.8 hours for 7B, 2.8 hours for 13B). A component-level breakdown would be a nice-to-have, not a weakness.

- **"Limited discussion of limitations"** — The paper explicitly acknowledges not supporting MoE/Mamba models (line 181). Requesting a broader limitations discussion beyond the paper's stated scope is not a valid weakness.

- **The critic's claim that the pruning metric confound makes it "impossible to attribute the observed gains" and that "the headline claims... are all potentially inflated by this confound"** is factually contradicted by the paper's ablation data (Table 5: Wanda within STBLLM achieves 28.11 vs BiLLM's 688.73 — a ~660-point gap that cannot be explained by the metric). The confound exists but is bounded and minor relative to the total effect. This assertion is removed as factually overblown.

## Novel Insights

None beyond the paper's own contributions. The reviews add useful scrutiny of the experimental design but do not identify an entirely new perspective on the work.

## Suggestions

1. **Add BiLLM+SI as a baseline** in Tables 2 and 3. This single change would cleanly separate the effect of the SI metric from the effect of the STBLLM framework (adaptive allocation + three-region quantization). The data in Table 5 suggests the gap will be small, but making this explicit would preempt the primary reviewer concern and strengthen the paper considerably.

2. **Recalibrate the hardware evaluation**: Add comparisons against (a) a 1-bit dense kernel (e.g., BiLLM's) and (b) a 2-bit 2:4 sparse kernel. Phrase the 17.85× figure as "speedup over a 2-bit dense implementation" rather than the unqualified "speedup over ABQ-LLM."

3. **Validate the L2-norm-based layer importance heuristic** by correlating it with an oracle measure (e.g., per-layer perplexity degradation when that layer is fully binarized) or by comparing against a more principled alternative.

4. **Report C4 perplexity** alongside Wikitext2 in the main tables (Tables 2 and 3) to demonstrate that results are not dataset-specific.
