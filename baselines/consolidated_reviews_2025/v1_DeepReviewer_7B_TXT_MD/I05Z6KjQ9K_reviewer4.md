### Summary

This paper introduces a novel gradient regularization method, GrCPA, designed to enhance the transferability of adversarial attacks in vision-language models (VLMs). By regularizing gradients in both visual and textual modalities, GrCPA effectively mitigates overfitting and improves the attack success rate across multiple prompts. Extensive experiments demonstrate GrCPA’s effectiveness in generating robust adversarial examples that transfer well across different prompts, highlighting its potential for enhancing the security of VLMs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.
2. The paper addresses a significant problem in the field of adversarial attacks on VLMs, which is the instability of adversarial examples across different prompts.
3. The proposed method is simple yet effective, and the experimental results demonstrate its superiority over existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as its computational cost and sensitivity to hyperparameters.
2. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as its computational cost and sensitivity to hyperparameters.

### Suggestions

The paper should include a more thorough analysis of the computational overhead introduced by the gradient regularization method. While the method is presented as simple, the actual computational cost, especially when applied to large vision-language models, needs to be quantified. This should include a breakdown of the time and memory requirements for both the gradient calculation and the regularization step. Furthermore, the paper should explore the sensitivity of the method to the choice of regularization parameters, such as the regularization strength and the frequency of regularization. A sensitivity analysis would help to understand the robustness of the method and provide guidance on how to choose appropriate parameter values for different scenarios. It would also be beneficial to compare the computational cost of the proposed method with existing adversarial attack methods, to provide a clear understanding of the trade-offs involved.

To improve the practical applicability of the proposed method, the paper should provide more detailed guidance on how to select the hyperparameters. The current discussion of hyperparameter selection is limited, and it is unclear how to choose the optimal values for different models and tasks. The paper should include a more systematic approach to hyperparameter tuning, such as a grid search or a Bayesian optimization method. It should also provide a discussion of the impact of different hyperparameter settings on the performance of the method, including the attack success rate and the transferability of the adversarial examples. This would help to make the method more accessible to practitioners and facilitate its adoption in real-world applications. Furthermore, the paper should discuss the potential for adaptive hyperparameter selection, where the parameters are adjusted during the attack process based on the observed performance.

Finally, the paper should explore the limitations of the proposed method in more detail, particularly in scenarios where the adversarial examples may not transfer well across different prompts. The paper should discuss the potential reasons for this lack of transferability and suggest possible solutions. For example, the paper could explore the use of more sophisticated regularization techniques or the incorporation of additional information about the target model into the attack process. It would also be beneficial to investigate the robustness of the method to different types of adversarial attacks, such as those that are designed to be more transferable. A more comprehensive analysis of the limitations of the method would help to identify areas for future research and improve the overall understanding of the problem.

### Questions

1. How does the proposed method perform on other vision-language models, such as those trained on different datasets or with different architectures?
2. How does the proposed method compare to other state-of-the-art adversarial attack methods for VLMs, in terms of performance, computational cost, and transferability?
3. What are the potential limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

4

**********
