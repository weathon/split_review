# A Theoretical Framework for Partially-Observed Reward States in RLHF

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
The growing deployment of reinforcement learning from human feedback (RLHF) calls for a deeper theoretical investigation of its underlying models. The prevalent models of RLHF do not account for neuroscience-backed, partially-observed ``internal states'' that can affect human feedback, nor do they accommodate intermediate feedback during an interaction. Both of these can be instrumental in speeding up learning and improving alignment. To address these limitations, we model RLHF as reinforcement learning with partially observed reward-states (PORRL). We accommodate two kinds of feedback -- cardinal and dueling feedback. We first demonstrate that PORRL subsumes a wide class of RL problems, including traditional RL, RLHF, and reward machines. For cardinal feedback, we present two model-based methods (POR-UCRL, POR-UCBVI). We give both cardinal regret and sample complexity guarantees for the methods, showing that they improve over naive history-summarization. We then discuss the benefits of a model-free method like GOLF with naive history-summarization in settings with recursive internal states and dense intermediate feedback. For this purpose, we define a new history aware version of the Bellman-eluder dimension and give a new guarantee for GOLF in our setting, which can be exponentially sharper in illustrative examples. For dueling feedback, we show that a naive reduction to cardinal feedback fails to achieve sublinear dueling regret. We then present the first explicit reduction that converts guarantees for cardinal regret to dueling regret. In both feedback settings, we show that our models and guarantees generalize and extend existing ones.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces PORRL a framework that adds internal states and intermediate feedback into Reinforcement Learning from Human Feedback, which can speedup alignment. The authors provide two model-based algorithms POR-UCRL, POR-UCBVI for learning with cardinal feedback, and provide regret bounds for GOLF (a prior model-free algorithm) based on a new history aware bellman eluder dimension “HABE”. They also provide a reduction from duelling to cardinal PORRL.

### Strengths
- The PORRL framework is novel, and their modelling is highly general with non-Markovian transitions. The paper is technically solid and a good contribution in the space of theoretical guarantees for learning from Human feedback.
- The authors analyse both model-based and model-free algorithms with regret guarantees under cardinal and duelling feedback.

### Weaknesses
The practical takeaways in the conclusion are mainly phrased as conjectures, and the authors do not provide a concrete algorithm within the PORRL framework. Given the strong theoretical contributions, a practical algorithm would have strengthened the work further.

Intermediate feedback at each step requires substantially more human queries than single preferential feedback at the end of an episode. Can you compare your framework's query complexity compared to that in [1, 2]?

### Questions
Intermediate feedback at each step requires substantially more human queries than single preferential feedback at the end of an episode. Can you compare your framework's query complexity compared to that in [1, 2]?

[1] How to Query Human Feedback Efficiently in RL?

[2] Reinforcement Learning from Human Feedback with Active Queries

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a general formulation for RLHF by introducing humans' internal states. This new framework allows reward and policy to be non-Markovian but still tractable. The authors propose algorithms for both cardinal and dueling feedback and obtain improved regret compared with previous methods. Interestingly, to design model-free algorithms for cardinal feedback, the authors introduce a modified Bellman-eluder dimension, which can be exponentially smaller than the standard Bellman-eluder dimension for the combination lock example. In the end, the authors also propose the first explicit reduction that converts guarantees for cardinal regret to dueling regret.

### Strengths
1. This paper provides a general RLHF framework covering many important instances.
2. The proposed algorithms lead to improved regret compared with existing results,
3. The authors propose the first explicit reduction that converts guarantees for cardinal regret to dueling regret.
4. A new complexity measure called HABE is proposed, which can be exponentially smaller than the standard Bellman-eluder dimension for the combination lock example.

### Weaknesses
1. The proposed algorithms follow existing frameworks, which are generally computationally inefficient. Specifically, the reliance on techniques like optimism in the face of uncertainty and the need to explore the entire state-action space, even with function approximation, can lead to impractical sample complexities, especially in high-dimensional environments. The paper does not provide a detailed analysis of the computational cost associated with these algorithms, making it difficult to assess their scalability for real-world RLHF applications.

2. This paper assumes the internal state generation function $g$ is deterministic. While this simplification might be useful for theoretical analysis, it overlooks the inherent stochasticity in human feedback. For instance, in a casual conversation, the same prompt might elicit different responses from the same person at different times due to varying moods, contexts, or interpretations. This deterministic assumption limits the applicability of the proposed framework to scenarios where human feedback is more nuanced and less predictable.

### Questions
1. On Page 7, three main technical challenges for model-based algorithms are mentioned. Could the authors give brief explanations of how the new design tackles these challenges?

2. The model-free algorithms follow GOLF, which requires Bellman completeness (BC). Does the adaptation here also need BC? If so, I think it is better to explicitly mention it in the main text.

3. For cardinal feedback, the paper assumes it is emitted according to a Bernoulli distribution. Is this assumption also used in previous papers for cardinal feedback? It seems the KTO paper utilizes a more complex feedback model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of reinforcement learning with partially observed reward-states (PORRL). The authors accommodate two kinds of feedback – cardinal and dueling feedback. The authors first demonstrate that PORRL subsumes a wide class of RL problems, including traditional RL, RLHF, and reward machines. For cardinal feedback, the authors present two model-based methods (POR-UCRL, POR-UCBVI). The authors give both cardinal regret and sample complexity guarantees for the methods, showing that they improve over naive history-summarization. The authors then discuss the benefits of a model-free method like GOLF with naive history-summarization in settings with recursive internal states and dense intermediate feedback. For this purpose, the authors define a new history aware version of the Bellman-eluder dimension and give a new guarantee for GOLF in the setting of this paper, which can be exponentially sharper in illustrative examples. For dueling feedback, the authors show that a naive reduction to cardinal feedback fails to achieve sublinear dueling regret. The authors then present the first explicit reduction that converts guarantees for cardinal regret to dueling regret. In both feedback settings, the authors show that the proposed models and guarantees generalize and extend existing ones.

### Strengths
1.	The authors introduce PORRL, which generalizes current RLHF models to incorporate “internal states” and intermediate feedback.
2.	The authors design model-based optimistic algorithms that, POR-UCRL and POR-UCBVI, and provide regret guarantees under naive history-summarization. The authors further show that their guarantees subsume and improve over past results. 
3.	The authors study the model-free algorithm GOLF, applied using history-summarization. The authors establish a regret guarantee for GOLF. The authors also show that when internal states have a recursive structure, their guarantee can be exponentially smaller than existing guarantees and guarantees for their model-based methods.
4.	The authors show that a naive blackbox reduction from dueling to cardinal PORRL always fails. They design a whitebox reduction from dueling PORRL to a large class of optimistic algorithms for cardinal PORRL.

### Weaknesses
1.	The writing of this paper needs improvement. This paper is too dense, and hard to follow.
2.	There is no experiment provided. It is hard to validate the effectiveness and implementability of the proposed algorithm, and the provided theoretical results.
3.	The authors should elaborative more on the motivation of combining POMDPs and RLHF, e.g., give 1-2 concrete application scenarios.
4.	The authors should discuss more on the technical novelty in combining POMDPs and RLHF. It looks like a combination of existing POMDP works and preference feedback.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2
