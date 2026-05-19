### Summary

This paper proposes OmniSep, an omni-modal sound separation model that can separate sounds based on text, image, or audio queries. The model uses a Query-Mixup strategy to mix different modal embeddings during training, allowing it to optimize each modality concurrently. Additionally, a negative query is introduced to remove unwanted sound information, and a Query-Augment approach is proposed to enable open-vocabulary sound separation using unrestricted natural language descriptions. Experimental results demonstrate that OmniSep achieves state-of-the-art performance in sound separation tasks across different modalities.

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
4. Experimental results demonstrate that OmniSep achieves state-of-the-art performance in sound separation tasks across different modalities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed method, particularly in comparison to existing approaches. This is crucial for understanding the practical applicability of the model in real-world scenarios. Specifically, the paper lacks a breakdown of the computational cost associated with each component of the model, such as the embedding extraction, the separation network, and the negative query processing. Furthermore, the memory footprint of the model, especially during training with multiple modalities, is not discussed, which is a critical factor for deployment on resource-constrained devices.
2. The paper does not provide a detailed analysis of the limitations of the proposed method, such as its performance on complex sound mixtures or its robustness to variations in audio quality. The evaluation primarily focuses on relatively clean audio samples, and it is unclear how the model would perform in more challenging scenarios, such as those with significant background noise, overlapping sound sources, or variations in the acoustic environment. The paper should also discuss the sensitivity of the model to the quality of the input queries, particularly in cases where the queries are ambiguous or noisy.
3. The paper does not provide a detailed analysis of the generalization capabilities of the proposed method, particularly in scenarios that are not covered by the training data. The experiments are conducted on specific datasets, and it is unclear how well the model would generalize to unseen audio events or different acoustic environments. The paper should include experiments on more diverse datasets, including those with a wider range of sound sources and acoustic conditions, to assess the robustness of the model. Furthermore, the paper should discuss the potential for domain adaptation or fine-tuning to improve the model's performance on new tasks.

### Suggestions

To address the lack of computational analysis, the authors should provide a detailed breakdown of the computational cost of each component of the model, including the embedding extraction, the separation network, and the negative query processing. This analysis should include both time and memory requirements, and should be compared to existing approaches. The authors should also investigate the scalability of the model by evaluating its performance with increasing numbers of modalities and longer audio sequences. Furthermore, the authors should explore techniques for optimizing the model's efficiency, such as model pruning or quantization, to reduce its computational footprint. This would make the model more practical for real-world applications, especially in resource-constrained environments.

To improve the evaluation of the model's robustness, the authors should conduct experiments on more challenging datasets that include complex sound mixtures, background noise, and variations in audio quality. The evaluation should also include a quantitative analysis of the model's performance under different noise levels and acoustic conditions. The authors should also investigate the sensitivity of the model to the quality of the input queries, particularly in cases where the queries are ambiguous or noisy. This could involve adding noise to the queries or using queries with varying levels of detail. The authors should also explore techniques for improving the model's robustness, such as data augmentation or adversarial training. This would provide a more comprehensive understanding of the model's limitations and its potential for real-world applications.

To enhance the generalization capabilities of the model, the authors should conduct experiments on more diverse datasets that include a wider range of sound sources and acoustic conditions. This could involve using datasets that are not covered by the training data, such as datasets with different types of audio equipment or different acoustic environments. The authors should also investigate the potential for domain adaptation or fine-tuning to improve the model's performance on new tasks. This could involve training the model on a small set of target data or using techniques such as transfer learning. The authors should also provide a detailed analysis of the model's performance on different types of sound sources and acoustic conditions, to identify any limitations or biases. This would provide a more comprehensive understanding of the model's generalization capabilities and its potential for real-world applications.

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
