# Personalized Federated Learning on Flowing Data Heterogeneity under Restricted Storage

- Decision: Reject
- Scores: 5, 3, 1, 6

## Abstract
Recent years, researchers focused on personalized federated learning (pFL) to address the inconsistent requirements of clients causing by data heterogeneity in federated learning (FL). However, existing pFL methods typically assume that local data distribution remains unchanged during FL training, the changing data distribution in actual heterogeneous data scenarios can affect model convergence rate and reduce model performance. In this paper, we focus on solving the pFL problem under the situation where data flows through each client like a flowing stream which called Flowing Data Heterogeneity under Restricted Storage, and shift the training goal to the comprehensive performance of the model throughout the FL training process. Therefore, based on the idea of category decoupling, we design a local data distribution reconstruction scheme and a related generator architecture to reduce the error of the controllable replayed data distribution, then propose our pFL framework, pFedGRP, to achieve knowledge transfer and personalized aggregation. Comprehensive experiments on five datasets with multiple settings show the superiority of pFedGRP over eight baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces pFedGRP, a framework for pFL aimed at handling Flowing Data Heterogeneity under Restricted Storage. This setup reflects real-world scenarios where data distributions shift over time on each client, and clients have limited data storage. To address these challenges, the framework uses a category decoupled data generator and a local data distribution reconstruction scheme. This approach reduces errors in data replay and improves knowledge transfer between clients.

### Strengths
1. The paper tackles the novel problem of personalized federated learning under flowing data heterogeneity with restricted storage, which closely mimics real-world scenarios where data distributions shift over time, and clients are limited in storage capacity. The formulation of Flowing Data Heterogeneity under Restricted Storage is an innovative extension of traditional pFL, making the problem more applicable to diverse, real-world environments where federated learning is deployed.
2. The experimental design demonstrates quality through comprehensive testing across multiple datasets, including MNIST, FashionMNIST, CIFAR-10, CIFAR-100, and EMNIST. These experiments reflect a thorough analysis of accuracy and robustness metrics, especially focusing on average accuracy (AA) and average forgetting measure (AFM) to evaluate both model performance and resilience to catastrophic forgetting. The comparisons include eight baseline methods spanning standard federated learning (FL), pFL, and FCL methods, providing a robust benchmark for assessing pFedGRP’s effectiveness.
3. The paper is generally well-written and organized. The introduction and related work sections give clear motivations and delineate the scope of pFL under dynamic data.

### Weaknesses
1. While the auxiliary model provides a solution for replay-based continual learning, its computational cost and storage implications for each client could be substantial. The paper would benefit from a deeper discussion of resource constraints, especially in low-power devices or large-scale networks with many clients. Specifically, the paper lacks a detailed analysis of the memory footprint required by the auxiliary models, including the number of parameters and the storage needed for generated replay data. Furthermore, the computational overhead for training these auxiliary models on resource-constrained devices is not quantified. A performance evaluation showing the time complexity and energy consumption for maintaining the auxiliary model on each client would offer a clearer picture of its feasibility, especially when compared to simpler, less resource-intensive methods.
2. The success of pFedGRP heavily depends on the accuracy of generated replay data. Any inaccuracies in replay could misrepresent past distributions, thus introducing bias or increasing the error in training. While the paper discusses mitigating catastrophic forgetting, more insight into replay quality control mechanisms could enhance robustness. The paper does not provide a clear mechanism for detecting and correcting errors in generated replay data. For instance, it is unclear how the framework handles situations where the auxiliary model fails to capture the nuances of a particular data distribution, leading to poor replay quality. This could involve ablations showing how variations in replay accuracy, such as the introduction of noisy or out-of-distribution samples, affect model performance, or exploring regularization methods to enforce consistency between real and replayed data distributions, such as adversarial training or consistency regularization.
3. The methodology section is dense, especially the part on personalized aggregation and knowledge transfer via auxiliary models. While it is generally clear, some steps (e.g., the loss function design in personalized aggregation) could use further elaboration to improve understanding. Readers less familiar with pFL and FCL may find it challenging to grasp these nuanced details without additional guidance. Specifically, the paper lacks a detailed explanation of how the auxiliary models are trained and updated. The interaction between the local models and the auxiliary models during the personalized aggregation process is not fully clear. Consider adding a step-by-step breakdown in the appendix, including a more detailed description of the loss functions, optimization algorithms, and the specific parameters used for training the auxiliary models, to enhance clarity.

### Questions
1. Could you provide further details on the replay quality? For example, how do you handle potential discrepancies between the generated replay data and the actual historical data distribution? Is there a mechanism for adjusting the auxiliary model if replay quality degrades over time?
2. What is the typical storage and computational cost of maintaining the auxiliary model on each client? Have you considered any optimization techniques to reduce this burden, especially for resource-constrained devices?
3. Given that the framework is tailored for dynamic data, could you conduct an ablation on the sensitivity to data drift? This might involve varying the rate of data distribution change to observe its impact on accuracy and forgetting metrics.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses personalised federated learning (pFL) on flowing Data Heterogeneity under Restricted Storage. Compared to existing pFL framework, the proposed solution, i.e., pFedGRP redesigns the generated replay scheme so that is can mitigate catastrophic forgetting and improve model generalization ability. Specifically, this paper applies an idea of category decoupling for adapting continuous learning into pFL to achieve knowledge transfer and personalized aggregation in pFL.

### Strengths
This paper somehow extends the pFL setting. It proposes a new pFL framework where the CL has been introduced with restricted by the category decoupling. Experimental results have demonstrated the effectiveness of the proposed method.

### Weaknesses
The motivation of the proposed method is not very clear. The methodology is not well presented. Especially, why this proposed pFedGRP is more effective than existing methods, which aspect, is less clear to me. Please refer to the question section for details.

This paper highlights the Restricted Storage. However, it is not explicitly explained what case refers to "restricted storage" till the experiment section. "Due to the FL setting of Flowing Data Heterogeneity under Restricted Storage where the client is unable to access the real data encountered in the previous task, each client can build up to 150 tasks on the MNIST and FashionMNIST datasets and up to 125 tasks on the Cifar10 dataset."---I don't understand why this can be considered as the experiment of "flowing Data Heterogeneity under Restricted Storage".

Why the setting has to be "flowing Data Heterogeneity under Restricted Storage"? Does it mean existing studies already addressed "flowing Data Heterogeneity"? This aspect is not fully reviewed which results in my concerns on the motivation and novelty of this paper.

This paper claims that the proposed method can "achieve the goals of personalized aggregation, mitigating catastrophic forgetting and improving model generalization ability while protecting privacy." However, the experimental result does not support this claim as pFedGRP performs poor in forgetting. This somehow indicates the good performance on accuracy is not because of the proposed mechanism but the experimental setting of  "Restricted Storage" as in this case, there is no need of memorizing.

### Questions
This paper highlights the Restricted Storage. However, it is not explicitly explained what case refers to "restricted storage" till the experiment section. "Due to the FL setting of Flowing Data Heterogeneity under Restricted Storage where the client is unable to access the real data encountered in the previous task, each client can build up to 150 tasks on the MNIST and FashionMNIST datasets and up to 125 tasks on the Cifar10 dataset."---I don't understand why this can be considered as the experiment of "flowing Data Heterogeneity under Restricted Storage".

Why the setting has to be "flowing Data Heterogeneity under Restricted Storage"? Does it mean existing studies already addressed "flowing Data Heterogeneity"? This aspect is not fully reviewed which results in my concerns on the motivation and novelty of this paper.

This paper claims that the proposed method can "achieve the goals of personalized aggregation, mitigating catastrophic forgetting and improving model generalization ability while protecting privacy." However, the experimental result does not support this claim as pFedGRP performs poor in forgetting. This somehow indicates the good performance on accuracy is not because of the proposed mechanism but the experimental setting of  "Restricted Storage" as in this case, there is no need of memorizing.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
pFedGRP targets the challenge of data distribution change with respect to time for each client in a federated learning setting, where clients do not have sufficient space to store all the data samples. Combining a personalization strategy with continual learning, the authors propose (a) a scheme to reconstruct local data, (b) a local training algorithm based on the generated data, and (c) a global aggregation scheme to merge personalized models to achieve better generalization across clients.

### Strengths
The challenge of data distributions of each client changing with time (or federated rounds) is relevant and practical, this work is targeting a good problem.

### Weaknesses
1. The readability is low. Excluding the language-related mistakes, the technical content is often too hard to parse. Many symbols have 4-5 sub/superscripts (e.g., $\theta_{A^{t-1, *}_{j, c^{''}}}$), and it gets pretty hard to keep up with all those symbols. Instead of just having long paragraphs laying out the proposed algorithm, an actual algorithm (like in Appendix C) in the main content would have massively improved the readability. 

2. Lack of having explored more relevant literature, and hence the lack of more relevant baselines. What the authors title "Flowing data heterogeneity" already is more popularly called "data drift", "concept drift" [1, 2], or "concept shift" [3] in literature. The authors claim that no personalization methods have looked into this challenge of "flowing data heterogeneity" (referring to line 67: "these works are generally proposed based on the assumption of the static local data distribution..."), that's because personalization methods target the challenge of "data heterogeneity" (different data distributions across the participating clients). But there are works [1, 2] (more can be found in the related work section of these two works) that do target the challenge of "changing data distribution with respect to time for all the client separately". Although I agree that if all clients change their local distributions, there would be "data heterogeneity across clients" as well, the authors have not compared against the baselines which can be closer to their work than the baselines only related to generating local personalized models.

3. The need of a "personalized global model" is unclear. Lines 164-165 say "the goal of our method is to customize personalized models for each client rather than training a model that performs well globally...", then why are each client's personalized models getting sent to the server? But then lines 95-96 state "the goals of personalized aggregation, mitigating catastrophic forgetting and improving model generalization ability,". 

4. The claims about "privacy-preservation" (line 96) seem unfounded. If the auxiliary task models of each client are getting sent to the server, what if an adversary gets access to the auxiliary models and can generate similar data to a specific client's data? Line 933 (Algorithm line 7 in Appendix C) shows that each client's class auxiliary model can be transmitted to other clients as well.

5. The whole of the "Local Data Distribution Reconstruction Scheme" seems like a solution for a general continual learning (CL) method aiming to address catastrophic forgetting. It is unclear how that section is related to FL, or what specific challenges FL brings which can hinder using this type of solution. 

6. The method is not scalable. These are the following models sent to each client each round: (a) A set of auxiliary models, (b) a personalized model specific to a client, and (c) an aggregated global model. Moreover, there are no communication (in terms of transmitted parameter count and size in MBs/GBs) and computation costs (a rough estimation of FLOPs) given in the manuscript, which seems essential to learn whether the performance benefits against the baselines are practical or not.

### Questions
1. In "Introduction", line 32 states "... to reduce \textbf{communication bandwidth} and \textbf{real-time requirements}". Can the authors clarify how clients uploading model weights to the server "reduces communication bandwidth"? And what are those "real-time requirements"? In practical deployments, one round can last from a few hours to a few days, so I am unsure about the "real-time" claim.

2. What is the Y-axis in Figure 1?

3. What does this sentence mean (lines 55-56): "FL methods should provide personalized global models for each client when \textbf{data heterogeneity is unknown}"? 

4. Is Eq 1 the objective of both FL and pFL methods? Is it one client's objective or the server-side global model's training objective?

5. Can the proposed approach "remember" multiple past distributions? Or only the most recent previous distribution?

6. Related to the previous question (Q5), lines 243-244 state "client can train the local task model on the data distribution $({ \mathcal{X}^{t-1}}, \mathcal{Y}^{t-1}) + \mathcal{P}^t $" (excluding some other notations for brevity). But what if the past and the current distributions conflicting? (As an extreme case, what if the past distributions have all the dog photos tagged as "dog", but the current distributions have all the dog photos tagged as "cat"?).

7. Are there no other CL works that have used something similar to the "Local Data Distribution Reconstruction Scheme"?

8. Do all clients have to participate in each round?

9. What is the rationale behind the grouping strategy (lines 411-412) for larger-class-count datasets like CIFAR100 and EMNIST62?

10. What are the practical examples of "FL with Tasks Gradually Changing"? In other words, are there any examples where a client's data oscillates between two distributions, and then one distribution changes into a third one?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes pFedGRP to tackle data heteogeneity in federated learning (FL). The authors propose a local data distribution reconstruction scheme and a related category decoupled data generator architecture, then propose pFedGRP framework with personalized aggregation and local knowledge transferring based on the replayed data distribution which is low error and controllable. Extensive experiments validate the contribution.

### Strengths
The problem studied is interesting. The proposed algorithm is novel.

The authors provide solid experimental studies.

### Weaknesses
In terms of data heterogeneity in federated learning, the current version does not consider a popular benchmark setting [1]. For example, the Dirichlet-based label distributions (Dir(0.5), Dir(0.1), etc), and quantity-based label distributions (C=1, 2, 3, etc) can be further experimented on. The authors are suggested to discuss and experiment the proposed algorithm on the comprehensive non-IID settings. This would make the conclusion more convincing if the algorithm can achieve SOTA performance on various non-IID settings.

[1] Li, Qinbin, et al. "Federated learning on non-iid data silos: An experimental study." 2022 IEEE 38th international conference on data engineering (ICDE). IEEE, 2022.

### Questions
See weaknesses. I think the current version is on the borderline and will adjust based on the author's response.

### Soundness
3

### Presentation
3

### Contribution
2
