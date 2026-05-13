# Enhancing Federated Domain Adaptation with Multi-Domain Prototype-Based Federated Fine-Tuning

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
Federated Domain Adaptation (FDA) is a Federated Learning (FL) scenario where models are trained across multiple clients with unique data domains but a shared category space, without transmitting private data. The primary challenge in FDA is data heterogeneity, which causes significant divergences in gradient updates when using conventional averaging-based aggregation methods, reducing the efficacy of the global model. This further undermines both in-domain and out-of-domain performance (within the same federated system but outside the local client). To address this, we propose a novel framework called \textbf{M}ulti-domain \textbf{P}rototype-based \textbf{F}ederated Fine-\textbf{T}uning (MPFT). MPFT fine-tunes a pre-trained model using multi-domain prototypes, i.e., pretrained representations enriched with domain-specific information from category-specific local data. This enables supervised learning on the server to derive a globally optimized adapter that is subsequently distributed to local clients, without the intrusion of data privacy. Empirical results show that MPFT significantly improves both in-domain and out-of-domain accuracy over conventional methods, enhancing knowledge preservation and adaptation in FDA. Notably, MPFT achieves convergence within a single communication round, greatly reducing computation and communication costs. To ensure privacy, MPFT applies differential privacy to protect the prototypes. Additionally, we develop a prototype-based feature space hijacking attack to evaluate robustness, confirming that raw data samples remain unrecoverable even after extensive training epochs. The complete implementation of MPFL is available at \url{https://anonymous.4open.science/r/DomainFL/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies domain adaptation in federated learning scenarios, employing prototype-based fine-tuning to leverage knowledge from other clients. The fine-tuning procedure requires only one round of communication between clients and the server, making it communication-computationally efficient.

### Strengths
1, Experiments on two datasets indicate a significant performance boost from the proposal, increasing accuracy by 2%.

2. The approach is intuitive, sharing prototypes using three sampling strategies.

3. The proposal is communication-computationally efficient, as it involves a low number of interaction rounds and requires only prototypes for communication.

### Weaknesses
The motivating scenario may be impractical, as the proposal assumes that clients already possess a well-pretrained model. This assumption can be particularly challenging in sensitive areas where federated learning is essential, such as healthcare or finance, where data privacy concerns limit access to robust pre-trained models.

Can the authors discuss specific applications or scenarios within these sensitive domains where obtaining a pre-trained model might be more feasible? Additionally, it would be valuable to explore potential solutions or adaptations of their method for situations where a pre-trained model is not available.

The experimental settings are somewhat vague, particularly regarding whether competitive approaches, such as FedAvg and FedProx, are trained from scratch or from the same pretrained backbone model as the MPFT. Could the authors specify this information in the paper, ideally in the experimental setup or implementation details section?

The privacy protection measures appear informal. While Gaussian noise is added to prototypes (i.e., embeddings) as noted in Section 5.6, it is important to assess whether the noise level provides adequate privacy protection for sensitive attributes or labels. To strengthen this section, could the authors provide a more rigorous analysis of the privacy guarantees associated with their approach? For example, quantifying the level of privacy protection using established metrics or frameworks would be beneficial.

### Questions
1. The experimental settings are somewhat vague, particularly regarding whether competitive approaches, such as FedAvg and FedProx, are trained from scratch or from the same pretrained backbone model as the MPFT. Could the authors specify this information in the paper, ideally in the experimental setup or implementation details section?

2. The privacy protection measures appear informal. While Gaussian noise is added to prototypes (i.e., embeddings) as noted in Section 5.6, it is important to assess whether the noise level provides adequate privacy protection for sensitive attributes or labels. To strengthen this section, could the authors provide a more rigorous analysis of the privacy guarantees associated with their approach? For example, quantifying the level of privacy protection using established metrics or frameworks would be beneficial.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Multi-domain Prototype-based Federated Fine-Tuning (MPFT), a framework designed for Federated Domain Adaptation (FDA) by utilizing domain-specific prototypes. Instead of relying on traditional model aggregation techniques, which often falter due to data heterogeneity, MPFT transfers prototypes (compressed domain representations) to the server. This approach allows the server to learn a global adapter that improves both in-domain and out-of-domain performance. MPFT also incorporates differential privacy to protect prototypes from potential data leakage.

### Strengths
The main strength of the paper lies in its comprehensive experimentation, which provides a detailed view of MPFT’s performance across various scenarios, showing superior computational and communication efficiency.

### Weaknesses
The Multi-domain Prototype-based Federated Fine-Tuning (MPFT) method proposed in this paper is overly simplistic, primarily relying on basic prototype sampling strategies—such as mean, cluster, and random sampling—to generate client prototypes. The reliance on these basic sampling methods raises concerns about the framework's ability to capture the complexities of heterogeneous data distributions. Additionally, because the model does not undergo training on each client’s data during the initial global model training phase, it fundamentally deviates from the original design principles of federated learning (FL), where the iterative process of local training and global aggregation is central. The performance gains observed in the experiments likely stem from the strong pre-trained feature extractor, which does not require training on all client data but only a few representative prototypes to achieve reasonable performance. If the pre-trained feature extractor were removed and the model was trained solely on prototypes, the results would likely be poor. If only prototype fine-tuning is needed, then why even employ a federated learning framework? Thus, despite achieving certain results, this approach introduces no complex mechanisms or innovative architectures to enhance the FL system, lacking fresh or original design. It merely follows a standard process: feature extraction with a general pre-trained model, prototype selection, server training, and client fine-tuning, without presenting any real novelty.

The paper does not provide a thorough theoretical analysis of the different prototype sampling methods, nor does it uncover the fundamental differences between these sampling strategies in handling heterogeneous data distributions. Although the paper presents experimental results comparing mean, cluster, and random sampling methods, it lacks detailed explanations on the core differences among these strategies in terms of learning mechanisms, communication efficiency, and personalization effects. For instance, how does each method perform when faced with varying degrees of non-IID data? What are the trade-offs between computational complexity and model accuracy for each method? Consequently, the paper falls short in theoretical depth, failing to provide any deep insights into the impacts of these sampling strategies.

The theoretical analysis in this paper primarily focuses on convergence. However, training the adapter on aggregated prototype data is no different from centralized data training, so convergence is naturally expected. To provide valuable theoretical insights, the paper would need to show that the adapter’s performance on aggregated prototypes is comparable to that on aggregated raw client data or offer theoretical performance bounds. Furthermore, transmitting prototypes instead of models introduces a higher risk of privacy leakage, so the analysis should prioritize differential privacy (DP) guarantees rather than focusing solely on convergence. The current paper fails to address theoretical guarantees for privacy protection, which is particularly critical in privacy-sensitive federated learning contexts. The lack of a rigorous privacy analysis, including a formal definition of the threat model and a detailed explanation of how DP is applied to the prototypes, undermines the claimed privacy benefits of the MPFT framework.

Although the experimental section is comprehensive, covering multiple datasets, various sampling strategies, and different DP configurations, it does not clearly reveal the functional differences and applicability of each prototype sampling approach across different scenarios. While the experiments test different prototype configurations, they lack an in-depth discussion on how these configurations perform under different data distribution patterns and sample sparsity conditions. For example, how does the performance of each sampling method vary as the number of prototypes per class changes? What is the impact of imbalanced class distributions on the effectiveness of each method? This results in a set of experiments that, while extensive, fails to provide a robust summary of the unique characteristics of the prototype methods, thus missing an opportunity to elevate the research value.

### Questions
I suggest that the authors remove the overly powerful pre-trained feature extractor and instead use a simpler, more foundational model for feature extraction, such as ResNet or ConvNet. This would more accurately showcase the contribution of the prototype and methodology itself.

The authors should provide a validity proof to demonstrate that training the adapter on aggregated prototypes achieves comparable performance to training on aggregated raw client data or features—or, alternatively, establish an upper bound on the performance gap between these approaches.

Although differential privacy (DP) experiments were conducted, a theoretical analysis is also necessary. Specifically, the authors should clarify the noise variance conditions required for their method to satisfy DP. In particular, the statement “Furthermore, we observe that specific noise configurations can reduce bias across heterogeneous datasets, enhancing the robustness of prototype data” requires a more robust theoretical explanation.

I would encourage the authors to further explain, both theoretically and experimentally, the differences, advantages, and potential complementarities among various prototype selection mechanisms.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Multi-domain Prototype-based Federated Fine-Tuning (MPFT), a framework designed to address data heterogeneity and data privacy in federated learning (FL) by using prototype-based training rather than traditional averaging methods. In MPFT, each client generates a set of representative data embeddings (prototypes) that capture essential domain-specific characteristics without transferring raw data. These prototypes are then aggregated at the server, allowing for a simulated centralized learning approach and enabling fine-tuning of a global adapter. This method aims to achieve performance on par with centralized learning while solving the challenges incurred by aggregating client models.
The efficiency of MPFT lies in that it requires only a single round of global communication, significantly reducing computational and communication costs compared to multi-round FL methods. Furthermore, by selectively sampling prototypes, the framework limits data transfer volumes. To ensure privacy, MPFT integrates differential privacy mechanisms, mitigating risks of data exposure and rendering prototype-based data reconstruction ineffective—even when the prototype encoder is known to potential attackers.

### Strengths
+ They propose an interesting idea -- MPFT as a one-round federated fine-tuning approach for multi-domain environments, demonstrating its performance improved over previous methods. 
+ A new metric is introduced to evaluate model adaptability, assessing both out-of-domain and in-domain accuracy to balance knowledge retention and domain adaptation.
+ The writing and logic are clear and easy to follow. The problem formulation is clear and friendly to readers.

### Weaknesses
- The proof of convergence in Section B lacks the differential-privacy-related analysis. A supplemental analysis of "MPFT with DP" should be added for theoretical completeness. Intuitively, the addition of differential privacy introduces a bounded randomness during the convergence process.

- The selected experimental counterparts for comparison are mostly in 2017-2022, which are relatively not new. In Section 2, the authors think the "averaging-based aggregation results in poor out-of-domain adaptation performance." It would be better to show the performance of out-of-domain adaptation from the recent advances atop model/parameter aggregation. Some recent works (with or without aggregation) relevant to data heterogeneity in federated learning are expected to compare, such as,

Fedcp: Separating feature information for personalized federated learning via conditional policy. In KDD 2023.
FedFed: Feature Distillation against Data Heterogeneity in Federated Learning. In NeurIPS 2023.
Fedgh: Heterogeneous federated learning with generalized global header. In MM 2023.

### Questions
1. Would the authors explain how you chose the parameter $s$ in Section 5.6? 

2. Why is the class $k$ missing in the proof in Appendix B (while formulated before proof)?

3. Can authors make more comparisons with recent (>=2023) works? For example,
Fedcp: Separating feature information for personalized federated learning via conditional policy. In KDD 2023.
FedFed: Feature Distillation against Data Heterogeneity in Federated Learning. In NeurIPS 2023.
Fedgh: Heterogeneous federated learning with generalized global header. In MM 2023.

It would be better to compare aggregation-based improvements in recent works and the new mechanism proposed in this paper. Since the authors stressed the drawbacks of these works, it would be better to give detailed support or explanation.

### Soundness
3

### Presentation
3

### Contribution
3
