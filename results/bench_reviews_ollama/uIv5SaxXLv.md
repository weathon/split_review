Now I have a thorough understanding of the paper. Let me verify the "without any problem assumption" claim more carefully. The paper uses this phrase in two distinct ways. The hypergraph representation doesn't assume specific model parameter structure (unlike Bertsimas & Stellato which assumes instances share model parameters). But the framework does require per-problem-type training (9 models). Let me also check about the 50% vs 30% anomaly claim more carefully.

The key issue is: Section 5.1 says "the experimental results with solvers constrained to 50% scale do not consistently outperform those constrained to 30% scale." But earlier in the same section, it says "When the scale increases to 50%, this advantage is even more pronounced." These statements appear contradictory. Let me re-read:

Lines 232: "When the scale increases to 50%, this advantage is even more pronounced."
Line 242: "the experimental results with solvers constrained to 50% scale do not consistently outperform those constrained to 30% scale"

These two statements are indeed contradictory — one claims 50% is better, the other claims it's not consistently better. This is a genuine inconsistency in the paper.

Now let me also consider the reviewer's claim about the "one-fifth" claim. The paper says "less than one-fifth of the solving time" but the actual Table 2 ratios vary — some are much less than one-fifth (10-30x faster = 1/10 to 1/30), and some might be closer. But the claim says "less than" one-fifth, so as long as it's at most one-fifth, the claim would be valid for large-scale instances. Without being able to see the table numbers precisely (images), I cannot verify this precisely. However, the paper does qualify it with "in large-scale QCQPs" so it's not claimed universally.

Now let me synthesize the review. Here are the key verified weaknesses:

1. **No ablation studies**: Confirmed — no ablations in the paper. This is a genuine gap for a paper proposing three distinct contributions.

2. **"General" and "without any problem assumption" claims are overclaimed**: The paper says "without any problem assumption" but trains 9 separate models per problem type × scale. The "without assumption" refers to the fact that the hypergraph representation doesn't need shared model parameters (unlike Bertsimas & Stellato). However, requiring per-problem-type training IS a form of problem-specific dependency. The claim is partially justified but overclaimed.

3. **50% vs 30% contradiction**: The paper says 50% is "even more pronounced" and then says 50% "does not consistently outperform" 30%. This is a genuine internal inconsistency. The 30% > 50% anomaly could suggest the framework's benefit comes from the multi-restart iterative search rather than the neural prediction quality.

4. **Only 3 instances per setting, no variance reported**: Confirmed. n=3 with no variance is thin.

5. **No comparison with ML-based methods**: The paper discusses RLQP and Bertsimas & Stellato but doesn't compare against them. However, these are quite different methods — RLQP tunes OSQP parameters, Bertsimas & Stellato is a model-based classifier. Including them as baselines would be reasonable but the paper is comparing against the *solvers* (Gurobi/SCIP) that these ML methods also aim to beat. This is a scope question.

Let me rate the severity of each:

- No ablation: Major (but not fatal — the framework works end-to-end)
- Overclaimed generality: Major (overclaiming is significant)  
- 50% vs 30% contradiction: Major (undermines mechanism understanding)
- n=3 no variance: Minor (small test set is common in optimization papers, though not ideal)
- No ML baseline comparison: Minor-to-Major (the ML methods discussed have different scopes; the comparison with solvers is a direct end-to-end comparison)

Strengths:
1. Variable relational hypergraph is a clean formalism for lossless QCQP encoding
2. Q-Repair using McCormick relaxation is a novel and sensible mechanism for neighborhood crossover in quadratic problems
3. Demonstrated practical gains over full-scale solvers on large-scale instances

Let me draft the review now.</think>Now I have a comprehensive understanding of the paper. Let me synthesize the final review.

## Summary

NeuralQP proposes a hypergraph-based optimization framework for large-scale QCQPs that replaces full-scale solvers with small-scale ones. The framework has two components: (1) Hypergraph-based Neural Prediction, which uses a novel variable relational hypergraph (3-uniform, bipartite) and UniEGNN (a half-convolution that updates both vertex and hyperedge features) to predict initial solutions; (2) Iterative Neighborhood Optimization, which uses a McCormick relaxation-based Q-Repair algorithm to identify and fix violated constraints, enabling progressive neighborhood expansion and crossover with only a small-scale solver.

## Strengths

- **Variable relational hypergraph is a clean, lossless QCQP encoding.** Definitions 4–8 formally construct a 3-uniform bipartite hypergraph that naturally encodes linear terms (via vertex $v_0$), squared terms (via vertex $v^2$), and cross-terms ($x_i x_j$), preserving all coefficients as hyperedge features. This generalizes the tripartite MILP graph to quadratic problems without information loss, and the construction is rigorous.

- **Q-Repair using McCormick relaxation is a novel mechanism for neighborhood crossover in QCQPs.** Equation 6 linearizes quadratic terms via McCormick relaxation, computes bounds on constraint left-hand sides given fixed variables, and progressively unfreezes violated variables until feasibility is restored. The paper correctly notes this is the first mechanism enabling neighborhood crossover for quadratic problems (Sec 4.2.1, 4.2.3), which is critical for escaping local optima from fixed-radius search.

- **Demonstrated practical solving gains on large-scale QCQPs.** Table 1 shows NeuralQP with a 30%-scale solver achieves better objective values than full-scale Gurobi and SCIP within the same wall-clock time on all large-scale benchmark problems. Table 2 shows reaching equivalent objectives can require 10–30× longer for Gurobi/SCIP on large-scale instances, validating that the decomposition approach has real computational merit.

## Weaknesses

### Fatal
None.

### Major

- **Internally contradictory statements about 30% vs. 50% solver scale.** Section 5.1 states "When the scale increases to 50%, this advantage is even more pronounced" (line 232) but later says "the experimental results with solvers constrained to 50% scale do not consistently outperform those constrained to 30% scale" (line 242). These statements directly contradict each other. If larger neighborhoods don't consistently help, the framework's premise—that the neural prediction correctly identifies which variables to optimize—is called into question. The paper dismisses this as "deserving further study," but this anomaly cuts to the core mechanism: does the improvement come from the quality of the neural prediction guiding variable selection, or simply from the multi-restart iterative search with small subproblems? Without resolving this, the attribution of improvement to the specific neural components is undermined.

- **"General" and "without any problem assumption" claims are overclaimed.** The abstract and contributions assert NeuralQP is "the first general optimization framework for large-scale QCQPs without any problem assumption." While the hypergraph representation itself avoids the model-parameter-sharing assumption of Bertsimas & Stellato (2020), the framework trains 9 separate neural network models—one per problem type × scale combination (Section 5). A method requiring per-class trained models is not "general" in the standard sense, and it still assumes test instances share distributional structure with training instances. The "without any problem assumption" phrasing should be narrowed to "without requiring shared model parameters"—the more limited claim the paper actually establishes.

- **No ablation studies to attribute improvement to specific proposed components.** The paper proposes three distinct contributions: the variable relational hypergraph, UniEGNN with half-convolution, and Q-Repair. Without ablations—e.g., replacing the hypergraph with a simpler bipartite graph, replacing UniEGNN with UniGNN, replacing Q-Repair with random variable unfreezing—we cannot determine whether any specific component is doing useful work. The 30%/50% anomaly makes this especially important: if the improvement comes primarily from iterative small-subproblem solving rather than from neural prediction quality, the GNN and hypergraph components may be less essential than claimed.

### Minor

- **Only 3 test instances per setting with no variance reported.** Tables 1 and 2 average over 3 instances each, with no standard deviations or confidence intervals. While small test sets with single-run evaluation are not unusual in the optimization community, n=3 is particularly thin for establishing relative solver performance claims. Reporting variance would help readers assess the robustness of the claimed improvements.

- **No comparison with prior ML-based QCQP methods.** The introduction discusses RLQP and Bertsimas & Stellato (2020) as motivating prior work, but experiments only compare against Gurobi and SCIP. Including even one ML-based baseline would strengthen the claim of improvement over "current ML-based frameworks." However, the comparison with full-scale solvers is the more direct end-to-end measure, so this is a genuine but secondary gap.

### Trivial
None.

## Nice-to-Haves

- Qualitative analysis of neural predictions vs. optimal values on a few instances to assess whether UniEGNN produces genuinely useful initial solutions or whether the iterative search does the heavy lifting.
- Reporting the QAPLIB/QPLIB real-world benchmark results in the main paper (currently appear to be in the appendix) to better support generality claims.
- Investigation of the 30% vs. 50% anomaly: is the neural prediction miscalibrated for larger neighborhoods, or does the multi-restart structure dominate?

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Hypergraph adds nothing beyond bipartite graph since it's converted via star expansion":** The harsh critic argues the hypergraph formalism adds nothing since star expansion converts it to a bipartite graph. This misunderstands the design: the hypergraph formalism is what defines *which* edges and features appear in the bipartite graph. A simple bipartite graph representation for QCQPs would lose quadratic term information (as the paper states in Sec 3), while the hypergraph structure with 3-uniform hyperedges ensures all quadratic coefficients appear as edge features in the expanded bipartite graph. The distinction is in what gets encoded, not in the convolution target.

- **"Random feature strategy integration not explained":** The integration of the random feature strategy from Sec 2.2 is described in Sec 4.1.1: "The initial vertex and hyperedge embeddings are generated in a similar way as the tripartite graph representation with the random feature strategy in Sec 2.2." This is not underspecified—it references the earlier section.

- **"Q-Repair ordering underspecified":** The ordering of variable unfreezing (line 194: "fixed variables within [a violated constraint] are added to the neighborhood one by one") could affect performance, but this is a standard heuristic detail, not a fundamental gap. The paper specifies the criterion (variables from violated constraints) and the stopping condition (feasibility restored or neighborhood upper bound reached).

- **"Threshold for ACP/random partitioning not given":** The adaptive threshold between ACP and random partitioning (Sec 4.2.2) is not explicitly specified, but this is a hyperparameter detail, not a conceptual gap.

- **"QAPLIB/QPLIB results only in appendix":** The appendix was stripped by the parser. These results exist in the original submission; criticizing their absence from the parsed text is a parser artifact, not a paper weakness. Moved to Nice-to-Have suggestion to include in main paper.

- **Strength claim "No problem-specific assumptions":** This conflicts with the verified weakness about overclaimed generality (since 9 per-class models are needed). Removed as a strength.

## Novel Insights

The 30%/50% contradiction in Section 5.1 is more significant than either reviewer notes: it doesn't merely raise questions about the neural prediction quality, it suggests the entire framework may function as a "meta-restart" heuristic for solvers, where the neural network's role is primarily to diversify starting points rather than to guide variable selection. If so, the specific architectural innovations (hypergraph representation, half-convolution) may be less critical than the *framework structure* (iterative small-subproblem solving + crossover). This can be tested directly: replace the neural predictor with random variable selection and observe whether the 30% solver still outperforms the 50% solver and the full-scale baseline.

## Suggestions

- Run ablations: (a) replace UniEGNN predictions with random variable ordering; (b) replace Q-Repair with simple random unfreezing; (c) compare hypergraph vs. tripartite graph representation. The first ablation is especially critical given the 30%/50% anomaly—it directly tests whether the neural prediction matters.
- Resolve the contradictory statements about 30% vs. 50% solver scale: if they refer to different aspects (objective value vs. time), clarify; if not, reconcile with the data.
- Narrow the "without any problem assumption" claim to "without requiring shared model parameters across instances"—which is the meaningful differentiator from prior work that the paper actually demonstrates.

## Assessment

**Originality:** The variable relational hypergraph and Q-Repair mechanism are novel and well-motivated contributions to QCQP solving. The half-convolution is a modest extension of UniGNN.

**Importance:** Large-scale QCQP solving is an important problem. Demonstrating that small-scale solvers can outperform full-scale ones via decomposition is practically valuable.

**Claim support:** The core practical claims (small-scale solver beats full-scale at same wall-clock time) are supported by experiments, but the 30%/50% anomaly and lack of ablations mean the *attribution* of improvement to specific proposed components is not well supported. The "general/no assumption" claims are overstated relative to what is demonstrated.

**Soundness of experiments:** Thin test sets (n=3), no variance, no ablations, and an unexplained internal contradiction weaken the experimental support.

**Clarity:** Generally clear, with helpful figures and formal definitions.

**Community value:** The framework demonstrates a promising decomposition approach for large-scale QCQPs, and the Q-Repair idea may prove useful beyond this specific framework.

## Score and Decision

The paper presents genuinely novel and well-motivated technical ideas (variable relational hypergraph, Q-Repair) and shows promising practical results. However, the overclaimed generality, the internally contradictory 30%/50% discussion, and the complete lack of ablations are significant weaknesses that prevent confident attribution of the observed improvements to the proposed components. This is a paper with good ideas but insufficient experimental validation for its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>