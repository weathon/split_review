# MENTOR: Mixture-of-Experts Network with Task-Oriented Perturbation for Visual Reinforcement Learning

- Decision: Reject
- Scores: 5, 8, 5, 6

## Abstract
Visual deep reinforcement learning~(RL) enables robots to acquire skills from visual input for unstructured tasks. However, current algorithms suffer from low sample efficiency, limiting their practical applicability. In this work, we present {\model}, a method that improves both the \textit{architecture} and \textit{optimization} of RL agents. Specifically, {\model} replaces the standard multi-layer perceptron~(MLP) with a mixture-of-experts~(MoE) backbone, enhancing the agent's ability to handle complex tasks by leveraging modular expert learning to avoid gradient conflicts. Furthermore, {\model} introduces a task-oriented perturbation mechanism, which heuristically samples perturbation candidates containing task-relevant information, leading to more targeted and effective optimization. {\model} outperforms state-of-the-art methods across three simulation domains---DeepMind Control Suite, Meta-World, and Adroit. Additionally, {\model} achieves an average of 83\% success rate on three challenging real-world robotic manipulation tasks including Peg Insertion, Cable Routing, and Tabletop Golf, which significantly surpasses the success rate of 32\% from the current strongest model-free visual RL algorithm. These results underscore the importance of sample efficiency in advancing visual RL for real-world robotics. Experimental videos are available at \href{https://suninghuang19.io/mentor_page}{\textit{mentor}}.

\begin{figure}[ht]
\centering
\includegraphics[width=0.99\linewidth, trim= 2.3cm 9.7cm 2.3cm 0.1cm, clip]{figures/teaser.pdf}
\caption{\textbf{{\model} is validated in real-world tasks.} We design three challenging robotic learning tasks for the agent to acquire skills through real-world visual reinforcement learning. {\model} achieves the most efficient and robust policies compared to the baselines.}
\label{fig:teaser}
\end{figure}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce MENTOR, a visual deep RL algorithm designed to improve sample efficiency in robotic tasks. MENTOR enhances RL agents by replacing traditional MLPs with a MoE architecture. Additionally, the authors introduce a task-oriented perturbation mechanism that heuristically samples task-relevant perturbations. Their experiments show MENTOR can get good performance over the diverse tasks.

### Strengths
1. The paper is well-structured and easy to understand, with a clear presentation of the proposed method.
2. The authors conduct extensive experiments in both simulated and real environments, effectively demonstrating the method’s efficacy.

### Weaknesses
1. The proposed MoE architecture is not evaluated over multi-task environments, especially ones that need different strategies for the different tasks in the environments.
2. The benefit of the MoE and the task-oriented exploration strategies are coupled. The authors need to decouple this two components and show the effectiveness of the MoE.
3. The authors need to compare with other techniques that can handle the multi-modality like transformers, diffusion-based policy.

### Questions
The authors need to address my concerns in the weakness section.

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
The paper presents MENTOR, an innovative approach to enhance sample efficiency in visual deep reinforcement learning (RL) for robotics. By replacing the standard multi-layer perceptron with a mixture-of-experts (MoE) architecture and introducing a task-oriented perturbation mechanism, MENTOR improves the agent's performance in complex tasks and facilitates more effective optimization. The method demonstrates superior results across three simulation domains and achieves an impressive 83% success rate on challenging real-world robotic tasks, significantly outperforming the current best model-free visual RL algorithm, which only achieves 32%.

### Strengths
1. MENTOR introduces a mixture-of-experts (MoE) architecture that enhances learning efficiency by dynamically allocating gradients to modular experts, effectively mitigating gradient conflicts in complex scenarios.
2. The evaluation extends beyond simulations to real-world robotic manipulation tasks, demonstrating MENTOR’s practical value and sample efficiency, which are crucial for advancing reinforcement learning applications in robotics.

### Weaknesses
While MENTOR demonstrates impressive performance in both simulation and real-world tasks, the paper could benefit from a more detailed analysis of the limitations of the proposed approach, particularly in terms of scalability and generalization across diverse robotic platforms and environments. This would provide a clearer understanding of the framework's applicability in broader contexts.

### Questions
1. Are the experimental results in the real-world obtained through sim2real transfer of models trained in simulation, or are they trained from scratch entirely in a real environment?  
2. Why are external disturbance experiments not conducted in the simulation environment?

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
4

### Summary
This paper proposes a sample-efficient visual reinforcement learning approach called MENTOR, which utilizes a mixture-of-experts network instead of the traditional MLP network to mitigate gradient conflicts, along with a task-oriented perturbation method to enhance exploration. Evaluation results in multiple simulation environments show that MENTOR is sample efficient. Further, MENTOR can be successfully used for real-world reinforcement learning, which facilitates the application of reinforcement learning to real-world scenarios.

### Strengths
1) Attempts to alleviate the burden of shared parameters by introducing MoE architectures into reinforcement learning

2) A simple and effective perturbation method is proposed that can better guide the policy learning

3) The proposed method achieves an improvement in sample efficiency compared to DrM

4) Validates the effectiveness of the method on real-world robotics tasks, providing a valuable reference for the community

### Weaknesses
1) Lack of persuasion and ablation in the use of MoE. MoE has been widely used in the field of multi-task learning, and it can effectively alleviate the conflict problem due to multi-objective optimization. However, policy optimization in a single robot manipulation task often has only one optimization objective, which does not fit the context of multi-task learning. Although it is claimed in the paper that the architecture advantage can be propagated to a single task to alleviate the burden of shared parameters, there is no further analysis and ablation experiments on this. Specifically, the paper does not address whether the observed performance gains are due to the increased model capacity of the MoE, or its ability to specialize different experts to different phases of the task. Without such analysis, it is difficult to justify the architectural choice.

2) Lack of correlation between the two main improvements. MENTOR makes improvements in both architecture and optimization, yet there seems to be no necessary connection between the two. This makes the improvements in the paper appear as if they are just a combination of two tricks. In fact, optimization is often related to architecture, and it remains uncertain whether the use of MoE will introduce new challenges for policy optimization. For example, the paper does not discuss whether the task-oriented perturbation method is equally effective with a standard MLP architecture, or if the MoE structure requires specific tuning of the perturbation parameters. The lack of this analysis makes it unclear if the two components are truly synergistic.

3) Lack of ablation of the two improvements. The paper only provides performance curves for MENTOR in simulation tasks, lacking ablation studies on architecture and optimization, which makes the reasons for the final performance improvement unclear. Although incremental comparisons are made in real-robot experiments, comparisons in simulation tasks will be more convincing and fairer. The absence of ablation studies in simulation makes it impossible to determine the individual contribution of the MoE architecture and the task-oriented perturbation method. For example, it is not clear whether the performance improvement is primarily due to the more effective exploration strategy or the increased representational capacity of the MoE network.

### Questions
1) Whether it can be shown that the multi-stage property of the task in single-task learning leads to the gradient conflict problem or the existence of a shared parameter burden in policy optimization?

2) Is MoE more prone to dormancy than MLP or can it mitigate dormancy to some extent?

3) In Figure 6, why MENTOR performs worse on hammer than on hammer (sparse)?

4) Does the performance improvement in Fig. 6 arise mainly from the task-oriented perturbations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of reinforcement learning with visual observations, where learning an efficient policy from high-dimensional image data is difficult. The authors propose a novel approach by incorporating a mixture-of-experts (MoE) architecture in the policy and applying task-oriented perturbation to optimize learning efficiency. The method, called MENTOR, is tested on several reinforcement learning benchmarks, including DeepMind Control Suite, Meta-World, and Adroit, as well as real-world experiments. MENTOR demonstrates superior performance compared to prior state-of-the-art (SOTA) methods.

### Strengths
* The paper is clearly written and easy to follow.  
* The proposed approach—integrating a mixture-of-experts in the policy architecture and applying task-oriented perturbation—is well-motivated and empirically supported, as demonstrated in Figures 3 and 4\.  
* MENTOR shows significant empirical improvements over baseline methods in both simulated environments and real-world experiments.

### Weaknesses
 * The paper lacks a discussion of its limitations and possible future directions for addressing them.  
* Several clarifications could improve the writing and presentation of the work.  
* A more detailed analysis of hyperparameter sensitivity would be beneficial. It would be helpful to understand how MENTOR's performance is affected by hyperparameters such as the number of experts, the number of top-k experts, the perturbation rate, and the size of the set S_{top}​.


### Questions
1. **Ablation study**: If the method only used the MoE component and random perturbation (similar to DrM), what would the performance be? It would be valuable to analyze whether the mixture-of-experts or task-oriented perturbation contributes more to the success of MENTOR.  
2. **Task-oriented perturbation and self-imitation learning**: The task-oriented perturbation shares similar intuition with self-imitation learning (https://arxiv.org/abs/1806.05635), where agents benefit from their own past high-rewarding network weight or trajectories. Citing relevant work on self-imitation learning would strengthen the paper. Additionally, a discussion comparing the advantages and disadvantages of task-oriented perturbation versus self-imitation learning would enhance the contribution.  
3. **Expert output architecture (Line 199\)**: The paper mentions that expert i produces output a\_i​, but it is unclear how this output is derived from the latent vector z. Could you provide more details about the architecture of the feedforward network FFN\_i​ and its role in generating the expert output?  
4. **Clarification on MW (Line 215\)**: The paper refers to the "Assembly task from MW," but MW is not defined in the text. Does MW refer to Meta-World? A clear definition would improve readability.

### Soundness
3

### Presentation
3

### Contribution
3
