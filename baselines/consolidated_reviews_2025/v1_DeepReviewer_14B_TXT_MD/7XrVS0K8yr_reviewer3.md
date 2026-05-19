### Summary

This paper introduces Secure-FLOATING, a framework designed to establish real-time trust in mobility data for connected and autonomous vehicles (CAVs), micro-mobility devices, and smartphone users. The framework combines federated learning, blockchain, and secure multi-party computation (SMPC) to enable nearby nodes to coordinate and learn to trust each other's mobility data without compromising privacy. The paper evaluates Secure-FLOATING using realistic trajectories for up to 8,000 nodes in New York City, demonstrating its ability to achieve lower delays and overhead while maintaining high accuracy in data validation, even with a significant portion of malicious actors.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces Secure-FLOATING, a novel framework that combines federated learning, blockchain, and secure multi-party computation (SMPC) to establish real-time trust in mobility data.
2. The paper provides a theoretical analysis of the framework's privacy guarantees, security, and scalability, demonstrating its robustness and potential for real-world applications.
3. The paper evaluates Secure-FLOATING using realistic trajectories for up to 8,000 nodes in New York City, demonstrating its ability to achieve lower delays and overhead while maintaining high accuracy in data validation, even with a significant portion of malicious actors.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes. It is unclear how the framework handles potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process. Specifically, the paper lacks a discussion on the specific type of secret sharing scheme used (e.g., additive, Shamir) and how the reconstruction of the global model is performed. Furthermore, the paper does not address the potential for inference attacks, where an adversary could infer sensitive information about other nodes based on the shared model updates.
2. The paper could provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes. It is unclear how the framework handles potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process. The paper should elaborate on the specific mechanisms used to verify the correctness of local model updates and how the framework prevents malicious nodes from injecting false data into the global model. Additionally, the paper does not discuss the impact of node failures or malicious nodes on the overall performance and security of the SMPC protocol. The paper should also address the potential for inference attacks, where an adversary could infer sensitive information about other nodes based on the shared model updates.
3. While the paper mentions the use of zero-knowledge proofs, it could provide more details on how they are integrated into the framework and their impact on performance. The paper should specify the type of zero-knowledge proofs used (e.g., interactive or non-interactive) and how they are applied to verify the correctness of local model updates without revealing the actual updates. The paper should also provide a more detailed analysis of the computational overhead introduced by the zero-knowledge proofs and how this overhead scales with the number of nodes and the complexity of the model. It is unclear how the zero-knowledge proofs are used to ensure the integrity of the model updates and how they prevent malicious nodes from manipulating the global model.

### Suggestions

The paper should provide a more detailed explanation of the secure multi-party computation (SMPC) protocol, including the specific cryptographic primitives used, such as the type of secret sharing scheme (e.g., additive, Shamir) and the method for reconstructing the global model. It should also clarify the communication patterns between nodes, detailing how shares are distributed and combined. Furthermore, the paper needs to address potential vulnerabilities, such as node collusion and data poisoning attacks, by explaining the mechanisms used to verify the correctness of local model updates. This could involve describing techniques like differential privacy or secure aggregation rules that prevent malicious nodes from injecting false data into the global model. The paper should also discuss the impact of node failures or malicious nodes on the overall performance and security of the SMPC protocol, and how the framework mitigates these risks. For example, the paper could explore the use of techniques such as verifiable secret sharing or robust aggregation rules to enhance the security and reliability of the SMPC protocol. Additionally, the paper should address the potential for inference attacks, where an adversary could infer sensitive information about other nodes based on the shared model updates, and propose mitigation strategies.

To enhance the practical applicability of the proposed framework, the paper should provide a more detailed analysis of the computational overhead introduced by the zero-knowledge proofs (ZKPs). This analysis should include a discussion of the specific type of ZKPs used (e.g., interactive or non-interactive) and how they are applied to verify the correctness of local model updates without revealing the actual updates. The paper should also provide a more detailed analysis of the computational overhead introduced by the zero-knowledge proofs and how this overhead scales with the number of nodes and the complexity of the model. It is crucial to understand the trade-offs between security, privacy, and performance in the proposed framework. For example, the paper could explore the use of more efficient ZKP schemes or techniques to reduce the computational burden on individual nodes. The paper should also discuss how the zero-knowledge proofs are used to ensure the integrity of the model updates and how they prevent malicious nodes from manipulating the global model. This could involve describing the specific cryptographic primitives and protocols used to achieve this goal.

Finally, the paper should include a more comprehensive experimental evaluation that includes a wider range of datasets and scenarios. This would help to demonstrate the robustness and generalizability of the proposed framework. The evaluation should also include a detailed analysis of the performance of the framework under different attack scenarios, such as data poisoning attacks and node collusion. The paper should also compare the performance of the proposed framework with existing approaches, highlighting its advantages and limitations. This would provide a more complete picture of the strengths and weaknesses of the proposed framework and help to identify areas for future research. The evaluation should also include a detailed analysis of the computational overhead introduced by the zero-knowledge proofs and how this overhead scales with the number of nodes and the complexity of the model.

### Questions

1. Could the authors provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes?
2. How does the framework handle potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process?
3. What is the impact of zero-knowledge proofs on the performance of the framework, and how do they scale with the number of nodes?
4. What are the trade-offs between security, privacy, and performance in the proposed framework, and how do the authors balance these factors in their design choices?

### Rating

3

### Confidence

3

**********
