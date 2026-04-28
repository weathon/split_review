# Kick Bad Guys Out! Zero-Knowledge-Proof-Based Anomaly Detection in Federated Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
Federated learning (FL) systems are vulnerable to malicious clients that submit poisoned local models to achieve their adversarial goals, such as preventing the convergence of the global model or inducing the global model to misclassify some data. Many existing defense mechanisms are impractical in real-world FL systems, as they require prior knowledge of the number of malicious clients or rely on re-weighting or modifying submissions. This is because adversaries typically do not announce their intentions before attacking, and re-weighting might change aggregation results even in the absence of attacks. To address these challenges in real FL systems, this paper introduces a cutting-edge anomaly detection approach with the following features: i) Detecting the occurrence of attacks and performing defense operations only when attacks happen; ii) Upon the occurrence of an attack, further detecting the malicious client models and eliminating them without harming the benign ones; iii) Ensuring honest execution of defense mechanisms at the server by leveraging a zero-knowledge proof mechanism. We validate the superior performance of the proposed approach with extensive experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an anomaly detection approach for Federated Learning. Their method eliminates the need for prior knowledge of the number of malicious clients and avoids reliance on re-weighting or modifying submissions. Experimental results demonstrate the efficacy of their approach.

### Strengths
1. The paper is well written and generally easy to follow.  
2. The method has been compared to a significant amount of related research.
3. A well-structured and clear presentation.

### Weaknesses
1.The explanations of some experimental results are not entirely convincing.
2.The description of the threat model needs to be more accurate.
   Specifically, the description lacks details regarding the adversary's capabilities, such as whether they can perform adaptive attacks or have knowledge of the global model's architecture. The current description also does not specify the level of control malicious clients have over their local training process, which is crucial for understanding the attack surface.


### Questions
1.	It is preferable to describe the threat model based on adversary goals, knowledge, and capabilities.
2.	The justification provided for selecting the 'second-to-the-last layer' in Exp1 is not sufficient.
3.	I didn't fully grasp the significance of "VERIFIABLE ANOMALY DETECTION USING ZKP," and the authors should emphasize the research objectives of this section more prominently.
4.	The paper is very well structured and. There are occasional grammar hiccups and typos, so I recommend a light editing pass (below are a few of the mistakes I’ve collected, but there are more).
Page 5 In this ppaer –>in this paper

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel anomaly detection approach for addressing the vulnerability of federated learning (FL) systems to malicious clients. It focuses on detecting and eliminating malicious client models without harming benign ones, using a zero-knowledge proof mechanism to ensure honest execution of defense mechanisms at the server.

### Strengths
The proposed approach detects attacks and performs defense operations only when attacks occur, and further identifies and removes malicious client models, therefore being harmless on benign ones.

### Weaknesses
1. The mechanism relies heavily on the assumption that malicious clients will remain below 50% of the total. However, its effectiveness may be limited if this assumption does not hold, as adversarial clients constituting over half the clients could possibly sabotage the defense. The authors did not sufficiently discuss limitations to the mechanism or potential strategies if this threshold is exceeded. Specifically, the paper lacks analysis on how the proposed defense behaves when the majority of clients are adversarial, potentially leading to a scenario where malicious updates are incorrectly deemed benign due to the skewed distribution of model parameters.

2. The proposed method relies on applying the **Three Sigma Rule** to identify outlier clients, but does not adequately justify the underlying assumption that client behavior will follow a **Gaussian/normal distribution**. Without evidence or validation that the models meet this statistical requirement, the correctness and reliability of using this rule is unclear. The authors need to provide empirical or theoretical support for why these distributions were expected in this context, otherwise the key thresholding technique lacks rigorous foundation. Furthermore, the paper does not address the potential impact of non-Gaussian distributions on the performance of the Three Sigma Rule, which could lead to either false positives (benign clients being flagged as malicious) or false negatives (malicious clients evading detection).

3. The paper claims to propose a new defensive mechanism, but its core algorithms - Krum, Three Sigma Rule and Zero-knowledge proofs - are already well-established in prior work. While integrating existing techniques can still yield new systems, the paper does not provide sufficient insight into how this combination offers meaningful advantage. Without novel algorithmic or analytical insights, the technical value of merely assembling known pieces is limited. To strengthen the paper, the authors should demonstrate deeper understanding of how this specific integration improves upon the state-of-the-art. The paper needs to articulate the specific challenges in federated learning that this particular combination of techniques addresses, and how it overcomes limitations of existing methods.

4. The evaluation of the proposed method's scalability and performance is limited by the small-scale datasets used (e.g. FEMNIST, CIFAR). While useful for proof-of-concept, these datasets do not adequately represent the data and computational heterogeneity of modern large-scale Federated Learning systems. To fully demonstrate the practicality and effectiveness of this defense, it will be important for the authors to test its performance and overhead when applied to real-world FL scenarios at a larger scale. Without such experimentation on industry-grade datasets and systems, the approach's scalability and real-world viability remain uncertain. The paper should also include an analysis of the computational and communication overhead introduced by the zero-knowledge proofs, especially in large-scale settings.

### Questions
Please refer to the Weaknesses section.

### Soundness
2 fair

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
The paper proposed a FL anomaly detection method with the following features: i) Detecting the occurrence of attacks and performing defense operations only when attacks happen; ii) Upon the occurrence of an attack, further detecting the malicious client models and eliminating them without harming the benign ones; iii) Ensuring honest execution of defense mechanisms at the server by leveraging a zero-knowledge-proof mechanism.

### Strengths
1. The authors proposed a new method for FL anomaly detection.

### Weaknesses
1. The authors did not compare with FL anomaly detection methods such as FLDetector in experiments.
2. The authors did not test their methods with some strong attacks such as [1], [2] , and [3].

[1] Gilad Baruch, Moran Baruch, and Yoav Goldberg. 2019. A Little Is Enough: Circumventing Defenses For Distributed Learning. In NeurIPS      
[2] Eugene Bagdasaryan, Andreas Veit, Yiqing Hua, Deborah Estrin, and Vitaly Shmatikov. 2020. How to backdoor federated learning. In AISTATS
[3] Chulin Xie, Keli Huang, Pin-Yu Chen, and Bo Li. 2019. Dba: Distributed backdoor attacks against federated learning. In ICLR

3. The authors did not explore the influence of the number of malicious clients.

### Questions
Please see the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
