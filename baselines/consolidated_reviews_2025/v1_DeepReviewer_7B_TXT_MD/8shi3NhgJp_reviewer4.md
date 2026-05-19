### Summary

The paper proposes a novel approach to continual learning, which is based on Bayesian learning and the concept of Pareto optimality. The proposed method is able to generate models for specified trade-offs between tasks and does not require retraining with previous tasks. The authors provide theoretical guarantees for the proposed method and show that it has sublinear buffer growth. The experimental results show that the proposed method outperforms the baselines in terms of accuracy and stability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and has theoretical guarantees.
3. The experimental results show that the proposed method outperforms the baselines in terms of accuracy and stability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed comparison with existing continual learning algorithms. It is unclear how the proposed algorithm compares to other methods in terms of performance, computational cost, and memory usage. Specifically, the paper lacks a discussion of how the proposed method scales compared to other approaches, especially as the number of tasks increases. A more thorough comparison with methods like Elastic Weight Consolidation (EWC), Learning without Forgetting (LwF), or other replay-based methods would be beneficial.
2. The paper does not provide a detailed analysis of the impact of the number of preferences on the performance of the proposed algorithm. It is not clear how the algorithm's performance changes with an increasing number of preference vectors. The paper should include experiments that systematically vary the number of preferences and analyze the resulting performance trade-offs. This analysis should also consider the computational cost associated with generating models for a large number of preferences.
3. The paper does not provide a detailed analysis of the impact of the buffer size on the performance of the proposed algorithm. It is not clear how the algorithm's performance changes with an increasing buffer size. The paper should include experiments that systematically vary the buffer size and analyze the resulting performance trade-offs. This analysis should also consider the computational cost associated with maintaining a large buffer.

### Suggestions

The paper would benefit from a more comprehensive experimental evaluation that includes a detailed comparison with existing continual learning algorithms. Specifically, the authors should compare their method against a range of established techniques, such as Elastic Weight Consolidation (EWC), Learning without Forgetting (LwF), and other replay-based methods. This comparison should not only focus on the final performance but also on the computational cost, memory usage, and the number of training steps required to achieve comparable performance. Furthermore, the authors should provide a theoretical analysis of the computational complexity of their algorithm and compare it to the complexity of other methods. This analysis should consider the number of tasks, the number of preferences, and the buffer size. It would also be beneficial to include a discussion of the limitations of the proposed method and the scenarios where it might not be the most suitable approach.

To address the lack of analysis regarding the number of preferences and buffer size, the authors should conduct a series of experiments that systematically vary these parameters. For the number of preferences, the experiments should explore a range of preference vectors, analyzing how the performance of the algorithm changes with an increasing number of preferences. This analysis should also consider the computational cost associated with generating models for a large number of preferences. For the buffer size, the experiments should systematically vary the size of the buffer and analyze the resulting performance trade-offs. This analysis should also consider the computational cost associated with maintaining a large buffer. The authors should also provide a discussion of the practical implications of these findings, such as how to choose the optimal number of preferences and buffer size for a given application.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method and the scenarios where it might not be the most suitable approach. For example, the authors should discuss the potential challenges of applying the method to very large-scale datasets or to tasks with complex dependencies. They should also discuss the potential limitations of the variational inference approach used in the algorithm. This discussion should provide a more balanced view of the proposed method and help the reader understand its strengths and weaknesses. The authors should also consider the potential for future research directions, such as exploring alternative inference techniques or incorporating other continual learning strategies.

### Questions

1. How does the proposed algorithm compare to other continual learning algorithms in terms of performance, computational cost, and memory usage?
2. How does the performance of the proposed algorithm change with an increasing number of preferences?
3. How does the performance of the proposed algorithm change with an increasing buffer size?

### Rating

6

### Confidence

2

**********
