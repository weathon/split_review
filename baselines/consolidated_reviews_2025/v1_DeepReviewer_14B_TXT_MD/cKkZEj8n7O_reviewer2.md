### Summary

This paper presents a new bias-variance decomposition framework for analyzing generalization error in DNNs, leading to a novel training approach called Generalization Error Minimized (GEM) DL. GEM DL jointly minimizes the conventional training loss and a proxy for generalization error, resulting in reduced overfitting and improved generalization. The method demonstrates consistent accuracy gains across various DNN architectures and scenarios, including data distribution shifts, few-shot learning, and imbalanced datasets. The approach is grounded in theory, practical, and compatible with existing regularization techniques.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel bias-variance decomposition framework that offers a fresh perspective on understanding generalization error in DNNs. This new framework is a valuable contribution to the field, providing a more nuanced understanding of the factors influencing generalization.

2. The proposed GEM DL framework is theoretically sound and practically useful. It is not only grounded in solid mathematical foundations but also easy to implement, making it accessible to both researchers and practitioners.

3. The authors conduct extensive experiments on CIFAR-100 and ImageNet datasets, demonstrating the effectiveness of GEM DL across various DNN architectures and application scenarios. The consistent performance gains in different settings highlight the robustness and generalizability of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity of the GEM DL framework. It is important to understand how the proposed method scales with increasing model size and dataset complexity. Specifically, the paper should provide a breakdown of the computational cost associated with calculating the generalization error proxy, including the number of forward and backward passes required, and how this cost compares to the baseline training procedure. Furthermore, the memory requirements of the method, especially when dealing with large batch sizes or complex models, should be discussed.

2. The experiments are primarily focused on image classification tasks. It would be beneficial to evaluate the performance of GEM DL on other types of data and tasks, such as natural language processing or time-series analysis, to demonstrate its broader applicability. For example, the authors could consider evaluating the method on tasks such as text classification or sentiment analysis using standard datasets like GLUE, or on time-series forecasting tasks using datasets like those from the UCI repository. This would provide a more comprehensive understanding of the method's strengths and limitations.

3. The paper could benefit from a more in-depth discussion of the limitations of the proposed method and potential directions for future research. For instance, the authors could discuss the sensitivity of the method to the choice of hyperparameters, such as the weighting factor for the generalization error proxy, and how this might affect performance in different scenarios. Additionally, the paper should address the potential challenges of applying GEM DL to very large-scale models or datasets, and how these challenges might be overcome.

### Suggestions

To address the lack of computational complexity analysis, the authors should include a detailed breakdown of the computational cost associated with the GEM DL framework. This should include an analysis of the number of forward and backward passes required for calculating the generalization error proxy, and how this compares to the baseline training procedure. The authors should also discuss the memory requirements of the method, particularly when dealing with large batch sizes or complex models. Furthermore, it would be beneficial to provide empirical results on the training time and memory usage of GEM DL compared to standard training methods, across different model sizes and dataset complexities. This analysis should be presented in a clear and concise manner, allowing readers to understand the practical implications of using the proposed method.

To broaden the applicability of the proposed method, the authors should conduct experiments on a wider range of tasks beyond image classification. Specifically, they should evaluate the performance of GEM DL on natural language processing tasks, such as text classification or sentiment analysis, using standard datasets like GLUE. Additionally, the authors should consider evaluating the method on time-series analysis tasks, such as time-series forecasting, using datasets from the UCI repository. These experiments should include a variety of model architectures and datasets to demonstrate the robustness and generalizability of the proposed method. The results should be presented in a clear and concise manner, allowing readers to understand the strengths and limitations of GEM DL in different application domains. This would significantly enhance the impact and relevance of the paper.

Finally, the authors should provide a more in-depth discussion of the limitations of the proposed method and potential directions for future research. This should include a discussion of the sensitivity of the method to the choice of hyperparameters, such as the weighting factor for the generalization error proxy, and how this might affect performance in different scenarios. The authors should also address the potential challenges of applying GEM DL to very large-scale models or datasets, and how these challenges might be overcome. Furthermore, the authors should discuss potential avenues for future research, such as exploring alternative formulations of the generalization error proxy or investigating the theoretical properties of the proposed method in more detail. This would provide a more complete and nuanced understanding of the proposed method and its potential for future development.

### Questions

See weakness.

### Rating

6

### Confidence

2

**********
