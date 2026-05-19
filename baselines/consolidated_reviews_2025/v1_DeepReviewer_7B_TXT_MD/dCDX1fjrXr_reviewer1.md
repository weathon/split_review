### Summary

This paper studies the sparse node classification problem. The authors propose a framework to enhance the performance of GNNs in this task. The framework includes four steps: 1) label distribution estimation, 2) key nodes selection, 3) label distribution incorporation, and 4) optimization. The authors conduct experiments on several datasets and demonstrate the effectiveness of their proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct experiments on several datasets and demonstrate the effectiveness of their proposed method.

### Weaknesses

#### Some Related Works

[1] Graph random neural networks for semi-supervised learning on graphs.
[2] Graph-less neural networks.
[3] Graph-less gnn: Learning effective and efficient 100-layers deep gnns on a single hardware accelerator.
[4] Graph neural networks with learnable structural and positional representation.
[5] Graph neural networks with learnable structural and position representation.
[6] Graph neural networks with structural and positional representation learning.
[7] Dropedge: Towards deep graph convolutional networks on node classification.
[8] Dropedge: Towards removing noisy edges for graph neural networks training.
[9] Dropmessage: Unifying random dropping for graph neural networks.
[10] Graph contrastive learning with augmentations.
[11] Graph contrastive learning with adaptive augmentations.
[12] Graph structure learning with self-supervised graph neural networks.

#### comment

1. The novelty of this paper is limited. The proposed framework is similar to the existing methods [1-3]. The authors should discuss the differences between their proposed method and these existing methods. Specifically, the label distribution estimation step, while presented as a key contribution, appears to be a straightforward adaptation of existing techniques for estimating pseudo-labels in semi-supervised learning. The paper lacks a detailed comparison of the specific implementation choices and their impact compared to prior work, making it difficult to assess the true novelty of this component. Furthermore, the key node selection process, which relies on a clustering-based approach, also seems to be a common practice in graph-based learning, and the paper does not sufficiently justify its novelty in this context.

2. The authors claim that the proposed method can enhance the performance of GNNs in the SLNC task. However, the experimental results do not support this claim. The authors only compare their method with the original GNNs, and the performance improvement is marginal. The authors should compare their method with more advanced GNNs, such as GPRGNN [4] and GPSGNN [5], which have demonstrated superior performance on graph datasets. The lack of comparison with state-of-the-art GNN models makes it difficult to evaluate the practical significance of the proposed method. Additionally, the authors should provide a more detailed analysis of the performance gains, including statistical significance tests and ablation studies to understand the contribution of each component of the framework.

3. The authors should conduct experiments on more datasets. The datasets used in the experiments are relatively small, and the authors should consider using larger datasets to evaluate the scalability of their method. The current experiments do not provide sufficient evidence to demonstrate the generalizability of the proposed method to larger and more complex graphs.

4. The authors should compare their method with the existing methods in the literature. The paper lacks a comprehensive comparison with relevant methods, making it difficult to assess the relative performance of the proposed approach. The authors should include a more thorough literature review and compare their method with a wider range of state-of-the-art techniques, including both semi-supervised and self-supervised learning methods.

5. The authors should provide more details on the experimental settings. The paper lacks sufficient details on the hyperparameter settings, the training procedures, and the computational resources used. This makes it difficult to reproduce the results and to assess the validity of the experimental evaluation.

### Suggestions

The authors should provide a more detailed explanation of the novelty of their proposed framework, particularly in comparison to existing methods for label distribution estimation and key node selection. A thorough analysis of the differences in implementation and performance compared to prior work is needed to justify the claims of novelty. Specifically, the authors should discuss how their approach differs from existing pseudo-labeling techniques, such as those used in consistency regularization or graph-based methods, and provide a clear rationale for their design choices. Furthermore, the authors should clarify the specific advantages of their clustering-based key node selection approach compared to other node selection strategies, such as random selection or centrality-based methods. A more detailed discussion of the theoretical underpinnings of their approach, including convergence properties and error bounds, would also be beneficial.

To strengthen the experimental evaluation, the authors should compare their method with more advanced GNN baselines, such as GPRGNN [4] and GPSGNN [5], which have demonstrated superior performance on graph datasets. The authors should also conduct a more comprehensive ablation study to understand the contribution of each component of their framework, including the label distribution estimation, key node selection, and label distribution incorporation steps. This would help to identify the key factors that contribute to the performance gains and to provide a more detailed analysis of the method's effectiveness. Additionally, the authors should provide a more detailed analysis of the performance gains, including statistical significance tests and error bars, to demonstrate the robustness of their results. The authors should also consider using a wider range of evaluation metrics, such as F1-score or AUC, to provide a more comprehensive assessment of the method's performance.

Finally, the authors should conduct experiments on larger and more diverse datasets to evaluate the scalability and generalizability of their method. The current experiments are limited to relatively small datasets, which may not be representative of real-world applications. The authors should also provide more details on the experimental settings, including the hyperparameter settings, the training procedures, and the computational resources used. This would make it easier for other researchers to reproduce their results and to assess the validity of their experimental evaluation. The authors should also consider releasing their code and datasets to the community to facilitate further research in this area.

### Questions

1. What is the difference between the proposed framework and the existing methods?
2. How does the proposed framework perform on larger datasets?
3. How does the proposed framework perform compared to the existing methods?

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
