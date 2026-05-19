### Summary

This paper introduces Secure-FLOATING, a framework designed to establish trust in real-time mobility data for applications involving Connected and Autonomous Vehicles (CAVs) and other road users. The framework combines federated learning, blockchain, and secure multi-party computation (SMPC) to ensure data privacy and validation. The authors evaluate Secure-FLOATING using realistic trajectories in New York City, demonstrating its scalability and robustness against malicious data, achieving up to 75% successful endorsement even with 50% attacker penetration.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper presents a novel approach by combining federated learning, blockchain, and SMPC to ensure data privacy and trust in real-time mobility data.
2. The framework is evaluated using realistic trajectories in New York City, demonstrating its scalability and robustness against malicious data.
3. The paper provides a theoretical analysis of the framework's privacy guarantees and scalability, adding rigor to the proposed solution.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed framework, such as its performance in highly dense or sparse networks, and how it handles node heterogeneity. Specifically, the paper lacks an analysis of how the framework's performance degrades with increasing network density, particularly concerning communication overhead and latency. Furthermore, the paper does not address the impact of varying computational capabilities and data availability across different nodes, which is a common challenge in real-world vehicular networks.
2. The experimental evaluation could be expanded to include comparisons with a broader range of existing trust models and security frameworks for CAVs. The current evaluation lacks a direct comparison with established trust management systems, making it difficult to assess the relative advantages and disadvantages of the proposed approach. A more comprehensive benchmark against state-of-the-art solutions would strengthen the paper's claims.
3. The paper could provide more details on the practical implementation of the framework, including the specific hardware and software requirements for deployment in real-world scenarios. The paper does not specify the computational resources required for the proposed framework, such as CPU, memory, and storage, which are critical for real-world deployment. Additionally, the paper lacks details on the software stack and communication protocols needed to implement the framework in a practical setting.

### Suggestions

To address the limitations regarding network density and node heterogeneity, the authors should conduct a more thorough analysis of the framework's performance under varying network conditions. This should include simulations or experiments that systematically vary the density of nodes and evaluate the impact on communication overhead, latency, and overall trust establishment. The analysis should also consider the effects of node heterogeneity, such as differences in computational power, storage capacity, and data availability. For instance, the authors could explore how the framework performs when some nodes have limited processing capabilities or when data distribution is highly skewed across the network. This would provide a more realistic assessment of the framework's robustness and scalability in practical scenarios. Furthermore, the paper should discuss potential mitigation strategies for addressing performance degradation in highly dense or heterogeneous networks, such as adaptive communication protocols or load balancing techniques.

To strengthen the experimental evaluation, the authors should include a more comprehensive comparison with existing trust models and security frameworks for CAVs. This comparison should not only focus on the performance metrics but also on the security guarantees, privacy preservation, and computational overhead of different approaches. The authors should select a range of representative baseline methods, including both centralized and decentralized solutions, and provide a detailed analysis of their strengths and weaknesses compared to the proposed framework. This would allow readers to better understand the relative advantages and disadvantages of Secure-FLOATING and its suitability for different application scenarios. The comparison should also include a discussion of the trade-offs between security, privacy, and performance, highlighting the specific contexts in which the proposed framework is most effective.

Finally, the paper should provide more concrete details on the practical implementation of the framework, including the specific hardware and software requirements for deployment in real-world scenarios. This should include a detailed description of the computational resources needed for the framework, such as CPU, memory, and storage, as well as the software stack and communication protocols required for implementation. The authors should also discuss the practical challenges of deploying the framework in a real-world vehicular network, such as the management of cryptographic keys, the handling of node failures, and the integration with existing vehicle infrastructure. This would make the paper more accessible to practitioners and facilitate the adoption of the proposed framework in real-world applications.

### Questions

1. How does Secure-FLOATING perform in highly dense or sparse networks, and what are the limitations in such scenarios?
2. Can the authors provide more details on the practical implementation of the framework, including the specific hardware and software requirements for deployment in real-world scenarios?
3. How does the framework handle node heterogeneity, and what are the implications for trust establishment and data validation?

### Rating

3

### Confidence

5

**********
