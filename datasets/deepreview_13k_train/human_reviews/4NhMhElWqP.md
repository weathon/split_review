# DAM: Towards a Foundation Model for Forecasting

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
It is challenging to scale time series forecasting models such that they forecast accurately for multiple distinct domains and datasets, all with potentially different underlying collection procedures (e.g., sample resolution), patterns (e.g., periodicity), and prediction requirements (e.g., reconstruction vs. forecasting). We call this general task universal forecasting. Existing methods usually assume that input data is regularly sampled, and they forecast to pre-determined horizons, resulting in failure to generalise outside of the scope of their training. We propose the DAM -- a neural model that takes randomly sampled histories and outputs an adjustable basis composition as a continuous function of time for forecasting to non-fixed horizons. It involves three key components: (1) a flexible approach for using randomly sampled histories from a long-tail distribution, that enables an efficient global perspective of the underlying temporal dynamics while retaining focus on the recent history; (2) a transformer backbone that is trained on these actively sampled histories to produce, as representational output, (3) the basis coefficients of a continuous function of time. We show that a single univariate DAM, trained on 25 time series datasets, either outperformed or closely matched existing SoTA models at multivariate long-term forecasting across 18 datasets, including 8 held-out for zero-shot transfer, even though these models were trained to specialise for each dataset-horizon combination. This single DAM excels at zero-shot transfer and very-long-term forecasting, performs well at imputation, is interpretable via basis function composition and attention, can be tuned for different inference-cost requirements, is robust to missing and irregularly sampled data by design.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is an interesting paper proposing to solve a very general time series problem. This paper aims at flexible (long or short horizon) time series forecasting with long or short context input for any general time series. Moreover the context could also be irregularly sampled. The paper additionally proposes a strategy for efficient long context inputs.

The model is therefore a general time series forecaster and trained on many time series for generalization to any held out datasets. As such it could be considered a foundational model for time series forecasting.

Experimental results are promising, especially on held out datasets. One of the main advantages of a foundational model is to be general enough to be able to predict on held out datasets. While the results are most positive on held out datasets, the model performs at par with the baselines on the training datasets. To summarize, I believe this to be an interesting contribution to the time series literature, and I am willing to increase my score if the concerns below are addressed.

Update: Increased the score

### Strengths
- The problem being solved in the paper is one of the most interesting problems in the time series community i.e. general time series forecasting for flexibly sampled time series.
- The proposed solution (described as a foundational model) involving attention is a befitting solution to this problem by virtue of its ability to adapt to flexible input sizes.
- Experimental results are promising on both training and held out datasets.

### Weaknesses
 - The model architecture is quite complex and the rationale behind such a choice is not fully explained. One important question that is raised is the usefulness of each of the components in the model. An ablation study may be performed to measure the importances of each of the components proposed in the paper.
- Simple linear forecasting models are not considered as baselines. For comparison between different models a normalized score is preferred rather than a absolute score. Normalization helps interpret the improvements easier since they are scaled. As such, the experimental section need improvement.

### Questions
- When using a trained model for forecasting a single time series, how does inference look like in such a simple setting? Do attention models work well in such scenarios? In other words, do attention models produce better forecasts when a larger context in provided? The larger context could be in the form of multiple time series or a larger history.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes deep data-dependant approximate analytical model (DAM) as a "foundational model" for time series forecasting. DAM uses a long tail distribution to sample from the history of the time series. These irregularly-sampled time-value pairs are fed into a transformer-based model which outputs basis coefficients. The basis coefficients are then used in a basis function composition to generate forecasts. The authors trained a single DAM model across multiple datasets and show that this model is competitive against dataset-specific baselines on long-term forecasting benchmarks. Small-scale analyses have also been conducted on very long-term forecasting and imputation tasks.

### Strengths
- The combinations of ideas presented in this work involving history regime sampling, basis composition-based forecasting, and training a single model across multiple datasets are original and interesting.
- The model provides the flexibility to forecast arbitrarily far into the future which is an attractive property. While autoregressive models can already do that, they are generally slow.
- The paper is well-written in general. Some discussion and visualizations can be improved (see weaknesses).

### Weaknesses
 - The main weakness of this paper is that it overclaims and underdelivers. In its current state, the study is not strong enough to claim the title of a "foundational model".
    - The authors mention that they use datasets from diverse domains. However, out of the 12 datasets studied, 6 come from a single domain. The distribution of sampling frequencies of these datasets are also not diverse with 6 hourly datasets and a limited representation of other frequencies (and some popular frequencies completely missing). The lack of diversity in both domain and sampling frequency limits the generalizability of the model and weakens the claim of a foundational model. For instance, the absence of daily or weekly datasets, which are common in many real-world applications, raises concerns about the model's applicability in those contexts.
    - Another aspect that could have justified the term "foundational" is a diversity of tasks. However, the paper mostly focuses on the long-term forecasting tasks with limited discussion of other tasks. Importantly, the practically relevant task of short-term forecasting (e.g., Monash time series forecasting archive) gets very less attention. The limited exploration of diverse tasks, such as anomaly detection or classification, further undermines the claim of a foundational model, which should ideally be versatile across various time series analysis tasks.
    - The claim _Most existing forecasting models were designed to process regularly sampled data of fixed length. We argue that this restriction is the central reason for poor generalisation in time series forecasting_ has not been justified convincingly. The paper does not provide a thorough analysis or empirical evidence to support this strong claim. It is not clear why the restriction of fixed length inputs is the central reason for poor generalization, and other factors such as model architecture and training procedures could also play a significant role.
- The visualizations are poorly done and confusing for a serious academic paper. Please consider using cleaner figures. It is unclear how exactly inference on a new dataset is performed. It would improve the clarity of the paper if a specific paragraph on inference is added. Please see specific questions in the questions section.
- The results on the long-term forecasting benchmarks, while reasonable, are not impressive for a "foundational model" that has been trained on a larger corpus of datasets. The performance gains over existing methods are not substantial enough to justify the claim of a foundational model. The results should demonstrate a clear and significant improvement over existing methods to support such a claim.
- The very-long-term forecasting task is of limited practical significance. Despite that, the discussion requires improvement, e.g., by conducting experiments on more datasets and training the baseline models with the "correct" forecast horizon to put the results in a proper context. The practical relevance of very-long-term forecasting is questionable, and the lack of comparison with baselines trained with appropriate horizons makes it difficult to assess the true value of the proposed model in this context.
- The zero-shot analysis (Sec. 4.3) has only been conducted on two datasets. Moreover, since prior works such as PatchTST and NHITS do not claim to be foundational models, a proper comparison would be with baselines trained specifically on these held-out datasets. DAM would most likely be worse in that case but it would be a better gauge for the zero-shot performance.

### Questions
- How exactly is inference performed on a dataset? Is basis function initialization also required during inference?
- How costly is context selection during inference, in general?
- Can you clarify what is meant by "No training of the backbone is even required in this case because the initialisation coefficients are optimal for past data"? Is model training not needed for imputation?
- You mention "The DAM produces relatively high basis coefficients for ETTh2 in the year range, suggesting that it captures the long-term trend." but the ETTh2 dataset only has data over two years (from 2016 to 2018) while relatively high positive values are seen for 3, 5, 7, 9 yr basis components. How do you explain this phenomenon?

### Soundness
3 good

### Presentation
2 fair

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
The paper proposes a foundation model for universal time-series forecasting. Building such a model is challenging because the sample resolution, periodicity, and prediction task are different. To address these challenges, the paper proposes to take randomly sampled histories and output coefficients of basis functions. The designed basis function enables forecasting to non-fixed horizons.
Experiments show that the single model trained on 10 datasets can outperform or match existing SOTA dataset-specific models. It also performs well on held-out datasets and has good interpretability.

### Strengths
Building a foundation model for time series forecasting is challenging because different datasets have different patterns and resolutions. This paper proposes reasonable solutions to address these challenges. The experimental results also show that the proposed method is promising. Additionally, it has good interpretability and is robust to missing and irregularly sampled data.

### Weaknesses
Training such a foundational model requires high computational cost. The biggest advantage of the foundation model is its ability for zero-shot forecasting. However, the paper only reports the performance on two held-out datasets which is not sufficient. This restricts the practical use of the model in the real-world application.

### Questions
How does the training cost of the proposed method compare with the baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The author proposes a foundation model for time series forecasting called DAM (deep data-dependent approximate analytical model). 
DAM takes input time series data and samples (time, value) pairs using HSR (history sampling regime) technique. HSR is not a regular and fixed-length sampling method unlike other time series forecasting techniques. Instead, it defines a probability distribution that is closer to the top-head section as the sampling points are closer to the prediction target point, and closer to the long-tail section as they are farther away. The author claims that this method is a major difference from other time series forecasting models and prevents overfitting and improves generalization performance. The sampled (time, value) pairs and the coefficient values initialized by the linear solver are used in the transformer to determine the coefficient values of 219 basis functions. The final predicted time-series is a combination of the basis functions. 
The author evaluated 12 benchmark datasets used at training and 2 datasets not used at training (for validation of generalization performance), and compared them with 6 existing sota models trained specifically for each dataset, showing better or similar performance. In particular, DAM showed excellent performance in long-term forecasting. Additionally, DAM can adjust the trade-off between inference cost and performance by changing the context size, and also provides interpretabilty features based on basis function composition and attention map analysis.

### Strengths
1. Addressing foundation model for time-series forecasting model is a significant and timely task (and it is a very difficult problem). 

2. The irregular and non-fixed size sampling technique is interesting.

3. Various and numerous experiments were conducted to verify the ability of DAM.

### Weaknesses
1. To be a foundation model, it is necessary to verify that the computational amount and performance follow the scaling law, but there is no related content. Even if the computational amount and performance do not follow the scaling law in time series forecasting, the authors should have explained why they had to use 10 datasets to train DAM (not single dataset or many more), and what was the bottleneck for improving the foundation model performance.

2. The paper too much depends on appendix. The content provided in the main paper should be a complete argument, but it is difficult to follow without looking at the appendix. For example, in 4.1 Results and discussion, the authors need to summarize the content of Table 1 and argue the authors’ claim, but it is omitted. Instead, the content of the appendix is summarized. To be a regular paper, it seems that the structure of the paper needs to be more organized.

3. One of the most important abilities of a time series forecasting model is peak time prediction, but as the authors pointed out in Limitations, DAM does not seem to predict well. This limits the role of DAM in real-world problems.

### Questions
1. According to the description of Table 1, DAM performed multivariate forecasting. I guess that when creating (time, value) pairs, multiple variables were included in the value part. Is that right? If so, I think it should be more clarified in the paper.

2. At Figure 6, it seems that the inference time can be reduced from 200ms to below 100ms depending on the context size. However, the inference time and cost seem to be very small compared to LLM (~seconds), so it seems possible to reduce costs by increasing the computing resources not expensively at around 200ms. I don’t fully understand what the authors want to deliver in 5.1 FLEXIBLE INFERENCE COST. Could you explain more about it? (sorry)

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
