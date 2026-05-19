### Summary

The paper introduces a new framework for analyzing and minimizing the generalization error of deep neural networks (DNNs). It proposes a novel bias-variance decomposition of the generalization error, which is then used to develop a new training method called Generalization Error Minimized (GEM) DL. GEM DL jointly minimizes the conventional training loss and an analytical proxy for the generalization error, leading to improved generalization performance. The paper demonstrates the effectiveness of GEM DL through extensive experiments on image classification tasks, showing consistent gains in prediction accuracy across various DNN architectures and different application scenarios, including data distribution shifts, few-shot learning, and imbalanced datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel bias-variance decomposition framework for analyzing the generalization error of DNNs, which is a significant theoretical contribution to the field.

2. The proposed GEM DL framework is grounded in solid mathematical foundations, making it a theoretically sound approach to improving generalization.

3. The paper demonstrates the effectiveness of GEM DL through extensive experiments on CIFAR-100 and ImageNet datasets, showing consistent gains in prediction accuracy across various DNN architectures and different application scenarios.

4. The GEM DL method is compatible with existing regularization techniques and can be easily integrated into the standard deep learning pipeline, making it practical for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity of the GEM DL framework. It is important to understand how the proposed method scales with increasing model size and dataset complexity. Specifically, the paper does not discuss the overhead introduced by the additional terms in the loss function, which involve expectations over the data distribution. This is a critical aspect for practical application, especially when considering large-scale models and datasets.

2. The experiments are primarily focused on image classification tasks. It would be beneficial to evaluate the performance of GEM DL on other types of data and tasks, such as natural language processing or time-series analysis, to demonstrate its broader applicability. The current evaluation is limited to image datasets, which may not fully capture the generalization capabilities of the proposed method across diverse data modalities and task types. For instance, the behavior of GEM DL on sequential data or data with different statistical properties is not explored.

3. The paper could benefit from a more in-depth discussion of the limitations of the proposed method and potential directions for future research. For example, the paper does not discuss the sensitivity of the method to the choice of hyperparameters, or the potential for the method to be less effective in scenarios with very high-dimensional data or extremely complex model architectures. A more thorough analysis of these aspects would provide a more complete understanding of the method's strengths and weaknesses.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost associated with the GEM DL framework. This should include an analysis of the number of forward and backward passes required for calculating the additional terms in the loss function, and how this compares to the baseline training procedure. Furthermore, the memory requirements of the method, particularly when dealing with large batch sizes or complex models, should be discussed. It would be beneficial to provide empirical results on the training time and memory usage of GEM DL compared to standard training methods, across different model sizes and dataset complexities. This analysis should be presented in a clear and concise manner, allowing readers to understand the practical implications of using the proposed method. For example, a table showing the training time per epoch for different model sizes and datasets, with and without GEM DL, would be very helpful.

To broaden the applicability of the proposed method, the authors should conduct experiments on a wider range of tasks beyond image classification. Specifically, they should evaluate the performance of GEM DL on natural language processing tasks, such as text classification or sentiment analysis, using standard datasets like GLUE. Additionally, the authors should consider evaluating the method on time-series analysis tasks, such as time-series forecasting or anomaly detection, using datasets from the UCI repository. These experiments should include a variety of model architectures and datasets to demonstrate the robustness and generalizability of the proposed method. The results should be presented in a clear and concise manner, allowing readers to understand the strengths and limitations of GEM DL in different application domains. For example, the authors could show how GEM DL performs on a recurrent neural network (RNN) based model for time-series forecasting, and compare it with standard training methods.

Finally, the authors should provide a more in-depth discussion of the limitations of the proposed method and potential directions for future research. This should include a discussion of the sensitivity of the method to the choice of hyperparameters, such as the weighting factor for the generalization error proxy, and how this might affect performance in different scenarios. The authors should also address the potential challenges of applying GEM DL to very large-scale models or datasets, and how these challenges might be overcome. Furthermore, the authors should discuss potential avenues for future research, such as exploring alternative formulations of the generalization error proxy or investigating the theoretical properties of the proposed method in more detail. This would provide a more complete and nuanced understanding of the proposed method and its potential for future development. For example, the authors could discuss the potential of using different types of regularization terms in the loss function, or explore the use of adaptive weighting factors for the generalization error proxy.

### Questions

1. How does the computational complexity of the GEM DL framework compare to that of standard deep learning training procedures? It is important to understand the trade-offs between improved generalization performance and increased computational cost.

2. Can the authors provide more details on the implementation of the GEM DL framework? For example, what are the specific choices of hyperparameters and optimization algorithms used in the experiments? How sensitive is the performance of GEM DL to these choices?

3. How does the performance of GEM DL compare to other state-of-the-art methods for improving generalization in deep learning, such as adversarial training or data augmentation? It is important to understand the relative advantages and disadvantages of GEM DL compared to existing approaches.

### Rating

6

### Confidence

2

**********
