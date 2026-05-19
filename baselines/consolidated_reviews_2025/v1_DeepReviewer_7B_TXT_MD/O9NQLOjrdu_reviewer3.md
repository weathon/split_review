### Summary

The paper presents a simple method for zero-shot image classification that leverages multimodal large language models (LLMs) to enhance classification accuracy. The proposed approach generates textual descriptions of input images and combines these with initial predictions to improve zero-shot classification performance. The method achieves state-of-the-art results on multiple datasets, demonstrating its effectiveness and potential for practical applications.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a straightforward yet effective method for zero-shot image classification that leverages the power of multimodal large language models (LLMs). The simplicity of the approach makes it easy to implement and understand, which is a significant advantage for practical applications.

2. The paper presents comprehensive experimental results on multiple datasets, demonstrating the effectiveness of the proposed method. The results show significant improvements over existing zero-shot classification methods, highlighting the potential of the approach.

3. The paper is well-written and organized, making it easy for readers to follow the methodology and results. The clear presentation of the method and experiments contributes to the overall quality of the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed method, which could be a concern for practical applications. The use of large language models (LLMs) for generating textual descriptions of images can be computationally expensive, and the paper does not discuss the time and resources required for this step. Furthermore, the paper lacks a discussion on the memory footprint of storing and processing these textual descriptions, which is crucial for real-world deployment.

2. The paper does not explore the robustness of the proposed method to variations in image quality, such as different lighting conditions, occlusions, or image distortions. While the method may perform well on clean images, its performance on degraded images is unclear. The paper should include experiments that evaluate the method's performance under various image quality conditions to assess its practical applicability.

3. The paper does not discuss the potential limitations of the proposed method, such as its sensitivity to the choice of LLM or the quality of the generated textual descriptions. The paper should include a discussion on how the performance of the method varies with different LLMs and prompt designs. Additionally, the paper should address the potential for the generated textual descriptions to be misleading or inaccurate, and how this might affect the classification performance.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed method. This analysis should include the time required for generating textual descriptions using the LLM, the memory footprint of storing these descriptions, and the overall time required for the classification process. The authors should also compare the computational cost of their method with existing zero-shot image classification techniques to provide a clear understanding of the trade-offs involved. Furthermore, the paper should explore techniques to reduce the computational cost, such as using smaller or more efficient LLMs, or employing techniques like knowledge distillation to transfer the knowledge of the LLM to a smaller model.

To address the robustness concerns, the paper should include experiments that evaluate the method's performance under various image quality conditions. This could involve introducing controlled variations in lighting, occlusions, and image distortions, and then measuring the classification accuracy under these conditions. The authors should also investigate the impact of different prompt designs on the quality of the generated textual descriptions and the overall classification performance. This analysis should include a discussion on how the method performs when the generated descriptions are noisy or inaccurate. The paper should also explore techniques to improve the robustness of the method, such as using ensemble methods or data augmentation techniques.

Finally, the paper should include a more thorough discussion of the potential limitations of the proposed method. This discussion should include an analysis of how the performance of the method varies with different LLMs and prompt designs. The authors should also address the potential for the generated textual descriptions to be misleading or inaccurate, and how this might affect the classification performance. The paper should also discuss the potential for bias in the generated textual descriptions and how this might affect the classification results. The authors should also explore techniques to mitigate these limitations, such as using adversarial training or data augmentation techniques.

### Questions

1. How does the proposed method perform on datasets with highly complex or ambiguous images where textual descriptions may not be easily generated?

2. What is the computational cost of using large language models (LLMs) for generating textual descriptions of images, and how does this scale with the size of the dataset?

3. How robust is the proposed method to variations in image quality, such as different lighting conditions, occlusions, or image distortions?

4. How sensitive is the proposed method to the choice of LLM or the specific prompt design used for generating textual descriptions?

5. What are the potential limitations of the proposed method, and how can they be addressed?

### Rating

6

### Confidence

4

**********
