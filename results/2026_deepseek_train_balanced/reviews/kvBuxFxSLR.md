Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This empirical study evaluates seven layer-freezing strategies (BOT, TOP, INT, ADT-L, ADT-H at multiple ratios) applied to sub-3B decoder-only models (Gemma2b, Phi-2, MiniCPM-2b) on NLI tasks, comparing against full fine-tuning and LoRA. The central claim is that freezing the bottom 25% or 50% of transformer layers can match or exceed both baselines in accuracy while reducing training memory and time. The paper conducts a systematic sweep of strategies and ratios, reports results with 5 seeds and error bars, and includes an honestly reported negative result for adaptive freezing — but the experimental protocol is too limited (100 steps on subsampled data) to support the "fine-tuning" framing, and key results are presented only in aggregated form, making the core claims only weakly supported.

## Strengths

- **Systematic, multi-dimensional comparison**: The paper tests 7 freezing strategies at multiple ratios (25%, 33.3%, 50%, 75%) across 3 distinct decoder-only models and 5 NLI datasets, yielding 15 model×task combinations. This coverage is broader than prior layer-freezing work (Ben Zaken et al. 2022; Tang et al. 2024), which focused primarily on speed.

- **Memory measurement with component-level breakdown**: Figure 5 separates static model memory from training-specific memory (activations/optimizer states) and reports per-strategy percentages. BOT25 achieves ~30% training-memory reduction and BOT50 achieves ~50% — concrete, per-strategy numbers that support the paper's efficiency claims, with an honest account of why interval freezing yields smaller savings.

- **Statistical rigor with 5 seeds and error bars**: All experiments use seeds 42–46, and results are reported with μ±σ bands (Figure 3 shows ±1σ corridors for the ALL baseline). This allows readers to assess whether differences fall within noise — a level of uncertainty reporting that is a real asset for an empirical study.

- **Honest reporting of negative results**: The Adapted Freezing strategies (ADT-L, ADT-H) are transparently shown to *not* outperform simpler fixed strategies, and the ~13-second overhead of the adaptive step is explicitly measured (Section 4.5). The paper also notes that top-down and interval freezing yield less memory savings than bottom-up, with a plausible hardware-level explanation. This candor strengthens trust in the positive findings for BOT25/BOT50.

## Weaknesses

### Major

- **Training regime (100 steps on subsampled data) is far from standard fine-tuning, undermining the scope of the claims.** The paper trains for 100 steps with batch size 32 on a maximum of 3,200 randomly sampled examples per dataset (Section 4.1, line 105; Section 4.3, line 127). For MNLI (392k training samples), this is less than 1% of the data; each example is seen roughly once. This protocol amounts to few-shot adaptation on a tiny fraction of the data, not fine-tuning to convergence. The paper's central claim — that freezing bottom layers "achieves performance equal to or better than full model fine-tuning" — is made on the basis of a regime where *none* of the compared methods are properly fine-tuned. It is well known that findings in the low-data regime (where freezing may coincidentally act as regularization) do not necessarily transfer to convergence. Critically, the Limitations section (Section 7) discusses small model scale and narrow task scope but *never mentions* this short-training/subsampling limitation, which is arguably the most important constraint on external validity.

- **LoRA comparison is disadvantaged by the fixed 100-step budget.** LoRA adapters start from zero-initialized low-rank matrices and typically require more training steps to converge because the learned updates must build up from scratch. By contrast, the freezing strategies train a subset of pre-existing layers that already have meaningful weights. Comparing both at only 100 steps measures which method gets off the ground faster, not which is better *at convergence*. The paper's conclusion that freezing "demonstrated superior performance metrics relative to LoRA" (line 30) cannot be accepted without evidence that the comparison holds when both methods are trained to convergence or at least for comparable effective budgets (e.g., steps × trainable parameters).

- **Per-task results are shown only for QNLI; all other results are hidden behind an aggregated ranking score.** Figure 3 shows disaggregated accuracy for QNLI across all three models. For RTE, CB, MNLI, and the fifth unnamed task, no individual results are reported — only a ranking score that averages across all 15 model×task combinations (Section 4.6). The paper never explicitly names the fifth task (it says "3 models × 5 tasks" at line 155 but the running text names only QNLI, MNLI, RTE, and CB). Without per-task accuracies with confidence intervals, the reader cannot assess whether BOT25's strong ranking is consistent across tasks or driven by a single task. A ranking score also conflates meaningful differences on some tasks with negligible ones on others.

### Minor

- **Memory reduction framing in the abstract is selectively favorable.** The abstract and Conclusion claim the approach "reduces memory consumption by about 30% and 50%" without qualification. Section 4.5 (line 148) clarifies that this is the reduction in *training-specific* memory (activations + optimizer states) excluding the static model weights. Since model weights constitute a large fraction of total GPU memory for sub-3B models, the total memory reduction is substantially smaller than the headline numbers suggest. The abstract and Conclusion should state the basis for the percentage.

- **No convergence analysis or learning curves.** The paper reports accuracy only after 100 fixed steps. It does not show whether models have converged, whether rankings between strategies shift with more training, or even whether the 100-step endpoint is stable. Learning curves (accuracy vs. training step) for at least one representative setting would be far more informative than a single endpoint.

- **No discussion of validation strategy for hyperparameter selection.** The paper describes finding the optimal freezing ratio and position by comparing strategies (Section 4.2) but does not mention a held-out validation set used for this selection. If the best-performing strategy was identified by comparing on the same data used for evaluation, this constitutes implicit multiple comparisons.

### Trivial

- Inconsistent memory numbers: The abstract and line 30 state BOT25 reduces *training* memory by "over 30%," while line 148 says BOT strategies (covering all ratios) reduce training memory by 12–25%. If BOT25 falls at the lower end (~12%), the "over 30%" claim is unsupported. The paper should reconcile these numbers.
- The fifth task in the "3 models × 5 tasks" evaluation is never named in the text (only QNLI, MNLI, RTE, CB are mentioned), making the evaluation scope ambiguous.

## Nice-to-Haves

- Train to convergence (≥3 epochs) on the full datasets for at least one model×task combination to test whether the freezing advantage holds under proper fine-tuning.
- Report per-task accuracy in a table (with confidence intervals) instead of relying solely on a ranking score.
- Provide learning curves for the main strategies to show convergence behavior.

## Removed Points

- *"QNLI is not an NLI task"* — QNLI is standardly included in GLUE's NLI grouping and widely used as an NLI benchmark. The criticism is pedantic and factually questionable given community norms.
- *"No inference speed analysis"* — The paper's stated scope is training efficiency; inference analysis is outside that scope.
- *"Adaptive freezing motivation unclear"* — Section 3.2 clearly describes the motivation (track weight changes to identify important layers) and the 5-step window choice.
- *"Motivation mismatch (sub-3B vs 7B+)"* — The paper explicitly limits experiments to models that fit on a single GPU (line 28). This is a scope choice, not a flaw.
- *"No held-out validation set for hyperparameter tuning"* — Partially speculative; the paper mentions 5 random seeds which mitigates overfitting to some degree. Moved here as insufficiently grounded.

## Novel Insights

None beyond the paper's own contributions. The finding that bottom-up freezing at 25% outperforms both full fine-tuning and LoRA under a short-training regime is potentially interesting, but the experimental design limitations mean it remains a preliminary observation rather than a settled result. The negative result on adaptive freezing (tracking weight changes in the first 5 steps does not help) is a useful data point that others can build on.

## Suggestions

- **Reframe the scope.** Acknowledge explicitly that the study compares freezing strategies under a *fixed short-training budget* (100 steps on subsampled data), not under convergence. The claim "freezing matches or exceeds full fine-tuning" should be qualified to this specific setting.
- **Run convergence experiments.** Extend training to 3–5 epochs on full data for at least one model (e.g., Gemma2b on RTE and a subset of MNLI) and verify whether the ranking of BOT25 vs. ALL vs. LoRA holds.
- **Add a per-task results table.** Supplement the ranking score with a table showing mean accuracy ± std for all strategies × all tasks × all models.
- **Clarify memory reporting.** State in the abstract that the 30–50% reduction applies to training-specific memory (activations/optimizer states), and provide total-GPU-memory percentages alongside.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>