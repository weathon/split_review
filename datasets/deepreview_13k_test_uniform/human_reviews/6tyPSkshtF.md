# Gap-Dependent Bounds for Q-Learning using Reference-Advantage Decomposition

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We study the gap-dependent bounds of two important algorithms for on-policy $Q$-learning for finite-horizon episodic tabular Markov Decision Processes (MDPs): UCB-Advantage (Zhang et al. 2020) and Q-EarlySettled-Advantage (Li et al. 2021). UCB-Advantage and Q-EarlySettled-Advantage improve upon the results based on Hoeffding-type bonuses and achieve the {almost optimal} $\sqrt{T}$-type regret bound in the worst-case scenario, where $T$ is the total number of steps. However, the benign structures of the MDPs such as a strictly positive suboptimality gap can significantly improve the regret. While gap-dependent regret bounds have been obtained for $Q$-learning with Hoeffding-type bonuses, it remains an open question to establish gap-dependent regret bounds for $Q$-learning using variance estimators in their bonuses and reference-advantage decomposition for variance reduction. We develop a novel error decomposition
framework to prove gap-dependent regret bounds of UCB-Advantage and Q-EarlySettled-Advantage that are logarithmic in $T$ and improve upon existing ones for $Q$-learning algorithms. Moreover, we establish the gap-dependent bound for the policy switching cost of UCB-Advantage and improve that under the worst-case MDPs. To our knowledge, this paper presents the first gap-dependent regret analysis for $Q$-learning using variance estimators and reference-advantage decomposition and also provides the first gap-dependent analysis on policy switching cost for $Q$-learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper establishes improved gap-dependent upper bounds on finite-horizon episodic Markov decision processes (MDPs). There already exists a gap-dependent upper bound of $\tilde O( \Delta_{\min}^{-1} H^6 SA)$. To provide improved guarantees, the paper analyzes two algorithms with variance-aware regret-analysis, UCB-Advantage due to Zhang et al. 2020 and Q-EarlySettled-Advantage due to Li et al. 2021. The paper proves that both algorithms admit regret upper bounds of $\tilde O( \Delta_{\min}^{-1} H^5 SA)$.

### Strengths
- Improved gap-dependent regret upper bounds for learning finite-horizon episodic MDPs are provided.
- The guarantees are obtained by analyzing some existing near-optimal algorithms for learning finite-horizon episodic MDPs.
- The regret analysis based on decomposing the errors into reference estimations, advantage estimations, and reference settling seems technically novel.

### Weaknesses
-

### Questions
Is it possible to demonstrate how close the provided regret upper bounds are to optimality? Are there gap-dependent regret lower bounds?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides gap-dependent regret bounds for Q-learning-like algorithms which use variance estimation/also achieve variance dependent regret. They also provide an algorithm with a gap-dependent policy switching cost. The algorithms used (or small variations) appear in prior work. The authors describe a novel error decomposition and a surrogate reference function technique (which assists in the application of concentration inequalities) as main analytical contributions.

### Strengths
The regret bounds achieved by the paper improve upon those of prior works.

The gap-dependent analysis of the switching cost is new, and I think it is interesting to expand gap-dependent analyses beyond the regret performance metric.

I am somewhat unclear on the level of technical contribution of the paper (see questions), but it seems like the analysis techniques may be useful for future work involving reference-advantage decomposition algorithmic ideas.

### Weaknesses
The proof sketch is not very easy to follow and does not seem very useful for an initial read of the paper. This is especially due to the fact that the statements of the algorithms are only provided in the appendix and many forward references are made. I think it would be more helpful if the algorithms (or maybe just one) were provided in the main body of the text and the proof sketch were shortened to focus on higher-level steps and main differences compared to prior works.

The contribution appears to be somewhat limited, since it is a re-analysis of existing algorithms and the level of technical contribution of the analysis is not fully clear to me (see questions below). It is very common in RL for the analysis of the same/similar algorithms to be gradually refined, but then I think it is very important that the authors do a good job highlighting the analytical improvements.

### Questions
I would like to better understand the level of technical contribution of this paper.
Why are surrogate reference functions needed in your analyses but not those of the previous works (Zhang et al 2020, Li et al 2021)?
Could you provide more discussion on exactly how the error/regret decomposition differs from previous work and why it is novel/what issues are being solved?

Could you provide more comparison and discussion of related work which is model-based and tries to achieve similar goals (gap and variance dependent guarantees)?

### Soundness
3

### Presentation
3

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
The paper analyzes the UCB-Advantage algorithm and a slightly modified version of the Q-EarlySettled-Advantage algorithms and provides the gap-dependent regret bounds and switching-cost bounds for them. Those two algorithms are worst-case optimal algorithms via references. Similarly, the gap-dependent regret bounds of such algorithms provided in this paper are better than the gap-dependent bounds of the algorithms without references in the literature. Discussions on the choice of hyperparameter $\beta$ and sketch of the proofs are clearly presented. For switching cost, analysis by separating the impact of the optimal and suboptimal actions is provided, so that the multiplicative factor before the leading order log(T) only depends on the tuples with optimal actions.

### Strengths
The analysis of "gap-dependent bound + reference-based algorithm" is novel and of interest to the RL theory study. 

The proof sketch is clearly written. I checked some technical parts of the paper, and they are correct to me. 

The technique of introducing an auxiliary "surrogate reference function" via cut-off based on optimal value function and $\beta$ to avoid non-martingale if using the last step reference function is new to gap-dependent bound.

### Weaknesses
I did not see major weaknesses in the paper. Here are some minor/barely ones. 

In the discussion "Comparisons with Zhang et al. (2020); Li et al. (2021" after Theorem 3.3. The claim of better than worst-case since one is log(T) and the other is sqrt{T} is not quite fair. Either say it is asymptotic/for sufficiently large T, or discuss whether the proposed gap-dependent bounds can degrade to the worst-case bound naturally. The latter is worth investigating, but I do not see an immediate solution to this.

### Questions
Since the hyperparameter $\beta$ plays a more important bound-dependent role in the gap-dependent bound compared to that of the worst-case bound. Is there an adaptive way of updating the hyperparameter \beta? Say initialize \beta to be sufficiently large at the beginning while decreasing it gradually as the estimates get more accurate.

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
4

### Summary
This work studies the instance-dependent regret guarantee in tabular Markov Decision Processes. The author focuses on the minimal sub-optimality gap structure and provides a logarithmic regret guarantee for two existing algorithms: UCB-Advantage and Q-EarlySettled-Advantage. Compared with previous instance-dependent guarantees, this work achieves a variance-aware regret bound that improves by a factor of H even under maximum variance. Additionally, when variance is low (e.g., deterministic transitions), the regret demonstrates improved dependency on the minimal sub-optimality gap. Furthermore, the author also proposes a gap-dependent policy-switching cost for the UCB-Advantage algorithm.

### Strengths
1. The author first proposes a novel algorithm that achieves a variance-aware regret bound with respect to the minimal sub-optimality gap.

2. The author also proposes an instance-dependent policy-switching cost for the UCB-Advantage algorithm, which could be of independent interest.

3. When variance is low (e.g., in deterministic transitions), the regret exhibits improved dependency on the minimal sub-optimality gap.

### Weaknesses
The main weakness is that the improvement in this work over existing results appears too limited.

1. As discussed in line 264, the instance-dependent regret bound depends on the point-wise sub-optimality gap. In comparison, this work relies on the minimal sub-optimality gap across all state-action pairs. In most situations, the sub-optimality gap varies significantly across different state-action pairs, leading to a weaker performance in the regret guarantee presented in this work.

2. For the instance-dependent guarantee with zero variance, this work achieves a sub-linear dependency on the sub-optimality gap. However, a similar result already exists without relying on the minimal sub-optimality gap assumption [1]. Compared with previous results, this work demonstrates worse dependency on the episode length H and the sub-optimality gap.
[1] Sharp Variance-Dependent Bounds in Reinforcement Learning: Best of Both Worlds in Stochastic and Deterministic Environments

3. Regarding the gap-dependent policy-switching cost, the claim in line 136 appears incorrect. When the optimal action set is small, the dominant term in equation (4) becomes the second term, resulting in an improvement of only 
log T rather than a factor of A, which is minor.

4. Regarding technical novelty, the author claims the introduction of a surrogate reference function; however, the importance of this reference function is not clearly explained in section 3.2. It would be helpful to further highlight its effect in the proof sketch.

### Questions
1. In line 310, there is a typo fo$Q_h^k-Q_h^k$. 

2. In line 313, it seems questionable that the first term in G3 does not diminish to zero, while the regret should converge to zero as the episode k becomes sufficiently large.

3. Lemma B.3 seems incorrect when $\check{n}(s,a)=1$ immediately after a reset to 0.

4. The $N(s,a)$ in Algorithm 1 should be $n(s,a)$.

### Soundness
3

### Presentation
2

### Contribution
3
