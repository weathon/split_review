# How Does Unlabeled Data Provably Help Out-of-Distribution Detection?

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Using unlabeled data to regularize the machine learning models has demonstrated promise for improving safety and reliability in detecting out-of-distribution (OOD) data. Harnessing the power of unlabeled \textcolor{black}{in-the-wild} data is non-trivial due to the heterogeneity of both in-distribution (ID) and OOD data. This lack of a clean set of OOD samples poses significant challenges in learning an optimal OOD classifier. Currently, there is a lack of research on formally understanding how unlabeled data helps OOD detection. 
 This paper bridges the gap by introducing a new learning framework \model (\textbf{S}eparate
\textbf{A}nd \textbf{L}earn) that offers both strong theoretical guarantees and empirical effectiveness. The framework separates candidate outliers from the unlabeled data and then trains an OOD classifier using the candidate outliers and the labeled ID data. Theoretically, we provide rigorous error bounds from the lens of separability and
learnability, formally justifying the two components in our algorithm.  Our theory shows that \model can separate the candidate outliers with small error rates, which leads to a generalization guarantee for the learned OOD classifier.  Empirically, \model achieves state-of-the-art performance on common benchmarks, reinforcing our theoretical insights.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel framework for Out-Of-Distribution (OOD) detection, named SAL, which aims to improve machine learning models through regularization using unlabeled data. SAL comprises two main components: (1) Filtering–distinguishing potential outliers from the general dataset, and (2) Classification utilizing the identified candidate outliers to train an OOD classifier. The paper includes pertinent theoretical proofs to substantiate the proposed method, and experimental results are provided to demonstrate its effectiveness.

### Strengths
1 SAL’s methodology is structured around two distinct phases—screening and classification—which can be independently optimized, offering enhanced flexibility.
2 Utilizing a Large Volume of Unlabeled Data: SAL effectively leverages substantial amounts of unlabeled data to extract valuable information, thereby bolstering its detection capabilities.
3 Theoretical Support: Beyond its impressive empirical performance, SAL is underpinned by robust theoretical foundations.

### Weaknesses
1 In scenarios where the actual OOD data markedly diverges from the outliers present in the unlabeled dataset, there arises a question regarding the preservation of SAL’s performance.
 2 The efficacy of SAL is significantly influenced by the quality of the unlabeled data employed, indicating a substantial dependence on data integrity.

### Questions
1 Could you design experiments to further confirm and answer issues in weaknesses?
2 In table 1, how can this discrepancy be accounted for in datasets or scenarios that perform well in other methods but have degraded performance (ID ACC) in SAL?

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel setting for OOD detection, termed as ”wild OOD detection,” building upon the foundation established by the preceding work ”Training OOD Detectors in their Natural Habitats.” A novel methodology, denoted as SAL, is presented, encapsulating at wo-stage process comprising filtering and classification components. Empirical evaluations have demonstrated that SAL achieves SOTA performance, boasting substantial improvements over existing methods. Additionally, theoretical underpinnings are provided to bolster the credibility and effectiveness of SAL.

### Strengths
1. A theory has been established to investigate aspects of separability and learnability. This contribution is both novel and significant. 

2. Experimental evaluations conducted on standard benchmarks demonstrate that SAL achieves SOTA performance. 

3. A novel method grounded in theory has been developed to advance safe machine learning practices. Theory serves as a crucial driver in this endeavour. I am very happy to see the novel work on provable OOD detection.

### Weaknesses
1. Could you provide explanations or conduct experiments to elucidate the factors contributing to the decreased ID accuracy depicted in Table 1? 

2. Why is pi set to 0.1 in most experiments? Could you conduct additional experiments to investigate whether pi remains robust across a range of values? Furthermore, does the performance of pi align with theoretical predictions? 

3. It appears that the top singular vector is crucial for SAL. Have you conducted any experiments to demonstrate the performance when considering the top 2, top 3, ..., top k singular vectors?

4. What would occur if you were to use the gradient norm in place of the top singular vector? Could you elucidate the rationale behind opting for the top singular vector instead of the norm?

### Questions
Please refer to the Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Leveraging unlabeled data has shown potential in enhancing the safety and reliability of machine learning models for out-of-distribution (OOD) detection, despite the challenges posed by the heterogeneity of both in-distribution (ID) and OOD data. This paper introduces SAL (Separate And Learn), a novel learning framework that addresses the existing gap in understanding how unlabeled data aids OOD detection by providing strong theoretical guarantees and empirical effectiveness. SAL operates by isolating potential outliers from the unlabeled data, training an OOD classifier with these outliers and labeled ID data, and achieving state-of-the-art performance on standard benchmarks, thereby validating the theoretical framework and its components.

### Strengths
1. The manuscript presents some theoretical analyses as well as a number of intriguing illustrations.
2. The experimental results look promising, with comparisons made against numerous baseline methods.

### Weaknesses
1. The manuscript lacks crucial baselines, such as [1] and [2], which are essential for a comprehensive evaluation, and fails to provide an analysis or comparison with them. The absence of these comparisons makes it difficult to assess the true novelty and performance gains of the proposed method, especially considering that these methods also leverage unlabeled data for OOD detection. Specifically, the STEP method [1] addresses OOD detection with limited labeled data, a scenario that is relevant to the proposed method. Similarly, the TSL method [2] uses topological learning for weakly supervised OOD detection, which is also closely related to the problem setting of this paper.
2. The essential topic of the article is weakly supervised out-of-distribution detection, although it is described from different perspectives. The paper does not explicitly acknowledge or discuss the connection to the existing literature on weakly supervised OOD detection, which could provide a more comprehensive understanding of the proposed method's contribution and limitations. This lack of connection to the broader field makes it difficult to position the work within the existing body of knowledge.

### Questions
1. Near OOD Scenario: It is unclear how effective the method presented in this article would be in a near OOD scenario, such as treating the first 50 classes of CIFAR-100 as ID and the last 50 classes as OOD. This specific situation could pose challenges since near OOD samples may share similarities with the ID data, potentially affecting the method's performance.
2. Generalization Performance Across Different Backbones: The article does not provide information on how well the method generalizes when different backbone architectures are used. The performance stability of the method when transitioning between various model architectures is a critical aspect to consider for its widespread applicability.
3. Generalization Performance on unseen OOD data: There is no discussion on the method's effectiveness when the test OOD data and the OOD data in the unlabeled set are not identically distributed. Understanding how the method handles such disparities is crucial for evaluating its robustness in real-world scenarios.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study addresses wild Out-Of Distribution (OOD) detection, benefiting from the availability of more unlabeled data to enhance OOD data identification. The paper proposes the utilization of the top singular value as a criterion to differentiate between In-Distribution (ID) and OOD samples. The authors, grounded in novel theoretical insights, posit that ID samples should exhibit larger top singular values compared to OOD samples. Both experimental results and theoretical analyses corroborate the effectiveness of the proposed method, Separate And Learn (SAL). Overall, this work stands out for its solid foundation.

### Strengths
- Using gradients to make distinctions is a common and intuitive approach that makes sense to me. How ever, the method of distinguishing based on the top singular value is both intriguing and non-obvious. This innovative discovery holds significant importance for OOD detection.

- The availability of extra unlabeled data undoubtedly enables wild OOD detection to outperform traditional OOD detection, which does not utilize unlabeled data. However, what I find astonishing is that the performance of wild OOD detection surpasses even that of outlier exposure, showcasing its remarkable effectiveness.

- The method is supported by a theoretical examination of its generalization bounds, ensuring a solid foundation for reliable ML.

### Weaknesses
 - One of my major concerns with the paper lies in the discrepancy assumption stated in Theorem 1. To validate this, additional experiments with diverse datasets are imperative to ascertain whether the assumption is consistently met in practical scenarios. While I acknowledge that assumptions are essential for theoretical foundations, and the experiments in Appendix F provide a good start, they are insufficient for a comprehensive evaluation. I recommend extending the empirical analysis to additional datasets (e.g., CIFAR-10 as ID and another data as OOD), with the goal of thoroughly investigating the generality of the assumption and its ability to underpin SAL robustly.

- In the majority of the experiments conducted, the value of pi is set to 0.1. To ensure a comprehensive evaluation, it is crucial to conduct additional experiments with varied values of pi.

### Questions
Please address the issues outlined in the weaknesses. This work is solid and good. So addressing all of my concerns comprehensively will lead me to reconsider and potentially raise my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
