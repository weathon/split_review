Now let me write the final consolidated review.

## Summary

This paper proposes NeuralQP, a two-stage framework for large-scale QCQPs combining (1) a hypergraph neural network (UniEGNN) operating on a novel "variable relational hypergraph" representation to predict solutions, and (2) an iterative neighborhood optimization procedure that uses a small-scale solver (Gurobi/SCIP restricted to 30–50% of variables) on subproblems, with a McCormick relaxation-based repair strategy (Q-Repair) to handle infeasibility from neighborhood crossover. Experiments on three benchmark QCQP types report that the framework achieves better objective values than full-scale Gurobi and SCIP within the same wall-clock time.

## Strengths

- **Novel variable relational hypergraph representation for QCQPs** (Section 3.3, Definitions 4–8). The paper formally defines a 3-uniform bipartite hypergraph that encodes linear, squared, and bilinear terms from both objective and constraints using auxiliary vertices v₀ and v². Prior graph representations for optimization (Gasse et al. 2019, Ding et al. 2019) were restricted to MILPs; this is a principled extension that enables GNN-based methods to operate on QCQPs without requiring shared parametric structure across instances. The representation is well-defined and the connection to hypergraph neural networks is clearly established.

- **McCormick relaxation-based repair strategy for neighborhood crossover in quadratic problems** (Section 4.2.1, Equation 6). The Q-Repair algorithm linearizes quadratic terms via term-wise McCormick envelopes, then applies a linear repair procedure to detect violated constraints and progressively reintroduce fixed variables into the neighborhood. This is a nontrivial extension of prior repair methods (Ye et al. 2023b) that addressed only linear problems, and it enables the iterative neighborhood optimization loop for QCQPs.

- **Adaptive neighborhood partitioning** (Section 4.2.2). The framework switches between constraint-based (ACP) and variable-based random partitioning depending on problem density, addressing a practical issue where dense constraints cause excessive neighborhoods. This shows awareness of the diversity of QCQP structures beyond a monolithic recipe.

## Weaknesses

### Major

1. **Missing critical baseline: NeuralQP without neural prediction.** The paper compares NeuralQP (neural prediction + iterative neighborhood optimization with a small-scale solver) against full-scale Gurobi and SCIP. This conflates two effects: (a) the benefit of the decomposition strategy itself (solving many small subproblems with a solver that is vastly more effective at smaller scales), and (b) the benefit of the neural prediction over random initialization. The essential control experiment — running the **same iterative neighborhood optimization pipeline with random initialization instead of neural prediction** — is absent. Without it, the reader cannot attribute the observed performance to the claimed neural contribution. The results may be driven entirely by the well-known fact that Gurobi/SCIP scale superlinearly in problem size, making subproblem decomposition trivially more efficient. **This is the single most significant evidential gap in the paper.**

2. **Near-complete absence of training and architectural details.** The paper mentions training "9 neural network models" but provides **none** of the following: loss function, optimizer, learning rate schedule, number of epochs, batch size, number of UniEGNN layers, hidden dimension sizes, activation functions, dataset sizes per problem type/scale, train/validation/test split, random seeds, or compute infrastructure. The only architectural information is that aggregation functions are SUM (for hyperedges) and MEAN (for vertices), and that MLPs are used for φₑ, φᵥ, ψₑ, ψᵥ. This makes it impossible to assess the soundness of the neural component, impossible to reproduce the results, and impossible to determine whether the GNN is even learning meaningful representations. For a paper whose title foregrounds the neural method, this is a critical omission.

3. **Insufficient statistical evidence.** Results are reported as averages over only 3 instances per problem type/scale combination (line 234: "Each value is averaged among 3 similar instances"). No standard deviations, confidence intervals, or instance-level variance are reported. For optimization problems where solution quality can vary dramatically across instances of the same class, 3 instances is far too small to draw reliable conclusions. The absence of any uncertainty quantification means the reported advantages may be driven by idiosyncratic instance selection.

### Minor

4. **Overclaimed generality.** The paper repeatedly claims to operate "without any problem assumption" (abstract, contributions, conclusion) and contrasts this against prior work that "make strong assumptions about the model parameters." However, the method requires training separate neural network models per problem type **and** per scale (9 models for 3 types × 3 scales), which assumes training data from the same distribution as test problems — itself a substantive data availability assumption. The claim is overstated relative to what the method actually delivers.

5. **UniEGNN is not ablated against standard UniGNN.** The paper introduces UniEGNN as an enhancement of UniGNN that uses hyperedge features explicitly (Equation 5 vs. Equation 4). However, no ablation study compares UniEGNN against standard UniGNN on the same hypergraph representation. Without this, the reader cannot assess whether the architectural modification matters, or whether any baseline GNN operating on the same hypergraph would perform similarly.

6. **Q-Repair algorithm description leaves key details unspecified.** The algorithm (Section 4.2.1) states that "if the constraint is violated, the fixed variables within it are added to the neighborhood one by one until the solution becomes feasible," but does not specify the ordering heuristic for variable reintroduction, the exact criterion for detecting violation under the McCormick relaxation, or how the guarantee that the unfixed count stays below α_ub·n is maintained. These details are necessary for reproducibility of the central repair mechanism.

### Trivial

- The conclusion states "A future direction is extending our framework to nonlinear programming" — but QCQPs are already a subclass of nonlinear programs. This phrasing is confused.

## Nice-to-Haves

- Report results on the real-world libraries (QAPLIB, QPLIB) mentioned in the paper, at least in summary form in the main text.
- Compare against prior ML-based QCQP methods (e.g., Bertsimas & Stellato 2020/2021) if the problem settings permit.
- Provide the density threshold used for switching between ACP and random partitioning (Section 4.2.2).
- Analyze the computational overhead of the neural network inference and Q-Repair relative to the solver time.

## Removed Points

These points were flagged by reviewers but removed during consolidation:

1. **Criticism about missing footnotes (1., 2., 3., 4.) and missing appendix results for QAPLIB/QPLIB.** — Removed. The parser strips footnotes and appendix content from all papers; these sections exist in the original submission. Per the hard rules, I may not penalize for missing appendix content.

2. **Criticism about "unfair comparison" framed as Gurobi/SCIP on small subproblems vs. full problem being inherently biased.** — Merged into Weakness #1 (missing baseline). The core issue is the absence of a random-initialization control, not that the comparison is "unfair." Per the rule: remove weaknesses about unfair comparison if asymmetry favors the baseline (here the asymmetry could favor the method, but the proper fix is a control experiment, not discarding the comparison).

3. **Complaint that "Table 1... the claims in the text are clear enough to evaluate" while noting images are embedded.** — Tables are embedded as images in the parsed text, but the paper itself presumably renders them properly. This is a parser artifact, not a paper flaw.

4. **Strength Finder's more generic/superficial claims** (e.g., "addressed an important problem" — removed; the retained strengths are concrete and evidence-backed).

## Novel Insights

Beyond the paper's own contributions, the reviews reveal that the fundamental challenge this line of work faces is the attribution problem: when a combined neural+decomposition method outperforms a full-scale solver, is the improvement due to the learned predictions or simply the subproblem decomposition? The paper's experimental design does not resolve this ambiguity, and its missing baseline is not a minor oversight but a structural gap that prevents the reader from evaluating whether the neural component is genuinely useful or ornamental. This attribution problem is likely to recur in similar ML-for-optimization frameworks that combine neural prediction with local search or decomposition — the community would benefit from methodological standards (e.g., always including a "no neural" control) that the current paper does not follow.

## Suggestions

1. **Add the single most important control experiment:** run the entire iterative neighborhood optimization pipeline with random initialization (or a simple heuristic like the variable bounds midpoint) instead of neural prediction, keeping everything else identical. If the gap between this baseline and NeuralQP is small, the neural component adds little.

2. **Provide complete training details:** report loss function, optimizer, learning rate, epochs, batch size, hidden dimensions, number of UniEGNN layers, activation functions, dataset sizes, train/val/test splits, and compute infrastructure. Without these, the paper's ML component cannot be evaluated.

3. **Report results over more instances** (at least 20–30 per setting) with standard deviations and, ideally, per-instance results.

4. **Add an ablation comparing UniEGNN against standard UniGNN** on the same hypergraph to validate the architectural contribution.

5. **Tone down the "without any problem assumption" claim** to accurately reflect the method's data distribution requirements.

## Score and Decision

**Score:** 4.0

**Decision:** Reject

The paper introduces a plausible framework and a legitimate hypergraph representation for QCQPs. However, the evaluation has a critical gap: the missing baseline that isolates the neural prediction's contribution. Combined with the near-complete absence of training details for the neural component (making it impossible to assess or reproduce) and the very small test set (3 instances per setting with no variance reporting), the evidence is insufficient to support the paper's claims at a top conference. The core ideas have potential, but the experimental validation does not meet the standard required for acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>