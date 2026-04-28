# TAFS: Task-aware Activation Function Search for Graph Neural Networks

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Since the inception of Graph Neural Networks (GNNs), extensive research efforts have concentrated on enhancing graph convolution, refining pooling operations, devising robust training strategies, and advancing theoretical foundations. Notably, one critical facet of current GNN research remains conspicuously underexplored—the design of activation functions. Activation functions serve as pivotal components, imbuing GNNs with the essential capacity for non-linearity. Yet, the ubiquitous adoption of Rectified Linear Units (ReLU) persists.
In our study, we embark on a mission to craft task-aware activation functions tailored for diverse GNN applications. We introduce TAFS (Task-aware Activation Function Search), an adept and efficient framework for activation function design. TAFS leverages a streamlined parameterization and frames the problem as a bi-level stochastic optimization challenge. To enhance the search for smooth activation functions, we incorporate additional Lipschitz regularization. Our approach automates the discovery of the optimal activation patterns, customizing them to suit any downstream task seamlessly. Crucially, this entire process unfolds end-to-end without imposing significant computational or memory overhead. Comprehensive experimentation underscores the efficacy of our method. We consistently achieve substantial improvements across a spectrum of tasks, including node classification over diverse graph data. Moreover, our approach surpasses state-of-the-art results in the realm of link-level tasks, particularly in biomedical applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces TAFS, a framework for designing task-specific activation functions in Graph Neural Networks (GNNs). TAFS uses a search algorithm to optimize activation functions for specific tasks, resulting in improved performance compared to traditional activation functions. The design of TAFS is more efficient than baseline methods on optimizing such bi-level optimization problems. The experiment results show that using TAFS usually achieves better performances than using fixed activation functions.

### Strengths
1. The paper is overall clearly written and easy to follow.
2. This paper studies a interesting research problem that is rarely studied in the GML domain.

### Weaknesses
1. The experimental results are not very convincing. The experiments are all conducted on very small datasets, and I don't think the datasets for link prediction experiments are the commonly used ones in literature. I'd recommend the authors to use more standardized and commonly accepted benchmarks such as the OGB ones.
2. Although the proposed method is already much more efficient than the baselines Swish and APL, it still takes about 10x times of runtime when compared with fixed activation functions. It's hard to tell whether the performance improvements worth such huge overhead on the time cost.

### Questions
1. I'd appreciate if the authors can elaborate more on the difference of the proposed method versus the activation function search methods for CNNs and RNNs (as referenced in Sec. 1).

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a framework for designing activation functions for graph neural networks (GNNs) based on the downstream task. The framework, called TAFS, uses a bi-level stochastic optimization problem with Lipschitz regularization to search for the optimal activation patterns. The authors claim that TAFS can automate the discovery of task-aware activation functions without significant computational or memory overhead and show that TAFS can achieve substantial improvements over existing methods in various tasks.

### Strengths
S1. The authors review the existing work, explain the necessity of achieving task-aware activation functions in the context of GNNs, and identify two challenges for this goal. To address them, the authors design a new framework consisting of a compact search space and an efficient search algorithm, which enables automated activation function search.

S2. The paper writing is relatively good, and the authors provide a detailed explanation of the key parts of their method, namely the implicit functional search space and the stochastic relaxation.

### Weaknesses
W1. Some of the experimental settings and results explanations in the paper are vague, such as Figure 1 in the Introduction section and Figure 3 in the Experiments section. I cannot understand how the experimental results in the figures were obtained, and what the data in the figures mean.

W2. From the experimental results, the performance of TAFS needs to be improved. Table 2 shows that in some experimental scenarios on the DBLP, Cornell, Texas and Chameleon datasets, the results obtained by TAFS are only marginally better than directly using a specific activation function, or even worse. The authors did not explain this phenomenon.

W3. I wonder why in the drug and protein interaction prediction experiments, only the results of TAFS and ReLU were provided, instead of comparing with multiple activation functions as in the node classification experiments.

W4. Since the authors compared the search efficiency with Swish and APL, why didn’t they involve the comparison with these two search-based methods in the effectiveness validation experiments (Table 2 and Table 3)?

### Questions
See the weakness part

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a Task-Aware Activation Function Search method, abbreviated as TAFS. TAFS is capable of efficiently searching for and discovering new, effective activation functions within GNN applications. Firstly, for the search space of activation functions, TAFS introduces a continuous latent space equipped with a general approximator that includes an additional smoothness constraint. Specifically, TAFS utilizes a MLP to approximate the optimal activation function, where the parameters of the MLP are optimized as part of the search space, incorporating a Jacobian regularization term. Secondly, employing stochastic relaxation techniques, the search space is reparameterized with a Gaussian distribution, shifting the optimization target from the parameters of the activation function to those of the Gaussian distribution. Comprehensive evaluations on node and link-level tasks demonstrate that this method achieves excellent performance.

### Strengths
1. Presents an innovative and intriguing approach to activation function search within the context of Graph Neural Networks, marking a novel area of research.
2. Introduces a probabilistic search algorithm capable of effectively exploring a regularized function space, leading to the discovery of novel activation functions.
3. Experimental results demonstrate that, compared to baseline methods, TAFS achieves excellent performance in node and link prediction tasks, significantly enhancing the efficiency of the search process.

### Weaknesses
1. The search strategy presented in this paper does not support a larger GNN search space. For instance, if there is a need to search for aggregation functions or message passing functions, the optimal form of the activation function is likely to change. The method's focus on activation functions in isolation may limit its applicability in more complex GNN architectures where different components interact. The paper does not address how the discovered activation functions would perform when combined with different aggregation or message passing schemes.

2. If TAFS employs an MLP to approximate the optimal activation function, the performance of activation function would also depend on the number of layers in the MLP and the non-linear transformation functions. This has not been discussed in this paper. The choice of MLP architecture, including the number of hidden layers and the activation functions within the MLP, is a critical hyperparameter that could significantly impact the search results. The paper lacks a systematic exploration of these hyperparameters and their influence on the discovered activation functions.

3. In experiments, although the paper introduces a Jacobian regularization term, the impact of this regularization has not been empirically tested. The paper does not provide any ablation studies to demonstrate the effectiveness of the Jacobian regularization term. Without this analysis, it is unclear whether the regularization is actually contributing to the performance gains or if it is simply an added complexity.

4. In TAFS, a stochastic relaxation is used, involving the reparameterization of the activation function parameters using a Gaussian distribution. However, this paper does not discuss the advantage of this strategy. Specifically, the paper does not analyze the impact of using a Gaussian distribution versus other possible distributions, nor does it justify why this particular choice is suitable for the problem. The lack of discussion on the properties of the Gaussian distribution and its implications for the search process is a significant gap.

### Questions
1. In a previous work [1], the best-performing activation function is referred to as Swish, which has a specific functional form. Similarly, can the best-performing activation function identified by TAFS be represented using a generic function?
[1] Prajit Ramachandran, Barret Zoph, and Quoc V . Le. Searching for activation functions. In International Conference on Learning Representations, ICLR, 2018.

2. The sentence in the main text, "… how can we design GNN activation functions to adapt effectively to various graph-based tasks, creating task-aware activation functions??" seems to have an issue with the use of symbols.

3. In the text, "... and demote by ¯w_δ all the parameters of GNN, …", the word "demote" appears to be misspelled.

4. The experimental section lacks clear explanations of the metrics used in the tables. For example, the description of Table 2 does not specify whether the results represent accuracy, AUC, or something else.

5. In Figure 4, subfigure (a) shows that larger values of K yield better results but at a slower pace, demonstrating a "trade-off between accuracy and computation time." Is the Y-axis in (a) representing accuracy? And it's not clear how the relationship between K value and computation time is depicted.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The study presents a novel approach to Graph Neural Network (GNN) activation function search using bi-level optimization. An efficient algorithm is introduced that explores a search space defined by universal approximators with smoothness constraints, allowing for quick optimal function discovery. By using stochastic relaxation, the algorithm bypasses the challenges of non-differentiable objectives, outperforming existing activation functions across various GNN models and datasets, leading to a tailored GNN activation function design.

### Strengths
1. The idea of designing a task-aware activation function for GNNs is excellent, since it could universally enhance the performance of GNNs across different datasets and tasks.
2. The writing and expression of this paper are good.

### Weaknesses
1. Graph classification is crucial in graph mining due to its emphasis on global topological structures. Given its distinct objectives from node classification, it's imperative for the author to include experiments on graph classification.
2. As a universal method, TAFS should be tested on as many GNN models as possible. GCN and GraphSAGE are quite similar, while GAT and GIN are different, which should also be used as backbone to evaluate the performance of TAFS.
3. The authors should conduct a time complexity analysis and compare it with GReLU.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
