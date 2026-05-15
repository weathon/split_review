Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces EEP (Efficient Expert Pruning), a gradient-free evolutionary search method for pruning experts in SMoE language models like Mixtral 8×7B. The approach uses two learnable matrices (router mapping W_RM and expert merging W_EM) that are optimized via evolutionary search over a calibration set, and operates in two phases — discrete expert pruning followed by continuous expert merging. Results on 10+ downstream tasks across Mixtral 8×7B, 8×22B, and Qwen MoE models show that EEP significantly outperforms existing expert pruning baselines (Random, Frequency, Soft Activation, NAEE) and can even improve over the full model while reducing total experts by up to 75% and GPU memory by up to 71%.

## Strengths

- **Gradient-free design requiring only inference.** EEP relies solely on forward passes through the model, with no backpropagation through the 47B+ parameters. The paper explicitly states that the search "can be conducted on devices capable of inference" (Section 4), making pruning accessible to users without large-scale training hardware. This is a genuine practical advantage over gradient-based alternatives.

- **Consistent and substantial improvements over all existing baselines.** Across both sparsity levels (4 experts and 2 experts) and all 10 evaluated tasks, EEP (both Prune Only and Prune+Merge) outperforms Random, Frequency, Soft Activation, and NAEE by large margins (Table 1). For example, at Num=4 the average of EEP (Prune+Merge) is 74.2% vs. 60.5% for NAEE, the strongest baseline. This consistent superiority strengthens the claim that the search space design and evolutionary optimization are effective.

- **Demonstrated generalization across models and to large-scale/out-of-distribution data.** EEP generalizes from Mixtral 8×7B to Mixtral 8×22B, Qwen1.5-MoE, and Qwen2-MoE (Section 5.2). On MMLU (57 tasks), EEP outperforms baselines on both held-in tasks (50 datasets) and unseen OOD tasks (7 datasets, e.g., 71.3% vs. 69.4% for NAEE at Num=6), showing the searched pattern transfers beyond the calibration distribution (Table 4).

- **Measurable and meaningful efficiency gains.** Profiling on Mixtral 8×7B (Table 5) shows pruning to 2 experts reduces GPU memory from 88.6 GB to 25.6 GB (71% reduction). Combining total and active pruning yields a 1.41× inference speedup while maintaining or improving task accuracy. These numbers directly support the paper's deployment-oriented motivation.

## Weaknesses

### Major

- **SQuAD evaluation protocol and baseline need clarification.** The full model achieves only 53.4% on SQuAD under the paper's generation-based evaluation (Table 1), which is notably lower than typical SQuAD scores reported for Mixtral 8×7B-Instruct under standard extractive QA evaluation (EM/F1). The same evaluation is applied to all methods, so relative comparisons between methods are valid. However, the paper does not explain why the absolute SQuAD numbers differ from expected values, nor does it validate the generation-based template-matching protocol (e.g., via human inspection or correlation with standard SQuAD EM/F1 scores). Since the SQuAD improvement from 53.4% to 80.6% (27 points) is the paper's most striking headline result, the evaluation protocol's behavior on SQuAD warrants direct scrutiny. **Recommendation**: compare the generation-based results on SQuAD to standard EM/F1 evaluation on a subset, and/or report human-validated sample outputs showing what changes.

- **No variance reporting for EEP results despite stochastic search.** The evolutionary search involves random initialization, mutation, and crossover — all stochastic processes. Yet all EEP results are reported as single numbers. Meanwhile, the Random baseline includes standard deviations on MMLU (e.g., ±9.6). Without multiple runs (≥3–5) with mean and standard deviation, it is impossible to assess whether EEP's margins over baselines are statistically significant. This is especially important where margins are modest (e.g., MMLU Num=6: 61.8 vs. 57.5 for NAEE — a 4.3 point gap that could be within noise for a stochastic method).

### Minor

- **Evolutionary search hyperparameters are underspecified.** The paper does not report population size, number of generations, mutation rate, crossover scheme details, or convergence criteria (Section 4.3). The paper references an algorithm (`\cref{alg:evo_search}`) that may be in the appendix, but core experimental reproducibility parameters should be stated in the main text. This also makes it difficult to assess the search cost, which the paper itself acknowledges as a limitation but never quantifies (no GPU-hours, number of forward passes, or wall-clock time reported).

- **Why EEP outperforms NAEE's exhaustive per-layer search is not explained.** NAEE exhaustively evaluates all pruning choices for each layer to select the one minimizing per-layer reconstruction loss. EEP, which instead optimizes for downstream task accuracy on a calibration set, outperforms NAEE by large margins. The paper attributes this to EEP's superior search but does not discuss the likely explanation: the per-layer reconstruction loss optimized by NAEE may be poorly correlated with task accuracy. A brief note reconciling why an "exhaustive" loss-minimizing method can be outperformed by a heuristic search would help the reader.

- **Speedup comparisons do not isolate the contribution of the search from the architectural change.** The paper reports a 1.41× speedup for 4 experts + 1 active expert. But the baseline for speed should separate what is simply "fewer experts/active experts" from what is "EEP-specific optimization." The paper shows Full Model with top-1 achieving 51.4% average (Table 2) vs. EEP top-1 at 65.3% — but this conflates the method's optimization with the architectural speed benefit. A cleaner ablation would compare speed and accuracy of: (a) Full Model (top-2), (b) Full Model (top-1), (c) EEP Prune Only (top-1), (d) EEP Prune+Merge (top-1), to isolate what EEP contributes beyond simply using fewer active experts.

### Trivial

- The paper states "no parameter updates" for the prune-only results, which is accurate. However, the merging phase does produce new weight matrices (through linear combination). This could cause minor confusion. Clarifying "no gradient-based fine-tuning" vs. "no parameter updates" would be more precise.

## Nice-to-Haves

- Adding a comparison to lightweight gradient-based fine-tuning (e.g., LoRA on the router or on expert weights with the same calibration budget) would strengthen the claim that EEP's gradient-free approach offers a practical advantage. As presented, it's unclear whether a few LoRA steps on the same calibration data would recover similar or better performance at lower search cost.

- Quantifying the search cost (GPU-hours, number of forward passes) for a representative run would help practitioners assess the practical trade-off against alternatives.

## Removed Points

- **Criticism about SQuAD improvement being "physically implausible without parameter updates."** Removed because: (1) the paper provides a testable hypothesis (the router functions better with fewer experts — Section 5.6) and supporting evidence (Figure 4 shows changed activation patterns); (2) the improvement is not isolated to SQuAD — EEP improves on nearly all datasets at Num=4 (COPA 89→99, BoolQ 77→85, etc.), making it a pattern rather than an isolated artifact; (3) "physically implausible" is an opinion, not a factual claim, and the critic provides no proof that this cannot happen. The improvement magnitude is surprising but not impossible, and the paper's own analysis offers a plausible mechanism.

- **Criticism about the evaluation being "broken" and "makes no valid empirical claim."** Removed because: the paper explicitly states it uses OpenCompass (a standard, widely-used evaluation framework) with modifications for the Mixtral family (Section 5.1). The same evaluation protocol is applied consistently to all methods. Even if absolute numbers differ from standard benchmarks, the *relative* comparisons between methods are valid. The critic's claim that "if the metric is broken, the paper makes no valid empirical claim" is an overstatement.

- **Criticism that MMLU margin shrinkage "is consistent with overfitting."** Removed because: the paper also demonstrates OOD generalization on 7 unseen MMLU datasets where EEP still outperforms baselines (71.3% vs. 69.4% for NAEE at Num=6, Table 4). Overfitting to the calibration set should not transfer to unseen tasks.

- **Strength from Strength Finder about "Analysis of why fewer experts can improve performance"** — dropped because the analysis in Section 5.6 is acknowledged by the authors as a hypothesis with supporting observations (Figure 4) but no causal link. The strength is overstated relative to what the paper actually provides.

## Novel Insights

None beyond the paper's own contributions. The observation that pruning can improve SMoE performance is itself the paper's most novel empirical finding, and the reviews do not contribute deeper insight beyond noting this should be more rigorously validated.

## Suggestions

1. **Clarify the SQuAD evaluation.** Compare generation-based results to standard EM/F1 evaluation on a subset of SQuAD. Report what examples the full model "fails" on under generation-based eval that the pruned model "passes." This would either validate the metric or reveal a systematic bias.

2. **Run EEP with multiple seeds (≥3) and report mean ± std** for at least a representative subset of tasks (e.g., SQuAD, BoolQ, MMLU). Without this, the statistical significance of EEP's advantage over baselines is unverifiable.

3. **Report the evolutionary search cost** (population size, generations, number of forward passes, GPU-hours) for a representative run. This is critical for practitioners evaluating whether the search overhead is worth the performance gain.

4. **Add a brief explanation** of why EEP outperforms NAEE despite NAEE's exhaustive per-layer search — specifically, that NAEE optimizes a proxy loss (per-layer reconstruction) which may not correlate well with downstream accuracy, while EEP optimizes directly for task performance on the calibration set.

## Score and Decision

This paper presents a genuinely novel gradient-free approach to expert pruning with consistent experimental support across multiple models and datasets. The core weaknesses are addressable — the SQuAD evaluation needs clarification, variance reporting is missing, and search details should be documented. These do not fatally undermine the paper's contributions, as the pattern of improvement is consistent across many datasets and models, not an isolated artifact.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>