# Solving Homogeneous and Heterogeneous Cooperative Tasks with Greedy Sequential Execution

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Cooperative multi-agent reinforcement learning (MARL) is extensively used for solving complex cooperative tasks, and value decomposition methods are a prevalent approach for this domain. However, these methods have not been successful in addressing both homogeneous and heterogeneous tasks simultaneously which is a crucial aspect for the practical application of cooperative agents. 
On one hand, value decomposition methods demonstrate superior performance in homogeneous tasks. Nevertheless, they tend to produce agents with similar policies, which is unsuitable for heterogeneous tasks. On the other hand, solutions based on personalized observation or assigned roles are well-suited for heterogeneous tasks. However, they often lead to a trade-off situation where the agent's performance in homogeneous scenarios is negatively affected due to the aggregation of distinct policies. An alternative approach is to adopt sequential execution policies, which offer a flexible form for learning both types of tasks. However, learning sequential execution policies poses challenges in terms of credit assignment, and the limited information about subsequently executed agents can lead to sub-optimal solutions, which is known as the relative over-generalization problem. To tackle these issues, this paper proposes Greedy Sequential Execution (GSE) as a solution to learn the optimal policy that covers both scenarios. In the proposed GSE framework, we introduce an individual utility function into the framework of value decomposition to consider the complex interactions between agents. 
This function is capable of representing both the homogeneous and heterogeneous optimal policies. Furthermore, we utilize greedy marginal contribution calculated by the utility function as the credit value of the sequential execution policy to address the credit assignment and relative over-generalization problem. We evaluated GSE in both homogeneous and heterogeneous scenarios. The results demonstrate that GSE achieves significant improvement in performance across multiple domains, especially in scenarios involving both homogeneous and heterogeneous tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a general framework for solving both homogeneous and heterogeneous cooperative tasks, which they call Greedy Sequential Execution (GSE). The key idea behind GSE is to sequentially execute the actions of each agent, while taking into account the dependencies between agents measured by greedy marginal contribution.

### Strengths
1. The analysis in Sec 3.1 is valuable for readers to gain a deeper understanding of the performance of different policies in homogeneous and heterogeneous scenarios.

### Weaknesses
The authors claim that existing solutions have not been successful in **addressing both homogeneous and heterogeneous** scenarios simultaneously, and thus GSE is the first to propose for both scenarios, whose key idea is integrating **sequential execution** and **value decomposition** framework for better **credit assignment** and **cooperation**. However, [1] was published in 2022, which also proposed a general framework based on **sequential execution** for **cooperative games** with **both homogeneous and heterogeneous** agents, and leveraged **advantage value decomposition** for **credit assignment**.

There are too many overlaps in key ideas between these two works, while the main difference seems to be [1] implements these ideas with PPO and sequence model, i.e. transformer, and GSE implements these ideas in a QMIX-like pattern.

However, I have not found any comparison, discussion, or citation to [1] in this paper, which should be compared thoroughly, or the contributions might be significantly weakened.

### Questions
I have no further question.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a unified framework for learning policies for multiple agents where there are homogeneous and heterogeneous tasks, with the goal of addressing limitations of current methods that work with either homogeneous or heterogeneous tasks. Specifically, the paper proposes greedy sequential execution, with value decomposition including a utility that encodes also the interactions between agents and credit assignment calculated as marginal contribution of Shapley values. Simulation experiments considering different types of tasks are performed and results include comparison with other methods.

### Strengths
- the paper addresses an open problem in MARL, where a general framework able to learn optimal policies for both homogeneous and heterogeneous tasks is still not fully present.

- the paper presents a technically sound method, with the augmented utility, sampled considering the joint actions of other agents who might cooperate, and with the greedy marginal contribution 

- the paper includes a fairly comprehensive evaluation of the proposed method and compares with a good number of state-of-the-art approaches, with corresponding insights from the results, as well as ablation studies.

- the paper has a structure that overall clearly show the gap, with specific examples, and motivates the proposed approach.

### Weaknesses
 - a trend that should be discussed more in detail is in Overcooked, where there is a large standard deviation for both Easy and Medium, with Easy having a decreasing return past 900 episodes. It seems that it didn't converge.

A few minor presentation comments: 
- Section V already introduces comparison methods that are presented in Section VI. It is better instead to introduce the comparison methods in Section V so that the reader doesn't have to guess what methods are they.
- it is worth including graphically the map for the overcooked environment.
- the references, when the authors name are not used in the sentence should be all in parentheses, e.g., " experiences Sunehag et al. (2017); Rashid et al. (2018)." -> "experiences (Sunehag et al., 2017); (Rashid et al., 2018)."
- please ensure to include the correct venue for papers, instead of just including the arxiv version, e.g., the MAVEN paper was published in NeurIPS 2019.

### Questions
Please comment on the trends of overcooked as mentioned in the "Weaknesses" box.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a way of handling cooperative tasks with multi-agents when the tasks are not all homogeneous.
The approach proposed uses sequential execution policies, proposing the Greedy Sequential Execution (GSE), which learns the optimal policy for both cases (homogeneous and heterogeneous tasks). The GSE is evaluated empirically in multiple domains. The GSE  uses a value decomposition method that works for both homogeneous and heterogeneous tasks, and enables the agents to learn utilities that take into account the interactions with other agents. They also propose a credit assignment method that computes the marginal contributions of each agent. The marginal contribution avoids over-generalization, since it represents the optimal value of an action instead of the average value. A couple of theorems are proved in an appendix (not attached to the paper). The experiments use homogeneous scenarios, heterogeneous scenarios, and mixed scenarios. 
Multiple appendices are mentioned but they are not attached to the paper and are not accessible.

### Strengths
The paper is very well written and easy to follow. The work presented addresses a known problem (over-generalization) that takes place when combining homogeneous and heterogeneous tasks and expands the applicability of agent-based approaches to situations where some tasks are homogeneous and some are heterogeneous. Having to deal with a mix of the two types of tasks might not be too common, but when mixes of tasks are used, the approach proposed here, even if greedy, becomes quite useful.

### Weaknesses
The paper is more appropriate for a journal than for a conference. The numerous appendices are not included in it for space reasons, but are important to understand the method more in depth.
Figure 2 with the architecture is hard to read and not well explained. The description of the Monte Carlo method used to estimate the optimal cooperative actions is too vague. The paper mentions that the method selects actions to maximize the greedy marginal contribution, but it does not specify how many actions are selected, or how this number affects the results. In the Overcooked scenario, the paper mentions that the size of the map affects the complexity, but there is no indication of how large the maps are. The paper also does not explore the effect of having a larger number of agents in the Overcooked scenario, which could reveal limitations of the proposed approach.

### Questions
1. The use of Monte Carlo method to estimate the optimal cooperative actions with previous agents to maximize the greedy marginal contribution is mentioned with no other details. How is the number of actions selected?
2. In the Overcooked scenario, I understand why the size of the map affects the complexity, but there is no indication of how large the maps are. I believe the number of agents is fixed to two. Have you tried a larger number of agents?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors incorporate sequential execution into a value-decomposition-based MARL algorithm, which can thus be applied to both homogeneous and heterogeneous tasks, while maintaining effective credit assignment. 
Two approximations are involved: 1) using greedy marginal contribution as the assigned credit for each individual, and 2) using greedy actions (augmented by Monte Carlo samples) as the optimal actions taken by subsequent agents.
The experiments show the efficacy of this approach, demonstrating its ability to adapt to dynamically changing partners within homogeneous, heterogeneous, and mixing scenarios.

### Strengths
- Originality. The proposed method addresses common problems in MARL algorithms, such as the relative overgeneralization and credit assignment, at the same time. This enhancement expands the scope of potential applications of value-decomposition-based MARL algorithms. 
- Clarity. The paper is basically clear and easy to follow.

### Weaknesses
 - The algorithm is tested exclusively on specially designed tasks. There are no additional experiments conducted on common benchmarks.
- The ablation study section fails to provide an in-depth discussion of the functions of the key components in the algorithm. I would appreciate a more detailed description of the ablated algorithms and a clearer explanation of the results.

### Questions
- To generate a joint action $u$, each agent must calculate its action $a$ sequentially, which prevents parallel processing. Therefore, with each agent requiring $t$ time to produce its action, a single environment step requires $n*t$ units of time for $n$ agents. Compared with baseline algorithms like QMIX, does GSE require more wall-clock time for training and evaluation? If so, could you provide a rough estimate of the additional time required?
- During training, is the execution sequence of all agents fixed, or do you shuffle the sequence?
- What does 'training with a larger scale of agents' mean in Section 6.3 & Figure 6?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
