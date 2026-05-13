# Learning Multi-Agent Communication from Graph Modeling Perspective

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
In numerous artificial intelligence applications, the collaborative efforts of multiple intelligent agents are imperative for the successful attainment of target objectives.
    To enhance coordination among these agents, a distributed communication framework is often employed.
    However, information sharing among all agents proves to be resource-intensive, while the adoption of a manually pre-defined communication architecture imposes limitations on inter-agent communication, thereby constraining the potential for collaborative efforts.
    In this study, we introduce a novel approach wherein we conceptualize the communication architecture among agents as a learnable graph. 
    We formulate this problem as the task of determining the communication graph while enabling the architecture parameters to update normally, thus necessitating a bi-level optimization process. 
    Utilizing continuous relaxation of the graph representation and incorporating attention units, our proposed approach, CommFormer, efficiently optimizes the communication graph and concurrently refines architectural parameters through gradient descent in an end-to-end manner.
    Extensive experiments on a variety of cooperative tasks substantiate the robustness of our model across diverse cooperative scenarios, where agents are able to develop more coordinated and sophisticated strategies regardless of changes in the number of agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method for learning optimal communication graphs in multi-agent systems using attention. Unlike previous methods that use a predefined graph communication structure with unlimited comms bandwidth, CommFormer learns to create directed communication links such that some level of graph sparsity $S$ is maintained. To do this, they formulate a constrained optimization problem to learn a value encoder and action decoder with an upper bound on the norm of the graph adjacency matrix. In reality, they create a bi-level optimization that steps the encoder/decoder optimizers to find approximate optima then update the adjacency matrix. They perform experiments on StarCraftII with various value-based and policy gradient-based baselines and demonstrate that ComFormer can outperform the baselines in SMAC tasks ranging from Easy to Super Hard.

### Strengths
This is an interesting and well written paper. To my knowledge, the learned graph for graph communication using transformers is a novel idea with clear applications to the real world. The architecture is simple/clear and the motivation for the necessity of this solution is motivated very well in Figure 1.

1. The CommFormer method significantly outperforms most of the baselines on most of the tasks (with the exception of some super hard SMAC tasks)
2. Performs ablative studies to demonstrate the importance of the sparsity claimed in the paper. 
3. Adaptable to various actor-critic methods, not just PPO

### Weaknesses
There are some concerns I have about the problem formulation. It is assumed in many MARL tasks that communication at test time is limited, as per the CTDE paradigm. However, my understanding is that at each time step, the CommFormer can choose to create/destroy communication links between any arbitrary agents as long as a sparsity measure is met. While this is not unreasonable, it is a very large assumption to make while claiming the CTDE paradigm. Further, in seciton 3.2, the authors state that they restrict communication of agent $i$ to only agents $j$ where $j< i$; this assumes that there is some implicit (or explicit) ordering of the agents that we are assuming. Again, I don't think this is unreasonable as many MARL algorithms use one-hot agent id encoding, it imposes additional nuances that are important to the functioning of the algorithm.

Finally, the authors do not compare to a recent graph-based MARL baseline called QGNN[1]

### Questions
1. Can the authors compare their method to QGNN 
2. How is the ordering of agents decided when inputting to the transformer and is there positional encoding?
3. I understand that graph sparsity if a necessary assumption to manage the bandwidth of any given agent. However, can the authors discuss or demonstrate what would happen if more realistic assumptions on graph communication were made, such as only communicating with agents within some specified communication range?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- learning to leverage communication in bandwidth-restricted settings with a learnable adjacency matrix

- continuous relaxation of adjacency matrix to enable differentiable updating of the parameters and adjacency matrix with bootstrapping

### Strengths
- Solid formalization of the communication graph problem

- novel contribution**

- impressive experimental results on SMAC compared to SOTA methods

- well written paper, a pleasure to read

** Possible related work: Learning multi-agent coordination through connectivity-driven communication, Pesce and Montana, 2022, springer https://link.springer.com/article/10.1007/s10994-022-06286-6

### Weaknesses
 - fixed communication network after training. Despite the authors claiming that dynamic adjustments fall outside the scope of the paper, it would be interesting to see performance comparisons. The lack of dynamic adjustments limits the applicability of the method in scenarios where communication needs change over time, or where the environment is non-stationary. 

- task 8m is not in figure 4 (as opposed to what the "Sparsity" paragraph would suggest in 4.3 Ablations).

- "Nevertheless, As task complexity and the number of participating agents increase, a higher
level of sparsity becomes necessary to attain superior performance." this is a very confusing way to say that the matrix needs to be *less* sparse. The phrasing suggests that as complexity increases, fewer connections are needed, which is counterintuitive, given that more complex tasks typically require more coordination and thus more communication.

### Questions
Why do Dynamic adjustments fall outside the scope of the paper? It seems like this is more about considering a simplified problem setting, where the communication graph between training and execution must be similar. Did you run any experiments testing the performance of CommFormer when the nature of the communication graph changes between training and execution?

"where  ̄φ is the target network’s parameter, which is non-differentiable and updated every few epochs" what does this mean?

How does the actual runtime complexity (i.e. walltime or asymptotic) compare between the different methods? S = 0.4 is still quadratic in the number of agents, which can be limiting for large numbers of agents. Rather than having a sparsity proportion, wouldn't it be more relevant to evaluate sparsity as the actual number of non-zero values in the matrix?

Doesn't this method overfit its communication graph to the task? What does a train/test split look like in such a scenario? Do I need to assume with this training method that the communication graph remains the same between training and testing?

Why does additional environment steps seem to solve the sparsity problem in 25m?

In figure 6, any intuition as to what kind of tasks lead Commformer to perform similarly to MAT, and under FC? Since MAT allows unrestricted communication between agents, it's weird that FC seems to massively outperform MAT on some tasks.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces CommFormer, a novel approach for optimizing the communication architecture among multiple intelligent agents involved in collaborative tasks. By conceptualizing the architecture as a learnable graph and employing a bi-level optimization process with attention units, CommFormer enables agents to efficiently optimize their communication and adapt more coordinated strategies in a variety of scenarios, as demonstrated in experiments on StarCraft II combat games.

I have several comments and questions that need to be addressed before publication:

- what if the communication graph determined by your approach is not physically feasible, for instance due to environmental constraints such as a far physical distance, etc.? Isn’t a graph communication approach that determines the communication based on physical proximity better in such real-world scenarios? Maybe the best solution is a hybrid approach where environment constraints are considered and baked into the problem for determining the communication graph?

- I find the presented related work section to be weak and relatively old. Many recent SOTA graph-based multi-agent communication learning approaches are never mentioned or discussed, despite their high relevance to the proposed approach. For instance, [1]-[4] below are only a few of such works. Almost all of these works offer a distributed graph-based learned multi-agent communication method that work under POMDPs and are trained under CTDE. There are more of such recent paper. I believe the authors need to perform a more comprehensive search on the recent literature.

[1] Seraj, Esmaeil, et al. "Learning efficient diverse communication for cooperative heterogeneous teaming." Proceedings of the 21st international conference on autonomous agents and multiagent systems. 2022.

[2] Niu, Yaru, Rohan R. Paleja, and Matthew C. Gombolay. "Multi-Agent Graph-Attention Communication and Teaming." AAMAS. 2021.

[3] Bettini, Matteo, Ajay Shankar, and Amanda Prorok. "Heterogeneous Multi-Robot Reinforcement Learning." Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems. 2023.

[4] Meneghetti, Douglas De Rizzo, and Reinaldo Augusto da Costa Bianchi. "Towards heterogeneous multi-agent reinforcement learning with graph neural networks." arXiv preprint arXiv:2009.13161 (2020).

- There are many existing recent, SOTA graph-based multi-agent communication learning approaches, see above [1]-[4] (which are not even mentioned in the paper), that could be a competition for the proposed approach. The selected benchmarks do not necessarily specialize in graph-based distributed communication. The proposed learned communication graph approach should be experimented and evaluated against other graph-based methods.

- All the evaluations are performed in SMAC domains. Is this approach specialized and designed for SMAC? If not, and the solution is in fact generalizable, other domains and different problem settings must be considered. Many of such standard domains can be found in the prior work. Although SMAC domains are interesting game scenarios, the point is to have a comparable baseline performance in standard domains that can also solve other multi-agent coordination and collaboration problems, social interactions, etc.

- Related to the point above, if the presented approach does not apply to other multi-agent problems and scenarios, this should be mentioned and discussed as a limitation. Otherwise, only presenting results in one domain does not suffice.

- The second contribution bullet-point mentions the use of attention units for allocating credit to received messages. Doesn’t TarMAC already do that?

- What are the limitations of the approach? The limitations are never discussed.

At current states I vote weak rejection, since the algorithm seems to be sound and working, however there are some notable weaknesses in literature review and benchmarking (methods and domains) that need to be addressed as much as possible. I’d be happy to increase my score further when authors satisfactorily addressed my comments and questions.

### Strengths
See above.

### Weaknesses
The paper introduces CommFormer, a novel approach for optimizing the communication architecture among multiple intelligent agents involved in collaborative tasks. By conceptualizing the architecture as a learnable graph and employing a bi-level optimization process with attention units, CommFormer enables agents to efficiently optimize their communication and adapt more coordinated strategies in a variety of scenarios, as demonstrated in experiments on StarCraft II combat games.

I have several comments and questions that need to be addressed before publication:

- what if the communication graph determined by your approach is not physically feasible, for instance due to environmental constraints such as a far physical distance, etc.? Isn’t a graph communication approach that determines the communication based on physical proximity better in such real-world scenarios? Maybe the best solution is a hybrid approach where environment constraints are considered and baked into the problem for determining the communication graph?

- I find the presented related work section to be weak and relatively old. Many recent SOTA graph-based multi-agent communication learning approaches are never mentioned or discussed, despite their high relevance to the proposed approach. For instance, [1]-[4] below are only a few of such works. Almost all of these works offer a distributed graph-based learned multi-agent communication method that work under POMDPs and are trained under CTDE. There are more of such recent paper. I believe the authors need to perform a more comprehensive search on the recent literature.

[1] Seraj, Esmaeil, et al. "Learning efficient diverse communication for cooperative heterogeneous teaming." Proceedings of the 21st international conference on autonomous agents and multiagent systems. 2022.

[2] Niu, Yaru, Rohan R. Paleja, and Matthew C. Gombolay. "Multi-Agent Graph-Attention Communication and Teaming." AAMAS. 2021.

[3] Bettini, Matteo, Ajay Shankar, and Amanda Prorok. "Heterogeneous Multi-Robot Reinforcement Learning." Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems. 2023.

[4] Meneghetti, Douglas De Rizzo, and Reinaldo Augusto da Costa Bianchi. "Towards heterogeneous multi-agent reinforcement learning with graph neural networks." arXiv preprint arXiv:2009.13161 (2020).

- There are many existing recent, SOTA graph-based multi-agent communication learning approaches, see above [1]-[4] (which are not even mentioned in the paper), that could be a competition for the proposed approach. The selected benchmarks do not necessarily specialize in graph-based distributed communication. The proposed learned communication graph approach should be experimented and evaluated against other graph-based methods.

- All the evaluations are performed in SMAC domains. Is this approach specialized and designed for SMAC? If not, and the solution is in fact generalizable, other domains and different problem settings must be considered. Many of such standard domains can be found in the prior work. Although SMAC domains are interesting game scenarios, the point is to have a comparable baseline performance in standard domains that can also solve other multi-agent coordination and collaboration problems, social interactions, etc.

- Related to the point above, if the presented approach does not apply to other multi-agent problems and scenarios, this should be mentioned and discussed as a limitation. Otherwise, only presenting results in one domain does not suffice.

- The second contribution bullet-point mentions the use of attention units for allocating credit to received messages. Doesn’t TarMAC already do that?

- What are the limitations of the approach? The limitations are never discussed.

At current states I vote weak rejection, since the algorithm seems to be sound and working, however there are some notable weaknesses in literature review and benchmarking (methods and domains) that need to be addressed as much as possible. I’d be happy to increase my score further when authors satisfactorily addressed my comments and questions.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach called CommFormer, which addresses the challenge of learning multi-agent communication from a graph modeling perspective. The communication architecture among agents is modelled as a learnable graph. The problem is treated as the task of determining the communication graph while enabling the architecture parameters to update normally, thus necessitating a bi-level optimization process. By leveraging continuous relaxation of graph representation and incorporating attention mechanisms within the graph modeling framework, CommFormer enables the concurrent optimization of the communication graph and architectural parameters in an end-to-end manner.

### Strengths
This paper introduces a novel approach which models the communication architecture among agents as a learnable graph. The considered problem is formulated as the task of determining the communication graph while enabling the architecture parameters to update normally, thus necessitating a bi-level optimization process.

### Weaknesses
There have been some works which learns multi-agent cooperative behaviors based on learnable graphs. It would be better to illustrate the differences of the paper compared to them. An example is provided below.

Liu, Y., Dou, Y., Li, Y., Xu, X., & Liu, D. (2022). Temporal Dynamic Weighted Graph Convolution for Multi-agent Reinforcement Learning. Proceedings of the Annual Meeting of the Cognitive Science Society.


There are some concerns regarding the experimental setup. The paper proposes a communication-based MARL method. In fact the paradigm CTDE is not suited for such method. There are still some communications among agents for the execution of policies. It seems that CTCE is more suited for the proposed method. Some CTCE based MARL methods. for example, graph-based MARL methods, should be considered for the comparison in the experiment. Further, the use of a fully connected (FC) communication graph as an upper bound is questionable. While a 100% win rate is theoretically the maximum, it is not a practical upper bound, as performance depends on opponent behavior. The value 93.8% for the FC column is also not explained, making it unclear how this upper bound was determined.

### Questions
1. The paper proposes a communication-based MARL method. In fact the paradigm CTDE is not suited for such method. There are still some communications among agents for the execution of policies. It seems that CTCE is more suited for the proposed method. Some CTCE based MARL methods. for example, graph-based MARL methods, should be considered for the comparison in the experiment. 

2. In Table 1, the FC is a little bit confusing. Even there are no constrictions on the communication bandwidth, the win rate is still hard to be 100% as it depends how the opponents perform. Of course, 100% is the maximum value for the win rate, but it is a meaningless upper bound. Further, how the value 93.8 is obtained in FC column as the upper bound?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
