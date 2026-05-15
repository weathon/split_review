Now I have all the information needed. Let me produce the authoritative final review.

## Summary

This paper proposes LeanQuant, a post-training quantization method that replaces the standard min-max affine grid in GPTQ/OBQ-style iterative quantization with "loss-error-aware" grids (both non-uniform via weighted k-means and affine via constrained search) to better preserve weights corresponding to inverse-Hessian-diagonal outliers. The method is evaluated across models from 7B to 405B parameters, demonstrating improved perplexity and zero-shot accuracy over GPTQ, AWQ, OmniQuant, and SqueezeLLM, while using substantially less GPU memory (e.g., 7.9 GB vs. 25.3 GB for Llama-3-8B) and scaling to Llama-3.1-405B on two 48 GB GPUs in ~21 hours.

## Strengths

- **Well-motivated problem and insight.** The paper correctly identifies that min-max affine grids used by GPTQ/OBQ are suboptimal when inverse-Hessian diagonals contain outliers (Figure 1, left), and provides empirical evidence for this phenomenon on Llama-3-8B (Section 3.1). This diagnosis is a distinct conceptual contribution.

- **Scalability demonstration is concrete and impressive.** Quantizing Llama-3.1-405B on two 48 GB GPUs in 21 hours, and Mistral-Large 123B on a single 48 GB GPU in 4.2 hours (Section 4.2, Tables 6–7), is a genuine engineering achievement that goes beyond what existing competitive methods (OmniQuant, SqueezeLLM) can do without OOM errors.

- **Fused GPU kernel for affine grid search.** The >50× speedup from the fused kernel (Table 8) is a practical contribution that makes the method tractable at scale and is well documented with timing comparisons.

- **Memory efficiency is clearly demonstrated.** LeanQuant uses 7.9 GB for Llama-3-8B vs. 25.3 GB for OmniQuant, and avoids the OOM failures of both OmniQuant and SqueezeLLM on larger models (Table 6). This advantage is quantified across multiple model scales.

- **Versatility across quantization formats.** The method is validated for both affine and non-uniform formats and the paper explicitly notes compatibility with existing inference kernels (Marlin, LUT-GEMM), supporting the claim of practical deployability.

## Weaknesses

### Fatal

None.

### Major

- **The objective function discrepancy weakens the core motivational claim.** The paper states (line 125) "Our idea is to learn quantization grids that minimize the loss error ε." Directly minimizing ε_i corresponds to the objective with p=1 (since ε_i ∝ (quant(w_i)−w_i)² / H^{-1}_{i,i}). However, the actual objective (Eq. 4, Eq. 5) uses p=4, which minimizes a different weighted reconstruction error. The paper explains p as controlling "the strength of preserving the quantized precision of outliers" (lines 162, 138), which is a reasonable design choice, but the framing conflates "loss-error-aware" with "inverse-Hessian-weighted with an ad-hoc exponent." The claimed causal chain — loss error → inverse Hessian diagonals → weighted k-means with exponent 4 — has a gap at the p=4 step that is not justified. The sensitivity analysis only checks p∈{3,4} (Section 4.3, Q2), which is insufficient to establish that p=1 (the direct ε-minimizer) is worse, or to explain why p=4 is the correct choice. This does not invalidate the method (p=4 could still produce good grids for other reasons), but it weakens the paper's central narrative.

- **The ablation study is incomplete in key respects.** (a) Q3 is entirely absent from the extracted text — whether due to parser stripping or author omission, the reader cannot evaluate it. (b) Q1 is answered only through a figure (Figure 3) and a one-sentence statement about "sum of loss errors" (line 266), without numeric summaries (mean, max, per-layer breakdown) that would allow quantitative comparison. (c) There is no ablation that isolates the grid-learning component from the GPTQ backbone: a direct comparison of GPTQ (min-max affine) vs. LeanQuant with standard affine grid (no learning) vs. LeanQuant with learned grid, all else equal. Without this, the reported accuracy gains cannot be cleanly attributed to the grid learning rather than other incidental differences (calibration data, Hessian dampening, etc.). For a method whose novelty rests entirely on the grid-learning component, this evidential gap is significant.

- **The reported zero-shot accuracy improvements at 3-bit are exceptionally large and lack statistical context.** The paper claims absolute improvements of 17.18% over OmniQuant and 18.38% over GPTQ for 3-bit Llama-3-8B, and 14.14%/9.16% for 3-bit Mistral-7B. These are very large for a PTQ method. No standard deviations, confidence intervals, or per-task breakdowns are provided to contextualize these numbers (the main accuracy table was input from a separate file and is not visible in the extracted text — this is a parser artifact, not an author error, but the textual claims themselves lack statistical support). While single-run evaluation is common in the quantization literature, the magnitude of these claims demands more rigorous validation.

### Minor

- **The affine grid search space is unnecessarily constrained.** The search space S (Eq. 5) only considers shrinking the min-max range symmetrically inward (t_min, t_max ∈ [0, T/2−1]), which excludes grids that expand the range or shift the interval asymmetrically. The paper provides no justification for this restriction. While shrinking the range can put more grid points in dense weight regions, the optimal affine grid for loss-error minimization might lie outside this space.

- **The choice p=4 needs a broader sweep.** The sensitivity analysis only checks p∈{3,4} and concludes the method is "not very sensitive." A sweep over p∈{0,1,2,3,4,5} with both loss-error and accuracy metrics would be more informative, particularly to show whether p=1 (direct ε minimization) produces worse results and why.

- **Lack of per-task breakdown for the largest models.** For Llama-3.1-405B, only 4 tasks are reported (Table 9), and for Mistral-Large-123B, the gains are small (0.33% average improvement over GPTQ). The paper's strongest claims come from smaller models at 3-bit, but the larger-model results show more modest gains. A per-task breakdown for the 3-bit results would help assess whether gains are concentrated in certain tasks.

### Trivial

None that survive filtering — the parser-stripped tables and formatting artifacts are not author errors.

## Nice-to-Haves

- Inference latency/throughput benchmarks using existing kernels (Marlin, LUT-GEMM) in a framework like llama.cpp or vLLM would strengthen the practical deployment claim, though this is outside the paper's stated scope.
- Reporting the distribution of loss errors (mean, max, sum per layer) numerically in addition to Figure 3 would make the ablation more actionable.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Criticism about missing latency benchmarks / deployment experiments (Harsh Critic, Introduction ¶2 on kernels).** The paper explicitly scopes itself as a quantization *accuracy* method that achieves compatibility with existing kernels — demanding latency benchmarks is scope creep. The contribution is the grid-learning method, not inference framework benchmarking.

- **Criticism about missing experimental configuration details for baseline peak memory (Harsh Critic, Memory and Time Efficiency).** The group size and calibration data size are standard and well-known for these baselines; this is a nitpick without substantive impact.

- **Criticism about the main results table being absent (Harsh Critic, Section 4.1).** The table was input via \input{tables/accu} and stripped by the parser — this is a tool limitation, not an author omission.

- **"Rigorous ablation studies" (Strength Finder).** This strength overstates the evidence. As noted in Major weaknesses, the ablation study has significant gaps (missing Q3, no grid-type vs. GPTQ isolation). Dropped because it conflicts with verified weaknesses.

- **"Consistent accuracy improvements" / "direct evidence for accurate claim" (Strength Finder).** The Strength Finder claims these improvements are "presented in Table 1" — but Table 1 is in the stripped input file and cannot be verified. The textual claims are large and lack statistical context. Weakened to the verified weaker form above.

## Novel Insights

The reviewers' critiques cluster around a common theme: the paper's empirical claims outpace its evidential support. The most interesting tension is between the paper's framing ("loss-error-aware grids minimize ε") and the actual objective (p=4, which is a heuristic weighting that over-emphasizes outliers beyond what ε minimization would dictate). This suggests the method's success may stem less from theoretically minimizing ε and more from robustly clustering grid points around outlier weights — a distinction the paper does not explore. The scalability results (405B on 2×48 GB GPUs) are impressive but are for 4-bit, where the accuracy gains over GPTQ are modest (0.47% on the 405B), raising the question of whether the main value is accuracy at ultra-low bits on smaller models or memory efficiency at 4-bit on very large models. These are different contributions with different evidentiary requirements.

## Suggestions

1. **Address the p-exponent issue directly.** Add an ablation sweeping p ∈ {0,1,2,3,4,5} with both loss-error and accuracy metrics. Show whether p=1 (direct ε minimization) underperforms p=4, and discuss why. This either justifies the design choice or reveals the method works for different reasons than claimed — either outcome improves the paper.

2. **Add an ablation isolating the grid learning.** Compare: (a) GPTQ with min-max affine grid, (b) LeanQuant-aff with min-max affine grid (i.e., no grid learning), (c) LeanQuant-aff with learned grid — all else equal (same calibration data, dampening, block size). This pins the gains to the grid component.

3. **Provide variance or per-task breakdowns for the 3-bit results.** At minimum, report per-task accuracy for each benchmark so the reader can assess whether gains are concentrated or broad. Repeating 2–3 runs with different calibration subsets for one setting (e.g., 3-bit Llama-3-8B) would strengthen credibility.

4. **Broaden the affine search space justification or relax the constraint.** Either prove that the optimal solution lies within the shrunken-range space, or open the space to include range expansion and asymmetric shifts.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>