# Handling Cost and Constraints with Off-Policy Deep Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Methods for off-policy deep reinforcement learning (DRL) offer improved sample efficiency relative to their on-policy counterparts, due to their ability to reuse data throughout the training process. For continuous action spaces, the most popular approaches to off-policy learning include policy improvement steps where a learned state-action ($Q$) value function is maximized over selected batches of data. These updates are often paired with regularization to combat associated overestimation of $Q$ values. With an eye toward safety, we revisit this strategy in environments with ``mixed-sign'' reward functions; that is, with reward functions that include independent positive (incentive) and negative (cost) terms. This setting is common in real-world applications, and may be addressed with or without constraints on the cost terms. We find the combination of function approximation and a term that maximizes $Q$ in the policy update to be problematic in such environments, because systematic errors in value estimation impact the contributions from the competing terms asymmetrically. This results in overemphasis of either incentives or costs and may severely limit learning. We explore two remedies to this issue. First, consistent with prior work, we find that periodic resetting of $Q$ and policy networks can be used to reduce value estimation error and improve learning in this setting. Second, we formulate novel off-policy actor-critic methods for both unconstrained and constrained learning that do not maximize $Q$ in the policy update.  We find that this second approach, when applied to continuous action spaces with mixed-sign rewards, consistently and significantly outperforms state-of-the-art methods augmented by resetting. We further explore the applicability of our approach to more frequently-studied control problems that do not have mixed-sign rewards, finding it to both more reliably produce competent performance and be competitive in terms of overall performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the challenges of reinforcement learning (RL) in settings where the environment returns both positive and negative rewards. The authors highlight the limitations of standard off-policy RL algorithms such as SAC and TD3 in handling such scenarios and discuss methods like periodic network resets and constrained-MDPs to mitigate these issues. They propose a method called, constrained off-policy actor-critic algorithm that combines elements of said approaches to build a method that can work in such scenarios. The performance of their method is evaluated using some of the OpenAI Safety Gym benchmark tasks.

### Strengths
The paper effectively motivates the difficulties of employing standard RL algorithms in scenarios where the environment provides both positive and negative rewards. The writing is clear and engaging with a well-structured flow up to section 4.2.1.

### Weaknesses
 - This is an empirical paper as the proposed method is nothing but the combination and examination of existing ideas without introducing new ones. Being an empirical paper is not a negative point, however, it requires comprehensive and thorough results. Unfortunately, it is not the case in this paper. In particular, the paper uses OpenAI Safety Gym benchmark to evaluate their method but failed to include more Safe-RL methods, like [1], etc. It was shown in previous papers that CMDP methods work the best in this benchmark and using standard RL methods ( MDP-based not CMDP) don't result in good performance.


- The authors' main contribution appears to be Algorithm 1, which is briefly described in Section 4.2.1. There are many issues here. First of all, this algorithm has many moving parts and is a rather very complicated method. For instance, it requires assigning 5 different learning rates (i.e. $\lambda_\beta, \lambda_\phi, \lambda_\psi, \lambda_\theta, \lambda_\alpha$) which clearly shows level of complexity in this method. In addition, while this method sometimes shows some improvement in some of the benchmarks, it remains unclear what drives these enhancements. It's crucial to note that the proposed algorithm is evaluated against not right baselines which are not designed for this specific problem setting. The results are also mixed and this method doesn't show a consistent trend in the experiments. For instance, compare results of DoggoGoal and CarPush in Figure 2. Finally, writing of section 4.2.1 and experiments section need major work as it's either too shallow (e.g. 4.2.1) or excessively and unnecessarily detailed, making it challenging to follow ( e.g. especially in the experiment section).

-  The idea of having an environment that returns multiple rewards is a valid idea. However, limiting it to just positive and negative rewards seems narrow. This scenario appears more akin to a constrained markov decision process (CMDP), where one function serves as a reward, and the other as a cost. Authors could have studied this topic in a multi-objective RL setting where there are multiple rewards and the goal is to find a policy that is "optimal" across different rewards. This is a well-studied topic ( see [2], etc) and this paper seems to have selected a setting which is very limited. 

Despite this paper studies an important problem, unfortunately, it presents several shortcomings as mentioned above and is not yet ready for ICLR at the current form and requires major work.

### Questions
In page 4, it is mentioned that "When the reward function has independent terms of different signs, errors in the magnitude of the estimates for |Qr| and |Qc| will grow in opposite directions". This might be true in very limited cases, but I don't think that always holds. Do you have any mathematical or numerical evidence that justify your claim?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is about RL with "mixed-sign" rewards, i.e., the reward function includes independent incentive and cost terms. The authors then argue that learning based on maximizing the summation of two Q-function approximations would lead to overestimates. Relying on these observations, the authors explore two approaches based on resetting and an off-policy actor-critic that does not include Q maximization in the policy improvement step. Experiments are conducted using OpenAI SafetyGyms to compare these new approaches with the standard SAC and TD algorithms.

### Strengths
The problem of solving RL with mixed-sign rewards is relevant and worthy of attention. The exploration based on decomposing the Q and V network, and resetting, seems to be a good approach. Experiments show that the new algorithm performs well compared to SAC and TD. The proposed algorithm is not difficult to implement.

### Weaknesses
I believe the paper's contributions are somewhat incremental and unclear at several points. Please find my comments below:

- I assume the main selling point of the work is Section 3, where the authors discuss the limitations of learning two Q-functions. This section, however, is not clear and not convincing. First, the authors state that under mixed-sign rewards, the Q function can be decomposed into two Q functions, one for the rewards and one for the costs. Why should this decomposition be considered and analyzed? Why shouldn't we keep the overall Q function and learn it based on the total reward $r_{total}$? I can see that the decomposition would lead to over or underestimations for both the rewards and the costs, as the summation would fail to manage how the costs and rewards contribute to the overall rewards. So, it may not be a suitable approach to handle mixed-sign reward situations.
- Later on, Algorithm 1 is also based on two Q and two V functions. This raises the question of how this way of learning compares to learning one Q function based on $r_{total}$. In other words, can we say anything about the equivalence or convergence of this decomposition approach compared to single-Q learning?
- The constrained approach requires introducing the threshold $d$." I am not sure how this can be done systematically as all we know are only the costs and rewards and an upper bound on the accumulated costs is essentially not available. In the experiments, the authors say that "we chose a target cost level equal to half the cost accumulated by a fully-trained TRPO agent unaware of cost." It is very unclear why it should be chosen this way. This needs more justifications.
- The constrained RL approach based on Lagrange multipliers is simply to convert the overall rewards from $r+c$ to $r+\beta c$. This does not seem to be a good approach. 
- The Resetting approach is clearly not new. The authors simply apply this to their problem context and find improvements. So it should not be considered a major contribution

### Questions
Please see the Weaknesses above

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study focuses on environments with "mixed-sign" reward functions. The authors investigate the root cause of the poor performance and discover that it arises from an asymmetric error in estimating the magnitude of returns associated with terms of different signs. And provide a novel algorithm (OPAC^2) building around the off-policy actor-critic. The experiments demonstrate that the proposed algorithm outperforms state-of-the-art methods augmented by resetting.

### Strengths
1. The proposed method is detailed and easy to follow.
2. The proposed algorithm seems competitive in both constrained and unconstrained settings.

### Weaknesses
1. The authors analyze why mixed-sign rewards are problematic in Sec.3, which is not so obvious to me. Could you please provide some more pieces of evidence to help me understand this? Specifically, it's unclear how the asymmetry in error estimation arises and why this is more pronounced with mixed-sign rewards. The explanation lacks a concrete example of how this bias manifests during training and impacts the learning process.
2. I'm not quite sure why resetting can improve this issue. Do you have any intuition on this? It's not clear how resetting addresses the underlying problem of biased value estimation. A more detailed explanation of the mechanism by which resetting mitigates the issue would be beneficial.
3. Similarly, I don't quite understand the intuition behind OPAC. Are there any ablation studies available? The description of OPAC lacks a clear explanation of how it tackles the asymmetric error issue. It would be helpful to see ablation studies that isolate the contributions of different components of OPAC.
4. Do you compare OPAC with other Constrained RL algorithms?

### Questions
Please refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the RL problem with mixed-signed reward functions, where there are costs in the MDP steps. The authors proposes C-OPAC2 method to solve the problem. At the same time, the author suggests useful tricks including resetting $Q$ and policy network and  remove the maximization term. The superiority of the method is validated from the robotic navigation task.

### Strengths
1. The paper considers an important problem in RL community, where costs exists are constraints are required to satisfy.
2. The experiment studies demonstrate great potential of the proposed method.

### Weaknesses
1. Although the studied problem is interesting, the manuscript is not written and hard to follow. 
2. Some notations in Algorithm 1 are not mentioned in Section 3 and Section4, we suggest the authors to explain some important notations in Section 3&4.
2. For mixed-signed reward, it is suggested to give more practical examples, otherwise the statements seems confusing. The authors first claim the mixed-signed reward, later in equation 8, the $c(t)$ is cost. Then in Section 4.2.1, the $C(\tau)$ is constraint. So the constraint could be part of negative reward?
3. In abstract, the authors mentions removing maximization term and reseting the networks, however, this seems not the crucial part of the manuscript.

### Questions
1. The authors considers the constrained RL problem, and it is suggested to consider and compare some related reference [1]
2. In Section 3, the author mentions ``'When Q is underestimated, |$Q_c$| will tend to be overestimated and |$Q_r$| underestimated,'. Why will  |$Q_c$| will tend to be overestimated and |$Q_r$| underestimated, could the author give more insights or theoretical explanations? Why not both Q networks underestimated?
3. There are some concerns why we use two Q networks for $Q_r$ and $Q_c$, even if the reward are assigned at the same time, we can still use one network to estimate. 
The reviewer will consider the increase the rating when the concerns are fully resolved.

[1]: Reward Constrained Policy Optimization. https://arxiv.org/abs/1805.11074

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
