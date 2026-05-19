### Summary

This paper presents a novel approach, Graph Assisted Offline-Online Deep Reinforcement Learning (GOODRL), for dynamic workflow scheduling (DWS) in cloud computing. The authors address the challenges of heterogeneous machine configurations, unpredictable workflow arrivals, and evolving environments, which are often oversimplified in existing research. GOODRL introduces three key innovations: a task-specific graph representation and Graph Attention Actor Network for focused task assignment, a system-oriented graph representation and Graph Attention Critic Network for efficient information processing, and an offline-online reinforcement learning method that combines imitation learning with gradient control and decoupled high-frequency critic training. The experimental results demonstrate that GOODRL significantly outperforms state-of-the-art algorithms in terms of mean flowtime and adaptability in various online and offline scenarios.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach, GOODRL, which combines graph representations with deep reinforcement learning to address the complex problem of dynamic workflow scheduling in cloud computing.
2. The authors propose a task-specific graph representation and a Graph Attention Actor Network, enabling the agent to dynamically assign tasks to heterogeneous machines while considering the future impact of each machine on the tasks.
3. The paper presents a comprehensive experimental evaluation, demonstrating that GOODRL significantly outperforms several state-of-the-art algorithms in various scenarios. The results show substantial reductions in mean flowtime and high adaptability in both offline and online settings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential directions for future work. For example, the current approach assumes a specific type of cloud computing environment and may not be directly applicable to other types of scheduling problems. It is unclear how the task-specific graph representation and the Graph Attention Actor Network would adapt to scenarios with different resource constraints or task dependencies. The system-oriented graph representation and the Graph Attention Critic Network might also face challenges when dealing with highly dynamic environments where the system state changes rapidly and unpredictably. Furthermore, the offline-online RL method, while effective in the tested scenarios, may require significant retraining or fine-tuning when applied to new environments with different characteristics. A more thorough analysis of these limitations would strengthen the paper.
2. The paper could provide more details on the computational complexity of the proposed approach and its scalability to larger and more complex scheduling problems. While the paper mentions that GOODRL can handle large-scale problems, it lacks a rigorous analysis of how the computational cost scales with the number of tasks, machines, and workflow complexity. The use of graph neural networks, while powerful, can be computationally expensive, especially when dealing with large graphs. The paper should provide a more detailed breakdown of the time complexity of each component of the GOODRL approach, including the graph construction, the actor and critic network forward passes, and the training process. This analysis should also consider the memory requirements of the approach, which can be a limiting factor when dealing with large-scale problems. A more detailed discussion of the computational complexity and scalability would provide a better understanding of the practical applicability of the proposed approach.

### Suggestions

To address the limitations regarding the applicability of the proposed approach, the authors should consider including a more detailed discussion on how the task-specific and system-oriented graph representations can be adapted to different scheduling scenarios. For instance, in environments with varying resource constraints, the graph representation could be extended to include node features that capture the specific resource requirements of each task and the availability of resources on each machine. Similarly, for scenarios with different task dependencies, the edge connections in the graph could be modified to reflect these dependencies. The authors could also explore the use of transfer learning techniques to leverage the knowledge gained from one scheduling environment to improve performance in another. This would involve pre-training the model on a diverse set of scheduling problems and then fine-tuning it on the target environment. Furthermore, the authors should investigate the robustness of the proposed approach to changes in the environment, such as unexpected machine failures or changes in task arrival patterns. This could be done by evaluating the performance of the approach under different levels of uncertainty and comparing it to other scheduling algorithms that are designed to handle such uncertainties.

To address the concerns about computational complexity and scalability, the authors should provide a more detailed analysis of the time and space complexity of each component of the GOODRL approach. This analysis should include a breakdown of the computational cost of graph construction, actor and critic network forward passes, and the training process. The authors should also consider the impact of different graph sizes and network architectures on the overall computational cost. Furthermore, the authors could explore techniques for reducing the computational cost of the approach, such as using more efficient graph neural network architectures or employing approximation methods for the critic network. The paper should also include a discussion of the memory requirements of the approach, particularly when dealing with large-scale problems. This discussion should consider the memory needed to store the graph representations, network parameters, and intermediate results. The authors could also investigate techniques for reducing the memory footprint of the approach, such as using sparse graph representations or model compression techniques. Finally, the authors should provide empirical evidence of the scalability of the approach by evaluating its performance on a range of problem sizes and complexities.

In addition to the above, the authors should also consider a more in-depth analysis of the sensitivity of the proposed approach to hyperparameter settings. The performance of reinforcement learning algorithms can be highly sensitive to the choice of hyperparameters, such as the learning rate, discount factor, and exploration strategy. The authors should provide a detailed analysis of how these hyperparameters affect the performance of GOODRL and provide guidelines for selecting appropriate values for different scheduling scenarios. This analysis could include a sensitivity study that systematically varies the hyperparameters and evaluates their impact on the performance of the approach. Furthermore, the authors should discuss the potential limitations of the offline-online RL method when applied to environments that are significantly different from the offline training data. The paper should also explore techniques for mitigating these limitations, such as using domain adaptation methods or incorporating online learning techniques that can adapt to changes in the environment.

### Questions

1. How does the proposed approach handle different types of cloud computing environments and scheduling problems? Can it be adapted to other types of environments and problems, or is it specifically designed for the scenarios considered in the paper?
2. What is the computational complexity of the proposed approach, and how does it scale to larger and more complex scheduling problems? Are there any limitations in terms of the size and complexity of the problems that can be handled by GOODRL?

### Rating

6

### Confidence

3

**********
