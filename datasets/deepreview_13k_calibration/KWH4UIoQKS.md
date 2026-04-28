# Computing Circuits Optimization via Model-Based Circuit Genetic Evolution

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Optimizing computing circuits such as multipliers and adders is a fundamental challenge in modern integrated circuit design. Recent efforts propose formulating this optimization problem as a reinforcement learning (RL) proxy task, offering a promising approach to search high-speed and area-efficient circuit design solutions. However, we show that the RL-based formulation (proxy task) converges to a local optimal design solution (original task) due to the deceptive reward signals and incrementally localized actions in the RL-based formulation. To address this challenge, we propose a novel model-based circuit genetic evolution (MUTE) framework, which reformulates the problem as a genetic evolution process by proposing a grid-based genetic representation of design solutions. This novel formulation avoids misleading rewards by evaluating and improving generated solutions using the true objective value rather than proxy rewards. To promote globally diverse exploration, MUTE proposes a multi-granularity genetic crossover operator that recombines design substructures at varying column ranges between two grid-based genetic solutions. To the best of our knowledge, MUTE is the first to reformulate the problem as a circuit genetic evolution process, which enables effectively searching for global optimal design solutions. We evaluate MUTE on several fundamental computing circuits, including multipliers, adders, and multiply-accumulate circuits. Experiments on these circuits demonstrate that MUTE significantly Pareto-dominates state-of-the-art approaches in terms of both area and delay. Moreover, experiments demonstrate that circuits designed by MUTE well generalize to large-scale computation-intensive circuits as well.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Paper presents a genetic algorithm based optimization framework (MUTE) to finding more hardware efficient multipliers and adders with respect to area and latency. The main degrees of freedom are the placement of the compressor blocks in the compressor trees. The results clearly show that their framework finds more optimal pareto fronts compared to existing RL based optimization approaches and standard synthesis techniques.

### Strengths
1)  clear problem statement and objectives, with a lot of discourse on RL related work
2)  good discussion of the theory regarding multi-variable optimization and pareto fronts /hyper volume metrics
3)  nice coverage of the limitations of pure RL approaches
4)  sound results including lots of experiments and ablation studies 
5)  novel application of genetic algorithms for HW optimization

### Weaknesses
 - The authors posit an assumption on deceptive reward signals—through the inconsistency between the RL and original optimization objectives. While a detailed theoretical proof is provided in the appendix, the oscillations shown in Figure 2 and Figure 6 are highly related to the search space and the scope of the underlying optimization problem. The authors are recommended to study the optimization objective landscape and the convergence into local optima in previous RL-based works, notably RL-MUL, AdaReset, and HAVE. Specifically, the analysis should explore how the reward function's shape and the exploration strategy of these RL methods contribute to the observed oscillations, and whether these oscillations are inherent to the RL approach or a consequence of specific implementation choices. A more detailed analysis of the optimization landscape, including the presence of saddle points or local optima, would strengthen the argument that the observed oscillations are due to deceptive reward signals rather than other factors.
- The idea behind RL-guided mutation to apply strategic modifications to the circuit design is compelling. However, details about the learned Q-network and how it guides the mutation are missing in the paper, particularly in section 4.3. The authors should add more details about the Q-network model, learning, action space (i.e., what mutations are to be applied), and more importantly, how the evolutionary framework handles invalid circuit designs after mutations. For instance, what is the specific architecture of the Q-network (e.g., number of layers, type of activation functions)? What is the reward function used to train the Q-network? How are the mutations encoded as actions, and what is the range of possible mutations? Furthermore, how does the system ensure that the mutated circuits remain functionally correct, and what mechanisms are in place to handle or discard invalid designs?
- The rationale behind leveraging two cascade models to rank the explored circuit designs needs to be further justified–specifically, why use two models instead of one ranking model that can be updated with real-world evaluation during the evolution process? Furthermore, details about the learned model to estimate the fitness and performance of the circuit design are missing. The authors are recommended to emphasize the fitness evaluation stage and running methods proposed in this paper by conducting an ablation study when using a single ranking model, a single adaptive ranking model (whose learning parameters can be updated by some real-world evaluations during the optimization process), the proposed two-stage ranking model, and ranking based on real-world evaluations only. The four strategies should be compared for performance estimation accuracy, Pareto ranking preserving, and evaluation time. This comparison should include metrics such as the correlation between predicted and actual performance, the ability of each model to maintain the Pareto front, and the computational cost of each approach.

### Questions
1)  Have you considered hybrid RL / genetic optimization approaches?  What about other optimization algorithms (simulated annealing w/ predictive heuristics)?  Can you compare MUTE's performance with a simple simulated annealing + heuristics?  
2)  Can you consider adding some context and tie-in to the larger benefits of this work to the AI/ML community? Either outside of circuit design, or even w/in circuit design, how it helps to advance the AI/ML field? 
3)  From Table 3, there is a relatively small difference in hypervolume when removing individual components in the ablation study.  Can you provide a more detailed analysis of the trade-offs between performance gains and computational costs for each component? Can you also do the same for a simplified version of MUTE since it seems like this could be an interesting approach? 
4)  Can you consider adding a discussion of the complexity and runtime tradeoffs in a new sub-section in the results section rather than the Appendix?

### Soundness
3

### Presentation
4

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
This paper tackles a fundamental challenge in circuit design by proposing an innovative approach called MUTE, a model-based circuit genetic evolution framework. The authors effectively identify limitations in current reinforcement learning (RL)-based methods, such as deceptive reward signals and limited action scope, which hinder achieving optimal circuit designs. MUTE addresses these gaps by introducing a grid-based genetic representation, allowing for a global search of design solutions that enhance performance across various circuits, including multipliers, adders, and multiply-accumulate circuits. Experimental results are impressive, with MUTE consistently outperforming state-of-the-art methods in area and delay optimization, achieving up to a 38% improvement in hypervolume metrics. Additionally, MUTE shows strong scalability to larger, more complex circuits, making it a highly promising direction for future research in circuit optimization.

### Strengths
- The authors effectively identify and address significant shortcomings in existing RL-based methods, specifically the issues of deceptive reward signals and localized actions, which often lead to suboptimal solutions in circuit design. 
- The proposed framework, MUTE, is a fresh perspective on circuit design optimization. Specifically, MUTE's grid-based genetic representation allows for a more comprehensive and global search of optimal design solutions, providing a significant advantage over RL methods that may focus too narrowly on localized actions.
- The paper backs its claims with extensive empirical evidence, showing that MUTE outperforms state-of-the-art methods on fundamental computing circuits like multipliers, adders, and multiply-accumulate circuits.
- The evaluation section is comprehensive and detailed; the results are also promising. They demonstrate the effectiveness of the MUTE framework, with improvements in hypervolume metrics by up to 38% and clear and measurable advancements in area and delay optimization.
- Overall, the paper is very well written and flows nicely. Also, by introducing a framework that can Pareto-dominate existing and recent methods in terms of area efficiency and speed, the paper makes a notable contribution to the field of circuit optimization.

### Weaknesses
• The paper argues that RL’s objective function is a proxy since it optimizes cumulative reward rather than the best reward achieved in the trajectory. This might be a significant problem in greedy RL algorithms such as DQN. There are other RL algorithms, such as PPO, that use entropy to promote exploration to escape local optimum. How does MUTE compare to this type of RL algorithm that promote exploration during optimization?
• The runtime for MUTE is longer than that of previous EA methods and some RL methods.
• Genetic Evolution Algorithms (GA) are established algorithms developed years ago. Is MUTE the first GA approach applied to optimize computing circuits? Are there any other global optimization algorithms, such as simulated annealing or other types of EA algorithms, used in this problem? The majority of the paper seems to narrow the related work to only EA and RL, which might not be the whole picture of this problem. I am curious about the advantages and novelty MUTE has over other traditional global optimization algorithms.

### Questions
- The authors assume that deceptive reward signals arise from inconsistencies between the RL and original optimization objectives, which may contribute to the oscillations observed in Figures 2 and 6. Could you elaborate on how this assumption impacts the results and whether analyzing the search space and optimization landscape in related works like RL-MUL, AdaReset, and HAVE might clarify these oscillations?
- The paper mentions an RL-guided mutation strategy for circuit design, yet details about the Q-network, including its structure, learning process, and action space, are limited. Could the authors provide more specifics on how the Q-network decides on mutations and manages invalid designs resulting from these mutations? Further explanation could clarify how the framework ensures robustness in the mutation process, especially in Section 4.3, where details on this aspect are limited.
- Why do the authors choose a two-stage cascade ranking model instead of a single, adaptive ranking model that could be continuously updated with real-world evaluations? Could you justify this choice by explaining the specific benefits of two models over one in the context of fitness evaluation and performance estimation? An ablation study is recommended to compare the proposed two-stage ranking model with a single ranking model, an adaptive ranking model, and real-world evaluation-based ranking. How would each strategy affect performance estimation accuracy, Pareto ranking preservation, and evaluation time?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a novel model-based circuit genetic evolution (MUTE) framework for optimizing computing circuits such as multipliers and adders by proposing a grid-based genetic representation of design solutions, which is true objective value rather than proxy rewards used in reinforcement learning (RL) frameworks. This work also proposes a multi-granularity genetic crossover operator to promote globally diverse exploration. Experiment results demonstrate MUTE’s superior ability to optimize the circuit to achieve excellent performance in terms of area and latency and is able to generalize to large-scale computation-intensive circuits.

### Strengths
• The paper is well-written and has both theoretical and experimental details to support its argument about RL's focus on local optimization.
• MUTE achieves relatively better local optimum compared to previous methods in empirical results.

### Weaknesses
• The paper argues that RL’s objective function is a proxy since it optimizes cumulative reward rather than the best reward achieved in the trajectory. This might be a significant problem in greedy RL algorithms such as DQN. There are other RL algorithms, such as PPO, that use entropy to promote exploration to escape local optimum. How does MUTE compare to this type of RL algorithm that promote exploration during optimization?
• The runtime for MUTE is longer than that of previous EA methods and some RL methods.

### Questions
Genetic Evolution Algorithms (GA) are established algorithms developed years ago. Is MUTE the first GA approach applied to optimize computing circuits? Are there any other global optimization algorithms, such as simulated annealing or other types of EA algorithms, used in this problem? The majority of the paper seems to narrow the related work to only EA and RL, which might not be the whole picture of this problem. I am curious about the advantages and novelty MUTE has over other traditional global optimization algorithms.

### Soundness
3

### Presentation
4

### Contribution
3
