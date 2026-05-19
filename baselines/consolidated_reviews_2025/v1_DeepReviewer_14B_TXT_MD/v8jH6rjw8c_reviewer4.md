### Summary

This paper focuses on the problem of learning from noisily labeled long-tailed data. The authors first observe that existing methods fail to consistently improve the learning when the dataset is long-tailed with label noise. The authors then propose a fairness regularizer to improve the performances of sub-populations on the tail and the overall learning performance. Extensive experiments demonstrate the effectiveness of the proposed solution when complemented with certain existing popular robust or class-balanced methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experimental results are sufficient.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation of the proposed method is not clear. It is unclear why the fairness regularizer can help with learning from noisily labeled long-tailed data.
2. The novelty of the proposed method is limited.
3. The experimental results are not very convincing. The authors only provide the overall test accuracy, which does not show the performance of the tail classes.

### Suggestions

The paper introduces a fairness regularizer to address the challenge of learning from noisily labeled long-tailed data. While the idea is interesting, the paper would benefit from a more detailed explanation of the underlying mechanisms. Specifically, the connection between fairness and robustness to noisy labels in long-tailed distributions needs further clarification. The authors should elaborate on why enforcing fairness across sub-populations, as defined by their method, would inherently lead to better generalization on the tail classes, especially when the labels are noisy. A more rigorous theoretical analysis or a more detailed empirical study could help to justify this connection. For example, the authors could explore how the fairness regularizer affects the gradient updates for different sub-populations, and how this impacts the model's ability to learn from noisy labels. Furthermore, it would be beneficial to provide some empirical evidence to support the claim that the fairness regularizer helps with learning from noisily labeled long-tailed data. This could involve experiments with varying levels of label noise and different long-tail distributions, and analyzing how the proposed method performs under these conditions.

To strengthen the novelty of the proposed method, the authors should clearly articulate the specific challenges in applying fairness techniques to long-tailed learning and how their approach overcomes these challenges. It is important to highlight the unique aspects of their method compared to existing approaches that combine fairness and long-tailed learning. The authors should also discuss the limitations of their approach and potential avenues for future research. For example, the authors could discuss the computational cost of the fairness regularizer and whether it scales well to large datasets. Additionally, it would be beneficial to compare the proposed method with other state-of-the-art methods for learning from noisily labeled long-tailed data, including those that do not explicitly use fairness regularization. This would help to demonstrate the advantages and disadvantages of the proposed method compared to existing techniques.

Finally, the experimental results need to be more comprehensive. The authors should provide per-class performance metrics, especially for the tail classes, to demonstrate the effectiveness of their method. It is crucial to show that the proposed method improves the performance of the tail classes, which are most affected by both long-tail distributions and label noise. The authors should also provide a more detailed analysis of the experimental results, including error analysis and ablation studies to understand the contribution of different components of their method. For example, they could analyze how the performance of the method changes with different values of the fairness regularization parameter. Furthermore, the authors should consider using more challenging datasets and evaluation metrics to further validate their approach. The current evaluation only provides overall test accuracy, which is not sufficient to demonstrate the effectiveness of the proposed method on long-tailed distributions.

### Questions

1. Why the fairness regularizer can help with learning from noisily labeled long-tailed data? The authors should provide some theoretical or empirical evidence to support this claim.
2. What is the novelty of the proposed method? The authors should clearly articulate the specific challenges in applying fairness techniques to long-tailed learning and how their approach overcomes these challenges.
3. The authors should provide the performance of the tail classes to demonstrate the effectiveness of the proposed method.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
