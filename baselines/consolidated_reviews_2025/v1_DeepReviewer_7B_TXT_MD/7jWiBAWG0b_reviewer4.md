### Summary

This paper studies the generalization and optimization error bounds for non-convex pairwise learning with heavy-tailed gradient noise. The authors first establish the stability-based generalization error bound for non-convex pairwise learning under the general non-convex setting. Then, they further study the optimization error and excess risk bounds for the non-convex pairwise learning under the gradient dominance condition. Finally, they extend the analysis to the corresponding minibatch case and provide the first stability-based learning guarantees for non-convex pairwise minibatch learning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper studies the generalization and optimization error bounds for non-convex pairwise learning with heavy-tailed gradient noise, which is a more realistic setting than the bounded gradient assumption. 
2. The authors provide the first stability-based learning guarantees for non-convex pairwise minibatch learning, which is a novel contribution. 
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed discussion of the limitations of the proposed approach. For example, the authors do not discuss the computational complexity of the proposed algorithm or the sensitivity of the results to the choice of hyperparameters. Specifically, the paper lacks an analysis of how the stability constants, which are central to the generalization bounds, scale with the dimensionality of the problem or the size of the dataset. This is crucial for understanding the practical applicability of the theoretical results. Furthermore, the paper does not explore the potential for the derived bounds to be loose in certain scenarios, which could limit their usefulness in practice.
2. The paper does not provide any empirical results to validate the theoretical findings. It would be helpful to see some experiments on real-world datasets to demonstrate the effectiveness of the proposed approach. The absence of empirical validation makes it difficult to assess the practical relevance of the theoretical results. For instance, it is unclear how the derived generalization bounds translate into actual performance improvements or trade-offs in practical scenarios. The paper should include experiments that compare the performance of the proposed method with existing approaches under different levels of heavy-tailed noise and varying dataset characteristics.

### Suggestions

The paper would benefit significantly from a more thorough discussion of the practical limitations of the proposed approach. Specifically, the authors should investigate the computational complexity of their algorithm, particularly in the context of large-scale datasets. This analysis should include a discussion of the time and space requirements for computing the stability constants and how these requirements scale with the problem size. Furthermore, the authors should provide a sensitivity analysis of the stability constants with respect to the choice of hyperparameters, such as the learning rate and batch size. This analysis would help practitioners understand how to tune these parameters to achieve optimal performance. It would also be beneficial to explore the potential for the derived bounds to be loose in certain scenarios, and discuss the implications of these limitations for the practical applicability of the theoretical results. For example, the authors could investigate whether the bounds are tightest under specific conditions, and how these conditions relate to real-world datasets.

To enhance the practical relevance of the paper, the authors should include empirical results on real-world datasets. These experiments should demonstrate the effectiveness of the proposed approach in practice and validate the theoretical findings. The experiments should compare the performance of the proposed method with existing approaches under different levels of heavy-tailed noise and varying dataset characteristics. The authors should also investigate the impact of different hyperparameter settings on the performance of the proposed method. Furthermore, the authors should provide a detailed analysis of the experimental results, including a discussion of the observed trends and any limitations of the proposed approach. This would help practitioners understand the practical implications of the theoretical results and make informed decisions about the use of the proposed method.

Finally, the authors should provide more intuition behind the derived bounds. While the paper presents the bounds, it does not fully explain why these bounds are expected to hold and what they signify in terms of the generalization performance of pairwise learning. A more detailed discussion of the factors that influence the tightness of the bounds, such as the learning rate, the batch size, and the properties of the loss function, would be beneficial. The authors should also discuss the practical implications of their results, such as how they can be used to guide the design of pairwise learning algorithms. This would make the paper more accessible and impactful to a wider audience.

### Questions

1. How do the derived generalization bounds depend on the dimensionality of the problem and the size of the dataset?
2. How sensitive are the derived bounds to the choice of hyperparameters?
3. How do the proposed approach perform in practice compared to existing approaches?

### Rating

8

### Confidence

2

**********
