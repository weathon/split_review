# Test-time Adaptation for Regression by Subspace Alignment

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
This paper investigates \textbf{test-time adaptation (TTA) for regression}, where a regression model pre-trained in a source domain is adapted to an unknown target distribution with unlabeled target data.
Although regression is one of the fundamental tasks in machine learning, most of the existing TTA methods have classification-specific designs, which assume that models output class-categorical predictions, whereas regression models typically output only single scalar values.
To enable TTA for regression, we adopt a feature alignment approach, which aligns the feature distributions between the source and target domains to mitigate the domain gap.
However, we found that naive feature alignment employed in existing TTA methods for classification is ineffective or even worse for regression because the features are distributed in a small subspace and many of the raw feature dimensions have little significance to the output.
For an effective feature alignment in TTA for regression, we propose \textbf{Significant-subspace Alignment ({\proposedmethod})}.
{\proposedmethod} consists of two components: subspace detection and dimension weighting.
Subspace detection finds the feature subspace that is representative and significant to the output.
Then, the feature alignment is performed in the subspace during TTA.
Meanwhile, dimension weighting raises the importance of the dimensions of the feature subspace that have greater significance to the output.
We experimentally show that {\proposedmethod} outperforms various baselines on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses a crucial yet under-explored area in machine learning: test-time adaptation (TTA) for regression models. The authors rightly highlight the limitations of existing TTA methods, which are primarily tailored for classification tasks, and propose a novel approach termed Significant-subspace Alignment (SSA). The paper presents a clear rationale for the need to adapt TTA techniques for regression and offers a compelling solution through feature alignment.

### Strengths
The topic of adapting regression models to unknown target distributions is highly relevant, particularly given the increasing use of machine learning in diverse applications. The proposed SSA approach is innovative and addresses a gap in the literature.

### Weaknesses
1. In Section 3.1 of the article, the use of "two diagonal Gaussian distributions" is not adequately justified, and the advantages and limitations of employing such distributions are not discussed. Specifically, the paper lacks a clear explanation of why a diagonal Gaussian is chosen over other distributions, and it does not address the potential impact of this choice on the method's performance under various data conditions. The assumption of independence between features, implied by the diagonal covariance, is a strong one that needs further justification, especially given that real-world data often exhibits complex correlations.
2. The proposed method in this paper exhibits limited originality, as its various components are commonly found in existing models. The paper does not sufficiently highlight the novelty of combining these components in the specific way proposed, nor does it provide a detailed comparison to existing methods that use similar components to demonstrate its unique contribution. The lack of a clear and compelling argument for the originality of the method weakens its overall impact.
3. The dataset utilized in this study has a relatively small sample size, which weakens the persuasiveness of the findings. Additionally, there is a lack of comparative algorithms from the past three years, resulting in insufficient theoretical validation. Furthermore, the measurement standard is solely based on R²; incorporating additional metrics such as RMSE and RMAE would enhance the evaluation. The small dataset size limits the generalizability of the results, and the absence of recent baselines makes it difficult to assess the method's performance relative to the current state-of-the-art. The exclusive use of R² also provides an incomplete picture of the method's performance, as it does not capture the magnitude of errors.

### Questions
1. Why are "two diagonal Gaussian distributions" used in Chapter 3? What is the rationale behind this choice?
2. In Section 4.1, the first dataset utilizes a classification dataset as a regression task. Is this approach reasonable and justifiable? Regarding the second dataset, is it appropriate to consider a noisy version of the test set as the target domain?
3. Could you provide a proof or evidence demonstrating the effectiveness of Significant-subspace Alignment (SSA)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the application of Test-Time Adaptation for regression tasks, where a regression model pre-trained in a source domain is adapted to an unknown target distribution using unlabeled target data. The authors note that most existing TTA methods are designed for classification tasks and do not directly apply to regression models, which typically output single scalar values rather than class-categorical predictions. To address this, the paper proposes a feature alignment approach called Significant-subspace Alignment, which consists of two components: subspace detection and dimension weighting. SSA aims to align feature distributions between the source and target domains to mitigate the domain gap, focusing on a representative and significant subspace of the feature space. Experimental results on various real-world datasets demonstrate that SSA outperforms several baseline methods.

### Strengths
1.SSA introduces a novel approach for TTA in regression tasks by combining subspace detection and dimension weighting, which is an innovative contribution to the field.
2.The paper conducts extensive experiments on multiple real-world datasets, validating the effectiveness of SSA.
3.Compared to the original model and other baseline methods, SSA achieves higher R2 scores across multiple datasets, demonstrating performance improvements in regression tasks.

### Weaknesses
1.SSA assumes covariate shift, where p(y|x) remains unchanged. The paper does not address distribution shifts where p(y|x) changes, such as concept drift, limiting its applicability in broader scenarios. Specifically, the method's reliance on aligning feature distributions without considering potential changes in the conditional distribution p(y|x) makes it vulnerable to performance degradation when the underlying relationship between features and target variables evolves over time or across different environments. This is a significant limitation as real-world regression problems often exhibit such non-stationary behavior.
2.While the paper mentions the selection of the parameter λ, it lacks a detailed discussion on the impact of other hyperparameters, which could affect the model's generalizability and adaptability. The paper does not provide sufficient analysis on how the learning rate, batch size, and other optimization parameters influence the performance of SSA. This lack of hyperparameter sensitivity analysis makes it difficult to reproduce the results and to apply the method effectively in new scenarios. The absence of a clear guideline for hyperparameter tuning is a significant drawback.
3.The paper does not discuss the computational complexity of SSA, particularly its performance with large-scale datasets, which is crucial for practical applications. The paper does not provide any analysis of the time and space complexity of the proposed method. Without such analysis, it is difficult to assess the scalability of SSA for large-scale regression problems. The lack of discussion on computational cost limits the practical applicability of the method.

### Questions
How does SSA perform in multi-task and multi-class regression tasks? Can it be extended to these scenarios?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a test-time domain adaptation method for regression. They show that learned embeddings are more compressed in regression than classification. To address this, they introduce Significant-subspace Alignment (SSA). SSA uses PCA to detect a significant feature subspace where features are concentrated, then aligns the first two moments of source embeddings and target batch within this subspace. They also apply dimension weighting to prioritize subspace dimensions based on their significance to the output. The proposed method is evaluated on four regression datasets and demonstrates superior performance compared to baseline TTA methods designed for classification tasks, and domain adaptation for regression adapted for TTA .

### Strengths
- The paper proposes a novel method for Test time domain adaptation for regression, and adapted common benchmarking procedures for classification to regression, especially on the UTK Face dataset.

- The paper is well-written and clear.

- The method and results seem convincing and easy to implement.

### Weaknesses
 - In the related work, feature alignment methods for TTA are reviewed with the claim, “Although some of these methods are directly applicable to regression, we have observed that they are not effective or even degrade regression performance.” However, these methods are not included in the experiments, leaving this claim unsupported.
- In Table 1, the subspace dimension for Biwi Kinect is shown as ‘34.5’, which is unclear, as dimensions are typically integers.
- MLPs and CNNs seem to produce embeddings with different ranks, with MLPs showing less low-rank behavior. A discussion or remark on this difference could provide useful insights.
- The test setup lacks clarity on whether SSA is applied in an online or episodic adaptation manner, and it’s unclear if batches are fed uniformly.
- The dimension weighting approach may lead to disproportionately high contributions from small-scale features if they are assigned high weights (when learned on source), potentially resulting in values similar to large-scale features with lower weights (when learned on source).   Did you consider any normalization or balancing mechanism to prevent this scaling effect?

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates test-time adaptation (TTA) for regression, where a regression model pre-trained in a source domain is adapted to an unknown target distribution with unlabeled target data. To enable TTA for regression, the authors adopt a feature alignment approach, which aligns the feature distributions between the source and target domains to mitigate the domain gap. A propose Significant-subspace Alignment (SSA) is proposed for feature alignment in TTA for regression, which consists of two components: subspace detection and dimension weighting. Some experiments have been conducted to verify the performance of the proposed method.

### Strengths
1.	A Significant-subspace Alignment (SSA) method is proposed to address TTA for regression on the basis of the feature alignment approach.
2.	SSA consists of two components: subspace detection and dimension weighting. 
3.	Subspace detection uses principal component analysis (PCA) to find a subspace and dimension weighting raises the importance of the subspace dimensions.

### Weaknesses
1.	The description of Figure 1 is too simple to understand the procedure of the proposed method. Some key variables (i.e., gφ and hψ) should be introduced. For easy understand, I suggest the authors provide a step-by-step description of the workflow shown in the figure. 
2.	The used compared methods are all published before 2023, how the proposed method compares to or differs from some newer approaches, such as “Backpropagation-free Network for 3D Test-time Adaptation, CVPR 2024”, “Improved Self-Training for Test-Time Adaptation, CVPR, 2024”.
3.	Why no results for RSD are given in Table 3? Please provide the missing results for RSD in Table 3 or explain why these results were not included.
4.	What is the visualization effect of the proposed method? Provide T-SNE rendering.
5.	What is the limitation of the proposed method? Are there any situations where SSA might not perform well, or any assumptions it makes that might not hold in all regression tasks?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
