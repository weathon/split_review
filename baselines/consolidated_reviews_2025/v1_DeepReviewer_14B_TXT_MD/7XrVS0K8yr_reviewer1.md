### Summary

The paper proposes Secure-FLOATING, a framework for real-time trust verification in mobility data from connected and autonomous vehicles (CAVs) and other road users. It combines federated learning, blockchain, and secure multi-party computation (SMPC) to ensure data privacy and integrity. The framework is evaluated using realistic trajectories in New York City, demonstrating low delays and high scalability.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces Secure-FLOATING, a novel framework that combines federated learning, blockchain, and secure multi-party computation (SMPC) to ensure real-time trust verification in mobility data while preserving user privacy.
2. The framework is rigorously evaluated using realistic trajectories in New York City, demonstrating its effectiveness in handling up to 8,000 nodes with low delays and high scalability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes. It is unclear how the framework handles potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process. Specifically, the paper lacks details on how the secret shares are generated and distributed, and how the reconstruction of the global model is performed. Furthermore, the paper does not discuss the impact of node failures or malicious nodes on the overall performance and security of the SMPC protocol.
2. The paper could provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes. It is unclear how the framework handles potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process. The paper should elaborate on the specific mechanisms used to verify the correctness of local model updates and how the framework prevents malicious nodes from injecting false data into the global model. Additionally, the paper does not discuss the impact of node failures or malicious nodes on the overall performance and security of the SMPC protocol. The paper should also address the potential for inference attacks, where an adversary could infer sensitive information about other nodes based on the shared model updates.
3. While the paper mentions the use of zero-knowledge proofs, it could provide more details on how they are integrated into the framework and their impact on performance. The paper should specify the type of zero-knowledge proofs used (e.g., interactive or non-interactive) and how they are applied to verify the correctness of local model updates without revealing the actual updates. The paper should also provide a more detailed analysis of the computational overhead introduced by the zero-knowledge proofs and how this overhead scales with the number of nodes and the complexity of the model.
4. The paper could provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes. It is unclear how the framework handles potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process. The paper should also discuss the trade-offs between security, privacy, and performance in the proposed framework. For example, how does the choice of different cryptographic primitives or the number of nodes involved in the SMPC protocol affect the overall performance and security of the system? The paper should also discuss the limitations of the proposed approach and potential areas for future research.

### Suggestions

The paper should provide a more detailed explanation of the SMPC protocol, including the specific cryptographic primitives used (e.g., additive secret sharing, homomorphic encryption, or oblivious transfer), and the communication patterns between nodes. It should also clarify how the secret shares are generated, distributed, and reconstructed to form the global model. The paper should discuss the impact of node failures or malicious nodes on the overall performance and security of the SMPC protocol, and how the framework mitigates these risks. For example, the paper could explore the use of techniques such as verifiable secret sharing or robust aggregation rules to enhance the security and reliability of the SMPC protocol. Furthermore, the paper should provide a more detailed analysis of the computational overhead introduced by the SMPC protocol and how this overhead scales with the number of nodes and the complexity of the model.

To address the potential vulnerabilities of node collusion and data poisoning attacks, the paper should elaborate on the specific mechanisms used to verify the correctness of local model updates. This could include techniques such as differential privacy, secure aggregation, or robust statistical methods. The paper should also discuss how the framework prevents malicious nodes from injecting false data into the global model, and how it detects and mitigates the impact of such attacks. For example, the paper could explore the use of reputation systems or incentive mechanisms to encourage honest participation in the federated learning process. Additionally, the paper should address the potential for inference attacks, where an adversary could infer sensitive information about other nodes based on the shared model updates. This could involve techniques such as differential privacy or secure multi-party computation with added noise.

The paper should also provide more details on the integration of zero-knowledge proofs, specifying whether they are interactive or non-interactive, and how they are applied to verify the correctness of local model updates without revealing the actual updates. A more detailed analysis of the computational overhead introduced by the zero-knowledge proofs is needed, including how this overhead scales with the number of nodes and the complexity of the model. The paper should also discuss the trade-offs between security, privacy, and performance in the proposed framework. For example, how does the choice of different cryptographic primitives or the number of nodes involved in the SMPC protocol affect the overall performance and security of the system? The paper should also discuss the limitations of the proposed approach and potential areas for future research, such as exploring more efficient cryptographic techniques or developing more robust mechanisms for handling node failures and malicious behavior.

### Questions

1. Could the authors provide more details on the specific implementation of the SMPC protocol, including the choice of cryptographic primitives and the communication patterns between nodes?
2. How does the framework handle potential vulnerabilities such as node collusion or data poisoning attacks during the federated learning process?
3. What is the impact of zero-knowledge proofs on the performance of the framework, and how do they scale with the number of nodes?
4. What are the trade-offs between security, privacy, and performance in the proposed framework, and how do the authors balance these factors in their design choices?

### Rating

3

### Confidence

4

**********
