# CHG Shapley: Efficient Data Valuation and Selection towards Trustworthy Machine Learning

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
Understanding the decision-making process of machine learning models is crucial for ensuring trustworthy machine learning. Data Shapley, a landmark study on data valuation, advances this understanding by assessing the contribution of each datum to model accuracy. However, the resource-intensive and time-consuming nature of multiple model retraining poses challenges for applying Data Shapley to large datasets. To address this, we propose the CHG (Conduct of Hardness and Gradient) score, which approximates the utility of each data subset on model accuracy during a single model training. By deriving the closed-form expression of the Shapley value for each data point under the CHG score utility function, we reduce the computational complexity to the equivalent of a single model retraining, an exponential improvement over existing methods. Additionally, we employ CHG Shapley for real-time data selection, demonstrating its effectiveness in identifying high-value and noisy data. CHG Shapley facilitates trustworthy model training through efficient data valuation, introducing a novel data-centric perspective on trustworthy machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a gradient-based method to reduce the computational cost of Data Shapley: the CHG (compound of Hardness and Gradient) utility function, which approximates the utility of each data subset on model performance in every training epoch. By deriving the closed-form Shapley value for each data point using the CHG utility function, they reduce the computational complexity to that of a single model retraining. They test CHG Shapley for real-time data selection in three settings: standard datasets, label noise datasets, and class imbalance datasets.

### Strengths
The paper is very well written and organized. The main idea and the method are presented very clearly.

### Weaknesses
I do not see substantial difference between the proposed method and the existing gradient based methods, especially the following one. Even in the experiments, the difference is not always noticeable.

- Wang et al., 2024, Data Shapley in One Training Run.

Minor comments: The previous gradient-based methods are not listed in Table 1.

### Questions
Is there fundamental difference between your method and the methods in the three papers below? What is the advantage of your method?
- Wang et al., 2024. Data Shapley in One Training Run.
- Xia et al., 2024. LESS: Selecting Influential Data for Targeted Instruction Tuning
- Pruthi et al. 2020. Estimating Training Data Influence by Tracing Gradient Descent

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies data evaluation with regard to its contribution to model performance. Prior work on Shapley value and Data Shapley suffers from high resource and time requirements to evaluate each data point. To circumvent this issue, the authors propose instead to estimate the utility function using the CHG (Compound of Hardness and Gradient) score to obtain a close-formed Shapley value for each data point. This approach reduces the computation complexity of Data Shapley to that of a single model training run. Furthermore, the authors extend this framework to real-time data selection, which was previously impractical using prior methods of calculating data value.

### Strengths
- The proposed method of combining hardness and gradient utility function is novel. 
- The authors provided experimental results to support their theoretical claims.

### Weaknesses
 - The writing is confusing and lacks intuition. In Theorem 1, the authors provided a long equation 4 without explaining the importance of each term in this expression.
- In Table 2, it is not immediately clear why CHG Shapley outperforms other methods w.r.t accuracy and time. For example, CHG Shapley does not always provide the highest accuracy across different fractions of CIFAR 10 and CIFAR 100. Moreover, in CIFAR10, AdaptiveRandom sometimes even outperforms CHG Shapley while running for a shorter time.
- Similarly, in Table 3, the authors only draw the conclusion that CHG Shapley is outperforming Gradient Shapley. However, CHG Shapley is not better than existing methods in most comparisons.

### Questions
- Can the authors clarify how CHG Shapley is doing better than prior work when the empirical findings seem to suggest the contrary? 
- Can the authors provide more intuition in Equation 4 (Theorem 1)? What does each term here mean and where do they come from?

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
4

### Summary
The paper studies the problem of data valuation and an application of data valuation, namely data selection during training. The authors focus on the efficiency of data valuation for large datasets, which presents an issue for many common Shapley value-based methods. They propose a Gradient Shapley and a compound of hardness and Gradient Shapley as the data valuation method. Empirical investigation shows the comparison of these two proposed methods with several existing methods.

### Strengths
- The data valuation problem is highly relevant and interesting to the community. In particular, the issue being studied is the computational cost of Shapley value-based methods. It is also a highly relevant issue.
- The writing is relatively clear.
- There are experimental results against several existing methods.

### Weaknesses
 - The authors propose a new utility function that takes into account the "hardness". From lines 234-235, it seems the optimization objective of the ML model is changed. However, this new optimization objective does not seem to have been theoretically justified. Specifically, the introduction of the hardness term, which appears to be a measure of the loss gradient magnitude, is not clearly motivated in the context of Shapley value. The paper does not provide a theoretical analysis of how this modification affects the properties of the Shapley value, such as fairness or efficiency.
- The proposed approach utilizes an approximation of the change in the loss function, but does not seem to show how good this approximation is. The use of the last-layer gradient as a proxy for the full gradient is a significant approximation, and the paper lacks a rigorous error analysis of this approximation. The authors do not quantify the potential discrepancy between the last-layer gradient and the true gradient, which could impact the accuracy of the data valuation.
- Furthermore, the proposed approach requires computing a per-sample gradient and storing these gradients. It does not seem to significantly reduce the computational cost of training, and additionally incurs memory overhead. While the authors claim efficiency, the need to compute and store per-sample gradients, even if only for the last layer, introduces a computational and memory burden that is not negligible, especially for large datasets. The paper does not provide a detailed comparison of the computational cost against other methods, taking into account both time and memory.
- More extensive expreimental results, larger datasets and larger models can add to the strength of the claims. The experimental evaluation is limited in scope, focusing primarily on CIFAR datasets and relatively small models. The paper would benefit from experiments on larger datasets, such as ImageNet, and with more complex models, to demonstrate the scalability and robustness of the proposed method.

### Questions
How are (Wu et al., 2022) and (Ki et al., 2023) related to this work? Should they be compared?

`In this paper, we focus on the efficiency problem of data valuation on large-scale datasets.`

How large is considered large-scale datasets? Data-OOB seems to be able to scale to millions of data points. Is there comparison on datasets of similar scales?

What is $\alpha$ in Theorem 1?

What is the memory overhead from storing the per-sample gradients?

Typically, mini-batch SGD is used for training (namely the gradient is computed w.r.t. a mini-batch instead of each data point), which does not compute per-sample gradients. Does that mean you method needs to incur additional computational overhead?

What is the error (theoretical or empirical) of the last-layer gradient as an approximation?

_References_

DAVINZ: Data Valuation using Deep Neural Networks at Initialization. Zhaoxuan Wu, Yao Shu, Bryan Kian Hsiang Low. In ICML 2022.

DATA VALUATION WITHOUT TRAINING OF A MODEL. Nohyun Ki, Hoyong Choi, Hye Won Chung. In ICLR 2023.

### Soundness
2

### Presentation
2

### Contribution
2
