### Summary

This paper introduces OmniSep, an omni-modal sound separation model that can separate sounds based on text, image, or audio queries. The authors propose a novel Query-Mixup strategy to mix different modal embeddings during training, enabling the model to optimize each modality concurrently and achieve a unified sound separation model. The paper also introduces a negative query to remove unwanted sound information and a Query-Augment approach to enable open-vocabulary sound separation using unrestricted natural language descriptions. The experimental results demonstrate that OmniSep achieves state-of-the-art performance in sound separation tasks across different modalities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel omni-modal sound separation model that can handle text, image, and audio queries, addressing limitations in existing methods that are limited to single-modal inputs.
2. The proposed Query-Mixup strategy allows the model to mix different modal embeddings during training, enabling it to optimize each modality concurrently and achieve a unified sound separation model.
3. The paper introduces a negative query approach to remove unwanted sound information and a Query-Augment approach to enable open-vocabulary sound separation using unrestricted natural language descriptions.
4. The experimental results demonstrate that OmniSep achieves state-of-the-art performance in sound separation tasks across different modalities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed method, particularly in comparison to existing approaches. This is crucial for understanding the practical applicability of the model in real-world scenarios. Specifically, the paper lacks a breakdown of the computational cost associated with each component of the model, such as the embedding extraction, the separation network, and the negative query processing. Furthermore, the memory footprint of the model, especially during training with multiple modalities, is not discussed, which is a critical factor for deployment on resource-constrained devices.
2. The paper does not provide a detailed analysis of the limitations of the proposed method, such as its performance on complex sound mixtures or its robustness to variations in audio quality. The evaluation primarily focuses on relatively clean audio samples, and it is unclear how the model would perform in more challenging scenarios, such as those with significant background noise, overlapping sound sources, or variations in the acoustic environment. The paper should also discuss the sensitivity of the model to the quality of the input queries, particularly in cases where the queries are ambiguous or noisy.
3. The paper does not provide a detailed analysis of the generalization capabilities of the proposed method, particularly in scenarios that are not covered by the training data. The experiments are conducted on specific datasets, and it is unclear how well the model would generalize to unseen audio events or different acoustic environments. The paper should include experiments on more diverse datasets, including those with a wider range of sound sources and acoustic conditions, to assess the robustness of the model. Furthermore, the paper should discuss the potential for domain adaptation or fine-tuning to improve the model's performance on new tasks.

### Suggestions

The paper would benefit from a more thorough analysis of the computational aspects of the proposed OmniSep model. Specifically, a detailed breakdown of the time and memory requirements for each component of the model, including the embedding extraction, the separation network, and the negative query processing, should be provided. This analysis should compare the computational cost of OmniSep with existing approaches, highlighting any potential bottlenecks or areas for optimization. Furthermore, the paper should discuss the scalability of the model with respect to the number of modalities and the length of the audio sequences. This would provide a more complete understanding of the practical applicability of the model in real-world scenarios, especially in resource-constrained environments. The authors should also consider providing a more detailed analysis of the model's performance under different computational constraints, such as varying batch sizes or hardware configurations.

To address the limitations regarding robustness and generalization, the authors should conduct experiments on more challenging datasets that include complex sound mixtures, background noise, and variations in audio quality. This would provide a more realistic assessment of the model's performance in real-world scenarios. The paper should also include a detailed analysis of the model's sensitivity to the quality of the input queries, particularly in cases where the queries are ambiguous or noisy. This analysis should explore the impact of different types of noise and variations in the queries on the model's performance. Furthermore, the authors should investigate the potential for domain adaptation or fine-tuning to improve the model's performance on new tasks. This could involve training the model on a small set of target data or using techniques such as transfer learning. The paper should also discuss the potential for the model to generalize to unseen audio events or different acoustic environments, and provide a more detailed analysis of the model's performance on diverse datasets.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method, including its performance on complex sound mixtures and its robustness to variations in audio quality. The authors should also discuss the potential for domain adaptation or fine-tuning to improve the model's performance on new tasks. This would provide a more balanced and realistic assessment of the model's capabilities and limitations. The paper should also include a more detailed analysis of the model's generalization capabilities, particularly in scenarios that are not covered by the training data. This could involve training the model on a more diverse set of datasets and evaluating its performance on unseen audio events or different acoustic environments. The authors should also discuss the potential for domain adaptation or fine-tuning to improve the model's performance on new tasks.

### Questions

1. How does the proposed method perform on complex sound mixtures or in noisy environments?
2. How does the model handle variations in audio quality or different acoustic environments?
3. How does the model generalize to unseen audio events or different acoustic environments?
4. What are the computational requirements and efficiency of the proposed method compared to existing approaches?

### Rating

6

### Confidence

4

**********
