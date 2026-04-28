# TwinsFormer: Revisiting Inherent Dependencies via Two Interactive Components for Time Series Forecasting

- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 5, 6, 5, 5

## Abstract
Due to the remarkable ability to capture long-term dependencies, Transformer-based models have shown great potential in time series forecasting. However, real-world time series usually present intricate temporal patterns, making forecasting still challenging in many practical applications. To better grasp inherent dependencies, in this paper, we propose \textbf{TwinsFormer}, a Trans\underline{former}-based model utilizing \underline{tw}o \underline{in}teractive component\underline{s} for time series forecasting. Unlike the mainstream paradigms of plain decomposition that train the model with two independent branches, we design an interactive strategy around the attention module and the feed-forward network to strengthen the dependencies via decomposed components. Specifically, we adopt dual streams to facilitate progressive and implicit information interactions for trend and seasonal components. For the seasonal stream,  we feed the seasonal component to the attention module and feed-forward network with a subtraction mechanism. Meanwhile, we construct an auxiliary highway (without the attention module) for the trend stream by the supervision of seasonal signals. Finally, we incorporate the dual-stream outputs into a linear layer leading to the ultimate prediction. In this way, we can avoid the model overlooking inherent dependencies between different components for accurate forecasting. Our interactive strategy, albeit simple, can be adapted as a plug-and-play module to existing Transformer-based methods with negligible extra computational overhead. Extensive experiments on various real-world datasets show the superiority of TwinsFormer, which can outperform previous state-of-the-art methods in terms of both long-term and short-term forecasting performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents TwinsFormer, a Transformer-based framework designed for time series forecasting. The primary innovation lies in its ability to model interactions between the trend and seasonal components of time series data via an interactive dual-stream design.

### Strengths
+ The proposed framework addresses the challenge of accurately capturing the intricate temporal dependencies between trend and seasonal components in time series forecasting. The dual-stream design and interaction mechanism are novel, offering an efficient way to learn the dependencies between these components while maintaining computational efficiency.
+ The paper provides a clear and rigorous explanation of why traditional independent decomposition models (which separate trend and seasonal components) might miss crucial interactions.
+ The authors highlight that their interactive strategy can be applied to existing Transformer-based architectures with minimal computational overhead. 
+ Extensive experiments across 13 real-world datasets, including both short-term and long-term forecasting scenarios, demonstrate the effectiveness of TwinsFormer. The paper shows that it outperforms several state-of-the-art models, such as iTransformer, TimeMixer, and Crossformer, across a variety of metrics (MSE, MAE).

### Weaknesses
 +  The paper uses a simple moving average kernel for decomposing the time series into trend and seasonal components, which assumes that the trend and seasonal components are captured well by linear operations. Could more sophisticated decomposition techniques (such as wavelet or non-linear methods) potentially offer better results? Specifically, the moving average kernel, with its fixed window size, may struggle to adapt to time series with varying seasonal patterns or abrupt changes in trend. This limitation could lead to suboptimal decomposition, impacting the overall forecasting accuracy, especially for time series with complex dynamics.
+ The paper doesn’t provide detailed analysis regarding the sensitivity of the model’s performance to hyperparameters, especially those related to the decomposition mechanism (such as kernel size). The lack of a hyperparameter sensitivity analysis makes it difficult to assess the robustness of the model. It is unclear how the performance would change with different kernel sizes, and whether the default value is optimal across all datasets. This is a critical consideration, as the optimal kernel size may be dataset-dependent and significantly impact the decomposition quality and subsequent forecasting performance.
+ The dual-stream design, although innovative, introduces significant architectural complexity.  While the paper mentions that the model is computationally efficient, it does not provide a comprehensive analysis of the computational cost for both training and inference across different model sizes (e.g., small, medium, and large). The absence of a detailed computational cost analysis, particularly concerning memory usage and training time, makes it challenging to evaluate the practical applicability of the model, especially in resource-constrained environments. It is essential to understand how the computational demands scale with model size and data complexity.
+ The paper introduces a subtraction mechanism in the seasonal branch of the model to eliminate redundant information. How about other operations like concatenation or addition? The choice of subtraction as the interaction mechanism is not sufficiently justified. While it may help in removing redundant information, it is unclear whether other operations, such as concatenation or addition, could potentially offer better performance or capture different aspects of the interaction between trend and seasonal components. A more thorough exploration of different interaction mechanisms is needed.

### Questions
Check Weaknesses

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a Transformer-based model (TwinsFormer) to improve time series forecasting by capturing long-term dependencies. The key point of the model is to enable the interaction of decomposed time series components, which is realized by employing a dual-stream approach with an attention module and a feed-forward network to strengthen dependencies between trend and seasonal parts. Experiments demonstrate that TwinsFormer outperforms previous state-of-the-art methods in long-term and short-term tasks. Further analysis reveals that the interactive strategy can be a plug-and-play module to existing Transformer-based methods.

### Strengths
* The motivations are well-summarized and the paper's writing is easy to follow.
* There is a good summary of the differences from previous works, such as the decomposition of observed time series rather than the time series embeddings, which I think is reasonable.

### Weaknesses
 * This work is not innovative in the decomposition, which I think is worth further exploration. The claim "TwinsFormer is the first attempt to consider interactions between decomposed components on Transformer for time series forecasting" can be overstated (e.g., TimeMixer).
* How about the results of Table 1 if using a longer lookback length? I think the lookback window of lookback=96 is too short to obtain the robustly decomposed trend and seasonal components. These results would greatly influence my evaluation of this work.
* Whether the ablation in Table 4 can further improve the performance on more recent Transformer-based forecasters, for example, PatchTST, iTransformer, and Crossformer.
* Does the model adopt channel independence? Are the interactions between decomposed components carried out independently within the channel or among multiple channels?
* The efficient version of TwinsFormer is trained with 20% variates and prediction for all variates, which is the same as iTransformer. I don't think it is an innovative part to place these experiments. Similarly, other model analyses basically follow the previous work (such as TimeMixer), so I think Sections 4.2 and 4.3 lack originality and do not provide enough insight to readers. It should undergo a major revision to delve more into the perspective of time series decomposition.

### Questions
* It seems that the model only decomposed input series at the beginning. Could you verify that the subsequent TwinsBlock can still adequately deal with trend and seasonal components? Does it matter if you randomly swap the Treand-Seasonal input for a TwinsBlock in the middle of the model?
* Can the author provide more concrete showcases: How does Twinsformer cope with the intricate interactions between decomposed components to precisely unravel the inherent dependencies as mentioned in Figure 2?
* Why does Figure 1 compute MAE instead of MSE?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed TwinsFormer  for time series forecasting that uses dual streams to interactively process trend and seasonal components, enhancing dependency learning between them. By integrating these interactions within the attention and feed-forward layers, TwinsFormer improves forecasting accuracy without adding significant computational cost.

### Strengths
(1) The proposed TwinsBlock is novel and well justified by rationality analysis, ablation and visualization analysis.

(2) The proposed TwinsFormer demonstrates better performance than  baseline models  in most datasets,

(3) The paper is well-organized and easy to follow.

### Weaknesses
 (1) The improvements of TwinsFormer over baselines in the Main results (Tables 1 and 2) are quite marginal.  Generally, the improvement over the second-best baseline is less than **0.02** for MSE and MAE metrics. 

 (2) Given the marginal improvements over baselines shown in Tables 1 and 2, it is essential to include the variance of repeated experiments for a more accurate assessment.

 (3)  In Equation (9), the authors justify their design with the assumption of "replacing [.] with +". Given that '+' appears to be a more appropriate choice based on your analysis, why not simply sum up \( X_t \), \( g(X_s) \), and \( h(X_s, g(X_s)) \)? Is there any evidence to support concatenation as the optimal design choice?

 (4) It seems that all evaluations are currently conducted on multivariate forecasting tasks. Including evaluations on univariate forecasting tasks would provide a more comprehensive assessment for TwinsFormer.

### Questions
(1) Is the improvement in Tables 1 and 2 statistically significant? Could you report the confidence level using a statistical hypothesis test ,e.g. T-test?

(2) Does the proposed TwinFormer still work well for univariate forecasting tasks?

### Soundness
3

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
4

### Summary
The paper proposed the TwinsFormer architecture for time series forecasting. TwinsFormer decomposes the observed time series into trend and seasonal components and designs a dual-branch Transformer architecture that models their interaction at each layer. For the seasonal branch, the author applies an FFN + attention architecture that is similar to iTransformer. The only difference is that author subtracts the attention output from the input embeddings to capture the seasonal variations. For the trend branch, the autor adopts a convolution-based structure called Interactive Module (IM). The author compared TwinsFormer with a few baselines on 9 datasets and also conducted ablation study on the design choices. Experiments show that TwinsFormer consistently outperforms baselines. In addition, the author applied the dual-branch design in other transformer-based time-series forecasting models and observed consistent performance boost.

### Strengths
The paper is well-written and it is easy to understand the design and motivation of TwinTransformer. The author also conducted experiments and ablation studies on a variety of datasets to verify the conclusions.

### Weaknesses
The contribution is marginal because several previous papers (e.g., DESTformer: A Transformer Based on Explicit Seasonal–Trend Decomposition for Long-Term Series Forecasting, https://www.mdpi.com/2076-3417/13/18/10505) have tried to decompose the Transformer into trend and seasonal component and fuse the encoded features at each layer. Actually, if we closely insepct Table 3, Variant #2 performs similarly as TwinsFormer. This may indicate that part of the dual-branch design (e.g., the choice of using Interactive Module IM) is not that beneficial compared with the high-level choice of separately modeling the seasonal and trend features. In addition, the performance boost of TwinsFormer may come from adopting iTransformer in the seasonal branch. We can compare the iTransformer column and TwinsTransformer column in Table 1, 2, 6, 7 and notice that iTransformer performs well in most benchmarks. The core idea of using a dual-branch architecture for time series decomposition is not novel, and the specific implementation details, such as the Interactive Module (IM), do not demonstrate a significant performance advantage over simpler alternatives. The ablation study, particularly the performance of Variant #2, suggests that the primary benefit might stem from the separate processing of trend and seasonal components rather than the specific design of the IM or the interaction mechanism. Furthermore, the consistent performance of iTransformer across various benchmarks raises concerns that the reported improvements of TwinsFormer might be largely attributed to the strong performance of the iTransformer backbone within the seasonal branch, rather than the novel contributions of the proposed architecture.

### Questions
What's the variance of the performance numbers in Table 3? Are they really significant?

### Soundness
3

### Presentation
4

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
The paper proposes a method to improve transformer based time series forecasting. A dual stream architecture is proposed, where the multi-variate time series is decomposed into trend and seasonality components. Then the learned embedding for each of these components are then combined through an interactive module, to give the final combined representation. To my understanding, the key differentiator from existing works that do decomposition, is that, Twinsformer learns a better interaction between the decomposed components leading to a better downstream forecasting performance. Empirical performance is quite detailed on long term and short term forecasting tasks, and compared to the baselines, the performance is quite strong. Ablation studies appear comprehensive.

### Strengths
Originality & Significance
- strong empirical performance
- interesting idea to address interaction among different components, but not very novel

### Weaknesses
 - the motivation is not very convincing
- "inherent dependencies" are not well defined
- lines 79-82, motivation on channel 11 is not clear, how does this make a case for "inherent dependencies", or what that is?
- lines 191-194 - it seems the goal has changed to address the problem of limitations in "multi-variate correlation" which is addressed by Twinsformer - makes it further unclear what the goal is
- many of the design choices also do not seem to have a clear motivation, and seem heuristic, and are post-hoc justified in ablation rather than a clear reason for selection

### Questions
- Please help clarify the motivations and the key problem being addressed through the proposed module, as it seems rather ad-hoc and heuristic

### Soundness
2

### Presentation
2

### Contribution
2
