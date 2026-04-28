# iTransformer: Inverted Transformers Are Effective for Time Series Forecasting

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
The recent boom of linear forecasting models questions the ongoing passion for architectural modifications of Transformer-based forecasters. These forecasters leverage Transformers to model the global dependencies over \emph{temporal tokens} of time series, with each token formed by multiple variates of the same timestamp. However, Transformers are challenged in forecasting series with larger lookback windows due to performance degradation and computation explosion. Besides, the embedding for each temporal token fuses multiple variates \update{that represent potential delayed events and distinct physical measurements}, which may fail in learning variate-centric representations and result in meaningless attention maps. In this work, we reflect on the competent duties of Transformer components and repurpose the Transformer architecture without any modification to the basic components. We propose \textbf{iTransformer} that simply \update{applies the attention and feed-forward network on the inverted dimensions}. Specifically, the time points of individual series are embedded into \emph{variate tokens} which are utilized by the attention mechanism to capture multivariate correlations; meanwhile, the feed-forward network is applied for each variate token to learn nonlinear representations. The iTransformer model achieves state-of-the-art on challenging real-world datasets, which further empowers the Transformer family with promoted performance, generalization ability across different variates, and better utilization of arbitrary lookback windows, making it a nice alternative as the fundamental backbone of time series forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explored a new angle to apply Transformer model to the multivariate time-series forecasting problem. Without the modification of the original transformer component, the proposed iTransformer inverted the duties of the self-attention mechanism and the feed-forward network. In iTransformer, the feed-forward network was used for series encoding, while the self-attention mechanism captured the correlation among different variates. The authors conducted experiments on six real-world datasets to evaluate the proposed model.

### Strengths
1.	This paper provided a simple and effective inverted view to improve transformer-based multivariate time-series forecasters.

2.	Compared with the previous use of Transformer structure (without invert), the iTransformer showed some advantages, including better generalization on unseen variates, and the desired performance improvement over enlarged historical information.  

3.	Extensive experiments on different multivariate time-series forecasting tasks were conducted for evaluation. The author compared the proposed model with various baselines, along with a comprehensive modal analysis.

### Weaknesses
1.	According to Table 3 and Table 7, most of the result values are relatively small. This suggests that some marginal improvement may be susceptible to random factors (e.g., iTransformer v.s. PatchTST on ETT and Weather dataset, iTransformer v.s. SCINet on PEMS dataset). Therefore, I recommend reporting the standard deviation under different random runs and adding a significance test to provide further insights. The lack of statistical rigor in the comparison makes it difficult to ascertain whether the observed improvements are truly meaningful or simply due to random variations in the training process. Specifically, the reported MSE values are often below 0.5, and differences between models are often in the range of 0.001-0.005, which could easily be within the noise of the experiment. A more robust statistical analysis is needed to validate the claims of superior performance.


2.	Although the proposed efficient training strategy can reduce the required memory, it would still be better to compare its efficiency with linear models, since recent studies have indicated their advantages in both performance and efficiency. The paper focuses on comparing against other Transformer-based models, but it neglects to benchmark against simpler, computationally cheaper linear models. This is a significant oversight, as linear models often provide a strong baseline in time series forecasting, and their efficiency is a known advantage. Without this comparison, it is difficult to assess the true practical benefit of the proposed iTransformer, especially in resource-constrained environments. The paper needs to demonstrate that the performance gains justify the additional computational cost compared to linear models.

### Questions
1.	Can you please explain why the TiDE results are so different from those reported in their original paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a simple variant of transformer for time series forecasting, where the embedding is applied on each time series and the attention is across each variate. The idea is simple and effective. The improved performance is shown on various real-world datasets. The paper is well-written and easy to read. The idea can be viewed as a principal way to be adopted on various transformer-based architectures. The numerical experiments on different architectures and analysis of representations/correlations greatly enhance the importance of this work.

### Strengths
The authors propose a principal way to apply the transformer-based model for time series forecasting. The idea is simple and effective, and the effectiveness is demonstrated via extensive experiments and ablation studies.

### Weaknesses
The paper is relatively short of explanation/justification about the effectiveness of such an approach.

### Questions
1. It would be better to describe the train-validation-test split in experiments, like training in past years and predicting in the next year, as it could be tricky for data pre-processing in time series forecasting and cause data leakage issues.

2. After reading this paper, does the author implicitly assume the heterogeneity of variates is more important than temporal dependency in terms of forecasting? 

3. There are some interesting results in Table 3. Could the author comment on the not-so-good performance of the second row (both attention)?

4. A minor one: in the left panel of Figure 6, there is a little jump on the red line from 336 to 720. Any reason why? Do multiple runs help?

### Soundness
3 good

### Presentation
4 excellent

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
In this paper, Authors propose to investigate why Transformer-based models do not seem to be as efficient as Linear-based models for Multivariate Time Series Forecasting (MTSF), while they are predominant in other AI domains. They suggest that the way Transformer is implemented for MTSF is inappropriate. To better benefit from Transformer architecture, they propose to tokenize dataset based on variate and not on timestep. It ends up modifying the input and the FFN. Their proposal also uses only an encoder compared to the vanilla Transformer architecture.

Authors conduct extensive experiments with several Linear-based and Transformer-based baselines to determine the performance of their proposal. These experiments are performed over 6 usual MTSF datasets along with 6 market-based datasets. Their proposal, iTransformer, appears to achieve best predictions for all datasets despite the selected prediction horizon.

### Strengths
In my opinion, this paper will have a high impact on MTSF research and community. They back-up their proposal with extensive experiments on several datasets and compared to multiple baselines. 
The results and ablation study are discussed even though I feel it could have gone further, but the page limitation was probably the issue.

### Weaknesses
 The biggest weaknesses in my opinion are first, the writing style, which sometimes is not going to the point (could be improved to better convey the idea and have greater impact) and second that Authors fail to include some important SOTA baselines and properly synthetize/discuss CD/CI/distribution shift comparing all the baselines (including the missing ones) and iTransformer.

 The following claim “with potentially unaligned timestamps” need to be referenced or proven. Which datasets have unaligned timestamps, or by unaligned does Authors means that there are delays between values from variates? In other terms, are physical measurements unaligned (which is not the case in the considered dataset)? or do values that correspond to the same “event” appears at different timesteps for different variates (which means that there are delays, which might be the case for Traffic, but for the others, in my opinion, Authors would need to demonstrate it. For instance, in Weather (which are data from the same weather station), it is clearly not the case).

 In my opinion, Figure 1 is focusing too much on iTransformer results. Why not having each axis of the web going from 1 (in the center) to 0? For better fairness in the visualization.

 Figure 7 (b?) right part is difficult to understand without explanation of x and y axis, and what is the differences between Score Map and Correlations. What is important in this figure? How should reader interpret these lines. Why is it better than usual Transformer?

 Figure 8 needs label of x axis.

 “which can be attributed to the extremely fluctuating series of the dataset, and the patching mechanism of PatchTST may lose focus on specific locality to handle rapid fluctuation. By contrast, our proposed method aggregating the whole series variations for series representations can better cope with this situation” I would need proof for such a claim (even in appendix). First, showing this situation and second showing learning weight for iTransformer that shows it cope with the situation.

 For the experiments where only P% of the variates are used for training, as the variates are selected randomly, it would be good to perform the experiment with different set of random variates and plot an error plot or box plot. This will further highlight that the set selected randomly is not a specific case. For instance, in Figure 8 (a? left one), we could have for each % of variate the min, max, average among the different sets. Figure 5 could be a boxplot. In addition, Authors should make clear that the set of variates use with iTransformer is the same set used in CI transformer (Figure 5) to avoid any misunderstanding from Reader.

 Especially, I also expect Figure 6 for dataset like Solar energy to not be as good as the others. Because seasonality of Solar energy is high and it strongly depend on the weather, so increasing the lookback window might not be that beneficial.

### Questions
# Paper as is
As far as I am concern, the paper in its current version with some proof-reading and the following revisions can be Accepted.
 * In abstract “the duties of the attention mechanism” should be “the following duties of the […]” to make reading smoother and avoid readers from questioning on what duties means here.
 * The following claim “with potentially unaligned timestamps” need to be referenced or proven. Which datasets have unaligned timestamps, or by unaligned does Authors means that there are delays between values from variates? In other terms, are physical measurements unaligned (which is not the case in the considered dataset)? or do values that correspond to the same “event” appears at different timesteps for different variates (which means that there are delays, which might be the case for Traffic, but for the others, in my opinion, Authors would need to demonstrate it. For instance, in Weather (which are data from the same weather station), it is clearly not the case).
 * In my opinion, it is more appropriate to call Electricity dataset as ECL.
 * Reproducibility
   * Avoid confusion and precise which ETT is used. It looks like it is ETTm according to appendix (15min frequency), but is it m1 or m2? Informer results looks like ETTh though…

   * Also, precise which PEMS you use PEMS-Bay (occupancy ratio or speed in San Francisco Bay?) or other?
 * In my opinion, Figure 1 is focusing too much on iTransformer results. Why not having each axis of the web going from 1 (in the center) to 0? For better fairness in the visualization.
 * Figure 7 (b?) right part is difficult to understand without explanation of x and y axis, and what is the differences between Score Map and Correlations. What is important in this figure? How should reader interpret these lines. Why is it better than usual Transformer?
 * Figure 8 needs label of x axis.
 * “which can be attributed to the extremely fluctuating series of the dataset, and the patching mechanism of PatchTST may lose focus on specific locality to handle rapid fluctuation. By contrast, our proposed method aggregating the whole series variations for series representations can better cope with this situation” I would need proof for such a claim (even in appendix). First, showing this situation and second showing learning weight for iTransformer that shows it cope with the situation.

Proof-read is required for instance:
 * “this goal can be hardy achieved” I guess there is a typo here and Authors was aiming to write hardly?
 * “Soloar-Energy”- > Solar Energy


# Toward a bigger impact

## Additional baselines and larger scope
Nonetheless, I feel that Authors are missing the opportunity to have an even greater impact in the MTSF community (And having my contribution score going from Good to Excellent). Indeed, the proposal is very promising and is on a very important topic, i.e., how to consider variate in MTSF. Are they channel dependent (CD) or channel independent (CI), and if CI are projection perform commonly or individually? However, in my humble opinion, despite doing a good job to present their proposal and results with ablation study and visualization, Authors fail to really position their proposal in the landscape of the above question. It is true that they compare they work to PatchTST, and the CD/CI discussion, but RLinear or RMLP (depending on the dataset) [2] appears to also beat PatchTST. And especially, RLinear with individual projection (one linear layer per variate) similarly to NLinear or DLinear performs better. In addition, RLinear or RMLP use RevIN that was proposed in [1]. The latter show that RevIN helps to handle distribution shift and could be applied to Transformer-based models such as Informer to improve their performance.

Therefore, in my opinion, the paper will have a greater impact if Authors compare their results to these following baselines: revInformer, RLinear and RMLP (and so corresponding papers). And discuss the results and impact of inverse versus CI versus distribution shift handling. This extra step would really be significant for the community in order to have a better understanding of the big picture and what is happening here.

In addition, the abstract and intro emphasis that Transformer superiority is “shaken” by Linear-based models. However, Authors have only few of such Linear models as baselines. Therefore, adding RLinear and RMLP, especially if iTransformer can beat them, will emphasis such a claim. 

Authors cited [2] in their paper, so they are aware of this work and in my opinion should have included it.

Finally, for the experiments where only P% of the variates are used for training, as the variates are selected randomly, it would be good to perform the experiment with different set of random variates and plot an error plot or box plot. This will further highlight that the set selected randomly is not a specific case. For instance, in Figure 8 (a? left one), we could have for each % of variate the min, max, average among the different sets. Figure 5 could be a boxplot. In addition, Authors should make clear that the set of variates use with iTransformer is the same set used in CI transformer (Figure 5) to avoid any misunderstanding from Reader.

## More results in appendix to ensure proper reproducibility
Furthermore, in order to target greater impact on the community, I would suggest Authors to add results and visualizations for the other datasets (similar to Table2, Figure 5, and following) in appendix. This would help to make sure results showed applied to all datasets. Indeed, Authors mentioned that PEMS is more difficult so the nature/type/characteristics of the dataset may impact the results and it would be important to mention it and discuss it (even though this point might what Authors expect to do as future work by saying “explore iTransformers for extensive time series analysis tasks”).

Especially, I also expect Figure 6 for dataset like Solar energy to not be as good as the others. Because seasonality of Solar energy is high and it strongly depend on the weather, so increasing the lookback window might not be that beneficial.



[1] https://openreview.net/pdf?id=cGDAkQo1C0p

[2] https://arxiv.org/pdf/2305.10721.pdf

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of time series forecasting.
The authors propose a model that embeds univariate
channels as a whole and then uses attention between
embedded channels. In experiments on several datasets
they show that their model outperforms current models
and established new state of the art results.

### Strengths
s1. very simple idea and model.
s2. very good results, establishing new state of the art results.
s3. interesting additional finding that longer lookback windows
  now are mostly beneficial (fig. 6).

### Weaknesses
w1. experiments only on selected datasets compared to some
  major baselines.
- You do not report on datasets Exchange, ILI and ETTm1, ETTm2,
  ETTh1 and ETTh2, different from the experiments reported in TimesNet.
  This way it is hard to see if the proposed method really outperforms
  the baselines consistently or just on the selected datasets.

w2. experimental results for close baseline PatchTST varies from
  published results.
- PatchTST consistently reports better results, e.g., for Electricity
  with horizon 96 they report an MSE of 0.129, you report 0.195.
  Where does the difference come from?

w3. no standard deviations reported.
- Standard deviations will help to assess which differences might be
  significant and which spurious.

### Questions
The paper proposes a very simple idea, but the experiments
to the best of my knowledge are establishing a new state of the
art, making it an important contribution like an indepth study.
I also liked the ablation study with growing observation horizons,
as they now are more plausible than in the related work: longer
observation horizons usually pay off for your model.

Some points should be discussed:
w1. experiments only on selected datasets compared to some
  major baselines.
- You do not report on datasets Exchange, ILI and ETTm1, ETTm2,
  ETTh1 and ETTh2, different from the experiments reported in TimesNet.
  This way it is hard to see if the proposed method really outperforms
  the baselines consistently or just on the selected datasets.

w2. experimental results for close baseline PatchTST varies from
  published results.
- PatchTST consistently reports better results, e.g., for Electricity
  with horizon 96 they report an MSE of 0.129, you report 0.195.
  Where does the difference come from? 

w3. no standard deviations reported.
- Standard deviations will help to assess which differences might be
  significant and which spurious. 

Some minor language issues:
- abstract, "However, Transformer is challenged": missing "a".
- p. 2 "irrationality": sounds a little bit too strong to me.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
