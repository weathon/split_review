# Learning with Real-time Improving Predictions in Online MDPs

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
In this paper, we introduce the Decoupling Optimistic Online Mirror Descent (DOOMD) algorithm, a novel online learning approach designed for episodic Markov Decision Processes with real-time improving predictions. Unlike conventional methods that employ a fixed policy throughout each episode, our approach allows for continuous updates of both predictions and policies within an episode. To achieve this, the DOOMD algorithm decomposes decision-making across states, enabling each state to execute an individual sub-algorithm that considers both immediate and long-term effects on future decisions. We theoretically establish a sub-linear regret bound for the algorithm, providing a guarantee on the worst-case performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies online episodic MDP with time-varying cost functions and predictions. A novel algorithm, Decoupling Optimistic Online Mirror Descent (DOOMD), is proposed to update both predictions and policies throughout the episodes. A sublinear regret guarantee is also established to demonstrate the effectiveness of the proposed algorithm.

### Strengths
1. Involving real-time predictions in online MDP is an interesting idea since many real-world applications have certain predictions on the future costs.

2. The paper is well-written. The algorithm procedures are well explained.

3. The proposed algorithm can update its predictions and policies during the episode instead of at the end of each episode, which has some practical appeal.

### Weaknesses
1. One of my major concerns is about the assumptions. This paper considers a deterministic transition function but claims that it can be easily generalized to stochastic transitions. Can the authors provide more details on this generalization? Specifically, how would the algorithm need to be modified to handle stochastic transitions, and what specific changes to the regret analysis would be required? The current lack of detail makes it difficult to assess the validity of this claim.

2. The lack of simulation results is another major weakness of this paper. The authors should provide some numerical justifications of their algorithm, hopefully in both deterministic cases and stochastic cases. It would be beneficial to see how the algorithm performs under different levels of prediction accuracy and how sensitive it is to the choice of hyperparameters. Without these results, it is hard to gauge the practical applicability of the proposed method.

3. It is true that any episodic MDP can be transformed into a loop-free MDP. However, this comes at the cost of enlarging the state space. How does this transformation affect the regret bounds' dependence on dimensionality and episode length? Specifically, what is the precise increase in the state space size, and how does this impact the constants and exponents in the regret bound? A more rigorous analysis of this transformation's impact is needed.

### Questions
There are several other papers considering predictions in online learning and online control, such as [C1] [C2]. 

Q1: How does the prediction model compare with the prediction models considered in [C1] and [C2]? 

Q2: Besides, can the regret analysis in this paper be generalized to the prediction model in [C1] and [C2]? 



[C1] Li, Y., Chen, X. and Li, N., 2019. Online optimal control with linear dynamics and predictions: Algorithms and regret analysis. Advances in Neural Information Processing Systems, 32.

[C2] Li, Y. and Li, N., 2020. Leveraging predictions in smoothed online convex optimization via gradient-based algorithms. Advances in Neural Information Processing Systems, 33, pp.14520-14531.

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
The paper proposes an algorithm to solve episodic MDP with deterministic transitions by allowing the policies to update continuously within an episode. To this end, the paper builds on Optimistic mirror descent (OMD), which provides a prediction functionality via the so-called predictable sequences.

### Strengths
The model is novel and exciting; while the broad area of improving RL with predictions is not new, the methodology and the model are new.
The methodology nicely adopts the optimistic mirror descent technique for solving deterministic episodic MDP with clear and complete regret analysis.

### Weaknesses
1) I have significant concerns about the clarity of the content presentation and layout, e.g.,
Algorithm 2 is incomprehensible without looking at the appendix, which does not seem to be a good workaround around the page limit of the submission at the cost of clarity. The core issue is that the algorithm's description lacks sufficient detail to understand the update rules and the interplay between the different components. For instance, the precise meaning of the 'predictable sequence' and how it is used in the update is not immediately clear from the main text, requiring the reader to constantly refer to the appendix, which disrupts the flow of understanding.

2) To my understanding, in episodic MDPs, the learned policy is itself non-stationary, I.e., it depends on h. The policy takes into account how many times steps are remaining in the episode. While the setting is different here it is not clear what is the baseline case that the paper is trying to contrast. Can something easier/computationally faster be done when there are no predictions, what will be the regret then? It's unclear what the performance would be without the prediction mechanism, and how much the added complexity of the prediction model is actually contributing to the overall performance. A clear baseline comparison is needed to understand the true value of the proposed method.

3) The nature of predictions is not clearly defined in the introduction. The authors need to consider a comparison with a large body of work with online learning with predictions (which is not done) e.g. https://proceedings.mlr.press/v119/bhaskara20a/bhaskara20a.pdf (Online Learning with Imperfect Hints) and related papers cited and citing the linked paper. The introduction should clearly define the type of predictions being used, their source, and how they differ from existing prediction models in online learning. The current lack of clarity makes it difficult to assess the novelty and relevance of the proposed approach. The connection to existing work on online learning with predictions is missing, and the paper needs to clearly differentiate its approach from existing methods.

4)Lines 181-182 say the methodology can be generalized to stochastic transition. How? The paper provides no details on how the algorithm can be adapted to handle stochastic transitions. This is a significant gap, as most real-world MDPs involve stochasticity. The lack of detail makes this claim unsubstantiated.

5)The model has unbounded robustness. Ideally, it is expected that the model should be robust when errors in the predictions are really high. What can be done to mitigate this? The paper does not discuss the robustness of the algorithm to inaccurate predictions. In practice, predictions are likely to be noisy, and the algorithm should be able to handle such scenarios. The lack of analysis on this aspect is a major concern.

6)While the paper builds on the ideas of Optimistic mirror descent for predictable loss sequences, it does not explain the key technical insights that make the algorithm applicable to this setting. This is an important constituent of a well-written theory paper. The paper needs to clearly articulate the technical challenges in adapting OMD to this specific setting and how the proposed algorithm overcomes these challenges. The current explanation is insufficient for a reader to understand the core technical contributions.

### Questions
Please refer to the above section

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new framework that enables a more general and flexible interaction between the learner and the environment in online episodic MDPs. Different from traditional methods that use a fixed policy throughout each episode, this framework allows for updates to both predictions and policies within an episode.

The authors introduce the concept of cumulative cost, which considers both immediate costs and the long-term effects on future decisions. Building on this idea, they propose the Decoupling Optimistic Online Mirror Descent (DOOMD) algorithm.

A \sqrt{T} regret bound is established in this work.

### Strengths
This paper is straightforward and easy to follow.

It introduces a new framework that facilitates a more general and flexible interaction between the learner and the environment in online episodic MDPs.

### Weaknesses
This paper appears to consider only the deterministic transition case, though it mentions that the approach can be easily generalized to the stochastic case. Could you provide more details on how this generalization would work?

The paper lacks technical novelty, as many of the proofs are largely adapted from previous works such as Zimin & Neu (2013).

It seems that this paper assumes the agent has access to the cumulative cost, which is a stronger assumption. However, it’s unclear if this assumption actually leads to an improved regret bound.

Related to the above, it's not clear how the regret bound of DOOMD compares to those in previous studies. Could you include further discussion on the sharpness of the results, e.g., in terms of factors like ∣S∣ and ∣A ∣? Without stronger guarantees, it’s hard to see the why allowing changing the policy within the episode is favorable, especially since it doesn’t achieve a better regret bound.

### Questions
This paper addresses the transition to a from a nonlayered structure to a layered structure. However, the sharp bounds in layered Markov Decision Processes (MDPs) do not appear to be easily transferable to unlayered MDPs and vice versa. A straightforward conversion on a bound between these two settings could result in a more relaxed dependence on H.

It appears that the paper assumes the learner receives an updated cost prediction for state-action pairs across all subsequent layers. Can you provide a motivating example to justify this assumption in real-world scenarios, particularly when dealing with a stochastic transition function? Additional elaboration on this would be helpful.

The main text lacks self-containment. It would be beneficial to discuss some high-level concepts of Algorithms 3 to 5 within the main text.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduce the Decoupling Optimistic Online Mirror Descent (DOOMD) algorithm, a novel approach for episodic Markov Decision Processes that incorporates real-time updates in predictions. Unlike traditional methods with fixed policies per episode, DOOMD continuously adjusts both predictions and policies. By decomposing decision-making across states, each state executes a unique sub-algorithm that considers immediate and future decision impacts. This paper also establish a sub-linear regret bound for DOOMD, ensuring a worst-case performance guarantee.

### Strengths
- While computing different policies across episodes or steps is an established concept, this paper introduces a novel approach by computing an optimal policy based on distinct subspaces within the state space. Unlike prior decision-making algorithms in non-stationary or time-varying environments that focus on optimal policy computation over the time dimension, this work innovates by emphasizing optimal policy computation across the spatial dimension of the state space.

### Weaknesses
Thanks for the paper and the efforts. Please see the *questions* for the weakness.

- The reviewer understands that the primary algorithm divides the state space into subspaces and computes policies independently for each. Could the authors clarify how, in practical terms, one might decide on these partitions?

- On line 38: It appears that the route $1 \to 2 \to 3$ is more optimal than $1 \to 2 \to 4$ for Figure 1-(a). Please verify this.

- On line 56: Could you please be specific on how the current paper's approaches can help the development of Large Language Models?

- Please consider referring to the following papers that use predictions to dynamically update policies (or relate to optimal early stopping for policy updates):

  - Lee, H., Jin, M., Lavaei, J., & Sojoudi, S. Pausing Policy Learning in Non-stationary Reinforcement Learning. Forty-first International Conference on Machine Learning.
  - Pettet, G., Mukhopadhyay, A., & Dubey, A. (2022). Decision Making in Non-stationary Environments with Policy-Augmented Monte Carlo Tree Search. arXiv preprint arXiv:2202.13003.

- Regarding the partition $\mathcal{X} = \bigcup_{l \in \mathcal{L}} \mathcal{X}^l$, are $\mathcal{X}^l, l \in [L]$ disjoint sets?

- Lemma 3.1 would benefit from further elaboration. Could the authors clarify the significance of Lemma 3.1 and its implications?

- On line 190: This equation seems to need adjustment. Here, $M^l_t$ is defined as the prediction cost from $l$ to $L-1$, with the cost’s input as $\mathcal{U}$. Should there be a new notation, such as $c^l_t$, representing the actual cost function from $\mathcal{U}^l_t \to [0,1]$?

- With this in mind, Assumption 3.2 appears somewhat straightforward, as $c_t(u)$ and $M^l_t$ account for different input lengths.

### Questions
- The reviewer understands that the primary algorithm divides the state space into subspaces and computes policies independently for each. Could the authors clarify how, in practical terms, one might decide on these partitions?

- On line 38: It appears that the route $1 \to 2 \to 3$ is more optimal than $1 \to 2 \to 4$ for Figure 1-(a). Please verify this.

- On line 56: Could you please be specific on how the current paper's approaches can help the development of Large Language Models?

- Please consider referring to the following papers that use predictions to dynamically update policies (or relate to optimal early stopping for policy updates):

  - Lee, H., Jin, M., Lavaei, J., & Sojoudi, S. Pausing Policy Learning in Non-stationary Reinforcement Learning. Forty-first International Conference on Machine Learning.
  - Pettet, G., Mukhopadhyay, A., & Dubey, A. (2022). Decision Making in Non-stationary Environments with Policy-Augmented Monte Carlo Tree Search. arXiv preprint arXiv:2202.13003.

- Regarding the partition $\mathcal{X} = \bigcup_{l \in \mathcal{L}} \mathcal{X}^l$, are $\mathcal{X}^l, l \in [L]$ disjoint sets?

- Lemma 3.1 would benefit from further elaboration. Could the authors clarify the significance of Lemma 3.1 and its implications?

- On line 190: This equation seems to need adjustment. Here, $M^l_t$ is defined as the prediction cost from $l$ to $L-1$, with the cost’s input as $\mathcal{U}$. Should there be a new notation, such as $c^l_t$, representing the actual cost function from $\mathcal{U}^l_t \to [0,1]$?

- With this in mind, Assumption 3.2 appears somewhat straightforward, as $c_t(u)$ and $M^l_t$ account for different input lengths.

### Soundness
3

### Presentation
3

### Contribution
3
