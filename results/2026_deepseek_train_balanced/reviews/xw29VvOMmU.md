## Summary

This paper proposes LQ-LoRA, which decomposes each pretrained weight matrix into a quantized component (fixed during finetuning) and a low-rank component (updated during finetuning), using an iterative algorithm that alternates between truncated SVD and NF quantization. The method also uses an integer linear program (ILP) to assign mixed quantization configurations across layers given a target memory budget, and explores a Fisher-weighted variant of the decomposition. Experiments on RoBERTa-Large, LLaMA-2-7B, and LLaMA-2-70B show that LQ-LoRA outperforms QLoRA and GPTQ-LoRA baselines at aggressive quantization levels (sub-3 bits).

## Strengths

- **Well-motivated core idea (Section 3.1, Algorithm 1, Eqs. 3–6):** The paper identifies a genuine limitation of zero-initialized LoRA when applied to heavily quantized models — the quantization error at initialization means the model output at step 0 is already different from the pretrained output. The iterative low-rank plus quantized decomposition provides a principled fix. Figure 1 provides clear evidence that the algorithm converges quickly and reduces reconstruction error across all layers of LLaMA-2-7B compared to vanilla NF-3 quantization.

- **ILP-based mixed-configuration quantization (Section 3.2, Eqs. 7–8, Table 2):** The paper formalizes per-matrix assignment of quantization parameters as an integer linear program with a target memory budget constraint, enabling a mixed-precision strategy that uniform quantization cannot discover. The empirical results (Table 2 — GLUE with RoBERTa-Large) show that the combination of LQ decomposition + ILP mixed quantization substantially outperforms QLoRA at similar bit budgets (e.g., 87.3 vs 85.5 at 3.0 bits, and 85.7 vs 75.4 at 2.5 bits). Figure 5 further confirms that the ILP allocates bits differently across layers, showing non-trivial decisions.

- **Honest and thorough limitations discussion (Section 6):** The paper explicitly acknowledges several negative results and limitations: the ILP only minimizes reconstruction error rather than downstream performance, the iterative algorithm is heuristic, periodic refactorization did not help, and hybrid initialization also did not help. This transparency strengthens the paper's credibility.

- **Scalability demonstration (Section 4):** The paper shows LQ-LoRA working on LLaMA-2-70B, compressing it to ~2.85 effective bits (27 GB for the model) and fitting forward/backward passes on a single 80 GB GPU. This demonstrates the method's practical viability at the largest commonly-used open LLM scale.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Fisher-weighted results on GLUE show an unexplained inconsistency:** On GLUE with RoBERTa-Large (Table 2), the Fisher-weighted variant underperforms the unweighted version at 2.75 bits (86.4 vs 87.1) and ties at 3.0 bits (87.3 vs 87.3), while outperforming at 2.5 and 3.25 bits. The paper notes "Fisher-weighted LQ-LoRA is especially effective at 2.5 bits" (line 245), which is accurate, but does not discuss why Fisher hurts at 2.75 bits or why the benefit is inconsistent across bit rates. Since the Fisher approximation is acknowledged to rely on a violated assumption ("the homogenous row/column assumption clearly does not hold for F"), the mixed results deserve a brief explanation or hypothesis.

- **The ILP's reconstruction-error objective is not validated against simpler alternatives:** The ILP minimizes Frobenius-norm reconstruction error of the decomposition, which is a proxy for downstream performance. The paper acknowledges this limitation in Section 6. However, there is no ablation comparing the ILP-chosen allocation against simple baselines (e.g., uniform allocation at the same average bit rate, or a heuristic like allocating more bits to matrices with larger spectral radius). Without such a comparison, it is difficult to assess whether the ILP's allocations are genuinely beneficial or whether any allocation at the same bit rate would perform similarly. Given that the ILP precomputation takes "a few hours when parallelized across four A100 GPUs for LLaMA-2-7B," validating its utility against cheaper alternatives would strengthen the contribution.

- **GLUE results reported only as a single average:** Table 2 reports only the aggregate GLUE score without per-task breakdowns. Since GLUE comprises diverse tasks (MNLI, QQP, SST-2, etc.), a per-task table would help assess whether LQ-LoRA's gains are uniform or concentrated on certain tasks. This is especially relevant for understanding the Fisher variant's behavior, which may help on some tasks and hurt on others.

- **Preprocessing cost not fully characterized:** The paper mentions that each SVD+quantization step takes "a few seconds on a modern GPU for a 4096×4096 matrix" and that the ILP error precomputation "takes a few hours when parallelized across four A100 GPUs for LLaMA-2-7B." However, the total wall-clock time for the full pipeline (decomposition of all matrices + ILP precomputation) for each model scale is not reported. For practitioners deciding whether the preprocessing overhead is worthwhile, this information would be useful.

### Trivial
None.

## Nice-to-Haves

- **Variance/confidence intervals:** The paper reports no variance across runs. For comparisons where scores are close (e.g., Fisher 87.3 vs non-Fisher 87.3 at 3.0 bits on GLUE), it is impossible to tell whether differences are meaningful. Reporting standard errors over 2–3 seeds for the main comparisons would increase confidence. This is noted as a nice-to-have rather than a weakness because single-run evaluation is standard practice in this line of work at these model scales.

- **Training-time memory breakdown:** Figure 6 shows storage breakdown but not the GPU memory used during finetuning (activations, gradients, optimizer states). A brief quantification would help readers understand the practical memory savings during training.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Issue 1 ("LQ decomposition and mixed quantization not cleanly disentangled"):** This is factually incorrect. The paper includes QLoRA with ILP in Table 2 (labeled "QLoRA (ILP)"), and the rank ablation in Section 5.3 (Table 4) fixes quantization to NF-3 (uniform), isolating the decomposition effect. Direct comparisons are present.

- **Harsh Critic Issue 3 partial claim ("'all target bit widths' contradicted by GLUE"):** The "all target bit widths" claim (line 243) refers to LLaMA-2 7B language modeling results, not to the RoBERTa GLUE results. These are different models and tasks, so there is no contradiction. The remaining sub-issue (Fisher's inconsistent behavior on GLUE not discussed) is retained above as a Minor weakness.

- **Strength Finder Strength 3 ("Fisher-weighted SVD" as a core strength):** Given the inconsistent results (Fisher underperforms on one of four GLUE settings and the approximation's key assumption is acknowledged to be violated), claiming this as a core strength overstates the evidence. Removed.

- **"GPTQ-LoRA excluded from instruction tuning"**: The paper explicitly notes this (line 198, footnote) and the baseline is included in the other two settings. Not a weakness.

- **"No variance" and "Memory breakdown"**: Demoted to Nice-to-Haves per the filtering rules — single-run reporting is standard for LLM finetuning at these scales.

- **Generic criticism about ILP minimizing reconstruction error**: The paper explicitly acknowledges this in Section 6. Retained as Minor only because the paper does not validate the ILP against simpler heuristics, not because the limitation exists in isolation.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation: the two components of LQ-LoRA (decomposition + mixed quantization) are somewhat independent innovations, and the paper's case would be stronger if it more explicitly separated them — not because the paper fails to do so (it does, through Table 2's QLoRA(ILP) rows and Table 4's fixed-config rank ablation), but because a single clean four-way table (QLoRA fixed, QLoRA+ILP, LQ-LoRA fixed, LQ-LoRA+ILP) would make the attribution of gains more transparent at a glance. The honest limitations discussion is a genuine strength that should be preserved in any revision.

## Suggestions

1. Add a brief discussion of the Fisher-weighted results on GLUE at 2.75 bits, hypothesizing why the weighted decomposition might hurt at certain bit rates.
2. Add a simple ablation comparing ILP-chosen allocations against uniform allocation at the same bit rate, or against a basic heuristic (e.g., allocate higher bits to matrices with larger spectral norms). This would validate whether the ILP's complexity is worthwhile.
3. Report per-task GLUE scores in an appendix table.
4. Include the total preprocessing wall-clock time for the complete pipeline (decomposition + ILP precomputation) for both 7B and 70B scales.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>