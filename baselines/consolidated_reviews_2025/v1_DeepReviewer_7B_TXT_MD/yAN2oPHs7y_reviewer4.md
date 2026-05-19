### Summary

This paper presents a new method for learning rule lists that are interpretable, differentiable, and capable of handling both continuous and categorical features. The method addresses the limitations of traditional rule list learning approaches, which often rely on pre-discretization and are restricted by rule size and feature pre-processing. The proposed method learns the discretization of features, the conjunction of rules, and the ordering of rules without any pre-processing or restrictions. The method is evaluated on a variety of real-world and synthetic datasets, demonstrating superior performance compared to existing methods in terms of accuracy, rule list length, and sample complexity.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is novel and addresses the limitations of traditional rule list learning approaches by learning the discretization of features, the conjunction of rules, and the ordering of rules without any pre-processing or restrictions.
2. The method is differentiable, allowing for end-to-end training and optimization of the entire rule list structure.
3. The method is evaluated on a variety of real-world and synthetic datasets, demonstrating superior performance compared to existing methods in terms of accuracy, rule list length, and sample complexity.
4. The method is able to handle both continuous and categorical features, making it more flexible and applicable to a wider range of datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on temperature annealing to ensure that the learned rule list converges to a strict rule list. However, the paper does not provide a detailed analysis of the impact of the temperature schedule on the performance of the method. Specifically, it is unclear how the choice of temperature annealing schedule affects the trade-off between accuracy and rule list complexity. A more thorough investigation into different temperature annealing schedules and their impact on the final rule list performance is needed.
2. The method is evaluated on a variety of real-world and synthetic datasets, but the paper does not provide a detailed analysis of the types of datasets where the method performs well and where it may struggle. For example, it would be beneficial to understand how the method performs on datasets with high dimensionality, noisy data, or complex relationships between features. A more detailed analysis of the method's strengths and weaknesses across different types of datasets is needed to fully understand its applicability.
3. The method is compared against several baselines, but the paper does not provide a detailed analysis of the computational cost of the method compared to the baselines. It is important to understand the computational complexity of the method, especially when dealing with large datasets. A more detailed analysis of the time and memory requirements of the method is needed to assess its scalability.

### Suggestions

The paper would benefit from a more in-depth analysis of the temperature annealing schedule. The authors should explore different temperature annealing strategies, such as linear, exponential, or step-wise decay, and evaluate their impact on the final performance of the rule list. It would be useful to provide a theoretical justification for the chosen temperature schedule and to analyze how the rate of temperature decrease affects the trade-off between accuracy and rule list complexity. Furthermore, the authors should investigate the sensitivity of the method to the initial temperature value and provide guidelines for selecting an appropriate initial temperature. A detailed analysis of the convergence behavior of the method under different temperature annealing schedules would also be valuable.

To better understand the applicability of the method, the authors should conduct a more detailed analysis of its performance across different types of datasets. This analysis should include datasets with varying dimensionality, noise levels, and complexity of feature relationships. For example, the authors could evaluate the method on datasets with a large number of features, datasets with significant noise, and datasets with complex non-linear relationships between features. This analysis should also include a comparison of the method's performance on datasets with different types of target variables (e.g., binary vs. multi-class). The authors should also investigate the method's performance on datasets with imbalanced class distributions and provide insights into how the method handles such scenarios. This would help to identify the strengths and weaknesses of the method and to determine the types of datasets where it is most suitable.

Finally, the paper should include a more detailed analysis of the computational cost of the method. The authors should provide a theoretical analysis of the time and memory complexity of the method and compare it to the baselines. It would be useful to provide empirical results on the runtime of the method on different datasets and to analyze how the runtime scales with the size of the dataset and the number of features. The authors should also investigate the memory requirements of the method and provide guidelines for selecting an appropriate implementation for different hardware platforms. This analysis should also include a discussion of the potential for parallelizing the method to improve its scalability.

### Questions

1. How does the method handle noisy or irrelevant features in the dataset? Does the method have any mechanisms to filter out or down-weight the influence of noisy features?
2. How does the method scale to very large datasets with millions of samples and hundreds of features? Are there any optimizations or approximations that can be used to improve the scalability of the method?
3. How sensitive is the method to the choice of hyperparameters, such as the learning rate, the number of iterations, and the temperature schedule? Are there any guidelines for selecting appropriate hyperparameter values for different datasets?

### Rating

8

### Confidence

3

**********
