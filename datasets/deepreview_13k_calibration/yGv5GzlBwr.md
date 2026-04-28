# Diffusion Auto-regressive Transformer for Effective Self-supervised Time Series Forecasting

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Self-supervised learning has become a popular and effective approach for enhancing time series forecasting, enabling models to learn universal representations from unlabeled data. However, effectively capturing both the global sequence dependence and local detail features within time series data remains challenging. To address this, we propose a novel generative self-supervised method called \textbf{TimeDART}, denoting \textbf{D}iffusion \textbf{A}uto-regressive \textbf{T}ransformer for \textbf{T}ime series forecasting. In TimeDART, we treat time series patches as basic modeling units. Specifically, we employ an self-attention based Transformer encoder to model the dependencies of inter-patches. Additionally, we introduce diffusion and denoising mechanisms to capture the detail locality features of intra-patch. Notably, we design a cross-attention-based denoising decoder that allows for adjustable optimization difficulty in the self-supervised task, facilitating more effective self-supervised pre-training. Furthermore, the entire model is optimized in an auto-regressive manner to obtain transferable representations. Extensive experiments demonstrate that TimeDART achieves state-of-the-art fine-tuning performance compared to the most advanced competitive methods in forecasting tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TimeDART (Diffusion Auto-Regressive Transformer for Time Series Forecasting), a novel self-supervised learning framework designed to enhance time series forecasting. TimeDART addresses key challenges in the field, particularly capturing both long-term dependencies and local features within time series data.

### Strengths
+ Combining self-attention for inter-patch dependencies, diffusion mechanisms for intra-patch dependencies, and auto-regressive optimization is an interesting and innovative approach to time series forecasting.
+ The diffusion-based reverse process for reconstructing the sequence is novel in the context of time series forecasting.
+ Good writing and organization.

### Weaknesses
 + The combination of Transformer-based attention mechanisms with the denoising diffusion process introduces substantial computational overhead. The paper mentions running experiments on a single NVIDIA RTX 4090 GPU, but it doesn't provide detailed insights into the time and memory consumption required for training. How scalable is TimeDART for larger datasets or real-time applications? Specifically, the paper lacks a thorough analysis of how the computational cost scales with increasing sequence lengths, patch sizes, and the number of diffusion steps. This is critical for assessing the practical applicability of the method.
+ The experiments conducted on noise scheduling, the number of diffusion steps, and the number of layers in the denoising network highlight a significant degree of sensitivity to hyperparameter selection. How the model will perform well in practical settings with minimal tuning? The paper should provide more guidance on how to choose these hyperparameters, potentially through a sensitivity analysis or a discussion of the underlying principles that guide their selection. The lack of a clear strategy for hyperparameter tuning makes the method less accessible to practitioners.
+ The cross-domain evaluation shows strong results on energy datasets but weaker performance on datasets like Exchange. Is TimeDART overly sensitive to the type of data it is pre-trained on? For instance, does it struggle with financial or highly volatile datasets because of the lack of shared characteristics between domains (e.g., energy vs. finance)? Could this method benefit from domain adaptation techniques to make the cross-domain transfer more robust? The paper should investigate the reasons behind the performance differences across datasets and explore potential solutions to improve the model's generalization capabilities. It is unclear if the pre-training captures universal time-series features or if it is biased towards specific data characteristics.
+ The model uses a denoising diffusion loss, which may not be the most suitable for every type of forecasting task. How does TimeDART perform with other loss functions (e.g., Quantile Loss, Huber Loss) that are often used in time series forecasting tasks where the goal is to forecast confidence intervals or robustly handle outliers? The paper should explore the use of alternative loss functions in downstream tasks, particularly those that are more robust to outliers or that allow for the estimation of prediction intervals. The current focus on MSE may not be sufficient for all practical applications.

### Questions
Check Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Recently, effectively capturing both the global sequence dependence and local detail features within time series data remains challenging. To address this, the authors propose a novel generative self-supervised method called TimeDART, denoting Diffusion Auto-regressive Transformer for time series forecasting.

### Strengths
1. We propose a novel generative self-supervised learning framework, TimeDART, which in tegrates diffusion and auto-regressive modeling to effectively learn both global sequence dependencies and local detail features from time series data, addressing the challenges of capturing comprehensive temporal characteristics.
 2. We design a cross-attention-based denoising decoder within the diffusion mechanism, which enables adjustable optimization difficulty during the self-supervised task. This design significantly enhances the model’s ability to capture localized intra-patch features, improving the effectiveness of pre-training for time series forecasting. Diffusion models and autoregressive attention mechanisms are rare collaborations in temporal tasks, and this field brings new ideas. 
3. The experimental results show that the combination of Mamba and propagation mechanism is very effective, and it also exceeds the predictive performance of supervised learning.

### Weaknesses
1. The reviewer is concerned about the computational overhead associated with this approach. The reviewer's core concern stems from the introduction of diffusion mechanisms, which can lead to a substantial increase in training and inference overhead for the model as a whole. If the model is expensive, the computational conditions required to solve the real task will be severe. Therefore, the authors need to report the actual time of the training and inference phase of other baseline models in the future and report the GPU and server model.
2. The motivation for choosing to use a causal mechanism in Transformer requires further explanation. After all, time series data is encoded with more complex patterns. In particular, there are random changes caused by extreme weather events in the meteorological data, and this causal relationship is strong. But many things cause and effect is unclear, so whether such a component is appropriate needs to be used for the specific task.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To effectively capture both the global sequence dependence and local detail features within time series data, this paper proposed a novel generative self-supervised method called TimeDART, denoting Diffusion Auto-regressive Transformer for Time series forecasting. Extensive experiments demonstrate that TimeDART achieves state-of-the-art fine-tuning performance compared to the most advanced competitive methods in forecasting tasks.

### Strengths
1. Well-written
2. The author provides the code
3. The performance of the model is proved by experiments

### Weaknesses
1. In the original paper [1], the performance of patchTST seems to be better, and it is suggested that the author should evaluate it more fairly.
2.  Why didn't the author consider evaluating the performance of classification tasks? Currently, aside from forecasting tasks, most self-supervised learning models [2] also focus on the performance of classification tasks. This is because the main purpose of self-supervised learning is to enhance the quality of representations generated by the model and to uncover key semantic features, which is especially important for classification tasks.
3.  A crucial role of self-supervised learning is to improve the performance of backbone models [3], but the author only uses Transformer as the backbone. I am curious whether the proposed method would still be effective if MLP or TCN were used as the backbone.
4. The author's core motivation remains to capture both global and local dependencies, which is similar to most existing works [1] [4]. In other words, this paper lacks a central challenging problem, making the contribution at the motivational level somewhat limited.
5. Considering that the core motivation of this paper is to capture global and local dependencies, I suggest the author evaluate the model's performance on datasets with stable patterns, such as PEMS04. This is because datasets like ETT and Exchange have inherent issues with distributional shifts [5].

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes TimeDART, a novel self-supervised learning paradigm that hopes to learn transferable generic representations from unlabeled data through pre-training and then fine-tune them to different downstream tasks, e.g., forecasting tasks, etc. In this paper, a unified self-supervised learning framework is established by fusing the diffusion-denoising process and autoregressive modeling. By learning global sequence dependencies and local detail features in multi-domain time series data, the model's ability to capture comprehensive time series features and cross-domain generalization ability are improved. Specifically, TimeDART designs a cross-attention based denoising decoder in the diffusion mechanism, which improves the effectiveness of time series pre-training by significantly enhancing the model's capability to capture features within local blocks.

### Strengths
The authors outline the main approaches to self-supervised learning in the time series domain, including mask reconstruction and contrast learning, and analyses the shortcomings of the two existing self-supervised learning paradigms separately, e.g., the mask reconstruction-based approach introduces a huge gap between pre-training and fine-tuning, and the contrast-learning-based approach prioritizes the capture of discriminative features, which lead to a huge discrepancy between pre-training tasks and fine-tuning tasks.

In addition, the authors raise two issues critical to the self-training paradigm, 1) how to narrow the gap between the pre-training target and the downstream fine-tuning task, and 2) modelling both long-term dependencies and local pattern information in the self-supervised pre-training phase. However, we believe that TimeDART is not the best solution to these problems.

### Weaknesses
 **Weakness 1:** 

As a Diffusion-based model, we would like to introduce more valuable metrics to fully examine the performance of the proposed TimeDART. Specifically, in order to evaluate the prediction accuracy and generalization capability of TimeDART from both forecasting and generation perspectives, existing studies often include the following four metrics (including Context-FID, Correlational Score, Discriminative Score, and Predictive Score) for comprehensively evaluating the performance of Diffusion methods. 

In addition, the proposed TimeDART is not compared with advanced Diffusion-based approaches, such as Diffusion-TS[1], mr-Diff[2], and MG-TSD[3]. We believe that the introduction of more competitive and up-to-date approaches can demonstrate the effectiveness of the proposed method more objectively.

**Weakness 2:** 

In the in-domain setting (Table 2), there are the following weaknesses: 

* The performance improvement of the proposed TimeDART over SOTA methodologies SimMTM and PatchTST is less than 5%, which indicates that the performance improvement of the model is not obvious.

* In addition, we note that the performance of "Random Init" shown in Table 1 is slightly worse than Supervised PatchTST. Does this indicate that in the supervised setting of a single domain, the proposed model architecture exhibits worse performance compared to PatchTST? If the modeling capability of the TimeDART is poor in small datasets, the model will often show worse generalization ability in cross-domain pre-training, which leads to the rationality of the model architecture being questioned.

**Weakness 3:** 

In the cross-domain setting (Table 3), there are the following weaknesses that can be improved: 

* The model is pre-trained on only two power domain datasets (ETT and Electricity). As a result, only the single domain information is included in the model, which limits the generalization ability of the model under cross-domain challenges. Recent unified time series forecasting models include two paradigms. The first is unified models based on LLM fine-tuning, such as OneFitsAll[4] and TimeLLM[5]. This is followed by pre-training on a multi-domain hybrid Time series dataset followed by fine-tuning on specific downstream tasks, e.g., Timer[6], Moriai[7] and MOMENT[8]. In conclusion, we believe that introducing information from more domains during pretraining can improve the cross-domain generalization of the model, and TimeDART is expected to be pretrained on a wider range of datasets. 

* Table 3 only shows the performance comparison of TimeDART under different Settings; however, it lacks the comparison with the latest baseline. In fact, recent UniTime[9] have achieved joint pretraining across multiple domains. Therefore, we expect the authors to introduce more advanced baselines to compare with TimeDART, which will help us get a comprehensive understanding of TimeDART's performance.

**Weakness 4:** 

In ablation experiments (Table 4), there are the following drawbacks: 

* There is a lack of detailed descriptions specific to ablation experiments, such as in-domain Settings or cross-domain Settings. When we compare the results in Table 4 and Table 2, we can speculate that the ablation experiment is only carried out in the in-domain setting. However, in the cross-domain setting, the reader is eager to know whether the proposed autoregressive diffusion model is effective. 

* In Table 4," The "W/o AR" model obtained the improved "W/o AR" model after introducing the Diffusion-based decoder; However, the performance of the latter was slightly degraded on the ETTh2 and Electricity datasets. This may indicate that the predictions of the model become worse when the diffusion model is introduced. This casts doubt on the rationality of introducing a Diffusion-Denoising process in the Decoder.

### Questions
**Question 1:** 

This paper uses an autoregressive prediction paradigm, however autoregressive approaches generally suffer from error accumulation and high inference time overheads. To the best of our knowledge, TimeDART has not designed a special training-inference strategy or model architecture to mitigate these problems. Further discussion of TimeDART's limitations in the autoregressive prediction paradigm is urgent and necessary.

**Question 2:** 

As the authors say ‘we adopted the channel-independence setting’. However, for datasets with a very large number of channels, such as ECL and Traffic, how can a channel-independent design establish connections between multiple channels? Meanwhile, the experimental results of Crossformer[10], SAMformer[11] and iTransformer[12], show that cross-channel modelling is crucial for multivariate time series, and we believe that a discussion on inter-channel modelling for multivariate time series is necessary. However, to the best of our knowledge, TimeDART does not consider these factors in its modelling.

**Question 3:** 

See Weakness 2,3 for our concerns about the experimental results, and we believe that the introduction of competitive and up-to-date baselines is considered necessary.  In addition, the authors are expected to explain the phenomena in the ablation experiments, details of which can be referred to Weakness 4.

**Reference:** 

10) Zhang, Yunhao and Junchi Yan. “Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting.” ICLR 2023.

11) Ilbert, Romain et al. “SAMformer: Unlocking the Potential of Transformers in Time Series Forecasting with Sharpness-Aware Minimization and Channel-Wise Attention.” ICML 2024.

12) Liu, Yong et al. “iTransformer: Inverted Transformers Are Effective for Time Series Forecasting.” ICLR 2024.

### Soundness
1

### Presentation
2

### Contribution
2
