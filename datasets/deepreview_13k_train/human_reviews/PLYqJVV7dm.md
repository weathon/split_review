# CRAFT: Time Series Forecasting with Cross-Future Behavior Awareness

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Time series forecasting is the crucial infrastructure in the field of e-commerce, providing technical support for consumer behavior analysis, sales trends forecasting, etc. E-commerce allows consumers to reserve in advance. These pre-booking features reflect future sales trends and can increase the certainty of time series forecasting issues. In this paper, we define these features as Cross-Future Behavior, which occurs before the current time but takes effect in the future. To increase the performance of time series forecasting, we leverage these features and propose the CRoss-Future Behavior Awareness based Time Series Forecasting method (CRAFT). The core idea of CRAFT is to utilize the trend of cross-future behavior to mine the trend of time series data to be predicted. Specifically, to settle the sparse and partial flaws of cross-future behavior, CRAFT employs the Koopman Predictor Module to extract the key trend and the Internal Trend Mining Module to supplement the unknown area of the cross-future behavior matrix. Then, we introduce the External Trend Guide Module with a hierarchical structure to acquire more representative trends from higher levels. Finally, we apply the demand-constrained loss to calibrate the distribution deviation of prediction results. We conduct experiments on real-world dataset. Experiments on both offline large-scale dataset and online A/B test demonstrate the effectiveness of CRAFT. Our dataset and code will be released after formal publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CRAFT (Cross-Future Behavior Awareness based Time Series Forecasting), a novel time series forecasting method designed to enhance technical support for consumer behavior analysis and sales trend prediction in the e-commerce sector. CRAFT focuses on "Cross-Future Behavior" (CFB), which refers to features that occur before the current time but take effect in the future, reflecting future sales trends and increasing the certainty of forecasting.

### Strengths
CRAFT is an innovative time series forecasting method that enhances predictive model performance by defining and leveraging Cross-Future Behavior (CFB). It comprises three main modules to address the sparsity and partiality of CFB, as well as to acquire representative trends from higher levels, and calibrates the distribution deviation of forecast results with a demand-constrained loss. CRAFT has demonstrated exceptional performance on real-world datasets, significantly improving prediction accuracy over existing techniques, and has been successfully applied to practical scenarios such as online hotel inventory negotiations. Moreover, its design facilitates further research and development, exploring its potential application in a variety of scenarios.

### Weaknesses
The research on CRAFT, while presenting a significant advancement in time series forecasting, does have certain limitations that can be discussed in terms of real-world data complexity, redundancy, interpretability, and data transferability:

1. **Real-World Data Complexity and Variability:**
   - Real-world data is often characterized by noise, outliers, and non-stationarity, which can affect the model's ability to learn accurate patterns. CRAFT may struggle to capture these complex dynamics, especially if they are not well-represented in the training data. The paper does not provide sufficient detail on how the model handles abrupt changes or anomalies, which are common in real-world time series.

2. **Data Redundancy:**
   - The incorporation of CFB along with other features might lead to data redundancy, which could impact the model's efficiency and potentially its accuracy. There is a need for feature selection techniques to ensure that the information used is diverse and non-redundant, focusing on the most predictive signals. The paper lacks a clear explanation of how feature importance is assessed and how redundant features are handled.

3. **Interpretability:**
   - The black-box nature of some components in CRAFT, such as the Koopman Predictor Module, can make it difficult to interpret how predictions are made, which is a critical aspect for stakeholders who need to understand the reasoning behind the model's outputs. The paper does not offer methods for visualizing or explaining the internal workings of the KPM, making it hard to trust the model's decisions.

4. **Data Transferability:**
   - The model's performance may not be consistent across different domains or datasets due to the unique characteristics of each data environment. The reliance on CFB, which may not be universally applicable, could limit the model's transferability to other contexts where such behavior patterns do not exist or are less pronounced. The paper does not explore the sensitivity of the model to different types of time series data or provide guidelines for adapting it to new domains.

5. **Generalizability:**
   - The study primarily focuses on e-commerce data, and it is unclear how well CRAFT would perform in other industries or with different types of time series data. Further testing and validation on a diverse range of datasets are needed to establish the model's generalizability. The paper should include experiments on datasets from other domains to demonstrate its broader applicability.

6. **Scalability:**
   - The paper does not extensively address the scalability of the CRAFT model, particularly in handling large-scale datasets that are common in many real-world applications. The computational complexity and resource requirements could be a limiting factor. There is no analysis of the model's performance with increasing data size or its suitability for real-time processing.

7. **Robustness to Changing Conditions:**
   - The model's robustness to changing conditions, such as shifts in consumer behavior or market dynamics, is not fully explored. Real-world applications require models that can adapt to new trends and patterns over time. The paper lacks a discussion on how the model can be retrained or adapted to changing market conditions.

8. **Dependency on High-Quality Data:**
   - CRAFT's performance is likely to be highly dependent on the quality and granularity of the input data. In scenarios where data is limited or of poor quality, the model's effectiveness may be compromised. The paper does not discuss how the model performs with missing data or noisy inputs.

### Questions
When evaluating the experimental data and model practices of CRAFT papers, the following are several key ethical and practical issues:
1. Ethical and Privacy Issues of Data:
-Experimental data must ensure compliance with ethical standards, especially regarding the protection of user privacy. Any data containing personally identifiable information should be anonymized to prevent privacy breaches.
2. Data ownership issue :
-The data used needs to have clear ownership and usage rights. Researchers must ensure that they have the right to use this data and that the use of the data complies with the regulations and laws of the data source.
3.   Use publicly available benchmark data for evaluation  :
-To improve the transparency and comparability of model evaluation, publicly available benchmark datasets can be used for evaluation. This helps to validate the generalization ability and performance of the CRAFT model on different datasets.
4.   Generalization ability of the model  :
-The generalization ability of a model is a key factor in evaluating its practicality. The CRAFT model needs to be tested on multiple different datasets to ensure that it not only performs well on specific datasets, but also can be widely applied in various scenarios.
5.   Ensure the stability and security of the model  :
-The stability and security of the model are crucial for its practical application. Strict testing and validation are required to ensure that the model maintains performance under various conditions and is resistant to potential security threats.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces CRAFT (CRoss-Future Behavior Awareness-based Time Series Forecasting), an approach designed to enhance time series forecasting (TSF) in e-commerce by leveraging what the authors term Cross-Future Behavior (CFB). 
The authors define CFB and introduce it as a novel feature in TSF. Unlike traditional features that only use historical data to predict future trends, CFB includes partially observable future behavior, which can provide early indicators of upcoming trends. 
CRAFT integrates CFB through a structured, multi-module framework, including the Koopman Predictor Module (KPM), Internal Trend Mining Module (ITM), and External Trend Guide Module (ETG). 
To further enhance prediction accuracy, CRAFT incorporates a loss function that accounts for upper and lower demand limits. 
The authors validate CRAFT's effectiveness with offline experiments and online A/B tests, showing improvements over state-of-the-art baselines in both error metrics (MAE, RMSE, wMAPE) and application-specific metrics like Inventory Waste Rate (IWR) and Proportion of Hotels with Depleted Inventory (PHDI). 
Overall, CRAFT aims to leverage future behavior patterns effectively to improve TSF, particularly in scenarios where demand is partially predictable through pre-booked actions or similar forward-looking behaviors.

### Strengths
S1. 
The definition of CFB expands the traditional understanding of time series features by including elements that are observable in advance but affect future outcomes.

S2.
This work is evident in its robust methodology and empirical validation. 
The authors employ a well-structured framework composed of three distinct modules—KPM, ITM, and ETG—each addressing specific challenges associated with CFB and time series forecasting.

S3.
This work's demonstrated improvement in forecasting accuracy can have practical implications for businesses, aiding in better resource allocation and inventory management.

### Weaknesses
W1.
First of all, while the introduction of CFB is a strong point, the paper could benefit from a broader exploration of its implications and applications. 
The current formulation primarily focused on e-commerce and hotel booking scenarios. The lack of discussion on how CFB could be adapted or generalized to other domains limits the impact of the proposed method. For instance, the paper does not address whether CFB could be applied in areas like supply chain management, financial forecasting, or energy consumption prediction, where advance knowledge of future events might also be available.

W2.
The experimental section could be improved in several ways.
For example, conducting longitudinal studies to evaluate how CRAFT performs over extended periods or under different market conditions would add depth to the findings. The current experiments appear to be limited in scope, and it is unclear how the model would perform in the long term or under significant shifts in market dynamics. It would be valuable to see results that demonstrate the model's robustness and adaptability over time. Furthermore, the paper lacks a detailed analysis of the computational cost associated with the proposed method, which is crucial for practical deployment.

W3.
- A systematic sensitivity analysis could be conducted to understand how hyperparameter variations affect the model’s predictions. This would help practitioners better tune CRAFT for their specific applications. The paper does not provide sufficient guidance on how to select optimal hyperparameters for different datasets or scenarios. The absence of such analysis makes it difficult to assess the model's reliability and generalizability.

- Providing specific guidelines for selecting hyperparameters based on data characteristics could enhance the practical utility of the model. The current lack of clear guidelines makes it challenging for practitioners to effectively implement and optimize the model for their specific use cases.

### Questions
Q1.
How do you envision CFB being applied in domains beyond e-commerce? 
Could you provide specific examples or potential use cases in different sectors?

Q2.
Have you considered conducting longitudinal studies to evaluate the stability and performance of CRAFT over time? 
What are the challenges you foresee in such an analysis?

### Soundness
2

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
This paper focuses on the application of time series in the field of e-commerce, attempting to incorporate e-commerce characteristics into the model building process and proposing the concepts of CFB and the CRAFT model. In the model design process, the authors drew inspiration from a lot of previous work, combining them to form the CRAFT model. Finally, some experiments were conducted by the authors to demonstrate the effectiveness of the proposed model.

### Strengths
1. The field of time series forecasting that this paper focuses on is worth studying.

2. The structure of the article is relatively complete.

### Weaknesses
1. The research motivation has significant issues. Although there are instances in e-commerce where actions are taken at a past moment for a future one, it is evident that they are entirely corresponding. Changes in final labels can be understood as minor variations based on the booking situation. Therefore, even though the actual future events have not occurred at the current time, crucial actions that influence the future have already taken place in history. Introducing the so-called CFB data essentially involves bringing in a part of real future data, thus constituting data leakage. This approach is fundamentally distinct from previous attempts to introduce more features because earlier works aimed at extracting or learning more features from historical time series data without any data leakage.

2. There are serious shortcomings in the survey of time series forecasting methods. The author noted PatchTST from ICLR 2023 but overlooked contemporaneous models such as TimesNet (CNN-Based) and MICN (CNN-Based). The author mentioned Koopa from NeurIPS 2023 but failed to acknowledge concurrent models like WITRAN (RNN-Based) and Basisformer (Attention-Based). Furthermore, no attention was given to any time series forecasting methods from ICLR 2024, such as FITS (MLP-Based), TimeMixer (MLP-Based), ModernTCN (CNN-Based), and iTransformer (Attention-Based).

3. The model lacks innovation, as the designs in KPM, ITM, and ETG are primarily derived from previous works, making it challenging to identify entirely independently innovative content.

4. Code was not provided, leading to poor reproducibility of experimental results.

5. The experiments are insufficient as the methods compared are relatively older works and do not comprehensively prove the efficacy of the experiments. Additionally, the method proposed by the author can only be applied under the assumption of data leakage through CFB, making its applicability weak for scenarios with only labels. Moreover, in Table 2, it is evident that in certain instances, utilizing only labels yields better results compared to using CFB in nearly every baseline method. This further indicates that the effectiveness of CFB is not necessarily proven.

6. The author did not present the full search space for reproducing the baselines. Results can vary significantly for the same parameters on different platforms. Therefore, a fair approach would involve setting a consistent search space for all methods on the same platform and determining the best parameters for each model on various tasks using a validation set. I noticed that the experimental platform used by the author is inconsistent with the platforms of the compared methods, so the author should address this to demonstrate the credibility of the experiments. Otherwise, it is challenging to eliminate the significant impact of parameter selection on the experimental conclusions.

### Questions
1. Can the author provide the search space and optimal parameters for all methods in all tasks?

2. Can the author provide the code and a small portion of the dataset for reproducibility purposes?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces CRAFT, a Cross-Future Behavior Awareness-based Time Series Forecasting model, designed to enhance time series predictions by leveraging future-aware information that occurs prior to the forecast period but has future relevance. CRAFT incorporates the trend of Cross-Future Behavior (CFB) into time series forecasting, addressing challenges like the sparsity and unpredictability of CFB through modules specifically crafted for key trend extraction, internal trend completion, and hierarchical guidance.Offline benchmarks and online A/B tests  validate CRAFT’s effectiveness, showing improvements over established models in both accuracy and practical forecasting metrics. The results highlight CRAFT’s potential to enhance forecasting performance in complex, real-world scenarios.

### Strengths
1. The paper presents an innovative approach to time series forecasting by incorporating Cross-Future Behavior (CFB), which effectively captures future events that impact the forecast. This concept is novel and valuable, especially for applications like e-commerce and hotel bookings where advance information is critical.
2. The proposed CRAFT framework is comprehensive, utilizing three modules—Koopman Predictor Module (KPM), Internal Trend Mining Module (ITM), and External Trend Guide Module (ETG)—to tackle challenges related to CFB, such as sparsity and trend ambiguity, thereby improving forecasting accuracy.
3. The inclusion of demand-constrained loss is a notable strength, as it aligns the model’s predictions more closely with practical constraints in real-time applications.

### Weaknesses
### weaknesses:
 1. The citation in line 54 regarding the series decomposition method used in DLinear appears to be inaccurate. The method originates from Autoformer, and it decomposes the time series into trend and seasonal components, not trend and remainder components. This discrepancy should be addressed to ensure the accuracy of the paper's background information.
2. The description in Table 2 is unclear, particularly the phrase “Comparative forecasting results with the look-back window length $L$ and prediction window length $P$ respectively.” The look-back window length $L$ is not displayed in the table, which creates confusion. A more precise explanation of the parameters used in the table is needed.
3. The paper suffers from inconsistent notation. For example, the notation near line 152, $C_t = \{C_{t−L+1:t}, C_{t+1:t+P}\}$, implies an infinite inclusion by reusing the same $C$. Additionally, the forecasting length is denoted by both $K$ and $L$ in Section 5, leading to confusion. A thorough review and standardization of the notation throughout the paper are necessary.

### Questions
1. TSMixer also uses future features for time series forecasting and evaluated the model on the M5 dataset, where auxiliary information like promotions and vacations are provided, similar to the “CFB” in your work. How does your method compare to TSMixer in this context?
2. The introduction refers to two main challenges, but these are not clearly defined. Could you elaborate on these challenges?
3. In Table 2, why does a longer prediction window generally result in lower error? Typically, a larger forecasting horizon is more challenging due to increased uncertainty.

### Soundness
2

### Presentation
2

### Contribution
2
