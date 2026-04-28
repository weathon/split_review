# Metadata Matters for Time Series: Informative Forecasting with Transformers

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Time series forecasting is prevalent in extensive real-world applications, such as financial analysis and energy planning. Previous studies primarily focus on time series modality, endeavoring to capture the intricate variations and dependencies inherent in time series. Beyond numerical time series data, we notice that metadata (e.g.~dataset and variate descriptions) also carries valuable information essential for forecasting, which can be used to identify the application scenario and provide more interpretable knowledge than digit sequences. Inspired by this observation, we propose a \textbf{Meta}data-informed \textbf{T}ime \textbf{S}eries \textbf{T}ransformer (MetaTST), which incorporates multiple levels of context-specific metadata into Transformer forecasting models to enable informative time series forecasting. To tackle the unstructured nature of metadata, MetaTST formalizes them into natural languages by pre-designed templates and leverages large language models (LLMs) to encode these texts into metadata tokens as a supplement to classic series tokens, resulting in an informative embedding. Further, a Transformer encoder is employed to communicate series and metadata tokens, which can extend series representations by metadata information for more accurate forecasting. This design also allows the model to adaptively learn context-specific patterns across various scenarios, which is particularly effective in handling large-scale, diverse-scenario forecasting tasks. Experimentally, MetaTST achieves state-of-the-art compared to advanced time series models and LLM-based methods on widely acknowledged short- and long-term forecasting benchmarks, covering both single-dataset individual and multi-dataset joint training settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work explores the forecasting of endogenous time series using both endogenous and exogenous data, alongside metadata. The authors categorize metadata into three types and leverage a pretrained LLM for time series forecasting. The study includes short-term forecasting experiments on five electricity price datasets and long-term forecasting on seven public datasets. The proposed approach is evaluated through comparisons with naive time series models (e.g., PatchTST, iTransformer, Timer) and LLM-based models (e.g., GPT4Ts, TimeLLM).

### Strengths
- The proposed method achieves state-of-the-art performance.
- Leveraging meta data for time series forecasting is an interesting topic. The authors propose a method that employs pretrained large language models to effectively utilize meta data.
- The study includes extensive experimental analysis.

### Weaknesses
 - The performance improvements over SOTA models do not appear significant. Including standard deviation metrics is crucial for a more robust evaluation. If it is unavailable, conducting statistical tests would have strengthened the claims.
- The novelty of the proposed method is limited, as similar concepts and methodologies have been presented in recent works such as TimeLLM, UniTime, PatchTST, and iTransformer. This overlap with other recent methods its novelty.
- While the paper includes numerous experiments, some key experiments supporting the main claims are absent. For instance, a quantitative comparison between models using all three types of meta data and models using only a subset of these types is not provided.
- The paper does not sufficiently analyze how the use of meta data enhances specific aspects of model predictions. A more in-depth examination is needed to identify scenarios where the use of meta data shows clear benefits and where it does not.
- The absence of supplementary code hinders reproducibility, making it challenging for others to replicate the results. 
- It is unclear how meta data was used for datasets such as ETT, ECL, and weather in long-term forecasting. This lack of clarity can reduce reproducibility and is a weakness.

### Questions
1. TimeLLM (ICLR, 2024) also uses pretrained LLMs as encoders to input meta data into the model. What are the distinct novel aspects of MetaTST compared to this approach?
2. In Figure 8, the authors present a sensitivity analysis indicating that MetaTST's performance remains relatively stable with respect to hyperparameter changes. However, in the main text, the reported performance differences among models appear at the third decimal place. Could the authors clarify whether such minimal performance variations imply a significant difference in model effectiveness? 
3. The performance improvement appears minimal. It would be beneficial to conduct a statistical analysis across multiple experimental runs to confirm whether the observed improvement is substantial and consistent.
4. UniTime (WWW, 2024) and TimesFM (ICML, 2024) are both methodologies that employ joint training across multiple domains. UniTime, in particular, incorporates domain-specific instructions to guide the model. It would be helpful to have a clear distinction regarding how MetaTST differs from these techniques. Additionally, while UniTime and TimesFM are designed for univariate input leading to univariate time series forecasting, MetaTST utilizes multivariate input for univariate time series forecasting. It would be insightful to understand whether MetaTST demonstrates superior performance in this context.
5. Many recently proposed time series forecasting methods incorporate instance normalization techniques like RevIN (ICLR, 2022). Could the authors clarify whether the proposed method also utilizes such normalization techniques? Providing clarity on this point would be helpful.
6. Most of the performance evaluations in the main text use T5 as the encoder, but only GPT-2 is used for efficiency analysis. Could the authors clarify the rationale behind this choice? A comparison using T5 would provide a fairer assessment in this context. Additionally, please specify the dataset used for the efficiency measurements. Based on the reported performances, I think the results come from joint training on the BE dataset. 
7. Is Figure 1 based on actual results, or is it simply an illustrative concept? If it is just intended as a conceptual figure, please provide experimental analyses and evidence that support this concept clearly.
8. How was the proposed metadata template constructed? If the same information is provided with variations in the prompt template, does this lead to significant performance differences?
9. For long-term forecasting (Table 3), the input length is set to 96, while the output length is 192 or greater. Could the authors clarify whether this input length might be too short relative to the output length? Would increasing the input length to match or exceed the output length improve performance, potentially reducing the need for metadata? It would be insightful to see the impact on performance when the input length is extended to match the output length.
10. In the ablation study, some datasets show substantial performance differences with and without metadata, while others do not. Could the authors discuss the characteristics of these datasets and possible reasons for this variation? Given that the use of metadata is core component to the paper’s contributions, a detailed analysis would be valuable.
11. Since existing baselines do not include modules for handling metadata, could the authors provide more details on how they adapted the experimental setup for joint training? Specifically, was the setup designed to indicate that data originated from different sources? For instance, would using methods such as one-hot encoding or dataset-specific learnable encodings to identify different data sources enable the baselines to achieve similar performance improvements?

### Soundness
2

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
5

### Summary
The paper presents the Metadata-informed Time Series Transformer (MetaTST), a model that incorporates metadata in time series forecasting using a novel approach where metadata is embedded as language tokens processed through Large Language Models (LLMs). The proposed model aims to improve forecast accuracy by enriching the context of time series data with structured metadata.

### Strengths
Use of Metadata: By integrating metadata through structured natural language tokens, MetaTST significantly enriches the contextual representation of time series data, addressing gaps left by traditional time series models.

LLM Integration as Metadata Encoder: The approach of using LLMs as fixed encoders allows MetaTST to leverage the semantic understanding of LLMs without extensive fine-tuning, thereby maintaining computational efficiency.

Robust Performance: MetaTST achieves state-of-the-art results across several datasets, both in single-dataset and multi-dataset training settings, showcasing its adaptability to various forecasting scenarios.

### Weaknesses
Complexity in Implementation: The use of LLMs as metadata encoders and the structured metadata embedding mechanism might increase the model's complexity, which could be challenging for practitioners to implement. The $h_0$ dimension is too high consisting of three components, a better idea is to try cross attention between these components.

Limited Explanation of Metadata Selection: The paper provides limited detail on the criteria for selecting specific metadata fields and their impact on forecasting accuracy, leaving questions about its generalizability to other domains.

Interpretability Challenges: With multiple embedding and alignment processes, understanding the contribution of each metadata token may be challenging, which affects the model's interpretability.

### Questions
what are the exogenous series in your experiments? In the paper, the model is trained on mixed data from all datasets and then probed in the target dataset.

The paper's objective is to talk about informative forecasting with metadata extends series representation for higher accurate forecasting. But the performance may be from the exogenous series, there is no ablation study ablating exogenous series.

Detaily, the metadata is the same from TimeLLM, the related news or reports would be preferred.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript introduces a framework for time-series forecasting, which integrates dataset-, task-, and sample-level descriptions with endogenous and exogenous series to jointly consider semantic and temporal representations. These representations are concatenated to serve as the inputs of the Transformer, which is different from conventional LLM4TS methods that utilize LLMs as the backbone. The experiments are evaluated on both well-known short-term and long-term time-series forecasting tasks.

### Strengths
1. The major motivation of this work is clearly stated. The idea of incorporating context-specific metadata and exogenous series provides clear contributions.
2. The paper is generally well-written and the proposed framework is intuitive with sufficient discussions in the literature review and intuitive paradigms to provide readability.
3. The experiments on various ranges of time-series forecasting support the authors' claim, especially for the potential to serve as the time-series foundation model.

### Weaknesses
=== AFTER REBUTTAL ===
The authors has resolved most of my concerns and questions. The remaining concerns lie in the need of sample-level metadata as well as the reason that MetaTST could have effective performance in terms of low-resource scenarios.


1. The proposed method may not be able to generalize to the unseen task that does not have metadata. Maybe it has task-level metadata, but dataset- and sample-level seem to have additional efforts to obtain. Specifically, the reliance on detailed dataset-level metadata such as domain and frequency, and sample-level metadata like statistical features and timestamps, raises concerns about the practical applicability of the method in scenarios where such information is not readily available or is costly to acquire. The method's performance might degrade significantly if these metadata components are missing or inaccurate, limiting its real-world utility.
2. The descriptions of the method should be improved. The paper does not describe related details for exogenous series. For example, how are the exogenous series selected for each sequence? How many exogenous series are used for each target series? Do exogenous series contain future records or only historical behaviors? Do the authors use positional encoding when feeding to the Transformer? The lack of clarity regarding the selection and processing of exogenous series makes it difficult to assess the method's robustness and generalizability. The paper should specify whether the exogenous series are chosen based on domain knowledge or data-driven approaches, and whether they include future information, which could lead to unrealistic performance gains.
3. In my opinion, some experiments and discussions should be further improved. The authors should compare their proposed method with more advanced LLM4TS methods, e.g., [1, 2]. In addition, it would be better to include only w/ En., w/ Ex., and w/ Meta to understand where the improvements come from. As one of the main contributions is the incorporation of metadata, the authors should provide the analysis only including single-level metadata.
5. [Minor] There are some numbers different from the original TimeXer paper, e.g., 0.238 -> 0.236 MSE for NP, 0.211 -> 0.208 MAE for FR, 0.418 -> 0.415 MAE for DE. It is not an issue if the authors replicated the experiments. In addition, the number of the long-term forecasting results is significantly different from those baselines (e.g., Table 3 of TimeXer and also significant difference compared with the TimeLLM paper although the given length is slightly different). Please correct me if I misunderstood anything since I didn't find the descriptions in the main text and appendix.

### Questions
1. Regarding sample-level metadata, is it only computed based on the historical records for the target series? Would it be recomputed during forecasting? Given that time-series domains often have periodic patterns (e.g., electricity and weather) [1], I suspect that sample-level could provide an advantage for future forecasting.
2. Could the authors elaborate more on the reason that the embedding processes are different in Eq. 4? How would the performance behave if using PatchEmbed for exogenous series?
3. As the authors state the adjustment in L323 for experiments, do the baselines used in the experiments follow the settings from their papers? I only found the parameters for MetaTST in the appendix, but none for the baselines.

[1] LLM4TS: Aligning Pre-Trained LLMs as Data-Efficient Time-Series Forecasters.

### Soundness
3

### Presentation
3

### Contribution
3
