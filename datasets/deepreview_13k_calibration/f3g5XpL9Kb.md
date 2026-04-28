# LiDAR: Sensing Linear Probing Performance in Joint Embedding SSL Architectures

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Joint embedding (JE) architectures have emerged as a promising avenue for acquiring transferable data representations. A key obstacle to using JE methods, however, is the inherent challenge of evaluating learned representations without access to a downstream task, and an annotated dataset. Without efficient and reliable evaluation, it is difficult to iterate on architectural and training choices for JE methods. In this paper, we introduce \emph{LiDAR} (\textbf{Linear Discriminant Analysis Rank}), a metric designed to measure the quality of representations within JE architectures. Our metric addresses several shortcomings of recent approaches based on feature covariance rank by discriminating between informative and uninformative features. In essence, \emph{LiDAR} quantifies the rank of the Linear Discriminant Analysis (LDA) matrix associated with the surrogate SSL task—a measure that intuitively captures the information content as it pertains to solving the SSL task. We empirically demonstrate that \emph{LiDAR} significantly surpasses naive rank based approaches in its predictive power of optimal hyperparameters.
Our proposed criterion presents a more robust and intuitive means of assessing the quality of representations within JE architectures, which we hope facilitates broader adoption of these powerful techniques in various domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper proposes a new metric for the measurement of the representation quality within joint embedding architectures, which is called Linear Discriminat Analysis Rank.
This metric discriminate between informative and uninformative features by quantifying the rank of the Linear Discriminant Analysis matrix.
The experiments on several downstream tasks show the proposed metric improves the performance.

### Strengths
1. The paper generally explain their motivation and inspiration clearly.
2. The experiments are sufficient to show the effectiveness of the proposed method on the downstream tasks.
3. The supplementary material shows the details of the proposed method.

### Weaknesses
1. The abbreviation of the proposed method "LiDAR" is irrelavent of the problem it tries to solve. The irrelavent abbreviation misleads the readers what the paper want to express. Some readers may think the paper is on the lidar.

2. Some typos:

a. In section 2.1: In practice, a set of downstream tasks {T_j} are used to asses ->  In practice, a set of downstream tasks {T_j} are used to assess

b. in Section 4.0.1: There is a blank line, where a sentance seem missed.

### Questions
Actually, I have no background of the topics of the paper. I cannot assess and ask any questions on this paper. I do not know why this paper is assigned to me. I think the reason maybe the abbreviation of the proposed method "LiDAR" is related with my previous paper, however, this paper is not related with lidar at all.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present LiDAR, a new metric designed to assess the quality of self-supervised representations in Joint Embedding (JE) architectures using the linear probing protocol, without requiring labeled downstream tasks. LiDAR employs Linear Discriminant Analysis (LDA) to evaluate dimensional collapse and implicitly integrates the SSL objective. Through thorough empirical validation, the authors demonstrate LiDAR's superiority over existing metrics in predicting optimal hyperparameters.

### Strengths
1) The addressed problem holds significance in self-supervised learning. By evaluating SSL representations without labeled tasks, improvements in hyperparameter selection and algorithm development are facilitated.

2) Utilizing Linear Discriminant Analysis (LDA) to assess the dimensionality collapse of SSL representations is both theoretically grounded and considerably novel. While RankMe assessed SSL methods via the effective rank of the covariance matrix (related to PCA), LiDAR focuses on the rank of the scatter-ratio matrix through LDA.

3) Detailed experiments highlight a significant and consistent positive correlation (measured by Spearman and Kendall coefficients) between LiDAR and linear probing performance on the same source-target datasets, surpassing RankMe across most settings.

### Weaknesses
1) The manuscript lacks evaluation on out-of-distribution (OOD) target datasets. Although the ImageNet dataset results are promising, the evidence for LiDAR's effectiveness in more realistic downstream tasks, often involving OOD datasets, is missing. Comparing with datasets like iNaturalist-2018 or Stanford Cars, following the protocol in RankMe, would strengthen LiDAR's position as a useful proxy metric. Specifically, the absence of evaluations on datasets with different image characteristics and class distributions limits the generalizability of the findings. The paper should include a more diverse set of OOD benchmarks to thoroughly validate the proposed metric.

2) LiDAR introduces two hyperparameters: the number of surrogate classes (n) and the number of samples per class (q). Yet, the manuscript does not provide guidance on determining these values. Given that these values differ across methods, a hyperparameter sensitivity analysis seems essential. The lack of a principled approach for setting n and q introduces a potential source of variability and makes it difficult to apply LiDAR consistently across different architectures and datasets. A detailed ablation study is needed to understand the impact of these hyperparameters on the metric's performance.

3) The comparative analysis appears limited, with LiDAR mainly being evaluated against RankMe. Other potential baselines, like $\alpha$-ReQ mentioned in related work, are overlooked. The absence of comparisons with other established representation quality metrics makes it difficult to assess the relative strengths and weaknesses of LiDAR. A more comprehensive comparison with a wider range of baselines is needed to establish LiDAR's superiority.

4) In Section 4.1, the authors advocate for dimensionality reduction (DR) of embedding features, possibly adding another layer of dependency for LiDAR evaluation. The necessity of DR for LiDAR's effective application, and any specific DR algorithms used in experiments, remain ambiguous. The lack of clarity on the role of DR raises concerns about the practical applicability and potential computational overhead of LiDAR. The authors should clarify the conditions under which DR is needed and specify the DR algorithms used in their experiments.

5) Although the authors claim LiDAR integrates the SSL objective, the manuscript does not delve into the relationship between LiDAR and different SSL losses. The lack of a theoretical connection between LiDAR and the SSL objective limits the understanding of why LiDAR works and how it relates to the underlying learning process. A more in-depth analysis of this relationship would strengthen the theoretical foundation of the proposed metric.

### Questions
1) Scatter matrices, $\Sigma_w$ and $\Sigma_b$, having dimensions ( p $\times$ p ), are influenced by both n and the data dimensionality (p). In Section 4.1, the authors note they "maintain a total of 50 features" for VICreg. How does this align with rank constraints dictated by the data dimensionality?

2) What guidance can be provided for practitioners to select appropriate values for the number of surrogate classes (n) and the number of samples per class (q)?

3) The authors re-implemented RankMe (without data augmentation) for new architectures, namely I-JEPA and data2vec, using 10k images for rank estimation. This contrasts with the originally suggested 25.6k images. Meanwhile, LiDAR employs at least 50k total samples. What motivated this choice?

The rebuttal addressed the raised issues well. Therefore, I updated the review.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces LiDAR (Linear Discriminant Analysis Rank) as a novel  metric for assessing the quality of representations within joint embedding (JE) architectures. The authors conduct comprehensive experiments and demonstrate that their proposed LiDAR metric correlates significantly and consistently higher with downstream linear probing performance than RankMe. They further show that LiDAR demonstrates consistently strong performance in hyperparameter selection, outperforming RankMe.

### Strengths
- The proposed LiDAR metric for accessing the quality of representations within joint embedding (JE) architectures sounds novel.
- The theoretical motivation for proposing the LiDAR metric is clear and logical.
- Comprehensive experiments have been carried out to demonstrate the superiority of LiDAR over RankMe.
- The paper is clear and easy to follow.

### Weaknesses
 - No disucssions on computational overhead and runtime.

### Questions
None.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
