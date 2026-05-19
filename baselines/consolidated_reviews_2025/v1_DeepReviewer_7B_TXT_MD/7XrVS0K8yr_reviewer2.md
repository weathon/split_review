### Summary

The paper proposes a blockchain-based system for verifying the trustworthiness of mobility data from connected vehicles and other mobile devices. The system uses federated learning and secure multi-party computation to ensure data privacy and integrity, and it is evaluated using real-world data from New York City.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a timely and important problem of ensuring the trustworthiness of mobility data in the context of connected and autonomous vehicles.
2. The use of federated learning and secure multi-party computation is a relevant and promising approach to tackle this challenge.
3. The evaluation is conducted using real-world data from New York City, which adds credibility to the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the specific threats it aims to mitigate. A clear articulation of the security goals and the potential attacks the system is designed to defend against would enhance the paper's clarity and impact.
2. The paper does not adequately address the potential vulnerabilities of the proposed system to common attacks in the context of federated learning and secure multi-party computation. For example, the paper does not discuss the potential for Sybil attacks, where malicious actors create multiple identities to compromise the system, or the impact of data poisoning attacks, where malicious actors inject false data to degrade the performance of the federated learning model. Furthermore, the paper does not consider the potential for model inversion attacks, where an attacker attempts to reconstruct the private data of the participants from the shared model updates.
3. The evaluation of the system is based on real-world data from New York City, but the paper does not provide sufficient details about the data collection process, the characteristics of the data, or the specific scenarios in which the system was tested. The paper lacks a detailed analysis of the system's performance under various conditions, such as different network topologies, data distributions, and attack scenarios. The evaluation should include a more comprehensive set of experiments to demonstrate the robustness and scalability of the proposed system.
4. While the paper claims that the system is scalable, the theoretical analysis of the communication overhead is not sufficiently rigorous. The paper should provide a more detailed analysis of the communication complexity of the system, including the number of messages exchanged between the nodes and the size of these messages. The paper should also consider the impact of network latency and bandwidth limitations on the performance of the system. The paper should also discuss the limitations of the proposed approach, such as the computational overhead of the federated learning and secure multi-party computation protocols, and the potential for privacy breaches under certain conditions.

### Suggestions

The paper should provide a more detailed discussion of the security goals and the specific threats that the proposed system is designed to mitigate. This should include a clear articulation of the security model, specifying the assumptions about the adversary and the capabilities of the system. The authors should also discuss the potential vulnerabilities of the system to common attacks in the context of federated learning and secure multi-party computation, such as Sybil attacks, data poisoning attacks, and model inversion attacks. Furthermore, the paper should provide a more rigorous analysis of the system's security properties, including a formal proof of the system's resistance to these attacks. This analysis should consider the specific mechanisms used in the system, such as the federated learning algorithm, the secure multi-party computation protocol, and the data verification mechanism. The authors should also discuss the limitations of the proposed approach and the potential for privacy breaches under certain conditions.

The evaluation of the system should be significantly expanded to include a more comprehensive set of experiments. This should include a detailed analysis of the system's performance under various conditions, such as different network topologies, data distributions, and attack scenarios. The authors should also provide a more detailed description of the data collection process, including the characteristics of the data used in the evaluation. The evaluation should include a quantitative analysis of the system's performance, such as the accuracy of the federated learning model, the communication overhead, and the time complexity of the system. The authors should also provide a qualitative analysis of the system's performance, such as the impact of the system on the trustworthiness of the mobility data. The evaluation should also consider the impact of different parameters, such as the number of nodes, the size of the dataset, and the communication bandwidth, on the performance of the system.

The theoretical analysis of the communication overhead should be more rigorous and should consider the specific mechanisms used in the system. The authors should provide a more detailed analysis of the communication complexity of the system, including the number of messages exchanged between the nodes and the size of these messages. The authors should also consider the impact of network latency and bandwidth limitations on the performance of the system. The authors should also discuss the limitations of the proposed approach, such as the computational overhead of the federated learning and secure multi-party computation protocols, and the potential for privacy breaches under certain conditions. The paper should also provide a more detailed analysis of the system's scalability, including the number of nodes that can be supported by the system and the communication overhead as the number of nodes increases.

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
