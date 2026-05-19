### Summary

This paper proposes a method for improving the decomposition of indoor scenes using convex primitives by introducing an ensembling technique and incorporating negative primitives. The authors demonstrate that using negative primitives in the primitive fitting process and ensembling over different regression procedures significantly improves the accuracy of scene decomposition. The method is evaluated on the NYUv2 dataset, and the results show that the proposed approach outperforms the state-of-the-art methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to scene decomposition by using negative primitives and an ensembling technique. This approach is different from previous works that only use positive primitives.
2. The paper provides a detailed explanation of the proposed method, including the use of negative primitives, ensembling, and other performance improvements. The figures and tables are helpful in understanding the method and the results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is mentioned that the method requires ensembling a number of regressors, but the impact of this on the overall computational cost is not discussed.
2. The paper does not provide a detailed analysis of the impact of the number of primitives on the performance of the proposed method. It is mentioned that the method uses a fixed number of primitives, but it is not clear how this number is chosen and how it affects the accuracy of the scene decomposition.
3. The paper does not provide a detailed analysis of the impact of the choice of loss function on the performance of the proposed method. It is mentioned that the method uses a specific loss function, but it is not clear how this loss function was chosen and how it compares to other possible loss functions.
4. The paper does not provide a detailed analysis of the impact of the choice of optimizer on the performance of the proposed method. It is mentioned that the method uses a specific optimizer, but it is not clear how this optimizer was chosen and how it compares to other possible optimizers.
5. The paper does not provide a detailed analysis of the impact of the choice of learning rate on the performance of the proposed method. It is mentioned that the method uses a specific learning rate, but it is not clear how this learning rate was chosen and how it compares to other possible learning rates.
6. The paper does not provide a detailed analysis of the impact of the choice of batch size on the performance of the proposed method. It is mentioned that the method uses a specific batch size, but it is not clear how this batch size was chosen and how it compares to other possible batch sizes.
7. The paper does not provide a detailed analysis of the impact of the choice of number of iterations on the performance of the proposed method. It is mentioned that the method uses a specific number of iterations, but it is not clear how this number was chosen and how it compares to other possible numbers of iterations.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed ensembling approach. While the authors mention that multiple regressors are used, a detailed breakdown of the time complexity for both training and inference is needed. This should include a comparison of the computational cost with and without ensembling, and how the number of regressors in the ensemble affects the overall runtime. Furthermore, it would be beneficial to analyze the memory footprint of the ensemble, as this could be a limiting factor for deployment on resource-constrained devices. A clear understanding of these computational trade-offs is crucial for assessing the practical applicability of the method. The authors should also consider providing a more detailed analysis of the convergence behavior of the individual regressors within the ensemble, as this could provide insights into the efficiency of the training process.

Regarding the number of primitives, the paper should include a more rigorous analysis of how this parameter affects the performance of the method. While the authors mention that a fixed number of primitives is used, a sensitivity analysis is needed to determine the optimal number of primitives for different scene complexities. This analysis should include a range of primitive counts and evaluate the impact on both accuracy and computational cost. It would also be beneficial to explore adaptive methods for determining the number of primitives, rather than using a fixed value. For example, the method could start with a small number of primitives and iteratively add more based on the fitting error. This could lead to a more efficient and accurate decomposition of scenes. The authors should also discuss the limitations of using a fixed number of primitives and how this might affect the generalization ability of the method.

Finally, the paper should provide a more detailed justification for the choice of loss function, optimizer, learning rate, batch size, and number of iterations. While the authors mention that these choices were made to align with prior work, a more thorough analysis is needed to demonstrate that these choices are optimal for the proposed method. This analysis should include a comparison of different loss functions, optimizers, learning rates, batch sizes, and number of iterations, and how these choices affect the performance of the method. The authors should also discuss the sensitivity of the method to these hyperparameters and provide guidelines for selecting appropriate values. A more rigorous analysis of these factors would strengthen the paper and provide a more complete understanding of the proposed method.

### Questions

1. How does the number of primitives affect the performance of the proposed method?
2. How does the choice of loss function affect the performance of the proposed method?
3. How does the choice of optimizer affect the performance of the proposed method?
4. How does the choice of learning rate affect the performance of the proposed method?
5. How does the choice of batch size affect the performance of the proposed method?
6. How does the choice of number of iterations affect the performance of the proposed method?

### Rating

3

### Confidence

3

**********
