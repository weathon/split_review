# Learning from Sparse Offline Datasets via Conservative Density Estimation

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Offline reinforcement learning (RL) offers a promising direction for learning policies from pre-collected datasets without requiring further interactions with the environment. However, existing methods struggle to handle out-of-distribution (OOD) extrapolation errors, especially in sparse reward or scarce data settings. In this paper, we propose a novel training algorithm called Conservative Density Estimation (CDE), which addresses this challenge by explicitly imposing constraints on the state-action occupancy stationary distribution.  
  CDE overcomes the limitations of existing approaches, such as the stationary distribution correction method, by addressing the support mismatch issue in marginal importance sampling. 
  Our method achieves state-of-the-art performance on the D4RL benchmark. Notably, CDE consistently outperforms baselines in challenging tasks with sparse rewards or insufficient data, demonstrating the advantages of our approach in addressing the extrapolation error problem in offline RL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work the authors propose CDE, an offline algorithm that builds upon a similar formulation as that of the DICE method of Nachum et al. In DICE the state-action distribution is optimized in order to maximize the reward under that distribution subject to an f-divergence regularization between the visit distribution and the empirical distribution under observed data. In additiona this optimization problem is constrained such that the state-action visit distribution is a valid discounted distribution under the initial-state and transition model of the MRP. Where CDE departs from DICE is in introducing an additional constraint such that the state-action distribution function evaluated at any state-action is less than a multiplicative factor of epsilon of some alternative distribution mu defined to have support only over out-of-distribution actions, and where mu is restricted to have the same marginal state distribution as the empirical distribution. Given this formulation the state-action distribution can then be optimized and the policy implied by this distribution can be extracted from the distribution. Additionally the authors extend the f-divergence to include an f-divergence with an extended distribution which mixes the empirical and mu distribution which a trade-off factor.

Based on these results the authors present some theoretical results bounding the importance ratio and bound the performance gap. The authors also provide a number of results on maze2d tasks and sparse mujoco tasks, predominantly showing that their method outperforms other comparable offline RL algorithms.

### Strengths
Overall the paper was quite good and the algorithm was well presented, albeit quite dense. The theoretical results do add to the paper (although I'm not sure how much) and the results were quite good and well presented.

### Weaknesses
Overall the paper was good and from my perspective merits inclusion at ICLR. My only real criticism of the work lies in its presentation, which although good I felt was dense. And the precise differences with e.g. DICE could have been made more clear, i.e. I would have liked to see more discussion of the effects of the additional constraint. To that end I'm not sure how much was added by the theoretical contributions of this work which could have been rather spent on explaining these differences at a higher level. And to be clear, I think the theorem(s) are useful, but since the proof itself and some of the underlying assumptions could not be included due to space constraints I'm not sure if these would not have been better moved into the appendix as a whole.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new offline RL method, called Conservative Density Estimation (CDE). It builds upon the DICE work by utilizing the state-action occupancy stationary distribution. However, the DICE type work requires the assumption on the concentrability, and the boundedness of the IS ratio for stable training. This paper tries to address this by introducing pessimism on the state-action stationary distribution, via a similar principle like conservative Q-learning.

### Strengths
- This paper points out the two type of approaches for offline RL, conservative Q-value based, which might perform worse under sparse reward setting due to iterative Bellman update; and DICE based, which implicitly relies on the concentrability. The proposed method nicely combines these two approaches, via a pessimism approach on the state-action stationary occupancy, which is a neat idea especially on the sparse reward setup.

- The paper is very well-written and easy to read. The method is very well-motivated, and clearly described, from policy evaluation to policy extraction. It also shows theoretical guarantees regarding to the concentrability bound, as well as performance gap. 

- The experiments on sparse reward settings and small data regime is interesting, and support the CDE's effectiveness, especially at the sparse reward setup.

### Weaknesses
 - Some parts of the method need to be dived into more details, for example, the CDE policy update happens when the value function converges. This also marks a difference compared with classical actor-critic methods, is it a key component in improving the empirical performance? The paper does not adequately explore the impact of this design choice on the overall performance or convergence behavior. It's unclear whether this 'warm-up' stage is critical or simply a practical trick.

- More hyper-parameters introduced by the algorithm, such as the max OOD IS ratio, the mixture coefficient, etc. The ablation study on the mixture coefficient is interesting, demonstrating the robustness and giving some empirical guidelines on how to pick them. However, the study of max OOD IS ratio, though interesting, it does not provide any meaningful guidelines on how to choose them for various environments and applications. The paper lacks a clear methodology for selecting this crucial parameter and its impact on the final performance.

- A clear understanding between CDE and CQL is missing, one is pessimism on the state-action state-action occupancy stationary distribution, the other is on the value function. Figure 2(d) only probably only shows the performance of CQL for a fixed pessimism-coefficient, it would be great to compare these two methods in detail, both theoretically and empirically. The comparison should include a sensitivity analysis of CQL's pessimism coefficient and a discussion on how the different forms of pessimism affect the learning dynamics and final policy quality. The paper should also discuss the theoretical relationship between the two approaches, particularly how they relate to the Bellman optimality.

### Questions
See Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a density estimation-based offline RL algorithm that aims to incorporate the strengths of value penalization-based offline RL methods and DICE-based offline RL methods. The proposed method outperforms the certain baselines in considered sparse reward D4RL tasks.

### Strengths
- The proposed method outperforms the considered baselines significantly in maze2d tasks.
- The motivation which is to achieve the best of both worlds (between the value penalization methods and the DICE-based methods) is solid.

### Weaknesses
 - Some clarifications are required in the introduction section. 1) "pessimism-based techniques may be prone to over-pessimism, especially in high-dimensional state-action spaces" => why is over-pessimism a bigger problem for high-dimensional state-action spaces? Specifically, the curse of dimensionality makes accurate density estimation more difficult, but it's not clear how this directly translates to *more* over-pessimism compared to lower-dimensional spaces. The connection between estimation error and over-pessimism needs to be explicitly stated and justified. 2) "regularization methods often struggle with the tuning of the regularization coefficient" => Why does the author think this is true? The cited paper seems to be about DICE and not about regularization methods. Additionally, IQL (which is a baseline considered in the paper) uses the same hyperparameters for experiments in the same domain, just like the proposed method.
- The considered tasks are not thorough. First, there are no experiment results on D4RL Gym *-medium-replay datasets, which contain trajectories that vary significantly in performance. These datasets can test if the proposed method can handle datasets with mixed quality. Second, on Adroit, I am curious on why the authors did not include the *-cloned datasets while including *-human datasets. Third, some important tasks with sparse reward are missing: Antmaze and Kitchen. These tasks are much harder than simple maze2d and at the same time have sparse rewards.
- Some important baselines are missing. To name a few, DecisionTransformer [1] and Diffuser [2] also claim they have strength in the sparse reward settings.

### Questions
- On sparse-MuJoCo tasks, how does the proposed method and the baselines perform if you change the cut-off percentile (which is currently 75)?
- How does the proposed method perform compared to the baselines on dense reward settings?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an Offline RL algorithm called Conservative Density Estimation (CDE) incorporating pessimism within the stationary distribution space. Extensive empirical study shows that CDE outperforms existing baselines in both the sparse-reward settings and the scarce-data settings.

### Strengths
The authors present a novel method of mixing pessimistic-based methods with DICE-style methods. Unlike other pessimistic methods that balance pessimism using a hyperparameter called a penalty coefficient, CDE finds the optimal balance based on theoretical grounds. The paper also introduces a new way to convert dense-reward MuJoCo tasks into a sparse-reward setting based on the trajectory return. Together with the scarce-data setting experiments, the two additional benchmarks can help test the robustness of offline RL algorithms. Finally, the arguments provided by the authors are mathematically sound.

### Weaknesses
1. §3.2.1 states that the strong duality holds due to Slater's condition. The fact that the optimization problem of our interest satisfies Slater's condition does not seem trivial. Specifically, under stochastic transition dynamics, the Bellman flow constraint may not hold for the empirical dataset distribution $d^{\mathcal{D}}$ because the left-hand side (LHS) represents a discrete distribution derived from sampled transitions, while the right-hand side (RHS) involves a continuous distribution due to the stochastic transition function. This discrepancy raises concerns about whether $d^{\mathcal{D}}$ can truly satisfy the constraint, which is a requirement for Slater's condition to hold.

2. The RHS of (7) may not exist. For example, $\tilde{A}(s, a)$ might be negative.

3. According to §B.2.2, the authors set $d^*(s)$ as a uniform distribution on the state in the successful trajectories. It would have been better if this explanation were included in the main paper. I am doubtful that this distribution will be close to $\tilde{w}^*(s, a)\hat{d}^{\mathcal{D}}(s, a)$, though.

### Questions
1. How are the OOD actions sampled? Do you just sample a random action and reject it if it is in distribution?

2. Does Slater's condition also hold for optimization problems dealing with infinite-dimensional vectors (i.e., functions)?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
