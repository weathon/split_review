# Embedding Safety into RL: A New Take on Trust Region Methods

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 3, 5, 8

## Abstract
Reinforcement Learning (RL) agents are able to solve a wide variety of tasks but are prone to producing unsafe behaviors.
Constrained Markov Decision Processes (CMDPs) provide a popular framework for incorporating safety constraints. 
However, common solution methods often compromise reward maximization by being overly conservative or allow unsafe behavior during training.
We propose Constrained Trust Region Policy Optimization (C-TRPO), a novel approach that modifies the geometry of the policy space based on the safety constraints and yields trust regions composed exclusively of safe policies, ensuring constraint satisfaction throughout training.
We theoretically study the convergence and update properties of C-TRPO and highlight connections to TRPO, Natural Policy Gradient (NPG), and Constrained Policy Optimization (CPO).
Finally, we demonstrate experimentally that C-TRPO significantly reduces constraint violations while achieving competitive reward maximization compared to state-of-the-art CMDP algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel method for safe RL, i.e. solving CMDPs while ensuring safety during training. The method is based on modifying trust region methods (i.e. TRPO and its constrained variant CPO) to yield trust regions that are contained in the set of safe policies. This is achieved by incorporating a barrier-like function to the trust region divergence, that approaches infinity as the expected cost of the updated policy approaches the threshold. The modified constrained objective is then approximately solved similarly to TRPO, with an additional recovery step in the case that an unfeasible point is reached. The authors provide a detailed theoretical analysis of their approach, and demonstrate the effectiveness of their method compared to other safe RL algorithms.

### Strengths
- The paper investigates an important problem and draws interesting connections to prior works on trust region methods.
- While the idea of using barrier functions for safe RL has been explored before in a number of works, the present paper provides an original and interesting theoretical connection based on modifying the Bregman divergence of trust region methods.
- The authors propose a simple yet effective recovery scheme for unfeasible policies.
- The main part of the paper is well-structured. Ideas are introduced clearly and it is explicitly shown how they relate to previous works.
- A further strength of the paper is the sound theoretical analysis of the proposed method, which is based on similar investigations for other trust region methods.
- The experimental results are promising: the method is shown to achieve competitive return with lower cost regret compared to the presented baselines.

### Weaknesses
While the paper provides worthwhile contributions, in my view there are several improvements that could be made. These mainly concern experimental results and exposition. If these concerns are accounted for, I am happy to increase my score.

Exposition
- The comparison to related work could be improved. In particular, while the related work section in the introduction summarises relevant approaches, it does not explicitly contrast them to the proposed method.
- For example, in the discussion of penalty methods it is stated that they introduce bias and produce suboptimal policies. Why does introducing a logarithmic barrier function to the Lagrangian (as in e.g. IPO) introduce more bias than modifying the trust region divergence?
- It would also be interesting to compare the theoretical bounds of the proposed method to those of other baselines besides CPO, e.g. IPO and the work by Ni et al. (2024).
- The discussion of relevant material in the background section focuses on the setting of discrete state and action spaces. However, one of the primary appeals of policy gradient methods is their applicability to the continuous setting (and this is indeed where the proposed method is evaluated). A discussion of how this relates to the introduced background would be appreciated.
- Furthermore, a brief discussion of Bregman divergences (possibly in the Appendix) would increase readability of the paper for readers not familiar with the topic.
- The experiments section is missing a (brief) discussion of the environments and associated constraints.

Experiments:
- The experimental evaluation does not include other approaches (e.g. P3O), particularly those also based on log-barriers (e.g. IPO, Ni et al. (2024)), which are relevant baselines.
- The ablation study on the hysteresis parameter shows that it is an important component of the achieved cost regret. The same idea can equally be applied to CPO. An ablation study comparing the proposed approach to CPO with hysteresis would highlight the effect of the main contribution of the paper, which is the modified trust region.

Minor remarks:
- The citation for IPO is wrong, this should be Liu et al. (2020) (line 71).
- $V_r^\pi(s)$ in Eq. 31 should be $V_{c_i}^\pi(s)$ (line 737).
- The definition of $L_\theta$ is missing in Eq. 40 (line 792).
- The presentation of Table 1 could be improved. Please highlight the best achieved cost in each row (e.g. bold or underline) and add standard deviations if possible. In the CarButton1 line, no return is bold.

### Questions
- How does the proposed approach compare to relevant baselines (e.g. IPO, Ni et al. (2024)), both in terms of theoretical bounds and empirical performance?
- Why does introducing a logarithmic barrier function to the Lagrangian (as in e.g. IPO) introduce more bias than modifying the trust region divergence?
- Can you provide an ablation study in which the proposed approach is compared to CPO with the same hysteresis scheme?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces Constrained Trust Region Policy Optimization (C-TRPO), an approach that maintains safety constraints throughout reinforcement learning by shaping policy space trust regions to contain only safe policies. C-TRPO achieves competitive rewards and constraint satisfaction compared to leading CMDP algorithms, with theoretical convergence guarantees and experimental success in reducing constraint violations.

### Strengths
1. The idea of incorporating safety constraints into the trust region in TRPO is very reasonable and novel compared with penalty-based methods. 
2. Both theoretical explanation of the C-TRPO and intuitive visualization in the toy MDP as in Figure 2 help to understand the effectiveness of C-TRPO, that it tries to behave safely in the trust region part instead of the target part.

### Weaknesses
1. One concern is the learning of the cost value V_c if this term is unknown. Since CPO suffers from estimation errors, C-TRPO has exactly the same problem. The theoretic analysis builds on the assumption that this function is accurate. The reliance on an accurate cost value function, V_c, is a significant limitation. In practice, V_c must be estimated from samples, introducing approximation errors that can undermine the theoretical guarantees. This is particularly problematic because the constraint satisfaction of C-TRPO depends on the accuracy of this estimate, and errors could lead to unsafe policy updates. The paper does not adequately address how these estimation errors are handled in the algorithm or how they might affect the performance and safety of the method.
2. From the experimental results, the improvement over certain baselines is limited. For example, TRPO-Lag achieves smaller costs by the end of training and similar reward performance. Also in Table 1, CPO outperforms C-TRPO in many tasks. The experimental results do not convincingly demonstrate the superiority of C-TRPO over existing methods. The fact that TRPO-Lag achieves lower costs and CPO outperforms C-TRPO in several tasks raises questions about the practical benefits of the proposed approach. It is not clear from the experiments that C-TRPO offers a significant advantage in terms of both reward and constraint satisfaction, which is the core claim of the paper.

### Questions
1. Is the action dimension two for the toy MDP used in Figure 2? Then the y-axis should represent a_2? 
2. Line 167, D_k is not consistent with the previous Bregman divergence?

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
This paper presents a constrained optimization method called Constrained Trust Region Policy Optimization (C-TRPO), which modifies the geometry of the policy space based on safety constraints to create trust regions comprised solely of safe policies. They also provide an approximate implementation of C-TRPO. The main contribution is integrating safety constraints into policy divergence without introducing additional computational complexity or bias. The theoretical analysis of convergence is also provided. Experimental results show that C-TRPO achieves comparable policy performance and smaller constraint violations compared to common safe optimization methods.

### Strengths
## Originality and Significance

1) Safe RL is a crucial direction in reinforcement learning, which has significant implications for the application of reinforcement learning in real-world scenarios.

2) This paper proposed the approach C-TRPO to address the constrained optimization problem by modifying policy divergence, which appears to be novel.

## Quality and Clarity
1) This paper provides mathematical formulations for the main concepts needed to understand the approach. They also provide relevant theoretical results. 

2) The paper includes  a number of Figures which are helpful in understanding the main concepts in the paper. The use of figures (such as Figure 1 to illustrate the constrained KL - divergence in policy space) and examples (like the description of the optimization trajectories in Figure 2) enhances the clarity of the explanations.

3) The optimization implementation and approximation process is provided in detail.

### Weaknesses
1) The motivation and impact of integrating safety constraints into policy divergence are not sufficiently clear.

2) The core idea of this paper is to incorporate the constraints into the policy divergence, but according to the definition in equation (15), the divergence approaches $\infty$ when the policy approaches the constraint boundary, which results in the new divergence $D_c$ failing to satisfy the constraints, potentially leading to the absence of a solution. This is a critical issue because it directly impacts the optimization process and the ability of the algorithm to find a feasible solution. The paper does not adequately address how this issue is handled in practice, especially when the policy is very close to the constraint boundary.

3) The paper does not provide sufficient evidence to prove that the improved effectiveness of C-TRPO is solely due to the new policy divergence. It states that the enhanced constraint satisfaction compared to CPO is attributed to a slowdown and reduction in the frequency of oscillations around the cost threshold. This effect may also be partially due to the hysteresis-based recovery mechanism. However, the paper does not demonstrate whether introducing the same hysteresis-based recovery mechanism to CPOs would yield similar improvements. Without this control, it's difficult to isolate the impact of the proposed divergence modification.

4) Some of the theoretical explanations in the paper are not clear.

## Experiments
1) The paper does not include state-of-the-art baselines. It would be beneficial to compare C-TRPO with some of the latest safe RL algorithms to verify its effectiveness.

2) No ablation studies have been conducted to assess the roles of the core components in C-TRPO. Specifically, it is unclear how much each component contributes to the overall performance of the algorithm. For example, the impact of the modified divergence and the hysteresis-based recovery mechanism should be evaluated separately.

3) The observed results improvement is limited. The experimental results in the appendix indicate that the constraints in C-TRPO appear to be at the same level as in CPO, showing no smaller constraint violations (e.g., in safetycarbutton1 and safetyracecarcircle1). The lack of significant improvement in constraint violation raises concerns about the practical benefits of the proposed method.

4) No code is provided, raising concerns about reproducibility.

### Questions
1) In Proposition 3, when $\beta = 0$, $D_C = D_{KL}$ according to equation (9), why does C-TRPO approach CPO but not TRPO in this case？

2) In Proposition 4, according to the proof in the appendix,  $\mathbb{A}_c < \Psi^{-1}$, Why is the upper bound of C-TRPO smaller than that of CPO? Could the authors provide a more detailed explanation of this upper bound?

3) As the policy approaches the constraint boundary, $D_\phi$ in equation 15 will approach infinity, which may make Equation (14) unsatisfiable and results in no solution. How is this situation addressed in the proposed framework?

I am willing to raise my score if the authors can address my concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposes Constrained Trust Region Policy Optimization (C-TRPO) that aims to ensure safe exploration (always being safe during the training) without sacrificing performance in reward. Inspired by TRPO, the main idea of this work is to incorporate cost constraints into divergence to create safer trust regions. The divergence is obtained by mapping the policy onto its occupancy measure on the state-action polytope, where a safe geometry can be defined using standard tools from convex optimization.

### Strengths
Overall, this paper is well-written and well-presented.

The authors honestly point out and discuss the similarities and differences from the existing literature, and cite the paper correctly.

Some figures in the paper are intuitive such as Figure 2.

Overall, the mathematical proofs are sound.

I indeed have several concerns regarding this work, and I hope some of them can be answered or addressed after rebuttal.

### Weaknesses
Line 43. Does " without sacrificing performance" mean C-TRPO can achieve exactly the same performance as that of TRPO (unconstrained RL)? The experiment does not support this. Indeed, Figure 3 shows that C-TRPO is even a bit worse than CPO. (TRPO should be have even much higher return as it is unconstrained.)


Line 60-62, please provide more details that why model-based safe RL is less general, and what kind of stricter guarantees they provided.


Line 74-75. I am not sure if I argree with this. In the convex problems (which I understand may not hold in RL) and the problems where the policy parameterization is "perfect", there is no "bias". Solving the langragian-weighted objective is as good as solving the constrained RL. See the reference below

"Paternain, S., Chamon, L., Calvo-Fullana, M., & Ribeiro, A. (2019). Constrained reinforcement learning has zero duality gap. Advances in Neural Information Processing Systems, 32."


Line 76-82. The dicussion of trust region methods is too short. It is even shorter than the Penalty methods, while the paper focuses on the trust region methods.


Line 86-87. I don't understand. C-TRPO is an approximation of C-TRPO itself?


Line 112-120. Please make it clear in the formula that the expectation is w.r.t. initial state distribution, policy, and the transition function. "the expectations are taken over trajectorie" is too brief and not clear.


Line 188-189. If I remember correctly, doesn't CPO already inherit TRPO's update guarantees for reward and constraints?


Line 188. Refer to Figure 1 too early. There is no enough explaination in the main text or the caption of Figure, e.g., what is \beta, etc.

From Figure 1, why the proposed method is better than CPO? One is a clipped policy space, and the other one is a newly constructed policy space. It is hard to see which one is better intuitively. It also seems like C-TRPO has the same bounds as that of CPO (on page 7). The novelty is a bit limited in this sense.

To be honest, it is hard to tell if C-TRPO is better than baselines from Figure 3. Especially that it has lower return than CPO.

In general, I am a bit worried about the novelty of this work. It seems to me that there is not too much change compared to TRPO and CPO. Especially that Figure 1 does not clearly explain the difference. Why the fourth is better? Also, are these figures just hand-drawn intuition illustration? Are they true in practice?

Enhance the writing and fix typos, e.g., Line 63, Line 142,

### Questions
Please see my questions in the "Weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel policy optimization method for safe RL by constructing trust region of each iteration within the safe policy set for update.

### Strengths
By constructing trust region within the safe policies set, this method maintains competitive returns with less constraint violations during training. Since only construction of trust region is altered, this method still preserve convergence and policy improvement guarantee of original TRPO. This paper is technically solid and well-written. In the analysis part, author also provides a thorough explanation on connection between C-TRPO and CPO on policy update and constraint violation.

### Weaknesses
1, line 142 CMPD &rarr; CMDP
2, line 354 Proposition 1 refers to Theorem 1?

### Questions
1, For safety during training and convergence of constrained natural policy gradient, what kind of initial set assumptions are needed?
2, It would be interesting to see some comparison with hard constraints based approaches such as control barrier function based method[1, 2, 3], since similar notion of invariance seems to be brought up in section 4.2 to ensure safety during training. 


[1]Charles Dawson, Sicun Gao, and Chuchu Fan. Safe control with learned certificates: A survey of neural lyapunov, barrier, and contraction methods for robotics and control. IEEE Transactions on Robotics, 2023.\
[2]Yixuan Wang, Simon Sinong Zhan, Ruochen Jiao, Zhilu Wang, Wanxin Jin, Zhuoran Yang, Zhaoran Wang, Chao Huang, and Qi Zhu. Enforcing hard constraints with soft barriers: Safe reinforcement learning in unknown stochastic environments. In International Conference on Machine Learning, pages 36593–36604. PMLR, 2023b.
[3]Jason Choi, Fernando Castaneda, Claire J Tomlin, and Koushil Sreenath. Reinforcement learning for safety-critical control under model uncertainty, using control lyapunov functions and control barrier functions. arXiv preprint arXiv:2004.07584, 2020.

### Soundness
3

### Presentation
3

### Contribution
3
