### Summary

This paper studies the distributed TD-learning for a networked multi-agent Markov decision process. The proposed approach is based on distributed optimization algorithms, which can be interpreted as primal-dual Ordinary differential equation (ODE) dynamics subject to null-space constraints. Based on the exponential convergence behavior of the primal-dual ODE dynamics subject to null-space constraints, the authors examine the behavior of the final iterate in various distributed TD-learning scenarios, considering both constant and diminishing step-sizes and incorporating both i.i.d. and Markovian observation models. Unlike existing methods, the proposed algorithm does not require the assumption that the underlying communication network structure is characterized by a doubly stochastic matrix.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using ODE to analyze the distributed TD-learning is interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only provide the convergence results of the TD-learning under the Markovian observation and the i.i.d. observation with diminishing step-size. What about the Markovian observation with constant step-size? I think the authors should also consider this setting.

2. The authors should also discuss the iteration complexity of the proposed algorithm. Specifically, what is the convergence rate of the average of the iterates, $\bar{x}^t$? I think this is the main advantage of the distributed TD-learning over the centralized TD-learning, since the latter needs to re-communicate the collected data to all agents, whereas the former does not need this step. Moreover, the iteration complexity may also help to compare the proposed algorithm with other distributed optimization algorithms, e.g., push-sum and push-pull.

3. The authors should also compare the proposed algorithm with other distributed RL algorithms, e.g., [1,2].

### Suggestions

The paper would benefit from a more thorough investigation into the constant step-size scenario, particularly under Markovian observations. While the authors present results for diminishing step-sizes, the constant step-size case is crucial for practical implementation, as it avoids the need for a diminishing step-size schedule. The analysis should include a convergence proof, demonstrating that the iterates converge to a neighborhood of the optimal solution, and characterize the size of this neighborhood. Furthermore, it would be beneficial to investigate the impact of the step-size on the convergence rate and the size of the steady-state error. This analysis should also consider the practical implications of choosing different step-size values and provide guidelines for selecting an appropriate step-size in practice. The authors could also explore the use of adaptive step-size methods, which could potentially improve the convergence rate and robustness of the algorithm.

Regarding the iteration complexity, a detailed analysis of the convergence rate of the average of the iterates, $\bar{x}^t$, is essential. The authors should provide a clear comparison of the convergence rate of their algorithm with existing distributed optimization algorithms, such as push-sum and push-pull, in terms of the number of communication rounds and the number of local computations. This analysis should consider the impact of the network topology and the size of the data on the convergence rate. Furthermore, the authors should discuss the practical implications of the iteration complexity, such as the computational cost and the communication overhead. It would also be helpful to provide a numerical comparison of the convergence rate of the proposed algorithm with other distributed optimization algorithms in different scenarios. This would help to demonstrate the advantages and limitations of the proposed algorithm in practice.

Finally, the authors should provide a more comprehensive comparison with other distributed reinforcement learning algorithms. While the current paper focuses on the convergence analysis of the proposed algorithm, it is important to position it within the broader context of distributed RL. The authors should discuss the similarities and differences between their algorithm and other distributed RL algorithms, such as those based on policy gradients [1,2]. This comparison should include a discussion of the advantages and disadvantages of each algorithm, as well as the scenarios in which each algorithm is most suitable. Furthermore, the authors should provide a numerical comparison of the performance of their algorithm with other distributed RL algorithms in different environments. This would help to demonstrate the effectiveness of the proposed algorithm and its potential for real-world applications.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********
