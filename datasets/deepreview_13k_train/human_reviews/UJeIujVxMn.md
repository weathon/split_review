# FedEBA+: Towards Fair and Effective Federated Learning via Entropy-based Model

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Federated Learning (FL) enables collaborative model training across decentralized devices while preserving data privacy.
However, achieving consistent global model performance across heterogeneous data distributions poses a challenge. Existing fairness algorithms often prioritize client accuracy at the expense of the global model's performance. To address this challenge, we propose a novel fairness algorithm derived from a bi-level optimization built upon the proposed constrained maximum entropy model. This approach concurrently enhances both global model performance and fairness. We further provide theoretical analysis, demonstrating how it guarantees convergence in the nonconvex FL setting and enhances fairness under generalized regression and strongly convex models. Empirically, our method outperforms state-of-the-art fairness FL algorithms, showcasing improved global model performance and fairer performance among clients.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the challenge of achieving fairness in FL without compromising the performance of the global model. The proposed FedEBA+ algorithm employs an entropy-based aggregation strategy to give higher weights to underperforming clients and an alignment update method to improve fairness and global model performance. The paper provides convergence analysis and fairness proof for FedEBA+, and shows that it outperforms existing state-of-the-art methods on several datasets in terms of both fairness and global model performance. The paper also conducts ablation studies to evaluate the impact of hyperparameters.

### Strengths
- The FedEBA+ algorithm addresses the accuracy-fairness trade-off issue. The extensive results on four datasets show that FedEBA+ reduces variance without compromising the performance of clients.
- An ablation study highlights the advantages of the proposed aggregation approach of FedEBA+. Specifically, it shows that the aggregation strategy alone can differ from FedAvg, while the addition of the aligned update ($\alpha$ >0) further improves performance, demonstrating the effectiveness of each component of the algorithm.
- Theoretically, the authors provide convergence analysis and fairness analysis.

### Weaknesses
The algorithm may have flaws: 
- The communication overhead appears to be much higher than FedAvg in Algorithm 1.  According to Line 3  and Line 9,  clients need to communicate with the server twice at each round t. This contradicts the traditional FedAvg that only communicates once at each round. This two-way communication is required because clients need the global gradient to regularize local training, which is not the case for other fairness-focused algorithms like q-FFL and AFL that manage with a single communication per round.
- In Line 9, $\tilde{g}^t$ is the fair gradient of the selected clients obtained using one local update. However, there is no step before line 9 that collects the one local update from clients. The authors should clarify this process. Furthermore, the notation $\tilde{g}^t$ in line 9 is not defined, and it is unclear how it differs from $\tilde{g}^{b,t}$ in line 6.
-  In algorithm 1, Line 10  indicates that Eq 3 will use the local model $x_{t,K}^j$ as $x$ to calculate the $p_j$. However, using local model $x_{t,K}^j$ for Eq 3 leads to different denominators $\sum_{i=1}^N \exp[F_i(x_{t,K}^j)/\tau]$ for different client $j$. Then $p_j$ for different clients is not normalized by the same denominator.  I am not sure how it satisfies the constraint  $\sum_j p_j=1$ in Eq 2. An explanation of how this approach satisfies the constraint would be helpful.


Writing: 
- Although the high-level idea is communicated well, the mathematical presentation could be improved for better accessibility. The paper's current use of a complex and inconsistent notation system hampers understanding.   For example, it seems that the notations, $\nabla \tilde{f}(x)$, $\tilde{\Delta}_t$,  and $\tilde{g}^t$ are interchangeably used to represent the FedSGD global gradient,  (e.g., the aggregation of one-step local updates) in different sections, causing confusion. 
- It would be clearer if the authors could connect Eq 8 and Eq 10 to Eq 6, given that they share a similar form and intuition. For example, Eq 6 is not referenced in Section 4.2.2, thus making the purpose of Equation 10 unclear.

- The motivation of maximum entropy for fairness may need further clarification.  Though the authors discussed fairness in the introduction and mentioned the Shannon entropy in Section 4.1, the connection between entropy and fairness is not intuitively clear. More explicit reasoning or examples illustrating why higher entropy equates to greater fairness would be beneficial, especially in federated learning settings.

- From equation (2),  the term “ideal loss” $\tilde{f}(x)$ is introduced without a clear definition or expression, leading to confusion that is not resolved until later sections (4.2.1 and 4.2.2).  It would be beneficial if the authors could provide more discussion or examples for  “ideal loss” here. 


Clarification: 
- The fairness of FedEBA+ is partly achieved based on the assumption that the FedSGD global gradient is an ideal fair gradient. Specifically, according to the end of Section 4.2, the authors view a FedSGD global gradient as the ideal global gradient and the ideal fair gradient. Clarity is needed on why this assumption is made and whether the FedSGD gradient truly encapsulates ideal fairness.  Also, it would be helpful to consider FedSGD as one fairness baseline in the experiments, to demonstrate the effect of another component in FedEBA+, maximum entropy aggregation, for fairness. 


- The following statement is not clear: “The specific challenge lies in finding a way to introduce entropy into the FL training process while incorporating FL’s uniform performance as a constraint within the framework.”  Isn’t maximum entropy encouraging uniform performance? (Intuitively,  the outcomes with uniform probability give the highest entropy, i.e., uncertainty, based on the definition of entropy)  Does maximum entropy go against the goal of uniform performance? The reason why these concepts are treated distinctly in this statement requires clarification. 

Theory: 
- The claimed convergence rate is not appropriate because there is a non-vanishing constant error term, which means that the gradient of the algorithm will never approach zero. The convergence rate is O(1) instead. This finding is inconsistent with previous studies, such as FedAvg convergence under the non-iid setting [1], which does not have the constant error term. 

- The Theorem 5.3 claims that FedEBA+ achieves a smaller variance than FedAvg. However, the effect of FL data distributions is not reflected in Theorem 5.3. It would be clearer if the authors could justify how non-iid degree will affect the fairness results. Moreover, could the authors provide definitions for T() and A() in the variance analysis?

Experiments: 
- The algorithms introduce a few additional hyperparameters: temperature $\tau$, angle threshold $\theta$, and $\alpha$. From Figure 4, it appears that the performance of the algorithm is quite sensitive to the hyperparameters, and different datasets have different optimal hyperparameters. It indicates a need for extensive hyperparameter tuning across different datasets. This requirement potentially reduces the algorithm's practicality compared to more straightforward federated learning algorithms like FedAvg.
- The influence of the angle threshold $\theta$ on FedEBA+'s performance is not demonstrated. It would be beneficial to provide an ablation study on  $\theta$.

### Questions
Please see my questions in Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces FedEBA+, an algorithm designed to increase fairness without sacrificing overall performance. It begins by formulating a constrained optimization problem to optimize the entropy of the aggregation probability while constraining the model to achieve ideal performance.

The algorithm includes convergence analysis, variance analysis, and pareto-optimality analysis. Additionally, the authors evaluate FedEBA+ on several datasets against various baseline algorithms, demonstrating its superior performance in terms of global accuracy and fairness.

### Strengths
1. The paper addresses an important question in federated learning systems: how to achieve fairness without sacrificing accuracy.
2. The proposed approach is supported by convergence analysis and fairness guarantees.
3. The proposed approach's effectiveness is demonstrated by comparing it with a significant number of baselines and presenting experimental results.

### Weaknesses
1. [Major] It is unclear which contributes to the improved performance, the optimization algorithm, or the entropy-based fairness regularization. 
2. [Medium] The performance of the proposed FedEBA+ doesn’t seem to be significant, especially in terms of worst 5% accuracy.

### Questions
See the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to formulate a concurrently fair and efficient protocol in federated learning. Even though fairness has been a widely studied topic in federated learning and many earlier works have discussed that, it remains a major challenge to design an FL algorithm that both improves the global (final) model performance and guarantees fairness. The authors tackled the challenge by modifying the aggregation rule via a method inspired by entropy, a central notion in information theory.

### Strengths
The source of inspiration is fundamental (information in the learning protocol).

The objective function is novel to the best of my knowledge, and many novel hyper-parameters (e.g. temperature) are intuitive and well-explained.

Analyses on convergence and fairness preservation are provided and comprehensive.

### Weaknesses
Section 5.2 carries significant importance as it assesses the fairness performance of the protocol. However, the analysis is based on regression only.

Although the authors' choice of definition of fairness (Definition 3.1, fairness via variance) is a common one, there are many more definitions available in the literature. Even in the cited original source of this definition (Li, et al 2019), they introduced a few other fairness metrics (cosine similarity and entropy). The theoretical analyses and experiments in this paper prove the FedEBA+'s efficiency for the chosen fairness definition for the regression task, but does not show the efficiency nor limitations for other definitions. It would also be beneficial if the authors could summarize some other commonly used definitions and comment on their advantages and disadvantages.

### Questions
As mentioned in the weakness section, there are some other fairness metrics, in the cited reference and some other ones. Would you provide any justifications to use this metric instead of others?

Did you try FedEBA+ on other tasks beyond regression?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
