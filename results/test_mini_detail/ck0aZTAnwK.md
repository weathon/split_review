Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies pre-training language models with fixed data but unlimited compute — the regime that arises as compute grows faster than web text. The authors show that standard data-constrained recipes (epoching + scaling parameters) overfit, and propose a regularized recipe with 30× larger weight decay than standard practice, which yields monotone power-law scaling in parameter count. They further find that ensembling independently trained models achieves a lower loss asymptote than scaling a single model, and that composing both (joint scaling) gives an estimated 5.17× data efficiency at 200M tokens. Distillation and downstream evaluation confirm the approach.

## Strengths

1. **Clear demonstration that strong regularization fixes overfitting in data-constrained pre-training.** Section 3 and Figure 3 show that after tuning weight decay to 30× standard (0.1), the loss follows a monotone power law $(0.05/N^{1.02}+3.43)$ across models up to 140× Chinchilla ratio, whereas the standard recipe plateaus and then degrades (Figure 2). This is a clean empirical finding supported by the finite-scale points, not just extrapolation.

2. **Ensembling outperforms parameter scaling at matched total parameter counts, visible in finite data.** Figure 4 shows that at every tested total parameter count (150M–1.4B), the 300M-member ensemble curve lies below the single-model curve. This advantage does not rely on asymptote extrapolation — even a K=3 ensemble of 300M models (900M total parameters) has loss ~3.40, below the best 1.4B single model at ~3.46.

3. **Distillation preserves most of the ensemble gains in a smaller model.** Section 6.1 and Figure 8 show that a 300M student distilled from an 8-ensemble of 300M teachers achieves loss 3.36, retaining 83% of the ensemble's improvement over the regularized 300M baseline (3.57), and outperforming the regularized recipe's asymptote. This concretely demonstrates the practical utility of the ensemble approach.

4. **Downstream validation confirms that validation-loss improvements translate to real tasks.** Section 7 and Figure 9 show that the best ensemble outperforms the best unregularized model by 9% average on PIQA, SciQ, and ARC Easy, with strong correlation between validation loss and downstream error across all recipes.

5. **Novel framing of recipe evaluation via asymptotes rather than fixed-budget performance.** The paper introduces a conceptually clean metric (asymptotic loss under infinite compute) that captures the data-constrained, compute-rich setting, and provides a concrete procedure for computing it.

## Weaknesses

### Major

1. **Headline data-efficiency numbers (2.29×, 3.03×, 5.17×) are based on underdetermined extrapolation without uncertainty quantification.** The regularized-recipe asymptote (3.43) comes from a 3-parameter power law $A/N^\alpha+E$ fit to 4 points (150M, 300M, 600M, 1.4B parameters). The joint-scaling asymptote involves three cascaded power-law fits with similar data-to-parameter ratios. The paper reports sensitivity to seed variance (Appendix I.1: ±0.02) but not to model-form uncertainty — many functional forms would fit 4 points equally well, yielding different asymptotes. The reader cannot assess whether the observed differences between asymptotes (e.g., 3.43 vs 3.34) are real or fitting artifacts. *(Lines 95, 115-118; Figures 3, 5, 7)*

2. **Asymmetric comparison inflates the claimed gains.** The paper compares the regularized recipe's *asymptote* (limit as $N\to\infty$) against the standard recipe's *finite best loss* (minimum over $N$ at tested scales). Since the standard recipe's loss increases at high $N$ due to overfitting, its best is achieved at a modest $N$ and is not an asymptotic quantity. The framing thus compares regularized-infinite to unregularized-finite, not two equally extrapolated limits. The paper partially mitigates this by also reporting finite-scale numbers (2.09× without extrapolation, line 185), but the headline 5.17× number inherits this asymmetry. *(Lines 34-36, 177-181, 188-189)*

3. **The data-scaling-law analysis (Section 5) uses only four token counts and cascades extrapolations.** The joint-recipe data efficiency at 200M tokens involves: (a) fitting power laws in $K$ for four $N$ values (4 points each), (b) fitting asymptotes from (a) into a power law in $N$ (4 points), then (c) fitting the resulting asymptotes into a power law in $D$ (4 points). Each step compounds extrapolation error. The paper acknowledges that "data scaling laws are expected to be noisy" (line 199) but provides no confidence bounds on the final 5.17× number or the claim that improvements "persist at higher token budgets." *(Lines 191-199)*

### Minor

1. **Ensemble hyperparameters are not fully optimized.** Section 4.3 acknowledges that "we cannot fully find locally optimal hyperparameters" for the joint recipe and instead uses a heuristic (2× epochs, 0.5× weight decay from the regularized recipe, Appendix D.4). The ensemble asymptote could shift with better tuning. This is noted in the paper but its impact on the comparison is not quantified.

2. **Distillation experiments are at a single token count (200M) and single student size (300M).** The 83% retention and the self-distillation result (green star in Figure 8) are each based on a single operating point. The paper cites theory for why self-distillation helps (Allen-Zhu & Li, 2023), but the generality across scales and model sizes is untested.

3. **The coordinate descent hyperparameter search (Appendix C.1) is described only briefly in the main text.** While appendix details are standard, the main text could more clearly state how the "locally optimal" hyperparameters were found and whether the optimum was stable across initialization or order of search. The strong claims about 30× optimal weight decay would benefit from this context.

### Trivial

None.

## Nice-to-Haves

- **Report uncertainty intervals on all asymptote estimates** (e.g., bootstrap confidence intervals or profile-likelihood intervals) so readers can assess how much the 2.29×, 3.03×, and 5.17× numbers might shift with more data or different fitting procedures.
- **Estimate the standard recipe's asymptote** under an analogous limit (e.g., extrapolating its best-tuned loss as $N\to\infty$ with fixed regularization) to enable a symmetric comparison.
- **Add more data points** in the mid-range (e.g., 400M and 800M parameters, 1B tokens) to validate the power-law form rather than relying on the minimum number of points for a 3-parameter fit.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about asymmetric comparison being "structural" and invalidating the paper's core claims.** While the asymmetry is real and noted as a major weakness, the paper provides non-extrapolated finite comparisons (2.09×, 3.75×) that support the same direction of results. The asymmetry inflates the numbers but does not invalidate the qualitative finding that regularization and ensembling improve data efficiency.

- **Criticism that the standard recipe could be improved with other forms of regularization (dropout, label smoothing).** This is speculative — the paper scoped its study to weight decay, which is the standard regularizer in pre-training. Asking for a broader regularization search is a reasonable suggestion but not a weakness of the presented work.

- **Criticism about the ensembling-vs-scaling comparison relying on a non-robust 0.09 loss difference.** The finite-scale data (Figure 4) visibly shows the ensemble advantage across all tested total parameter counts without extrapolation. The asymptote comparison is supplementary, not the sole evidence.

- **Strength Finder's claim that "data scaling laws show that improvements persist at higher token budgets" is overstated.** I rephrased this as a weakness instead: the data scaling laws rely on few points and should be treated as suggestive.

- **Generic strengths about the paper addressing an important problem.** These are removed — kept only concrete, evidence-grounded strengths.

- **Request for a limitations section.** This is standard practice but not a specific weakness of the paper's content; the paper does discuss limitations inline (e.g., "data scaling laws are expected to be noisy" at line 199).

## Novel Insights

The reviews surface a tension that the paper does not fully address: the asymptotic analysis that makes the paper novel is also its weakest link. The paper's most compelling evidence is not the extrapolated asymptotes but the finite-scale results — the 30× weight decay finding, the monotone scaling after regularization, and the ensemble advantage visible at every tested parameter count. These are robust observations that stand independently. The asymptote framework is a provocative framing device, but treating it as the paper's central quantitative contribution (as the abstract and Figure 1 do) puts the headline numbers on fragile footing. A stronger version of this paper would restructure around the finite-scale empirical findings and present the asymptote analysis as a secondary, exploratory perspective with appropriate caution.

## Suggestions

1. **Reframe the paper around the finite-scale evidence**, presenting the 2.09× and 3.75× numbers (lines 185, 189) as the primary results and the asymptote estimates as suggestive extrapolations with acknowledged uncertainty.
2. **Add confidence intervals** on every asymptote using bootstrap or profile likelihood, so readers can assess statistical significance.
3. **Estimate the standard recipe's limit symmetrically** (e.g., best achievable loss under the standard recipe with infinite compute), even if that limit is trivially large.
4. **Conduct a limited sensitivity analysis** on the power-law fitting procedure (e.g., leaving out the smallest or largest data point) to show how much the asymptote estimates change.

## Score and Decision

My round-1 bracket placed the paper between ~3.5 and ~7.5, with weak anchors near 3 and strong anchors near 8. The most topically similar anchor was the "Language models scale reliably" paper (avg 6.5, Accept Poster), which shares the scaling-law + over-training theme. That paper had far more extensive experiments (104 models) but less novel framing.

Round 2 narrowed the bracket to 5.0–6.5. Comparing against:

- **AutoScale** (avg 5.5, Reject): Similar-scale experiments with extrapolation concerns. This paper has stronger novelty (the "infinite compute" regime framing) and cleaner experiments.
- **Small-to-Large** (avg 5.25, Accept Poster): Mixed reviews, limited novelty but solid experiments. This paper contributes more novel findings (30× weight decay, ensemble advantage, distillation) but relies more heavily on extrapolation.
- **Scaling Law with LR Annealing** (avg 6.75, Reject): Had fundamental formulation issues despite sparkle. This paper has more defensible core findings but less impressive extrapolation.
- **Solvable Attention** (avg 6.75, Accept Poster): Theoretical paper with very different character. Its strengths are analytical depth, which can't be directly compared.

This paper sits near 5.5—6.0: the core empirical contributions (regularization fixes overfitting, ensembling helps at tested scales, distillation preserves gains) are well-supported and novel, but the headline quantitative claims are over-extrapolated. The paper would be a clear accept if it either reduced reliance on the asymptote numbers or provided proper uncertainty quantification. As presented, it is borderline — accepted by a narrow margin.

**Anchor papers used across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| iZeQBqJamf.md (Over-training scaling) | 6.50 | 1 | More thorough experiments (104 models) but less novel framing. This paper is weaker empirically but more novel thematically. |
| 79ZkWgY2FI.md (Small-to-Large) | 5.25 | 1,2 | Both papers have real contributions with notable limitations. This paper has more novel findings. |
| o9YC0B6P2m.md (LR Annealing) | 6.75 | 1,2 | Theoretical paper rejected for fundamental flaws. This paper's flaws are less fundamental. |
| LJ1zlaGdPm.md (Sub-Scaling) | 4.50 | 1 | Weaker paper; this paper is clearly stronger. |
| 54KcduuYeG.md (AutoScale) | 5.50 | 2 | Similar extrapolation concerns at small scale. This paper is roughly comparable or slightly stronger. |
| MLhquJb1qN.md (Time Transfer) | 5.25 | 2 | Both have interesting findings limited by experimental scope. Comparable. |
| wYxOMEzpkl.md (Solvable Attention) | 6.75 | 2 | Theoretical paper with different standards of evidence; not directly comparable. |
| FM21yYBhuE.md (Equally Critical) | 5.00 | 2 | Weaker experimental grounding; this paper is stronger. |
| 7LZjuA4AB2.md (Distribution Shift) | 3.00 | 1 | Much weaker; not comparable. |
| UldnqRQWKS.md (Mixed Quantization) | 3.00 | 1 | Much weaker; not comparable. |
| EOPLy80bBm.md (Data Pruning) | 3.00 | 1 | Much weaker; not comparable. |
| qgLyKwXVDs.md (FreeLM) | 2.00 | 1 | Much weaker; not comparable. |
| wg1PCg3CUP.md (Scaling Precision) | 8.00 | 1 | Much stronger paper with rigorous experiments at scale. |
| Tzh6xAJSll.md (Associative Memories) | 7.60 | 1 | Different type of contribution (theory); not directly comparable. |
| f4gF6AIHRy.md (Dimensional Collapse) | 8.00 | 1 | Stronger paper with more thorough evaluation. |
| PdaPky8MUn.md (Never Train from Scratch) | 8.00 | 1 | Stronger paper with more rigorous comparisons. |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>