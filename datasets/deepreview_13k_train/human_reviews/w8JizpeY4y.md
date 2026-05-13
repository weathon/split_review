# Time Series Continuous Modeling for Imputation and Forecasting with Implicit Neural Representations

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
We introduce a novel modeling approach for time series imputation and forecasting, tailored to address the challenges often encountered in real-world data, such as irregular samples, missing data, or unaligned measurements from multiple sensors. Our method relies on a continuous-time-dependent model of the series' evolution dynamics. It leverages adaptations of conditional, implicit neural representations for sequential data. A modulation mechanism, driven by a meta-learning algorithm, allows adaptation to unseen samples and extrapolation beyond observed time-windows for long-term predictions. The model provides a highly flexible and unified framework for imputation and forecasting tasks across a wide range of challenging scenarios. It achieves state-of-the-art performance on classical benchmarks and outperforms alternative time-continuous models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The problem setting is time series data, with irregular sampling and missing data. The paper proposes a method that learns a (conditional) implicit neural representation for time series. The model can be used for forecasting and imputation. It shows promising results on these tasks, compared to other baselines.

### Strengths
Since the method is a pretty straightforward application of Dupont et al. (2022) to time series, the approach is sound.

The results on imputation are decent. The methods shows promising results in terms of MAE and the imputation in Figure 3 looks good compared to BRITS. However, it seems there is still a lot of performance improvement left on the table. Electricity is a pretty simple periodic dataset so I can imagine achieving better results with further tuning or some other model.

Forecasting results are again good but the model is only matching the competitors. Forecasting + imputation is showing even better results and has some potential real-world applications. However, some other models can be included in the comparison here.

### Weaknesses
The approach has limited novelty since it's mostly building upon known previous work. This same architecture can be applied to images, point clouds, and so on. Although the discussion of implementation choices is a nice addition, they are again not necessarily time series dependent. The core idea of using an implicit neural representation (INR) conditioned on time for time series data, while sound, lacks significant innovation beyond existing applications of INRs in other domains. The specific architecture choices, such as the MLP used for the INR, are standard and do not introduce novel time-series-specific mechanisms. The discussion of implementation choices, while helpful, does not address the fundamental lack of novelty in the approach itself.

Results on imputation are decent, but the method is not beating other baselines most of the time. It is usually close to BRITS and some other baselines. This might indicate used datasets are too simple. Also, using such regular data for imputation is not ideal since one of the points of the proposed method is that it can handle irregular sampling rate. Something like MIMIC dataset might be a better choice, especially since it already contains missing values. The performance of the proposed method on imputation tasks is not consistently superior to existing baselines, suggesting that the method may not be fully exploiting the potential of INRs for time series imputation. The datasets used for evaluation, while common, may not be sufficiently complex to highlight the advantages of the proposed approach, particularly its ability to handle irregular sampling. The lack of experiments on real-world, irregularly sampled datasets, such as MIMIC, limits the practical relevance of the results.

According to Table 16, the model is more costly compared to already costly transformer-based models. The computational cost of the proposed method, as indicated by Table 16, is a significant drawback, especially when compared to transformer-based models, which are already known for their high computational demands. This increased cost may limit the practical applicability of the method, particularly in resource-constrained environments. According to Table 17, PatchTST is often outperforming proposed method which means that it's better at adapting to new time series, contrary to what is stated in the main text. The claim that the proposed method is better at adapting to new time series is not supported by the results in Table 17, where PatchTST often outperforms the proposed method. This discrepancy raises concerns about the generalization capabilities of the proposed method and its ability to adapt to new time series effectively.

As a side note, it would be interesting to have a probabilistic version of this model.

The biggest drawbacks of this paper are lack of novelty, not so stellar results and not applying this method to actual continuous-in-time data.

### Questions
- Can you compute MAE in Figure 3 for a naive baseline that simply connects training points with a line?

- Can you explain why the results in Table 13 and 14 differ for AutoFromer and Informer?

- If I understand the setting in 4.3 correctly, all models for imputation from 4.1 should be able to produce imputed values and forecast. Then, they should be included in Table 2.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new algorithm for time-series imputation and forecasting via using implicit neural representations. The proposed method particularly leverages an idea of latent modulation, extending a previous approach by making the latent vectors evolve over time. During the inference, for both imputation and forecasting, the method assumes there exist a few samples and fine-tunes the INR via auto-decoding. The paper tests the proposed methods on well-known time-series benchmark datasets and compares the result with several time-series modeling methods that can be considered as the current state-of-the-art.

### Strengths
- The paper is written clearly, elaborating the architecture design, and training/test algorithms. 

- Time-series modeling has not been investigated much in the INR literature and this paper provides some insights that modeling time-series data in a continuous neural function can be beneficial.

- The paper compares the proposed method with several important baselines.

### Weaknesses
 - Although the domain of the application (i.e., time-series modeling) is new and the proposed design brings an idea of the latent state evolution (in forecasting), the novelty seems to be limited. The overall architectural design follows the FFN architecture (Tancik, et al, 2020) without any consideration on how to handle multivariate time-series. Also, the idea of the latent modulation and the meta-learning-based training algorithm largely follow the previous approach (Dupont, et al, 2022). Finally, a similar idea of employing temporally-refined latent variables has been explored in (Yin, et al, 2023).

- Regarding auto-decoding process:
  
  - For imputation, it is natural to assume that there is a given set of measurements for a new time-series, and to set up the goal to fill-in unseen data via imputation.  For forecasting, however, the assumption of having a separate training period and a look-back window raises some concerns. Having a separate look-back window suggests that the method needs to wait until the new observations are collected to make forecasting. Some of the datasets that are considered in the paper have hourly sampling rate and this time gap might provide enough time to fine-tune other baseline models (with many model parameters, e.g., Transformers). If the ultimate goal is to achieve accurate prediction, with the given time period (an hour), fine-tuning those baselines with a new observation may provide better prediction results.  

  - Similarly, another concern is fairness on the comparisons. Although it is just 3 gradient steps, auto-decoding is considered as solving an optimization problem to fine-tune the model for the new observations. What happens if the small portion of the other baselines (e.g., the last layer) is fine-tuned during the inference? For example, in forecasting, the model can be fine-tuned after making predictions on the current sliding window and then make predictions on the next sliding window with the updated models. 
 
  - Although the method seems to provide accurate predictions both in imputation and forecasting, the method seems to struggle in predicting peaks accurately. In many applications, predicting peaks accurately would have more importance than simply minimizing MSEs (e.g., to properly prepare the electricity supply or properly set up the cost during the peak time period). Based on the eye-ball examination (Figure 5 for example), the model does not seem to provide accurate predictions in peak values.

### Questions
- As mentioned in the weakness section, could the author provide more justifications for performing auto-decoding while other baselines are used only for inference? Also, could the authors mention more about the fairness of the comparisons? 

- Appendix section D, Tables 13 and 14 emphasize the performance degradation in Transformers models as the testing window is far apart from the training period. Would there be realistic cases where we have only the old history for training, measurements are stopped for a while, and collecting results regularly again afterwards?

- In Appendix, the paper provides experimental results for varying dimensionalities on the latent vectors and the number of gradient steps in auto-decoding during the inference. However, these experiments are performed in a limited experiment setting. Could the authors provide more insight on the effect of these hyper-parameters? For example, Table 6 provides the results with a specific dataset (Electricity) with a horizon length 720 and a look-back window length 512 and essentially says there will be no improvement after 10 or 50 gradient steps. Would this observation be valid for other datasets, for other sizes of windows? Also, what happens if the dimensionality of the latent vector is changed? Are these results also obtained by the multiple number of runs? 

- Could the authors also provide justifications on not to include other time-continuous models for their baselines? Such as neural ODEs and their variants for irregular time-series modeling?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new method, TimeFlow, for time series analysis aimed to address imputation and forecasting tasks under the realistic issues of irregularly sampled and unaligned data. The authors compare with many SOTA methods and clearly showcase where their novel method outperforms other methods.

### Strengths
Excellent explanation of the method and figures diagramming what was done and the distinctions between training and inference periods, for both the imputation and the forecasting applications. 

The algorithm's ability to be applied to previously unseen datasets/time series is a definite strength.

### Weaknesses
The conclusion/discussion was quite brief. I would have loved to read more about limitations and the approach for extending this to the multivariate case. 

Section 3.4 was a strong inclusion of rationale for their authors' choices, but the disjoint list of conclusions and redirection to the Appendix was weak. Perhaps some (unnecessary) details of the datasets could be left to the appendix to provide space for more description of the actual method.

To better compare and align this method to others in the literature, could the authors expand on statements such as what exactly they mean by how transformer models 'often suffer from significant performance degradation'? (Which performance metrics?)

Similarly, when discussing efficiency: 'less efficient than the aforementioned discrete models for regular time series' do the authors mean sample efficiency? Scalability of the algorithm to multiple dimensions or longer time series?  

The 'efficient adaptation in latent space' is interesting. Is there anything to be learned about the structure of the latent spaces and how they are modified between potentially similar datasets? Which could explain perhaps why other models require a full retraining. 

Would this work for imputation or forecasting not on a grid? As in, could forecasted data be easily predicted on an arbitrary grid? Is this related to the discrete performance in Table 2?

### Questions
To better compare and align this method to others in the literature, could the authors expand on statements such as what exactly they mean by how transformer models 'often suffer from significant performance degradation'? (Which performance metrics?)

Similarly, when discussing efficiency: 'less efficient than the aforementioned discrete models for regular time series' do the authors mean sample efficiency? Scalability of the algorithm to multiple dimensions or longer time series?  
 
The 'efficient adaptation in latent space' is interesting. Is there anything to be learned about the structure of the latent spaces and how they are modified between potentially similar datasets? Which could explain perhaps why other models require a full retraining. 

Would this work for imputation or forecasting not on a grid? As in, could forecasted data be easily predicted on an arbitrary grid? Is this related to the discrete performance in Table 2?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
