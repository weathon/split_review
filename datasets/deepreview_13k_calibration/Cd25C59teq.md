# GraphPINE: Graph importance propagation Neural Network for interpretable drug response prediction

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Explainability is necessary for tasks that require a clear reason for a given result such as finance or biomedical research. Recent explainability methodologies have focused on attention, gradient, and Shapley value methods. These do not handle data with strong associated prior knowledge and fail to constrain explainability results by relationships that may exist between predictive features.

We propose a GraphPINE, a novel graph neural network (GNN) architecture that leverages domain-specific prior knowledge for node importance score initialization. Use cases in biomedicine necessitate generating hypotheses related to specific nodes. Commonly, there is a manual post-prediction step examining literature (i.e., prior knowledge) to better understand features. While node importance can be obtained for gradient and attention-based methods after prediction, these node importances lack complementary prior knowledge; GraphPINE seeks to overcome this limitation. GraphPINE differs from other GNNs with gating methods that utilize an LSTM-like sequential format such that we introduce an importance propagation layer that unifies 1) updates for feature matrix and node importances, jointly and 2) uses GNN-based graph propagation of feature values.  This initialization and updating mechanism allows for more informed feature learning and improved graph representation.

We apply GraphPINE to cancer drug response prediction using pharmacogenomics data (i.e., both drug screening and gene data collected by several assays) for ~5K gene nodes included in a gene-gene input graph with drug-target interaction (DTI) knowledge graph as initial importance. The gene-gene graph and DTIs were taken from literature curated prior knowledge sources and weighted by the literature information. GraphPINE demonstrates competitive performance and achieves a PR-AUC of 0.894 and ROC-AUC of 0.796 across 952 drugs. To highlight the interpretability aspect of our work, we provide the ability to generate sub-graphs of node importances. While our use case is related to biology, our work is generally applicable to tasks where information is separately known about feature relationships. Code: https://anonymous.4open.science/r/GraphPINE-40DE

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript introduces GraphPINE, a Graph Neural Network (GNN) architecture aimed at enhancing interpretable drug response prediction. By leveraging prior biological knowledge through a knowledge graph with weighted edges, GraphPINE generates initial importance scores for nodes. The core innovation of the work is the Importance Propagation (IP) layer, which facilitates the propagation of node importance throughout the GNN, thereby promoting biological interpretability.

### Strengths
1. The manuscript addresses an important challenge in drug response prediction, highlighting the need for interpretable models in biomedical applications.

2. The integration of a knowledge graph to inform initial importance scores is a compelling approach that could enhance the interpretability of GNNs in drug response contexts.

### Weaknesses
1. The methodology lacks novelty, as graph convolutional networks (GCN) and importance gating have been previously employed in similar contexts. The claim of novelty in this paper is undermined by the existence of other interpretable GNN-based methods for drug response prediction. Specifically, the use of a knowledge graph to initialize node importance scores, while intuitive, does not represent a significant departure from existing practices where node features or embeddings are often derived from similar biological knowledge sources. The core mechanism of propagating importance through a GNN, while presented as an 'Importance Propagation' layer, is conceptually similar to attention mechanisms or other forms of weighted message passing already present in numerous GNN architectures.

2. The ablation study is missing, and important baseline models are not included in the comparisons. The results show only marginal improvements over baseline models. For instance, ROC-AUC results show GraphPINE at 0.7955 compared to LightGBM at 0.7901, and PR-AUC results indicate 0.8939 vs 0.8917. These limited improvements weaken the overall impact of the claims. The lack of a thorough ablation study makes it difficult to assess the contribution of each component of GraphPINE. For example, it is unclear how much of the performance gain is attributable to the knowledge graph initialization versus the IP layer itself. Furthermore, the comparison with LightGBM, while a common baseline, does not sufficiently demonstrate the superiority of GraphPINE over other GNN-based methods designed for similar tasks. The reported marginal improvements are not compelling enough to justify the added complexity of the proposed architecture.

3. The authors should provide comprehensive comparative analyses with and without drug-target interaction (DTI) information to demonstrate the importance of DTI. If predictive performance is comparable to models that exclude DTI, this raises questions about the effective utilization of the interaction information. The current evaluation does not isolate the impact of DTI, and it remains unclear whether the inclusion of DTI provides a substantial benefit over simpler models that do not consider this information. A rigorous analysis should include a comparison with models that use the same graph structure but exclude DTI information, or use DTI information in a different way, to isolate the contribution of the proposed approach.

### Questions
see above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present GraphPINE, an interpretable GNN for drug response prediction. This methodology is able to deliver accurate results in terms of drug response prediction and, at the same time, provide interpretable outcomes in terms of important genes in the input graph. The authors properly described their methodology and compared their results with other methods. Finally, they show how it is possible to obtain and visualize interpretations for the predictions obtained.

### Strengths
The main strengths of the paper are the following:

1) The work is original and relevant since it touches on an important aspect of GNNs (interpretability). Instead of relying on external explainers (which can deliver biased results), the authors propose a way to render GNN interpretable by using importance score propagation.

2) The domain of application is of extreme importance and relevance since it could help facilitate the detection of drug response/resistance, speeding up drug development and clinical trial phases.

3) The interpretability results are in line with the knowledge present in the literature.

4) Overall, the work is well-presented and also the Appendix provides useful information.

5) The authors provided an anonymous repository for reproducibility

### Weaknesses
The main weaknesses of the paper are the following:

1) It is not clear to me how the initial importance scores are assigned. The authors say these scores are obtained using the weights of the edges of a knowledge graph. How is this done? My doubt is that if we start from consolidated importance scores, the result's final propagated importance will present a bias since it will be strongly dependent on the initial weights. Specifically, the method relies on co-occurrence counts from PubMed articles, but the process of transforming these counts into edge weights and then node importance scores is not sufficiently detailed. The lack of clarity here makes it difficult to assess the objectivity of the initial importance scores and their potential influence on the final results. It is crucial to understand whether these initial scores are simply reflecting the frequency of co-mentions or if they incorporate any additional weighting or normalization that could introduce bias.

2) It is not clear to me if the authors compared their results against GAT, GT, and GINE. They present three GraphPINE versions based on those architectures, but a direct comparison with them is not provided. I am puzzled since, in the Appendix, they describe the hyperparameter tuning for those models, but no result from them is present in Table 1. This lack of direct comparison makes it difficult to ascertain the true benefit of the proposed GraphPINE architecture. The ablation study should include the performance of the base GNN models (GAT, GT, and GINE) without the importance propagation mechanism to properly evaluate the contribution of the proposed approach.

3) The improvement brought by GraphPINE in terms of evaluation metrics is marginal with respect to other methods. In particular, it would be interesting to see how GAT, GT, and GINE perform when used as standalone techniques. The reported improvements are not substantial enough to justify the added complexity of the proposed method. A more rigorous comparison is needed to demonstrate the practical advantages of GraphPINE over existing GNN architectures, especially when considering the computational overhead of the importance propagation mechanism.

### Questions
My questions are related to the weak points I described. 

1) Can the authors better describe how the initial importance scores are obtained? This should be carefully described in the main paper and not in the Appendix.

2) If one used the initial importance scores to build a ranking of important nodes, would the outcome be different? If yes, then the methodology is effective; if no, probably the resutls are strongly affected by the initial importance scores.

3) Can the authors show how GAT, GT, and GINE perform when used as standalone strategies?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes GraphPINE to handle the problem of drug response prediction. GraphPINE uses a graph neural network incorporating biomedical prior knowledge from various resources. As for the model architecture, GraphPINE utilizes Graph Transformer and GAT to handle features, and designs Importance Propagation Layer to provide understandings for nodes and their relations. In experiments, GraphPINE outperforms other baseline methods and provide interpretable results for drug response prediction examples.

### Strengths
1. This work utilizes different kinds of biomedical information to tackle drug response prediction, including gene-gene network, drug-target interaction and methylation. 
2. GraphPINE introduces Importance Propagation Layer, which is good at processing information from multi sources.

### Weaknesses
1. This work lacks a problem formulation for the problem of drug response prediction, which makes the input and the output of the learning problem unclear. Specifically, it is not clear what the input graph G represents (e.g., is it a single graph representing all cells/patients or multiple graphs for each cell/patient?) and what the node and edge features are. Similarly, the output y is vaguely defined, lacking details on whether it's a continuous value (like IC50) or a discrete label (sensitive/resistant), and how these are obtained from experimental data.
2. The model architecture design is generally lack of novelty. For the feature processing part, Graph Transformer and GAT are existing works widely used. While the Importance Propagation Layer is similar to LSTM/GRU gates, it is not clear how it is different from the existing gated mechanisms in recurrent neural networks. The paper does not provide a clear justification for why this specific design is necessary or advantageous compared to other existing methods for information aggregation in graph neural networks.
3. In the experiment part, all baselines are learning methods proposed several years ago and none of them is specially designed for drug response prediction. This makes the experimental comparison unreasonable, as the drug response prediction methods introduced in related work part are not compared. Furthermore, the evaluation metrics used are not clearly defined, and it is not clear if the reported performance is statistically significant.

### Questions
1. What are the differences between drug response prediction and other drug-related prediction problems (e.g. drug-target interaction prediction and drug-drug interaction prediction)?
2. In section 2.2 “graph neural network in computational biology”, why molecular property prediction methods are not mentioned? GNN is widely used for molecular property prediction problems. 
3. Why the title of section 3.3.2 is “GraphPINE model”? It seems that the title and contents do not match. 
4. In Figure 2, 3, 4, why there are color bars on the right? There are only two types of colors for nodes in the figure.

### Soundness
3

### Presentation
3

### Contribution
2
