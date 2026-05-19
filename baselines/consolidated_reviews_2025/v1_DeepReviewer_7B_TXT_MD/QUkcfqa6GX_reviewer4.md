### Summary

This paper introduces STLLM, a novel framework that integrates Large Language Models (LLMs) with a cross-view mutual information maximization paradigm to capture implicit spatio-temporal dependencies and preserve point-of-interest (POI) information in urban computing tasks. STLLM leverages LLMs to generate semantic embeddings of POIs, which are then aligned with graph neural network (GNN)-based structural embeddings through a cross-view mutual information maximization objective. The framework is evaluated on three distinct prediction tasks: crime prediction, traffic flow forecasting, and property price prediction. The results demonstrate that STLLM outperforms state-of-the-art baselines in various prediction tasks, highlighting its ability to capture complex spatio-temporal patterns and achieve robust and invariant representations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The integration of LLMs with a cross-view mutual information maximization paradigm is a novel approach that effectively captures implicit spatio-temporal dependencies and preserves POI information.
2. The paper is well-organized and clearly written, making it easy to follow and understand the proposed methodology and experimental results.
3. The authors provide a comprehensive evaluation of STLLM on three distinct prediction tasks, demonstrating its effectiveness and robustness across different urban computing applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the computational complexity and scalability of the proposed framework, especially when dealing with large-scale urban datasets. Specifically, the paper does not provide a breakdown of the computational cost associated with each component of the STLLM framework, such as the LLM inference, GNN training, and the mutual information maximization process. This makes it difficult to assess the practical feasibility of the approach for real-world applications with large datasets.
2. The paper does not explore the sensitivity of the proposed framework to different hyperparameter settings, such as the learning rate, the number of layers in the GNN, and the size of the LLM. Without a thorough sensitivity analysis, it is unclear how robust the results are and whether the performance gains are consistent across different parameter configurations. This is particularly important for a method that combines two complex models, as the interaction between their hyperparameters can be non-trivial.
3. The paper does not provide a detailed analysis of the limitations of the proposed framework, such as its performance on different types of urban data or its robustness to noisy or incomplete data. For example, it is unclear how the framework would perform in scenarios with highly sparse or irregular spatial data, or in the presence of adversarial attacks that could compromise the integrity of the input data. A more thorough discussion of these limitations would provide a more balanced view of the proposed approach.

### Suggestions

The paper should include a more detailed analysis of the computational complexity of the STLLM framework. This should include a breakdown of the time and memory requirements for each component, such as the LLM inference, GNN training, and the mutual information maximization process. The authors should also provide a comparison of the computational cost of STLLM with other state-of-the-art methods, especially those that also use LLMs or GNNs. This analysis should consider the impact of different dataset sizes and feature dimensions on the computational cost. Furthermore, the authors should discuss potential strategies for optimizing the computational efficiency of the framework, such as using more efficient LLM architectures or GNN training techniques. This would make the proposed approach more practical for real-world applications with large-scale urban datasets.

To address the lack of sensitivity analysis, the authors should conduct a thorough investigation of how the performance of STLLM varies with different hyperparameter settings. This should include a systematic exploration of the learning rate, the number of layers in the GNN, and the size of the LLM. The authors should also investigate the impact of different activation functions, regularization techniques, and optimization algorithms. The results of this sensitivity analysis should be presented in a clear and concise manner, such as through tables or graphs, and should include a discussion of the optimal hyperparameter settings for different tasks. This would provide a more robust understanding of the performance of STM and its applicability to different scenarios. The authors should also discuss the potential trade-offs between different hyperparameter settings and their impact on the overall performance of the framework.

Finally, the paper should include a more detailed discussion of the limitations of the proposed framework. This should include an analysis of the performance of STLLM on different types of urban data, such as highly sparse or irregular spatial data, and in the presence of noisy or incomplete data. The authors should also discuss the robustness of the framework to adversarial attacks and other forms of data corruption. This discussion should be supported by experimental results or simulations that demonstrate the performance of STLLM under different conditions. The authors should also suggest potential directions for future research that could address these limitations and improve the robustness and generalizability of the proposed approach.

### Questions

1. How does the proposed framework handle the curse of dimensionality in high-dimensional spatio-temporal data?
2. How does the proposed framework ensure the privacy of the data, especially when dealing with sensitive information such as crime data or traffic patterns?
3. How does the proposed framework handle the uncertainty and noise in the data, especially when dealing with real-world datasets?

### Rating

6

### Confidence

4

**********
