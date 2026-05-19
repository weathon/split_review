### Summary

This paper proposes a novel information-theoretic hierarchical perception model for multimodal learning. The model constructs a hierarchical structure of latent states to compress and distill multimodal information, and the optimization process is achieved through the variational information bottleneck. The authors conduct experiments on several multimodal datasets, including MUStARD, CMU-MOSEI, and CMU-MOSEI, to validate the effectiveness of the proposed method.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with a clear presentation of the proposed method and experimental results.

2. The authors provide a thorough explanation of the theoretical foundations of the ITHP model, including the formulation of optimization problems and the derivation of loss functions.

3. The paper conducts extensive experiments on multiple benchmark datasets, including MUStARD, CMU-MOSEI, and CMU-MOSEI, to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with existing multimodal fusion methods. While the authors mention several related works, they do not provide a comprehensive analysis of how the proposed method differs from and improves upon these approaches. A more thorough comparison, including both quantitative and qualitative analysis, would be beneficial.

2. The paper does not provide a clear explanation of the experimental setup and the choice of hyperparameters. The authors should provide more details on how the hyperparameters were selected and how they affect the performance of the model.

3. The paper does not discuss the limitations of the proposed method and potential directions for future research. A more thorough discussion of the limitations of the proposed method and potential directions for future research would be beneficial.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing multimodal fusion techniques. While the authors mention several related works, a deeper analysis is needed to highlight the specific advantages of the proposed Information-Theoretic Hierarchical Perception (ITHP) model. For instance, the paper should discuss how ITHP's hierarchical latent state construction and variational information bottleneck approach differ from methods that use attention mechanisms or recurrent neural networks for fusion. A quantitative comparison, using metrics relevant to each task (e.g., accuracy for classification, F1-score for sentiment analysis, MAE for regression), would be essential to demonstrate the superiority of ITHP. Furthermore, a qualitative analysis, such as visualizing the learned latent spaces or analyzing the attention weights, could provide insights into how ITHP captures and integrates multimodal information. This would help to better position the proposed method within the existing literature and highlight its unique contributions.

To improve the clarity and reproducibility of the experimental results, the authors should provide a more detailed description of the experimental setup and the selection of hyperparameters. Specifically, the paper should include a table or a section that lists all the hyperparameters used in the experiments, along with the range of values explored during the hyperparameter search. The authors should also explain the criteria used to select the optimal hyperparameters, such as cross-validation or grid search. Furthermore, the paper should discuss the sensitivity of the model to different hyperparameter settings. For example, how does the performance of the model change when the Lagrange multipliers for the information bottleneck are varied? This analysis would help to understand the robustness of the proposed method and provide guidance for future users.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential directions for future research. For example, the authors should discuss the computational complexity of the ITHP model and how it scales with the number of modalities and the size of the input data. They should also discuss the potential challenges of applying the proposed method to real-world scenarios, such as noisy or incomplete data. Furthermore, the authors should suggest potential avenues for future research, such as exploring different architectures for the latent state construction or investigating the use of other information-theoretic measures. This would help to position the proposed method within the broader context of multimodal learning and highlight its potential for future development.

### Questions

1. How does the proposed method compare to existing multimodal fusion methods in terms of performance and computational complexity?

2. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

5

### Confidence

3

**********
