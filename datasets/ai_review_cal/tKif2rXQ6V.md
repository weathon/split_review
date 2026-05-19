- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have all the information I need to produce the final consolidated review. Let me write it.

## Summary

This paper introduces SteBen, a benchmark dataset for the Steiner Tree Problem (STP) aimed at the neural combinatorial optimization (NCO) community. The dataset claims 1.28 million optimally solved instances across four graph models (ER, WS, RR, Grid) with node sizes up to 1000. The paper implements and compares baselines spanning the four combinations of autoregressive/non-autoregressive and supervised/reinforcement learning paradigms (PtrNet, Cherrypick, DIFUSCO, DIMES), and provides a reinforcement learning environment.

## Strengths

- **Addresses a genuine gap in the NCO literature.** The paper correctly identifies that STP — an NP-hard problem with practical applications in network design and facility location — has been underserved by learning-based methods partly due to the lack of large-scale datasets. Existing resources (SteinLib, Bonnet & Sikora 2018) offer only dozens of instances, which is insufficient for training modern neural models. (Section 1, Section 2.3)

- **Comprehensive baseline implementation across four NCO paradigms.** The paper adapts methods spanning all four combinations (AR+SL: PtrNet; AR+RL: Cherrypick, AM; nAR+SL: DIFUSCO; nAR+RL: DIMES) and describes STP-specific modifications such as level-order tree traversal for PtrNet, GNN-based edge feature initialization for DIFUSCO, and shared decoding strategies. This provides a standardized evaluation framework that did not previously exist for STP. (Section 4.2)

- **Sample efficiency analysis.** Figure 2 and the accompanying discussion examine how supervised methods (PtrNet and DIFUSCO) degrade with reduced training samples, showing that DIFUSCO maintains greater robustness in low-sample regimes while exhibiting a steeper relative performance drop from its peak. This provides practical guidance for future data collection. (Section 6, Figure 2)

## Weaknesses

### Fatal

None.

### Major

- **Optimal solution generation method is not specified.** The paper repeatedly claims that SteBen provides 1.28 million "optimally solved" instances (Section 4.1: "optimally solved samples"; Abstract: "high-quality instances with optimal solutions"). The STP is NP-hard; solving instances up to 1000 nodes to proven optimality is computationally intense. However, the paper provides **no description of how optimal solutions were obtained** — no solver name (SCIP-Jack, Gurobi, CPLEX, etc.), no time limits, no verification procedure, no discussion of what fraction of large instances could be solved to proven optimality versus approximated. Section 4.1 and Algorithm 1 describe only instance *generation* (graph sampling, terminal assignment, edge costs), not solution computation. Without this information, the dataset's foundational claim — that it provides exact solutions for supervised learning — is unverifiable. The authors must specify the exact solver, parameters, computational budget, and optimality certification process.

- **Real-world generalization claim is unsubstantiated.** The abstract states that "solvers trained on our datasets generalize well to real-world instances without fine-tuning, proving its practical utility," and Contribution 3 repeats this claim. However, the paper contains **no description of any real-world test set, no evaluation methodology for this claim, and no results on real-world instances.** This claim appears as an assertion without any supporting experiment. Either it must be removed from the contributions or supported with a proper experiment description and results.

### Minor

- **The "Gap" evaluation metric is never defined.** Section 5.1 states that "evaluation metrics include the average Gap of the predicted solutions" but never specifies the formula. It is reasonable to assume Gap = (solution cost − optimal cost) / optimal cost, but this should be stated explicitly. The missing definition is a clarity issue that affects interpretability of any results.

- **Dataset composition breakdown is missing.** The paper states there are 1.28 million instances across four graph types and five training sizes (10, 20, 30, 50, 100) plus larger test sizes (200, 500, 1000). However, the distribution per graph type per node size is not given. For a benchmark dataset paper, this breakdown is important for understanding coverage and potential biases.

- **Training hyperparameters for baselines are sparse.** The paper states that all baselines were evaluated "under the same computational budget, using identical feature embedding techniques and decoding strategy" and gives training/validation split sizes (1M/280K). However, no hyperparameters (learning rates, batch sizes, number of training episodes for RL methods, optimizer choices, etc.) are reported. While hyperparameter disclosure is a standard reproducibility expectation for baseline comparisons, this is a common and addressable issue.

- **The "smoothing" explanation for AR model degradation is asserted without evidence.** Section 6 attributes the superior performance of non-autoregressive models to a "smoothing problem when aggregating partial solution information" in AR models. This is presented as the explanation but no diagnostic experiments (e.g., measuring representation quality vs. solution length) are provided to support it. It remains a plausible hypothesis rather than an evidenced finding.

- **Cherrypick decoding method is referenced but not explained.** The paper states that DIFUSCO and DIMES use the "Cherrypick decoding method" to maintain consistency, but what this decoding strategy entails is not described in the paper beyond the original Cherrypick citation. A brief summary would help readers understand the shared evaluation framework.

### Trivial

- None.

## Nice-to-Haves

- **Variance or confidence intervals on reported gaps.** The paper evaluates out-distribution on only 500 test samples; reporting variance would help assess reliability of these results.
- **Ablation of the shared decoding strategy.** The paper unifies decoding across baselines for fairness, but an ablation isolating its effect on each method would strengthen the comparison.
- **Broader terminal probability settings.** Using a single terminal probability (0.2) is noted as a limitation; including additional values would increase dataset diversity.
- **Dataset release information.** Explicitly stating how and when the dataset and code will be released (e.g., anonymized repository link) would improve reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Experimental results are absent from the review copy" / "Table 1 and Figure 2 cannot be evaluated."** The paper clearly contains Figure 2 (present as an image reference) and references Table 1 in the discussion text (Section 6: "As shown in Table 1"). The missing content is a parser artifact — Table 1 is likely an embedded image that was not extracted. The discussion text describes the trade-offs found. This is not a paper flaw; it is a parsing limitation. **Removed per the rule that formatting artifacts are parser issues, not author errors.**
- **"Transductive learning techniques excluded may disadvantage some methods."** The paper explicitly states this exclusion was "for fairness" (Section 4.2), which is a reasonable design choice for comparing constructive solvers. Speculating about disadvantage is not a concrete weakness.
- **"Single terminal probability (0.2) may be too uniform."** This is a dataset design choice acknowledged by the paper's own limitation statement. It is not a flaw per se, though a broader range would strengthen the resource. Moved to Nice-to-Haves.
- **Generic strengths about the problem being "important" or "well-motivated."** These are superficial and lack specific paper content.
- **"Real-world generalization" cited as a strength by the Strength Finder.** This claim is unsubstantiated (as noted in Major weaknesses), so it cannot be listed as a strength — the weakness and strength disagree, and the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The two-input reviews do not surface any perspective that meaningfully reinterprets the paper or reveals a non-obvious implication of its results that the authors themselves did not articulate.

## Suggestions

1. **Specify the optimal solution generation methodology in full.** State the exact solver (e.g., SCIP-Jack, Gurobi), time limits per instance, machine specifications, optimality verification procedure, and — critically — report for which instance sizes 100% of instances were solved to proven optimality and whether any approximations were used for the largest instances. This is the single most important revision.

2. **Either provide a real-world evaluation or remove the claim.** If real-world instances exist, describe them, explain how they were obtained, and report quantitative results. If such an evaluation has not been performed, the generalizability claim should be removed from the abstract and contributions.

3. **Define the Gap metric explicitly** in Section 5.1.

4. **Provide a composition table** showing the number of instances per graph type (ER/WS/RR/Grid) per node size (10/20/30/50/100 for training; 200/500/1000 for test), so users can assess coverage and balance.

5. **Report training hyperparameters** for all baselines (learning rate, batch size, optimizer, number of RL episodes, etc.) to improve reproducibility.
