- Decision: Accept
- Scores: 8, 8, 6, 6

## Merged Review

### Summary
This paper introduces a reward dimension reduction technique for multi-objective reinforcement learning (MORL) that applies an affine transformation with row-stochastic and positivity constraints to map high-dimensional rewards to a lower-dimensional space. Theoretical conditions are established to guarantee that Pareto-optimality is preserved after transformation and that a valid mapping between reduced and original preference spaces exists. A reconstruction neural network is added to retain information. The method is designed for online learning, unlike prior static-dataset approaches. Evaluation is performed on a traffic light control environment with sixteen objectives, and the results demonstrate superiority over existing reduction and non-reduction baselines. The paper also proposes a new training and evaluation framework for reward dimension reduction in MORL.

### Strengths
- Well-motivated: scalability of MORL to many objectives is crucial for real-world applications but rarely studied (R1, R3).
- Simple, elegant, and modular approach that can be applied with other MORL methods (R2, R4).
- Clear theoretical explanations and proofs (sufficient condition for Pareto-optimality preservation) that are easy to follow (R1, R4).
- Well-written and organized, accessible to non-experts (R1, R2, R4).
- Empirical evaluations and ablation studies (including dropout effect, Table 3) are convincing and show strong performance in a high-dimensional environment (R1, R2, R4).
- Novelty: first method to address reward dimension reduction in an online MORL setting with theoretical Pareto-optimality guarantees (R2, R4).
- Proposes a new evaluation setup/benchmark tailored for high-dimensional MORL (R2).
- Demonstrates potential new state-of-the-art for the given experiment (R4).
- Focuses on an important and under-explored problem (R3).

### Weaknesses
- **Limited empirical scope**: Experiments are conducted on only a single environment (traffic light control) (R2, R3, R4). This restricts generalization; claims of superiority should be interpreted with caution (R2). No variation of the number of objectives \(m\) is explored (R3).
- **Lack of uncertainty estimates**: Despite using 8 random seeds, evaluation tables do not include confidence intervals or standard deviations. Reviewer 2 would raise their score if these are added.
- **Theoretical concerns**:
  - No theoretical justification that reward dimension reduction actually improves MORL training; compression may cause information loss (R3).
  - The condition provided is sufficient but not necessary; text (L320) implies necessity, which oversells the result (R4).
  - Theorem 1 is limited to linear relationships; a counterexample for the missing direction would help understand the breakdown (R4).
  - It remains unclear whether the approach generalizes to PSD matrices (R4).
- **Insufficient coverage of Pareto front**: Number of test preferences \(N_e\) may be too small even for the 4-dimensional reduced space. Learned policies may cover a broad front in reduced space but only a narrow region in the original 16-dim space, leading to low sparsity. Metrics like hypervolume and sparsity might not detect this issue (R1).
- **Missing evaluations on existing MORL benchmarks**: Evaluation on benchmarks with fewer objectives would help assess the influence of the reduction method and visualize the Pareto front in both spaces (R1).
- **Pre-assumed reduced dimensionality**: Rank \(r=4\) is treated as known at the end of training. The impact of different rank choices and the possibility of adaptive rank selection are not investigated (R4).
- **Comparison to baselines**:
  - Unclear whether NPCA was properly tuned (regularization strength) and the reference is missing (R4).
  - Additional baselines from the MORL or successor features literature could enrich the comparison (R4). Reviewer 2 suggests including Weber et al. (2023).
- **Metric and reporting questions**:
  - Values in Tables 1 and 2 are extremely large; explanation of metric scaling and normalization requested (R3, R4). The choice of reference point for hypervolume in Table 1 is unclear (R4).
  - Learning curves or dynamic statistics (e.g., rliable) would provide more insight (R4).
- **Implementation/ablation details**:
  - Ablation of the positivity constraint (in addition to row-stochastic) is missing from Table 4 (R4).
  - Complexity of the constrained optimization problem and the overhead due to finite episode length (L500) are not addressed (R4).
  - Dropout effect explanation (L475) is confusing and needs rewording (R4).
- **Missing connections to related work**:
  - Relationship to the successor features framework (R4, reference [2]).
  - Connection to paper referenced as [1] (L325) is mentioned but not discussed (R4).
- **Minor issues**: Figure 2 quality is low (increase DPI); typo: “works” should be “work” (R4).

**Reviewer disagreement**: Two reviewers (R1, R2, scores 8) found the evaluation convincing and praised novelty and clarity. Two others (R3, R4, scores 6) had stronger reservations about experimental breadth and theoretical depth, requesting additional justification, environments, and analysis.