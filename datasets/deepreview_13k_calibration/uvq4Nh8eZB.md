# Protecting Sensitive Data through Federated Co-Training

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
In many critical applications, sensitive data is inherently distributed. Federated learning trains a model collaboratively by aggregating the parameters of locally trained models. This avoids exposing sensitive local data. It is possible, though, to infer upon the sensitive data from the shared model parameters. At the same time, many types of machine learning models do not lend themselves to parameter aggregation, such as decision trees, or rule ensembles. It has been observed that in many applications, in particular healthcare, large unlabeled datasets are publicly available. They can be used to exchange information between clients by distributed distillation, i.e., co-regularizing local training via the discrepancy between the soft predictions of each local client on the unlabeled dataset. This, however, still discloses private information and restricts the types of models to those trainable via gradient-based methods. We propose to go one step further and use a form of federated co-training, where local hard labels on the public unlabeled datasets are shared and aggregated into a consensus label. This consensus label can be used for local training by any supervised machine learning model. We show that this federated co-training approach achieves a model quality comparable to both federated learning and distributed distillation on a set of benchmark datasets and real-world medical datasets. It improves privacy over both approaches, protecting against common membership inference attacks to the highest degree. Furthermore, we show that federated co-training can collaboratively train interpretable models, such as decision trees and rule ensembles, achieving a model quality comparable to centralized training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In order to achieve privacy under a federated learning setting, this paper proposes the use of a form of federated co-training called FEDCT, where local hard labels on the public unlabeled datasets are shared and aggregated into a consensus label. This consensus label is then used in training each local model. The paper analyzes the convergence of the proposed FEDCT and further develops a privacy version of FEDCT based on the XOR-Mechanism. The paper compares the proposed method with two baseline methods on several datasets for both iid and non-iid settings.

### Strengths
1. This paper considers the privacy issue in training machine learning models, which is a very important problem.

2. This paper employs the membership inference attack to practically demonstrate the model's ability to resist real-world attacks.

3. This paper conducts the convergence analysis for the proposed algorithm FEDCT.

### Weaknesses
1. This paper does not discuss the difference between the proposed method and PATE (Papernot et al., 2016). In PATE, each teacher model can be viewed as a local model, and a majority vote is also utilized to reach a consensus for learning from each other's knowledge. The key distinction is that PATE transfers this knowledge to a student model, while the method in this paper circulates the knowledge back to each teacher/local model. Without further discussion, it's challenging to ascertain whether the contribution of this paper is incremental when compared to PATE and DD (Bistritz et al., 2020). The paper should clarify how the iterative co-training approach of FEDCT provides a significant advantage over the single-step knowledge transfer in PATE, especially in terms of privacy and utility trade-offs. A more detailed analysis of the mechanisms and their implications is needed to justify the proposed method's novelty.

2. The experimental results are not promising. As depicted in Table 1, only in 1 out of 5 datasets does the proposed method outperform the baselines in terms of ACC, and on none of the datasets does the proposed method achieve the best privacy utility trade-off, that is the best ACC, while at the same time, having the best VUL compared to baselines. The paper needs to provide a more thorough analysis of why the proposed method does not consistently outperform baselines and under what conditions it is expected to perform well. The lack of a clear advantage in the privacy-utility trade-off raises concerns about the practical applicability of the proposed method.

3. This paper lacks clarity on the algorithm's scalability in relation to the number of clients, as it only reports the impact of client numbers on one dataset, and default settings of m (client numbers) for other datasets are only 5. The paper should include a more comprehensive evaluation of how the performance of FEDCT changes with varying numbers of clients across different datasets. The current analysis is insufficient to draw conclusions about the scalability of the proposed method, particularly in scenarios with a large number of participating clients.

### Questions
1. How does FEDCT compare with PATE in terms of the underlying mechanism design?
2. Besides differentially private distributed SGD (Xiao et al., 2022), are there any other related works that can be utilized as baselines for comparison with DP-FEDCT on the Privacy-Utility Trade-Off with Differential Privacy?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a federated learning framework namely FedCT to provide a privacy-preserving collaborative learning by sharing “hard labels” for unlabeled dataset. The authors theoretically demonstrate the convergence of FedCT. Besides, they propose an XOR-Mechanism to protect the privacy of sharing labels. Experiments on 7 datasets showcase the superiority of FedCT compared to some baselines.

### Strengths
S1. The proposed FedCT is technically sound. 

S2. This paper provides a sufficient theoretical analysis of convergence and privacy guarantees. 

S3. The writing is generally good and easy to understand.

### Weaknesses
W1. The contribution is trivial. There are a lot of federated learning frameworks, to name a few [1,2,3,4,5], based on sharing knowledge via a public unlabeled dataset. It seems that the only difference is that clients in FedCT upload “hard label” while other works’ clients share soft labels.

W2. The motivation is not clear. According to the basic idea of knowledge distillation, soft labels should potentially contain more useful information than hard labels. The authors are encouraged to clarify the reason for replacing soft labels with hard labels.

W3. More representative baselines are needed. As mentioned in W1, there are many similar works; it would be more convincing to conduct experiments to compare them.

W4. The appendix mentioned in the paper cannot be found; maybe it is just for me.

### Questions
See Weeknesses. Addressing these weaknesses (especially W1 and W2) will improve the convincing and quality of this paper.

### Soundness
3 good

### Presentation
3 good

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
The paper proposes an algorithm to protect the privacy of shared soft predictions on a public dataset used to achieve consensus in the server in semi-supervised learning. In particular, the server owns a unlabeled dataset and clients own private labeled datasets. Client utilizes local model to infer on the public dataset and compute the soft predictions on the unlabeled data, then sends those information to the server in a differentially private manner. The server aggregates those local knowledge into consensus and matigate the over-fitting in local trainings.

### Strengths
1. The paper attempts to solve an important problem: semi-supervised federated learning.
2. The paper provides theoretical guarantee of the privacy confidence.
3. utilizing a different differential privacy mechanism (XOR) instead of Gaussian mechanism, which is interesting.

### Weaknesses
1. The novelty is limited. There are many prior studies have explored semi-supervised federated learning [1-3] and knowledge distillation [4-6]. The paper does not propose a new framework of FedSSL but just naively combining differential privacy techniques. The paper does not illustrate the difference between FedCT and those previous work.
2. The motivation to protect the privacy of soft predictions is weak. Comparing to raw data/ features map, the soft predictions are not likely to leak privacy.
3. The paper is not well-organized and using non-standard terminology. For example, the term 'semi-honst' in section 4. Usually, we use 'honest-but-curious' to descrtibe the server which can not modify the local updates but trys to infer private information of clients. 
4. The baselines are not comprehensive. DP-FedAvg is using DP to the updated gradients but the proposed FedCT is using DP in the soft  predictions, it is not comparable. FedCT should compare other FedSSL methods [1-3] and conduct attach on the method to verify the effect of FedCT.
5. Setting for data heterogenity is not sufficient. With beta = 2 for non-i.i.d setting is not good. Most of papers set beta = 0.01 or 0.1 to create heterogeneous data partitions.

### Questions
1. What is the main difference between FedCT and the previous FedSSL methods?

2. what's the motivation to use XOR mechanism instead of Gasussian mechanism? What's the benefit?

3. I don't understand the last discussion of Interpretable Models? Why there is only FedCT and Centralized in the experimental results?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors use federated co-training, in which local hard labels on the public unlabeled datasets are shared and aggregated into a consensus label. Then, the server forms a consensus, while clients use this consensus as pseudo-labels for the unlabeled dataset in their local training. For data protection, the idea is to integrate XOR-mechanism for achieving differential privacy over binary data. At last, the authors provide empirical experiments over multiple datasets.

### Strengths
+ The authors conducted many experiments.

### Weaknesses
 + The idea seems to be just a combination of different modules.
+ The explicit motivation is unclear.
+ The writing logic should be improved.

+ The first half introduces some general and basic knowledge of federated learning, data privacy, applications, and co-training. The logic is not smooth. Several sentences have no much relation here. What is the explicit problem that you target here? What are the explicit problems of prior research?
+ The proposed idea seems to have better model quality and privacy. However, the ambiguious language makes me confused. What is the definition of privacy or quality?

+ The introduction mentions differential privacy, unlabeled datasets, and gradient-based methods? What are the problems of these research areas? Do the authors improve each of them?
+ The authors detailed what they have done. I feel confused that why the idea of combination (co-training, differential privacy, federated learning) is meaningful. What are your insights?

Section 3 combines the prior research and the new idea.
Section 4 starts with introduction of differential privacy.
Could the authors elaborate what is new here? What research line do you follow?

What is the explicit definition of privacy in this paper? For example, differential privacy has its definition. What is the exact meaning of improving privacy (improve differential privacy?) in your paper? Using some attacks to verify is not strong for claiming improved privacy. Actually, the response is still ambiguous from my view.

### Questions
What is the explicit motivation of this paper?
Why is this idea important?

### Abstract
- The first half introduces some general and basic knowledge of federated learning, data privacy, applications, and co-training. The logic is not smooth. Several sentences have no much relation here. What is the explicit problem that you target here? What are the explicit problems of prior research?
- The proposed idea seems to have better model quality and privacy. However, the ambiguious language makes me confused. What is the definition of privacy or quality?

### Introduction
- The introduction mentions differential privacy, unlabeled datasets, and gradient-based methods? What are the problems of these research areas? Do the authors improve each of them?
- The authors detailed what they have done. I feel confused that why the idea of combination (co-training, differential privacy, federated learning) is meaningful. What are your insights?

### Construction
Section 3 combines the prior research and the new idea.
Section 4 starts with introduction of differential privacy.
Could the authors elaborate what is new here? What research line do you follow?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
