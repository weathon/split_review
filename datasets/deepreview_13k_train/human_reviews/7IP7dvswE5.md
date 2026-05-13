# Rare-Mark-Aware Next Event Prediction In Marked Event Streams

- Decision: Reject
- Scores: 3, 6, 5, 8

## Abstract
In marked event streams, Marked Temporal Point Process (MTPP) is central to predicting when and what mark the next event will occur based on the history. In various real-world applications, the mark distribution is significantly imbalanced, i.e., some marks are frequent, and others are rare. We unveil that such imbalance can cause the rare mark missing issue when predicting the next event – frequent marks are dominant, and rare marks often have no chance. However, rare marks can be essential in some applications (e.g., the occurrence of a 7-magnitude earthquake), and missing such rare marks in the next event prediction is risky. To address this issue, we tackle a novel Rare-mark-aware Next Event Prediction problem (RM-NEP), answering two questions for each mark m: “what is the probability that the mark of the next event is m?, and if m, when will the next event happen?”. Solving RM-NEP gives rare marks equal opportunity as frequent marks in the next event prediction. This guarantees that rare marks are always included in the predicted results. Moreover, RM-NEP allows arbitrary number of rare marks samples for time prediction without interference from frequent marks, ensuring the time prediction is accurate. To solve RM-NEP effectively, we first unify the improper integration of two different functions into one and then develop a novel Integral-free Neural Marked Temporal Point Process (IFNMTPP) to approximate the target integral directly. Extensive experiments on real-world and synthetic datasets demonstrate the superior performance of our solution for RM-NEP against various baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper solves a problem in marked event prediction when the distribution of marks is significantly imbalanced i.e., some marks are frequent, and others are rare. The paper introduces a problem namely Rare-mark-aware Next Event Prediction (RM-NEP) and solves the problem to answer two questions: “what is the probability that the mark of the next event is m? and if m, when will the next event happen?”. Solving RM-NEP gives rare marks equal opportunity as frequent marks in the next event prediction. This guarantees that rare marks are always included in the predicted results. To solve RM-NEP effectively, the authors first unify the improper integration of two different functions into one and then develop a novel Integral-free Neural Marked Temporal Point Process (IFNMTPP) to approximate the target integral directly.

### Strengths
1.	The problem is interesting.
2.	The Figures are intuitive.

### Weaknesses
1.  The main difference between the problem of the paper and the existing problem is not clear. For example, what are the differences between RM-NEP and rare event forecasting? It is unclear if the existing rare event forecasting techniques, such as oversampling or undersampling, could be directly applied to the next event prediction (NEP) problem within the context of Marked Temporal Point Processes (MTPP). The paper does not adequately explore this connection, making it difficult to assess the novelty of the proposed RM-NEP.
2.  The motivation of RM-NEP is not convincing. (i) If a mark is rare (i.e., it occurs very few times in the history). Then, it can be dominated by frequent marks in the prediction. This phenomenon is completely normal.  (ii) If a mark is rare and important compared to other marks, why don’t we only consider that mark as a single variable so that there is no imbalance anymore? The paper does not sufficiently justify why a new problem formulation is necessary instead of adapting existing methods or focusing on individual rare marks.
3.  The paper is not self-contained. For example, how the existing studies solve NEP is not clear. The authors only list a large number of papers in the Related Work section. Similarly, how the existing studies model MTPP is not clear. The authors only list a large number of papers in the Introduction section. A summarization and comparison are needed to provide a better understanding. The paper lacks a clear explanation of how existing methods handle the integration of intensity functions and how they are used for prediction, making it difficult to understand the specific challenges the proposed method addresses.
4.  Some words are hard to understand. For example, RMTPP is not defined. The paper uses the term RMTPP without a clear definition, leaving the reader to guess its meaning and relevance to the proposed method. This lack of clarity hinders the understanding of the paper's contribution.
5.  Some notations are not defined. For example, what is $\tau$? The paper uses the notation $\tau$ within the integral without explicitly defining its meaning or role, which is crucial for understanding the mathematical formulation of the proposed method.
6.  Intuitively, can we solve the problem by undersampling dominating marks? The paper does not discuss the possibility of using undersampling techniques as a baseline, which could be a simpler alternative to the proposed method. This omission makes it difficult to evaluate the necessity of the proposed approach.
7.  I cannot understand lines 297-299. If t=t_l then the integration equals 0. The explanation of $\Gamma^*(m, t)$ and its relationship to Equation (3) is unclear. Specifically, it's not clear why setting $t = t_l$ would solve Equation (3) if the integral evaluates to zero at that point.
8.  The main idea of using integral-free comes from FullyNN by using IEM. Basically, the authors adapt it to marked events, which is straightforward. The paper does not adequately address the differences between the integration problems solved by FullyNN and the proposed IFNMTPP. The adaptation to marked events is not as straightforward as presented, and the paper lacks a detailed explanation of the necessary modifications.
9.  The authors do not prove why using IEM can achieve the integral-free solution. The paper lacks a rigorous explanation of how the Integral Estimator Module (IEM) achieves an integral-free solution. It is not clear how the non-negative weights and monotonic-increasing activation functions of IEM directly lead to the desired integral approximation.
10. There is no ablation study. For example, what is the performance of TFNMTPP with different imbance ratios? The paper does not include an ablation study to evaluate the performance of the proposed method under different imbalance ratios. This lack of analysis makes it difficult to assess the robustness of the method.

### Questions
1.	If a mark is rare and important compared to other marks, why don’t we only consider that mark as a single variable such that there is no imbalancing anymore.
2.	What is the performance of TFNMTPP with different imbance ratios.
3.	Intuitively, can we solve the problem by undersampling dominating marks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper makes a substantial contribution to the field of MTPPs by addressing the rare mark missing issue and providing a computationally efficient solution through IFNMTPP. The work is theoretically robust, empirically validated, and has practical significance in domains where rare events play a critical role.

### Strengths
1.The paper provides a thorough theoretical foundation for the RM-NEP problem, including detailed derivations of the probability distributions and the integral-free approximation.

2.This paper proposes a novel approach, IFNMTPP, which avoids the computational burden of traditional numerical integration methods (e.g., Monte Carlo integration) by directly approximating the integral using a neural network. This is a computationally efficient solution that enables the model to handle large-scale datasets.

3.The authors conduct extensive experiments on various datasets, showing that their approach consistently outperforms existing baselines. The empirical results are strong and demonstrate the practical utility of the proposed method.

### Weaknesses
W1: If I understand correctly, RM-NEP assumes that rare marks can be predicted accurately by decoupling time and mark prediction. Does this assumption hold across different types of datasets, especially when the marks exhibit temporal correlations?

W2: The IFNMTPP model approximates improper integrals using a "monotonically decreasing neural network." However, the paper does not provide sufficient details about how this approximation is performed, nor does it explain the intuition behind why a monotonically decreasing function is appropriate.

### Questions
Q1: How interpretable are the results of RM-NEP, particularly for rare marks? Does the neural network-based approximation provide any insight into why a rare mark might be predicted? 

Q2: The paper focuses on marked temporal point processes where marks are categorical. How well does the proposed method generalize to cases where the marks are continuous.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates how to reduce the problem of rare mark missing when event prediction is imbalanced, thereby reducing the risk of missing key events. The paper provides a detailed description of the proposed IFNMTPP method and conducts comparative experiments on multiple datasets. Results show the performance of IFNMTPP.

### Strengths
S1: The paper studies the RM-NEP problem, unifies abnormal integrals, and proposes IFNMTPP to ensure that the prediction results of rare marks are not missed when the marks are imbalanced.
S2. The paper is well-articulated, offering a clear explanation of the concepts and methodologies employed.
S3. Extensive experiments on real-world and synthetic datasets demonstrate the effectiveness of the proposed method.

### Weaknesses
W1. The purpose of this article is to improve the prediction accuracy of rare events. According to the experimental results of macro-F1 in Table 3, there is a slight improvement in the prediction accuracy of rare marks. In addition, earthquakes are unlikely to be accurately predicted through event prediction. Both the accuracy of frequent marks and rare marks before and after improvement are very low. Does this study have practical application value?
W2. Figure 2 is not very clear. It is recommended to refine it. The symbols inside are not consistent with the description in the text, such as v, s, and f.
W3. Incorrect punctuation is used in line 20 and line 78.

### Questions
Q1: BookOrder's mark type [1] account for over 40%. Does this meet the definition of the rare mark?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on utilizing Marked Temporal Point Process (MTPP) models to address the Next-event Prediction (NEP) problem. It highlights a primary challenge of NEP: the imbalanced distribution of mark types. To address this, the paper introduces a new problem, Rare-mark-aware Next Event Prediction (RM-NEP), which is designed to ensure that rare marks consistently appear in prediction results. The paper also presents a novel IFNMTPP model to resolve issues related to inadequate integration over infinite time intervals when estimating the probability of marks and their timing in RM-NEP.

### Strengths
1. The proposed RM-NEP problem offers fresh insights into the NEP challenge and the field of MTPP, presenting a potentially effective solution for addressing the issue of imbalanced mark types.
2. The paper is well-written, with a clear and fluent presentation of the NEP problem, its challenges, and the proposed solution.
3. The IFNMTPP model is straightforward in its design, with empirical studies demonstrating its superior efficiency.

### Weaknesses
1. Although the primary focus of the paper is on accurately predicting rare mark types, Table 3 suggests that IFNMTPP does not show significant superiority in mark prediction performance. Instead, its strengths appear more pronounced in time prediction and efficiency. The paper could benefit from more detailed experimental analysis regarding the accuracy of predicting rare mark types. Specifically, the evaluation could include metrics that are more sensitive to the performance on rare marks, such as precision, recall, and F1-score calculated specifically for the rare marks, rather than just the macro-averaged F1 score across all marks. This would provide a clearer picture of the model's ability to address the rare mark prediction problem.
2. The illustration depicting the architecture of IFNMTPP could be refined to provide a clearer demonstration of its design. For example, the diagram could explicitly show how the integral-free formulation is implemented within the model architecture, and how the different components interact to produce the final predictions. More detailed annotations and a clearer flow of information would be beneficial.

### Questions
1. (Related to W1) Could the authors elaborate on how their experimental results empirically demonstrate the effectiveness of the proposed RM-NEP problem and IFNMTPP model in addressing the issue of missing rare marks in NEP?

### Soundness
3

### Presentation
4

### Contribution
4
