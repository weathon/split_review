# Differentiable Cluster Graph Neural Network

- Decision: Reject
- Scores: 6, 3, 8, 5

## Abstract
Graph Neural Networks often struggle with long-range information propagation and in the presence of heterophilous neighborhoods.
We address both challenges with a unified framework that incorporates a clustering inductive bias into the message passing mechanism, using additional cluster-nodes.
Central to our approach is the formulation of an optimal transport based implicit clustering objective function. However, the algorithm for solving the implicit objective function needs to be differentiable to enable end-to-end learning of the GNN. To facilitate this, we adopt an entropy regularized objective function and propose an iterative optimization process, alternating between solving for the cluster assignments and updating the node/cluster-node embeddings. 
Notably, our derived closed-form optimization steps are themselves simple yet elegant message passing steps operating seamlessly on a bipartite graph of nodes and cluster-nodes.
Our clustering-based approach can effectively capture both local and global information,  
demonstrated by extensive experiments on both heterophilous and homophilous datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a differentiable end-to-end clustering-based graph neural network for node classification tasks. The proposed model attempts to address over-squashing and heterogeneity. The model is carefully designed to make it differentiable and the authors provide theoretical guarantees on convergence and time complexity.

### Strengths
1. The paper is clearly written and easy to read.
2. The proposed end-to-end differentiable model is convincing and the proposed model is trying to solve the important problems encountered in graph representation learning models such as over-squashing and heterophily.
3. Experimental results show that the model works well and experimental details are provided in the appendix.

### Weaknesses
1. The model has multiple hyperparameters, which is very confusing for the potential user of the proposed model to select the optimal hyperparameters.
2. The proposed model seems difficult to train and converge despite Theorem 3.3 can provide some guarantee for convergence. I'm not sure if the model can converge only in a very narrow range of hyperparameters, and the code is not open-sourced.
3. $|\Omega|$ can not be removed from asymptotic time complexity $O(T|\mathcal{V}||\Omega|)$ simply because of $|\Omega| \ll |\mathcal{V}|$. ). I suggest that the authors keep the original complexity with these hyperparameters, and then provide a simplified complexity when these hyperparameters are considered as constants. I suggest that the authors report in their experiments the training time and running time of DCGNN in comparison with classical models such as GCN.
4. For this reason and concerns about convergence speed, I am worried about the actual training-to-convergence time might be longer than expect. I note that run times are provided in Appendix D.3, but I would expect the authors to report training times and loss curves.

### Questions
1.  How to choose model hyper-parameters in practice?
2. I expect the authors to provide the training time and loss curves for the model.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a GNN that uses cluster-based messaging passing to address the over-squashing and heterophily problems in graph representation learning.The author claims that their cluster-based method (DC-GNN) can handle both long-range dependencies and heterophilous aggregation, by projecting graphs and node neighbors into a bipartite graph of global clusters and local clusters. DC-GNN is different than the current methods by taking the bipartite graph as input instead of using the adjacency or graph Laplacian in the network.

### Strengths
1. Converting the graph structure (adjacency or graph Laplacian) into a bipartite graph as GNN input is interesting.

### Weaknesses
1. No model access, no code access. (major)

2. Most baseline results reported in Table1 do not align with the results reported in original papers. Where did you get the baseline results? If you run the baselines, please provide codes/loggers or any proof. If not, please cite the sources that you used. (major)

3. Overall contribution is not much, not so exciting. (minor)

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a differentiable cluster GNN to deal with the long-rage information propagation and local heterophilous neighborhood aggregation problem in graph domain. Specifically, the framework considers a clustering inductive bias into the message propagation by using additional cluster-nodes. Besides, authors adopt an iterative process to optimize the cluster assignments and node/cluster-node embeddings. Extensive experimental results show the effectiveness of the proposed framework.

### Strengths
1.	The paper addresses two critical challenges—over-squashing and heterophilous neighborhood aggregation with a unified framework.
2.	The iterative optimization with soft cluster assignment makes it possible to learn both node and cluster-node embeddings efficiently.
3.	Experimental results are sufficient to demonstrate the effectiveness of the proposed model.

### Weaknesses
1.	The complexity analysis is very rough, the preprocessing of constructing bipartite graph may cost time, so it would be better to supplement the complexity of preprocessing data.
2.	The introduction of so-called “cluster nodes” is basically assigning a pseudo label to each node, which is quite common among methods on graph heterophily. 
3.	The novelty of directly integrate clustering into the message-passing mechanism is somehow weak.

### Questions
1.	The authors mention “cluster patterns” many times, but it is unclear what the definition of cluster patterns is?
2.	How does the construction of the bipartite graph scale for extremely large datasets?
3.	The paper uses soft cluster assignments but it lacks the sensitivity analysis of the entropic regularization \lambda and the number of clusters?
4.	From the ablation studies, the contributions of local and global clustering vary. It would be better to provide further intuition or guidelines on when one should prioritize local or global clusters for new datasets.
5.	As the bipartite graph grows with the addition of cluster-nodes, what are the memory implications?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper incorporates a clustering inductive bias, combining nodes with "cluster nodes" in a bipartite structure and leveraging optimal transport for differentiable clustering. The framework iteratively optimizes node and cluster-node embeddings and integrates clustering directly within message passing, effectively capturing both global and local patterns.

### Strengths
1. This work integrates clustering into message passing, allowing for both global and local pattern capture, which is effective for diverse graphs.
2.  This work demonstrates effectiveness on multiple datasets.

### Weaknesses
1. The author claims that facilitating long-range interactions across distant nodes. Thus it should be tested on long-range graph datasets in [1].
2. The proposed method does not achieve the best performance in all cases in Table 2. More analysis on why performing poorly should be added.
3. [2] and [3] are related to this work. I think quoting them is needed.
4. The OT-based clustering and iterative optimization may add implementation complexity.

[1] Dwivedi, Vijay Prakash, et al. "Long range graph benchmark." Advances in Neural Information Processing Systems 35 (2022): 22326-22340.
[2] Kosmala, Arthur, et al. "Ewald-based long-range message passing for molecular graphs." International Conference on Machine Learning. PMLR, 2023.
[3] Chen, Dexiong, Till Hendrik Schulz, and Karsten Borgwardt. "Learning Long Range Dependencies on Graphs via Random Walks." arXiv preprint arXiv:2406.03386 (2024).

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
2
