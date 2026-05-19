### Summary

The paper proposes a framework called Secure Floating (FLOATING) for verifying the trustworthiness of mobility data from connected and autonomous vehicles (CAVs) and other mobile devices in real-time. FLOATING leverages federated learning and blockchain technology to ensure data privacy and integrity, allowing nodes to collaborate and validate each other's trajectory data without compromising sensitive information. The framework is evaluated using real-world data from New York City, involving up to 8,000 nodes, and shows promising results in terms of accuracy, privacy preservation, robustness, and scalability.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses a critical issue in the field of connected and autonomous vehicles by proposing a decentralized framework for verifying the trustworthiness of mobility data, which is essential for ensuring safety and reliability in real-world applications.
- The use of federated learning and blockchain technology is innovative and aligns with the current trends in data privacy and security, making FLOATING a relevant and timely contribution to the literature.
- The evaluation using real-world data from New York City adds credibility to the findings and demonstrates the practical applicability of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the specific challenges and limitations of applying FLOATING in real-world scenarios, such as the impact of varying network conditions, data quality, and the potential for adversarial attacks.
- The scalability of FLOATING is mentioned as a key advantage, but the paper lacks a thorough analysis of how the framework performs under different network topologies and scales with the number of nodes.
- The paper does not provide a comprehensive comparison with existing approaches for verifying mobility data, which makes it difficult to assess the novelty and effectiveness of FLOATING in the context of the broader literature.
- The theoretical analysis of the communication overhead is limited to a linear growth with the number of nodes, but it does not provide a detailed analysis of the constant factor involved, which is crucial for practical implementation.
- The paper lacks a discussion on the computational overhead of FLOATING, which is an important factor to consider for real-time applications in resource-constrained environments.

### Suggestions

The paper should include a more thorough discussion of the practical challenges encountered when deploying FLOATING in real-world scenarios. For instance, the impact of varying network conditions, such as intermittent connectivity or high latency, on the system's performance should be analyzed. Furthermore, the paper should address the potential for data quality issues, such as noisy or incomplete trajectory data, and how FLOATING handles these scenarios. A detailed analysis of the system's robustness against adversarial attacks, including data poisoning or manipulation, is also necessary. This should include a discussion of the specific mechanisms used to detect and mitigate such attacks, and the potential impact of these attacks on the overall trustworthiness of the system. The paper should also provide a more detailed analysis of the scalability of FLOATING, including how the framework performs under different network topologies and how the communication overhead scales with the number of nodes. This analysis should include a discussion of the constant factor involved in the linear growth of communication overhead, which is crucial for practical implementation. 

To address the lack of comparison with existing approaches, the paper should include a comprehensive comparison with state-of-the-art methods for verifying mobility data. This comparison should not only focus on the theoretical aspects but also on the practical performance of the proposed framework. The paper should clearly articulate the advantages and disadvantages of FLOATING compared to existing methods, highlighting the specific scenarios where FLOATING excels or falls short. This comparison should include a discussion of the trade-offs between privacy, accuracy, and computational overhead. Furthermore, the paper should provide a more detailed analysis of the computational overhead of FLOATING, including the computational cost of federated learning and blockchain operations. This analysis should consider the computational resources required for real-time applications in resource-constrained environments, such as mobile devices or embedded systems. The paper should also discuss the potential for optimizing the computational efficiency of FLOATING, such as through the use of lightweight machine learning algorithms or distributed computing techniques.

Finally, the paper should include a more detailed discussion of the limitations of FLOATING, including the assumptions made about the data and the environment. The paper should also discuss the potential for future research directions, such as the integration of FLOATING with other privacy-enhancing technologies or the development of more robust and efficient algorithms for federated learning and blockchain. The paper should also discuss the ethical implications of FLOATING, including the potential for bias in the data or the misuse of the system for malicious purposes. A thorough discussion of these limitations and ethical considerations is essential for ensuring the responsible development and deployment of FLOATING.

### Questions

- How does FLOATING handle scenarios where the data quality is poor or the network conditions are unreliable?
- What are the specific assumptions made about the data and the environment in the FLOATING framework?
- How does FLOATING compare with other existing approaches for verifying mobility data in terms of accuracy, privacy, and computational efficiency?
- What are the potential limitations and ethical considerations of FLOATING in real-world applications?
- How does FLOATING ensure the fairness and transparency of the verification process?

### Rating

5

### Confidence

4

**********
