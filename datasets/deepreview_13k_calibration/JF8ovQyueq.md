# Interaction Based Gaussian Weighting Clustering for Federated Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Federated learning emerged as a decentralized paradigm to train models while securing privacy. However, conventional FL faces data heterogeneity and class imbalance challenges, affecting model performance. In response to these issues, Personalized FL has been developed as an innovative methodology that relies on fine-tuning the distinct local models based on individual training datasets. In this work, we propose a novel PFL method, FedGW (Federated Gaussian Weighting), which groups clients based on their data distribution, allowing training of a more robust and personalized model on the identified clusters. FedGW identifies homogeneous clusters by transforming individual empirical losses to model client interactions with a Gaussian reward mechanism. Additionally, we introduce a new clustering metric for FL to evaluate cluster cohesion with respect to the individual class distribution. Our experiments on benchmark datasets show that FedGW outperforms existing FL algorithms in cluster quality and classification accuracy, validating the efficacy of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the heterogeneity and class imbalance issues in FL, this paper proposes FedGWC, a novel PFL method. Further experiments show that FedGWC outperforms existing FL methods. The clients are grouped into clusters with similar data distribution based on an interaction matrix.

### Strengths
- Comprehensive experiments
- mathematical analysis.

### Weaknesses
 - This paper is hard to follow, especially in the methodology part. e.g, the description of Eq(1). It is also unclear how we get the clusters based on Algorithm 1.
- What’s the meaning of the dash line in Figure1 and how we get the average loss process.
- The relation between $L_k^{t,s}$ and $l_k^{t,s}$.
- What if some clients are hardly sampled, does that affect his reward estimate?
- In the line 259, “relying only on the values of the Gaussian weights is insufficient to identify clusters of clients with similar data distributions, as they do not capture the interactions among pairs of clients.” However, it is not clear why we need the interactions among pairs of clients. I can not catch the motivation.
- What is the clients’ sampling rate at each round?
- It is not applicable that this method needs 20000 communication rounds to be converged.
- Extra communication and computation overhead analysis is needed to compare with baselines.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose a novel PFL method named FedGWC (Federated Gaussian Weighting). FedGWC groups clients based on their data distribution, allowing training of a more robust and personalized model on the identified clusters. The experimental results have shown the effectiveness of the proposed method and its versatile integration to various FL aggregation algorithms.

### Strengths
1. FedGWC introduces a Gaussian weighting method that offers a fresh approach to clustering by leveraging interaction-based weights instead of relying on traditional model updates. 
2. The proposed method addresses significant FL challenges like non-IID data and class imbalance, showing strong adaptability in scenarios with high heterogeneity.
3. The FedGWC algorithm can be applied with various FL aggregation algorithms (e.g., FedAvg, FedProx) and performs well even with personalized FL techniques like pFedMe and Per-FedAvg.
4. The paper provides a mathematical foundation for the convergence and consistency of the Gaussian weights, adding robustness to the proposed method.

### Weaknesses
1. Although the algorithm mitigates communication overhead, the interaction matrix and clustering computations may still introduce complexity, especially in large-scale FL deployments with a high number of clients.
2. The paper doesn’t extensively discuss the implications of FedGWC’s clustering on privacy, especially since clustering-based methods might reveal distribution characteristics indirectly.
3. The clustering results are influenced by parameters such as the RBF kernel spread, which could require extensive tuning. This dependency may limit FedGWC’s practicality across different datasets without manual optimization.
4. The empirical validation is limited to specific datasets (CIFAR10, CIFAR100, and FEMNIST). Broader evaluations on diverse datasets, including real-world applications, could strengthen the practical applicability of the findings.

### Questions
I would be appreciated if the authors can address my concerns listed in the weaknesses, including the communication efficiency, privacy, scalability, and more comprehensive experiments.

### Soundness
3

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
3

### Summary
This paper proposes a personalized federated learning (PFL) framework called FedGWC (Federated Gaussian Weighting Clustering), which groups clients based on data similarity using Gaussian weighting on empirical losses. This clustering technique is designed to address data heterogeneity and class imbalance by forming homogeneous clusters, where each cluster benefits from personalized federated models trained on data with similar distributions. The authors introduce a clustering metric for evaluating cohesion among clients and conduct experiments that demonstrate FedGWC's performance gains over baseline methods in heterogeneous data scenarios.

### Strengths
1. The FedGWC method effectively addresses the challenge of data heterogeneity and class imbalance by leveraging a novel clustering-based approach.

2. The introduction of a new clustering metric specific to federated learning provides a valuable tool for assessing clustering quality in class-imbalanced environments.

### Weaknesses
1. The clustering methodology relies on empirical losses, which may not fully capture data distribution nuances across diverse client datasets, potentially leading to suboptimal clustering in more complex scenarios. Specifically, using only the final loss value after training might obscure the dynamic behavior of the loss function during training, which could be a more informative feature for clustering. The method does not account for the variance in loss values across different epochs or mini-batches, potentially leading to misclassification of clients with similar data distributions but different training dynamics.

2. The computational cost of clustering based on interaction matrices and Gaussian weighting could limit scalability, especially in large federations with numerous clients and communication rounds. While the authors mention that the clustering is done on the server, the construction and manipulation of the interaction matrix, which grows quadratically with the number of clients, could become a bottleneck. The Gaussian weighting, while effective, also adds computational overhead, particularly when the number of clients is large and the matrix becomes dense. The paper lacks a detailed analysis of the time complexity of these operations in relation to the number of clients and communication rounds.

3. The method's convergence properties, though theoretically addressed, lack extensive empirical validation in highly non-IID settings, making its performance in real-world FL scenarios uncertain. Although the authors provide some theoretical justification, the empirical validation is limited to a few datasets and scenarios. There is a need for more extensive experiments on diverse datasets with varying degrees of non-IIDness, including real-world datasets with complex data distributions and class imbalances. The paper should also explore the sensitivity of the method to different hyperparameter settings in highly non-IID scenarios.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a federated learning clustering strategy based on loss function similarity and introduces a clustering metric based on Wasserstein distance. The paper provides a theoretical proof of the algorithm’s convergence and demonstrates its performance in various imbalanced scenarios.

### Strengths
1. This work uses the similarity of loss functions as the basis for clustering and provides a theoretical proof of the convergence of the optimization algorithm using Gaussian weights.

2. The proposed method, FedGWC, is orthogonal to other aggregation methods.

3. The algorithm’s performance is examined under imbalanced scenarios.

### Weaknesses
1. The study lacks recent federated learning clustering baselines. The three comparison methods are [CFL, 2020], [FeSEM, 2023], and [IFCA, 2020]. Moreover, the proposed FedGWC performs weaker than other methods on CIFAR-10 and FEMNIST datasets and is similar to FeSEM on CIFAR-100. Overall, it does not achieve superior performance.

2. The comparative experiments in Table 3 are unfair, as FeSEM is selected across all three datasets. Instead, the best baseline should be selected for each dataset: IFCA for CIFAR-10, FeSEM for CIFAR-100, and IFCA for FEMNIST.

3. The experiments in Table 5 are not convincing. Other baseline methods’ Rand Index scores should be added.

4. The design of Tables 2 and 3 could be optimized, as they are somewhat confusing.

### Questions
1. This work is inspired by (Cho et al., 2022) to capture the similarity in client data distributions through a transformation of the loss function. Please further explain why measuring loss function distance can “effectively identify clusters of clients with similar levels of heterogeneity and class distribution.”

2. What is the significance of the evaluation metric introduced based on the Wasserstein distance, and is there any further improvement to FedGWC based on this metric?

### Soundness
3

### Presentation
2

### Contribution
2
