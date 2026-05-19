### Summary

The paper proposes Newton Losses, a method for improving the performance of existing hard to optimize losses by exploiting their second-order information via their empirical Fisher and Hessian matrices. The method only utilizes the loss function's second-order information to replace it by a Newton Loss, while training the network with gradient descent. The authors apply Newton Losses to eight differentiable algorithms for sorting and shortest-paths, achieving significant improvements for less-optimized differentiable algorithms, and consistent improvements, even for well-optimized differentiable algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to improving the performance of hard-to-optimize losses by utilizing second-order information from the loss function. This is a significant contribution to the field of differentiable algorithms.

2. The authors provide a clear and detailed explanation of the proposed method, including the mathematical formulation and implementation details. This makes the paper easy to follow and understand.

3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method across a range of differentiable algorithms and tasks. The authors also provide a thorough analysis of the results, including ablation studies and comparisons with baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the application of Newton Losses to differentiable algorithms for sorting and shortest-paths. It would be interesting to see how the method performs on other types of differentiable algorithms and tasks. Specifically, the method's applicability to algorithms with non-convex loss landscapes, or those with high-dimensional input spaces, is not explored. This limits the generalizability of the findings.

2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to understand how the method scales with the size of the input data and the complexity of the neural network. The computational overhead of calculating the Hessian and Fisher information matrix, especially for large models, is not addressed, which is a critical factor for practical applications.

3. The paper does not discuss the potential limitations of the proposed method. For example, it would be useful to know under what conditions the method might not be effective or might even degrade performance. The paper lacks a discussion on the sensitivity of the method to hyperparameter choices, such as the learning rate and the damping parameter used in the Newton update, and how these might interact with the curvature information.

### Suggestions

The paper introduces an interesting approach by leveraging second-order information to improve the optimization of differentiable algorithms. However, the evaluation is limited to sorting and shortest-path algorithms. To strengthen the paper, the authors should explore the performance of Newton Losses on a broader range of differentiable algorithms, particularly those with more complex loss landscapes and higher-dimensional inputs. For example, algorithms used in reinforcement learning or generative modeling, which often exhibit non-convexity and high dimensionality, would be valuable test cases. This would provide a more comprehensive understanding of the method's applicability and limitations. Furthermore, the authors should investigate the sensitivity of the method to different initialization strategies and optimization hyperparameters, as these can significantly impact the performance of second-order methods.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and memory requirements of the proposed method. This should include the cost of computing the Hessian and Fisher information matrix, as well as the cost of the Newton update step. The analysis should consider the scalability of the method with respect to the size of the input data and the number of parameters in the neural network. It would be beneficial to compare the computational cost of Newton Losses with that of standard gradient-based optimization methods. Additionally, the authors should explore techniques to reduce the computational overhead, such as using approximations of the Hessian or Fisher matrix, or employing more efficient algorithms for matrix inversion. This would make the method more practical for large-scale applications.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. This should include a discussion of the conditions under which the method might not be effective or might even degrade performance. For example, the authors should investigate the behavior of the method when the loss function is highly non-convex or when the Hessian matrix is ill-conditioned. The paper should also discuss the sensitivity of the method to the choice of hyperparameters, such as the learning rate and the damping parameter used in the Newton update. A more detailed analysis of these limitations would provide a more complete understanding of the method and its practical applicability.

### Questions

1. How does the performance of Newton Losses compare to other state-of-the-art optimization methods for differentiable algorithms?

2. How does the computational cost of Newton Losses compare to other optimization methods for differentiable algorithms?

3. Are there any limitations or potential drawbacks to using Newton Losses for differentiable algorithms?

### Rating

6

### Confidence

3

**********
