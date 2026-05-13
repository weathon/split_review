# Exploiting Structure in Offline Multi-Agent RL: The Benefits of Low Interaction Rank

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
We study the problem of learning an approximate equilibrium in the offline multi-agent reinforcement learning (MARL) setting. We introduce a structural assumption---the \textit{interaction rank}---and establish that functions with low interaction rank are significantly more robust to distribution shift compared to general ones. Leveraging this observation, we demonstrate that utilizing function classes with low interaction rank, when combined with regularization and no-regret learning, admits \textit{decentralized, computationally and statistically efficient} learning in offline MARL. Our theoretical results are complemented by experiments that showcase the potential of critic architectures with low interaction rank in offline MARL, contrasting with commonly used single-agent value decomposition architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new notion of interaction rank to characterize the structure of a Markov game. If the true reward function and the learned reward function has a low interaction rank, then the authors designed decentralized \chi^2 regularized policy gradient approach and prove it converges to a CCE. The idea of low interaction rank is interesting. It may have potential in practice to help understand a wide range of multi-agent RL problems.

### Strengths
The notion of interaction rank is new and interesting. The authors provide statistical convergence and sample complexity guarantee under the assumption of low interaction rank for decentralized Markov game.

### Weaknesses
1. The assumption MGs with decoupled transitions is very restrictive.

2. Assumption that the reward function and transition kernel belong to the function class is restrictive. Further assumption that the function classes are finite are not practical at all.

3. The algorithm 1, line 3, estimating the transition kernel may not be as easy as it looks to be. Solving for the arg max in practice will be difficult.

4. In the discussion on page 9, the authors claim that existing studies are not decentralized. However, it looks to this reviewer that the advantage in this paper may come from the assumption of decoupled transition.

### Questions
1. Can the authors explain the on-support and off-support components in Theorem 2? The off-support component depends on the gap between the best response policy of agent i over the entire probability simplex and the best response policy within a bounded $\chi^2$ divergence ball. This seems to be due to the $\chi^2$ divergence regularizer in the algorithm. It is not clear here whether such a $\chi^2$ divergence regularizer is a wise choice, though it may provide some convenience for the analysis, it limits the performance of the obtained policy.

2. The authors then define the C_sin, which can be infinity due to taking the max over $\mu_i$ if $\nu_i$ is zero for some action a_i and context c. This reviewer is curious whether the single policy concentration coefficient can be defined here, and the optimality gap can be derived as a function of the single policy concentration coefficient. (similar comment for assumption 4).

3. Can the authors provide some examples where the low interaction rank assumption can be satisfied? If given unknown environment, how to verify such a low interaction rank assumption?

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
3

### Summary
This paper introduces a structural assumption -- the interaction rank (IR), and establishes that functions with low interaction rank are more robust to distribution shift compared to general ones. The authors show that learning an approximate equilibrium in offline MARL can scale exponentially with the IR instead of exponentially with the number of agents. The proposed algorithm is a decentralized, no-regret learning algorithm that can be implemented in practical settings while utilizing standard RL algorithms.

### Strengths
* The paper leverages a structural assumption that shows the potential of using reward architectures with low interaction rank in offline MARL setting with an orderly better sample complexity, which seems to be a promising future direction.
* The paper is well-written and easy to follow.

### Weaknesses
 * I don't see much discussion on related MARL or RL literature regarding interaction rank or similar assumptions. Discussion on literature of related topic would help determine the novelty of the idea and quantify the contribution.

 * By leveraging the low interaction rank assumption, the proposed algorithm achieves a sample complexity that scales exponentially
 with the interaction rank instead of number of agents. Meanwhile, there exists a constant as the coefficient of the sample complexity that hides behind the operator "$\lesssim$". How to understand the constant? Does it scales with the problem size?
* In extreme case where the problem has full interaction rank, does the proposed sample complexity orderly equal to the case that scales with number of agents? If not what makes the difference?

### Questions
* By leveraging the low interaction rank assumption, the proposed algorithm achieves a sample complexity that scales exponentially
 with the interaction rank instead of number of agents. Meanwhile, there exists a constant as the coefficient of the sample complexity that hides behind the operator "$\lesssim$". How to understand the constant? Does it scales with the problem size?
* In extreme case where the problem has full interaction rank, does the proposed sample complexity orderly equal to the case that scales with number of agents? If not what makes the difference?

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
2

### Summary
The paper first shows that if the underlying problem has low interaction rank then it is robust to distribution shifts coming from the mismatch between training and target distributions. Then the authors propose a decentralised algorithm for multi-agent offline reinforcement learning and explicitly derive a performance guarantee that depends on the interaction rank of the function K. The theoretical results are verified with experiments on a toy problem.

### Strengths
- The paper states a clear research question and draws clear conclusions that explicitly show low interaction rank games are easier to learn. While this result is not surprising, it is good that the paper explicitly derives it and quantifies this dependence.
-  The paper proposes a novel algorithm, which is decentralised and can learn from offline data.

### Weaknesses
 - The empirical evaluation is limited to one toy problem only, with no real-world experiments
- The paper could use a more explicit related work section. For example, currently when reading the paper it is not clear what is the state of the art when it comes to offline, decentralised, MARL and how does the proposed algorithm compares to it.

### Questions
- The authors considered specifically the decentralised setting. I wonder if a better performance guarantee can be obtained if we assumed centralised setting.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies learning a coarse correlated equilibrium in the offline multi-agent reinforcement learning. By imposing assumptions on the interaction rank of reward models, the paper establishes a sample complexity bound that grows exponentially with respect to the interaction rank, instead of the number of agents. Finally, the author use numerical experiments to examine the effectiveness of the proposed algorithm.

### Strengths
* The paper is the first that proposes a decentralized algorithm for offline general-sum MARL games and establishes its probable statistical guarantees.
* The integration of interaction rank to MARL provides an interesting yet also technically non-trivial angle. 
* The paper flow is good, and the author uses contextual games to serve as a toy example to help readers understand the idea of the paper. I like the proof sketch provided for the contextual game when K = 2.

### Weaknesses
 * The authors are encouraged to release the codes of the numerical experiments.
* Just a suggestion, maybe the author can consider using Markov Game or MG to replace RL in the title or in the abstract. I feel like people usually refers to the cooperative setting when saying MARL.
* The considered problems are contextual game, which does not have the notion of state, and transition-decoupled MG. I believe the author could directly brought up the transition decouple assumption in the problem formulation, since it is an assumption on the setting instead of technical assumptions.

### Questions
* I wonder does similar property applies to the cooperative setting? I would like to hear the author's insight on the difference between these two settings (cooperative and competitive).
* In MARL, another widely-used property is the exponential decay of transition dynamics, e.g., [1,2]. From a intuitive perspective, is "low interaction rank" basically assumes a similar property, instead of on the transition dynamics, but on the reward structure? If they do share relevant ideas, I suggest the authors also discuss in the paper. Also, do you think the exponential decay property can be used to alleviate the current decoupled transition property in the paper? 

[1] Qu, G., Wierman, A., & Li, N. (2022). Scalable reinforcement learning for multiagent networked systems. Operations Research, 70(6), 3601-3628.

[2] Ying, D., Zhang, Y., Ding, Y., Koppel, A., & Lavaei, J. (2024). Scalable primal-dual actor-critic method for safe multi-agent rl with general utilities. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
3

### Contribution
3
