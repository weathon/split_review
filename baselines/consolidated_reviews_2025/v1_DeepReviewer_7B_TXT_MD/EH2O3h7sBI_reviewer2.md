### Summary

This paper proposes a new continual learning method, prompt gradient projection (PGP), which combines prompt-tuning with gradient projection. The authors claim that the proposed method can reduce forgetting. The authors conduct experiments on three datasets to demonstrate the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors propose a new method for continual learning, which combines prompt-tuning with gradient projection.
2. The authors conduct experiments on three datasets to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method can reduce forgetting. However, the authors do not provide a theoretical analysis of the proposed method to prove that it can reduce forgetting.
2. The authors do not provide a detailed analysis of the computational cost of the proposed method.
3. The authors do not provide a detailed analysis of the memory cost of the proposed method.
4. The authors do not provide a detailed analysis of the scalability of the proposed method.

### Suggestions

The paper introduces an interesting approach by combining prompt tuning with gradient projection for continual learning. However, the lack of theoretical grounding is a significant weakness. While empirical results are presented, a theoretical analysis demonstrating how the proposed method mitigates catastrophic forgetting is crucial. The authors should provide a formal proof or a detailed argument explaining why the gradient projection, when applied to the prompt parameters, leads to better retention of previously learned knowledge. This could involve analyzing the gradient updates and showing that they do not significantly interfere with the learning of past tasks. Furthermore, the analysis should consider the interaction between the prompt parameters and the model parameters, and how the gradient projection affects this interaction. Without such analysis, the claim of reduced forgetting remains unsubstantiated.

Additionally, the paper needs a more thorough analysis of the computational and memory costs associated with the proposed method. The authors should provide a detailed breakdown of the time and memory requirements for both training and inference. This analysis should compare the proposed method with existing continual learning techniques, highlighting the trade-offs between performance and computational resources. For example, the authors should quantify the memory footprint of storing the prompt parameters and the gradients, and how this scales with the number of tasks and the size of the model. Furthermore, the computational cost should be analyzed in terms of the number of forward and backward passes required for each task. This analysis is essential for understanding the practical applicability of the proposed method, especially in resource-constrained environments. The authors should also discuss the potential for optimization to reduce the computational and memory overhead.

Finally, the scalability of the proposed method needs further investigation. The authors should provide experimental results on a larger number of tasks and datasets to demonstrate the method's ability to handle more complex continual learning scenarios. It is important to analyze how the performance of the proposed method degrades as the number of tasks increases. The authors should also investigate the impact of different hyperparameters on the scalability of the method. For example, how does the learning rate or the projection parameter affect the performance on a large number of tasks? The authors should also discuss the potential limitations of the proposed method in terms of scalability and identify potential areas for improvement. This analysis should include a discussion of the computational complexity of the method as the number of tasks increases, and how this compares to other continual learning methods.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
