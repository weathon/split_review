### Summary

The authors propose a new method for dataset condensation, aiming to preserve the validation-performance rankings of models across different hyperparameters/architectures. The method, called Hyperparameter-Calibrated Dataset Condensation (HCDC), generates a synthetic validation dataset by matching the hyperparameter gradients computed via implicit differentiation and efficient inverse Hessian approximation. The authors demonstrate that HCDC effectively maintains the validation-performance rankings of models and speeds up hyperparameter/architecture search for tasks on both images and graphs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to dataset condensation that focuses on preserving the validation-performance rankings of models across different hyperparameters/architectures. This is a significant contribution to the field of hyperparameter optimization and dataset condensation.

2. The authors provide a thorough theoretical analysis of the proposed method, including the equivalence between hypergradient alignment and hyperparameter calibration. This analysis strengthens the credibility of the proposed method.

3. The experimental results are comprehensive and demonstrate the effectiveness of HCDC in maintaining the validation-performance rankings of models and speeding up hyperparameter/architecture search for tasks on both images and graphs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method. For example, how does the method perform when the hyperparameter space is very large or when the relationship between hyperparameters and performance is highly non-linear? The current discussion does not adequately address the potential for the method to fail in these scenarios, which are common in practice. Specifically, the paper should explore the sensitivity of the method to the number of hyperparameters and the complexity of the performance landscape. It would be beneficial to see experiments on datasets with a larger number of hyperparameters and more complex relationships to understand the practical limitations of the approach.

2. The paper could provide more details on the computational cost of the proposed method. How does the computational cost of HCDC compare to other dataset condensation methods? The paper should include a detailed analysis of the time and memory requirements of the proposed method, especially in comparison to existing techniques. This analysis should consider the cost of computing hypergradients and the inverse Hessian approximation, which are key components of the method. A comparison with other dataset condensation methods, including both training time and memory usage, would be valuable for assessing the practical applicability of the proposed method.

### Suggestions

The paper should include a more thorough investigation into the limitations of the proposed method, particularly concerning the size and complexity of the hyperparameter space. The authors should conduct experiments on datasets with a larger number of hyperparameters and more complex relationships between hyperparameters and performance. This could involve using benchmark datasets specifically designed for hyperparameter optimization, which often exhibit these challenging characteristics. Furthermore, the authors should analyze the sensitivity of the method to the number of hyperparameters and the non-linearity of the performance landscape. This analysis should include a discussion of the potential failure modes of the method and how these limitations might be addressed in future work. For example, the authors could explore the use of adaptive sampling techniques or more sophisticated optimization algorithms to improve the robustness of the method in challenging scenarios.

To address the computational cost concerns, the authors should provide a detailed analysis of the time and memory requirements of the proposed method. This analysis should include a breakdown of the computational cost of each step of the algorithm, such as the computation of hypergradients and the inverse Hessian approximation. The authors should also compare the computational cost of HCDC with other dataset condensation methods, including both training time and memory usage. This comparison should be performed on a range of datasets and hyperparameter settings to provide a comprehensive understanding of the practical applicability of the proposed method. The authors should also discuss potential optimizations to reduce the computational cost of the method, such as using more efficient approximation techniques or parallelizing the computations.

Finally, the authors should provide a more detailed discussion of the practical implications of the proposed method. This should include a discussion of the potential benefits and drawbacks of using HCDC in real-world applications. The authors should also discuss the potential for the method to be used in conjunction with other hyperparameter optimization techniques, such as Bayesian optimization or reinforcement learning. This discussion should be grounded in practical examples and should provide guidance to practitioners on how to effectively use the proposed method in their own work. The authors should also discuss the potential for the method to be extended to other types of data and tasks, such as natural language processing or time series analysis.

### Questions

1. How does the proposed method perform when the hyperparameter space is very large or when the relationship between hyperparameters and performance is highly non-linear?

2. How does the computational cost of HCDC compare to other dataset condensation methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
