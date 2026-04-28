# Partial Channel Dependence with Channel Masks for Time Series Foundation Models

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 6, 6, 3, 5

## Abstract
Recent advancements in foundation models have been successfully extended to the time series (TS) domain, facilitated by the emergence of large-scale TS datasets.
However, previous efforts have primarily focused on designing model architectures to address explicit heterogeneity among datasets such as various numbers of channels, while often overlooking implicit heterogeneity such as varying dependencies between channels.
In this work, we introduce the concept of \textit{partial channel dependence} (PCD), which enables a more sophisticated adjustment of channel dependencies based on dataset-specific information.
To achieve PCD, we propose a \textit{channel mask} that captures the relationships between channels within a dataset using two key components:
1) a \textbf{correlation matrix} that encodes relative dependencies between channels, and
2) \textbf{domain parameters} that learn the absolute dependencies specific to each dataset, refining the correlation matrix.
We validate the effectiveness of PCD across four tasks in TS including forecasting, classification, imputation, and anomaly detection, under diverse settings, including few-shot and zero-shot scenarios with both TS foundation models and single-task models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the limitation that time series models often consider only explicit heterogeneity among datasets, such as varying sequence lengths and numbers of channels, while overlooking implicit heterogeneity like channel dependencies within the data. The authors propose a module called the Channel Mask (CM) to enable models to reflect channel dependence (CD) by adjusting the degree of CD based on dataset characteristics, achieving Partial Channel Dependence (PCD). By integrating CM into existing time series models, they demonstrate improved performance across various time series tasks.

### Strengths
1. The paper critiques the limitations of using correlation coefficients for measuring inter-channel relationships and proposes a new way to measure channel dependence through the CD ratio. The CM introduces very few parameters (α and β from domain parameters) yet effectively learns the implicit inter-channel relationships, leading to performance improvements in time series models.

2. The authors validate their approach through various experiments, including few-shot and zero-shot settings, and provide thorough ablation studies and analyses to demonstrate the effectiveness and suitability of the CM structure and its relationship with CD.

### Weaknesses
1. The paper lacks theoretical grounding or in-depth analysis to explain why the proposed method leads to performance improvements. A deeper understanding of the underlying mechanisms would clarify and strengthen the contribution.
1.1. For example, how can (or how should) we define the concept of “implicit heterogeneity”? Why do we need this concept? While there are studies on channel dependence in time series machine learning, is the concept in this work different from existing studies? Furthermore, how is the rigorous definition of implicit heterogeneity connected to the proposed CM method?  What is the rationale behind the use of correlation information between different real-world time series datasets in different domains to achieve better performance?
1.2. For another example, while the use of correlation matrices primarily captures linear relationships between channels, the application of a sigmoid function in the CM introduces nonlinearity to the model. The authors mention that static correlations (global CD) are reflected through the CM, while dynamic, local correlations are captured by the attention mechanism. This design may help address some aspects of nonlinearity and temporal variation in channel dependencies. However, it remains a question whether this approach is fully sufficient to reflect the complex and changing characteristics inherent in time series data. A clear explanation of the rationale behind how the CM models these dynamic changes, or further investigation into its effectiveness in this regard, would strengthen our understanding. These considerations might be related to the rigorous definition of implicit heterogeneity in time series.
1.3. Meanwhile, the authors state that “However, most previous works have focused on the model architecture to either capture or disregard CD, often overlooking the potential differences in CD across datasets.” However, they do not show specific theoretical analysis results on why and how existing studies on the model architecture are limited in capturing the differences in CD across datasets.

2. The technical contribution is also limited.
2.1. Following the above comment, the claim that existing CD models overlook differences in CD between datasets may not be fully substantiated. Since models like Crossformer, iTransformer, and TimeSiam learn attention patterns specific to each dataset, it's unclear whether they truly neglect dataset-specific CD differences.
2.2. While the authors introduce PCD as an intermediary concept between channel independence (CI) and channel dependence (CD), the structure of CM, which uses a channel correlation matrix, cannot be applied to CI models. The study applies CM to CD models (iTransformer, UniTS) and shows performance improvements but does not verify whether applying CM to CI models can enhance performance. Thus, the proposed PCD cannot be extended to CI settings, limiting its utility in models that assume channel independence.
2.3. The CM seems to be applicable only to Transformer models that apply attention along the channel axis and cannot be applied to models that apply attention along the time axis. For instance, existing studies like ST-MEM [1] and UniTST [2], which learn CD by applying attention along the time axis after channel flattening, cannot utilize CM. This limitation reduces the general applicability of the proposed method to other architectures.
2.4. The CD ratio proposed in the study is calculated after combining CM with the time series model and training, and its value may vary depending on the model used. The paper does not provide sufficient evidence to demonstrate that the CD ratio is consistent across different models for the same dataset, raising concerns about its adequacy as a metric for measuring channel dependence.
2.5. Meanwhile, although the authors started their argument from the emergence of time series foundation models (TSFMs), they do not provide sufficient validation of this work for different TSFMs.

### Questions
Please see the weaknesses. Some other (related) questions are as follows.
1. In the experiments involving TimeSiam, which encoder was used? The TimeSiam paper proposes both PatchTST (CI properties) and iTransformer (CD properties) as encoders. Since they have different characteristics, specifying the encoder used is essential. Additionally, since TimeSiam is utilized for classification tasks in your paper, it should be categorized appropriately, and the performance of CM + TimeSiam in classification tasks should also be evaluated.
2. The CI framework does not attend between channels but attends with timestamps or patches in each channel. Then, how is the formulation of A in equation (1) justified as the identity matrix in equation (1) indicates the channel relationship? For example, how does PatchTST match to this formulation?
3. Is the CD ratio consistent across different models for the same dataset? To establish the CD ratio as a reliable metric for measuring dataset CD, it should be verified whether CD ratios computed using different models (e.g., iTransformer vs. UniTS) yield consistent results.
4. Since the CM has been validated on datasets with significant CD, it would be beneficial to test its performance on synthetic datasets with uncorrelated channels to verify that CM yields a low CD ratio and does not introduce unnecessary dependencies.
5. Time series data often exhibit non-stationarity, which can affect correlation measures. How does your method handle non-stationary data, and does the CM adjust for changes in channel dependencies over time?
6. Have you considered other measures that can capture nonlinear or more complex dependencies between channels, such as mutual information? This could potentially enhance the CM's ability to model complex inter-channel relationships.

### Soundness
1

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
3

### Summary
The paper introduces a novel concept called Partial Channel Dependence (PCD) to address implicit heterogeneity in time series data, specifically focusing on varying dependencies between channels. The authors propose a channel mask mechanism that combines correlation matrices (for relative dependencies) with learned domain parameters (for absolute dependencies). The approach is evaluated across multiple time series tasks (forecasting, classification, imputation, and anomaly detection) in both few-shot and zero-shot settings, demonstrating its versatility across different foundation models and single-task models.

### Strengths
- Introduces a novel methodology for handling channel relationships specifically designed for pretraining foundation models in time series
- Proposes a systematic framework for incorporating dataset-specific channel dependencies into the pretraining process
- Demonstrates superior performance in challenging scenarios (few-shot and zero-shot learning)

### Weaknesses
 - **Dataset Identification Requirement**: The method requires knowing exactly which samples belong to which dataset during pretraining. This is a strong assumption that may not hold in real-world applications where data sources might be mixed or unclear.
- **Lack of Fixed vs. Variable Dependency Analysis**: The paper assumes variable channel dependencies are necessary but doesn't justify why a simpler fixed dependency structure wouldn't work equally well. Without this comparison, the added complexity of variable dependencies might be unnecessary.

- **Missing Critical Baseline Comparison**

    - No comparison against the same architecture with full channel dependence
    - No comparison against the same architecture with full channel independence

### Questions
- Can you provide comparisons of your method against the same architecture with full channel dependence and full channel independence?
- What theoretical guarantees or analysis can you provide to show when partial dependence would outperform the extreme cases?
- How does your method handle scenarios where dataset boundaries are ambiguous or when data comes from multiple unknown sources?
- Can you quantify the computational overhead and memory requirements of your approach compared to full dependence and independence cases?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Partial Channel Dependence (PCD), a method designed to capture the varying dependencies between channels across different datasets. PCD achieves this by applying channel-wise attention multiplied by the corresponding dataset mask. Experimental results demonstrate that PCD yields an average performance improvement across various time series tasks.

### Strengths
* The method is straightforward, and the motivation is clearly articulated.
* Extensive experiments across various scenarios validate that PCD enhances the performance of Transformer-based multivariate time series models.

### Weaknesses
 * The results for iTransformer and PatchTST presented in Table 3 differ significantly from those reported in the original papers. Additionally, the ETTh2, ETTm1, and ETTm2 datasets are well-known multivariate time series datasets. Could you please provide a comprehensive comparison of the same baselines on these datasets across all prediction lengths?
* While PCD does enhance the performance of Transformer-based models for multivariate time series forecasting, I recommend including recent MLP-based and CNN-based models in the baselines, such as RLinear and ModernTCN. Additionally, GNN-based models like CrossGNN are also adept at capturing multivariate relationships. Including these would strengthen the performance comparisons.
* The length of the input time series is an important factor influencing experimental results. Therefore, I would like to see the impact of varying sequence lengths on the results w CM and w/o CM.
* There are several literature on channel dependency modeling, such as [1-2]. Detailed discussion is needed.

### Questions
1.	Could the authors apply a similar masking approach to CI models like PatchTST or PITS, and compare their performance across different datasets? If possible, please provide performance comparisons for the original settings w CM and w/o CM.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work introduces the concept of partial channel dependence (PCD) to address implicit heterogeneity in time series (TS) data. By utilizing a channel mask that incorporates a correlation matrix to encode relative dependencies between channels and domain parameters to learn dataset-specific absolute dependencies, the authors refine the correlation matrix for better channel dependency adjustments. The effectiveness of PCD is validated across four TS tasks—forecasting, classification, imputation, and anomaly detection.

### Strengths
1. This work focuses on a highly valuable research direction and highlights the importance of Partial Channel Dependence in Time Series analysis.
2. This work proposes a concise approach to adjust the correlation matrix obtained from prior knowledge.

### Weaknesses
 1. The concept of Partial Channel Dependence (PCD) is already discussed in the CCM[1] where the authors employ a clustering approach to capture latent PCD. The current content lacks a detailed comparison and discussion with this work.
 2. It is important to note that not all foundation models are based on attention mechanisms (TTM [2]), and not all methods that utilize attention mechanisms effectively capture the attention between channels like UniTS (TimesFM[3], Timer[4], MOIRAI[5], MOMENT[6]). As a plugin for foundation models, the generality of the CM method is insufficient.
 3. The paper does not specify how the correlation matrix mentioned was constructed, and references [7] and [8] primarily focus on capturing correlation relationships with lag properties. In contrast, this work does not explore lag properties but instead utilizes the complete sequences. The construction method of the correlation matrix needs to be explained in detail.
 4. Domain parameters highly correlated with the construction method of the correlation matrix, If use other methods, they may not be effective. The effectiveness of domain parameters in the experiments lacks further validation.
 5. In the experiments, there is a lack of comparison with other plugins, such as LIFT[8], and each task only validates the plugin's improvement on a few models, making its generality difficult to confirm. More importantly, a large number of foundation models have not been considered in the experiments, such as [2-6]. The existence of these issues raises serious doubts about the effectiveness and generality of the plugin.

### Questions
See weaknesses.

### Soundness
1

### Presentation
2

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
This work proposes a time-series foundation model designed to capture varying channel dependencies across different datasets. By using a correlation matrix as a prior, the model incorporates a learnable domain parameter to construct a domain-specific channel mask, effectively capturing global channel dependencies. In conjunction with local channel dependency masks (as introduced in prior works, such as iTransformer), the proposed model accommodates diverse channel dependencies across datasets, leading to performance improvements in tasks such as forecasting, imputation, and anomaly detection (in full-shot, few-shot, and zero-shot settings).

### Strengths
- The paper presents a straightforward algorithm with clear explanations.
- The manuscript covers a broad range of experiments across various time-series tasks (anomaly detection, forecasting, imputation, etc.) in different settings (supervised, few-shot/zero-shot domain/task) with extensive analyses (e.g., robustness to missing values) that support its claimed advantages.
- The newly introduced experiment, "masked channel prediction," is particularly novel and promising, though it is only briefly discussed in the manuscript.

### Weaknesses
Despite the demonstrated performance gains across multiple tasks and settings, some of the motivation and design choices remain insufficiently addressed in the manuscript. Additionally, certain reported experimental results differ from what appears in the paper, and key experimental details are not fully explained.

First, I would appreciate clarification from the authors regarding the principles underlying channel dependency in the proposed time-series foundation model:

- Why is it crucial to account for varying channel dependencies? To what extent is this heterogeneity in channel dependency necessary for constructing a robust foundation model for time-series data? Prior research has highlighted its importance for forecasting tasks both empirically [1][2] and theoretically [3], yet the rationale for its role in the foundation model is not fully studied. What is the anticipated impact of the time-series foundation model, and how does it address channel dependencies? (Simply stating "inherent heterogeneity" may be insufficient in this context.) Specifically, how does the model differentiate between scenarios where channels are inherently independent versus those where dependencies are present but vary across datasets? The manuscript needs to articulate the specific mechanisms by which the model adapts to these different scenarios.
- The global mask encapsulates correlation across various domains during training, which is then reused during testing without further adjustment. Is it sufficient to rely on the global correlation matrix alone? Since local correlations may vary over time, the correlation matrix at test time might differ significantly from that during training. How do you ensure its stability under these conditions? The paper should discuss the potential for the global correlation matrix to become outdated or irrelevant as temporal dynamics shift, and how the model mitigates this issue. Furthermore, the manuscript should provide empirical evidence of the stability of the learned global correlation matrix across different time periods.
- Is correlation an appropriate metric for capturing channel dependencies? Some studies in forecasting suggest a "causal relationship" between channels, while others tackle spurious correlations (where channels appear correlated but are not causally related). The paper should justify the use of correlation over other metrics, such as Granger causality, especially given that the model is applied to time-series data where temporal precedence and causation are often relevant. The manuscript should also discuss the potential limitations of using correlation, particularly in the presence of spurious correlations, and how this might affect the model's performance.

Furthermore, several design choices would benefit from clarification:

- What motivated the choice to use domain-specific global attention while sharing local attention across multiple domains? What specific roles do global and local attention play in the model's functioning? The manuscript should provide a more detailed explanation of why global attention needs to be domain-specific while local attention does not, and how this design choice aligns with the goal of capturing varying channel dependencies. It should also discuss the potential limitations of this approach, such as the possibility of overfitting to domain-specific global dependencies while neglecting important local variations.
- Is the "pair-wise dot product" between global and local attention sufficient to achieve the intended effect? Under extreme test-time scenarios where variables v1 and v2 exhibit low global correlation (approaching zero) but high local correlation, this design might yield low attention scores, potentially failing to capture abrupt correlation increases under certain test-time conditions. The paper should discuss the implications of this design choice, particularly in cases where local correlations are strong but global correlations are weak, and how this might affect the model's ability to adapt to sudden changes in channel dependencies. It should also explore alternative methods for combining global and local attention that might be more robust to these scenarios.

In addition, some minor experimental inconsistencies and essential experimental details require clarification:

- Some scores of baselines appear lower than what has been reported in the original paper. In Table 3, the MSE/MAE score on iTransformer is way higher than it has been reported (Appendix F, Table 8 in [4]) Have these results been reproduced, and if so, what could account for the discrepancies? The manuscript should provide a detailed account of the reproduction process, including the specific hyperparameters used and any modifications made to the original code. It should also discuss potential reasons for the discrepancies, such as differences in data preprocessing or random initialization.
- How is the global correlation matrix defined? Does it only consider the correlation matrix over the training period? The paper should clearly specify whether the global correlation matrix is computed using the entire dataset or only the training data, and justify this choice. It should also discuss the potential impact of this choice on the model's performance, particularly in cases where the distribution of the training data differs significantly from the test data.
- In zero-shot experiments on new datasets, how is the domain parameter handled? As the domain parameter cannot be directly learned for unseen domains, is it substituted with that of a similar domain? The manuscript should provide a detailed explanation of how the domain parameter is handled in zero-shot settings, including the criteria used to select a similar domain and the potential limitations of this approach. It should also discuss the potential impact of this choice on the model's performance, particularly in cases where the selected domain is not truly representative of the unseen data.

### Questions
In conclusion, while the paper presents an extensive array of experimental evidence, the motivation for addressing channel dependency heterogeneity is not entirely convincing in terms of its necessity for building a foundational model. Although channel dependencies may be relevant to specific tasks in the time-series domain (e.g., forecasting), the underlying rationale and its influence on design choices are not fully explained in the manuscript. Additionally, certain key experimental results appear inconsistent, which is problematic given the paper's emphasis on empirical performance gains over theoretical justification. Nevertheless, the proposed architecture is straightforward and appears tailored to address varying channel dependencies, and it has the potential to be impactful if the dependencies are better elucidated and some of the reported results are clarified.

If the authors address these points and resolve potential experimental issues in the main results table, I would be inclined to raise my rating.

### Soundness
2

### Presentation
3

### Contribution
2
