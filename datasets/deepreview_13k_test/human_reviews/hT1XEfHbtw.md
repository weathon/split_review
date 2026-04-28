# Variational Mode Decomposition and Linear Embeddings are What You Need For Time-Series Forecasting

- Decision: Reject
- Scores: 1, 3, 3, 8

## Abstract
Time-series forecasting often faces challenges due to data volatility, which can lead to inaccurate predictions. Variational Mode Decomposition (VMD) has emerged as a promising technique to mitigate volatility by decomposing data into distinct modes, thereby enhancing forecast accuracy. In this study, we integrate VMD with linear models to develop a robust forecasting framework. Our approach is evaluated on 13 diverse datasets, including ETTm2, WindTurbine, M4, and 10 air quality datasets from various Southeast Asian cities. The effectiveness of the VMD strategy is assessed by comparing Root Mean Squared Error (RMSE) values from models utilizing VMD against those without it. Additionally, we benchmark linear-based models against well-known neural network architectures such as LSTM, BLSTM, and RNN. The results demonstrate a significant reduction in RMSE across nearly all models following VMD application. Notably, the Linear + VMD model achieved the lowest average RMSE in univariate forecasting at 0.619. In multivariate forecasting, the DLinear + VMD model consistently outperformed others, attaining the lowest RMSE across all datasets with an average of 0.019. These findings underscore the effectiveness of combining VMD with linear models for superior time-series forecasting.git}

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This study addresses the challenge of data volatility in time-series forecasting by employing Variational Mode Decomposition (VMD) to enhance prediction accuracy. VMD decomposes data into distinct modes, which, when integrated with linear models, creates a robust forecasting framework. Tested on 13 datasets (ETTm2, WindTurbine, M4, and air quality data from Southeast Asia), the approach shows that models using VMD outperform those without it, as evidenced by lower Root Mean Squared Error (RMSE) values. The Linear + VMD model achieved the best RMSE in univariate forecasting (0.619), while the DLinear + VMD model excelled in multivariate forecasting with an average RMSE of 0.019. This highlights the advantage of combining VMD with linear models for effective time-series forecasting.

### Strengths
* The paper explores enhancing time series forecasting using Variational Mode Decomposition (VMD).
* The proposed approach is tested across 13 diverse time series datasets.

### Weaknesses
* The focus is on point forecasting, whereas probabilistic forecasting would be more relevant and challenging for many practical applications.
* The statement "Data decomposition techniques also significantly influence forecasting outcomes," supported by only two citations, lacks sufficient evidence for this claim.
* Phrases such as "to mitigate data volatility" and "under unstable data conditions" are used without clarifying how the proposed method directly addresses these issues.
* Key references are missing in the related work, such as [https://dl.acm.org/doi/full/10.1145/3533382](https://dl.acm.org/doi/full/10.1145/3533382).
* Section 3, the main one, is challenging to read, with multiple variables missing math mode formatting and variables not introduced.
* In Tables 1 and 2, the substantial increase in accuracy from "No VMD" to "VMD" is unclear, suggesting that factors beyond VMD may be influencing the performance.
* Simple yet effective forecasting baselines like ARIMA and exponential smoothing were not considered in the comparisons.

### Questions
See weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
This paper proposes a technique of time series forecast using Variational Mode Decomposition (VMD) and linear post-processing. VMD decomposes the original time series into different intrinsic mode functions. The light-weight linear post-processing provides additional model capacity for different forecasting tasks. The authors evaluate their proposed method on 4 datasets and demonstrate that the proposed technique (combined with the base model) improves the forecast accuracy of each base model.

### Strengths
1. Overall, the paper is clearly written and easy to understand, although additional technical details need to be provided (see below). 
2. Using Variational Mode Decomposition (VMD) with linear embedding for time series forecast is moderately novel and potentially applicable in other domains.

### Weaknesses
1. The authors should use additional metrics to comprehensively evaluate the proposed method, such as MAE, MAPE, etc. 
2. The baseline methods used in the evaluations are too generic (e.g., linear, RNN, LSTM) and not used in SOTA time series forecasts. The authors should compare the proposed method against several Transformer-based models with SOTA forecast accuracy, such as the ones reviewed in Section 2.1. 
3. The dataset size is too small since the authors only use up to 10,000 rows in each dataset (page 6). This may potentially lead to bias in the datasets and the reported evaluation metrics. The authors should use complete datasets to train and evaluate the proposed method, which should be able to handle larger datasets than 10,000 rows.
4. Ablation studies are needed to understand the impact of different model components and hyperparameters in the model architecture. For instance, the number of modes K is an important hyperparameter to analyze via ablation studies. 
5. The authors should discuss the limitations of their work and how these limitations can be addressed in future research.
6. The metrics for No VMD reported in Tables 1 and 2 are incorrect (probably due to typo). The value should be 1.041 instead of 1,041 (and similarly for all other values).
7. The authors should report the size of each of the 13 datasets in Table 2.

### Questions
1. Why do the authors trim the dataset with more than 10000 rows down to the first 10,000 rows? 
2. Why do authors only use M4 weekly dataset in the evaluations? M4 datasets consists of time series with various periodicities (hourly, daily, weekly, monthly). They should all be used in the evaluations.   
3. What is the value of K (the number of modes in VMD) used in model training? How is K selected? How does the model performance change with different values of K? Ablation studies are needed to address these questions. 
4. Why are the forecasting results of each mode summed to get the final prediction (page 6), instead of using a weighted average with fixed or learned weights?
5. In additional to the aggregate RMSE, what are the common failure modes of VMD (e.g., fail to capture outliers)? This error audit is important to informing whether the proposed method is applicable in other domains.

### Soundness
2

### Presentation
2

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
This paper proposes integrating Variational Mode Decomposition (VMD) with linear models for time-series forecasting to address data volatility challenges. Experimental evaluation is given to show its performance.

### Strengths
By decomposing data into modes, the VMD-LTSF (Long-Term Series Forecasting) framework aims to improve forecast accuracy.

### Weaknesses
1. Although VMD is integrated, the motivation is missing in this paper. The authors are suggested to give more theoretical discussions and an intuitionistic example to strongly motivate the work. Notably, based solely on the results in Tables 1 and 2, which compare primarily with classic models like LSTM and RNN, it is difficult to discern the authors’ claimed conclusion that -- ***VMD and Linear are what you need for TSF***.

2. This work lacks a comprehensive analysis of existing time series forecasting and decomposition techniques. Additionally, the paper overemphasizes benchmarks against neural network models like LSTM and RNN, overlooking other competitive decomposition-based techniques or hybrid methods, such as N-BEATS (ICLR2020), OneNet (NeurIPS2023), etc.

3. The mathematical foundation of the VMD model is briefly presented, but lacks an in-depth explanation of how the VMD decomposition can theoretically improve linear predictive models, for example, by connecting the VMD components to specific improvements in fluctuation mitigation or pattern separation. Besides, specific parameters and architecture choices, such as the number of modes in VMD, aren’t fully justified. Also, it’s unclear how sensitive the VMD-Linear model is to hyperparameter tuning (such as Lagrange multiplier $ \lambda$ and penalty parameter $ \alpha$), which could impact model generalizability.

4. The experimental part only includes comparisons with a few classic models, making it resemble an ablation study rather than a comprehensive performance evaluation. Consequently, it is difficult to discern the actual contribution of the proposed model. Besides, the authors emphasize multivariate forecasting improvements but mainly compare against linear models without showing performance relative to advanced multivariate models or ensemble methods.

### Questions
As provided in weakness.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors propose using Variational Mode Decomposition (VMD) to mitigate volatility by decomposing data into distinct modes. VMD is applied to three linear models (Linear, DLinear, and NLinear) and three neural networks (LSTM, BiLSTM, and RNN), and tested on 13 diverse datasets, including ETTm2, WindTurbine, M4, and 10 air quality datasets from Southeast Asian cities. Performance is evaluated using Root Mean Squared Error (RMSE). The results show that in multivariate settings, VMD consistently outperforms non-VMD approaches across all datasets and models, with DLinear+VMD achieving the smallest errors. However, in univariate settings, models without VMD generally perform better, with both linear models and neural networks showing the lowest errors for their respective datasets.

The authors also provide an overview of linear models, neural networks, transformers, and large language models, alongside a detailed description of the 13 datasets used. In Section 3.2, they present the mathematical foundation of Variational Mode Decomposition (VMD) and explain how it is solved using the Alternating Direction Method of Multipliers (ADMM) within a penalized Lagrange function framework.

### Strengths
1. Innovatively introduce the VMD method for time-series datasets and apply it to two distinct types of models: Linear models and Neural Networks

2. Implement both VMD and Non-VMD approaches across 13 large datasets, presenting results for both multivariate and univariate cases

3. Provide comprehensive background on the datasets and the development of time-series analysis techniques

### Weaknesses
1. In Table 1 and Table 2, some data use commas (e.g., "1,041") while others use periods (e.g., "0.005"). Please standardize these formats or provide an explanation for the differences.

2. Add more explanations and visualizations for the three neural network models, similar to the detailed descriptions provided for the linear models in Section 3.3.

3. I am not familiar with the ADMM algorithm. Are Equations (5), (6), and (7) derived specifically from the problem, or are they part of a standard algorithm? If they are derived, please include more mathematical details. If they follow a fixed iterative algorithm, kindly provide additional references.

### Questions
1. In the Univariate RMSE Results, it is observed that VMD does not consistently outperform non-VMD models. Could this be due to specific characteristics or structures of the datasets?

2. If possible, could you provide more mathematical details explaining why VMD tends to perform better than non-VMD models? Additionally, why do linear models consistently outperform neural networks in the multivariate cases?

### Soundness
3

### Presentation
3

### Contribution
4
