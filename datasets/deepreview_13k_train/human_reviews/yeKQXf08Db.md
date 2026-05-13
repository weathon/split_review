# Dynamic Continuous Hyperparameter Tuning for Generalized Linear Contextual Bandits

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
In stochastic contextual bandits, an agent sequentially makes actions from a time-dependent action set based on past experience to minimize the cumulative regret. Like many other machine learning algorithms, the performance of bandits heavily depends on the values of hyperparameters, and theoretically derived parameter values may lead to unsatisfactory results in practice. Moreover, it is infeasible to use offline tuning methods like cross-validation to choose hyperparameters under the bandit environment, as the decisions should be made in real time. To address this challenge, we propose the first online continuous hyperparameter tuning framework for contextual bandits to learn the optimal parameter configuration within a search space on the fly. Specifically, we use a double-layer bandit framework named CDT (Continuous Dynamic Tuning) and formulate the hyperparameter optimization as a non-stationary continuum-armed bandit, where each arm represents a combination of hyperparameters, and the corresponding reward is the algorithmic result. For the top layer, we propose the Zooming TS algorithm that utilizes Thompson Sampling (TS) for exploration and a restart technique to get around the \textit{switching} environment. The proposed CDT framework can be easily utilized to tune contextual bandit algorithms without any pre-specified candidate set for multiple hyperparameters. We further show that it could achieve a sublinear regret in theory and performs consistently better than all existing methods on both synthetic and real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores hyperparameter tuning for generalized linear contextual bandits. The foundational concept behind the paper is the OFUL algorithm, where the chosen arm at round $t$ is:

$a_{t}=\arg\max_{a\in [K]}$ $x_{t,a}^{\top}$ $\hat \theta_{t}$ $+\alpha $ $ ||x_{t,a}||_{V{t}{-1}}$.

While setting $\alpha=\tilde{\Theta}(d)$ can yield the worst-case optimal regret bound, this parameter might result in subpar performance in real-world scenarios. 

The primary objective of this paper is to adjust the parameter $\alpha$ to ensure that the algorithm maintains its theoretical guarantee while also demonstrating good empirical results. Given certain conditions, the paper achieves this goal.

### Strengths
See summary.

### Weaknesses
However, there are some notable limitations:

1. The paper overlooks key benchmarks both theoretically and experimentally:
   - Regret Bound Balancing and Elimination for Model Selection in Bandits and RL.
   - Syndicated bandits: A framework for auto-tuning hyper-parameters in contextual bandit algorithms.
   
2. The rationale behind the decomposition in Eq(2) suggests that “the bandit algorithm is likely to select similar arms if the hyperparameters chosen are close at round $t$.” This reasoning is not entirely convincing. When feature vectors are determined by either a non-oblivious or oblivious adversary, the claim doesn't hold up. Such an adversary can present arms where the hyperparameters are similar, yet the arms differ considerably. Hence, it's crucial for the authors to specify these conditions in the problem definition and offer a more plausible explanation for Eq(2).

3. The regret bound presented in this paper is $\Omega(T^{2/3})$. This is less favorable than the bound provided in "Syndicated bandits: A framework for auto-tuning hyper-parameters in contextual bandit algorithms," which doesn't necessitate any stringent conditions.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

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
This paper studies the problem of generalized linear bandits. Though there are optimal algorithms proved for this setting, the theoretically optimal choice of their hyper-parameters are often very conservative and useless in practice. This paper attempts to learn the hyper-parameters that are best suited for the problem instance at hand which lead to significant performance boost in comparison to theoretical choice.

### Strengths
- The problem they study is well motivated in practice
- Novel regret analysis is presented for handling time switching lipschitz bandits
- Extensive experiments are conducted

### Weaknesses
 I think this work studies an important practical problem. Though I am positive in general, some clarifications regarding the current draft are needed:

- The authors propose Algorithm 1 to zoom quickly into a good area in the parameter space. However, this introduces extra hyper-parameters in Algorithm 1 which is unclear to tune. The authors say that it is possible to mitigate this issue by adding another layer of EXP3, essentially treating the epoch size candidate in Alg. 1 as arms. Then how sensitive is the overall performance wrt the parameters of outer EXP3 layer?

- A follow-up on the previous question. While the master EXP3 algorithm does compete with the base algorithms (with different epoch parameters) in terms of their actual performance during the run, this performance could be significantly worse than if the base algorithm were run on its own, updating its state after every prediction. For instance, a base algorithm which is performing bad initially but excels later on might quickly fall out of favor with the master,  never reach its good performance regime. How do you address this problem? How are the base-learners defined? Doesn't this problem persist, even if we are only trying to optimize a given bandit algorithm like linUCB over a discrete candidate set of hyper-parameters? This is essentially the same problem faced by corralling a band of bandits literature (eg. https://arxiv.org/abs/1612.06246).

- I am confused about the usefulness of having fixed length epochs between two restarts in Alg.1. For example, we can expect that after sufficient number of rounds, the expected reward is stable. So isn't it more practical to have an adaptive restart schedule where one restarts more often during earlier rounds and less toward later rounds?  Further, I agree with the authors that similar hyper-parameter choices most often can result in similar arms getting pulled. However, there could be discontinuities in the rewards as a function of hyper-parameters. So I am curious, why the authors didn't study the case where the reward at a round is also modelled as a piece-wise lipschitz function of hyper-parameters: meaning the parameter space is partitioned into several clusters. within each cluster the reward is a lipschitz function.

- How do you tune Alg.1 wrt sub-gaussian parameter $\tau$ present in the noise of Eq.(2)?

### Questions
see above

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
In response to some hyperparameter selection issues in bandit problems, this paper notes that theoretically derived parameter often yield unsatisfactory results in practice. At the same time, existing methods for hyperparameter search often lack theoretical guarantees and cannot be directly applied to real-world problems. To address this, the paper introduces a a double-layer BOB framework named CDT, for learning the hyperparameters. This models the hyperparameter selection issue as a continuum-arm Lipschitz bandit problem, ultimately providing sub-linear regret theoretical guarantees. Moreover, the method demonstrates significant performance improvements in experiments.

### Strengths
The paper introduces an algorithm for tuning parameters in a continuous parameter space, provides the corresponding theoretical guarantees, and demonstrates performance improvement through experiments.

### Weaknesses
It seems that your meta-algorithm's parameter $H$ still requires some prior knowledge about $T$ and $p_{z,*}$, which doesn’t fully resolve the issue of parameter tuning. In practical scenarios, it is impossible to know the total iteration number $T$ and other prior knowledge in advance. Addressing this issue would need an additional layer of BOB, resulting in a three-layer algorithm structure. Are you sure that such an algorithm can run efficiently and can still have a good performance? Moreover, this approach may impose certain constraints on the total duration $T$, such as requiring $T$ to be larger than certain values.

The theoretical results of the CDT algorithm only provide sublinear outcomes, and it seems like it can't recover the optimal results of the base algorithms. However, your experiments indicate that CDT is optimal, which feels somewhat hard to explain.

The author mentions in the contributions section that the algorithm presented in the paper is efficient. However, there is no comparison of running times in the experiments. This is quite crucial for bandit settings. Therefore, I would suggest that the author add a comparison of the algorithm's running time in the experiments.

There is a typo in Notation: write \top as T

### Questions
1. The theoretical results of the CDT algorithm only provide sublinear outcomes, and it seems like it can't recover the optimal results of the base algorithms. However, your experiments indicate that CDT is optimal, which feels somewhat hard to explain.

2. The author mentions in the contributions section that the algorithm presented in the paper is efficient. However, there is no comparison of running times in the experiments. This is quite crucial for bandit settings. Therefore, I would suggest that the author add a comparison of the algorithm's running time in the experiments.

3. There is a typo in Notation: write \top as T

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
