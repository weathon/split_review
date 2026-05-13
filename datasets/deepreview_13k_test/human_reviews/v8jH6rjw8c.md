# Fairness Improves Learning from Noisily Labeled Long-Tailed Data

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Both long-tailed and noisily labeled data frequently appear in real-world applications and impose significant challenges for learning. Most prior works treat either problem in an isolated way and do not explicitly consider the coupling effects of the two. Our empirical observation reveals that such solutions fail to consistently improve the learning when the dataset is long-tailed with label noise. Moreover, with the presence of label noise, existing methods do not observe universal improvements across different sub-populations; in other words, some sub-populations enjoyed the benefits of improved accuracy at the cost of hurting others. Based on these observations, we introduce the \textbf{F}airness \textbf{R}egularizer (\fr), inspired by regularizing the performance gap between any two sub-populations. We show that the introduced fairness regularizer improves the performances of sub-populations on the tail and the overall learning performance. Extensive experiments demonstrate the effectiveness of the proposed solution when complemented with certain existing popular robust or class-balanced methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is trying to address an interesting problem, that is, how to eliminate long-tailed effect and noisy labels simultaneously. Previous approaches have often tackled these issues independently and have not considered the combined effects of both. This paper empirically demonstrates that such isolated solutions are ineffective when dealing with long-tailed datasets that also have label noise. Furthermore, existing methods do not consistently improve accuracy across all sub-populations, leading to uneven performance improvements. In response to these observations, the paper introduces the Fairness Regularizer (FR), which aims to reduce performance disparities between sub-populations. FR is shown to enhance the performance of tail sub-populations and overall learning in the presence of label noise. Experiment results support the effectiveness of this approach, especially when combined with existing robust or class-balanced methods.

### Strengths
S1: This paper introduces a novel perspective on addressing both long-tailed problem and noisy label problem, which is rarely discussed in previous studies.

S2: This paper provides some empirical evidence, which helps to better interpret motivation.

S3: This paper is well-organized and clearly written.

### Weaknesses
W1: The logic of this paper is rather confusing; the author discusses the issues of noisy data and long tail problem together, but does not build a good bridge of them. In addition, the significance and necessity of the empirical evidence is not clear. Because it is also necessary to deal with the long tail problem on clean data, instead of only need to deal with the long tail problem on noisy data. The authors need to emphasize the differences and connections between dealing with long tail problems on noisy data and dealing with long tail problems under clean data (e.g., problem formalization or techniques).

W2: Why observation 3.1 holds？Specifically, if prediction model trained on noisy data has larger variance than the prediction model trained on clean data, the same pattern will be also observed. Therefore, observation 3.1 depends on the original variance of the prediction model. In addition, if we did not remove any sub-population and draw an Acc plot for clean data and noisy data, can we observe the similar pattern in Figure 4?  Similar arguments are also holds for observation 3.2.

W3: The problem is handled by simply adding the distance of each class from the "center" to the original loss function, which is simple and lacks some novelty. For example, is it possible to calibrate clean data with noisy data or head with tail data to address this problem?

W4: How can we choose $\lambda_{i}$ for each sample in practice when it is not set to a constant?

W5: This paper is missing some noisy label and long-tail baselines. There are many works trying to denoise, like [1-4], and many long-tail baselines like [5-6]. I didn't intend for the authors to compare all noisy label and long-tail baselines, but it is necessary to consider some of them.

[1] Patrini, Giorgio, et al. "Making deep neural networks robust to label noise: A loss correction approach." in CVPR 2017

[2] Han, Bo, et al. "Co-teaching: Robust training of deep neural networks with extremely noisy labels." in NeurIPS 2018.

[3] Xia, Xiaobo, et al. “Are anchor points really indispensable in label-noise learning?.” in NeurIPS 2019.

[4] Yong, Lin., et al. "A Holistic View of Label Noise Transition Matrix in Deep Learning and Beyond." in ICLR 2022.

[5] Chen, Wei, et al. "Crest: A class-rebalancing self-training framework for imbalanced semi-supervised learning. in CVPR 2021.

[6] Zhong, Zhisheng, et al. "Improving Calibration for Long-Tailed Recognition" in CVPR 2021.

### Questions
Please refer to weakness part for the questions.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a challenging learning problem under the existence of long-tailed and noisily labeled data. The paper makes efforts to understand and mitigate the heterogeneous effects of label noise for the imbalaenced data. The paper empirically examines the role of each sub-population and its influence on the test data. It proposes a fairness regularizer to encourage the learned classifier to achieve fair performance across different sub populations.

### Strengths
The paper is generally well written. The structure is clear and the motivation is strong. The Fairness Regularizer (FR) is easy to implement. The numerical results are relatively complete. Some theoretical insights are also included in the appendices.

### Weaknesses
The paper overally has no big weakness.

Minor suggestions: 

(i) How to tune $\lambda_i$'s? Is there any recommendation or theory to support this?
(ii) Some theory presented in the appendix can be moved into main content.
(iii) Can author make some comments on distribution shift problem? If some sub-population in the test data does not appear in training data, how to guarantee its performance?

### Questions
See weakness points.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores the problem of learning from noisy labeled and long-tailed data. The paper starts by observing that existing methods to improve learning from noisy labeled or long-tailed data create accuracy disparities across different sub-populations in the dataset. The paper proposes a method called Fairness Regularizer (FR) that incentivizes the learned classifier to have uniform performance across subpopulations, aiming to mitigate accuracy disparities and improve learning. Experiments indicate that the proposed method improves the model performance in underrepresented populations in the dataset while increasing overall model performance.

### Strengths
•	The idea of connecting fairness with robust learning is exciting and could lead to interesting results.   

•	The discovery in Figure 2 of the disparate impact in underrepresented groups when using methods to learn from data with label noise or long-tail is interesting and should be communicated to the community.   

•	The conclusion that methods that incentivize statistical parity led to better model performance under noisy labels and long-tail data is very nice. The results contradict the folklore that fairness improvement methods *always* decrease the model performance.  

•	The results demonstrated in the paper had strong statistical guarantees, as shown in Table 2.

### Weaknesses
•	The proposed method, Fairness Regularizer, is similar to the reductions approach for statistical parity [1]. But I didn’t find a citation for the paper.  

•	There are multiple existing in-processing methods to ensure fairness (statistical parity) across groups in the population check [2] Table 1 for multiple references. The authors should, ideally, compare their results with other fairness improvement methods. At least, the paper should mention other fairness improvement methods and discuss the difference between the proposed and existing approaches.  

•	I believe the points in the lower-left corner of Figure 2 and 6 are the underrepresented groups. However, Figure 6 and Figure 2 could provide a more explicit message to the reader by adding one more axis of information (e.g., the intensity of the color of the points) with the group representation.

### Questions
•	Could the authors please highlight the main differences between FR and the reductions approach [1]?

•	Why is the proposed method preferred compared to other fairness (statistical parity) improvement methods?



[1] Agarwal et al. A Reductions Approach for Fair Classification. 2018.

[2] Lowy et al.  A Stochastic Optimization Framework for Fair Risk Minimization. 2022

### Soundness
3 good

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
The paper assesses whether fairness methods can improve learning on noisy imbalanced data. A regularization approach is taken to promote similar losses across sub-populations.

### Strengths
- The claim is interesting and well-motivated: that fairness improves learning on noisy long-tail sub-populations.
- Extensive experiments are conducted.

### Weaknesses
- Table 3: empirical improvements seem marginal and lack confidence intervals or pairwise statistical significance tests.
  - I'm not too convinced that, e.g., changes from 74.46 to 74.48-74.50 are significant;
  - I suggest bolding only cells whose difference to the baseline are statistical significant, as opposed to a simple "larger than" test.
  - As an example, you can get confidence intervals using bootstrapping on the test set, without retraining; or running k-fold cross-validation to obtain a measure of dispersion of results.

- It's not clear whether access to group membership is useful given that the work is not targeting fairness improvements.
  To target the noisy long-tail sub-populations couldn't we just up-weight samples with higher loss and down-weight samples
  with lower loss? (an approach that is also quite common in the fairness literature)
  - What is the intuition behind the use of group membership supposedly leading to better performance?

- Fig. 6: there seems to be a lot of noise on the effect of FR across sub-populations;
  the paper is missing a more in depth analysis of the mechanism by which overall performance is increased.
  - Intuitively, it should improve performance on populations with lower representation in the dataset (tail populations);
    one example plot would show performance change on the y-axis (acc. increase or decrease after introducing FR), and sub-population size on the x-axis.

- Using a regularizer on the performance differences among sub-populations is not particularly novel.
  - The novelty stems from the use of a standard fairness tool to improve learning performance
    (regardless of fairness); but the fact that this is a standard fairness tool (and that FR is not
    the focus of the paper in any way) should really be made more clear in the paper.
  - Perhaps, if the goal is to show that standard fairness tools can have a positive impact on "noisy
    long-tailed sub-populations", it'd make more sense to use unaltered fair ML methods (that aim to
    bring sub-population performance closer) and show that the paper claim on improved learning holds.
  - Essentially, most fair ML methods reduce to the same thing as FR: up-weighing samples whose loss
    is larger than the average loss, or samples whose group has a larger loss than average.

### Questions
- Fig. 3: does the index have any meaning? Should this be sorted by frequency?
- Fig. 4: please use a more adequate font size, it's completely unreadable when printed.
- Instead of holding all $\lambda_i$ constant it would be interesting to use a standard dual ascent framework to jointly optimize the Lagrange multipliers.
  - "Intuitively, applying dual ascent is likely to result in a large $\lambda_i$ on the worst sub-population, inducing possible negative effects"
  - It'd be interesting to back this up with actual results.
- Eq. 3: given that the constraint that is actually used in practice is different from the definition of $\text{Dist}_i$ given in Section 4.1., I'd suggest giving a different name to each of these constraints.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
