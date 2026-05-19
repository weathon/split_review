### Summary

This paper studies the problem of out-of-distribution (OOD) generalization and detection. The authors propose a graph-based framework that can be optimized with contrastive learning. Theoretical analysis shows that minimizing the loss is equivalent to performing spectral decomposition on the graph. The authors also provide empirical results on CIFAR-10 and other datasets to demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for the problem and a detailed explanation of the proposed method.

2. The theoretical analysis is interesting and provides insights into the behavior of the proposed method.

3. The empirical results show that the proposed method outperforms existing baselines on several datasets.

### Weaknesses

#### Some Related Works

[1] Out-of-distribution generalization via risk extrapolation.

#### comment

1. The authors claim that the proposed method can be optimized with stochastic gradient descent (SGD). However, the proposed loss function is non-convex, and the authors do not provide any theoretical analysis on the convergence of SGD for this loss function. Specifically, the contrastive loss, while often used in practice, does not guarantee a globally optimal solution when optimized with SGD. The paper lacks a discussion on the potential for local minima and how the proposed method avoids them, or if the authors are relying on empirical observations rather than theoretical guarantees.

2. The authors only compare their method with SCONE. However, there are many other methods for OOD generalization and detection, such as [1]. The lack of comparison with a broader range of baselines makes it difficult to assess the true novelty and effectiveness of the proposed method. It is important to compare against methods that use different approaches, such as domain adaptation techniques or methods that explicitly model the OOD data distribution.

3. The authors do not provide a detailed analysis of the computational complexity of the proposed method. The graph-based approach may be computationally expensive, especially for large datasets. The paper should include a discussion of the time and space complexity of the proposed method, and how it scales with the size of the dataset and the number of nodes in the graph. This is crucial for understanding the practical applicability of the method.

### Suggestions

The paper would benefit from a more thorough analysis of the optimization process. While the authors claim that SGD can be used to optimize the proposed loss function, they do not provide any theoretical justification for this claim. It would be helpful to include an analysis of the loss landscape and discuss the potential for local minima. Furthermore, the authors should provide empirical evidence to support their claim that SGD converges to a good solution. This could include plots of the loss function over training iterations, or an analysis of the sensitivity of the results to different learning rates and initialization strategies. Without such analysis, it is difficult to assess the robustness of the proposed method.

To strengthen the empirical evaluation, the authors should include comparisons with a wider range of baselines. Specifically, methods that explicitly model the OOD data distribution, such as those based on generative models, should be included. Additionally, domain adaptation techniques that aim to learn domain-invariant representations could provide a useful comparison point. The authors should also consider comparing their method with techniques that use different approaches to OOD generalization, such as methods that focus on uncertainty estimation. This would provide a more comprehensive assessment of the proposed method's performance and its advantages over existing approaches. The evaluation should also include a more detailed analysis of the performance of the method under different levels of OOD shift, and on datasets with different characteristics.

Finally, the paper should include a more detailed analysis of the computational complexity of the proposed method. The authors should provide a theoretical analysis of the time and space complexity of the method, and discuss how it scales with the size of the dataset and the number of nodes in the graph. This analysis should also include a discussion of the memory requirements of the method, and how it can be optimized for large datasets. Furthermore, the authors should provide empirical results on the runtime of the method on different datasets, and compare it with the runtime of the baseline methods. This would provide a more complete picture of the practical applicability of the proposed method.

### Questions

1. What is the computational complexity of the proposed method?

2. How does the proposed method compare with other methods for OOD generalization and detection, such as [1]?

3. What is the effect of the hyperparameters on the performance of the proposed method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
