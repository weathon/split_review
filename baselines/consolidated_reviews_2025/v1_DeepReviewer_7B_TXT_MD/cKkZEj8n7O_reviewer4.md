### Summary

This paper proposes a new method to improve the generalization of DNNs by jointly minimizing the conventional training loss and an analytical proxy for the generalization error. The authors provide a new bias-variance decomposition of the generalization error and derive a new training framework, GEM, which can be applied to various DNN architectures. The method is evaluated on CIFAR-100 and ImageNet datasets, demonstrating improved generalization performance compared to standard ERM.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a novel bias-variance decomposition of the generalization error, which is a valuable theoretical contribution.
2. The proposed GEM method is simple to implement and can be applied to various DNN architectures.
3. The paper is well-organized and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques. It is unclear how GEM compares to these methods in terms of performance and computational cost.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It is important to understand the trade-offs between performance gains and computational overhead.
3. The paper does not discuss the limitations of the proposed method. It is important to understand the scenarios where GEM might not be effective or might even degrade performance.
4. The paper does not provide a clear explanation of why minimizing the proposed proxy for generalization error is expected to lead to better generalization compared to other objectives that directly aim to minimize the generalization gap.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing methods for improving generalization. Specifically, the authors should benchmark their method against techniques like data augmentation strategies (e.g., random cropping, color jittering) and regularization methods (e.g., dropout, weight decay, batch normalization). A detailed analysis should not only focus on the final performance metrics but also on the computational cost and the convergence behavior of each method. For example, it would be useful to see a comparison of training time and memory usage for GEM versus these other techniques. Furthermore, the authors should investigate the sensitivity of GEM to different hyperparameter settings and compare it to the sensitivity of other methods. This would provide a more complete picture of the practical applicability of the proposed approach.

In addition to the performance comparisons, the paper needs a more detailed analysis of the computational cost of the proposed method. The authors should provide a breakdown of the computational overhead introduced by the proxy term and the joint optimization process. This analysis should include both training and inference time. It would also be beneficial to compare the computational cost of GEM with that of standard ERM and other regularization techniques. Furthermore, the authors should discuss the scalability of the method to larger datasets and more complex models. This would help to understand the practical limitations of the proposed approach and identify potential areas for improvement. The authors should also consider providing an ablation study to understand the contribution of each component of the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should identify scenarios where GEM might not be effective or might even degrade performance. For example, it would be useful to explore the performance of GEM on datasets with different characteristics or with different types of DNN architectures. The authors should also discuss the potential drawbacks of using the proposed proxy for generalization error and how these drawbacks might affect the performance of the method. Furthermore, the authors should provide a more intuitive explanation of why minimizing the proposed proxy for generalization error is expected to lead to better generalization. This explanation should be supported by theoretical arguments or empirical evidence.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques?
2. What is the computational cost of the proposed method compared to standard ERM and other regularization techniques?
3. What are the limitations of the proposed method, and under what conditions might it not be effective?
4. Why is minimizing the proposed proxy for generalization error expected to lead to better generalization compared to other objectives that directly aim to minimize the generalization gap?

### Rating

5

### Confidence

4

**********
