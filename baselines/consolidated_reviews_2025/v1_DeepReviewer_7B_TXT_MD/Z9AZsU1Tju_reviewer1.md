### Summary

This paper proposes a novel Information-Theoretic Hierarchical Perception (ITHP) model for multimodal learning. The ITHP model utilizes the concept of information bottleneck to construct compact latent states for different modalities, enabling a hierarchical fusion of multimodal information. The model is designed to distill relevant information from multiple modalities in a sequential manner, mimicking a hierarchical information processing approach observed in human cognition and neural systems. The authors evaluate the proposed model on three multimodal datasets: MUStARD, MOSI, and MOSEI, focusing on tasks such as sarcasm detection, sentiment analysis, and emotion recognition. The results demonstrate that ITHP achieves competitive performance compared to existing multimodal fusion methods and, in some cases, even surpasses human-level benchmarks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper introduces a novel approach to multimodal fusion by integrating the information bottleneck principle, which is an innovative perspective in multimodal learning. The hierarchical structure of the model, inspired by neural information processing, offers a unique way to manage and integrate information from multiple modalities.
- The paper provides a thorough explanation of the theoretical foundations of the ITHP model, including the formulation of optimization problems and the derivation of loss functions. The use of Lagrangian multipliers to balance information retention and compression is well-justified.
- The empirical evaluation of ITHP is conducted on multiple benchmark datasets (MUStARD, MOSI, MOSEI), covering a range of multimodal tasks (sarcasm detection, sentiment analysis, emotion recognition). The model demonstrates competitive performance, often outperforming existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper claims that the ITHP model outperforms human-level benchmarks in sarcasm detection on the MUStARD dataset. However, the comparison is made against other machine learning models, not actual human performance data. This claim is not well-supported and requires further clarification or justification.
- The paper lacks a detailed analysis of the computational complexity and scalability of the ITHP model. Given the hierarchical structure and multiple latent states, it is important to understand the computational cost and potential bottlenecks, especially for larger datasets or real-time applications.
- The paper does not provide a comprehensive ablation study to analyze the contribution of each component of the ITHP model. For example, the impact of the hierarchical structure, the information bottleneck principle, and different loss functions could be investigated separately to better understand their individual contributions to the overall performance.
- The paper does not discuss the limitations of the ITHP model or potential failure cases. It would be beneficial to analyze scenarios where the model might struggle, such as with noisy or ambiguous data, or with modalities that are significantly different from the training data.

### Suggestions

The paper should provide a more rigorous justification for the claim that the ITHP model outperforms human-level benchmarks. This could involve referencing existing studies that have measured human performance on sarcasm detection tasks and comparing the ITHP model's performance against these reported human benchmarks. If such data is not available, the authors should clearly state that the comparison is against other machine learning models and avoid making claims of human-level performance without proper justification. Furthermore, the paper should include a more detailed analysis of the computational complexity and scalability of the ITHP model. This analysis should consider the number of parameters, the computational cost of each layer, and the overall training and inference time. It would be beneficial to provide a comparison of the computational cost of the ITHP model with other state-of-the-art multimodal fusion methods. The authors should also discuss potential bottlenecks in the model that could limit its scalability and explore possible solutions, such as model parallelism or distributed training.

To better understand the contribution of each component of the ITHP model, a comprehensive ablation study is necessary. This study should systematically remove or modify different parts of the model, such as the hierarchical structure, the information bottleneck principle, and different loss functions, and evaluate the impact on the overall performance. For example, the authors could compare the performance of the full ITHP model with a version that uses a single latent state, or a version that does not use the information bottleneck principle. This would help to isolate the contribution of each component and provide a more detailed understanding of the model's behavior. The ablation study should also include an analysis of the sensitivity of the model to different hyperparameters, such as the Lagrange multipliers, and provide guidelines for selecting optimal values.

Finally, the paper should include a discussion of the limitations of the ITHP model and potential failure cases. This discussion should analyze scenarios where the model might struggle, such as with noisy or ambiguous data, or with modalities that are significantly different from the training data. For example, the authors could investigate the model's performance on datasets with high levels of noise or with modalities that have different characteristics than those used in the training data. The authors should also discuss the potential for the model to overfit to the training data and propose strategies to mitigate this risk. This discussion should provide a more balanced and realistic assessment of the model's capabilities and limitations.

### Questions

- How does the ITHP model handle situations where the primary modality lacks sufficient information, requiring significant contributions from other modalities? Are there specific mechanisms or constraints within the model to address this?
- Could you provide more details on the computational complexity and scalability of the ITHP model, especially for larger datasets or real-time applications?
- What are the potential limitations of the ITHP model, and in what scenarios might it fail to perform well? How sensitive is the model to the choice of hyperparameters, such as the Lagrange multipliers?

### Rating

5

### Confidence

3

**********
