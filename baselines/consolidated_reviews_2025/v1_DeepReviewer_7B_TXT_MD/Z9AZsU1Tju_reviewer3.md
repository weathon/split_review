### Summary

This paper proposes an information-theoretic hierarchical perception (ITHP) model for multimodal learning. The model utilizes the concept of information bottleneck to construct compact latent states for different modalities, enabling a hierarchical fusion of multimodal information. The model is designed to distill relevant information from multiple modalities in a sequential manner, mimicking a hierarchical information processing approach observed in human cognition and neural systems. The authors evaluate the proposed model on three multimodal datasets: MUStARD, MOSI, and MOSEI, focusing on tasks such as sarcasm detection, sentiment analysis, and emotion recognition. The results demonstrate that ITHP achieves competitive performance compared to existing multimodal fusion methods and, in some cases, even surpasses human-level benchmarks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough explanation of the theoretical foundations of the ITHP model, including the formulation of optimization problems and the derivation of loss functions.
3. The paper conducts extensive experiments on multiple benchmark datasets, including MUStARD, MOSI, and MOSEI, to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with existing multimodal fusion methods. While the authors mention several related works, they do not provide a comprehensive analysis of how the proposed method differs from and improves upon these approaches. A more thorough comparison, including both quantitative and qualitative analysis, would be beneficial.
2. The paper does not provide a clear explanation of the experimental setup and the choice of hyperparameters. The authors should provide more details on how the hyperparameters were selected and how they affect the performance of the model.
3. The paper does not discuss the limitations of the proposed method and potential directions for future research. A more thorough discussion of the limitations of the proposed method and potential directions for future research would be beneficial.

### Suggestions

The paper would significantly benefit from a more rigorous comparison with existing multimodal fusion techniques. The authors should not only compare the performance metrics but also delve into the architectural differences and the underlying mechanisms of how each method processes multimodal data. For instance, methods that employ attention mechanisms might focus on dynamically weighting the importance of different modalities, while others might use a more static fusion approach. A detailed comparison should include a discussion of how the proposed ITHP model's hierarchical latent state construction and variational information bottleneck approach differ from these mechanisms. This analysis should go beyond simple performance comparisons and explore the specific strengths and weaknesses of each method in different scenarios, such as varying levels of modality correlation or different types of multimodal data. Furthermore, the authors should provide a more detailed analysis of the computational complexity of their method compared to existing approaches, which is crucial for practical applications.

To enhance the reproducibility and understanding of the experimental results, the authors should provide a comprehensive description of the experimental setup, including the specific hyperparameter settings used for each experiment. This should include not only the values of the hyperparameters but also the rationale behind their selection. For example, the authors should explain how they chose the learning rate, batch size, and the number of layers in their neural networks. Furthermore, the authors should discuss the sensitivity of their model to different hyperparameter settings. This could be done by showing how the performance of the model changes when the hyperparameters are varied. This analysis would help the reader understand the robustness of the proposed method and provide guidance for future users. The authors should also provide details on the training procedure, such as the optimization algorithm used and the convergence criteria.

Finally, the paper needs a more thorough discussion of the limitations of the proposed method and potential avenues for future research. The authors should acknowledge the potential limitations of the ITHP model, such as its computational cost, its sensitivity to hyperparameter settings, or its performance on specific types of multimodal data. For example, the authors could discuss how the model might perform when dealing with noisy or incomplete data, or when the modalities are highly dissimilar. The authors should also suggest potential directions for future research, such as exploring different architectures for the latent state construction, investigating the use of other information-theoretic measures, or applying the proposed method to other multimodal tasks. This discussion should be grounded in the current state of the literature and should provide a clear roadmap for future research in this area.

### Questions

1. How does the proposed method compare to existing multimodal fusion methods in terms of performance and computational complexity?
2. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

5

### Confidence

2

**********
