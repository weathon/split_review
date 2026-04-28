# Federated Natural Policy Gradient Methods for Multi-task Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
Federated reinforcement learning (RL) enables collaborative decision making of multiple distributed agents without sharing local data trajectories. In this work, we consider a multi-task setting, in which each agent has its own private reward function corresponding to different tasks, while sharing the same transition kernel of the environment. Focusing on infinite-horizon tabular Markov decision processes, the goal is to learn a globally optimal policy that maximizes the sum of the discounted total rewards of all the agents in a decentralized manner, where each agent only communicates with its neighbors over some prescribed graph topology. 


We develop federated vanilla and entropy-regularized natural policy gradient (NPG) methods under softmax parameterization, where gradient tracking is applied to the global Q-function to mitigate the impact of imperfect information sharing. We establish non-asymptotic global convergence guarantees under exact policy evaluation, which are nearly independent of the size of the state-action space and illuminate the impacts of network size and connectivity. To the best of our knowledge, this is the first time that global convergence is established for federated multi-task RL using policy optimization. Moreover, the convergence behavior of the proposed algorithms is robust against inexactness of policy evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the federated RL problem with multi-task objectives. It develops NPG based algorithms and provides non-asymptotic convergence guarantees under exact policy evaluation.

### Strengths
- The paper is well written. The problem setting and formulation are clearly presented, and the ideas are well explained.

### Weaknesses
 - From the algorithm description, it seems that the agents would need to communicate and share their information with others. This seems to be different from the motivation of using a federated algorithm, where usually agents share parameters with a central entity for aggregation. The paper would benefit from a more concrete example of the proposed scenario to better motivate the use of a decentralized approach. Specifically, the authors should elaborate on the practical scenarios where agents communicate with each other over a network topology, rather than with a central server. A clearer explanation of how the mixing matrix is determined in practice and its impact on the algorithm's performance would also be beneficial.

- The technical results need more explanation. Right now it is quite dry, in the sense that there is not much discussions. Specifically, the authors should provide more intuition behind the convergence rates presented in Theorems 1 and 2. For instance, how do the convergence rates relate to the properties of the underlying Markov Decision Process (MDP) and the chosen policy parameterization? Additionally, a more detailed discussion of the impact of the network topology on the convergence behavior would be valuable. How does the convergence rate change as the network becomes more or less connected? What are the trade-offs between communication cost and convergence speed?

### Questions
- From the algorithm description, it seems that the agents would need to communicate and share their information with others. This seems to be different from the motivation of using a federated algorithm, where usually agents share parameters with a central entity for aggregation. Please elaborate. 
- The technical results need more explanation. Right now it is quite dry, in the sense that there is not much discussions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes federated vanilla and entropy-regularized natural policy gradient methods under softmax parameterization. Some extensibility properties are given or proven, including global convergence and etc. Overall, this paper is well-written, and it has clearly expressed their work and the author's importance.

### Strengths
Complete work with well-designed algorithms and theoretical analysis. The authors have considered a less common but easily thought of issue, i.e., multi-task RL.

### Weaknesses
It is easy to be considered as a combination of multiple existing works with not clearly discussed motivation. The most important issue is the lack of numercial experiments which could prove the efficiency of the proposed algorithms. The proposed theoretical results are overclaimed a bit, for the reason that there should be some assumpotions on the the structural form of the policy $pi$, like (107), in order to obtain the global covergence.

### Questions
1. More experiments to show the efficiency of the proposed algorithms;
2. The convergence results should be improved, or the contributions should be properly clarified;
3. More comparison with distributed optimization methods should be discussed, especially some convergence results. For the reason that maybe there are already some global convergence results for general distributed optimization problems (with multi-task RL as a special case).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study employs the federated NPG method to address a multi-task reinforcement learning challenge. In their setup, there is reward heterogeneity among various agents, though they share identical transition kernels. Two algorithms, namely the vanilla and entropy-regularized FedNPG, are introduced to tackle the decentralized FRL issue within a graph topology. Additionally, the authors offer theoretical assurances for these algorithms.

### Strengths
1.The paper is well-written and clearly presented
2. The authors provide a clear comparison of their findings with existing results.
3. The analyses are solid.

### Weaknesses
 * The study lacks simulation results that would validate the efficacy of the presented algorithms.

* The framework presented is relatively simplistic, being limited to the tabular scenario with deterministic gradients. There's no consideration for function approximation or the presence of noise. This significantly limits the practical applicability of the proposed algorithms, as real-world RL problems often involve high-dimensional state and action spaces and stochastic transitions.

* A notable omission is the lack of multiple local updates in the algorithms, which are the key features in Federated Learning (FL). Heterogeneity only exists  when there are more than one local updates. Consequently, the authors did not examine the influence of heterogeneity between agents, since their algorithms do not incorporate the multiple local update steps. The absence of local updates also means that the algorithms do not fully capture the communication efficiency benefits typically associated with federated learning.

### Questions
* How would the algorithms behave if the transition kernels differ between agents?

* Regarding agents' motivation to participate in the federation, prior studies [1][2][3][4] have explored the incentives in terms of linear or sublinear speedup. Do the proposed algorithms match this expected speedup in convergence rate as the number of agents increases?

[1] Fan, Xiaofeng, Yining Ma, Zhongxiang Dai, Wei Jing, Cheston Tan, and Bryan Kian Hsiang Low. "Fault-tolerant federated reinforcement learning with theoretical guarantee." Advances in Neural Information Processing Systems 34 (2021): 1007-1021.

[2] Khodadadian, Sajad, Pranay Sharma, Gauri Joshi, and Siva Theja Maguluri. "Federated reinforcement learning: Linear speedup under markovian sampling." In International Conference on Machine Learning, pp. 10997-11057. PMLR, 2022.

[3] Wang, Han, Aritra Mitra, Hamed Hassani, George J. Pappas, and James Anderson. "Federated temporal difference learning with linear function approximation under environmental heterogeneity." arXiv preprint arXiv:2302.02212 (2023).

[4] Shen, Han, Kaiqing Zhang, Mingyi Hong, and Tianyi Chen. "Towards Understanding Asynchronous Advantage Actor-critic: Convergence and Linear Speedup." IEEE Transactions on Signal Processing (2023).

### Soundness
3 good

### Presentation
3 good

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
This paper analyzes the decentralized federated natural policy gradient method for multi-tasks in the infinite-horizon tabular setting. Precisely, all agents have the same transaction matrix but different rewards. Agents communicate with neighbors in a prescribed graph topology. Both federated vanilla and entropy-regularized NPG methods are analyzed with global convergence rates. With exact policy evaluation, non-asymptotic global convergence is guaranteed. With imperfect policy evaluation, convergence rates remain the same when the infinite norms of approximation errors are small.

### Strengths
1.	To the best of my knowledge, this is the first work on decentralized FedNPG with convergence analysis.
2.	Without trajectory transmission, the results show that the convergence rates do not show down a lot.
3.	With function approximation, the communication complexity of vanilla FedNPG would be very high. But the natural policy gradient update in the tabular setting has a simple form. It is wise to choose this as no higher-order matrix is involved.

### Weaknesses
1. Only the tabular setting is studied. The action and state space are discrete and finite.
2. It is good enough to give convergence performances for previously proposed algorithms (or with minor changes). However, the decentralized FedNPG algorithm is quite new. Some simulations are needed to verify the proposed algorithms.
3. In practice, it is very hard to be synchronous in each iteration with fully distributed settings. Especially, each agent randomly (categorical distribution) selects one agent to communicate.
4. Should the mixing matrix $\mathbf{W}$ be ergodic? I cannot find a related assumption or discussion, which confuses me with the statement “illuminate the impacts of network size and connectivity”. Can each agent compute independently and do a one-shot average? There is a connectivity rule in (Nedic & Ozdaglar, 2009), but not here.
5. As the local update is a key point in federated learning, is it possible to compute locally for several iterations without communication?
6. (Clarification) Are the reward functions deterministic?
7. (Motivation) I personally like this topic, and would like to know more about the motivation. As each agent has its own reward function, why don’t they simply use the local policies instead of the global policy? Does it make sense to force them to use the same policy?

### Questions
1.	Should the mixing matrix $\mathbf{W}$ be ergodic? I cannot find a related assumption or discussion, which confuses me with the statement “illuminate the impacts of network size and connectivity”. Can each agent compute independently and do a one-shot average? There is a connectivity rule in (Nedic & Ozdaglar, 2009), but not here.
2.	As the local update is a key point in federated learning, is it possible to compute locally for several iterations without communication?
3.	Is it possible to show some simulation results?
4.	(Clarification) Are the reward functions deterministic?
5.	(Motivation) I personally like this topic, and would like to know more about the motivation. As each agent has its own reward function, why don’t they simply use the local policies instead of the global policy? Does it make sense to force them to use the same policy?

This work is generally good. I promise to raise the score if questions 1 - 3 are fairly (or partially) addressed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
