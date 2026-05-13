# Reinforcement learning with combinatorial actions for coupled restless bandits

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Reinforcement learning (RL) has increasingly been applied to solve real-world planning problems, with progress in handling large state spaces and time horizons. However, a key bottleneck in many domains is that RL methods cannot accommodate large, combinatorially structured action spaces. In such settings, even representing the set of feasible actions at a single step may require a complex discrete optimization formulation. We leverage recent advances in embedding trained neural networks into optimization problems to propose SEQUOIA, an RL algorithm that directly optimizes for long-term reward over the feasible action space. Our approach embeds a Q-network into a mixed-integer program to select a combinatorial action in each timestep. Here, we focus on planning over restless bandits, a class of planning problems which capture many real-world examples of sequential decision making. We introduce coRMAB, a broader class of restless bandits with combinatorial actions that cannot be decoupled across the arms of the restless bandit, requiring direct solving over the joint, exponentially large action space. We empirically validate SEQUOIA on four novel restless bandit problems with combinatorial constraints: multiple interventions, path constraints, bipartite matching, and capacity constraints. Our approach significantly outperforms existing methods—which cannot address sequential planning and combinatorial selection simultaneously—by an average of 28.3% on these difficult instances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the CoRMAB problem, in which there are complex combinatorial arm structures to be learned. Such complexity often arises in many real-world applications such as public health etc. The problem, as far as I can see, is kind of like an intermediate area between traditional bandits where each arm is independent, and that of the more general Markov Decision process where any transition might happen. This paper, however, focuses on the more tractable scenario where some sort of information is known beforehand about the arm dependence structure. In particular, the paper considers four specific scenarios, including multiple interventions, bipartite matching, capacity constrained, and path planning. The paper proposed SEQUOIA, which applies Q-network with mixed-integer linear programming to solve the problem. Experiments demonstrate the effectiveness and efficiency of the proposed algorithm.

### Strengths
The paper studied a very novel and niche problem that is more tractable than RL but also more practically relevant in real-world bandit applications. I think it's important to have deeper investigations on such problems to directly applying SOTA RL algorithms. One novelty is that the paper combines RL with MILP to solve the problem more effectively.

### Weaknesses
Although the paper studied very interesting bandit problems, but the problem is solved via RL plus MILP. I was curious why not directly apply SOTA RL algorithms? How does that compare to the SEQUOIA proposed in this paper? I think one weakness of the paper is that it didn't compare with more advanced baselines like certain RL algorithms.

Another major weakness of the paper is that it doesn't have theoretical analysis on the algorithm performance, which is very critical for bandit papers. I would hope the authors provide regret bounds for each of the four cases studied in the paper.

### Questions
How does the algorithm in this paper compare to SOTA RL algorithms?

How to derive theoretical analysis?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel reinforcement learning framework for a challenging setting known as combinatorial restless multi-armed bandits (CoRMAB). In these problems, the vast combinatorial action space presents a key bottleneck, especially for real-world applications like public health. The authors address this by proposing SEQUOIA, a method that combines a Q-network with mixed-integer linear programming (MILP) solvers. Four distinct constraint types (such as capacity and matching constraints) are applied to CoRMAB instances to explore the method's performance. Experimental results show that SEQUOIA significantly outperforms existing baselines across these settings.

### Strengths
- The paper highlights meaningful applications, particularly in public health, where combinatorial decision-making is crucial. By focusing on real-world-inspired constraints, the paper emphasizes the practical utility of SEQUOIA.
- The experimental results suggest that SEQUOIA has a strong advantage over other methods, particularly in scenarios that require both sequential planning and combinatorial action selection. This shows potential for the method to be impactful in complex decision-making tasks.

### Weaknesses
 - The four specific CoRMAB instantiations appear somewhat interdependent. For instance, the first instance involving multiple interventions seems to implicitly contain elements of the second (path constraints) and third (capacity constraints). This overlap could obscure the unique contributions of each instance, and the presentation of these distinctions would benefit from clarification. Additionally, a more precise formulation of the optimization goals and constraints in each problem setting could strengthen the paper. The description of the multiple interventions setting, for example, lacks detail on how the cumulative impact is modeled, specifically whether it is a linear or non-linear accumulation of effects, and how this might interact with the reward function. Similarly, the path constraints setting could benefit from a clearer explanation of how the path is represented and how the algorithm ensures path feasibility. The capacity constraints setting, while seemingly straightforward, could be more rigorously defined in terms of how the budget $b_j$ is determined and whether it is static or dynamic.
- Although the SEQUOIA framework is innovative in combining Q-networks with MILP, the method lacks theoretical guarantees, which may reduce its general appeal in theoretical RL circles. The paper leans toward practical applications without rigorously addressing theoretical underpinnings. Given that the CoRMAB problems are motivated by real-world scenarios, it would be beneficial for the authors to demonstrate how SEQUOIA could operate on actual datasets or real-world instances. The absence of theoretical convergence proofs or bounds on the suboptimality of the learned policy makes it difficult to assess the robustness of the method. Furthermore, the paper does not discuss the sensitivity of the method to hyperparameter choices, which is crucial for practical deployment. A sensitivity analysis would be valuable to understand the limitations of the method and to provide guidance on parameter tuning.
- The method's training demands significant computational resources, as evidenced by Table 3, where training times extend to hours. For online applications, this can be a prohibitive factor. The paper would benefit from a discussion on optimizing computational efficiency or alternative approaches to reduce overhead. The paper does not explore the potential for parallelizing the training process, which could significantly reduce the wall-clock time. Also, the memory footprint of the method is not discussed, which is an important consideration for large-scale problems. A detailed analysis of the computational bottlenecks would be beneficial to identify areas for optimization.

### Questions
- Since SEQUOIA’s primary application appears to be in public health, there are concerns about performance during the initial training phase. If the network’s early-stage predictions are suboptimal, this could lead to unacceptable decisions in real-world use. How do the authors envision mitigating this issue in practice, particularly in high-stakes domains like public health where early errors could have critical impacts?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a RL problem setting where the action space is combinatorial and discrete, I.e. in which actions are coupled with combinatorial constraints. This work uses the formalism of restless multi-armed bandits to tackle the problem and consider the setting where arms are coupled which leads to a large action space using 4 different examples: multiple interventions, path constraints, bipartite matching and capacity constraints. The proposed approach relies on embedding a Q-network into a mixed integer program fro combinatorial action selection at each time step. The proposed RL algorithm SEQUOIA optimizes for long-term reward over the action space allows to perform sequential planning for a combinatorial action space setting. The performance of the algorithm shows empirical improvement over existing approaches.

### Strengths
- The 4 example settings provided are compelling for motivating the work. I find the public healthcare example interesting and it is nicely used as a running example. I believe these sequential planning problems are important problems to solve in practice. 
- Writing is clear overall and the presentation with the figures is nice.

### Weaknesses
 - The mathematical formulation of the problem is a bit confusing and could be more rigorous: 
(a) Is it an infinite horizon problem (since you seem to be using discounting)? 
(b) l. 99: you mention that your approach enables per-timestep combinatorial action spaces. Where does this flexibility show up in the problem formulation in sec. 2.2. The set C is a fixed combinatorial action vector set. I do not see any time dependence taken into account in the formulation, C also seems to be fixed in Algorithm 1. Usually in RL, action sets are fixed. In your setting, it might be useful to consider time varying ones as the actions that might be available might change because of the coupling of the actions, for instance reducing over times due to the previous actions chosen that limit the remaining possible choices. 

- Transition dynamics and rewards are assumed to be known a priori (l. 104). This might be quite limiting regarding the health care motivating example. 

- About the comparison to standard DQN (Fig. 2 + l. 243-247): in standard DQN the output size of NN scales with the size of the action space. In your approach, now the input size has to be of the size of the action space (which is exponentially large) to be able to encode any action input from the large combinatorial space you consider. Any comment about this? Why is it more tractable as for the main scaling challenge you want to overcome? 

- As discussed in l. 319-323: having to solve an MILP for each sample and for each time step seems extremely expensive. 

- Q learning has even been used for continuous actions spaces via appropriate discretization of the action space.  I believe stronger and more convincing arguments have to be made here to support the claims of the paper since this is a crucial point given the motivation of the paper. Could you please elaborate and clarify better what makes your approach scalable compared to prior existing algorithms applied to your combinatorial action space setting? See follow-up question below. 

- As discussed in the paper, the idea of embedding a neural network into a mixed-integer problem is not new. Could you elaborate more on the technical challenges faced when following this approach and why does it address the scalability challenge in your problem?

Minor: l. 1028: seems empty for ‘Multiple interventions’, any missing description here?

### Questions
**Main questions:**
- How crucial is the assumption of known dynamics and rewards for your approach?  
- Running time: Table 3 in the appendix shows the total running time depending on the number of arms. What about the number of workers? Is it fixed in this table? 
- Why is step 9 involving an argmax over actions more tractable than given the combinatorial nature of the action space? This is an important point for scalability that is not very clear to me from the presentation. 
- What’s the size of the combinatorial action set in the experiments for each of the 4 examples? Why is it prohibitive for existing RL methods? 
- l. 345 ‘We introduce diversity into the sampled actions with additional random perturbations’. It seems that there is no way to bypass the need to see a sufficient number of diverse actions. I guess this is also an exploration requirement to solve the RL task. If you cannot explore a large number of actions, I guess there is little that can be said about the quality of the obtained policy. 
- Can you further justify the use of DQN? I understand that this is probably the most famous one but since you consider a known transition model, would DDPG make also sense to be tested? 
- Why don’t you compare to the approach you mention in l. 494-498? 


**Minor questions:**
- Why do you need a piecewise linear approximation of the sigmoid link function (l. 181) which is known and can be computed?  
- Any interpretation for including self-loops (l. 196)?

### Soundness
3

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
The work introduces a new class of multi armed bandits problem, coRMAB which generalizes Restless bandits problem where the arm action cannot be decoupled because of the constraint of the problem that is common in real world scenarios. The authors also briefly go through the four scenarios with valid examples and propose an algorithm SEQUOIA based on deep RL algorithm – Q learning & mathematical optimization to optimize long-term reward. The authors also highlight the issue with very large action space and showcase the ability of SEQUOIA to perform on those scenarios with experiments comparing them with some of the other algorithms that can handle this problem.

### Strengths
1.	The problem setting and formulation are interesting. The formulations discussed in this paper is a natural and general extension of restless bandits. Most of the real-world scenarios often fall under one of the four scenarios highlighted by the authors in this work. 

2.	Deep Q learning type algorithms are generally computationally heavy, and it only grows with the action and state space. This work addresses this issue and takes this into account in their problem formulation and algorithm.  

3.	A key challenge in using deep learning within a RL problem or any problem in general is the need for optimizing the network architecture and resource for hyper-parameter tunning and the algorithm seems to work with minimal alterations across domains.

### Weaknesses
1.	The work highlights the empirical results of the proposed algorithm SEQUOIA but it did not have any theoretical guarantees on measures like Regret or convergence bounds. Having them would have greatly benefitted the solidarity of the developed algorithm.

2.	The major results shown in this work is about the experiments and how SEQUOIA, the developed algorithm performs on four scenarios of the problem formulation and competes with some of the other algorithms that can be modified to work on coRMAB, however a detailed experimental design could be carried out to further showcase the benefits and limitations of the proposed algorithm and how they perform in different regimes on different transition dynamics. 

3.	The work also assumes that it is an offline planning setting, i.e., the transition dynamics are known in advanced which can be a limiting factor on many practical settings where the transition dynamics are harder to compute. Most of the real-world setting involves an agent interacting with an environment to understand them.

### Questions
1.	The problem of coRMAB extends the problem of restless MAB to handle actions that cannot be decoupled. If we were to set the no of actions (N) equal to the no. of arms (J)  and using a simple budget constraint where \sum j \in [J] a_j <= B and also making each action only connect to its corres. arm, we end up in restless MAB setting. In that case, How does SEQUOIA handle the Restless bandit problem ?

2.	For the case of standard restless bandit problem, how does SEQUOIA competes with some of the existing algorithm in the space of restless bandit problem like restless-UCB [Reference B], which tends to have a sublinear Regret bound with good empirical performance on real-world data too. ? 

3.	Also, a detailed comparison of the algorithm with other algorithms or approach could help better understand the performance of the developed algorithm. For instance, a comparison of SEQUOIA with other algorithm/ approach on the basis of either Regret/ Normalized Average reward would better help understand the performance gain of the proposed algorithm. ?

4.	The metrics used in this paper is normalized average reward. Given that we know the transition dynamics, does comparison against the optimal best policy performance be a better metrics like Regret ? Or Other convergence guarantees like one shown in this paper [Reference A] be better fitted to potentially quantify the significance of this work ?


5.	Also, solving the large action space problem is computationally hard, however how does the complexity grows if we were to increase the neural network size for a more complex system ?

6.	Also, the SEQUOIA uses the same network architecture across all the four constraint type proposed in the paper, Is it optimal or does tunning the hyper-parameter for each constraint provide better performance ?

7.	How does SEQUOIA’s result compare to existing domain specific solution for the four-constraint type setting discussed. This would better help SEQUOIA solidify its performance gain with better clarity ? 

Reference:
A.	Guojun Xiong, Jian Li, Finite-Time Analysis of Whittle Index based Q-Learning for Restless Multi-Armed Bandits with Neural Network Function Approximation, Advances in Neural Information Processing Systems 36 (NeurIPS 2023) 
B.	Siwei Wang, Longbo Huang, John C. S. Lui, Restless-UCB, an efficient and low-complexity algorithm for online restless bandits, Advances in Neural Information Processing Systems (NeurIPS 2020)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a more general restless bandit model---coRMAB, in which the action space for different arms could also be correlated (e.g., one action can influence multiple arms). In this model, the authors adapt the idea of DQN, and utilize the fact that solving integer programming with a feed-forward neural network programming representation is efficient. They propose the SEQUOIA algorithm, and show that it achieves good performances in experiments.

### Strengths
- The problem setting is well-motivated.

- I quite like the idea that instead of solving the exact combinatorial optimization, we choose to solve the optimization based on our estimation as an approximate approach. 

- From experiments, this idea seems work well.

### Weaknesses
 - There are no real data experiments. For a paper that does not contain too much theories, I believe real data experiments are necessary. 

- There are some parts that are not very clear to me, e.g., 

In Eq. (2), why there is no $s'$ in RHS?

For "Schedule-constrained", "Capacity-constrained", and "Path-constrained", are there any formulation about the transitions?

Why we only consider these four kinds of cdRMAB? I think your algorithm (or solving the MILP) is not restricted to these four settings, right? 

In line 431-432, it is said that "For example the ITERATIVE myopic approach performs on average 14.6% lower than optimal MYOPIC". But I do not see that? In Figure 3(b) and 3(c), they are very close, and in Figure 3(a), it seems that ITER.MYOPIC is higher than MYOPIC?

### Questions
See "Weaknesses" for details.


======After rebuttal=======

Thanks for the reply. I do not have further questions.

### Soundness
3

### Presentation
3

### Contribution
2
