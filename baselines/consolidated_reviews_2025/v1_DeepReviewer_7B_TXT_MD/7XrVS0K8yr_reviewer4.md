### Summary

The paper introduces Secure Floating (FLOATING), a framework designed to enhance the trustworthiness of mobility data from connected and autonomous vehicles (CAVs) and other mobile devices in real-time. FLOATING addresses the critical need for reliable and trustworthy mobility data by leveraging federated learning and blockchain technology. The framework ensures data privacy through lightweight Secure Multi-Party Computation (SMPC) and robustness through verifiable federated learning (VFL), allowing nodes to collaborate and validate each other’s trajectory data without compromising sensitive information. FLOATING is evaluated using real-world data from New York City, involving up to 8,000 nodes, and demonstrates promising results in terms of accuracy, privacy preservation, robustness, and scalability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to verifying the trustworthiness of mobility data from connected and autonomous vehicles (CAVs) and other mobile devices in real-time. FLOATING addresses the critical need for reliable and trustworthy mobility data by leveraging federated learning and blockchain technology. The framework ensures data privacy through lightweight Secure Multi-Party Computation (SMPC) and robustness through verifiable federated learning (VFL), allowing nodes to collaborate and validate each other’s trajectory data without compromising sensitive information.

2. The paper is well-written and easy to follow. The authors provide a clear and concise explanation of the proposed framework, making it accessible to a wide audience. The use of diagrams and examples helps to illustrate the key concepts and mechanisms of FLOATING.

3. The paper provides a thorough evaluation of FLOATING using real-world data from New York City, involving up to 8,000 nodes. The evaluation demonstrates the effectiveness of FLOATING in terms of accuracy, privacy preservation, robustness, and scalability. The results show that FLOATING outperforms existing approaches in terms of accuracy and overhead, while ensuring privacy guarantees.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the specific challenges and limitations of applying FLOATING in real-world scenarios, such as the impact of varying network conditions, data quality, and the potential for adversarial attacks.

2. The scalability of FLOATING is mentioned as a key advantage, but the paper lacks a thorough analysis of how the framework performs under different network topologies and scales with the number of nodes.

3. The paper does not provide a comprehensive comparison with existing approaches for verifying mobility data, which makes it difficult to assess the novelty and effectiveness of FLOATING in the context of the broader literature.

4. The theoretical analysis of the communication overhead is limited to a linear growth with the number of nodes, but it does not provide a detailed analysis of the constant factor involved, which is crucial for practical implementation.

5. The paper lacks a discussion on the computational overhead of FLOATING, which is an important factor to consider for real-time applications in resource-constrained environments.

### Suggestions

The paper should include a more thorough discussion of the practical challenges that FLOATING might face in real-world deployments. For example, the impact of intermittent connectivity, varying network latency, and the potential for packet loss should be addressed. Furthermore, the paper should discuss how FLOATING handles noisy or incomplete trajectory data, which is common in real-world scenarios. The authors should also consider the potential for adversarial attacks, such as data poisoning or manipulation, and how FLOATING can detect and mitigate these threats. A more detailed analysis of the system's robustness against such attacks would significantly strengthen the paper.

To address the scalability concerns, the paper should provide a more detailed analysis of how FLOATING performs under different network topologies. This should include an evaluation of the framework's performance in scenarios with varying degrees of network density and connectivity. The authors should also discuss the communication overhead of FLOATING as the number of nodes increases, including the constant factor involved in the linear growth. This analysis should consider the practical implications of the communication overhead for real-time applications, especially in resource-constrained environments. Furthermore, the paper should discuss the computational overhead of FLOATING, including the computational resources required for federated learning and blockchain operations. This analysis should consider the practical implications of the computational overhead for real-time applications in resource-constrained environments.

Finally, the paper should include a more comprehensive comparison with existing approaches for verifying mobility data. This comparison should not only focus on the theoretical aspects but also on the practical performance of the proposed framework. The authors should discuss the advantages and disadvantages of FLOATING compared to other methods, highlighting the specific scenarios where FLOATING excels or falls short. This comparison should include a discussion of the trade-offs between privacy, accuracy, and computational overhead. A more detailed comparison with existing approaches would help to better position FLOATING within the broader literature and highlight its unique contributions.

### Questions

1. How does FLOATING handle scenarios where the data quality is poor or the network conditions are unreliable?

2. What are the specific assumptions made about the data and the environment in the FLOATING framework?

3. How does FLOATING compare with other existing approaches for verifying mobility data in terms of accuracy, privacy, and computational efficiency?

4. What are the potential limitations and ethical considerations of FLOATING in real-world applications?

5. How does FLOATING ensure the fairness and transparency of the verification process?

### Rating

6

### Confidence

4

**********
