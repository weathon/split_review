# Threshold-Consistent Margin Loss for Open-World Deep Metric Learning

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Existing losses used in deep metric learning (DML) for image retrieval often lead to highly non-uniform intra-class and inter-class representation structures across test classes and data distributions. %\yifan{across classes and data distributions? if over the training set, I think we were able to get pretty uniform inter-class structures}
When combined with the common practice of using a fixed threshold to declare a match, this gives rise to significant performance variations in terms of false accept rate (FAR) and false reject rate (FRR) across test classes and data distributions. We define this issue in DML as \textbf{threshold inconsistency}. In real-world applications, such inconsistency often complicates the threshold selection process when deploying %large-scale
commercial image retrieval systems%}
. To measure this inconsistency, we propose a novel variance-based metric called \textbf{O}perating-\textbf{P}oint-\textbf{I}nconsistency-\textbf{S}core (OPIS) that quantifies the variance in the operating characteristics across classes. Using the OPIS metric, we find that achieving high accuracy levels in a DML model does not automatically guarantee threshold consistency. In fact, our investigation reveals a Pareto frontier in the high-accuracy regime, where existing methods to improve accuracy often lead to degradation in threshold consistency. To address this trade-off, we introduce the \textbf{T}hreshold-\textbf{C}onsistent \textbf{M}argin (TCM) loss, a simple yet effective regularization technique that promotes uniformity in representation structures across classes by selectively penalizing hard sample pairs. %Large-scale 
Extensive experiments %} 
demonstrate TCM's effectiveness in enhancing threshold consistency while preserving %or even improving 
accuracy, simplifying the threshold selection process in practical DML settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of threshold inconsistency in deep metric learning (DML) for image retrieval. Existing DML methods often result in uneven representation structures within and between classes, leading to significant variations in performance across different test classes and data distributions, measured by false accept rate (FAR) and false reject rate (FRR). To tackle this issue, the authors propose a novel variance-based metric called Operating-Point-Inconsistency-Score (OPIS) to quantify the inconsistency in threshold performance across classes. They observe a trade-off between accuracy and threshold consistency, where improving accuracy can negatively impact threshold consistency. To mitigate this trade-off, they introduce the Threshold-Consistent Margin (TCM) loss, a simple yet effective regularization technique that penalizes difficult sample pairs to encourage uniform representation structures across classes. Extensive experiments on large-scale datasets demonstrate that TCM enhances threshold consistency while maintaining or even improving accuracy, simplifying the threshold selection process in practical DML applications. The key contributions of the paper include the introduction of the OPIS metric, the identification of the accuracy-threshold consistency trade-off, and the proposal of the TCM loss as a solution to improve threshold consistency in DML. The approach outperforms state-of-the-art methods on various large-scale image retrieval benchmarks, achieving significant improvements in threshold consistency.

### Strengths
1. The proposed Operating-Point-Inconsistency Score (OPIS) and ϵ-OPIS provide valuable insights.
2. The experiments comparing high accuracy with high threshold consistency are objective.
3. The proposed Threshold-Consistent Margin (TCM) loss is relatively simple and easy to understand.
4. The visualization of the TCM effect is interesting.
5. The experiments are comprehensive, with detailed implementation and coverage of mainstream metric learning settings.
6. The ablation experiments are extensive, exploring margin, DML losses, different architectures, and time complexity. They also validate the proposed method against state-of-the-art approaches such as RS.

### Weaknesses
It is meaningful to pull the scores of positive pairs towards a fixed value and the scores of negative pairs towards another fixed value, even though it sounds simple.

Apart from that, I did not see any other weaknesses.

### Questions
1. Since you conducted experiments on the large-scale iNaturalist-2018 dataset, what are the differences between open-set metric learning and face recognition or re-identification (re-ID)? Can your method be applied in the field of face recognition?
2. If your method can use a single model to maintain the same threshold across multiple test sets, would it be meaningful, such as in this work[1].

[1] https://cmp.felk.cvut.cz/univ_emb/

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces and addresses the threshold inconsistency problem in Deep Metric Learning (DML). To tackle this issue, the authors present the Operating-Point-Inconsistency-Score (OPIS) metric, which is based on the variance of utility score derived from the F-score. Additionally, they propose the Threshold-Consistent Margin (TCM) loss, which selectively penalizes hard sample pairs. The experimental results on various deep metric learning benchmarks validate the efficacy of their proposed method.

### Strengths
1.The paper effectively identifies and defines the threshold inconsistency problem within the context of Deep Metric Learning (DML). 

2.To address this issue, the authors introduce a novel loss function, the Threshold-Consistent Margin (TCM) loss. 

3.Their proposed method is rigorously evaluated through comprehensive experiments.

### Weaknesses
1. The use of the term "large-scale" in this paper may be misleading as the experiment datasets do not contain a sufficiently large number of samples to be accurately characterized as "large-scale." Typically, datasets with more than 10 million or 1 billion samples could be considered as large-scale. The iNaturalist-2018 dataset, while larger than CUB or Cars, is still not within the range of datasets like LAION-400M or LAION-5B. The authors should clarify the scale of their experiments and consider removing the term "large-scale" if it does not accurately reflect the dataset sizes.

2. The threshold inconsistency problem, as described in this paper, is also referred to as the generalization problem and has been previously discussed in the deep metric learning (DML) literature [1, 2]. In reference [1], the authors proposed the adoption of a metric variance constraint (MVC) to enhance generalization ability, which is essentially a variance-based metric. Reference [2] provided an in-depth discussion of the generalization problem in DML, particularly focusing on how excessive feature compression can negatively impact generalization. It would be beneficial for this paper to incorporate discussions and comparisons with these existing works in the context of addressing the threshold inconsistency problem, especially since the proposed TCM loss shares similarities with the MVC approach in [1]. The authors should also clarify how their work differs from the generalization problem discussed in [2], especially regarding the relationship between feature compression and generalization.

### Questions
See the weaknesses.

### Soundness
3 good

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
This paper addresses the issue of inconsistency in threshold determination for negative samples in threshold-based image retrieval. The authors propose a new metric called Operating-Point-Inconsistency-Score (OPIS) to measure inconsistency and introduce the Threshold-Consistent Margin (TCM) loss as a regularization technique to enhance consistency. The key contributions include identifying the problem with existing method, introducing an intuitive evaluation metric and regularization approach, and demonstrating improved threshold consistency without sacrificing accuracy in large-scale experiments.

### Strengths
- The paper is well-written, making it easy to understand while offering comprehensive comparisons with current methods.

- It clearly highlights issues in existing models and presents an intuitive metric and regularization technique to tackle them.

- The research goes a step further by demonstrating not just improved threshold consistency but also better performance in several instances.

### Weaknesses
- The most significant concern with this paper is the lack of experimentation in the domain of face verification. While image retrieval often utilizes metrics like mAP or Recall@k, face verification relies heavily on threshold-based evaluations, such as TAR@FAR. The proposed method, with its focus on threshold consistency, appears particularly well-suited for face verification tasks. The absence of experiments in this area raises questions about the practical applicability of the method in a domain where threshold determination is paramount.

- The paper posits that high accuracy does not necessarily imply high threshold consistency. However, in face verification, achieving consistent thresholds often directly contributes to improved accuracy. This discrepancy suggests a potential disconnect between the paper's focus on general image retrieval and the specific requirements of face verification. It would be beneficial to see a more detailed discussion of this relationship, particularly in the context of how threshold consistency impacts accuracy metrics like TAR@FAR in face verification.

- While the paper mentions related works like Liu et al. (2022) and OneFace, it lacks direct experimental comparisons with these methods in the context of face recognition. Given that OneFace specifically addresses threshold consistency, a comparative evaluation is crucial to understand the proposed method's advantages in improving threshold consistency within the face recognition domain. This comparison should include standard face recognition datasets and metrics.

- The paper needs to update the state-of-the-art results presented for the CUB and Cars-196 datasets. Recent work, such as HIER [1], has shown superior performance on these datasets. Incorporating these updated results is necessary for a fair and accurate evaluation of the proposed method's performance relative to the current state-of-the-art.

### Questions
Figure 3 shows ProxyAnchor (ResNet50) with a low threshold consistency. It would be beneficial to compare the improvement in R@K and OPIS when using the proposed method. Ideally, the proposed method should show a significant OPIS improvement compared to others.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
