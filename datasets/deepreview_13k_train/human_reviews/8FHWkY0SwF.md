# Learning Personalized Causally Invariant Representations for Heterogeneous Federated Clients

- Decision: Accept
- Scores: 6, 6, 3

## Abstract
Personalized federated learning (PFL) has gained great success in tackling the scenarios where target datasets are heterogeneous across the local clients. However, the application of the existing PFL methods to real-world setting is hindered by the common assumption that the test data on each client is in-distribution (IND) with respect to its training data. Due to the bias of training dataset, the modern machine learning model prefers to rely on shortcut which can perform well on the training data but fail to generalize to the unseen test data that is out-of-distribution (OOD). This pervasive phenomenon is called shortcut learning and has attracted plentiful efforts in centralized situations. In PFL, the limited data diversity on federated clients makes mitigating shortcut and meanwhile preserving personalization knowledge rather difficult. In this paper, we analyse this challenging problem by formulating the structural causal models (SCMs) for heterogeneous federated clients. From the proposed SCMs, we derive two significant causal signatures which inspire a provable shortcut discovery and removal method under federated learning, namely FedSDR. Specifically, FedSDR is divided into two steps: 1) utilizing the available training data distributed among local clients to discover all the shortcut features in a collaborative manner. 2) developing the optimal personalized causally invariant predictor for each client by eliminating the discovered shortcut features. We provide theoretical analysis to prove that our method can draw complete shortcut features and produce the optimal personalized invariant predictor that can generalize to unseen OOD data on each client. The experimental results on diverse datasets validate the superiority of FedSDR over the state-of-the-art PFL methods on OOD generalization performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on addressing the "shortcut trap" issue within personalized federated learning (pFL) by introducing FedSDR. This solution aims to identify and eliminate shortcut features, leading to enhanced performance for individual clients within pFL on their respective local datasets. The authors support their approach with theoretical proofs and comprehensive experiments, demonstrating the effectiveness of FedSDR across multiple scenarios.

### Strengths
1. Originality: The paper pioneers the exploration of the shortcut trap problem in pFL.

2. Solid Theoretical Support: The inclusion of strong theoretical foundations.

3. Sufficient Experiments: The comprehensive set of experiments strengthens the paper's contributions.

### Weaknesses
1. Notation Conciseness: The notation could be more concise, potentially enhancing the paper's readability.

2. Confusing Training Process: A section of the training process appears confusing and requires clarification. Specifically, the interaction between the shortcut feature identification and the local model update is not entirely clear. It's difficult to discern how the identified shortcut features are explicitly removed or mitigated during the local training phase. The description lacks the necessary detail to understand the exact mechanism.

3. Inconclusive Experimental Results: Certain aspects of the experimental outcomes lack conviction and need further clarification for robustness. The significantly lower worst-case accuracies observed for some baseline methods on CMNIST and CFMNIST are concerning and require a more thorough analysis. It's not clear why these methods perform so poorly in these specific scenarios, which casts doubt on the overall validity of the comparisons.

### Questions
1. The paper’s algorithmic approach (Algorithm 1) deviates from the conventional practice of client selection in Federated Learning (FL). Could the authors elucidate why they've chosen this approach over the typical FL client selection methodology?

2. Concerns arise from certain experimental results in Table 1, particularly the unexpected lower accuracies observed for specific baseline methods on CMNIST and CFMNIST. Can the authors provide an explanation to address these concerns?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new personalized federated learning approach named FedSDR. Considering generalization on unseen test data, the paper utilizes invariant learning in the federated setting. Specifically, FedSDR first extracts shortcut features that are irrelevant to the task and them remove it to extract the most informative personalized invariant features by carefully designing the objectives. Experiments show that FedSDR outperforms the other baselines in the settings where the test data distribution shifts.

### Strengths
1. Applying invariant learning in the federated setting is interesting and promising.

2. The organization of the paper is clear.

3. FedSDR significantly outperforms the other baselines.

### Weaknesses
1. My main concern is about the experimental setting. Experiments are based on the simulated setting where the authors manually add shortcut features and change the test data distributions. Based on the motivation, the shortcut features should naturally exist in datasets. Experiments on real-world natural datasets are necessary. Otherwise, the application of FedSDR may be very limited. The current experiments do not adequately demonstrate the practical relevance of the proposed method, as the manually injected shortcut features might not accurately reflect the complexities of real-world biases or spurious correlations. This raises concerns about the generalizability of the findings to actual federated learning scenarios.

2. The theoretical analysis has strong assumptions, e.g., logistic regression, linear function, etc. The analysis may not be applicable in the experimental settings. The theoretical guarantees are derived under very restrictive assumptions, such as linear models and logistic regression, which are not representative of the complex non-linear models used in the experiments, such as ResNet. This discrepancy between the theoretical framework and the experimental setup undermines the theoretical claims. The lack of theoretical support for the non-linear models used in the experiments makes it difficult to understand the behavior of the proposed method in more realistic scenarios.

3. The number of clients used in the experiments is missing. Experiments to evaluate the scalability of FedSDR are not provided. The absence of experiments with a varying number of clients makes it difficult to assess the scalability of the proposed method. It is unclear how the performance of FedSDR would be affected by an increase in the number of clients, which is a critical factor in federated learning. Without such experiments, the practical applicability of FedSDR in large-scale federated learning systems remains uncertain.

4. Typos: 1. Page 4: “Theorem 1” -> “Lemma 1”; 2. Page 6: “guarantee” -> “guarantees”

### Questions
1. Can you add a synthetic dataset with a simple model in the experiments? It can be used to verify the theorems by satisfying the assumptions.

2. Can you add experiments without manually adding shortcut features? It is quite important. Currently, I’m not clear what are the real applications of FedSDR.

3. Can you add experiments that increase the number of clients and adopt client sampling?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel approach to mitigating shortcut learning in personalized federated learning, which is a challenging problem in real-world settings. The proposed method, FedSDR, utilizes structural causal models to discover and remove shortcuts while preserving personalization knowledge.

### Strengths
1. This paper provides extensive background information, offering readers significant convenience in understanding the topic.

2. The authors conducted extensive experiments on some real-world datasets, validating the excellent performance of the proposed method.

### Weaknesses
1. I believe the main issue with this paper is that the research motivation seems weak. The paper claims to primarily address the scenario where training sets are Non-IID among clients, and where within each client, the training and test sets are also Non-IID. However, I think existing Robust Federated Learning and Federated Domain Generalization methods are capable of handling the aforementioned scenario. Although these two methods primarily focus on the issue of Non-IID training and test sets within each client.

2. The paper states, "To the best of our knowledge, we are the first to consider the shortcut trap problem in personalized federated learning and analyze it by formulating the structural causal models for heterogeneous clients." While it's true that this paper is indeed the first to study the use of PFL+SCM to address the shortcut trap problem, existing Robust Federated Learning and Federated Domain Generalization methods can also address the shortcut trap problem. Therefore, the contribution of this paper appears to be limited.

3. In Figure 1, I find the classification of the scenarios where RFL&FedDG are applicable not very accurate. In the scenarios where RFL&FedDG are applicable, the Test-test relation can also be IID or Non-IID.

4. In the experimental section, the proposed model is only compared to FL and PFL methods. However, I believe it should also be compared to RFL and FedDG methods to provide more convincing experimental results.

5. The experimental section lacks detailed information about the configuration of the model used in this paper. More detailed information is needed.

6. The paper lacks a thorough discussion of the limitations of the proposed FedSDR method. While the authors mention some potential limitations in passing, a more detailed discussion of the assumptions and constraints of the method would be helpful for readers to better understand its applicability in different scenarios.

7. Although the authors provide some high-level explanations of how FedSDR works, a more detailed discussion of the causal modeling framework and how it is used to address shortcut learning would be helpful for readers who are not familiar with this area of research.

### Questions
Please see above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
