### Summary

This paper proposes a new loss function for weak-to-strong knowledge distillation. The proposed loss function adaptively adjusts the weight of hard labels and soft labels based on the discrepancy between them. The authors validate the effectiveness of the proposed method through experiments on few-shot learning, transfer learning, and noisy label learning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple yet effective.
2. The proposed method outperforms other knowledge distillation methods in various tasks.

### Weaknesses

#### Some Related Works

[1] Self-training with noisy student improves image net classification
[2] Decoupled knowledge distillation
[3] Knowledge distillation: A survey

#### comment

1. The proposed method is similar to the self-training strategy [1,2], where the student model is trained with its own predictions. The only difference is that the proposed method uses cross-entropy loss to control the weight of hard labels and soft labels, while [1,2] use confidence. Although [1] is cited in the manuscript, there is no comparison between the proposed method and [1,2]. Besides, the proposed method is also similar to the conventional knowledge distillation loss weighted by a constant factor $\beta$ [3]. The proposed method seems to be more complex as it makes $\beta$ dependent on the input.

2. The proposed method is claimed to be a weak-to-strong boosting method. However, in Table 3 and Table 7, the student models are stronger than the teacher models. Therefore, the experiments do not support the proposed claim. It would be better if the proposed method could be evaluated on more weak-to-strong settings.

### Suggestions

The core weakness of this paper lies in the limited novelty of the proposed method and the lack of rigorous experimental validation of its central claim. The adaptive weighting of hard and soft labels, while presented as a key contribution, is not sufficiently distinct from existing self-training techniques [1,2] or standard knowledge distillation with a constant weighting factor [3]. The use of cross-entropy discrepancy to modulate the weight, instead of confidence, needs more thorough justification and empirical comparison. Specifically, a direct comparison with self-training using confidence-based weighting is essential to demonstrate the advantages of the proposed approach. Furthermore, the paper should include an ablation study to analyze the impact of using cross-entropy discrepancy versus confidence for weighting, which would provide a clearer understanding of the method's behavior.

To address the concerns regarding the weak-to-strong claim, the authors should conduct experiments where the student model is demonstrably weaker than the teacher model. The current experiments, where the student models are often stronger, do not adequately support the claim of weak-to-strong boosting. It would be beneficial to explore scenarios with significant capacity differences between teacher and student, such as using a very small student model compared to a large teacher model. This would more clearly demonstrate the method's ability to transfer knowledge from a weak to a strong model. Additionally, the authors should provide a more detailed analysis of the performance gains achieved by their method in the weak-to-strong setting, compared to standard knowledge distillation or self-training. This analysis should include a discussion of the conditions under which the proposed method is most effective and the limitations of the approach.

Finally, the paper would benefit from a more in-depth discussion of the theoretical underpinnings of the proposed method. While the empirical results are promising, a theoretical analysis of why the adaptive weighting strategy works would strengthen the paper's contribution. This analysis could include a discussion of the convergence properties of the method and its relationship to existing knowledge distillation techniques. Furthermore, the authors should explore the sensitivity of the method to the choice of hyperparameters, such as the temperature parameter used in the soft labels. A more thorough investigation of these aspects would enhance the paper's overall quality and impact.

### Questions

Please see the Weaknesses.

### Rating

3

### Confidence

4

**********
