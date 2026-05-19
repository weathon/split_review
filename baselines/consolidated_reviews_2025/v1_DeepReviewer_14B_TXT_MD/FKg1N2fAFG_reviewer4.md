### Summary

The paper addresses the problem of architecture overfitting in dataset distillation, where the distilled data is optimized for a specific architecture and performs poorly on others. The authors propose a series of methods to mitigate this issue, including a modified DropPath technique, knowledge distillation from a smaller teacher network, and a periodical learning rate scheduler. The paper demonstrates the effectiveness of these methods through extensive experiments on various datasets and network architectures.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a combination of existing techniques, and the novelty is limited.
2. The performance improvement is marginal.
3. The proposed method may not be generalizable to other dataset distillation methods.

### Suggestions

The paper's primary weakness lies in its limited novelty. While the combination of DropPath, knowledge distillation, and a periodical learning rate scheduler is effective, each component is individually well-established. The paper would benefit from a more in-depth analysis of how these specific techniques interact to mitigate architecture overfitting in the context of dataset distillation. For instance, a detailed ablation study could explore the individual contributions of each component and their synergistic effects. Furthermore, the paper should investigate the sensitivity of the proposed method to the hyperparameters of each component, such as the DropPath rate, the temperature in knowledge distillation, and the period of the learning rate scheduler. A more thorough exploration of these aspects would strengthen the paper's contribution and provide a deeper understanding of the proposed approach.

Regarding the marginal performance improvement, the paper should provide a more detailed analysis of the computational overhead introduced by the proposed method. While the performance gains are not dramatic, it is crucial to understand the trade-off between performance and computational cost. The paper should quantify the additional training time and memory requirements associated with the proposed method compared to baseline approaches. This analysis should include a breakdown of the computational cost of each component, such as the overhead of DropPath, the forward pass of the teacher network in knowledge distillation, and the learning rate scheduler. Furthermore, the paper should explore the scalability of the proposed method to larger datasets and more complex network architectures. This would provide a more comprehensive understanding of the practical applicability of the proposed approach.

Finally, the paper should address the concern about the generalizability of the proposed method to other dataset distillation techniques. The current evaluation focuses on a limited set of distillation methods, and it is unclear whether the proposed approach would be effective with other techniques, such as gradient matching or trajectory matching. The paper should include experiments with a wider range of dataset distillation methods to demonstrate the robustness of the proposed approach. Furthermore, the paper should analyze the potential limitations of the proposed method when applied to different distillation techniques. This analysis should consider the specific characteristics of each distillation method and how they might interact with the proposed approach. A more thorough investigation of these aspects would significantly enhance the paper's contribution and provide a more comprehensive understanding of the proposed method's applicability.

### Questions

Please refer to the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
