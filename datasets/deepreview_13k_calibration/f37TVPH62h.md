# Compound Returns Reduce Variance in Reinforcement Learning

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Multistep returns such as $n$-step returns are commonly used to improve the sample efficiency of deep reinforcement learning (RL). Variance becomes the limiting factor in the length of the returns; looking too far into the future increases uncertainty and reverses the benefit of multistep learning. In our work, we study the ability of compound returns---weighted averages of $n$-step returns---to reduce variance. The $\lambda$-return, used by TD($\lambda$), is the most well-known compound return. We prove for the first time that any compound return with the same contraction rate as a given $n$-step return has strictly lower variance when experiences are not perfectly correlated. Because the $\lambda$-return is expensive to implement in deep RL, we also introduce an approximation called Piecewise $\lambda$-Return (PiLaR), formed by averaging two $n$-step returns, that offers similar variance reduction while being efficient to implement with minibatched experience replay. We conduct experiments showing PiLaRs can train Deep Q-Networks faster than $n$-step returns with little additional computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the variance of compound returns in reinforcement learning both theoretically and empirically. Under the uniform covariance assumption between TD error at different steps, it proves that any compound return has lower variance than corresponding $n$-step return with the same contraction rate as long as the TD errors are not perfectly correlated. The contraction rate measures that convergence speed of a $n$-step TD estimator for value function estimation of a policy. Therefore, it concludes that compound return in general has lower variance under the same convergence rate. They also conduct experiments to verify this effect in value estimation tasks. Empirically, the paper proposes an approximation of $\lambda$-return using only the mixture of two multi-step returns named Piecewise $\lambda$-Return (PiLaR). Experiments with DQN on a tabular example shows the effectiveness of PiLaR on top of the standard $n$-step TD learning.

### Strengths
The variance of compound returns is a fundamental problem in reinforcement learning. This paper provides new insights on this problem by verifying the compound returns have lower variance than $n$-step returns under uniform covariance assumption. The paper clearly lists convincing theoretical and empirical evidence to support this claim.

### Weaknesses
1. It is unclear whether the uniform covariance assumption is reasonable in real-world problems, since the hardness to approximate the covariance between different steps should not be an evidence to support the validity of this assumption. Intuitively, the variance of TD errors at further steps should be larger since the entropy of state should increase along the diffusion over the MDP. Therefore, it is appreciated to verify this assumption empirically on synthetic examples.

2. The contraction rate measures the contraction level of the policy evaluation process. It is not clear the effect of this rate in the policy optimization process, nor is it discussed in the paper. Therefore, it is still not clear whether the faster learning with DQN is a consequence of smaller variance of PiLaR or smaller contraction rate in the policy optimization process as $n_2$ is generally larger than $n$. Specifically, the paper does not address how the contraction rate impacts policy improvement, and whether the observed speedup is due to variance reduction alone or also due to the change in contraction rate during policy optimization.

3. The theoretical results of the paper are mostly conceptual in the sense that it proves some variance reduction results but do not discuss how this lower variance accelerate the learning of optimal policies. The "equally fast" claim for two estimators with the same contraction rate is also conceptual without solid evidence. Does it correspond to smaller sample complexity in theory? The insight of this paper is also limited in both practice and theory, since the baseline is the $n$-step TD learning and DQN, which is away from current SOTA algorithms used in RL. Is is possible to compare the PiLaR (or more refined compound error with even smaller variances) with some SOTA RL algorithms such PPO or CQL?

### Questions
See above.

Eqn. (8): the second $S_t$ --> $s$ 

Eqn. (12): missing $\kappa$ in the RHS

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the widely used $\lambda$-compounded returns and show that they have lower variance than $n$-steps return if the temporal difference errors have equal correlation strictly less than one.

In addition they propose PILAR which is a practical deep RL approximation of the TD($\lambda$) compatible with experience replay.

### Strengths
The paper discovers few new characteristics of a very common method in RL that is TD($\lambda$).

### Weaknesses
1) I think that most of the results are slightly incremental and not clearly novel.

2) Assuming that all temporal differences error have the same correlation is a strong assumption in my opinion.

3) In general in RL it is not clear if minimizing the variance of the return estimators is helpful to improve the sample complexity of an algorithm. Check for example this paper investigating the role of the minimum variance baseline in policy gradient as in [1].

4) The experiments in Deep RL are limited to only one environment. I think that a larger empirical evaluation is necessary.

### Questions
Is it possible to use the results in this paper to show more informative results regarding the performance of TD($\lambda$). For example that having a lower variance in the returns improves the sample complexity needed for either policy evaluation or for learning an $\epsilon$-optimal policy ?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the variance reduction property of compound returns. While compound returns, such as the lambda-return, are often viewed as helping with variance reduction via averaging, the authors claim that this variance properties is formally investigate for the first time. Under certain assumptions on the variance/covariance model, the authors prove for the first time that any compound return with the same contraction rate as a given n-step return has strictly lower variance. The studies shed light on the theoretical understanding of using compound returns in learning value functions. Subsequently, the authors propose a computationally friendly piecewise lambda-return and verify the efficacy of their approach on one Atari Freeway environment.

### Strengths
The paper considers an interesting question. While it may be commonly believed that averaging helps with variance and hence learning in RL, the authors formally study the problem and show that compound returns admit a better bias-variance trade-off. The writing is overall very clear and organized. The proposed piecewise lambda-return is theoretically sound and seems to also perform in the limited experimental evaluations.

### Weaknesses
While a formal study on the variance reduction property is valuable, the theoretical contributions of this paper seem limited. The assumptions help abstract a lot of the difficulties and with the uniform variance/correlation assumptions, the derivation in this paper seems to be straightforward/follow standard arguments. As such, the technical depth is limited. Consequently, for such paper with limited theoretical innovations, one might expect a more comprehensive experimental evaluations, ablation studies and comparisons. The current manuscript unfortunately only evaluates on the Atari Freeway environment.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
