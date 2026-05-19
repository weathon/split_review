### Summary

This paper proposes a new method for learning interpretable rule lists from data. The method is differentiable and uses a soft rule conjunction. The method is compared against several baselines on a variety of datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The method is compared against several baselines on a variety of datasets.
- The method is differentiable, which is a nice property for interpretability.
- The method is able to learn exact thresholds for continuous features.

### Weaknesses

#### Some Related Works


#### comment

 - The method is compared against several baselines on a variety of datasets. However, the baselines are not the most recent state-of-the-art methods. It would be beneficial to compare against more recent methods, especially those that are also differentiable or use similar techniques.
- The method is able to learn exact thresholds for continuous features. However, it is not clear how this is achieved, and the paper does not provide a detailed explanation of the mechanism. It would be helpful to have a more in-depth discussion of the specific algorithm used to determine these exact thresholds.
- The method is differentiable, which is a nice property for interpretability. However, the paper does not discuss the potential limitations of using a differentiable approach, such as the possibility of converging to local optima or the sensitivity to initialization. A more thorough analysis of these aspects would be beneficial.
- The method is compared against several baselines on a variety of datasets. However, the paper does not provide a detailed analysis of the performance of the method on different types of datasets, such as those with high dimensionality or those with complex relationships between features. It would be helpful to have a more granular analysis of the method's performance across different dataset characteristics.

### Suggestions

The paper would benefit from a more thorough comparison against state-of-the-art methods, particularly those that are also differentiable or use similar techniques. Specifically, the authors should consider comparing against methods that use neural networks to learn rule lists or methods that use differentiable approximations of logical operators. This would provide a more comprehensive evaluation of the proposed method's performance and highlight its strengths and weaknesses compared to the current state of the art. Furthermore, the authors should consider including a more detailed analysis of the computational complexity of the proposed method, especially in comparison to the baselines. This would help to understand the practical applicability of the method in different scenarios.

To address the lack of clarity regarding the exact threshold learning, the authors should provide a more detailed explanation of the algorithm used to determine these thresholds. This should include a step-by-step description of the process, along with a discussion of the mathematical formulation and the underlying assumptions. It would also be helpful to provide a visual representation of the threshold learning process, such as a graph or a diagram, to aid in understanding. Additionally, the authors should discuss the sensitivity of the method to the choice of hyperparameters, such as the learning rate and the number of iterations, and provide guidelines for selecting appropriate values.

Finally, the paper should include a more detailed analysis of the method's performance on different types of datasets. This should include a discussion of the method's performance on datasets with varying dimensionality, sample sizes, and complexity. The authors should also consider including a more detailed analysis of the method's performance on datasets with different types of relationships between features, such as linear or non-linear relationships. This would help to understand the strengths and weaknesses of the method in different scenarios and provide guidance on when it is most appropriate to use. Furthermore, the authors should discuss the limitations of the differentiable approach, such as the possibility of converging to local optima or the sensitivity to initialization, and provide potential solutions to mitigate these issues.

### Questions

- How does the method compare to other state-of-the-art methods?
- How is the exact threshold learned for continuous features?
- What are the limitations of the differentiable approach?
- How does the method perform on different types of datasets?

### Rating

6

### Confidence

3

**********
