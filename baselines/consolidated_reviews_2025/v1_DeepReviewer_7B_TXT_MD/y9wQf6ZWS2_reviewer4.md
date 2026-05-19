### Summary

The paper proposes a new Q-learning algorithm with linear function approximation. The proposed algorithm is shown to converge under linear function approximation, and its convergence is proved using the switching system framework. The paper also provides an error bound for the solution of the projected Bellman equation. Experimental results show that the proposed algorithm outperforms other algorithms in terms of convergence speed.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important problem in reinforcement learning, namely the divergence issue of Q-learning with linear function approximation.
2. The proposed algorithm is simple and easy to implement.
3. The paper provides a theoretical analysis of the convergence of the proposed algorithm.
4. The paper provides an error bound for the solution of the projected Bellman equation.
5. The experimental results show that the proposed algorithm outperforms other algorithms in terms of convergence speed.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of why the proposed regularization term is effective in addressing the divergence issue of Q-learning with linear function approximation. Specifically, it is unclear how the regularization term interacts with the linear function approximation to ensure convergence, and what specific properties of the regularization term are crucial for this behavior. A more detailed explanation of the mechanism behind the regularization's effectiveness is needed.
2. The paper does not provide a comparison with other state-of-the-art algorithms for Q-learning with linear function approximation. The experimental results only compare the proposed algorithm with two baselines, which are not strong enough to demonstrate the effectiveness of the proposed algorithm. A more comprehensive comparison with other relevant algorithms is needed to establish the superiority of the proposed approach. The lack of comparison with algorithms that also use regularization techniques makes it difficult to assess the novelty and contribution of the proposed method.
3. The paper does not provide a discussion of the limitations of the proposed algorithm. It is important to understand the scenarios where the proposed algorithm might not perform well, and what are the potential issues that might arise in practice. For example, the paper does not discuss the sensitivity of the algorithm to the choice of hyperparameters, or the potential for instability in certain environments.

### Suggestions

The paper should provide a more detailed explanation of the regularization term and its interaction with the linear function approximation. Specifically, the authors should explain how the regularization term addresses the divergence issue, and what specific properties of the regularization term are crucial for this behavior. A more rigorous analysis of the regularization term's effect on the convergence of the algorithm is needed. For example, the authors could analyze the effect of the regularization term on the eigenvalues of the system matrix, or provide a theoretical justification for why the regularization term leads to a stable solution. This analysis should be included in the main body of the paper, not just in the appendix.

To strengthen the experimental evaluation, the paper should include a comparison with a wider range of state-of-the-art algorithms for Q-learning with linear function approximation. This should include algorithms that also use regularization techniques, as well as algorithms that do not. The comparison should be done on a variety of environments, and the results should be analyzed in detail. The authors should also provide a discussion of the computational cost of the proposed algorithm, and compare it to the computational cost of the other algorithms. This would help to establish the practical applicability of the proposed approach. Furthermore, the authors should consider using more challenging environments to test the robustness of the proposed algorithm.

Finally, the paper should include a discussion of the limitations of the proposed algorithm. This should include a discussion of the scenarios where the algorithm might not perform well, and what are the potential issues that might arise in practice. For example, the authors should discuss the sensitivity of the algorithm to the choice of hyperparameters, and the potential for instability in certain environments. The authors should also discuss the limitations of the theoretical analysis, and what are the assumptions that are made in the analysis. This would help to provide a more complete picture of the proposed algorithm and its limitations.

### Questions

1. Can the authors provide a more detailed explanation of why the proposed regularization term is effective in addressing the divergence issue of Q-learning with linear function approximation?
2. Can the authors provide a comparison with other state-of-the-art algorithms for Q-learning with linear function approximation?
3. Can the authors provide a discussion of the limitations of the proposed algorithm?

### Rating

6

### Confidence

3

**********
