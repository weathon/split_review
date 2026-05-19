### Summary

This paper proposes LabelDP-Pro, a label differential private algorithm based on DP-SGD. The main idea is to project the gradient onto the convex hull of the gradients of the batch of the samples. This is done by solving a minimization problem using the coefficients smoothing technique. The authors provide a theoretical analysis of the algorithm and show that it is better than the randomized response algorithm in the high privacy regime. The authors also provide experiments on various datasets and show that their algorithm outperforms previous algorithms in the high privacy regime.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well written and easy to follow.
- The proposed algorithm is novel and interesting.
- The experiments are comprehensive and show the effectiveness of the algorithm.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed discussion on the computational complexity of the proposed algorithm. The projection step, while described as efficient, involves solving a minimization problem, and it's unclear how this scales with the size of the dataset, the number of classes, and the dimensionality of the gradients. A more thorough analysis of the time and space complexity is needed to assess the practical applicability of the method, especially for large-scale datasets.
- The experimental section, while comprehensive, could benefit from a more in-depth analysis of the results. For instance, it would be helpful to see a breakdown of the performance gains across different datasets and privacy parameters, and a discussion of the trade-offs between privacy and accuracy. The current analysis lacks a detailed exploration of why the proposed method outperforms the baselines in certain regimes and underperforms in others. It would be beneficial to understand the factors that contribute to these performance variations.

### Suggestions

The paper would significantly benefit from a more rigorous analysis of the computational complexity of the proposed LabelDP-Pro algorithm. While the authors claim the projection step is efficient, a detailed breakdown of the time complexity with respect to the number of samples (n), the number of classes (K), and the dimensionality of the gradients (d) is necessary. Specifically, the authors should provide a clear explanation of how the minimization problem in the projection step is solved, including the specific optimization algorithm used and its convergence properties. Furthermore, it would be valuable to discuss the memory requirements of the algorithm, especially when dealing with large datasets. A comparison of the computational cost of LabelDP-Pro with that of DP-SGD and other label differential privacy algorithms would also be beneficial. This analysis should include both theoretical bounds and empirical measurements of runtime and memory usage on different datasets.

To strengthen the experimental section, the authors should provide a more granular analysis of the results. This should include a breakdown of the performance gains across different datasets and privacy parameters, highlighting the specific scenarios where LabelDP-Pro excels or underperforms. For example, it would be useful to analyze the performance of the algorithm on datasets with varying levels of label noise or different class distributions. The authors should also investigate the impact of different hyperparameters on the performance of the algorithm and provide guidelines for selecting appropriate values. Furthermore, a more detailed discussion of the trade-offs between privacy and accuracy is needed. The authors should explore the relationship between the privacy parameter (epsilon) and the resulting accuracy, and explain why the proposed method performs better than baselines in certain regimes and underperforms in others. This analysis should include a discussion of the factors that contribute to these performance variations, such as the dataset characteristics, the model architecture, and the choice of hyperparameters.

Finally, the authors should consider including a more detailed discussion of the limitations of the proposed method. While the paper focuses on the high-privacy regime, it would be beneficial to acknowledge the potential challenges of applying LabelDP-Pro in scenarios with very low privacy budgets. The authors should also discuss the sensitivity of the algorithm to the choice of the projection set and provide guidance on how to select an appropriate set for different datasets. Furthermore, the authors should explore the potential for extending the proposed method to other types of models and loss functions. This would help to establish the generality and applicability of the proposed approach. A more thorough discussion of these limitations and potential extensions would significantly enhance the paper's overall impact.

### Questions

- How does the computational complexity of the proposed algorithm compare to that of DP-SGD and other label differential privacy algorithms?
- What are the limitations of the proposed algorithm, and how can it be extended to other types of models and loss functions?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
