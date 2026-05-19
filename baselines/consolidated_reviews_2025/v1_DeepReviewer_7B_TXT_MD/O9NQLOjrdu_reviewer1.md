### Summary

The paper proposes an innovative approach to enhance zero-shot image classification by leveraging multimodal large language models (LLMs). The method generates comprehensive textual descriptions of input images and combines these with initial class predictions to improve classification accuracy. The approach is straightforward, requires no dataset-specific tuning, and achieves significant performance gains across multiple datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach by integrating multimodal LLMs into zero-shot image classification, generating detailed textual descriptions to enrich image representation.
2. The method is straightforward and easy to implement, requiring no dataset-specific tuning.
3. The approach achieves substantial performance gains across multiple datasets, demonstrating its effectiveness and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with using multimodal LLMs, which could be a significant factor in practical applications.
2. The paper does not explore the sensitivity of the method to different LLMs or prompt designs, which could impact the robustness and generalizability of the approach.
3. The paper does not discuss the potential limitations of the method when dealing with complex or ambiguous images that may not have clear textual descriptions.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the proposed method. Specifically, it should detail the time complexity of each step, including the generation of textual descriptions by the LLM, the encoding of these descriptions and images, and the final classification. This analysis should not only consider the theoretical complexity but also provide empirical measurements of runtime and memory usage on different hardware configurations. Furthermore, the paper should investigate the scalability of the method with respect to image resolution and batch size. This would provide a more complete picture of the practical feasibility of the approach, especially for real-time applications or resource-constrained environments. It would also be beneficial to compare the computational cost of the proposed method with other zero-shot image classification techniques.

To address the sensitivity to different LLMs and prompt designs, the paper should conduct a more extensive ablation study. This study should systematically evaluate the impact of using different LLMs, such as GPT-3.5, GPT-4, and other available models, on the final classification performance. The study should also explore the effect of varying the prompt design, including the inclusion of different types of instructions and examples. For example, the paper could investigate the impact of using more detailed prompts that explicitly ask the LLM to generate descriptions focusing on specific image features. Additionally, the paper should analyze the variance in performance across different LLMs and prompt designs to understand the robustness of the method. This would provide valuable insights into the factors that contribute to the method's success and help identify potential limitations.

Finally, the paper should address the limitations of the method when dealing with complex or ambiguous images. The paper should discuss scenarios where the LLM-generated descriptions may be inaccurate or incomplete, and how this could impact the final classification. For example, the paper could investigate the performance of the method on images with multiple objects, occlusions, or unusual viewpoints. The paper should also explore potential strategies for mitigating these limitations, such as incorporating additional image features or using more sophisticated fusion techniques. Furthermore, the paper should discuss the potential for using the LLM-generated descriptions as a form of data augmentation to improve the robustness of the classification model. This would provide a more comprehensive understanding of the method's capabilities and limitations.

### Questions

1. How does the method perform on datasets with highly ambiguous or complex images where textual descriptions may not be easily generated?
2. What is the computational cost of using multimodal LLMs for each image, and how does this scale with the size of the dataset?
3. How sensitive is the method to the choice of LLM or the specific prompt design used for generating textual descriptions?

### Rating

5

### Confidence

4

**********
