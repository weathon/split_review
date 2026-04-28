# SEMDICE: Off-policy State Entropy Maximization via Stationary Distribution Correction Estimation

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
In the unsupervised pre-training for reinforcement learning, the agent aims to learn a prior policy for downstream tasks without relying on task-specific reward functions. We focus on state entropy maximization (SEM), where the goal is to learn a policy that maximizes the entropy of the state's stationary distribution. In this paper, we introduce SEMDICE, a principled off-policy algorithm that computes an SEM policy from an arbitrary off-policy dataset, which optimizes the policy directly within the space of stationary distributions. SEMDICE computes a single, stationary Markov state-entropy-maximizing policy from an arbitrary off-policy dataset. Experimental results demonstrate that SEMDICE outperforms baseline algorithms in maximizing state entropy while achieving the best adaptation efficiency for downstream tasks among SEM-based unsupervised RL pre-training methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The work proposed a novel state entropy maximization method called SEMDICE for RL pre-training. SEMDICE addresses the limitations of existing methods by directly optimizing the stationary distribution space rather than the policy or Q-function space, utilizing arbitrary offline samples. The study demonstrates that SEMDICE converges to the optimal SEM policy in tabular MDP experiments and is more efficient in RL policy pre-training compared to existing data-driven (i.e., SEM-based) unsupervised RL methods.

### Strengths
* The proposed algorithm SEMDICE is a novel method suitable for off-policy training.
* SEMDICE demonstrates efficient convergence in tabular MDP experiments and outperforms existing methods in RL policy pre-training.
* Theoretical analysis is provided to demonstrate the efficacy of the SEMDICE.

### Weaknesses
 * The hyperparameter $\alpha$ may have a significant impact on the results.
* Though experiments in tabular RL and continuous state spaces are conducted, it does not address high-dimensional data (such as image-based tasks), which may pose computational complexity issues. This could be a potential direction for future improvements.

### Questions
* Including the algorithm flowchart within the main text would enhance readers' understanding of the algorithm.
* Is the algorithm sufficiently robust to the hyperparameters, especially the $\alpha$? Is there any method can be employed to mitigate adverse effects?
* How is the computational efficiency in high-dimensional data?

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
4

### Summary
This paper focuses on developing an effective pretraining policy in an unsupervised reinforcement learning setting by maximizing state entropy. Previous methods either utilized k-nearest neighbors (kNN)-based particle entropy estimation, which is biased, or were based on the on-policy algorithms from Hazan et al. (2019), which are sampling inefficient. The authors build on the DICE (Stationary Distribution Correction Estimation) series of methods to propose a new off-policy entropy maximization approach named SEMDICE. The paper demonstrates the advantages of their method on benchmarks including Gridworld, MountainCar, and URL Benchmark.

### Strengths
The motivation is well. The particle entropy method operates off-policy but optimizes the entropy of the replay buffer rather than the target policy. In contrast, the method proposed by Hazan et al. (2019) is on-policy but sample inefficient. Using DICE-like approaches can address these issues.

While the original DICE framework focuses on Linear MDPs (where the objective function is linear with respect to the state visitation distribution), this paper examines Convex MDPs (where state entropy is convex with respect to the state visitation distribution). This shift introduces differences from the original DICE algorithm, such as the emergence of an exponential term. To mitigate gradient explosion, the paper employs a log-sum-exponential replacement for this term and theoretically demonstrates that this substitution does not significantly impact optimality.

Experimental results indicate that the proposed method, which emphasizes state coverage, outperforms other methods, thereby validating its effectiveness.

### Weaknesses
1. The work of Hazan et al. (2019) is a primary reference, yet the paper lacks a comparative analysis of its experiments, particularly like the MountainCar experiment.
2. The implementation details are vague. For instance in Equation 56 of Appendix, the paper estimates $−log d^D(s)$ using a k-nearest neighbors (kNN) based particle entropy estimation, which introduces bias and contradicts the paper's motivation. This needs clarification and should be discussed in the main text. Specifically, the use of kNN for density estimation, while common, is known to be biased, and this bias is not addressed in the paper. The paper claims to maximize the entropy of the target policy's state distribution, but the kNN estimation is based on samples from the replay buffer, which can be significantly different, leading to a mismatch between the objective and its approximation. The paper needs to provide a more detailed analysis of how this bias affects the overall performance and convergence of the algorithm.
3. For readers unfamiliar with DICE, the paper is quite opaque. I strongly recommend that the authors organize the theoretical results and the main derivation process similarly to Appendix B in [1], rather than presenting a cumbersome Theorem (e.g., Theorem 3.2).

**Other Typos:**
- Line 49: Missing space before "However."
- Line 296: "inimizing" should be corrected to "minimizing."
- Line 298: The numbering (1), (2) is likely to cause confusion.
- Appendix A: The meaning of $d_+$ is not explained.

### Questions
1. This paper addresses Convex MDP problems (where state entropy is convex with state visitation distribution). Is there potential for applying the DICE method to other Convex MDP problems, such as diverse skill discovery, as summarized in Table 1 of [2]?
2. The experimental results indicate that the CIC method performs poorly in state coverage during the pretraining phase but excels in downstream task fine-tuning. This suggests that maximizing state entropy may not be the optimal pretraining strategy. Could you provide clarification on this point?

Reference：

[2]  Reward is Enough for Convex MDPs. NeurIPS 2021.

I am willing to increase my score, if the authors can further address my concern.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the challenge of unsupervised pre-training in reinforcement learning, aiming to develop a versatile policy that can generalize to downstream tasks without relying on specific reward signals. The authors focus on maximizing state entropy (SEM) to derive a policy that promotes diversity in the agent's experience by increasing the entropy of its stationary state distribution. They introduce **SEMDICE**, a structured off-policy algorithm that derives an SEM policy from arbitrary off-policy data by directly optimizing within the space of stationary distributions. SEMDICE produces a single, stationary policy that effectively maximizes state entropy. Experimental results indicate that SEMDICE surpasses existing baselines in enhancing state entropy and demonstrates superior efficiency in adapting to downstream tasks, making it a strong candidate for SEM-based unsupervised RL pre-training approaches.

### Strengths
1. This paper addresses the limitation of existing SEM methods in their inability to support off-policy learning, introducing the objective of optimizing the state distribution. By integrating optimization techniques from the DICE family of methods, the authors propose a well-motivated and logically consistent algorithm.  
2. The mathematical derivations in this paper are both accurate and well-founded.  Specifically, this paper provides a detailed explanation of why it is necessary to introduce both $d(s,a)$ and  $\bar{d}(s)$, which is highly convincing from an algorithm design perspective.
3. The experiments demonstrate that the SEMDICE method outperforms all baselines.  

In summary, this paper presents a clearly motivated approach, complete algorithmic derivation, and comprehensive experimental analysis.

### Weaknesses
1. I think there may be an oversight in the derivation. Specifically, in Equation (15), the summation over $s$ is replaced by sampling $s$ from $D$ through importance sampling, which in fact overlooks cases where $s$ is not in $D$. Therefore,  if $s$ is severely out-of-distribution (OOD), the calculated $ \log \bar{d}(s) $ may be highly inaccurate. Consequently, even though SEMDICE is off-policy, it still introduces a significant bias. The authors might consider adding experiments to demonstrate the impact of OOD-induced bias on the algorithm's performance.

2. In Section 5.1, the different baselines represent various intrinsic reward construction methods, all of which are based on policy-gradient algorithms. Why not use value-based methods as the core algorithms instead? This could help avoid the gradient bias introduced by off-policy policy gradients. Since SEMDICE’s off-policy nature does not suffer from gradient bias, using value-based methods would allow for a fairer comparison between SEMDICE and other algorithms.

### Questions
Similar to the issue of weaknesses.

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
2

### Summary
This paper addresses the issue of state entropy maximization by off-policy and principled method. 
Key idea underlying this work is the Eq.4-6, where the authors jointly optimize state stationary distribution and state-action stationary distribution.
The method is evaluated in both toy examples and tasks in URLB.

### Strengths
1, There is a theoretical analysis (Lagrange dual formulation and convex problem simplification) for the proposed approach. While I have not checked the proofs carefully, they appear to be correct.

2, The goal of the paper for addressing the challenge of state entropy maximization in RL is well motivated.

3, The results in the experiments clearly support the claims made in the paper.

### Weaknesses
1, Why the performance (entropy index) of APT and CIC drop after training in Fig.3 in Quadruped experiment?

2, Will the code be publicly available after acceptance? Some details of the specific implementation are not given.

3, Line 296: inimizing -> minimizing

### Questions
1, As described in Eq.57, the performance of network $e_{\phi}$ is heavily dependent on the optimality of network v and u. This design may lead to unstable training.

### Soundness
3

### Presentation
3

### Contribution
3
