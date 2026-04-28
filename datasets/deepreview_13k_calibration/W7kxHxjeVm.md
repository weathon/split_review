# ImAD: An End-to-End Method for Unsupervised Anomaly Detection in the Presence of Missing Values

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Common anomaly detection methods require fully observed data for model training and inference and cannot handle data containing missing values. The missing data problem is pervasive in various real-world scenarios but the study of anomaly detection with missing data is quite limited. In this work, we first construct and evaluate a straightforward strategy, "impute-then-detect", which combines state-of-the-art data imputation methods with unsupervised anomaly detection methods, where the training data are only composed of normal samples. We observe that such two-stage methods often yield imputation bias for normal data, namely, the imputation methods are inclined to make incomplete samples "normal". The fundamental reason is that the imputation models are learned from normal data and cannot be generalized to abnormal data. To solve the challenging problem, we propose an end-to-end method called ImAD for unsupervised anomaly detection in the presence of missing values. ImAD integrates data imputation with anomaly detection into a unified optimization problem and introduces well-designed pseudo-abnormal samples to ensure the discrimination ability of the imputation process. Experiments in the settings of three different missing mechanisms, including MCAR, MAR, and MNAR, show that the proposed ImAD alleviates the imputation bias and achieves much better detection performance on balanced and skewed data, in comparison to the baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new end-to-end approach called ImAD, which integrates data imputation with anomaly detection in a unified optimization problem. ImAD addresses the imputation bias issue and demonstrates improved detection performance on balanced and skewed data compared to existing methods in various missing data scenarios.

### Strengths
- The concept of initially generating pseudo-abnormal samples and subsequently constructing an imputation model from both the normal and pseudo-abnormal datasets is a novel approach.
- The authors provide a theoretical analysis of the generation and detection of pseudo-abnormal samples.
- The observed performance enhancement in comparison to the baseline methods is substantial and noteworthy.

### Weaknesses
 - The current scope of experiments is somewhat limited, and it is strongly recommended to expand the experimental evaluation to include a broader range of datasets. This will facilitate a more comprehensive validation of the efficacy of the proposed method.
- The assumption of a Gaussian distribution in the latent space could potentially impose limitations on the practical applicability of the proposed method. Real-world datasets with inherent complexity may not fit into a single Gaussian distribution, raising concerns about the generalizability of the approach to such intricate data scenarios.



### Questions
- How can we ensure that the generated pseudo abnormal samples are similar to real abnormal samples? Because the distribution of pseudo abnormal samples in latent space is assumed, it can differ significantly from that of real abnormal samples. This difference can lead to strange imputation.
- When dealing with a dataset of very high dimensionality, is the proposed method scalable? Will the assumption in generating pseudo-abnormal samples still hold?
- There is an excessive use of similar symbols placed above characters, which can impede readability.
- Typo. The last paragraph of 2 Related Work. impuate -> impute.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors present an anomaly detection framework which can handle missing values. One of the key challenges being addressed is to ensure that the imputation model trained on normal data should generalize to abnormal data. Authors pursue a generative modeling approach to generate pseudo-abnormal samples and learn an imputation model on both samples.  A composite loss term evaluating imputation, anomaly and reconstruction losses is formulated for the proposed method. Authors provide results on sample UCI datasets and compare performance to deep learning based anomaly detection and other AD baselines.

### Strengths
1) Paper is technically sound and the presentation is good.
2) Proposed framework is simple and makes sense mostly. The problem although heavily studied, there is not a lot of literature on AD with missing data. 
3) Empirical results compare performance against both deep AD and other regular AD baselines.

### Weaknesses
1) Figure 1 uses AUROC on y-axis whereas for anomaly detection I think AUPR is better to motivate as most anomaly detection techniques have poor precision. Also Adult and KDD are UCI datasets which do not have a lot of relevance today as most techniques perform superlatively on these datsets. Given that the framework is applicable for missing values, it makes more sense to benchmark/motivate on real world use cases for anomaly detection (IoT sensor data, etc). The choice of AUROC, while common, may obscure the practical limitations of the method in scenarios with imbalanced data, which is typical in anomaly detection. AUPR would provide a more realistic view of the method's performance, particularly in identifying true anomalies, which are often rare. Furthermore, the use of Adult and KDD datasets, which are well-studied and often yield high performance for many methods, does not adequately demonstrate the method's effectiveness in more challenging, real-world scenarios where data is more complex and less structured.
2) Section 3.5 seems way too short and not very insightful with the purpose of just being added in the paper to have such a section in the main paper. The section lacks depth and does not provide a clear understanding of the constrained sampling radius. It is unclear how this radius is determined, and the theoretical justification is not well-explained. The practical implications of this constrained sampling are also not discussed, leaving the reader with limited insight into its importance.
3) Also on a more real-world applicability note, imputation is not often used within industry and missing data if any is more often discarded. I would encourage authors to think of very strong real-world insights of when imputation should be used and when should it be avoided. The paper does not adequately address the practical considerations of using imputation in real-world applications. The authors should discuss the potential drawbacks of imputation, such as the introduction of bias or the amplification of noise, and provide guidance on when imputation is appropriate and when it should be avoided. A more nuanced discussion of these trade-offs is needed to enhance the paper's practical relevance.

### Questions
1) I would like to see stronger results on AUPR for high dimensional real-world datasets which actually have a lot of missing values. Some real-world datasets from IoT sensor domains or others will definitely help in improving contributions of this paper. Some other questions are mentioned in the weakness section above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the challenge of anomaly detection in data with missing values. The authors propose a novel approach called ImAD that combines data imputation and anomaly detection in a unified framework. The proposed method generates pseudo-abnormal samples from the latent space to mitigate the imputation bias that the traditional two-stage methods tend to exhibit. Experimental results show that it outperforms baseline methods in common scenarios.

### Strengths
The study on anomaly detection in datasets with missing values represents an underexplored area within the traditional field of anomaly detection. The recognition of imputation bias in the two-stage methods seems well-founded. The methodology for generating pseudo-anomalies in the latent space appears to be sound.

### Weaknesses
 - Section 2.2 introduces a few related studies on anomaly detection with incomplete data, but these methods are not included in the experimental evaluation. The results primarily rely on conventional approaches that do not explicitly account for missing data, such as DeepSVDD. 
- Experimental scenarios are too limited. Only two datasets are tested, while there exist many other benchmark datasets available for anomaly detection. The choice of two specific missing rates (0.2 and 0.5) may not realistically represent the practical scenarios. Only AUROC results are presented, omitting other essential metrics. 
- Although this paper includes some theoretical analysis in section 3.6, the derivations of the inequalities appear to be straightforward in the context of plain neural nets. It remains unclear whether these inequalities provide more valuable insights than those derived from other related methods, especially on practical utility.

### Questions
- In Figure 1, OC-SVM outperforms IForest across different missing rates, but OC-SVM is excluded in other experiments. Can you provide a rationale for this selectiveness?
- Can you provide results using additional performance metrics such as AUPRC?
- Justification on the use of the sinkhorn divergence in the loss function will be helpful.  
- It would be interesting to see some results on the robustness in relation to the values of r1 and r2.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
