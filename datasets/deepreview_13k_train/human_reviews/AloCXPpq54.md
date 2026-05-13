# Sequential Stochastic Combinatorial Optimization Using Hierarchal Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Reinforcement learning (RL) has emerged as a promising tool for combinatorial optimization (CO) problems due to its ability to learn fast, effective, and generalizable solutions. 
Nonetheless, existing works mostly focus on one-shot deterministic CO, while sequential stochastic CO (SSCO) has rarely been studied despite its broad applications such as adaptive influence maximization (IM) and infectious disease intervention. 
In this paper, we study the SSCO problem where we first decide the budget (e.g., number of seed nodes in adaptive IM) allocation for all time steps, and then select a set of nodes for each time step. The few existing studies on SSCO simplify the problems by assuming a uniformly distributed budget allocation over the time horizon, yielding suboptimal solutions. We propose a generic hierarchical RL (HRL) framework called wake-sleep option (WS-option), a two-layer option-based framework that simultaneously decides adaptive budget allocation on the higher layer and node selection on the lower layer. 
WS-option starts with a coherent formulation of the two-layer Markov decision processes (MDPs), capturing the interdependencies between the two layers of decisions. Building on this, WS-option employs several innovative designs to balance the model's training stability and computational efficiency, preventing the vicious cyclic interference issue between the two layers. Empirical results show that WS-option exhibits significantly improved effectiveness and generalizability compared to traditional methods. Moreover, the learned model can be generalized to larger graphs, which significantly reduces the overhead of computational resources.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes WS-option, a hierarchical RL (HRL) algorithm to tackle sequential stochastic combinatorial optimization (SSCO) problems. These type of problems require to allocate a fixed budget over multiple timesteps, and solve the problem over these timesteps under allocation constraint. WS-option defines a high-level policy that allocates the budget, and a low-level policy that solves the underlying problem (selecting a combination of nodes of a graph in this case). The algorithm is experimentally validated on 2 problem instances.

### Strengths
There are many ways to combine RL with combinatorial optimization, but it seems particularly well-suited in this case, as RL naturally handles the stochastic and sequential nature of SSCO. I believe the RL-based approach envisioned by the authors has high potential. It also seems to adapt well to different problem-size instances, which is not necessarily the case for RL-based methods for combinatorial optimization.

### Weaknesses
Nevertheless, I believe that it is insufficient in its current form for the following main reasons:

1. Design choices lack proper justification

     a. The use of HRL here introduces 2 different agents, which introduces nonstationarity due to multiple policies interacting with each other. However, it seems here that a single policy with 2 different action-spaces -- one for the budget allocation, another one for the node selection -- (or one action-space with an action-mask to select only valid actions) could mitigate this issue. The importance of HRL is unclear. Specifically, the authors do not provide a clear explanation of why a single agent with a more complex action space would not be sufficient. The added complexity of HRL should be justified by demonstrating that it offers a clear advantage over simpler alternatives.

    b. The lower-level MDP includes an option that can either be 0 or 1, which defines if the lower-level policy can continue to select nodes. From my understanding, the state-space does not include the allocated budget defined by the higher-level policy.  But this information should be crucial for the lower-level policy to choose which nodes to select. Now, at each timestep, the lower-level policy does not know if it will be able to continue selecting a node at the next timestep or not. Why resort to an "intermediate" option with 0 or 1, instead of allocating the $o_t^I$ in the state? The absence of the allocated budget in the lower-level state space is a critical flaw, as it prevents the low-level policy from making informed decisions based on the available resources. This design choice limits the potential for effective planning and optimization at the lower level.

    c. The first half of training does not use the higher level policy to stabilize the training of the low-level policy. Are there any preliminary experiments that justify the choice of 1/2 of the training time? How dependent is this on the problem? The lack of justification for this specific training split is concerning. It is unclear why the low-level policy requires such a long period of isolated training, and how this choice affects the overall performance and convergence of the algorithm. The authors should provide empirical evidence to support this design choice.

    d. The Route Planning problem (Appendix E) updates the profits by sampling U(-0.05, 0.05). What is the reason for this choice? Also, sampling from U(-0.05, 0.05) results in 0 in expectation. Wouldn't this affect the marginal reward? What are the consequences on the sequentiality of the problem (i.e., how much does this change compared to solving everything in one shot)? The use of a uniform distribution centered around zero for profit updates is questionable. The authors should explain how this choice impacts the problem's sequential nature and whether it introduces any biases or limitations in the evaluation.

    e. The results do not show the standard-deviation, resorting instead to two-sample t-tests. Why? There is no clear justification as to why the standard-deviation is left out.
 
2. Experimental baselines are non-adaptive

    a. I understand that, since the authors are the first to propose an adaptive budget allocation for SSCO problems, they compare it with some fixed allocation strategies (average, static, normal). But there are no RL baselines, making it hard to assess the added value of the proposed algorithm. A standard RL baseline would also help understanding the need for HRL (e.g., using 2 action spaces as mentioned in 1b).

    b. Even though the baselines are non-adaptive, they are different for AIM and for RP. I fail to understand why, and why the average/normal/static high-level policies could not be used for RP.

### Questions
Additional questions:

 1. In table 1, the performance of WS-option seems to be close to the "score" baseline  (for static and average). Are there any insights for this?
 2. It is unclear to me how the simulations are performed. Is it executing the greedy policy 10 times from the current state?
 3. Why are the WS-option scores in table 3 not the same as in table 1? Shouldn't they be the same, since they use the same high-level/low-level policy combination?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel hierarchical reinforcement learning (HRL) framework, WS-option, which addresses the sequential stochastic combinatorial optimization (SSCO) problem. This framework is innovative as it combines budget allocation and node selection in a two-layer option-based structure, which is a creative approach not commonly seen in the prior works.

### Strengths
1.The authors have formulated a generic class of SSCO problems, which is an original contribution to the field. This formulation allows for a more structured approach to solving a broad range of combinatorial optimization problems with stochastic and sequential elements.
2.The paper presents a rigorous methodology, with a clear definition of the Markov decision processes (MDPs) for both layers of the HRL framework. The authors have thoughtfully designed the MDPs to capture the interdependencies between the layers, which is crucial for the model's performance.
3.The paper includes a theoretical analysis of the algorithm's convergence, which is a strong point. The theorems provided offer a solid foundation and justify the effectiveness of the proposed approach.

### Weaknesses
1.The paper primarily uses synthetic datasets for experiments, which might not fully capture the complexities of real-world scenarios. Including datasets from diverse real-world applications could strengthen the validity of the results.
2.The paper primarily uses synthetic datasets for experiments, which might not fully capture the complexities of real-world scenarios. Including datasets from diverse real-world applications could strengthen the validity of the results.
3.The paper notes that each new problem may require a new graph embedding technique, which adds complexity to the framework's implementation. Further exploration into developing model-agnostic or more universally applicable graph embedding techniques could enhance the framework's usability across different domains.

### Questions
1.Will the WS-option framework's performance vary significantly when applied to real-world datasets compared to synthetic ones? Could the authors share any insights or preliminary results if this framework has been tested on real-world data?
2.How does the WS-option framework scale in terms of computational resources and time when applied to extremely large problem instances, such as graphs with millions of nodes?
3.Are there any plans to explore more universal graph embedding techniques that could be applicable across different SSCO problems without the need for customization?
4.Could the authors provide more details on the computational complexity of the WS-option framework, especially when compared to existing methods in the literature?
5.Are there any plans to conduct ablation studies to isolate the impact of the wake-sleep training procedure and layer-wise learning method selection on the overall performance?
6.Will increasing the number of trials and providing confidence intervals for the experimental results further strengthen the conclusions drawn from the data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes WS-option, a hierarchical RL approach for sequential stochastic combinatorial optimisation (SSCO). The setting is formulated as a 2-layer MDP, with the higher level policy - trained using an MC approach - learning the budget allocation, while the lower level policy - trained using Q-learning - deciding on the node selection. The key idea, denoted as wake-sleep (WS), is to avoid the adversarial dynamics and instability during training, by fixing the higher level policy for the first half of the training procedure.  The approach is evaluated in two settings, adaptive influence maximisation and route planning.

### Strengths
The work provides a formulation of sequential stochastic combinatorial optimisation problems as a 2-layer MDP, facilitating the application of RL methods for this setting. It also proposes a hierarchical RL framework, the WS-option, for solving such settings.

### Weaknesses
While the work has some merits in terms of problem formulation under the HRL framework, I argue it lacks a sufficient algorithmic contribution, a comprehensive evaluation and remains generic in many of the implementation details and experiments. I provide below more details and raise also questions that would allow a better comprehension of the work. 

The provided details are insufficient to understand and reproduce the work. As far as I understand, Double DQN is used for both policies, but the higher level uses an MC update method, with an action-in network, trained with offline trajectory data gathered by the average budget fixed policy. Providing the complete neural architecture details, number of layers and sizes would improve this issue. Also please see Q3.

I am not sure the convergence analysis for the tabular case is complete and correct, since it does not discuss the dependency between the Q-value of the two layers in terms of how the reward is defined. Eq. 4 claims consistency between layers for the reward definition, but this is not further discussed or supported. See Q2 for further questions on the reward definition. Furthermore,  lines 316-317 state that the Q-functions of the layers are independent, but as detailed in the proof of Theorem 1, this is not the case. 

For the experiments, it is not clear in the AIM case, which settings from [1] are used and how the results compare to the ones in the referenced work. I also argue that the baseline selection is weak, only looking at fixed or heuristic based methods. Similar remark stands for the RP case, with no details or references provided for the GA approach. See Q4. 

[1] Guangmo Tong, Ruiqi Wang, Zheng Dong, and Xiang Li. Time-constrained adaptive influence maximization. IEEE Transactions on Computational Social Systems, 8(1):33–44, 2020.

Minor remarks:
- I advise to avoid using abbreviations without introduction (e.g., WS, MC, TD lines 88-96, HER line 150)
- typos: adpative (line 219), MD (line 365)

### Questions
Q1. The problem formulation proposes to learn a higher level policy for the budget allocation and a lower level policy for the node selection. I failed to understand, given the simplification of the option from the actual budget to a binary value, how the option termination is taking place. Or in other words, how is the connection between the budget and sequence of selected nodes being made in the activation/propagation process, especially since in the lower level the nodes are deterministically activated.

Q2. Secondly, I was also not able to properly grasp the marginal reward calculation (Eq. 4). Could you please provide additional details on the simulation averaging and scaling procedure and its importance on the training stability. Also, how does this definition ensure consistency between the MDPs?

Q3. Could you provide more details and a reference for the action-in architecture and its role in generalisation?

Q4. Could you provide a motivation for the baseline selection and also explain how the results compare to Tong et al. [1].

### Soundness
2

### Presentation
2

### Contribution
2
