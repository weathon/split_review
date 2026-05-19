### Summary

This paper studies data selection for LLMs. The key idea is to select data that nudges the pre-training distribution closer to the target distribution. The authors show the optimality of this approach for fine-tuning tasks under certain conditions. The authors demonstrate the effectiveness of the proposed method on several datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The studied problem is important. 
- The paper is well-written.

### Weaknesses

#### Some Related Works

[1] Data selection for neural networks through importance resampling.
[2] Data selection for language models via importance resampling.

#### comment

My main concern is about the novelty. The proposed method is quite similar to some existing methods (e.g.,  Pham et al. (2020), Everaert et al. (2023)). In Everaert et al. (2023), the authors propose to minimize the Gromov-Wasserstein distance, which is also a discrepancy measure. In Pham et al. (2020), the authors propose to minimize the optimal transport cost. In these works, the authors also use the gradient of the discrepancy measure to select data. The main difference is that the authors use the optimal transport, and the previous work uses the Gromov-Wasserstein distance. The difference between these two discrepancy measures is not clear to me. Can the authors provide some comparisons between these two discrepancy measures? Why is the proposed method better than the previous methods?

### Suggestions

The paper would benefit from a more detailed explanation of the differences between the proposed method and existing approaches, particularly those using Gromov-Wasserstein distance and optimal transport for data selection. While the authors mention using optimal transport, they do not fully elaborate on how their specific application of it differs from prior work that also uses optimal transport costs for data selection. A more thorough discussion is needed to clarify the unique aspects of their approach. For example, it would be helpful to understand if the difference lies in the specific formulation of the optimal transport problem, the choice of cost function, or the way the gradient is used for data selection. Furthermore, a more detailed comparison with the Gromov-Wasserstein distance is needed. The authors should discuss the theoretical properties of each distance metric and explain why optimal transport is more suitable for the task of data selection in the context of fine-tuning large language models. This discussion should include specific examples of scenarios where one metric might be preferred over the other, and provide a clear rationale for the choice of optimal transport in this work.

To strengthen the paper, the authors should provide a more detailed analysis of the practical implications of using optimal transport versus Gromov-Wasserstein distance. This analysis should go beyond theoretical considerations and include empirical evidence demonstrating the advantages of their approach. For instance, the authors could compare the performance of their method with a baseline that uses Gromov-Wasserstein distance on the same datasets. This would provide a more concrete understanding of the practical benefits of their approach. Additionally, the authors should discuss the computational complexity of their method compared to existing approaches. This discussion should include an analysis of the time and memory requirements of their method, and how these scale with the size of the dataset and the number of samples selected. This would help to understand the practical applicability of the proposed method in real-world scenarios.

Finally, the authors should provide a more detailed explanation of how the gradient of the optimal transport cost is used for data selection. It is not clear how the gradient is computed and how it is used to rank the data points. A more detailed explanation of the algorithm is needed, including a step-by-step description of the data selection process. The authors should also discuss any hyperparameters involved in the data selection process and how they are chosen. This would help to make the method more reproducible and easier to understand. Furthermore, the authors should provide a more detailed analysis of the sensitivity of their method to different choices of hyperparameters. This analysis should include a discussion of how the performance of the method varies with different choices of hyperparameters, and how these choices can be optimized for different datasets.

### Questions

Please see the weakness section.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
