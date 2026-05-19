### Summary

This paper presents a novel approach to Dynamic Workflow Scheduling (DWS) in cloud computing environments, addressing the challenges of heterogeneous machines, unpredictable workflows, and constantly evolving workloads. The authors introduce GOODRL, a Graph-assisted Offline-Online Deep Reinforcement Learning (DRL) framework that leverages both task-specific and system-oriented graph representations. The proposed method features three key innovations: a task-specific graph representation and Graph Attention Actor Network for efficient task assignment, a system-oriented graph representation and Graph Attention Critic Network for managing complex interactions across workflows and machines, and an offline-online method that utilizes imitation learning for efficient offline training and gradient control and decoupled high-frequency critic training techniques for online learning. Experimental results demonstrate that GOODRL significantly outperforms state-of-the-art algorithms, achieving substantially lower mean flowtime and high adaptability in various online and offline scenarios.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors clearly explain the problem, methodology, and experimental setup, making it accessible to a broad audience.

- The proposed GOODRL framework is innovative in its use of graph representations and deep reinforcement learning for dynamic workflow scheduling. The task-specific and system-oriented graph representations are particularly well-suited to the challenges of DWS in cloud environments.

- The experimental results are compelling, demonstrating the superiority of GOODRL over state-of-the-art algorithms in terms of mean flowtime and adaptability. The ablation studies further validate the effectiveness of the proposed components.

- The paper addresses a critical and practical problem in cloud computing, where efficient workflow scheduling is essential for performance and resource utilization. The proposed solution has the potential to significantly impact real-world cloud systems.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational complexity of the graph-based representations and the potential challenges in scaling to very large and complex workflow systems. Specifically, the paper lacks a discussion on how the graph construction and processing scale with the number of workflows and machines, which is crucial for practical deployment in large-scale cloud environments. The memory footprint of the graph representations, especially for dense graphs, could also be a limiting factor.

- The paper could provide more details on the specific implementation of the Graph Attention Networks (GATs) and the PPO algorithm. For example, the number of layers, the size of the hidden units, and the specific reward function used for training the actor and critic networks are not clearly described. Furthermore, the paper does not discuss the sensitivity of the results to these hyperparameters, which is important for reproducibility and practical application. The choice of using a transformer-based architecture for the actor and critic networks, instead of a GAT, is not well-justified, and the paper lacks a comparison with GAT-based implementations.

- The paper could include a more comprehensive comparison with other state-of-the-art DWS algorithms, especially those that also use graph-based representations or reinforcement learning techniques. The current comparison is limited to a few baselines, and it would be beneficial to include a wider range of algorithms, including both traditional scheduling algorithms and more recent deep learning-based approaches. The paper should also discuss the specific advantages and disadvantages of GOODRL compared to these other methods.

- The paper could provide more insights into the practical implications of the proposed approach, such as its potential impact on the performance and cost of cloud services. The paper lacks a discussion on how the proposed method can be integrated into existing cloud infrastructure and how it can be used to optimize the overall performance and cost of cloud services. The paper should also discuss the potential challenges in deploying the proposed method in real-world cloud environments.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the proposed GOODRL framework, particularly concerning the graph-based representations and the deep reinforcement learning components. This analysis should consider the time and space complexity of graph construction, graph traversal, and the training of the actor and critic networks. The authors should provide a detailed breakdown of the computational cost associated with each component of the framework, including the graph construction, the GAT layers, and the PPO algorithm. Furthermore, the paper should discuss the scalability of the proposed approach to very large and complex workflow systems, including the potential bottlenecks and limitations. It would be beneficial to include experiments that evaluate the performance of GOODRL on larger datasets and more complex workflow scenarios to demonstrate its scalability. The authors should also discuss the memory requirements of the graph representations and the impact of graph density on the performance of the framework.

To enhance the reproducibility and practical applicability of the proposed method, the paper should provide a more detailed description of the implementation of the Graph Attention Networks (GATs) and the PPO algorithm. This should include the number of layers, the size of the hidden units, the activation functions used, and the specific reward function employed for training the actor and critic networks. The authors should also discuss the sensitivity of the results to these hyperparameters and provide guidelines for selecting appropriate values. Furthermore, the paper should justify the choice of using a transformer-based architecture for the actor and critic networks, instead of a GAT, and provide a comparison with GAT-based implementations. The authors should also discuss the potential limitations of the chosen architecture and the impact of these choices on the performance of the framework. It would be beneficial to include ablation studies that evaluate the impact of different architectural choices on the performance of GOODRL.

The paper should include a more comprehensive comparison with other state-of-the-art DWS algorithms, especially those that also use graph-based representations or reinforcement learning techniques. This comparison should include both traditional scheduling algorithms and more recent deep learning-based approaches. The authors should discuss the specific advantages and disadvantages of GOODRL compared to these other methods, highlighting the unique contributions of their approach. The paper should also discuss the specific scenarios where GOODRL is expected to outperform other methods and the scenarios where other methods might be more suitable. The authors should also provide a discussion of the practical implications of the proposed approach, including its potential impact on the performance and cost of cloud services. This discussion should include a description of how the proposed method can be integrated into existing cloud infrastructure and how it can be used to optimize the overall performance and cost of cloud services. The paper should also discuss the potential challenges in deploying the proposed method in real-world cloud environments and provide guidelines for addressing these challenges.

### Questions

- Could the authors provide more details on the computational complexity of the proposed GOODRL framework, especially concerning the graph-based representations and the deep reinforcement learning components? How does the framework scale with the number of workflows and machines in large-scale cloud environments?

- Could the authors elaborate on the specific implementation details of the Graph Attention Networks (GATs) and the PPO algorithm? What are the number of layers, the size of the hidden units, and the specific reward function used for training the actor and critic networks? How sensitive are the results to these hyperparameters?

- Could the authors provide a more comprehensive comparison with other state-of-the-art DWS algorithms, especially those that also use graph-based representations or reinforcement learning techniques? What are the specific advantages and disadvantages of GOODRL compared to these other methods?

- Could the authors discuss the practical implications of the proposed approach, including its potential impact on the performance and cost of cloud services? How can the proposed method be integrated into existing cloud infrastructure, and what are the potential challenges in deploying it in real-world cloud environments?

### Rating

6

### Confidence

3

**********
