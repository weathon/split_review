# Privacy-Preserving Federated Learning via Homomorphic Adversarial Networks

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3, 5, 3, 3

## Abstract
Privacy-preserving federated learning (PPFL) aims to train a global model for multiple clients while maintaining their data privacy.
However, current PPFL protocols exhibit one or more of the following insufficiencies: considerable degradation in accuracy, the requirement for sharing keys, and cooperation during the key generation or decryption processes.
As a mitigation, we develop the first protocol that utilizes neural networks to implement PPFL, as well as incorporating an Aggregatable Hybrid Encryption scheme tailored to the needs of PPFL.
We name these networks as \emph{Homomorphic Adversarial Networks}~(HANs) which demonstrate that neural networks are capable of performing tasks similar to multi-key homomorphic encryption~(MK-HE) while solving the problems of key distribution and collaborative decryption.
Our experiments show that HANs are robust against privacy attacks.
Compared with non-private federated learning, experiments conducted on multiple datasets demonstrate that HANs exhibit a negligible accuracy loss (at most 1.35\%).  Compared to traditional MK-HE schemes, HANs increase encryption aggregation speed by 6,075 times while incurring a 29.2$\times$ increase in communication overhead.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The paper claims that it presents a novel privacy-preserving federated learning (PPFL) protocol that utilizes neural networks, specifically Homomorphic Adversarial Networks (HANs), to enhance data privacy without significantly sacrificing accuracy. It addresses key limitations of existing PPFL methods, such as accuracy degradation and key management issues, by introducing an Aggregatable Hybrid Encryption (AHE) scheme. This approach enables individual clients to maintain privacy while allowing efficient encryption and aggregation of model updates.

### Strengths
1. The article provides a wealth of formal definitions.

2. A novel concept has been proposed.

### Weaknesses
1. It is difficult to quickly determine the details of the design AHE scheme, as the related definitions and statements are overly redundant.

2. The experimental analysis provided seems insufficient.

### Questions
1. Why did the authors choose simple models to validate the security of the proposed scheme? What I mean is whether sufficient security can be demonstrated under these complex models.

2. The security assessment lacks a systematic approach. Could you provide a more formal and systematic security analysis?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors develop the first protocol that utilizes neural networks to implement PPFL, as well as incorporating an Aggregatable Hybrid Encryption scheme tailored to the needs of PPFL.

### Strengths
Using neural network methods to implement MK-HE is a very interesting direction. The use of hybrid encryption can fully leverage the advantages of both symmetric and asymmetric encryption.

### Weaknesses
1. There is a lack of understanding of related work. Methods based on secret sharing inherently have strong resistance to collusion attacks, as demonstrated in works such as (Bell J, Gascón A, Lepoint T, et al. {ACORN}: input validation for secure aggregation[C]//32nd USENIX Security Symposium (USENIX Security 23). 2023: 4805-4822. Bonawitz K, Ivanov V, Kreuter B, et al. Practical secure aggregation for privacy-preserving machine learning[C]//Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. 2017: 1175-1191.). However, the authors did not mention or compare these in the paper.
2. According to the experimental results, although HANs are more computationally efficient than SecFed, the communication overhead increases by dozens of times, as shown by the experimental results in Table 6. This is unacceptable for a large number of users and would limit the practical application of HANs.

### Questions
1. How does the performance compare with other schemes that can also resist collusion attacks, such as (Bell J, Gascón A, Lepoint T, et al. {ACORN}: input validation for secure aggregation[C]//32nd USENIX Security Symposium (USENIX Security 23). 2023: 4805-4822. Bonawitz K, Ivanov V, Kreuter B, et al. Practical secure aggregation for privacy-preserving machine learning[C]//Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. 2017: 1175-1191.)?
2. The additional communication makes the proposed HANs unsuitable for most federated learning scenarios. Is there a way to reduce communication, or is the additional communication unavoidable?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a novel privacy-preserving federated learning method that attempts to integrate multi-key homomorphic encryption with neural networks. Each client generates a public key and two private keys using KeyGen with a security parameter $\kappa$. During the encryption phase, plaintext and private keys are input into the encryption model held by each client for encryption. In the aggregation phase, the ciphertexts and public keys are input into the decryption model held by the aggregator for decryption. The training process employs adversarial training, aiming to maximize the error in attacker's data reconstruction while minimizing the loss after data aggregation. The authors define two attack models: Pseudo N-1 Collusion Attack based on the Original Model (PCAOM) and Pseudo N-1 Collusion Attack based on the Public Dataset (PCAPD), achieving privacy-protected federated learning under these attacks.

### Strengths
- **Originality**: The paper introduces an innovative privacy-preserving federated learning method that combines homomorphic encryption with neural networks, enhancing the security and usability of the model.
- **Effectiveness**: The research demonstrates the effectiveness of enhancing data privacy through adversarial training, increasing the model's robustness against complex attack scenarios.
- **Clarity**: The article provides a detailed description of the transformation from the original model to a private model and demonstrates how to defend against two specific attacks.
- **Practicality**: Compared to traditional encryption and decryption methods, the neural network's black-box nature increases the difficulty of attacks. The authors also claim that this method eliminates collaborative decryption, key sharing, and collective key generation among clients, optimizing processing time.

### Weaknesses
 - **Accuracy**: Since the model is involved in the encryption and decryption process, it cannot guarantee that the parameters obtained by the decryptor are completely correct, only ensuring accuracy within a certain error rate, which is inconsistent with traditional homomorphic encryption standards. This deviation from established cryptographic norms raises concerns about the practical security and reliability of the proposed method in scenarios requiring precise computations. The inherent approximation introduced by neural network-based encryption could lead to unpredictable errors accumulating during iterative processes common in federated learning.
- **Insufficient Proof**: Despite the model's difficulty to be breached due to its black-box nature, there is a lack of rigorous formal proof to support its security claims. The reliance on the black-box nature of neural networks as a security feature is not sufficient, as it does not provide a quantifiable measure of security against determined adversaries. The absence of formal security analysis, such as proofs based on computational hardness assumptions, makes it difficult to assess the method's resistance to sophisticated attacks.
- **Incomplete Documentation**: The paper does not detail the specific implementation of KeyGen, how to ensure Perfect Key Uniformity, or how to resist chosen-plaintext attacks, limiting the method's verifiability and reliability. The lack of clarity regarding the KeyGen process, specifically whether it involves a model or a deterministic algorithm, prevents a thorough security analysis. Furthermore, the paper does not explain how the method prevents key reuse or how the keys are distributed, which are critical for ensuring the security of the system. The absence of a clear explanation of how the method resists chosen-plaintext attacks, which are standard in cryptographic analysis, further undermines the confidence in the method's security.

### Questions
- The paper does not detail how KeyGen operates, whether it is generated by a model or some algorithm, thus we cannot verify how it eliminates key sharing. It is also unclear how Perfect Key Uniformity is ensured, thus it is uncertain how the method resists chosen-plaintext attacks.
- The paper does not provide specific model structures or other information, making it impossible to verify and replicate the authors' experiments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the challenges of key sharing and collaboration in Privacy-Preserving Federated Learning (PPFL) protocols, which may lead to privacy risks and inconvenience. The authors propose a PPFL protocol implemented using neural networks, combined with an aggregatable hybrid encryption scheme. By accepting some trade-offs in communication overhead and accuracy, this approach significantly enhances the encryption aggregation speed.

### Strengths
The proposed method in this paper significantly enhances encryption aggregation speed, which is often a key factor influencing the overall efficiency of federated learning (FL) systems. The approach of using neural networks as a substitute for the MK-HE algorithm introduces a novel perspective with meaningful research value. Additionally, this method is robust against various forms of collusion, ensuring the privacy of both the model and users.

### Weaknesses
The paper contains a typographical error in the abstract’s first word, which reads “Privacy-peserving” instead of “Privacy-preserving”.

In the Introduction, the main technique of the paper (using neural networks to simulate MK-HE) is not clearly stated, instead appearing in the contributions section, which makes the structure feel somewhat unbalanced. Additionally, the flow of the introduction could be improved for better clarity. It is recommended to briefly introduce the neural network simulation technique within the Introduction to set up the main idea clearly, while streamlining the first part of the contributions section. Structuring the Introduction by first presenting the problem context, followed by current challenges, and then the proposed solution would improve readability. Limiting the number of paragraphs and avoiding interleaved content would also enhance the flow.

The Method section lacks organization and could benefit from a more structured presentation. The neural network application, which is central to the proposed approach, is not discussed in the main paragraphs, resulting in a structural imbalance. Important content should be integrated into the main body rather than relegated to the appendix to improve the paper’s clarity and readability. It is recommended to provide a more detailed description of the content from Appendix B and Appendix E in Section 3.6. If space constraints are a concern, consider simplifying the key concepts in Section 3.1 to make room for these additions.

Lastly, some equations in the Appendix B extend beyond the page boundaries. Attention to formatting standards would enhance the overall presentation.

### Questions
Proofreading for Spelling and Formatting: Could the authors carefully review the paper for any spelling and formatting errors to ensure accuracy and readability throughout?

Clarity of Introduction and Main Contributions: In the Introduction, could the authors clarify the primary method of their approach, particularly the use of neural networks as a substitute for MK-HE, rather than emphasizing this only in the contributions section? This adjustment may help readers understand the significance of the method from the outset.

Organization of the Method Section: The main outline of the proposed method is somewhat difficult to follow, and it is challenging to locate the main content regarding the neural network application. Could the authors consider reorganizing this section to more clearly outline the process and central elements? Moving the key explanations from the appendix to the main text may also improve clarity.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel approach to Privacy-Preserving Federated Learning (PPFL) by introducing Homomorphic Adversarial Networks (HANs). HANs utilize neural networks to emulate multi-key homomorphic encryption (MK-HE), addressing key distribution and collaborative decryption challenges. The proposed Aggregatable Hybrid Encryption (AHE) scheme is designed to balance computational efficiency, cryptographic security, and the distributed nature of FL systems. The paper claims that HANs exhibit robustness against privacy attacks with negligible accuracy loss and significantly improved encryption aggregation speed compared to traditional MK-HE schemes.

### Strengths
1. Originality: The paper introduces Homomorphic Adversarial Networks (HANs), an innovative approach using neural networks for multi-key homomorphic encryption in federated learning, offering a new perspective on privacy preservation.
2. Quality: This study is of fair quality. It achieved a notable 6,075-fold acceleration in encryption aggregation with minimal loss in accuracy, showcasing the practicality and robustness of HANs against a variety of attacks.
3. Clarity: The paper is clearly written, with a well-structured presentation that effectively communicates the novelty of HANs and their advantages over existing methods.
4. Significance: The work is significant for advancing privacy in federated learning, particularly in resisting collusion attacks and maintaining model accuracy.

### Weaknesses
1. The security of HANs is predicated on the presence of at least two honest clients, which may not always be feasible. The paper could be improved by discussing alternative security models that do not rely on this assumption or by exploring the implications of a higher number of malicious clients. Specifically, the paper does not address scenarios where a majority of clients could be compromised, which would significantly impact the security guarantees of the proposed method. The analysis should consider how the system behaves under various adversarial settings, including collusion attacks involving more than half of the participating clients.
2. While the paper provides a general discussion on the security aspects of Homomorphic Adversarial Networks (HANs), the analysis lacks the rigor and formality expected in a comprehensive security evaluation. The security claims are not supported by formal proofs or a detailed threat model. For example, a formal analysis of the information leakage during the training of HANs and the aggregation process is missing. The paper should include a more detailed analysis of the potential vulnerabilities and attack vectors, such as model poisoning or inference attacks.
3. The paper's comparison with traditional MK-HE schemes is compelling, but a more comprehensive benchmark against a broader range of state-of-the-art PPFL methods would strengthen the paper's claims. The current evaluation does not include comparisons with other privacy-preserving techniques, such as differential privacy or secure multi-party computation, which are commonly used in federated learning. A more thorough comparison would provide a better understanding of the advantages and limitations of HANs compared to existing approaches.
4. The experiments only focus on a few datasets and models. To strengthen the paper's arguments, the authors should consider demonstrating the versatility of HANs across a broader range of datasets (e.g., text datasets) and various model architectures. The current evaluation is limited to image classification tasks and does not explore the performance of HANs in other domains, such as natural language processing or time-series analysis. The paper should include experiments with more diverse datasets and models to demonstrate the general applicability of the proposed method.
5. The paper mentioned the increase in communication overhead by HANs, but it indeed provided a detailed analysis, including performance under various network conditions. The paper should provide a more detailed analysis of the communication overhead, including the size of the encrypted gradients and the impact of network latency on the overall performance. The analysis should also explore potential optimization techniques to reduce the communication costs.
6. The paper does not demonstrate the adaptability and effectiveness of the AHE method in various federated learning scenarios, especially in environments with significant variations in data sensitivity and attack surfaces, which limits a comprehensive understanding of the performance and security of the AHE scheme in practical applications. The paper should include experiments that evaluate the performance of AHE under different data distributions and varying levels of data sensitivity. The analysis should also consider the impact of different attack surfaces on the security of the AHE scheme.

### Questions
1. The security of HANs relies on the presence of at least two honest clients. Can the authors discuss alternative security models that do not depend on this assumption, or explore the impact on HANs' security when the number of malicious clients increases?
2. The authors should provide more rigorous security proofs or mathematical models to support the security claims made in the paper.
3. Regarding the comparison with traditional MK-HE schemes, the authors should expand the comparison to include a broader range of PPFL methods.
4. To strengthen the arguments in the paper, the authors should consider demonstrating the diversity and applicability of HANs across a wider range of datasets and various model architectures.
5. Regarding the communication overhead issue of HANs, the authors can further discuss the impact of this increased communication overhead on practical deployment and consider whether it is possible to reduce these costs through optimization.
6. Regarding the adaptability and effectiveness of AHE, the authors can provide more experimental data or theoretical analysis on the performance and adaptability of AHE in different scenarios.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes an empirical solution leveraging GAN to address the privacy challenge during federated model aggregation.

### Strengths
1. The paper focuses on one of the important privacy issues in federated learning. Aggregation data privacy has been a constant challenge, especially considering the tradeoffs among privacy, overhead, and performance.

2. The paper proposes an empirical solution using GAN for privacy protection.

### Weaknesses
1. The paper misses a major related domain, which is threshold HE. Compared to MK-HE, threshold HE (1) in general does not incur additional overheads both in computation and ciphertext; (2) does not suffer from client dropout issues, which is a common challenge in practical FL systems.

2. There is no formal rigorous security proof, as the authors stated themselves in the paper. The informal discussion in Appendix G does not satisfy the requirement needed for the claimed privacy guarantee, I would like to see security proofs under, for example, UC-Security, but it seems like GAN-based solutions would fail to be assessed this way. Regarding the collusion models, the paper introduces pseudo N−1 collusion attacks, but it does not fully address the potential vulnerabilities in scenarios with more sophisticated collusion strategies or when attackers can coordinate over time. Additionally, per my understanding of the paper, the assumed security is bounded and realized by obfuscating the training of the GAN, what if the adversary can train a similar GAN? This approach largely relies on security through obscurity, which is generally regarded as an unreliable security approach. The privacy guarantee of this paper is far from being convincing and considered as a serious privacy/security work.


3. Even if the idea of using a GAN-like solution worked to satisfy the privacy guarantee, there would be limited novelty compared to the previous NN-based encryption systems referred in the related work, other than applying it in the federated learning setup.

4. In a lot of FL systems in practice, the communication limitation is more of a bottleneck compared to the aggregation computation overhead which is relatively easier to solve by scaling up the server. This communication overhead for the computation improvement approach might not solve the more practical challenges. 

5. It is hard to follow the paper, especially given the confusing structures of Section 1 and Section 3. In Section 1, it is unclear what the major research challenge this paper tries to tackle regarding MK-HE and the research contribution of this paper following that. In Section 3, the threat model could have been precisely captured and a structured description of the proposed method is missing. The majority of the technical details of the proposed HAN are in Appendix (e.g. PPU in Appendix E) while the main paper contains little information on how and why HAN would work in terms of performance and privacy.

### Questions
1. Are all experiments a simulation of FL running on a single machine?
2. Why not consider more recent stronger attacks than DLG? 
3. Did the authors perform analysis on the proposed method when applied to LLMs?
4. What does "Primarily, they focus on symmetric encryption without addressing homomorphic computation." mean? Symmetric encryption and homomorphic encryption are not two mutually exclusive concepts.
5. Could you provide a more formal definition of AHE that complies with the standard security definition? Also, why does the $m_{agg}$ step only consider 3 ciphertexts?
6. The paper mentioned that CKKS-based implementation would have a huge accuracy drop. Could you show the experimental results supporting this claim? In the FL setting, CKKS's approximation error will generally not significantly impact the performance due to the relatively simple aggregation operations, compared to a full-on end-to-end encrypted NN.
7. Some of the experiments do not have error bars, for example, Table 5.

### Soundness
1

### Presentation
1

### Contribution
2
