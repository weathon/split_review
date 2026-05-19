### Summary

The paper proposes a new objective function for training neural networks that aims to improve generalization performance by jointly minimizing the empirical loss and an analytical proxy for the generalization error. The authors derive a new bias-variance decomposition of the generalization error and propose a method called GEM (Generalization Error Minimization) that leverages this decomposition to train models. The paper presents experimental results on CIFAR-100 and ImageNet datasets, demonstrating that GEM can outperform standard empirical risk minimization (ERM) in terms of generalization performance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides a new bias-variance decomposition of the generalization error, which is a valuable theoretical contribution.

2. The proposed GEM method is simple to implement and can be applied to various deep learning models.

3. The paper includes a wide range of experiments on different datasets and architectures, demonstrating the effectiveness of GEM.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for why minimizing the proposed proxy for generalization error is a good objective for training deep neural networks. It is unclear why minimizing this specific proxy is expected to lead to better generalization compared to other objectives that directly aim to minimize the generalization gap. The connection between the proposed proxy and the actual generalization error is not well-established, making it difficult to understand the theoretical justification for the method.

2. The paper does not provide a theoretical analysis of the convergence properties of the GEM method. It is not clear whether the proposed method converges to a global minimum or a local minimum, and how the convergence rate compares to standard empirical risk minimization (ERM). The lack of theoretical guarantees makes it difficult to assess the robustness and reliability of the method.

3. The paper does not provide a detailed comparison of the computational cost of GEM compared to standard ERM. It is not clear whether the additional computations required by GEM are justified by the performance gains. The paper should provide a detailed analysis of the computational overhead and its impact on the overall training time.

4. The paper does not provide a thorough analysis of the sensitivity of the GEM method to the choice of hyperparameters. It is not clear how the performance of GEM is affected by different choices of hyperparameters, and whether the method is robust to hyperparameter tuning. The paper should provide a sensitivity analysis to assess the robustness of the method.

5. The paper does not provide a detailed discussion of the limitations of the GEM method. It is not clear under which conditions the method is expected to perform well and when it might fail. The paper should provide a thorough discussion of the limitations of the method and its potential drawbacks.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical justification for the proposed GEM method. Specifically, the authors should provide a clear explanation of why minimizing the proposed proxy for generalization error is expected to lead to better generalization. This could involve a more detailed analysis of the relationship between the proxy and the actual generalization error, possibly by showing that the proxy is a tight upper bound or a lower bound on the generalization error under certain conditions. Furthermore, the authors should provide a theoretical analysis of the convergence properties of the GEM method. This analysis should include a discussion of whether the method converges to a global or local minimum, and how the convergence rate compares to standard ERM. It would be beneficial to show that the proposed method has a convergence guarantee and that it converges to a solution that minimizes the generalization error. The authors should also provide a detailed comparison of the computational cost of GEM compared to standard ERM. This analysis should include a breakdown of the computational overhead of each step in the GEM algorithm, and it should quantify the impact of the additional computations on the overall training time. It is important to understand whether the performance gains justify the additional computational cost. The paper should also include a thorough sensitivity analysis of the GEM method to the choice of hyperparameters. This analysis should explore how the performance of GEM is affected by different choices of hyperparameters, and it should identify the optimal hyperparameter settings. The authors should also discuss the limitations of the GEM method. This discussion should include a clear explanation of under which conditions the method is expected to perform well and when it might fail. It is important to understand the limitations of the method and its potential drawbacks. Finally, the authors should provide a more detailed discussion of the practical implications of the proposed method. This discussion should include a comparison of the performance of GEM with other state-of-the-art methods for improving generalization, and it should provide guidance on how to choose the appropriate hyperparameters for different datasets and architectures.

### Questions

1. What is the motivation for minimizing the proposed proxy for generalization error? How does it relate to the actual generalization error?

2. What is the theoretical analysis of the convergence properties of the GEM method?

3. How does the computational cost of GEM compare to standard ERM?

4. How sensitive is the GEM method to the choice of hyperparameters?

5. What are the limitations of the GEM method?

### Rating

3

### Confidence

3

**********
