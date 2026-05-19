### Summary

This paper proposes OptBatch, a data selection method for instruction tuning of large language models (LLMs). OptBatch focuses on the learnability of whole batch data rather than individual samples, using stratified sampling and Hessian gradient optimization to enhance diversity and reduce computational costs. The method achieves robust generalization across various downstream tasks and models, reducing computational costs by 20-40% while maintaining optimal performance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. This paper proposes a novel data selection method for instruction tuning of large language models (LLMs), which focuses on the learnability of whole batch data rather than individual samples.
2. OptBatch effectively captures the intrinsic value of data curation, surpassing previous state-of-the-art methods.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The authors claim that the proposed method is different from previous methods in that it considers the learnability of whole batch data rather than individual samples. However, the concept of learnability is not clearly defined, and it is unclear how the proposed method specifically addresses this aspect. The use of Hessian gradients for data selection is also not novel, as it has been explored in prior work. The paper does not adequately highlight the unique aspects of their Hessian-based approach compared to existing methods.
2. The paper does not provide a detailed analysis of the computational overhead of the proposed method. While the authors claim that the method reduces computational costs, they do not provide a breakdown of the computational costs associated with each step of the method, such as the Hessian gradient calculation and the optimization process. This makes it difficult to assess the practical efficiency of the proposed method.
3. The paper lacks a comprehensive comparison with existing data selection methods. The authors only compare their method with a few baselines, but they do not compare it with other state-of-the-art data selection methods, such as those based on uncertainty sampling or active learning. This makes it difficult to assess the relative performance of the proposed method.

### Suggestions

The paper needs to provide a more rigorous definition of 'learnability' and clearly articulate how the proposed method's batch-level approach differs from existing sample-level methods in terms of learnability. The authors should provide a theoretical justification for their approach and explain why considering the learnability of whole batch data is more effective than considering the learnability of individual samples. They should also discuss the limitations of their approach and compare it with other methods that consider learnability at different levels. Furthermore, the authors should provide a more detailed analysis of the computational overhead of their method. They should break down the computational costs associated with each step of the method, such as the Hessian gradient calculation and the optimization process. This analysis should include a comparison with the computational costs of existing data selection methods. The authors should also provide a more comprehensive comparison with existing data selection methods. They should compare their method with other state-of-the-art methods, such as those based on uncertainty sampling or active learning. This comparison should include a detailed analysis of the performance of each method on different datasets and tasks. The authors should also discuss the limitations of their method and compare it with other methods that consider learnability at different levels.

To improve the paper, the authors should consider providing a more detailed explanation of the Hessian gradient calculation and its role in the proposed method. They should also provide a more detailed analysis of the impact of the Hessian gradient on the selection of data. The authors should also consider providing a more detailed explanation of the optimization process and its impact on the performance of the proposed method. The authors should also consider providing a more detailed analysis of the sensitivity of the proposed method to different hyperparameters. This analysis should include a discussion of the optimal values for these hyperparameters and the impact of different values on the performance of the proposed method. The authors should also consider providing a more detailed analysis of the robustness of the proposed method to different types of data and tasks. This analysis should include a discussion of the limitations of the proposed method and the conditions under which it performs well or poorly.

Finally, the authors should consider providing a more detailed explanation of the experimental setup and the evaluation metrics used in the paper. They should also provide a more detailed analysis of the results obtained in the experiments. The authors should also consider providing a more detailed discussion of the limitations of the proposed method and the directions for future research. This discussion should include a discussion of the potential applications of the proposed method and the challenges that need to be addressed to further improve its performance. The authors should also consider providing a more detailed explanation of the potential impact of the proposed method on the field of natural language processing.

### Questions

1. How does the proposed method handle the issue of noisy data in instruction tuning datasets?
2. How does the proposed method handle the trade-off between computational efficiency and model performance?

### Rating

3

### Confidence

4

**********
