### Summary

The paper introduces MUBen, a benchmarking tool designed to evaluate uncertainty quantification (UQ) methods in molecular representation models. It assesses various UQ approaches, including Bayesian neural networks, post-hoc calibration, and ensembles, across different state-of-the-art backbone models for molecular property prediction. The study provides insights into selecting appropriate UQ methods for backbone models, aiming to enhance reliability in critical applications like drug discovery and materials science.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

MUBen evaluates a comprehensive range of UQ methods, providing insights into their effectiveness across different molecular property prediction tasks.

The benchmark includes various backbone models that use diverse molecular descriptors, making it applicable to a wide range of scenarios.

### Weaknesses

#### Some Related Works


#### comment

While the paper compares numerous UQ methods, it lacks in-depth theoretical insights or innovative adaptations of UQ techniques tailored specifically for molecular representation models. The application of UQ methods appears to be rather straightforward, without exploring potential modifications or enhancements that could leverage the unique characteristics of molecular data. For instance, the paper does not delve into how the specific structure of molecular graphs or the chemical properties of molecules could influence the choice or adaptation of UQ methods. This is a missed opportunity to advance the field beyond standard applications of existing techniques.

Many of the compared UQ methods come from other domains, and their suitability for molecular representation tasks is not fully justified. The paper does not provide a clear rationale for why certain UQ methods, which may have been developed for image processing or natural language processing, are expected to perform well in the context of molecular property prediction. This lack of justification raises concerns about the relevance and interpretability of the benchmark results. A more thorough discussion of the underlying assumptions and limitations of these methods when applied to molecular data is needed.

### Suggestions

To enhance the paper, the authors should consider exploring UQ methods that are specifically designed or adapted for molecular data. This could involve investigating techniques that incorporate the graph structure of molecules or leverage chemical domain knowledge. For example, one could explore Bayesian neural networks with priors that are informed by chemical properties or develop ensemble methods that combine models trained on different molecular representations. Such adaptations could lead to more effective and reliable uncertainty estimates for molecular property predictions. Furthermore, the authors should provide a more detailed analysis of the performance of different UQ methods across various types of molecular datasets. This could involve categorizing datasets based on the type of molecular properties being predicted (e.g., physical, chemical, biological) or the complexity of the molecules themselves. Such an analysis would help to identify which UQ methods are most suitable for different types of molecular prediction tasks and provide more nuanced guidance for practitioners.

Additionally, the paper would benefit from a more thorough discussion of the limitations of the applied UQ methods in the context of molecular representation learning. For example, the authors could discuss the potential for calibration errors to arise due to the specific characteristics of molecular data, such as the presence of outliers or the high dimensionality of the feature space. They could also explore the computational cost of different UQ methods and discuss the trade-offs between accuracy and efficiency. This would provide a more balanced and critical assessment of the benchmark results and help to guide future research in this area. It is also important to justify the choice of backbone models and UQ methods, explaining why these specific methods were chosen over others and what their expected strengths and weaknesses are in the context of molecular property prediction. A more detailed explanation of the experimental setup, including the hyperparameter settings and training procedures, would also be beneficial for reproducibility.

Finally, the authors should consider including a more in-depth analysis of the uncertainty estimates themselves. For example, they could investigate whether the uncertainty estimates correlate with the actual prediction errors or whether they can be used to identify cases where the model is likely to make incorrect predictions. This would provide a more practical assessment of the value of the UQ methods and help to demonstrate their utility in real-world applications. The authors could also explore the use of visualization techniques to better understand the uncertainty estimates and identify potential areas for improvement. This would help to move the paper beyond a simple benchmarking exercise and provide more meaningful insights into the challenges of uncertainty quantification in molecular representation learning.

### Questions

see weakness

### Rating

3

### Confidence

4

**********
