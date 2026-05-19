### Summary

This paper addresses the architecture overfitting problem in dataset distillation, where models trained on distilled datasets perform poorly when tested with different network architectures. The authors propose a series of approaches in both architecture designs and training schemes which can be adopted together to mitigate this issue. The proposed methods are efficient, generic, and can improve the performance when training on a limited real data. The authors conduct extensive experiments to demonstrate the effectiveness and generality of their methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive, covering various settings and ablation studies to validate the proposed methods.
3. The proposed methods are efficient and generic, and can improve the performance when training on a small real dataset directly.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed methods lack novelty. The use of DropPath in dataset distillation was first introduced by FRePo [R1], and the authors should acknowledge this. The other methods, such as a modified residual shortcut connection, knowledge distillation, periodic learning rate scheduling, stronger optimizers, and enhanced data augmentation, are also not novel and have been explored in previous works [R2, R3, R4]. The combination of these existing techniques does not constitute a significant contribution.
2. The experiments are insufficient. The authors should include additional comparisons with other dataset distillation methods, such as [R3, R4], to provide a more comprehensive evaluation of their approach. Furthermore, the experiments should be conducted on more complex datasets, such as ImageNet, to assess the scalability and effectiveness of the proposed methods in more challenging scenarios.
3. The paper lacks an analysis of the computational cost of the proposed methods. It is important to understand the trade-offs between performance gains and computational overhead, especially when considering the practical applicability of the approach.

### Suggestions

The authors should more clearly delineate the specific novel contributions of their work beyond the combination of existing techniques. While the paper identifies architecture overfitting as a key issue in dataset distillation, the proposed solutions, such as DropPath and modified residual connections, are not entirely novel in isolation. A more detailed analysis of how these methods interact and uniquely address the overfitting problem is needed. For example, the authors could investigate the specific mechanisms through which DropPath mitigates overfitting in the context of dataset distillation, rather than simply stating that it is a known technique. Similarly, the modified residual shortcut connection should be analyzed in terms of its impact on feature propagation and generalization, rather than just being presented as a design choice. The authors should also provide a more thorough comparison with existing methods, including a detailed analysis of the differences in their approaches and the specific advantages of the proposed methods. This would help to establish the novelty and significance of their work more clearly.

To strengthen the experimental evaluation, the authors should include a more comprehensive set of comparisons with other state-of-the-art dataset distillation methods. This should include a wider range of techniques, such as those based on adversarial training, optimal transport, and universal feature extractors. Furthermore, the experiments should be conducted on more complex datasets, such as ImageNet, to assess the scalability and effectiveness of the proposed methods in more challenging scenarios. The authors should also provide a detailed analysis of the performance of their methods across different architectures and datasets, including a discussion of the limitations and potential failure cases. Additionally, the authors should include a more detailed analysis of the computational cost of their methods, including a comparison with other dataset distillation techniques. This analysis should include a breakdown of the time and memory requirements of each step of their method, and should also discuss the scalability of their approach to larger datasets and more complex models. This would provide a more complete picture of the practical applicability of the proposed methods.

Finally, the authors should provide a more detailed explanation of the specific implementation details of their method. This should include a description of the specific hyperparameters used, and a discussion of how these hyperparameters were chosen. The authors should also provide a more detailed explanation of the training procedure, including the specific optimization algorithms and learning rate schedules used. This level of detail would allow other researchers to reproduce their results and build upon their work. The authors should also consider releasing their code to the community, which would further enhance the reproducibility and impact of their work.

### Questions

See Weaknesses

### Rating

6

### Confidence

4

**********
