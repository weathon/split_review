# Understanding and Robustifying Sub-domain Alignment for Domain Adaptation

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
In unsupervised domain adaptation (UDA), aligning source and target domains improves the predictive performance of learned models on the target domain. A common methodological improvement in alignment methods is to divide the domains and align sub-domains instead. These sub-domain-based algorithms have demonstrated great empirical success but lack theoretical support. In this work, we establish a rigorous theoretical understanding of the advantages of these methods that have the potential to enhance their overall impact on the field. Our theory uncovers that sub-domain-based methods optimize an error bound that is at least as strong as non-sub-domain-based error bounds and is empirically verified to be much stronger. Furthermore, our analysis indicates that when the marginal weights of sub-domains shift between source and target tasks, the performance of these methods may be compromised. We therefore implement an algorithm to robustify sub-domain alignment for domain adaptation under sub-domain shift, offering a valuable adaptation strategy for future sub-domain-based methods. Empirical experiments across various benchmarks validate our theoretical insights, prove the necessity for the proposed adaptation strategy, and demonstrate the algorithm's competitiveness in handling label shift.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the understanding and robustifying of the application of sub-domain alignment to unsupervised domain adaptation. To achieve this goal, this paper provides a theoretical foundation for sub-domain alignment methods and an algorithm DARSA to address the shifted marginal sub-domain weights. The experiments show that the proposed method outperforms some previous methods.

### Strengths
(1)This paper is well-written, and it is enjoyable to read.
(2)The proposed algorithm is simple yet effective to some extent.

### Weaknesses
 (1)The theoretical analysis is not instructive. The theoretical analysis has two main theorems, Sub-domain-based Generalization Bound (Theorem 4.5) and Benefits of Sub-domain Alignment (Theorem 4.7 and 4.10). Theorem 4.5 shows that the error of the target domain can be bounded by the weighted error of the source domain and the weighted error of the sub-domain distance. However, some works [1,2] have pointed out similar conclusions. Specifically, the bound in Theorem 4.5, while incorporating sub-domain weighting, does not offer a significantly novel perspective compared to existing domain adaptation bounds. The connection between the proposed bound and practical improvements in sub-domain alignment is not clearly established. Theorem 4.10 shows that the error bound of Theorem 4.5 is at least as strong as the full domain generalization bound without the sub-domain information. However, the authors may overlook the finiteness of real datasets, which is also important for reliable generalization bound and thus may lead to a different conclusion. Considering that the sub-domains have fewer samples than the whole domain, the finiteness improves more value of the sub-domain generalization bound than the whole-domain generalization bound. The analysis does not adequately address the impact of reduced sample sizes within sub-domains on the tightness and reliability of the derived bounds, potentially leading to over-optimistic conclusions about the benefits of sub-domain alignment.
(2)Although the paper is based on previous sub-domain alignment works, the previous works are not well connected in theoretical analysis, algorithm, or experiments. The author should give some examples of how the work enhances the understanding and robustifying of previous methods. The paper lacks a clear explanation of how the proposed theoretical framework and algorithm specifically build upon and improve existing sub-domain alignment techniques. The theoretical analysis does not explicitly address the limitations of previous sub-domain methods, making it difficult to assess the novelty and impact of the proposed approach. The experimental section does not include a detailed comparison with previous methods, making it hard to understand the practical advantages of the proposed method.
(3)The experiments are not sufficient to show the effectiveness of the proposed algorithm. First, the number of datasets used for the experiments is too small. Second, the compared methods are not advanced enough. The experimental evaluation is limited in scope, failing to demonstrate the generalizability of the proposed algorithm across a diverse range of datasets. The choice of baseline methods does not include state-of-the-art domain adaptation techniques, making it difficult to assess the competitiveness of the proposed approach.

### Questions
As the weakness above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper first presents a theoretical analysis to establish that the sub-domain based methods are in fact optimizing a generalization bound that is at least as strong as the full-domain-based objective functions. Besides, the paper presents a UDA algorithm, Domain Adaptation via Rebalanced Sub-domain Alignment (DARSA), which addresses the case when marginal subdomain weights shift. DARSA optimizes reweighted classification error and discrepancy between sub-domains of the source and target task.

### Strengths
(1) This work provides a theoretical foundation for subdomain-based methods in domain adaptation, addressing their previous lack of rigorous understanding.
(2) The authors design a DARSA model, aiming to address shifted marginal sub-domain weights, which adversely impact existing sub-domain based methods.
(3) The experimental results on different benchmarks show the effectiveness of the proposed framework over other existing UDA methods.

### Weaknesses
 (1) Most of the compared UDA methods were published before 2020. To fully validate the superiority of the proposed DARSA model, more SOTA UDA methods should be included in comparison experiments. 

 (2) More insightful analyses should be provided. For example, the visualization of the subdomain rebalancing weights should be shown. 

 (3) The current experiments are conducted on two datasets, which is not sufficient. It is recommended to conduct on large-scale datasets.

### Questions
(1) Most of the compared UDA methods were published before 2020. To fully validate the superiority of the proposed DARSA model, more SOTA UDA methods should be included in comparison experiments. 

(2) More insightful analyses should be provided. For example, the visualization of the subdomain rebalancing weights should be shown. 

(3) The current experiments are conducted on two datasets, which is not sufficient. It is recommended to conduct on large-scale datasets.

### Soundness
2 fair

### Presentation
3 good

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
This paper establishes a theoretical foundation for sub-domain alignment in domain adaptation. Under certain plausible assumptions, they demonstrate that this bound is as tight, if not tighter, than those of full-domain alignment approaches. Drawing from this theorem, they introduce the Domain Adaptation via Rebalanced Sub-domain Alignment (DARSA) to address the challenge of marginal sub-domain weight shifts. Empirical evidence shows that their method, with sub-domains based on class labels, outperforms other leading domain adaptation methods in label shift scenarios.

### Strengths
1. The theoretical analysis regarding the sub-domain alignment is thorough and insightful. The method proposed is clearly grounded in this theory. While I haven't delved into every detail of the derivation, the conclusions seem sound.
2. The paper is well-structured and reader-friendly.
3. The effectiveness of their approach, when segmenting by class to form subdomains, is confirmed by results on both Digits and TST for the label shift scenario.

### Weaknesses
1. While the theory behind sub-domain alignment is certainly compelling, in its practical application, it merely utilizes class labels to segment subdomains. This results in a method that essentially merges class importance weighting with W1 distance to gauge domain discrepancies. While this is a fresh approach, it's not exceptionally innovative. It would enhance the paper if the author explored alternative sub-domain segmentation techniques.

2. It would enrich the study if the author included baselines that are specifically designed for label shift scenarios, like the method outlined in [1]. Many of their referenced baselines, such as DANN and ADDA, are primarily constructed for the covariate shift setting.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
