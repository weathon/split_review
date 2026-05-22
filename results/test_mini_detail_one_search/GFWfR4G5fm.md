Now I have all the verification I need. Let me write the final consolidated review.

---

## Summary

This paper identifies three fundamental out-of-distribution limitations of static Supervised Causal Learning (SCL) — fragility to distribution shifts, compositional generalization failure, and a synthetic-to-real generalization gap — and proposes a Test-Time Training framework (TTT-SCL) to address them. The core idea is to dynamically construct a training set aligned to the test instance at test time, using an Alignment of Distribution (AD) metric (based on likelihood) combined with a sparsity constraint. The instantiation TACTIC performs stochastic graph refinement seeded by a traditional method (e.g., NOTEARS), generates training data from the refined graphs, and trains an SCL model on that data. Experiments on synthetic, pseudo-real, and real-world (Sachs) data show substantial improvements over both traditional causal discovery methods and prior SCL approaches.

## Strengths

1. **Well-motivated problem, cleanly demonstrated.** Section 3 provides a rigorous controlled factorial experiment (Fig. 2, Table 1) isolating three distinct failure modes of static SCL: shifts in graph structure, mechanism, noise, and crucially, compositional generalization failure on *combinations* of seen components. This goes beyond prior work (Montagna et al., 2024) and convincingly motivates the need for test-time adaptation.

2. **Novel framework with a principled core idea.** The TTT-SCL paradigm — shifting from static diversity-seeking pre-training to dynamic test-time concentration — is a genuine conceptual contribution. The AD metric (Eq. 3) provides a tractable way to operationalize distributional alignment between candidate graphs and test data, and the sparsity constraint (Eq. 4) correctly prevents degenerate dense solutions. The ablation in Table 3 confirms that removing the sparsity penalty crashes performance (Sachs: 78.9 → 63.5), validating the design.

3. **Strong empirical results on realistic data.** TACTIC (Notears) achieves 78.9 AUROC on Sachs and 80.1 on Syntren, substantially outperforming all baselines (best prior: PC 67.1 on Sachs, AVICI 65.4 on Syntren). These are the most challenging settings where static SCL fails most dramatically. The improvement over the seed NOTEARS graph is particularly striking on Syntren (49.8 → 80.1) and Chebyshev_G (52.2 → 83.0), showing the TACTIC pipeline adds real value beyond the seed.

4. **Stage-wise analysis isolates the two-phase contribution.** Table 4 separates the search improvement (seed → highest-score graph) from the learning improvement (highest-score graph → SCL output). The consistent gains in the second stage (e.g., Sachs 66.6 → 78.9, Chebyshev_G 75.8 → 83.0) demonstrate that the SCL training phase adds value beyond what score-based search alone provides.

## Weaknesses

### Major

- **Missing baseline for the "learning improvement" claim.** The stage-2→3 improvement in Table 4 is attributed to SCL learning, but the comparison is between a *single* highest-scoring graph and an SCL model trained on *many* candidate graphs (K=200). The improvement could partly arise from ensembling/averaging over multiple candidates rather than from the SCL model learning a generalizable mapping. An ablation that aggregates the K candidate graphs without training an SCL model (e.g., majority vote on edges, averaging adjacency matrices, or ensembling their predictions) is needed to support the claim that the SCL phase provides benefits beyond simple ensembling of the search results.

- **No hyperparameter sensitivity analysis for λ.** The joint score (Eq. 5) depends critically on λ, yet only λ=0 vs. the chosen λ is compared (Table 3). The paper does not report how λ was selected, how performance varies across a range of λ values, or whether the results are robust to its choice. Given that the ablation shows λ=0 crashes performance (Sachs 78.9→63.5), the sensitivity of the method to this parameter is a material concern.

### Minor

- **Acceptance rule ambiguity in stochastic refinement.** Figure 3 describes the acceptance probability as α = min[1, score(G^{k+1})/score(G^k)]. Since the AD metric is a log-likelihood (negative for continuous data) and sparsity is subtracted, the joint score is typically negative. For negative scores this ratio-based rule inverts the desired acceptance behavior (improvements accepted with prob < 1, regressions accepted with prob 1). The paper should clarify whether the scores are transformed, or whether the intended rule is a standard Metropolis-Hastings form α = min[1, exp(score_{new} - score_{old})].

- **Missing standard deviations for Sachs and Syntren in Table 2.** All entries for the Sachs and Syntren columns lack standard deviations, making it impossible to assess the variability of the comparisons on the most practically relevant datasets.

- **The "random" seed variant is not thoroughly discussed.** TACTIC (random) underperforms PC on Sachs (58.6 vs 67.1), which the paper mentions but does not analyze. A brief discussion of when and why the random seed fails would strengthen the presentation.

### Trivial

- The acceptance rule formula in Figure 3 is described in the text as "accepted with probability proportional to its score" (Section 4.2), which is a different description from the explicit ratio formula in the figure. These should be consistent.
- Some figure references (e.g., Appendix G cites a non-functional `[Appendix G](#)`) suggest formatting issues from the review system.

## Nice-to-Haves

- A seed sensitivity study varying seed quality (random, PC, NOTEARS, no seed) across multiple datasets to systematically separate the contribution of the seed from the contribution of the TACTIC pipeline.
- For the Linear_U case in Table 4 (seed 82.0 → highest-score 80.1 → final 86.3), the search degrades the AUROC relative to the seed, yet the SCL phase still produces the best result. Explaining this phenomenon (e.g., does the SCL model learn to discount spurious patterns in the search output?) would be illuminating.
- Distribution plots of AD and sparsity scores over the refinement iterations for a few test instances to visualize search convergence.

## Removed Points

The following points from the reviewers were removed per the filtering rules:

- **"Under-specified method — how mechanisms are fitted"**: The paper states that mechanisms are regressed via SIM and refers to Appendix A for implementation details. Per the evaluation protocol, missing appendix content stripped by the parser is not a valid criticism.
- **"TACTIC (random) worse than basic baselines" as a weakness against the core claim**: TACTIC (random) outperforms PC on 4 of 5 datasets (RFF_G, Linear_U, Chebyshev_G, Syntren). The cherry-picked Sachs case is the exception, not the rule. This does not support the claim that performance is primarily driven by the seed.
- **Strength Finder claims about "importance of the problem"**: Generic/superficial statements about the problem being "important" and "well-motivated" are removed. The concrete demonstrations in Section 3 are retained as a genuine strength.
- **Strength Finder claim about "systematic documentation"**: This is sufficiently covered by Strength #1 above.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the paper that the authors had not already made.

## Suggestions

1. Add an ensemble baseline (majority vote on edges or averaging adjacency matrices over the K=200 candidate graphs from TACTIC's search) and compare its performance to the SCL-trained output in Table 4. This would cleanly separate the value of ensembling from the value of SCL learning.
2. Report a λ sensitivity study across a range (e.g., 0, 0.01, 0.1, 1, 10) on at least two datasets, and describe how λ was selected.
3. Clarify the acceptance rule used in stochastic refinement: if the formula in Figure 3 is correct for positive scores, explain how scores are guaranteed positive; if it is a heuristic, state that explicitly; or adopt the standard exp-ratio form.
4. Report standard deviations for Sachs and Syntren across multiple seeds/splits.
5. Add a brief section acknowledging the risk of transductive overfitting (training on data derived from the test instance) and discuss mitigation strategies.

## Score and Decision

**Calibration anchors** (from `deepreview_13k_calibration`):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `xByvdb3DCm` (When Selection meets Intervention) | 8.0 | Stronger theoretical contribution with formal soundness proof; the current paper is more empirically driven and less theoretically rigorous. |
| `eeJz7eDWKO` (Meta-Learning for Bayesian Causal Discovery) | 6.0 | Similar quality: both have clear contributions and limitations, but the current paper has a more novel framework idea and stronger real-world evaluation. |
| `lQYi2zeDyh` (Demystifying amortized CD) | 5.0 | Narrower scope (bivariate only); current paper is broader and more comprehensive. |
| `ZXs3pkmrRG` (Test-Time Learning of Causal Structure) | 5.5 | Similar TTT+SCL concept, but with less compelling results and more presentation issues. Current paper is stronger. |
| `TRHyAnInUC` (D³PM) | 3.25 | Weak contributions and unclear method; current paper is substantially stronger across all dimensions. |

Relative to these anchors, the paper has a genuinely novel framework, strong empirical validation on realistic data, and clear motivation. It falls short of the 8.0-level papers due to missing ablations (no ensemble baseline, no λ sensitivity analysis) and some methodological ambiguity. It clearly exceeds the 5–6 range papers.

**Score**: 6.5

**Decision**: Accept

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>