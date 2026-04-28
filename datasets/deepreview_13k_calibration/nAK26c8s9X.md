# Boosting Membership Inference Attacks with Upstream Modification

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Membership Inference Attacks (MIAs) can be used by model owners to identify privacy leakage of specific points in their machine learning models. In this setting, the model owner (who is playing the role of the attacker) has perfect knowledge of the training data but a limited computational budget. However, current MIAs have limited effectiveness in this scenario: 1) They perform poorly against the most vulnerable points 2) They require training too many models. To overcome this weakness, we modify two limitations, in the initial/upstream stages of the MIA framework, namely sampling bias (i.e., too many points dropped during sampling) and attack aggregation (i.e., average attack results over all the data points instead of only the most vulnerable ones). Our improvements carryover downstream and boost attack accuracy of existing MIAs by \textit{increasing the TPR of existing attacks at incredibly low FPRs (as low as zero) while achieving a near-perfect AUC}. As a consequence, our modifications enable the practical and effective application of MIAs for identification of data-leakage in machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses an important limitation in Membership Inference Attacks (MIAs), i.e., their true positive rate is extremely low under strict false positive constraints, often nearing random guessing. The authors enhance MIA performance by addressing sampling bias and refining attack aggregation methods, resulting in improved true positive rates (TPR) even at very low false positive rates (FPRs). Their approach achieves near-zero FPR while delivering a near-perfect Area Under the Curve (AUC).

### Strengths
1. The paper’s findings on the relationship between dropout rate and true positive rate are intriguing. The discovery that the shadow model should approach the leave-one-out ideal state is meaningful.
2. The experimental results are impressive, which demonstrates a substantial boost in AUC. 
3. The paper is well-structured, making complex concepts accessible and easy to follow.

### Weaknesses
1. The novelty of the work is unclear. Privacy research on outliers has been extensively explored, as in the paper “Membership Inference Attacks from First Principles”.  If the approach primarily involves filtering these samples, the novelty seems incremental.
2. The description of settings for the shadow model pool and the victim model’s training data is unclear, such as the training data size, pool size, etc. Besides, it would be helpful to include some ablation studies on these settings.
3. It’s debatable of one of this paper’s argument, which believes that evaluating the average attack accuracy over the entire dataset is a flaw. It appears more as an evaluation of certain MIA performance. Thus, the second claimed contribution may just reflect an alternative display of attack results, rather than a true improvement. This raises questions about the paper’s contribution.
4. One of the optimizations is the reduction in partitions, but it’s unclear from the experiments where this is applied or how this benefit can be quantified.
5. Presentation issues: The appendix presentation is somewhat rough, with figures lacking captions and Table 4 missing all borders.

### Questions
1. Taking the LiRA method as an example, if the dropout rate is reduced to 10%, would this imply that, for a single data point, it is labeled as membership much more often than non-membership? Could you explain in detail how this method affects the number of positive and negative samples and the impact of these sample counts on true positive and false positive rates?
2. Could the proposed method be limited by a strong dependency between the training dataset sampling size and the pool used for the shadow model? For instance, if the training dataset contains 10,000 samples but the pool has 50,000, would the observation about the relationship between dropout rate and AUC still hold?
3. It’s unclear how the experiments specifically support the claim that your method reduces the number of partitions. Could you provide more explicit experimental evidence demonstrating this advantage?

### Soundness
3

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
The paper investigates the problem of improving the evaluated performance (including accuracy and TPR at fixed FPR) of membership inference attacks, via (1) increasing the member/non-member ratio in sampling the training dataset for the target model; and (2) only performing membership inference attack on a subset of selected outlier data records (instead of the whole training dataset). Extensive experiments on CIFAR-10, CIFAR-100, and Tiny-Imagenet datasets show the effectiveness of the proposed method in improving the evaluated performance of MIAs, across various attack strategies.

### Strengths
1. Interesting experimental investigations of how to increase the member/non-member ratio and subselect the most vulnerable data records to improve the evaluated performance of membership inference attacks.
2. Novel experimental observations that certain outlier detection methods (such as ApB) could effectively identify data records with high information leakage.

### Weaknesses
Under the modified data sampling and selection schemes, the paper lacks discussions regarding why the evaluated MIA performance remains meaningful and comparable with prior works. See questions for details.



### Questions
1. Could the authors provide the exact equations for computing the MIA performance (accuracy, TPR, FPR, and AUC) under the modified data sampling/selection schemes? Specifically, how many member/non-member instances are there? 

2. Is the TPR in Table 3 computed over the entire training dataset, or the TPR is only averaged over the subset of vulnerable data records selected by the outlier detection method? If it is the former, then a naive strategy that always guesses `member` for non-outlier records and guesses `non-member` for outlier records could achieve a 0.95 TPR at zero FPR (because the selected outlier records consist of 5% of the total data). 

3. Could the authors comment on the significance of the evaluated MIA performance under modified data sampling/selection schemes? Given examples as mentioned in question 2, it may not be fair to directly compare the performance under different data sampling/selection schemes. It would help clarify if the authors relate the evaluated performance to the same quantity (e.g., DP lower bound) to understand the fair improvement compared to prior works.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper identifies two limitations in previous membership inference attacks: excessive data point exclusion during sampling and the evaluation of attack performance across all data points rather than focusing solely on the most vulnerable ones. The author argues that reducing the drop rate during dataset partitioning and applying membership inference attacks only to outliers can significantly improve the attack success rate at low false positive rates.

### Strengths
- The paper benchmarks its proposed approach against state-of-the-art methods using various datasets.

### Weaknesses
 - The paper demonstrates a misunderstanding of membership inference attack objectives and threat models, leading to flawed assumptions and analyses. First, the authors argue that one primary limitation is sampling bias due to excessive data dropping during partitioning. However, this contradicts the approach taken in leading studies (e.g., Zarifzadeh et al., 2024; Carlini et al., 2022), which suggests that data partitioning for reference model training should be unbiased. These works typically recommend a balanced dropout rate of 50%, where each sample $x$ is present in half the reference models (IN models) and excluded from the other half (OUT models). The authors’ observation of increased success rates at lower dropout rates likely arises from impractical assumptions. Since this paper follows the experimental protocols of previous works, where they use the entire dataset for partitioning (Carlini et al., 2022), each example $x$ is included in exactly half the shadow models’ training sets. In this case, **the training sets of individual shadow models and the target model may partially overlap**. This overlap increases as the dropout rate decreases, leading to artificially inflated success rates since shadow models may inadvertently use data closer to the target model’s dataset. In practical applications, such extensive overlap between shadow and target datasets is improbable, especially with larger overlaps, making the paper’s claims less meaningful.

- In the section limitation, the author suggests that limiting MIA to outliers can significantly improve attack success. However, this claim reflects a fundamental misunderstanding of MIA’s objectives. MIA aims to quantify privacy leakage or perform data auditing under regulations (e.g., GDPR) to determine if specific data resides within the original training model. In practice, the data points for MIA evaluations are typically predetermined, meaning we cannot selectively choose only the most vulnerable ones. Although certain data points may indeed be more susceptible to attacks, **MIA’s goal is to examine privacy leakage across all available training data, regardless of vulnerability, to yield an accurate picture of the model’s privacy risk**. Additionally, the paper's claim that recent work advocates evaluating only the most vulnerable points is incorrect. Recent studies emphasize improving evaluation metrics, specifically achieving a low false positive rate (FPR), rather than focusing on selective evaluation targets.

- Given the above analysis, it is unsurprising that this paper’s evaluation results outperform existing baselines, as the methodology is based on unrealistic threat models. The extensive overlap between shadow and target datasets, combined with evaluation focused solely on highly vulnerable points, leads to overly optimistic results that are unlikely to translate to practical scenarios.

- Minor issues. The citation style should be corrected. Use \citet{} when the author(s) names are part of the sentence and \citep{} when the entire citation is parenthetical.

### Questions
Please see my previous comments.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates and proposes improvements to the membership inference attack (MIA) framework used to assess privacy risks in machine learning models. The authors identify two main limitations in current MIAs: sampling bias and attack aggregation. They show that a high data drop rate in sampling introduces bias and that averaging attack accuracy across all data points dilutes the impact of outliers, which are often more vulnerable to MIAs. Based on this finding, they propose creating data partitions not from the entire dataset but solely from the most vulnerable points selected through outlier detection methods. Extensive evaluations demonstrate that their approach improves the true positive rate (TPR) while reducing the false positive rate (FPR), thereby enhancing the effectiveness of MIAs in privacy assessment.

### Strengths
- This paper addresses limitations in MIA processes, which is crucial for improving privacy assessments as machine learning models continue to grow in complexity and application.
- This paper thoroughly evaluates challenges, such as sampling bias and attack aggregation, demonstrating that upstream modifications can yield significant improvements in MIA effectiveness across various datasets.
- The proposed approach, particularly the focus on outlier detection for data partitioning, leads to notable increases in true positive rates while maintaining low false positive rates, outperforming traditional MIA techniques.

### Weaknesses
 - This paper lacks an in-depth exploration of the feasibility of the proposed improvement strategy. Although experiments indicate that as the drop rate decreases, the attack success rate increases, the paper does not clarify the relationship between a low drop rate and the selection of the most vulnerable samples. Furthermore, it does not clearly explain why MIAs should focus exclusively on the most vulnerable samples(outliers). The justification for focusing solely on outliers is not sufficiently addressed from an attacker's perspective; if the method only targets a small subset of vulnerable samples, the trade-off between focusing on these samples and assessing overall privacy leakage remains unclear. Providing MIA performance on non-outlier samples would help clarify this point.
- While the paper’s modifications achieve improved performance at low false positive rates, a comparison with defense mechanisms (such as differential privacy) under similar FPR conditions would make the findings more actionable. Assessing whether the method still improves MIA accuracy when applied to models with built-in defenses could demonstrate its real-world applicability for assessing privacy risks. The paper also needs to address the robustness of the outlier detection method. For instance, would the effectiveness of the method be affected in scenarios where the target model's data distribution changes or when data augmentation techniques are applied?
- The experimental setup lacks a detailed description of the target model, evaluation metrics, and the baseline method (RMIA and LiRA) implementation. More experimental details are also needed. The paper provides only a brief description of model selection and parameter settings on CIFAR-10 in Section 3.1, without detailing the experimental setup on other datasets. This lack of detail makes it difficult to assess the generalizability of the findings. Specifically, the paper should clarify the exact architecture of the ResNet-18 model, the specific loss function used, and the optimization algorithm, including the learning rate schedule and batch size. Furthermore, the implementation details of the baseline methods (RMIA and LiRA) are not provided, making it difficult to reproduce the results.
- Code is not released for reproducibility.

### Questions
Q1: The paper proposes a partitioning strategy based on outlier detection. Does this approach impact membership inference attack results for inliers?

Q2: Does the proposed improvement strategy rely entirely on the accuracy of the chosen outlier detection method, ApB? How should the approach handle data points that are missed or incorrectly identified by the detection method?

Q3: One motivation for the modified partitioning strategy is to reduce the computational budget, but it remains unclear if the additional cost for outlier detection is acceptable. Quantitative assessments of computational cost and scalability analysis with increasing model complexity would offer practical insights for real-world application.

### Soundness
3

### Presentation
3

### Contribution
2
