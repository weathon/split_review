# Flashback: Understanding and Mitigating Forgetting in Federated Learning

- Decision: Reject
- Scores: 3, 3, 5, 3, 5

## Abstract
In Federated Learning (FL), forgetting, or the loss of knowledge across rounds, hampers algorithm convergence, particularly in the presence of severe data heterogeneity among clients.
    This study explores the nuances of this issue, emphasizing the critical role of forgetting in FL's inefficient learning within heterogeneous data contexts. Knowledge loss occurs in both client-local updates and server-side aggregation steps; addressing one without the other fails to mitigate forgetting. We introduce a metric to measure forgetting granularly, ensuring distinct recognition amid new knowledge acquisition.
    Leveraging these insights, we propose Flashback, an FL algorithm with a dynamic distillation approach that is used to regularize the local models, and effectively aggregate their knowledge.
    Across different benchmarks, Flashback outperforms other methods, mitigates forgetting, and achieves faster round-to-target-accuracy, by converging in 6 to 16 rounds.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper formulates the NonIID problem in FL as the catastrophic forgetting from both local and global perspective. To solve this problem, they propose using knowledge distillation in both local and global sides to maintain knowledge to mitigate forgetting.

### Strengths
1.	The NonIID problem in FL is important and using distillation to solve this issue achieves promising results.
2.	The writing is easy to follow.

### Weaknesses
The major concern is that the experiments are too limited: 
1.	All baselines are too old. The newest baseline FedReg which is proposed in 2022. In fact, many recent baselines for soving the NonIID problem are proposed in 2023 and 2024.
2.	The evaluations should be conducted on different NonIID settings. This paper only adopt a fixed NonIID setting across all datasets, which is not sufficient to demonstrate the effectiveness of the proposed method.
3.	Larger models such as ResNet18 can be included. Merely 2-layer CNN may not be enough.
4.	Varying fraction of one-round selected clients should be evaluated. This factor is strongly related to the global knowledge forgetting. 
5.	Current datasets only cover 10-classes settings, which may be limited to make a comprehensive comparison because $\alpha$ proposed by the method is strongly related to the number of classes. Cifar100 is recommended to add to the experiments.

### Questions
1.	Federated Continual Learning (FCL) also focuses on the catastrophic forgetting problem. What’s the difference between the problem of this paper and that of FCL?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work focuses on addressing the problem of data heterogeneity in federated learning. This work analyzes the mechanism of data heterogeneity in multiple rounds of iterations of federated learning from the novel perspective of forgetting. In addition, this paper proposes a new metric for measuring the degree of forgetting between training rounds. The major contribution of this paper is the proposed Flashback algorithm, which utilizes knowledge distillation to mitigate forgetting during the local update and global update phases. In conclusion, this paper presents a novel perspective to study data heterogeneity in federated learning and proposes methodological solutions, and the article ideas are easy to understand.

### Strengths
This paper deals with data heterogeneity in federated learning from the perspective of forgetting which is very novel and gives a comprehensive framework from observation, derivation, solution design and experimental proof.

It is well written and easy to understand.

### Weaknesses
1 The researched work related to data heterogeneity in federated learning is insufficient, especially for personalized federated learning and clustered federated learning.

2 The elaboration of the concept of forgetting is not detailed enough, lacking comparisons between different categories of continual learning (class-CL, task-CL, domain-CL), and lacks a detailed elaboration of forgetting mechanisms (e.g., weight drift, activation drift, inter-task confusion, and task-recency bias).

3 The forgetting metric between training rounds proposed in this paper is also computed based on accuracy, which is not different enough from the forgetting rate metric in continual learning to be considered as a contribution point.

4 The idea of using knowledge distillation in Flashback has been widely used, and the approach in this paper lacks innovation.

5 Flashback's dependence on labeled datasets on the server side is the major limitation and is not feasible in real scenarios, perhaps try unlabeled datasets or data-free distillation.

6 The experiments are less persuasive:

The datasets used (CIFAR10, CINIC10, FEMNIST) are too simple, it would be more persuasive to use more complex datasets such as CIFAR100 or TinyImageNet.

Comparison methodology lacks the most recent work (including 2023 and 2024) and work related to personalized federated learning.

7 The font sizes in images is inconsistent, e.g., Figures 4 and 5.

### Questions
What are the differences between forgetting in federated learning and forgetting in continual learning?

What are the differences between the federated continual learning scenario and the federated learning scenario in this paper?

Since the paper states that forgetting occurs in both local updating and global aggregation phases, shouldn't there be more detailed forgetting metrics (e.g., phased forgetting metrics)?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
his paper analyzes the problem of forgetting in a non.iid federated learning environment, and concludes that the forgetting occurs in local updating and aggregation processes. For this, the authors propose metrics to measure the degrees of forgetting in the training process. In addition, the authors propose Flashback, a knowledge distillation (KD)-based model to mitigate forgetting. Flashback allows both clients and the server to perform dynamic KD according to the relative label count, and achieve fast convergence against baselines.

### Strengths
1. The authors provide a detailed analysis and illustration of the key issues - where forgetting occurs in non.iid FL, which is an important problem in FL.

2. The proposed Flashback method is simple and easy to understand, and it outperforms a variety of FL baselines

3. This paper introduces fine-grained evaluation metrics for forgetting in FL.

### Weaknesses
1. This paper proposes a fine-grained metric for assessing forgetting, but this does not seem to be reflected in Flashback. The authors should emphasize the connection between this metric and Flashback. Specifically, it's unclear how the insights gained from the forgetting metric directly inform the design choices within the Flashback algorithm. The paper would benefit from a more explicit explanation of how the metric guides the selection of the knowledge distillation strategy or the dynamic adjustment of distillation parameters.

2. I have concerns about the use of the public dataset on the server. If the distribution of that dataset is similar to the distribution of data on each client, does this mean that there is already a leakage problem in that environment? Also, I'm curious what happens if a different dataset is used than the training dataset (e.g., cifar10 as the public dataset and cinic10 as the training data). The paper should include experiments with public datasets that have different distributions from the client data to fully explore the robustness of the proposed method.

3. The authors should reorganize Sections 3, 4 for clearer understanding, and placing the algorithm in 4.1 would make it easier to understand. Currently, the flow of ideas between the analysis of forgetting and the introduction of Flashback is not smooth. The algorithm description should be placed earlier to provide a clearer context for the subsequent experimental results.

4. Flashback involves a variety of additional parameters (e.g., label counts for teacher and student models, dependency on the global model, etc.), do these parameters make the algorithm less robust to some extent? This paper would benefit from an analysis of this problem. Specifically, a sensitivity analysis of these parameters and their impact on the performance of Flashback is needed to understand the robustness of the proposed method. The paper needs to clarify how the algorithm's performance varies with different choices of these parameters.

5. Missing some related works, e.g. test-time FL [1-3].

### Questions
In addition to the weaknesses, one more question is as below.

1. In the experiments, do all baselines use the public dataset on the server?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new distillation method to solve the NonIID problem in FL. Specifically, they consider the NonIID problem will cause the forgetting of model knowledge in both local update and global aggregation processes. Then, they apply the distillation over both local and global processes to mitigate the forggeting.

### Strengths
1. The NonIID problem in FL is important and using distillation to solve this issue achieves promising results.

2. The writing is easy to follow.

### Weaknesses
1. The novelty is limited. In fact, there have been massive methods using knowledge distillation to solve the NonIID problem, e.g., [1,2]. The experiments should also include them for the comprehensiveness of comparison.

[1] DaFKD: Domain-Aware Federated Knowledge Distillation. CVPR 2023.

[2]  Data-free knowledge distillation for heterogeneous federated learning. ICML 2021.

2. It is better to include a figure to illustrate the method framework for ease of understanding.

3. It would be better if the theoretical advantages were provided.

4. The ablation study about the proposed method of local and global distillation should be provided.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The motivation of this paper is to address the problem of forgetting in Federated Learning (FL), which slows down convergence, particularly in settings with high data heterogeneity among clients. The main contribution is the introduction of Flashback, a new FL algorithm that uses dynamic distillation to mitigate forgetting by regularizing both client-local updates and server aggregation.

### Strengths
(a) The method includes comparisons with a variety of baselines that incorporate regularization and distillation techniques. 

(b) The paper is well-written, with clear presentation and structure that is easy to follow.

### Weaknesses
 (a) The investigation of forgetting is less systematic than claimed. While the paper frames forgetting as a key factor in FL underperformance, it lacks detailed analysis and comparisons with baselines from continual learning, where many regularization- [1] based methods effectively mitigate forgetting. Exploring whether these methods can similarly address forgetting in FL would be valuable.

(b) Fairness in performance comparison on public datasets is an issue, as the proposed method uses a portion of data for validation while other methods do not, making the comparisons unfair. Including simple baselines that utilize similar validation strategies, such as server-side distillation [2] or model selection, would improve fairness.

(c) The motivation and application of the new forgetting metric in FL are not clearly explained, making it difficult to fully understand this contribution’s impact.

### Questions
(a) Why are so many values missing in Table 1, particularly for the FEMNIST dataset?

(b) Why is the baseline performance on FEMNIST so low, appearing to learn almost nothing, and why does performance fluctuate significantly across all datasets? This fluctuation suggests that hyperparameters may not be well-tuned for optimal convergence. Providing the training and validation loss trends for each baseline would help demonstrate convergence.

### Soundness
3

### Presentation
3

### Contribution
2
