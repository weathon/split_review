### Summary

This paper studies distributed temporal difference (TD) learning for a networked multi-agent Markov decision process. The authors propose a distributed optimization algorithm that can be interpreted as primal-dual ODE dynamics subject to null-space constraints. The paper analyzes the convergence behavior of the algorithm under various scenarios, including constant and diminishing step-sizes, and i.i.d. and Markovian observation models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a comprehensive analysis of the proposed algorithm under various scenarios, including different step-size choices and observation models. This makes the results more robust and applicable to a wider range of problems.

2. The paper is well-written and easy to follow, with clear explanations of the technical details and intuitive interpretations of the results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only considers linear function approximation. It would be interesting to see how the proposed algorithm performs with non-linear function approximation.

2. The paper does not provide any experimental results to validate the theoretical findings. It would be helpful to see some numerical simulations to demonstrate the practical performance of the algorithm.

### Suggestions

The paper's focus on linear function approximation, while providing a strong theoretical foundation, limits its practical applicability. Many real-world problems involve complex, non-linear relationships that linear models cannot capture effectively. Exploring the performance of the proposed algorithm with non-linear function approximators, such as neural networks, would be a valuable extension. This would involve adapting the analysis to handle the non-convexity introduced by these approximators, which could be challenging but would significantly broaden the impact of the work. Specifically, the authors could investigate how the convergence properties of the algorithm are affected by the choice of non-linear function approximator and the associated optimization landscape. This would require careful consideration of the approximation error and its impact on the overall convergence rate. Furthermore, it would be beneficial to explore different types of non-linear function approximators, such as kernel methods or recurrent neural networks, to understand their suitability for different types of problems.

To strengthen the paper's practical relevance, it is crucial to include experimental results that validate the theoretical findings. The current analysis, while rigorous, lacks empirical support. Numerical simulations on benchmark problems would provide valuable insights into the algorithm's performance in practice. These experiments should include a comparison with existing distributed TD learning algorithms to demonstrate the advantages and limitations of the proposed approach. The experiments should also explore the sensitivity of the algorithm to various parameters, such as the step-size and the communication frequency. Furthermore, it would be beneficial to investigate the algorithm's performance in different network topologies and with varying numbers of agents. This would help to understand the scalability and robustness of the proposed approach. The experimental results should be presented clearly and concisely, with appropriate statistical analysis to support the conclusions.

Finally, the paper could benefit from a more detailed discussion of the assumptions made in the theoretical analysis. While the authors mention the assumptions, a more in-depth discussion of their implications and limitations would be helpful. For example, the assumption of i.i.d. samples may not hold in all practical scenarios, and it would be useful to discuss how the algorithm's performance might be affected by violations of this assumption. Similarly, the assumption of a fixed communication network may not be realistic in dynamic environments, and it would be beneficial to explore how the algorithm could be adapted to handle changing network topologies. A more thorough discussion of these assumptions would help to clarify the scope and limitations of the proposed approach and provide guidance for future research.

### Questions

1. Can the proposed algorithm be extended to non-linear function approximation?

2. How does the proposed algorithm compare to existing distributed TD learning algorithms in terms of computational complexity and communication overhead?

### Rating

6

### Confidence

3

**********
