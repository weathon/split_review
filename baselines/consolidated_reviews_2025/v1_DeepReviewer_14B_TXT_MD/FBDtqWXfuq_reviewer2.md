### Summary

This paper introduces a novel setting in federated learning (FL), called Modality-Collaborated Federated Learning (MCFL), which facilitates collaboration among uni-modal clients with different data modalities. To address the challenges of model heterogeneity and modality gaps in MCFL, the authors propose a framework based on a modality-agnostic transformer, named Federated Modality Collaboration (FedCola). FedCola explores optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement. The comprehensive evaluations demonstrate that FedCola significantly outperforms existing solutions.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1.	This paper introduces a novel setting in federated learning (FL), called Modality-Collaborated Federated Learning (MCFL), which facilitates collaboration among uni-modal clients with different data modalities.
2.	The authors propose a framework based on a modality-agnostic transformer, named Federated Modality Collaboration (FedCola). FedCola explores optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement.
3.	The comprehensive evaluations demonstrate that FedCola significantly outperforms existing solutions.

### Weaknesses

#### Some Related Works


#### comment

1.	This paper investigates a specific case of heterogeneous federated learning, focusing on scenarios where different clients possess data from various modalities (e.g., images, text). While this is an interesting direction, it may not be sufficiently general or widely applicable to be considered a major contribution to the field of federated learning as a whole. The core challenge of modality-specific feature extraction and alignment within a federated setting is not fully addressed, limiting the impact of the proposed method to a narrow domain.
2.	The novelty of the proposed method is somewhat limited. The approach primarily combines existing techniques, such as attention mechanisms, for parameter sharing and introduces a warm-up training strategy. The specific adaptation of attention mechanisms for cross-modal parameter sharing, while practical, lacks a theoretical justification or a novel architectural contribution that significantly advances the state-of-the-art in federated learning.
3.	The experimental evaluation is limited in scope. The paper only considers two modalities (vision and language) and uses relatively small datasets (CIFAR-100 and AGNews). This limited evaluation does not adequately demonstrate the scalability or robustness of the proposed method to more complex scenarios involving a larger number of modalities, larger datasets, or more diverse data distributions. The choice of datasets, while common, does not fully capture the challenges of real-world multi-modal federated learning.

### Suggestions

To strengthen the paper, the authors should first address the limited scope of the proposed method by providing a more rigorous theoretical analysis of the attention-based parameter sharing mechanism. Specifically, they should investigate the conditions under which this approach is effective and provide a theoretical justification for why it is suitable for cross-modal federated learning. This could involve analyzing the convergence properties of the proposed method or providing insights into how the attention mechanism facilitates the alignment of modality-specific features. Furthermore, the authors should explore alternative parameter sharing strategies and compare their performance with the proposed approach. This would provide a more comprehensive understanding of the strengths and limitations of the proposed method and help to establish its novelty.

Second, the experimental evaluation needs to be significantly expanded to include a more diverse set of modalities, datasets, and scenarios. The authors should consider including datasets with a larger number of modalities, such as those involving audio, video, or sensor data, to demonstrate the scalability of the proposed method. They should also evaluate the performance of the proposed method on larger datasets with more complex data distributions to assess its robustness. Additionally, the authors should investigate the impact of different data heterogeneity levels across clients and explore strategies to mitigate the effects of data imbalance. This would provide a more comprehensive evaluation of the proposed method and help to establish its practical applicability.

Finally, the authors should provide a more detailed analysis of the computational and communication costs associated with the proposed method. This should include an analysis of the memory requirements, training time, and communication overhead. The authors should also compare these costs with those of existing federated learning methods to demonstrate the efficiency of the proposed approach. Furthermore, the authors should discuss the limitations of the proposed method and suggest directions for future research. This would help to provide a more balanced and comprehensive assessment of the proposed method and its potential impact on the field of federated learning.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
