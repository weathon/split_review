### Summary

This paper proposes a new method for continual learning called Prompt Gradient Projection (PGP). PGP combines prompt tuning with gradient projection to mitigate catastrophic forgetting. The authors provide a theoretical analysis of the proposed method and demonstrate its effectiveness on several benchmark datasets. The paper also discusses the relationship between PGP and existing methods, highlighting its advantages in terms of stability and plasticity.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its theoretical foundations.
2. The paper provides a comprehensive comparison of PGP with existing methods, highlighting its advantages in terms of stability and plasticity.
3. The paper demonstrates the effectiveness of PGP on several benchmark datasets, showing its potential for practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of PGP. It would be helpful to understand how the computational cost of PGP compares to other continual learning methods.
2. The paper does not discuss the limitations of PGP. It would be helpful to understand the scenarios where PGP may not perform well.
3. The paper does not provide a detailed analysis of the sensitivity of PGP to hyperparameters. It would be helpful to understand how the performance of PGP is affected by different hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by Prompt Gradient Projection (PGP). While the method combines prompt tuning with gradient projection, the practical implications of this combination in terms of computational cost need to be explored. Specifically, the authors should provide a breakdown of the computational cost associated with each component of PGP, such as the prompt tuning process and the gradient projection step. This analysis should include a comparison with existing continual learning methods, highlighting the trade-offs between performance and computational resources. For example, the authors could analyze the time and memory requirements of PGP during both training and inference phases, and compare these with methods like Elastic Weight Consolidation (EWC) or other gradient-based approaches. Furthermore, it would be beneficial to discuss the scalability of PGP with respect to the number of tasks and the size of the model, as this is a crucial factor for practical applications in continual learning scenarios. This analysis should be supported by empirical results, demonstrating the computational efficiency of PGP under various conditions.

In addition to the computational cost, the paper should also address the limitations of PGP. While the method shows promising results on the benchmark datasets, it is important to understand the scenarios where PGP may not perform optimally. For instance, the authors should investigate the performance of PGP on tasks with highly dissimilar data distributions or when the task boundaries are not clearly defined. It would be helpful to analyze the sensitivity of PGP to the choice of prompts and the initialization of the gradient projection parameters. Furthermore, the authors should discuss the potential for catastrophic forgetting in scenarios where the tasks are very similar, and how PGP addresses this issue. A more detailed analysis of the failure cases of PGP would provide a more comprehensive understanding of its applicability and limitations. This analysis should include a discussion of the potential for bias in the prompt selection process and how this might affect the performance of PGP across different tasks.

Finally, a more detailed analysis of the sensitivity of PGP to hyperparameters is needed. The authors should provide a systematic study of how different hyperparameter settings affect the performance of PGP. This analysis should include a discussion of the impact of the learning rate, the projection parameter, and other relevant hyperparameters on the stability and plasticity of the model. The authors should also provide guidelines for selecting appropriate hyperparameter values for different tasks and datasets. This analysis should be supported by empirical results, demonstrating the robustness of PGP to different hyperparameter settings. Furthermore, the authors should discuss the potential for overfitting or underfitting when using PGP, and how to mitigate these issues. This analysis should include a discussion of the potential for the gradient projection step to interfere with the learning of new tasks, and how to prevent this from happening. A thorough analysis of the hyperparameter sensitivity would greatly enhance the practical applicability of PGP.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
