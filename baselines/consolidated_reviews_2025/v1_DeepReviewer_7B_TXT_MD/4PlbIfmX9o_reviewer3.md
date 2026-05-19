### Summary

This paper proposes a novel graph-assisted offline-online deep reinforcement learning (GOODRL) approach to address the dynamic workflow scheduling (DWS) problem in cloud computing. The key contributions include: (1) a task-specific graph representation and a Graph Attention Actor Network that efficiently assign focused tasks to heterogeneous machines; (2) a system-oriented graph representation and a Graph Attention Critic Network that manage complex interactions across workflows and machines; (3) an offline-online method that utilizes imitation learning for efficient offline training and gradient control and decoupled high-frequency critic training techniques for online learning. Experimental results show that GOODRL significantly outperforms several state-of-the-art algorithms in terms of mean flowtime and adaptability in various online and offline scenarios.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel graph-assisted offline-online deep reinforcement learning approach for dynamic workflow scheduling, which is a significant contribution to the field of cloud computing. The proposed method effectively addresses the challenges of heterogeneous machines, unpredictable workflows, and constantly evolving workloads.
2. The paper provides a comprehensive evaluation of the proposed GOODRL approach, demonstrating its superiority over several state-of-the-art algorithms in terms of mean flowtime and adaptability. The ablation studies further validate the effectiveness of the proposed components.
3. The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a detailed explanation of the problem, methodology, and experimental setup, which enhances the reproducibility of the results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational complexity of the graph-based representations and the potential challenges in scaling to very large and complex workflow systems. Specifically, the paper lacks a discussion on the memory footprint of the graph representations, which could be a limiting factor for very large graphs. Furthermore, the paper does not address the potential impact of graph sparsity on the performance of the graph attention networks, which could be a concern in sparse workflow scenarios.
2. The paper could provide more details on the specific implementation of the Graph Attention Networks (GATs) and the PPO algorithm. For example, the number of layers, the size of the hidden units, and the specific reward function used for training the actor and critic networks are not clearly described. The paper also lacks a discussion on the sensitivity of the results to these hyperparameters, which is important for reproducibility and practical application. The choice of using a transformer-based architecture for the actor and critic networks, instead of a GAT, is not well-justified, and the paper lacks a comparison with GAT-based implementations.
3. The paper could include a more comprehensive comparison with other state-of-the-art DWS algorithms, especially those that also use graph-based representations or reinforcement learning techniques. The current comparison is limited to a few baselines, and it would be beneficial to include a wider range of algorithms, including both traditional scheduling algorithms and more recent deep learning-based approaches. The paper should also discuss the specific advantages and disadvantages of GOODRL compared to these other methods.
4. The paper could provide more insights into the practical implications of the proposed approach, such as its potential impact on the performance and cost of cloud services. The paper lacks a discussion on how the proposed method can be integrated into existing cloud infrastructure and how it can be used to optimize the overall performance and cost of cloud services. The paper should also discuss the potential challenges in deploying the proposed method in real-world cloud environments.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed GOODRL approach. Specifically, the authors should provide a detailed breakdown of the time and space complexity of each component of the framework, including the graph construction, the GAT layers, and the PPO algorithm. This analysis should consider the impact of the number of workflows, machines, and tasks on the overall computational cost. Furthermore, the authors should discuss the memory requirements of the graph representations and the potential bottlenecks for very large and complex workflow systems. It would also be beneficial to include experiments that evaluate the performance of GOODRL on larger datasets and more complex workflow scenarios to demonstrate its scalability. The authors should also discuss the potential impact of graph sparsity on the performance of the graph attention networks and provide strategies to mitigate this issue.

To enhance the reproducibility and practical applicability of the proposed method, the authors should provide a more detailed description of the implementation of the Graph Attention Networks (GATs) and the PPO algorithm. This should include the number of layers, the size of the hidden units, the activation functions used, and the specific reward function employed for training the actor and critic networks. The authors should also discuss the sensitivity of the results to these hyperparameters and provide guidelines for selecting appropriate values. Furthermore, the authors should justify the choice of using a transformer-based architecture for the actor and critic networks, instead of a GAT, and provide a comparison with GAT-based implementations. This comparison should include a discussion of the advantages and disadvantages of each approach and the reasons for choosing the transformer-based architecture. The authors should also provide details on the training process, including the number of training epochs, the learning rate, and the batch size.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art DWS algorithms, especially those that also use graph-based representations or reinforcement learning techniques. This comparison should include both traditional scheduling algorithms and more recent deep learning-based approaches. The authors should discuss the specific advantages and disadvantages of GOODRL compared to these other methods, highlighting the unique contributions of their approach. The paper should also discuss the practical implications of the proposed approach, including its potential impact on the performance and cost of cloud services. This discussion should include a description of how the proposed method can be integrated into existing cloud infrastructure and how it can be used to optimize the overall performance and cost of cloud services. The authors should also discuss the potential challenges in deploying the proposed method in real-world cloud environments and provide guidelines for addressing these challenges.

### Questions

1. Could the authors provide more details on the computational complexity of the proposed GOODRL framework, especially concerning the graph-based representations and the deep reinforcement learning components? How does the framework scale with the number of workflows and machines in large-scale cloud environments?
2. Could the authors elaborate on the specific implementation details of the Graph Attention Networks (GATs) and the PPO algorithm? What are the number of layers, the size of the hidden units, and the specific reward function used for training the actor and critic networks? How sensitive are the results to these hyperparameters?
3. Could the authors provide a more comprehensive comparison with other state-of-the-art DWS algorithms, especially those that also use graph-based representations or reinforcement learning techniques? What are the specific advantages and disadvantages of GOODRL compared to these other methods?
4. Could the authors discuss the practical implications of the proposed approach, including its potential impact on the performance and cost of cloud services? How can the proposed method be integrated into existing cloud infrastructure, and what are the potential challenges in deploying it in real-world cloud environments?

### Rating

6

### Confidence

3

**********
