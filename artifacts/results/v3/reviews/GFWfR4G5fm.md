Now I have enough information to write the consolidated review. Let me compile my analysis.

## Anchor List

Below is every anchor retrieved across all rounds, with comparison to the paper under review:

**Round 1 — Topic Bands (Low/Medium/High)**

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| AvXrppAS2o | 3.00 | R1-topic-low | Weaker paper — marginal empirical gains, poorly motivated. Our paper has clearer contributions (diagnostic analysis + strong real results). |
| JzFLBOFMZ2 | 3.20 | R1-topic-low | LLM-based CSL with different framing. Our paper is stronger empirically. |
| MVpvyeVeyI | 3.40 | R1-topic-low | Labeled 6.5 but landed in wrong band (scores 5,8,3,10). Not directly comparable. |
| fSxiromxAq | 3.00 | R1-topic-low | Sparse causal models with limited framing. Our paper is stronger. |
| ZXs3pkmrRG (TICL) | 5.50 | R1-topic-mid | **Most comparable anchor.** Test-time training + MCMC for causal discovery, same MCMC acceptance concerns raised by reviewers. TICL is better specified (PC-like classifier is explicit). Our paper has stronger real-world results (Sachs) but worse method specification. |
| lQYi2zeDyh (Demystifying) | 5.00 | R1-topic-mid | Analytical paper about SCL limitations. Limited scope (bivariate only, synthetic). Our paper has broader scope and real data but weaker theoretical grounding. |
| cbFqqtJGtA | 4.25 | R1-topic-mid | Perturbation target prediction. Different problem. Our paper stronger on relevance. |
| 0sO2euxhUQ | 4.00 | R1-topic-mid | Latent SCM learning. Different framing, similar quality tier. |
| xByvdb3DCm | 8.00 | R1-topic-high | Rigorous theoretical causal discovery paper. Our paper is far less rigorous. |
| 3cuJwmPxXj | 8.00 | R1-topic-high | High-quality representation learning paper. Not comparable. |
| hrqNOxpItr | 8.00 | R1-topic-high | Cross-entropy identifiability theory. Much stronger theoretically. |
| k38Th3x4d9 | 8.00 | R1-topic-high | Root cause analysis in time series. Not directly comparable. |

**Round 1 — Weakness-Anchored Queries**

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| UoGv8d3MMy | 3.00 | R1-weakness-underspecified | Missingness-aware concept explainer. Lower quality. |
| fSxiromxAq (duplicate) | 3.00 | R1-weakness-underspecified | Already listed above. |
| iaP7yHRq1l | 5.50 | R1-weakness-underspecified | Differentiable causal discovery robustness study. Comparable quality. |
| X0fDR10B7c | 4.75 | R1-weakness-underspecified | Predictive coding for causal inference. Comparable quality. |
| 2pEqXce0um | 4.50 | R1-weakness-underspecified | Root cause analysis. Comparable. |
| i5JfdnCob7 | 4.40 | R1-weakness-underspecified | Kernel choice for score-based causal discovery. More narrow. |
| BlSIKSPhfz | 6.00 | R1-weakness-underspecified | MCMC ground-state sampling. Different topic. |

**Round 2 — Narrowing within 4.0–6.5**

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| ZXs3pkmrRG (TICL, dup) | 5.50 | R2-topic-narrow | Same anchor. The key comparison. |
| lQYi2zeDyh (Demystifying, dup) | 5.00 | R2-topic-narrow | Same anchor. |
| cbFqqtJGtA (dup) | 4.25 | R2-topic-narrow | Same anchor. |
| x3F8oPxKV2 (Zero-Shot) | 6.25 | R2-topic-narrow | Better specified method, strong empirical results on synthetic data. Our paper is weaker in specification but has real-world results. |
| Lxst78Rrwj | 5.00 | R2-weakness-MCMC | Causal graph learning via distributional invariance. Better theory. |
| jE6VXUhxq9 | 6.25 | R2-weakness-MCMC | Deterministic relations in causal discovery. More rigorous. |
| 2pEqXce0um (dup) | 4.50 | R2-weakness-MCMC | Same anchor. |

**Round-1 bracket:** [3.5, 6.0] — based on band queries showing papers like ours cluster in 4–6 range.

**Round-2 narrowing:** Within the bracket, the paper sits at ~4.5. The closest comparable paper (TICL, 5.5) is better specified and shares the same MCMC concern but is still stronger methodologically. The "Demystifying" paper (5.0) is analytical with narrower scope. Our paper has stronger real-world validation than either but worse specification.

**What the low-band anchors failed at:** They had marginal or unsupported empirical gains, unclear methodology, or narrow scope. Our paper shares the unclear methodology problem (underspecified SCL model, AD regression class, MCMC acceptance criterion) but has clearly demonstrated empirical gains on real data that are absent in the low-band papers.

**Final score: 4.5** — This reflects that the diagnostic analysis and empirical results are genuine contributions, but the method underspecification and methodological concerns (MCMC acceptance, missing runtime, sensitivity to initialization) prevent this from being a clearly acceptable paper at a top venue.

Now let me write the full review.## Summary

This paper identifies three limitations of static Supervised Causal Learning (SCL)—fragility under distribution shifts, failure in compositional generalization, and synthetic-to-real performance gaps—then proposes Test-Time Training for SCL (TTT-SCL) and a concrete instantiation called TACTIC. TACTIC performs a stochastic search over DAGs guided by an Alignment of Distribution (AD) metric and sparsity penalty, generates aligned training data for each test instance, and trains an SCL model on that data. Experiments on synthetic, pseudo-real (SynTReN), and real-world (Sachs) data show that TACTIC substantially outperforms existing SCL and classical causal discovery methods on the real and pseudo-real benchmarks.

## Strengths

- **Systematic diagnostic analysis of static SCL limitations (Section 3, Figure 2, Table 1):** The paper cleanly demonstrates three failure modes—distribution shifts across graph/mechanism/noise dimensions, compositional generalization failure (models cannot recombine training components into unseen configurations), and a stark synthetic-to-real gap (AVICI drops from 97.8 AUROC on RFF_G to 62.3 on Sachs). This analysis is well-executed and constitutes a genuine contribution to the SCL literature regardless of the method proposed.

- **Strong empirical validation on real and pseudo-real data (Table 2):** TACTIC (Notears) achieves 78.9 AUROC on Sachs (vs. AVICI 62.3, best traditional method PC 67.1) and 80.1 on SynTReN (vs. AVICI 65.4). These are substantial, unambiguous improvements over strong baselines on the most practically relevant benchmarks. The improvement is consistent across multiple metrics (AUROC, AUPRC, F1, ACC; Appendix D).

- **Ablation studies clarify design choices (Tables 3, 4):** Removing the sparsity penalty degrades performance across all settings (e.g., Sachs drops from 78.9 to 63.5). The stage-wise analysis (seed → highest-score graph → final SCL output) shows that both the search phase and the supervised learning phase contribute additive value, distinguishing the approach from purely score-based methods.

- **Conceptual framework (TTT-SCL) with principled motivation:** The shift from static diversity-seeking pre-training to test-time-concentrated training is well-motivated by the diagnostic experiments. The AD metric (likelihood-based) and sparsity constraint (causal minimality) form a coherent optimization objective.

## Weaknesses

### Major

- **The "specialized SCL model" trained at test time is critically underspecified (Section 4.2).** The paper states "An SCL model is then trained on this set and applied to infer G_test" but never specifies: (a) whether this is the AVICI architecture (used elsewhere in the paper) trained from scratch or fine-tuned from pre-trained weights, (b) the training hyperparameters (epochs, learning rate, optimizer), or (c) whether initialization matters. This is the central mechanism of the proposed method. Without these details the pipeline cannot be reproduced or scientifically assessed, and claims about the value of the supervised learning phase (Table 4) cannot be properly interpreted.

- **The regression method used for the AD metric ($f_i^k$) is not stated (Eq. 3, Section 4.1).** The entire AD score depends on fitting functions $f_i^k$ ("the fitting function of $X_i$ according $Pa_{train}^k(X_i)$"). The paper never says whether these are linear regressions, Gaussian processes, neural networks, or another class. This choice determines the inductive bias of the search (e.g., linear regressors will favor linear mechanisms, flexible regressors will favor dense graphs). The score function is not fully defined without this information, making the optimization objective ambiguous and the method non-reproducible.

- **The MCMC acceptance criterion shown in Figure 3 is methodologically questionable.** The figure shows $\alpha = \min(1, score(G')/score(G))$. Since $score(G) = AD(G, D_{test}) - \lambda\|A_G\|_0$, where AD is an average log-likelihood, the score can be negative. When scores are negative, this ratio-based acceptance produces counterintuitive behavior: a worse-scoring graph is always accepted (ratio > 1 → accept with prob 1) while a better-scoring graph is accepted with probability less than 1. This does not correspond to a valid Metropolis-Hastings algorithm. The paper must clarify the actual acceptance criterion used or correct the description.

- **Computational cost is not reported (Section 4.3, cf. Appendix F reference).** TACTIC involves iterative MCMC search with per-proposal mechanism fitting, generation of 200 training datasets, and training an SCL model—this is orders of magnitude more expensive than all baselines (PC, GES, NOTEARS, even AVICI inference). Without any runtime measurement in the main text, the comparison in Table 2 is incomplete. The paper claims practical applicability but provides no evidence about the cost of achieving its results.

- **Sensitivity to initialization is understated (Table 2).** TACTIC(random) on Sachs achieves only 58.6 AUROC—*worse* than the AVICI baseline (62.3) it claims to improve upon—while TACTIC(Notears) reaches 78.9. This 20-point gap shows that the method's performance is heavily dependent on the quality of the seed graph. The paper frames this as robustness ("strong performance of both variants confirms the robustness of our core approach"), which is misleading. This dependency should be discussed as a limitation.

### Minor

- The "Component-mixed" experimental design (Section 3.1) is described too loosely ("contains all individual components… seen in isolation") without a precise table of factorial assignments. This makes it difficult to verify that the failure is due to compositional generalization versus another form of distribution shift.

- The number of MCMC iterations and the proposal distribution for the stochastic graph refinement (Section 4.2) are not specified. The paper states the final training set size ($K=200$) but not how many search steps are taken.

- The acceptance ratio $score(G')/score(G)$ in Figure 3 uses a ratio of scores rather than the standard Metropolis-Hastings ratio $\exp(score(G')-score(G))$ that would be natural for a penalized log-likelihood objective. This should be justified or corrected.

## Nice-to-Haves

- An ablation comparing different regression classes for the AD metric (e.g., linear vs. GP vs. MLP) would clarify how much of the pipeline's behavior depends on this choice.
- A summary of wall-clock time for TACTIC versus baselines, even just for one representative setting (e.g., Sachs, 11 variables), would address the cost concern.

## Removed Points

These points were raised by the reviewers but are not included as retained weaknesses:

- **"Score is not a probability" (Harsh Critic, Strengthening section):** This concern is subsumed by the Major weakness about the MCMC acceptance criterion above. The ratio formula itself is the specific issue, not the general fact that the score is not a probability.

- **"Component-mixed design needs precise table" (Harsh Critic):** This is a reasonable request but does not undermine any core claim; moved to Minor.

- **"Robustness to initialization" as a strength (Strength Finder point 6):** The evidence on Sachs shows this is not actually a strength; removed from Strengths list and added as a weakness.

- **Generic strengths about problem importance, timeliness, and writing quality:** Removed per filtering rules (no specific evidence cited, or they are baseline expectations).

- **Criticism about missing related work:** Removed per hard rule against speculating about missing references.

- **Criticism about appendix content being missing:** Removed per hard rule (parser strips appendices; they exist in the original submission).

- **Formatting/style nitpicks and reproducibility nitpicks about hyperparameters:** Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface methodological underspecification and evaluation gaps; they do not contribute novel interpretations not already present in the paper.

## Suggestions

1. **Specify the test-time-trained SCL model completely:** State the architecture (AVICI or other), whether it initializes from pre-trained scm-v0 weights or from scratch, training hyperparameters (epochs, learning rate, batch size), and the inference procedure used to produce the predicted graph from the trained model.

2. **Define the regression class for the AD metric:** State explicitly what function class is used to fit $f_i^k$ (e.g., "ordinary least squares regression" or "Gaussian process with RBF kernel"). Consider adding an ablation of this choice.

3. **Fix the MCMC acceptance criterion:** Either show that $score(G)$ is always positive under the chosen implementation (explaining why the ratio formula is valid) or replace it with a standard acceptance probability such as $\min(1, \exp(score(G') - score(G)))$.

4. **Report runtime in the main text:** Add a wall-clock time comparison (even just for one representative setting per dataset size class) to contextualize the accuracy improvements.

5. **Discuss the initialization sensitivity:** Acknowledge that TACTIC(random) underperforms AVICI on Sachs and explain the implications for the method's robustness claims.

## Score and Decision

**What the low-band anchors (3.0–3.4) failed at:** They had marginal empirical gains, poorly supported claims, or unclear contributions. Our paper shares some of these weaknesses—particularly method underspecification—but its diagnostic analysis is genuinely strong, and the real-world empirical gains (Sachs: 78.9 vs. 62.3) are large and unambiguous, unlike the marginal improvements in the low-band papers.

**How this compares to the closest anchor (TICL, 5.5):** Both papers use test-time training + MCMC search for causal discovery and both have an MCMC acceptance issue flagged by reviewers. TICL is better specified (its model is explicitly a PC-like classifier; hyperparameters are given). Our paper has stronger real-world validation (Sachs is biological ground truth, not a semi-synthetic bnlearn benchmark). The underspecification in our paper is more severe—the core trained model is not identified—which pulls it below TICL.

**MY FINAL SCORE: 4.5**
**MY FINAL DECISION: Reject**