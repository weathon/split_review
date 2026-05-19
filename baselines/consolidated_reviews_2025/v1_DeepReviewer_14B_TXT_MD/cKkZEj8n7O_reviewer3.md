### Summary

The paper proposes a novel framework called Generalization Error Minimized (GEM) Deep Learning, which aims to improve the generalization ability of deep neural networks (DNNs). The authors establish a new bias-variance decomposition formula to analyze the generalization error of DNNs and develop a new training framework that jointly minimizes the conventional training loss and an analytical proxy for the conditional generalization error. The effectiveness of GEM DL is verified through extensive experiments on CIFAR-100 and ImageNet datasets, demonstrating consistent gains in prediction accuracy across various DNN architectures and different application scenarios.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel bias-variance decomposition formula that offers new insights into the generalization behavior of DNNs.
2. The authors develop a new training framework, GEM DL, which is grounded in solid mathematical foundations and can be easily integrated with existing regularization techniques.
3. The effectiveness of GEM DL is demonstrated through extensive experiments on CIFAR-100 and ImageNet datasets, showing consistent gains in prediction accuracy across various DNN architectures and different application scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the GEM DL framework. It is important to understand how the proposed method scales with increasing model size and dataset complexity. Specifically, the paper lacks a discussion on the number of additional parameters or operations introduced by the GEM loss term, and how this impacts training time and memory usage, especially when compared to standard empirical risk minimization (ERM).
2. The experiments are primarily focused on image classification tasks. It would be beneficial to evaluate the performance of GEM DL on other types of data and tasks, such as natural language processing or time-series analysis, to demonstrate its broader applicability. The current evaluation is limited to image datasets, which may not fully capture the generalization capabilities of the proposed method across diverse data modalities and task types.
3. The paper could benefit from a more in-depth discussion of the limitations of the proposed method and potential directions for future research. For example, the paper does not discuss the sensitivity of the method to the choice of hyperparameters, or the potential for the method to be less effective in scenarios with very high-dimensional data or extremely complex model architectures.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost associated with the GEM DL framework. This should include an analysis of the number of additional parameters or operations introduced by the GEM loss term, and how this impacts training time and memory usage. It would be beneficial to compare the computational cost of GEM DL with that of standard ERM, and to provide empirical results on the training time and memory usage of GEM DL on different datasets and model architectures. This analysis should also consider the impact of different batch sizes and optimization algorithms on the computational cost of GEM DL. Furthermore, the authors should discuss the scalability of the method to very large datasets and models, and provide recommendations for how to optimize the computational efficiency of GEM DL in such scenarios.

To broaden the applicability of the proposed method, the authors should conduct experiments on a wider range of tasks beyond image classification. Specifically, they should evaluate the performance of GEM DL on natural language processing tasks, such as text classification or sentiment analysis, using standard datasets like GLUE. Additionally, the authors should consider evaluating the method on time-series analysis tasks, such as time-series forecasting or anomaly detection, using datasets from the UCI repository. These experiments should include a variety of model architectures and datasets to demonstrate the robustness and generalizability of the proposed method. The results should be presented in a clear and concise manner, allowing readers to understand the strengths and limitations of GEM DL in different application domains. It would also be beneficial to analyze the performance of GEM DL on tasks with different levels of data complexity and dimensionality, to understand the conditions under which the method is most effective.

Finally, the authors should provide a more in-depth discussion of the limitations of the proposed method and potential directions for future research. This should include a discussion of the sensitivity of the method to the choice of hyperparameters, such as the weighting factor for the generalization error proxy, and how this might affect performance in different scenarios. The authors should also address the potential challenges of applying GEM DL to very large-scale models or datasets, and how these challenges might be overcome. Furthermore, the authors should discuss potential avenues for future research, such as exploring alternative formulations of the generalization error proxy or investigating the theoretical properties of the proposed method in more detail. This would provide a more complete and nuanced understanding of the proposed method and its potential for future development.

### Questions

1. How does the computational complexity of the GEM DL framework compare to that of standard deep learning training procedures? It is important to understand the trade-offs between improved generalization performance and increased computational cost.
2. Can the authors provide more details on the implementation of the GEM DL framework? For example, what are the specific choices of hyperparameters and optimization algorithms used in the experiments? How sensitive is the performance of GEM DL to these choices?
3. How does the performance of GEM DL compare to other state-of-the-art methods for improving generalization in deep learning, such as adversarial training or data augmentation? It is important to understand the relative advantages and disadvantages of GEM DL compared to existing approaches.

### Rating

6

### Confidence

2

**********
