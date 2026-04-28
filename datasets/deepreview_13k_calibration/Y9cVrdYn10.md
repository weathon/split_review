# Delay-Aware Reinforcement Learning: Insights From Delay Distributional Perspective

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Although deep reinforcement learning (DRL) has achieved great success across various domains, the presence of random delays in real-world scenarios (e.g., remote control) poses a significant challenge to its practicality. Existing delay-aware DRLs mainly focus on state augmentation with historical memory, ensuring that the actions taken are aligned with the true state. However, these approaches still rely on the conventional expected $Q$ value. In contrast, to model delay uncertainty, we aim to go beyond the expected value and propose a distributional DRL to represent the distribution of this $Q$ value. Based on the delay distribution, we further propose a correction mechanism for the distributional $Q$ value, enabling the agent to learn accurate returns in delayed environments. Finally, we apply these techniques to design the delay-aware distributional actor-critic (DADAC) DRL framework, in which the critic is the corrected distributional value function. Experimental results demonstrate that compared to the state-of-the-art delay-aware DRL methods, the proposed DADAC exhibits substantial performance advantages in handling random delays in the MuJoCo continuous control tasks. The corresponding source code is available at https://anonymous.4open.science/r/DADAC.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a reinforcement learning algorithm for environments with random delays. In real-world scenarios, feedback delays and actuator delays frequently occur due to limited computing resources and bandwidth constraints. Thus, it is crucial to develop a robust algorithm capable of performing well under challenging, low-bandwidth conditions. The proposed algorithm, DADAC, addresses these random delays through two primary components: (1) a Distributional Critic and (2) Delay-Aware Value Correction. The Distributional Critic enhances the agent's robustness by more accurately modeling the uncertainty associated with random delay environments. Meanwhile, Delay-Aware Value Correction adjusts the Bellman equation to account for the probabilistic nature of delays, helping the agent to accurately compute the returns.

### Strengths
The paper is well-structured and the contributions are clear.

The novel use of Delay-Aware Value Correction, which applies Bellman updates based on delay-adjusted expectations.

The proposed algorithm shows clear improvement compared to other approaches.

While many conventional methods only handle fixed delays, the proposed algorithm effectively handles random delays, making it a more practical solution.

### Weaknesses
Theorem 1 lacks rigorous proof.

More thorough ablation experiments are needed to illustrate how the Delay-Aware Value Correction approach contributes to handling random delays.

Based on my understanding, the proposed method requires prior knowledge of the delay distribution, which may limit its applicability.

### Questions
**[Q1]**
In Equation (3), $\gamma$ is expressed with exponential terms for each i. Why is $\gamma$  not expressed this way in Equation (5)?

**[Q2]**
In the proof of Theorem 1, for which distance is the distributional Bellman operator a contraction? Is it KL-divergence, Wasserstein distance, or Cramér distance? Given that your method relies heavily on KL-divergence for the critic loss (Line 200), it is natural to show that the distributional Bellman operator is a contraction with respect to KL-divergence; however, it does not (Bellemare, 2017). Could you elaborate further on the proof of Theorem 1?

**[Q3]**
Why does the "SAC+Value Correction" method perform so poorly on some tasks? It looks like the only difference between DADAC and SAC+Value Correction is whether or not a distributional critic is used. Especially in Humanoid-v4 and Ant-v4, there was no performance improvement at all.

It’s surprising that DSAC and "SAC+Value Correction" show pretty much the same performance across almost all tasks, even though DSAC naively uses the delayed observation. Could you explain why this is happening? It seems like Delay-aware Value Correction does not contribute significantly to DADAC.

**[Minor]**
Typically, many reinforcement learning algorithms conduct experiments using 10 random seeds. Why did you use 8 random seeds instead of 10? Was it to exclude outlier seeds for a more reliable comparison?


[1] Bellemare, Marc G., Will Dabney, and Rémi Munos. "A distributional perspective on reinforcement learning." International conference on machine learning. PMLR, 2017.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces an innovative approach that integrates distributional value function and value correction mechanism to handle random and unpredictable delay environments. Experiments are conducted on MuJoCo, comparing with baselines of State Augmentation-MLP and BPQL.

### Strengths
•	Overall, the concept presented in the paper is simple and straightforward. It is interesting to use a value correction mechanism targeting the value function.

•	The results show that DADAC generally surpasses two baselines, and achieves outstanding performance in some environments. The ablation study shows the effectiveness of both the distributional value function and value correction mechanism.

### Weaknesses
•	The authors mentioned that observation and action delays are considered. However, there is a lack of relevant experiments to support their claims. The absence undermines the credibility of the proposed method's robustness in scenarios where both types of delays occur simultaneously.

•	It seems that the authors do not discuss the reason why using the correction mechanism on the distribution of return, although the ablation study shows its effectiveness. Besides, this mechanism assumes precise estimation of delay dynamics, which might not be easy to obtain in practice.

•	The experiments are insufficient. Only two baseline models are compared, and the results are primarily visualized through training curves, lacking other forms of analysis. And the two random delay distributions are not sufficiently varied to capture the true random delays. Also, the algorithms employed in the ablation study can be replaced with more advanced ones.


Minor comments:

•	There is a typo "a gama distribution", it should be "a gamma distribution".

•	The presentation of related work could be more concise. Specifically, the discussion of prior methods could be less detailed in the introduction and moved to the related work.

### Questions
1.	Why focus on correcting the distribution of return rather than simply correcting the expected value of return? 

2.	How do you calculate $p_i$ in Equation (3)? If $p_i$ is constant, Equation (3) is essentially the same as the Bellman equation.

3.	In Experimental Results, how do you determine the mean of gamma distribution and double Gaussian distribution? Why do you use these two distributions? Can you use a different distribution with a random mean to re-implement the experiment? 

4.	Considering fixed delays are still common in the real world, can you implement DADAC under fixed delays?

5.	How does DADAC compare to a delay-free algorithm like robust RL?

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
This paper proposes a novel approach to solve the random delay problem in the delayed reinforcement learning by using distributional RL techniques to capture both state and action delays in the observation signals.

### Strengths
Author did a great job illustrating the motivation of the work, making it intuitive and easy to understand. Most parts of the paper is well-written and structured with logic coherence.

### Weaknesses
### Related Works
1, Missing some recent benchmarks: DC/AC[1], AD-RL[2], DIDA[3], VDPO[4], RTAC[5]

### Section 4
1, Assumptions should be clearly stated either in the prelim part or the start of this section.
2, the reward defined in Eq 2, 3, and 4 are all different, which is quite misleading for interpretation. 
3, Proof of Thm 1 is not rigorous: a) Reviewer expect the author to write out a few more steps on bellman property of newly defined bellman operator for both stationary and non-stationary delay distribution if stationarity of delay distribution is not universal. Otherwise Thm1 seems not be sufficient enough as an independent theorem. 
4, Following up to the convergence, it would be more technical solid to analyze optimality of the method, since convergence itself cannot provide any info on optimality. In [2,3,4], their optimality is investigated through study on the fixed point of optimization, which could be a possible direction of extension.  

### Experiments
1, The review suggests to involve more baselines for comparison aside from mentioned approaches, at least the recent works DIDA, AD-RL, DC/AC, etc. Current experiments seem not be sufficient enough to support author's arguments.
2, All the experiments are conducted in the deterministic MDP. It would be interesting to have some analysis/ablation studies on the stochastic setting, since the proposed method seems to support the stochastic MDPs.

### Questions
1, Is the delay distribution a required prior knowledge and also stationary? If so, what is the rationale picking gamma and double gaussian? What if an uniform distribution? \
2, How the prior delay distribution will affect the final return distribution of the DRL in both theoretical and empirical way, since no matter what the return of DRL seems to be assumed as a Gaussian? Only mean and log_std of Gaussian are affected or the way to choose value instead of expectation? \
3, Out of curiosity, the observation-delayed MDP have been proved to be the superset of the action-delayed MDP problem[7,8] also stated in Thm 2. Why not simplify the Eq (4) where both delay are considered to some form of Eq (3) for simplicity of unification?    


[7]Katsikopoulos, K. V. and Engelbrecht, S. E. Markov decision processes with delays and asynchronous cost collection. IEEE transactions on automatic control, 48(4):568–574, 2003.\
[8]Nath, S., Baranwal, M., and Khadilkar, H. Revisiting state augmentation methods for reinforcement learning with stochastic delays. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management, pp. 1346–1355, 2021.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a distributional delayed RL method named DADAC from the perspective of distributional RL. The theoretical result shows that the proposed Distributional Value Correction Bellman Equation has the convergence guarantee. The experimental results show that the

### Strengths
1. The motivation behind the proposed method is straightforward.
2. The theoretical analysis of the convergence makes sense.

### Weaknesses
The proposed method's motivation is straightforward. However, this paper ignores too many closely related references and/or important baselines. Therefore, the reviewer must point out these issues.

1.  The description should be unified across the paper. For instance, times $t+1$ (lines 232), $i$ timesteps (lines 239), $i$-th step (lines 240), and $(t+i+j)$-th time step (lines 250).
2.  There are multiple different definitions of the reward function. For instance, $r(s,a)$ in Eq.(1), $r(s,a,s')$ in Eq.(2), $r_{t+i}(s_t, a_t, s_{t+i})$ in Eq.(3). Especially, what's the meaning of $r_{t+i}(s_t, a_t, s_{t+i})$.
3.  Typo issues. $i$-th step (lines 240). $(t+i+j)$-th time step (lines 250).

1. The theorem 1 just shows the contraction property based on the existing literature, but the reviewer looks forward to the authors giving the analysis on the fixed point which can measure the performance of the proposed operator in the delayed RL settings.
2. The equivalent of different delays (theorem 2) has been proven by previous works [1, 2] experimentally and theoretically. The authors should highlight the difference with previous works if providing novel theoretical contributions.

1. The performance of BPQL[8] and State-Aug-MLP[9] is doubtful. The setting for the constant delayed RL methods is not fair somehow (using the expectation of the delay distribution). From the perspective of the reviewer, using the maximum delay is more fair. Specifically, based on the experimental results provided in the BPQL paper, the performance in Walker2d-v3 with the 9 constant delays is 4104.3, showing a serious performance drop (around 2700.0 in Walker2d-v4) in this paper (Figure 4).
2. DATS[5], DIDA[6], and AD-RL[7] should be considered as baselines in the constant delay settings.
3. RTAC[3], DC/AC[4] and VDPO[10] should be considered as baselines in the stochastic delay settings. In particular, VDPO[10] can be regarded as a recent work, the performance comparison is not compulsory.

### Questions
See Weakness.

### Soundness
3

### Presentation
1

### Contribution
2
