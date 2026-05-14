**Calibration Anchors Used for Scoring**

I retrieved the following human reviews from the corpus. For each I report the path, the average human score, and a one-sentence comparison to the paper under review.

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `3YKeB9R1g9.md` (Scaling with Collapse) | 8.0 | Much stronger — thorough multiscale experiments, practical diagnostics, trained a new LLM family; the current paper has a narrower scope. |
| `FMjeC9Msws.md` (ScaleRL) | 7.5 | Stronger — 400k GPU-hour study with rigorous validation; the current paper has less empirical depth. |
| `x54wwB6QvL.md` (Scaling Laws Revisited – Data Quality) | 6.0 | Comparable — both extend scaling laws with a new framework (data quality asymptote framework), both limited to small models (~150M). The current paper covers more experimental dimensions. |
| `0BkvUY61MX.md` (ATLAS) | 5.33 | Comparable — both make novel contributions but have some review disagreement. ATLAS has more experiments (774 runs) but the current paper has cleaner narrative. |
| `nrVbL1CK1A.md` (Bootstrapped Pretraining) | 4.0 | Weaker — similar scale limitations (1.1B max) but the current paper has stronger qualitative findings and more honest limitation reporting. |
| `pJcHaD3mvn.md` (Extrapolating Large Models) | 4.0 | Weaker — serious writing and theoretical issues; the current paper is better presented and more empirically grounded. |

---

## Summary

This paper studies pre-training under data constraints with no compute constraints — a timely framing given that compute grows ~4×/year while web text grows ~1.03×/year. The authors find that standard data-constrained recipes (epoching + parameter scaling) overfit, and show that tuning weight decay ~30× higher than the standard 0.1 default restores monotone power-law scaling. They introduce the *asymptote* of a scaling law as a metric for comparing recipes under infinite compute, demonstrate that ensembling independently trained models achieves a lower asymptote than scaling a single model, and show that distillation preserves most gains in smaller models. Data scaling laws suggest the efficiency improvements persist at higher token counts.

---

## Strengths

1. **The problem framing is well-motivated and the asymptote evaluation framework is novel.** The paper correctly identifies that as compute outpaces data growth, we need new ways to evaluate pre-training recipes — comparing asymptotes rather than compute-optimal points is a sensible proposal. The framework cleanly separates the question of "how good can this recipe get?" from "how much compute does it cost?"

2. **The finding that optimal weight decay is ~30× standard practice for over-parameterized models is concrete and actionable.** Figure 3 shows that jointly tuning weight decay, learning rate, and epoch count yields monotone power-law scaling across models up to 140× the Chinchilla parameter-to-token ratio, directly contradicting the decaying scaling laws reported by Muennighoff et al. (2023). This is a clear empirical finding with immediate practical value for practitioners training at extreme parameter-to-token ratios. The ablation in Appendix C.2 (Figure 10) convincingly shows that naive hyperparameter transfer across scales breaks monotonicity, underscoring the need for per-scale tuning.

3. **The ensemble scaling analysis (Section 4) provides clean evidence that ensembling achieves a lower loss asymptote than parameter scaling at the same total parameter count.** Figure 4 shows that even a K=3 ensemble of 300M models outperforms the asymptote of the regularized single-model recipe. The comparison between scaling N and scaling K at matched parameter totals is one of the paper's strongest experiments.

4. **Distillation preserves ensemble gains in smaller models (Section 6).** Distilling an 8-ensemble into a 300M student retains 83% of the ensemble loss improvement, and the self-distillation result (matching the regularized asymptote without training larger models) is a practically significant finding even if the mechanism deserves more analysis.

5. **Transfer to downstream benchmarks and continued pre-training.** Figure 9 confirms that validation loss improvements translate to downstream accuracy (9% average improvement). Appendix A provides a clean external validation on a different setting (OctoThinker CPT with a 3B model), showing a 17.5× data efficiency win. This demonstrates the findings are not an artifact of the specific pre-training-from-scratch setup.

6. **The paper is honestly written.** The authors acknowledge the non-standard 1.4B architecture (Appendix C.5), advise taking asymptotes "with a grain of salt" (Appendix I.1), and provide a sensitivity analysis showing asymptote variation ≤0.02 loss across seeds (Figure 20). This transparency should be credited.

---

## Weaknesses

### Fatal
None.

### Major

1. **Scaling laws are fit from very few data points, making the quantitative claims (specific asymptote values, 5.17× efficiency number) statistically fragile.** The parameter scaling law in Figure 3 uses 4 model sizes and 3 free parameters (A, α, E), yielding 1 degree of freedom. The data scaling laws (Figures 6, 7) cascade multiple such fits: the joint scaling recipe uses a three-tier stacking of power laws, each tier with ~4 points. With so few degrees of freedom, the excellent R² values (>0.999, reported in Appendix K.3.1) are expected and do not indicate robustness. *The authors are transparent about this* — Appendix I.1 explicitly advises taking asymptotes "as rough estimates" — but the headline quantitative claims (5.17× data efficiency, specific asymptotes of 3.43, 3.34, 3.17, the exponent comparisons to Chinchilla) are presented as results rather than rough estimates. This creates a mismatch between the strength of the evidence and the precision of the claims. The extrapolation validation (Appendix K.3.2, predicting 1.5B and 3.2B models within 0.005–0.008 loss) is encouraging but only tests the parameter scaling fit, not the three-tier data scaling cascade.

2. **The 1.4B model has a non-standard architecture (16 layers vs. 24 for the 600M model), breaking the clean scaling curve in the main paper.** The authors acknowledge this (Appendix C.5) and add 1.5B/3.2B models with proper aspect ratios in Appendix K.1 during rebuttal. The extrapolation validation shows the power law holds, partially addressing this concern. However, the main body and key figures (Figures 3, 5, 6) fit scaling laws using the 1.4B point as part of the 4-point curve, meaning those fits are partially contaminated by an architecture that is not on the same scaling curve. The rebuttal additions are a fix, but they do not retroactively clean the original fits.

### Minor

3. **The self-distillation result (student outperforming teacher by 0.27 loss) is under-analyzed given its surprising nature.** The paper cites Allen-Zhu and Li (2023) for a theoretical explanation and shows that mixing real and synthetic data is critical (Appendix F.3), but this is a striking result — a same-size student outperforming its teacher — that directly contradicts standard intuitions from the model collapse literature (which the authors cite). A deeper analysis (e.g., measuring the diversity of synthetic generations, tracking how the student's predictions differ from the teacher's over training, or testing whether the finding generalizes across data sources) would significantly strengthen the claim.

4. **The "30× larger than standard practice" framing is slightly imprecise.** The optimal weight decay varies from 0.8 (150M) to 3.2 (600M, 1.4B), while the "standard" 0.1 comes from Brown et al. (2020). The ratio is indeed as large as 32× for the 600M model, but only 8× for the 150M model. The optimal weight decay trends with model size in a way the paper notes but does not explain — understanding this mechanism (e.g., is it about memorization capacity, effective regularization per parameter, or something else?) would make the result more actionable.

5. **The downstream evaluation is limited to relatively simple benchmarks.** The initial set (PIQA, SciQ, ARC Easy) is standard for models at this scale, and additional benchmarks are added in Appendix K.4. However, for a paper making claims about "data efficiency gains [that] will persist at higher token counts," broader evaluation (e.g., on reasoning or knowledge-intensive tasks) would strengthen the case that validation loss improvements translate to capabilities of interest.

6. **The heuristic for ensemble hyperparameter tuning ("double epochs, half weight decay") is validated on limited settings and has a known counter-example (1.4B, 200M tokens).** The authors acknowledge this counter-example (Appendix D.4) and report using the best run instead for that setting. This is honest, but it raises questions about how reliably the heuristic transfers to novel configurations.

### Trivial
- The asymptote values in the abstract/introduction (e.g., 3.43, 3.34, 3.17) are presented with two decimal places, implying precision that is not supported by the underlying fits. Adding explicit uncertainty intervals (e.g., 3.43 ± 0.02, which the sensitivity analysis supports) would better communicate the true confidence.

---

## Nice-to-Haves

- **Vary the order of limits systematically.** The paper compares asymptotes from different scaling directions (N→∞ vs. K→∞ vs. both). An obvious complementary experiment is to compare recipes at matched *total parameter budgets* (e.g., single 1.4B model vs. 2×700M ensemble), which would directly test whether ensembling beats scaling without relying on asymptote extrapolation. The paper does this partially in Figure 4 but could extend the analysis.
- **Validate the data scaling law predictions with a held-out token count** (e.g., 1.2B tokens) not used in the fits. The paper does this for parameter scaling (Appendix K.3.2) but not for the data scaling cascade.
- **Decompose why varying data order alone captures most of the ensemble benefit.** Understanding whether this is about exposure to different patterns vs. different local minima could guide cheaper ensemble strategies.

---

## Removed Points

- **Criticism that asymptote comparisons are ill-motivated / conflate multiple limits.** (Harsh Critic point 2). The paper is explicit about what each limit represents (Section 4.3, Appendix D.6) and why comparing them is meaningful under the "no compute constraints" framing. The comparison between different scaling directions is exactly the paper's central methodological contribution.
- **Criticism that the teacher model in Table 4 is inconsistent with Figure 8.** The teacher in Table 4 (loss 3.71) is the 1-ensemble, not the regularized 300M model (loss ~3.57). Appendix F.1 explicitly clarifies this distinction and reports that both choices yield similar self-distillation results (3.43 vs. 3.44).
- **Criticism about the Muennighoff et al. characterization.** The paper provides a specific citation to their Appendix D. The distinction between "overfit runs" and "diverging runs" is too fine-grained and the paper's claim is supported by a cited reference.
- **Criticism that Appendix A results are "relegated to an appendix" suggesting lack of confidence.** This is external validation that strengthens the paper; placement in an appendix is standard for secondary experiments.
- **Formatting/style nitpicks** about grammar, typos, whitespace (these are parser artifacts).
- **Generic strengths** from the Strength Finder that were superficial or generic (none were flagged as such — all strengths are specific and backed by citations).

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a novel observation that the paper itself does not make. The synthesis confirms that the paper's main strengths (asymptote framework, weight decay finding, ensemble scaling) and main weaknesses (statistical thinness of quantitative scaling laws) are accurately reflected in the paper's own presentation.

---

## Suggestions

1. **Add explicit confidence intervals to all asymptote values.** The sensitivity analysis (Appendix I.1) shows seed-to-seed variation ≤0.02 loss — this should be reported alongside every asymptote (e.g., 3.43 ± 0.02). The headline "5.17× data efficiency" should be accompanied by a plausible range.

2. **Acknowledge the statistical fragility of the quantitative claims more prominently — in the abstract or Section 1, not just in Appendix I.1.** The qualitative findings (regularization helps, ensembling helps, distillation preserves gains) are robust; the precise numbers are not. The paper would be stronger if it explicitly separated these tiers of evidence.

3. **Provide a deeper analysis of why self-distillation works when model collapse theory says it shouldn't.** Specifically: measure whether the diversity of synthetic generations decreases over training, and test whether the finding holds across data sources (e.g., Wikipedia vs. web text) and different mixing ratios beyond the one studied.

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>