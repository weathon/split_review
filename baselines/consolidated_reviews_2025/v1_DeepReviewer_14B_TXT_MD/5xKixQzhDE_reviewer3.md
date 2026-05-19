### Summary

This paper proposes a novel hyperparameter-calibrated dataset condensation (HCDC) algorithm, which obtains the synthetic validation dataset by matching the hyperparameter gradients computed via implicit differentiation and efficient inverse Hessian approximation. The proposed framework effectively maintains the validation-performance rankings of models and speeds up hyperparameter/architecture search for tasks on both images and graphs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of hyperparameter-calibrated dataset condensation is novel and interesting.
3. The authors provide extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method seems to be limited to the hyperparameter search. It is unclear whether the proposed method can be used for other tasks, such as neural architecture search (NAS). Specifically, the method's reliance on matching hyperparameter gradients raises questions about its applicability to scenarios where the search space is not defined by continuous hyperparameters but rather by discrete architectural choices. The paper does not provide sufficient justification for how the gradient matching objective would translate to the selection of optimal architectures, which often involves non-differentiable choices.
2. The proposed method seems to be computationally expensive. The authors should provide a detailed complexity analysis of the proposed method. The paper lacks a rigorous analysis of the computational cost associated with the implicit differentiation and inverse Hessian approximation steps. It is not clear how the computational overhead scales with the size of the hyperparameter space, the size of the condensed dataset, and the number of training epochs. A detailed breakdown of the time complexity for each step of the algorithm is needed to assess its practical feasibility.

### Suggestions

The authors should provide a more thorough discussion on the limitations of the proposed method, particularly regarding its applicability to neural architecture search (NAS). While the paper focuses on hyperparameter optimization, it is crucial to address the challenges of extending the method to discrete search spaces. The authors could explore potential adaptations of the gradient matching objective to handle non-differentiable choices, such as using surrogate gradients or reinforcement learning techniques. Furthermore, a discussion on the potential limitations of the method when dealing with complex architectural choices, such as those involving skip connections or attention mechanisms, would be beneficial. The paper should also include a more detailed analysis of the method's performance on a wider range of NAS benchmarks to demonstrate its practical utility.

To address the computational concerns, the authors should provide a detailed complexity analysis of the proposed method. This analysis should include a breakdown of the time complexity for each step of the algorithm, including the implicit differentiation, inverse Hessian approximation, and gradient matching steps. The analysis should also consider the impact of various factors, such as the size of the hyperparameter space, the size of the condensed dataset, and the number of training epochs, on the overall computational cost. The authors could also explore potential optimizations to reduce the computational overhead, such as using more efficient approximation techniques or parallelizing the computations. A comparison of the computational cost of the proposed method with existing hyperparameter optimization techniques would also be valuable.

Finally, the authors should provide a more detailed explanation of the experimental setup, including the specific hyperparameters used for the proposed method and the baseline methods. This would allow for a more thorough evaluation of the results and facilitate reproducibility. The paper should also include a more detailed analysis of the results, including a discussion of the statistical significance of the observed differences. The authors could also explore the sensitivity of the method to different choices of hyperparameters and provide guidelines for selecting appropriate values.

### Questions

Please see the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
