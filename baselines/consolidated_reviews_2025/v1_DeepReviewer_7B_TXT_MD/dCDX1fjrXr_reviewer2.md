### Summary

This paper proposes a new framework to solve the sparse labels node classification problem. The framework includes four steps: (1) label distribution estimation, (2) key nodes selection as labeled nodes, (3) label distribution incorporation in sparse labels classification, and (4) optimize and generalize the proposed framework. Experiments on several datasets show that the proposed framework can enhance the performance of GNNs in the SLNC task.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-organized and easy to follow.
2. The paper proposes a new framework to solve the sparse labels node classification problem.
3. Experiments on several datasets show that the proposed framework can enhance the performance of GNNs in the SLNC task.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The proposed framework is similar to the existing methods [1-3]. The authors should discuss the differences between their proposed method and these existing methods. Specifically, the label distribution estimation step, while presented as a key contribution, appears to be a straightforward adaptation of existing techniques for estimating pseudo-labels in semi-supervised learning. The paper lacks a detailed comparison of the specific implementation choices and their impact compared to prior work, making it difficult to assess the true novelty of this component. Furthermore, the key node selection process, which relies on a clustering-based approach, also seems to be a common practice in graph-based learning, and the paper does not sufficiently justify its novelty in this context.
2. The authors claim that the proposed method can enhance the performance of GNNs in the SLNC task. However, the experimental results do not support this claim. The authors only compare their method with the original GNNs, and the performance improvement is marginal. The authors should compare their method with more advanced GNNs, such as GPRGNN [4] and GPSGNN [5], which have demonstrated superior performance on graph datasets. The lack of comparison with state-of-the-art GNN models makes it difficult to evaluate the practical significance of the proposed method. Additionally, the authors should provide a more detailed analysis of the performance gains, including statistical significance tests and ablation studies to understand the contribution of each component of the framework.
3. The authors should conduct experiments on more datasets. The datasets used in the experiments are relatively small, and the authors should consider using larger datasets to evaluate the scalability of their method. The current experiments do not provide sufficient evidence to demonstrate the generalizability of the proposed method to larger and more complex graphs.

### Suggestions

The paper needs a more thorough justification of its novelty, particularly in the label distribution estimation and key node selection steps. The authors should provide a detailed comparison of their approach with existing methods, highlighting the specific differences in implementation and their impact on performance. For example, they could analyze the computational complexity of their label distribution estimation compared to methods that rely on iterative refinement or other pseudo-labeling techniques. Similarly, they should justify the choice of clustering algorithm for key node selection, explaining why it is more suitable than other node selection strategies, such as centrality-based methods or random selection. A more rigorous analysis of the novelty is crucial for establishing the contribution of this work.

To address the lack of experimental validation, the authors should include comparisons with state-of-the-art GNN models, such as GPRGNN and GPSGNN, which have demonstrated superior performance on graph datasets. The current comparison with only the original GNNs is insufficient to demonstrate the practical significance of the proposed method. Furthermore, the authors should provide a more detailed analysis of the performance gains, including statistical significance tests and ablation studies to understand the contribution of each component of the framework. For instance, they could analyze the impact of each step in the proposed framework on the final performance, such as the label distribution estimation, key node selection, and label distribution incorporation. This would help to identify the key factors that contribute to the performance improvement and provide a more comprehensive understanding of the method's effectiveness.

Finally, the authors should conduct experiments on larger and more diverse datasets to evaluate the scalability and generalizability of their method. The current experiments are limited to relatively small datasets, which may not be representative of real-world applications. The authors should consider using larger graph datasets with varying characteristics to assess the robustness of their approach. This would provide a more comprehensive evaluation of the proposed method and demonstrate its applicability to a wider range of scenarios. Additionally, the authors should provide more details on the experimental settings, including the hyperparameter settings, the training procedures, and the computational resources used. This would make it easier for other researchers to reproduce their results and to assess the validity of their experimental evaluation.

### Questions

See Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
