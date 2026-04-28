# FMP-AE: A HYBRID APPROACH TO TIME SERIES ANOMALY DETECTION

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 3, 5

## Abstract
Unsupervised anomaly detection in time series presents significant challenges, especially due to the lack of labeled data and the prevalence of highly imbalanced datasets. Traditional statistical and machine learning methods often suffer from low recall and computational inefficiency. While deep learning techniques can automatically extract features, they still struggle with data imbalance. This paper introduces a novel anomaly detection model, Feature map Matrix Profile with an AutoEncoder (FMP-AE), which integrates matrix profile techniques with deep learning. The model uses a 1D-CNN to extract features and compute the matrix profile. A new Matrix Profile loss function is introduced and combined with the Autoencoder's reconstruction loss to enhance anomaly detection. The approach also incorporates a sliding window technique to improve sensitivity to sparse anomalies and increase efficiency. Experimental results on the UCR250 benchmark datasets demonstrate the model's superior performance across multiple metrics, including accuracy, precision, recall, F1-score, and AUC. These results highlight the FMP-AE model's ability to efficiently process large-scale datasets and generalize well across diverse time series domains, offering significant improvements in both detection accuracy and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents FMP-AE, a hybrid model for unsupervised anomaly detection in time series, combining Matrix Profile (MP) structures with deep learning components, specifically a 1D Convolutional Neural Network (1D-CNN) and an Autoencoder. The novelty lies in introducing an MP-based loss function that complements the Autoencoder’s reconstruction loss to improve anomaly detection performance. The model is evaluated on the UCR250 benchmark, where it demonstrates strong performance across several metrics.

### Strengths
1. Combines Matrix Profile with Deep Learning for Anomaly Detection: The paper’s main contribution lies in the integration of Matrix Profile with an Autoencoder, aiming to leverage both global and local sequence information for more robust anomaly detection.

2. Positive Empirical Results on UCR250 Dataset: FMP-AE shows strong empirical results on the UCR250 dataset, indicating that the model is capable of achieving high precision, recall, and F1 scores within this dataset, and the authors conduct ablation studies to explore the contribution of each model component.

### Weaknesses
1. Incremental Methodological Innovation: While combining Matrix Profile (MP) with Autoencoder reconstruction loss is practical, it mainly builds on existing methods without substantial theoretical innovation. The A.2 Loss Function section explains how this combination may enhance anomaly detection but lacks deeper theoretical justification for why MP loss would improve sensitivity beyond reconstruction loss alone. The explanation is largely empirical, without rigorous theoretical support to clarify this enhancement mechanism. Specifically, the paper does not delve into the mathematical properties of the MP that make it suitable for capturing local anomalies, nor does it provide a formal analysis of how the gradients of the MP loss interact with the gradients of the reconstruction loss during training. This lack of theoretical grounding makes it difficult to understand the specific conditions under which the combined loss function will outperform a standard reconstruction-based approach. The paper should include a more detailed analysis of the mathematical properties of the MP and how it complements the reconstruction loss, which would strengthen the theoretical contribution.

2. Restricted Dataset Evaluation and Generalizability Concerns: The evaluation is limited to a single dataset, UCR250, which restricts insights into FMP-AE’s applicability across diverse real-world scenarios. Furthermore, there is no theoretical justification for the combined loss function, making it unclear whether the observed improvements generalize beyond this dataset. Expanding the evaluation to include more varied datasets or providing theoretical analysis could help validate the model’s robustness and adaptability. The UCR250 dataset, while extensive, primarily consists of relatively short time series. The performance of the proposed method on longer time series, which are common in many real-world applications, is not evaluated. Additionally, the dataset does not fully represent the diversity of anomaly types that might be encountered in practice. The paper should include experiments on datasets with longer time series and a wider range of anomaly characteristics to better assess the generalizability of the proposed method.

3. Comparison with Outdated Baselines: The baseline methods used for comparison are primarily from 2022 or earlier, omitting more recent approaches in anomaly detection. This limits the assessment of FMP-AE’s competitiveness against the latest advancements in the field, making it difficult to gauge how the proposed method stands relative to state-of-the-art techniques. A comparison with newer methods would provide a clearer picture of FMP-AE’s effectiveness within the current landscape. Specifically, the paper does not compare against recent deep learning-based anomaly detection methods that have shown strong performance on time series data. Including such comparisons would provide a more comprehensive evaluation of the proposed method's performance.

### Questions
1.	Could the authors offer further theoretical justification for the combination of MP loss with reconstruction loss? Specifically, what theoretical basis supports the idea that MP loss enhances anomaly detection sensitivity beyond what reconstruction loss alone can achieve?

2.	How does FMP-AE perform on other datasets beyond UCR250, and how generalizable is the model across different domains? Additional experiments on varied time series data would help clarify the model’s robustness and adaptability.

3.	Why were no post-2022 methods included in the baseline comparisons? Would a comparison with more recent techniques clarify FMP-AE’s standing within the current anomaly detection landscape?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The author proposes a new method for time-series anomaly detection, FMP-AE, which combines the TCN network with the MP algorithm to achieve better detection performance.

### Strengths
The writing is clear and easy to understand.

### Weaknesses
Insufficient innovation. The organization of the paper is not good enough and the experiments are not sufficient.

The organization of the introduction has a lot of room for improvement. The author's focus should be on TSAD (Time-Series Anomaly Detection) rather than general anomaly detection. Therefore, the introduction should be revised. Additionally, it should explain why past methods face challenges and what their deficiencies are.

The ablation experiment lacks analysis of 1D-CNN + AE.

The analysis in the ablation experiment part lacks some more valuable conclusions. It should not be just a simple comparison of the performance of different methods.

Figure 4 does not show the original time series and abnormal regions, making it difficult to understand the pros and cons of different losses. Moreover, necessary analysis is lacking.

Figures 5 and 6 lack analysis, making it impossible to understand the analysis results of Figure 5. The significance of Figure 6 is unclear, and it is impossible to know the analyzed object and results.

The analysis conclusion of Figure 7 seems to overlap with the previous ones and lacks more insightful conclusions. At the same time, there is no comparison with other methods, lacking persuasiveness.

Figures 4-7 do not indicate on what data the experiments are conducted and there is no comparison with other methods.

In setting up comparison methods, recent works such as NPSR, SimAD, D3R, LLM and other models are lacking.

Figure 10 is difficult to understand, with a large amount of blank time series.

The author does not analyze from the experimental and theoretical levels why their method can solve existing challenges.

There is a lack of necessary comparison of space-time complexity and algorithm time consumption, making it impossible to effectively prove that the author's proposed algorithm is efficient.

The author only validates on one dataset, UCR, lacking mainstream datasets in the current TSAD community such as MSL, SMAP, SMD, etc. It is difficult to evaluate the performance of the algorithm under complex conditions.

There is a lack of analysis of the classic Matrix Profile algorithm. What would be the performance if features are obtained using TCN or MLP and then the classic MP is used?

The author's experimental organization is not good enough and does not effectively verify the motivation of their algorithm.

I suggest that the author open source the code for follow-up research.

### Questions
1. The organization of the introduction has a lot of room for improvement. The author's focus should be on TSAD (Time-Series Anomaly Detection) rather than general anomaly detection. Therefore, the introduction should be revised. Additionally, it should explain why past methods face challenges and what their deficiencies are.
2. The ablation experiment lacks analysis of 1D-CNN + AE.
3. The analysis in the ablation experiment part lacks some more valuable conclusions. It should not be just a simple comparison of the performance of different methods.
4. Figure 4 does not show the original time series and abnormal regions, making it difficult to understand the pros and cons of different losses. Moreover, necessary analysis is lacking.
5. Figures 5 and 6 lack analysis, making it impossible to understand the analysis results of Figure 5. The significance of Figure 6 is unclear, and it is impossible to know the analyzed object and results.
6. The analysis conclusion of Figure 7 seems to overlap with the previous ones and lacks more insightful conclusions. At the same time, there is no comparison with other methods, lacking persuasiveness.
7. Figures 4-7 do not indicate on what data the experiments are conducted and there is no comparison with other methods.
8. In setting up comparison methods, recent works such as NPSR, SimAD, D3R, LLM and other models are lacking.
9. Figure 10 is difficult to understand, with a large amount of blank time series.
10. The author does not analyze from the experimental and theoretical levels why their method can solve existing challenges.
11. There is a lack of necessary comparison of space-time complexity and algorithm time consumption, making it impossible to effectively prove that the author's proposed algorithm is efficient.
12. The author only validates on one dataset, UCR, lacking mainstream datasets in the current TSAD community such as MSL, SMAP, SMD, etc. It is difficult to evaluate the performance of the algorithm under complex conditions.
13. There is a lack of analysis of the classic Matrix Profile algorithm. What would be the performance if features are obtained using TCN or MLP and then the classic MP is used?
14. The author's experimental organization is not good enough and does not effectively verify the motivation of their algorithm.
15. I suggest that the author open source the code for follow-up research.

### Soundness
2

### Presentation
2

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
The paper proposes a combination of CNN and matrix profile to detect anomalies. The paper is easy to follow.

### Strengths
1. The paper studies an important problem.
2. It is interesting to consider matrix profile in deep learning.

### Weaknesses
1. The challenges presented in the paper are well known and have been solved by many other time series anomaly detection methods, such as label scarcity. The paper lacks an argument on why existing methods fails to address these challenges and why the proposed method show advantages over the existing methods to solve these challenges.
2. The method is quite easy and straightforward. It uses CNN to extract features of time series, and uses MP to compute similarity between subsequences. These are well-known techiniques.
3. The baselines and datasets are limited. SOTA baselines, such as DCdetector, ModernTCN, D3R, etc., are missing. Only UCR dataset is used, and many other well-known datasets are missing, such as MSL, PSM, SMAP, etc.

### Questions
See weaknesses.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper claims that there are three challenges facing by time series anomaly detection work: 1) label scarcity; 2) generalizability; 3) efficiency. Based on this recognition, the authors proposes a time series anomaly detection method by combining a matrix profile and an auto-encoder. The authors believe the matrix profile can improve the method efficiency, but the other two challenges was not discussed. The authors have made some experiments to verify the effectiveness of their method, but not compared with the most SOTA baselines. Besides, they also do not prove that the proposed method can improve method efficiency experimentally.

### Strengths
1. Overall well written. The paper is easy to follow and understand.
2. The idea of matrix profile is somewhat novel in time series anomaly detection.

### Weaknesses
1. Unsolved challenges. As mentioned in summary part, this paper mainly proposes three challenges. However, the authors only claim that the proposed method is more efficient by introducing matrix profile. The other two challenges is not solved by the proposed method. Also, it is not clear why matrix profile combining with an auto-encoder can improve the method efficiency compared with a solely auto-encoder. The authors state that the matrix profile reduces noise and focuses on data similarity, but this claim lacks experimental validation or theoretical justification. Specifically, there is no analysis of how the matrix profile's distance calculations lead to more efficient feature extraction compared to the autoencoder alone, nor is there a discussion of the computational overhead of calculating the matrix profile itself.
2. Unpersuasive experiments. On one hand, the proposed methods do not compare with the most SOTA methods, for example [1] [2] [3]. The latest method included in baseline is published in 2022. On the other hand, since the authors claimed that introducing matrix profile can improve method efficiency in their contributions, they should also have made experiment to prove it. However, this aspect is not discussed thoroughly in experiment. The paper lacks a direct comparison of training and inference times between the proposed method and a standard autoencoder, making it impossible to verify the claimed efficiency gains. Furthermore, the experimental setup needs to be more detailed, including the specific hardware used, batch sizes, and optimization algorithms, to ensure reproducibility and allow for a fair comparison.
3. Limited contribution. There are mainly two part in the proposed method: one is matrix profile and another is an auto-encoder. The structure of auto-encoder is really common by combining max-pool and CNN. The matrix profile may be somewhat novel, but it is a really marginal improvement. The novelty of combining a matrix profile with an autoencoder is not clearly demonstrated, as the paper does not provide a rigorous analysis of how this combination leads to superior performance compared to existing methods. The paper should include a more detailed analysis of the feature space learned by the combined model and how it differs from that of a standard autoencoder.
4. Misunderstanding of the shortage of deep-learning-based anomaly detection methods. In the abstract, the authors claimed that deep-learning-based anomaly detection methods is affected by data imbalance problem. Actually, many unsupervised deep-learning-based anomaly detection methods assume there are fewer anomalous samples in training set, so that when training by it, the model can better fit the normal pattern rather than anomalous one. Thus, deep-learning-based anomaly detection method actually benefit from those data imbalance.

### Questions
1. Could you please add some statics about the proposed method efficiency and baseline efficiency?
2. Why matrix profile combining an auto-encoder can improve the method efficiency, compared with a solely auto-encoder?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a model based on the computation of Feature map Matrix Profile, combined with an Autoencoder (FMP-AE) for time series anomaly detection. It introduces a novel loss function which enhances the model’s ability to detect anomalies by leveraging both global similarity and local feature reconstruction. The Matrix Profile is also designed based on the 1D-CNN extracted feature for a rapid and reliable identification of anomalies. Extensive experiments on UCR250 benchmark datasets demonstrate the effectiveness of the proposed method.

### Strengths
- The unsupervised time series anomaly detection task is quite challenging, the author build a unified hybrid solution and demonstrate great results.

- The paper is well-organized and clearly written, and it provides enough figures and demonstration to explain the methods well.

- I like the ablation study part, it clearly shows the effectiveness of each utilized component.

### Weaknesses
The paper writing and the proposed method all look good to me, however, I do have concerns on the experiment part.

- The experiments are only conducted on the UCR Anomaly Detection dataset, while the recent papers usually conduct experiments on multiple datasets to make the results more convincing (e.g., apart from UCR, AD Transformer also reports the results on SMD , PSM, MSL& SMAP, SWaT,  NeurIPS-TS etc.).

- The compared methods are relatively old (AD transformer is proposed on 2021 and published on 2022), how about compared with some recent  methods (2023 ~ 2024). For example, 

[D3R]  Drift doesn’t matter: Dynamic decomposition with diffusion reconstruction for unstable multivariate time series anomaly detection

[GPT4TS] One fits all: Power general time series analysis by pretrained LM

[ModernTCN] ModernTCN: A modern pure convolution structure for general time series analysis.

[SensitiveHUE]  Sensitivehue: Multivariate time series anomaly detection by enhancing the sensitivity to normal patterns.

- It's hard to say it outperforms ADTransformer on UCR, since the recall of UCR results is higher, there's a trade of between the precision and the recall (F1 measurement usually cannot accurately catch this trade off). Besides, from their paper, the P=72.80, R=99.60, and F1=84.12, which are different from what you reported.

### Questions
- Did you also evaluate on other datasets? Could you share some data points?

- It would be better if you also compared with the recent methods.

- Could you provide some info on why ADTransformer is different from their reported results, and what might be the cause?

### Soundness
3

### Presentation
3

### Contribution
3
