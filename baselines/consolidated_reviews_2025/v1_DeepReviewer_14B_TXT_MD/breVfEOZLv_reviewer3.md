### Summary

This paper explores the concept of weak-to-strong knowledge distillation within vision models, where a smaller, weaker model assists in training a larger, stronger model. The authors introduce an adaptively adjustable loss function that dynamically calibrates the weaker model’s supervision based on the discrepancy between soft labels and hard labels. The approach is evaluated across various scenarios, including few-shot learning, transfer learning, noisy label learning, and common knowledge distillation settings.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to follow.
2. The proposed method is evaluated across various scenarios, including few-shot learning, transfer learning, noisy label learning, and common knowledge distillation settings.

### Weaknesses

#### Some Related Works

[1] Self-training with noisy student improves imageNet classification
[2] Decoupled knowledge distillation
[3] Knowledge distillation: A survey

#### comment

1. The proposed method is similar to the self-training strategy [1,2], where the student model is trained with its own predictions. The only difference is that the proposed method uses cross-entropy loss to control the weight of hard labels and soft labels, while [1,2] use confidence. Although [1] is cited in the manuscript, there is no comparison between the proposed method and [1,2]. Besides, the proposed method is also similar to the conventional knowledge distillation loss weighted by a constant factor $\beta$ [3]. The proposed method seems to be more complex as it makes $\beta$ dependent on the input.

2. The proposed method is claimed to be a weak-to-strong boosting method. However, in Table 3 and Table 7, the student models are stronger than the teacher models. Therefore, the experiments do not support the proposed claim. It would be better if the proposed method could be evaluated on more weak-to-strong settings.

### Suggestions

The paper's primary weakness lies in the limited novelty of the proposed method and the lack of a clear distinction from existing self-training and knowledge distillation techniques. While the authors introduce an adaptive weighting scheme for combining soft and hard labels, this approach bears a strong resemblance to self-training methods that utilize student predictions for training. The key difference, using cross-entropy loss to determine the weight instead of confidence, requires more rigorous justification. A direct comparison with existing self-training methods, particularly those that employ confidence-based weighting [1,2], is crucial to demonstrate the unique advantages of the proposed method. Furthermore, the paper should include an ablation study to analyze the impact of using cross-entropy discrepancy versus confidence for weighting, which would provide a clearer understanding of the method's behavior. The authors should also clarify the specific scenarios where their method outperforms existing approaches and provide a more detailed analysis of the results.

To strengthen the claim of weak-to-strong boosting, the authors need to conduct more experiments where the student model is demonstrably weaker than the teacher model. The current experiments, where the student models are often stronger, do not adequately support the claim of weak-to-strong boosting. It would be beneficial to explore scenarios with significant capacity differences between teacher and student, such as using a very small student model compared to a large teacher model. This would more clearly demonstrate the method's ability to transfer knowledge from a weak to a strong model. Additionally, the authors should provide a more detailed analysis of the performance gains achieved by their method in the weak-to-strong setting, compared to standard knowledge distillation or self-training. This analysis should include a discussion of the conditions under which the proposed method is most effective and the limitations of the approach. The paper should also include a discussion of the computational overhead of the proposed method compared to existing techniques.

Finally, the paper would benefit from a more in-depth discussion of the theoretical underpinnings of the proposed method. While the empirical results are promising, a theoretical analysis of why the adaptive weighting strategy works would strengthen the paper's contribution. This analysis could include a discussion of the convergence properties of the method and its relationship to existing knowledge distillation techniques. Furthermore, the authors should explore the sensitivity of the method to the choice of hyperparameters, such as the temperature parameter used in the soft labels. A more thorough investigation of these aspects would enhance the paper's overall quality and impact.

### Questions

Please see the Weaknesses.

### Rating

5

### Confidence

4

**********
