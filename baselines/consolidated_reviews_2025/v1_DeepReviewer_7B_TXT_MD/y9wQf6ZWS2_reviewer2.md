### Summary

The paper proposes a new Q-learning algorithm with linear function approximation, called RegQ, that converges under linear function approximation. The proposed algorithm is a simple modification of the standard Q-learning algorithm with a regularization term. The authors provide a theoretical analysis of the convergence of the proposed algorithm and an upper bound on the approximation error. The paper also presents experimental results to demonstrate the effectiveness of the proposed algorithm.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important problem in reinforcement learning, namely the divergence issue of Q-learning with linear function approximation.

2. The authors provide a theoretical analysis of the convergence of the proposed algorithm and an upper bound on the approximation error.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed algorithm is limited. The algorithm is a simple modification of the standard Q-learning algorithm with a regularization term, which has been widely used in practice. The authors do not provide a clear explanation of why this specific regularization term is effective in addressing the divergence issue of Q-learning with linear function approximation. The paper lacks a detailed analysis of how the regularization term interacts with the specific challenges of linear function approximation in Q-learning, such as the potential for instability due to the choice of feature representation and the learning rate schedule. It is not clear if the regularization term is sufficient to guarantee convergence under all possible linear function approximation settings.

2. The theoretical analysis of the proposed algorithm is not novel. The analysis follows the same approach as in previous works and does not provide any new insights. The paper does not provide a rigorous comparison of the convergence properties of the proposed algorithm with existing methods. The analysis does not consider the impact of the regularization parameter on the convergence rate and the final approximation error. The paper also does not discuss the limitations of the theoretical analysis and the assumptions made in the analysis.

3. The experimental results are not convincing. The authors only compare their algorithm with two baselines, which are not strong enough to demonstrate the effectiveness of their algorithm. The experimental results do not show a significant improvement over the baselines. The paper does not provide a detailed analysis of the experimental results, including the impact of different hyperparameter settings and the sensitivity of the algorithm to different environments. The paper also does not discuss the computational cost of the proposed algorithm and compare it with the baselines.

### Suggestions

The paper should provide a more detailed explanation of the specific challenges of Q-learning with linear function approximation that the proposed regularization term is designed to address. The authors should provide a theoretical analysis of how the regularization term interacts with the specific challenges of linear function approximation, such as the potential for instability due to the choice of feature representation and the learning rate schedule. The paper should also include a more comprehensive experimental evaluation, comparing the proposed algorithm with a wider range of state-of-the-art algorithms for Q-learning with linear function approximation. The experimental results should be analyzed in detail, including the impact of different hyperparameter settings and the sensitivity of the algorithm to different environments. The paper should also discuss the computational cost of the proposed algorithm and compare it with the baselines. Furthermore, the paper should provide a more rigorous comparison of the convergence properties of the proposed algorithm with existing methods, including a discussion of the limitations of the theoretical analysis and the assumptions made in the analysis. The paper should also discuss the impact of the regularization parameter on the convergence rate and the final approximation error. The authors should also consider providing a more intuitive explanation of the theoretical results, making them more accessible to a broader audience.

To improve the paper, the authors should consider the following: First, they should provide a more detailed explanation of the specific challenges of Q-learning with linear function approximation that the proposed regularization term is designed to address. This should include a discussion of the potential for instability due to the choice of feature representation and the learning rate schedule. Second, the authors should provide a more comprehensive experimental evaluation, comparing the proposed algorithm with a wider range of state-of-the-art algorithms for Q-learning with linear function approximation. The experimental results should be analyzed in detail, including the impact of different hyperparameter settings and the sensitivity of the algorithm to different environments. Third, the authors should provide a more rigorous comparison of the convergence properties of the proposed algorithm with existing methods, including a discussion of the limitations of the theoretical analysis and the assumptions made in the analysis. Finally, the authors should consider providing a more intuitive explanation of the theoretical results, making them more accessible to a broader audience. This could include providing a visual representation of the convergence behavior of the algorithm and a discussion of the practical implications of the theoretical results.

### Questions

1. Can the authors provide a more detailed explanation of why the proposed regularization term is effective in addressing the divergence issue of Q-learning with linear function approximation?

2. Can the authors provide a more comprehensive experimental evaluation, comparing the proposed algorithm with a wider range of state-of-the-art algorithms for Q-learning with linear function approximation?

3. Can the authors provide a more rigorous comparison of the convergence properties of the proposed algorithm with existing methods?

### Rating

3

### Confidence

4

**********
