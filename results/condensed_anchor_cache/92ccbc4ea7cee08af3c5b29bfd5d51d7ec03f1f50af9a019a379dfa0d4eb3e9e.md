- Decision: Accept
- Scores: 6, 6, 6, 8

## Merged Review

### Summary
The paper proposes UNR-Explainer, an MCTS-based method for generating counterfactual (CF) explanations in unsupervised node representation learning. It identifies important subgraphs whose perturbation causes a significant change in a node's k-nearest neighbors in the embedding space. The method is evaluated on six datasets (BA-Shapes, Tree-Cycles, Tree-Grid, Cora, CiteSeer, PubMed) with GraphSAGE and DGI, and compared against eight baselines on precision, recall, validity, size, and importance. A case study on NIPS shows meaningful subgraphs. The paper also provides an upper bound analysis of the Importance measure and an ablation study of MCTS variants. Overall, reviewers find the topic interesting and the evaluation thorough, but raise concerns about novelty relative to SubgraphX, lack of analysis on simple baselines that achieve strong performance, computational cost of MCTS, insufficient discussion of underperformance, and missing practical validation. One reviewer is notably more positive (score 8, “exhaustive experiments,” “well written”), while the other three rate it 6 and are more critical of novelty, presentation, and analysis depth.

### Strengths
- **Novel problem and setting**: Tackles counterfactual reasoning for unsupervised node representation learning, which is relatively unexplored (R1, R2, R4). The work helps explain GNN models for unseen downstream tasks (R1).
- **MCTS-based approach**: Using Monte Carlo Tree Search to efficiently explore large subgraph spaces is a suitable choice (R2, R4). The method includes a “restart” policy in the Selection step to mitigate search bias (R1). Alterations to vanilla MCTS are theoretically grounded (R4).
- **Novel importance metric**: Equation 1 defines the counterfactual property via change in top-k nearest neighbors; this metric is inventive and well-motivated (R2, R3, R4). Reviewer 3 explicitly calls it novel.
- **Theoretical foundation**: An upper bound on the Importance function is provided for GraphSAGE (R2, R4).
- **Comprehensive experiments**: Evaluation on 3 synthetic and 3 real datasets with multiple metrics (precision, recall, validity, size, importance) and 8 methods (R4). Ablation study on MCTS variants and hyperparameter sensitivity (k, restart, perturbation) are included (R4).
- **Case study**: The NIPS citation-network case study demonstrates that UNR-Explainer selects qualitatively meaningful subgraphs (R3, R4).
- **Reproducibility**: Code is provided (R3).
- **Well-structured**: Paper is clearly organized, with problem definition leading to methodology to experiments (R1, R4). Reviewer 4 calls it “very well written.”

### Weaknesses
- **Limited novelty relative to SubgraphX**: The core MCTS framework is adapted from SubgraphX, with the main addition being a “restart” policy in Selection. This is seen as incremental (R1). Reviewer 1 rates contribution “fair.”
- **Counterfactual definition not fully rigorous**: Perturbations change not only the node embedding of interest but also other node embeddings, which conflicts with the idealized illustration in Figure 1(b,c) (R1).
- **Lack of discussion on simple baselines**: The 1hop-2N and 1hop-3N baselines achieve surprisingly high precision on synthetic datasets (e.g., BA-Shapes, Tree-Cycles, Tree-Grid) with no analysis of why. This weakens the argument for UNR-Explainer’s superiority (R3, R4). Multiple reviewers ask for an explanation (R3 Q1, R4 Q2).
- **Insufficient analysis of underperformance**: UNR-Explainer underperforms on precision in several synthetic experiments. More discussion on these cases is needed (R4).
- **Computational cost and scalability**: MCTS is slow compared to gradient-based methods, especially on large graphs. The paper acknowledges this but does not fully explore implications for practical use cases (R2, R3). Questions remain about scaling with graph size, density, and node degrees (R2 Q1). Reviewer 3 notes time complexity analysis is only in appendix.
- **Missing visual illustrations**: The paper lacks clear diagrams of the MCTS exploration process and the perturbation mechanism, making it hard to grasp core mechanics (R2). Small text in Figure 2 (embedding labels) hinders readability (R3).
- **Motivation and challenges not fully articulated**: The challenges specific to generating counterfactual explanations in unsupervised learning, compared to supervised methods (CF-GNNExplainer, RCExplainer, CF2), are not stated (R1). Why MCTS is chosen over gradient-based or causal methods is not justified (R1 Q1). What new challenges UNR-Explainer addresses compared to supervised CF methods is not clarified (R1 Q2).
- **No real-world validation for perturbation strategy**: The claim that adding edges/nodes is risky in real scenarios is not supported by applications or pilot studies (R1). Reviewer 1 asks for examples of real-world scenarios using only edge removal (R1 Q3).
- **Hyperparameter choice of k not fully explained**: The choice k=5 is used without clear justification for when larger or smaller values are appropriate. While a sensitivity study is provided, further discussion is needed given k is central to the importance metric (R4). Reviewer 4 also asks about the impact of k on importance score (R4 Q1).
- **Missing analysis of method sensitivity to perturbation degree**: It is unclear how minor changes in perturbation affect the importance algorithm (R2 Q2).
- **Lack of integration with other models**: No discussion of how DGI’s contrastive approach or GraphSAGE’s inductive learning influence the types of explanations generated, nor how the method would adapt to generative models like GraphGAE or S2GAE (R2 Q3).
- **Minor errors**: Page 9 first line is not left-justified; Table 1 lacks arrow indicators for measures (R1).