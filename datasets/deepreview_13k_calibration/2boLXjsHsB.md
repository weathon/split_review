# Multi-Objective Reinforcement Learning for Forward-Backward Markov Decision Processes

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
This work introduces the notion of Forward-Backward Markov Decision Process (FB-MDP)
for multi-task control problems. In this context, we devise a novel approach called Forward-Backward Multi-Objective Reinforcement Learning (FB-MORL).
Specifically, we analytically characterize its convergence towards a Pareto-optimal solution and also empirically evaluate its effectiveness.
For the latter, we consider a use case in wireless caching and perform several experiments to characterize performance in that context. Finally, an ablation study demonstrates that FB-MDP is instrumental to optimize rewards for systems with forward-backward dynamics.
The outcomes of this work pave the way for further understanding of multi-objective RL algorithms for FB-MDPs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Forward-Backward Multi-Objective Reinforcement Learning (FB-MORL), an approach for addressing a special family of multi-task control problems. It presents the concept of the Forward-Backward Markov Decision Process (FB-MDP). Unlike the existing RL algorithms, this work primarily focuses on environments that cannot be modeled solely by a forward Markov decision process. This paper derives the policy gradient in the FB-MDP setting and proposes FB-MOAC, a stochastic actor-critic implementation of the policy gradient approach. In the policy update step, the author employs Monte Carlo Sampling (MCS) with an exponential moving average called episodic MCS-average to estimate the gradient. The proposed method is evaluated in wireless communication environments, and an ablation study highlights the importance of backward optimization and episodic MCS-average. The paper also provides theoretical analysis of FB-MOAC, demonstrating its convergence capability.

### Strengths
- The main contributions of this paper are mainly two-fold:
1. To the best of my knowledge, this paper offers the first formal study on the forward-backward MDPs and the resulting learning problem.
2. Accordingly, from the perspective of multi-objective RL, this paper proposes FB-MOAC, which is a policy-gradient-based actor critic method. This is built on the derived policy gradient in the FB-MDP setting.
- Convergence results of FB-MOAC are also provided (convergence to optimal total return under strict convexity and convergence to a local optimum in the general case).
- FB-MOAC is empirically evaluated on a hybrid delivery environment against a randomized baseline. A brief ablation study is also provided.

### Weaknesses
 - The formulation of forward-backward MDP could be further justified. Despite that there is a whole line of research on backward SDEs, the use of the coupled forward and backward dynamics in the context of Markov processes and RL is quite rare and shall be justified. A motivating example early on in the paper would be helpful for readers to better appreciate this problem setting. Specifically, the paper should elaborate on why a standard forward MDP is insufficient to model the problems they are targeting. The current explanation lacks a concrete example that clearly demonstrates the necessity of the backward component.

- The FB-MOAC algorithm is mainly built on Lemma 3.1, which suggests a first-order iterative descent approach to solve the general multi-objective optimization problems. However, this does not guarantee that an optimal policy could be achieved under FB-MOAC in general. While the authors did provide some convergence results in Section 5.1 and Appendix B, the best that FB-MOAC could achieve is convergence to a first-order stationary point (as the RL objective in general is not strictly convex). The paper should more clearly acknowledge this limitation and discuss its implications for practical applications. It would be beneficial to analyze the conditions under which the algorithm might converge to a sub-optimal solution and how this might affect the performance.

- Based on the above, one important missing piece is the characterization of an optimal policy or the optimal value function in FB-MDPs. In the standard forward MDP, the widely known Bellman optimality equations offer a salient characterization of what an optimal value function and an optimal policy shall look like. It remains unclear what such conditions shall look like in the FB-MDP setting. In my opinion, further efforts on this is needed to design an algorithm that provably finds an optimal policy in general. The paper should provide a more rigorous analysis of the theoretical properties of FB-MDPs, including a discussion on the existence and uniqueness of optimal policies.

- Another related concern is on the policy class needed in the FB-MDP setting. In the standard forward (tabular) MDP setting, it is known that the class of (randomized) stationary policies is large enough to contain an optimal policy. However, it is rather unclear whether this is still true in FB-MDPs. However, this paper appears to directly presume that the policy is stationary. More discussion on this would be helpful and needed. The paper should justify the use of stationary policies in the FB-MDP setting, possibly by providing a theoretical argument or empirical evidence.

- Regarding the experiments of the hybrid delivery problem, while I could understand that this problem could be formulated as an FB-MDP (for keeping track of the latency), an alternative forward MDP formulation could still be used to solve this problem (for example, instead of keeping track of the latency of file n, the agent could look at the “time since the first transmission of file n”, which could be compatible with the standard forward MDP). Then, one natural question is: is there any benefit of using an FB-MDP instead of the (simpler) forward MDP formulation? The paper needs to provide a clear explanation of the advantages of using an FB-MDP formulation over a standard forward MDP in the context of the hybrid delivery problem. The current justification is not strong enough to convince the reader of the necessity of the proposed approach.

- Moreover, the experimental results are not very strong for two reasons: (1) It is unclear how far the performance of FB-MOAC is from an optimal policy (this is also related to one of my comments above). (2) The baseline (a simple randomized policy) is certainly not very strong. Given the plethora of research on unicast and multicast control in the wireless networking community, I would expect that there are some more competitive benchmark methods included in the experiments, either rule-based or learning-based. Also, it would be good to strengthen the experimental results by evaluating FB-MOAC on other RL environments. Otherwise, the application scope of FB-MOAC is somewhat limited.

### Questions
Please see the above for the main questions.

Here are some additional detailed questions:
- In Eq. (18), shall the 1/2 in the second term be just 1 (as Ln(t) denotes the latency)?

- While the whole Section 5.2.1 is used to describe the environment setup, it is still somewhat a bit difficult to parse (probably due to the use of terminology). For example, 
    - How to define the event of multicast outage? 
    - And accordingly how to derive the probability of this event? 
    - How does the “request process” of each user work? 

- The referencing numbers in the caption in Figure 1 and Figure 2 appear misplaced.

---------- Post-Rebuttal ----------

Thank the authors for the detailed response. Some of my concerns have been eased or addressed (e.g., added motivating examples for justifying FB-MDP and additional baselines).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses sequential tasks that consider not only forward MDPs where states follow forward dynamics but also backward dynamics from which trajectories evolve in reverse-time order. In this setting, there can be conflicts between rewards from forward dynamics and those from backward ones. In this Forward-Backward Markov decision process (FB-MDP) setting, the authors propose an on-policy multi-objective reinforcement learning algorithm called Forward-Backward Multi-Objective Actor-Critic (FB-MOAC). The core idea is to use a multi-objective optimization technique so that the cumulative vector reward sum becomes a Pareto-optimal point. Numerical results show that the proposed FB-MOAC algorithm is applicable in the FB-MDP setting.

### Strengths
- This paper addresses sequential tasks on the Forward-Backward Markov decision process (FB-MDP) setting, which seems to provide a new perspective in (multi-objective) reinforcement learning.
- The paper provides some mathematical proofs regarding convergence to Pareto-optimal points.
- Based on previous works (Lemma 1), the proposed methodology gives technical soundness.

### Weaknesses
1. The paper is not easy to follow. There are many notational errors in the core formula. I recommend checking them to improve the overall readability.

2. The most critical weakness is that there are no baseline algorithms to compare with the proposed method in experiments. Readers cannot verify how much the FB-MOAC performs well.

3. Another issue is about the setting: FB-MDP. When can we consider this backward dynamics setting? It was hard to understand. Could the authors provide an example or detailed explanation regarding the necessity of considering backward dynamics?

4. Related to the above 3, the experiment part is hard to understand. Readers may not be familiar with wireless communication areas. Providing high-level pictures describing the environment is recommended.

5. Regarding reproducibility, it would be better to provide anonymous source code to verify the proposed algorithm.

6.  There is another issue about Lemma 1 which is the core foundation of FB-MOAC. Lemma 1 tells us about the Pareto-optimal convergence, but not about 'which Pareto-optimal point' to converge to. In most multi-objective RL works, there is a preference function (either linear or non-linear) that the designer cares about. Can Lemma 1 explain the characteristics of the converged Pareto-optimal point?

7. Conditions of Corollary 1 should be stated more precisely. There are inverse matrix operations and KKT conditions should be carefully considered.

8. Does saving past model parameters raise any memory issues of the algorithm?

### Questions
Please check the above weakness part. Additional questions are as follows.

6.  There is another issue about Lemma 1 which is the core foundation of FB-MOAC. Lemma 1 tells us about the Pareto-optimal convergence, but not about 'which Pareto-optimal point' to converge to. In most multi-objective RL works, there is a preference function (either linear or non-linear) that the designer cares about. Can Lemma 1 explain the characteristics of the converged Pareto-optimal point?

7. Conditions of Corollary 1 should be stated more precisely. There are inverse matrix operations and KKT conditions should be carefully considered.

8. Does saving past model parameters raise any memory issues of the algorithm?

### Soundness
3 good

### Presentation
2 fair

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
In this paper, the authors have devised a new approach known as Forward Backward Multi-objective Reinforcement Learning (FB-MORL). The convergence behavior of the proposed approach to Pareto optimality is analyzed. The effectiveness of the proposed approach is evaluated on a use-case from wireless caching.

### Strengths
A new approach is proposed for FB-MORL. A real-world wireless communication problem has been taken as a use case of the proposed methodology.

### Weaknesses
The presentation of the paper needs to be improved. A small real-world example illustrating FBMDP would help strengthen the motivation. The algorithm may be computationally expensive.

The forward and backward processes' interaction through the action space is not clearly explained. The paper states that the backward dynamics in the backward Markov Decision Process (MDP) result in a known final state; however, the relationship to a forward MDP with an absorbing state is not adequately addressed. The analysis in Section 3.2 does not sufficiently highlight the conflict between forward and backward trajectories. The analysis seems to replicate existing forward MDP results for backward MDP, and the additional challenges in obtaining the convergence results are not clearly articulated. The choice of $\gamma \in (0,1]$ in Equation (2) is not well-justified, especially considering that $\gamma=1$ is often more appropriate for finite $T$. In Equation (3), the conditioning of $\pi_\theta$ on $s_t$ rather than $y_t$ requires further explanation. The computational feasibility of calculating $\beta_f^*$ and $\beta_b^*$ at each iteration is questionable. It is unclear why equation (18) cannot be expressed as a forward MDP, and the paper does not adequately explain why the problem in 5.2.1 cannot be modeled with forward-only dynamics. The FB-MOAC algorithm should be moved from the appendix to the main text, and the additional challenges in obtaining the analytical results in Section 5.1 compared to the forward MDP only case need to be clarified.

### Questions
My comments are as follows:

1.	How do the forward and backward processes conflict with each other through the action space? A small real-world example illustrating this would help strengthen the motivation.

2.	The authors stated that the backward dynamics in the backward Markov Decision Process (MDP)  result in a known final state. Can’t it be analyzed by a forward MDP with an absorbing state?

3.	In Section 3.2, it is considered that the backward and forward trajectories conflict with each other. However, the analysis does not reflect that. Rather, it seems the analysis presented in the paper replicates the existing forward MDP results for backward MDP. For example, Lemma 4.1 is just an extension of (5). What are the additional challenges in obtaining the convergence results?

4.	In Equation (2), why is $\gamma \in (0,1]$? Usually for a finite $T$, $\gamma=1$ is more appropriate. 

5.	In Equation (3), why is the $\pi_\theta$ conditioned on $s_t$ and not on $y_t$? 

6.	The computation of  $\beta_f^*$ and $\beta_b^*$ needs to be done at every iteration. Is it computationally feasible?

7.	Can’t equation (18) be alternatively expressed as a forward MDP? In other words, can the problem in 5.2.1 be modeled with forward-only dynamics? 

8.	The presentation of the paper needs to be improved. The  FB-MOAC algorithm should be moved from the appendix to the main text since this is one of the main contributions of the paper. What are the additional challenges in obtaining the analytical results in Section 5.1 compared to the forward MDP only case?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
