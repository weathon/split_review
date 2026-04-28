# Proximal Curriculum with Task Correlations for Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
Curriculum design for reinforcement learning (RL) can speed up an agent's learning process and help it learn to perform well on complex tasks. However, existing techniques typically require domain-specific hyperparameter tuning, involve expensive optimization procedures for task selection, or are suitable only for specific learning objectives. In this work, we consider curriculum design in contextual multi-task settings where the agent's final performance is measured w.r.t. a \emph{target distribution over complex tasks}. We base our curriculum design on the Zone of Proximal Development concept, which has proven to be effective in accelerating the learning process of RL agents for \emph{uniform distribution over all tasks}. We propose a novel curriculum, \AlgoOurs{}, that effectively balances the need for selecting tasks that are not too difficult for the agent while progressing the agent's learning toward the target distribution via leveraging task correlations. We theoretically justify the task selection strategy of \AlgoOurs{} by analyzing a simple learning setting with \textsc{Reinforce} learner model. Our experimental results across various domains with challenging target task distributions affirm the effectiveness of our curriculum strategy over state-of-the-art baselines in accelerating the training process of deep RL agents.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors suggest a curriculum approach to reinforcement learning within a contextual multi-task framework. Initially, this framework is used to formulate a teacher-student curriculum learning strategy, and the authors analyze the learning objective from the perspective of the teacher. Following this, the authors propose a strategy called ProxCoRL, which selects tasks $c_t\$ based on their analysis. The paper ultimately demonstrates that the proposed strategy empirically outperforms previous curriculum-based reinforcement learning methods and baseline algorithms across a variety of tasks.

### Strengths
The paper emphasizes the significance of a balanced task selection strategy, which ensures that the tasks presented to the agent are neither too difficult nor too simple. This strategy facilitates the agent's progressive learning towards the target distribution. The approach employs a task selection mechanism and is supported by a mathematical analysis within a simplified setting.

### Weaknesses
The paper does not present a method that is fundamentally different from those in prior work[1]. The authors attempt to extend the idea proposed in ProCuRL[1] to a general target distribution, yet the core of this extension appears to be a mere application of an existing concept. Specifically, the core idea of using a proximal update based on a KL divergence between task distributions remains largely unchanged from [1]. The modification to incorporate a target distribution, while seemingly novel, simply adds a weighting term to the existing proximal update, which does not represent a significant conceptual leap. Moreover, the simplified setting used to conduct the mathematical analysis diverges significantly from a typical RL setting, given it encompasses only two possible actions and a single isolated state space. This raises questions about the scalability of such an analysis in a general reinforcement learning framework, particularly in complex environments with continuous state and action spaces. Furthermore, the analysis lacks consideration of the exploration-exploitation trade-off, which is a critical aspect of RL. Additionally, while the authors claim that their proposed approach eliminates the need for domain-specific hyperparameter tuning, it nonetheless requires the determination of $V_{max}$, which represents the maximum possible value. The estimation or approximation of $V_{max}$ can be non-trivial and may require domain-specific knowledge or heuristics, thus contradicting the claim of eliminating domain-specific tuning.

### Questions
1. Answer the concerns in the above weakness section.

2. While the authors assert that their proposed method, ProxCoRL, is robust to the target distribution $\mu$ in contrast to ProxCuRL, the results presented in Figure 2 do not substantiate this claim. It is evident that ProxCoRL does not demonstrate effectiveness as the performance gap between ProxCoRL and ProxCuRL narrows in the case of a non-uniform task distribution (PointMass-s:2G). Could you clarify these results?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* This paper introduces a curriculum strategy that applies the “Zone of Proximal Development” concept to accelerate the learning progress of RL agents.

### Strengths
* The paper is well-written. 
* The method is motivated well; the proper background is introduced, and the technical details are clear. 
* The paper provides good context for related work, and the appropriate baselines are used for evaluation.
* The results are convincing.

### Weaknesses
 * Use “citep” instead of “citet” for citations where the citation is not part of the sentence. In the Section 2, there are many instances of this error (e.g. “Hallack et al., 2015…”, “Sutton et al., 1999).
 * The above error occurs in following sections as well (see paragraph 3 in Section 3.1; First paragraph in Section 4).
 * Minor: Figure 2 plotlines are a bit thick, making it somewhat difficult to read. I would suggest slightly decreasing the line width.

### Questions
* None.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the curriculum learning setting in reinforcement learning problems. It focuses on the selection strategy of tasks from the target task distribution. The goal is to maximize the expected return of the learned policy on target task distribution. This work approximates this objective in a simplified learning setting (a single state and two actions in contextual MDP) with a single target task. And the approximation yields a curriculum strategy. According to the theoretical derivation, the authors propose the task selection strategy in the general setting of contextual MDP with arbitrary target task distributions.

The experiments are conducted on the tasks of sparse goal-reaching and bipedal walker stump tracks. The proposed method almost outperforms all baselines, including SOTA algorithms for curriculum learning.

### Strengths
The proposed method is well-motivated with a theoretical foundation. 

This paper is generally well-written and the proposed approach is clearly presented.

### Weaknesses
The theoretical contribution is not strong enough, since the theorem is derived from a super simplified setting. And the adaptation to more general setting is not directly supported by the theorem.

The proposed algorithm is not obviously better than the baselines.

The experiments are only conducted on relatively simple tasks with state-based policy. It will be much more impressive if the proposed method can handle vision-baed RL policy.

### Questions
As for the theoretical derivation in Section 3, is it possible to make the theoretical contribution stronger? Can we extend Theorem 1 by relaxing its assumption about the MDP or the target task distribution? The theoretical derivation looks a bit trivial when only considering the contextual MDP with singleton state space and a single target task.

As for the changes from Equation 1 to Equation 2, why we can replace V*() with V_{max}? Is there any mathematical derivation behind it?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a curriculum learning method for multi-task reinforcement learning agents to solve a target distribution of tasks. It balances between selecting tasks of moderate difficulty for the learning agent to solve and proposing tasks that are similar to the target distribution. The metric for sampling tasks is derived in a specific learning scenario and is then applied to other more general settings. In implementation, the method involves sampling a discrete pool of tasks from the uniform and target distribution of tasks and prioritizing the learning of the tasks proportional to the proposed metric. The experiments are conducted in both binary sparse reward and dense reward environments to solve various target distributions of tasks.

### Strengths
1. The method can deal with curriculum learning towards various target distributions of tasks, different to other works that consider a uniform target distribution. 
2. The paper is generally well-written and easy to follow.

### Weaknesses
1. It is not unconvincing to directly apply the curriculum strategy derived from the simple scenario in Sec 3.1 to the general case in Sec 3.2, since the simple scenario is with specific action and reward settings. The analysis in Section 3.1 relies on a contextual bandit setting with a specific reward structure and discrete action space. This makes the direct transfer of the derived curriculum strategy to the general RL setting, which involves complex action spaces, temporal dependencies, and delayed rewards, questionable. The justification for the extended application is not thoroughly established, and the potential impact of these differences on the validity of the approach is not discussed.
2. The metric for task similarity is a bit specific to the tasks. Currently, the metric is defined based on the L2 distance of context parameters. However, there are many cases where such a metric is not positively correlated with the intuitive similarity between tasks. For example, consider a table-top manipulation environment with a drawer and a cube on the table. Suppose the initial state is with the drawer closed and the cube on the table outside the drawer. Consider a desired state A with the cube on top of the closed drawer and a desired state B with the cube inside the closed drawer. Suppose the context parameters are defined as the open width of the drawer and the pose of the cube. We can see that the L2 distance between A and B is small, but the complexity of strategies to reach A and B is different: reaching state A only requires one pick-and-place while reaching state B requires opening the drawer, placing the cube, and then closing the drawer. It is inappropriate for the curriculum to treat these tasks as similar, and I think a better metric for task similarity is required.
3. Fig. 2(b) shows that PROXCORL performs similarly to PROXCORL-UN in PointMass-s:2G environment. Since the target task distribution is non-uniform in this environment, the result weakens the contribution of the proposed curriculum that takes task correlation into consideration. The similarity in performance raises concerns about the effectiveness of the proposed task correlation term, especially given the non-uniform target distribution. The fact that the uniform sampling method performs comparably suggests that the proposed method might not be providing a significant advantage in this specific setting, which undermines the overall contribution.

### Questions
Please refer to the "weaknesses" part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
