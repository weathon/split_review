# Distributed Epigraph Form Multi-Agent Safe Reinforcement Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
Most existing safe multi-agent reinforcement learning (MARL) algorithms consider the constrained Markov decision process (CMDP) problem, which targets bringing the mean of constraint violation below a user-defined threshold.
However, as observed by existing works albeit for the single-agent case, CMDP algorithms suffer from unstable training when the constraint threshold is zero.
This paper proposes **EFMARL**, a novel MARL algorithm that improves upon the problems faced in the zero constraint threshold setting by extending the *epigraph form*, a technique to perform constrained optimization, to the centralized training and distributed execution (CTDE) paradigm.
We validate our approach in different Multi-Particle Environments and Safe Multi-agent MuJoCo environments with varying numbers of agents. Simulation results show that our algorithm achieves stable training and the best performance while satisfying constraints: it is as safe as the safest baseline that has significant performance loss, and achieves similar performance as baselines that prioritize performance but violate safety constraints.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an approach called EFMARL, which extends the epigraph form optimization method to address safe multi-agent reinforcement learning (MARL). Based on the epigraph form, EFMARL targets the problem of achieving zero constraint violations in multi-agent environments by using a centralized training and distributed execution (CTDE) approach. The method is tested in both multi-particle and Safe Multi-agent MuJoCo environments, demonstrating stability and performance in enforcing safety constraints while avoiding performance degradation.

### Strengths
1. The paper is well-written and easy to follow.
2. The related work is well investigated.

### Weaknesses
1. The Lagrangian multiplier, $\lambda$, may also decrease depending on various Lagrangian version configurations.

2. The performance of the Lagrangian method depends on the parameter settings for different tasks. In my understanding, if we fine-tune the Lagrangian parameters, the Lagrangian method can also perform better.

### Questions
1. Can the study provide a convergency analysis?
2. Given the centralized training requirement, what specific computational challenges arise, and how are these managed to ensure scalability with an increasing number of agents?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new multi-agent constrained optimal control formulation, addressing the zero constraint violation setting. Specifically, the authors highlight and address the main limitations of Constrained MDP-based approaches in ensuring safety, particularly under strict constraints where any violation of safety requirements is unacceptable. Hence, they propose to extend the epigraph form method proposed for a single-agent scenario in (So\&Fan 2023) to multi-agent reinforcement learning (MARL), presenting Epigraph Form MARL (EFMARL).

### Strengths
The paper introduces a novel epigraph formulation to solve the multi-agent constrained optimal control problem. While based on established concepts, the authors' extension to the multi-agent reinforcement learning (MARL) context is not trivial. I particularly appreciate the authors' comparison to existing theoretical approaches, highlighting where current methods fail to handle constraint satisfaction and safety issues in MARL settings. The proposed formulation for the multi-agent optimal control seems an interesting and valid alternative to the well-studied Constrained MDP.

### Weaknesses
Even though the paper tries to address a very important problem with an elegant novel formulation, several concerns arise when reading the paper.

**On the comparison with existing literature**:

In the introduction section, the authors state that there is a lack of theoretical and practical solutions for safe RL, especially when policies are executed in a distributed manner. This statement is partially incorrect as several works, for instance, [A, B, C, D], proposed an in-depth study and benchmarks on the mentioned problem. A brief discussion and an empirical comparison against one or two of these methods are missing.

**On the global guarantees of epigraph-based solution**:

The authors correctly notice that existing Constrained MARL approaches provide safety guarantees either in the form of asymptotic convergence guarantees to the optimal safe solution or other approximate forms. Nonetheless, what type of guarantees they can provide with their novel formulation remains unclear. If I understand correctly, by using distributed constraint-value functions during execution, the agents theoretically ensure safety without needing a centralized update. In fact, as reported by the authors in lines 310-318, with this formulation, even without communication between agents, safety is ensured as long as each agent solves the local problem for each $z_i$. However, this decentralized approach primarily guarantees "constraint satisfaction" rather than task completion, meaning that while the agents may stay safe, they might not achieve the global objective if staying in place satisfies the constraints without addressing the task goals. A clear discussion of this aspect is needed to properly assess the value of the work.

**Weak empirical evaluation**:

A significant limitation of this work is the lack of a thorough empirical evaluation that addresses both task completion and scalability challenges. The primary metrics presented—cost and safety rate—demonstrate the method’s effectiveness in meeting constraints, but they do not reveal whether the agents actually complete the intended tasks. Essential performance indicators, such as mean reward (or mean success rate), are needed to clarify the method’s ability to balance constraint satisfaction with successful task completion. Without these measures, the empirical results do not fully validate the theoretical concerns raised for the CMDP formulation. For instance, a trained CMDP-based policy that opts to take no action (e.g., zero velocity) could theoretically match an epigraph-based method in having zero constraint violations, but only the latter may achieve task completion while also respecting safety constraints. Thus, without a metric for task completion, the reported experiments do not provide a comprehensive assessment of the novel formulation’s effectiveness compared to the existing formulation.

Additionally, a detailed comparison with recent Safe MARL approaches (e.g., [A, B, C]), even if they do not strictly enforce zero constraint violations, is missing. Finally, a discussion on the scalability limitations associated with using Graph Neural Networks (GNNs) as the backbone for $z$-conditioned policies is also not discussed. Although GNNs are effective in handling complex inter-agent dependencies, they may introduce computational and structural limitations that impact scalability in larger, more complex multi-agent scenarios. An in-depth investigation of these scalability issues would better validate the robustness and applicability of the proposed formulation.


**Minor comments**: 

The formulation lacks a little bit of clarity. For instance, in Eq.(2), the cumulative cost over an infinite horizon is defined with $l(x^k, \pi(x^k))$, while in Eq.(3), the authors introduce the epigraph form using a "cost" function $J(x)$. While this is done only for practical purposes, however consistency in the background formulation would be beneficial to the clarity of the paper. In Eq. (7), there is $k \geq \tau$, but $\tau$ is never defined/discussed.
In line 235, the authors refer to a "total value function," which should properly be a "total \textit{cost} value function". Moreover, using the term "value function"  in an RL-based context could be misleading, as we typically denote by "value function" $V_\pi(x)$ the value of a state, considering the immediate reward plus the future discounted reward following the current policy $\pi$.

### Questions
Q1: What are the global guarantees on the safety aspect when using the proposed epigraph formulation?

Q2: Do the methods proposed in the empirical evaluation solve the tasks? If so, why the author do not reported the mean global success rate/ mean global return?

Q3: What is the scalability of the proposed formulation? Does the use of GNNs limit the applicability of the proposed methods to a significant number of agents?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the safe marl problem under the zero constraint violation setting. A multi-agent constrained optimal control problem is formulated using the epigraph form technique in optimization theory. A safe marl algorithm is proposed, where graph neural networks are used to model distributed policies. Simulation results demonstrate the effectiveness of the proposed algorithm.

### Strengths
(1) Graph neural networks are used to model distributed policies to improve coordination performance.

(2) Extensive simulations are performed on standard marl benchmarks.

### Weaknesses
 (1) There exist severe theoretical issues in the paper.

 (2) The comparison between the proposed method and the Lagrange-based method is not sufficient.

 (3) The paper is poorly written, which is very hard to follow.

 More details are given in the question part.

 (1) Is the multi-agent system considered in the paper homogeneous or heterogeneous? It seems that the MAS is homogeneous in Section 3.1 due to the shared observation space. However, as stated in Section 4.2, the advantage decomposition method is used to train NNs, such that the MAS seems to be heterogeneous.

 (2) (6) is not the correct Lagrangian for (3). Please provide the correct form of the Lagrangian for (3), and ensure the comparison between your method and the Lagrangian method is accurate. Can your method reduce computational complexity for example?

 (3) Proposition 1 is wrong. Neither $h(x^k)$ nor $V(x^{k+1}, z^{k+1}; \pi)$ is a function of $u^k$. It also seems that the proposed algorithm is irrelated to this proposition.

 (4) In the policy and value function update section, if each agent has its local policy and constraint-value function, then $\pi_{\theta}$ and $V_{\psi}^h$ should be respectively rewritten as $\pi_{\theta^i}$ and $V_{\psi^i}^h$. In addition, do you use MAPPO or HAPPO? The authors are suggested to incorporate the update formulas of NNs in the appendix.

 (5) How to determine the sampling interval of $z$? What will happen if we choose the interval too large or too small?

 (6) Why is $z$ updated during the policy and value function update process (lines 295-296)?

 (7) The proof of Theorem 1 is very hard to follow. Both $V^h$ and $V^l$ are functions of $x$, but the authors seem to neglect this property. Formula (16) should be rewritten. Why is $\varepsilon$ positive (line 846)? In the proof of Lemma 1, what will happen if $\varepsilon  - \eta < \zeta < \varepsilon $? Too many redundant notations exist in the proof. If the authors are confident in the correctness of the theoretical derivation, please revise the proof carefully. Thanks.

 (8) In section 4.3, the authors should explain how to obtain the optimal $z$ once the updates for both the policy and the value function are completed.

 (9) It is confusing that the authors emphasize solving the outer problem during the distributed execution process. Why can’t this problem be addressed during centralized training? Sharing local $z_i$ in an all-to-all or centralized communication network doesn’t seem to increase communication cost, as $z_i$ is a scalar.

### Questions
(1) Is the multi-agent system considered in the paper homogeneous or heterogeneous? It seems that the MAS is homogeneous in Section 3.1 due to the shared observation space. However, as stated in Section 4.2, the advantage decomposition method is used to train NNs, such that the MAS seems to be heterogeneous.

(2) (6) is not the correct Lagrangian for (3). Please provide the correct form of the Lagrangian for (3), and ensure the comparison between your method and the Lagrangian method is accurate. Can your method reduce computational complexity for example?

(3) Proposition 1 is wrong. Neither $h(x^k)$ nor $V(x^{k+1}, z^{k+1}; \pi)$ is a function of $u^k$. It also seems that the proposed algorithm is irrelated to this proposition.

(4) In the policy and value function update section, if each agent has its local policy and constraint-value function, then $\pi_{\theta}$ and $V_{\psi}^h$ should be respectively rewritten as $\pi_{\theta^i}$ and $V_{\psi^i}^h$. In addition, do you use MAPPO or HAPPO? The authors are suggested to incorporate the update formulas of NNs in the appendix. 

(5) How to determine the sampling interval of $z$? What will happen if we choose the interval too large or too small?

(6) Why is $z$ updated during the policy and value function update process (lines 295-296)?

(7) The proof of Theorem 1 is very hard to follow. Both $V^h$ and $V^l$ are functions of $x$, but the authors seem to neglect this property. Formula (16) should be rewritten. Why is $\varepsilon$ positive (line 846)? In the proof of Lemma 1, what will happen if $\varepsilon  - \eta < \zeta < \varepsilon $? Too many redundant notations exist in the proof. If the authors are confident in the correctness of the theoretical derivation, please revise the proof carefully. Thanks.

(8) In section 4.3, the authors should explain how to obtain the optimal $z$ once the updates for both the policy and the value function are completed.

(9) It is confusing that the authors emphasize solving the outer problem during the distributed execution process. Why can’t this problem be addressed during centralized training? Sharing local $z_i$ in an all-to-all or centralized communication network doesn’t seem to increase communication cost, as $z_i$ is a scalar.

### Soundness
2

### Presentation
1

### Contribution
2
