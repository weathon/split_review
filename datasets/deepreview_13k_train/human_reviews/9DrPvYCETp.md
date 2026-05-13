# Shared Memory for Multi-agent Lifelong Pathfinding

- Decision: Reject
- Scores: 3, 8, 5

## Abstract
Multi-agent reinforcement learning (MARL) demonstrates significant progress in solving cooperative and competitive multi-agent problems in various environments. One of the main challenges in MARL is the need to explicitly predict other agents' behavior to achieve cooperation. As a solution to this problem, we propose the Shared Recurrent Memory Transformer (SRMT), which extends memory transformers to multi-agent settings by pooling and globally broadcasting individual working memories, enabling agents to implicitly exchange information and coordinate actions. We evaluate SRMT on the Partially Observable Multi-Agent Path Finding problem, both in a toy bottleneck navigation task requiring agents to pass through a narrow corridor and on a set of mazes from the POGEMA benchmark. In the bottleneck task, SRMT consistently outperforms a range of reinforcement learning baselines, especially under sparse rewards, and generalizes effectively to longer corridors than those seen during training. On POGEMA maps,  including Mazes, Random, and Warehouses, SRMT is competitive with a variety of recent MARL, hybrid, and planning-based algorithms. These results suggest that incorporating shared memory into transformer-based architectures can enhance coordination in decentralized multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work considers the application of a shared memory mechanism to the MAPF setting.

### Strengths
- The writing is generally clear and polished. 
- The approach is well-grounded in prior literature, and the algorithmic details are well-explained.  
- Figure 1 is a useful complement to the written algorithmic details, and makes it easy to understand the method at a glance. 
- Figure 10 analysis is nice.

### Weaknesses
 * It is hard to get a relative sense of the competitiveness of this approach. The baselines did not feel particularly well-motivated, and MARL communication works, which I'd argue share a similar goal, were not used as baselines (e.g. [1])
* More generally, I am left not knowing exactly what I should take away from the results—Figure 5 seems to show that SRMT and variants achieve modest results compared to baselines (and the baselines used are not motivated or described in sufficient detail).
* [2] I consider this a necessary work to acknowledge, given it is one of the first works discussing the use of attention in MARL
* Nitpicks: 
	* I cannot interpret the error bars in Figure 4—it is too muddled.
	* Despite the writing overall being clear, the language could be tightened somewhat; e.g. L043: "has to reach its goal" is quite colloquial; also contraction in L497. I recommend combing through the paper and essentially asking each word/phrase to justify itself—and to be as specific as possible, avoiding colloquialisms. 

### Questions
- Following up on a weakness above: Why was this approach not evaluated against any MARL baselines that implement communication channels between agents?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the Shared Recurrent Memory Transformer (SRMT), a novel model in multi-agent reinforcement learning designed for multi-agent lifelong pathfinding tasks. SRMT extends memory transformers to decentralized multi-agent environments by pooling individual agent memories into a shared memory space, allowing agents to indirectly share information and coordinate. The model is tested in various pathfinding tasks, including bottleneck navigation and complex environments from the POGEMA benchmark. SRMT demonstrates superior performance in coordination and generalization, particularly in high-density and partially observable environments.

### Strengths
1. The SRMT model is an adaptation of memory transformers to multi-agent settings, facilitating indirect communication among agents through a shared memory. This approach addresses a significant challenge in decentralized coordination by leveraging shared recurrent memory, which is unique compared to conventional communication strategies.
2. The paper provides a rigorous evaluation of SRMT on multiple benchmark tasks, including POGEMA and bottleneck navigation. The use of diverse reward settings (e.g., sparse, directional) further strengthens the experimental framework, revealing SRMT’s adaptability in various coordination scenarios.
3. The architecture and methods are clearly explained, supported by diagrams and flowcharts that help clarify SRMT’s working mechanism. The comparisons with baselines and the explanation of the multi-agent Markov decision process formulation are presented in a straightforward and understandable manner.
4. SRMT’s ability to handle decentralized pathfinding without explicit communication protocols has considerable implications for real-world applications, particularly in settings where communication might be unreliable or costly. Its effectiveness across different maps and scenarios demonstrates potential for scalability in complex, large-scale environments.

### Weaknesses
1. While SRMT performs well on small to medium-sized environments, its scalability to very large maps or highly dense environments remains uncertain. The evaluation could be extended to more challenging settings, particularly with greater agent populations or larger obstacles, to fully assess SRMT’s scalability. Specifically, the paper lacks a rigorous analysis of how the shared memory mechanism scales with an increasing number of agents and map complexity. The current evaluation does not sufficiently explore scenarios where the number of agents significantly exceeds the capacity of the shared memory, potentially leading to information bottlenecks or reduced coordination effectiveness. Furthermore, the experiments should include environments with varying obstacle densities and sizes to evaluate the robustness of SRMT in cluttered spaces.
2. While SRMT is designed for decentralized systems, it would be beneficial to see comparisons with centralized approaches on key metrics to understand the trade-offs better, particularly in environments that demand high coordination. The paper should include a more detailed comparison with centralized methods, focusing on metrics such as optimality of solutions, computational cost, and communication overhead. This comparison is crucial for understanding the limitations of the decentralized approach, especially in scenarios where a centralized solution might be more efficient or effective. The current evaluation lacks a clear analysis of the performance gap between SRMT and centralized methods in highly coordinated tasks.
3. While the paper claims that shared memory improves coordination, additional analysis on how shared memory influences individual agent behavior would provide a deeper understanding. An ablation study removing the shared memory aspect could further validate its impact on SRMT’s performance. The paper should include a more detailed analysis of how agents utilize the shared memory during task execution. This analysis should include visualizations of memory representations and their evolution over time, as well as an ablation study that removes the shared memory component to quantify its impact on overall performance. The current analysis does not provide sufficient insight into the internal dynamics of the shared memory mechanism.
4. The model's performance varied across different reward structures, and while this is discussed, a more detailed exploration of how reward shaping influences learning would strengthen the analysis. This would help in tailoring SRMT to tasks where only sparse rewards are available. The paper should include a more detailed analysis of how different reward structures affect the learning process and the resulting coordination strategies. Specifically, the paper should explore how sparse rewards impact the convergence rate and the final performance of SRMT, as well as how different reward shaping techniques can be used to improve learning in sparse reward environments. The current analysis does not provide sufficient insight into the interaction between reward structure and the effectiveness of shared memory.

### Questions
1. How well does SRMT scale with an increased number of agents or more complex map structures? Additional experiments in larger environments could help evaluate its robustness in real-world applications.
2. Would SRMT benefit from combining shared memory with limited explicit communication for certain high-density environments?
3. How does shared memory impact the decision-making process for individual agents? Further analysis on memory usage patterns and shared memory dynamics could provide insights into SRMT’s internal coordination mechanisms.
4. Does SRMT allow for integration with hierarchical pathfinding methods, such as combining local and global pathfinding strategies?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a global shared recurrent memory transformer (SRMT) mechanism for multiagent reinforcement learning to address the multiagent pathing finding problem. Specifically, SRMT uses self-attention to aggregate agent memory and observation history while utilizing cross-attention to aggregate the shared memory from other agents to help coordination. Results on a toy bottleneck navigation task and a set of maze environments from the POGEMA benchmark show that SRMT outperforms various baselines.

### Strengths
1.	The motivation for using a global shared memory to help coordination and the idea of using the transformer to implement it are clear.
2.	The background is clearly explained and the related works are well discussed.

### Weaknesses
1.	It seems that a lot baselines are missing. For example, in the Bottleneck Task, only some basic memory mechanisms from single-agent RL are compared while more advanced memory mechanisms such as relational memory [1] and AMRL [2] from the single-agent RL domain are not compared. Specifically, the comparison lacks methods that explicitly model inter-agent relationships and aggregated memory, which are crucial for multi-agent coordination.
2.	At the same time, although some works about MARL memory such as RATE and ATM are discussed in Section 2.2, they are not compared in the experiments. This omission makes it difficult to assess the true advantage of the proposed approach against existing MARL memory mechanisms.
3.	The ablation study to validate each component of the proposed SRMT is not given. It is unclear how much each component of the SRMT, such as the self-attention and cross-attention mechanisms, contributes to the overall performance. Without a detailed ablation study, it is hard to justify the design choices of SRMT.
4.	There are some typos. In Line 36, “MAPF” is not defined.

### Questions
1.	Could the authors give the number of network parameters of each method? As SRMT uses transformers and ResNet, it may obtain advantages by more network parameters.
2.	Could SRMT scale well with the number of agents? If the number of agents increases, will the training time become much longer?
3.	Why does MAMBA with discrete communication protocol outperform SRMT in some scenarios? Does it mean that the global shared memory is not always the best choice? If yes, how could we choose the right method for the multiagent path-finding problem?

### Soundness
2

### Presentation
2

### Contribution
2
