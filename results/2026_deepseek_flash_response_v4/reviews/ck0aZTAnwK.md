## Summary

This paper studies language model pre-training in a data-constrained, compute-unconstrained regime—a scenario motivated by the observation that compute grows 4×/year while web text grows only 1.03×/year. It shows that standard data-constrained recipes (epoching + parameter scaling) overfit; that tuning weight decay 30× higher than standard practice enables monotonic parameter scaling and a well-defined asymptote; that ensembling independently trained models achieves a lower loss asymptote than infinite single-model parameter scaling; and that these gains compose into a joint scaling recipe estimated to be ~5× more data-efficient. The paper also shows these gains survive distillation into smaller models and transfer to held-out downstream benchmarks.

## Strengths

1. **Concrete, actionable finding about weight decay.** Section 3 (Figure 3, lines 97–101) reports optimal weight decay values of 0.8–3.2 for models from 150M to 1.4B parameters, versus the standard default of 0.1 from Brown et al. (2020). This 30× increase is a specific, testable recommendation for practitioners facing data-constrained pre-training.

2. **Clean identification of a flaw in prior data-constrained scaling laws.** Section 2.1 (lines 56–58) empirically shows that the data-constrained scaling law of Muennighoff et al. (2023) fails because it discards overfit runs. Figure 2 (left) shows loss rising after 8 epochs, directly contradicting the monotonic-decay assumption, and the paper cites the prior work's own acknowledgment of this practice.

3. **Ensembling beats parameter scaling at equal parameter budget.** Figure 4 demonstrates that scaling ensemble members (K → ∞) achieves asymptote 3.34, lower than the regularized infinite-parameter asymptote of 3.43. Even a K=3 ensemble of 300M models beats the regularized asymptote (line 133). This is a non-trivial reversal of conventional scaling intuition.

4. **Held-out downstream evaluation.** Section 7 (lines 229–233) confirms that no downstream benchmarks were evaluated until after all recipes were selected via validation loss, making the reported 9% improvement on PIQA, SciQ, and ARC Easy a genuinely held-out test rather than a post-hoc selection artifact.

5. **Distillation preserves ensemble gains in a smaller student.** Distilling an 8-ensemble of 300M models into a 300M student preserves 83% of the ensemble's loss improvement (lines 211–213) and beats the regularized recipe's asymptote (3.43), showing the theoretical gains are practically realizable under inference-parameter constraints.

## Weaknesses

### Fatal
None.

### Major

1. **Power-law asymptotes are weakly constrained, undermining the precision of headline quantitative claims.** The paper fits functions L(D) = A/D^α + E with three free parameters to just four data points per recipe (200M, 400M, 800M, 1.6B tokens — lines 91, 173). With 4 points and 3 parameters, each fit has 1 degree of freedom. The asymptote E — the central quantity for all headline claims — represents the limit D → ∞, yet the data spans only a factor of 8 in D. The joint scaling recipe's 5.17× figure (lines 9, 185) involves a double limit (K → ∞ then N → ∞) built from composing power-law fits at three levels (Figure 7), each with a handful of points. The paper acknowledges noise ("Although the data scaling laws are expected to be noisy," line 195) and provides run-to-run variance in Appendix I.1 (line 113), but does not report fit uncertainty (standard errors or confidence intervals) on the asymptote or exponent parameters. The precision implied by "5.17×" is not commensurate with the evidence.

2. **Joint scaling recipe uses untuned hyperparameters.** Section 4.3 (line 143) states: "we cannot fully find locally optimal hyperparameters due to experimental constraints. Instead, we use the heuristic of taking the optimal regularized hyperparameters with 2× epochs and 0.5× weight decay." The best reported data efficiency (5.17×) depends on this recipe, yet we have no measure of how much better a properly tuned version would be — or whether the gap relative to the baseline would hold at all under proper tuning. This is a significant gap for the paper's most impressive quantitative claim.

### Minor

1. **Limited downstream evaluation.** The paper evaluates on three benchmarks (PIQA, SciQ, ARC Easy) described as "informative for models at our scale" (lines 229–233). While this is acknowledged, the set is small and these are relatively simple tasks. It is unclear whether the data efficiency gains transfer to more challenging evaluations.

2. **No confidence intervals on scaling law exponents.** Section 5.3 claims "all recipes decay at a similar rate with exponents between 0.23 and 0.24" (line 195), but no confidence intervals or standard errors are reported. With ~4 data points per fit, these intervals would be wide; reporting them would help assess whether the similarity is robust or coincidental.

3. **Practical value of the asymptote is modest for the regularized recipe alone.** At 200M tokens, the best measured regularized 1.4B model achieves loss ~3.46, while the asymptote is 3.43 (Figure 3) — a difference of only ~0.03 loss. The asymptote adds conceptual clarity, but the practical improvement over the largest measured model is small for this recipe.

### Trivial
None.

## Nice-to-Haves

- Reporting compute cost (total FLOPs) for each recipe would help contextualize the engineering effort for readers interested in practical adoption, though the paper's explicit framing (no compute constraints) means this is outside its core scope.

## Removed Points

These points from the reviews were removed with justification:

- **"Never reporting compute cost"**: Removed because the paper's explicit framing is "no compute constraints" (title, abstract, line 15, line 50). The premise is to study what is best when compute is not a limitation; asking for compute-efficiency reporting conflicts with this framing.

- **"Distillation evaluation conflates comparisons"**: Removed because the comparison is clearly stated: the 83% metric compares the distilled 300M student against the regularized 300M single-model baseline (line 213) — the natural baseline for a same-size student. The ensemble is the teacher, not the baseline being compared against.

- **"'No compute constraints' premise inconsistently applied"**: Removed because the paper's practical limitation ("we cannot fully find locally optimal hyperparameters due to experimental constraints") is about experimental budget, not a contradiction of the conceptual premise.

- **"Ensemble vs asymptote comparison is apples-to-oranges"**: Removed because comparing a finite ensemble's performance to an asymptotic limit is exactly the paper's methodological contribution — the asymptote is the relevant metric under no compute constraints.

- **"Compute growth rate data cited with uncertainty"**: Removed because the paper cites a published external source (Villalobos et al., 2024); speculating about uncertainty in that source is not a problem with the paper under review.

- **"Missing appendix" style points**: Removed per protocol — the appendix is stripped by the parser.

## Novel Insights

The reviews converge on a useful characterization: the paper's qualitative findings (regularization helps via 30× weight decay, ensembling helps more than parameter scaling, distillation preserves gains) are well-supported and likely robust. However, the precision of the 5.17× headline number is not commensurate with the evidence — it rests on several layers of power-law fits each constrained by very few data points. The paper's contributions would benefit from being reframed around the qualitative results, with the multipliers presented as rough estimates with appropriate caveats. The weight decay finding (30× standard practice) is the most directly actionable and best-supported result in the paper.

## Suggestions

1. Add confidence intervals (bootstrapped or via standard error propagation) on all asymptote estimates, and report the full fitted parameters with uncertainties in a table.
2. For the joint scaling recipe, either tune hyperparameters properly for ensemble members or explicitly characterize how much the heuristic suboptimality could affect the estimate (e.g., via a sensitivity study).
3. Reframe headline claims to emphasize the qualitative result (ensembling beats parameter scaling; regularization enables monotonic scaling) rather than foregrounding the precise multiplier 5.17×, which is not robustly determined from 4 data points per fit.
4. Consider reporting error bars on the scaling law exponent comparison (Section 5.3) to substantiate the claim that all recipes decay at similar rates.

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| OW5Gf4cse1 (emergent abilities) | 3.00 | R1 | Much weaker — no actionable findings, rejected with low scores |
| EOPLy80bBm (data pruning) | 3.00 | R1 | Much weaker — more narrow contribution |
| SaOxhcDCM3 (self-consuming loop) | 3.20 | R1 | Weaker — controversial scoring (5,5,5,10) |
| **xGM5shdGJD (Hitchhiker's Guide)** | **5.20** | R1/R2 | Weaker — methodological study with ill-formed metric; no actionable findings |
| T2h2V7Rx7q (Multilingual Scaling) | 5.25 | R1/R2 | Weaker — small improvements, overclaims |
| **79ZkWgY2FI (Small-to-Large Generalization)** | **5.25** | R2 | Comparable — accepted with average scores, but this paper has more novel findings |
| **i7oU4nfKEA (Multilinguality Curse)** | **6.25** | R2 | Comparable — rejected despite extensive experiments; this paper has more surprising findings |
| **iZeQBqJamf (Over-training Scaling)** | **6.50** | R1/R2 | Stronger — more rigorous experiments (104 models), cleaner validation |
| vPOMTkmSiu (MT Scaling) | 6.60 | R1/R2 | Stronger — accepted with mixed reviews (3,6,8,8,8) |
| wg1PCg3CUP (Precision Scaling) | 8.00 | R1 | Much stronger — unanimous high scores, rigorous methodology |

**Round 1 bracket:** Between 3.5 and 7.5 (middle band).

**Round 2 narrowing:** The paper sits between the Hitchhiker's Guide (5.20, weaker methodology focus, no actionable findings) and the Over-training Scaling paper (6.50, more rigorous experiments). It is comparable to Small-to-Large Generalization (5.25, accepted) and the Multilinguality Curse paper (6.25, rejected for unsurprising results despite massive experiments). The paper's novel and actionable findings raise it above the Hitchhiker's Guide, but the weak quantitative validation prevents it from reaching the Over-training Scaling paper's level.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>