# UNICORNN: Unimodal Calibrated Ordinal Regression Neural Network

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Ordinal regression is a supervised machine learning technique aimed at predicting the value of a discrete dependent variable with an ordered set of possible outcomes. Many of the algorithms that have been developed to address this issue rely on maximum likelihood for training. However, the standard maximum likelihood approach often fails to adequately capture the inherent order of classes, even though it tends to produce well-calibrated probabilities. Alternatively, some methods use Optimal Transport (OT) divergence as their training objective. Unlike maximum likelihood, OT accounts for the ordering of classes; however, in this manuscript, we show that it doesn't always yield well-calibrated probabilities. To overcome these limitations, we introduce UNICORNN, an approach inspired by the well-known Proportional Odds Model, which offers three key guarantees: (i) it ensures unimodal output probabilities, a valuable feature for many real-world applications;
(ii) it employs OT loss during training to accurately capture the natural order of classes;
(iii) it provides well-calibrated probability estimates through a post-training accuracy-preserving calibration step.
Experimental results on six real-world datasets 
demonstrate that UNICORNN consistently either outperforms or performs as well as recently proposed deep learning approaches for ordinal regression. It excels in both accuracy and probability calibration, while also guaranteeing output unimodality. The code will be publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors propose an ordinal regression approach that enforces unimodularity in the output distribution. They use a truncated normal distribution to model the output probabilities.  They provide unimodular proof of the output distribution. They show experimental results to highlight the effectiveness of the proposed approach compared with baseline approaches on various metrics.

### Strengths
1. Authors propose a theoretically sound approach for ordinal regression, which can output unimodular outputs.
2. Paper is very well written and easy to read.

### Weaknesses
1. Some references are missing. E.g.
(a) Rank consistent ordinal regression for neural networks with application to age estimation. Wenzhi Caoa, Vahid Mirjalilib, Sebastian Raschkaa. Pattern Recognition Letters, (2020), 325-331.
(b) Garg, B. & Manwani, N.. (2020). Robust Deep Ordinal Regression under Label Noise. Proceedings of The 12th Asian Conference on Machine Learning. 129:782-796

2. The baseline approaches used do not cover a variety of algorithms for ordinal regression. Please see the Questions section for suggested baselines.

3. Code is not provided.

### Questions
1. Please comment on the rank consistency of the proposed approach. In think, unimodularity of the output distribution and rank consistency of the two contradictory properties. Please comment. It would be good to see the average number of rank violations made by the proposed approach.
2. Please compare with a rank-consistent baseline (e.g. Shi et al., 2023)
3. A simple approach for imposing unimodularity in the output vector is by posing the constraint $P(Y=1)\leq P(Y=2)\leq \ldots \leq P(Y=c)\leq \ldots P(Y=K)$, where $c$ be the target class and $K$ be the total number of classes. Minimizing loss with these constraints can be an alternate approach to achieving unimodularity. It can be a good baseline for the proposed approach. Can you show some results why such an is not good?
4. Please explain the truncated normal distribution properly. What is the support set for this distribution?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
**Summary**:

The paper presents a technique for ordinal regression tasks, focusing on two aspects: (1) constructing uni-modal distribution, which is desirable in many cases; (2) generating calibrated predictive distribution that is comparable to the empirical distribution. For the uni-modal distribution construction, it generates a truncated normal distribution, and constructs evenly spaced thresholds to ensure the unimodality. For the calibration, the model performs retraining using Brier loss to adjust the parameter from the first stage. The authors then demonstrate the performance of the proposed model in the real experiments.

### Strengths
**Strengths**:

1. The paper clearly describes the motivations and explanations of the proposed model.
2. A rather simple and interesting approach for ensuring unimodality of the predictive distribution.
3. Retraining procedure for producing calibrated distributions.
4. The experiments show the benefit of the proposed approach on several datasets.

### Weaknesses
 **Weaknesses**:

1. The description of the proposed training algorithm in Sec. 4.4 is rather simple. I would suggest the authors to put a proper algorithm (using formal notation) for the model
2. The way the authors ensure unimodal distribution can be limiting. Even though the proposed method always generates a unimodal distribution, not every unimodal distribution can be represented by the proposed construction. In fact, with just two degrees of freedom, it is rather limited.
3. The novelty of the proposed models is rather limited, as similar unimodality construction and the calibrated distributions constructions have been proposed before.

### Questions
**Questions**:

Please address the weaknesses mentioned above.

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
This paper introduces UNICORNN, a deep-learning approach designed for ordinal regression tasks where class labels follow a natural order. The authors address three primary challenges in ordinal regression: (1) enforcing unimodal output probability distributions, (2) capturing the ordered relationships among classes effectively, and (3) providing well-calibrated probability estimates. Extensive experiments on six real-world datasets demonstrate that UNICORNN consistently matches or outperforms recent ordinal regression methods, excelling in accuracy, probability calibration, and ensuring output unimodality.

### Strengths
1. UNICORNN addresses significant limitations in existing ordinal regression methods by providing an approach that ensures both unimodal and calibrated probabilities, which is critical for applications 
2. The paper is well-structured and Explanations are generally clear.
3. The combination of Optimal Transport (OT) loss with accuracy-preserving calibration is original and significant for ensuring both order respect and reliable probability estimates

### Weaknesses
1. The proposed method has a two-stage training process, significantly increasing the model's computational complexity. Can the author show the time complexity of training or compare the training time of the proposed method with other methods?
2. The methods used in experiments are too old. The authors should include comparisons with methods from recent years such as [1,2]. Can the author show the results on some large-scale datasets, such as the datasets with more training samples or more classes? 
3. More experiments are needed in ABLATION STUDY. It only has two datasets. More experiments on different datasets are required.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2
