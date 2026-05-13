# FedGT: Federated Node Classification with Scalable Graph Transformer

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
Graphs are widely used to model relational data. As graphs are getting larger and larger in real-world scenarios, there is a trend to store and compute subgraphs in multiple local systems. For example, recently proposed \emph{subgraph federated learning} methods train Graph Neural Networks (GNNs) distributively on local subgraphs and aggregate GNN parameters with a central server. However, existing methods have the following limitations: (1) The links between local subgraphs are missing in subgraph federated learning. This could severely damage the performance of GNNs that follow message-passing paradigms to update node/edge features.
(2) Most existing methods overlook the subgraph heterogeneity issue, brought by subgraphs being from different parts of the whole graph.
To address the aforementioned challenges, we propose a scalable \textbf{Fed}erated \textbf{G}raph \textbf{T}ransformer (\textbf{FedGT}) in the paper. 
Firstly, we design a hybrid attention scheme to reduce the complexity of the Graph Transformer to linear while ensuring a global receptive field with theoretical bounds.
Specifically, each node attends to the sampled local neighbors and a set of curated global nodes to learn both local and global information and be robust to missing links. The global nodes are dynamically updated during training with an online clustering algorithm to capture the data distribution of the corresponding local subgraph. Secondly, FedGT computes clients' similarity based on the aligned global nodes with optimal transport. The similarity is then used to perform weighted averaging for personalized aggregation, which well addresses the data heterogeneity problem. %Moreover, local differential privacy is applied to further protect the privacy of clients. 
Finally, extensive experimental results on 6 datasets and 2 subgraph settings demonstrate the superiority of FedGT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose to use Graph Transformer and optimal-transport-based personalized aggregation to alleviate the fundamental problems in the subgraph federated learning algorithm such as missing links and subgraph heterogeneity.

### Strengths
(1) Leverages graph transformer architecture within subgraph FL for the first time in the federated graph learning literature.

(2) The algorithm is compatible with local DP.

(3) Experimentally shows that Transformers are useful for subgraph federated learning. 

(4) Theoretical analysis of global attention being able to capture and approximate information in the whole subgraph is provided.

### Weaknesses
(1) How Graph Transformer deals with the missing links is unclear. The explanation that global attention is robust to missing links is not sufficient. It is necessary to elaborate on the specific mechanisms within the transformer architecture that contribute to this robustness in the context of subgraph federated learning. For example, how does the attention mechanism handle the absence of expected connections, and how does this differ from message-passing GNNs which are known to be sensitive to missing links?

(2) The assumption that nodes are equally distributed to the global nodes seems unrealistic due to graph partitioning. While the authors mention that the global nodes are updated with an online clustering algorithm, it is not clear how this clustering is performed in a distributed manner and what guarantees exist for balanced assignment given the heterogeneous nature of subgraphs. The potential for skewed distributions of nodes to global nodes could lead to biased global representations and impact performance.

(3) Theorem is not rigorous as it is a known fact that more nodes less error [1]. The theorem should provide a more precise bound on the approximation error, taking into account the specific properties of the graph transformer and the personalized aggregation method. Simply stating that more nodes lead to less error is not a sufficient contribution.

(4) Local LDP does not guarantee privacy for sensitive node features, edges, or neighborhoods on
distributed graphs [2,3]. Using LDP does not reflect an actual privacy guarantee for this case. The application of LDP to model parameters and global node representations, while common, does not address the inherent privacy risks associated with graph structure and node attributes in a distributed setting. The paper should acknowledge the limitations of this approach and discuss potential vulnerabilities.

### Questions
(1) Could you please compare FedGT with FedDEP [1]? 



[1] Zhang, Ke, et al. "Deep Efficient Private Neighbor Generation for Subgraph Federated Learning."

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a scalable Federated Graph Transformer (FedGT) for subgraph federated learning, which addresses the challenges of missing links between subgraphs and subgraph heterogeneity. It uses a hybrid attention scheme to reduce complexity while ensuring a global receptive field and computes clients’ similarity for personalized aggregation.

### Strengths
1.	The paper is easy to read, and generally well-written.
2.	The idea of using the Graph Transformer to address the issue of missing links across clients is well-motivated.

### Weaknesses
1.	How to aggregate global nodes is not clearly illustrated. On page 6, the authors state, “the global nodes are first aligned with optimal transport and then averaged similar to Equation 8”. However, it is unclear which optimal transport method is applied and how the similarity between global nodes from different clients is calculated. The authors should clarify whether the normalized similarity α_ij used for model parameters is also employed for global nodes or if a different similarity calculation is used. Besides, in Algorithm 3 lines 11 and 13, the aligning process for the global nodes seems to be performed twice, which needs a clearer explanation.

2.	Since the weighted averaging of local models, i.e., Equation (8), is the same in [1], the authors should provide a discussion or experiment to explain why their similarity calculation is superior to that in [1]. Specifically, the authors should elaborate on how the global node-based similarity captures client relatedness compared to the functional similarity used in [1], and whether this difference leads to improved performance or robustness.

3.	To show the convergence rate, Figure 5 and Figure 6 did not contain FED-PUB, which is the runner-up baseline in most cases. This omission makes it difficult to assess the relative convergence speed of the proposed method compared to a strong competitor.

4.	In the ablation study, the authors only conduct experiments on w/o global attention and w/o personalized aggregation. Results of w/o the complete Graph Transformer (i.e., without local attention) should also be provided. This is crucial to isolate the contribution of the Graph Transformer component itself, as opposed to just the global attention or personalized aggregation mechanisms.

### Questions
1.	The authors opt for a consistent number of global nodes n_g across all clients. However, how does the methodology account for scenarios in which clients have a varying number of nodes, with some having significantly more and others noticeably fewer? Is there a suggested approach for determining varying n_g values that are customized to each client’s node count?

2.	In the typical federated learning framework, the number of training samples is considered when aggregating the model parameters. However, Equation (8) only uses the normalized similarity for the weighted aggregation. Why can we ignore the number of training samples here? Or do we assume the number of training samples is equivalent across clients?

3.	The Hungarian algorithm only finds a bijective mapping while optimal transport can be generalized to many-to-many cases, could the authors explain the reason for making a one-to-one alignment of the global nodes?

4.	Since the global nodes are dynamically updated during the training, and the representations of the nodes are not stable at the beginning of the training, would this impact the effectiveness of similarity calculation based on the global nodes?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a scalable Federated Graph Transformer
(FedGT) to address the data heterogeneity and missing link challenges. In contrast to GNNs that follow message-passing schemes and focus on local neighborhoods, Graph Transformer has a global receptive field to learn long-range dependencies and is, therefore, more robust to missing links. Moreover, a novel personalized aggregation scheme is proposed. Extensive experiments show the advantages of FedGT over baselines in 6 datasets and 2 subgraph settings.

### Strengths
1.The paper is well-written and organized. The details of the models are described clearly and are convincing.
2.The limitations of applying GNNs for subgraph federated learning are clearly illustrated in Figure 1 and Figure 4 in appendix. The motivation for leveraging graph transformers is easy to understand.
3.The authors proposed a series of effective modules to tackle the challenges, including scalable graph transformers, personalized aggregation, and global nodes. The contribution is significant enough.
4.FedGT is compared with a series of SOTA baselines, including personalized FL methods, federated graph learning methods, and adapted graph transformers. Extensive experiments on 6 datasets and 2 subgraph settings demonstrate
that FedGT can achieve state-of-the-art performance.

### Weaknesses
1.The authors are suggested to clearly discuss the case studies in the main paper.
2.Leveraging local differential privacy mechanisms to protect privacy in FL is not new.
3.Please provide more explanations of the assumptions in Theorem 1.

### Questions
1.Can the authors introduce more about the roles of global nodes in FedGT?
2.Is FedGT applicable to other subgraph settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
