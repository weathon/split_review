### Summary

The paper proposes a graph-based framework for joint OOD generalization and detection. The proposed framework is based on a contrastive loss that can be derived from the spectral decomposition of the graph's adjacency matrix. The authors provide theoretical analysis of the proposed loss function and its relation to the graph's spectral decomposition. The authors also provide empirical results on CIFAR-10 and other datasets, showing that the proposed method can outperform existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a novel perspective on OOD generalization and detection by formulating it as a graph-based problem.
3. The authors provide theoretical analysis of the proposed loss function and its relation to the graph's spectral decomposition.
4. The empirical results show that the proposed method can outperform existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed discussion of the limitations of the proposed method.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method.
3. The paper does not provide a detailed discussion of the hyperparameters of the proposed method and their impact on the performance.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed graph-based framework for OOD generalization and detection. Specifically, the authors should address scenarios where the graph structure might not accurately capture the underlying relationships between data points, or where the spectral decomposition might be sensitive to noise or outliers in the graph. For instance, if the graph is constructed based on a similarity metric, the choice of this metric and its parameters could significantly impact the performance of the method. A discussion of how the method behaves when the similarity metric is not appropriate for the data would be valuable. Furthermore, the authors should consider the potential for the graph to become too dense or too sparse, and how this might affect the spectral decomposition and the overall performance of the method. It would be beneficial to include experiments that specifically test the robustness of the method to different graph construction parameters and similarity metrics.

In addition to the limitations, the paper should include a more detailed analysis of the computational complexity of the proposed method. The authors should provide a breakdown of the time and space complexity of each step in the algorithm, including the graph construction, the spectral decomposition, and the contrastive learning process. This analysis should consider the impact of the number of nodes and edges in the graph, as well as the dimensionality of the data. It would be helpful to compare the computational complexity of the proposed method with existing methods for OOD generalization and detection. Furthermore, the authors should discuss the practical implications of the computational complexity, such as the scalability of the method to large datasets. The authors should also discuss the memory requirements of the method, and how it can be optimized for large datasets.

Finally, the paper needs a more detailed discussion of the hyperparameters of the proposed method and their impact on the performance. The authors should provide a sensitivity analysis of the key hyperparameters, such as the temperature parameter in the contrastive loss, the number of top eigenvectors used in the spectral decomposition, and the learning rate. The authors should also discuss how these hyperparameters should be tuned for different datasets and tasks. It would be beneficial to include a table or figure that shows the performance of the method as a function of these hyperparameters. The authors should also discuss the potential for using automated hyperparameter tuning methods, such as grid search or Bayesian optimization, to improve the performance of the method. A more thorough discussion of the hyperparameter selection process would make the method more practical and easier to use.

### Questions

1. How does the proposed method handle the case where the graph structure is not informative or is noisy?
2. How does the proposed method scale to large datasets?
3. How sensitive is the proposed method to the choice of hyperparameters?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
