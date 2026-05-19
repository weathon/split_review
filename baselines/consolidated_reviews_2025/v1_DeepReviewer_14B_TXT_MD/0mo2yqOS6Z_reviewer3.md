### Summary

This paper presents a novel approach to enhance the accuracy and parameter efficiency of neural networks through the use of predictor networks for weight parameterization. The authors introduce a new training scheme that decouples the reconstruction objective from auxiliary objectives, such as knowledge distillation, leading to significant improvements in model performance and compression. The key contributions include demonstrating that the reconstruction loss alone can improve model accuracy, proposing a progressive training method to compound performance gains, and showing that decoupled training enhances both accuracy and parameter efficiency. The approach is validated through extensive experiments on various datasets and architectures, including CIFAR-10, CIFAR-100, STL-10, and ImageNet, with results showing improved robustness and generalization.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel and surprising finding that the reconstruction loss alone can improve model accuracy, which challenges conventional wisdom and opens new avenues for research in neural network optimization.
2. The proposed decoupled training strategy and progressive training method are innovative and demonstrate significant improvements in both accuracy and parameter efficiency compared to existing approaches like NeRN.
3. The experiments are thorough and well-designed, covering multiple datasets and architectures, and including evaluations of robustness and generalization, which strengthens the validity of the findings.
4. The paper provides a detailed analysis of the underlying factors contributing to the performance improvements, such as the smoothing effect of the reconstruction loss, which adds depth and clarity to the research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed approach, particularly in scenarios where the predictor network capacity is constrained or when applied to different types of neural architectures. The current analysis lacks a rigorous exploration of how the predictor network's size and architecture impact the effectiveness of the proposed method. For instance, it is unclear how the performance degrades when the predictor network is significantly smaller than the original network, or if specific architectural choices for the predictor network are more suitable than others. A more thorough investigation into these aspects would provide a more complete understanding of the method's applicability.
2. While the paper focuses on CNN architectures, it would be valuable to explore the potential of extending the proposed approach to other types of neural networks, such as recurrent neural networks or transformers. The current scope limits the generalizability of the findings. The method's effectiveness might be highly dependent on the specific structure of CNNs, and it is not clear if the same approach can be directly applied to other architectures without significant modifications. The paper should at least discuss the challenges and potential adaptations required for these different architectures.
3. The paper could provide more insights into the computational overhead of the proposed training scheme, especially in comparison to traditional training methods. The paper lacks a detailed analysis of the computational cost associated with the proposed method, including the training time and memory requirements. It is important to quantify the additional computational burden introduced by the predictor network and the decoupled training process, and compare it with the computational cost of standard training methods. This analysis should also consider the impact of different predictor network sizes on the overall computational overhead.

### Suggestions

To address the limitations regarding predictor network capacity, the authors should conduct a more detailed analysis of how the predictor network's size and architecture affect the performance of the proposed method. This should include experiments with predictor networks of varying sizes, ranging from very small to relatively large, and a discussion of the trade-offs between predictor network size, computational cost, and the resulting model accuracy. Furthermore, the authors should explore different architectural choices for the predictor network, such as using different activation functions, numbers of layers, or layer widths, and analyze how these choices impact the effectiveness of the method. This analysis should provide clear guidelines on how to select an appropriate predictor network architecture for a given task and resource constraint. The authors should also investigate the sensitivity of the method to the initialization of the predictor network and provide recommendations on how to initialize it for optimal performance.

To broaden the scope of the research, the authors should investigate the applicability of the proposed method to other types of neural networks, such as recurrent neural networks (RNNs) and transformers. This should include a discussion of the challenges and potential adaptations required to apply the method to these architectures. For example, the authors could explore how to define the reconstruction loss for RNNs, which have temporal dependencies, and how to handle the different parameter structures of transformers. The authors should also conduct experiments on these architectures to validate the effectiveness of the proposed method and compare it with existing training techniques. This would significantly enhance the generalizability of the findings and demonstrate the broader applicability of the proposed approach.

Finally, the authors should provide a more detailed analysis of the computational overhead of the proposed training scheme. This should include a comparison of the training time and memory requirements of the proposed method with those of traditional training methods. The authors should also analyze the impact of different predictor network sizes on the computational overhead and provide guidelines on how to select a predictor network size that balances performance and computational cost. This analysis should be presented in a clear and concise manner, with quantitative data to support the claims. The authors should also discuss the potential for optimizing the training process to reduce the computational overhead, such as using techniques like gradient checkpointing or mixed-precision training.

### Questions

1. How does the proposed method perform when applied to very deep neural networks or models with a large number of parameters? Are there any scalability issues that need to be addressed?
2. Can the authors provide more insights into the choice of hyperparameters for the progressive training method, such as the number of rounds and the learning rate schedule? How sensitive is the performance to these hyperparameters?
3. The paper mentions the smoothing effect of the reconstruction loss. Could the authors elaborate on how this smoothing effect contributes to the improved generalization and robustness of the model? Are there any theoretical insights or empirical evidence to support this claim?
4. How does the proposed method compare to other state-of-the-art techniques for model compression and knowledge distillation in terms of both accuracy and parameter efficiency? Are there any scenarios where the proposed method might be preferred over existing techniques?

### Rating

6

### Confidence

3

**********
