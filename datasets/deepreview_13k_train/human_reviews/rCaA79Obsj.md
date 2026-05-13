# Towards zero shot multivariate time series anomaly detection - A Realistic Evaluation

- Decision: Reject
- Scores: 5, 8, 5, 5, 3

## Abstract
A long line of multivariate timeseries anomaly detection (MTAD) approaches use performance enhancement techniques that are not feasible in practical scenarios. In specific, a) point adjustment technique is employed which uses ground truth to forcefully convert false negatives to true positives and inflates precision to unrealistic proportions, and b) significant data leakage is introduced where anomaly score threshold is determined using the test data and test labels. In this paper, we show the real world performance of existing MTAD techniques when point adjustment and threshold learning on test data is disabled. Moreover, we show that anomalies introduced in real world benchmark datasets result in significant distribution shift between normal and anomalous data, and when point adjustment and threshold learning are used even untrained deterministic methods can perform on par or even beat baseline techniques. We then introduce six synthetic benchmark examples derived from real world systems, where anomalous data and normal data have statistically insignificant distribution shift. We propose, sparse model identification enhanced anomaly detection (SPIE-AD), a model recovery and conformance based zero shot MTAD approach that outperforms state of art MTAD techniques on three real world benchmark datasets without using point adjustment and threshold learning on test data. We evaluate state-of-art MTAD and SPIE-AD on the novel synthetic benchmarks. SPIE-AD outperforms state-of-art MTAD techniques on both standard and novel benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a zero-shot time series anomaly detection method called SPIE-AD, which leverages sparse model recovery (SMR) technology to detect anomalies by monitoring changes in model parameters. SPIE-AD makes two main modifications: it does not rely on manually labeled labels for hyperparameter tuning in the validation set, and it abandons the controversial point adjustment evaluation method that has been heavily relied upon. The evaluation results are explicit, showing that SPIE-AD significantly outperforms existing methods on the U2 benchmark.

### Strengths
1. The method proposed in the paper for anomaly detection through model recovery is innovative, as traditional methods that model normal patterns based on data and then compare them have high dependencies on the quantity and quality of data.
2. The challenge of consistent distribution between anomalous and normal data in the U2 benchmark presented in this paper, which is difficult to distinguish, has not been addressed in many works, making it somewhat innovative.

### Weaknesses
1. The meanings of H and P in Figure 3 are not indicated.
2. Lines 6 and 9 in Algorithm 2 are reversed.
3. On line 84, it is stated that existing anomaly detection methods are based on the assumption of anomaly-free data, which is invalid. The biggest difference between anomaly detection tasks and time series tasks is that anomaly detection tasks do not assume that training data is free of anomalies, which is why there are many reconstruction methods have been proposed.
4. The relationship between zero-shot and A1, A2, A3 needs to be clarified. Are they parallel, or do A1, A2, and A3 make the zero-shot objective face greater challenges?

### Questions
1. Some very classic MTS evaluation datasets, besides SMD, have not been evaluated, such as Yahoo[1].
2. Some very classic MTS baselines and methods have not been compared, such as OmniAnomaly[2].
3. To achieve good zero-shot performance, some time series foundation models proposed through time series analysis have been proposed, which can do both time series forecasting and anomaly detection. These methods should also be compared, such as OFA's sec 4.2[3], and some related work mentioned by OFA.
4. A very similar evaluation work, TimeseriesBench[4], has not been mentioned. TimeseriesBench discusses zero-shot and point adjustment comparisons. How would SPIE-AD perform on TimeseriesBench?

[1] Y. Research, “A benchmark dataset for time series anomaly detection.” https://yahooresearch.tumblr.com/post/114590420346/a-benchmark-dataset-for-time-series-anomaly, 2015.
[2] Su, Ya, et al. "Robust anomaly detection for multivariate time series through stochastic recurrent neural network." Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining. 2019.
[3] Zhou, Tian, et al. "One fits all: Power general time series analysis by pretrained lm." Advances in neural information processing systems 36 (2023): 43322-43355.
[4] Si, Haotian, et al. "Timeseriesbench: An industrial-grade benchmark for time series anomaly detection models." arXiv preprint arXiv:2402.10802 (2024).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces SPIE-AD, a zero-shot multivariate time series anomaly detection approach that aims at overcoming the prevalent information leakage from threshold selection prevalent in the literature. The key innovation is combining sparse model identification with conformance testing to detect anomalies without requiring anomaly examples during training. The authors also contribute new synthetic benchmarks and demonstrate issues with current evaluation practices.

### Strengths
The paper tackles an important problem, pervasive in the anomaly detection literature that puts into question the validity of a lot of published results in real-work scenarios. The paper introduces a novel technical approach combining model identification with conformance testing and performed a comprehensive empirical evaluation including with the release of new benchmarks. The theoretical foundations of the paper appear sound.

### Weaknesses
The paper contains limited discussion of computational complexity of the proposed methods. This is an important weakness given that the proposed method is not straightforward. Specifically, the paper lacks a detailed analysis of the time and space complexity of both the sparse model identification and the conformance testing components. The authors should provide a breakdown of the computational cost associated with each step, including the impact of the dimensionality of the time series data and the length of the time windows used. Similarly, the authors could better explain parameter sensitivity and failure cases. For example, how does the performance vary with different choices of regularization parameters in the sparse model identification step, or with different thresholds in the conformance testing? The paper should also discuss scenarios where the method might fail to detect anomalies, such as when anomalies are very short-lived or when they exhibit patterns that are not well captured by the chosen models. 
The issue with information leakage from calibration of threshold on the training set has been identified in previous works, the related literature section is missing a discussion of this. The authors should explicitly acknowledge and discuss this issue, citing relevant papers that have previously addressed this problem. This would help to contextualize the contribution of the paper and highlight the novelty of the proposed approach.

The empirical analysis is limited. It relies mostly on the synthetic datasets proposed by the authors. While the synthetic datasets are useful for controlled experiments, they may not accurately reflect the complexity and variability of real-world time series data. The quality and informativeness of the real-world datasets they use have been questioned, rightfully so in this reviewer's opinion. UCR offers a large collection on time-series anomaly datasets that are well documented. The authors should use them. Similarly, the authors should include simple, algorithmic baselines to their comparison and include computational cost as a relevant dimension. The current comparison is largely limited to other complex methods, making it difficult to assess the practical value of the proposed approach. A comparison with simpler, more computationally efficient methods would provide a more comprehensive evaluation.

### Questions
What is the computational overhead of SPIE-AD compared to existing methods?
How sensitive is the method to the choice of window size?
Are there specific types of anomalies where the method might fail?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a multi-variant time series anomaly detection (MTAD) method that differs from existing approaches by learning the relationships between points on a curve. Instead, it judges whether a certain time series is anomalous by comparing the changes in model parameters \( w_i \) fitted from different data. This method no longer relies on labels from the validation set to tune the model and can achieve good results without using point adjustment.

### Strengths
1. The paper points out that both point adjustment and reliance on validation labels are significant issues.
2. The application of the SMR method to anomaly detection in the paper is innovative.
3. The paper contributes a synthetic evaluation dataset.

### Weaknesses
1. More related methods should be compared and discussed. The current comparison is limited, and the paper would benefit from a more thorough analysis against state-of-the-art methods in multi-variate time series anomaly detection. Specifically, methods such as TFAD[1], OFA[2], and FITS[3], which have demonstrated strong performance, should be included in the comparison to properly contextualize the proposed method's performance. The paper needs to justify the selection of baselines and explain why certain high-performing methods were not considered.
2. The writing part of the paper requires some improvement; the introduction is too long. The introduction section could be more concise and focused, directly addressing the core problem and the proposed solution. The current length detracts from the clarity and impact of the paper. Additionally, the paper lacks a clear narrative flow, making it difficult to follow the key ideas and contributions.
3. The references are not placed in parentheses, which affects readability. The lack of standard citation formatting makes it difficult to quickly identify the sources and disrupts the flow of reading. This should be corrected for better readability and to adhere to academic standards.
4. The placement of related work in the middle of the paper, together with the baseline in the evaluation, is not intuitive. Related work should be an independent section as it discusses relevant papers in this research field. The current structure makes it difficult to understand the context of the proposed method and how it relates to existing research. The related work section should be placed at the beginning of the paper to provide a clear background and motivation for the work.

### Questions
1. The paper uses relatively simple baselines. Some methods with better performance, such as TFAD[1], OFA[2], and FITS[3], are not compared. It is uncertain whether the method in this paper still has certain advantages under zero-shot evaluation methods and the u2 dataset.
2. The paper only mentions the SMD dataset, but there is a benchmark[4] that even focuses on zero-shot and point adjustment alternatives. How does the paper's method perform on this benchmark?

[1] TFAD: A decomposition time series anomaly detection architecture with time-frequency analysis

[2] Zhou T, Niu P, Sun L, et al. One fits all: Power general time series analysis by pretrained lm[J]. Advances in neural information processing systems, 2023, 36: 43322-43355.

[3] FITS: Modeling time series with 10k parameters, in The Twelfth International Conference on Learning Representations, 2024.

[4] Si, Haotian, et al. "Timeseriesbench: An industrial-grade benchmark for time series anomaly detection models." arxiv.org/pdf/2402.10802 (ISSRE 2024).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a sparse model identification enhanced anomaly detection (SPIE-AD) model which is a recovery and conformance-based zero shot MTAD approach. It disables point adjustment and thresholding methods. The backbone of SPIE-AD are the two fundamental theoretical contributions of this paper: a) robust sparse non-linear dynamical model recovery from real-world multi-variate data using neural architectures with automated differentiation and b) statistical conformance-based model robustness interval extraction (CRIE) algorithm that can identify statistically relevant difference in recovered models.

### Strengths
The proposed model using dynamic modeling is novel. And paper is mathematically sound and well-written. Performance on synthetic data is good.

### Weaknesses
U2 scenario is nonrealistic as real world data is mixed with unknown noise. It is hard to get training data cleaned up in real-world data. It will be better to discuss how author would handle noisy or imperfect training data in real-world applications.

What is a contribution against the Autoencoder-based method? Can you please compare SPIE-AD approach to autoencoder-based methods like USAD, highlighting key differences and potential advantages in terms of performance, computational efficiency, or interpretability.

Also, validation data should not be used as training data. Is there any real-world application in your mind behind this?

What happens if you use separate validation data? It would be better to conduct an additional experiment using a separate validation set that is distinct from both the training and test sets and kindly report how this affects the results.

The author models robustness as a reconstruction error. Why the dynamic model is called sparse and robust in not clear. Please provide a more detailed explanation of the definition of "sparse" and "robust" in the context of their dynamic model. Can you please explain how sparsity is enforced in the model structure and how robustness is quantified beyond reconstruction error?  Some experimental evidence on the usefulness of sparsity and robustness for detecting anomalies would be nice to have.

Table 4 shows that the proposed model is performing worse than many benchmarks. Please provide a more in-depth analysis of these results, discussing potential reasons for underperformance.

Some analytical results about where the proposed method fails would be good.  Please provide a detailed error analysis, identifying specific types of anomalies, datasets, or scenarios where your method underperforms. Please also discuss potential reasons for these failures and propose potential improvements or future work to address these limitations.

### Questions
As above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces zero shot multivariate time series anomaly detection that can avoid point adjust step and data leakage in hyperparameter tuning. The proposed method is a sparse model recovery built upon ODE. A neural network is also used to handle the robustness. The proposed method could finally produce an interval based on the kth smallest value for labeling.

### Strengths
1. The proposed method can outperform existing methods by a large margin without point adjustment.
2. The hyperparameter of the proposed method can be tuned only with training data.
3. Build new benchmarks for better evaluating the U2 anomaly.

### Weaknesses
1. The writing needs a lot of improvement.  Below are some examples:
  + It is hard to follow the main content of the proposed method. 
  + There are limited details about how the proposed benchmark can reflect the claimed properties. 
  + Why can the claimed difficulty not be handled by some heuristics or advanced tech? For example, A1 could also be addressed by extreme value theory for dynamic threshold [1]. A2 could be mitigated by some better measurements to mitigate the effect of noisy labeling [2]. 

2. The experiments are not rigious, which decreases the confidence of the experiments. 
  + The compared methods are too weak. In the real-world dataset evaluation, the compared method achieves a 0 F1 score. This is hard to trust. Why not provide heuristics like quantile for thresholding or extreme value theory for dynamic threshold?
  + Recent progress [2] in evaluating AD has proposed several threshold-free measurements. It seems the bad performance of the compared method largely results from only using F1 score, which requires a threshold.
  + There is zero empirical analysis for the proposed benchmark. 
  + In Table 3, AT+ is the best but is not marked as bold in F8Slow. 

### Questions
Please address the concerns in the weakness.

### Soundness
2

### Presentation
1

### Contribution
2
