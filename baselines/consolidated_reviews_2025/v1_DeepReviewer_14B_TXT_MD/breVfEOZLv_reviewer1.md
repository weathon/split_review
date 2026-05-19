### Summary

This paper proposes a weak-to-strong knowledge distillation method, where a smaller model teaches a larger model. The proposed method adaptively adjusts the weight between the hard label and soft label based on the cross-entropy loss. Experiments are conducted on image classification, few-shot learning, transfer learning, and learning with noisy labels.

### Soundness

2

### Presentation

1

### Contribution

1

### Strengths

* The proposed method is easy to understand.
* The proposed method works well when the teacher label is inaccurate.

### Weaknesses

#### Some Related Works

[1] Self-training with noisy student improves imageNet classification, CVPR 20
[2] Decoupled Knowledge Distillation, CVPR 22

#### comment

 * The paper lacks a clear motivation. The proposed method appears to be a variant of AugConf, which adjusts the weight between hard labels and soft labels. However, the limitations of AugConf and the advantages of the proposed method are not clearly explained.
* The proposed method has a limited novel contribution. Similar ideas have been explored in previous works, such as self-training with a noisy student [1], which uses cross-entropy loss to adjust the weight between the soft and hard labels. Another example is Decoupled Knowledge Distillation [2], which employs a similar approach with a consistency weight. The proposed method lacks a clear motivation and novel contribution.
* The writing is unclear. Section 3.1, which discusses the selection of the vision model, seems irrelevant to the proposed method. Additionally, the paper contains several typos and errors, such as "Table 4b" in Section 4.2.1, which makes it difficult to read.

#### questions:
 * Table 3 shows that a ViT-Base achieves 85.06% with AdaptConf and 85.00% with the teacher. This result is surprising because it suggests that the student's performance exceeds that of the teacher, which contradicts the expected outcome of weak-to-strong learning. Could you provide a justification for this result?

### Suggestions

The paper needs a more thorough explanation of the limitations of existing methods, particularly AugConf, to justify the proposed approach. The current explanation is insufficient to demonstrate the novelty of the method. A detailed analysis of why a fixed weighting scheme is inadequate and how the proposed adaptive weighting addresses these specific shortcomings is necessary. For example, the authors could discuss scenarios where a fixed weight might lead to suboptimal performance, such as when the teacher's predictions are highly uncertain or when the student model is significantly more capable than the teacher. The paper should also include a more in-depth comparison with existing methods that use similar weighting strategies, such as self-training with a noisy student and decoupled knowledge distillation. A clear explanation of how the proposed method differs from these approaches and why these differences lead to improved performance is crucial. Specifically, the authors should analyze the mathematical formulations of these methods and highlight the unique aspects of their approach. The paper should also provide a more detailed analysis of the experimental results, including a discussion of the performance differences between the proposed method and the baselines. The authors should also provide a more detailed analysis of the experimental results, including a discussion of the performance differences between the proposed method and the baselines. For example, the authors could analyze the convergence behavior of the proposed method and compare it to that of the baselines. They could also analyze the sensitivity of the proposed method to different hyperparameter settings and compare it to that of the baselines.

The writing needs to be significantly improved to enhance clarity and readability. Section 3.1, which discusses the selection of the vision model, should be either removed or rewritten to directly relate to the proposed method. The paper should also be carefully proofread to eliminate typos and errors, such as the incorrect reference to "Table 4b". The authors should also consider restructuring the paper to improve the flow of ideas. For example, the motivation for the proposed method should be clearly stated in the introduction, and the related work should be discussed in detail in the related work section. The paper should also include a clear and concise explanation of the proposed method, including a detailed description of the adaptive weighting mechanism. The authors should also provide a more detailed explanation of the experimental setup, including the datasets, evaluation metrics, and hyperparameter settings. The paper should also include a more detailed discussion of the limitations of the proposed method and potential directions for future research.

Finally, the surprising result in Table 3, where the student outperforms the teacher, needs a more thorough explanation. The authors should provide a detailed analysis of why this occurs and how it aligns with the principles of weak-to-strong learning. It is crucial to investigate whether this result is consistent across different datasets and model architectures. The authors should also consider the possibility that the teacher model is not sufficiently strong or that the training procedure is not optimal. A more rigorous analysis of the teacher and student models' capabilities and the training dynamics is needed to justify this result. The authors should also consider adding additional experiments to further investigate this phenomenon, such as varying the capacity gap between the teacher and student models or using different training strategies.

### Questions

* Table 3 shows that a ViT-Base achieves 85.06% with AdaptConf and 85.00% with the teacher. This result is surprising because it suggests that the student's performance exceeds that of the teacher, which contradicts the expected outcome of weak-to-strong learning. Could you provide a justification for this result?

### Rating

3

### Confidence

4

**********
