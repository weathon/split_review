# FedCDA: Federated Learning with Cross-rounds Divergence-aware Aggregation

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
In Federated Learning (FL), model aggregation is pivotal. It involves a global server iteratively aggregating client local trained models in successive rounds without accessing private data. Traditional methods typically aggregate the local models from the current round alone. However, due to the statistical heterogeneity across clients, the local models from different clients may be greatly diverse, making the obtained global model incapable of maintaining the specific knowledge of each local model. In this paper, we introduce a novel method, FedCDA, which selectively aggregates cross-round local models, decreasing discrepancies between the global model and local models.
The principle behind FedCDA is that due to the different global model parameters received in different rounds and the non-convexity of deep neural networks, the local models from each client may converge to different local optima across rounds. Therefore, for each client, we select a local model from its several recent local models obtained in multiple rounds, where the local model is selected by minimizing its divergence from the local models of other clients. This ensures the aggregated global model remains close to all selected local models to maintain their data knowledge. Extensive experiments conducted on various models and datasets reveal our approach outperforms state-of-the-art aggregation methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Traditional federated learning aggregation methods only consider the local model from the current round, failing to account for differences between clients. The proposed FedCDA method selectively aggregates local models from multiple rounds for each client to decrease discrepancies between clients. By aggregating models that remain aligned with all clients' data, FedCDA can better preserve each client's local knowledge in the global model, outperforming state-of-the-art aggregation baselines as shown in experiments.

### Strengths
The paper is well organized, and it is mostly easy to follow the different parts.
This paper makes the multi-epoch aggregation model problem equivalent to a combinatorial optimization problem.
The method seems novel to me, however there may be other methods that include a similar mechanism which I have missed.
Sufficient theory illustrations well explain the objective of the proposed FedCDA.

### Weaknesses
 - The variables in the formula are very complex, and a lot of space was spent on deriving the objective function. At the same time, it is still difficult to understand why selectively aggregating them can make the global model approach local models more closely and affect the targeting of local data knowledge? Specifically, the paper does not clearly articulate how the proposed selection mechanism ensures that the aggregated global model is closer to the local optima of individual clients compared to standard aggregation methods. The intuition behind the cross-round aggregation and its impact on preserving local knowledge remains unclear. It would benefit from a more detailed explanation of how the distance between the global model and local models is minimized through the selection process.
- It seem that the caption of Fig(2) is wrong.
- There seems to be a lack of discussion on memory and communication costs. While the paper mentions caching models, it does not provide a thorough analysis of the memory overhead, especially in scenarios with a large number of clients or complex models. Furthermore, the communication costs are not discussed in detail, and it is unclear if the proposed method introduces any additional communication burden compared to traditional federated learning approaches.

### Questions
- How to understand that there are varied received global models and they result in local models? (Quote from Introduction: "each client often converges to different models due to varied received global models and multiple local optima of deep neural networks”?)
- Do the local models achieve different local minimal only due to their own private local data?
- Why are there varied received global models?
- Authors claim that selectively aggregating them can make the global model approach local models more closely and affect the forgetting of local data knowledge. 
- Does Equation (2) have used the approximation (∇wn Fn(wn))’ ≈ 0 ?
- What is the meaning of N-P+bP/B? why add the #nums unselected N-P?
- why selectively aggregating them can make the global model approach local models more closely and affect the targeting of local data knowledge? 
- Authors seem to use the random sampling strategy to minimize the eq.7, i.e. selectively aggregating multi-epoch local models, what if P=N?
- The authors aim to make the global model approach any of the different local models in multiple rounds, how do define the “approach”, and how approach between the multi-local epoch global model and last-epoch local models?
- What differences between this work “Understanding How Consistency Works in Federated Learning via Stage-wise Relaxed Initialization. Dacheng Tao et.al .Nips2023.”

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced FedCDA to solve statistical heterogeneity issues, especially the discrepancies between local models. The principle behind FedCDA is that the local model from each client may converge to different local optima over rounds. Based on this principle, the author utilizes a local model from multiple rounds to minimize the divergence from other clients to make sure that the aggregated global model remains aligned with selected local models. Empirical results show their algorithm’s superiority to other benchmark methods.

### Strengths
1. The proposed algorithm addressed the data heterogeneity issues from a novel view, considering the aggregation of cross-round local models. 
2. This paper provides theoretical insights and the convergence bound of the proposed method.

### Weaknesses
1.	In FedCDA, each local client needs to store a set of recent K local models, which requires a much higher demand of memory space compared to other FL methods.
2.	Although FedCDA employed the approximation strategy, communicating the model set is still too heavy and the considerable extra communication may be a severe problem when there exists a large number of engaging clients.

### Questions
1.	Why not compare with those methods that personalize partial model parameters for each client? Personalized Federated Learning can help local models adapt to local data distribution.
2.	FedCDA maintains a consistent global model that will not interfere with those outlier local models as the authors selected the closer local model to do aggregation. The potential problem is that the aggregated model may not adapt to those outliers and be quite sub-optimal.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focus on designing a model aggregation strategy for federated learning. Different from the traditional methods that aggregate local models from the current round only and may cause diversity issues, this paper introduces FedCDA, which selectively combines models from different rounds to maintain knowledge diversity. Experiments show that FedCDA outperforms the existing model aggregation methods.

### Strengths
1. This paper is easy to follow.
2. To the best of the reviewer's knowledge, the approach presented in this paper, which involves the selective aggregation of local models from various rounds to mitigate disparities between them, appears to be relatively novel.
3. The author conducted an extensive series of comparative experiments.

### Weaknesses
1. First of all, the motivation about Figure 1 is difficult to understand, where the authors attempt to illustrate the usefulness of cross-round local models. But according to the reviewer's understanding, the model aggregation strategy of Fig. 1(b) will cause the global model to overfit to the local node, resulting in extremely unstable global convergence. Further clarification is needed on why it is better to update model via Fig. 1(b).
2. Why the optimization objective function presented in Eq. (2) is derived based on the effectiveness of cross-round local models remains unclear. The connection between the optimization objective and the effectiveness of cross-round local models requires further elucidation.
3. Another issue lies in the optimization objective presented in Eq. (7) on the server side, where model derivatives appear to be computed for inactivate nodes. Question then arises as to whether these non-active models are stored on the server side. In federated scenarios characterized by a large number of nodes and typically large models, this could lead to substantial storage overhead.

### Questions
In Theorem 3, the authors claimed that convergence is achievable but did not provide a specific rate of convergence. It would be beneficial for the authors to elucidate the relationship between the convergence rate and parameter $T$ to enhance the assessment of the theoretical contribution when compared to other algorithms.

*Post-rebuttal comments:*

While some of my concerns have been addressed, several questions still remian.

1. The author's depiction of motivation in Figure 1 still appears somewhat speculative. The clients trained based on local data, and the rationale behind the considerable variation in the direction of updates across clients in different rounds remains unclear.

2. The proposed method incurs a substantial storage cost, significantly constraining the practicality of the algorithm.

Overall, I will maintain the original score.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Unlike existing federated learning methods that aggregate the weights of local models of clients participating in the current round, this paper proposes an aggregation method that considers local models from recent rounds for the first time. This idea uses the fact that local models in different rounds within a client converge to different local optimal points after the warm up stage, as clients perform local training of multiple epochs to reduce communication costs. This paper also proposes several tricks to simplify the computation of which local model to select and aggregate among local models from multiple rounds. In addition to the theoretical background of the proposed method, experiments show that it has better performance compared to other aggregation methods.

### Strengths
The idea of selectively aggregating local models from several recent rounds is novel. It seems to have successfully overcome the limitations of existing aggregation methods by taking advantage of the fact that deep learning models have multiple local optimal points.

The feasibility and reasoning of the proposed method were confirmed through several theoretical backgrounds. Also, several tricks were presented to reduce the computational complexity of the proposed method.

### Weaknesses
The effectiveness of the proposed method was not sufficiently proven in the evaluation section, so doubts remain about the proposed method.

Considering that the proposed method is about a new aggregation method, 20 clients and a participation ratio of 20% are too unrealistic.

As shown in figure 2 (c), the proposed method is sensitive to local epoch hyperparameter because it assumes that local models converge. However, most experiments are conducted at a local epoch of 20, and such a large local epoch makes comparisons with baselines unfair. It is of course an advantage that the performance of the proposed method is good even when the local epoch is large, but this does not mean that simply increasing the local epoch is always good. 

In addition to the local epoch, I believe that other hyperparameters used in the experiment are not suitable for comparison with baselines.

For example, the learning rate was set to 1e-3, which helps the local model to converge quickly with a large local epoch. However, it is unclear whether such a small learning rate and large local epoch are suitable for other baselines.

Based on the code included in the supplementary material, I reproduced the FedAvg experiment of CIFAR100 - Dirichlet (0.5) in Table 1. Using the same hyperparameter presented in the paper, FedAvg showed an accuracy of about 38%, which is almost similar to 38.86% recorded in Table 1. However, when lr is 0.1, weight decay is 1e-3, local epoch is 5 and the same experiment was performed with SGD without momentum, the accuracy was about 49%, which is almost similar to the proposed method (49.31%). This does not mean that the proposed method shows similar performance to FedAvg, but I just think that the hyperparmaters should have been chosen a little more carefully. (If possible, can you run the experiment again with the hyperparameters mentioned above?)

The overall writing quality of the paper is not good. There are many incorrect parts in the notation related to formulas and figures in the paper, and many sentences require revision.

### Questions
Please refer to weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good
