# Position: Ignoring Hyperparameter Tuning Costs Misleads the Development of Efficient RL Algorithms

- Decision: Reject
- Scores: 4, 6, 6

## Abstract
The performance of reinforcement learning (RL) algorithms is often benchmarked without accounting for the cost of hyperparameter tuning, despite its significant practical impact. In this position paper, we argue that such practices distort the perceived efficiency of RL methods and impede meaningful algorithmic progress.  We formalize this concern by proving a lower bound showing that tuning 
$m$ hyperparameters in RL necessarily induces an exponential 
$\exp(m)$ blow-up in the sample complexity or regret, in stark contrast to the linear 
$O(m)$ overhead observed in supervised learning. This highlights a fundamental inefficiency unique to RL. To address this, we propose evaluation protocols that account for the number and cost of tuned hyperparameters, enabling fairer comparisons across algorithms. Surprisingly, we find that once tuning cost is included, elementary algorithms can outperform their successors with more sophisticated design. These findings call for a shift in how RL algorithms are benchmarked and compared, especially in settings where efficiency and scalability are critical.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
2

### Summary
This position paper argues that benchmarking RL algorithms should take into account the cost of hyperparameter tuning. Specifically, the authors demonstrate that the statistical cost of tuning $m$ hyperparameters in RL is significantly higher (e.g., exponential in RL compared to linear in supervised learning). They further propose two metrics to quantify an algorithm’s learning efficiency while incorporating hyperparameter tuning costs, and observe that many popular RL algorithms are less efficient than simpler alternatives. Based on these findings, the authors advocate for the development of parameter-free RL algorithms.

### Strengths
* The position of this paper is interesting and may hold value for the RL community.
* The argument is well-supported by both theoretical and empirical analyses.

### Weaknesses
* The authors mention the high cost of hyperparameter tuning in online RL settings (lines 34–39). However, it is unclear whether their position also applies to offline RL.
* Is developing parameter-free RL algorithms a feasible goal?
* Could the authors provide a more detailed derivation of the proof in Section 3?
* The writing and structure of the paper could be improved.

### Questions
Please see weaknesses.

### Presentation
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
This position paper argues that current benchmarking practices in reinforcement learning (RL) overlook the statistical cost of hyperparameter tuning, which leads to misleading claims about algorithm efficiency. The authors formalize this concern by proving that tuning \( m \) hyperparameters in online RL incurs a sample complexity overhead of \( \Theta(\exp(m)) \), in stark contrast to the \( O(\log M) \) or \( O(m) \) overhead in supervised learning. They propose two tuning-aware evaluation metrics — **Effective Sample Complexity** and **Effective AUC** — to penalize algorithms that rely heavily on hyperparameter search. Empirical results demonstrate that when these metrics are applied, simpler algorithms with fewer tunable parameters can outperform more sophisticated alternatives. The paper concludes by advocating for a shift toward parameter-free or tuning-efficient RL algorithm design.

### Strengths
The paper clearly argues that ignoring hyperparameter tuning costs in reinforcement learning (RL) can lead to misleading comparisons between algorithms. It supports this argument with both theory—showing that tuning even a few hyperparameters can greatly increase sample complexity—and experiments on MuJoCo tasks. The proposed metrics (Effective Sample Complexity and Effective AUC) are simple and useful for comparing algorithms more fairly. The experiments are well designed and show that simpler methods can sometimes outperform complex ones when tuning costs are considered. This is a relevant and important topic for the NeurIPS community, where benchmarking practices often focus too much on best-case results.

### Weaknesses
The paper does not consider or discuss alternative viewpoints. For example, some may argue that reporting best-tuned results is still useful for comparing potential performance, especially if all methods are tuned equally. The authors also do not explore cases where tuning costs can be shared across tasks (e.g., via meta-learning or transfer HPO), which might reduce the impact of their main claim.

### Questions
How do the authors view the role of transfer or meta-learning approaches that reuse tuning knowledge across tasks—could these offer a practical way to reduce the effective tuning cost, and if so, how would that fit into their evaluation framework?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript argues that RL algorithms without considering the cost of hyperparameters tuning may lead negative effect to RL algorithms. The authors demonstrated their ideas via theoretical proving showing introducing hyperparamters in RL would definity induce extra cost. To address this issue, the authors propose new evaluation framework enabling fair comparisons. In addition, the authors performs additional experiments demonstrating the effectiveness of the proposed metrics.

### Strengths
The manuscript is well-written and mathematically solid. The structure is very clear and the claim is solid. It is appreciated that the author provides solid proves demonstrating the cost of black-box HPO in RL environment. It is appreciated that the authors not only show in ineffectiveness of the traditional HPO method in RL situation, but also delivers novel metrics for practical use.

### Weaknesses
The idea in this manuscript is quite interesting. However, there are some issues not clear. 

The reviewer feels confusing about the Theorem 3.4, and the reviewer has another understanding. If Theorem 3.4 holds strongly, if the number of tuning parameters parameters $\Theta$ becomes large enough, will the value function converge to the optimal one? However, intuitively, when the number of tuning parameters increase, the model will be more difficult to converge, which shows the PAC guarantee is difficult to achieve under RL scenario, right? 

In addition, in Theorem 3.5, ``with probability greater than 1/2'' does not make too much sense, right?

The number of parameters tuned range from 1 to 4 in the experiments, and each parameter only has 2-4 choices. Actually, the search space is not large enough (although not very small).  We suggest more hyperprameters for tuning proving in the experiment studies. 

The experiment seems somehow confusing. The authors applies the proposed metrics for parameter tuning. However, it lacks comparison with other methods. Therefore, there are some difficulties claiming the proposed metrics are effective. It is suggested to consider some practical HPO methods as comparisons.

### Questions
See the weakness part above

### Presentation
3
