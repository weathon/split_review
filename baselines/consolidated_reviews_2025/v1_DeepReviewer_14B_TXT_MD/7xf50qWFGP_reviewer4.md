### Summary

The paper proposes a novel approach for online Laplacian-based representation learning in reinforcement learning (RL), where the graph-based representation is updated simultaneously while the policy is updated by the RL algorithm. The authors introduce the Asymmetric Graph Drawing Objective (AGDO) and provide a theoretical analysis of the convergence of running online projected gradient descent on AGDO under mild assumptions. The paper also includes extensive simulation studies that empirically validate the guarantees of convergence to the true Laplacian representation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel framework for online Laplacian-based representation learning, addressing the challenge of simultaneously updating state representations and policies.
2. The authors provide a rigorous theoretical analysis, proving the ergodic convergence of the AGDO under bounded policy drift conditions.
3. The experimental results demonstrate the effectiveness of the proposed method in various simulated environments, supporting the theoretical claims.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed comparison with existing methods, particularly in terms of computational efficiency and scalability. While the authors mention the limitations of the tabular setting, a more thorough discussion of how the proposed method compares to other non-tabular Laplacian-based representation learning methods would be valuable. Specifically, the paper lacks a detailed analysis of the computational complexity of the proposed approach, including the number of gradient computations required and the memory footprint of the algorithm. Furthermore, the scalability of the method to large state spaces is not sufficiently addressed, and it is unclear how the method would perform in environments with high-dimensional state representations.
2. The assumptions made, especially regarding the bounded drift of the policy, may limit the applicability of the theoretical results to more complex or non-stationary environments. The paper does not provide a clear justification for why the bounded drift assumption is reasonable in practical scenarios. It is also unclear how the magnitude of the drift affects the convergence rate of the algorithm. A more detailed analysis of the sensitivity of the theoretical results to the policy drift would be beneficial.
3. The empirical evaluation could be strengthened by including a wider range of environments and tasks, particularly those with high-dimensional or continuous state spaces. The current experiments are limited to relatively simple simulated environments, which may not accurately reflect the challenges of real-world applications. The paper should include experiments in more complex environments with high-dimensional state spaces and continuous action spaces to demonstrate the robustness and generalizability of the proposed method.

### Suggestions

To address the lack of detailed comparison with existing methods, the authors should include a comprehensive analysis of the computational complexity of the proposed AGDO. This analysis should consider both the time and space complexity of the algorithm, and compare it with alternative methods for Laplacian representation learning. The comparison should not only focus on the number of operations but also on the practical implications for training time and resource consumption. For example, the authors could provide a table summarizing the computational cost of each method in terms of Big O notation, and discuss the factors that affect the runtime and memory usage of the proposed approach. Furthermore, the authors should include experiments that directly compare the training time and resource consumption of the proposed method with existing methods, using a range of different environment sizes and complexities. This would provide a more concrete understanding of the practical advantages and disadvantages of the proposed approach.

To address the limitations imposed by the bounded drift assumption, the authors should explore the sensitivity of the method to violations of this assumption. This could involve conducting experiments in environments where the policy changes rapidly or exhibits complex dynamics. The authors should also discuss the potential impact of violating this assumption on the convergence guarantees and the practical performance of the algorithm in such environments. Furthermore, the authors could explore alternative assumptions or modifications to the algorithm that could make it more robust to violations of the bounded drift condition. For example, the authors could investigate the use of adaptive learning rates or other techniques that could help the algorithm converge even when the policy changes rapidly. The paper should also discuss the trade-offs between the theoretical guarantees and the practical performance of the algorithm under different assumptions.

To strengthen the empirical evaluation, the authors should include experiments in a wider range of environments and tasks, particularly those with high-dimensional or continuous state spaces. This could involve using benchmark environments from the OpenAI Gym or other similar platforms. The authors should also consider evaluating the method on tasks with more complex dynamics, such as those involving multiple agents or non-stationary environments. This would provide a more comprehensive assessment of the method's generalizability and robustness. Furthermore, the authors should provide a detailed analysis of the performance of the method in these different environments, including a discussion of the factors that affect its performance and the limitations of the approach. This would help to identify the strengths and weaknesses of the method and provide guidance for future research.

### Questions

1. How does the proposed method compare to other online representation learning techniques in terms of convergence speed and stability?
2. Can the authors provide more insights into the choice of hyperparameters for the AGDO, particularly the barrier coefficient b?
3. How sensitive is the performance of the proposed method to the choice of policy learning algorithm?

### Rating

6

### Confidence

3

**********
