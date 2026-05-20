Now I have everything I need. Let me write the consolidated final review.

## Summary

This paper identifies three fundamental limitations of static supervised causal learning (SCL)—fragility to distribution shifts, compositional generalization failure, and a synthetic-to-real performance gap—and proposes Test-Time Training for SCL (TTT-SCL) as a solution. The framework dynamically generates training data aligned with each test instance using an Alignment of Distribution (AD) metric with sparsity constraints. The authors instantiate this as TACTIC, which performs stochastic graph refinement guided by the AD + sparsity score, generates synthetic training data, and trains an SCL model at test time. Experiments on synthetic, pseudo-real, and real-world benchmarks (including Sachs) show TACTIC outperforming existing SCL and traditional causal discovery methods.

## Strengths

1. **Identifies a novel compositional generalization failure in SCL that goes beyond prior work.** Figure 2 and the "Component-mixed" condition show that SCL models fail on unseen combinations of seen components (e.g., RFF_G: 86 vs 90, Chebyshev_G: 83 vs 93), revealing memorization of training configurations rather than modular causal understanding. This goes beyond Montagna et al. (2024), who studied only individual component shifts.

2. **Strong and consistent empirical results across diverse settings.** TACTIC (Notears) achieves state-of-the-art performance on 4 out of 5 datasets (Table 2), including real-world Sachs (78.9 AUROC vs. 62.3 for AVICI and 67.1 for PC) and Syntren (80.1 vs. 65.4 for AVICI). This directly addresses the synthetic-to-real gap identified as Issue 3.

3. **Stage-wise analysis (Table 4) validates the two-stage improvement.** The final SCL prediction consistently beats both the seed graph and the highest-scoring graph found during search (e.g., Sachs: 61.8 → 66.6 → 78.9; Chebyshev: 52.2 → 75.8 → 83.0), demonstrating that the SCL training phase adds value beyond the score-based search.

4. **Ablation confirms sparsity necessity.** Removing the sparsity penalty (Table 3) causes significant drops across all datasets (e.g., Sachs: 78.9 → 63.5; Chebyshev: 83.0 → 69.7), validating the joint AD + sparsity objective design.

5. **Consistent validation across architectures and metrics.** The SCL failure patterns are confirmed using the SiCL backbone (Appendix C), and results hold across ACC, F1, and AUPRC (Appendix D), showing robustness.

## Weaknesses

### Fatal

None.

### Major

1. **The SIM regression method is underspecified, affecting reproducibility and analysis.** The paper states it "regress[es] the corresponding mechanisms from the observed D_test" (Section 4.1) to compute the AD likelihood (Eq. 3) and generate training data, but never specifies the function class used for regression (linear regression? random forests? neural networks?). Since AD(G, D_test) = (1/d) Σ log p(X_i | f_i^k), the computation of p(X_i | f_i^k) also requires specifying whether a Gaussian conditional with estimated variance or another density model is used. The paper mentions "practical heuristics" in the supplement (which was stripped by the parser), but the main text lacks any specification. This undermines reproducibility and makes it impossible to assess whether the AD score's behavior is robust to the regression choice.

2. **The incremental benefit of the SCL training phase over a simpler score-based ensemble is not fully disentangled.** The paper shows in Table 4 that the SCL output (91.8 on RFF_G) outperforms the highest-scoring single graph from the search (88.9). However, a natural baseline is missing: averaging edge probabilities across the top-K graphs (ranked by the joint score) to produce an ensemble prediction. This baseline would directly test whether the SCL model is genuinely extracting additional signal beyond what a score-based ensemble already captures. The improvement from highest-score graph to SCL output (e.g., 88.9→91.8 for RFF_G; 66.6→78.9 for Sachs) is substantial for Sachs but modest for RFF_G, and without the ensemble baseline one cannot rule out that a simpler procedure would achieve similar gains.

### Minor

3. **Missing confidence intervals for Sachs (real-world) results.** Table 2 reports single AUROC values for Sachs and Syntren for TACTIC variants with no standard deviation, while synthetic benchmarks include them. For a single-dataset evaluation with a known gold-standard graph, reporting bootstrapped confidence intervals (or at minimum acknowledging the lack of replication) is important, especially since Sachs is a small dataset (853 samples, 11 variables).

4. **The acceptance probability formulation in Figure 3 is non-standard and could be clarified.** The transition probability "α = min[1, score(G_{k+1}) / score(G_k)]" uses a ratio of scores directly. Since score(G) = AD(G) − λ·Sparsity(G) is typically negative (log-likelihood minus a non-negative penalty), the ratio of two negative numbers is positive and the formula is well-defined. However, a Metropolis-Hastings acceptance would typically use exp(score_new − score_old) rather than score_new/score_old. The paper also says "accepted with probability proportional to its score" (Section 4.2), which is inconsistent with the ratio formula in Figure 3. This should be clarified.

5. **Hyperparameter λ (sparsity coefficient) selection is not discussed.** The paper defines the joint score as AD(G, D_test) − λ·Sparsity(G) but does not specify how λ is chosen across datasets. If λ is set differently per dataset, a sensitivity analysis is needed; if it is fixed, that should be stated.

### Trivial

- The paper states "Results are presented as AUROC (standard deviation)" in Table 1 and 2 but then omits standard deviations for Sachs and Syntren in Table 2. This is a formatting inconsistency.

## Nice-to-Haves

- Adding the top-K graph ensemble baseline (as described in Major Weakness 2) would substantially strengthen the paper's central claim about the necessity of the SCL training phase.
- A discussion of computational cost and scaling (wall-clock time, applicability beyond d ≤ 20) would help readers assess practical usefulness. The paper references Appendix F (which the parser stripped), but a brief statement in the main text would be helpful.
- The paper could discuss how the number of search iterations and K=200 graphs were determined.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Fatal: The method is essentially a repackaged score-based causal discovery pipeline"** — the harsh critic framed this as a critical issue, but the paper directly addresses it via Table 4's stage-wise analysis showing that SCL output consistently beats the highest-score graph. The critic's specific claim that "one could simply take the highest-scoring graph directly" is contradicted by the paper's evidence (the SCL output outperforms the highest-score graph on all four benchmarks). The remaining concern (top-K ensemble) is retained as a Major weakness above.

2. **"Criticism about negative scores making the acceptance ratio undefined"** — scores are typically negative (log-likelihood ≤ 0 minus sparsity ≥ 0), so score(G_{k+1})/score(G_k) is a ratio of two negative numbers, which is positive and well-defined. The formulation is non-standard but not invalid, and is now captured as a Minor weakness about clarity.

3. **Strength Finder's generic strengths** — "The paper addresses an important problem" and "robustness across diverse metrics" are generic/superficial and have been dropped or folded into concrete strengths above.

## Novel Insights

The harsh critic's main structural critique—that AD + sparsity is essentially a score-based causal discovery objective—highlights a genuine tension in the paper's framing. The paper presents TTT-SCL as a paradigm shift from "diversity to concentration," but the search component is indeed a score-based method. The novelty lies not in the search itself but in the *purpose* of the search: it generates training data for an SCL model rather than outputting a final graph. The stage-wise analysis (Table 4) is the paper's strongest evidence that this distinction matters. An interesting observation from the calibration anchors is that this paper's problem diagnosis (documenting SCL's failures) is unusually thorough compared to many causal discovery papers, which often jump straight to proposing a new method without rigorously demonstrating why existing approaches fail.

## Suggestions

1. **Specify the SIM regression method.** State the function class (e.g., ridge regression, random forest, or neural network) and the likelihood computation (e.g., Gaussian conditional with variance estimated from residuals) in the main text. A brief robustness experiment in the appendix showing that results are stable under different regression choices would further strengthen the paper.

2. **Add the top-K ensemble baseline.** Average edge probabilities across the top-K graphs (ranked by the AD + sparsity score) and compare to the SCL model's output. If the ensemble is competitive, discuss what additional signal the SCL model captures; if not, this directly proves the SCL model's value.

3. **Report confidence intervals for Sachs.** Bootstrapped CIs or at minimum an acknowledgment of the single-dataset limitation.

4. **Clarify the acceptance probability.** Align the text ("accepted with probability proportional to its score") with the figure formula, or justify why score(G_{k+1})/score(G_k) is used instead of a standard exponential Metropolis ratio.

5. **Discuss λ selection.** State how the sparsity coefficient is chosen and include a sensitivity analysis.

## Score and Decision

**Round 1 bracketing:** Three queries on "test time training supervised causal learning" returned anchors in bands: weak (avg 2.5–3.0, Reject/Withdrawn), middle (avg 4.0–6.8, mixed Accept/Reject), strong (avg 8.0, Accept). The paper clearly sits in the middle band.

**Round 2 narrowing:** Queries targeting 4.0–7.0 for causal discovery papers and 5.0–7.0 for TTT papers returned:
- "Dynamic Causal Graphs" (6.0, Accept Poster) — comparable novelty and empirical rigor; our paper has stronger real-world validation but less theory.
- "Risk-Optimal Prediction under Unseen Causal Perturbations" (5.5, Reject) — weaker empirical validation than our paper; our paper is stronger.
- "Architecture-Agnostic TTA" (5.5, Accept Poster) — comparable execution quality but less novel problem.
- "Specialization after Generalization" (6.8, Accept Poster) — cleaner theoretical contribution; our paper has stronger empirical breadth.

The paper is clearly stronger than the 4.0 TTT-ICL paper (Reject) and 5.0 Adaptive TTA paper (Accept Poster). It is comparable to the 6.0 Dynamic Causal Graphs paper and slightly below the 6.8 TTT theory paper. The weaknesses identified are addressable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>