# PowerGPT: Foundation Model for Power Systems

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 5, 3, 3

## Abstract
The emergence of abundant electricity time series (ETS) data provides ample opportunities for various applications in the power systems, including demand-side management, grid stability, and consumer behavior analysis. 
Deep learning models have advanced ETS modeling by effectively capturing sequence dependence. 
Nevertheless, learning a generic representation of ETS data for various applications remains challenging due to the inherently complex hierarchical structure of ETS data. Moreover, ETS data exhibits intricate temporal dependencies and is susceptible to the influence of exogenous variables. Furthermore, different instances exhibit diverse electricity consumption behavior.
In this paper, we propose a foundation model \model{} to model ETS data, providing a large-scale, off-the-shelf model for power systems. 
\model{} consists of a temporal encoder and a hierarchical encoder. The \textit{temporal encoder} captures both temporal dependencies in ETS data, considering exogenous variables. The \textit{hierarchical encoder} models the correlation between hierarchy. Furthermore, \model{} leverages a novel self-supervised pre-training framework consisting of \textit{masked ETS modeling} and \textit{dual-view contrastive learning}, which enable \model{} to capture temporal dependency within ETS windows and aware the discrepancy across ETS windows, providing two different perspectives to learn generic representation. 
Our experiments involve five real-world scenario datasets, comprising private and public data. Through pre-training on massive ETS data, \model{} achieves SOTA performance on diverse downstream tasks within the private dataset. Impressively, when transferred to the public datasets, \model{} maintains its superiority, showcasing its remarkable generalization ability across various tasks and domains. Moreover, ablation studies, few-shot experiments provide additional evidence of the effectiveness of our model.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes PowerGPT, a foundation model for electricity time series (ETS) data in power systems. PowerGPT is pre-trained on a large-scale ETS dataset and captures long-term temporal dependency and hierarchical correlation. It achieves state-of-the-art performance on various downstream tasks in power systems, such as forecasting, missing value imputation, and  anomaly detection. The paper highlights the effectiveness of the large-scale pre-training strategy and explores the impact of model size on performance.

### Strengths
1. Foundation model for power systems could be a powerful assistant tool for dispatcher. However, whether it should be used for forecasting and anomaly detection is worthy for more discussion.

### Weaknesses
1. ETS data is not as structural as language tokens, which actually reflects the inherent physical laws of power systems, as well as human behaviors. These can hardly be captured by foundation model and also be predicted by autoregressive methods.
2. The completion level of the article is low, and the dataset is not open-source. There are multiple referencing errors.

### Questions
1. Can PowerGPT adapt to topology changes without re-training?
2. Can you demonstrate performance on open-sourced dataset? Such as Pecan Street.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a time series model for predicting electricity consumption using a large amount of data from a province in China. Their model is a transformer-based model that takes into account not only the temporal dimension of the problem but also the hierarchical structure of the power network. Their model works very well on several downstream tasks involving forecasting, missing value imputation, and anomaly detection.

### Strengths
- The proposed PowerGPT model works very well in forecasting power consumption across different horizons, beating other state-of-art time-series forecasting models. 

- In addition to the usual time series window, the model take into account the hierarchical relations in a power network to help with forecasting. 

- The model also excels in other downstream tasks such as missing value imputation and anomaly detection.

### Weaknesses
 - We do see significant improvements in forecasting performance by PowerGPT. However, it does use more information, especially the hierarchical information in the forecasting. It is not clear from the paper how those information are used. Do we get the same history window from different hierarchies? For example, when predicting at the district level, do we get the past 256 history values at city, province, industry and user level? It is crucial to understand how the model aggregates and utilizes these different levels of information, as this could significantly impact the model's performance and interpretability. The paper lacks a detailed explanation of the information fusion process within the hierarchical structure.

- Although the authors claim that their PowerGPT is a foundational model, there are no transfer experiments on other datasets. We don't know how well the model might perform on electricity consumption data from other countries, or even a different province in China (since the dataset only contain 1 province). This makes the claim of a foundational model weak. The absence of transfer learning experiments severely limits the generalizability of the model and its claim as a foundational model. Without such experiments, it's difficult to assess whether the model's performance is due to specific characteristics of the training dataset or the model's inherent capabilities.

- From the results in the tables I cannot see any forecasting experiments on individual user electricity load. These time series are usually much more variable and interesting. are they indicated by one of the rows 'exclusive' or 'public' in the tables? There are no explanations for those. The lack of clarity regarding the 'exclusive' and 'public' categories makes it difficult to interpret the results. It's unclear if these categories represent individual users or aggregated groups, and the paper does not provide sufficient detail on the characteristics of each category.

### Questions
- Why is a history window of size 256 used? For 15-min user level data that's not even 1 week of consumption data to capture the weekly patterns. Have the authors tried longer windows sizes like 512 or 1024? 

Minor typos: 
- p6, Table labels are missing
- p8, 'miss value' -> 'missing value'

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a foundation model for electricity time series data called PowerGPT. The model is designed to explicitly model correlations across types of customers and hierarchies of aggregation levels. One such model is trained on a large dataset provided by State Grid Corporation of China spanning on ~1.5M user’s data spanning multiple years. The pretraining task is based on the masked autoencoder strategy. It is empirically compared to a variety of deep SOTA time series models on pretrain-then-fine tasks using the same State Grid data (forecasting, anomaly detection, and missing value imputation).

### Strengths
- I believe studying the application of the ideas behind foundation models to energy systems to be of key importance.
- The PowerGPT architecture combines key ideas (temporal patching, random masking, and hierarchical GNNs) in a sound way. 
- The empirical results on multiple downstream tasks validate the effectiveness of the architecture on the State Grid dataset.
- I think it is valuable to provide evidence that relatively large transformers are able to be trained on large, diverse time series datasets (see [1,2]).

### Weaknesses
 - Overall I believe the significance and novelty of this paper is low. Despite the large size of the model, which is interesting, this by itself is not a sufficiently significant or novel contribution for ICLR. 
- Moreover, I do not think the problem setting is of wide interest, as I am confident that geographical electricity time series data, down to the level of specific users linked on a graph, in actual cities is not in general publicly available data (see possible ethical concerns). 
- The model is only evaluated on the State Grid test datasets/tasks, which is a dataset introduced by the authors and which has not been vetted by peer review. It would be recommended to conduct experiments on one or more established benchmarks as well. I can recommend BuildingsBench [2], which is a recently published benchmark of 7 electricity datasets for evaluating pretraining-the-finetuning approaches for short-term (24 hour) building load forecasting.
- A discussion on related work is missing. See examples of references, including papers on transformers for load forecasting as well as transfer learning for load forecasting [3,4,5,6].
- The paper needs proofreading to correct typos and fix grammar issues.

### Questions
- Why did the authors make a distinction between electricity consumption (1 day temporal granularity) and electricity load (15 minute)?
 It seems like 1 day forecasts could be obtained by aggregating the predictions made at a finer granularity?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a foundation model to model electricity time series (ETS) data. 
The objective is learning generic representations of electricity consumption data, providing a large-scale, off-the-shelf model for power systems.

### Strengths
The motivation and the idea behind the paper is interesting and the access to a big dataset of electricity time series is rare in this context and a foundation model off-the-shelf could be very interesting.

### Weaknesses
Generally speaking the work is not mature for a scientific publication and especially for ICLR2024
The literature review is insufficient, many recent and important trends were not taken in account.
The experimental results are not convincing and discussed wrongly.
An ablation study is not provided
The results are assessed considering only a portion of the considered dataset but no results are provided on literature dataset that can be useful to demonstrate how the trained model can be general.

The authors talk about load and electricity consumption but they didn't describe the difference. Usually load/demand and consumption are used as synonyms (except some cases) and, if there is not the case, authors should describe clearly.
This is present over all paper and the authors should describe the difference and modify accordingly.

All the works and discussion related to the global models are missing.
For example : Montero-Manso, P.; Hyndman, R.J. "Principles and algorithms for forecasting groups of time series: Locality and globality", 2021; Buonanno et al., "Global vs. Local Models for Short-Term Electricity Demand Prediction in a Residential/Lodging Scenario", 2022; etc.

On Missing value imputation there is a lot of recent literature not considered.

"But most of them rely heavily on labeled data at scale, making it infeasible and expensive to obtain in power systems" --> authors should describe better.

Maybe there is a different understanding on labelling for timeseries but in forecasting or autoencoder-based models no labels are needed. What is the downstream task the authors have in mind when they talk about missing of labeled data? Also after the authors talk a lot about pre-training/fine-tuning and the necessity of the labelled data. For the forecasting, e.g., you can use transfer learning/fine-tune. This is related to the discussion on global models that is missing.

Related Works.
In Forecasting section: there are a lot of works, authors should at least cite as Makridakis competitions (M4, M5, M6), moreover, the Gradient Boosting methods (XGB and LGBM) are also often employed and not mentioned.

In missing value imputation section there are some recent works that use autoencoder methods as a fusion architecture that are not discussed [e.g., Pereira et al., Reviewing Autoencoders for Missing Data Imputation: Technical Trends, Applications and Outcomes, 2020; Buonanno et al.,Fusion of energy sensors with missing values, 2023; ]

Also in anomaly detection more recent works applied to the energy context are missing.

Fig.2(a) the colors of the nodes are too similar.

What is the meaning of "masked and unmasked patches of different nodes can overlap at temporal axis"? What is the unmasked patches? What is \tilde{N}?

What is the "learnable mask token"? A particular token that subtistute the missing data? How this token is learned?

The table 3 and 4 don't show that PowerGPT is SOTA for the imputation task!

A lot of typos:
e.g. empolyed
trys
we retrieval
horicontal
trianin
are in v --> are in bold?
Tab. ?? 
constrastive
to to
I suggest to carefully check the english

I suggest to reorganize the results section. In fact table 3 and 4 are discussed after table 5

Will the authors plan to release the trained models? The code? The dataset?

### Questions
The authors talk about load and electricity consumption but they didn't describe the difference. Usually load/demand and consumption are used as synonyms (except some cases) and, if there is not the case, authors should describe clearly.
This is present over all paper and the authors should describe the difference and modify accordingly.

All the works and discussion related to the global models are missing.
For example : Montero-Manso, P.; Hyndman, R.J. "Principles and algorithms for forecasting groups of time series: Locality and globality", 2021; Buonanno et al., "Global vs. Local Models for Short-Term Electricity Demand Prediction in a Residential/Lodging Scenario", 2022; etc.

On Missing value imputation there is a lot of recent literature not considered.

"But most of them rely heavily on labeled data at scale, making it infeasible and expensive to obtain in power systems" --> authors should describe better.

Maybe there is a different understanding on labelling for timeseries but in forecasting or autoencoder-based models no labels are needed. What is the downstream task the authors have in mind when they talk about missing of labeled data? Also after the authors talk a lot about pre-training/fine-tuning and the necessity of the labelled data. For the forecasting, e.g., you can use transfer learning/fine-tune. This is related to the discussion on global models that is missing.

Related Works.
In Forecasting section: there are a lot of works, authors should at least cite as Makridakis competitions (M4, M5, M6), moreover, the Gradient Boosting methods (XGB and LGBM) are also often employed and not mentioned.

In missing value imputation section there are some recent works that use autoencoder methods as a fusion architecture that are not discussed [e.g., Pereira et al., Reviewing Autoencoders for Missing Data Imputation: Technical Trends, Applications and Outcomes, 2020; Buonanno et al.,Fusion of energy sensors with missing values, 2023; ]

Also in anomaly detection more recent works applied to the energy context are missing.

Fig.2(a) the colors of the nodes are too similar.

What is the meaning of "masked and unmasked patches of different nodes can overlap at temporal axis"? What is the unmasked patches? What is \tilde{N}?

What is the "learnable mask token"? A particular token that subtistute the missing data? How this token is learned?

The table 3 and 4 don't show that PowerGPT is SOTA for the imputation task!

A lot of typos:
e.g. empolyed
trys
we retrieval
horicontal
trianin
are in v --> are in bold?
Tab. ?? 
constrastive
to to
I suggest to carefully check the english

I suggest to reorganize the results section. In fact table 3 and 4 are discussed after table 5

Will the authors plan to release the trained models? The code? The dataset?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
