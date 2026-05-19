### Summary

This paper addresses the issue of model collapse in deep canonical correlation analysis (DCCA) and proposes a novel noise regularization approach to prevent it. The authors demonstrate that the model collapse issue in DCCA is due to the low-rank nature of the DNN weight matrices. They introduce the Correlation Invariant Property (CIP) and show that enforcing it can prevent model collapse. The proposed NR-DCCA method is evaluated on both synthetic and real-world datasets, showing consistent outperformance and stability compared to existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed NR-DCCA method is simple yet effective in preventing model collapse in DCCA.
3. The authors provide a theoretical analysis of the Correlation Invariant Property (CIP) and its connection to the full-rank property of weight matrices.
4. The paper includes comprehensive experiments on both synthetic and real-world datasets, demonstrating the effectiveness and robustness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method. For example, how does the performance of NR-DCCA vary with different choices of noise distribution or the number of views? Specifically, the paper does not explore the sensitivity of the method to the variance of the added noise, which could significantly impact the regularization effect. Furthermore, the impact of the number of views on the performance of NR-DCCA is not thoroughly investigated. It is unclear if the method's effectiveness is maintained with a large number of views or if it degrades as the number of views increases beyond a certain point.
2. The paper does not provide a comparison of the computational cost of NR-DCCA with other DCCA-based methods. It is important to understand the trade-offs between performance and computational efficiency, especially when dealing with large-scale datasets. The paper should include a detailed analysis of the time and memory complexity of the proposed method, as well as a comparison with existing DCCA methods.
3. The paper does not provide a detailed analysis of the convergence properties of the proposed method. While the authors mention that the method is stable, a more rigorous analysis of the convergence behavior is needed. This should include an analysis of the convergence rate and the conditions under which the method is guaranteed to converge to a stable solution.

### Suggestions

The paper should include a more comprehensive analysis of the limitations of the proposed NR-DCCA method. Specifically, the authors should investigate the sensitivity of the method to the variance of the added noise. This could be done by conducting experiments with different noise levels and analyzing the impact on the performance of the method. Furthermore, the paper should explore the impact of the number of views on the performance of NR-DCCA. It is important to determine if the method's effectiveness is maintained with a large number of views or if it degrades as the number of views increases. This analysis should include experiments with different numbers of views and a discussion of the results. The authors should also discuss the potential limitations of the method in scenarios where the noise distribution is not Gaussian or when the data is highly non-linear.

To address the lack of computational cost analysis, the authors should provide a detailed analysis of the time and memory complexity of the proposed method. This analysis should include a comparison with existing DCCA methods. The authors should also discuss the practical implications of the computational cost of the method, especially when dealing with large-scale datasets. This could include a discussion of the scalability of the method and the potential for parallelization. The paper should also include a discussion of the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate method for a given application.

Finally, the paper should include a more detailed analysis of the convergence properties of the proposed method. This analysis should include an analysis of the convergence rate and the conditions under which the method is guaranteed to converge to a stable solution. The authors should also discuss the potential for oscillations or divergence during training and provide strategies for mitigating these issues. This analysis should be supported by theoretical results and empirical evidence. The paper should also discuss the potential limitations of the method in scenarios where the convergence is slow or difficult to achieve.

### Questions

1. How does the performance of NR-DCCA vary with different choices of noise distribution or the number of views?
2. What is the computational cost of NR-DCCA compared to other DCCA-based methods?
3. What are the convergence properties of the proposed method?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
