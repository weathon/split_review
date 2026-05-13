# GTR: Semi-supervised Learning with Grouping and Transporting for Robust Thresholding

- Decision: Reject
- Scores: 3, 5, 6, 5, 5, 3

## Abstract
Semi-supervised learning (SSL) digs unlabeled data by pseudo-labeling when labeled data is limited. Despite various auxiliary strategies enhancing SSL training, the main challenge is how to determine reliable pseudo labels through a robust thresholding algorithm based on quality indicators (e.g., confidence scores). However, the existing strategies for distinguishing low or high-quality labels through simple grouping indicators remain in trivial design, ignoring the characteristics of the data distribution itself, which cannot guarantee robustness and efficiency. To this end, we group the quality indicators of pseudo labels into three clusters (easy, semi-hard, and hard) and statistically reveal the real bottleneck of threshold selection, i.e., the sensitivity of semi-hard samples, through empirical analysis. We propose an adaptive Grouping and Transporting method that Robustly selects semi-hard samples with test-time augmentations and consistency constraints while saving the selection budgets of easy and hard samples, dubbed as GTR. Our proposed GTR can effectively determine high-quality data when applied to existing SSL methods while reducing redundant costs in the selection. Extensive experiments on 11 SSL benchmarks across three modalities verify that GTR can achieve significant performance gains and speedups over Pseudo Label, FixMatch, and FlexMatch.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript delineates an approach, termed GTR, which is designed for semi-supervised learning. The paper claims that the latest methods for distinguishing low or high-quality labels require complex-designed thresholding strategies but still fail to guarantee robust and efficient selection. In addressing this issue, the GTR model exhibits an amalgamation of data grouping/clustering, optimal transportation, test-time augmentations, and consistency regularization, a combination that endows the method with superior performance in comparison to baseline methods.

### Strengths
S1. An approach to grouping into three clusters (easy, semi-hard, and hard) is worth typing.

S2. The evaluation is comprehensive, with comparisons to baseline methods and ablation study providing a compelling demonstration of the superior performance of the proposed method.

### Weaknesses
W1. A significant concern regarding this paper is its lack of technical innovation. The proposed method is more like a combination of existing techniques. Technical contribution is somewhat limited. Further technical insights regarding the implementation and specific algorithms within the GTR model would also be beneficial.

W2. Those hyperparameters and thresholds somewhat degrade the model's applicability in practice. 

W3. The paper could have a further explanation of the methods TTA,  threshold settings, consistency constraints, and how these methods are applied to the model, a factor which could be helpful for fully understanding the proposed method. 

W4. The empirical evidence presented in the paper lacks persuasiveness. A substantial performance boost could have justified the paper's simplicity and application-oriented nature. However, the minor improvement over baselines, as indicated primarily in experiments, does not substantiate the approach's effectiveness convincingly. In addition, no code has been released or noted in the paper.

W5. The notation $T$ in Lines 285, 293, 295, etc. need more clarification.

### Questions
See weaknesses above.

### Soundness
3

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
In this paper, the authors introduce a new thresholding technique to create better pseudo labels for semi-supervised learning. The authors argue that thresholds used for pseudo labeling change based on difficulty of the unlabelled samples’ indicator (e.g., confidence scores) distribution. Therefore, the authors group the into 3 clusters as easy, semi-hard and hard ones by using Gaussian mixture modelling. Then, they use a transporting mechanism to align the distributions of semi-hard and easy indicator groups. The authors test their proposed technique adapting it to existing semi-supervised learning methods such as FlexMatch and Pseudo Label methods and report improvements over the baselines.

### Strengths
The main strengths of the paper can be summarized as follows:
i) Grouping the unlabelled samples’ indicator values into three clusters as easy, semi-hard and hard ones and utilizing semi-hard ones for improving pseudo labelling seems reasonable.
ii) The authors report accuracy and training time improvements over the baseline methods.

### Weaknesses
The main weaknesses of the paper can be summarized as follows.
i) Although I understand the general idea, I had difficulty understanding the details regarding implementation. There a lot of missing details, notation problems and unexplained terms throughout the paper, and  the paper is written badly from this perspective. The following details must be explained more:
-- The authors must first explain the general network used for learning. They mention from the student network in a few places. Did the authors use a teacher student network training pipeline in the paper?
-- There are terms that are not explained in the equations. For examples, the first term after summation operation in Equations 2 and 4.
-- I did not understand how the authors implement transporting, what is done in that step? How the semi-hard and easy distributions are aligned and how this alignment is used for training?
-- What is the purpose of filtering defined in Section 3.2?
-- What is the dimension d of the z vector used in Equation 5?
ii) The figures are misleading. In Figure 1, confidence scores are used in left part whereas reward score distributions are used on the right. As far as we understand from the text, they are different, therefore comparing confidences to reward scores does not make sense. Confidence score or reward scores must be used for both cases.
iii) Figures 2 and 3 conflict each other. In figure 2, it seems both easy and semi-hard indicator values are sensitive to thresholding, yet in figure 3, only semi-hard indicator values are sensitive to thresholding.
iv) Experimental evaluations is not fair. One cannot use a pre-defined network trained on ImageNet for training a semi-supersived training on ImageNet, STL and Cifar 100 datasets. The network already seen all the examples of ImageNet dataset during training. Fine-tuning a semi supervised learning algorithm from this pre-trained network is a clear violation of a fair testing procedure. Also why different networks are used for different datasets (e.g., why the authors do not use FlexMatch for the test reported in Table 3 although it I used for ImageNet dataset or why FixMatch is not used in Table 2?)
v) The authors must also report the state-of-the-art accuracies obtained the tested datasets.

Minor Issue: there are some minor typos such as in the title of Section 3.2 that must be corrected.

### Questions
I have some questions indicated in Weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the semi-supervised learning problem and divide the pseudo labels into three groups (easy, semi-hard, and hard). The authors find that the bottleneck of threshold selection lies in the sensitivity of semi-hard samples. To solve this issue, the authors propose an adaptive grouping and transporting method to align the semi-hard samples with easy samples. Experiments show that the propose method not only achieves performance improvements but also accelerates the convergence.

### Strengths
1.	This paper addresses an important problem in semi-supervised learning, i.e., robust thresholding selection.
2.	The motivation is clearly derived from experimental findings, making it straightforward and intuitive.
3.	The proposed method is effective and efficient according to the reported results in this paper.

### Weaknesses
1.	The proposed method relies heavily on the partition of three types of samples, which may introduce the risk of non-robustness, especially when the partition is not accurate.
2.	Sensitivity analyses of the hyperparameters are absent.
3.	Compared with the SOTA method SR, the speedup is not that significant.

### Questions
1.	On page 2, lines 68-69, the authors claim that “GTR mitigates the threshold sensitivity by focusing on the intra-class properties”. Could you clarify which specific properties you are referring to?
2.	When you report the training time, do you include the time of preprocessing of dividing the pseudo labels into three groups?
3.	In Table 4, why do you not report the results of FlexMatch+SR? I am more interested in the comparisons between GTR and SR.
4.	There are some typos in line 285, (“Changes” should be “changes”) and in Eq.(9) (“$ \sim $” may be “$ \approx$”).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript proposes a semi-supervised learning method called GTR (Grouping and Transporting for Robust Thresholding), which improves the robustness of pseudo-label selection through grouping and transporting mechanisms. Specifically, the GTR method divides the quality indicators of pseudo labels into three groups: easy, semi-hard, and hard. Then, it uses transporting mechanisms to efficiently select semi-hard samples with test-time augmentations and consistency constraints while saving the selection budgets of easy and hard samples. Finally, this manuscript elucidates how the GTR method promotes the semi-hard group towards the easy group by employing kernel density estimation.

### Strengths
1. This manuscript reveals that the obstacle of existing thresholding techniques lies in their inability to separate the semi-hard group of indicators when selecting high-quality pseudo labels. 
2. This manuscript proposes the GTR method to obtain robust thresholding through grouping and transporting. 
3. This manuscript employs kernel density estimation to analyze how the GTR method promotes the semi-hard group towards a better-optimized distribution, such as that of the easy group.

### Weaknesses
1. Some symbols and parameters are not provided in the context, causing difficulty in understanding.
2. The description of Section 3 is unclear, it is suggested to add an algorithm summary.
3. In the experiments, there are few comparative methods and no comparison with recent works.

### Questions
1. This method divides data into three categories based on confidence or reward indicators: easy, semi-hard, and hard. Then, multiple selection and consistency constraints are used to reduce the uncertainty of semi-hard samples and improve the accuracy of pseudo labels. As shown in Figure 1(a), the separation boundaries (yellow lines) of various classes are different. Therefore, will the proposed method lead to class imbalance due to the selection of reliable pseudo labeled data, thereby reducing the model's generalization ability.
2. In the transportation section, is the number of easy groups kept constant? Is the number of hard groups constantly decreasing as the high-scoring half of the data is assigned to the semi-hard group in the next iteration? Will this setting result in minimal hard data that can be ignored and increase the low scores of data in semi-hard groups? How is the final equation of unlabeled loss obtained? The description of this part is lacking.
3. The introduction of Equation 6 seems abrupt, authors claim that the Mahalanobis distance is used to assess the fit of pseudo-labels, with larger distances indicating lower reliability, which guides thresholding decisions. However, the threshold decision has been given in the transporting mechanism, and introducing Mahalanobis distance seems meaningless.
4. In the experiment, this manuscript demonstrates that the proposed method can reduce training time, but does not provide theoretical analysis.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes GTR for improving semi-supervised learning tasks. GTR includes grouping and transporting, where grouping tries to cluster pseudo-labels into distinct groups and transporting is used to process different groups. Experiments on benchmarks show GTR outperforms other methods, achieving better performance and speedup.

### Strengths
(1) The paper is easy to follow.

(2) Better performance and speedup are achieved in the experiments.

### Weaknesses
(1) The authors should improve the writing of this paper. Especially, the description of transporting is confusing. For example, the  examples for equation (3) need more explanation.

(2) There is not enough explanation for the reason why TTA technique is effective for selecting more reliable   semi-hard pseudo-labels.

(3) Lack of theoretical understanding for the proposed method.

(4) More SSL methods need to be included in the experiments, such as SoftMatch and FreeMatch.

### Questions
(1) Why the example in line 216 violates the claim in line 184 that the probability is summing up to 1?

(2) In equation (4), what is the detailed process of indicator?

(3) How to estimate kernel density in this paper?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a Grouping and Transporting for Robust thresholding (GTR) method for semi-supervised learning (SSL). The method addresses the challenge of determining reliable pseudo labels by clustering quality indicators into three groups and using test-time augmentations and consistency constraints to select and transport semi-hard samples. The authors claim that GTR can effectively determine high-quality data when applied to existing SSL methods while reducing redundant selection costs. The paper conducts extensive experiments on eleven SSL benchmarks across three modalities to verify the effectiveness of GTR.

### Strengths
1. The proposed GTR method is novel and addresses an important problem in SSL. The idea of clustering quality indicators and using transporting to handle different groups of samples is intuitive and has the potential to improve the performance of SSL methods.

2. The experimental results are comprehensive and show significant performance gains and speedups over several baseline methods. The experiments cover a wide range of datasets and modalities, which adds to the credibility of the results.

3. The paper provides a detailed analysis of the SSL training process and the properties of different groups of samples. This analysis helps to understand the behavior of the proposed method and its advantages over existing methods.

### Weaknesses
1. As can be seen from Table 1, the greatest advantage of proposing this method compared to previous methods lies in whether the threshold can ensure robustness. However, this is not reflected in the description of the method and analysis, and it is not stated what kind of robustness it is, why it can maintain robustness, and why the previous methods cannot guarantee the robostness.

2. The formulas representing the transporting process are confusing. Could it be possible to use some set operations (intersection, union, complement, etc.) and element selection conditions to represent this process, in order to increase the readability of the article?

3. Some reasonable and logical explanations are needed for the transporting process, e.g., why the distribution of semi-hard samples should be made consistent with that of easy samples, what kind of distribution is it, how to make them consistent, and what are the effects after they are made consistent.

### Questions
1. Please explain the robustness of the threshold in the proposed method in detail.

2. Please explain the transporting process clearly at the beginning, because the readers may be confused when encountering 'transporting' from Abstract and Introduction.

### Soundness
2

### Presentation
2

### Contribution
2
