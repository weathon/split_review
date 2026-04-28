# STRUCTDROP: A STRUCTURED RANDOM ALGORITHM TOWARDS EFFICIENT LARGE-SCALE GRAPH TRAINING

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
Graph neural networks (GNNs) have gained considerable success in graph-based learning tasks, yet training GNNs on large graphs is still inefficient. The root cause is the graph-based sparse operations are difficult to accelerate with commodity hardware. Prior art reduces the computation cost of sparse matrix based operations (e.g., linear) via sampling-based approximation. However, two under-explored pain points still persist in this paradigm. Inefficiency Issue: The random-based sampling approaches have the non-zero entries randomly distributing over adjacency matrix, which slows down memory access process and is difficult to accelerate with commodity hardware. Under-fitting Problem: The previous sampling methods only utilize the same subset of nodes during the training, which may cause the under-fitting problem on other remain nodes. Aiming to systematically address these two pain points, we propose StructuredDropout, a.k.a, StructDrop. This method involves the selective random sampling of columns and rows from a sparse matrix for computation. Comprehensive experiments validate the efficiency and generalization of our framework: StructDrop achieves up to 5.09x speedup for a single sparse operation and 6.48x end-to-end speedup with negligible accuracy loss or even better accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces Structured Dropout, i.e., StructDrop, to improve the efficiency of graph neural networks’ (GNNs) training on large graphs. Specifically, StructDrop replaces the sparse matrix multiplication (SpMM) in both the forward and backward passes of GNNs with its randomized counterpart achieved through uniformly sampling column-row pairs. Furthermore, to address the distribution shift brought by random sampling, instance normalization is applied after SpMM to rescale node embeddings and stabilize training. Experimental results on the benchmark datasets show that StructDrop significantly accelerates training with negligible accuracy loss or even better accuracy.

### Strengths
The proposed method, StructDrop, is straightforward and easy to understand. Experiments on benchmark datasets, employing two different GNN architectures, validate the effectiveness of StructDrop in accelerating the training of GNNs. The paper also demonstrates the benefits of incorporating instance normalization to mitigate the negative impact caused by StructDrop. Furthermore, the clarity and smooth flow of the paper contribute to its overall quality.

### Weaknesses
The proposed method, StructDrop, makes an incremental technical contribution within the context of existing research. Previous work has already explored the application of randomized matrix multiplication to sparse operations in the backward pass of GNNs. StructDrop builds upon this work by extending the method to the forward pass, with the primary modification being the adoption of a uniform sampling strategy for selecting column-row pairs, as opposed to the previous top-k sampling method. Furthermore, there are some inconsistent statements in this paper. For example, this paper states that StructDrop can address the inefficiency issue in the abstract but lacks elaboration in subsequent sections. Specifically, the paper does not clearly articulate how uniform sampling of column-row pairs directly translates to improved computational efficiency compared to other sampling strategies or standard sparse matrix multiplication. The paper also lacks a rigorous analysis of the computational cost associated with the proposed uniform sampling strategy, particularly in relation to the overhead of generating random samples and managing the data structures involved. The paper also lacks theoretical justification for why uniform sampling is effective in preserving the accuracy of GNNs, and how it compares to other sampling strategies in terms of convergence and generalization properties.

### Questions
1.	In the abstract, the paper highlights the inefficiency issue associated with random-based sampling approaches but lacks elaboration in subsequent sections. 

2.	In section 2.2, the paper reviews fast matrix multiplication with sampling. In the original formulation, the column-row pairs are sampled based on the probability distribution given in Equation 4. Did you try this original probability distribution instead of uniform sampling and top-k sampling? It's better to add it as a comparison baseline.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes StructDrop, a straightforward strategy that uniformly samples column-row pairs to optimize sparse matrix multiplication for accelerating graph training. They integrate the proposed strategy with the existing classic graph neural network (i.e., GCN and GraphSAGE) in both forward and backward passes. Experimental results show that the proposed approach achieves significant speedup in graph training compared to the vanilla baseline.

### Strengths
1. The proposed approach is simple and easy to follow. Experimental results show its effectiveness in accelerating graph training.
2. The paper is easy to read and generally well-written.

### Weaknesses
1. The theoretical foundation is insufficient. The proposed method appears naive and relies more on observation and intuition. Specifically, the paper lacks a rigorous analysis of why uniformly sampling column-row pairs leads to an unbiased estimate of the full matrix multiplication. The authors should provide a formal proof or at least a detailed argument showing that the expected value of the result from StructDrop is equal to the result of the full matrix multiplication. Furthermore, the paper does not discuss the variance introduced by the sampling process and how this variance affects the convergence and stability of the training process.
2. Experiments are insufficient. StructDrop only integrates with GCN and GraphSAGE. More classic models, such as GAT [1], and state-of-the-art models on large-scale graph data, like GraphSAINT [2], GCNII [3], Cluster-GCN[4], etc., should be included for comparison. The current experiments do not fully demonstrate the generalizability of the proposed approach to different graph neural network architectures and training paradigms. The lack of experiments on models specifically designed for large-scale graphs is a major limitation, as the benefits of StructDrop might be more pronounced in such scenarios.


### Questions
1. The proposed approach primarily relies on observation and intuition. More theoretical evidence is needed to explain why the proposed method is unbiased, how it ensures training accuracy, and its error boundaries.

2. The Top-k sampling method only accelerates the backward process, and the maximum speedup is limited to 2x. However, from Table 2 we can see the acceleration effect of Top-k sampling far exceeds that of StructDrop. Please explain the reasons.

3. It is insufficient to demonstrate the effectiveness of the proposed approach by only applying StructDrop to GCN and GraphSAGE. It would be helpful to integrate StructDrop with more classical GNN models, such as GAT [1].

[1] Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. Graph attention networks. arXiv preprint arXiv:1710.10903, 2017.

4. Both GCN and GraphSAGE do not perform well on large-scale data. Many GNN-related approaches have demonstrated better results and faster training speed on large graphs, such as GraphSAINT [2], GCNII [3], Cluster-GCN[4], etc. It would be beneficial to apply the proposed approach on these models for comparison.

[2] Zeng, H., Zhou, H., Srivastava, A., Kannan, R., and Prasanna, V. Graphsaint: Graph sampling based inductive learning method. In International Conference on Learning Representations, 2020. 
[3] Chen, M., Wei, Z., Huang, Z., Ding, B., and Li, Y. Simple and deep graph convolutional networks. International Conference on Machine Learning, 2020. [4] Chiang, W. L., Liu, X., Si, S., Li, Y., Bengio, S., & Hsieh, C. J. Cluster-gcn: An efficient algorithm for training deep and large graph convolutional networks. In Proceedings of the 25th ACM SIGKDD International Conference on knowledge discovery & data mining, 2019

5. In Table 7, why does the accuracy decrease as the sample ratios increase in the ogbn-Products dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes StructDrop to speed up the sparse and fast matrix multiplication during the training of GNNs. The authors point out two main limitations in the previous works: the inefficiency issue and the under-fitting problem. To this end, they propose uniform sampling and instance normalization to address these problems. Experiments show that the proposed StructDrop achieves considerable speedup for sparse operations and end-to-end GNN with less to no or even better accuracy.

### Strengths
1. The authors observe the under-fitting problem from the previous column-row pairs selection and employ a uniform sampling to solve this problem to make the trained GNN models more generalizable and speed up the computation by setting the sample ratio.
2. To address the accuracy degradation problem from the fast matrix multiplication with sampling, this paper proposes an instance normalization to recover the accuracy for different graph model architectures.
3. The experiments, especially the ablation studies are well done and the paper is easy to follow.

### Weaknesses
1. In Table 4, without applying the instance normalization, the accuracy of GCN has a big difference between the max and min values, does this mean the convergence is not yet complete? The large variance in accuracy, specifically the range between the maximum and minimum values observed across multiple runs, suggests that the training process without instance normalization may be unstable. This raises concerns about the reliability of the reported results and whether the model has truly converged to a stable solution. It's possible that the model is oscillating within a range of suboptimal solutions, rather than settling into a consistent minimum. Further investigation into the training dynamics, such as plotting learning curves, would be beneficial to confirm convergence.
2. According to Table 2, for ogbn-Arxiv dataset, the DropEdge seems slower than vanilla algorithm, which means different datasets would achieve different speedups since their distribution, do you have any ideas about improving the sampling algorithm for specific datasets from their features? The observation that DropEdge is slower than the vanilla algorithm on the ogbn-Arxiv dataset highlights a potential limitation of the proposed uniform sampling strategy. The performance variation across different datasets suggests that the sampling method might not be universally optimal and could be sensitive to the specific characteristics of the graph structure and data distribution. It raises the question of whether a more adaptive sampling strategy, tailored to the unique features of each dataset, could lead to more consistent and improved speedups.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a sampling mechanism for Graph Neural Networks (GNN) to improve its efficiency on commodity accelerators. The GNN training for large graphs is inefficient due to the requirement for two sparse matrix multiplications in the forward and backward passes of the gradient descent. The authors made an observation that sampling the row-column pairs of the adjacency matrix using their norms (as suggested by previous works since they provide the most accurate numerical approximation) leads to an under-fitting problem. The authors instead suggest sampling the row-column pairs uniformly and using instance normalization to stabilize the training. The experimental results and comparison with previous work show promising results for efficiency gains while retaining similar accuracy as the original GNN.

### Strengths
- The idea of structured sampling is simple and yet results in large performance gains with limited to none accuracy loss. 
- The paper is well written and organized and can be followed easily by non-experts. 
- The related literature has been sufficiently reviewed and nicely categorized.
- The authors provided sufficient ablation study on the effect of the instance normalization and dropping ratio.
- The authors have motivated the problem very well in the Introduction Section with examples.

### Weaknesses
 - It was not clear why the authors chose only DropEdeg from the previous works on random dropout for GNN to compare with. It would’ve been better if they could compare StructDrop with more methods, especially the more recent ones like Grand [Feng et al. 2020b] and DropNode [Feng et al. 2020a].

 - It would have been beneficial to see a comparison with methods that perform sampling on the node embeddings themselves, in addition to the adjacency matrix. This is particularly relevant given that the authors introduce instance normalization, which operates on the node embeddings. Without this comparison, it's difficult to fully assess whether the performance gains are solely attributable to the structured sampling of the adjacency matrix or if the normalization plays a significant role.

 - The paper lacks a discussion on the potential limitations of the proposed method in scenarios with highly heterophilous graphs, where node connections are not indicative of node similarity. Uniform sampling may not be optimal in such scenarios, and it would be valuable to acknowledge this limitation.

### Questions
- It would be better if the authors could mention similar sampling methods like DropEdge in the introduction and explain the differences between the proposed method and them.
- It was not mentioned in the text that what numbers are reposted in Table 1, for example, are they the test accuracy?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
