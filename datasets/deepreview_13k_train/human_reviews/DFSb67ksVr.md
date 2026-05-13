# Clique Number Estimation via Differentiable Functions of Adjacency Matrix Permutations

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Estimating the clique number in a graph is central to various applications, e.g., community detection, graph retrieval, etc. 
Existing estimators often rely on non-differentiable combinatorial components. Here, we propose a full differentiable estimator for clique number estimation, which can be trained from distant supervision of clique numbers, rather than demonstrating actual cliques.
Our key insight is a formulation of the maximum clique problem (MCP) as a maximization of the size of fully dense square submatrix, within a suitably row-column-permuted adjacency matrix.
We design a differentiable mechanism to search for permutations that lead to the discovery of such dense blocks.
However, the optimal permutation is not unique, which leads to the learning of spurious permutations. To tackle this problem, we view the MCP problem as a sequence of subgraph matching tasks, each detecting progressively larger cliques in a nested manner. This allows effective navigation through suitable node permutations.
These steps result in MxNet, an end-to-end differentiable model, which learns to predict clique number without explicit clique demonstrations, with the added benefit of interpretability.  Experiments on eight datasets show the superior accuracy of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this submission, the authors propose a differentiable solution to the clique number estimation problem. In particular, they formulate the maximum clique problem (MCP) as a maximization of the size of a fully dense square submatrix within a suitably row-column-permuted adjacency matrix. 
This problem can be further treated as a sequence of subgraph matching tasks, and the cliques can be progressively detected, leading to a fully differentiable neural network called MxNet. Experiments show that the proposed method outperforms baselines in most situations, which is more robust to the OOD issue.

### Strengths
1. The problem is significant for many applications.
2. The proposed method is reasonable, and the re-formulation of MCP is insightful.
3. The experiments are solid and sufficient. Analytic experiments such as ablation studies are provided.

### Weaknesses
1. The writing and organization of the proposed method are not friendly to readers without sufficient background. In the introduction section, adding a figure illustrating the task may help readers quickly grasp the key concepts of the paper. Similarly, in Figure 1, binding notations like MSS(B) and rho_theta to the modules in the figure is necessary.  
2. The motivation and rationale behind certain modeling strategies are not clearly explained. For instance, in Figure 1, what is the purpose of using a smooth surrogate for the adjacency matrix, specifically the Hadamard product with $XX^T$? Is there an ablation study that supports this approach? Additionally, the effects of the bicriteria early stopping strategy have not been verified, specifically how the performance of the submatch loss is affected by this choice.
3. The scalability of the proposed method for large graphs has not been verified. In particular, the Sinkhorn network often experiences numerical instability when dealing with very large graphs, due to the iterative normalization. What approaches can be taken to mitigate this issue? Additionally, how should the temperature of the Gumbel-softmax be set within the network, and what is the sensitivity of the method to this parameter?
4. The lambda balances the two terms in the loss function, is the proposed method robust to this hyperparameter? What is the sensitivity of the method to the choice of lambda across different datasets?

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors present a method for learning the maximum clique size in graphs by parameterizing node permutations using neural networks and training them with a composition of two types of losses, maximal subsquare (MSS) and SubMatch. Combined with techniques including various neural relaxations, curriculum training and bi-criteria early stopping, the model is able to learn to predict maximum clique size better than or close to the best among a number of baseline methods on several benchmark datasets.

### Strengths
While prior works have proposed various deep learning approaches for solving the maximum clique problem, the "distant supervision regime" where only the size of the maximum clique is provided during training is under-explored, and the authors' proposal to parameterize node permutation matrices with GNNs and Sinkhorm iterations is novel to my knowledge and an interesting one. The authors have also performed extensive numerical experiments to compare the proposed method with several baselines as well as analyzing the various design choices such as the loss choice and the early stopping criteria. The paper is clearly-written overall with technical details well-documented.

### Weaknesses
As acknowledged by the authors, the computational burden of the MxNet model may be a concern when dealing with larger graphs, and indeed the datasets used in the experiments consist of relatively small graphs.

See two questions below regarding some design choices in the MxNet model.

1. In Section 3.1, the authors proposed a differentiable approximation of the combinatorial MCP by relaxing the discrete objective in three fronts, and I am curious if there is evidence or to believe that the first (relaxing the adjacency matrix to be continuously-valued embeddings) and the third (replacing Algorithm 1 by a message passing GNN) are necessary / beneficial in the case of featureless graphs. Without them, it seems that the model can still be trained via a differentiable loss function and the model might actual be more interpretable. A similar question on the relaxation of the clique average loss for the definition of MxNet (SubMatch) in Section 3.2.

2. In equation (8) for the subgraph matching problem, the last inequality ($K_{\omega(G)} \leq P A P^{\intercal}$) necessarily entails the earlier ones (e.g., $K_1 \leq P A P^{\intercal}$). Hence, instead of using the full curriculum with $c$ ranging from $2$ to $\omega(G)$, it seems possible to consider a simplification of the SubMatch loss in (9) by reducing the first (respectively, second) inner summation over $c$ to only the last term with $c = \omega(G)$ (respectively, $c = \omega(G)-1$). Is there evidence that including the full sequence of $c$'s is helpful?

Finally just a typo: On the bottom of Page 7, "$u$ indicating" --> "indicates".

### Questions
1. In Section 3.1, the authors proposed a differentiable approximation of the combinatorial MCP by relaxing the discrete objective in three fronts, and I am curious if there is evidence or to believe that the first (relaxing the adjacency matrix to be continuously-valued embeddings) and the third (replacing Algorithm 1 by a message passing GNN) are necessary / beneficial in the case of featureless graphs. Without them, it seems that the model can still be trained via a differentiable loss function and the model might actual be more interpretable. A similar question on the relaxation of the clique average loss for the definition of MxNet (SubMatch) in Section 3.2.

2. In equation (8) for the subgraph matching problem, the last inequality ($K_{\omega(G)} \leq P A P^{\intercal}$) necessarily entails the earlier ones (e.g., $K_1 \leq P A P^{\intercal}$). Hence, instead of using the full curriculum with $c$ ranging from $2$ to $\omega(G)$, it seems possible to consider a simplification of the SubMatch loss in (9) by reducing the first (respectively, second) inner summation over $c$ to only the last term with $c = \omega(G)$ (respectively, $c = \omega(G)-1$). Is there evidence that including the full sequence of $c$'s is helpful?

Finally just a typo: On the bottom of Page 7, "$u$ indicating" --> "indicates".

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces MXNET, an end-to-end differentiable model for estimating the clique number in the graph. It contains MXNET(MSS) detection that detects cliques via message passing on permuted adjacency matrix and MXNET(SubMatch) that curriculum matches a series of cliques. Extensive experiments highlight the effectiveness of the proposed methods.

### Strengths
S1: It integrates both the message-passing-based clique detection and the matching-based techniques for accurate clique number estimation.

S2: The design of the proposed method has sufficient motivations.

S3: Experiments over multiple datasets validate its effectiveness.

### Weaknesses
W1: A more thorough comparison and introduction of related works would enhance the quality of this paper.
W1.1: A related field is subgraph counting [1]. We can directly use 2-cliques, 3-cliques, ..., k-cliques as query graphs and apply subgraph counting methods to determine the number of k-cliques in the data graph. If the number of k-cliques is 1, then the clique number may be k. Given the limited availability of direct baselines for the problem of clique number estimation, this method could serve as a promising baseline. Some promising methods are in [1] and [4]. The first one stands as a representative that uses the neural method to estimate the subgraph number while the second, while the second one stands as a representative that designs an algorithm for subgraph counting. It would be beneficial to explore how these methods perform, especially considering their different approaches (neural vs. algorithmic) and computational costs.

W1.2: Another promising area is the development of algorithm-based methods for approximate maximum clique detection or k-clique detection, as well as exact maximum clique detection [2]. These methods appear capable of quickly identifying accurate cliques. Exploring the motivation for using learning-based approaches and comparing these methods would be beneficial. Some promising methods are in [2] and [3]. The method in [2] is for exact maximum clique detection while the method in [3] is for approximate k-clique detection with theoretical guarantee which can be adapted for Clique Number Estimation. Specifically, it would be helpful to understand how the proposed learning-based method compares to these algorithms in terms of accuracy, runtime, and scalability, especially since some of these algorithms offer theoretical guarantees on approximation quality.

========

W2: Some claims can be improved
W2.1: The authors seem to argue that relying on "extreme or no supervision" is not beneficial (Line 061).  However, intuitively, avoiding such supervision could enhance the generalization and applicability of the algorithms used. A better explanation would help the understanding of this paper. It's unclear why the authors believe that some level of supervision is necessary, and what specific limitations they see in methods that operate without it. A more detailed discussion of the trade-offs between different levels of supervision would be valuable.

W2.2: The author seems to focus on introducing prior work related to the Maximum Clique problem (Lines 49-62) in the introduction. However, the existing methods for estimating the clique number and their limitations are not sufficiently explored. The introduction should clearly differentiate between the maximum clique problem and the clique number estimation problem, highlighting the specific challenges and existing approaches for the latter.

========

W3: Some experiments can be enhanced.

W3.1: As demonstrated in the related works introduced in Section 1.2, the clique number can be bounded. (There are also many other metrics that can be used to bound the clique number.) Given that the graph used in this paper is small and dense (see Table 7), employing these bounded metrics may yield good results and assist in pruning unpromising outcomes. As there are not many methods directly predicting the clique number, this bound-based baseline would be a good choice. It would be useful to see how these bounds compare to the proposed method, especially in terms of computational efficiency and accuracy.

W3.2: The datasets evaluated in the paper are dense and small, with the largest containing only 300 nodes. It would be interesting to assess the performance on more diverse and larger datasets, as we can easily identify the exact cliques in smaller graphs. For example, the method proposed in previous works like in [3] can handle billion-scale graphs. Some smallest datasets in this paper like Email and Amazon would be helpful to asses the performance of the MXNET. The paper should provide a clear rationale for why these specific datasets were chosen and discuss the potential limitations of generalizing the results to larger and sparser graphs.


W3.3: The authors evaluate the effect of distribution shift; however, they remain within the same graph. It would be interesting to assess whether the trained model can generalize to different datasets, especially since there may be scenarios where labels are not available for training. An interesting scenario is that could the model trained in this paper can be generalized to predict the clique number for the datasets in [3]. This is important to understand the robustness and generalizability of the proposed method.

### Questions
Q1: How do these subgraph counting algorithms perform in the clique number estimation?

Q2: How do these bound-based algorithms perform in the clique number estimation?

Q3: How does the proposed method perform in large graph.

### Soundness
3

### Presentation
3

### Contribution
3
