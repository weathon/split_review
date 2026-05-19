### Summary

This paper investigates the modality gap in CLIP models and its impact on intra-modal tasks like image-to-image and text-to-text retrieval. The authors demonstrate that relying solely on intra-modal similarities can lead to suboptimal performance due to the misalignment between image and text features in the shared embedding space. To address this, they propose using modality inversion techniques to transform native modality inputs into the complementary modality, which improves performance on intra-modal tasks. The paper shows that adding intra-modal loss or reducing the modality gap can further mitigate the misalignment issue. Extensive experiments across multiple datasets and models demonstrate that inter-modal representations significantly outperform intra-modal baselines on various tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The motivation is clear, and the proposed method is well-justified.
2. The paper provides a comprehensive analysis of the modality gap in CLIP models and its impact on intra-modal tasks.
3. The proposed method is simple yet effective, and the experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on image-to-image and text-to-text retrieval tasks, which may not fully capture the complexities of other intra-modal tasks such as image captioning or visual question answering. The analysis and experimental results are limited to these specific tasks, and it is unclear how the proposed modality inversion techniques would perform on tasks that require more complex reasoning or multimodal understanding. For example, image captioning requires generating a sequence of words that describe the image, which is a different task than retrieval where the goal is to find the most similar image or text. Similarly, visual question answering involves answering questions based on an image, which requires a deeper understanding of the image content and the question context.
2. While the paper demonstrates the effectiveness of modality inversion, it does not provide a detailed analysis of the computational overhead associated with this approach. The optimization-based techniques used for modality inversion can be computationally expensive, especially for large-scale datasets or complex models. The paper lacks a discussion of the time and memory requirements of the proposed method, which is a critical factor for practical applications. It is important to understand the trade-offs between performance gains and computational costs.
3. The paper does not explore the potential limitations of the proposed approach, such as its sensitivity to hyperparameter settings or its performance on datasets with different characteristics. The paper lacks a discussion of the robustness of the proposed method to different hyperparameter settings, such as the learning rate, the number of optimization steps, and the regularization parameters. It is also unclear how the method would perform on datasets with different characteristics, such as datasets with noisy or ambiguous images or text.

### Suggestions

The paper would benefit from a more comprehensive evaluation of the proposed modality inversion techniques on a wider range of intra-modal tasks. Specifically, the authors should consider including experiments on tasks such as image captioning and visual question answering to demonstrate the generalizability of their approach. These tasks would provide a more rigorous test of the method's ability to handle complex reasoning and multimodal understanding. Furthermore, the authors should analyze the performance of the proposed method on datasets with varying characteristics, such as datasets with noisy or ambiguous images or text. This would provide a better understanding of the robustness of the method and its limitations. It would also be beneficial to explore the impact of different hyperparameter settings on the performance of the proposed method. A sensitivity analysis of the hyperparameters would help to identify the optimal settings for different tasks and datasets.

To address the computational overhead concerns, the authors should provide a detailed analysis of the time and memory requirements of the proposed method. This analysis should include a comparison of the computational cost of the proposed method with that of standard intra-modal methods. The authors should also explore techniques to reduce the computational overhead of the proposed method, such as using more efficient optimization algorithms or reducing the number of optimization steps. It would be helpful to provide guidelines for selecting the appropriate hyperparameters to balance performance and computational cost. The authors should also discuss the scalability of the proposed method to large-scale datasets and models.

Finally, the paper should include a more detailed discussion of the theoretical underpinnings of the proposed method. While the authors demonstrate the effectiveness of modality inversion, they do not provide a clear explanation of why this approach works. A theoretical analysis of the method would help to provide a deeper understanding of its properties and limitations. This analysis should include a discussion of the convergence properties of the optimization algorithm and the conditions under which the proposed method is guaranteed to converge to a good solution. It would also be helpful to compare the proposed method with other existing techniques for addressing intra-modal misalignment.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
