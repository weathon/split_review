### Summary

The paper proposes a system for verifying the trustworthiness of mobility data from various sources, such as connected vehicles, micro-mobility devices, and smartphone users, in real-time. The system utilizes federated learning and secure multi-party computation to ensure data privacy and integrity. The authors claim that the proposed approach is scalable, with a communication overhead that grows linearly with the number of nodes in the network. The evaluation is conducted using real-world data from New York City, involving up to 8,000 nodes.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper addresses a significant problem in the field of connected and autonomous vehicles, particularly the need for a decentralized and privacy-preserving system for verifying the trustworthiness of mobility data. The use of federated learning and secure multi-party computation is a relevant and promising approach to tackle this challenge.

### Weaknesses

#### Some Related Works


#### comment

The paper presents a system for verifying the trustworthiness of mobility data, but it lacks a thorough discussion of the specific threats it aims to mitigate. A clear articulation of the security goals and the potential attacks the system is designed to defend against would enhance the paper's clarity and impact. The paper does not adequately address the potential vulnerabilities of the proposed system to common attacks in the context of federated learning and secure multi-party computation. For example, the paper does not discuss the potential for Sybil attacks, where malicious actors create multiple identities to compromise the system, or the impact of data poisoning attacks, where malicious actors inject false data to degrade the performance of the federated learning model. Furthermore, the paper does not consider the potential for model inversion attacks, where an attacker attempts to reconstruct the private data of the participants from the shared model updates. These omissions weaken the security analysis of the proposed system.

The evaluation of the system is based on real-world data from New York City, but the paper does not provide sufficient details about the data collection process, the characteristics of the data, or the specific scenarios in which the system was tested. The paper lacks a detailed analysis of the system's performance under various conditions, such as different network topologies, data distributions, and attack scenarios. The evaluation should include a more comprehensive set of experiments to demonstrate the robustness and scalability of the proposed system. The paper should also provide a more detailed comparison with existing approaches in the field, highlighting the advantages and limitations of the proposed system.

While the paper claims that the system is scalable, the theoretical analysis of the communication overhead is not sufficiently rigorous. The paper should provide a more detailed analysis of the communication complexity of the system, including the number of messages exchanged between the nodes and the size of these messages. The paper should also consider the impact of network latency and bandwidth limitations on the performance of the system. The paper should also discuss the limitations of the proposed approach, such as the computational overhead of the federated learning and secure multi-party computation protocols, and the potential for privacy breaches under certain conditions.

### Suggestions

To enhance the paper, the authors should provide a more detailed discussion of the security goals and the specific threats that the proposed system is designed to mitigate. This should include a clear articulation of the security model, specifying the assumptions about the adversary and the capabilities of the system. The authors should also discuss the potential vulnerabilities of the system to common attacks in the context of federated learning and secure multi-party computation, such as Sybil attacks, data poisoning attacks, and model inversion attacks. Furthermore, the authors should provide a more rigorous analysis of the system's security properties, including a formal proof of the system's resistance to these attacks. This analysis should consider the specific mechanisms used in the system, such as the federated learning algorithm, the secure multi-party computation protocol, and the data verification mechanism. The authors should also discuss the limitations of the proposed approach and the potential for privacy breaches under certain conditions.

The evaluation of the system should be significantly expanded to include a more comprehensive set of experiments. This should include a detailed analysis of the system's performance under various conditions, such as different network topologies, data distributions, and attack scenarios. The authors should also provide a more detailed comparison with existing approaches in the field, highlighting the advantages and limitations of the proposed system. The evaluation should include a quantitative analysis of the system's performance, such as the accuracy of the federated learning model, the communication overhead, and the time complexity of the system. The authors should also provide a qualitative analysis of the system's performance, such as the impact of the system on the trustworthiness of the mobility data. The evaluation should also consider the impact of different parameters, such as the number of nodes, the size of the dataset, and the communication bandwidth, on the performance of the system.

The theoretical analysis of the communication overhead should be more rigorous and should consider the specific mechanisms used in the system. The authors should provide a more detailed analysis of the communication complexity of the system, including the number of messages exchanged between the nodes and the size of these messages. The authors should also consider the impact of network latency and bandwidth limitations on the performance of the system. The authors should also discuss the limitations of the proposed approach, such as the computational overhead of the federated learning and secure multi-party computation protocols, and the potential for privacy breaches under certain conditions. The authors should also provide a more detailed analysis of the system's scalability, including the number of nodes that can be supported by the system and the communication overhead as the number of nodes increases.

### Questions

1. How does the proposed system defend against potential security threats, such as Sybil attacks, data poisoning attacks, and model inversion attacks?
2. What are the specific scenarios in which the proposed system was tested, and what are the characteristics of the data used in the evaluation?
3. What is the communication overhead of the system, and how does it scale with the number of nodes in the network?
4. How does the system ensure the privacy of the participants, and what are the limitations of the privacy guarantees provided by the system?

### Rating

3

### Confidence

4

**********
