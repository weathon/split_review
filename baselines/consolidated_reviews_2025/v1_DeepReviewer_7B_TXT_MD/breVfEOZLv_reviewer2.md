### Summary

This paper proposes a novel knowledge distillation method called AdaptConf, which adaptively adjusts the supervision from weak models based on the discrepancy between soft labels and hard labels. The authors conduct extensive experiments on various tasks, including image classification, few-shot learning, noisy label learning, and transfer learning, demonstrating the effectiveness of the proposed method.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, achieving state-of-the-art performance on multiple tasks.
3. The authors conduct extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed AdaptConf is very similar to the existing methods, such as Decoupled Knowledge Distillation (DKD) and Self-Distillation (SD). The core idea of using a combination of soft and hard labels for knowledge distillation is not new, and the specific formulation of AdaptConf, while presented as novel, appears to be a minor variation of existing techniques. The adaptive weighting mechanism, while potentially beneficial, does not introduce a fundamentally new concept to the field.
2. The authors should compare the proposed method with more advanced knowledge distillation methods, such as FitNet, FitNets, and FitNets++. The lack of comparison with these methods makes it difficult to assess the true contribution of AdaptConf. Specifically, the paper should address how AdaptConf compares to FitNet's approach of selectively transferring knowledge based on the reliability of the teacher's predictions, and how it handles the potential for negative transfer when the teacher's soft labels are noisy or inaccurate. The absence of these comparisons leaves a significant gap in the evaluation.
3. The authors should provide more details about the experimental settings, such as the hyperparameters and the training time. The lack of specific details regarding hyperparameter tuning and training time makes it difficult to reproduce the results and assess the practical applicability of the proposed method. For example, the paper should specify the learning rate, batch size, optimizer, and the number of training epochs used for each experiment. Furthermore, the training time for each experiment should be reported to allow for a fair comparison with other methods.

### Suggestions

To strengthen the paper, the authors should first provide a more detailed analysis of the differences between AdaptConf and existing methods like Decoupled Knowledge Distillation (DKD) and Self-Distillation (SD). A more rigorous comparison should be made, highlighting the specific scenarios where AdaptConf is expected to outperform these methods, and providing a theoretical justification for these claims. The authors should also explore the limitations of AdaptConf, such as its sensitivity to the choice of hyperparameters and its performance under different levels of teacher model quality. Furthermore, the authors should provide a more in-depth analysis of the adaptive weighting mechanism, explaining how it adapts to different teacher-student architectures and datasets. This analysis should include a discussion of the potential for negative transfer and how AdaptConf mitigates this issue. 

Secondly, the authors should include a more comprehensive comparison with advanced knowledge distillation methods, such as FitNet, FitNets, and FitNets++. This comparison should not only focus on performance metrics but also on the underlying principles and mechanisms of each method. The authors should discuss how AdaptConf addresses the limitations of FitNet's selective transfer approach and how it handles the potential for negative transfer when the teacher's soft labels are noisy or inaccurate. The comparison should also include a discussion of the computational cost and training time of each method, providing a more complete picture of their practical applicability. The authors should also consider including a discussion of the potential for combining AdaptConf with other advanced knowledge distillation techniques to further improve performance.

Finally, the authors should provide a more detailed description of the experimental settings, including the specific hyperparameters used for each experiment, the training time, and the hardware used for the experiments. This information is crucial for reproducibility and for assessing the practical applicability of the proposed method. The authors should also provide a discussion of the sensitivity of the results to different hyperparameter settings, and provide guidelines for selecting appropriate hyperparameters for different tasks. The authors should also consider including ablation studies to analyze the contribution of each component of AdaptConf, providing a more thorough understanding of the method's behavior.

### Questions

1. How does the proposed method compare to other advanced knowledge distillation methods, such as FitNet, FitNets, and FitNets++?
2. What are the hyperparameters used in the experiments, and how were they selected?
3. How does the proposed method perform on larger-scale datasets, such as ImageNet-1K?

### Rating

3

### Confidence

4

**********
