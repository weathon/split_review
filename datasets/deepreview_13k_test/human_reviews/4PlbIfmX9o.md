# Graph Assisted Offline-Online Deep Reinforcement Learning for Dynamic Workflow Scheduling

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Dynamic workflow scheduling (DWS) in cloud computing presents substantial challenges due to heterogeneous machine configurations, unpredictable workflow arrivals/patterns, and constantly evolving environments. However, existing research often assumes homogeneous setups and static conditions, limiting flexibility and adaptability in real-world scenarios. In this paper, we propose a novel *Graph assisted Offline-Online Deep Reinforcement Learning* (GOODRL) approach to building an effective and efficient scheduling agent for DWS. Our approach features three key innovations: (1) a *task-specific* graph representation and a *Graph Attention Actor Network* that enable the agent to dynamically assign focused tasks to heterogeneous machines while explicitly considering the future impact of each machine on these tasks; (2) a *system-oriented* graph representation and a *Graph Attention Critic Network* that facilitate efficient processing of new information and understanding its impact on the current state, crucial for managing unpredictable workflow arrivals/patterns in real-time; and (3) an *offline-online* method that utilizes imitation learning for effective offline training and applies gradient control and decoupled high-frequency critic training techniques during online learning to sustain the agent’s robust performance in rapidly changing environments. Experimental results demonstrate that GOODRL significantly outperforms several state-of-the-art algorithms, achieving substantially lower mean flowtime and high adaptability in various online and offline scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel Graph-assisted Offline-Online Deep Reinforcement Learning (GOODRL) approach for Dynamic Workflow Scheduling (DWS) in cloud environments. The authors introduces three main innovations: a task-specific graph representation with a Graph Attention Actor Network for focused task assignments, a system-oriented graph representation with a Graph Attention Critic Network for real-time state evaluation, and a hybrid offline-online RL method to improve adaptability. The offline stage uses imitation learning for stable initial policy development, while the online stage applies advanced PPO techniques for continuous adaptation. Experiments demonstrate GOODRL’s superiority over state-of-the-art methods in minimizing mean flowtime and enhancing performance in several offline and online settings.

### Strengths
1. The paper is well-written and easy to follow
2. Special designs on the actor and critic network to have more efficient embeddings and long-range interaction modeling
3. customized gradient for stabilizing the PPO training for the online settings
4. Experiments are conducted on many online and offline settings

### Weaknesses
This paper presents a comprehensive learning pipeline for addressing the dynamic workflow scheduling (DWS) problem. I appreciate the authors for their efforts in adapting various components to suit the unique challenges of DWS.

The primary concern with this paper is the applicability of the proposed pipeline. Many of the modifications and design choices appear closely tailored to DWS, leaving it unclear how generalizable this approach might be to other scheduling problems, such as flexible job shop scheduling. Can these designs be readily adapted for other problem domains? The paper would be significantly strengthened by demonstrating the pipeline’s transferability to other scheduling scenarios.

Several techniques are introduced throughout the pipeline, though not all are rigorously validated in the ablation study. A more thorough investigation into the contributions of each component would enhance our understanding of their individual benefits.

Overall, I appreciate the contributions of this work and currently lean toward a borderline acceptance.

---
I increase my score to 8 in response to the author's rebuttal.

### Questions
Besides the concerns raised in the weakness part, I have the following additional questions:

1. PPO has also been applied to solve other combinatorial optimization problems like routing problems, where the horizons are also very large. Could you give some intuitions why PPO is particularly unstable for this problem?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Prior works often consider homogeneous setups and static conditions, and fails to consider the dynamic nature of the workflow scheduling problem. To this end, the paper proposes a GNN-based DRL approach with an offline stage as well as an online stage.

### Strengths
- The paper has many diagrams, which help the readers to understand.
- GOODRL shows strong performance against other baselines.

### Weaknesses
- My main concern is that the paper seems to be applying some existing algorithms to a scheduling problem. There are some simple modifications at different parts of the overall method, and ended up giving us good performance. However, what are the broader insights of this work?
- Consider adding more background on the DWS problem and studies on real traces.

### Questions
1. In a real-world data cluster, how does the arrival pattern change over time? Consider plotting the 95%-99% quantile of the number of simultaneous arrivals. Please also consider adding other more background information.
2. How long does the model take to make a decision at inference time, compared to prior approaches?
3. It seems that in Table 1 and 2, the arrival rates during training and testing are always the same for each scenario. However, in a real-world data center, the arrival pattern might fluctuate over time, especially in the case of extreme events (e.g., holidays or deadlines). How robust is your approach to such distribution shifts?
4. In Table 1 and 2, "Ours-Offline" already achieves a very good performance. If due to distribution shifts, the offline version gets a much lower performance, can the online algorithm quickly adapt to such changes?
5. Many real-world scenarios involve some type of resource contention or performance interference. For example, two tasks are both memory intensive, so maybe we should allocate them on different machines. How does GOODRL address this issue?

Minor:
- Line 45, "In fact existing" --> "In fact, existing"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Graph assisted Offline-Online Deep Reinforcement Learning (GOODRL) for Dynamic Workflow Scheduling for Cloud Computing. The presence of heterogenous configurations, dynamic arrival of workflows, and constant evolving environment makes this a challenging problem for State of the Art Models.

The Contributions presented in the paper are:

1) A Task-Specific Graph Representation and Graph Attention Actor Model that dynamically assign focused tasks to heterogenous machines.
2) Explicit Consideration of the future impact of the crucial state.
3) A combination of Offline Imitation Learning followed by Online PPO.

### Strengths
- Clear and detailed explanation of the approach being used.
- Easy to understand figures.
- Compared against Multiple Benchmarks and show that the model outperforms the baselines in most instances

### Weaknesses
- The topic of Resource Opimization using Graph Neural Networks is an open problem that has applications not limited to Cloud Computing. The problem itself is also explored under Multiple Travelling Salesman Problems [1, 2], Vehicle Routing Problem [3], Job Shop Scheduling [4] and Task Allocation and Scheduling in Multi-Agent Systems [5, 6]. While the application of the problem into Cloud Computing is novel, the use of Reinforcement Learning and Graph Attention Networks to similar optimization problems exists.

- It is unclear how the proposed method differs from Online Predictive Scheduling using Heterogenous Graph Attention presented in Wang et al 2022 [7]:

- The enhancement provided by the Online RL part of the model is unclear. The experimental results show that the Offline Learning allows for the model to be within 2% of the Online Training results. The significance of this improvement is unclear and needs to be discussed clearly.
 
[1] Yujiao Hu, Yuan Yao, and Wee Sun Lee. 2020. A reinforcement learning approach for optimizing multiple traveling salesman problems over graphs. Knowledge-Based Systems 204 (Sept. 2020), 106244. https://doi.org/10.1016/j.knosys.2020. 106244

[2] Yujiao Hu, Zhen Zhang, Yuan Yao, Xingpeng Huyan, Xingshe Zhou, and Wee Sun Lee. 2021. A bidirectional graph neural network for traveling salesman problems on arbitrary symmetric graphs. Engineering Applications of Artificial Intelligence 97 (Jan. 2021), 104061. https://doi.org/10.1016/j.engappai.2020.104061

[3] Steve Paul and Souma Chowdhury. 2022. A scalable graph learning approach to capacitated vehicle routing problem using capsule networks and attention mechanism, Vol. 86236. American Society of Mechanical Engineers, V03BT03A045

[4] Song, Wen, et al. "Flexible job-shop scheduling via graph neural network and deep reinforcement learning." _IEEE Transactions on Industrial Informatics_ 19.2 (2022): 1600-1610.

[5] Z. Wang and M. Gombolay, "Learning Scheduling Policies for Multi-Robot Coordination With Graph Attention Networks," in IEEE Robotics and Automation Letters, vol. 5, no. 3, pp. 4509-4516, July 2020, doi: 10.1109/LRA.2020.3002198.

[6] B. Altundas, Z. Wang, J. Bishop and M. Gombolay, "Learning Coordination Policies over Heterogeneous Graphs for Human-Robot Teams via Recurrent Neural Schedule Propagation," _2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_, Kyoto, Japan, 2022, pp. 11679-11686, doi: 10.1109/IROS47612.2022.9981748.

[7] Wang, Z., & Gombolay, M. (2022). Stochastic Resource Optimization over Heterogeneous Graph Neural Networks for Failure-Predictive Maintenance Scheduling. _Proceedings of the International Conference on Automated Planning and Scheduling_, _32_(1), 527-536. https://doi.org/10.1609/icaps.v32i1.19839

### Questions
- How does this model differ from the model presented in Wang et al 2022 [7]?

- How does the heterogeneity of the agent-task is accounted for in the graph representation?

- It is unclear what the novelty of this work is compared to similar works published in Multi-Agent Coordination, and Task Allocation and Scheduling Domains.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces an innovative approach, GOODRL, for handling dynamic workflow scheduling in cloud computing environments. This method integrates a task-specific graph representation with Graph Attention Networks (GATs) for actor-critic networks and incorporates offline imitation learning alongside online reinforcement learning to adapt to changing conditions. The proposed system is evaluated in various online and offline scenarios and is shown to outperform existing state-of-the-art methods in terms of mean flowtime and adaptability.

### Strengths
- The paper proposes a unique combination of graph representations tailored for actor and critic networks, enhancing action differentiation and value estimation.
- GOODRL demonstrates improvements in mean flowtime over established baseline algorithms, showcasing robust performance in both offline and online settings.
- The offline-online learning approach with imitation learning and gradient control addresses challenges in adapting to dynamic environments, adding practical value.
- The ablation studies and performance comparisons are thorough, providing strong evidence for the contributions and architectural decisions.

### Weaknesses
- The paper's reliance on simulations limits its generalizability to real-world cloud environments. Practical tests in real cloud data centers would bolster the validity of the results.
- The experiments primarily focus on a specific set of workflow types and machine configurations, potentially limiting the applicability of findings to other types of DWS problems.
- The computational overhead associated with the proposed GAT-based architectures is not discussed in detail, raising questions about deployment feasibility in large-scale, real-time applications.
- While the method performs well in flowtime reduction, other practical objectives, such as energy efficiency and cost, are not explored, which would be valuable for broader applicability.
- The paper lacks discussion on how the model generalizes to varied workloads, impacting its robustness in dynamic cloud environments.

### Questions
- Could the authors elaborate on how their model adapts to significant changes in workflow patterns or cloud configurations without extensive retraining? How does the method maintain robust performance under dynamic conditions that differ from the training data?
- What are the practical deployment requirements for GOODRL in terms of computational resources, and how do they compare with simpler heuristic-based solutions in large-scale, real-time applications?
- Can the authors provide more insights into how the method handles noisy or incomplete data, which is a common challenge in real-world cloud scheduling environments?
- How might the proposed approach be extended or adapted to incorporate multi-objective optimization, such as balancing energy efficiency with flowtime reduction, and what specific challenges would need to be addressed to achieve this?
- Could the authors comment on potential scalability issues when deploying GOODRL in larger cloud infrastructures or in environments with highly heterogeneous machine configurations, and how these challenges could be mitigated?

### Soundness
3

### Presentation
3

### Contribution
3
