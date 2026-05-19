### Summary

This paper introduces Uni-O4, a unified framework for offline and offline-to-online reinforcement learning (RL). The authors propose a novel approach that leverages an ensemble of policies to address the mismatch between the estimated behavior policy and the offline dataset. They also introduce an offline policy evaluation (OPE) method, called AM-Q, to achieve multi-step policy improvement without requiring online evaluation. The proposed method is evaluated on a variety of simulated and real-world tasks, demonstrating its effectiveness in both offline and offline-to-online settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a detailed explanation of the proposed method.
2. The proposed method, Uni-O4, is a novel and unified approach for offline and offline-to-online RL. The use of an ensemble of policies to address the mismatch between the estimated behavior policy and the offline dataset is an interesting idea.
3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method in both offline and offline-to-online settings. The authors compare their method with a wide range of baselines and show that Uni-O4 achieves competitive performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors mention that the method is computationally efficient, they do not provide any quantitative analysis of the computational resources required for training and inference. This makes it difficult to assess the practical applicability of the method.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters. The authors mention that the method is robust to hyperparameter settings, but they do not provide any experimental results to support this claim. It is important to understand how the performance of the method varies with different hyperparameter values.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. The authors do not discuss the potential challenges of applying the method to real-world problems, such as high-dimensional state and action spaces, or the presence of noise in the offline dataset.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of their method. This should include a breakdown of the time and memory requirements for each component of the algorithm, as well as a comparison with other offline-to-online RL methods. Specifically, the authors should quantify the computational overhead of training the ensemble of policies and performing offline policy evaluation (OPE). It would be beneficial to report the training time, inference time, and memory usage for different problem settings and dataset sizes. This analysis should also consider the impact of the ensemble size on the computational cost. Furthermore, the authors should discuss the scalability of their method to larger datasets and more complex environments. This analysis is crucial for assessing the practical applicability of the proposed method in real-world scenarios.

To address the lack of hyperparameter sensitivity analysis, the authors should conduct a more comprehensive study of how the performance of Uni-O4 varies with different hyperparameter values. This should include a systematic exploration of the hyperparameter space, using techniques such as grid search or random search. The authors should report the performance of the method for different combinations of hyperparameters, and they should provide insights into how the different hyperparameters affect the learning process. For example, the authors could investigate the impact of the ensemble size, the learning rate, and the regularization parameters on the performance of the method. It would also be helpful to provide guidelines for selecting appropriate hyperparameter values for different problem settings. This analysis is essential for ensuring the robustness and reliability of the proposed method.

Finally, the authors should provide a more detailed discussion of the limitations of their method. This should include a discussion of the potential challenges of applying the method to real-world problems, such as high-dimensional state and action spaces, or the presence of noise in the offline dataset. The authors should also discuss the potential impact of these challenges on the performance of the method. For example, the authors could investigate the performance of the method in environments with high-dimensional state spaces, or in environments with noisy observations. It would also be helpful to discuss the potential limitations of the offline policy evaluation (OPE) method, and to suggest potential directions for future research. This discussion is crucial for providing a balanced and realistic assessment of the proposed method.

### Questions

1. How does the proposed method handle the exploration-exploitation trade-off during online fine-tuning?
2. How does the proposed method perform in environments with high-dimensional state and action spaces?

### Rating

6

### Confidence

4

**********
