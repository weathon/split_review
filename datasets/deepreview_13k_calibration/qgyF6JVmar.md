# OTMatch: Improving Semi-Supervised Learning with Optimal Transport

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Semi-supervised learning has made remarkable strides by effectively utilizing a limited amount of labeled data while capitalizing on the abundant information present in unlabeled data. 
However, current algorithms often prioritize aligning image predictions with specific classes generated through self-training techniques, thereby neglecting the inherent relationships that exist within these classes. 
In this paper, we present a new approach called OTMatch, which leverages semantic relationships among classes by employing an optimal transport loss function to match distributions. We conduct experiments on many standard vision and language datasets. The empirical results show improvements in our method above baseline, this demonstrates the effectiveness and superiority of our approach in harnessing semantic relationships to enhance learning performance in a semi-supervised setting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a semi-supervised learning method based on optimal transport, exploiting the relation of different classes. Evaluated on the classic benchmark, the proposed method outperforms the previous SOTA methods.

### Strengths
1. The proposed method provides state-of-the-art performance on classic benchmarks.
2. Provides a connection between optimal transport and thresholding-based method.

### Weaknesses
1. More evaluation results are expected to show on datasets of other modalities [1]. 
2. As the authors stated, the O(K) complexity of the proposed method comes from the mild assumptions. Providing actual runtime would be helpful to justify this statement further. 
3. What's the loss weight of the proposed loss term, How is it affecting training? Ablation study of it is missing.

### Questions
1. The contrastive learning-based methods such as SimMatch and CoMatch also consider the relation between classes. What's difference of optimal transport to this?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on semi-supervised learning and proposes a new algorithm called OTMatch. The proposal aims to capture relationships between classes and adopt the optimal transport distance as a loss function. Experimental results show that the proposal can achieve performance improvement over previous SSL methods on some benchmark datasets.

### Strengths
This paper proposed a new SSL algorithm, compared with previous SSL methods, the proposal considers capturing the relationship between classes. The idea is insightful to some extent.

### Weaknesses
1. Why the class relationship is helpful for semi-supervised learning? Is there any analysis or discussion?
2. If the class relationship is important for semi-supervised learning, is there any easier method to exploit the relationship?
3. The proposed unsupervised loss is difficult to compute. Although the authors claim in some conditions, the computational complexity can be reduced, whether these conditions are satisfied in real-world tasks is hard to know.
4. When there are many classes (such as ImageNet or CIFAR-100), the performance improvement is limited.

### Questions
As discussed above.

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
This paper proposes a method that leverages the inherent relationships among existing classes by using optimal transport.

### Strengths
1. The paper proposes an interesting idea that exploits the inherent relationship between classes in semi-supervised learning

### Weaknesses
1. Ablation study on \(\epsilon\) is missing? How did you determine the appropriate \(\epsilon\) value for OT?
2. The novelty is limited. In comparison to Freematch, this paper introduces an additional loss, \( L_{un3} \). However, an ablation study detailing \( L_{un3} \) under various hyperparameters seems to be absent. 
3. Section 4 lacks clarity and could benefit from further elucidation.
4. I strongly recommend presenting a structured algorithm or providing a comprehensively defined overall loss function for better clarity.


### Questions
1. In the text following the second formulation, "q_ui" should be corrected to "Q_ui."
2. The depiction in Figure 1 is ambiguous. What constitutes the input for the OT loss?
3. How can we obtain the ground truth matching matrix \( T \) in formulation (1)?
4. Why was KL divergence chosen as the loss function?
5. I am unclear about the statement in the paper that suggests the objective is "to push \( f(x) \) in the direction of \( wk \)." Can this be clarified?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper discusses the limitation of cross-entropy loss in addressing relationships between classes and introduces the OTMatch framework, which uses the optimal transport method to improve semi-supervised learning by incorporating inter-class information. The proposed method is evaluated on CIFAR-10/100, ImageNet, and STL-10.

### Strengths
1. The motivation behind this work is evident.
2. The overall organization the paper is commendable, making it easy to follow and understand.

### Weaknesses
1. The novelty is limited. Using OT strategy to address semi-supervised learning has been proposed in previous work [1]. The proposed method does not show significant improvement compared to existing work and lacks the necessary experimental comparisons.
2. The improvement of proposed method on the evaluated dataset is not significant, and there is no comparison regarding its impact on convergence speed and the loss curve.

### Questions
It is suggested to add more analysis about the impact of long-tail classes on the OT approach, and more analysis of the advantage/disadvantage of the threshold-free methods.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
