### Summary

This paper addresses the issue of architecture overfitting in dataset distillation, where performance degrades when testing networks with different architectures than those used to create the distilled dataset. The authors propose a solution involving DropPath, a modified residual shortcut connection, knowledge distillation, periodic learning rate scheduling, a stronger optimizer (Lion), and enhanced data augmentation. Experiments demonstrate the effectiveness of these methods in mitigating architecture overfitting.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive, covering various settings and ablation studies to validate the proposed methods.

### Weaknesses

#### Some Related Works

[1] Dataset Distillation with Activation Matching
[2] Dataset Distillation with Adversarial Examples
[3] Dataset Distillation via the Wasserstein Metric
[4] Dataset Distillation with a Universal Feature Extractor

#### comment

1. The proposed methods lack novelty. The use of DropPath in dataset distillation was first introduced by FRePo [R1], and the authors should acknowledge this. The other methods, such as a modified residual shortcut connection, knowledge distillation, periodic learning rate scheduling, stronger optimizers, and enhanced data augmentation, are also not novel and have been explored in previous works [R2, R3, R4]. The combination of these existing techniques does not constitute a significant contribution.

2. The experiments are insufficient. The authors should include additional comparisons with other dataset distillation methods, such as [R3, R4], to provide a more comprehensive evaluation of their approach. Furthermore, the experiments should be conducted on more complex datasets, such as ImageNet, to assess the scalability and effectiveness of the proposed methods in more challenging scenarios.

3. The paper lacks an analysis of the computational cost of the proposed methods. It is important to understand the trade-offs between performance gains and computational overhead, especially when considering the practical applicability of the approach.

### Suggestions

The authors should more clearly delineate the specific novel contributions of their work beyond the combination of existing techniques. While the paper identifies architecture overfitting as a key issue in dataset distillation, the proposed solutions, such as DropPath and modified residual connections, are not entirely novel in isolation. A more detailed analysis of how these methods interact and uniquely address the overfitting problem is needed. For example, the authors could investigate the specific mechanisms through which DropPath mitigates overfitting in the context of dataset distillation, rather than simply stating that it is a known technique. Similarly, the modified residual shortcut connection should be analyzed in terms of its impact on feature propagation and generalization, rather than just being presented as a design choice. The authors should also provide a more thorough comparison with existing methods, including a detailed analysis of the differences in their approaches and the specific advantages of the proposed methods. This would help to establish the novelty and significance of their work more clearly.

To strengthen the experimental evaluation, the authors should include a more comprehensive set of comparisons with other state-of-the-art dataset distillation methods. This should include a wider range of techniques, such as those based on adversarial training, optimal transport, and universal feature extractors. Furthermore, the experiments should be conducted on more complex datasets, such as ImageNet, to assess the scalability and effectiveness of the proposed methods in more challenging scenarios. The authors should also provide a more detailed analysis of the performance of their methods across different architectures and datasets, including a discussion of the limitations and potential failure cases. This would help to provide a more complete picture of the strengths and weaknesses of their approach. Additionally, the authors should include a more detailed analysis of the computational cost of their methods, including a comparison with other dataset distillation techniques. This would help to assess the practical applicability of their approach in real-world scenarios.

Finally, the authors should provide a more detailed analysis of the impact of each proposed method on the performance of the distilled dataset. This should include a breakdown of the performance gains attributable to each technique, as well as an analysis of the interactions between them. For example, the authors could investigate the impact of DropPath on the feature representations learned by the distilled dataset, and how this affects the performance of different architectures. Similarly, they could analyze the effect of the modified residual shortcut connection on the stability and convergence of the training process. This would provide a more fine-grained understanding of the mechanisms through which their methods address architecture overfitting, and would help to identify potential areas for further improvement. The authors should also consider releasing their code to facilitate reproducibility and further research in this area.

### Questions

See the weaknesses above.

### Rating

3

### Confidence

5

**********
