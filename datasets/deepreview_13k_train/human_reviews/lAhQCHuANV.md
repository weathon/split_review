# Assessing Uncertainty in Similarity Scoring: Performance & Fairness in Face Recognition

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
The ROC curve is the major tool for assessing not only the performance but also the fairness properties of a similarity scoring function. In order to draw reliable conclusions based on empirical ROC analysis, accurately evaluating the uncertainty level related to statistical versions of the ROC curves of interest is absolutely necessary, especially for applications with considerable societal impact such as Face Recognition.  In this article, we prove asymptotic guarantees for empirical ROC curves of similarity functions as well as for by-product metrics useful to assess fairness. We also explain that, because the false acceptance/rejection rates are of the form of U-statistics in the case of similarity scoring, the naive bootstrap approach 
may 
jeopardize the assessment procedure. A dedicated recentering technique must be used instead. Beyond the theoretical analysis carried out, various experiments using real face image datasets provide strong empirical evidence of the practical relevance of the methods promoted here, when applied to several ROC-based measures such as popular fairness metrics.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces introduces a method to quantify the uncertainty of similarity ROC curves in order to make meaningful comparison between different FR models. A naive bootstrap procedure tends to underestimate the ROC curve. Thus, a recentering technique is proposed so that a scalar uncertainty measure for ROC and fairness metrics is defined. With the statistical analysis and numerical experiments, a discussion about the practical use of the uncertainty value is done to achieve more reliable decisions related to accuracy and fairness.

### Strengths
+ The problem to measure the uncertainty in FR similarity function is well motivated. While ROC curve has become the standard to compare face recognition models, inconsistent comparison might occur due to the differences in evaluation dataset. The proposed method is able to build the confidence bands around the performance/fairness metrics by incorporating the uncertainty measures.

+ The recentering bootstrap technique refines the naive bootstrap that tends to underestimate the empirical FRR as shown in Figure 3. 

+ The numerical experiments in face recognition problem is done to discuss how the proposed uncertainty metric and confidence band around ROC curve can be used in real-application. If the upper bound of the confidence band is lower, then the empirical fairness is better.  The differences between upper bound and lower bound of the confidence means that the uncertainty is high, thus it is better to choose a method that has small difference especially in the case where a strict fairness constraint is needed.

+ Multiple fairness metric has been evaluated using multiple FR methods. It is shown the max geomean metric has the lowest uncertainty in terms of FAR and FRR.

### Weaknesses
 - There is a lack of justification of why Adacos has lower uncertainty than Arcrface in fairness metric. To fairly compare the performance of Adacos and Arcface, training those methods on Fair Face Recognition dataset [A] might help to justify the performance better. Note that there are multiple FR methods [B,C] that focus on solving fairness problem in face recognition. Comparison with those methods might be useful to justify the proposed metric.

- Instead of the background and preliminaries, it is more important to include more comparison of fairness metrics with various FR methods in the supplementary material in the main manuscript. As the paper focuses on the application of fair recognition technology, it is important to add more justification on the corresponding problem.

### Questions
* In Figure 4, the $FRR^{max}_{min}$ is used as the fairness metric, why don't the authors use the best fairness metrics in Figure 5 (max-geomean)? It could lead to more consistent analysis.
* Why do the authors not evaluate the method in the fair face recognition dataset?
* Does the training dataset affect the uncertainty of the face recognition methods?

### Soundness
4 excellent

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
This paper focuses on the uncertainty of ROC curve in Face Recognition applications based on similarity scoring. It first proves asymptotic consistency guarantees for empirical ROC curves of similarity functions, which is the theoretical basis of the methodology of building confidence bands for ROC. Then, it provides recentering technique to counteract the underestimation of the similarity ROC curve caused by naïve bootstrap. Resulting from this bootstrap variant, the confidence bands and uncertainty measures for the ROC are defined and shown to be consistent. Finally, the results of various experiments using real face image datasets are illustrated to discuss the practical relevance of the proposed methods.

### Strengths
1. In some cases, the simple ROC curve is not enough to compare the performance of different FC models, and the idea of introducing uncertainty into the evaluation metric fills this gap and is relatively practical. 
2. The proposed method for estimating the confidence intervals and uncertainty of ROC is intuitive and simple, and can be easily applied directly to various Face Recognition models.

### Weaknesses
1. This paper is not the first to apply the bootstrap method to ROC curves and there isn’t enough difference between it and Bertail’s work proposed in 2008. The concept of uncertainty proposed in this paper in relatively new in the field of ROC curve estimation, but it is too simplistic in the field if uncertainty estimation, which needs deeper elaboration. The bootstrap method, while useful, requires careful consideration of the data's underlying structure, and the paper does not adequately address the potential for bias introduced by the pairwise nature of face recognition data. Specifically, the dependence between similarity scores within pairs, and across different pairs, is not sufficiently accounted for, potentially leading to inaccurate uncertainty estimates. The paper should provide a more thorough discussion of the assumptions underlying the bootstrap procedure and how these assumptions are met (or not) in the context of face recognition. Furthermore, the notion of uncertainty is not fully explored, particularly in comparison to other methods for quantifying uncertainty in statistical inference; a deeper dive into this aspect would be beneficial.
2. The experiments demonstrates the scenarios and ways in which the method proposed in this paper can be applied, but it is not sufficient to illustrate its effectiveness, and there is a lack of experimental evidence that the proposed uncertainty is a better evaluation metric to compare the performance and fairness of Face Recognition models. Besides, there is no comparison of the proposed method with other methodologies. The experimental section lacks a rigorous evaluation of the proposed uncertainty measure. While the paper demonstrates the application of the method, it does not provide sufficient evidence that the uncertainty measure is a better metric for comparing face recognition models. The paper should include experiments that directly compare the proposed uncertainty measure with other existing methods, demonstrating its advantages and disadvantages. Additionally, the paper should provide a more thorough analysis of the practical implications of the uncertainty measure, such as how it can be used to make informed decisions about model selection and deployment. The absence of a comparative analysis with other methodologies is a significant weakness, as it makes it difficult to assess the relative merits of the proposed approach.

### Questions
1. This paper is not the first to apply the bootstrap method to ROC curves and there isn’t enough difference between it and Bertail’s work proposed in 2008. The concept of uncertainty proposed in this paper in relatively new in the field of ROC curve estimation, but it is too simplistic in the field if uncertainty estimation, which needs deeper elaboration.
2. The experiments demonstrates the scenarios and ways in which the method proposed in this paper can be applied, but it is not sufficient to illustrate its effectiveness, and there is a lack of experimental evidence that the proposed uncertainty is a better evaluation metric to compare the performance and fairness of Face Recognition models. Besides, there is no comparison of the proposed method with other methodologies.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for evaluating uncertainty on the ROC curve in face recognition problem.

### Strengths
The paper provides a theoretical analysis of the properties and uncertainties associated with the ROC curve in face recognition evaluations and introduces a novel method for quantifying this uncertainty.

### Weaknesses
1. This paper dedicates excessive length and involves many complex formulas to introduce some basic knowledge of face recognition evaluation, which seems unnecessary.
2. While fairness in face recognition is a pressing issue, the contributions of this paper appear limited. As the authors themselves note, typically, global ROC curves and their comparisons with specific attribute-driven ROC curves would suffice for the uncertainty analysis in most face recognition scenarios.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
