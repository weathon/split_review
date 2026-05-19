### Summary

This paper studies the convergence of distributed TD-learning. The authors first analyze the continuous-time version of the distributed TD-learning, i.e., the primal-dual ODE. Then, based on the analysis of the ODE, the authors study the distributed TD-learning with both constant and diminishing step-size.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and well-organized. The analysis is detailed and convincing.

### Weaknesses

#### Some Related Works

[1] Accelerating distributed reinforcement learning with gradient tracking.
[2] Distributed reinforcement learning with policy gradients.
[3] Decentralized Primal-Dual Stochastic Gradient Method.

#### comment

 1. The authors only provide the convergence results of the TD-learning under the Markovian observation and the i.i.d. observation with diminishing step-size. What about the Markovian observation with constant step-size? I think the authors should also consider this setting.

 2. The authors should also discuss the iteration complexity of the proposed algorithm. Specifically, what is the convergence rate of the average of the iterates, $\bar{x}^t$? I think this is the main advantage of the distributed TD-learning over the centralized TD-learning, since the latter needs to re-communicate the collected data to all agents, whereas the former does not need this step. Moreover, the iteration complexity may also help to compare the proposed algorithm with other distributed optimization algorithms, e.g., push-sum and push-pull.

 3. The authors should also compare the proposed algorithm with other distributed RL algorithms, e.g., [1,2].

### Suggestions

The paper would benefit from a more thorough investigation into the constant step-size scenario, particularly under Markovian observations. While the authors present results for diminishing step-sizes, the constant step-size case is crucial for practical implementation, as it avoids the need for a diminishing step-size schedule. The analysis should include a convergence proof, demonstrating that the iterates converge to a neighborhood of the optimal solution, and characterize the size of this neighborhood. Furthermore, it would be beneficial to investigate the impact of the step-size on the convergence rate and the size of the steady-state error. This analysis should also consider the practical implications of choosing different step-size values and provide guidelines for selecting an appropriate step-size in practice. The authors could also explore the use of adaptive step-size methods, which could potentially improve the convergence rate and robustness of the algorithm.

Regarding the iteration complexity, a detailed analysis of the convergence rate of the average of the iterates, $\bar{x}^t$, is essential. The authors should provide a clear comparison of the convergence rate of their algorithm with existing distributed optimization algorithms, such as push-sum and push-pull, in terms of the number of communication rounds and the number of local computations. This analysis should consider the impact of the network topology and the size of the data on the convergence rate. Furthermore, the authors should discuss the practical implications of the iteration complexity, such as the computational cost and the communication overhead. It would also be helpful to provide a numerical comparison of the convergence rate of the proposed algorithm with other distributed optimization algorithms in different scenarios. This would help to demonstrate the advantages and limitations of the proposed algorithm in practice.

Finally, the authors should provide a more comprehensive comparison with other distributed reinforcement learning algorithms. While the current paper focuses on the convergence analysis of the proposed algorithm, it is important to position it within the broader context of distributed RL. The authors should discuss the similarities and differences between their algorithm and other distributed RL algorithms, such as those based on policy gradients [1,2]. This comparison should include a discussion of the advantages and disadvantages of each algorithm, as well as the scenarios in which each algorithm is most suitable. Furthermore, the authors should provide a numerical comparison of the performance of their algorithm with other distributed RL algorithms in different environments. This would help to demonstrate the effectiveness of the proposed algorithm and its potential for real-world applications.

### Questions

1. In Assumption 3, why do we require that $\mathbb{E}[\delta_{a_i,t}\delta_{a_j,t}]>0$ for all $i,j$? Is this condition practical? 

2. In Eq.(12), why do we require that $\mu\geq \frac{NL}{2\lambda_{\min}(\Pi^T W \Pi)}$? It seems that $\lambda_{\min}(\Pi^T W \Pi)$ may be very small, especially when the network is very sparse. In this case, $\mu$ may be very large. However, a large $\mu$ may lead to a slow convergence. 

3. In Eq.(20), why do we require that $\mu<\frac{1}{\lambda_{\max}(D) L}$? In my opinion, $\lambda_{\max}(D)$ may also be very large, especially when the underlying Markov chain is very recurrent. In this case, the step-size should be very small, e.g., $O(1/t)$. However, the authors only prove the convergence with the diminishing step-size. I think the authors should also discuss the constant step-size case.

### Rating

6

### Confidence

4

**********
