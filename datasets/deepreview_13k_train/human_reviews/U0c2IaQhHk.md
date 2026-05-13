# Exploring the State and Action Space in Reinforcement Learning with Infinite-Dimensional Confidence Balls

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Reinforcement Learning (RL) is a powerful tool for solving complex decision-making problems. However, existing RL approaches suffer from the curse of dimensionality when dealing with large or continuous state and action spaces. This paper introduces a non-parametric online RL algorithm called RKHS-RL that overcomes these challenges by utilizing reproducing kernels and the RKHS-embedding assumption. The proposed algorithm can handle both finite and infinite state and action spaces, as well as nonlinear relationships in transition probabilities. The RKHS-RL algorithm estimates the transition core using ridge regression and balances exploration and exploitation through infinite-dimensional confidence balls. The paper provides theoretical guarantees, demonstrating that RKHS-RL achieves a sublinear regret bound of $\tilde{\mathcal{O}}(H\sqrt{T})$, where $T$ denotes the time step of the algorithm and $H$ represents the horizon of the Markov Decision Process (MDP), making it an effective approach for RL problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a non-parametric online RL algorithm called RKHS-RL that overcomes the curse of dimensionality in RL by utilizing reproducing kernels and the RKHS-embedding assumption. The proposed algorithm can handle both finite and infinite state and action spaces, as well as nonlinear relationships in transition probabilities. The paper provides theoretical guarantees, demonstrating that RKHS-RL achieves a sublinear regret bound, making it an effective approach for RL problems.

### Strengths
The key contributions of the paper are:

1. **Theoretical Foundation**: It establishes a solid theoretical foundation for applying RKHS to reinforcement learning, providing a new perspective on how to handle the curse of dimensionality in such problems.

2. **Regret Bounds**: The paper presents a significant theoretical result by proving that RKHS-RL achieves sublinear regret bounds, specifically \( \tilde{O}(H\sqrt{T}) \), where \( T \) is the time step and \( H \) is the horizon of the Markov Decision Process (MDP). This indicates that the algorithm is efficient in balancing exploration and exploitation over time.

3. **Experimental evaluation**: The paper evaluates the performance of finite-dimensional RKHS-RL through simulations. The experiment examines the asymptotic property of the average value, which indicates that the solution of the function is stable. Additionally, the regret bound proposed in the paper is evaluated. The results show that the regret is bounded and align with Theorem 1.

### Weaknesses
1. **Empirical Evidence**: The paper could be strengthened by including more empirical evidence to support the theoretical findings. This includes detailed comparisons with existing methods, such as those mentioned in the references, to demonstrate the practical effectiveness of RKHS-RL. The current evaluation is limited to demonstrating asymptotic properties and regret bounds, but lacks a thorough comparison to established RL algorithms in standard benchmark environments. For instance, the paper could benefit from comparisons with algorithms like Deep Q-Networks (DQN) or Proximal Policy Optimization (PPO) on common RL tasks.

2. **Scalability and Computation**: While the theoretical aspects are strong, the paper does not thoroughly address the scalability of the algorithm, especially considering the potential growth of the kernel matrix, which is a known issue in kernel methods as the number of state-action pairs increases. The paper needs to discuss the computational complexity of the kernel ridge regression step and how it scales with the number of samples and the dimensionality of the RKHS. The practicality of infinite-dimensional confidence balls in real-world applications is not addressed. The paper could improve by discussing how this aspect of the algorithm translates to practical implementations and what trade-offs might be involved. Specifically, the method for solving the maximization problem in equation (4) needs to be elaborated upon, including its computational cost and any approximations used.

3. **Generalization and Application**: The paper would benefit from a discussion on the generalization capabilities of RKHS-RL across different domains and a demonstration of its application to real-world problems, which are areas of interest in the references. The theoretical results are promising, but the paper lacks evidence showing how the algorithm performs on tasks with different state and action spaces, or with different transition dynamics. It would be beneficial to see results on a variety of environments to assess the robustness and adaptability of the proposed method.

### Questions
0. **Typo**: Is it a typo in section 4 simulation?
> we observe that $\operatorname{Regret}(T) / N^{2 / 3}$ is bounded.
1. **Assumptions of RKHS-Embedding**:
Could you elaborate on the conditions under which the RKHS-embedding of transition probabilities is a valid assumption? Are there known classes of RL problems where this assumption may not hold?
2. **Algorithmic Scalability**:
How does the RKHS-RL algorithm scale with the dimensionality of the state and action spaces in practice? Are there computational constraints that could limit its application to large-scale problems?
3. **Comparison with Existing Methods**:
The paper would benefit from a comparative analysis with other RL algorithms. Have you conducted such comparisons, and if so, could you share these results?
4. **Hyperparameter Sensitivity**:
How sensitive is the RKHS-RL algorithm to the choice of hyperparameters, including the selection of kernels and regularization parameters in ridge regression?
5. **Practical Implementation**:
Can you provide insights into the practical implementation of infinite-dimensional confidence balls? How does this concept translate into a computationally feasible algorithm?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a model-based algorithm for episodic MDP whose transition probability is embedded in a given reproducing kernel Hilbert space. The assumption of RKHS-embedding of transition probability can handle non-linear relationships in transition probability. The proposed algorithm (RKHS-RL) estimates the transition core using ridge regression based on the collected data, and constructs an optimistic action-value function based on the infinite dimensional confidence ball. The proposed method achieves a dimension independent regret bound of $O(H \sqrt{T})$ where $H$ is the horizon length, $T$ is the total number of interaction between the agent and the environment. Furthermore, the authors confirm the performance of finite-dimensional RKHS-RL through experiments in a simple tabular setting.

### Strengths
- The motivation for the problem addressed in this paper is well-explained, drawing from the literature and related work. Additionally, the organization of the paper is appropriately structured to facilitate understanding.

- The RKHS-embedding of transition probability is useful in modeling non-linear transition probabilities for state-action pairs. The author has demonstrated that the regret bound of the proposed method can achieve dimension-free sub-linear regret.

### Weaknesses
 - The computational complexity of the proposed method has not been addressed. In “Introduction”, the authors mentioned that the proposed model can handle infinite state and action spaces. However, it seems that the computation in Algorithms 1 and 2 is heavily influenced by the size of the state-action space. It would be helpful to specify how efficient the proposed method is both statistically and computationally compared to previous algorithms, particularly for infinite state spaces.

- The proposed algorithm appears similar to KernelMatrixRL (Yang & Wang, 2020). While the authors mentioned that the RKHS-embedding setting poses significant challenges compared to approach of Yang & Wang (2020), it would be beneficial to explain in detail what specific challenges arise and how they were addressed using mathematical techniques in the paper.

- There is a gap between the settings discussed in the paper and the simulations. The proposed method can handle settings that previous approaches, such as tabular MDPs, linear MDPs, and parametric MDPs, cannot. However the experiments were conducted in a simple tabular setting. Additionally, it is anticipated that Q-learning or SARSA would perform significantly better in the current experiments. It would be valuable to include comparisons with other baseline algorithms.

### Questions
1. How can the proposed method be applied to a continuous state-action space? The current planning approach seems challenging to implement in a continuous state-action space.

2. How was it possible to achieve a tight regret bound with respect to H when compared to the regret bound of Yang & Wang (2020)?

3. The regret bound of RKHS-RL does not include the effective dimension of the kernel. In that case, does the regret not depend on dimension even when using a finite-dimensional kernel? What is the key technique to eliminate dimension dependence when compared to KernelMatrixRL in Yang & Wang (2020) ?

4. In the finite-dimensional case of RKHS-RL, how is the regularity bound in Assumption 2 defined? Can we assume a bound independent of the size of the state-action space in finite-dimensional case?

5. Why does Figure 1-(b) show negative values for regret?

6. How does the following inequality in the Proof of Lemma 2 hold? 
: $$ H || \Phi\_{n,h} \tilde{\circ} (M^* - M'\_n) ||_1 \le H || \Phi\_{n,h} \tilde{\circ} (M^* - M'\_n) ||_2 $$

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies online RL where (1) both state and action spaces are assumed to be infinite and (2) the transition kernel is approximated by an RKHS. The paper proposes a model-based algorithm to directly optimize over the space of transition kernels and provides a concentration analysis for the concentration of the transition kernel. The resulting algorithm is shown to have $\tilde{O}(\sqrt{T})$ regret. Simulation studies are included.

### Strengths
- The paper proposes a possibly computationally efficient algorithm for RL with function approximation when state and action spaces are infinite.
- Assuming that the transition kernel itself is drawn from an RKHS seems an interesting idea that has not been explored fully in prior literature.

### Weaknesses
1. The proof appears to be incomplete and is hard to follow. It is not clear how the concentration analysis in A.2 helps the regret bound in A.1. Specifically, the connection between the confidence bound on the transition kernel and its impact on the regret is not clearly established. It remains unclear how "the sum of the right-hand side" is bounded in Lemma 3, without invoking the later lemmas. There is no clear indication of how an elliptical potential lemma or similar technique is used to bound the sum of the kernel norms, which is crucial for obtaining the regret bound.
2. Some related works appear to be missing, such as earlier works on sample-efficient RL for low-rank MDPs or MDPs with bounded Bellman-Eluder dimension, or recent works such as admissible Bellman characterization.
3. Is it assumed, perhaps implicitly, that the reward function is known beforehand? The paper appears to estimate the transition kernel only and does not discuss how the reward function $r$ is estimated. It would be surprising if the paper can obtain the regret guarantee without any regularity assumptions on the reward function. The assumption that the reward function is known is not explicitly stated, which is a significant oversight given that most RL algorithms need to estimate the reward function or make assumptions about it.
4. The algorithm design appears to be similar to earlier works on RL with general function approximation: it appears to be a specialization of earlier algorithm such as OLIVE for when (1) only the transition is estimated and (2) the function class is known to be an RKHS, which allows the optimization problem to be written directly over the space of $M$. The paper does not adequately discuss how the proposed approach differs from simply adapting existing algorithms to the RKHS setting.
5. Algorithm 2 requires $S$ and $A$ to be finite, which is not assumed by Section 3.4. This discrepancy between the theoretical setup and the simulation is a concern.
6. The remark after Algorithm 1 is a bit misleading. Without any assumption on $r$, I am not sure if $\max_{a} Q(s, a)$ can be done efficiently. Specifically, if $r(s,a)$ is non-concave or non-convex in $a$, and the action space is continuous, this optimization problem is not trivial and may not be solvable efficiently.

### Questions
1. Can the authors provide more details on the proof?
2. Can the authors discuss how the paper relates to additional prior works not discussed in the paper?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
