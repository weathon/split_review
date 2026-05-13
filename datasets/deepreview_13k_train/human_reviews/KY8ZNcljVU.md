# NetInfoF Framework: Measuring and Exploiting Network Usable Information

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Given a node-attributed graph, can we tell whether the graph neural networks (GNNs) will perform better than multi-layer perception (MLP) on graph tasks? 
Graph tasks, such as link prediction and node classification, are commonly solved by adopting GNNs.
\xiangsx{What are graph tasks? Can we introduce graph tasks first, i.e., the second sentence then raise this question?}
However, they may not always work as expected in some graph scenarios, for example, in the case that the structure is randomly connected. 
\xiangsx{What does structure is uniform mean?}
Figuring out the reasons is not trivial and can cost a huge amount of time and resources. 
That is to say, how can we identify the usable information in the graph data in a principled way?
To address this, we propose \method, including \analysis and \model, for the detection and the exploitation of network usable information, respectively.
Given a graph data, \analysis measures the network usable information (NUI) without any model training, and \model to solve link prediction and node classification, while two modules share the backbone.
\james{what tasks do we refer to? I cannot understand the NetInfoA\_Act\'s function purely based on this sentence}
In summary, \method has following notable advantages:
(a) \general, handling both link prediction and node classification;
(b) \principled, with theoretical guarantee and closed-form solution;
(c) \effective, with the highest average rank, thanks to the proposed adjusted node similarity;
\james{ may change this to our performance numbers}
\christos{YES! lets give our best few numbers!}
(d) \scalable, being linear with the input size.
Applied \method on both synthetic and real-world graphs, \analysis successfully identifies the ground truth usable information in the synthetic datasets, and \model always wins or ties with many GNN baselines.
Our success story further demonstrate the correctness of \analysis in a real-world scenario, where there is no usable information in graphs constructed with some specific types of edges.
Given a node-attributed graph, and a graph task (link prediction or node classification),
can we tell if a graph neural network (GNN) will perform well?
More specifically, do the graph structure and the node features carry enough usable information for the task?
Our goals are 
(1) to develop a fast tool to measure how much information is in the graph structure and in the node features, and
(2) to exploit the information to solve the task, if there is enough.
We propose \method, a framework including \analysis and \model, for the measurement and the exploitation of network usable information (NUI), respectively.
Given a graph data, \analysis measures NUI without any model training, and \model solves link prediction and node classification, while two modules share the same backbone.
In summary, \method has following notable advantages:
(a) \general, handling both link prediction and node classification;
(b) \principled, with theoretical guarantee and closed-form solution;
(c) \effective, thanks to the proposed adjustment to node similarity;
(d) \scalable, scaling linearly with the input size.
In our carefully designed synthetic datasets, \method correctly identifies the ground truth of NUI and is the only method being robust to all graph scenarios.
Applied on real-world datasets, \method wins in \textit{11 out of 12} times on link prediction compared to general GNN baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel framework, NETINFOF, designed to quantify and leverage Network Usable Information (NUI) for graph tasks like link prediction and node classification. The approach tackles the need for extensive model training by using NETINFOF_PROBE to measure NUI directly from graph data, which is a significant improvement  from traditional GNNs that rely on trained low-dimensional representations. The NETINFOF_ACT component then uses this measured information to enhance the performance of graph tasks. The framework's robustness is tested on synthetic datasets designed to include various graph scenarios and validated on real-world datasets, showing superior results in link prediction tasks over standard GNN models. This paper's primary contribution is a method that can quickly assess a graph's usefulness for a task, offering a theoretical lower bound for accuracy without the computational overhead of model training​. The empirical study of this paper is very strong, surpassing most GNN methods both in accuracy and scalability.

### Strengths
- **Methodological Innovation**: NetInfoF introduces a novel approach to measure NUI directly from the graph structure and node features, which is a different from traditional methods that rely heavily on model training. This innovation could have a broad impact, particularly in scenarios where computational efficiency is paramount​. Also, the adjustments of node similarity using compatibility matrix w/ negative edges is very interesting.
- **Teoretical Foundation and Empirical Validation**: The paper provides a theoretical analysis for the NetInfoF_Score, presenting it as a lower bound for the accuracy of a GNN on a given task. This theoretical contribution is well-supported by empirical evidence on both synthetic datasets and real-life datasets.
- **Scalability**: The demonstrated scalability of NetInfoF, especially its linear scaling with input size (Fig. 6), and the use of significantly fewer parameters compared to GAE methods (1280 vs 279k) demonstrates its potential for application in large-scale graph tasks, presenting a substantial advancement in the practical deployment of GNNs​. Though NetInfoF is slower than SlimG [1], NetInfoF has better accuracy. 

Combining 2nd and 3rd points, NetInfoF is better than GAE methods both in accuracy and scalability empirically, which is a significant contribution in link prediction tasks.






[1] Yoo, Jaemin, Meng-Chieh Lee, Shubhranshu Shekhar, and Christos Faloutsos. "Slendergnn: Accurate, robust, and interpretable gnn, and the reasons for its success." arXiv preprint arXiv:2210.04081 (2022).

### Weaknesses
1. The proof of Theorem 2 is problematic due to the incorrect use of conditional entropy. The proof incorrectly states the conditional entropy in Appendix A.2 as:
$$
H(Y|X) = \sum_{i=1}^{m} p_i \left(-\sum_{j=1}^{n} p_{ij} \log_2 p_{ij}\right),
$$
which is incorrect because it uses the joint probabilities $p_{ij}$ instead of the conditional probabilities. The correct expression for conditional entropy, which is based on the conditional probabilities, is:
$$
H(Y|X) = -\sum_{i=1}^{m} \sum_{j=1}^{n} p_{ij} \log_2 P(Y=y_j|X=x_i),
$$
where $P(Y=y_j|X=x_i) = \frac{p_{ij}}{p_i}$ is the conditional probability of $Y$ given $X=x_i$. And $p_i = \sum_{j=1}^{n} p_{ij}$ represents the marginal probability of $X$ taking the value $x_i$. This definition adheres to the fundamental property that the conditional probabilities for a given $x_i$ should sum to 1, i.e., $\sum_{j=1}^{n} P(Y=y_j|X=x_i) = 1$.

The misuse of conditional entropy in the proof leads to an erroneous application of Jensen's Inequality and subsequently invalidates the derived bound on the NetInfoF score.

2. (Minor) Given the paper is mostly dealing with link prediction tasks. It will be beneficial to include some subgraph-based methods as baselines, such as SEAL [1]. I understand that NetInfoF is intended as an advancement beyond traditional GNN approaches, but including subgraph-based methods will give the community a more comprehensive evaluation of NetInfoF's capabilities. It's evident NetInfoF is way more scalable than subgraph-based methods, but subgraph-based methods are still SOTA on some datasets, e.g. Ogbl-collab.

### Questions
1. Can the authors provide a more detailed justification for Theorem 2, particularly in light of the concerns highlighted in the first weakness?  I will raise my score if the authors can give a reasonable update. 
2. How are the "Our bound" lines in Figures 3 and 4 derived? Additional details on this calculation would aid in understanding these figures.
3. How NetInfoF_Probe estimates and calculates the discretizer in section 4.2? Maybe some examples or explanations will help reader understand this.
4. An ablation study detailing the individual contributions of the five different node embedding components mentioned in Section 3.2 would be beneficial. Are these components equally influential in terms of accuracy, or do some weigh more significantly than others?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a framework called NETINFOF for measuring and exploiting network usable information (NUI) in node-attributed graphs. The authors aim to determine if a graph neural network (GNN) will perform well on a given task by assessing the information present in the graph structure and node features. NETINFOF consists of two components: NETINFOF PROBE, which measures NUI without model training, and NETINFOF ACT, which solves link prediction and node classification tasks. The framework offers several advantages, including generality, principled approach, effectiveness, and scalability. The authors demonstrate the superiority of NETINFOF in identifying NUI and its performance in real-world datasets compared to general GNN baselines.

### Strengths
1. The paper introduces the novel NETINFOF framework, which addresses the problem of measuring and exploiting network usable information in graph for GNNs. 
2. The paper demonstrates sound technical claims, supported by theoretical guarantees and empirical evaluations on synthetic and real-world datasets.
3. The writing style is clear, and the paper is well-organized, making it easy to understand the proposed framework and its contributions.
4. The paper's contributions are promising as they provide a practical tool (NETINFOF) for assessing the usefulness of graph structure and node features in GNN tasks. The framework shows promising results and outperforms existing baselines in link prediction.

### Weaknesses
1. How does the NETINFOF framework handle noisy or incomplete graph data? Can it effectively measure and exploit network usable information in such scenarios?

2. Are there specific types of graph structures or node features for which NETINFOF may not perform well? How robust is the framework in diverse graph settings?

3. I have concerns regarding the sensitivity of NETINFOF to the estimated compatibility matrix (H) used in the framework. It would be beneficial if the authors could provide additional empirical results that examine the performance of NETINFOF under different label rates, as label rates can significantly impact the correctness of H.

### Questions
see weaknesses

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
The paper discusses the NETINFOF framework, which focuses on measuring and utilizing the usable information in node-attributed graphs for graph tasks such as link prediction and node classification. The authors propose two components of the framework: NETINFOF PROBE, which measures the amount of information present in the graph structure and node features without any model training, and NETINFOF ACT, which uses the measured usable information to solve the graph tasks.

### Strengths
Lots of experiments

### Weaknesses
1. "How to connect the graph information with the performance metric on the task?" Here are some missed related works [1,2,3,4,5].

2. What is $f$ in C4? I suggest not using $f$, because you already use it as the number of features.

3. In theorem 1, "Given a discrete random variable Y , we have..." What is "accuracy(Y)"? Accuracy of a a discrete random variable? This looks weird and I suggest giving a more strict and accurate statement. What is $p_y$?

4. "Predicting links by GNNs relies on measuring node similarity, which is incorrect if the neighbors have heterophily embeddings." The embedding will be similar even with heterophily connections if the nodes share similar neighborhood patterns [6].

5. "the node embeddings of linear GNNs require no model training“ I don't understand this. Why linear GNNs don't require training? Do you mean SGC [7] don't require training?

6. "It results in low value when node i and node j have heterophily embeddings, even if they are connected by an edge." This is not correct, see [2,3,6].

### Questions
1. "How to connect the graph information with the performance metric on the task?" Here are some missed related works [1,2,3,4,5].

2. What is $f$ in C4? I suggest not using $f$, because you already use it as the number of features.

3. In theorem 1, "Given a discrete random variable Y , we have..." What is "accuracy(Y)"? Accuracy of a a discrete random variable? This looks weird and I suggest giving a more strict and accurate statement. What is $p_y$?

4. "Predicting links by GNNs relies on measuring node similarity, which is incorrect if the neighbors have heterophily embeddings." The embedding will be similar even with heterophily connections if the nodes share similar neighborhood patterns [6].

5. "the node embeddings of linear GNNs require no model training“ I don't understand this. Why linear GNNs don't require training? Do you mean SGC [7] don't require training?

6. "It results in low value when node i and node j have heterophily embeddings, even if they are connected by an edge." This is not correct, see [2,3,6].



[1] Characterizing graph datasets for node classification: Beyond homophily-heterophily dichotomy. arXiv preprint arXiv:2209.06177.

[2] Revisiting heterophily for graph neural networks. Advances in neural information processing systems, 35, 1362-1375.

[3] When do graph neural networks help with node classification: Investigating the homophily principle on node distinguishability. arXiv preprint arXiv:2304.14274.

[4] Demystifying Structural Disparity in Graph Neural Networks: Can One Size Fit All?. arXiv preprint arXiv:2306.01323.

[5] Exploiting Neighbor Effect: Conv-Agnostic GNN Framework for Graphs With Heterophily. IEEE Transactions on Neural Networks and Learning Systems.

[6] Is Homophily a Necessity for Graph Neural Networks?. In International Conference on Learning Representations 2022.

[7] Simplifying graph convolutional networks. In International conference on machine learning, pp. 6861–6871. PMLR, 2019.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
