### Summary

This paper addresses the architecture overfitting problem in dataset distillation, where models trained on distilled datasets perform poorly when tested with different network architectures. The authors propose several methods to mitigate this issue, including DropPath, modified residual connections, knowledge distillation, periodic learning rate scheduling, and stronger data augmentation. These methods collectively improve the generalization performance of distilled datasets across various network architectures.

### Soundness

3

### Presentation

3

### Contribution

2

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

The paper would benefit significantly from a more thorough analysis of the novelty of the proposed methods. While the authors combine several existing techniques, they need to clearly articulate the specific contributions and how their combination leads to a novel approach. For example, the authors should provide a detailed comparison of their modified residual shortcut connection with existing methods, highlighting the specific differences and advantages. Similarly, the knowledge distillation approach should be compared with other distillation techniques, demonstrating the unique aspects of their method. The authors should also provide a more detailed explanation of why the specific combination of these methods is effective in mitigating architecture overfitting in dataset distillation, rather than simply stating that it works. A more rigorous analysis of the individual contributions of each method, and their interactions, would significantly strengthen the paper.

To address the insufficient experiments, the authors should include a more comprehensive evaluation of their method. This should include comparisons with a wider range of state-of-the-art dataset distillation techniques, such as those mentioned in the weaknesses, and should also include experiments on more complex datasets like ImageNet. The authors should also provide a detailed analysis of the performance of their method across different network architectures and datasets, including a discussion of the limitations and potential failure cases. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method, including a comparison with other dataset distillation techniques. This analysis should include a breakdown of the time and memory requirements of each step of their method, and should also discuss the scalability of their approach to larger datasets and more complex models. This would provide a more complete picture of the practical applicability of the proposed methods.

Finally, the authors should provide a more detailed explanation of the specific implementation details of their method. This should include a description of the specific hyperparameters used, and a discussion of how these hyperparameters were chosen. The authors should also provide a more detailed explanation of the training procedure, including the specific optimization algorithms and learning rate schedules used. This level of detail would allow other researchers to reproduce their results and build upon their work. The authors should also consider releasing their code to the community, which would further enhance the reproducibility and impact of their work.

### Questions

1. How does the proposed method compare to other dataset distillation methods in terms of performance and computational cost?
2. How does the proposed method perform on more complex datasets, such as ImageNet?
3. What is the computational cost of the proposed method, and how does it compare to other dataset distillation techniques?

### Rating

5

### Confidence

4

**********
