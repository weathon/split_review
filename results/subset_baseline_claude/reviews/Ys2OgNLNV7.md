## Summary
The paper proposes using raw Query-Key (QK) dot-product alignment scores from transformer attention heads as a white-box, training-free mechanism to select and verify answers in LLM reasoning tasks. Building on prior work (Tulchinskii et al., 2024; 2025), the method is extended to three settings: (i) MCQA with and without CoT prompting, (ii) correctness verification of generated reasoning chains, and (iii) open-ended candidate selection across MMLU-Pro, HLE-1/4, MATH-500, and GSM8K. A single attention head is chosen via calibration, and its QK-score is used as a decision rule without modifying model weights.

## Strengths
- **Training-free and white-box mechanism with clear practical motivation.** The method requires no fine-tuning or auxiliary models — only access to attention states — which is practically appealing. Results in Table 1 show genuine improvements on MMLU-Pro, with permutation accuracy (PA) rising substantially (e.g., DeepSeek-R1-Distill-Qwen-32B: PA from 3.00 to 37.49 for MCQA, 20.2 to 36.2 for MCQA+CoT), suggesting QK-score selection is more robust to positional artifacts than token-decoded baselines.
- **Cross-domain head transfer.** The cross-domain calibration result in Table 4 and the correlation plot in Figure 2 show that head selection generalizes across datasets (MATH-500 ↔ HLE-1/4), suggesting the selected head captures a general reasoning signal rather than dataset-specific artifacts. This is a meaningful finding.
- **Broad model coverage.** Results are reported across eight model families (LLaMA-3.1-8B, DeepSeek-R1-Distill-{1.5B, 7B, 14B, 32B}, Qwen3-{8B, 14B, 32B}), giving reasonable confidence that the results are not model-specific.

## Weaknesses

### Fatal
None.

### Major
1. **Verification baselines are methodologically flawed.** In Table 3, baselines on HLE-1/4 are 0–2% for nearly all models. For a binary correctness-verification task, random performance is ~50%, so these near-zero numbers indicate severe class imbalance, not a reasonable baseline. The paper does not report the proportion of correct vs. incorrect solutions in each 100-sample pool. A verifier that predicts "incorrect" for everything would trivially achieve high accuracy if, say, 90% of solutions are wrong. Without reporting dataset balance or using class-balanced metrics (e.g., balanced accuracy, F1, MCC), the large QK-score gains (e.g., 0% → 90%) are uninterpretable and potentially an artifact of the class distribution. This is the most significant methodological issue in the paper.

2. **The claim of "surpassing preference-optimized LLMs" is never substantiated.** The abstract states: "we surpass the performance of full-scale, preference-optimized LLMs on two fundamental reasoning tasks." No such head-to-head comparison appears anywhere in the paper. No preference-optimized model is named or evaluated. This claim should either be substantiated with explicit comparison data or removed entirely.

3. **Ambiguous and shifting "baseline" definition.** The baseline in MCQA settings (Acc. 12–28% for 10-way MCQA where random = 10%) appears to be the model's decoded letter output, but this is never stated explicitly. The baseline in verification is the model's self-judgment accuracy. The baseline in hypothesis selection is majority consistency. These are different quantities, and the inconsistency in baseline framing across experiments makes comparing the reported Δ values misleading.

### Minor
1. **Hypothesis selection experiments use only LLaMA-3.1-8B** (Table 4). Extending to at least one additional model family would substantially strengthen this experiment.
2. **Verification experiment uses only 100 samples per dataset.** Given the binary nature of the task and potential class imbalance, confidence intervals or variance estimates are essential and absent.
3. **No analysis of the selected head's identity.** Whether the same head (or heads with similar function) tends to be selected across models and tasks would provide mechanistic insight. Currently, the head selection is treated as a black box.
4. **Mixed and inconsistent results.** For MCQA+CoT in Table 1, QK-score underperforms the CoT baseline for Qwen3-8B (35.67% vs. 36.13%), Qwen3-14B (42.25% vs. 44.0%), and DeepSeek-R1-Distill-Qwen-1.5B (16.8% vs. 19.9%). In Table 3, QK-score underperforms for Qwen-7B and Qwen-14B on MATH-500. The paper glosses over these regressions without analysis.

### Trivial
- GSM8K is mentioned in the abstract as a target dataset but no table reports GSM8K results; only MATH-500 is used.

## Nice-to-Haves
- Report class-balanced accuracy (or F1/MCC) for the binary verification task in addition to raw accuracy.
- Provide an oracle upper bound for hypothesis selection (best of 8 candidates).
- Ablate the choice of representative tokens (c_r, a_r) — the paper selects end-of-line/punctuation tokens by heuristic, but no sensitivity analysis is provided.
- Include confidence intervals or variance across multiple calibration seeds for the permutation accuracy results.

## Novel Insights
The observation that CoT reasoning systematically strengthens QK alignment between premise and response tokens — making the QK-score signal more discriminative after deliberation than without it — is a meaningful mechanistic hypothesis. The cross-domain transfer of head quality (Figure 2, Table 4) provides suggestive evidence that certain attention heads encode general reasoning alignment rather than task-specific patterns. However, these insights remain at the level of empirical observations without mechanistic explanation, and the most striking claimed results (verification gains on HLE-1/4) are confounded by the class imbalance issue described above.

## Suggestions
- Fix the verification experiment by reporting balanced accuracy or per-class precision/recall, and include the base rate of correct solutions in each 100-sample pool.
- Either substantiate the "surpassing preference-optimized LLMs" claim with actual comparisons, or remove it from abstract and text.
- Clearly define the "baseline" for each experimental setting (decoded letter, self-judge, majority voting) in a unified table header or footnote.
- Report hypothesis selection across at least two models, not just LLaMA-3.1-8B.

## Score and Decision
The core idea — using raw QK-scores as a training-free, white-box reasoning signal — is grounded in interesting prior work and has genuine merit. The MCQA results (especially the permutation accuracy improvements) represent a real and reproducible contribution. However, the verification experiment contains a fundamental class-imbalance issue that makes its headline results uninterpretable, the central claim about outperforming preference-optimized LLMs is never backed up, baselines are inconsistently defined, and the paper is thin in both depth of analysis and experimental scale. As presented, the paper does not meet the bar for acceptance, though the underlying direction is worth developing.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>