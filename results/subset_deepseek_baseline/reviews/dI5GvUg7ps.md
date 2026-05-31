## Summary

This paper introduces RewardRank, a two-stage learning-to-rank framework that directly optimizes counterfactual user utility rather than traditional proxy metrics like NDCG. The approach first learns a permutation-aware reward model from logged user interactions, then trains a ranker to maximize predicted utility using differentiable soft permutation operators (SoftSort). The authors also propose two evaluation benchmarks—PO-Eval (parametric oracle on Baidu-ULTR) and LAU-Eval (LLM-as-user on Amazon-KDD-Cup)—for reproducible counterfactual ranking evaluation. Experiments show RewardRank achieves higher counterfactual utility than existing methods, and establishes state-of-the-art on Baidu-ULTR with real user clicks.

## Strengths

- **Novel problem formulation**: The paper correctly identifies that traditional LTR metrics (NDCG) are misaligned with true user utility, and proposes a principled counterfactual utility maximization framework. This is an important and under-explored direction in learning-to-rank.

- **Two-stage architecture with theoretical grounding**: The separation into reward model learning and ranker optimization via soft permutations is well-motivated. The use of SoftSort for differentiable ranking and the misspecification correction term (Eq. 13) show thoughtful design.

- **Comprehensive evaluation framework**: The two proposed benchmarks (PO-Eval and LAU-Eval) address the critical challenge of counterfactual evaluation in ranking. The LAU-Eval using LLMs to simulate behavioral biases (position, brand, similarity aversion) is particularly innovative and addresses real limitations of existing evaluation protocols.

- **Strong empirical results**: RewardRank achieves the highest counterfactual utility on both benchmarks and establishes SOTA on Baidu-ULTR with real clicks (DCG@5: 5.83, DCG@10: 8.42), outperforming strong baselines including LambdaRank and PiRank.

- **Clear demonstration of metric misalignment**: The paper provides concrete evidence (Table 1) that methods optimizing NDCG can achieve high surrogate scores while underperforming on true utility, validating the core motivation.

## Weaknesses

### Major

- **Limited novelty relative to existing work**: The two-stage "generator-evaluator" framework is already established in prior work (URCC, NLGR, PRS, PIER). The main technical differences—using SoftSort for differentiable ranking and a transformer-based reward model—are incremental. The paper would benefit from clearer articulation of what is fundamentally new versus engineering improvements.

- **Computational cost concerns**: The approach requires training a transformer-based reward model (110M parameters) and a separate transformer-based ranker, plus computing soft permutation matrices during training. The paper does not discuss training time, inference latency, or practical feasibility for real-time ranking systems. This is a significant omission for a method targeting production deployment.

- **The misspecification correction (Eq. 13) is heuristic**: The weighting scheme $w_i = 1 - \lambda|u_i - \hat{u}_i|$ is motivated by intuition but lacks theoretical justification. The paper does not prove that this provides a valid upper bound or that it converges to the correct objective. The ablation shows modest gains, suggesting this component may not be critical.

- **Limited analysis of failure cases**: The paper does not discuss scenarios where RewardRank might underperform. For example, when the reward model is poorly calibrated (common with limited data), the ranker could be misled. The paper acknowledges reward misspecification but provides limited analysis of when and why it occurs.

### Minor

- **The LAU-Eval prompt design is not fully specified**: While Appendix C.2 is referenced, the paper does not provide the exact prompt template or discuss potential biases in LLM-based evaluation (e.g., LLMs may exhibit different behavioral patterns than real users). The reproducibility of LAU-Eval depends on prompt details.

- **Ablation results are only briefly mentioned**: The paper states that removing the auxiliary item-level loss decreases performance and that $\tau=0.5, \lambda=0.7$ are optimal, but does not provide full ablation tables or statistical significance tests. This makes it difficult to assess the robustness of these design choices.

- **The "Upper-Bound" in PO-Eval is only reported for the oracle method**: The paper does not explain why an upper bound is not computed for LAU-Eval, which would help contextualize the 0.561 purchase rate achieved by RewardRank.

### Trivial

- Figure 2 is difficult to interpret due to repetitive caption text (likely a parser artifact).

## Nice-to-Haves

- Analysis of training/inference computational cost compared to baselines
- Ablation study with full tables and statistical significance
- Discussion of when the reward model might fail and how to detect such failures
- Comparison with reinforcement learning approaches (e.g., policy gradient methods beyond PG-Rank)

## Novel Insights

The paper's key insight is that optimizing NDCG or similar surrogate metrics can be fundamentally misaligned with true user utility, and that a data-driven reward model trained on logged interactions can capture behavioral biases (position, diversity, similarity aversion) without explicit modeling assumptions. The demonstration that LLMs can serve as evaluators for ranking quality, capturing complex behavioral patterns beyond position bias, is a novel methodological contribution. However, the core idea of learning a utility function and then optimizing a ranker against it is not new; the novelty lies in the specific implementation choices (SoftSort, transformer architecture, misspecification correction) and the evaluation framework.

## Suggestions

1. Provide a more detailed comparison with the closest prior work (URCC, NLGR) to clearly delineate technical differences and advantages. Currently, the paper claims superiority but does not fully explain why the soft permutation approach outperforms pairwise swap exploration.

2. Include training time and inference latency comparisons. For a method targeting production systems, practical feasibility is crucial.

3. Add a discussion of when the reward model might fail (e.g., distribution shift between training and deployment, sparse feedback regimes) and how practitioners could detect such failures.

4. Provide the full LAU-Eval prompt in the main paper or appendix to ensure reproducibility.

5. Consider adding a simple baseline that directly optimizes the reward model's predictions without the two-stage framework, to isolate the benefit of the ranker optimization stage.

## Score and Decision

The paper addresses an important problem (misalignment between proxy metrics and true utility in ranking) and provides a well-engineered solution with strong empirical results. The evaluation framework (PO-Eval and LAU-Eval) is a valuable contribution to the community. However, the technical novelty is incremental relative to existing two-stage counterfactual ranking methods, and the paper lacks discussion of computational costs and failure modes. The work is solid and deserves acceptance, but does not represent a breakthrough.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>