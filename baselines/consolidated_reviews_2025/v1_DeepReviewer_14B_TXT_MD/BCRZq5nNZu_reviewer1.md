### Summary

This paper studies the problem of online learning, in which the dataset is split into multiple smaller chunks. The authors show that this "chunking" of the dataset alone (without any task shift) can cause a significant drop in performance due to forgetting, which is usually overlooked in continual learning. The authors also show that per-chunk weight averaging can mitigate this issue by reducing forgetting.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The paper introduces a new perspective on continual learning by studying the problem of forgetting under chunking, which has been largely ignored in the literature.
- The paper demonstrates the benefits of weight averaging in the context of continual learning, which is often overlooked in the literature.

### Weaknesses

#### Some Related Works

[1] A unified theory of stochastic approximation and stochastic optimization
[2] On the error of stochastic gradient descent

#### comment

 - The analysis of the linear case is not novel.
- The paper lacks a theoretical analysis of non-linear cases using neural networks. Specifically, the paper does not provide any justification for why per-chunk weight averaging should mitigate forgetting in non-linear models. The paper also does not explore the impact of different neural network architectures or hyperparameters on the observed chunking problem.
- The paper does not provide a comparison of the proposed weight averaging approach with other existing methods for online learning or continual learning. It is unclear how the proposed method compares to techniques like adaptive learning rates or regularization methods designed for online settings.

### Suggestions

The paper introduces an interesting perspective on the impact of data chunking on model performance, but it needs further investigation to solidify its claims. The analysis of the linear case, while insightful, relies on assumptions that may not hold in practice, such as the invertibility of covariance matrices. It would be beneficial to explore alternative approaches that do not rely on such strong assumptions, or at least provide a sensitivity analysis of the results to violations of these assumptions. Furthermore, the paper should investigate the effect of the number of chunks on the performance of the proposed method. It is not clear whether there is an optimal number of chunks or if performance degrades with too many chunks.

To strengthen the paper, the authors should provide a more detailed analysis of the non-linear case. While the empirical results suggest that weight averaging helps, a theoretical justification would be valuable. The authors could explore the use of tools from optimization theory, such as stochastic approximation, to analyze the behavior of the proposed method in non-linear settings. Specifically, it would be useful to investigate how the per-chunk weight averaging affects the convergence properties of the algorithm. Additionally, the authors should investigate the impact of different neural network architectures and hyperparameters on the observed chunking problem. It is possible that certain architectures or hyperparameter settings are more susceptible to the chunking problem than others. A thorough investigation of these factors would provide a more complete understanding of the problem and the effectiveness of the proposed solution.

Finally, the paper should include a more comprehensive comparison with existing methods for online learning and continual learning. The authors should compare their method with techniques such as adaptive learning rates, regularization methods, and replay buffers. This comparison should include both theoretical and empirical analysis. It is important to understand the strengths and weaknesses of the proposed method compared to existing approaches. For example, it would be useful to investigate whether the proposed method can be combined with other techniques to further improve performance. A more thorough comparison would help to position the proposed method within the broader context of online learning and continual learning.

### Questions

- The analysis in Section 4.2 assumes that the covariance matrix is invertible. However, this assumption may not hold in practice, especially when the number of features is large or when the data is highly correlated. How does this affect the results?
- It would be helpful to include an analysis of the non-linear case. One possible approach is to use the theory of stochastic approximation, such as the ODE method [1] or the stochastic approximation (SA) framework [2]. Specifically, how does per-chunk weight averaging affect the SA update?
- The analysis in Section 4.2 assumes a specific chunk size. How does the number of chunks affect the performance?

[1] Wei B. B. Bao and Tsinfong J. Yang. A unified theory of stochastic approximation and stochastic optimization. SIAM Journal on Mathematics of Data Science, 4(3):834–857, 2022.

[2] Yair Carmon and Tsinfong J. Yang. On the error of stochastic gradient descent. SIAM Journal on Mathematics of Data Science, 4(2):688–710, 2022.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
