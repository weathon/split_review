### Summary

The paper proposes a novel loss function, called Newton Losses, for improving the performance of existing hard to optimize losses. The key idea is to exploit the second-order information of the loss function via its empirical Fisher and Hessian matrices. The authors show that Newton Losses can be used to replace the original loss function by a quadratic with second-order Taylor expansion, which provides a (locally) convex loss leading to better optimization behavior. The authors also propose two variants of Newton Losses: Hessian-based Newton Losses and empirical Fisher matrix-based Newton Losses. The empirical Fisher variant can be easily implemented on top of existing algorithmic losses because it does not require to compute their second derivatives, while the Hessian variant requires computation of second derivatives and leads to greater improvements when available. The authors evaluate Newton Losses for an array of eight families of algorithmic losses on two popular algorithmic benchmarks: the four-digit MNIST sorting benchmark and the Warcraft shortest-path benchmark. The results show that Newton Losses leads to consistent performance improvements for each of the algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a novel loss function, called Newton Losses, for improving the performance of existing hard to optimize losses. The key idea is to exploit the second-order information of the loss function via its empirical Fisher and Hessian matrices. The authors show that Newton Losses can be used to replace the original loss function by a quadratic with second-order Taylor expansion, which provides a (locally) convex loss leading to better optimization behavior. This is a novel and interesting idea that has not been explored before in the literature.
2. The authors propose two variants of Newton Losses: Hessian-based Newton Losses and empirical Fisher matrix-based Newton Losses. The empirical Fisher variant can be easily implemented on top of existing algorithmic losses because it does not require to compute their second derivatives, while the Hessian variant requires computation of second derivatives and leads to greater improvements when available. This provides a flexible and practical approach for differentiable algorithms.
3. The authors evaluate Newton Losses for an array of eight families of algorithmic losses on two popular algorithmic benchmarks: the four-digit MNIST sorting benchmark and the Warcraft shortest-path benchmark. The results show that Newton Losses leads to consistent performance improvements for each of the algorithms. This demonstrates the effectiveness and practical value of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the convergence properties of Newton Losses. It would be helpful to provide some theoretical guarantees on the convergence rate and the optimality of the proposed method. Specifically, it is unclear how the local convexity induced by the second-order approximation affects the global optimization landscape, and whether the method is guaranteed to converge to a local minimum or a saddle point. A more rigorous analysis of the conditions under which the method converges, and the rate of convergence, would be beneficial.
2. The paper does not provide a detailed comparison with other second-order optimization methods, such as quasi-Newton methods or natural gradient methods. It would be helpful to compare the performance of Newton Losses with these methods and discuss the advantages and disadvantages of each approach. For example, how does the performance of Newton Losses compare to methods that approximate the Hessian using finite differences or other techniques? A more thorough comparison would help to contextualize the contribution of this work.
3. The paper does not provide a detailed analysis of the computational cost of Newton Losses. It would be helpful to provide a breakdown of the computational cost of each step in the algorithm and compare it to the cost of other optimization methods. For example, the computation of the Hessian and Fisher matrix can be computationally expensive, and it would be useful to understand how this cost scales with the size of the problem. A detailed analysis of the computational complexity would help to assess the practical applicability of the method.

### Suggestions

The paper introduces an interesting approach by using second-order information to modify the loss function, but it lacks a thorough theoretical analysis. To strengthen the paper, the authors should provide a more detailed analysis of the convergence properties of Newton Losses. This should include a discussion of the conditions under which the method is guaranteed to converge, and the rate of convergence. It would be beneficial to explore the relationship between the curvature of the original loss function and the modified loss function, and how this affects the optimization process. Furthermore, the authors should investigate the potential for the method to get stuck in saddle points or local minima, and how this can be mitigated. A theoretical analysis of the method's behavior in non-convex settings would also be valuable, as many real-world loss functions are non-convex. This analysis should include a discussion of the limitations of the method and the scenarios where it is most likely to be effective.

In addition to a theoretical analysis, the paper would benefit from a more comprehensive experimental evaluation. The authors should compare the performance of Newton Losses with other second-order optimization methods, such as quasi-Newton methods and natural gradient methods. This comparison should include a discussion of the advantages and disadvantages of each approach, and the scenarios where each method is most effective. The authors should also investigate the sensitivity of Newton Losses to the choice of hyperparameters, such as the learning rate and the regularization parameter. A more detailed analysis of the experimental results would help to understand the strengths and weaknesses of the proposed method. Furthermore, the authors should consider evaluating the method on a wider range of benchmark problems, including those with higher dimensionality and more complex loss landscapes.

Finally, the paper should include a more detailed analysis of the computational cost of Newton Losses. The authors should provide a breakdown of the computational cost of each step in the algorithm, including the computation of the Hessian and Fisher matrix. This analysis should include a discussion of how the computational cost scales with the size of the problem, and how it compares to the cost of other optimization methods. The authors should also investigate the potential for optimizing the implementation of Newton Losses to reduce its computational cost. This could include exploring techniques such as low-rank approximations of the Hessian or Fisher matrix, or using more efficient algorithms for matrix inversion. A detailed analysis of the computational complexity would help to assess the practical applicability of the method and identify areas for further improvement.

### Questions

1. Can you provide a theoretical analysis of the convergence properties of Newton Losses?
2. Can you provide a detailed comparison with other second-order optimization methods, such as quasi-Newton methods or natural gradient methods?
3. Can you provide a detailed analysis of the computational cost of Newton Losses?

### Rating

6

### Confidence

3

**********
