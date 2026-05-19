### Summary

This paper introduces a new federated learning setting called Modality-Collaborated Federated Learning (MCFL), where clients only possess data from a single modality. The authors propose FedCola, a framework based on modality-agnostic transformers, to address the challenges of model heterogeneity and modality gaps in MCFL. The paper presents comprehensive evaluations that demonstrate the effectiveness of FedCola in terms of performance and efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel federated learning setting called Modality-Collaborated Federated Learning (MCFL), which focuses on enabling collaboration among clients with uni-modal data to benefit all modalities. This setting addresses a practical scenario where clients have uni-modal data and aims to facilitate collaboration among them while ensuring privacy.

2. The paper proposes a framework called FedCola, which leverages modality-agnostic transformers to address the challenges of model heterogeneity and modality gaps in MCFL. The authors conduct comprehensive evaluations that demonstrate the effectiveness of FedCola in terms of performance and efficiency.

3. The paper is well-written and organized, making it easy to follow and understand.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed FedCola framework, especially in comparison to existing methods. Specifically, the paper lacks a breakdown of the computational cost associated with the modality-agnostic transformer, including the number of parameters, FLOPs, and memory requirements. This makes it difficult to assess the practical feasibility of the approach, particularly for resource-constrained devices. Furthermore, the paper does not discuss the impact of the transformer's architecture on the overall computational cost, such as the number of layers and attention heads.

2. The paper does not provide a comprehensive comparison of the proposed FedCola framework with other state-of-the-art federated learning methods. While the paper compares FedCola with Uni-FedAVG and CreamFL, it does not include comparisons with other relevant methods, such as those that use model aggregation techniques or those that explicitly address model heterogeneity. This makes it difficult to assess the relative advantages and disadvantages of FedCola compared to the broader landscape of federated learning algorithms. The paper should also discuss the limitations of the proposed method in comparison to other approaches.

3. The paper does not provide a detailed analysis of the communication overhead of the proposed FedCola framework. While the paper mentions that the framework is communication-efficient, it does not provide a quantitative analysis of the communication cost, including the number of bits transmitted per round and the impact of different communication protocols. This makes it difficult to assess the practical viability of the approach in scenarios with limited bandwidth or high latency. The paper should also discuss the impact of the transformer's architecture on the communication overhead.

### Suggestions

The paper should include a more detailed analysis of the computational complexity of the FedCola framework. This analysis should include a breakdown of the computational cost associated with the modality-agnostic transformer, including the number of parameters, FLOPs, and memory requirements. The authors should also discuss the impact of the transformer's architecture on the overall computational cost, such as the number of layers and attention heads. Furthermore, the paper should provide a comparison of the computational cost of FedCola with other state-of-the-art federated learning methods, including both model-agnostic and model-agnostic approaches. This would allow readers to better understand the trade-offs between performance and computational cost when choosing a federated learning framework. The analysis should also consider the impact of different hardware platforms and resource constraints on the practical feasibility of the proposed approach.

To address the lack of comprehensive comparison with other state-of-the-art federated learning methods, the paper should include a more extensive experimental evaluation that compares FedCola with a wider range of baselines. This should include methods that use different model aggregation techniques, such as FedAvg, SCAFFOLD, and FedProx, as well as methods that explicitly address model heterogeneity, such as those based on adaptive learning rates or knowledge distillation. The paper should also discuss the limitations of the proposed method in comparison to other approaches, highlighting the specific scenarios where FedCola may not be the most suitable choice. This would provide a more balanced and comprehensive assessment of the proposed framework and its place in the broader landscape of federated learning algorithms.

The paper should also provide a more detailed analysis of the communication overhead of the proposed FedCola framework. This analysis should include a quantitative assessment of the communication cost, including the number of bits transmitted per round and the impact of different communication protocols. The authors should also discuss the impact of the transformer's architecture on the communication overhead. Furthermore, the paper should consider the practical implications of the communication overhead in scenarios with limited bandwidth or high latency. The analysis should also include a discussion of potential strategies for reducing the communication overhead, such as model compression or quantization techniques. This would allow readers to better understand the trade-offs between communication cost and model performance when choosing a federated learning framework.

### Questions

1. How does the proposed FedCola framework handle the issue of data heterogeneity across modalities? Specifically, how does FedCola perform when the data distributions across modalities are significantly different?

2. What is the computational cost of training and deploying the modality-agnostic transformer? How does this cost scale with the number of modalities and the size of the data?

3. How does FedCola compare to other state-of-the-art federated learning methods in terms of performance, computational cost, and communication overhead?

### Rating

6

### Confidence

3

**********
