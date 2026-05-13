# Online Decision Deferral under Budget Constraints

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
Machine Learning (ML) models are increasingly used to support or substitute decision making. In applications where skilled experts are a limited resource, it is crucial to reduce their burden and automate decisions when the performance of an ML model is at least of equal quality. 
However, models are often pre-trained and fixed, while tasks arrive sequentially and their distribution may shift. In that case, the respective performance of the decision makers may change, and the deferral algorithm must remain adaptive. We propose a contextual bandit model of this online decision making problem. Our framework includes budget constraints and different types of partial feedback models. Beyond the theoretical guarantees of our algorithm, we propose efficient extensions that achieve remarkable performance on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript introduces a framework for online learning-to-defer under constrained budget for the human expert.

### Strengths
The topic of the manuscript originates from a practical problem.

### Weaknesses
1. Considering optimal static policy seems to be limited as it can be far from the true dynamic optimal policy. Would it be possible or how difficult it is to extend the current regret analysis in the paper to handle dynamic regret which uses the dynamic optimal policy as benchmark?
2. The regret analysis seems to be straightforward extensions from existing works on UCB-based algorithms for bandit problems as the authors mentioned in Section~4.
3. There is no regret guarantee for the neural linear algorithm provided in the paper. Could you at least explain the specific challenges in deriving such guarantees for this approach?

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies an online decision-making problem with a human expert. The authors phrase the problem as a contextual bandit problem, where a deferral learner needs to choose whether to use an ML model or a human expert to obtain the reward. The authors propose an algorithm to solve this problem based on a UCB-like algorithm and characterize its regret guarantees. The authors further extend their algorithm using neural networks to handle complicated datasets.

### Strengths
1. The problem formulation and the algorithm design seem to be novel and of practical interest. 
2. Theoretical regret guarantees are provided for the proposed algorithms.

### Weaknesses
The paper has limited novelty and contribution.

1. The paper simply uses the an existing framework (Bandits with Knapsacks [Badanidiyuru et al., 2018], [Agrawal and Devanur, 2016]) to choose between a model's prediction or to defer to a skilled expert.
2. Limited contribution:
- The regret guarantee provided is a straightforward combination of the linear contextual bandit with knapsack guarantee [Agrawal and Devanur, 2016] with the generalized linear bandit analysis from  of [Li et al. (2017)], with the bulk of proof in the appendix filled with re-statments of specific Lemmas and Corollaries from [Agrawal and Devanur, 2016] and [Li et al. (2017)].

- The experiments are very limited. Section-5.1 is synthetic, while section 5.2 provides results for two different problems: 1) 0-1 Knapsack problem, that chooses between human solutions to the 0-1 knapsack problem and the solution to a greedy algorithm. This does not align with the original desription of distribution shift leading to decline in ML model's prediction accuracy. 2) ImageNet: chooses between a pretrained model and human prediction. Although this aligns with the original problem set-up, the evaluation is shallow and limited.

3. Some missing references on further developments in Bandits with Knapsacks:

- https://arxiv.org/abs/2211.07484v6

- https://arxiv.org/abs/2210.11834

- https://proceedings.mlr.press/v162/sivakumar22a.html

- https://proceedings.mlr.press/v238/deb24a

### Questions
1.	In line~163, what is the distribution D there?
2.	Does Algorithm~1 work for the full information setting or the bandit information setting? Please clarify how the algorithm design differs when full information or bandit information is considered.  It would be good to discuss the implications of using the algorithm in each setting, and how this choice affects the algorithm's performance or implementation.
3.	In general full information online learning algorithm typically yields smaller regret (e.g., algorithms for online convex optimization Hazan9 & Levy NIPS 2014). Could you explain why this is not the case for the algorithm studied in this paper?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes using the framework of Bandits with Knapsacks to choose a model's prediction or to defer to a skilled expert, where the expert is the limited resource available to the meta learner.

### Strengths
None

### Weaknesses
a. The proposed algorithm and analysis largely build on the work of Agrawal and Devanur (2016) [1], which addresses a similar problem. Although the authors claim that they extend the algorithm to generalized linear rewards, it is unclear what specific challenges this extension presents. For example, what are the specific difficulties in adapting the optimization techniques or theoretical analysis from the linear case to the generalized linear case? Does this require fundamentally different proof techniques or algorithmic modifications? A more detailed discussion of the technical novelties introduced by handling generalized linear rewards would strengthen the paper.

b. The theoretical results only hold when the budget $B$ is relatively large, $B \geq d^{1/2} T^{3/4}$. This requirement may limit the applicability of the algorithm in scenarios with a limited budget. In particular, many real-world applications may have budget constraints that do not scale with the time horizon $T$ in this manner. It would be helpful to have a more in-depth discussion of the implications of this constraint and whether the algorithm's performance degrades gracefully as the budget decreases below this threshold.

c. The neural linear algorithm is a straightforward extension of Algorithm 1, treating the neural network’s embedding as the context. And there is no theoretical guarantees for the neural linear algorithm. While empirical results are presented, the lack of theoretical grounding makes it difficult to understand the conditions under which this approach is expected to perform well. Further investigation into the theoretical properties of the neural linear algorithm would be valuable.

d. In the experiments, the authors only consider scenarios where $B$ is at least $0.25T$, which is a relatively large budget when $T$ is large. Results for smaller values of $B$ would be helpful to further validate the algorithm's performance. Specifically, it would be interesting to see how the algorithm performs when the budget is a smaller fraction of $T$, such as $0.1T$ or even smaller. This would provide a more comprehensive understanding of the algorithm's behavior under different budget constraints.

### Questions
- Could the authors specify the contributions if any, beyond a simple combination of [Agrawal and Devanur, 2016] and [Li et al. (2017)] and the limited empirical evaluation on the ImageNet dataset?

- There have been several new developments in the Neural Bandits literature since Riquelme et al. (2018) (see [1], [2] and [3]). Why have the authors not used these frameworks instead?

[1] Dongruo Zhou, Lihong Li, and Quanquan Gu. Neural contextual bandits with ucb-based exploration. In International Conference on Machine Learning, pp. 11492–11502. PMLR, 2020.

[2] Weitong Zhang, Dongruo Zhou, Lihong Li, and Quanquan Gu. Neural thompson sampling. In International Conference on Learning Representation (ICLR), 2021.

[3] Rohan Deb, Yikun Ban, Shiliang Zuo, Jingrui He, and Arindam Banerjee. Contextual bandits with online neural regression. In The Twelfth International Conference on Learning Representations.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new online decision-making problem that includes budget constraints and different types of feedbacks. The authors formalize this problem into a contextual bandit setting and propose a new algorithm for generalized linear rewards. They show that the algorithm achieves a near-optimal regret bound. They also validate its effectiveness with empirical results on real-world datasets.

### Strengths
a. The authors consider an interesting and practical problem that is well-motivated.

b. The paper provides both theoretical analysis and experimental results for the proposed algorithm. The regret bound of the algorithm is near-optimal under certain conditions. Experiments are conducted on both synthetic and real datasets, and the proposed algorithms outperform the baselines.

c. The presentation is clear and easy to follow.

### Weaknesses
a. The proposed algorithm and analysis largely build on the work of Agrawal and Devanur (2016), which addresses a similar problem. Although the authors claim that they extend the algorithm to generalized linear rewards, it is unclear what specific challenges this extension presents and whether it requires new techniques.

b. The theoretical results only hold when the budget $B$ is relatively large, $B \geq d^{1/2} T^{3/4}$. This requirement may limit the applicability of the algorithm in scenarios with a limited budget.

c. The neural linear algorithm is a straightforward extension of Algorithm 1, treating the neural network’s embedding as the context. And there is no theoretical guarantees for the neural linear algorithm.

d. In the experiments, the authors only consider scenarios where $B$ is at least $0.25T$, which is a relatively large budget when $T$ is large. Results for smaller values of $B$ would be helpful to further validate the algorithm's performance.

### Questions
a. Is it possible to obtain a theoretical guarantee (even if suboptimal) when $B$ is relatively small?

b. What is the challenge in extending the work of Agrawal and Devanur (2016) to your setting?

c. What are the empirical results of the proposed algorithm when $B < 0.25T$, such as $0.1T$?

### Soundness
3

### Presentation
3

### Contribution
2
