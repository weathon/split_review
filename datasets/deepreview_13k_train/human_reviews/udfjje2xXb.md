# Kolmogorov–Arnold Graph Neural Networks

- Decision: Reject
- Scores: 5, 3, 3, 3, 3

## Abstract
Graph neural networks (GNNs) excel in learning from network-like data but often
lack interpretability, making their application challenging in domains requiring
transparent decision-making. We propose the Graph Kolmogorov–Arnold Network
(GKAN), a novel GNN model leveraging spline-based activation functions on edges
to enhance both accuracy and interpretability. Our experiments on five benchmark
datasets
demonstrate that GKAN outperforms state-of-the-art GNN models in node
classification, link prediction, and graph classification tasks. In addition to
the improved accuracy, GKAN's design inherently provides clear insights into the
model’s decision-making process, eliminating the need for post-hoc
explainability techniques. This paper discusses the methodology, performance,
and interpretability of GKAN, highlighting its potential for applications in
domains where interpretability is crucial.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the Kolmogorov-Arnold Network for Graphs (KANG), a new Graph Neural Network (GNN) model that enhances interpretability and accuracy in tasks like node classification, link prediction, and graph classification. Utilizing spline-based activation functions on edges, KANG not only improves performance on benchmark datasets but also allows for better insight into decision-making processes, eliminating the need for external explainability techniques. This approach is especially beneficial in domains where understanding model decisions is crucial.

### Strengths
originality: medium
quality: medium
clarity: medium
significance: medium

### Weaknesses
1. It's better to split the second paragraph in the first section for readability.

2. The paper borrows too much content from the original KAN paper and makes incremental modification.

3. In section 2.2.2, where is $m_j^{(l)}$ in the following equations? It seems that this notation is defined but not used. Check out the consistency of the notations.

### Questions
1. "This kind of neural network has an activation function on the edges instead of nodes" What is the edges and nodes here? Are they the same as the edges and nodes in graph?

2. "KANG employs learnable spline-based activation functions on the edges of the graph" Is this similar to graph attention network or graph transformer? What is the difference and what is your advantage?

3. How does KANG perform on heterophilic datasets, especially on those challenging datasets identified in [1]? And how does KANG compare with some SOTA models instead of the baseline models, e.g. [2,3].

4. How does KANG compare with other GNN interpretability methods, e.g. [4]?




[1] The heterophilic graph learning handbook: Benchmarks, models, theoretical analysis, applications and challenges. arXiv preprint arXiv:2407.09618. 2024 Jul 12.

[2] Revisiting heterophily for graph neural networks. Advances in neural information processing systems. 2022 Dec 6;35:1362-75.

[3] Simplifying approach to node classification in graph neural networks[J]. Journal of Computational Science, 2022, 62: 101695.

[4] Miao S, Liu M, Li P. Interpretable and generalizable graph learning via stochastic attention mechanism. InInternational Conference on Machine Learning 2022 Jun 28 (pp. 15524-15543). PMLR.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces Kolmogorov-Arnold Networks (KANs) for enhancing graph neural networks. The core idea is to apply KANs to the aggregation process, replacing linear transformations with KANs.

### Strengths
1. Applying KANs to GNNs is intriguing, and the writing is clear. The core idea of the paper is easy to grasp.

2. The experimental results demonstrate the superior performance of KANs.

### Weaknesses
1. I don't understand why a widely used benchmark (https://paperswithcode.com/sota/node-classification-on-cora-with-public-split) was not employed for evaluation.

2. The idea lacks novelty.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel graph neural network (GNN) model KANG, built on the recently emerged Kolmogorov-Arnold network (KAN). KANG has a KAN-based convolution layer for the propagation and aggregation of messages between nodes, and a KAN-based linear layer to perform a linear transformation on the aggregated node features. The main advantage of KANG is its inherent interpretability (thanks to KAN), making it different from existing post-hoc GNN explainers. For this purpose, KANG computes feature influence (leveraging interaction of the gradients and the spline weights at each KAN hidden layer) and edge importance (combing spline weights and activations of the two node features), and use both of them to interpret the outcomes of KANG. Through extensive experiments on five benchmark datasets, KANG is demonstrated to outperform SOTA GNN models in node classification, link prediction, and graph classification tasks. In particular, feature influence of KANG is analysed on the CORA dataset, and edge importance is also shown to be consistent with the explainability provided by GNNexplainer using the same dataset.

### Strengths
This is a timely paper to introduce KAN for graph representation learning, with a focus on increasing interpretability of existing GNN models. This makes it different from other papers in integrating KAN and GNNs (see a few examples in the second last paragraph of Section 1). KANG utilises information flow across the graph and different KAN layers to develop two new notions, feature influence and edge importance, for its interpretability. I appreciate their effort to use insightful information from KAN to enhance interpretability. The evaluation in the paper shows that KANG has strong performance in both accuracy and interpretability for node classification, link prediction, and graph classification tasks. Most parts of the paper are clearly written, and some suggestions on how to further improve the paper can be found in the next review section.

### Weaknesses
Overall, I like the idea of KANG, but I also notice the following weaknesses.

1. Presentation of the paper can be still improved. I give a few examples.

1.1 Section 2.2: Figure 1 can be improved to better illustrate the main idea of KANG. I cannot fully understand why node x6 is connected to the two dots in the part of KANG convolution.  

1.2 Section 2.2.2: ${\bf m}_j^{(l)}$ is defined, but not used in the following formulation. Should it be $x_j^{(l)}$? The notion $N(i)$ is used but not defined. If it is the set of direct neighbours of node $i$, the aggregation function at the KANG convolution layer does not take node $i$'s own feature into account. 

1.3 Section 2.3.3: I don't fully understand the weights ${\bf W}^{(l)}$ and how to compute mean(${\bf W}^{(l)} \cdot S_{mean}^{(l)}$).

1.4 When reading the paper, I found a few typos: "is it possible", "at layer". 

2. I believe the main contribution of KANG is about interpretability, but the evaluation of KANG's interpretability in this paper is insufficient.

2.1 The evaluation of feature influence and edge importance is only demonstrated on the CORA dataset. 

2.2. KANG is only compared with GNNExplainer. 

3.3 The paper claims that KANG interpretability is consistent with the explainability provided by GNNExplainer. Somehow, I am not fully convinced by this statement. For example, in Figure 2, node 2175 in Figure 2(a) is almost as important as node 2176, but in Figure 2(b), it has a much smaller importance than node 2176. Figure 9 in the Appendix has similar problems: node importances (values and ranks) are quite different for KANG's direct interpretation and GNNExplainer's explanation.

### Questions
1. I would encourage the authors to perform a comprehensive evaluation of KANG's interpretability, considering datasets used by existing post-hoc GNN explanation methods, and more baselines such as PGExplainer and EdgeSHAPer.

2. It is interesting to see that KANG outperforms SOTA GNN models (GCN, GAT, GraphSAGE, GIN) in node classification, link prediction, and graph classification tasks. Can you provide more information about the models, such as hidden dimension, the total number of parameters?

3. In general KAN networks are difficult to train. Appendix A.4 shows that KANG scales very well. This is a bit surprising. Can you give more explanation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces KANG, a Graph Neural Network (GNN) model that incorporates Kolmogorov–Arnold Network Layers into the message-passing framework typical of GNNs. In KANG, messages from node $j$ are computed using spline-based activation functions in each layer. The paper claims that KANG 1) outperforms state-of-the-art GNN models on standard graph tasks (Cora, PubMed, Citeseer, MUTAG, and PROTEINS), and 2) provides interpretable results with negligible computational overhead.

### Strengths
1) The main strength is the focus on the explainability of the proposed Network. KANs are known to be, by construction, more interpretable than standard Neural Networks [1]. Extending this to both feature and edge influence with virtually no cost is interesting and well-explained.

2) The authors decided to include brief discussion of other KAN-based GNNs at the beginning of the paper even if they are new and still non-peer-reviewed. This paragraph provides helpful context. 

3) The paper is clear and provides the code for reproducibility.

### Weaknesses
## Main Weaknesses
---

Having tested and re-run part of the provided code, I have several concerns regarding the empirical evaluation and some significant errors in the code:

1) I ran `comparison.py` to reproduce the Link prediction results for all models (GCN, GATv2, GraphSAGE, GIN, KANG) on the three datasets (Cora, PubMed and CiteSeer). My results differ significantly from those in Table 1. Here are the results I obtained:

| Dataset  | GCN        | GAT        | SAGE       | GIN        | KANG       |
|----------|------------|------------|------------|------------|------------|
| Cora     | 89.5 ± 0.7 | **90.5 ± 0.5** | 85.4 ± 2.4 | 80.8 ± 8.5 | 87.9 ± 0.6 |
| PubMed   | **94.2 ± 0.4** | 90.0 ± 0.2 | 86.4 ± 1.1 | 89.3 ± 0.5 | 85.2 ± 0.3 |
| CiteSeer | 85.3 ± 3.0 | **86.8 ± 2.6** | 82.5 ± 2.8 | 84.2 ± 1.0 | 85.9 ± 0.5 |

These results seem to contradict one of the two main claims of the paper:
"Our experiments [...] demonstrate that KANG outperforms state-of-the-art GNN models in node classification, link prediction, and graph classification tasks." (lines 13-15). The reported standard deviations also suggest potential convergence issues, which should be addressed by using more seeds (>= 30) and ensuring all runs converge. The discrepancy in results raises concerns about the robustness of the reported performance.

2) In the scalability experiment (lines 357–367), the number of parameters is fixed across networks. This comparison is not fair, as models like GCN tend to require fewer parameters to obtain optimal performances and thus may scale more efficiently. The comparison should be made at fixed performance levels. Furthermore, the claim that KANG only "slightly" increases computational cost (line 363) is not supported by my experiments. On my GPU (NVIDIA RTX A5000), KANG's training time was approximately 10 times slower than GCN for Cora, PubMed, and CiteSeer. This significant difference in training time needs to be addressed and accurately reported.

3) For node classification, models are validated on the test set and tested on the validation set. This is a critical error that makes it impossible to compare results with existing literature, where models like GCN and GATv1 might outperform KANG on tasks for Cora and CiteSeer [2,3]. This incorrect validation procedure invalidates the node classification results.

4) GAT models typically perform better with additional attention heads [3]. The hyperparameter for attention heads should be tuned (e.g., in the set [2, 4, 8]). The current setting of a single attention head is likely suboptimal and limits the performance of the GAT baseline.

5) In the link predictor experiment, average training time per epoch is calculated as ((end_time - start_time) / n_epochs). This calculation is invalid if early stopping is triggered, as the number of epochs will vary between runs. This incorrect calculation undermines the reported training time analysis.

## Minor Weaknesses
---

1) KANG introduces three additional hyperparameters (spline grid size, spline degree, and aggregation function). For the hyperparameter search space you considered, this addition makes the hyperparameter search 126 times slower. This fact should be highlighted. The computational cost of hyperparameter tuning should be explicitly stated.

2) The statement "For each run, to achieve unbiased outcomes, we randomly split the datasets, utilizing 80% for training, 10% for validation, and 10% for testing" (lines 355–356) is not accurate for all experiments. The data splitting procedure should be consistent across all experiments, and any deviations should be clearly stated.

3) The `node_classification.py` script is located only in the `del` folder and throws an error when run both inside and outside the folder. I did not investigate why. The code organization needs to be improved to ensure that all scripts are accessible and executable.

4) There are few typos in the paper:
- In Equation (2) `b()` is missing
- In lines 225-226 change "incluence" with "influence"

### Questions
1) What is the synthetic dataset used in the scalability study of Appendix A.4? I didn't see it explained neither in the main paper nor in the appendix. Its description should be included in the paper.

2) Inspired by GNNs, you experimented with `average()`, `sum()` and  `max()` aggregation functions for KANG. Since the Kolmogorov–Arnold representation theorem holds for the `sum()`, the other two aggregation functions do not have the same theoretical guarantees. However, in Table 4, Appendix A2 you actually show that `mean()` is favoured. Is this statistically significant, or is it not an important hyperparameter to tune? Did you investigate what happens to the splines when different aggregations are used? Do you think this result extends to deeper networks and/or traditional KAN?

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose a novel graph neural network (GNN) model named KANG, which combines Kolmogorov–Arnold Networks (KANs) with GNNs and employs spline-based activation functions to enhance the accuracy and interpretability of GNNs. Different from existing methods, KANG can inherently provide interpretability, which is suitable for transparent decision-making. Experiments are conducted on several benchmark datasets, which demonstrates that KANG can outperform existing GNN methods in various graph tasks, such as node classification, link prediction, and graph classification.

### Strengths
- Different from traditional GNN methods, KANG can inherently provide interpretability for GNNs, which is particularly valuable for transparency. Additionally, KANG integrates interpretability directly into its architecture, which removes the need for additional post-hoc explainability tools.
- Moreover, the spline-based activation functions in KANG provide increased flexibility in modeling complex relationships in graph data, which helps capture nonlinear interactions more effectively and contributes to inprove the performance and interpretability of KANG.

### Weaknesses
 - The writing of this paper could be improved. For instance, the introduction is overly long and lacks clarity, which makes it difficult for readers to understand the key motivations and contributions of the work. 
- The motivation of this paper is unclear, which is challenging to understand the specific limitations of existing GNN methods. KANG emphasizes enhanced interpretability and performance, but it does not adequately highlight the practical issues or real-world scenarios.
- The novelty of KANG is limited, as it simply combines Kolmogorov–Arnold Networks (KANs) with GNNs. Although this integration enhances interpretability and performance of GNNs, it does not introduce fundamentally new mechanisms or theoretical advancements beyond those already present in KANs and existing GNN architectures.
- The experimental results are not convincing, and the baseline methods are not strong enough. Although the authors compare KANG with widely used GNN methods like GCN, GAT, GIN, and GraphSAGE, these methods are neither the latest nor the most competitive, which undermines the significance of the reported performance.

### Questions
- The authors should provide clearer motivations to explain why combining KAN and GNNs is necessary.
- The time and space complexity of KANG should also be provided in method part.
- More recent GNN baseline methods should be introduced in the experimental part for fair comparisons, such as rLap [1], UGNN [2], and PANDA [3] for graph classification, as well as GRLC [4], SEK [5] and UGT [6] for node classification.

[1] Kothapalli V. Randomized schur complement views for graph contrastive learning[C] International Conference on Machine Learning. PMLR, 2023: 17580-17614.

[2] Luo X, Zhao Y, Qin Y, et al. Towards semi-supervised universal graph classification[J]. IEEE Transactions on Knowledge and Data Engineering, 2023, 36(1): 416-428.

[3] Choi J, Park S, Wi H, et al. PANDA: Expanded Width-Aware Message Passing Beyond Rewiring[C] Forty-first International Conference on Machine Learning.

[4] Peng L, Mo Y, Xu J, et al. GRLC: Graph representation learning with constraints[J]. IEEE transactions on neural networks and learning systems, 2023.

[5] Yao T, Wang Y, Zhang K, et al. Improving the expressiveness of k-hop message-passing gnns by injecting contextualized substructure information[C] Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023: 3070-3081.

[6] Lee O J. Transitivity-Preserving Graph Representation Learning for Bridging Local Connectivity and Role-Based Similarity[C] Proceedings of the AAAI Conference on Artificial Intelligence. 2024, 38(11): 12456-12465.

### Soundness
2

### Presentation
2

### Contribution
2
