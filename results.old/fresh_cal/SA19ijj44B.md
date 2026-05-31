Now let me produce the final consolidated review.

---

## Summary

This paper presents a large-scale empirical benchmark comparing Bayesian neural network (BNN) surrogates—finite-width BNNs with HMC, SGHMC, deep ensembles, linearized Laplace, infinite-width BNNs (I-BNNs), and deep kernel learning (DKL)—against standard Gaussian process surrogates for Bayesian optimization. Across diverse synthetic and real-world problems varying in dimensionality, stationarity, and input type, the study finds that method rankings are highly problem-dependent, HMC is the best inference method for finite-width BNNs, deep ensembles perform surprisingly poorly, and I-BNNs are particularly promising in high-dimensional settings. The paper does not advocate for a single method but provides a nuanced, honest assessment.

## Strengths

- **Comprehensive empirical comparison across diverse settings.** The paper evaluates 6+ surrogate classes on 6 synthetic and 6 real-world benchmarks spanning varying dimensionality (low to high), multiple objectives, non-stationarity, and discrete/continuous inputs. The ranking visualization (Fig. 6, Sec. 4.4) summarizes a broad sweep of comparisons in one informative plot.

- **Clear demonstration that I-BNNs excel in high dimensions.** The high-dimensional experiments (Fig. 5, Sec. 4.3) on polynomial functions, neural network draws, and knowledge distillation show I-BNNs consistently outperforming GPs and all other BNN variants. This is a novel and practically useful finding grounded in specific experimental evidence.

- **Rigorous evidence that HMC is the best finite-width BNN inference method.** On synthetic benchmarks (Fig. 3) and real-world problems (Fig. 4), HMC consistently achieves higher rewards than SGHMC, deep ensembles, and linearized Laplace. The paper backs the claim with multiple experiments rather than cherry-picked results.

- **Useful sensitivity analysis of architectural choices.** Section 3.1 (Figs. 1–2) systematically varies network depth, width, prior variance, and likelihood variance, showing how these affect posterior predictive distributions and BO performance. This provides practical guidance for practitioners.

- **Ablation study on mean vs. uncertainty quality.** Section 4.5 constructs hybrid models that swap mean and uncertainty estimates between surrogates, revealing that HMC and I-BNNs tend to have better mean estimates while GPs have better uncertainty estimates. This deepens understanding beyond aggregate performance numbers.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No formal statistical testing of observed differences.** The paper reports means and standard errors over 10 trials (which is standard practice) but provides no hypothesis tests (e.g., paired t-tests, Wilcoxon signed-rank tests, or multiple-comparison corrections) to assess whether differences between methods are statistically significant. Many comparative claims (HMC best among finite BNNs, deep ensembles underperform, I-BNNs dominate in high dimensions) are supported by visual inspection of plots. While unlikely to overturn the main conclusions, formal testing would strengthen confidence, especially for borderline cases where confidence intervals overlap. This is a common limitation in benchmarking papers but worth noting.

- **The ranking metric definition contains a minor textual ambiguity.** Line 310 reads: "The score of model with maximum reward is $(r_i - r_h) / (r_h - r_l)$." This appears to mean "The score of model i" rather than "model with maximum reward." The intended formula produces scores from 0 (best) to −1 (worst), which is reasonable, but the wording could confuse readers. This is a small presentation issue.

### Trivial

None.

## Nice-to-Haves

- A dedicated "Limitations" subsection would help readers understand the study's scope (e.g., which BNN methods were excluded, acquisition function choices, computational budget considerations). The current Discussion section touches on these implicitly but would benefit from explicit treatment.

- For the high-dimensional experiments, additional analysis on *why* I-BNNs outperform (better mean estimates vs. better uncertainty vs. stronger prior) would strengthen the contribution. The hybrid model ablation hints at this but is not fully connected to the high-dimensional finding.

- A summary table reporting final mean rewards with confidence intervals across all benchmarks would complement the visual figures and help readers make quantitative comparisons.

## Removed Points

These points were raised in the reviews but are removed or demoted for the reasons given; treat them with caution:

- *"Deep ensembles evaluation may be unfairly pessimistic because the paper does not specify how many ensembles were used or how they were trained (defers to the appendix)."* **Removed.** Hard rule: nitpicks about undisclosed hyperparameters and missing appendix content are not valid criticisms. Additionally, the paper already provides a mitigating experiment (large-query setting, Sec. 4.5) showing that ensemble performance improves with more data, directly addressing the concern.

- *"The 'standard GP' baseline may be too restrictive."* **Demoted to Nice-to-Have.** The paper's own Section 4.6 (Revisiting Standard Assumptions) directly investigates this concern by comparing Matérn vs. RBF kernels and marginalization vs. optimization, finding no consistent advantage for alternative specifications. The concern is acknowledged but the paper provides evidence that it does not change the conclusions.

- *"Missing discussion of variational inference, MC dropout, SWAG."* **Removed.** The paper's scope is clearly stated as a broad but not exhaustive study; it covers 6+ inference classes. Criticizing the omission of further methods is scope creep.

- *"Architecture sensitivity study only uses HMC."* **Removed.** The paper explicitly motivates this (line 136: HMC is the gold standard). Testing all architecture variants across all inference methods would be prohibitively expensive and is not required for a valid sensitivity study.

- *"The claim of 'exhaustively evaluating' is an overstatement."* **Removed.** This is a minor rhetorical over-claim common in papers and not a substantive weakness. The study covers an impressively wide range of methods.

## Novel Insights

The main novel insight from the review synthesis is that the paper's principal contribution—showing that I-BNNs excel in high-dimensional BO where standard GPs struggle—is well-supported and not seriously contested by any reviewer. The secondary insight about deep ensembles underperforming in the small-data BO regime is also consistent across reviewers. The reviews converge on the assessment that the paper's weaknesses (statistical rigor, scope limitations) are real but do not undermine the core findings; rather, they point to natural improvements for a stronger version of the paper.

## Suggestions

1. Add a statistical summary table with mean final rewards and 95% bootstrap confidence intervals (or critical difference diagrams) for all surrogate-model × benchmark combinations. This would complement the visual plots and address the statistical-rigor concern without requiring formal hypothesis tests.

2. Fix the ranking metric description (line 310) to read "The score of model i is $(r_i - r_h) / (r_h - r_l)$" for clarity.

3. Add a brief "Limitations" subsection to the Discussion that acknowledges: (a) the study's scope relative to the full space of BNN inference methods, (b) reliance on qEI as the sole acquisition function, and (c) how conclusions might shift with larger query budgets or different problem families.

## Score and Decision

The paper provides a thorough, well-designed empirical study that fills a genuine gap in the Bayesian optimization literature. The weaknesses identified are minor—lack of formal statistical testing is standard practice in this field and does not undermine the clearly demonstrated findings. The contribution is substantial: it gives practitioners concrete guidance on when to use which surrogate type, and it identifies I-BNNs as a promising direction for high-dimensional BO. I recommend acceptance.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>