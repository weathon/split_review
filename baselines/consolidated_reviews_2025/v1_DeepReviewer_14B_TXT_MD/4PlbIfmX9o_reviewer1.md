### Summary

The paper proposes GOODRL, a Graph assisted Offline-Online Deep Reinforcement Learning, for dynamic workflow scheduling (DWS) in cloud computing. The contributions are:

1) Task-specific graph representation and Graph Attention Actor Network for dynamic task assignment on heterogeneous machines.

2) System-oriented graph representation and Graph Attention Critic Network for efficient processing of new information and understanding its impact on the current state.

3) Offline-online RL method that utilizes imitation learning for effective offline training and applies gradient control and decoupled high-frequency critic training techniques during online learning.

Experimental results demonstrate that GOODRL outperforms several state-of-the-art algorithms, achieving lower mean flowtime and high adaptability in various online and offline scenarios.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

S1. The proposed task-specific graph representation and Graph Attention Actor Network enable the agent to dynamically assign focused tasks to heterogeneous machines while explicitly considering the future impact of each machine on these tasks.

S2. The proposed system-oriented graph representation and Graph Attention Critic Network facilitate efficient processing of new information and understanding its impact on the current state, crucial for managing unpredictable workflow arrivals/patterns in real-time.

S3. The proposed offline-online RL method utilizes imitation learning for effective offline training and applies gradient control and decoupled high-frequency critic training techniques during online learning to sustain the agent’s robust performance in rapidly changing environments.

### Weaknesses

#### Some Related Works


#### comment

W1. The proposed algorithm is still based on the PPO algorithm, with some improvements such as gradient control and decoupled high-frequency critic training techniques. These improvements are not very innovative. Moreover, these improvements are not specifically tailored to the DWS problem, and they do not fully consider the characteristics of the DWS problem. The use of gradient clipping, while common, is a relatively standard technique in RL, and its application here does not represent a significant methodological advancement. The decoupled critic training, while potentially beneficial, lacks a strong theoretical justification for why it is particularly suitable for DWS beyond empirical observation.

W2. The related work section lacks a detailed introduction to DRL-based DWS algorithms. Currently, it mainly introduces DRL-based static scheduling algorithms, which is not very relevant to this paper. The absence of a thorough discussion of existing DRL approaches specifically designed for dynamic scheduling leaves a gap in contextualizing the proposed method's novelty and contribution. The related work should include a more comprehensive overview of how DRL has been applied to dynamic scheduling problems, highlighting the specific challenges and solutions proposed in that space.

W3. The authors mention that "Current methods rely on graph representations with fixed structures, shared feature embeddings, and unmodified RL methods", but no experimental evidence (e.g., ablation studies) has been provided to support this. The claim that existing methods suffer from these limitations needs to be substantiated with empirical evidence. Without ablation studies, it is difficult to assess the individual impact of the proposed modifications to the graph representation and RL method.

W4. The proposed GOODRL algorithm is an offline-online RL method, but the authors do not provide a detailed introduction to the transition from offline to online, such as the specific conditions for transitioning from offline to online learning, and how to ensure the policy learned offline can be effectively transferred to online. The lack of clarity on the offline-to-online transition process raises concerns about the practical applicability of the method. The paper should detail the specific criteria used to determine when to switch from offline to online learning and provide a theoretical or empirical justification for this transition strategy.

### Suggestions

The paper would benefit from a more detailed analysis of the proposed improvements over PPO. While gradient control and decoupled critic training are beneficial, the paper needs to provide a more in-depth explanation of why these specific techniques are particularly well-suited for the dynamic workflow scheduling (DWS) problem. For instance, the authors could explore the theoretical implications of decoupled critic training in the context of non-stationary environments, which are characteristic of DWS. Furthermore, the paper should include a comparative analysis of the proposed method with other RL algorithms that are not based on PPO, to demonstrate the specific advantages of the proposed approach over a broader range of methods. The authors should also consider adding ablation studies to isolate the impact of each component of the proposed method, such as the task-specific graph representation and the system-oriented graph representation, to better understand their individual contributions to the overall performance.

To address the lack of a detailed introduction to DRL-based DWS algorithms, the related work section should be significantly expanded. This section should include a comprehensive review of existing DRL methods applied to dynamic scheduling, highlighting their strengths and weaknesses. The discussion should focus on how these existing methods address the challenges of dynamic environments, such as changing task arrivals and machine availability, and how the proposed method differs from and improves upon these existing approaches. This would provide a more solid foundation for the paper's contributions and help the reader understand the specific niche that the proposed method aims to fill. The related work should also discuss the specific graph representations and RL techniques used in existing DWS algorithms, providing a clear comparison with the proposed approach.

Finally, the paper needs to provide a more detailed explanation of the offline-to-online transition process. The authors should specify the exact conditions that trigger the switch from offline to online learning, such as a specific number of online tasks or a measure of the agent's performance in the online environment. Furthermore, the paper should discuss the potential challenges associated with transferring the policy learned offline to the online environment, such as the possibility of negative transfer or the need for fine-tuning. The authors could also consider adding experiments to evaluate the effectiveness of the offline-to-online transition strategy under different conditions, such as varying the size of the offline dataset or the complexity of the online environment. This would provide a more robust evaluation of the proposed method's practical applicability.

### Questions

Q1. The proposed algorithm is still based on the PPO algorithm, with some improvements such as gradient control and decoupled high-frequency critic training techniques. These improvements are not very innovative. Moreover, these improvements are not specifically tailored to the DWS problem, and they do not fully consider the characteristics of the DWS problem.

Q2. The related work section lacks a detailed introduction to DRL-based DWS algorithms. Currently, it mainly introduces DRL-based static scheduling algorithms, which is not very relevant to this paper.

Q3. The authors mention that "Current methods rely on graph representations with fixed structures, shared feature embeddings, and unmodified RL methods", but no experimental evidence (e.g., ablation studies) has been provided to support this.

Q4. The proposed GOODRL algorithm is an offline-online RL method, but the authors do not provide a detailed introduction to the transition from offline to online, such as the specific conditions for transitioning from offline to online learning, and how to ensure the policy learned offline can be effectively transferred to online.

### Rating

3

### Confidence

4

**********
