# Policy Consistency in Multi-Agent Reinforcement Learning with Mixed Reward

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
The sparsity of team rewards poses a significant challenge that hinders the effective learning of optimal team policies in cooperative multi-agent reinforcement learning. One common approach to mitigate this issue involves augmenting sparse rewards with individual rewards to guide policy training. However, a significant drawback of such approaches is that modifying the reward function can potentially alter the optimal policy. To tackle this challenge, we propose a novel multi-agent policy optimization approach that ensures consistency between the mixed policy (learned from a combination of individual and team rewards) and the team policy (based solely on team rewards), through a new policy consistency constraint that aligns the returns of both policies in policy optimization model. We further develop an iterated policy optimization procedure to solve the formulated problem, deriving an approximate optimization objective for each iteration of the mixed and team policies. Experimental evaluation conducted in the StarCraft II Multi-Agent Challenge Environment (SMAC), Multi-Agent Particle Environment (MPE), and Google Research Football (GRF) environments demonstrate that our proposed approach effectively addresses the policy inconsistency problem, ${\it i.e.}$, it consistently outperforms strong baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work addresses the issue of suboptimal policy deviation when simultaneously utilizing individual rewards and team rewards in multi-agent reinforcement learning (MARL) training. It introduces a consistency constraint and designs an iterative framework for solving the Lagrangian dual problem to derive the optimal policy. Extensive experiments were conducted on several MARL tasks.

### Strengths
* The new introduced consistency policy constraint is somehow innovative in addressing the problem targeted by this work and comes with solid theoretical guarantees.
* Extensive experiments were conducted to demonstrate the effectiveness of the proposed method CMT.

### Weaknesses
 * The presentation of the paper can be improved, especially in the section Introduction and Related Work. Some parts are overly verbose and lack clarity. I hope the authors to further refine their expressions for conciseness and clarity.
* Including the algorithm in the main paper would facilitate readers' understanding of the algorithm.
* Equation (7) in the main text lacks a definition for $U$. While it is defined in the appendix, it would be better to provide its meaning upon its first appearance in the main text.
* line 216-217, "However, with the help of individual rewards, ... even surpasses $\pi_{E}^{i, *}$ ". There are some issues with the phrasing here. The use of 'performance' seems to refer to $J_{E+i}$, but it could also be interpreted as $J_{E}$, which does not satisfy the condition for 'surpasses $\pi_{E}^{i, *}$.' I recommend the authors revising this for clarity.

### Questions
* Equation (7) in the main text lacks a definition for $U$. While it is defined in the appendix, it would be better to provide its meaning upon its first appearance in the main text.
* line 216-217, "However, with the help of individual rewards, ... even surpasses $\pi_{E}^{i, *}$". There are some issues with the phrasing here. The use of 'performance' seems to refer to $J_{E+i}$, but it could also be interpreted as $J_{E}$, which does not satisfy the condition for 'surpasses $\pi_{E}^{i, *}$.' I recommend the authors revising this for clarity.

### Soundness
3

### Presentation
2

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
This paper addresses the challenge of deviation in optimal policies in MARL due to the introduction of individual rewards. A multi-agent
constrained policy optimization procedure (CMT), which maximizes the cumulative rewards while ensuring
the consistency between the team policy and the mixed policy, is proposed. Better results are achieved against strong baselines.

### Strengths
- The paper is well written and well organized.
- Experimental studies are good.

### Weaknesses
 - The main weakness, in my opinion, lies in the gap between the actual implementation of CMT and its aim. The paper claims that a significant drawback of previous methods is that modifying the reward function can potentially alter the optimal policy. I was expecting this paper can ensure that the optimization procedure of CMT leads to the optimial team policy. It turns out a number of approximations are made in CMT, and I am not convinded that CMT improves over previous methods in terms of fixing the drawback.

 - lack of theoretical results that ensure the optimization procedure of CMT leads to the optimial team policy.

### Questions
- Assumption 1. If $\pi_{E+i}^i$ and $\pi_{E}^i$ share the same policy space, Assumption 1 holds by default. I don't understand why this assumption is made explicitly. 

- " During policy execution phase, each agent utilizes the actor network of both policies to generate actions and sampling trajectories based on its local information from the environment." Could you please explain this in more details? I don't understand how two polices merge into one execution policy.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the use of individual rewards to enhance team policy learning in cooperative multi-agent reinforcement learning (MARL). The authors introduce a multi-agent policy optimization approach that employs a policy consistency constraint to ensure alignment between the mixed policy and the team policy. The proposed method is evaluated on several benchmarks including SMAC, MPE, and GRF.

### Strengths
1. The primary research question - leveraging individual rewards to assist in learning team policies - addresses an important aspect of MARL.
2. The incorporation of a consistency constraint between the returns of the optimal team policy and the learned mixed policy is intuitively sound and well-motivated.

### Weaknesses
1. The key innovation of this paper can be further clarified. It's unclear whether the primary contribution is the policy consistency constraint or another aspect. The authors mention IRAT [1] as the most closely related work, but a more detailed comparison between the two methods would be beneficial, particularly in explaining the differences between their respective policy consistency constraints. Specifically, it is not clear if the policy consistency constraint is a novel contribution or an adaptation of existing techniques. A more precise explanation of how this constraint is formulated and how it differs from related approaches is needed.

2. While this work appears to be an improvement on IRAT, with core methods following similar intuitions of ensuring policy consistency, the reasons for CMT's superior performance over IRAT in the experiments are not thoroughly discussed. An analysis of the key design elements contributing to this improvement would strengthen the paper. It would be beneficial to understand if the improvement comes from the specific form of the consistency constraint, the optimization method, or other factors. A detailed ablation study could help isolate the contributions of each component.

3. The experimental evaluation covers three different benchmark environments (SMAC, MPE, GRF), which is commendable. However, there's inconsistency in the evaluation of baselines across different subsets of tasks. For instance, IRAT, MAPPO, and QMIX are evaluated on 11 tasks in SMAC, while LAIES and MASER are evaluated on 5 tasks. A more uniform evaluation across baselines would provide a clearer comparison. This makes it difficult to assess the relative performance of the proposed method against all baselines across a consistent set of tasks. A more comprehensive evaluation with all baselines on all tasks would be beneficial.

4. Minor comments:
    - The notation $CD_{KL}$ should be explained upon first use, or the more commonly used $D_{KL}$ could be adopted for clarity.

### Questions
1. Could the authors further clarify the main contributions of this paper?
2. What are the key differences between Equation 9 in this paper and Equation 7 in [1]?
3. Could the authors elaborate on the rationale for selecting evaluation tasks?
4. When comparing CMT with LAIES and MASER, does CMT use rule-based individual rewards of LAIES/MASER-constructed individual rewards?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Augmenting sparse team rewards with individual rewards to guide MARL policy training may potentially alter the optimal policy. This paper proposes a method CMT that ensures consistency between the mixed policy trained with individual and team rewards and the team policy trained solely on team rewards. Specifically, the paper formulates a constrained policy optimization model and transforms it into its Lagrangian dual problem to solve it without knowing the optimal team policy. The authors iteratively optimize mixed policy and team policy with the min-max dual objective derived from the Lagrangian dual model and model them into two types of policy networks. Sufficient experiments are conducted in SMAC, MPE, and GRF to demonstrate CMT’s effectiveness.

### Strengths
1. The article is well-structured, with a clear and well-defined motivation.
2. The paper provides a rigorous theoretical derivation to demonstrate the consistency of policy learning after the inclusion of individual rewards.
3. The paper conducted extensive experiments to validate its effectiveness.

### Weaknesses
1. The effectiveness of the method relies on the careful design of individual rewards.

### Questions
1. According to the training framework proposed by the authors, are there any requirements for individual rewards? In other words, if the rewards are inappropriate, how does the lower bound of this framework compare to the original training method without additional rewards?

2. Based on Question 1, when the scale of individual rewards is too large, even exceeding that of team rewards, will the method in the paper still ensure policy consistency? Can the method eliminate the inconsistency in policy learning objectives caused by the scale disparity between individual rewards and team rewards?

### Soundness
3

### Presentation
3

### Contribution
3
