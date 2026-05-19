### Summary

The paper introduces a novel approach to continual learning called Prompt Gradient Projection (PGP). The proposed method combines prompt-tuning with gradient projection to mitigate catastrophic forgetting. The authors claim that PGP provides a theoretical guarantee against forgetting and achieves a balance between stability and plasticity. The paper presents experimental results on multiple benchmark datasets, demonstrating the effectiveness of the proposed approach compared to existing continual learning methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a novel combination of prompt-tuning and gradient projection for continual learning.
2. The authors provide a theoretical analysis of the proposed method and claim a guarantee against forgetting.
3. The paper presents extensive experimental results on multiple benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for why combining prompt-tuning and gradient projection is beneficial for continual learning. The authors do not provide a strong theoretical justification for the proposed approach, and the connection between the two techniques is not well-explained. Specifically, it's unclear why the gradient projection method, which is typically used to stabilize training, would be beneficial in the context of prompt tuning, and how this interaction leads to improved continual learning performance. The paper needs to elaborate on the specific mechanisms by which the gradient projection helps the prompt tuning process to avoid catastrophic forgetting.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors should compare the training time and memory usage of PGP with other continual learning methods. The analysis should include a breakdown of the computational overhead introduced by the gradient projection step, and how this overhead scales with the number of tasks and the size of the model. It is important to understand if the added complexity of PGP is justified by the performance gains.
3. The experimental results are not thoroughly analyzed. The authors should provide a more detailed discussion of the results, including the limitations of the proposed method. The analysis should go beyond simply reporting the performance numbers and should delve into the reasons behind the observed results. For example, it would be useful to analyze the forgetting behavior on a per-task basis and to investigate the sensitivity of the method to different hyperparameter settings. The paper should also discuss the cases where the method performs poorly and provide potential explanations for these failures.

### Suggestions

The paper should provide a more detailed explanation of the theoretical underpinnings of the proposed Prompt Gradient Projection (PGP) method. Specifically, the authors should elaborate on why the gradient projection is beneficial in the context of prompt tuning for continual learning. A more rigorous analysis of how the gradient projection helps to maintain the stability of the learned representations across different tasks is needed. This could involve a mathematical analysis of the gradient projection operation and its effect on the optimization landscape. Furthermore, the authors should provide a clear explanation of how the proposed method addresses the catastrophic forgetting problem, and how it differs from existing approaches. The paper should also include a discussion of the limitations of the proposed method and the scenarios where it might not perform well. This would provide a more balanced and comprehensive evaluation of the proposed approach.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the computational cost of the PGP method. This should include the time and memory requirements for both training and inference. The analysis should compare the computational cost of PGP with other continual learning methods, including both prompt-based and gradient-based approaches. The authors should also analyze how the computational cost of PGP scales with the number of tasks, the size of the model, and the size of the input data. This analysis should be presented in a clear and concise manner, with appropriate tables and figures. Furthermore, the authors should discuss the practical implications of the computational cost of PGP, and whether the performance gains justify the added computational overhead. It would be beneficial to explore potential optimizations to reduce the computational cost of the method.

The experimental section should be significantly enhanced with a more thorough analysis of the results. The authors should provide a detailed discussion of the performance of PGP on each task, including an analysis of the forgetting behavior. This analysis should go beyond simply reporting the overall accuracy and should delve into the reasons behind the observed performance. For example, the authors could analyze the forgetting behavior on a per-task basis, and investigate the sensitivity of the method to different hyperparameter settings. The paper should also discuss the cases where the method performs poorly and provide potential explanations for these failures. It would be useful to include ablation studies to evaluate the contribution of different components of the proposed method. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach.

### Questions

1. How does the proposed method handle the trade-off between plasticity and stability in continual learning?
2. What are the computational costs associated with the proposed method compared to other continual learning approaches?
3. How does the proposed method perform on more complex and realistic continual learning scenarios?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
