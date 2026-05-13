# Federated Virtual Learning on Heterogeneous Data with Local-global Distillation

- Decision: Reject
- Scores: 5, 6

## Abstract
Despite Federated Learning (FL)'s trend for learning machine learning models in a distributed manner, it is susceptible to performance drops when training on heterogeneous data. In addition, FL inevitability faces the challenges of synchronization, efficiency, and privacy. Recently, dataset distillation has been explored in order to improve the efficiency and scalability of FL by creating a smaller, synthetic dataset that retains the performance of a model trained on the local private datasets.  \emph{We discover that using distilled local datasets can amplify the heterogeneity issue in FL.} To address this, we propose a new method, called \textbf{Fed}erated Virtual Learning on Heterogeneous Data with \textbf{L}ocal-\textbf{G}lobal \textbf{D}istillation (\ours{}), which trains FL using a smaller synthetic dataset (referred as \emph{virtual data}) created through a combination of local and global dataset distillation.
Specifically, to handle synchronization and class imbalance, we propose iterative distribution matching to allow clients to have the same amount of balanced \emph{local virtual data}; to harmonize the domain shifts, we use federated gradient matching to distill \emph{global virtual data} that are shared with clients without hindering data privacy to rectify heterogeneous local training via enforcing local-global feature similarity. We experiment on both benchmark and real-world datasets that contain heterogeneous data from different sources, and further scale up to an FL scenario that contains large number of clients with heterogeneous and class imbalance data. Our method outperforms \textit{state-of-the-art} heterogeneous FL algorithms under various settings with a very limited amount of distilled virtual data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a federated learning method called FedLGD that uses local and global dataset distillation to handle data heterogeneity.FedLGD uses an iterative distillation process to generate local and global virtual datasets that mitigate data heterogeneity and improve efficiency in federated learning. The local-global distillation and feature regularization are key components that help FedLGD achieve strong performance.

### Strengths
1. The discover of using dataset distillation can amplify the statistical distances is interesting.
  2. Achieves state-of-the-art results on benchmark datasets with domain shifts, outperforming existing federated learning algorithms.

### Weaknesses
1. t-SNE figures are not represented as vectors.

2. Sharing gradients from clients to the server for a global virtual data update may pose security risks. Some attacks could potentially reconstruct raw data using gradient information, similar to the risks associated with Deep Gradient Leakage. Why sharing averaged gradients is safe?

3. What is the rationale behind clients requiring local virtual data instead of training directly on their local private data?

4. Could you clarify why this method has not been compared to other FL methods utilizing dataset distillation?

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
1.	This paper proposes a federated virtual learning approach that leverages local and global dataset distillation techniques to simultaneously tackle the challenge of data heterogeneity as well as efficient training in federated learning. The authors claim that dataset distillation can exacerbate the heterogeneity among clients’ local data and propose to alleviate this issue with distribution matching.
2.	The problem addressed in this paper is novel and interesting. The adverse effect of dataset distillation in a federated learning setting is insightful. The proposed approach seems feasible and promising.
3.	In your paper, the model on clients is split into feature extractors and classification heads. This split learning-like paradigm has been widely adopted by a series of prior works [1,2,3]. Please explain the deplorability of your approach on existing methods. More elaboration on how your proposed method relates to these works would be appreciated.
4.	If I understand you correctly, FedProx is proposed by [4] rather than [5]. Do I misunderstand something?
5.	Some of the benchmark algorithms, such as FedProx [4], Scaffold [6], are somewhat outdated. In your experiments, you have used different open-sourced datasets as private data for clients, and this degree of data heterogeneity is apparently unfavorable for the regularization-based methods mentioned above. Would it be possible to compare your approach with some novel federated learning methods based on GANs [7], which seem to be more suitable for your scenario?

[1]  "FedICT: Federated Multi-task Distillation for Multi-access Edge Computing." IEEE Transactions on Parallel and Distributed Systems (2023).

[2] "Group knowledge transfer: Federated learning of large cnns at the edge." Advances in Neural Information Processing Systems 33 (2020): 14068-14080.

[3] "Exploring the distributed knowledge congruence in proxy-data-free federated distillation." arXiv preprint arXiv:2204.07028 (2022).

[4] "Federated optimization in heterogeneous networks." Proceedings of Machine learning and systems 2 (2020): 429-450.

[5] "On the convergence of fedavg on non-iid data." arXiv preprint arXiv:1907.02189 (2019).

[6] "Scaffold: Stochastic controlled averaging for federated learning." International conference on machine learning. PMLR, 2020.

[7] "Data-free knowledge distillation for heterogeneous federated learning." International conference on machine learning. PMLR, 2021.

### Strengths
The problem addressed in this paper is novel and interesting. The adverse effect of dataset distillation in a federated learning setting is insightful. The proposed approach seems feasible and promising.

### Weaknesses
1.In your paper, the model on clients is split into feature extractors and classification heads. This split learning-like paradigm has been widely adopted by a series of prior works [1,2,3]. Please explain the deplorability of your approach on existing methods. More elaboration on how your proposed method relates to these works would be appreciated.

2.If I understand you correctly, FedProx is proposed by [4] rather than [5]. Do I misunderstand something?

3.Some of the benchmark algorithms, such as FedProx [4], Scaffold [6], are somewhat outdated. In your experiments, you have used different open-sourced datasets as private data for clients, and this degree of data heterogeneity is apparently unfavorable for the regularization-based methods mentioned above. Would it be possible to compare your approach with some novel federated learning methods based on GANs [7], which seem to be more suitable for your scenario?

[1]  "FedICT: Federated Multi-task Distillation for Multi-access Edge Computing." IEEE Transactions on Parallel and Distributed Systems (2023).

[2] "Group knowledge transfer: Federated learning of large cnns at the edge." Advances in Neural Information Processing Systems 33 (2020): 14068-14080.

[3] "Exploring the distributed knowledge congruence in proxy-data-free federated distillation." arXiv preprint arXiv:2204.07028 (2022).

[4] "Federated optimization in heterogeneous networks." Proceedings of Machine learning and systems 2 (2020): 429-450.

[5] "On the convergence of fedavg on non-iid data." arXiv preprint arXiv:1907.02189 (2019).

[6] "Scaffold: Stochastic controlled averaging for federated learning." International conference on machine learning. PMLR, 2020.

[7] "Data-free knowledge distillation for heterogeneous federated learning." International conference on machine learning. PMLR, 2021.

### Questions
1.In your paper, the model on clients is split into feature extractors and classification heads. This split learning-like paradigm has been widely adopted by a series of prior works [1,2,3]. Please explain the deplorability of your approach on existing methods. More elaboration on how your proposed method relates to these works would be appreciated.

2.If I understand you correctly, FedProx is proposed by [4] rather than [5]. Do I misunderstand something?

3.Some of the benchmark algorithms, such as FedProx [4], Scaffold [6], are somewhat outdated. In your experiments, you have used different open-sourced datasets as private data for clients, and this degree of data heterogeneity is apparently unfavorable for the regularization-based methods mentioned above. Would it be possible to compare your approach with some novel federated learning methods based on GANs [7], which seem to be more suitable for your scenario?

[1]  "FedICT: Federated Multi-task Distillation for Multi-access Edge Computing." IEEE Transactions on Parallel and Distributed Systems (2023).

[2] "Group knowledge transfer: Federated learning of large cnns at the edge." Advances in Neural Information Processing Systems 33 (2020): 14068-14080.

[3] "Exploring the distributed knowledge congruence in proxy-data-free federated distillation." arXiv preprint arXiv:2204.07028 (2022).

[4] "Federated optimization in heterogeneous networks." Proceedings of Machine learning and systems 2 (2020): 429-450.

[5] "On the convergence of fedavg on non-iid data." arXiv preprint arXiv:1907.02189 (2019).

[6] "Scaffold: Stochastic controlled averaging for federated learning." International conference on machine learning. PMLR, 2020.

[7] "Data-free knowledge distillation for heterogeneous federated learning." International conference on machine learning. PMLR, 2021.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
