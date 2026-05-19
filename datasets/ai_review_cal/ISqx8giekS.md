- Decision: Accept
- Avg Score: 5.17
- Scores: 6, 6, 6, 3, 5, 5
Now I have a clear picture of the paper. Let me write the consolidated review.

## Summary

This paper proposes LeanQuant, a post-training quantization method for LLMs that replaces the standard min-max affine quantization grid with learned "loss-error-aware" grids. The key idea is to weight the quantization objective by $(H^{-1}_{i,i})^{-p}$, which gives higher importance to weights whose quantization errors cause large increases in task loss. The method supports both affine and non-uniform quantization formats, integrates into the GPTQ iterative framework, and includes a fused GPU kernel for efficient grid search. Experiments show competitive or improved perplexity/accuracy across models up to 405B parameters, with strong memory and time efficiency.

## Strengths

- **Loss-error-aware grid learning is a sound technical contribution with clear empirical support.** The paper proposes learning quantization grids (non-uniform via weighted k-means, affine via constrained search) that minimize the loss error $\epsilon$ directly, rather than using a fixed min-max grid. The objective $\sum_i (H^{-1}_{i,i})^{-p} |\text{quant}(w_i)-w_i|^2$ is mathematically principled — it correctly assigns higher weight to weights with small $H^{-1}_{i,i}$ (which are the sensitive ones per Eq.~4). The ablation in Figure~2 confirms that LeanQuant achieves lower layer-wise cumulative $\epsilon$ than GPTQ during iterative quantization.

- **Impressive scalability to 405B parameters on modest hardware.** The paper demonstrates quantization of Llama-3.1-405B-Instruct to 4.25 bits using only two 48GB GPUs in ~21 hours (Table~3, Table~4), and Mistral-Large-123B on a single 48GB GPU in 4.2 hours. Competitors (OmniQuant, SqueezeLLM) OOM on much smaller models (70B, 8B respectively). This is a genuine practical advantage.

- **Efficient fused GPU kernel for affine grid search.** The brute-force search over $(\frac{T}{2})^2 \approx 10^6$ candidates per group is parallelized via a custom kernel, achieving >50× speedup (Table~5: 15.1 hrs → 0.27 hrs for row-wise, >100 hrs → 0.40 hrs for group-wise). This makes the method practical for very large models.

- **Versatility across widely-supported quantization formats.** The method works with both affine and non-uniform formats, enabling compatibility with existing inference frameworks (llama.cpp, vLLM) without custom kernels. This is a well-motivated design choice.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguous framing of zero-shot accuracy improvements.** The paper states (Section~4.1) that LeanQuant$_{\text{aff}}$ improves average zero-shot accuracy "by 17.18%" for 3-bit Llama-3-8B and "by 14.14%" for 3-bit Mistral-7B over OmniQuant, with similar numbers vs. GPTQ. It is unclear whether these are absolute percentage points (e.g., 30% → 47.18%) or relative improvements. The magnitude is large in either case. The main accuracy table (\texttt{\textbackslash input\{tables/accu\}}) is missing from the parsed text, preventing verification against per-task numbers. The visible results on 123B and 405B models (Tables~1,~2) show much more modest gains (~0.3–0.5 absolute points at 4-bit). The paper should clarify the exact metric, provide the complete table, and explain the discrepancy between the large 3-bit gains on small models and the small 4-bit gains on large models. This is the most significant weakness — the headline numbers cannot be properly assessed as presented.

- **Missing ablation that isolates the grid contribution.** The ablation shows lower loss errors for LeanQuant (Figure~2), which is helpful. But there is no experiment that isolates the effect of the learned grid alone vs. GPTQ with a min-max grid while keeping all other Hessian-based weighting identical. The comparison of GPTQ (min-max grid) vs. LeanQuant (learned grid, same GPTQ update procedure) for the same model, reported in terms of perplexity/accuracy rather than just loss errors, would cleanly demonstrate the source of improvement.

### Minor

- **Inconsistent terminology in the motivation (Section~3.1/Figure~1).** The paper correctly states $\epsilon_i \propto 1/H^{-1}_{i,i}$ (Eq.~8) and says it examines the distribution of $1/\text{diag}(H^{-1})$ (line~125). However, the Figure~1 caption says "The empirical distributions of inverse Hessian diagonals" (which is $H^{-1}_{i,i}$, not $1/H^{-1}_{i,i}$), and the text later refers to "inverse-diagonal outliers" without distinguishing which quantity. The weighting scheme $(H^{-1}_{i,i})^{-p}$ is mathematically correct — it assigns higher weight to small $H^{-1}_{i,i}$ (sensitive weights). But the presentation muddles the logical flow: a reader could reasonably infer the paper is making the wrong claim. This does not invalidate the method (which is correctly derived), but the narrative should be cleaned up to avoid ambiguity.

- **No variance or multiple-run statistics.** Single-run results are reported without error bars. While common in LLM quantization papers, this is worth noting given the small calibration set (128 sequences).

- **Sensitivity analysis for $p$ is only briefly mentioned.** The paper states $p=4$ works well and the method is not very sensitive to $p$, but provides no sweep results (e.g., a table showing perplexity/accuracy for $p \in \{1,2,3,4,5\}$ for at least one model). This would be easy to add and would strengthen the paper.

### Trivial

- The Figure~1 caption refers to "grids better preserves" (subject-verb agreement).

## Nice-to-Haves

- An ablation comparing GPTQ + min-max grid (same Hessian, same updates) with GPTQ + learned grid, reporting perplexity/accuracy rather than just loss errors.
- Reporting the 3-bit zero-shot accuracy improvements as absolute percentage points alongside the relative percentages for clarity.

## Removed Points

- **"Fundamental misinterpretation of the loss-error formula" (Harsh Critic's Issue 1, rated as Fatal).** REMOVED as factually incorrect. The paper explicitly states it examines the distribution of $1/\text{diag}(H^{-1})$ (line~125), which is proportional to $\epsilon$. The weighting $(H^{-1}_{i,i})^{-p}$ correctly assigns higher weight to small $H^{-1}_{i,i}$ (sensitive weights). The figure caption uses imprecise terminology, but the mathematical reasoning and method are sound. I have downgraded this to a Minor presentation issue above.

- **"Implausible magnitude of accuracy improvements" framed as potentially invalidating the paper's core results.** WEAKENED. The critic's claim relies on not seeing the main table (parser artifact) and speculates about implausibility without evidence. The concern about relative vs. absolute percentages is valid and retained as Major; the speculation that the results "cannot be accepted at face value" is removed.

- **"Missing related works"** — not included per instructions.

- **"Missing appendix/proofs"** — parser artifact, removed per instructions.

- **"Code not provided"** — parser artifact (stripped), removed per instructions.

- **Strength claimed about "Identification of the root cause"** — generic/superficial, removed.

- **"Calibration data robustness" suggestion** — scope creep, removed.

- **Various formatting/style nitpicks** — removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already present or imply.

## Suggestions

1. **Clarify the accuracy improvement metric.** State explicitly whether the reported percentages (17.18%, 14.14%, etc.) are absolute percentage point differences or relative improvements. Provide the full accuracy table so readers can inspect per-task numbers.
2. **Fix the terminological inconsistency in Section~3.1.** Ensure the figure caption and surrounding text consistently describe whether Figure~1 shows $H^{-1}_{i,i}$ or $1/H^{-1}_{i,i}$, and make the logical chain from the formula to the histogram to the weighting scheme unambiguous.
3. **Add an ablation isolating the grid.** Compare GPTQ + min-max grid vs. GPTQ + learned grid (with identical Hessian computation and weight updates) on at least one model, reporting perplexity and accuracy.
4. **Provide a sensitivity sweep for $p$.** Show quantized perplexity/accuracy for $p \in \{0,1,2,3,4,5\}$ for at least one model to justify the default $p=4$.
