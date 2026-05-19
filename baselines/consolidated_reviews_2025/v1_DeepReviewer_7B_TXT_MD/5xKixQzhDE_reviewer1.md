### Summary

This paper addresses the challenge of efficiently performing hyperparameter optimization (HPO) and neural architecture search (NAS) within the constraints of a condensed dataset. Traditional dataset condensation methods, while effective for accelerating training, often fail to maintain the performance rankings of models when applied to HPO and NAS tasks. The authors propose a novel approach called Hyperparameter-Calibrated Dataset Condensation (HCDC), which synthesizes a condensed dataset by aligning the hypergradient of models trained on the condensed and original datasets. This alignment ensures that the relative performance rankings of different hyperparameters and architectures are preserved, leading to significant speedups in HPO and NAS without compromising solution quality. The paper demonstrates the effectiveness of HCDC through experiments on image and graph datasets, showing substantial reductions in search time and improved performance compared to existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to dataset condensation specifically tailored for HPO and NAS tasks, addressing a critical gap in the existing literature.
2. The authors provide a solid theoretical foundation for their method, with a clear explanation of how hypergradient alignment preserves performance rankings.
3. The paper is well-organized and clearly written, making it accessible to a broad audience.
4. The empirical results are compelling, demonstrating significant improvements in search time and performance compared to existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the computational overhead associated with calculating hypergradients, especially in high-dimensional hyperparameter spaces. While the authors mention the use of implicit differentiation, a more in-depth analysis of the computational complexity and potential bottlenecks would be valuable. Specifically, the paper should address how the cost of computing the hypergradient scales with the size of the model, the number of training iterations, and the dimensionality of the hyperparameter space. Furthermore, the practical implications of this overhead, such as the time required to compute the hypergradient for different datasets and models, should be discussed.
2. The paper could include a more comprehensive comparison with other dataset condensation techniques, particularly those that also aim to preserve performance. A more detailed analysis of the trade-offs between performance preservation and computational efficiency would be beneficial. The comparison should not only focus on the final performance but also on the computational cost of each method, including the time required for dataset condensation and the time required for hyperparameter optimization on the condensed dataset. This would provide a more complete picture of the advantages and disadvantages of the proposed method compared to existing techniques.
3. The paper could explore the sensitivity of the proposed method to different hyperparameters of the dataset condensation process, such as the number of samples used to represent each data point. A sensitivity analysis would help to understand the robustness of the method and provide guidance on how to choose the optimal hyperparameters for different tasks. For example, the paper should investigate how the performance of the method changes when the number of condensed samples is varied, and whether there is a trade-off between the number of samples and the computational cost.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with calculating hypergradients. This analysis should go beyond a simple mention of implicit differentiation and should delve into the specific computational bottlenecks. For instance, the paper could discuss the number of forward and backward passes required to compute the hypergradient, and how this scales with the size of the model, the number of training iterations, and the dimensionality of the hyperparameter space. Furthermore, the authors should provide empirical results on the actual time required to compute the hypergradient for different datasets and models. This would give a more concrete understanding of the practical computational overhead of the proposed method. It would also be beneficial to compare the computational cost of the proposed method with other dataset condensation techniques, including those that do not explicitly focus on hyperparameter optimization. This would help to contextualize the computational trade-offs of the proposed method and highlight its advantages and disadvantages compared to existing approaches.

To strengthen the paper, the authors should include a more comprehensive comparison with other dataset condensation techniques, particularly those that also aim to preserve performance. This comparison should not only focus on the final performance but also on the computational cost of each method, including the time required for dataset condensation and the time required for hyperparameter optimization on the condensed dataset. The authors should consider including a wider range of dataset condensation techniques in their comparison, including both gradient-based and gradient-free methods. This would provide a more complete picture of the advantages and disadvantages of the proposed method compared to existing techniques. The comparison should also discuss the trade-offs between performance preservation and computational efficiency, and how the proposed method balances these trade-offs compared to other methods. This would help to better position the proposed method within the existing literature and highlight its unique contributions.

Finally, the paper should include a sensitivity analysis of the proposed method to different hyperparameters of the dataset condensation process. This analysis should investigate how the performance of the method changes when the number of condensed samples is varied, and whether there is a trade-off between the number of samples and the computational cost. The authors should also discuss how the choice of hyperparameters for the dataset condensation process affects the performance of the method. For example, the paper could investigate the impact of different choices of the implicit differentiation method on the performance of the method. This would provide a more complete understanding of the robustness of the method and provide guidance on how to choose the optimal hyperparameters for different tasks. This analysis should also consider the impact of other hyperparameters, such as the learning rate and the batch size, on the performance of the method.

### Questions

See above.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
