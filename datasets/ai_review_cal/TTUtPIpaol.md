- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6
## Summary

This paper proposes EEP (Efficient Expert Pruning), a gradient-free evolutionary strategy for pruning and merging experts in Sparse Mixture-of-Experts (SMoE) language models. The method searches over a parameter space of router-mapping and expert-merging matrices (W_RM and W_EM) using evolutionary optimization. It operates in two phases: (1) a discrete pruning phase where rows of W_RM = W_EM are constrained to one-hot vectors to select expert subsets, and (2) a continuous merging phase where these matrices are decoupled and take real-valued weights to consolidate knowledge from discarded experts. Experiments on Mixtral 8×7B, Mixtral 8×22B, and other SMoE models show that EEP can reduce total experts by up to 75% while often maintaining or even improving task performance, and can reduce active experts (e.g., from top-2 to top-1) with modest speedups (1.24–1.41×). The most striking result is a 22-percentage-point gain on SQuAD (53.4% → 75.4%) after pruning 4 of 8 experts with no parameter updates.

## Strengths

- **Strong empirical results across multiple sparsity levels and tasks.** Table 1 shows that EEP (Prune Only) with 4 experts achieves an average accuracy of 70.3 across 10 datasets, surpassing the full model's 62.4 and far exceeding the best baseline NAEE's 60.5. At 2 experts, EEP (Prune+Merge) averages 65.6 vs. the full model's 62.4. These are not isolated artifacts — improvement is consistent across nearly all datasets.

- **Gradient-free operation is a genuine practical advantage.** The method uses only forward passes and evolutionary search, avoiding backpropagation entirely (Section 4.3). This means the pruning/merging process can run on inference-capable hardware where gradient computation is infeasible, directly supporting the "more widely applicable" claim.

- **Measurable memory and speed benefits.** Table 5 shows a 71% GPU memory reduction (88.6→25.6 GB) when reducing to 2 total experts, and a 1.41× inference speedup when combining 4 total experts with 1 active expert. These numbers are concrete and realistic.

- **Generalization demonstrated on diverse and out-of-distribution tasks.** On the MMLU split (Table 4), EEP (Prune+Merge) with 4 experts achieves 56.9 on 50 IID validation sets (vs. NAEE's 53.5) and 64.6 on 7 unseen OOD datasets (vs. NAEE's 63.6). This cross-task generalization strengthens the method's credibility.

- **Expert merging consistently improves over pruning alone.** Across all datasets in Table 1, EEP (Prune+Merge) outperforms EEP (Prune Only), e.g., on CB with 4 experts: 75.0 vs. 69.6. This validates the design choice of consolidating knowledge from pruned experts.

- **Unified parameter space for pruning and merging.** The W_RM and W_EM matrices (Section 4.2, Figure 1) elegantly handle both discrete expert selection (one-hot rows) and continuous weight merging within a single framework, providing a principled search space.

## Weaknesses

### Fatal

None.

### Major

- **No variance or statistical significance reported for EEP.** Random selection is run 30 times with mean reported (line 187), but EEP itself is run only once per dataset. Given the stochastic nature of evolutionary search and the cost of the search procedure, it is unknown whether the reported gains are reproducible across independent runs or whether they vary substantially. This is especially important for the most surprising result (the SQuAD improvement) — the paper would be substantially stronger with at least 3–5 independent EEP runs with mean ± std.

- **Search procedure underspecified in the main text.** The paper does not state population size, number of generations, mutation rate, crossover details, or total number of forward passes required for the evolutionary search (Section 4.3). The paper mentions a "predetermined number of iterations" (line 163) without specifying what that number is. While details may reside in the appendix (app:exp, which is stripped here), a method's core hyper-parameters should appear in the main text to allow basic reproducibility assessment. The paper's own Limitations section (line 390) acknowledges "a potentially costly search process" but gives no quantification, making it impossible to assess the method's practical deployment cost.

- **It is not clarified whether the search is per-layer or joint across layers.** The parameter space is defined per SMoE block (line 136: "for each SMoE block (l=1…L)"), and NAEE is described as per-layer exhaustive search. However, whether EEP optimizes W_RM and W_EM independently per layer or jointly across layers is never stated. This distinction is critical: per-layer search over 4-of-8 selections reduces to 70 combinations per layer (manageable), while joint search over 32 layers is 70^32 (intractable without ES). The ambiguity makes it hard to assess whether the evolutionary search is genuinely needed or whether a simpler method would suffice.

### Minor

- **Analysis of why pruning improves performance is thin.** Section 5.6 provides a reasonable hypothesis (the router network delegates more effectively to fewer experts) and supporting evidence from one layer (Figure 5 — correlation, frequency, and routing-weight plots for layer 0 on SQuAD). However, this single-layer analysis does not establish a causal link. A stronger test would be to compare routing decisions before and after pruning on a per-token basis across multiple layers, or to show that the improvement persists when the original router weights are used with the pruned expert set.

- **Expert merging phase lacks analysis of the learned W_EM weights.** After the continuous search, it is unknown whether W_EM rows are close to one-hot (i.e., effectively still pruning) or genuinely blend multiple experts. Understanding the nature of the merged experts would validate that the merging phase actually produces different behavior from the pruning phase.

- **No comparison to parameter-efficient fine-tuning baselines.** The paper frames expert merging as a "memory-efficient way of fine-tuning" (Abstract, line 5). Given that the merging phase involves task-specific optimization (requiring many forward passes over a training set), comparisons to lightweight PEFT methods such as LoRA fine-tuning of the pruned model (or even the full model) with similar compute budgets would help contextualize the trade-offs. Without this, it is unclear whether the gains from the merging phase come from the structured merging operation or simply from any task-specific adaptation.

### Trivial

- In Table 2 (Mixtral 8×22B), the Frequency baseline achieves 0.0 on WIC at Num=4 and 0.0 on all tasks at Num=2. While not a bug (removing the least-frequently activated experts can be catastrophic at high sparsity), the table should include a brief footnote or note explaining that these zero values are methodological collapses of the baseline rather than evaluation errors.

## Nice-to-Haves

- **Comparison to per-layer exhaustive search.** For the 8-expert setting, C(8,4)=70 combinations per layer. A head-to-head comparison showing that EEP's evolutionary search finds a better solution than per-layer exhaustive search (or that EEP solves a harder joint-search problem that exhaustive search cannot scale to) would cleanly justify the use of ES.
- **Run-time cost in GPU-hours or forward passes.** Adding a concrete estimate of the search cost (e.g., "X GPU-hours on 2×A100 for Mixtral 8×7B on SQuAD") would allow readers to judge whether the method is practical for their own deployment scenarios.
- **A controlled experiment to test the router hypothesis.** For example, applying the pruned expert set but keeping the original (unpruned) router's weights to the top-4 active experts would isolate whether the improvement comes from the changed routing or from the expert selection itself.

## Removed Points

These points from the reviews were removed with justifications:

- **"Performance improvements not credibly explained / extraordinary claims"** — The paper does provide a hypothesis (Section 5.6) and consistent evidence across 10 tasks, not just SQuAD. The improvement is striking but not isolated; the method's average gain across all tasks is 7.9 points (from 62.4 to 70.3) with Prune Only at Num=4. SQuAD is the most dramatic example of a consistent pattern, not an anomaly.
- **"Baseline comparisons not sufficiently controlled"** — The paper specifies that the same per-dataset training subset is used for all methods (line 179) and describes each baseline's procedure (line 183). NAEE is applied as described in its own paper. No evidence supports the claim that baselines are "not well-tuned."
- **"MMLU results contradict the pattern"** — The paper does not claim universal improvement. The MMLU results show EEP outperforming baselines (Table 4) and the IID drop from full model (60.7→56.9 at Num=4, Prune+Merge) is moderate. Different tasks have different sensitivities to pruning; this is not a contradiction.
- **"Full model underperforming"** — This is speculative. The paper uses a consistent evaluation pipeline (OpenCompass-based, line 181) for all methods. Comparisons across methods within this pipeline are valid.
- **"Frequency=0.0 is an implementation bug"** — This is a plausible outcome of a bad baseline at high sparsity, not necessarily a bug.
- **"EEP vs. full model not apples-to-apples for active expert reduction"** — The comparison is clearly labeled as EEP's result after merging. The paper is transparent about what is being compared.
- **"Exhaustive search over C(8,4)=70 is feasible"** — This depends on whether search is per-layer or joint. The paper is ambiguous on this point (kept as a major weakness above), but the critic's framing assumes per-layer search without evidence.
- **"Figure 3 motivation is not new"** — Redundancy in SMoE has been observed before, but this is just motivation, not a claimed contribution.
- **All formatting, typo, and missing-appendix complaints** — The parser strips appendix content; these are not author errors.
- **"No related work discussion for X"** — Per policy, I cannot verify the existence of unmentioned works.
- **Strength Finder generic strengths** ("important problem", "interesting question") — These add no information and were removed.

## Novel Insights

None beyond the paper's own contributions. The two-step (prune-then-merge) evolutionary framework and the observation that pruning can improve downstream performance without weight updates are the paper's core insights. The reviews did not surface a genuinely new interpretation that the paper itself does not already express.

## Suggestions

1. **Report variance.** Run EEP with at least 3–5 random seeds per dataset and report mean ± std. This is the single most impactful improvement for the paper's credibility.
2. **Specify search procedure in main text.** Include population size, number of generations, mutation rate, and whether search is per-layer or joint. Even a brief statement ("we use 20 individuals for 50 generations, searched independently per layer") would suffice.
3. **Quantify search cost.** Add a sentence like "The full search process for Mixtral 8×7B on SQuAD required approximately X forward passes / Y GPU-hours."
4. **Strengthen the router analysis.** Show per-token routing decisions before and after pruning across multiple layers, or present results when using the original router with the pruned expert set.
5. **Add a comparison to LoRA fine-tuning of the pruned model.** This would contextualize the merging phase's benefits and could be done at modest cost.
