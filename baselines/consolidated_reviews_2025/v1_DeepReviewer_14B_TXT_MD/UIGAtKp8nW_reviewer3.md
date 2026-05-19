### Summary

This paper introduces MUBen, a benchmark for evaluating uncertainty quantification (UQ) methods in molecular representation models. It assesses various UQ techniques across different backbone models and molecular descriptors, providing insights into their effectiveness for property prediction and uncertainty estimation. The study highlights the importance of selecting appropriate UQ methods for reliable predictions in materials science and drug discovery.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-organized and easy to follow.
2. The studied problem is important and practical.
3. The results are comprehensive and insightful.

### Weaknesses

#### Some Related Works


#### comment

1. The studied backbones and UQ methods are not state-of-the-art. More recent and advanced methods should be included to enhance the relevance and impact of the study. Specifically, the benchmark lacks evaluation of transformer-based models which have shown significant promise in molecular representation learning. Furthermore, the UQ methods considered do not include more recent Bayesian deep learning techniques or methods that explicitly model epistemic uncertainty, which are crucial for reliable predictions in high-stakes applications.
2. The analysis of the results is not deep enough. More in-depth discussion and interpretation of the results are needed to provide valuable insights for the readers. For example, the paper should delve into why certain UQ methods perform better with specific backbones or datasets. A more granular analysis of the calibration performance across different molecular properties and dataset sizes is needed to understand the limitations of each method.

### Suggestions

To enhance the benchmark's relevance, it is crucial to incorporate more recent and advanced molecular representation models, particularly transformer-based architectures like ChemBERTa or MolFormer. These models have demonstrated superior performance in various molecular property prediction tasks and should be included to provide a more comprehensive evaluation of UQ methods. Additionally, the benchmark should explore more sophisticated UQ techniques beyond standard methods like Monte Carlo dropout. This includes Bayesian neural networks, deep ensembles with diverse training strategies, and methods that explicitly model epistemic uncertainty. The inclusion of these methods would provide a more robust and reliable assessment of uncertainty in molecular property predictions. Furthermore, the benchmark should also consider the computational cost of each UQ method, as this is a critical factor in practical applications. A comparison of the computational overhead of different UQ methods would be valuable for practitioners.

To improve the analysis of the results, the paper should include a more detailed investigation into the factors that influence the performance of different UQ methods. This includes analyzing the correlation between model size, dataset size, and the effectiveness of different UQ techniques. For example, it would be beneficial to examine whether certain UQ methods are more effective for smaller datasets or for models with specific architectures. The paper should also provide a more granular analysis of the calibration performance across different molecular properties. This could involve examining the calibration error for different types of properties (e.g., physical, chemical, biological) and identifying any systematic biases in the uncertainty estimates. Additionally, the paper should explore the impact of different training strategies on the calibration performance of the models. This includes investigating the effect of techniques like temperature scaling or focal loss on the reliability of the uncertainty estimates.

Finally, the paper should provide more concrete guidance on how to select the most appropriate UQ method for a given task. This could involve developing a set of guidelines or best practices based on the experimental results. For example, the paper could recommend specific UQ methods for different types of molecular property prediction tasks or for different levels of data availability. The paper should also discuss the limitations of each UQ method and highlight the potential risks of relying on inaccurate uncertainty estimates. This would help practitioners make informed decisions about the use of UQ methods in their own research.

### Questions

Please refer to the Weaknesses.

### Rating

5

### Confidence

3

**********
