### Summary

The paper presents a novel method for multi-view representation learning (MVRL) based on deep canonical correlation analysis (DCCA), aimed at addressing the issue of model collapse. Model collapse is a phenomenon where DCCA-based methods perform well initially but their performance degrades as training progresses. The authors propose a regularization technique called NR-DCCA (Noise Regularization Deep Canonical Correlation Analysis) to mitigate this issue. The key idea is to enforce the invariance of correlation between the original data and noise, which they term the Correlation Invariant Property (CIP). The authors provide theoretical analysis to support the effectiveness of their approach. They also introduce a synthetic data generation framework to evaluate MVRL methods comprehensively. The experimental results demonstrate that NR-DCCA outperforms existing methods on both synthetic and real-world datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper addresses an important issue in MVRL, namely model collapse, which is a significant challenge for DCCA-based methods.
2. The proposed NR-DCCA method is simple yet effective, and it is shown to outperform existing methods on both synthetic and real-world datasets.
3. The paper provides a theoretical analysis to support the effectiveness of the proposed method.
4. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to understand how the computational cost scales with the size of the dataset and the number of views. Specifically, the paper lacks a breakdown of the time complexity for each step in the NR-DCCA algorithm, including the computation of correlations, the noise regularization term, and the optimization process. This makes it difficult to assess the practical applicability of the method for large-scale datasets.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, such as the regularization parameter. It is unclear how the performance of the method varies with different values of this parameter, and what are the guidelines for selecting an appropriate value. A sensitivity analysis, perhaps by plotting performance against different parameter values, would be beneficial. Furthermore, the paper should discuss the potential impact of other hyperparameters, such as learning rate and batch size, on the performance of the method.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. For example, it is unclear how the method performs when the views are highly dissimilar or when the data is noisy. The paper should discuss the potential failure modes of the method and provide guidelines for when it is appropriate to use the method.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed NR-DCCA method. The authors should provide a detailed breakdown of the time complexity for each step in the algorithm, including the computation of correlations, the noise regularization term, and the optimization process. This analysis should consider the impact of the number of views, the size of the dataset, and the dimensionality of the data on the computational cost. Furthermore, it would be helpful to compare the computational complexity of NR-DCCA with that of existing DCCA-based methods. This would allow readers to better understand the trade-offs between performance and computational cost. The authors should also discuss potential strategies for improving the computational efficiency of the method, such as using more efficient optimization algorithms or parallelizing the computations.

In addition to the computational complexity, the paper should include a more detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters. The authors should conduct a sensitivity analysis by varying the regularization parameter and other relevant hyperparameters, and plot the performance of the method against these parameters. This analysis should provide guidelines for selecting appropriate values for these parameters. The authors should also discuss the potential impact of other hyperparameters, such as learning rate and batch size, on the performance of the method. This analysis should be performed on both synthetic and real-world datasets to ensure the robustness of the findings. Furthermore, the paper should discuss the potential impact of these hyperparameters on the convergence of the method and the stability of the results.

Finally, the paper should provide a more detailed analysis of the limitations of the proposed method. The authors should discuss the potential failure modes of the method and provide guidelines for when it is appropriate to use the method. For example, the paper should discuss how the method performs when the views are highly dissimilar or when the data is noisy. The authors should also discuss the potential impact of the choice of noise distribution on the performance of the method. It would be beneficial to include experiments that specifically test the robustness of the method to different types of noise and dissimilar views. This analysis should be supported by theoretical arguments and empirical evidence.

### Questions

1. How does the computational complexity of the proposed method compare to that of existing DCCA-based methods?
2. How sensitive is the proposed method to the choice of hyperparameters, such as the regularization parameter?
3. What are the limitations of the proposed method, and when is it appropriate to use it?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
