# A Benchmark Study For Limit Order Book (LOB) Models and Time Series Forecasting Models on LOB Data

- Decision: Reject
- Scores: 3, 5, 5, 3, 5

## Abstract
We present a comprehensive benchmark to evaluate the performance of deep learning models on limit order book (LOB) data. Our work makes four significant contributions: (i) We evaluate existing LOB models on a proprietary futures LOB dataset to examine the transferability of LOB model performance between various assets; (ii) We are the first to benchmark existing LOB models on the mid-price return forecasting (MPRF) task. (iii) We present the first benchmark study to evaluate SOTA time series forecasting models on the MPRF task to bridge the two fields of general-purpose time series forecasting and LOB time series forecasting; and (iv) we propose an architecture of convolutional cross-variate mixing layers (CVML) as an add-on to any deep learning multivariate time series model to significantly enhance MPRF performance on LOB data. Our empirical results highlight the value of our benchmark results on our proprietary futures LOB dataset, demonstrating a performance gap between the commonly used open-source stock LOB dataset and our futures dataset. Furthermore, the results demonstrate that LOB-aware model design is essential for achieving optimal prediction performance on LOB datasets. Most importantly, our results show that our proposed CVML architecture brings about an average improvement of 244.9% to various time series models’ mid-price return forecasting performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors present a comprehensive benchmark to evaluate the performance of deep learning models on limit order book (LOB) data with four contributions: evaluate existing LOB models on a proprietary futures LOB dataset, the first benchmark of existing LOB models on the mid-price return forecasting (MPRF) task, introduce the first benchmark study evaluating state-of-the-art (SOTA) time series forecasting models on the MPRF task, propose an architecture of convolutional cross-variate mixing layers (CVML) as an enhancement to any deep learning multivariate time series model.

### Strengths
The paper establishes a clear purpose, aiming to benchmark deep learning models on limit order book (LOB) data across different asset types. It identifies the primary gap in research, particularly for mid-price return forecasting (MPRF) in LOB data, and articulates four main contributions, including the novel Cross-Variate Mixing Layer (CVML) architecture, which adds value to the paper. This paper is also easy to follow with enough details on the performance of the benchmarks.

### Weaknesses
1: As a benchmark paper, although this paper provides lots of comparison methods and results. I feel like the datasets (2 datasets) selected for this study are not enough. LOB is based on different markets, which normally will have different kinds of results. The 2 datasets are from NASDAQ Nordic stock market and SC (Crude Oil), one of China’s most liquid futures contracts. For papers that are mainly focusing on technical achievements, these might be enough datasets and experiments to showcase superior performance, but for benchmark papers, two markets are not enough. I would recommend adding more market datasets, such as Bitcoin Limit Order Book (LOB) Data, which has many public resources. 

2: I have questions on CVML, 

2.1 The authors claim that, CVML can be added on any deep learning multivariate time series model to significantly enhance MPRF performance on LOB data. However, in Table 6, the performance variances are really different, from 3.1% to 958.3%. I'm not sure if this can be called as "can be added on any deep learning methods". Also, there are only 4 methods. I think it's not safe to claim "can be added on any deep learning methods" with only 4 methods experiments. 

2.2 "an average improvement of 244.9%" is the conclusion on CVML form the authors. I don't understand how the authors calculate this average. Can you explain me how you make such calculation?

### Questions
Please see the weakness part for my questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a study of many popular timeseries models for predicting future prices of assets. The important differentiator is the fact that models compared in this benchmark are using order book features (such as prices/quantities at different order book levels,  per-level mid-price, etc) in addition to standard features such as asset price.

Two main tasks are considered: Mid-Price Trend Prediction (a classification problem, where the model has to predict if the price will go up/down/stay) and Mid-Price Return Forecasting, where the model has to predict future mid-price return at some forecasting horizon (judged by Mean Square Error).

The study uses one open-source dataset (FI-2010 stock dataset) and one proprietary futures dataset (CHF-2023) which is not publicly available. Authors are providing the results for a variety of popular time-series models.

In addition, authors propose an architecture of convolutional cross-variate mixing layers (CVML) that improves various time series models mid-price return forecasting performance

### Strengths
- The topic of LOB models is very interesting, and this study (unlike other existing benchmarks) compares the models on futures data
- Good variety of the tested models and used features.
- Running experiments on a proper-size, realistic dataset (CHF-2023) 
- CVML architecture is a simple add-on that seems to perform well based on the experiments (however, probably needs to be confirmed if it still improves models that were more tuned than just batch_size / learning rate.)

### Weaknesses
 - No code provided to reproduce the results, even on the open-source dataset.
- One of the datasets is extremely small, almost toy-size (10 trading days, 5 companies). The limited scope of the FI-2010 dataset, with only 10 trading days and 5 companies, raises concerns about the generalizability of the findings. While high-frequency data is valuable, the short time span and limited number of assets may not capture the full range of market dynamics and could lead to overfitting.
- The other dataset is not available to the public, so it will be impossible to reproduce results for it. This lack of access severely limits the ability of other researchers to validate the findings and build upon this work.
- Very limited hyperparamter search (either just keeping original values or searching only learning rate / batch size). Study would be much 
 more convincing if the models got some computational budget to tune a bit hyper-params for CHF-2023 Dataset. The hyperparameter tuning process appears to be insufficient, focusing solely on learning rate and batch size. This limited search space may not uncover the optimal configurations for each model, potentially underestimating their true performance capabilities. A more comprehensive search, including parameters such as the number of layers, hidden dimensions, and regularization strengths, is needed to ensure a fair comparison.
- Overall, the paper and proposed techniques feels very specific to trading and would be better suited for a trading-related workshop or conference, rather than ICLR

### Questions
- The order book in the experiments was divided into 5 levels, what was the algorithm for determining the mapping layer -> value_range?   (motivation: if I would like to apply your method for other order book, how to decide the split)
- Did you try dividing order book into more than 5 layers ?
- Table 1 has in description “ (....) a set of 26 Time-insensitive features” , but looking at the Table it seems there are  2 * 5 (u2) + 4 * 4 (u3) + 4 (u4) + 2 (u5)  = 32 features in total ?
- Why some of the models (like DAIN) have lookback size which is much smaller than all other models? 
- CVML results on CHF-2023 seem to be missing, did you run the equivalent of Table 6, but with CHF-2023?

### Soundness
2

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
4

### Summary
This paper presents a comprehensive benchmark study evaluating deep learning models on limit order book (LOB) data, focusing on mid-price trend prediction (MPTP) and mid-price return forecasting (MPRF) tasks. The experiments present serval interesting findings. To overcome noise in LOB data for MPRF task, the paper introduces a novel architecture called convolutional cross-variate mixing layers (CVML) to enhance MPRF performance. The empirical results demonstrate the effectiveness of CVML.

### Strengths
+ The paper bridges gaps in the literature regarding MPRF
+ The experiments are extensive, and conducted in many facets, e.g., comprehensive datasets, multiple metrics, different horizons.
+ The proposed model CVML is and effective, and can be added into existing time series forecasters to enhance performance.

### Weaknesses
 - The importance of LOB problem is not adequately emphasized. Also, the scope of LOB problem is not very extensive.
- Why should we care about MPTP and MPRF tasks? Are there any other tasks we need to emphasize about LOB problem? The paper should make it clear.

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes to evaluate existing LOB models on the mid-price return forecasting(MPRF) task using a proprietary futures LOB dataset and present the first benchmark study to evaluate SOTA time series forecasting models on the MPRF task. Moreover, the paper proposes an architecture of convolutional cross-variate mixing layers (CVML) as an add-on to any deep learning multivariate time series model to significantly enhance MPRF performance on LOB data. However, I think the contribution of the paper is not sufficient, the innovation is average, and the relevant descriptions are relatively weak. In addition, there are some serious issues with the writing of the paper, such as the lack of Section 3 and Section 5 in the description of the paper organization.

### Strengths
The paper proposes to evaluate existing LOB models on the mid-price return forecasting(MPRF) task using a proprietary futures LOB dataset and present the first benchmark study to evaluate SOTA time series forecasting models on the MPRF task. Moreover, the paper proposes an architecture of convolutional cross-variate mixing layers (CVML) as an add-on to any deep learning multivariate time series model to significantly enhance MPRF performance on LOB data.

### Weaknesses
I think the contribution of the paper is not sufficient, the innovation is average, and the relevant descriptions are relatively weak. In addition, there are some serious issues with the writing of the paper, such as the lack of Section 3 and Section 5 in the description of the paper organization.

### Questions
How to verify the advantages of the benchmark proposed in this article without comparison with relevant benchmarks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper provides a benchmark to evaluate the performance of deep learning models on Limit Order Book (LOB) data, covering two key tasks: Mid-Price Trend Prediction (MPTP) and Mid-Price Return Forecasting (MPRF). 
The study utilizes an open-source stock LOB dataset (FI-2010) and a proprietary futures LOB dataset (CHF-2023).
Additionally, the paper introduces an innovative architecture, the Cross-Variate Mixing Layer (CVML), which significantly enhances the predictive performance of existing time series models on LOB data.

### Strengths
1. It is the first to benchmark existing LOB models on the Mid-Price Return Forecasting (MPRF) task.
2. The paper proposes a novel architecture, the Convolutional Cross-Variate Mixing Layer (CVML), as an add-on to existing deep learning multivariate time series models to significantly improve performance on LOB data.

### Weaknesses
The paper's contributions are somewhat limited in scope, and it does not fully address the significant challenges and value propositions within the Limit Order Book (LOB) scenario for time series prediction: 
1. The paper falls short in providing a detailed description of the unique challenges that LOB presents for time series prediction. It particularly lacks an articulation of these challenges in a way that informs the design of new LOB benchmarks,
2. The paper lacks comprehensive evaluation metrics tailored for LOB data. For instance, beyond conventional statistical indicators such as Mean Squared Error (MSE), Correlation (Corr), and R-squared (R²), there is a need for evaluation metrics or testing methods that better align with the characteristics of LOB data. This includes how to test the model's handling of LOB data features (e.g., high-frequency updates and noise issues), the complexity of market microstructure in LOB data, and insufficient testing of the model's robustness in the face of extreme market events.
3. Despite the inclusion of futures data, the paper does not convincingly demonstrate the breadth and representativeness of the datasets used to cover various LOB scenarios, including foreign exchange and cryptocurrencies. A more robust justification is needed to explain how the selected datasets capture the range of challenges encountered in diverse LOB environments.
4. The paper lacks a comparative analysis with existing methods, which is essential for validating the proposed CVML approach within the LOB domain. Without such comparisons, it is challenging to determine whether CVML provides a significant advantage over alternative methods in tackling the specific challenges of LOB time series prediction.

### Questions
1. CVML enhances the ability of time series models to capture cross-variate and temporal correlations. This type of method seems not to be limited to the LOB scenario; is it also applicable to other scenarios? What specific advantages does CVML offer in the context of LOB that make it particularly effective in this domain? Additionally, the authors have not compared CVML with other related methods. Could a comparison be made with other similar methods to demonstrate the advantages of the CVML approach?
2. While the paper utilizes stock and futures datasets, it is unclear whether these two types of datasets are sufficient to encapsulate the breadth of challenges present in various Limit Order Book (LOB) scenarios, including foreign exchange and cryptocurrencies. Can the authors provide a more detailed discussion on the specific challenges that LOB presents and how these compare to other LOB contexts? Additionally, can the authors demonstrate that the current datasets are comprehensive enough to address the challenges across all types of LOB scenarios?

### Soundness
2

### Presentation
2

### Contribution
2
