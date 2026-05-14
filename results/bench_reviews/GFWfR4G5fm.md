Now I have all the information needed. Let me produce the final consolidated review.

## Summary
This paper identifies three fundamental limitations of static supervised causal learning (SCL)—fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap—and proposes a Test-Time Training framework (TTT-SCL) that dynamically generates training data aligned with each test instance. The instantiation, TACTIC, uses a likelihood-based Alignment of Distribution (AD) metric with sparsity constraints to search for good candidate graphs via stochastic refinement, generates synthetic training data from those graphs, and trains an SCL model per test instance. Experiments on synthetic benchmarks, the Sachs real-world dataset, and SynTReN pseudo-real data show that TACTIC significantly outperforms both traditional causal discovery methods and the strong SCL baseline AVICI under distribution shift.

## Strengths
1. **Systematic identification of static SCL failures with empirical support.** The paper convincingly shows (Figure 2, Table 1) that current SCL models degrade under distribution shifts across graph structure, mechanisms, and noise; fail at compositional generalization; and exhibit a dramatic synthetic-to-real gap (AVICI drops from 97.8 AUROC on RFF_G to 62.3 on Sachs). This provides strong motivation for the proposed test-time adaptation paradigm.

2. **Principled and well-motivated framework.** The TTT-SCL framework is cleanly formulated around two concepts: the AD metric (Equation 3) which captures both structural and mechanistic similarity through likelihood, and sparsity constraints (Equation 4) that enforce causal minimality. The joint score (Equation 5) is theoretically grounded and directly operationalized.

3. **Strong empirical performance across diverse settings.** TACTIC (Notears) achieves state-of-the-art AUROC on Linear_U (86.3), Chebyshev_G (83.0), Sachs (78.9), and SynTReN (80.1), substantially outperforming AVICI (scm-v0) on all non-RFF datasets. The gains are particularly impressive on Sachs (78.9 vs. 62.3 for AVICI and 67.1 for PC).

4. **Ablation and stage-wise analyses validate core claims.** The sparsity ablation (Table 3) shows dramatic drops when λ=0 (e.g., Sachs 78.9→63.5), confirming that causal minimality is essential. The stage-wise analysis (Table 4) demonstrates clear improvement from seed→highest-score graph→final SCL output, isolating the value of both the search and the supervised learning phases.

5. **Evaluation on real-world and pseudo-real data.** Including Sachs (real protein-signaling data) and SynTReN (biologically plausible regulatory networks) goes beyond purely synthetic benchmarks and strengthens claims about real-world applicability.

## Weaknesses

### Fatal
None.

### Major
- **The evaluation protocol raises a legitimate concern about whether the test data is used too permissively.** The AD metric is computed directly on D_test to guide graph search, and the final SCL model is evaluated on the same D_test. While the SCL model is trained on *synthetic* data (not on D_test itself), the graphs used to generate that training data were explicitly selected to maximize fit to D_test. This creates a possible feedback loop where the training data encodes noise patterns from D_test rather than true causal structure. The paper does not provide a validation mechanism such as held-out test splits, cross-validation, or a separate evaluation set. The suspiciously large gap on Sachs (78.9 vs. 67.1 for the next-best PC) makes this concern acute. **This does not invalidate the results**—the SCL model genuinely generalizes from synthetic training data to D_test—but it does weaken the confidence that the method recovers true causal structure rather than patterns that happen to fit D_test.

### Minor
1. **No error bars or confidence intervals on the compositional generalization results (Figure 2).** The table embedded in Figure 2 reports only point estimates (e.g., Chebyshev_G_62.3 dropping from 93 to 83 under Component-mixed). Without standard deviations or statistical tests, it is impossible to assess whether these drops are significant or within the noise of the evaluation. This weakens one of the paper's three core motivating claims.

2. **The Sachs result lacks a standard deviation.** In Table 2, all other entries include standard deviations (e.g., 83.0±8.7), but the Sachs entry for TACTIC (Notears) is listed as 78.9 with no variability measure. Since Sachs is a single real dataset with 853 samples, reporting only a point estimate is insufficient.

3. **The Gaussian noise assumption for generated training data is noted but not analyzed.** The paper states noise is "set to a standard Gaussian distribution N(0,1) by default" (Sec 4.2). Yet the test data includes settings with Uniform noise (Linear_U). The paper does not quantify how this distributional mismatch affects performance, nor does it consider adaptive noise estimation. This is a notable gap since the entire framework is built on distributional alignment.

4. **No comparison against a strong score-based method optimizing the same objective.** The stage-wise analysis (Table 4) shows the highest-score graph found by TACTIC's search, but does not compare against a greedy hill-climber or exact search (for small d) that optimizes the same likelihood+sparsity objective. Without this, the improvement from "highest-score graph" to "final SCL output" could partially reflect an incomplete search rather than a genuine benefit of the supervised learning phase.

5. **The AD metric implementation is underspecified.** Equation (3) defines AD in terms of "the fitting function f_i^k" obtained "by SIM" (Structure-Induced Mechanism). The paper says "we regress the corresponding mechanisms from D_test" but does not specify the regression method (e.g., Gaussian Process, neural network, linear regression) or how the likelihood is computed. While Appendix A likely provides details (stripped by parser), the main text should be self-contained enough for a reader to understand what is being computed.

6. **λ hyperparameter is not reported or analyzed.** The sparsity penalty λ in Equation (5) is introduced without reporting its value or showing sensitivity analysis. The ablation sets λ=0 but does not explore intermediate values.

### Trivial
- Figure 3's acceptance rule α = min[1, score(G^{k+1})/score(G^k)] is described in the text as "accepted with probability proportional to its score"—this is technically the Metropolis acceptance probability (standard in MCMC) and the description is accurate, but the proposal distribution for graph modifications is not specified.

## Nice-to-Haves
- **Computational cost analysis.** The paper references Appendix F for complexity analysis (likely stripped by the parser). Given that TACTIC trains a deep model from scratch per test instance, a wall-clock time or GPU-hour analysis (even in the appendix) would help readers assess practical deployability.
- **Fine-tuning instead of training from scratch.** If a pre-trained SCL backbone exists (e.g., AVICI), TACTIC could fine-tune it on generated data rather than training a new model each time. This would be a natural path to reducing computational cost.
- **Held-out test split for overfitting check.** Using part of D_test for AD computation and a separate part for evaluation would directly address the data usage concern.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Computational infeasibility is unaddressed.** REMOVED per hard rule (parser stripped Appendix F, which the paper explicitly states contains complexity analysis). The concern about computational cost is real but is addressed in the original submission.
- **Acceptance rule inconsistency (deterministic vs. proportional).** REMOVED as factually incorrect. α = min[1, score_new/score_old] IS the standard Metropolis acceptance probability; improvements (ratio>1) are accepted deterministically and decreases are accepted with probability proportional to the ratio, which matches the paper's description.
- **Missing related works.** REMOVED per hard rule (reviewers cannot invent missing citations without external verification).
- **Formatting/style nitpicks (typos, grammar, etc.).** REMOVED per hard rule (parser artifacts).
- **The claim that "Component-mixed is poorly described."** The paper states: "This training setup contains all individual components... but crucially excludes the specific combinations present in the test instances." This is clear enough for a supervised learning paper; the criticism is overstated.
- **Strength Finder generic strengths.** The Strength Finder's claim that the paper has "clear motivation and problem framing" is retained; claims about "open-sourced AVICI backbone" are dropped as they reflect the baseline, not the paper's contribution.

## Novel Insights
The reviews collectively surface an important observation about the tension in the paper's core framing. The paper criticizes static SCL for overfitting to synthetic distributions, yet TACTIC itself generates synthetic training data and trains an SCL model on it. The key distinction is that TACTIC's synthetic data is *causally aligned* with the test instance rather than *diverse*. This reframes the central challenge of SCL from "how to maximize training diversity" to "how to measure and optimize causal alignment between training and test data." The AD + sparsity formulation is a concrete step toward operationalizing this. However, the reviews also reveal that this reframing inherits new challenges: the alignment metric itself must be computed from the test data, creating a dependence that static methods avoid. Whether this trade-off (alignment dependence vs. diversity dependence) is favorable remains an open question that the paper does not fully resolve, but it is a genuinely interesting direction for the field.

## Suggestions
1. **Report standard deviations for all point estimates**, including Figure 2 and Sachs in Table 2. Consider running multiple seeds of the graph refinement process.
2. **Add a held-out test split experiment** for the real datasets: use part of D_test to guide the search and a separate held-out portion for final evaluation. This directly addresses the data-usage concern.
3. **Compare the highest-score graph from TACTIC's search against a proper score-based optimizer** (e.g., greedy hill-climbing with BIC or the same likelihood+sparsity objective) to isolate the value of the SCL training phase.
4. **Report the value of λ** used in experiments and include a sensitivity analysis over a range of λ values.
5. **Specify the regression method** used to estimate mechanisms from D_test (e.g., the functional form of f_i^k) in the main text, rather than deferring entirely to the appendix.

## Score and Decision

Calibration anchors (from batch retrieval):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/WtbPaWO8lH.md` | 6.0 | Ensemble causal discovery with solid theory; stronger theoretical guarantees but less novel problem framing |
| `/home/wg25r/review_agent/human_reviews_2026/ta8BKRa1bl.md` | 6.0 | Multi-environment identifiability theory; stronger theory, much narrower experiments (bivariate only) |
| `/home/wg25r/review_agent/human_reviews_2026/sFjxg8cyJS.md` | 6.0 | Hidden confounding shift theory; comparable empirical breadth, stronger information-theoretic formalism |
| `/home/wg25r/review_agent/human_reviews_2026/s0nYSwlV3I.md` | 5.0 | Temporal causal discovery with carry-over; similar empirical scope, more restrictive linearity assumption |
| `/home/wg25r/review_agent/human_reviews_2026/MtdrOCLAGY.md` | 4.5 | CD robustness benchmark; comprehensive but a benchmark paper, not a new method |
| `/home/wg25r/review_agent/human_reviews_2026/J8TtDFZiR6.md` | 3.5 | Non-stationary temporal CD; weak experiments and unclear methodological novelty |

This paper is stronger than the 3.5–4.5 anchors: it has a clear new framework, strong empirical validation across synthetic and real data, and ablations that isolate the contribution of each component. It is slightly weaker than the 6.0 anchors, which have either stronger theoretical foundations or more rigorous empirical methodology (confidence intervals, held-out validation). The paper's core ideas are novel and well-motivated, and the empirical results are compelling, but the evaluation protocol concerns and missing error bars prevent it from reaching the top tier. I position it between the 5.0 and 6.0 anchors.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>