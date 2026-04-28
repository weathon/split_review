# Decentralized primal-dual actor-critic with entropy regularization for safe multi-agent reinforcement learning

- Decision: Reject
- Scores: 3, 5, 5, 5, 5, 5

## Abstract
We investigate the decentralized safe multi-agent reinforcement learning (MARL) problem based on homogeneous multi-agent systems, where agents aim to maximize the team-average return and the joint policy's entropy, while satisfying safety constraints associated to the cumulative team-average cost. A mathematical model referred to as a homogeneous constrained Markov game is formally characterized, based on which policy sharing provably preserves the optimality of our safe MARL problem. An on-policy decentralized primal-dual actor-critic algorithm is then proposed, where agents utilize both local gradient updates and consensus updates to learn local policies, without the requirement for a centralized trainer. Asymptotic convergence is proven using multi-timescale stochastic approximation theory under standard assumptions. Thereafter, a practical off-policy version of the proposed algorithm is developed based on the deep reinforcement learning training architecture. The effectiveness of our practical algorithm is demonstrated through comparisons with solid baselines on three safety-aware multi-robot coordination tasks in continuous action spaces.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposed a primal-dual algorithm for decentralized multi-agent safe RL in homogeneous constrained MDPs. The policy is shared by all the agents. The authors proposed an on-policy primal-dual algorithm and proved the asymptotic convergence. A practical off-policy algorithm is also proposed. The empirical results verify the effectiveness of the algorithm.

### Strengths
1. The writing and presentation are good and easy to read.
2. The theoretical part is technically correct.
3. The empirical results are presented clearly and verifies the algorithm performance.

### Weaknesses
1. The novelty is limited. The convergence proof is not new and can be found in many existing works in the references. The proof on homogeneous multi-agent MDP is just a repeated version and does not bring any novel theoritical insights.
2. The problem setting is confusing. The authors claim communications in the problem formulation, but use local policy and global observations in the later derivations.
3. The assumption of stochastic-optimization-based convergence proof is not practical. It is difficult to make the parameter set of neural networks bounded and do projected gradient descent.
4. The practical algorithm part is also not novel, the off-policy is a commonly seen algorithm in practical RL.

Minor questions:
1. The notation is confusing, especially the permutation notations in Definition 1.

### Questions
1. The communication graph setting is not clear. How to get global observation with only local communications? Does the local policy and reward function include neighborhoods?
2. What case is homogeneous MDP applicable to the real world? Is it an important question since the optimal policy structure is so simple that all agents share the same optimal policy?
3. What theoretical questions did you solve when you try to prove the convergence, based on previous stochastic optimization-based convergence proof?

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
This paper studies safe multi-agent reinforcement learning problem. The authors present a decentralized primal-dual actor-critic algorithm and analyze its convergence properties for *homogeneous*, *entropy regularized* and constrained Markov games with finite state and action spaces under linear function approximation while practical version adopting neural network approximation has also been discussed.

### Strengths
- The paper studies an important problem.
- Detailed numerical examples are provided.
- Claims are supported with theoretical analysis.

### Weaknesses
- The results are presented in a convoluted way such that it is challenging to make connections between different parts. For example, homogeneous MGs are defined yet not used in the convergence analysis except the one related to conditioning policies on limited observation. 
- There are no justifications for the assumptions 1-6 made. Justification is needed especially for the non-standard ones.
- There are no discussions about the key ideas of the convergence analysis. For example, how important is the role of the entropy regularization or homogeneity of MGs in the convergence analysis.
- There should be more qualitative discussions about the algorithm presented.

### Questions
I have the following concerns:
- A similar problem has already been addressed in [Lu et al. 2021; Ying et al. 2023b]. These existing works have been criticized for addressing discrete action spaces while this paper also presents results for discrete cases. Therefore, the last sentence in page 1 is misleading. Furthermore, these works have been criticized to keep track of global policy for privacy-related issues. However, it is not explicit whether the homogenous Markov game structure plays an important role not needing to keep track of global policy. For example, the algorithm uses the product of the same policy, with the copy operator, as if all other agents follow the same local policy independently. Can the authors provide more intuition/explanation on this regard? Indeed, it is also confusing that theorem statements do not include the homogeneous MG assumption except Theorem 1 discussing limited observations. Does the paper consider homogeneous MGs just for limited observations?
- The limited observation extension is confusing since agents can keep track of, e.g., $Q^z(s_t,a_t;\omega_{i,t}^z)$, whereas condition their policy on $o_i(s_t)$. The former implies that they can observe $s_t$. The first line at page 5 also says "Once a tuple $(s_t,...)$" is collected". Therefore, such a limitation for policies is not clear. Furthermore, why the policy at line 237 is not conditioned on $o_i(s_t)$. 
- Can the authors discuss the key technical ideas used in the proofs so that we can identify the technical novelty of the convergence analysis?
- There is a brief discussion about the duality gap at page 4. I think this is a major limitation and should be discussed in detail. For example, the convergence results are based on multi-time scale stochastic approximation theory, which necessitates global asymptotic stability for fast dynamics for any fixed parameter of the slow dynamics. Can the authors elaborate on whether this holds? Indeed, is this the reason to incorporate entropy regularization? Furthermore, is Assumption 6 related to this concern? Can the authors provide justification for Assumption 6?
- Related to the concern above, why do we consider entropy regularization especially because it is stated as a *huge* challenge at line 163. Furthermore, the entropy of the joint policy is the sum of the entropies of the local policies since joint policy is the product of the local policies, i.e., they are independent. The non-linear coupling of local policies does not sound. Can the authors provide more explanation in this regard?
- The update rule for $\omega$ is confusing since the temporal difference term at line 223 has the entropy regularization scaled by $\gamma$. However, at line 152, there is no such scaling for the regularization term.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a decentralized primal-dual actor-critic algorithm for safe multi-agent reinforcement learning (MARL). Initially, the authors formulate the studied problem as a homogeneous constrained Markov game with the addition of entropy regularization to enhance exploration. Then, an on-policy algorithm which can be trained in a decentralized manner, is presented based on policy gradient, using local gradient and consensus steps for updating the policies. Convergence guarantees for this algorithm are also provided under standard assumptions. Subsequently, an off-policy version of this method is provided using standard deep RL techniques. Finally, a comparison with other methods/variations on three multi-robot tasks is demonstrated which shows the advantages of the proposed algorithm.

### Strengths
The strengths of this paper can be summarized as:

1. The safe MARL problem is formally formulated as a homogeneous constrained Markov game. Entropy regularization is also incorporated for facilitating exploration. 

2. An on-policy decentralized primal-dual actor-critic method is presented for addressing this constrained Markov game. The included constraint is handled through the introduction of a dual variable, with the new goal now being to find a saddle point of the Lagrangian. Training takes place in a decentralized manner under the assumption that the global state and joint action can be observed by all agents. 

3. Convergence guarantees are provided for the on-policy method based on commonly used assumptions in the safe MARL literature. 

4. A practical off-policy variant of the method is presented for enhancing its performance and increasing sampling efficiency. 

5. The performance of the method is verified on three multi-robot tasks. The proposed DPDAC-ER method achieves similar performance to MASAC-Lag. It is also shown to respect the constraints in most cases in contrast with MASAC and DAC-ER that do not account for constraints. Finally, the importance of entropy regularization is highlighted since the performance of DPDAC is significantly inferior compared to DPDAC-ER.

### Weaknesses
The weaknesses/limitations of this work are outlined as follows:

1. The proposed approach appears to be a bit incremental compared to prior works presented in [R1, R2]. In [R1] a decentralized actor-critic algorithm was presented for homogeneous MGs without the additions of constraints or entropy regularization that the current submission is addressing. Subsequently, [R2] presented a decentralized actor-critic algorithm that also incorporated entropy regularization for encouraging exploration. Hence, to the reviewer’s best understanding, the main difference between [R2] and the current submission is the inclusion of the constraint and the related dual variable. In particular,  

   a) The on-policy algorithm presented in Section 4 of [R2] is essentially the same with the one in Section 3 of the current paper, without the addition of the dual update related to the constraint. In fact, the updates in Eq. (9) and (10) in [R2] are the same with the ones in Eq. (6) and (7) of the current paper.  

   b) The convergence analysis provided in Section 4 is very similar to the one in Section 5 in [R2]. The main difference lies in the inclusion of the dual variable, which is handled through the multi-timescale stochastic approximation theory, assuming the dual variable to be fixed when studying the convergence of the actor and the critic. 

   c) While the off-policy variant presented in Section 5 appears to be a practical alternative, this is not really a novel contribution as the suggested modifications (actor/critic neural networks and replay buffer) are common tricks in the deep RL literature. 

     Furthermore, primal-dual algorithms for handling constraints in safe MARL have already been quite popular in the literature; see for example [R3, R4, R5]. 

2. The authors claim to be using only observation-based policies. Nevertheless, the assumption in item (iii) of Definition 1 that each $o_i$ is a bijective function, implies that every observation corresponds to a unique state. It is unclear whether this is an indirect assumption of full observability.  

3. In the experiments, the three presented problems (Aggregation, Swapping and Formation) are quite simple multi-robot tasks on a 2D space. Exploring more complex tasks with more constraints or tasks in 3D space could further justify the importance of the proposed approach and how it can be advantageous compared to the other methods. 

4. In one of the presented tasks (Formation), it is unclear whether the algorithm can provide solutions satisfying the constraint, although this seems a quite simple constraint to meet. See question 7 for more details.  

 

[R1] Chen, D., Li, Y., & Zhang, Q. (2022). Communication-Efficient Actor-Critic Methods for Homogeneous Markov Games. In The Tenth International Conference on Learning Representations (ICLR 2022). 

[R2] Hu, Y., Fu, J., Wen, G., Lv, Y., & Ren, W. (2024). Distributed entropy-regularized multi-agent reinforcement learning with policy consensus. Automatica, 164, 111652. 

[R3] Paternain, S., Calvo-Fullana, M., Chamon, L. F., & Ribeiro, A. (2022). Safe policies for reinforcement learning via primal-dual methods. IEEE Transactions on Automatic Control, 68(3), 1321-1336. 

[R4] Ying, D., Zhang, Y., Ding, Y., Koppel, A., & Lavaei, J. (2024). Scalable primal-dual actor-critic method for safe multi-agent rl with general utilities. Advances in Neural Information Processing Systems, 36. 

[R5] Lu, S., Zhang, K., Chen, T., Başar, T., & Horesh, L. (2021, May). Decentralized policy gradient descent ascent for safe multi-agent reinforcement learning. In Proceedings of the AAAI conference on artificial intelligence (Vol. 35, No. 10, pp. 8767-8775).

### Questions
1. The authors are strongly encouraged to elaborate on the differences between their submission and [R2], as well as on the novelty of the contribution of this paper in general; see weakness (1). 

2. Please provide a clarification on the point raised in weakness (2), regarding whether full observability is indirectly assumed in this problem setup. 

3. The convergence analysis relies on the multi-scale approximation theory, essentially assuming that the critic and actor converge under fixed dual variables. The authors are encouraged to elaborate on why this is a reasonable assumption. 

4. In the convergence analysis, in line 823, it is mentioned that ‘Note that both the state and action spaces are discrete.’ Does this suggest that the convergence analysis is not applicable to the continuous action spaces? The authors are encouraged to provide a clarification given that the paper is supposed to be addressing continuous action spaces. 

5. The variable $\rho$ is defined as the ‘initial state distribution’ in line 156. But $\rho$ also appears in line 743 (as part of Eq. (25)), which in that context may be related to the spectral norm? 

6. Can the proposed algorithm be successfully applied to more complex tasks? The authors could consider for example, more “obstacles” that all agents need to avoid, or tasks in 3D space. It would also be interesting to comment on the advantages of entropy regularization in such tasks, since it could be expected that proper exploration would be even more critical in such scenarios. 

7. In Figures 1, 4 and 5, the average episode costs for the formation task never reach the threshold values. In fact, in Fig. 5, with threshold values 0.0, 2.0, 5.0, the cost of the resulting policies is around 2.0, 4.0 and 6.0, respectively. Does this indicate that the proposed algorithm cannot really satisfy the constraint for this task? It is also interesting how increasing the threshold gives “more unsafe” policies that violate even the additionally relaxed threshold.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers the decentralized safe multi-agent reinforcement learning (MARL) problem in homogeneous multi-agent systems. To address the problem, the paper formalizes it as a homogeneous constrained Markov game and proposes an on-policy decentralized primal-dual actor-critic algorithm. Theoretical results are provided on the convergence of the algorithm, and experimental results show the efficacy of the algorithm in 3 multi-particle environments.

### Strengths
The writing of the paper is clear. The paper considers an important problem. Both theoretical results and empirical results are provided. 3 ablation studies are provided.

### Weaknesses
1. The problem setting only considers finite state and action spaces. 

2. The proposed algorithm is standard. Seems that the only difference compared with MAPPO-Lagrangian [1] is that the update steps are decentralized by the parameter aggregation. 

3. There is some ambiguity in the presentation of the algorithm (see Questions for details).

4. The convergence analysis depends on many assumptions, some of which are not realistic. For example, 1) the critic is approximated by linear critic functions; 2) the stepsize of the critic is much larger than the stepsize of the actor, which is also much larger than the stepsize of $\lambda$. None of these assumptions can be realized in a practical algorithm. 

5. The proposed practical algorithm violates the assumptions of the convergence analysis. 

6. The experiments are only performed in Multi-agent Particle environments, which is easy. It is difficult to demonstrate the performance of the proposed algorithm only in these easy environments. 

7. Two of the baselines considered in the experiments do not consider the safety constraint at all. Therefore, these two baselines cannot justify the claims of the paper. I suggest the authors add costs to the reward functions such that the rewards become $r' = r - w c$, where $w$ is the weight, and then choose different $w$ to create several baselines. 

**Minors:**

1. The weight matrix $C_t = [c_t(i, j)]_{N\times N}$ uses the same notation as the cost. I suggest using another notation to avoid confusion. 


**References:** 

[1] Gu, Shangding, et al. "Safe multi-agent reinforcement learning for multi-robot control." Artificial Intelligence 319 (2023): 103905.

### Questions
1. The paper assumes the observation function is bijective, and therefore the agents have global observation. Then why is the observation function needed? What is the observation function in the environments in the experiments?

2. How is the weight matrix $C_t$ updated? Is it learned or handcrafted?

3. Why is the practical algorithm in Section 5 an off-policy one while all the previous analyses are based on the on-policy one?

4. Is the theoretical analysis valid on the practical algorithm?

5. The environments in the experiments have continuous action space. Does this violate Assumption 1?

6. What is the cost threshold for the Formation environment?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the decentralized, safe multi-agent reinforcement learning problem. The paper proposes a homogeneous, constrained Markov game framework to formulate the problem and an off-policy algorithm to solve it. The paper also proves the convergence of the on-policy version of the proposed algorithm under several assumptions. The proposed approach is validated in a safety-aware continuous swarm robot task in a simulation environment.

### Strengths
1. The study of the safety problem of multi-agent reinforcement learning is well-motivated. 
2. The paper is well-structured.

### Weaknesses
1. Problem Formulation isn't sound to me: In 2.2 Problem formulation, the authors assume the availability of the global state and agents' joint actions, which violates the problem setting of the decentralized multi-agent. In decentralized multi-agent RL, the local agent should only have access to the information of its local neighborhood. 

2. The novelty of the paper is limited. 1) problem formulation 2.2, policy gradient derivation, and the convergence proof seem like straightforward extensions of the work [1][4]. 2) The primal-dual method for multi-agent safe RL is also studied in [2-3]. 

3. The proposed approach is only demonstrated in simple robotic swarming tasks in simulation, which is a bit insufficient for validating the effectiveness of the proposed algorithm. From the attached video, I also noticed that in the safe swapping scenario, there were two instances where collisions occurred between agents. It seems the learned policy is not safe enough. 
 
4. I personally feel like the paper is a bit hard to follow due to the heavy notations.

[1] Zhang, Kaiqing, et al. "Fully decentralized multi-agent reinforcement learning with networked agents." International conference on machine learning. PMLR, 2018.

[2] Ying, Donghao, et al. "Scalable primal-dual actor-critic method for safe multi-agent rl with general utilities." Advances in Neural Information Processing Systems 36 (2024)

[3] Paternain, Santiago, et al. "Safe policies for reinforcement learning via primal-dual methods." IEEE Transactions on Automatic Control 68.3 (2022): 1321-1336.

[4] Zhang, Kaiqing, Zhuoran Yang, and Tamer Başar. "Multi-agent reinforcement learning: A selective overview of theories and algorithms." Handbook of reinforcement learning and control (2021): 321-384.

### Questions
How do you set the value of b in the loss function equation (15)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers a safe multi-agent MDP scenario and proposes a decentralized MARL algorithm to solve this problem. It assumes a homogenous constrained MG setup, which results in the fact that independent policies are enough. The paper then considers a communication graph structure over which agents communicate. The paper shows the convergence of the proposed approach.

### Strengths
1. The paper considers a really important problem of constrained multi-agent RL problem. 

2. The paper proposes algorithms that have a provable convergence guarantee.

3. The paper shows convergence under different communication graph structures.

### Weaknesses
1. What is the main motivation behind considering joint reward and the joint cost as permutation preserving? Can the paper provide some real examples that satisfy the above assumption?

2. The paper considers the constraint where the expected cumulative cost across the agents is below a certain threshold. In general, what types of problems have such constraints?

3. Assumption 5 states that it is a three-time scale approximation which might be very slow in convergence.

4. The paper did not bound the sub-optimality gap and even considered a stronger assumption for convergence. For example, Theorem 4 states that for a given dual-variable, the actor policy converges. Then, the paper assumes Assumptions 7 which states that the convergent points of the actor policy parameters are continuous. It seems that it is a very strong assumption. 
Nevertheless, it did not prove the sub-optimality gap. It may converge to some local solution.

### Questions
1. What are the technical novelties? In particular, unconstrained decentralized MARL is well-studied, distributed algorithms under communication graph structure are also well-studied. Finally, the two-time scale algorithms are also well-studied. This paper seems to combine all these approaches. Hence, the technical novelties are not at all clear.

2. From the simulation results, it seems that the performance is similar (or, negligible improvement) compared to MASAC-Lag approach. In fact, for Formation scenario MASAC-Lag has a smaller cost and a better reward. What is the value of the constraint ($b$) for the simulation?

### Soundness
3

### Presentation
3

### Contribution
2
