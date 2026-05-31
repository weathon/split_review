## Summary

The paper investigates how to best train language models when compute is unconstrained but training data is fixed ("pre-training under infinite compute"). The authors show that standard data-constrained approaches (epoch repetition and parameter scaling) overfit, then address this by tuning regularization—finding the optimal weight decay is ~30× larger than standard practice—which enables monotone scaling laws. They introduce the *asymptote* of a scaling law as the appropriate metric for comparing recipes under infinite compute, and demonstrate that ensembling K independently trained models achieves a lower loss asymptote than scaling parameter count alone. Combining both axes (joint scaling recipe) achieves an estimated 5.17× data efficiency gain over the baseline, with evidence that improvements persist at higher token counts and transfer to downstream benchmarks.

---

## Strengths

- **Timely, clearly-posed question with practical relevance.** The framing that compute grows 4× per year while web data grows only 1.03× per year is well-sourced and directly motivates the research agenda. Identifying the "infinite compute" regime as a distinct setting—rather than subsuming it under existing compute-constrained or data-constrained literature—is a valuable conceptual contribution.

- **Actionable empirical finding on regularization.** The discovery that optimal weight decay is ~30× larger than standard practice (0.1 from GPT-3) for heavily over-parameterized/epoched models is surprising, practically useful, and well-supported by Figure 3 showing the transition from non-monotone to monotone scaling curves.

- **Novel and principled asymptote metric.** Proposing to evaluate recipes by the asymptote of their parameter-scaling power law, rather than at a fixed compute budget, is a natural and elegant extension of the scaling laws literature. It cleanly separates "best possible performance under this recipe" from "performance at a specific compute point."

- **Ensemble scaling laws are clean and well-fit.** The finding that loss as a function of ensemble member count K follows a power law with exponent ≈1 (matching the parameter-scaling exponent), and that ensembles achieve a *lower asymptote* than single-model parameter scaling, is a non-obvious and meaningful result.

- **Rigorous benchmark holdout design.** The authors explicitly state that downstream benchmark evaluation (PIQA, SciQ, ARC Easy) was performed only after selecting all recipes via validation loss, making benchmark scores a genuine out-of-sample test rather than a selection artifact. This methodological discipline is commendable and produces credible results (9% improvement on average).

- **Distillation retains most ensemble benefit at 8× smaller model size.** The result that distilling an 8-ensemble into a 300M student retains 83% of the ensemble improvement is a practically valuable finding, especially given the inference-cost concern for large ensembles.

---

## Weaknesses

### Fatal
None.

### Major

- **Headline data-efficiency number (5.17×) rests on nested, heavily extrapolated asymptotes.** To arrive at 5.17×, the authors must: (1) fit a power law in K over K ∈ {1,…,5} and extrapolate to K→∞, (2) fit a power law in N over N ∈ {150M, 300M, 600M, 1.4B} on those K→∞ asymptotes and extrapolate to N→∞, and (3) read off the resulting number from a data-scaling law fitted over 4 token-count points. Each extrapolation compounds uncertainty, and the authors fit three nested extrapolation steps from just four data points each. The directly observed, non-extrapolated improvements—3.75× for the best concrete ensemble of five 1.4B models—are more credible, but they receive comparatively less emphasis. A more careful treatment of extrapolation uncertainty for the 5.17× figure would strengthen the paper considerably.

- **Optimal hyperparameters for the joint scaling recipe are heuristic, not optimized.** For the inner K-limit of the joint scaling recipe (Section 4.3), the authors adopt "2× epochs and 0.5× weight decay" relative to the optimal regularized hyperparameters instead of fully optimizing them (citing experimental constraints). This is disclosed but means the joint recipe's asymptote (3.17) may be either better or worse than a fully tuned version. Since the joint recipe asymptote is the centerpiece of the 5.17× claim, this limitation is material.

### Minor

- **Experiments are at small scale (≤1.4B parameters, ≤1.7B tokens), and generalizability to production-scale training is uncertain.** The paper acknowledges this (Section 5 tests up to 1.7B tokens) and provides extrapolation evidence, but whether the same scaling exponents and asymptotic behaviors hold at 10B+ parameters or 100B+ tokens is not tested.

- **Only three downstream benchmarks, all relatively easy for models at this scale.** PIQA, SciQ, and ARC Easy are sensible choices for 150M–1.4B parameter models, but the performance improvements at these benchmarks (where models are likely near ceiling) may not reflect the full downstream benefit shown in validation loss. A few harder benchmarks would strengthen the downstream transfer claim.

- **Ensemble inference cost analysis is simplified.** The authors use total parameter count (NK) as a proxy for inference FLOPs, which is correct for arithmetic operations but ignores practical costs such as memory bandwidth, batching inefficiency, and latency for parallel ensemble members. Acknowledging that realized costs may differ from FLOPs would improve completeness.

### Trivial

- The paper notes (via footnote 1) that power law numerator constants change with unit choice. Clarifying this explicitly in-text rather than as a footnote would prevent confusion.

---

## Nice-to-Haves

- Providing bootstrap confidence intervals or error bars on the asymptote estimates (beyond the 3-seed sensitivity analysis mentioned in Appendix I.1) would make the 5.17× claim more rigorously grounded.
- Including a few harder downstream benchmarks (e.g., HellaSwag, Winogrande at small scale) would make the downstream transfer story more convincing.
- A brief analysis of how the optimal weight decay scales with the token-to-parameter ratio (rather than just N) could yield a more transferable rule for practitioners.

---

## Novel Insights

The paper surfaces two particularly non-obvious insights that extend beyond its stated contributions. First, the empirical finding that the excess loss decreases at rate ≈1/N for parameter scaling and ≈1/K for ensemble scaling—with nearly identical exponents—suggests an intriguing structural symmetry: that in the data-constrained regime, ensembles of small models and single large models are operating in complementary but equally powerful modes of capacity expansion. Second, the self-distillation result (a 300M model distilled into another 300M model outperforms the teacher) is non-trivial given widespread concern about model collapse from synthetic data. The connection to Allen-Zhu and Li (2023)'s "implicit ensembling" interpretation of self-distillation suggests a unified theoretical lens—multi-view feature learning—that ties together ensembling, distillation, and over-parameterization in the data-constrained regime, which is a genuinely synthesizing observation.

---

## Suggestions

- Explicitly report 95% confidence intervals on the key asymptote estimates (3.43, 3.34, 3.17, 5.17×) using bootstrap resampling over the scaling law fits, not just seed variance.
- Consider testing one additional larger scale point (e.g., 3B or 7B parameters at 800M-1.7B tokens) to validate that the power law exponents do not change regime.
- Clarify in Section 4.3 what range of heuristic ensemble hyperparameters was explored and how sensitive the joint asymptote is to the 2×/0.5× heuristic choice.
- For practitioners, provide a concrete recipe: given a fixed data budget D, at what N does switching from parameter scaling to ensemble scaling become preferable?

---

## Score and Decision

The paper is a careful, timely, and well-executed empirical study on an important and increasingly practical question. Its core finding—that proper regularization, ensemble scaling, and their combination produce substantial, predictable improvements under data constraints—is well-supported by systematic experiments and backed by theoretical intuition. The novel asymptote metric is a clean conceptual contribution. The primary weakness is that the headline 5.17× claim depends on three nested extrapolations from small numbers of data points, making the specific number uncertain; the directly observed 3.75× improvement is more robust and still impressive. The scale of experiments (≤1.4B parameters) is limited but appropriate given the exploratory nature of the work, and the authors provide scaling-law evidence for persistence at higher token counts. This is a solid, publishable contribution that the community working on data-efficient pre-training and scaling laws will find valuable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>