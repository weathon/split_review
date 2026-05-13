# Generalization Performance Gap Analysis between Centralized and Federated Learning: How to Bridge this Gap?

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
The rising interest in decentralized data and privacy protection has led to the emergence of Federated Learning. Many studies have compared federated training with classical training approaches using centralized data and found from experiments that models trained in a federated setup with equal resources perform poorly on tasks. However, these studies have generally been empirical and have not explored the performance gap further from a theoretical perspective. The lack of theoretical understanding prevents figuring out whether federated algorithms are necessarily inferior to centralized algorithms in performance and how large this gap is according to the training settings. Also, it hinders identifying valid ways to close this performance distance. This paper fills this theoretical gap by formulating federated training as an SGD (Stochastic Gradient Descent) optimization problem over decentralized data and defining the performance gap within the PAC-Bayes (Probably Approximately Correct Bayesian) framework. Through theoretical analysis, we derive non-vacuous bounds on this performance gap, revealing that the difference in generalization performance necessarily exists when training resources are equal for both training setups and that variations in the training parameters affect the gap. Moreover, we also prove that the complete elimination of the performance gap is only possible by introducing new clients or adding new data to existing clients. Advantages in other training resources are not feasible for closing the gap, such as giving larger models or more communication rounds to federated scenarios. Our theoretical findings are validated by extensive experimental results from different model architectures and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the generalization performance of federated learning (FL) under local SGD updates, aiming at understanding why the generalization of federated learning is worse than that of centralized learning observed by empirical results. The authors provide theoretical results to show that the generalization performance gap between federated learning and its centralized counterpart given the same training resources is unavoidable. Based on their theory, the authors further claim that the performance gap can be possibly eliminated when introducing new clients or adding data to existing clients.

### Strengths
Both generalization bounds for FedAvg and centralized minibatch SGD are provided. Then based on derived generalization bounds for two scenarios, the analytic expression of the performance gap is derived, which shows that such gap is unavoidable under the same training resources. Two strategies, including introducing a new client or adding more data to existing clients, are provided to bridge the performance gap, which are supported by theoretical justifications.

### Weaknesses
1. The main weakness of the paper lies in Theorem 3. Actually, the metric of defined performance gap (i.e., $G_{Fed} - G_{Cen}$) seems unreasonable. Firstly, these are only upper bounds of the true generalization gaps, which are probably too conservative to reflect true generalization performances of two scenarios. Secondly, even the generalization gap (i.e., $R(Q) - \hat{R}(Q)$) is not a good metric to study the performance gap. Note that such generalization gap measures the difference between test loss and training loss. It is practically possible that the test losses for both cases are comparable while the training losses remain a large gap, especially when the training rounds of two cases are not equal (i.e., in the paper the rounds for FL is $n$ times less than centralized case). A more reasonable metric to quantify the performance gap should be $R(Q_{Fed}) - R(Q_{Cen})$.

2. In Theorem 3, the bounds does not reflect the dependence on the number of local updates (i.e., $t$). Recall that when $t=1$, FedAvg is exactly minibatch SGD, which thus should have the same generalization performance. However, the provided bounds does not capture this fact.

3. The assumptions are quite strong, especially Assumptions 2 and 3. These assumptions are hard to satisfy for modern neural networks.

4. In experiments, the learning rates for FL and centralized learning are set identical, which might not be reasonable. Note that for FL the learning rate is usually scaled inversely w.r.t. number of local updates $t$. Then for the i.i.d. case, the "effective" updates of FedAvg is actually $t T/ n$, compared with minibatch SGD. Then with identical learning rates, FL may suffer from worse generalization as shown in (Hardt et al., 2016). Moreover, non-i.i.d. case for FL is not considered.

### Questions
1. Could the authors explain why the difference of generalization upper bounds is a good and reasonable metric to evaluate the performance gap? As in Weakness 1, why not use the difference between test losses?

2. Why do not the bounds in Theorem 3 vanish when $t=1$, as in this case FedAvg and minibatch SGD are the same?

3. What the experimental results of the non-i.i.d. case for FL? How does it compare to the centralized setting? Why are the learning rates for both settings set to be the same?

4. The assumptions are too restrictive. Could them be released, e.g., convex but not quadratic or even non-convex losses?

5. In Section 5.2.2, are the total numbers of data points in both settings the same?

6. In the proof, it seems that SGD is treated as its continuous limit. However, there is some difference between the analyses in continuous and discrete settings. Do the theoretical conclusions still hold in the discrete case? Why not directly analyze SGD?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a theoretical understanding of the generalization gap between centralized and federated learning within the PAC-Bayes framework and reveals how to eliminate the performance gap. They also find that advantages in other training resources are not feasible for closing the gap, such as giving larger models or more communication rounds for FL. The empirical results prove the theoretical analysis with different model architectures and datasets.

### Strengths
1. This is the first study to understand the generalization performance gap between centralized and federated learning.
2. The paper is well-organized and easy to read.
3. The experiments can prove the theoretical results.

### Weaknesses
1. I wonder what are the technical contributions of this paper. It seems that the proposed analysis may appear to be an extension of PAC-Bayes generalization gap to centralized and FL scenarios. It is essential for the authors to underscore their technical contributions in a more prominent manner.
2. Is the analysis for FL based on federated SGD with only one local update (t=1)? Or is the generalization performance gap in this analysis related to the number of local updates?

### Questions
See the weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper primarily investigates the generalization performance gap between centralized and federated learning (FedAvg) algorithms. Previous empirical evidence suggests that the generalization performance in a federated setting is inferior to that in a centralized setting. Based on the Probably Approximately Correct (PAC) framework, this study derives the generalization performance for both centralized and federated paradigms, measures the performance disparity between them, and proposes several methods to bridge this gap, supported by theoretical deductions and validated through experimental evidence.

### Strengths
- The theory is solid: This paper introduces the PAC (Probably Approximately Correct) framework and, under certain assumptions, derives the generalization bounds for both centralized and federated settings.
- The conclusions hold significant implications: The results derived from theoretical deductions offer guidance for the practical deployment of Federated Learning (FL) algorithms.

### Weaknesses
1. Eq.(7) seems not to capture the situation where a client performs multiple rounds of local updates, such as $K$ rounds, because, in the FedAvg algorithm, clients typically need to update their models locally $K$ times.
2. Assumption 2 appears to be a strong assumption, especially \( F(0) = 0 \), which is often not satisfied in practice. Can some experimental validation be provided?
3. The main focus of this paper is theoretical exploration. The conclusions drawn are generally trivial and do not offer any methodological innovations. What, then, is the technical contribution of this paper?

### Questions
please see the weakness.

### Soundness
3

### Presentation
3

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
This paper theoretically analyzes the generalization performance gap between federated learning and centralized training. It also proves that the complete elimination of the performance gap is only possible by introducing new clients or addind new data.

### Strengths
1) This work formulates the generalization performance of federated learning and centralized learning and gives a detailed illustration for the generalization bound.

2) This work proposes a method to close the generalization gap between two learning systems by introducing new clients or new data.

### Weaknesses
1) Some related works are missing, e.g., [1] [2] [3]

[1] What Do We Mean by Generalization in Federated Learning? arxiv: 2110.14216, Neurips workshop

[2] Understanding Generalization of Federated Learning via Stability: Heterogeneity Matters AISTATS 2024

[3] Towards Understanding Generalization and Stability Gaps between Centralized and Decentralized Federated Learning arxiv: 2310.03461

2) Strong assumption: The loss function is assumed to be convex and 2-order differentiable, which limits the contributions of the theoretical findings.

3) The method to close the generalization gap seems be to less practical in real-world applications. By introducing new clients or new data, the training data may own different distribution and change the training goal. In this case, it is hard to compare this dynamic system with centralized one.

### Questions
1) In Theorem 3, are the lower bound and upper bound necessarily positive?

2) In Line 422, by introducing new clients or new data, will the number of data size mn be increased to be larger than D?

3) In Figure 1, when changing the number of clients, does the total data size on all clients also change? If not, we may not get the conclusion in Section 5.2.1.

### Soundness
2

### Presentation
3

### Contribution
2
