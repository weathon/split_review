Now I have a thorough understanding of the paper and all the reviews. Let me produce the consolidated review.

## Summary

This paper proposes VP-OR, a two-stage reoptimization framework for MILPs with dynamic parameters. The framework first uses a GNN to predict marginal probabilities for binary variables and feasible ranges for integer/continuous variables by incorporating historical branch-and-bound leaf-node information. It then employs a Thompson Sampling-based iterative refinement module that selects which variables to fix based on Beta-distribution updates from solver feedback. Experiments on nine reoptimization datasets from the MIP Workshop 2023 Competition show VP-OR finds feasible solutions faster and achieves better primal gaps than SCIP, ReTuning, and two GNN-based baselines under strict 10-second time limits.

## Strengths

1. **Strong empirical results against competitive baselines on a recognized benchmark.** Table 3 shows VP-OR is the only method that finds feasible solutions for every instance across all nine datasets within the 10-second time limit. Table 4 further shows VP-OR achieves the lowest relative primal gaps and the most wins, outperforming ReTuning (the competition winner) and the GNN-based methods PS and ND. The results are consistent across different parameter variation types (objective, bounds, RHS, matrix coefficients).

2. **Addresses an important and underexplored problem.** Reoptimization for general MILPs with dynamic parameters is a practical problem in logistics, scheduling, and control, yet existing reoptimization techniques are limited to LP or special-case MILPs. The paper's focus on general MILPs with integer/continuous variables goes beyond the predominantly binary-variable scope of most end-to-end ML-for-MILP methods (Section 1).

3. **Novel use of historical branch-and-bound leaf-node information as GNN features.** Incorporating feasible basic variables and dual solutions from the leaf node of the base instance's B&B tree (Section 3.1) is a well-motivated direction for capturing parameter sensitivity, going beyond standard bipartite graph representations that only use the optimal solution.

4. **Empirical motivation for the design choices.** Table 1 shows mispredictions concentrate in a small subset of variables, and Table 2 demonstrates that fixing even 50–70% of variables dramatically reduces solving time (3–10×). These observations directly justify the variable-fixing strategy and the need for an iterative refinement loop.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the stated MAB formulation and the actual Thompson Sampling algorithm.** The paper describes a combinatorial MAB with an enormous action space (e.g., 2^C(p, a%×p) possible arms in Equation (line 165)), but the actual algorithm (lines 168–172) uses per-variable independent Beta distributions, samples μ_i independently, ranks by a heuristic criterion, and fixes the top a%. The update rules then attribute the global binary reward (improvement over previous best) to individual variable-value changes without any mechanism to disentangle which variables actually caused the improvement. The paper acknowledges the "simplifying assumption that treats each variable as independent of others" (line 167), but this assumption turns the problem into something closer to independent Bernoulli bandits over each variable-position rather than combinatorial Thompson Sampling over sets. The heuristic credit assignment — comparing the current and previous-best selected sets to decide which variables to reward — has no theoretical grounding in the MAB framework and may lead to spurious updates. While such heuristics are not uncommon in applied work, the paper overclaims by presenting this as a principled bandit formulation, and the mismatch between the stated problem and the actual algorithm should be clarified.

2. **Insufficient experimental rigor given the small test set.** Each dataset has only 5 test instances (25 groups total: 20 train, 5 test). No confidence intervals, error bars, variance, or statistical significance tests are reported. With such a small sample, individual instances could disproportionately drive the aggregate numbers. The convergence plots (Figure 2) are shown for only 3 of the 9 datasets (bnd 1, mat 1, rhs 1), making it difficult to assess generalization across parameter change types. The paper does not report raw per-instance results, the number of Thompson Sampling iterations completed within the time limit, or a breakdown of runtime among GNN inference, iterative solving, and relaxation handling.

3. **Missing ablation: no comparison to random variable fixing.** Table 2 shows solving times for different fixed percentages, but the baseline is only "SCIP without reoptimization" and LNS. Without comparing to a random-fixing baseline (or a "fix the most confident GNN predictions in one round" baseline), it is impossible to isolate whether the Thompson Sampling refinement adds value over simply fixing variables based on the GNN's predictions in a single shot. The core claim that the online refinement improves solution quality is not directly tested.

### Minor

4. **GNN training for integer/continuous variables is underspecified.** Section 3.2 describes logarithmic binary encoding and confidence thresholding, but never explicitly states the training target or loss function. The paper says "predict the conditional probability of each bit" (line 85), which implies binary classification per bit, but the reader is left to infer the loss (binary cross-entropy) and how the training data pairs base-instance features with ground-truth optimal values of modified instances. The decomposition of high-dimensional binary representations is mentioned but not concretely described. This makes the method harder to reproduce even though the overall idea is clear.

5. **Single parameter setting for P=0.7 without sensitivity analysis.** The percentage of fixed variables P is the only free parameter, yet only P=0.7 is presented (line 181), with no exploration of how different values affect the trade-off between speed and solution quality. This is important because fixing too many variables risks infeasibility, while fixing too few reduces the speed benefit.

6. **Asymmetric ranking metrics for binary vs. integer/continuous variables are not explained.** For binary variables, the ranking uses min(μ_i, 1−μ_i) and selects the lowest a% (line 168); for integer/continuous variables, the ranking uses μ_j directly and selects the top a% (line 172). The rationale for this asymmetry is not discussed, and the different selection directions are confusing.

### Trivial

7. The formula for negative variable ranges ("−2^{k_{ub}+1} to −2^{k_{lb}^{-}}+1") contains garbled notation (k_{lb}^{-}) that appears to be a formatting artifact.

8. The paper states "SCIP using the base solution as a warm-start strategy" (line 177) is a baseline, but the actual results are relegated to an appendix section.

## Nice-to-Haves

- A comparison to a baseline that fixes variables based purely on GNN confidence in a single round (no iterative refinement) would directly measure the contribution of the Thompson Sampling stage. The current experiments mix the GNN prediction and TS refinement together.
- Reporting the number of Thompson Sampling iterations and the frequency of the relaxation mechanism (splitting into 10 groups) would help assess the algorithm's efficiency and the cost of infeasibility handling.
- Variance bars or per-instance raw data for the 5 test instances would substantially strengthen the empirical claims.

## Removed Points

These points are flagged to be removed, treat them with caution:
- Criticisms about missing comparison results (referenced as ".5", ".7") and missing appendix sections — the parser strips appendices; these exist in the original submission.
- Claim that "−" in Table 4 is unexplained — the paper explicitly states it "represents cases where the method could not find a feasible solution" (line 191).
- Claim that the LNS critique is incorrect — the paper's observation that pure LNS "does not actually decrease the problem's variable size" and adds complexity through neighborhood constraints is factually correct and acknowledged in the LNS literature.
- Claim that the Thompson Sampling approach is "fundamentally flawed" or that the reward attribution "has no sound basis" — the paper acknowledges the independence assumption (line 167), which is a standard simplification in this line of work (Nair et al., 2020; Han et al., 2023). The critic overstates the severity; the approach is a heuristic approximation, not a fatal error.
- Claim that comparing selected sets is "computationally expensive" — comparing two sets is O(n) and negligible compared to solving MILPs.
- Formatting/parsing artifacts presented as author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the paper's core findings — that combining GNN-based prediction with iterative heuristic refinement yields practical speedups for reoptimization — but do not contribute new analytical insight beyond what the paper already states.

## Suggestions

1. **Acknowledge and scope the Thompson Sampling approximation.** Explicitly state that the algorithm is a heuristic inspired by Thompson Sampling with an independence assumption, rather than a principled combinatorial MAB solution. This would better align the formulation with the actual algorithm and reduce the risk of overclaiming.

2. **Add an ablation study with random variable fixing and single-round GNN-only fixing** to separately measure the contribution of the GNN predictions and the iterative refinement loop. This is the most important missing experiment.

3. **Report variability** across the 5 test instances (e.g., min/max, standard deviation, or per-instance raw objective values) and show convergence plots for all 9 datasets (perhaps in supplementary material). If space permits, add a simple statistical test (e.g., Wilcoxon signed-rank) comparing VP-OR to the best baseline on each dataset.

4. **Provide explicit training details** for the GNN on integer/continuous variables: the exact loss function, how binary bit targets are aligned across instances, and the thresholding procedure for converting bit probabilities to bounds.

## Score and Decision

The paper tackles an important practical problem with a sensible two-stage design, and its empirical results — finding feasible solutions where all baselines fail on some datasets — are promising. However, the combination of (a) a significant gap between the claimed principled bandit formulation and the actual heuristic algorithm, (b) an ablation deficit (no random-fixing or single-round GNN-only baseline), and (c) limited statistical rigor (5 test instances, no variance reporting, only 3/9 convergence plots) tempers confidence in the results. The contributions are real but the evidence would benefit from strengthening before acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>