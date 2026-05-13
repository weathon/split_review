# Learning to Extrapolate and Adjust: Two-Stage Meta-Learning for Concept Drift in Online Time Series Forecasting

- Decision: Reject
- Scores: 5, 5, 8, 3, 6, 5

## Abstract
The non-stationary nature of time series data in many real-world applications makes accurate time series forecasting challenging. In this paper, we consider concept drift where the underlying distribution or environment of time series changes. We first classify concepts into two categories, macro-drift corresponding to stable and long-term changes and micro-drift referring to sudden or short-term changes. Next, we propose a unified meta-learning framework called LEAF (Learning to Extrapolate and Adjust for Forecasting). Specifically, an extrapolation module is first meta-learnt to track the dynamics of the prediction model in latent space and extrapolate to the future considering macro-drift.  Then an adjustment module incorporates meta-learnable surrogate loss to capture sample-specific micro-drift patterns. Through this two-stage framework, different types of concept drifts can be handled. In particular, LEAF is model-agnostic and can be applied to any deep prediction model. To further advance the research of concept drift on time series, we open source three electric load time series datasets collected from real-world scenarios, which exhibit diverse and typical concept drifts and are ideal benchmark datasets for further research. Extensive experiments on multiple datasets demonstrate the effectiveness of LEAF.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a two-stage meta-learning framework to address the concept drift issue for time-series forecasting. The authors identify and address the two types of drift namely macro-drift and micro-drift. Drifts in time series that occur over a longer time period are referred to as macro-drifts whereas drifts that occur (and perhaps disappear) within short windows of time are referred to as micro-drifts. Macro-drifts are modeled using an LSTM network that learns the evolution of an embedding space corresponding to macro-drift parameters. The LSTM returns a macro-drift-adjusted embedding which is then used further. Micro-drifts are addressed using meta-learning framework that evaluates the difference between current training data (which is supposed to have micro-drifts) and historical training data using a relation network and returns micro-drift adjusted model parameters.

The entire framework can learn in an online manner, meaning the model parameters are updated as more data is made available. Initial parameters are learned in an offline phase (warmup) which are then used as initial parameters for online learning phase.

Authors show comparison of their framework across various time series forecasting architectures (such as PatchTST) and other frameworks that address the concept drift in time series on benchmark datasets.

### Strengths
1. (quality and clarity) The paper is well-written, the identified concept drift issues and ways to address them have been clearly written with substantial experimental evidence suggesting that their method outperforms existing approaches.
2. (significance) The proposed framework is more suitable for online-learnning which is a more practical setup and more accurately depicts the real-world scenario in which ML models are deployed.
2. (significance) The benchmarking of datasets and baselines proposed by authors is essential for further developments in the field.

### Weaknesses
1. Authors employ an LSTM network to model the evolution of latent space for addressing the macro-drift. However, using an LSTM to model the evolution of latent space has been significantly explored in the past. I suggest authors to refer to the paper (and its citations): Deep State Space Models for Time Series Forecasting

The empirical success of LSTM-based evolution is well-known, hence I believe that the solution to the macro-drift issue is short of novelty. The proposed solution can act as a strong baseline for a more novel solution. Specifically, while the LSTM captures temporal dependencies, it might be beneficial to investigate models that can disentangle the latent space into components representing different aspects of the macro-drift. This could potentially lead to a more nuanced understanding and prediction of the drift's evolution. I suggest authors explore more aggressive approaches for extrapolation than only using a vanilla LSTM for predicting the evolution of parameters.

2. More details on the solution proposed for modeling micro-drifts are needed. Perhaps a more detailed description of the relation network (R) and embedding function (g) is required. What are the alternative ways to implement them and why proposed implementations work the best should also be addressed. The current description lacks sufficient detail regarding the architecture and hyperparameter choices for both the relation network and the embedding function. For instance, what is the dimensionality of the embeddings produced by function 'g'? What is the specific structure of the relation network 'R' - is it a feedforward network, and if so, how many layers does it have, and what activation functions are used? I also suspect any off-the-shelf MLP used for the relation network is at the risk of overfitting. I would like to know authors' comments on that, whether they saw any overfitting isses? If possible, please provide the necessary ablations. A more thorough exploration of these aspects would strengthen the paper considerably.

### Questions
1. In Figure 1a, it is not clear which dataset the shown time-series corresponds to. If this is a real-world dataset, please provide the reference.
2. Are there any external features and time-related features used in the models? If so, how does their presence affect the overall meta-learning process? Knowing this can also help in evaluating the quality of the proposed framework against external signals which are much easier to learn from.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to solve the time series prediction problem which always suffers from dynamics or noon stationarity.  The authors propose a unified meta-learning framework called LEAF (Learning to Extrapolate and Adjust for Forecasting) which divides the concept drift into macro-drift corresponding to stable and long-term changes and micro-drift referring to sudden or short-term changes. An extrapolation module is first meta-learnt to track the dynamics of the prediction model in latent space and extrapolate to the future considering macro-drift. Then an adjustment module incorporates meta-learnable surrogate loss to capture sample-specific micro-drift
patterns. Extensive experiments are conducted.

### Strengths
1. This paper is well-presented and well-organized.
2. This paper proposes a new meta-learning framework called LEAF (Learning to Extrapolate and Adjust for Forecasting) which divides the concept drift into macro-drift corresponding to stable and long-term changes and micro-drift referring to sudden or short-term changes. 
3. Extensive experiments are conducted.

### Weaknesses
1. The paper doesn't appear to provide a strong theoretical foundation for the proposed method. It would be beneficial to include a theoretical framework or proofs to support the claims made in the paper. The lack of theoretical analysis makes it difficult to understand the convergence properties of the meta-learning framework, especially how the extrapolation and adjustment modules interact and guarantee stable learning under different drift scenarios. A formal analysis of the generalization bounds of the proposed approach would significantly strengthen the paper.
2. It should be better if more ablation studies can be provided. Specifically, the contribution of the adjustment module is not clearly isolated in the current ablation studies. It is important to understand the individual impact of this module versus the extrapolation module, and how the combination of the two leads to the reported performance gains. Furthermore, it would be beneficial to explore the sensitivity of the method to different hyperparameter settings, especially those related to the meta-learning process, and how these parameters influence the effectiveness of the extrapolation and adjustment modules.

### Questions
Please address the questions above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this manuscript, the authors consider concept-drift phenomenon where the underlying distribution or environment of time series changes. We first classify concepts into two categories, macro-drift corresponding to stable and long-term changes and micro-drift referring to sudden or short-term changes. Obviously, changes in the variance of the data over time due to sudden changes in potential events in a time series prediction task is an interesting open problem.

### Strengths
1. It is very important to use the meta-learning method to alleviate the problem that the concept drift caused by the data in the online scene leads to the decline of the accuracy of the time series prediction model.
2. The effectiveness of the proposed algorithm is demonstrated by comparison with several baseline models and abundant ablation experiment and visualization results.

### Weaknesses
1. It is suggested that the author consult the related literatures on the concept drift problem of time series data, because the author obviously ignores some studies based on surrogate gradient.
2. The visual image resolution is too low, and the display effect is very poor.
3. The MAPE metric was missing of the time series prediction study.
4. Datasets related to power forecasting are more cyclical temporal patterns, so why does the author not use financial futures datasets with more abrupt phenomena (such as NASDAQ 100 dataset)?

### Questions
Please see details of Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper fixates on the concept drift problem in online time series forecasting. The authors classify this problem into macro-drift and micro-drift categories. Technologically, they present the LEAF as a model-agnostic algorithm for online learning, where a queue is stored for macro-drift and a special meta-learnable surrogate loss is adopted for micro-drift. FEAF can consistently boost the forecasting performance of various deep models.

### Strengths
-	The paper focuses on an important question: online time series forecasting.
-	The proposed LEAF is technologically sound. They also provide a new benchmark for concept drifts.
-	Detailed ablations are also included.

### Weaknesses
1.	About the efficiency.

Since they adopt the meta-learning strategy for training, the efficiency w.r.t. other online learning methods and naive training should be compared, such as the GPU memory, running time in both training and inference phases. The comparison should include a breakdown of the time spent on different components of the LEAF framework, such as the queue management for macro-drift, the meta-learnable surrogate loss calculation for micro-drift, and the parameter generation process. This detailed analysis is crucial to understand the computational overhead introduced by LEAF compared to simpler online learning methods.

2.	More baselines.

Actually, TimesNet [1] is a state-of-the-art TCN-based model for time series forecasting. They should also experiment on this model to demonstrate the effectiveness of LEAF, in addition to the vanilla TCN. Furthermore, the comparison should not only be limited to the vanilla TCN but also include other state-of-the-art TCN variants. Besides, Non-stationary Transformer also claims that it can handle the non-stationary time series, which should also be included in discussion and comparison. The comparison should also include the computational cost of these baselines. 

[1] TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis, ICLR 2023

[2] Non-stationary Transformers: Rethinking the Stationarity in Time Series Forecasting, NeurIPS 2023

One simple baseline for online learning is to retrain the model with new-coming data. How about this protocol? For example, suppose that the first training adopts 70% data, you can also train a new model when you receive 90% new data. This retraining baseline should also be included in the comparison to evaluate the effectiveness of the proposed method.

3.	The Naïve setting could be wrong. 

Why not train the model with both warm-up and meta-train data? Since LEAF also adopts the meta-train data for model training, a fair comparison is to adopt the same training data for all baselines. The current comparison is not fair, as the baselines are trained only on the warm-up data, while LEAF leverages both warm-up and meta-train data. This discrepancy in training data usage could lead to an overestimation of LEAF's performance gain. A more appropriate baseline would be to train the model on the combined warm-up and meta-train data, and then evaluate it on the meta-test set.

4.	About the "model agnostic" claim.

It is interesting to generate forecasting model parameters. I suggest listing the generated parameter size for each model, since the transformer-based models are quite big. How to directly decode such big model parameter with MLPs? Or you just change part of the model. This point should be made clearer. If you only adjust the final linear layer, it is hard to claim model agnostic, giving that there are a lot of models do not contain the final linear layer. The paper should explicitly state which parameters are generated for each model architecture and how these parameters are integrated into the existing model structure. The claim of model agnosticism needs to be supported by a detailed explanation of the parameter generation and integration process for a diverse set of models.

### Questions
I think the technical design of this paper is reasonable and interesting. But it is insufficient (maybe wrong) in the experiments and clarifications about their design. All the details are included in the weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper has two primary contribution: A framework that utilizes a two stage embedding approach to capture macro and micro drifts when forecasting time-series data, and introducing a new dataset that could potentially be used for benchmarking mechanisms over concept-drifting time series data streams. Particularly, the authors utilize embedding learned from LSTMs over a time window that are adjusted with a sample-specific surrogate loss to account for micro-drifts. The two functions are jointly learned from data, and embedding are updated over time. The empirical results comparing the proposed LEAF approach to other competing methods over well known datasets and the newly introduced electric load datasets shows that the proposed approach generally performs well, resulting in lower error. Furthermore, the ablation study conducted by the authors demonstrate the rationale behind the two stage optimization procedure proposed in the paper.

### Strengths
1. The approach has a unique take on predicting over multi-variate time-series data. The paper captures the differences among various competing methods and illustrates well the reasons why the proposed approach works.
2. The empirical analysis presented in the paper, along with case study, support the proposed hypothesis well.
3. The paper is well structured providing most of the relevant details needed to replicate the proposed approach.

### Weaknesses
1. While the problem of time-series prediction clearly assumes the availability of labeled data over time, it is not clear how the proposed approach is different from metric learning approaches proposed in general data stream classification papers such as Fischer, Lydia, Barbara Hammer, and Heiko Wersing. "Online metric learning for an adaptation to confidence drift." 2016 International Joint Conference on Neural Networks (IJCNN). IEEE, 2016. and Wang, Zhuoyi, et al. "Metric learning based framework for streaming classification with concept evolution." 2019 international joint conference on neural networks (IJCNN). IEEE, 2019.
2. While the paper conceptually explains the optimization function employed, it is not clear how the actual network architecture is constructed. The authors mention in the implementation details that MLPs were used for implementing decoder. However, lack of additional information significantly reduces the ability to reproduce provided results in the paper. For instance, the specific number of layers, the activation functions used, and the dimensionality of the hidden layers within the MLPs are not specified. This lack of detail makes it difficult to assess the complexity and potential for overfitting of the proposed model.
3. One of the key elements of a data classification/time series prediction mechanism over a data stream is space and time complexity. This is completely missing in the paper. While the authors claim that LEAF's performance improvements over competing methods are significantly better, it is not clear if this is due to higher cost in computation and/or time. It would be better for the authors to provide a computational complexity analysis and comparison. Specifically, the paper should include a breakdown of the computational cost associated with each stage of the proposed framework, such as the embedding learning, the adjustment with surrogate loss, and the final prediction. Furthermore, a comparison of the training and inference time with the baseline methods would be beneficial.

### Questions
1. In the experimental setting, is there a reason why all forecast horizon is set to 24? What is the relationship between forecast horizon and model performance?
2. In table 1 and table 2, it is not clear if the results are statistically significant. Can you please include variance among the five trials for these results?
3. In the last part of Section 4.2, the authors note that ER and DER++ methods incorporate mechanisms that alleviate catastrophic forgetting, and is orthogonal to the proposed solution. Is it possible to incorporate these mechanisms in the proposed solution as future work? What are the challenges?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed an online forecasting framework. It has two components to capture the macro and micro changes in the time series. An extrapolation network to predict the embedding of a time period based on optimal embedding from previous time periods. Then, the embedding is adjusted individually for each sample before using a decoder to generate the model parameters. The authors tested their methods on 6 datasets and compared them to several relevant continue learning baselines. An ablation study was done to show their impact on the performances. The authors also open sourced 3 datasets.

Disclaimer: I am not familiar with the continuing learning for forecasting literatures, and I would need to count on others to comment on the related works.

==== After reading the authors revision and response ===
I raised my score to 5 but I don't think the paper is good enough to be accepted at ICLR.

### Strengths
The paper tries to tackle a practical problem where forecasting models need to be updated given new data, continuously. It’s a bold attempt to combine many ideas: using embedding; decoding model parameters directly from embedding; using LSTM to predict embedding based on previous ones; adjust embeddings on a per-sample basis.

### Weaknesses
I could grasp the main ideas of the paper but some parts are not clear to me. For example, how exactly L_{surrogate} is computed? There are more in the question section.

Comparing Table 1 and Table 2, it seems the key to beat the baselines is the adjustment. Without it, the proposed method (which is quite complex) will not champion the others. This is not too surprising as the model is adjusted per-sample. But it comes with more computational cost and there is no address on this aspect in the paper.

Following from the above, the paper used many ideas and I think many of them, if studied thoroughly, can be a paper itself. For example, how effective learning is in the embedding space than in the original parameter space? How well one could predict parameters of the model in the new period, compared to parameters trained in the new period? What is the impact of just having per-sample adjusted parameters? How efficient is the adjustment? Is it generally applicable for other models? I would think the paper needs simplification, rather than complication.

### Questions
What is L_{surrogate}? In the paper it’s written to use a loss network s, but how the loss is computed is still not clear to me. 

For the adjustment of H_p for every sample, does it need to load a checkpoint for every sample? This can be very in-efficient. 

What is STOPGRAD in eq(7)? Does H_P in eq(7) mean the prediction after adjustment or the base embedding?

In Figure 3(b), I thought the L_{surrogate} is used to find the sample specific embedding, which is the adjustment. But then why before L_{surrogate}, there is a red-block of adjustment?

Why not take the model trained in the previous period as a baseline? This should be a good sanity check for all continue learning methods.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
