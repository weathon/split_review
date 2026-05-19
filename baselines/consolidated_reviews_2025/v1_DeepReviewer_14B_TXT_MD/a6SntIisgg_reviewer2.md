### Summary

This paper proposes a Local-Global Representation Alignment (LOGRA) framework for unsupervised domain adaptation (UDA) in time series classification. The authors argue that existing UDA methods struggle to extract and align both global and local features in time series data. LOGRA addresses this by using a two-branch encoder: a multi-scale convolutional branch for local features and a patching transformer branch for global features. A fusion module integrates these representations, and several strategies are employed for alignment, including invariant feature learning, triplet loss, dynamic time warping-based feature alignment, adversarial training, and per-class prototype alignment. The authors evaluate LOGRA on four time-series datasets, showing improvements over strong baselines.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is generally well-written and easy to follow, with clear explanations of the proposed method and its components.
2. The LOGRA framework is a novel approach that combines both local and global feature extraction, which is a significant advancement in the field of time series UDA.
3. The authors provide extensive experimental results on four benchmark datasets, demonstrating the effectiveness of LOGRA compared to several strong baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. For example, how does the performance of LOGRA vary with different time series lengths or sampling rates? Are there specific types of domain shifts where LOGRA might struggle? Addressing these questions would provide a more balanced view of the method's applicability.
2. The authors could provide more insights into the choice of hyperparameters for the LOGRA framework and how they might affect the performance. A sensitivity analysis of key hyperparameters would be valuable for practitioners looking to implement the method.
3. The computational complexity of LOGRA is not discussed in detail. Given the multiple components (transformer, CNN, fusion module), it would be useful to understand the computational overhead compared to simpler baselines. This is particularly important for real-world applications where computational resources may be limited.

### Suggestions

The paper would benefit from a more detailed analysis of how the LOGRA framework handles variations in time series data. Specifically, the authors should investigate the impact of different time series lengths on the performance of the model. It is unclear whether the multi-scale convolutional branch and the patching transformer branch are equally effective across varying lengths, or if one branch dominates the performance for certain time series lengths. For instance, shorter time series might not provide sufficient context for the transformer, while longer time series might be better suited for the convolutional branch. Furthermore, the authors should explore the effect of different sampling rates on the model's performance. Time series data often have varying sampling rates, and it is important to understand how LOGRA adapts to these differences. The authors could consider resampling techniques or adaptive methods to handle varying sampling rates, and analyze the performance of the model under these conditions. This analysis would provide a more comprehensive understanding of the method's robustness and applicability to real-world scenarios.

Additionally, a more thorough investigation into the hyperparameter sensitivity of the LOGRA framework is needed. The authors should provide a detailed analysis of how different hyperparameters, such as the learning rate, batch size, and the number of layers in the transformer and convolutional branches, affect the performance of the model. A sensitivity analysis would help practitioners understand which hyperparameters are most critical for achieving optimal performance. For example, the authors could explore the impact of different learning rates on the convergence of the model and the final accuracy. Similarly, they could investigate the effect of different batch sizes on the stability of the training process. Furthermore, the authors should provide guidelines for selecting appropriate hyperparameter values for different datasets. This would make the method more accessible and easier to use for practitioners. The authors could also consider using techniques such as grid search or Bayesian optimization to find optimal hyperparameter values.

Finally, the paper should include a more detailed discussion of the computational complexity of the LOGRA framework. The authors should provide a breakdown of the computational cost of each component, including the transformer, convolutional branch, and fusion module. This analysis should include the number of parameters, the number of floating-point operations (FLOPs), and the training time. It would be useful to compare the computational cost of LOGRA with that of the baseline methods. This comparison would help practitioners understand the trade-offs between performance and computational resources. The authors should also discuss the scalability of the method to larger datasets and longer time series. This analysis would provide a more complete picture of the method's practical applicability. Furthermore, the authors could explore techniques to reduce the computational cost of the method, such as model compression or pruning.

### Questions

Please refer to the weaknesses.

### Rating

5

### Confidence

4

**********
