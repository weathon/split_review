### Summary

This paper proposes a novel approach to determine the data domain of unknown black-box machine learning models, leveraging the generative capabilities of Stable Diffusion and the semantic understanding of CLIP. The method iteratively refines textual descriptions of target classes, using the model's feedback to guide the search for specific attributes within the data domain. The authors demonstrate the effectiveness of their approach through experiments on various datasets, including CIFAR-10, Places365, CelebA, and three models from the Hugging Face Model Hub. The results show that the proposed method outperforms traditional corpus-based approaches in identifying target classes and attributes.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is novel and innovative, leveraging the strengths of generative models and semantic encoders to address the challenge of forensic investigations of machine learning models.
2. The paper is well-structured and clearly written, making it easy to follow the proposed method and its evaluation.
3. The authors provide a comprehensive evaluation of the proposed method on multiple datasets and models, demonstrating its effectiveness and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies heavily on the quality of the generative model (Stable Diffusion) and semantic encoder (CLIP). The performance of the method may be affected by the limitations of these models, such as their ability to generate diverse and realistic images and their understanding of complex semantic relationships. Specifically, the reliance on CLIP's image encoder, which is trained on ImageNet, might limit its ability to generalize to datasets with different visual characteristics or domains. The method's performance could degrade if the target model's data domain contains features not well-represented in ImageNet.
2. The proposed method requires generating and evaluating multiple images for each textual description, which can be computationally expensive and time-consuming. The iterative process of generating images, extracting features, and refining descriptions could lead to a significant computational overhead, especially for large datasets or complex models. The paper does not provide a detailed analysis of the computational cost, making it difficult to assess the practical applicability of the method.
3. The paper does not provide a clear explanation of how the method handles noisy or ambiguous descriptions. The iterative refinement process may not always converge to a stable and accurate description, especially if the initial description is poor or the target model's data domain is complex and multi-faceted. The paper lacks a discussion on the robustness of the method to variations in the input descriptions.
4. The paper does not provide a detailed analysis of the limitations of the proposed method. It is unclear what types of data domains or models the method is not effective for. The paper should discuss the potential failure modes and the conditions under which the method might not perform well. For example, it is unclear how the method would perform on models trained with adversarial training or on datasets with highly complex or non-uniform distributions.

### Suggestions

The authors should investigate the sensitivity of their method to the choice of generative and semantic models. Specifically, they should explore the impact of using generative models trained on different datasets or with different architectures. For instance, using a generative model trained on a dataset more similar to the target dataset could potentially improve the quality of the generated images and, consequently, the performance of the method. Similarly, experimenting with different semantic encoders, such as those trained on different datasets or using different architectures, could provide insights into the robustness of the method. The authors should also analyze the impact of the semantic encoder's vocabulary size and its ability to capture complex semantic relationships on the overall performance. Furthermore, it would be beneficial to explore methods for adapting the semantic encoder to the specific characteristics of the target dataset, rather than relying on a fixed pre-trained model.

To address the computational cost, the authors should explore techniques for optimizing the iterative process. This could involve using more efficient generative models or employing techniques for early stopping or pruning the search space. For example, the authors could investigate the use of reinforcement learning to guide the search for optimal descriptions, rather than relying on a purely iterative approach. Additionally, the authors should provide a detailed analysis of the computational cost of their method, including the time required for each step of the process. This analysis should include a breakdown of the time spent on image generation, feature extraction, and description refinement. The authors should also explore the trade-off between computational cost and performance, and provide guidelines for selecting appropriate parameters for different datasets and models. It would be useful to compare the computational cost of their method with other existing approaches for forensic analysis of machine learning models.

Finally, the authors should provide a more detailed analysis of the method's limitations and failure modes. This should include a discussion of the types of data domains or models for which the method is not effective. For example, the authors should investigate the performance of their method on models trained with adversarial training or on datasets with highly complex or non-uniform distributions. The authors should also explore the impact of noisy or ambiguous descriptions on the performance of the method. It would be beneficial to provide a set of guidelines for selecting appropriate input descriptions for different types of data domains and models. The authors should also discuss the potential for adversarial attacks on their method, where an attacker might try to generate descriptions that lead to incorrect conclusions about the target model's data domain. This analysis should include a discussion of the robustness of the method to variations in the input descriptions and the potential for bias in the generated descriptions.

### Questions

1. How does the proposed method handle noisy or ambiguous descriptions?
2. How does the proposed method perform on models trained with adversarial training or on datasets with highly complex or non-uniform distributions?
3. What are the limitations of the proposed method, and under what conditions might it not perform well?
4. How does the computational cost of the proposed method scale with the size of the dataset or the complexity of the model?

### Rating

5

### Confidence

4

**********
