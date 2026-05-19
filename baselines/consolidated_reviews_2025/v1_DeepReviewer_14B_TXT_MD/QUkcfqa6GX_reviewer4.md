### Summary

This paper proposes a novel framework, STLLM, for spatio-temporal prediction in urban computing. The framework integrates Large Language Models (LLMs) with a cross-view mutual information maximization paradigm to capture implicit spatio-temporal dependencies and preserve spatial semantics in urban space. The authors demonstrate the effectiveness of STLLM through extensive experiments on real-world datasets, showing its ability to outperform state-of-the-art baselines in various prediction tasks such as traffic flow, crime rates, and air quality.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach, STLLM, which integrates Large Language Models (LLMs) with a cross-view mutual information maximization paradigm for spatio-temporal prediction in urban computing. This approach is innovative and has the potential to significantly advance the field.

2. The authors provide a thorough evaluation of STLLM through extensive experiments on real-world datasets. They compare the performance of STLLM with various state-of-the-art baselines across different spatio-temporal learning applications, demonstrating the superiority of their proposed method.

3. The paper is well-organized and clearly written, making it easy to follow the methodology and understand the results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed STLLM framework. For instance, the authors could address the potential challenges in scaling the approach to larger and more complex urban environments or the impact of data quality on the performance of the model. Specifically, the paper lacks a discussion on how the model would perform with significantly higher spatial and temporal resolution data, which is common in real-world urban scenarios. Furthermore, the sensitivity of the model to noisy or incomplete spatio-temporal data is not adequately explored, which is a critical factor for practical deployment.

2. While the paper focuses on urban computing applications, it would be valuable to explore the potential of STLLM in other domains. For example, the authors could discuss how the framework could be adapted for predicting weather patterns, traffic flow in transportation networks, or even social media activity. The current discussion is too narrow and does not fully explore the generalizability of the proposed method. The paper should also consider the necessary modifications to the framework to make it applicable to these diverse domains, including the need for different feature representations and evaluation metrics.

3. The paper could provide more insights into the interpretability of the STLLM framework. Understanding how the model makes predictions and what factors it considers most important could be valuable for researchers and practitioners. The current analysis lacks a detailed explanation of how the LLM component contributes to the final predictions and how the mutual information maximization paradigm influences the learned representations. Visualizing the learned embeddings and analyzing their correlation with specific spatial and temporal features would greatly enhance the interpretability of the model.

### Suggestions

To address the limitations regarding scalability and data quality, the authors should conduct experiments on datasets with varying spatial and temporal resolutions. This would provide a clearer understanding of how the model's performance changes with increasing data complexity. Additionally, the authors should introduce controlled levels of noise and missing data into the datasets and evaluate the model's robustness under these conditions. This could involve techniques such as random data masking or adding Gaussian noise to the input features. Furthermore, the paper should include a discussion on the computational cost of the proposed method, especially when applied to large-scale datasets, and explore potential optimization strategies to improve its efficiency. This would make the method more practical for real-world applications.

To broaden the applicability of the STLLM framework, the authors should provide a more detailed discussion on how the model can be adapted to different domains. This should include specific examples of how the input features and the LLM prompts would need to be modified for applications such as weather forecasting or traffic prediction. For instance, in weather forecasting, the model would need to incorporate meteorological variables such as temperature, humidity, and wind speed, while in traffic prediction, it would need to consider road network topology and traffic flow data. The authors should also discuss the challenges associated with adapting the model to these new domains, such as the need for domain-specific knowledge and the potential for overfitting to the training data. A comparative analysis of the model's performance across different domains would also be beneficial.

To improve the interpretability of the STLLM framework, the authors should conduct a more in-depth analysis of the learned representations. This could involve visualizing the embeddings using techniques such as t-SNE or PCA to understand the underlying structure of the data. The authors should also investigate the correlation between the learned embeddings and specific spatial and temporal features to identify the factors that the model considers most important for prediction. Furthermore, the paper should include an analysis of the attention weights of the LLM component to understand how it processes the input text and which parts of the text are most relevant for prediction. This would provide valuable insights into the model's decision-making process and increase its transparency.

### Questions

1. How does the STLLM framework handle missing or incomplete data in the spatio-temporal datasets? Are there any specific data preprocessing steps or techniques used to address this issue?

2. What are the computational requirements for training and deploying the STLLM framework? How does the computational cost scale with the size of the input data?

3. How does the choice of the Large Language Model affect the performance of the STLLM framework? Have the authors experimented with different LLMs, and if so, what were the results?

4. Can the STLLM framework be extended to handle multi-modal data, such as images or videos, in addition to the spatio-temporal data?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
