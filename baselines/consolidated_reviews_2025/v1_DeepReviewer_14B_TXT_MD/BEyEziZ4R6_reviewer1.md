### Summary

This paper proposes a method for computing increasingly tight Lipschitz bounds for neural networks, which in turn can be used to compute increasingly tight gradient bounds. The gradient bounds can then be used in DP training (where the per-sample gradients are clipped) to add less noise. The paper also includes an implementation of their method, as well as experiments showing the benefits of this approach on several datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well written and easy to follow.
- The experiments are well conducted and show significant improvements over prior work.
- The method itself is simple and straightforward to implement.
- The code is included as an open source library.

### Weaknesses

#### Some Related Works


#### comment

 - The method still requires per-sample clipping, which is a significant limitation in terms of computational efficiency.
- The theoretical analysis could be more rigorous, especially regarding the tightness of the Lipschitz bounds in different network architectures.
- The paper does not fully explore the limitations of the proposed method, particularly in scenarios with highly non-convex loss landscapes.

### Suggestions

The paper's primary weakness lies in its reliance on per-sample gradient clipping, which introduces a computational bottleneck. While the authors propose a method to compute tighter Lipschitz bounds, the need for per-sample clipping remains a significant hurdle for scaling this approach to larger models and datasets. Future work should focus on developing methods that can avoid per-sample clipping, perhaps by exploring alternative approaches to bounding the sensitivity of the gradient. For example, techniques that rely on layer-wise Lipschitz bounds or methods that use adaptive clipping parameters could be investigated. Furthermore, the authors should provide a more detailed analysis of the computational overhead of their approach, comparing it to other differentially private training methods, and explore techniques to reduce this overhead, such as using more efficient data structures or parallelizing the clipping process.

To strengthen the theoretical foundation of the work, the authors should provide a more in-depth analysis of the tightness of the proposed Lipschitz bounds. While the paper demonstrates empirical improvements, a more rigorous theoretical analysis is needed to understand the conditions under which these bounds are tight or loose. This analysis should consider different network architectures, activation functions, and weight initialization schemes. It would be beneficial to explore how the Lipschitz constant changes during training and how this affects the overall performance of the method. Furthermore, the authors should investigate the relationship between the Lipschitz constant and the generalization performance of the model, as well as the impact of the Lipschitz constant on the convergence properties of the optimization algorithm. This could involve analyzing the spectral properties of the weight matrices and their impact on the Lipschitz constant.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. While the experiments show promising results, the authors should acknowledge the potential challenges in applying their method to more complex scenarios, such as highly non-convex loss landscapes or datasets with high dimensionality. It would be beneficial to explore the sensitivity of the method to different hyperparameter settings and to provide guidelines for selecting appropriate values. The authors should also discuss the potential impact of the Lipschitz constraint on the expressiveness of the model and whether it limits the model's ability to learn complex patterns in the data. A more comprehensive discussion of these limitations would provide a more balanced perspective on the strengths and weaknesses of the proposed method.

### Questions

1. How does the choice of architecture affect the tightness of the Lipschitz bounds? Are there specific architectures for which the bounds are particularly tight or loose?
2. What are the limitations of the proposed method? When might it fail to provide meaningful improvements over existing approaches?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
