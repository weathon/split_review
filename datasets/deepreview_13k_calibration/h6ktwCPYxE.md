# Second Order Bounds for Contextual Bandits with Function Approximation

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 6, 8, 5

## Abstract
Many works have developed algorithms no-regret algorithms for contextual bandits with function approximation, where the mean rewards over context-action pairs belongs to a function class $\F$. Although there are many approaches to this problem, one that has gained in importance is the use of algorithms based on the optimism principle such as optimistic least squares. It can be shown the regret of this algorithm scales as $\widetilde{\O}\left(\sqrt{\delud(\F) \log(\F) T }\right)$ where $\delud(\F)$ is a statistical measure of the complexity of the function class $\F$ known as eluder dimension.  Unfortunately, even if the variance of the measurement noise of the rewards at time $t$ equals $\sigma_t^2$ and these are close to zero, the optimistic least squares algorithm’s regret scales with $\sqrt{T}$. In this work we are the first to develop algorithms that satisfy regret bounds of the form $\widetilde{\O}\left( \delud(\F)\sqrt{\log(\F)\sum_{t=1}^T \sigma_t^2  } + \delud(\F) \cdot \log(|\F|)\right) $ for contextual bandits with function approximation and unknown variances. These bounds generalize existing techniques for deriving second order bounds in contextual linear problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes variance-aware algorithms for contextual bandits with function approximation, with only mean reward realizability assumption for known and unknown variances of noise.

### Strengths
1. Solving for varying variance over time period is practical and may yield tighter regret bound in some cases.
2. The analysis of the variance and the truncated loss has novelty.

### Weaknesses
1. The organization of the paper is hard to follow. The theorems and colloraries are hard to follow since there is no intuitive explanation on the terms (e.g., $\mathcal{G}_t^\prime(\tau_i)$, $\tilde{\mathcal{E}_t^\prime}$ ). It is confusing whether the result mentions either $\sigma_t=\sigma$ case or not.  I suggest the authors move the $\sigma_t =\sigma$ case to appendix to clearly see the results.
2. Typos:

In line 163 $\mathcal{X} \times \mathcal{X} .. $ should be $\mathcal{X} \times \mathcal{A} .. $.

In Algorithm 1 line 5, $f_t^{\tau}$ should be $f_t^{\tau_i}$

In eq. (5), $\widehat{\sigma}_t$ should be $\widehat{\sigma}_t^2$
3. The paper does not adequately explain how the estimation of $\sigma_t^2$ is possible, especially when the variance is unknown and potentially changing at each time step. The core challenge is that when $\sigma_t$ is arbitrary, there is no clear mechanism to obtain sufficient observations to accurately estimate $\sigma_t$ at each step. The paper needs to clarify how it addresses the fundamental issue of estimating a time-varying variance with limited data, especially since the variance of the reward of the next decision period is unknown and can increase or decrease arbitrarily.

### Questions
1. Could the authors give an overview for the main contribution of the paper?
2. How the estimation of $\sigma^2_t$ is possible, especially for the unknown variance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces new regret bounds for contextual bandit problems with function approximation, assuming the realizability condition. The authors build on the framework of optimistic algorithms for contextual bandits, and they also propose new algorithms with improved regret bounds that adapt to the variance of the measurement noise under the eluder dimension.

### Strengths
- The authors present a study of contextual bandits with function approximation by developing algorithms with variance-dependent regret bounds, marking the first instance of such bounds in this setting. 
- These results improve upon existing bounds by requiring only a realizability assumption on the mean reward function, avoiding stronger, often impractical assumptions on measurement noise.
- The paper proposes two algorithms with distinct performance guarantees. Algorithm 1 is designed for cases with uniform but unknown measurement noise variance across time steps. This algorithm achieves a sharp dependence on the complexity of the reward function class, measured by the eluder dimension. Algorithm 2 is tailored for scenarios with variable noise variances. Its regret bound scales with the square root of the cumulative noise variance but linearly with the eluder dimension, providing an efficient approach for non-uniform noise settings.

### Weaknesses
However, several aspects of the paper’s presentation and empirical support could be improved:
- The authors did not include empirical experiments or numerical results to validate the theoretical bounds. This leaves the practical effectiveness of the algorithms untested. Specifically, the paper lacks any demonstration of the algorithms' performance on synthetic or real-world datasets, making it difficult to assess their behavior in practice. For example, it would be beneficial to see how the regret scales with the eluder dimension and the time horizon in a controlled environment, or how the algorithms perform when the realizability condition is only approximately met.
- The theoretical content is densely packed, with lemmas presented consecutively without sufficient exposition, making it challenging to follow the logical flow of arguments. The proofs often lack intuitive explanations, making it hard to grasp the key ideas behind the results. For instance, the connection between the optimistic exploration strategy and the derived regret bounds could be better elucidated. The paper would benefit from more discussion and motivation for each step in the proofs, rather than just stating the results.

### Questions
- There is no direct comparison with prior work is provided, making it difficult to clearly assess the improvements or distinctions of these results relative to existing bounds in the literature.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors studied the variance-dependent regret bound for contextual bandits with function approximation. They focus on scenarios where the reward function has a bounded eluder dimension. The analysis begins by considering the case where the variance is known. The authors introduce an optimistic least squares approach with multiple layers, where each layer maintains a confidence set using only data points with correspondingly small uncertainty. Combined with a routine that estimates the cumulative variance, they demonstrate that the algorithm can be adapted to the case with unknown variance. This algorithm matches the performance of the linear bandit case with unknown variance. Finally, with a modified filtering method that selects data points where the variance falls within a certain range, they show that their algorithm can be generalized to scenarios where the unknown variance changes.

### Strengths
1. The paper studied a variance-dependent regret bound for contextual bandits, which I think is an interesting problem to study.

2. The paper is generally well-written, and the proof appears to be correct.

3. Their regret bound for contextual bandits with unchanged unknown variance matches the results for linear bandits. I think this is a valuable addition to the literature and may have further theoretical impacts.

### Weaknesses
1. Given the variance-dependent regret bound for linear bandits in the literature, it is not surprising that one can obtain a variance-dependent regret bound under general function approximation. Moreover, there is still a $\sqrt{d}$ factor gap in the general case where variance changes are allowed, compared to the linear setting. I would suggest that the authors highlight the obstacle to removing this gap in the main content.

2. The approach in this paper adapts [Zhao et al., 2023] to the general function approximation case. I would suggest that the authors highlight the technical challenges and the key difference in a specific subsection or paragraph.

3. I am not sure whether the regret bound under changed variance is a significant setting on its own; it appears somewhat artificial. By contrast, the linear bandit case holds practical implications, as demonstrated by [Zhao et al., 2023], where their algorithm is applied to linear mixture MDPs as an example. It would be great to provide motivating examples or potential applications for the changed variance setting.

### Questions
1. Do you think the current regret bound for changed variance is tight?

### Soundness
3

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
4

### Summary
This work studies the contextual bandit problem under general function approximation with finite eluder dimension. The author proposes a novel algorithm based on the uncertainty-filtered multi-scale least squares procedure and achieves a variance-aware regret guarantee for general function approximation without requiring knowledge of the conditional variance. The regret for the homogeneous case seems near-optimal when reduced to the linear function class, while the regret for inhomogeneous variance has an additional dependency on $\sqrt{d}$.

### Strengths
1. This work provides the first algorithm with a variance-aware regret guarantee for general function approximation without requiring knowledge of the conditional variance.

2. The second-order regret for the homogeneous case seems near-optimal when reduced to the linear function class.

3. The author proposes a novel uncertainty-filtered multi-scale least squares method, which could be of independent interest.

### Weaknesses
1. Some parts of the presentation are highly confusing, making it difficult to follow.

(1) In Line 264, there is no Propositional 3.2, and Appendix C discusses an existing algorithm with a Hoeffding-type confidence set. The text refers to the proof of Proposition 3.2 being in Appendix C, but Proposition 3.2 concerns a Bernstein-type algorithm, while Appendix C details an existing algorithm using Hoeffding-type bounds. This mismatch creates significant confusion as the appendix does not seem to support the proposition.

(2) In Line 279, what is the definition of the event E?

(3) In Line 299, what is Algorithm 3?

2. Regarding the regret guarantee, there is a lack of comparison with previous results, making it hard to assess the contribution of the theoretical findings. To my knowledge, the regret for the homogeneous case seems near-optimal when reduced to the linear function class, while the regret for inhomogeneous variance has an additional dependency on $\sqrt{d}$ . However, more commentary on this point is needed. Additionally, it would be beneficial to compare the regret to that of previous algorithms for general function approximation.

3. The algorithm is highly inefficient. While calculating (threshold) confidence sets is a widely used technique in RL with general function approximation, this work further relies on calculating the intersection of the confidence sets and performing optimization over the intersected confidence set. This may be intractable when the confidence sets are not convex.

### Questions
1. Previous algorithms that achieved second-order regret with homogeneous variance typically relied on a weighted estimator, using either uncertainty weighting [1] or variance weighting [2]. It is interesting to explore how the proposed algorithm can achieve second-order regret without employing any weighting mechanisms, which could be of independent interest.

[1] Variance-dependent regret bounds for linear bandits and reinforcement learning: Adaptivity and computational efficiency.

[2] Nearly minimax optimal reinforcement learning for linear mixture markov decision processes

2. For the variance $\sigma_t$, should it be fixed, or can it be a random variable that depends on the selection of the action?

3. In Line 171, the claim regarding the first algorithm seems incorrect. As mentioned by the author in Line 99, second-order bounds for contextual bandits were already developed in Zhao et al. (2022).

4. For the contextual bandit problem, recently, a new work [3] achieved second-order regret for the dueling bandit case. It would be helpful if the paper provided some discussion on it.

[3] Variance-Aware Regret Bounds for Stochastic Contextual Dueling Bandits

### Soundness
3

### Presentation
1

### Contribution
3
