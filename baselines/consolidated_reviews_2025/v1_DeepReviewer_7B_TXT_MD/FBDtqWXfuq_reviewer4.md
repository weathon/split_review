### Summary

This paper introduces a novel federated learning setting called Modality-Collaborated Federated Learning (MCFL), where clients possess data from only a single modality. The authors propose FedCola, a framework based on modality-agnostic transformers, to address the challenges of model heterogeneity and modality gaps in MCFL. The paper presents comprehensive evaluations that demonstrate the effectiveness of FedCola in terms of performance and efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel federated learning setting called Modality-Collaborated Federated Learning (MCFL), which is a significant contribution to the field of federated learning.
2. The authors propose FedCola, a framework based on modality-agnostic transformers, to address the challenges of model heterogeneity and modality gaps in MCFL.
3. The paper presents comprehensive evaluations that demonstrate the effectiveness of FedCola in terms of performance and efficiency.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. For example, the paper does not discuss the potential impact of data heterogeneity on the performance of FedCola, or the computational cost of training and deploying the modality-agnostic transformer. Specifically, the paper does not explore how the performance of FedCola would be affected by varying degrees of data heterogeneity across modalities, such as differences in class distributions or feature scales. Furthermore, the computational overhead of the transformer, especially when dealing with high-dimensional data or a large number of modalities, is not analyzed in detail.
2. The paper does not provide a detailed comparison of the proposed method with existing federated learning approaches. While the paper mentions that FedCola outperforms existing solutions, it does not provide a comprehensive analysis of the advantages and disadvantages of FedCola compared to other state-of-the-art methods. For instance, the paper does not discuss how FedCola compares to methods that use different aggregation techniques or those that explicitly model inter-modal relationships. A more thorough comparison would include a discussion of the trade-offs between performance, computational cost, and communication overhead.
3. The paper does not provide sufficient details on the implementation of the proposed method. For example, the paper does not specify the exact architecture of the modality-agnostic transformer, the optimization algorithm used, or the hyperparameter settings. This lack of detail makes it difficult for other researchers to reproduce the results and build upon the proposed method. The paper should include a detailed description of the model architecture, including the number of layers, the size of each layer, and the activation functions used. Additionally, the paper should specify the optimization algorithm, the learning rate, and the batch size used during training. The hyperparameter settings, such as the learning rate and the number of epochs, should also be clearly stated.

### Suggestions

The paper should include a more detailed analysis of the limitations of the proposed method, particularly concerning the impact of data heterogeneity and computational cost. The authors should conduct experiments to evaluate the performance of FedCola under different levels of data heterogeneity, such as varying class distributions or feature scales across modalities. This could involve creating synthetic datasets with controlled levels of heterogeneity or using real-world datasets with known heterogeneity. The results of these experiments should be analyzed to determine how the performance of FedCola degrades as the degree of heterogeneity increases. Furthermore, the paper should provide a detailed analysis of the computational cost of training and deploying the modality-agnostic transformer. This should include an analysis of the time and memory requirements for training the model, as well as the communication overhead associated with transmitting model updates between clients. The authors should also discuss how the computational cost scales with the number of modalities and the size of the data. This analysis would provide a more complete picture of the practical feasibility of the proposed method.

To address the lack of detailed comparison with existing federated learning approaches, the paper should include a more comprehensive analysis of the advantages and disadvantages of FedCola compared to other state-of-the-art methods. This should include a discussion of the trade-offs between performance, computational cost, and communication overhead. The authors should compare FedCola with methods that use different aggregation techniques, such as FedAvg, FedProx, and FedDyn, as well as methods that explicitly model inter-modal relationships. The comparison should not only focus on the final performance of the methods but also on their convergence speed, robustness to different data distributions, and sensitivity to hyperparameter settings. The paper should also discuss the limitations of FedCola compared to other methods, such as its potential sensitivity to the choice of the modality-agnostic transformer architecture or its performance in scenarios with highly imbalanced data distributions. This would provide a more balanced and comprehensive assessment of the proposed framework.

Finally, the paper should provide more details on the implementation of the proposed method. This should include a detailed description of the architecture of the modality-agnostic transformer, including the number of layers, the size of each layer, and the activation functions used. The paper should also specify the optimization algorithm used, the learning rate, and the batch size used during training. The hyperparameter settings, such as the learning rate and the number of epochs, should also be clearly stated. This level of detail is essential for other researchers to reproduce the results and build upon the proposed method. The authors should also provide a discussion of the hyperparameter tuning process and the sensitivity of the results to different hyperparameter settings. This would allow other researchers to understand the robustness of the proposed method and its applicability to different scenarios.

### Questions

1. How does the proposed FedCola framework handle the issue of data heterogeneity across modalities? Specifically, how does FedCola perform when the data distributions across modalities are significantly different?
2. What is the computational cost of training and deploying the modality-agnostic transformer? How does this cost scale with the number of modalities and the size of the data?
3. How does FedCola compare to other state-of-the-art federated learning methods in terms of performance, computational cost, and communication overhead?

### Rating

6

### Confidence

3

**********
