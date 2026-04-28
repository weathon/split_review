# Scalable and Effective Implicit Graph Neural Networks on Large Graphs

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 3, 8

## Abstract
Graph Neural Networks (GNNs) have become the de facto standard for modeling graph-structured data in various applications. Among them, implicit GNNs have shown a superior ability to effectively capture long-range dependencies in underlying graphs. However, implicit GNNs tend to be computationally expensive and have high memory usage, due to 1) their use of full-batch training; and 2) they require a large number of iterations to solve a fixed-point equation. These compromise the scalability and efficiency of implicit GNNs especially on large graphs. In this paper, we aim to answer the question: how can we efficiently train implicit GNNs to provide effective predictions on large graphs? We propose a new scalable and effective implicit GNN (SEIGNN) with a mini-batch training method and a stochastic solver, which can be trained efficiently on large graphs. Specifically, SEIGNN can more effectively incorporate global and long-range information by introducing coarse-level nodes in the mini-batch training method. It also achieves reduced training time by obtaining unbiased approximate solutions with fewer iterations in the proposed solver. Comprehensive experiments on various large graphs demonstrate that SEIGNN outperforms baselines and achieves higher accuracy with less training time compared with existing implicit GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors identify 2 problems with mini-batching implicit GNNs:

1) The traditional minibatches formed for GNN training is often done through sampling which ignores long-range dependency nodes.

2) Implicit GNNs take a long time to converge, hurting scalability.

The authors propose 2 solutions to said problems.

1) The authors propose adding coarse nodes between minibatch subgraphs to facilitate long-range message propagation during training (when combined with standard techniques like GraphSAGE)

2) The authors extend Neumann series, a implicit GNN solver proposed in [1], by making it a unbiased stochastic solver.

The authors provide experiments and ablations to show their minibatch sampling method is superior to existing works.

[1] Eignn: Efficient infinite-depth graph neural networks

### Strengths
The authors provide a compelling argument that their augmentations to mini-batch sampling and implicit GNN solving can improve the scalability of implicit GNNs. 

- The authors identified a compelling issue with existing mini-batch approaches.

- The solutions the authors provide are simple, yet intuitive. 

- The paper is written clearly and is easy to follow.

- The authors provide timing experiments to empirically verify SEIGNN's scalability.

- The authors try various different minibatch methods with the coarse nodes.

- The method is targeted towards implicit GNNs, which is a subset of all possible GNNs (though the authors demonstrate the method generalizes to other GNNs)

### Weaknesses
To be fully convinced, I have a few more questions regarding the approach:

- [important] On datasets where full-batch training is available, what is the performance trade-off of using SEIGNN over the full implicit GNN and a naive subsampling of the full-batch?

- How does modifying the sizes of the minibatch subgraphs affect the efficacy of SEIGNN's coarse nodes?

- How important is using PPR for the coarse node idea? Could SEIGNN generalize to other importance metrics?

- The method is targeted towards implicit GNNs, which is a subset of all possible GNNs (though the authors demonstrate the method generalizes to other GNNs)

### Questions
In addition to the weaknesses section, I have a few more questions:

- Have you considered adding multiple coarse nodes in between mini-batch subgraphs? What would be the effect of this?

- What would be the effect of removing/keeping the coarse nodes post-training?

- Why is the stochastic solver slightly better in performance than the Neumann solver in Table 4 of the ablation studies? Is the Neumann solver a truncated version here?

### Soundness
3 good

### Presentation
4 excellent

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
This paper proposes a scalable and effective implicit GNN (SEIGNN) with a mini-batch training method. Experiments demonstrate SEIGNN outperforms the state-of-the-art implicit GNNs on various large graphs.

### Strengths
1. SEIGNN is fast and memory-efficient.
2. The accuracy of SEIGNN on the large datasets is significantly higher than the state-of-the-art implicit GNNs.

### Weaknesses
My major concern is the reproducibility of this paper.

1. Table 4 shows that the improvement of SEIGNN is due to the coarse nodes. However, the authors do not analyze why the coarse nodes improve the prediction performance.
2. The authors do not provide the codes for reproducibility.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a scalable and effective implicit graph neural network (GNN) model, called SEIGNN, that can handle large graph data. Implicit GNNs are models that can capture long-range dependencies in graphs by solving a fixed-point equation. However, they are computationally expensive and memory-intensive, due to their use of full-batch training and a large number of iterations. SEIGNN addresses these limitations by using a mini-batch training method with coarse nodes and a stochastic solver. The coarse nodes are added to the mini-batch to incorporate global information from the graph, and the stochastic solver is used to obtain unbiased approximate solutions with fewer iterations. SEIGNN can be integrated with any existing implicit GNN model to improve its performance. The paper evaluates SEIGNN on six datasets and shows that it achieves better accuracy with less training time than existing implicit GNNs.

### Strengths
* The paper tackles a novel and important problem of scaling up implicit GNNs to large graphs, which has applications in real-world massive graphs.
* The authors introduce a mini-batch sampling strategy that can preserve the global and long-range information of the graph by using coarse nodes and can achieve reduced training time by using a stochastic solver.
* Extensive experiments and analysis are conducted to demonstrate the advantages of the proposed framework in mini-batch training.

### Weaknesses
 * The paper fails to position itself with recent related works. More SOTA papers in mini-batch training strategy should be included for discussion, such as [1-3]. The idea of introducing coarse nodes during the process of mini-batching is relatively straightforward and appears in existing literature such as [3]. Therefore, it hurts the novelty of this work regarding the first contribution without a thorough comparison with the current mini-batching GNN methods that also include coarse nodes. Meanwhile, there is a very relevant and similar work that should be added for comparison [4].

* For the second contribution of accelerated training with the Neumann solver, it is unclear how the authors constrain $n$ to be sufficiently large during experiments. In other words, does the performance of SEIGNN be affected even if the proposed stochastic solver is not an unbiased estimator? Could the authors elaborate more on this? 

* The setting of the experiments could be improved to better reflect the contributions. Do the results for all implicit GNNs come from full-batch training on all benchmarks? What would performance be if we incorporated different mini-batching sampling strategies for the baseline implicit GNNs? Meanwhile, more recent baselines of scalable GNN should be added for comparison such as [5-6].

* This manuscript aims to scale implicit GNNs to large graphs, but the benchmarks have nearly become standard for even some GNNs that are not specifically designed for scalability. Therefore, large graphs such as ogbn-papers100M should be evaluated for the scalability aim. Note that even the largest dataset (ogbn-products) used in this manuscript is marked as medium in OGB benchmarks.

### Questions
Please kindly refer to the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to address the scalability and efficiency challenges associated with implicit Graph Neural Networks (GNNs), which are designed to capture long-range dependencies in graph-structured data. It first points out that the implicit GNNs are suffering from the computational burden brought by (1) full-batch training and (2) a large number of iterations to solve fixed-point equations, limiting their applicability to large graphs. This work proposes a scalable and effective SEIGNN model that employs mini-batch training with coarse-level nodes to encourage information propagation between subgraphs. Extensive experiments are conducted to justify the power of SEIGNN in terms of both efficiency and efficacy.

### Strengths
1. This work is clearly motivated, addressing the scalability issue of IGNN is an important problem.

2. Good performance and comprehensive ablation study.

3. Writing is clear and easy to follow.

### Weaknesses
Please refer to ``Questions``.

### Questions
1. I agree that subgraph-wise sampling (ClusterGCN) and node-wise sampling (GraphSage) indeed lead to a loss of long-range dependencies. However, how about layer-wise sampling, such as the approaches like LADIES[1] and fastGCN[2]? 

2. I want to confirm my understanding. In subgraph sampling, the coarse nodes are excluded from being the target nodes but will be included in the sampled subgraph through the top-k Personalized PageRank (PPR) selection step, is that correct?

3. Given that the purpose of introducing the coarse nodes is to maintain long-term dependencies in mini-batch training, can SEIGNN ensure that coarse nodes are included in each mini-batch? Or is there a way to encourage the sampled subgraph to include more coarse nodes?


[1] https://arxiv.org/abs/1911.07323
[2] https://arxiv.org/abs/1801.10247

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
