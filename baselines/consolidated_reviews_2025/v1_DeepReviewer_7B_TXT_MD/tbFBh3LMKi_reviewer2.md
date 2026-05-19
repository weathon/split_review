### Summary

This paper proposes Uni-O4, a unified framework for offline and offline-to-online RL. The key idea is to use an ensemble of policies for offline training, and use AM-Q for offline evaluation. The experiments show that Uni-O4 outperforms the baselines in the offline setting and can be further improved with online fine-tuning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The proposed method is simple and easy to implement. The idea of using an ensemble of policies for offline training is interesting.
- The experiments show that the proposed method outperforms the baselines in the offline setting and can be further improved with online fine-tuning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not well-written. The introduction is too short and does not provide enough background information. The related work section is also too short and does not provide a comprehensive overview of the existing literature.
- The paper lacks a clear motivation for using an ensemble of policies for offline training. While the authors claim that it helps to avoid the mismatch between the estimated behavior policy and the offline dataset, they do not provide any theoretical or empirical evidence to support this claim. The paper also does not discuss the potential limitations of using an ensemble of policies, such as increased computational cost and the risk of overfitting.
- The paper does not provide a thorough analysis of the proposed method's performance. While the experiments show that Uni-O4 outperforms the baselines in the offline setting, they do not provide any insights into why this is the case. The paper also does not discuss the sensitivity of the method to different hyperparameters or the impact of different offline datasets.
- The paper does not provide a clear definition of the offline-to-online RL problem. The authors do not specify the assumptions they are making about the offline dataset or the online environment. This makes it difficult to understand the scope and limitations of the proposed method.

### Suggestions

The paper needs a more thorough introduction that provides a comprehensive overview of the offline and offline-to-online RL literature. The introduction should clearly define the problem being addressed, the challenges involved, and the limitations of existing approaches. The related work section should also be expanded to include a more comprehensive discussion of the relevant literature, including both offline and offline-to-online RL methods. This would help to contextualize the proposed method and highlight its contributions. The authors should also clearly define the offline-to-online RL problem, including the assumptions they are making about the offline dataset and the online environment. This would help to clarify the scope and limitations of the proposed method.

The motivation for using an ensemble of policies for offline training needs to be strengthened. The authors should provide a more detailed explanation of why this approach is expected to be effective in avoiding the mismatch between the estimated behavior policy and the offline dataset. They should also discuss the potential limitations of this approach, such as increased computational cost and the risk of overfitting. The authors should also provide empirical evidence to support their claims, such as experiments that compare the performance of the ensemble policy with a single policy. This would help to validate the effectiveness of the proposed approach.

The experimental section needs to be significantly improved. The authors should provide a more thorough analysis of the proposed method's performance, including experiments that investigate the sensitivity of the method to different hyperparameters and the impact of different offline datasets. They should also provide a more detailed comparison of the proposed method with existing offline and offline-to-online RL methods. The authors should also provide a more detailed explanation of the experimental setup, including the specific environments and datasets used. This would help to ensure the reproducibility of the results. The authors should also consider including ablation studies to understand the contribution of each component of the proposed method.

### Questions

- How does the proposed method compare to other offline-to-online RL methods in terms of performance and computational cost?
- What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

3

### Confidence

4

**********
