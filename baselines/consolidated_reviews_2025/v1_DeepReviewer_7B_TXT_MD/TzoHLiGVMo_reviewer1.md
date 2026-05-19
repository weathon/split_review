### Summary

The paper introduces ODEFormer, a transformer-based model designed to infer multidimensional ordinary differential equations (ODEs) from noisy, irregularly sampled time series data. The authors also present ODEBench, a new benchmark dataset for evaluating dynamical system regression methods. ODEFormer is shown to outperform existing methods in terms of robustness to noise and irregular sampling while maintaining computational efficiency.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses the challenging problem of inferring governing equations from data, which is crucial for scientific discovery.
2. The authors provide a thorough evaluation of their method, comparing it against several baselines and demonstrating its effectiveness on both synthetic and real-world datasets.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper compares ODEFormer with several baselines, it would be beneficial to include more recent and state-of-the-art methods for dynamical system regression. This would help to better contextualize the contributions of ODEFormer and demonstrate its advantages over the current state of the art.
2. The paper focuses on inferring ODEs from time series data, but it does not discuss the limitations of this approach or potential challenges in applying it to real-world datasets. For example, the paper could discuss the impact of measurement noise, model complexity, and the choice of hyperparameters on the performance of ODEFormer. A more detailed analysis of these factors would provide a more comprehensive understanding of the method's strengths and weaknesses.
3. The paper claims that ODEFormer is computationally efficient, but it does not provide a detailed comparison of its computational cost with other methods. A more thorough analysis of the computational complexity of ODEFormer, including training and inference time, would be valuable for assessing its practical applicability.

### Suggestions

The paper would benefit from a more rigorous comparison against recent state-of-the-art methods in dynamical system regression. While the included baselines are relevant, the field has seen significant advancements, particularly in neural ODEs and related approaches. A more thorough comparison should include methods that explicitly address the challenges of noisy and irregularly sampled data, as these are common in real-world applications. For example, methods that incorporate data imputation or robust loss functions could be included to provide a more comprehensive evaluation. Furthermore, the comparison should not only focus on accuracy but also on computational efficiency, including training time, inference time, and memory usage. This would provide a more complete picture of the practical trade-offs associated with ODEFormer.

To enhance the discussion of limitations, the authors should delve deeper into the impact of various factors on the performance of ODEFormer. Specifically, the paper should include a sensitivity analysis of the model's hyperparameters, such as the number of layers, hidden units, and learning rate, to understand their influence on the accuracy and robustness of the inferred ODEs. The paper should also discuss the limitations of the model in handling high-dimensional systems or systems with complex nonlinearities. Furthermore, the authors should address the challenges of applying ODEFormer to real-world datasets, such as those with significant measurement noise or missing data. A discussion of potential strategies for mitigating these challenges, such as data preprocessing techniques or robust model architectures, would be valuable.

Finally, the paper should provide a more detailed analysis of the computational complexity of ODEFormer. This analysis should include a breakdown of the time and memory requirements for both training and inference, as well as a comparison with other methods. The authors should also discuss the scalability of ODEFormer to larger datasets and more complex models. This analysis should be supported by empirical results, such as training and inference times for different problem sizes. A more thorough analysis of the computational cost would be crucial for assessing the practical applicability of ODEFormer in real-world scenarios.

### Questions

1. How does ODEFormer handle situations where the underlying ODE is not unique or when the data is insufficient to uniquely determine the governing equations?
2. The paper mentions that ODEFormer is computationally efficient. Could you provide more details on the computational complexity of ODEFormer, including training and inference time, and compare it with other methods?

### Rating

6

### Confidence

3

**********
