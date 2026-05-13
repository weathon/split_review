# Stochastic Order Learning: An Approach to Rank Estimation Using Noisy Data

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
A novel algorithm, called stochastic order learning (SOL), for reliable rank estimation in the presence of label noise is proposed in this paper. For noise-robust rank estimation, we first represent label errors as random variables. We then formulate a desideratum that encourages reducing the dissimilarity of an instance from its stochastically related centroids. Based on this desideratum, we develop two loss functions: discriminative loss and stochastic order loss. Employing these two losses, we train a network to construct an embedding space in which instances are arranged according to their ranks. Also, after teaching the network, we identify outliers, which are likely to have extreme label errors, and relabel them for data refinement. Extensive experiments on various benchmark datasets demonstrate that the proposed SOL algorithm yields decent rank estimation results even when labels are corrupted by noise.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To solve the rank estimation problem with label noise, this manuscript proposes the stochastic order learning (SOL) method. Specifically, label errors are represented as random variables that follow a Gaussian distribution. Based on this, the stochastic dissimilarity of instance x from rank r is defined and the corresponding discriminative loss and stochastic order loss are designed to train a network to build an embedding space where instances are arranged according to their ranks. Furthermore, after network training, the SOL method identifies outliers that are likely to have extreme label errors and relabel them to refine the dataset.

### Strengths
1. This manuscript models label errors as stochastic variables and derives embedding space constraints to arrange instances based on their probabilistically associated ranks.
2. This manuscript proposes outlier detection and relabeling schemes to pinpoint and mitigate instances with extreme label errors, thereby diminishing the dataset's overall noise level.

### Weaknesses
1. The reason for setting formulas 12-14 lacks description. Specifically, why is the formula defined in this way? It is necessary to explain the meaning of setting $r_x-r_y-s+t$. In other words, whether I can consider that if the label noise of samples x and y is s and t, respectively, the distance between the true labels of the two samples is $r_x-r_y-s+t$.  
2. In the experiments, there are few comparative methods and no comparison with the state-of-the-art methods. If there are few recent papers about rank estimation with label noise, it can be compared with related methods mentioned in this paper. For example, if rank estimation is regarded as a classification task, is the SOL method better than the approach in the paper [1]? Besides, on datasets with a rank less than 5, whether the SOL method is still performing significantly and better than the method in the paper [2].

### Questions
1. The proposed method settings tend to have a risk of labeling errors for each sample. More likely, only a small amount of samples in the dataset is mislabeled. In this situation, is the performance of the method still effective? In addition, the proposed method is based on the key assumption that the label noise of each sample follows the same discrete Gaussian distribution. It is more natural that the standard deviation of noise variables varies among different samples. In the future, a fine-tuning mechanism for setting standard deviations for each sample can be considered while taking into account computational complexity.
2. There are many hyperparameters in the manuscript. Can an adaptive mechanism be designed to select the optimal values of these parameters for different datasets?
3. In the relabeling mechanism, the rank of each detected outlier is adjusted by the same magnitude, that is, half of the average absolute difference between noisy and estimated rankings overall training instances, which seems counterintuitive. It is reasonable to combine outlier detection with the relabeling mechanism to adjust the rank of the outlier.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel algorithm to address noise in rank ordering within learning-to-rank tasks. Extensive experiments are conducted to demonstrate the effectiveness of the proposed method.

### Strengths
This paper addresses a practical, real-world setting, and the experiments effectively demonstrate the method's effectiveness.

### Weaknesses
1. The problem of noisy classification is well-studied, particularly in image classification (e.g., [1]). However, the authors do not clearly explain how their approach to learning with rank labels differs from or improves upon standard classification methods. Furthermore, the fundamental distinction between ordered learning and classification remains unclear, particularly regarding why standard classification algorithms cannot be adapted for ordered data or why a specialized ordered learning approach is necessary. This lack of clarity undermines the novelty of the proposed method.
2. The writing quality requires improvement. Several notations are undefined, and some equations are presented without adequate derivation or verification.
3. The proposed method appears to have limited practical effectiveness due to its computational inefficiency. The requirement to scan the entire dataset for centroid calculation makes the algorithm unsuitable for large-scale datasets. This inefficiency is a significant drawback, especially when compared to methods that can operate on mini-batches or subsets of the data.
4. The method's reliance on a hyperparameter, specifically the variance $\sigma$ of the Gaussian noise distribution in Equation 2, is not well-justified. The authors do not explain how this variance is obtained or how it should be chosen in practice, which raises concerns about the method's robustness and generalizability.

### Questions
1. Where is the definition of $d(\cdot, \cdot)$ in Eq.(3)
2. How do the authors ensure that the noise $e_x$ remains within the range of true labels in Equations Eq.(1) and Eq.(2)
3. In line 155, could the authors clarify why $\mu_{r_{x + s}}$ the probablity $p_s$?
4. According to Equation (5), does the algorithm require scanning all data?
5. Is the probability in Equation (2) known or assumed?

### Soundness
2

### Presentation
2

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
This paper introduces a novel algorithm called Stochastic Order Learning (SOL) for reliable rank estimation in the presence of label noise. The proposed method models label errors as random variables and formulates a desideratum to minimize dissimilarity from stochastically related centroids. By employing discriminative loss and stochastic order loss, the algorithm constructs an embedding space that effectively arranges instances according to their true ranks. Additionally, it incorporates outlier detection and relabeling schemes to refine noisy data, demonstrating robust performance across various benchmark tasks.

### Strengths
1. The proposed algorithm in this paper demonstrates reasonable formulation for rank estimation in the presence of label noise, with clear mathematical derivations. 


2. The experimental section is adequately designed, covering multiple benchmark datasets to validate the algorithm's performance.

### Weaknesses
1. The novelty of the paper is relatively moderate. While it builds upon existing research, it lacks significant innovative contributions. 

2. The Dataset Section can be placed in the Appendix to allow more space for detailed analysis of experimental results.


3. The paper lacks comparisons with algorithms from the past two years. Including recent benchmarks would provide a more comprehensive evaluation for the proposed method. Besides, the number of comparison algorithms is too small. Adding more comparison algorithms will further highlight its advantages.

### Questions
See Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper solves the rank estimation problem under noisy data. The main novelty of this work is handling the input data with label noise, which seems limited, as other works can also handle noise data. Moreover, the motivation of the adopted techniques is also not clear. The experimental evaluation of this paper is good.

### Strengths
This paper proposes a model to handle the noisy rank learning problem. The experimental evaluation is good.

### Weaknesses
Many descriptions are not clear. For example: 
What is the difference between rank estimation and order learning? 
In Eq. (1), the ground truth label is represented by consecutive integers, while the observed noisy rank is assumed to be the sum of the true rank with some Gaussian noise. When the Gaussian noise is added, will the observed rank still be integers? Besides, why does the noise follow a Gaussian distribution? 
In line 137, what is the relationship between e and e_x?

### Questions
Please see the weakness.
Also, please describe the motivation for the proposed method.

### Soundness
2

### Presentation
1

### Contribution
2
