## Summary
This paper proposes combining sparse Mixture-of-Experts (MoE) architectures with instruction tuning (Flan), presenting extensive experiments showing that this combination yields models (Flan-ST) that outperform dense models at comparable or lower computational cost. The main claim is that MoE models benefit disproportionately more from instruction tuning than dense models do. The largest model, Flan-ST$_\text{32B}$, surpasses Flan-PaLM$_\text{62B}$ on four English benchmarks while using one-third of the FLOPs per token.

## Strengths
- **FLOPs-controlled Pareto dominance across multiple scales**: The controlled study (Section 3.2, Figure 2) compares Flan-ST variants to the authors' own re-finetuned Flan-T5 dense models at matched compute, showing that instruction-tuned MoE models dominate dense T5 counterparts on the cost-performance Pareto frontier from small through XXL scales, with "absolute performance improvements of 7.1% on average" for MMLU-Direct (lines 136–140). This is a clean, within-family comparison that directly demonstrates the synergy.
- **Compute-efficiency breakthrough with concrete benchmark numbers**: Flan-ST$_\text{32B}$ achieves 65.4% on MMLU and 54.4% on BBH while using only 32.1 GFLOPs/token — one-third of Flan-PaLM$_\text{62B}$'s compute — yet surpasses it on all four benchmarks (Section 3.3, lines 209–212). This quantifies the practical payoff and is the paper's strongest concrete result.
- **Systematic ablation inventory**: The paper evaluates three routing strategies, two auxiliary loss types, four freezing strategies, and hyperparameter sensitivity (Table 1, Section 4.1). The finding that freezing the gate slightly improves performance while freezing experts harms it (lines 249–251) is a non-obvious, actionable insight for practitioners.
- **Honest documentation of failure modes**: Section 4.2 (lines 343–348) transparently reports poor multilingual performance (15.5% on MGSM, 25.1% on TyDiQA) and attributes it to English-only instruction tuning. This candor is valuable for practitioners deciding whether to adopt the approach.
- **Identifies that MoE performance scales better with number of tasks than number of experts**: Line 307 reports this non-trivial insight, which guides resource allocation when building instruction-tuned MoE models.

## Weaknesses

### Fatal
None.

### Major
- **The headline comparative evidence for the core claim is confounded by cross-family comparison.** The paper's marquee evidence that "MoE models benefit more from instruction tuning" is the 45.2% improvement for ST$_\text{32B}$ vs. ~6.6% for Flan-PaLM$_\text{62B}$ (line 157). These are relative improvements over *different* base models from different model families (ST-MoE vs. PaLM), trained on different data, with different architectures, and at different parameter counts. If PaLM$_\text{62B}$ already had higher base performance, a smaller relative gain is expected and uninformative for comparing benefit magnitude. **However**, the paper does have cleaner within-family evidence: the controlled study in Section 3.2 (comparing Flan-ST to re-finetuned Flan-T5 at matched FLOPs) and Figures 1, 6. The problem is that the paper foregrounds the confounded cross-family comparison as the headline result, while the cleaner within-family evidence is only shown in figures without numerical reporting in the text (the 7.1% average improvement on MMLU is an exception). This weakens the paper's strongest rhetorical claim. The authors should numerically report the within-family comparisons as primary evidence.
- **Overclaimed resource equivalence between MoE and dense models during training.** The conclusion states that "these advancements are attained without necessitating an increase in computational resources or memory usage during training and inference" (line 378). During training, MoE models require all expert parameters to be loaded into GPU memory (e.g., 64 experts per layer in the 32B model), resulting in substantially higher memory requirements than an equivalently-computed dense model. The computational efficiency of MoE primarily applies to *inference* (sparse activation reduces per-token FLOPs), but the paper's language in the Introduction (line 22) and Conclusion (line 378) extends this claim to training memory without justification. The authors should explicitly scope the efficiency claim to inference FLOPs.

### Minor
- **Scope of the contribution is not fully conditioned on English-only results.** The abstract and conclusion describe "comprehensive experiments across a wide spectrum of NLP tasks" and claim broad advancements without acknowledging that all four primary benchmarks are English-only. The failure case section (4.2) honestly reports poor multilingual performance, but this limitation is not reflected in the paper's high-level claims. The multilingual weakness does not invalidate the English results, but the framing should be more precise.
- **Ablation results are inconsistent and the "practical recipe" framing is overblown.** Table 1 shows that for Flan-EC$_\text{base}$, balance loss helps (+0.6 avg) while Z-loss hurts (-0.9 avg); for Flan-ST$_\text{base}$, the pattern reverses (balance loss hurts by -1.6, Z-loss helps by +0.3). The freeze-gate improvements are tiny (+0.3–0.4 points). The paper offers a post-hoc explanation, but these results do not yield a clear, universally applicable recipe as claimed (line 222: "offer a practical recipe"). The results are honestly reported but the framing oversells what the ablations deliver.
- **Base model performance for the 45.2% improvement claim is not reported.** The paper claims instruction tuning enhances ST$_\text{32B}$ by 45.2% but never shows the base ST$_\text{32B}$ numbers from which this improvement is computed. Publishing these would allow readers to evaluate the claim directly.

### Trivial
None.

## Nice-to-Haves
- Variance or significance reporting would strengthen the ablation study, where some differences (e.g., freeze-gate: +0.3 to +0.4 points) are small enough to be noise. This is not standard practice for large-scale LLM benchmarking, so it is a suggestion rather than a weakness.
- The within-family comparisons (Figures 1, 2, 6) would benefit from numerical annotation or a supplementary table, as extracting precise values from scatter plots is difficult.

## Removed Points
These points were flagged by reviewers but removed after verification:
- **"The central empirical claim is supported only by confounded cross-family comparisons"** — Overstated. The paper provides within-family controlled evidence (re-finetuned Flan-T5 at matched FLOPs, the 7.1% average improvement on MMLU-Direct, Figures 1, 2, 6). The "only" claim is a strawman; the valid core (that the 45.2% vs. 6.6% comparison is confounded) is retained as a Major weakness above.
- **Strength citing the 45.2% vs. 6.6% comparison as "direct quantitative evidence"** — This specific evidence is confounded per the verified weakness. The underlying finding (MoE benefits more) is still supported by other evidence, but this particular datapoint is not clean evidence.
- **Missing variance/significance reporting as a weakness** — Not standard practice for large-scale LLM benchmarks; moved to Nice-to-Have.
- **Any formatting, typo, or grammar criticism** — These are parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Report the within-family, same-base-model comparison numerically (Flan-ST vs. re-finetuned Flan-T5 at matched FLOPs from Figures 1, 2, 6) in the main text or a table. This is the cleanest evidence for the "MoE benefits more" claim and should be foregrounded.
2. Scope the resource-efficiency claims precisely: MoE provides inference FLOPs savings, but training memory is higher. Remove or qualify claims about "memory usage during training."
3. Condition the high-level claims in the abstract and conclusion on English-language performance, or add a sentence noting the multilingual limitation.
4. Report the base ST$_\text{32B}$ pre-instruction-tuning performance to contextualize the 45.2% improvement figure.
5. Tone down the "practical recipe" framing for the ablations, since the auxiliary loss results are model-dependent and the freeze effects are negligible.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>