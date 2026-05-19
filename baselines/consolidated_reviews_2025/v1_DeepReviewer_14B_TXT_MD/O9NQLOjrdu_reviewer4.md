### Summary

The paper proposes a zero-shot image classification method using multimodal large language models (LLMs). The method generates textual representations from input images, fuses these with visual features, and performs classification using a linear classifier. The approach outperforms existing methods on multiple benchmark datasets without requiring dataset-specific prompt engineering.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is simple and effective, achieving state-of-the-art results on multiple datasets.
2. The method does not require prompt engineering for each dataset, making it more practical and easier to use.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The main contribution of this paper is the introduction of multimodal large language models (LLMs) to generate text descriptions for zero-shot image classification. However, this approach is quite straightforward and lacks innovation. The use of LLMs to generate textual descriptions, while effective, does not represent a significant departure from existing techniques that leverage multimodal embeddings for similar tasks. The core idea of using a text description as an intermediate representation is not new, and the paper does not sufficiently demonstrate a novel way of integrating this with LLMs.
2. The method relies on the availability and performance of multimodal LLMs, which may not be accessible or feasible in all settings. The computational cost and resource requirements of these models could be a limiting factor for practical applications, especially in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead or the scalability of the proposed method, which is a critical aspect for real-world deployment.
3. The paper does not provide a thorough analysis of the limitations and potential drawbacks of the proposed method. For example, the impact of the quality of the generated text descriptions on the classification accuracy is not discussed. The paper lacks a sensitivity analysis on how variations in the quality of the generated text descriptions affect the final classification performance. It is unclear how the method would perform with noisy or inaccurate descriptions, which is a crucial consideration for robustness.

### Suggestions

The paper should explore alternative methods for generating textual representations that do not rely on computationally expensive multimodal LLMs. For instance, the authors could investigate techniques such as using pre-trained vision-language models to extract pseudo-textual embeddings directly from images, or employing lightweight text generation models that are less resource-intensive. This would make the method more accessible and practical for a wider range of applications. Furthermore, the paper should include a detailed analysis of the computational cost associated with the proposed method, including the time and memory requirements for both training and inference. This analysis should compare the proposed method with existing approaches to provide a clear understanding of its computational efficiency. The authors should also investigate the scalability of the method, particularly when dealing with large-scale datasets, and discuss potential strategies for optimizing its performance in such scenarios.

To address the lack of analysis on the impact of text description quality, the authors should conduct a thorough sensitivity analysis. This analysis should involve generating text descriptions with varying levels of quality, perhaps by introducing noise or using different generation models, and then evaluating the impact on classification accuracy. This would provide valuable insights into the robustness of the method and its sensitivity to the quality of the generated text. The paper should also explore methods for improving the quality of the generated text descriptions, such as using techniques for error correction or incorporating feedback from the classification results. This would help to mitigate the impact of noisy or inaccurate descriptions and improve the overall performance of the method. Additionally, the authors should investigate the limitations of the method in handling ambiguous or complex images, where generating accurate text descriptions might be challenging.

Finally, the paper should include a more comprehensive comparison with existing zero-shot image classification methods, including those that do not rely on LLMs. This comparison should not only focus on accuracy but also consider other factors such as computational cost, memory requirements, and robustness. The authors should also discuss the potential limitations of the proposed method in specific application scenarios, such as medical imaging or remote sensing, where the characteristics of the images might differ significantly from the datasets used in the evaluation. This would provide a more complete understanding of the applicability and limitations of the method and guide future research in this area.

### Questions

1. How does the proposed method perform in terms of computational efficiency and scalability compared to existing methods?
2. What are the potential limitations or challenges of the proposed method in specific application scenarios, such as medical imaging or remote sensing?
3. How does the quality of the generated text descriptions impact the classification accuracy? Are there any methods to improve the quality of the generated text descriptions?

### Rating

6

### Confidence

3

**********
