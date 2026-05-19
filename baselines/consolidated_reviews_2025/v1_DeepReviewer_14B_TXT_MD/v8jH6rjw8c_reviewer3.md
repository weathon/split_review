### Summary

This paper studies the problem of learning from long-tailed and noisily labeled data. The authors first show that existing methods fail to consistently improve the learning when the dataset is long-tailed with label noise. The authors then propose a fairness regularizer to improve the performances of sub-populations on the tail and the overall learning performance. Extensive experiments demonstrate the effectiveness of the proposed solution when complemented with certain existing popular robust or class-balanced methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experimental results are sufficient.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation of the proposed method is not clear. It is unclear why the fairness regularizer can help with learning from noisily labeled long-tailed data. Specifically, the connection between enforcing fairness across sub-populations and mitigating the effects of label noise in long-tailed distributions is not well-established. The paper does not provide a clear theoretical justification or empirical evidence to support this claim. It's not immediately obvious why reducing performance disparities between head and tail classes would inherently lead to better robustness against label noise.
2. The novelty of the proposed method is limited. The fairness regularizer seems to be a straightforward application of existing fairness techniques to the long-tailed learning problem. The paper does not introduce any novel algorithmic components or theoretical insights that significantly advance the state-of-the-art in either fairness or long-tailed learning. The combination of these techniques, while potentially useful, does not represent a substantial conceptual leap.
3. The experimental results are not very convincing. The authors only provide the overall test accuracy, which does not show the performance of the tail classes. It is crucial to demonstrate the method's effectiveness on the minority classes, which are most affected by both long-tail distributions and label noise. The lack of per-class performance metrics makes it difficult to assess the true impact of the proposed method on the tail classes.

### Suggestions

The paper needs to provide a more detailed explanation of why the fairness regularizer is effective for learning from noisily labeled long-tailed data. The authors should elaborate on the theoretical underpinnings of their approach, possibly by showing how the fairness constraint interacts with the loss function to mitigate the effects of label noise. A more rigorous analysis, perhaps involving a simplified theoretical model, could help clarify the mechanism through which fairness regularization improves robustness. For example, the authors could explore how the fairness regularizer affects the gradient updates for different sub-populations, and how this impacts the model's ability to learn from noisy labels. Furthermore, it would be beneficial to provide some empirical evidence to support the claim that the fairness regularizer helps with learning from noisily labeled long-tailed data. This could involve experiments with varying levels of label noise and different long-tail distributions, and analyzing how the proposed method performs under these conditions.

To address the limited novelty, the authors should clearly articulate the specific challenges in applying fairness techniques to long-tailed learning and how their approach overcomes these challenges. They should also compare their method with other existing approaches that combine fairness and long-tailed learning, highlighting the unique aspects of their work. It would be beneficial to explore whether the proposed method introduces any new hyperparameters or design choices, and how these parameters affect the performance of the model. A more detailed discussion of the limitations of the proposed method and potential avenues for future research would also strengthen the paper. For example, the authors could discuss the computational cost of the fairness regularizer and whether it scales well to large datasets.

Finally, the experimental section needs to be significantly improved. The authors should provide per-class performance metrics, especially for the tail classes, to demonstrate the effectiveness of their method. It is also important to compare the proposed method with other state-of-the-art methods for learning from noisily labeled long-tailed data. The authors should also provide a more detailed analysis of the experimental results, including error analysis and ablation studies to understand the contribution of different components of their method. For example, they could analyze how the performance of the method changes with different values of the fairness regularization parameter. The authors should also consider using more challenging datasets and evaluation metrics to further validate their approach.

### Questions

1. Why the fairness regularizer can help with learning from noisily labeled long-tailed data? The authors should provide some theoretical or empirical evidence to support this claim.
2. What is the novelty of the proposed method? The authors should clearly articulate the specific challenges in applying fairness techniques to long-tailed learning and how their approach overcomes these challenges.
3. The authors should provide the performance of the tail classes to demonstrate the effectiveness of the proposed method.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
