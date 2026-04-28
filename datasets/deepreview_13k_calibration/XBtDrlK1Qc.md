# Masking the Gaps: An Imputation-Free Approach to Time Series Modeling with Missing Data

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 3, 8

## Abstract
Modeling time series is important in a variety of domains, yet it is  challenged by the presence of missing values in real-world time-series datasets. Traditional frameworks for modeling time-series with missing values typically involve a two-step process, where the missing values are first filled-in using some imputation technique, followed by a time-series modeling approach on the imputed time-series. However, existing two-stage approaches suffer from two major drawbacks: first, the propagation of imputation errors into subsequent time-series modeling performance, and second, the inherent trade-offs between imputation efficacy and imputation complexity. To this end, we propose a novel imputation-free approach for handling missing values in time series termed {Miss}ing Feature-aware {T}ime {S}eries {M}odeling ({MissTSM}) with two main innovations. {First}, we develop a novel embedding scheme that treats every combination of time-step and feature (or channel) as a distinct token, encoding them into a high-dimensional space. {Second}, we introduce a novel {Missing Feature-Aware Attention (MFAA) Layer} to learn latent representations at every time-step based on partially observed features. We evaluate the effectiveness of MissTSM  in handling missing values over multiple benchmark datasets using two synthetic masking techniques: masking completely at random (MCAR) and periodic masking, and a real-world missing-value dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an imputation-free approach called MissTSM to handle missing data in time series. The MissTSM framework is innovative, and the experiments demonstrate its effectiveness.

### Strengths
1. The paper is well organized and clearly articulates the methodology behind MissTSM;
2. The authors provided a link to their source code for reproducibility;

### Weaknesses
1. Three datasets for each task are limited and not enough to verify a framework;
2. Too many experiment setup details are missing. For example, a). hardware information is missing in the computational cost comparison; b). the authors do not mention how they determine models' hyperparameters;


### Questions
1. How did the hyperparameters of the baseline models get optimized? Please discuss and reveal more details regarding this point.
2. Baseline models are missing in the code repository. Did the authors reproduce the baseline methods by using their official code or other unified Python libraries (e.g.  Time-Series-Library [1], PyPOTS [2])? Data processing is quite different across imputation algorithms while unified interfaces can ensure fairness in the experiments.
3. Now that only three datasets are for the forecasting task, why select both ETTh2 and ETTm2 from ETT datasets for experiments? Generally, datasets from different application domains are more reasonable.

### References
[1] https://github.com/thuml/Time-Series-Library

[2] Wenjie Du. PyPOTS: a Python toolbox for data mining on Partially-Observed Time Series. In KDD MiLeTS Workshop, 2023. https://github.com/WenjieDu/PyPOTS

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a DL-based time-series method called MissTSM, which is designed to handle missing values in time series data without relying on imputation techniques. The key components of MissTSM include a Time-Feature Independent (TFI) embedding that treats each time-step and feature combination as a distinct token and a Missing Feature-Aware Attention (MFAA) layer that learns latent representations at each time-step based on the observed features (using missingness indicator when assigning the attention values). The authors evaluate MissTSM on multiple benchmark datasets using synthetic (MCAR and periodic) and real-world missing value scenarios. The results show that MissTSM achieves comparable performance to a wide variety of time-series classification and forecasting methods (equipped with state-of-the-art imputation methods).

### Strengths
-	The paper is in general well-written and easy to follow.

### Weaknesses
-	The authors have presented a limited perspective on time-series methods that avoid imputation. A broader range of approaches exists to tackle missing values in time series. One such approach involves augmenting the input data with indicators for each feature-time variable, which can be particularly informative when missingness is not random. Another line of research focuses on handling multivariate time series with irregular time intervals. This includes methods like GRU-D [A], which directly incorporates missingness indicators and time intervals as inputs, and ODE/SDE-based approaches [B]-[D] that inherently model such irregular time series.
-	The authors should consider a broader range of baseline models. This could include evaluating existing time-series methods that incorporate missingness indicators as input or exploring some of the mentioned techniques designed for handling irregular time intervals.
-	Treating each feature at each time point as a separate embedding and treating missingness indicator to bias the attention score are not technically novel. Moreover, the performance gain seems marginal and sometimes being lot worse than the benchmarks. 
-	While the utility of the imputation methods is often measured by the performance in downstream tasks, imputation is not designed to achieve higher discriminative/prediction power. More simpler imputation methods – such as mean/mode imputation or last observation carried forward – should be included as well in the experiments. 

### Questions
-	It seems that attention scores for the masked feature-time points can be naturally removed when computing those self-attention scores. What is the benefit of using the mask indicators as the bias terms rather than explicitly removing those from computation?
-	Why the quarries do not depend on the time point whereas the keys and values do?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To address the missing values in time series datasets, this work considers the imputation-free time series modeling. MCAR and periodic masking are considered in experiments by comparing with two stage baselines, consisting of imputation and modeling approaches.

### Strengths
S1. Various imputation baselines are considered in experiments.

S2. Time series modeling is important.

S3. Time series forecasting and classification are considered in experiments.

### Weaknesses
W1. The introduction is not well-written, which seems more like the related work. It is suggested to further polish the manuscript, to improve the readability.

W2. In the Introduction, the authors claim that all existing works for time-series modeling with missing values are two stage approaches, where missing values are first imputed, followed by feeding the imputed time-series to a modeling approach. Unfortunately, there already exists existing study [m1] considering the robust time series modeling over low quality data, where missing values and anomalies are associated with low importance in modeling, instead of treated as a two stage framework. Therefore, the motivation is unpersuasive, claiming that all the existing works are two stage approaches.

W3. In practice, in addition to the missing values, there also exist various data quality problems, e.g., anomaly, errors, staleness, etc. Only focusing modeling the time series data with missing values is insufficient to serve real applications. Please discuss how the approach might be extended or adapted to handle other types of data quality problems, or explain why you chose to focus specifically on missing values.

W4. MCAR and periodic masking are widely used operations in time series imputation, which are surprising to be proposed by this manuscript, at the end of the Introduction.

W5. Various imputation methods are considered in the experiments, but the most related works, i.e., robust modeling methods such as [m1], are totally ignored.

W6. The SOTA imputation baselines are ignored in the comparison, such as [m2]. Please include the comparison with it.

W7. In addition to the MCAR and periodic masking, MAR and MNAR are also widely considered in the experiments.

### Questions
W1-W5

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes an imputation-free approach for handling missing values in time series termed Missing Feature-aware Time
Series Modeling (MissTSM). MissTSM is composed of two primary modules. The first, Time-Feature Independent (TFI) Embedding, encodes each combination of time-step and feature into a high-dimensional space. The second module, the Missing Feature-Aware Attention (MFAA) Layer, is a novel mechanism designed to capture latent representations at each time-step by leveraging partially observed features. Empirical evaluations conducted under Masking Completely at Random (MCAR) and periodic masking validate the effectiveness of MissTSM in modeling time series data with missing features.

### Strengths
1. The intuition behind the idea is clear, effectively circumventing the imputation step typically used in traditional methods for handling missing data.
2. The presentation is strong, with clear figures that make the content easy to read and understand.
3. The experiments are comprehensive, covering both time series forecasting and classification, and include an insightful ablation study.

### Weaknesses
1. While the motivation is clear, the experimental results do not show significant improvement over the other baselines.
2. Time series missingness is a well-studied and widely researched field, making it difficult to assess the significance of the contribution here.
3. This work primarily represents an empirical study rather than a theoretical advancement.

### Questions
1. The author mentions two drawbacks of imputation: the propagation of imputation errors and the trade-off between imputation efficacy and complexity. Could the author clarify how MissTSM circumvents these drawbacks? I'm confused because: (1) it seems that errors in TFI would aggregate and influence MFAA, and (2) there's a clear trade-off between complexity and efficiency—for example, adding a dynamics module may improve performance but also increase complexity. Could the author clarify to what extent MissTSM addresses these two challenges?
2. Please clarify the intuition behind the 2D Positional Encodings (Line201-210) and explain why and how equations (2) and (3) are used in this context? Additionally, could the author elaborate on why these encodings provide an effective representation?
3. Can the authors explain the rationale for considering 60%-70% missing values in the experiments? Is it because MissTSM shows more significant improvements with a higher percentage of missing values? Typically, a missing range of 10-40% is more common, so additional clarification would be helpful.
4. My main concern lies in the significance of the experimental results. It appears that MissTSM's performance heavily depends on the dataset. For example, MissTSM only demonstrates comparable results on the ETTm2 and Weather datasets (Table 1, Figure 5), and the ablation study doesn’t clearly show the effectiveness of TFI and MFAA. Could the authors explain this? If additional results could be provided, specifically concerning MissTSM without TFI-Embedding but with MFAA, and address the previous questions, I would be happy to increase my score.

### Soundness
3

### Presentation
4

### Contribution
2
