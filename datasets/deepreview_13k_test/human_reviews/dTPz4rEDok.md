# Offline Hierarchical Reinforcement Learning via Inverse Optimization

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
Hierarchical policies enable strong performance in many sequential decision-making problems, such as those with high-dimensional action spaces, those requiring long-horizon planning, and settings with sparse rewards. 
However, learning hierarchical policies from static offline datasets presents a significant challenge.
Crucially, actions taken by higher-level policies may not be directly observable within hierarchical controllers, and the offline dataset might have been generated using a different policy structure, hindering the use of standard offline learning algorithms.
In this work, we propose \textit{OHIO}: a framework for offline reinforcement learning (RL) of hierarchical policies. 
Our framework leverages knowledge of the policy structure to solve the \textit{inverse problem}, recovering the unobservable high-level actions that likely generated the observed data under our hierarchical policy.
This approach constructs a dataset suitable for off-the-shelf offline training.
We demonstrate our framework on robotic and network optimization problems and show that it substantially outperforms end-to-end RL methods and improves robustness. 
We investigate a variety of instantiations of our framework, both in direct deployment of policies trained offline and when online fine-tuning is performed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors introduce a new offline HRL approach that can recover high level actions given trajectories of state transitions.  To find the most likely high level actions, a new simple maximum likelihood approach is used.  They show their approach is able to solve a series of robotics and network optimization tasks.

### Strengths
- The approach to discovering the high level actions given a set of state transitions is simple.  Select the high level action with the highest likelihood.
- Significant empirical outperformance versus baseslines
- Empirical performance was robust to different controllers and modeling errors
- Applied algorithm to domains with very high dimensional action spaces (i.e., the network optimization problems)

### Weaknesses
The approach does appear to have significant limitations.
1.  The approach assumes access to an approximate model of the transition dynamics.  The authors argue this can be relatively simple to learn because it only requires a single step, but this can be difficult in high-dimensional and stochastic settings.
2.  The approach often assumes a pre-trained low-level controller.

### Questions
1. Can you clarify what the observed state baseline is?  It seems that it is a high-level policy that always selects the next state from a trajectory as the subgoal?  Why was the next state chosen instead of e.g., 10 timesteps later?  Can you provide some intuition on why is performed poorly?
2.  Can you provide some data on the time horizon (i.e., number of primitive actions) to complete each task?

### Soundness
3

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
The paper presents a method for obtaining high-level actions from an offline (state only) dataset, by solving the lower level policy inverse problem. The motivation is very clear: High-level, temporal abstractions and hierarchical decomposition is crucial for solving many complex, long horizon problems, therefore, a method for extracting high-level options from an offline dataset that does NOT contain those high-level actions is crucial. In addition, the paper propose to exploit the extracted high-level actions for performing offline reinforcement learning with the resulting high-level dataset, such that the found high-level policy can parameterize the low-level policy at inference time. The proposed method (OHIO) is evaluated on diverse environments (multiple robotics problems as well as network optimization), and performs favorably in comparison with numerous online and offline RL methods.

### Strengths
Very well written, clearly motivated, thoroughly validated both empirically and analytically.
To the best of my knowledge this work addresses an important gap in the literature, the possibility to learn high-level actions that parameterize arbitrary low-level policies from state-only trajectories (and assuming approximate knowledge about transition dynamics).

### Weaknesses
Not much here to be honest. The only thing that comes to mind is that it was not immediately clear to me how to solve Eq (6) in practice and in the general case, but this becomes very clear with Appendix A.4 and algorithm 2 and 3. Perhaps the content of A.4 could be more integrated into the main method section. 

It seems to me like method mainly deals with the implicit policy case, therefore, I am not sure how much value is being added by discussing the explicit policy case.

### Questions
How much is this method affected by the quality of the approximate transition model? It would be extremely interesting to see how well the method performs when the ground truth transition model is used, compared with a model learned from the offline data (I guess this would only be possible when low-level actions are part of the trajectories). Did one of the experiments somehow access this and I missed it?

### Soundness
3

### Presentation
4

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
This paper presents OHIO, a framework for offline reinforcement learning (RL) using hierarchical policies. The framework uses inverse optimization to recover high-level actions that generated the observed data. The authors perform experiments in robotic manipulation and network optimization environments, and show improvements against end-to-end and hierarchical policies.

### Strengths
1. The paper presents an interesting approach for effectively leveraging the inherent hierarchical structure for downstream learning.

2. The authors show impressive results on roobotic and network optimization environments, with many ablations pertaining the hierarchical structure.

3. It covers good related work section and the limitations of this method are clearly mentioned in the discussion section.

### Weaknesses
1. The main weaknesses in this paper are the experiments. Although the authors mention prior related hierarchical approaches for offline learning, the comparisons with such sophisticated approaches are missing in the experiment section. This makes it hard to judge the efficacy of the method against prior approaches. A more detailed comparison with such baselines on complex multi-level reasoning tasks is thus necessary.

2. Further, Algorithm 1 provides minimal information for the hierarchical formulation, and can be significantly improved by adding appropriate details of the training procedure. Extensive details on how the hierarchical levels interact with each other during training is also missing. The paper would benefit by adding pseudocode for how the high-level and low-level policies are trained and interact, with details on how the inverse optimization is integrated into the training loop.

3. Minor: Typo in Line 201.

### Questions
Can you provide comparisons of OHIO with prior hierarchical approaches that leverage offline RL, e.g OPAL: Offline Primitive Discovery for Accelerating Offline Reinforcement Learning [1] and approaches that leverage expert demonstrations like Relay Policy learning [2]. 

Can you discuss how would the method compare against prior methods that leverage expert demonstrations for learning the inherent hierarchical structure, e.g. Relay Policy learning [2].

[1]. OPAL: Offline Primitive Discovery for Accelerating Offline Reinforcement Learning (Anurag Ajay, Aviral Kumar, Pulkit Agrawal, Sergey Levine, Ofir Nachum)
[2]. Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning (Abhishek Gupta, Vikash Kumar, Corey Lynch, Sergey Levine, Karol Hausman)

### Soundness
3

### Presentation
3

### Contribution
3
