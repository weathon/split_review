### Summary

This paper investigates the overfitting problem in conditional diffusion sampling. The authors first show that the overfitting problem is caused by model-fitting, and then propose a method to alleviate the overfitting problem by compressing the guidance steps. The proposed method is evaluated on both unconditional and conditional diffusion models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective.
3. The proposed method is evaluated on both unconditional and conditional diffusion models.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the proposed method. For example, the authors should provide the time cost of the proposed method. Specifically, it would be beneficial to understand how the compression of guidance steps impacts the overall runtime of the sampling process, and whether this compression introduces any additional overhead. A detailed breakdown of the computational cost associated with each step of the proposed method, compared to the standard sampling process, would be valuable.
2. The authors should provide more details about the experimental settings. For example, the authors should provide the number of training steps for the proposed method. It is important to know if the proposed method requires a different number of training steps compared to standard diffusion models, and if so, how this affects the overall training time and performance. The authors should also clarify whether the proposed method is applied during the training phase or only during the sampling phase, or both.
3. The authors should provide more details about the experimental results. For example, the authors should provide the results on the ImageNet dataset. The current results are not sufficient to demonstrate the effectiveness of the proposed method on a large-scale dataset. It is important to see how the proposed method performs on a more challenging dataset like ImageNet, and whether the benefits observed on smaller datasets generalize to larger and more complex datasets. The authors should also provide a more detailed analysis of the results, including quantitative metrics and visualizations.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the proposed compression method. The authors should provide a detailed breakdown of the time cost associated with each step of the proposed method, compared to the standard sampling process. This should include the time taken for guidance calculation, gradient updates, and any other relevant operations. It would also be helpful to analyze how the compression ratio affects the overall runtime, and whether there is a trade-off between computational efficiency and image quality. Furthermore, the authors should investigate the impact of the proposed method on different hardware platforms, such as GPUs with varying memory capacities, to understand its practical applicability. This analysis should also consider the potential for parallelization of the proposed method to further reduce the computational cost.

To strengthen the experimental evaluation, the authors should provide more details about the experimental settings, including the number of training steps, the specific hyperparameters used, and the training procedure. It is important to know if the proposed method requires a different number of training steps compared to standard diffusion models, and if so, how this affects the overall training time and performance. The authors should also clarify whether the proposed method is applied during the training phase, only during the sampling phase, or both. If the method is applied during training, the authors should provide details about how the guidance is incorporated into the training process. Additionally, the authors should provide a more detailed analysis of the experimental results, including quantitative metrics and visualizations. It would be beneficial to see a comparison of the proposed method with other existing methods for conditional diffusion models, to demonstrate its advantages and limitations. The authors should also provide a more detailed analysis of the results, including a discussion of the limitations of the proposed method and potential directions for future research.

Finally, the authors should provide more results on the ImageNet dataset to demonstrate the effectiveness of the proposed method on a large-scale dataset. The current results are not sufficient to demonstrate the effectiveness of the proposed method on a large-scale dataset. It is important to see how the proposed method performs on a more challenging dataset like ImageNet, and whether the benefits observed on smaller datasets generalize to larger and more complex datasets. The authors should also provide a more detailed analysis of the results, including quantitative metrics and visualizations. It would be beneficial to see a comparison of the proposed method with other existing methods for conditional diffusion models, to demonstrate its advantages and limitations. The authors should also provide a more detailed analysis of the results, including a discussion of the limitations of the proposed method and potential directions for future research.

### Questions

1. What is the time cost of the proposed method?
2. What is the number of training steps for the proposed method?
3. What is the experimental results on the ImageNet dataset?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
