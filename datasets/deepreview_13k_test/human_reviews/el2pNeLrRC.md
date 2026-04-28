# ECGN: A CLUSTER-AWARE APPROACH TO GRAPH NEURAL NETWORKS FOR IMBALANCED CLASSIFICATION.

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Classifying nodes in a graph is a common problem.
The ideal classifier must adapt to any imbalances in the class distribution.
It must also use information in the clustering structure of real-world graphs.
Existing Graph Neural Networks (GNNs) have not addressed both problems together.
We propose the Enhanced Cluster-aware Graph Network (\technique), a novel method that addresses these issues by integrating cluster-specific training with synthetic node generation.
Unlike traditional GNNs that apply the same node update process for all nodes, \technique\ learns different aggregations for different clusters.
We also use the clusters to generate new minority-class nodes in a way that helps clarify the inter-class decision boundary.
By combining cluster-aware embeddings with a global integration step, \technique\  enhances the quality of the resulting node embeddings.
Our method works with any underlying GNN and any cluster generation technique.
Experimental results show that \technique\  consistently outperforms its closest competitors by up to $11\%$ on some widely-studied benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces ECGN, a method designed to address class-imbalanced node classification. The approach begins by clustering nodes into groups, then computing node embeddings within each cluster through separate GNN models. Using these embeddings, it applies SMOTE to oversample minority nodes, augmenting the original graph, which is then processed by another GNN model for further training. Extensive experiments on datasets of varying sizes are conducted to evaluate the model, including ablation studies to assess the contribution of each component.

### Strengths
1. The experiments are thorough, covering datasets of various sizes, including a large-scale dataset.
2. The source code is available for review, and the repository is well-organized.

### Weaknesses
1. The paper is poorly organized. It devotes excessive space to related work and includes figures and tables, such as Figure 2, Table 3, and Table 4, that take up significant space without providing much information. Meanwhile, important details are missing from the main paper, particularly about the pre-training step in Proposed Algorithm section, which is crucial as an ablation study references it. However, placing these contents in the appendix forces readers to flip back and forth to follow this paper.

2. I have concerns about the pre-training stage. It appears to involve simple feature aggregation with separate GNNs within each cluster. Are these GNNs trained independently? If so, what is the training objective? If not, why not consider a non-parametric model for feature aggregation instead?

3. The clustering stage raises some concerns. Given the high class imbalance in the graph, minority nodes may end up grouped with a large number of majority nodes within the same cluster, leading to a poor clustering quality. Have the authors considered this possibility?

4. Equations in the paper lack indexing, making them difficult to reference. Additionally, in line 257, the paper states that connectivity measures the connections between minority nodes and nodes in other clusters. However, the equation that follows counts connections between minority nodes and nodes in other classes.

5. Standard deviations are missing from the reported results. This is particularly concerning given that each model is only run four times, which could yield results with high variability.

6. In Table 2, the performance difference between ECGN with and without SMOTE is minimal. This raises questions about the necessity of this component. Is synthesizing minority nodes essential for addressing class imbalance in this context? Again, the absence of standard deviation reporting makes it unclear whether this improvement is statistically significant.

7. In the related work section, the paper critiques previous generative methods, stating, “altering the graph structure introduces complexities, and finding the optimal mixing ratio between node features can be difficult, often leading to noisy results that hurt performance.” However, this work does not address these issues, as its node synthesis method appears to share the same limitations as previous node generative approaches.

### Questions
See Weakness.

### Soundness
2

### Presentation
1

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
This paper proposes an improved framework for building graph neural networks for imbalanced node classification tasks. The end-to-end flow includes the following steps:
1. Cluster-Specific Training: The input graph is partitioned into smaller clusters, and graph neural networks are pre-trained for each cluster to generate node embeddings.
2. Cluster-Aware SMOTE: Synthetic nodes are generated for minority classes, with a focus on nodes located near cluster boundaries. The embeddings from Step 1 are used to identify nearest neighbors, enabling interpolation to create new embeddings for the synthesized nodes.
3. Global Integration: All embeddings from Steps 1 and 2 are used to train a global classifier.

The framework leverages local structural information in Step 1 and global information in Step 3, while Step 2 addresses class imbalance. Experimental results demonstrate substantial improvement over previous state-of-the-art, including GraphSMOTE and Cluster-GCN.

### Strengths
The overall framework is novel and quite reasonable. It combines the strength from both GraphSMOTE and ClusterGCN while introducing innovative improvements on top of the previous SOTA in various aspects, including:
1. Carrying out SMOTE with a cluster aware approach. Synthesizing nodes around the cluster boundary would be more effective for imbalanced classification problems.
2. Using cluster specific GCN instead of a single GCN at the pre-training stage followed by global aggregation at a later stage. This balanced approach captures both local and global information, with trade-offs in compute and storage efficiency.

The proposed ECGN has been compared to a wide range of methods, and the experimental results consistently outperform the references across all evaluated datasets, demonstrating its effectiveness.

### Weaknesses
Presentation:
1. The network architecture for cluster specific pretraining and global aggregation in Figure 1 are illustrative at high level, lacking details of network architecture. It didn’t clarify whether local and global network structures are identical. Additionally, the Global aggregation is only described as “H′ ← convolution of G′ using H′ as node features.” in Algorithm 1, without clear correspondence from Figure 1.
2. The methods in experiment evaluation could be more clearly linked to references or description, specifically “Cluster-Aware SMOTE only” is confusing; see Q1 in the Question section.
3. No information on computational cost has been provided, so it is unclear what trade-offs were made to achieve accuracy improvements.

Reference:
The reference to (Chiang et al., 2019) should include the conference information (KDD ’19) rather than only an arXiv link. Additionally, (Zhao et al., 2021b) is not the correct reference for GraphSMOTE, and the information provided in the reference is also incorrect.

Experiments:
More detailed experiments are expected to clarify the value of Cluster-Aware SMOTE; see Q2 in the Question section.

### Questions
Q1:
a) What are the specifics of “Cluster-Aware SMOTE only” in the benchmark results, i.e. Table 2? Section 3.2 described “Cluster-Aware SMOTE” to synthesize nodes, but there is no mention of building a classifier. 
b) What’s the difference between “Cluster-Aware SMOTE only” and “ECGN with SMOTE”, and 
c) What’s the difference between “Cluster-Aware SMOTE only” and GraphSMOTE?
d) Why is “Cluster-Aware SMOTE only” showing inferior performance than GraphSMOTE if the cluster-aware SMOTE is supposed to be more effective than non-cluster-aware SMOTE?

Q2:
Cluster aware node synthesis in 3.2, especially synthesizing nodes around the cluster boundary seems to be an important and novel step compared to GraphSMOTE. How effective is this approach, what if it reverts to a baseline approach? Is there any experiment validating the contribution of this step?

Q3:
Related to Q2, the embeddings for the synthesized nodes are generated from their neighborhood. Neighborhood nodes could come from different clusters, but all embeddings were pre-trained within each cluster. Was any inter-cluster graph structure lost in this process?

### Soundness
3

### Presentation
2

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
This paper introduces ECGN, a framework that enhances Graph Neural Networks (GNNs) by incorporating cluster-specific training and synthetic node generation to address class imbalance in graph data, applicable to node classification tasks. ECGN employs a novel technique called Cluster-Aware SMOTE, which generates synthetic minority-class nodes, improving the decision boundary between classes and enhancing overall model performance. By combining cluster-aware updates with a global integration step, ECGN captures both local cluster-specific information and global graph structures. The model was evaluated on five benchmark datasets, including Citeseer and Reddit, and consistently outperformed existing state-of-the-art methods, with up to an 11% improvement in F1-score on imbalanced node classification tasks.

### Strengths
1. This paper proposes a novel framework for addressing the problem of label imbalance in graph data.

2. The method demonstrates strong performance on specific benchmark datasets.

3. The code is publicly available, which is beneficial for the community in terms of reproducibility and further research.

### Weaknesses
1. The summary of related work is incomplete. See question 1.

2. The description of the methodology is not clear enough. See questions 2, 3, and 4.

3. The experiments are not comprehensive enough. See questions 5 and 6.

### Questions
1. The summary of related work is incomplete. Considering that the main contribution of this paper lies in addressing the graph class imbalance problem, the authors should discuss recent papers that tackle this issue, such as [1][2][3][4][5][6], to strengthen the paper's motivation and contribution.

2. The methodology section lacks clarity. The most confusing aspect is the distinction between class and cluster. Specifically, when clustering algorithms like LSH group nodes with similar features into a cluster, is there any correlation between the clusters and the node labels (classes)? The authors should provide a specific example or diagram illustrating how classes and clusters relate in their approach.

3. Continuing from question 2: To what extent does the quality of the clustering algorithm affect the final results? If the clustering algorithm is optimal and clusters nodes perfectly according to their labels, would that improve prediction performance? How should we interpret the statement on line 200, "The choice of clustering algorithm is orthogonal to our method"? Does this imply that the clustering results have no impact on the final outcome of the method? It is recommended that the authors add an ablation study or sensitivity analysis to quantify how different clustering algorithms or their qualities affect the final results.

4.  Continuing from question 2: On line 257, the paper states, "For each minority node v in class Y_m, we compute its connectivity to nodes in other clusters." This statement blurs the distinction between class and cluster. How should we understand the relationship between class and cluster in this context?

5.  The experiments are insufficient. On one hand, the authors mention that the baselines are somewhat outdated. It is recommended to compare against more recent methods, such as [1][2][3][4][5][6]. On the other hand, even when comparing with the baselines mentioned in the paper, the performance improvements across several datasets are marginal, with numerical increases of only 0.02 to 0.03, representing less than a 5% improvement. It is suggested that the authors conduct comparisons with more updated work; this way, even modest improvements could be considered acceptable in the context of advancing the state of the art.

6.  Continuing from question 5: The authors are encouraged to provide training time and training parameters such as training time per epoch, total training time, and memory usage for both ECGN and baseline methods in the paper or appendix. Given that the framework appears to require training multiple GNNs, it is important to clarify whether the performance improvements come at the cost of significantly higher computational overhead.

References:  
[1]	Park, Joonhyung, Jaeyun Song, and Eunho Yang. "Graphens: Neighbor-aware ego network synthesis for class-imbalanced node classification." International conference on learning representations. 2021.  
[2]	Qian, Yiyue, et al. "Co-modality graph contrastive learning for imbalanced node classification." Advances in Neural Information Processing Systems 35 (2022): 15862-15874.  
[3]	Wang, Yu, Charu Aggarwal, and Tyler Derr. "Distance-wise Prototypical Graph Neural Network for Imbalanced Node Classification." Proceedings of the 17th International Workshop on Mining and Learning with Graphs (MLG). 2022.  
[4]	Song, Jaeyun, Joonhyung Park, and Eunho Yang. "TAM: topology-aware margin loss for class-imbalanced node classification." International Conference on Machine Learning. PMLR, 2022.  
[5]	Zeng, Liang, et al. "Imgcl: Revisiting graph contrastive learning on imbalanced node classification." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 9. 2023.  
[6]	Zhou, Mengting, and Zhiguo Gong. "GraphSR: a data augmentation algorithm for imbalanced node classification." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 4. 2023.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ECGN, a new method in Graph Neural Networks designed to improve node classification in class-imbalanced datasets by leveraging cluster-specific embeddings and synthetic node generation. ECGN operates by first pre-training subclusters to capture local graph structures, then generating synthetic nodes in boundary areas of minority clusters to enhance classification for underrepresented classes, and finally integrating these local representations into a global structure. This approach outperforms existing models, achieving up to an 11% improvement on benchmark datasets, highlighting its ability to maintain both global and local graph consistency for balanced, high-accuracy node classification.

### Strengths
- The paper is well-written, clear, and easy to follow. 
- Extensive experiments are conducted to validate ECGN's performance, and the inclusion of the code enhances reproducibility and supports the credibility of results. 
- ECGN is highly adaptable, functioning as a versatile enhancement for any GNN backbone, which underscores its potential generalizability across various GNN architectures.

### Weaknesses
- Motivation Clarity: Imbalanced classification and node clustering on graphs are two orthogonal problems. The motivation behind combining these two aspects is not sufficiently clear, and further elaboration is necessary to explain why clustering is beneficial for addressing class imbalance.
- Related Work: The related work lacks coverage of recent advancements in class-imbalanced node classification. Key methods such as "GraphENS: Neighbor-Aware Ego Network Synthesis for Class-Imbalanced Node Classification" (ICLR 2022), "TAM: Topology-Aware Margin Loss for Class-Imbalanced Node Classification" (ICML 2022), "GraphSHA: Synthesizing Harder Samples for Class-Imbalanced Node Classification" (KDD 2023), and "Class-Imbalanced Graph Learning without Class Rebalancing" (ICML 2024) should be discussed and ideally included in the empirical comparisons.
- Inappropriate claims: The statement in line 54, “uniform updates can make the GNN overlook rich local structures,” is Inappropriate. Through simple uniform aggregation, message passing in GNNs can also capture local structures. 
- Evaluation: The F1-score improvements shown in Table 2 are modest across all datasets. Incorporating additional evaluation metrics for imbalanced learning, such as balanced accuracy would provide a more nuanced view of the model’s performance.

### Questions
Please refer to weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2
