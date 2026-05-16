Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes EEP (Efficient Expert Pruning), a gradient-free evolutionary search method for pruning experts in SMoE language models. The key idea is to parameterize expert pruning and merging via two matrices (router mapping W_RM and expert merging W_EM) and optimize them using evolutionary strategies requiring only inference (no backpropagation). EEP supports two use cases: reducing total experts (memory savings) and reducing active experts (inference acceleration). Experiments on Mixtral 8×7B, 8×22B, and Qwen MoE models show that EEP achieves aggressive sparsity (up to 75% expert reduction) while maintaining or improving performance, often outperforming baselines like NAEE by large margins.

## Strengths

- **Novel gradient-free search space design.** The parameterization of expert pruning and merging via W_RM and W_EM matrices is clean and flexible, unifying two operations (pruning and merging) under a single evolutionary optimization framework. This allows the method to run on devices capable of inference without requiring gradient computation, lowering the barrier for practical deployment.

- **Consistent and large improvements across diverse settings.** EEP (Prune Only) with 4 experts on Mixtral 8×7B achieves 70.3% average accuracy across 10 tasks, far exceeding the best baseline NAEE (60.5%) and even the full model (62.4%). With 2 experts, EEP (Prune+Merge) achieves 65.6% vs. the full model's 62.4%. These improvements are consistent across nearly all 10 datasets, not just a cherry-picked subset (Table 1), which lends credibility to the phenomenon.

- **Cross-model and cross-task generalization.** EEP is validated on Mixtral 8×22B, Qwen1.5-MoE-A2.7B, and Qwen2-MoE-A14B with consistent improvements (e.g., Mixtral 8×22B with 4 experts: EEP 80.4% vs. full model 66.5%). The MMLU experiments (Table 4) show that EEP generalizes to out-of-distribution tasks, outperforming NAEE on both IID and OOD settings.

- **Practical dual-use efficiency.** Profiling results (Table 6) show concrete memory savings (71% reduction from 88.6 to 25.6 GB with 2 experts) and speedups (up to 1.41× with 4 total experts + 1 active expert), providing actionable guidance for deployment scenarios.

## Weaknesses

### Fatal
None.

### Major

- **Lack of statistical reliability for the stochastic search method.** EEP relies on evolutionary search, which is inherently stochastic, yet the paper reports only single-run results with no variance or confidence intervals. By contrast, the Random baseline is run 30 times and its variance is reported — the reader has no way to assess whether EEP's dramatic improvements (e.g., SQuAD: 53.4% → 75.2%) are consistent across seeds or a lucky configuration found by chance. Given the surprising nature of the central claim (pruning improves performance without any parameter update), this omission substantially weakens the empirical evidence.

- **Insufficient explanation of the mechanism behind performance improvement from pruning alone.** The paper reports a 22-point gain on SQuAD from simply removing 4 out of 8 experts. While Section 5.6 offers a plausible hypothesis (the router operates better with fewer experts), the analysis is limited to one transformer block's activation patterns (Figure 4). There is no causal analysis linking the observed routing changes to the performance increase, no ablation showing the hypothesis holds across layers, and no discussion of why the original router would be so suboptimal that removing half the experts produces a 22-point gain. The paper's most striking result is the least explained.

### Minor

- **The constraint W_RM = W_EM during the pruning phase is stated without justification.** The paper imposes that these matrices be identical during pruning yet does not explain why this restriction is necessary or what would happen if it were relaxed. This appears to artificially limit the search space without a clear rationale.

- **Computational cost of the evolutionary search is not quantified.** The paper mentions a "costly search process" in the limitations but does not report the number of forward passes, GPU-hours, or wall-clock time for any experiment. This makes it difficult to assess whether the method is practical for typical users and to compare its efficiency against NAEE (which also requires many forward passes for loss evaluation). The claim that EEP "can run on devices affordable for inference" is unsubstantiated without a concrete cost analysis.

- **The number of training examples used for the evolutionary search is unspecified.** The paper states that "a small subset" of the training set is used per dataset but does not quantify this. Given that the search directly optimizes downstream task accuracy on these examples, the risk of overfitting is non-trivial. The MMLU OOD experiment partially addresses this, but without knowing the search set size, the reader cannot evaluate how much the results depend on memorization vs. genuine generalization.

- **Speedups from active expert reduction are modest and the accuracy-speed tradeoff is not fully discussed.** The 1.24× speedup from reducing top-2 to top-1 active experts is useful but not dramatic, and the paper does not systematically discuss the performance drop vs. speedup tradeoff (e.g., Table 5 shows that with 8 total and 1 active, average accuracy drops from 59.6 to 51.4 for the full model, and EEP restores it to 65.3 — but the comparison is against the original top-2 full model, not a top-1 full model). Clarifying the exact nature of the improvement would help.

### Trivial

- The abstract reports a SQuAD improvement to 75.4% while Table 1 shows 75.2% (Prune Only, Num=4). Minor numerical inconsistency.

## Nice-to-Haves

- Run the evolutionary search with multiple seeds (≥5) and report mean and variance for the main results (especially SQuAD) to address the reproducibility concern.
- Include an ablation comparing EEP's use of downstream task accuracy as the search objective vs. using language modeling loss (like NAEE) to isolate whether the improvement comes from the search space/algorithm or the objective function.
- Add a cost analysis table (GPU-hours or number of forward passes) for a representative setting (e.g., Mixtral 8×7B, Num=4, 10 datasets).
- Analyze the merged experts (W_EM weights) to show whether the merging produces interpretable combinations (e.g., weighted averages of semantically similar experts).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing hyperparameters for evolutionary search (population size, iterations, mutation rate).** The paper defers these to the appendix, which is stripped by the parser. Per the hard rules, this is not a valid criticism of the submission as received.
- **"Cannot independently verify" concerns about entity existence.** Any cited model, benchmark, or reference is assumed to exist.
- **Criticism that NAEE comparison is unfair because EEP uses downstream task accuracy.** This is a design choice that gives EEP an advantage, not a flaw. If anything, it highlights that the objective function matters — a useful insight rather than a weakness.
- **Template-matching confound for SQuAD.** While theoretically possible, this is speculative and not supported by evidence in the review. The paper uses the same evaluation protocol (OpenCompass) for all methods, so any template artifacts would affect all methods equally.
- **Speedup is "modest" (1.24×).** This is a matter of perspective; 1.24× is a real improvement. The concern is reframed as a minor point about missing tradeoff discussion, not the magnitude itself.
- **Strength Finder claim that EEP surpasses full model on MMLU with 4 experts (56.9% vs. 60.7%).** This is factually incorrect; the full model outperforms EEP at Num=4. The Strength Finder's claim is inaccurate.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the consistent pattern of improvement across nearly all 10 datasets in Table 1 suggests that the phenomenon of "pruning improving performance" in SMoE models is not an evaluation artifact or a single-dataset fluke, but may reflect a genuine structural property of SMoE architectures — specifically, that a simple one-layer perceptron router struggles to effectively manage many experts, and reducing the number of experts alleviates this bottleneck. This hypothesis is stated in the paper but under-explored; the reviews reinforce that this is the paper's most provocative finding and deserves deeper investigation. The interaction between search objective (downstream accuracy vs. LM loss) and the gap between EEP and NAEE is another under-analyzed dimension.

## Suggestions

1. **Report multi-seed variance for EEP.** This is the single most important fix — without it, the central empirical claim is not fully credible. Run at least 5 seeds on the SQuAD experiment and report mean ± std.
2. **Quantify the search cost** in terms of GPU-hours or forward passes for a representative setting. This is essential to support the claim of practical deployability.
3. **Justify or remove the W_RM = W_EM constraint** in the pruning phase, or ablate it to show it matters.
4. **Provide the number of training examples used for search** on each dataset to allow readers to assess overfitting risk.
5. **Expand the mechanistic analysis** (Section 5.6) to multiple blocks/layers and consider adding a simpler metric like routing entropy or expert load balancing before/after pruning to strengthen the router-improvement hypothesis.

## Score and Decision

This paper proposes a novel and practical approach to expert pruning in SMoE models with consistently strong empirical results across multiple models and tasks. The core idea — gradient-free evolutionary search over a unified pruning+merging parameter space — is well-motivated and the experiments are extensive. However, the paper's most striking claim (pruning improves performance without parameter updates) rests on results lacking statistical variance reporting, and the mechanistic explanation is thin given the magnitude of the improvements. These are fixable weaknesses that reduce the paper's current credibility but do not invalidate its contribution. The paper would benefit from a major revision addressing reproducibility and analysis depth, but the method and results are compelling enough to warrant acceptance with the expectation that these issues be addressed in the camera-ready version.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>