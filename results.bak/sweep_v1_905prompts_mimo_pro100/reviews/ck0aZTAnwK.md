Now I have all the information needed. Let me write the final review.

## Summary

This paper studies pre-training under data constraints with unlimited compute, proposing an asymptote-based framework for evaluating scaling recipes. The authors find that (1) standard weight decay is ~30× too small for data-constrained regimes, (2) regularized parameter scaling yields a monotone power law with asymptote 3.43, (3) ensembling achieves a lower asymptote (3.34) than parameter scaling, and (4) combining both yields a joint asymptote of 3.17—corresponding to 5.17× data efficiency over the baseline at 200M tokens. The paper further shows these gains persist across token counts via data scaling laws, can be compressed via distillation, and generalize to downstream benchmarks.

## Strengths

- **Novel evaluation framework.** The paper introduces asymptote-based recipe comparison as a principled way to evaluate scaling recipes under infinite compute—comparing the best possible loss a recipe can achieve rather than loss at a fixed compute budget. This is a genuinely new conceptual contribution for the scaling law literature (Section 3, Figures 1, 3).

- **Actionable finding on regularization.** The paper demonstrates that optimal weight decay for data-constrained, over-parameterized models is 0.8–3.2 (Figure 3, right table), over 30× the standard 0.1. This is a concrete, immediately applicable result supported by monotone power-law scaling across 4 parameter counts (150M–1.4B).

- **Ensembling outperforms parameter scaling under the asymptote framework.** The finding that ensembles of 300M models achieve a lower asymptote (3.34) than scaling a single model to infinity (3.43) is non-trivial and theoretically supported by the "multi-view" structure argument from Allen-Zhu and Li (2023). Even K=3 ensembles beat the regularized recipe's asymptote (Section 4.2).

- **Non-extrapolated evidence supports the qualitative story.** Importantly, the paper reports directly measured results alongside extrapolated ones: the best 1.4B regularized model achieves 2.09× data efficiency without any asymptote extrapolation (Section 5.1), and the best finite ensemble (5×1.4B) achieves 3.75× (Section 5.2). The qualitative narrative—regularization helps, ensembling helps more, and they compose—is well-supported by direct measurements.

- **Distillation compresses ensemble gains into smaller models.** Distilling an 8-ensemble of 300M models into a single 300M student retains 83% of the ensemble improvement (loss 3.36 vs. 3.32 for the teacher, vs. 3.57 for the regularized 300M baseline) and outperforms the regularized recipe's asymptote of 3.43 (Section 6.1). Self-distillation is also shown to be effective (Section 6.2).

- **Transparent reporting.** The paper provides both extrapolated and directly measured metrics, acknowledges the "infinite compute" framing explicitly, reports seed sensitivity (Appendix I.1: asymptotes vary by at most 0.02), and notes that the data scaling laws are "expected to be noisy."

## Weaknesses

### Fatal
None

### Major

- **Headline claims depend on power-law extrapolations from few data points.** The regularized recipe's power law is fit across only 4 parameter counts (150M, 300M, 600M, 1.4B) with exponent ~1.02, yet the headline asymptote (3.43) and the 2.29× data efficiency depend on extrapolating this to N→∞. The ensemble scaling law is fit over K=1 to 5, yet the 3.34 asymptote depends on K→∞. The joint scaling recipe's 3.17 asymptote compounds both extrapolations. With only 3–4 free parameters in each fit and 4 data points, the functional form is underdetermined—alternative fit forms could yield different asymptotes. The paper reports seed variance (±0.02) but this measures uncertainty at the data points, not model-form uncertainty in the extrapolation. While the paper is honest about providing both extrapolated and direct metrics, the abstract and introduction foreground the extrapolated 5.17× claim without adequately flagging the extrapolation layers involved. This is the central structural concern: the quantitative headline claims are only as trustworthy as these thin fits.

- **The joint scaling recipe's hyperparameter heuristic is under-explored.** For the headline 3.17 asymptote (the basis for the 5.17× claim), the inner limit uses a heuristic of "2× epochs and 0.5× weight decay" relative to the regularized recipe's optimal hyperparameters (Section 4.3, Appendix D.4), because full tuning was infeasible. This heuristic is applied to the most important result in the paper without sensitivity analysis. If the asymptote is sensitive to these heuristic choices, the 5.17× claim could shift substantially. The paper should show how the joint asymptote varies when these hyperparameters are perturbed.

### Minor

- **Limited downstream evaluation.** Benchmark evaluation is restricted to PIQA, SciQ, and ARC Easy (Section 7). While the paper commendably reports these were only evaluated after recipe selection (a strong test protocol), these are relatively easy benchmarks that may not fully characterize capability differences. The 9% improvement is meaningful, but broader evaluation would strengthen the generalization claim.

- **Data scaling laws are fit on a narrow token range.** The data scaling laws (Section 5) are fit on 4 token counts (200M–1.6B) with similar exponents (0.23–0.24) and asymptotes (1.89–1.96). The paper extrapolates to "higher token counts" but the fit range is orders of magnitude below practical pre-training scales. The similar exponents conveniently support the constant-efficiency argument but also mean small fit errors could change conclusions.

- **The exponent of 1.02 for parameter scaling warrants more discussion.** This is remarkably high compared to Chinchilla's 0.34. The paper notes this but doesn't deeply explore whether the high exponent could reflect overfitting of the scaling law itself to a narrow parameter range, rather than a genuine physical property of data-constrained scaling.

### Trivial
None

## Nice-to-Haves

- Report confidence intervals on asymptotes from the scaling law fits themselves (e.g., via bootstrap over the power law parameters), not just seed variance. This would show whether the asymptote differences between recipes (3.43 vs. 3.34 vs. 3.17) are statistically distinguishable given the fit uncertainty.
- Add 1–2 additional parameter counts (e.g., 800M, 2B) to the regularized scaling law to reduce the underdetermination of the fit.
- Develop the "multi-view" analysis further—Footnote 3 notes that slightly overfit ensemble members help, which is mechanistically interesting and deserves main-text treatment.
- Provide a compute-equivalent comparison showing whether ensemble + distillation outperforms simply training a much larger single regularized model at the same total training FLOPs.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"The 'no compute constraints' framing makes the practical contribution unclear"** — The paper explicitly frames its setting as "infinite compute, fixed data" and this is a well-defined theoretical problem. Criticizing the paper for not addressing compute-constrained settings is scope creep. The paper does discuss practical implications via distillation (Section 6), which addresses the compute concern partially. Removed.

- **"Ensemble comparison is not compute-fair at finite budgets"** — The paper explicitly compares ensembles and single models on total parameter count NK (inference FLOPs) under an infinite-compute framing. Training compute asymmetry is explicitly made irrelevant by the paper's stated scope. The "infinite compute" framing makes this a deliberate and stated design choice, not an oversight. Removed.

- **"Distillation results are more modest than framing suggests"** — The critic claims the 1.4B regularized model at ~3.46 is "close" to the distilled student at 3.36. But a 0.10 gap in loss is meaningful in language modeling, and the student (300M parameters at inference) beats the regularized asymptote of 3.43, which is the theoretical best for that recipe. The paper correctly reports these comparisons. Removed.

## Novel Insights

The paper's genuinely novel contribution is the proposal to evaluate scaling recipes via their asymptotes rather than at fixed compute budgets—a reframing specifically designed for the data-constrained, compute-unconstrained regime. Combined with the finding that standard regularization is grossly insufficient for over-parameterized data-constrained models (30× too little weight decay), and that ensembling outperforms parameter scaling under this framework, the paper opens a new axis for thinking about pre-training recipes. The observation that the data scaling exponents are similar across recipes (0.23–0.24), implying constant data efficiency ratios across data scales if the asymptotes converge under infinite data, is also a useful structural insight.

## Suggestions

1. Add sensitivity analysis for the joint scaling recipe's hyperparameter heuristic (2× epochs, 0.5× weight decay). Even a small ablation varying these factors by ±25% would substantially strengthen the 3.17 asymptote claim.
2. Report bootstrap confidence intervals on all asymptote estimates from the power law fits, making clear how much model-form uncertainty (not just seed variance) affects the headline numbers.
3. In the abstract and introduction, qualify the 5.17× claim as an extrapolation from fitted scaling laws and also foreground the directly measured 3.75× improvement from the best finite ensemble.

## Score and Decision

**Calibration anchors retrieved:**

| Round | Paper | Avg Score | Comparison |
|-------|-------|-----------|------------|
| 1 | "The Role of Task Complexity in Emergent Abilities" | 3.0 | Much weaker; rejected for limited contribution |
| 1 | "Scaling Laws for Multilingual Language Models" | 5.25 | Weaker; similar scaling law topic but minimal improvements, weaker claims |
| 1 | "A Hitchhiker's Guide to Scaling Law Estimation" | 5.20 | Weaker; methodology paper that was rejected |
| 1 | "Language models scale reliably with over-training" | 6.50 | Comparable; novel scaling law work with practical value, similar extrapolation concerns, 104 models but narrower scope |
| 1 | "Scaling Laws for Downstream Task Performance in MT" | 6.60 | Comparable; scaling law study with practical value |
| 1 | "Dataset Distillation via Knowledge Distillation" | 7.00 | Slightly stronger; novel distillation method, good experiments |
| 1 | "Analyzing Neural Scaling Laws in Two-Layer Networks" | 7.33 | Stronger; more rigorous theoretical grounding |
| 1 | "Scaling Laws for Precision" | 8.00 | Stronger; 465 runs, very thorough, validates extrapolations to 1.7B/26B |
| 2 | "How much can we Forget about Data Contamination" | 6.75 | Comparable; interesting findings but mixed reviews |
| 2 | "No Free Lunch from Random Feature Ensembles" | 5.60 | Weaker in empirical validation; contradicts this paper's finding on ensembling |
| 2 | "Double Descent Meets OOD Detection" | 6.50 | Comparable; theoretical contribution with empirical support |

**Round 1 bracket:** Between 6.0 and 7.5. The paper is clearly stronger than rejected papers in the 5.0–5.6 range (novel conceptual framework, practical findings, multiple supporting experiments) but has a more central weakness than the 7.33–8.0 papers (extrapolation from few data points).

**Round 2 narrowing:** The paper is comparable to "Language models scale reliably" (6.50) — both make novel scaling law contributions with practical value and share concerns about extrapolation. The paper under review has a more novel conceptual framework (asymptote evaluation) and stronger qualitative findings (30× weight decay, ensembling > parameter scaling), but the headline claims rest on thinner empirical evidence. It is slightly weaker than "Dataset Distillation via Knowledge Distillation" (7.00) and "Analyzing Neural Scaling Laws" (7.33), which have stronger empirical/theoretical grounding. I place the paper at 6.5, matching the "Language models scale reliably" anchor.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>