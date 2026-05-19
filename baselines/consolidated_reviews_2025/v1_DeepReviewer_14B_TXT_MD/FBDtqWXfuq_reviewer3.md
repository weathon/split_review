### Summary

This paper introduces a novel setting in federated learning (FL), called Modality-Collaborated Federated Learning (MCFL), which facilitates collaboration among uni-modal clients with different data modalities. To address the challenges of model heterogeneity and modality gaps in MCFL, the authors propose a framework based on a modality-agnostic transformer, named Federated Modality Collaboration (FedCola). FedCola explores optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement. The comprehensive evaluations demonstrate that FedCola significantly outperforms existing solutions.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel setting in federated learning (FL), called Modality-Collaborated Federated Learning (MCFL), which facilitates collaboration among uni-modal clients with different data modalities. This is a significant contribution as it shifts the focus from multi-modal clients to uni-modal clients, making the system more practical and appealing to a wider range of participants.

2. The authors propose a framework called Federated Modality Collaboration (FedCola), based on a modality-agnostic transformer. FedCola addresses the challenges of model heterogeneity and modality gaps in MCFL by exploring optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement. This is a technical innovation that effectively leverages the strengths of transformers for multi-modal data.

3. The paper provides a thorough evaluation of FedCola, comparing it against adapted versions of existing methods like Uni-FedAVG and CreamFL. The evaluation considers various federated learning scenarios, including different numbers of clients, levels of data heterogeneity, and client availability ratios. The results demonstrate that FedCola outperforms existing solutions, establishing it as a robust baseline for MCFL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper introduces a novel setting in federated learning (FL), called Modality-Collaborated Federated Learning (MCFL), which facilitates collaboration among uni-modal clients with different data modalities. This is a significant contribution as it shifts the focus from multi-modal clients to uni-modal clients, making the system more practical and appealing to a wider range of participants.

2. The authors propose a framework called Federated Modality Collaboration (FedCola), based on a modality-agnostic transformer. FedCola addresses the challenges of model heterogeneity and modality gaps in MCFL by exploring optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement. This is a technical innovation that effectively leverages the strengths of transformers for multi-modal data.

3. The paper provides a thorough evaluation of FedCola, comparing it against adapted versions of existing methods like Uni-FedAVG and CreamFL. The evaluation considers various federated learning scenarios, including different numbers of clients, levels of data heterogeneity, and client availability ratios. The results demonstrate that FedCola outperforms existing solutions, establishing it as a robust baseline for MCFL.

1. The paper does not provide a detailed analysis of the computational and communication costs associated with the proposed FedCola framework. This is an important consideration for practical deployment, especially in resource-constrained environments. A thorough analysis of the computational complexity and communication overhead of FedCola compared to existing methods would be valuable.

2. The paper focuses on a specific type of multi-modal data (vision and language) for demonstration. While this is a common and relevant combination, it would be beneficial to explore the applicability of the proposed framework to other types of multi-modal data, such as audio and video, or different combinations of modalities. This would help to establish the generalizability of the proposed approach.

3. The paper does not extensively discuss the potential limitations or challenges of the proposed framework. For example, how does FedCola handle scenarios with highly imbalanced data distributions across modalities or clients? What are the potential failure modes of the proposed approach? A more thorough discussion of these aspects would provide a more balanced perspective on the strengths and weaknesses of the proposed framework.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational and communication costs associated with the FedCola framework. Specifically, the authors should provide a breakdown of the time and memory requirements for both the client-side and server-side operations. This should include an analysis of the number of floating-point operations (FLOPs) required for the attention mechanism and other key components of the modality-agnostic transformer. Furthermore, the communication overhead should be quantified in terms of the number of parameters transmitted between clients and the server during each communication round. A comparison of these costs with those of existing federated learning methods, such as Uni-FedAVG and CreamFL, would provide valuable insights into the practical feasibility of FedCola. This analysis should also consider the impact of different model sizes and client hardware capabilities on the overall performance and resource consumption.

To further strengthen the paper, the authors should explore the applicability of the FedCola framework to a wider range of multi-modal data. While the current focus on vision and language is relevant, the paper should also investigate how the framework performs with other modalities, such as audio and video. This could involve adapting the modality-agnostic transformer to handle different input data formats and feature representations. For example, the authors could explore the use of convolutional neural networks (CNNs) for processing image and video data and recurrent neural networks (RNNs) or transformers for processing audio data. Additionally, the paper should investigate the performance of FedCola with different combinations of modalities, such as vision and audio or language and video. This would help to establish the generalizability of the proposed approach and its potential for real-world applications.

Finally, the paper should include a more detailed discussion of the potential limitations and challenges of the FedCola framework. This should include an analysis of how the framework handles scenarios with highly imbalanced data distributions across modalities or clients. For example, the authors could investigate the impact of varying the number of samples per modality on the performance of the global model. Furthermore, the paper should discuss the potential failure modes of the proposed approach, such as the risk of negative transfer between modalities or the sensitivity of the framework to hyperparameter settings. A thorough analysis of these limitations would provide a more balanced perspective on the strengths and weaknesses of the proposed framework and guide future research in this area.

### Questions

1. Could you provide a more detailed analysis of the computational and communication costs associated with the FedCola framework? How does it compare to existing methods in terms of resource requirements?

2. How does the proposed FedCola framework handle scenarios with highly imbalanced data distributions across modalities or clients? Are there any specific strategies or techniques used to mitigate the impact of data imbalance?

3. What are the potential limitations or challenges of the FedCola framework that were not extensively discussed in the paper? Are there any known failure modes or scenarios where the proposed approach may not perform well?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
