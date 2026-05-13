# Dual-Forecaster: A Multimodal Time Series Model Integrating Descriptive and Predictive Texts

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Time series forecasting plays a vital role for decision-making across a wide range of real-world domains, which has been extensively studied. Most existing single-modal models rely solely on numerical series, which suffer from the limitations imposed by insufficient information. Recent studies have revealed that multimodal models can address the core issue by integrating textual information. However, these models focus on either historical or future textual information, overlooking the unique contributions each plays in time series forecasting. Besides, these models fail to grasp the intricate relationships between textual and time series data, constrained by their moderate capacity for multimodal comprehension. To tackle these challenges, we propose Dual-Forecaster, a pioneering multimodal time series model that combines both descriptively historical textual information and predictive textual insights, leveraging advanced multimodal comprehension capability. We begin by developing the historical text-time series contrastive loss to align the descriptively historical textual data and corresponding time series data, followed by encoding multimodal text-time series representations between them through the history-oriented modality interaction module, and then combining predictive textual data through the future-oriented modality interaction module to ensure textual insights-following forecasting. Our comprehensive evaluations on synthetic dataset and captioned-public datasets demonstrate that Dual-Forecaster is a distinctly effective multimodal time series model that outperforms or is comparable to other state-of-the-art models, highlighting the superiority of integrating textual information for time series forecasting. This work opens new avenues in the integration of textual information with numerical time series data for multimodal time series analysis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel text-guided time series forecasting model, named Dual-Forecaster, which leverages both historical and predictive textual data to enhance forecasting accuracy. This model has been evaluated using synthetic and real-world datasets, demonstrating superior performance.

### Strengths
- The paper is well-organized and easy to follow. 

- The model architecture is well explained and seems to be solid. 

- The ablation study, particularly the alignment heatmap between time series patterns and textual descriptions, provides in-depth understanding on how the model actually works.

### Weaknesses
 - The task definition may need further discussion. The statement right now is clear. However, the practicality of the task definition could be better justified, specifically regarding the availability of caption data in real-world applications.

- There may be potential information leakage in this setting/dataset used. According to the TGTSF [1] cited in related work, to avoid directly using the information in the future time series, it is advisable to use the text information from external sources that is related to the system we are analyzing. 

- The captioning process of public dataset needs further discussion. Directly asking the GPT to describe the time series may not be a promising method.
    - The GPT's ability of processing numerical values still remains under discussion. Asking it to generate description of time series which is also a sequence of float values, may suffer from severe hallucination problem. 
    - As mentioned above, since the textual descriptions are derived directly from the time series data, there is a risk of information leakage, particularly if these descriptions are used for future predictions.
    - It seems that the captioned textual information also contains numerical values. It is still questionable that if the information in these values still remains after the text embedding model, i.e. RoBERTa in this paper. 

- According to the ablation study, this work seems to fall into the category of aligning time series pattern and textual description. Maybe it is a better idea to apply this to classification and anomaly detection task, which is not very sensitive to the information leakage problem. 

[1] Zhijian Xu, Yuxuan Bian, Jianyuan Zhong, Xiangyu Wen, and Qiang Xu. Beyond trend and periodicity: Guiding time series forecasting with textual cues.

Minor:

- Some figures are hard to read, e.g. Figure 3 & 5.

### Questions
- How are the future-oriented predictive text generated? It seems that authors use the known time series for caption to generate the description for trend and periodicity. This is reasonable for the look-back window part of each training sample, but using the caption for forecasting horizon may lead to severe information leakage. 

- See Weakness.

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
This paper introduces a time series forecasting model that incorporates both historical and future textual data to improve forecasting accuracy. The proposed model, Dual-Forecaster, uses two main branches: a textual branch for embedding historical and predictive texts and a temporal branch for numerical time series data. It employs three cross-modality alignment techniques—contrastive loss, history-oriented, and future-oriented modality interaction modules—to align and integrate information across these modalities. Experimental results on synthetic and public datasets demonstrate that Dual-Forecaster outperforms baseline models by leveraging multimodal comprehension, thus underscoring the value of textual insights in time series forecasting. The study opens new pathways for integrating diverse data types to enhance predictive performance across various real-world applications.

### Strengths
- The paper is well-structured and clearly written, with a logical organization that makes it easy to follow the development of ideas. The authors include illustrative figures, such as the model architecture and case studies, which aid in understanding the Dual-Forecaster model’s interactions and multimodal integration strategies.
- The methodology is clearly presented, and the cross-modality alignment techniques—contrastive loss, history-oriented, and future-oriented interaction modules—are well-integrated within the model. These mechanisms aim to capture complex relationships between text and time series data, contributing to the overall approach.
- The experimental results are strong, including evaluations on synthetic and real-world datasets as well as ablation studies. The results indicate that the proposed components have a positive impact on performance, providing evidence of Dual-Forecaster’s potential effectiveness in multimodal time series forecasting.

### Weaknesses
 - **Missing Baseline Comparison**: The authors reference the paper "Beyond Trend and Periodicity: Guiding Time Series Forecasting with Textual Cues" by Xu et al. (2024), yet they do not conduct a comparison experiment with this approach. Given the conceptual similarity between the two models, it is crucial to include this as a baseline to demonstrate any distinct advantages of the proposed method. The absence of this comparison leaves a significant gap in the evaluation of the model's novelty and performance.
- **Over-reliance on Synthetic Data and Limited Real-world Testing**: While the paper includes evaluations on both synthetic and public datasets, the reliance on synthetic data limits the applicability of the results. Synthetic setups with artificial textual descriptions do not reflect the complexities and nuances of real-world time series data. The public datasets used (e.g., ETTm1, ETTm2) are also limited in variety and complexity. To strengthen the paper, the authors should include more challenging datasets, such as exchange rates or stock indices, which better represent real-world scenarios. Additionally, the paper lacks evaluation on how the model handles noisy or misleading textual data—an issue highly relevant in real-world, high-stakes contexts. The lack of robustness testing against noisy or irrelevant text inputs is a critical oversight, particularly given the model's reliance on textual data.
- **Limited Justification for Dual Textual Modality** The inclusion of both historical (descriptive) and future (predictive) textual information is presented as a core feature, yet the paper provides limited justification for this design choice. It is unclear whether this dual modality substantially enhances forecasting or if similar results could be achieved using only one type of text. A direct ablation study comparing the use of single versus dual text modalities would help clarify this. The ablation study provided is insufficient, as it only considers the ETTm2 dataset, and does not generalize to other datasets, especially the newly added exchange rate and stock data.
- **Error Bounds Missing** The paper does not report error bounds or standard deviations for the results across multiple runs. This omission makes it difficult to assess the consistency and robustness of the reported performance improvements. Including error bounds would provide a more rigorous evaluation of the model's stability.

### Questions
- Have you considered simply combining the historical and future texts into a single input rather than using separate modules to handle them? This approach could reduce model complexity. How do you anticipate that combining the texts would affect forecasting performance, and is there evidence that using separate modules significantly enhances results?
- How would your captioning method perform on more complex and volatile datasets, such as exchange rates or stock indices, where trends and patterns are less predictable? Given that these types of data often contain abrupt changes and noise, would your approach to generating textual descriptions still produce reliable or meaningful captions?
- Real-world applications, especially in high-stakes domains like finance, often include noisy or misleading textual data. How does your model handle such cases where the text may not accurately reflect trends in the time series? Have you tested the robustness of Dual-Forecaster with noisy or contradictory textual inputs, and if not, could you discuss any mechanisms that could be added to mitigate potential misdirection from unreliable text?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Dual-Forecaster, a novel multimodal time series forecasting model that integrates both historical and future textual data with numerical time series data. The model is designed to improve forecasting performance by leveraging rich semantic information from textual data, which traditional time series models often lack.

### Strengths
1. The paper presents a novel approach to time series forecasting by integrating both historical and future textual data, which is a creative extension of existing multimodal time series models. This work has the potential to significantly impact the field of time series forecasting by demonstrating the value of incorporating textual data. 
2. The extensive experiments and ablation studies provide robust evidence of the model's effectiveness and the importance of each component.

### Weaknesses
1. Although utilizing predictable future textual information is a commendable effort, I am concerned that in synthetic data and captioned datasets, the inclusion of predictable future textual information may lead to information leakage (where they represent future ground truth), potentially resulting in unfair comparisons with other models and an overestimation of this model's performance. The core issue is that the model is trained and evaluated with future textual data that is unrealistically accurate and predictive, which is unlikely to be available in real-world scenarios. This discrepancy between training/testing data and practical application data raises serious concerns about the model's actual utility.
2. While the paper focuses on time series forecasting, it does not explore the potential of Dual-Forecaster in other multimodal time series analysis tasks (Imputation, Anomaly Detection, etc.). Expanding the scope could provide a more comprehensive evaluation of the model's capabilities.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Based on transformer, this paper introduces Dual-Forecaster, a multimodal time series forecasting model designed to enhance prediction accuracy by integrating both numerical time series data and corresponding textual information, where the data is used and aligned to help time-series prediction task. To effectively merge these modalities, Dual-Forecaster incorporates three cross-modality alignment techniques: Historical Text-Time Series Contrastive Loss, History-oriented Modality Interaction Module, Future-oriented Modality Interaction Module.

### Strengths
1. Point out the information insufficiency problem, which I agree.
2. The model is clean and simple, and it works well in synthetic data. The use of pre-trained model and its application is acceptable.

### Weaknesses
1. I wonder how to use the model as the textual data is well-designed, and it seems that it performs bad when I don't input. For most of the users, I just wanna use the model as quick as possible.
2. What about I use wrong information in texts, this interests me. 
3. The example is too simple in Figure2
4. Compare with some multi-modal approach, (TIME-LLM eg.). the comparison is weak.
5. give more ablation study including pre-trained model.

### Questions
1. explain why textual data, in particular, is the most effective supplementary modality
2. why use the contrastive loss ?

### Soundness
3

### Presentation
3

### Contribution
3
