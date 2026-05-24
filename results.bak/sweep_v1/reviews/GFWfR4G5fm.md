Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper identifies three fundamental limitations of static Supervised Causal Learning (SCL) — fragility to distribution shifts, compositional generalization failure, and synthetic-to-real transfer gap — and proposes Test-Time Training for SCL (TTT-SCL), a framework that dynamically generates training data aligned to each test instance. The authors instantiate this framework via TACTIC, which performs a stochastic search over causal graphs using an Alignment of Distribution (AD) metric plus sparsity penalty, generates training data from the discovered graphs, and trains an SCL model to predict the test graph. Experiments on synthetic, pseudo-real (SynTReN), and real-world (Sachs) data show TACTIC achieves strong AUROC, outperforming prior SCL and traditional methods on most benchmarks.

## Strengths

1. **Systematic experimental diagnosis of SCL limitations.** The paper provides concrete evidence (Figure 2, Table 1) for three distinct failure modes: distribution shifts along graph/mechanism/noise axes degrade AUROC substantially, models fail to compositionally generalize to unseen combinations of seen components, and strong synthetic performance (AVICI: 97.8 on RFF_G) fails to transfer to real data (62.3 on Sachs). This analysis is thorough, well-controlled, and valuable to the community independent of the proposed method.

2. **The TTT-SCL framework is a conceptually novel paradigm.** The shift from static "diversity"-seeking pre-training to dynamic "concentration"-via-test-time-adaptation cleanly reframes the SCL generalization problem. The idea of dynamically generating training data that is causally aligned to the test instance, rather than hoping the pre-training distribution covers the test case, is well-motivated and opens a new direction for SCL research.

3. **TACTIC achieves strong empirical results on challenging benchmarks.** TACTIC (Notears) achieves SOTA AUROC on 4 of 5 datasets (Linear_U: 86.3, Chebyshev_G: 83.0, Sachs: 78.9, SynTReN: 80.1), substantially outperforming both traditional methods (PC, GES, NOTEARS) and the strongest SCL baseline (AVICI) on non-in-distribution settings. Performance on the real-world Sachs dataset (+16.6 AUROC over AVICI) is particularly notable.

4. **Sparsity ablation is clean and informative.** Table 3 shows that removing the sparsity penalty causes consistent degradation across all settings (e.g., Sachs drops from 78.9 to 63.5), validating the claim that preventing degenerate dense solutions is important for training data quality.

## Weaknesses

### Major

- **The stage-wise analysis (Table 4) does not isolate whether SCL training adds value beyond ensembling multiple candidate graphs.** The paper claims the SCL step provides "Learning Improvement" (2→3 in Table 4) by comparing the highest-score single graph (88.9 on RFF_G) against the SCL model trained on 200 graphs (91.8). However, this conflates two factors: using more graphs and the SCL learning process itself. A proper control would aggregate the top-K search graphs directly (e.g., average adjacency matrices or majority-vote prediction) and compare that to the SCL output. Without this baseline, the paper cannot support the claim that the TTT-SCL paradigm (generating data → training SCL) is more beneficial than simply combining the search outputs. Since this claim is central to distinguishing TACTIC from classical score-based discovery, the gap is significant.

- **Potential information leakage.** The SCL model is trained on data generated from graphs that were explicitly scored against D_test via the AD metric. The model then makes predictions on the same D_test. This creates a feedback loop: the training data is information-theoretically dependent on the test data, so the SCL model may partially be overfitting to D_test rather than learning causally meaningful mappings. The paper does not discuss or control for this (e.g., by holding out a portion of D_test during the search phase).

### Minor

- **Anomalous search behavior on Linear_U is unexplained.** In Table 4, the highest-score graph found during search (80.1 AUROC) is *worse* than the seed graph (82.0) on Linear_U. This suggests the search degraded performance for this setting, and the final SCL output (86.3) appears to "rescue" it. The paper should discuss why the search underperforms the seed here and whether this pattern holds across runs. This is relevant for understanding when the search procedure is reliable.

- **The AD metric (Equation 3) is underspecified.** The paper states "log p(X_i | f_i^k)" but does not specify the exact form of the likelihood (e.g., Gaussian with estimated variance? Residual MSE converted to likelihood?). The acceptance ratio in the stochastic refinement (Figure 3) uses a ratio of scores that is not a proper Metropolis-Hastings acceptance probability since the score is not a log-probability. While the heuristic works, the presentation implies more principled grounding than is provided. These details matter for reproducibility.

- **Gaussian noise assumption for generated training data.** The paper states "we set the noise distribution to a standard Gaussian distribution by default" (Section 4.2). For test instances with non-Gaussian noise (e.g., Linear_U uses uniform noise), the generated training data has a distributional mismatch with the test data. The paper does not discuss the impact of this assumption or whether alternative noise specifications were considered.

- **AVICI outperforms TACTIC on RFF_G (97.8 vs 91.8).** The paper acknowledges this is because AVICI was trained on RFF_G, so it is not a weakness per se, but it does show that TACTIC does not universally dominate the strongest SCL baseline even after test-time adaptation.

### Trivial

- None beyond what is covered above and in Removed Points.

## Nice-to-Haves

- Perform the missing control experiment: aggregate the top-K search graphs (e.g., average adjacency matrices) and compare to the SCL output. If the ensemble is comparable, the core contribution needs reframing.
- Sensitivity analysis for the sparsity weight λ.
- Assess information leakage via a held-out split of D_test during search.
- Analysis of why the search degrades performance on Linear_U.
- Discussion of non-Gaussian noise settings for training data generation.

## Removed Points

These points were raised in reviews but removed after verification against the paper:

- **"AUROC is insufficient for sparse graphs"** — The paper explicitly states (Section 4.3) that AUPRC, F1, and ACC are reported in Appendix D. The criticism is addressed by the paper.
- **"Not comparing AD against alternative similarity metrics"** — The AD metric is presented as an operationalization choice within the TTT-SCL framework, not as a novel metric. Criticizing the absence of comparisons to KL divergence, MMD, or Bayesian scores is scope creep; the paper's claim is about the framework, not about AD being a novel metric.
- **"Comparison against score-based methods using same score function"** — The paper does compare against NOTEARS, GES, and other score-based methods (Table 2). The critic's request for "NOTEARS with BIC" is a minor variant that does not change the conclusions.
- **Formatting nitpicks** about broken characters, line breaks, and other parser artifacts were removed per protocol — these are PDF extraction issues, not author errors.
- **Generic demands for larger-scale experiments (d=50, d=100)** — The paper is evaluated within its stated scope (d=10-20). Scaling is a natural next step, not a flaw in the existing evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the important observation that the current evaluation confounds ensembling with SCL learning, but this is a limitation to be addressed rather than a novel insight.

## Suggestions

1. **Crucial: Add a top-K ensemble baseline** for the stage-wise analysis. For each test instance, average the adjacency matrices of the top-K graphs (by score) from the search and compute AUROC. If this ensemble matches the SCL output, the paper should reframe the contribution — the benefit may be from using multiple candidate graphs, not from SCL-specific learning. If the SCL output still outperforms, the claim is strengthened considerably.
2. **Address information leakage** by discussing the issue explicitly and, if possible, adding a control experiment (e.g., hold out a subset of D_test from the search phase).
3. **Specify the likelihood form** in Equation (3) — what distribution family, how variance is estimated — and clarify that the Metropolis-like acceptance ratio is a heuristic rather than a proper MH step.
4. **Discuss the Linear_U anomaly** (seed > highest-score graph) and whether this is systematic or a rare occurrence.
5. **Add sensitivity analysis for λ** (sparsity weight) to show that the chosen value is not cherry-picked.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Human Score | Comparison |
|---|---|---|
| AvXrppAS2o ("The best of both worlds: Improved outcome prediction using causal structure learning") | 3.00 | Much weaker paper — marginal improvements over baselines, limited evaluation, unclear contributions. Current paper is substantially stronger in problem analysis, method novelty, and experimental breadth. |
| lQYi2zeDyh ("Demystifying amortized causal discovery with transformers") | 5.00 | Similar quality level — both papers make genuine contributions but have notable limitations (this one: bivariate-only scope; current: evaluation gap in stage-wise analysis). Current paper has broader experimental scope but a more significant methodological gap. |
| ZXs3pkmrRG ("Test-Time Learning of Causal Structure from Interventional Data") | 5.50 | Closest topical match (TTT+SCL for causal discovery). Similar strengths (clear writing, thorough experiments) but the TICL paper also faced concerns about framing and contribution clarity. The current paper has a stronger problem motivation and more interesting findings (compositional failure) but the evaluation gap on the SCL vs. ensemble question is a larger weakness. |
| 4wk2eOKGvh ("Test-Time Ensemble via Linear Mode Connectivity") | 6.50 | Cleaner evaluation and methodology. The current paper's problem analysis is more original, but the evaluation is less rigorous. |
| YHUGlwTzFB ("Active Test-Time Adaptation: Theoretical Analyses and An Algorithm") | 6.75 | Stronger paper with theory + thorough experiments. Current paper is below this level due to the evaluation gap. |

The paper has genuine contributions — the problem diagnosis is excellent, the TTT-SCL framework is conceptually novel, and TACTIC achieves strong empirical results. However, the central claim that the SCL training step adds value beyond the search is not adequately supported (the stage-wise analysis conflates ensembling with learning), and the information leakage concern is unaddressed. These are substantive gaps that the authors should resolve, but they do not invalidate the paper's overall contribution. Relative to anchors, this paper sits between the medium and stronger papers — comparable to the TICL paper (avg 5.50) but with a more significant evaluation gap, placing it slightly below.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>