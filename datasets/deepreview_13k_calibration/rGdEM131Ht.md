# GENERATIVE TIME SERIES LEARNING WITH TIME-FREQUENCY FUSED ENERGY-BASED MODEL

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 5, 6, 5

## Abstract
Long-term time series forecasting has gained significant attention in recent academic research. However, existing models primarily focus on deterministic point forecasts, neglecting generative long-term probabilistic forecasting and pre-training models across diverse time series analytic tasks, which are essential for uncertainty quantification and computational efficiency. In this paper, we propose a novel encoder-only generative model for long-term probabilistic forecasting and imputation. Our model is an energy-based model, employing a time-frequency block to construct an unnormalized probability density function over temporal paths. The time-frequency block consists of two key components, i.e., a residual dilated convolutional network to increase the receptive fields of raw time series, and a time and frequency features extracting network to integrate both local and global patterns. Our design enables the prediction of long-term time series in a single forward run using Langevin MCMC, which drastically improves the efficiency and accuracy of long-term forecasting. Moreover, our model naturally serves as a general framework for forecasting at varying prediction lengths and imputing missing data points with one pre-trained model, saving both time and resources. Experiments demonstrate that our model achieves competitive results in both forecasting and imputation tasks across a diverse range of public datasets, highlighting its potential as a promising approach for a unified time series forecasting model capable of handling multiple tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a time-frequency fused parameterization of EBM for long-term time series modeling. The EBM defines a bottom-up mapping which is a encoder architecture as mentioned in this paper. The design of this encoder can be tricky. The author(s) leveraged a novel residual time-frequency block fuse information from time and frequency domain and hence got pretty good results in several benchmarks.

### Strengths
1. The proposed method is simple and clear.

2. The overall performance is good.

3. The masked pretraining method seems interesting and may be used to scale-up time series training.

### Weaknesses
The paper got good results in several benchmarks but lack of novelty in two ways. If the author claims to improve EBM based learning method in time series, the author should discuss more results about MCMC sampling results, e.g. the chain mixing problem. MCMC chain mixing is a well-known issue in non-sequential signals, it could be worse in time series. If the author claim the novel parameterization of EBM and specially designed fusion block (i.e. the important inductive bias for time series), I would suggest add more insightful ablation studies. There are many design choices for fusion. The author should clarify the benefits of current design choice.

Meanwhile, the author missed some pioneering literature about basic EBM, such as,

[1] "A theory of generative convnet." International Conference on Machine Learning. PMLR, 2016.

[2] "Implicit generation and modeling with energy based models." Advances in Neural Information Processing Systems 32 (2019).

[3] "Cooperative training of descriptor and generator networks." IEEE transactions on pattern analysis and machine intelligence 42.1 (2018): 27-45.

For short-run Langevin dynamics learning of EBM, [4] is also an important work.

[4] "A tale of two flows: Cooperative learning of langevin flow and normalizing flow toward energy-based model." ICLR (2022).

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript describes a generative model that can be used for imputing or forecasting a univariate time series. The model's encoder block consists of a sequence of "time-freq blocks" (TFB). Within a single TFB, convolutional and MLP layers act on both the original input in the time domain, as well as the concatenated real and imaginary parts of a Fourier transform of those inputs. TFB are connected with residual connections. The decoder block consists of a series of convolutional layers followed by MLP layers. Model estimation was done via maximum likelihood by minimizing a measure of divergence between observed data samples and samples generated from the model -- though I will say that I am not familiar with the specific estimation methods used, and did not read them carefully. Experiments with forecasting and imputation tasks indicate that the model has performance that is generally comparable to or better than several recently published methods. An ablation study demonstrates that both the time and frequency features are useful.

### Strengths
My understanding is that the primary contribution of this article is the proposal of time-frequency blocks as described in the summary, which allow the model to use information from both the time and frequency domain. Previous modeling approaches have also incorporated mechanisms for incorporating time and frequency domain features, but the specific architecture proposed here may be novel. I do not possess sufficient knowledge of the related literature to fully assess the significance of this contribution, but it has the feeling of an interesting idea that is worth being published. The article was fairly clear overall; I could implement a similar model based on the descriptions given, though I could not exactly reproduce it. I am confident that man of my questions along these lines could be addressed in a revision.

### Weaknesses
The main weakness I see in the paper is that clear procedures for separating model development from the experiments evaluating model skill were not described. This leaves the reader with the impression that a clear "model development" and "model evaluation" data split was not made, and that claims about matching or exceeding state-of-the-art performance may not generalize to novel data sets. If careful procedures for evaluating the model on data that were not used for model development were indeed in place, it would be beneficial to describe them. If not, perhaps results could be given for new data sets?

I found equations 6 and 7 to be helpful, but they did not seem to align precisely with Figure 1 and did not completely fill out all details of the model. A few specific questions are below:

    a) The text just above Eq 6 defines the operator $g = MLP(SiLU(Conv1D(\cdot)))$, while Figure 1 and earlier text indicate that Dilated Conv and Conv1d layers were used. Am I understanding correctly that the Dilated Conv and Conv layers in the figure represent the $g$ operator? If so, can this inconsistency be resolved? Otherwise, can the figure or text be amended to address this point of confusion?

    b) I find the layout of the sub-blocks within the TFB on the left side of Figure 1 confusing. The inputs to the DC -> SiLU -> Conv1D block are the time feats or frequency feats, right? This is not apparent to me from the organization of the figure, which has arrows pointing from the DC -> SiLU -> Conv1D block to the time/freq feat modules. And why is there an arrow pointing up from the Conv1D block?

    c) I believe from the figure that $y^l = y^{(l-1)} + TFB(y^{(l-1)} = y^{(l-1)} + f^l_{freq} + f^l_{time}$, but I am not fully confident in this and didn't see a clear statement of this in the text. It would be helpful to add a line to Eq 6 clearly stating how the output of a TFB is calculated.

How were missing data values (e.g., as in imputation settings) handled in computation of the FFT?

I don't understand the motivation for using a probabilistic score CRPS for a distributional forecast in the short-term forecasting problem, and the MAE/MSE for a point prediction in the long-term forecasting and imputation problems. It seems to me that it would be valuable to examine measures of point forecast skill and distributional forecast skill in both forecasting settings. This is particularly salient since the second sentence of the abstract reads, "However, existing models primarily focus on deterministic point forecasts, neglecting generative long-term probabilistic forecasting and pre-training models across diverse time series analytic tasks, which are essential for uncertainty quantification and computational efficiency." The abstract states that long-term probabilistic forecasting is an important problem, but we do not see CRPS results for the long-term forecasting example. Could a more complete suite of results be added?

The ablation study looking at the contribution of time and frequency extraction only looks at a subset of the data sets. I think it would be interesting to provide results for all data sets used in the paper, and to provide some examination to indicate settings in which it is more or less helpful to use both feature sets.  For example, could columns be added to Table 6 giving something like the lag 1 autocorrelation of the series and the power of the first few dominant frequencies? With the hypothesis being that the relative value of using both feature groups may depend on characteristics of the timer series being modeled?

### Questions
1. I found equations 6 and 7 to be helpful, but they did not seem to align precisely with Figure 1 and did not completely fill out all details of the model. A few specific questions are below:

    a) The text just above Eq 6 defines the operator $g = MLP(SiLU(Conv1D(\cdot)))$, while Figure 1 and earlier text indicate that Dilated Conv and Conv1d layers were used. Am I understanding correctly that the Dilated Conv and Conv layers in the figure represent the $g$ operator? If so, can this inconsistency be resolved? Otherwise, can the figure or text be amended to address this point of confusion?

    b) I find the layout of the sub-blocks within the TFB on the left side of Figure 1 confusing. The inputs to the DC -> SiLU -> Conv1D block are the time feats or frequency feats, right? This is not apparent to me from the organization of the figure, which has arrows pointing from the DC -> SiLU -> Conv1D block to the time/freq feat modules. And why is there an arrow pointing up from the Conv1D block?

    c) I believe from the figure that $y^l = y^{(l-1)} + TFB(y^{(l-1)} = y^{(l-1)} + f^l_{freq} + f^l_{time}$, but I am not fully confident in this and didn't see a clear statement of this in the text. It would be helpful to add a line to Eq 6 clearly stating how the output of a TFB is calculated.

2. How were missing data values (e.g., as in imputation settings) handled in computation of the FFT?

3. I don't understand the motivation for using a probabilistic score CRPS for a distributional forecast in the short-term forecasting problem, and the MAE/MSE for a point prediction in the long-term forecasting and imputation problems. It seems to me that it would be valuable to examine measures of point forecast skill and distributional forecast skill in both forecasting settings. This is particularly salient since the second sentence of the abstract reads, "However, existing models primarily focus on deterministic point forecasts, neglecting generative long-term probabilistic forecasting and pre-training models across diverse time series analytic tasks, which are essential for uncertainty quantification and computational efficiency." The abstract states that long-term probabilistic forecasting is an important problem, but we do not see CRPS results for the long-term forecasting example. Could a more complete suite of results be added?

4. The ablation study looking at the contribution of time and frequency extraction only looks at a subset of the data sets. I think it would be interesting to provide results for all data sets used in the paper, and to provide some examination to indicate settings in which it is more or less helpful to use both feature sets.  For example, could columns be added to Table 6 giving something like the lag 1 autocorrelation of the series and the power of the first few dominant frequencies? With the hypothesis being that the relative value of using both feature groups may depend on characteristics of the timer series being modeled?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel generative model called Time-Frequency fused Energy-Based Model (TF-EBM) for long-term probabilistic time series forecasting and imputation.
TF-EBM is an encoder-only model that employs energy-based learning to construct an unnormalized probability density over temporal paths. This allows coherent long-term forecasting.

### Strengths
Originality:

Proposes a novel architecture combining energy-based models and time-frequency modeling for time series, which is an original contribution.

Leverages energy-based learning in a new way for coherent long-term time series forecasting.

Pre-training approach for time series using TF-EBM is an original idea inspired by NLP models.

Quality:

Comprehensive experiments across various forecasting and imputation tasks on multiple datasets.

Comparison to many strong baselines like DeepAR, Autoformer, etc. demonstrates quality.

Strong performance especially on long-term forecasting shows effectiveness of the approach.

Ablation studies analyze the model components like dilated CNN and time-frequency modules.

Clarity:

The method and architecture are clearly explained with useful diagrams.

The related work section covers relevant literature on energy-based models, transformers, etc.

Experiments are well-organized and different tasks nicely showcase model capabilities.

### Weaknesses
The motivation for using energy-based learning specifically is not clearly articulated. References connecting energy-based models to time series properties could help.

More analysis on why the time-frequency modeling outperforms just time or just frequency features could strengthen this contribution. It's unclear if the benefits are due to the combination itself or simply the increased model capacity from using both.

The pre-training evaluation is limited. More exhaustive experiments on the transfer learning capabilities could be done, including different pre-training datasets and fine-tuning scenarios.

Only univariate time series are evaluated. Comparing with PatchTST is needed in this setting, especially given its strong performance on univariate time series forecasting.

The comparison to autoregressive models like LSTMs is missing. This could reveal advantages over common recurrent approaches, particularly in capturing temporal dependencies.

The synthetic ablation study focuses on noise removal. Ablations on modeling long-term dependencies, such as varying the length of the forecast horizon or the complexity of the underlying temporal patterns, could be more insightful.

All datasets are regular time series. Applying to irregularly sampled data from healthcare etc. could reveal robustness and generalizability of the method.

Uncertainty estimation and calibration are not evaluated for the probabilistic forecasting. This could be an issue, as the quality of the uncertainty estimates is crucial for practical applications.

Hyperparameter tuning details are not provided clearly. It's unclear if suboptimal settings affect comparisons, and a sensitivity analysis of key hyperparameters would be beneficial.

The advantages over previous energy-based time series methods like TimeGrad are not fully fleshed out. A more detailed comparison, including computational cost and performance trade-offs, would be valuable.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a generative model for time series forecasting (and imputation). The proposed energy based model makes use of both temporal and frequency based features through a neural network architecture the paper calls Time-Frequency block. The two sub-parts that make up this block are derived from previous works but the combination allows for integrating local and global patterns.

### Strengths
The paper makes clever use of existing work in time series feature extraction to propose the Time-Frequency block as an original neural network building block for time series data. It would in fact be curious to see how an NN based on these blocks works for other more general tasks around time-series data such as prediction, unsupervised learning etc.

The paper is overall well written and is clear in its descriptions and in providing relevant background. The intro and related works section does a good job at summarizing the paper as well as how the proposed method relates to and improves upon existing approaches.

The proposed method is directed towards the significant task of time series forecasting, and the results seem promising.

### Weaknesses
This is overall a good paper. I do however have some concerns around the experiments section which are detailed in Questions below:



### Questions
1: It's unclear how significant the resulting improvements are, the numbers. Can the authors quantify if the improvements are significant? (instead of just reporting means, report the errors too). Also, this might be a typo but Table 3 first row FEDformer MSE is the lowest.

2: It could be worth discussing why certain differences in results arise, e.g. Table 2 DeepAR seems to perform basically identical to the proposed method for exhange rate and electricity datasets, but performs noticeably worse on the other two datasets. What's the reason? This could provide insight into where the proposed method can provide maximum improvement (and why).

3: The paper mentions that deterministic methods generally don't help with uncertainty quantification, that sets the reader up to seeing uncertainty quantification being addressed by the paper, but it doesn't seem like it has been addressed in text or in experiments.

I'll be happy to revisit my score if the above points are meaningfully addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
They proposed an energy-based model capable of both time-series forecasting and imputation. The model consists of a residual dilated convolutional network and considers both time and frequency features. They show good performance in long-term time series forecasting and imputation.

### Strengths
Originality: Models that apply energy-based models to time-series tasks already exist, but the proposed model (TB-EBM) differs in that it maintains long-term coherence better.

Quality: They structured the introduction, related works, and proposed method well to show the differences between TB-EBM and existing models.

Clarity: The paper is expressed well.

Significance: It is very interesting that it can handle long-term time-series forecasting and imputation at the same time.

### Weaknesses
1. They explained their model well, but the placement of Figures and Tables is not appropriate.
2. Figure 1 is not intuitive. I don't know what the "+" mark next to the Time-Freq Block part means. Also, the inference part in Figure 1 is more difficult to understand.
3. The table mentioned in the ablation study is difficult to see because it is not in the main paper.
4. The overall structure of the paper is not friendly to readers.
5.  In Equation 7, the scales of the frequency domain value and the time domain value will be different. Won’t one dominate?
6. Why does TF-EBM perform better in the long-range?

### Questions
1. Isn't there a process in Equation 6 to invert from the fequency domain back to the time domain? If so, I don't understand how the fequency domain feature and time domain feature are added in Equation 7.

2. The residual dilated convolutional network part in the 4.4 ablation study does not seem to have any meaning. There is no doubt that performance increases as the number of layers increases because the capacity of the model increases. Rather, it seems meaningful to use the same number of layers but subtract the residual part.

3. In [1], only one linear layer shows better performance than all existing models in long-term time-series forecasting. A model comparison with [1] seems necessary.

[1] Li, Zhe, et al. "Revisiting Long-term Time Series Forecasting: An Investigation on Linear Mapping." arXiv preprint arXiv:2305.10721 (2023).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
