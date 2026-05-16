Now I have all the evidence I need. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes VP-OR, a two-stage reoptimization framework for Mixed Integer Linear Programming (MILP) with dynamic parameters. The first stage trains a Graph Neural Network (GNN) on the base instance's branch-and-bound history to predict marginal probabilities for binary variables and feasible ranges (via logarithmic binary encoding) for integer/continuous variables. The second stage applies Thompson Sampling to iteratively select which variable predictions to fix, updating Beta distributions based on solution quality. Experiments on 9 reoptimization datasets from the MIP Workshop 2023 Competition show VP-OR finds feasible solutions within 10 seconds across all datasets and achieves smaller primal gaps than baselines including SCIP, Re Tuning (Patel, 2024), PS (Han et al., 2023), and ND (Nair et al., 2020).

## Strengths

1. **Novel two-stage architecture combining GNN prediction with bandit-style refinement for reoptimization.** VP-OR is, to my knowledge, the first framework to connect GNN-based variable prediction (for both binary and integer/continuous variables) with Thompson Sampling for iterative variable selection in the MILP reoptimization setting. The pipeline is well-motivated: prediction narrows the variable space, and the online refinement compensates for prediction errors.

2. **Explicit handling of integer and continuous variables beyond binary-only predictions.** Most prior ML-for-MILP methods (Han et al., 2023; Khalil et al., 2022) focus exclusively on binary variables. The paper identifies that in real-world datasets like "vary matrix rhs bounds" only 400 out of 27,710 variables are binary (Sec. 3.2), making this extension practically important. The logarithmic binary encoding with confidence thresholds is a reasonable heuristic approach to this problem.

3. **Strong empirical results across 9 diverse reoptimization datasets.** VP-OR is the only method that finds feasible solutions for all 9 datasets within the 10-second time limit (Table 3). It achieves the smallest absolute and relative primal gaps on the majority of datasets (Table 4, bold entries), and convergence plots (Figure 2) show faster primal gap reduction in early stages. The comparison against Re Tuning (the competition-winning reoptimization method from MIP Workshop 2023) on its own benchmark datasets is a meaningful stress test.

4. **Leverages leaf-node dual information from the base instance's branch-and-bound tree.** Beyond the typical use of the optimal solution, VP-OR extracts feasible basic variables and dual solutions from the leaf node that yielded the optimal solution (Sec. 3.1). This is grounded in LP sensitivity analysis and provides richer signal for predicting how the solution changes under perturbations.

5. **Principled infeasibility handling.** When variable fixing produces infeasible subproblems, the algorithm divides fixed variables into 10 groups and relaxes one group at a time (Sec. 4.2). This practical mechanism is necessary for real-world deployment and is clearly described.

## Weaknesses

### Fatal
None.

### Major

1. **GNN training objective is not specified, impairing reproducibility.** The paper describes the GNN's input features and output format (marginal probabilities for binary variables, binary-bit probabilities for integer/continuous variables) but never states the loss function, training labels, or supervision signal. For binary variables: what is the loss — cross-entropy against the optimal solution of the modified instance? For integer/continuous variables: the paper says it predicts "the conditional probability of each bit" in a logarithmic binary encoding (Sec. 3.2), but never specifies what ground-truth labels are used for these bits, how a "bit-level" prediction is trained, or how the confidence-threshold post-processing connects to the training objective. The main text mentions only that the model was "optimized using Adam" (Sec. 5.1), which is not a training specification. This is not a criticism about missing appendix content; it is a gap in the main text's description of the core method, and it prevents an informed evaluation of whether the learning component is sound.

2. **Small test set with no uncertainty quantification.** Each dataset has only 5 groups in the test set (Sec. 5.1: "25 groups, including 20 groups in the training set and 5 groups in the test set"). No error bars, confidence intervals, or statistical significance tests are reported for any of the central results (Tables 1–4, Figure 2). With 5 test observations per dataset, a single outlier can drive the reported averages, and the reader cannot assess whether the observed advantages of VP-OR are reliable. This is the most consequential weakness: it directly undermines the strength of the empirical claims.

### Minor

3. **The Thompson Sampling factored approximation lacks justification.** The paper correctly frames variable selection as a combinatorial multi-armed bandit (the joint space of fixing subsets is combinatorial) but immediately resorts to a factored approximation treating each variable independently (Sec. 4.2, line 167: "simplifying assumption commonly used in prior work"). The Beta update rules for integer/continuous variables are described as heuristic ("no penalty given when the current solution performs worse," "no immediate conclusion about its benefit can be drawn"). No experiments compare the factored approximation against simple baselines (e.g., random selection, greedy top-probability selection, or a bandit that considers pairs of variables). Without empirical justification, the connection to Thompson Sampling is more rhetorical than substantive — the actual algorithm is closer to adaptive probability-weighted filtering.

4. **Only 3 of 9 datasets are shown in convergence plots (Figure 2).** The paper shows relative primal gap over time for bnd 1, mat 1, and rhs 1 only. The selection criterion is not explained, and the remaining 6 datasets are absent. Given that Table 4 shows variable performance across datasets (e.g., VP-OR is weaker on obj 1 and obj 2), convergence behavior on the omitted datasets is directly relevant to assessing the method's scope.

5. **The "3–10× speedup" claim from fixing variables is not clearly substantiated.** The paper states (Sec. 4.1) that fixing variables yields 3–10× speedup, citing Table 2. However, Table 2 is an embedded image, and the textual discussion does not explain which specific entries in the table support this range or how it was computed. The claim is plausible but cannot be verified from the text alone.

6. **Warm-started SCIP baseline is relegated to the appendix.** The paper mentions (Sec. 5.1) that it provides "results for SCIP using the base solution as a warm-start strategy" but places these in an appendix reference. This is a natural and important baseline for reoptimization — using the previous optimal solution as a warm start is the simplest reoptimization strategy — and should appear in the main tables alongside the other methods.

### Trivial

7. The "Wins" metric definition in the Table 4 caption is slightly ambiguous: the paper text (line 182) clarifies it as "the number of datasets for which a method achieves the best solution," but the table caption says "the number of wins" without specifying the denominator.

## Nice-to-Haves

- Sensitivity analysis on the single hyperparameter \(P=0.7\) (percentage of fixed variables) would strengthen the paper's claims. The paper acknowledges it has only one parameter but does not study its impact.
- Reporting computational overhead of the Thompson Sampling loop (time spent per iteration, number of iterations, wall-clock breakdown) would help readers assess whether gains come from smarter fixing or from simply more compute.
- Showing convergence plots (Figure 2) for all 9 datasets rather than a selected subset would give a more complete picture.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 1 shows zero mispredicted variables for some datasets; this is implausible."** I cannot verify the specific entries in Table 1 (it is an embedded image). The paper's own text (line 121) says "inaccuracies... are typically concentrated in a small subset" — implying errors do exist — so the reviewer may have misread the table. Removed as unverifiable and potentially inaccurate.

- **"Baselines PS and ND are at a disadvantage because they don't receive historical information."** The paper's contribution is a reoptimization framework that *uses* historical information. Comparing against generic ML-for-MILP methods that solve from scratch is a valid way to isolate the value of reoptimization. The main comparison against Re Tuning (a reoptimization method) already controls for this. Removed because it evaluates VP-OR against the wrong expectation.

- **"The leaf-node historical feature encoding is not specified; cross-reference to Table 5 (appendix) doesn't remedy this."** The paper references an appendix for these details. Per the meta-instructions, criticisms about content that exists in the parser-stripped appendix are removed.

- **"Baseline implementation details not described."** The paper references an appendix for these. Removed for the same reason.

- **"Table 2 is nearly unreadable due to formatting."** This is a parser artifact affecting the embedded image rendering, not an author error.

- **Formatting/style nitpicks, grammar/typo complaints.** These are parser artifacts, not author errors.

## Novel Insights

The most interesting observation to emerge from this review is the tension between the paper's two stages. The GNN achieves remarkably low prediction error rates (the paper's own claim in Sec. 4.1 is that "only a very small number of variable predictions are inaccurate"). If this is true, the Thompson Sampling refinement stage has very little work to do — it needs only to identify a handful of mispredicted variables from a potentially large pool. But the MAB-style update rules treat all variables symmetrically, updating Beta distributions even for correctly predicted variables, which could introduce noise. A more targeted approach — e.g., using prediction uncertainty estimates to focus Thompson Sampling only on variables with low-confidence predictions — might be more sample-efficient. This tension between "almost everything is correct" and "we need bandit exploration" is not addressed in the paper and could be a fruitful direction for future work.

## Suggestions

1. **Specify the GNN training loss and labels explicitly in the main text.** This is the single most actionable fix. State whether binary variables are trained with cross-entropy against the optimal solution, and describe what ground-truth labels are used for the binary encoding bits of integer/continuous variables.

2. **Add error bars or confidence intervals** to all main results (Tables 1, 3, 4). With only 5 test-set groups per dataset, bootstrapped confidence intervals or per-dataset standard deviations are essential for the reader to assess reliability.

3. **Include warm-started SCIP in the main tables** and show convergence plots for all 9 datasets (or explain the selection criterion for the 3 shown).

4. **Add an ablation comparing the Thompson Sampling strategy against simpler alternatives** (e.g., random variable selection, fixed top-probability selection). This would ground the claim that the MAB formulation adds value beyond the GNN predictions.

5. **Clarify the "3–10× speedup" claim** by pointing to specific entries in Table 2 and explaining the calculation.

## Score and Decision

This paper addresses a practically important problem (MILP reoptimization under dynamic parameters) with a plausibly effective architecture. The two-stage design is well-motivated, and the empirical results — while limited by the small test set — suggest genuine promise. However, the paper has **two major weaknesses that must be resolved**: the GNN training objective is unspecified, rendering the core learning component non-reproducible; and the experimental evaluation lacks any uncertainty quantification, making it impossible to assess whether the reported advantages are reliable. These are not fatal — they can be fixed with careful writing and additional analysis — but they are too significant to overlook in the current form.

The contribution is real but the presentation and experimental rigor fall short of what is needed to support the claimed state-of-the-art performance. I would recommend **revision and resubmission** rather than acceptance as-is.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>