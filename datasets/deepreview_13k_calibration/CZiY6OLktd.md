# MG-TSD: Multi-Granularity Time Series Diffusion Models with Guided Learning Process

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Recently, diffusion probabilistic models have attracted attention in generative time series forecasting due to their remarkable capacity to generate high-fidelity samples. However, the effective utilization of their strong modeling ability in the probabilistic time series forecasting task remains an open question, partially due to the challenge of instability arising from their stochastic nature. To address this challenge, we introduce a novel \textbf{M}ulti-\textbf{G}ranularity \textbf{T}ime \textbf{S}eries \textbf{D}iffusion (\mgtsdnospace) model, which achieves state-of-the-art predictive performance by leveraging the inherent granularity levels within the data as given targets at intermediate diffusion steps to guide the learning process of diffusion models. The way to construct the targets is motivated by the observation that the forward process of the diffusion model, which sequentially corrupts the data distribution to a standard normal distribution, intuitively aligns with the process of smoothing fine-grained data into a coarse-grained representation, both of which result in a gradual loss of fine distribution features. In the study, we derive a novel multi-granularity guidance diffusion loss function and propose a concise implementation method to effectively utilize coarse-grained data across various granularity levels. More importantly, our approach does not rely on additional external data, making it versatile and applicable across various domains. Extensive experiments conducted on real-world datasets demonstrate that our \mgtsd model outperforms existing time series prediction methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper employs the diffusion model for time series forecasting and introduces the Multi-Granularity Time Series Diffusion model, which comprises three key components: 1). The Multi-Granularity Data Generator, responsible for generating multi-granularity data. 2). The Temporal Process Module, which utilizes an RNN architecture to capture temporal dynamics. 3). The Guided Diffusion Process Module is aimed at generating stable time-series predictions. This model leverages various levels of granularity within the data to guide the forward process of the diffusion model. Additionally, the paper designs a multi-granularity guidance loss function and explores optimal configurations for different granularity levels, proposing a practical rule of thumb. Extensive experiments are conducted to showcase its precision and effectiveness.

### Strengths
1. The research problem addressed in this study is of paramount significance and holds great interest. Accurate time prediction has broad applications, including tasks like anomaly detection and energy consumption control.
2. The paper introduces a novel and intriguing approach by linking various granularities in the time series with the forward process in the diffusion model.
3. The paper is excellently written and presented in a clear and comprehensible manner.

### Weaknesses
1. Some related works can be further discussed. Specifically, the paper should delve deeper into the nuances of existing diffusion-based time series forecasting methods. The current discussion lacks a detailed comparison of how the proposed Multi-Granularity Time Series Diffusion model (MG-TSD) differentiates itself from methods that also leverage diffusion models for time series, focusing on the specific mechanisms and theoretical underpinnings that set MG-TSD apart.
2. There is only one metric in the main experiment, which is not enough. The reliance on a single metric, especially when evaluating probabilistic forecasts, is insufficient. A more comprehensive evaluation should include metrics that assess different aspects of the forecast, such as sharpness and calibration, in addition to overall accuracy.
3. Compared with the baseline, the performance improvement is not obvious. While the paper reports improvements, the magnitude of these gains, particularly when compared to strong baselines, needs to be more substantial to demonstrate the practical significance of the proposed approach. A more detailed analysis of the statistical significance of the improvements is also needed.
4. The use of the RNN architecture requires further explanation. The rationale behind using an RNN for the Temporal Process Module should be more thoroughly justified, especially given the availability of alternative architectures, such as Transformers, which have demonstrated strong performance in time series modeling. The paper should discuss the specific advantages and disadvantages of using RNNs in this context, and why it is the most suitable choice.

### Questions
1.	There have been some similar works, such as TimeDiff[1] and D3VAE[2], which also applies the diffusion model. What are the technical advantages of these studies?
2.	The paper designed MG-TSD based on the diffusion model. Why is it not compared with the diffusion-based models in the baseline? Besides, There are some newer Transformer-based models, such as PatchTST[3], and Autoformer[4] should be compared in your experiments.
- [1]Shen L, Kwok J. Non-autoregressive Conditional Diffusion Models for Time Series Prediction[J]. arXiv preprint arXiv:2306.05043, 2023.
- [2] Li Y, Lu X, Wang Y, et al. Generative time series forecasting with diffusion, denoise, and disentanglement[J]. Advances in Neural Information Processing Systems, 2022, 35: 23009-23022.
- [3] Nie Y, Nguyen N H, Sinthong P, et al. A Time Series is Worth 64 Words: Long-term Forecasting with Transformers[C]//The Eleventh International Conference on Learning Representations. 2022.
- [4] Wu H, Xu J, Wang J, et al. Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting[J]. Advances in Neural Information Processing Systems, 2021, 34: 22419-22430.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Diffusion probabilistic models which can generate high-fidelity samples reserve stochastic nature. This characteristic makes it less effective in probabilistic time series forecasting tasks. To improve the efficiency of Diffusion probabilistic models, this paper introduces a novel MG-TSD model with an innovatively designed multi-granularity guidance loss function that efficiently guides the diffusion learning process. To effectively utilize coarse-grained data across various granularity levels, this paper propose a concise implementation method. What’s more, this approach does not rely on additional external data, making it versatile and applicable across various domains. Extensive experiments conducted on real-world datasets demonstrate the superiority of the proposed model, achieving the best performance compared to the state-of-the-art methods.

### Strengths
1. In the context of the time series forecasting, where fixed observations exclusively serve as objectives, diffusion probabilistic models would result in forecasting instability and inferior prediction performance. Unlike constraining the intermediate states during the sampling process, this paper creatively leverages multiple granularity levels within data to guide the learning process of diffusion models.
2. This paper provides a series of ablation experiments to test the effect of share ratio and the number of granularities, it evaluate the performance of MG-TSD using various share ratios across different coarse granularities and the number of granularities.
3. Clarity:  The paper offers a clear presentation to the model architecture with a good explanation of the methodology.

### Weaknesses
1. This paper lacks an evaluation of the time complexity of the model. It may be more sufficient to add experiments that consume memory and time.
2. MG-TSD is consisting of Multi-granularity Data Generator, Temporal Process Module (TPM), and Guided Diffusion Process Module. However, the ablation experiment part of this paper lacks performance testing of each module, especially Multi-granularity

### Questions
1. In Equation 7 of Section 3.2.1, is the distribution of ∈ consistent with the distribution of x_N? Does the distribution of ∈ obey the normal distribution? The distribution and meaning of ∈ are not pointed out.
2. Compared with the existing diffusion probabilistic models, does the MG-TSD model framework differs only in the Guided Diffusion Process Module ?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a Multi-Granularity Time Series Diffusion (MG-TSD) model for time series prediction. In general, MG-TSD controls the learning process of the diffusion model by leveraging the temporal signals in time series data at different granularity levels. In particular, the authors link the forward process of the diffusion model to the data smoothing process. Motivated by this, this work develops a multi-granularity guidance diffusion loss function, such that the inherent features within data can be preserved and a regularized sampling path can be achieved. Experiments on real-world time series datasets demonstrate the effectiveness of the proposed approach.

### Strengths
1. In the context of time series forecasting, it is a good idea to stabilize the diffusion model with the help of coarse-grained temporal signals in time series data. 
2. The derivation of the multi-granularity guidance loss function is solid. Besides, the learning procedure devised in this work is applicable.

### Weaknesses
1. The assumption that "... forward process of the diffusion model ... intuitively aligns with the process of smoothing fine-grained data into a coarser-grained representation ..." is not verified through theoretical analysis or empirical study.  It is not sufficient to simply state an intuitive alignment; a rigorous justification is needed. The authors should provide a formal argument demonstrating how the noise addition process in diffusion, which involves adding Gaussian noise at each step, is equivalent to a smoothing operation that reduces high-frequency components in the time series data. Furthermore, empirical evidence should be provided to demonstrate that the intermediate states of the forward diffusion process indeed resemble smoothed versions of the original time series at different granularities, perhaps using spectral analysis or other time series decomposition techniques to quantify the changes in frequency content.

2. Experimental settings for the time series forecasting task are unclear. For example, how the context interval and prediction interval are constructed in a time series dataset? Do you utilize a sliding window to roll the time series to build the context and predict intervals? Do the consecutive context/predict intervals overlap or not? The description should include specific details on how data is split into training, validation, and test sets. The method for selecting context and prediction windows should be clearly explained, including how the window size is determined and if any overlap exists between consecutive windows. Without these details, it's difficult to assess the validity of the experimental results.

3. More experimental results are expected. For instance, the authors only evaluate the time series forecasting methods under one length setting in each dataset, like the setting of context-24-predict-24 is utilized in Solar, Electricity, Traffic, Taxi, and KDD-Cup datasets. It is essential to evaluate the performance of the proposed method under different prediction horizons. The current experiments do not provide a comprehensive evaluation of the model's capabilities under various conditions. The paper should include experiments with varying prediction lengths to demonstrate the robustness and scalability of the method. For instance, the authors could explore settings such as context-24-predict-48, context-24-predict-96, and so on, to evaluate the performance of the model for long-term forecasting.

4. The reproductivity of this work is a concern.

### Questions
According to the inference procedure, the proposed time series forecasting approach can predict one future horizon time step at a time. How to apply this predictive approach for the long-term time series forecasting task effectively?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
