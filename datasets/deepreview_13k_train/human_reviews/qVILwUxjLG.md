# Non-stationary Contextual Bandit Learning via Neural Predictive Ensemble Sampling

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
Real-world applications of contextual bandits often exhibit non-stationarity due to seasonality, serendipity, and evolving social trends. 
While a number of non-stationary contextual bandit learning algorithms have been proposed in the literature, they excessively explore due to a lack of prioritization for information of enduring value, or are designed in ways that do not scale in modern applications with high-dimensional user-specific features and large action set, or both. In this paper, we introduce a novel non-stationary contextual bandit algorithm that addresses these concerns. It combines a scalable, deep-neural-network-based architecture with a carefully designed exploration mechanism that strategically prioritizes collecting information with the most lasting value in a non-stationary environment. Through empirical evaluations on two real-world recommendation datasets, which exhibit pronounced non-stationarity, we demonstrate that our approach significantly outperforms the state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the contextual bandits due to non-stationarity caused by factors like seasonality and evolving social trends. Existing algorithms either overly explore or cannot handle high-dimensional user-specific features and large action sets. The paper introduces a non-stationary contextual bandit algorithm that combines a scalable deep neural network architecture with a strategic exploration mechanism that prioritizes valuable information in a changing environment. Empirical evaluations on real-world recommendation datasets with non-stationarity show that this approach outperforms state-of-the-art baselines.

### Strengths
It is very interesting and necessary to extend neural bandits to the non-stationary environment. It is indeed my first time to see the neural bandit's work extending to non-stationary. The introduced algorithm is embedded with slide window to overcome the changing reward mapping.

### Weaknesses
However, (1) I am not very convinced by the exploration effectiveness of ensemble networks. The exploration comes from randomly draw ing neural models, but it doesn't consider the estimation confidence interval of a single neural model like UCB or TS. It looks like an ensemble of greedy models. The random sampling of neural networks for exploration lacks a theoretical basis tying it to regret minimization, unlike methods that explicitly consider uncertainty in their estimates. Specifically, the method does not account for the variance in the predictions of each neural network, which is a crucial component for effective exploration in bandit algorithms. Without this, the algorithm may not explore efficiently, especially in high-dimensional spaces where the uncertainty is high.

(2) The training cost is too huge for this approach. In linear bandits, the training of linear models can be trained quickly. But for neural models, it cannot work. For one neural model, the training cost is already huge, but the algorithm needs to train a set of neural models in each round. Especially, it is for online learning scenarios. I don't think this algorithm can be scaled to large systems in practice. The computational burden of training an ensemble of neural networks in each round is a significant practical limitation. The paper does not provide a detailed analysis of the computational complexity, which is crucial for understanding the scalability of the proposed method. Furthermore, the memory requirements for storing and updating multiple neural network models could also be a bottleneck.

(3) The analysis is for the linear model with linear reward function, which avoids the challenge of analyzing neural networks. This theoretical analysis does not address the core challenge of the paper, which is the use of neural networks. The analysis should be extended to the neural network setting to provide a more comprehensive understanding of the algorithm's performance. The current analysis only provides limited insights into the performance of the proposed method in the context of neural networks.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study a non-stationary contextual bandit problem and propose an algorithm called Neural Predictive Ensemble Sampling (NeuralPES), which is scalable with neural network structure and incorporates an exploration mechanism. The authors provide theoretical results that show the strength of their method over NeuralEnsemble, a neural network based Thompson sampling algorithm. Finally, they conducted numerical experiments and tested the effectiveness of their approach on non-stationary real-world data.

### Strengths
- The paper is well organized, with both theoretical results and empirical evaluations on real-world data set.
- The problem of non-stationary contextual bandits remain largely unexplored and has potential real-world significance. 
- The authors provide good insights for why prioritizing last information is important in a non-stationary environment.

### Weaknesses
 - One major weakness is that I find it hard to evaluate the significance of the theoretical results presented in this paper. It appears that the authors have only compared the performance of the LinPS algorithm against TS in a non-stationary environment, which is restricted to linear contextual bandits setting and also does not really reflect the optimality/near-optimality of the algorithm. 
- It is unclear how the non-stationarity of the environment is defined. Does the proposed algorithm deal with all kinds of non-stationarity? Related to the point I raised above, the theoretical results that the authors provide are only for environments with abrupt change or AR(1) type of changes. But the paper positions itself in a way that suggests the algorithm can deal with any kind of non-stationarity.
- The current results also appear to extend from similar results established under the non-contextual bandit setting. A discussion that establishes connection between the results here and those for non-contextual bandits would be helpful. 
- The presentation of the algorithms also make it difficult for readers to comprehend what each component is designed for. Currently there are 5 algorithms in the paper and the relationship among these algorithms is unclear. For example, what is TrainNN used as part of Algorithm 4? What are the connections between all of the algorithms? Why are you presenting Neural Ensemble Sampling before NeuralPES and can you highlight the differences?

### Questions
I also have some questions related to the theoretical results established:
- Could you provide more discussions that help readers understand the regret bounds in Theorem 1 and Corollary 1? For example, I am not sure what is $\mathbb{I}(\theta_2; \theta_1)$ in the regret bound of THM 1. In corollary 1, please also elaborate on what the entropy term represents.
- I am also unsure of the statement that says when $\theta_t$ changes very quickly, “then the regret of LinPS is zero that LinPS achieves optimal”. Could you elaborate? From the regret term defined in Definition 3, it seems that the benchmark that the algorithm is compared against is the best arm at every $t$. How could the regret be zero when the changes are even more frequent?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the contextual nonstationary bandit problem, presenting NeuralPES, a deep neural network-based algorithm as a solution. The algorithm is a combination of ensemble sampling and future reward prediction, achieved through sequence modeling.

In essence, NeuralPES can be interpreted as a neural network implemented version of Linear Predictive Sampling (LinPS), a model that holds regret guarantees under various nonstationary environments.

The effectiveness of this approach in dealing with nonstationarity is corroborated by experiments conducted with (i) synthetic data, (ii) a real-world dataset featuring short-term nonstationarity (one week), and (iii) a real-world dataset with long-term nonstationarity (two months).

### Strengths
This paper, to my knowledge, is the first to address nonstationarity by considering the rate at which information disappears in the future, taking into account the applicability to real-world data.

In real-world data, there exist high-dimensional, non-linear, and diverse features (or contexts). This paper proposes a neural network-based method and architecture that allows efficient handling of these features while effectively addressing non-stationarity (via prediction). The usefulness of this approach has been verified across various applications.

As an algorithm, it enables NN-based sequence reward modeling, which predicts future rewards based on the weight sequence of past models, and ensemble sampling, which can be applied even when it is difficult to calculate the posterior distribution, to be combined.

The authors have been able to experimentally demonstrate superior performance compared to other neural-based bandit algorithms, as well as their sliding window versions.

### Weaknesses
I have many concerns regarding this paper, all of which I believe to be addressed by the authors.

1. The paper lacks a clear comparative analysis between PS and NeurPS. It would be beneficial for the readers if the authors could elucidate the apparent differences between the two. Specifically, a table summarizing the key differences in terms of computational complexity, memory requirements, assumptions about the environment, and the type of non-stationarity each can handle would be highly valuable. Without this, it is difficult to understand the specific advantages of the proposed method.

2. The authors mention that PS "suffers from their scalability" and "it does not efficiently scale", however, the specifics of these issues are not clearly outlined. I would recommend providing concrete examples or explanations to support these statements. For instance, what specific computational bottlenecks does PS encounter when dealing with high-dimensional context spaces or a large number of actions? Are these limitations related to memory usage, or are they due to the need to sample infinite reward sequences?

3. It seems that PS (Liu et al. 2023) operates on an infinite reward sequence for decision-making, yet this element is not present in the current paper. It would be interesting to know how this differs or if it is similar. Either way, a discussion on this point seems necessary. The authors should clarify whether NeuralPES approximates this infinite sequence with a finite horizon, and if so, how the length of this horizon is determined and what impact it has on the algorithm's performance. A discussion of the trade-offs between computational cost and approximation accuracy would be beneficial.

4. The theoretical analysis may appear almost identical to that of (Liu et al. 2023). Are there any differences that the authors could highlight? Specifically, it would be helpful to see a detailed comparison of the assumptions made in the theoretical analysis of both methods, and how these assumptions impact the applicability of each method to different types of non-stationary environments. A clear explanation of any modifications or extensions to the original theoretical framework is needed.

5. How much execution time is required for NeuPS's learning and inference (or decision-making)? Considering the time-intensive nature of neural network training and inference, and even more so for ensemble models (depending on the value of M), it would be important to discuss the scalability implications of the execution time. A breakdown of the time spent on different stages of the algorithm (e.g., forward pass, backpropagation, ensemble sampling) would be useful.

6. Given that the authors are using an "A100 40GB GPU", if the learning time is long, this could significantly increase the cost, which is a critical factor for practical applications. A more detailed analysis of the computational resources required by NeuralPES, including memory usage and GPU requirements, is necessary to assess its practical feasibility.

7. The authors state that "the regret of LinPS is zero" and "LinPS achieves 0 regret". Is this regret referring to long-run average regret? The authors should explicitly define the type of regret they are referring to (e.g., cumulative regret, average regret) and clarify the conditions under which this zero regret is achieved. It is essential to be precise in the definition of regret.

8. The paper mentions that the algorithm "is such optimal". It would be helpful if the authors could clarify what they mean by "optimal", as many algorithms can achieve a long-run average regret of 0. The authors should provide a precise definition of optimality in the context of their algorithm, and explain how this optimality is achieved. Is it optimal in terms of regret, sample complexity, or some other metric?

9. How is the ensemble size M set? Is it adjusted for each experiment? Knowing the effect of its size on reward changes and computation time seems necessary for demonstrating scalability. A sensitivity analysis of the ensemble size M on the performance of the algorithm, including its impact on both reward and computational cost, is needed to understand the trade-offs involved.

10. For the long-term experiments, how is the data processed? The authors mention grouping every 12 hours of recommendation into a contextual bandit format. Does this mean that the order of recommendations presented within the 12-hour period is ignored? If so, could this introduce bias? The authors should discuss the potential impact of this data aggregation on the results, and whether it introduces any biases or limitations. A more detailed description of the data processing steps is needed.

11. Despite the major contributions of the paper appearing to lie in the experimental section, the experiments are not written in a reproducible manner. The code is not shared, and it seems that there are parameters, such as the value of M, that are not mentioned in the paper.

### Questions
I hope you can answer me about the comments I wrote in Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose their NeuralPES algorithm and mention that it aids recommendation systems for real-world dynamics such as seasonal preferences. They combine a  neural network architecture with their  proposed exploration strategy which they claim can more efficiently gather valuable information in evolving environments. They empirically evaluate it on real world datasets such as the Microsoft News website, where they compare it against baselines.

### Strengths
* Overall the paper is well written and clear to follow.
* The theoretical analysis and ablation studies are comprehensive.

### Weaknesses
* Nit: Some of the plots (Figure 3) are hard to read, could be plotted more clearly.
* It would be interesting to see this evaluated in a a real world dataset, distinct from the recommender system tasks to compare it's performance in a different domain, eg dynamic pricing

### Questions
The limitations of the work are not clearly described. What are (if any) some of the challenges with this approach?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
