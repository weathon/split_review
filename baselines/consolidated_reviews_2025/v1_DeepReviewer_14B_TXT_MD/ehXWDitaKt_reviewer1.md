### Summary

The paper proposes Newton Losses to improve the performance of hard to optimize losses by exploiting their second-order information via their empirical Fisher and Hessian matrices. The proposed method is computationally efficient and achieves significant improvements for less-optimized differentiable algorithms, and consistent improvements, even for well-optimized differentiable algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a novel method for improving the performance of hard to optimize losses by exploiting their second-order information via their empirical Fisher and Hessian matrices. 
2. The proposed method is computationally efficient and can be easily implemented on top of existing algorithmic losses.
3. The paper provides a theoretical analysis of the proposed method, showing that it is equivalent to a single Newton step.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only evaluates the proposed method on a limited number of differentiable algorithms and benchmarks. It would be beneficial to see how it performs on a wider range of problems and datasets. Specifically, the current evaluation focuses on sorting and shortest-path algorithms, which are relatively narrow in scope. It is unclear how the proposed method would generalize to other types of differentiable algorithms, such as those used in reinforcement learning or generative modeling. The lack of diversity in the evaluation makes it difficult to assess the broad applicability of the proposed approach.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to see how the runtime and memory usage scale with the size of the problem and the number of parameters. While the paper mentions computational efficiency, it lacks a rigorous analysis of the computational overhead introduced by the second-order optimization. A detailed breakdown of the time and memory complexity, especially in relation to the number of parameters and the size of the input data, is needed to fully understand the practical implications of the method. This analysis should also consider the cost of computing and inverting the Fisher and Hessian matrices.

### Suggestions

To address the limited evaluation, the authors should consider expanding their experiments to include a more diverse set of differentiable algorithms and benchmarks. This could involve testing the proposed method on problems from different domains, such as image recognition, natural language processing, or reinforcement learning. For example, the authors could evaluate the performance of Newton Losses on a differentiable reinforcement learning algorithm, where the loss function is often non-convex and hard to optimize. This would provide a more comprehensive assessment of the method's generalizability and robustness. Furthermore, the authors should consider including comparisons with other state-of-the-art optimization techniques for these additional problems, to better contextualize the performance gains achieved by Newton Losses. This would help to demonstrate the practical value of the proposed method in a wider range of applications.

Regarding the computational cost, the authors should provide a more detailed analysis of the runtime and memory usage of the proposed method. This analysis should include a breakdown of the time and memory complexity of each step in the algorithm, such as the computation of the gradients, the Fisher and Hessian matrices, and the matrix inversion. The authors should also investigate how the computational cost scales with the size of the problem and the number of parameters. This could involve conducting experiments with varying problem sizes and model complexities, and measuring the corresponding runtime and memory usage. Furthermore, the authors should compare the computational cost of Newton Losses with that of other optimization methods, such as standard gradient descent and other second-order optimization techniques. This would help to quantify the trade-off between performance and computational cost, and to identify the scenarios where Newton Losses is most beneficial.

Finally, the authors should provide more details on the practical implementation of the proposed method. This could include a discussion of the hyperparameter tuning process, and the sensitivity of the method to different hyperparameter settings. The authors should also provide guidelines for choosing the appropriate variant of Newton Losses (Hessian vs. Fisher) for different types of problems. Furthermore, the authors should consider releasing the code for their method, to facilitate reproducibility and further research. This would allow other researchers to easily implement and evaluate Newton Losses on their own problems, and to contribute to the further development of the method.

### Questions

1. How does the performance of Newton Losses compare to other state-of-the-art optimization methods for differentiable algorithms?
2. How does the computational cost of Newton Losses compare to other optimization methods for differentiable algorithms?
3. Are there any limitations or potential drawbacks to using Newton Losses for differentiable algorithms?

### Rating

6

### Confidence

3

**********
