# Graph Lottery Ticket Automated

- Decision: Accept
- Scores: 5, 6, 6

## Abstract
Graph Neural Networks (GNNs) have emerged as the leading deep learning models for graph-based representation learning. However, the training and inference of  GNNs on large graphs remain resource-intensive, impeding their utility in real-world scenarios and curtailing their applicability in deeper and more sophisticated GNN architectures. To address this issue, the Graph Lottery Ticket (GLT) hypothesis assumes that GNN with random initialization harbors a pair of core subgraph and sparse subnetwork, which can yield comparable performance and higher efficiency to that of the original dense network and complete graph. Despite that GLT offers a new paradigm for GNN training and inference, existing GLT algorithms heavily rely on trial-and-error pruning rate tuning and scheduling, and adhere to an irreversible pruning paradigm that lacks elasticity. Worse still, current methods suffer scalability issues when applied to deep GNNs, as they maintain the same topology structure across all layers. These challenges hinder the integration of GLT into deeper and larger-scale GNN contexts.  To bridge this critical gap, this paper introduces an $\textbf{A}$daptive, $\textbf{D}$ynamic, and $\textbf{A}$utomated framework for identifying $\textbf{G}$raph $\textbf{L}$ottery $\textbf{T}$ickets ($\textbf{AdaGLT}$). Our proposed method derives its key advantages and addresses the above limitations through the following three aspects: 1) tailoring layer-adaptive sparse structures for various datasets and GNNs, thus endowing it with the capability to facilitate deeper GNNs; 2) integrating the pruning and training processes, thereby achieving a dynamic workflow encompassing both pruning and restoration; 3) automatically capturing graph lottery tickets across diverse sparsity levels, obviating the necessity for extensive pruning parameter tuning. More importantly, we rigorously provide theoretical proofs to guarantee $\textbf{AdaGLT}$  to mitigate over-smoothing issues and obtain improved sparse structures in deep GNN scenarios. Extensive experiments demonstrate that $\textbf{AdaGLT}$ outperforms state-of-the-art competitors across multiple graph datasets of various scales and types, particularly in scenarios involving deep GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Adaptive, Dynamic, and Automated framework for identifying Graph Lottery Tickets to overcome the integration of
GLT into deeper and larger-scale GNN contexts. It attempts tailoring layer-adaptive sparse structures for various datasets and GNNs, thus endowing it with the capability to facilitate deeper GNNs; integrating the pruning and training processes, thereby achieving a dynamic workflow encompassing both pruning and restoration; and automatically capturing graph lottery tickets across diverse sparsity levels, obviating the necessity for extensive pruning parameter tuning.

### Strengths
1. The paper is well written with motivation explicitly explained. The evolution of both edges and weights might dynamically during the training process as well as the flexibility of prune ratio are important missing links that are explored.
2. The introduction of an edge explainer into GNN pruning that ensures interpretability during the pruning process while reducing unimportant edges, is a good way to mitigate the quadratic increase in parameters.
3. Appendix is rich. I will recommend the authors move some large-scale experiments on OGBN-Arxiv and Products to be moved to main draft.

### Weaknesses
Although the introduced components like join sparsification, edge explainer etc make sense, one major concern I have is how these individual components affect the performance of AdaGLT. I appreciate the authors for their extensive experiments, but the role/importance of individual modules is not well explained. How does removing some components affect the performance. Another question, no significant performance benefit is observed for low sparsity ratios eg 30-50%. Any explanation of why it is effective only in high sparsity ratios will improve the manuscripts. I am open to increasing my score after the rebuttal discussion.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed the AdaGLT to obtain the graph lottery ticket to sparsify both the trainable weights and the graph structure together. The AdaGLT learns different masks for different layers of graph and weights, providing higher freedom of the sparsification. To save the memory for the training mask, the edge explainer was also introduced. Through extensive evaluation, the proposed framework achieves satisfactory results.

### Strengths
1. The evaluation is sufficient to support the claims.
2. The paper presentation is clear enough to get the main ideas.
3. AdaGLT can work on deep GNNs and large-scale datasets.

### Weaknesses
1. Section 3.1 is the direct application of Liu et al. 2022, as stated in the paper. The edge explainer is also available. So, the main contribution seems incremental.
2. The assumption of Theorem 1 may not be true for $G^{(l)}$ in most cases, since $G^{(l)}$ should be different due to the layer-adaptive pruning.
3. The algorithm does not include the "Dynamic Pruning and Restoration" paragraph. And the statement of equation 10 is unclear to me. What does the restoration refer to?

### Questions
1. What does the "irreversible fashion" refer to? The baseline UGS updates the mask only, and both the original A and weights are stored, so it should be considered as "reversible"?
2. The authors stated that "Existing GLT methods .... and their lack of flexibility stems from the necessity of hyperparameter tuning". Can the author explain more in detail? The baseline UGS also has the trainable mask, which can be considered as the other version of the trainable threshold.
3. Could the author describe how to get the equation 10?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper argues that existing graph lottery ticket algorithms like UGS heavily rely on trial-and-error pruning rate tuning and scheduling, and suffer from stability issues when extended to deeper GCNs. Those limitations call for an adaptive framework to automatically identify the pruning hyper-parameters that improve the scalability of GCNs. To this end, the authors propose a framework called AdaGLT, adaptive graph lottery tickets, to overcome such limitations.
Extensive experiments validate the effectiveness of the proposed AdaGLT as compared to previous ad-hoc UGS.

### Strengths
1. The paper is well-written and organized. As compared to previous UGS, the proposed AdaGLT jointly sparsifies both graphs and GNN weights and adopts an adaptive layer sparsification process. In addition, it offers the practitioner the chance to adopt automatic pruning and dynamic restoration for extracting the graph lottery tickets.

2. The effective combination of automation, layer adaptivity, and dynamic pruning/restoration provides better properties as compared to previous methods.

### Weaknesses
Given the contribution of UGS and other series of graph lottery tickets work, this automated tool sounds like incremental work. However, the analysis of scalability issues when applied to deep GNNs is worth reading.

Most experiments are conducted on small and transductive graph/tasks. The ogbn-arxiv is a small graph and ogbn-protein is a medium graph actually but are claimed as large graphs, more reasonablely large graphs should be considered. Also, how about inductive settings like GraphSAGE or other SOTA ones?

Other than the above aspects, I think the other perspectives of this paper are clear.

### Questions
See weaknesses. I wonder whether the contribution applied to an inductive setting or evolving graphs with increasing nodes or edges.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
