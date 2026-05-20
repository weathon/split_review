Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper identifies three limitations of static Supervised Causal Learning (SCL)—fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap—and proposes a paradigm shift to test-time concentration. The core contribution is TTT-SCL, a framework that dynamically generates training data aligned with each test instance via a likelihood-based Alignment of Distribution (AD) metric combined with an L0 sparsity constraint. The instantiated method, TACTIC, uses stochastic graph refinement seeded by NOTEARS to produce K=200 training graphs, then trains an SCL model on forward-sampled data from these graphs. Experiments on synthetic, pseudo-real (SynTReN), and real-world (Sachs) benchmarks show TACTIC achieving 78.9 AUROC on Sachs and 80.1 on SynTReN, substantially outperforming both traditional methods (PC, GES, NOTEARS) and the pre-trained SCL baseline AVICI (62.3, 65.4).

## Strengths

- **Systematic identification and empirical demonstration of three fundamental SCL limitations.** The paper provides clean, quantitative evidence that static SCL models degrade under distribution shifts (Fig. 2, with drops of 10–58 AUROC points), fail at compositional generalization (Component-mixed vs i.i.d. drops of 3–10 points across six settings), and exhibit a dramatic synthetic-to-real gap (AVICI drops from 97.8 on synthetic RFF_G to 62.3 on Sachs, Table 1). This diagnosis is well-executed and motivates the paradigm shift convincingly.

- **Principled formulation of the TTT-SCL framework with the AD metric and sparsity constraint.** The Alignment of Distribution metric (Eq. 3) is grounded in likelihood, which inherently captures both structural and mechanistic fit. The incorporation of causal minimality via an L0 sparsity penalty (Eq. 4) prevents the degeneracy that would arise from optimizing AD alone. The joint score (Eq. 5) provides a tractable optimization target for searching the graph space at test time.

- **TACTIC achieves state-of-the-art performance on real-world and pseudo-real data where static SCL fails.** In Table 2, TACTIC (Notears) obtains 78.9 AUROC on Sachs and 80.1 on SynTReN, significantly surpassing AVICI (62.3, 65.4), PC (67.1, 58.1), and score-based methods like SCORE (64.9, 41.0) and NOTEARS (61.8, 49.8). The gains are large and consistent across all non-RFF_G settings.

- **Ablation and stage-wise analysis validate design choices.** Table 3 shows that removing the sparsity penalty degrades performance across all settings (e.g., Sachs drops from 78.9 to 63.5). Table 4's three-stage comparison (seed → highest-score graph → final SCL output) demonstrates that the SCL training phase provides consistent additional gains over any single graph from the search, clarifying the advantage over classical score-based methods that stop at the best-scoring graph.

## Weaknesses

### Fatal
None.

### Major
None that are fatal. The paper has limitations but they are addressable.

### Minor

- **No runtime or compute comparison with baselines.** TACTIC invests substantially more test-time computation (NOTEARS search + stochastic refinement with many AD evaluations + training an SCL model from scratch on 200 instances) than any baseline, which runs a single algorithm or forward pass. The paper does not report wall-clock time or FLOPs, making it difficult to interpret whether the performance gains reflect a better method or simply more compute. While Appendix F is referenced for complexity analysis, the main text should include at least a runtime comparison on one dataset. This does not invalidate the approach—trading compute for accuracy is legitimate—but it should be transparently quantified.

- **The contribution of the SCL training step over simpler post-processing is not fully isolated.** Table 4 shows that the SCL model improves over the highest-scoring graph, but the paper does not compare against a simple ensemble of the top-K refined graphs or a post-processing heuristic applied to the highest-scoring graph. Adding these controls would strengthen the claim that the SCL training component itself adds value beyond what the search phase already achieves.

- **Training set size K=200 is chosen without sensitivity analysis.** The paper uses K=200 training instances without justifying this choice or showing how performance varies with K (e.g., 50, 200, 1000). Given that standard SCL models like AVICI are trained on orders of magnitude more data, the paper should demonstrate that performance does not improve with more instances (which would imply saturation) or that 200 is a principled choice.

- **No statistical significance testing.** Standard deviations are not reported for Sachs and SynTReN results. For synthetic datasets where stds are reported (e.g., AVICI on Linear_U: 13.8, Chebyshev_G: 10.5), the variance is high enough that overlaps with TACTIC's mean performance occur. The paper should discuss whether the observed differences are statistically significant (e.g., via bootstrap or paired tests).

- **Compositional generalization is diagnosed but not shown to be solved by TACTIC.** The paper motivates TTT-SCL partly by the failure of compositional generalization (Issue 2), but the experiments demonstrating TACTIC's effectiveness do not include a compositional generalization test. It is unclear whether TACTIC's test-time adaptation overcomes this specific failure mode or primarily addresses the distribution shift and synthetic-to-real gap.

- **Evaluation is limited to small graphs (d=10, 11, 20).** While this is understandable given the computational cost of the AD-based search, the paper would be strengthened by demonstrating applicability to at least d=50 on one synthetic setting, even if performance is lower.

### Trivial
None that warrant listing.

## Nice-to-Haves

- A comparison against a test-time adaptation baseline that fine-tunes a pre-trained SCL model (e.g., AVICI weights) on the generated instances rather than training from scratch. This would align better with the test-time training literature and could be computationally cheaper.
- A quantitative comparison to Montagna et al. (2024) to substantiate the claim that compositional generalization is "more fundamental" than the limitations identified in that work.
- A Pareto-frontier analysis of the AD vs. sparsity trade-off to show that the joint objective is well-behaved.

## Removed Points

- **"The SCL model on 200 instances is almost certainly underfitting/memorizing"** — This is speculation contradicted by the evidence in Table 4, which shows systematic improvements from SCL training across all datasets. Training details (architecture, epochs, regularization) are in the appendix, which the parser stripped.
- **"AD derivation is circular"** — The reviewer misread the methodology. AD fits mechanisms on test data to **score candidate graphs** during search. The SCL model is then trained on **forward-sampled synthetic data** generated from those mechanisms, not on the test data itself. The SCL model never sees D_test during training.
- **"Gaussian noise for RFF/Chebyshev vs Uniform for Linear is a confound"** — This is standard practice in causal discovery to ensure identifiability, not a design flaw. The paper is transparent about this choice.
- **"PC has 'consistent performance' but it is consistently poor"** — The paper accurately describes PC's performance as "consistent, albeit lower." The reviewer's characterization misrepresents the paper's claim.
- **"Training details are missing"** — These are in Appendices B/C, which were stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected connection or observation not already in the paper.

## Suggestions

1. **Add a runtime comparison table** showing wall-clock time (or relative compute) for TACTIC vs. all baselines on at least one dataset (e.g., d=10 synthetic). This is essential for readers to assess the practical cost of the accuracy gains.
2. **Add a control experiment** comparing TACTIC's final output against: (a) the single highest-scoring graph from the search, (b) an ensemble of the top-K graphs (majority vote on edges), and (c) TACTIC with the K=200 graphs but a trivial classifier (e.g., logistic regression per edge). This would isolate the value of the SCL training step.
3. **Add sensitivity analysis on K** (training set size) for at least one synthetic setting. Show performance at K=50, 200, 500, 1000 to justify the choice of 200.
4. **Add statistical significance** for Sachs/SynTReN results (bootstrap intervals or paired tests across multiple seeds of TACTIC).
5. **Explicitly test whether TACTIC overcomes compositional generalization** by constructing a test scenario where the seed graph search and SCL model must recombine seen components in novel ways.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/.../EzHPHhSQMD.md (game-theoretic RL causal discovery) | 2.0 | Much weaker — unclear necessity of RL component, marginal improvements over baselines, loose theoretical bounds. The present paper has stronger motivation, clearer empirical gains, and a more principled framework. |
| /home/.../HfiRzzmFt8.md (ABCDEFG for causal discovery) | 4.0 | Comparable weakness in scale of evaluation, but the present paper has more systematic motivation (three-limitations diagnosis) and more comprehensive ablation. The present paper is stronger overall. |
| /home/.../sb3H1k3vCG.md (TTT for ICL of nonlinear functions) | 4.0 | Both papers propose TTT-based methods. The present paper has stronger empirical validation; the anchor has theory but suffers from theory-experiment mismatch and presentation issues. |
| /home/.../WtbPaWO8lH.md (voting-theoretic ensemble causal discovery) | 6.0 | Similar quality — both have strong empirical validation on multiple datasets. The anchor has stronger theoretical guarantees; the present paper has a more novel framework (TTT paradigm) but weaker computational fairness. |
| /home/.../4bnCXOtHTm.md (dynamic causal graphs via PCE) | 6.0 | Similar quality. Both papers propose a new paradigm/method with good empirical results. The anchor has stronger theory and works on larger-scale data; the present paper has cleaner diagnostic experiments. |

The paper makes a genuine contribution: it identifies real limitations of static SCL with clean experiments and proposes a novel test-time training framework that achieves strong empirical results. The main weaknesses—missing runtime comparison, incomplete ablation of the SCL step, and no K-sensitivity analysis—are addressable and do not invalidate the core contribution. The paper is comparable in quality to the ~6.0 anchors but slightly weighed down by the computational unfairness concern and the lack of statistical testing. These do not rise to the level of a fatal flaw but do prevent the paper from being in the top tier.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>