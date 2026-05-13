# Janus: Dual-server Multi-Round Secure Aggregation with Verifiability for Federated Learning

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Secure Aggregation (SA) in federated learning is essential for preserving user privacy by ensuring that model updates are masked or encrypted and remain inaccessible to servers. Although the advanced protocol Flamingo (S\&P'23) has made significant strides with its multi-round aggregation and optimized communication, it still faces several critical challenges: (i) $\textit{Dynamic User Participation}$, where Flamingo struggles with scalability due to the complex setups required when users join or leave the training process; (ii) $\textit{Model Inconsistency Attacks}$ (MIA), where a malicious server could infer sensitive data, which poses severe privacy risks; and (iii) $\textit{Verifiability}$, as most schemes lack an efficient mechanism for clients to verify the correctness of server-side aggregation, potentially allowing inaccuracies or malicious actions. We introduce Janus, a generic privacy-enhanced multi-round SA scheme through a dual-server architecture. A new user can participate in training by simply obtaining the servers' public keys for aggregation, eliminating the need for complex communication graphs. Our dual-server model separates aggregation tasks, ensuring that neither server can successfully launch a MIA without controlling at least $n-1$ clients. Additionally, we propose a new cryptographic primitive, $\textit{Separable Homomorphic Commitment}$, integrated with our dual-server approach to ensure the verifiability of aggregation results. Extensive experiments across various models and datasets show that Janus significantly boosts security while enhancing efficiency. It reduces per-client communication and computation overhead from  logarithmic to constant scale compared to state-of-the-art methods, with almost no compromise in model accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper consider several key challenges in secure aggregation: dynamic user paticipation, resistance to model inconsistency attacks (MIA), and verifiability of aggregation of malcious servers. This paper proposes a dual-server architecture where one server aggregates the masked gradients and the other aggregates the masks, ensuring that neither server has access to the final aggregation result, thus protecting against MIA. It also incorporates a novel cryptographic primitive, Separable Homomorphic Commitment (SHC), which enables clients to verify the correctness of the server’s aggregation without sacrificing efficiency.

### Strengths
-  While a two-server model is not new, I like the idea that the proposed method introduces the dual server model to protect against MIA by preventing either server from accessing the final aggregation result.
- This paper introduces SHC, which allows users to verify aggregation correctness without incurring heavy computational costs.
- It reduces the communication and computation overhead from logarithmic to constant scale, which is a major improvement over advanced schemes like Flamingo and BBSA. This makes it more practical for large-scale federated learning frameworks.

### Weaknesses
 - The proposed method relies heavily on the assumption that the two servers do not collude. While this assumption is reasonable in certain applications, it is also a potential limitation. In practice, ensuring non-collusion between two entities may not always be feasible, especially in untrusted environments. The paper does not sufficiently address the implications if the servers were to collude, and how this would compromise the security of the system. Specifically, if both servers collude, they could potentially reconstruct the individual client gradients by combining the masked gradients and the masks, thus completely bypassing the privacy protections.
- In addition, while the paper claims that the proposed scheme mitigates the risks associated with a single-server setup, the system still relies on the assumption that both servers should be successful in aggregation. If either server fails, the entire system could be at risk. The paper does not provide a clear mechanism for handling server failures, such as a fallback or recovery strategy. This lack of fault tolerance is a significant weakness, especially in distributed systems where server outages are not uncommon. Furthermore, the paper does not discuss the potential impact of a server providing incorrect aggregation results, and how this would affect the overall model convergence.
- As the SHC protocol plays key role to verify the correctness in the dual-server system, it would be helpful if the SHC protocol is described with clearer notation and more intuitive explanations. For instance, separation of commitments could be explained more thoroughly for readers unfamiliar with the cryptographic concepts. The current explanation lacks sufficient detail to fully grasp the underlying mechanisms of the SHC protocol, making it difficult to assess its security and efficiency. A more rigorous mathematical treatment of the SHC protocol, with clear definitions of the cryptographic primitives and their properties, would greatly enhance the paper's clarity and credibility.

### Questions
please see the comments in weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Janus, a privacy-enhanced multi-round secure aggregation (SA) scheme for federated learning. It addresses challenges faced by existing protocols like Flamingo, including dynamic user participation, model inconsistency attacks (MIA), and lack of verifiability. Janus uses a dual-server architecture and a new cryptographic primitive, Separable Homomorphic Commitment (SHC). New users can easily join training, and the dual-server setup prevents MIA. SHC ensures aggregation result verifiability. Experiments show improved security and efficiency with reduced per-client overhead and maintained model accuracy.

### Strengths
(1) The dual-server architecture and the concept of separable homomorphic commitmen are novel contributions. The combination of these elements to address multiple challenges in secure aggregation is interesting.

(2) The scheme is well-designed, with each component serving a specific purpose in enhancing security and efficiency. The integration of SHC with the dual-server model is seamless and effective.

### Weaknesses
(1) While the non-collusion assumption of servers is stated, a more in-depth analysis of potential threats and how they are mitigated in different scenarios could be added. For example, what if a malicious actor compromises one of the servers or if there are side-channel attacks? Specifically, the paper should elaborate on the implications if one server is compromised and how the proposed Separable Homomorphic Commitment (SHC) scheme would maintain privacy in such a scenario. The analysis should also consider the potential for timing attacks or other side-channel vulnerabilities that could leak information about the committed values or user gradients, and how the design of Janus mitigates these risks.

(2) The experiments could be more extensive. For instance, testing on a wider range of datasets and models, including those with more complex architectures and larger data volumes, would provide a more comprehensive evaluation of the scheme's performance. The current experiments lack diversity in terms of data characteristics and model complexity. Furthermore, the evaluation should include a detailed analysis of the impact of varying network conditions, such as latency and bandwidth limitations, on the performance of Janus. This would provide a more realistic assessment of its applicability in real-world federated learning environments. The experiments should also explore the scalability of the scheme with respect to the number of clients.

(3) Although the author has compared with some existing methods, there are few comparison methods. The author may need to add some comparison methods to further verify the effectiveness of Janus. The current comparisons do not fully contextualize the performance of Janus against a broad range of state-of-the-art secure aggregation techniques. A more comprehensive comparison would help to better understand the strengths and weaknesses of the proposed scheme.

(4) The author may also need to add some additional experiments to verify the effectiveness of Janus, such as aggregation completion time, computation costs, etc. The paper lacks a detailed breakdown of the computational overhead associated with each step of the Janus protocol, including the SHC operations, encryption, and aggregation. A thorough analysis of these costs, both in terms of time and resources, is crucial for evaluating the practical feasibility of the scheme. Furthermore, the paper should provide a more detailed analysis of the communication overhead, including the size of the messages exchanged between clients and servers, and how this impacts the overall efficiency of the system.

### Questions
The author needs to explain in detail the questions I mentioned above, and I will determine the final score based on your answers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Janus, a system for multi-round secure aggregation for federated learning. By having a very low round setup independent of the number of clients, Janus can easily be used for multiple rounds. Janus utilizes a dual-server setup where one server handles masked updates and the other manages aggregation of masks, ensuring that neither server has access to the final aggregated results. A novel cryptographic primitive, Separable Homomorphic Commitment, enables client-side verification of the correctness of the aggregation result. The authors evaluate Janus end-to-end, highlighting its constant per-client communication and computational overhead while preserving model accuracy.

### Strengths
- Addresses scalability challenges of privacy-preserving federated learning
- Comprehensive evaluation with end-to-end model training

### Weaknesses
 - Incomplete comparison with related work in the multi-server FL setting such as 2-party MPC or [ELSA: Secure Aggregation for Federated Learning with Malicious Actors, S&P’23]. These approaches also provide low overhead for clients, independent of the number of clients. Adding a more detailed comparison could help contextualize Janus' unique contributions and highlight differences in scalability and overhead reduction strategies.
- The threat model assumes non-collusion among entities, which may not align with practical scenarios, particularly regarding client behaviors. In real-world applications, service providers could potentially collude with a bounded subset of clients, as assumed in related works’ threat models. Janus’ reliance on a non-collusion model raises concerns about its susceptibility to model inconsistency attacks if a provider colludes with even a single client or introduces a Sybil client, potentially gaining access to the aggregated model and undermining security. Additionally, the threat model assumes the servers are semi-honest, which makes achieving verifiability property trivial.
- The security proof contains inaccuracies that hinder their clarity. For instance, Theorem 1 references two distinct ideal functionalities (Figures 6 & 7), though Figure 7 appears underdefined. The distinction in scenarios based on “whether the servers are corrupted by A” might incorrectly imply that both servers could be corrupted simultaneously, which conflicts with the intended security assumptions.

### Questions
1. In Table 1: What is the versatility property?
2. How does your approach compare with a straightforward 2PC baseline, and other multi-server FL systems such as [ELSA: Secure Aggregation for Federated Learning with Malicious Actors, S&P’23]?
3. Given that you focus much of the evaluation on the accuracy and loss of the approaches, would we expect a difference with related secure aggregation schemes?
4. How can new users join the training process? What prevents the service provider from setting up sybil clients to get access to the model?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Janus introduces a Secure Aggregation (SA) scheme for Federated Learning (FL) that overcomes some challenges in existing protocols by implementing a dual-server architecture and a  cryptographic primitive called Separable Homomorphic Commitment (SHC).

### Strengths
The paper is clear and well-organized, with complex concepts explained effectively and supported by useful visual aids.

### Weaknesses
While the paper introduces an approach with Janus, several weaknesses limit its contribution and practical applicability. First, it lacks a comparison with single-server state-of-the-art methods like VeriFL, raising questions about its feasibility and efficiency compared to existing solutions. The assumption that clients do not collude is unrealistic, especially if clients are interested in each other's model updates; the scheme does not specify how many colluding users it can tolerate, leaving potential vulnerabilities unaddressed. Fault tolerance is insufficient, as user dropout can disrupt the entire aggregation process, and the paper does not explain how it handles partial user failures or higher dropout rates. The scheme may be vulnerable to differential attacks if an attacker obtains masked data from multiple rounds and exploits similarities in user inputs to infer private information. The commitment mechanism lacks detailed specifications, and if a simple hash-based commitment is used, it may be susceptible to length extension attacks. The Separable Homomorphic Commitment (SHC) appears to be a variant of existing commitment schemes without substantial innovation and lacks essential properties like trapdoor mechanisms and equivalence, potentially weakening security; more theoretical support and security proofs are needed. Additionally, implementation details for comparative schemes are insufficient, experiments lack statistical significance analysis and detailed breakdowns of computational and communication overhead, and there is no evaluation of scalability with different user numbers or model sizes. Claims of resistance to Model Inconsistency Attacks and multi-round security are not experimentally validated, which undermines the credibility of the proposed security enhancements.

### Questions
1. The paper does not compare Janus's overhead and feasibility with existing single-server SOTA methods that achieve similar privacy and verifiability. Notably, schemes like VeriFL have demonstrated efficient verifiable federated learning in a single-server setting. In addition, the aggregation results of a single server can actually be kept secret (already exists).

2. The paper assumes that clients do not collude. However, if clients are interested in each other's model updates, this assumption may not hold. Colluding clients could potentially infer private information about other users.

3. The scheme's fault tolerance is limited; user dropout can adversely affect the entire aggregation process. The paper does not adequately explain how the system handles partial user failures or higher dropout rates.

4. Develop and describe mechanisms to handle user dropout more effectively. This could include techniques like dropout resilience protocols or asynchronous aggregation methods. Experiment with varying dropout rates, including those higher than the idealistic 10%, to demonstrate the scheme's robustness in realistic settings.

5. If an attacker obtains masked inputs from two rounds where the user's input remains similar (i.e., \( x_{i,t} \approx x_{i,t+1} \)), they could perform differential analysis to infer changes in the original inputs.

6. The paper does not specify the specific requirements or properties of the commitment algorithm used in the SHC. If a simple hash-based commitment is used (e.g., \( c_{i,t} = H(x_{i,t} || r_{i,t}) \)), it may be vulnerable to length extension attacks or other cryptographic weaknesses.

7. SHC is described as a variant of existing commitment schemes but lacks substantive innovation. It does not support essential properties like trapdoor mechanisms or equivalence, which are present in schemes like the one used in VeriFL. The security proofs provided are insufficient to establish its robustness.

8. The implementation details, particularly the parameter settings for Janus and the comparative schemes (BBSA and Flamingo), are not thoroughly documented. This omission hampers reproducibility and makes it difficult to assess the validity of the experimental results.

9. The experiments lack information on the number of repetitions and do not include statistical analyses to determine the significance of the results.

10. The paper only reports the total computation time without decomposing the overhead into its constituent components (e.g., cryptographic operations, communication latency).

11. There is no empirical data or graphical analysis of the communication overhead; the paper relies solely on theoretical analysis.

12. The experiments are conducted with a relatively small number of users (100), which is insufficient to demonstrate scalability. The impact of varying the number of users and the model size on performance is not evaluated.

13. While the paper claims that Janus resists MIA, it does not provide experimental tests or simulations to substantiate this claim.

14. The security of Janus over multiple rounds is not experimentally verified, leaving potential vulnerabilities unaddressed.

15. The scheme does not specify the maximum number of colluding users it can tolerate without compromising security.

16. By omitting features like trapdoor mechanisms and equivalence properties, SHC may be less secure than existing commitment schemes. For example, in VeriFL, the commitment scheme allows for equivalence operations, which enhance functionality and security.

### Soundness
1

### Presentation
2

### Contribution
1
