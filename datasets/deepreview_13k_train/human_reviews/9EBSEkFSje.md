# GIFT-Eval: A Benchmark for General Time Series Forecasting Model Evaluation

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Time series foundation models excel in zero-shot forecasting, handling diverse tasks without explicit training. However, the advancement of these models has been hindered by the lack of comprehensive benchmarks. To address this gap, we introduce the \textbf{G}eneral T\textbf{I}me Series \textbf{F}orecas\textbf{T}ing Model \textbf{Eval}uation,~\bench{}, a pioneering benchmark aimed at promoting evaluation across diverse datasets. ~\bench{} encompasses 23 datasets over 144,000 time series and 177 million data points, spanning seven domains, 10 frequencies, multivariate inputs, and prediction lengths ranging from short to long-term forecasts. To facilitate the effective pretraining and evaluation of foundation models, we also provide a non-leaking pretraining dataset containing approximately 230 billion data points. Additionally, we provide a comprehensive analysis of 17 baselines, which includes statistical models, deep learning models, and foundation models. We discuss each model in the context of various benchmark characteristics and offer a qualitative analysis that spans both deep learning and foundation models. We believe the insights from this analysis, along with access to this new standard zero-shot time series forecasting benchmark, will guide future developments in time series foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper targets at a critical and longstanding challenge in time-series forecasting research, lacking a unified, comprehensive, and diverse benchmark for evaluation. To address this challenge, GIFT-Eval is developed, encompassing 28 datasets across seven domains and sampled in ten different frequencies.

### Strengths
- Covering a diverse range of datasets and sampling frequencies, which can greatly facilitate our comprehensive understanding of existing time-series models
- Distinguishing pre-training and evaluation datasets, which can assist the comparison between supervised trained models (in-domain generalization) and pre-trained models (zero-shot forecasting)
- Conducting substantial experiments on these datasets (# experiments = # datasets x # sampling frequencies x  # models, such enormous computation!)

### Weaknesses
Overall, I appreciate and respect this paper, given its important research focus and huge amounts of experiments performed.

However, I find the current version of this paper is still on an early stage. Below I elaborate on my significant concerns, which need to be properly addressed before it reaches an acceptance bar.

### 1. The Necessity of Additional Evaluation Datasets

MOIRAI [1] has already done an excellent job in collecting pre-training datasets and conducting comprehensive evaluations on widely recognized datasets typically used to evaluate time-series forecasting models in the literature. The datasets introduced in this paper heavily overlap with them while creating a new division for pre-training and downstream evaluation. Currently, this paper argues improvements in quantity, namely more evaluation datasets and sampling frequencies, are included in the evaluation. However, the necessity of introducing more evaluation datasets and how this approach reveals unique insights not mentioned in previous research is relatively weak.

Covering an excess of comparison datasets can create a significant burden for resource-limited research groups to perform further research and for reviewers to check and compare results. This may lead to redundant model training and evaluation, which is energy-inefficient. I strongly recommend the authors analyze the uniqueness and necessity of any dataset introduced as a new testbed.

For example, when incorporating a new dataset, does it cover distinctive patterns that rarely exist in existing benchmarks, thereby delivering unique insights on different pros and cons of model designs?

The same question extends to the different sampling frequencies applied to each dataset. Is it necessary to include all sampling frequencies for every dataset? Does including the most prominent sampling frequency, which may be defined by different business scenarios, already provide sufficient and fair comparisons of different models?

According to Tables 20, 21, and 22, the total comparison covers 28 datasets, each with multiple sampling frequencies. Are these experimental comparisons overly redundant? For instance, can you identify a compact set of evaluation datasets, covering unique datasets accompanied by selected sampling frequencies, that still reveal comprehensive information while being much more energy-efficient, user-friendly, and economical? Perhaps you could calculate the real rank for the result comparison matrix presented in these tables (# datasets x # models).

Moreover, analyzing the data patterns in Figure 1 is beneficial, but how does the pattern coverage of these new benchmark datasets differ from that of existing benchmarks? Do newly introduced datasets include more pronounced trends and seasonality, or large entropy, etc.?

### 2. Lack of Some Related Work and Baselines

The comparison with previous benchmarks omits some classic and recent studies specializing in probabilistic forecasting. For instance, gluon-ts [2] is a Python package for probabilistic time-series forecasting that also provides a robust interface for accessing multiple time-series datasets. Built on gluon-ts, pytorch-ts [3] includes more advanced probabilistic forecasting models based on deep generative models. ProbTS [4] is another benchmark study offering a unique perspective by comparing capabilities in delivering point versus probabilistic forecasts, short versus long forecasts, and associated preferences in methodological designs. Specifically, ProbTS should be compared in Table 1, as it is highly relevant to your work in comparing both classical and foundation models. It unifies comparison conditions, covers diverse forecasting horizons and data patterns, calculates dominant data characteristics (such as trend, seasonality, and non-Gaussianity), and associates them with the strengths and weaknesses of different model designs.

Moreover, other time-series foundation models have been developed beyond MOIRAI, chronos, and TimesFM. Notably, Timer [5] and UniTS [6] have been accepted at conference proceedings and have publicly released their implementations. These models should at least be discussed in the related work section and, ideally, be included in your experimental comparisons.

Additionally, the paper could benefit from including more advanced probabilistic forecasting baselines, such as TimeGrad [7], CSDI [8], and their predecessor GRU NVP [9]. ProbTS has highlighted the unique advantages of these methods in delivering short-term distributional forecasting. Moreover, a simple combination of GRU NVP with RevIN [10] has demonstrated very competitive performance for both short-term and long-term forecasting. Including these more powerful probabilistic models is crucial, as merely adding probabilistic heads over forecasting models like MOIRAI and DeepAR does not sufficiently capture complex data distributions that extend beyond closed-form probabilistic distribution functions.


### 3 Some Missing Details and Analyses in Experiments

The use of MAPE as an only metric for evaluating point forecasts is somewhat "biased." I recommend referring to N-BEATS [11] and including metrics such as sMAPE and ND (normalized deviation, equivalent to normalized MAE) for a more comprehensive evaluation.

Regarding hyperparameter search for deep learning baselines, there is a notable omission in tuning their lookback lengths. This can be an extremely critical factor to adjust, given the diversity of datasets and sampling frequencies. Appendix A indicates that this tuning was performed only for MOIRAI. The same process should be applied to other baselines, including supervised learning models and pre-trained foundation models.

Moreover, regarding three foundation models used in the experiments, only MOIRAI is re-trained on this new data split while TimesFM and Chronos are compared with their released model checkpoints. There is a risk of data leakage in these experiment comparisons. For example, TimesFM has leverage the Electricity dataset for pre-training while this dataset is also used for evaluation in this paper. This may explain why TimesFM performs extremely on "Electricity, short, H" (line 1285, Table 20), but this good performance may come from test data leakage. Therefore, to provide a fair and comprehensive comparison across TimeFM, Chronos, MOIRAI, and other representative time-series foundation models, re-training them following the new data split could be a necessary step.

When comparing supervised time-series models with zero-shot foundation models, it is crucial to investigate the effect of allowed lookback length on forecasting performance. As revealed in MOIRAI, the lookback length significantly influences model performance, as MOIRAI employs an additional hyper-parameter adaptation process on the lookback data, unlike others.

The current analysis lacks depth across multiple experimental configurations. Presently, only aggregated comparisons are provided, without detailed analyses to derive new insights. For instance, why do some foundation models yield better zero-shot forecasting results on certain datasets than models specifically tuned for those datasets? Is it because pre-training datasets encompass more related patterns, pre-trained models have a larger model capacity, or classical models are not well-tuned, particularly regarding lookback length, modeling layers, or model designs? Merely presenting results without in-depth analysis can be detrimental to the research community, as others may expend significant efforts to re-analyze numerous results, which should be addressed within this benchmark.

Additionally, there is a lack of explicit connection with existing benchmarks to validate the reliability of the experiments conducted. For example, evaluation datasets in Tables 20, 21, and 22 cover some classical datasets like ETTh, Electricity, Solar, and M4. Comparing your results on shared datasets with existing studies could demonstrate the reliability of your experimental protocols. Moreover, some widely used datasets in the literature, such as Traffic, Wikipedia, and Exchange, appear to be excluded. Please clarify the reasons for their exclusion.

I suggest maintaining existing classical benchmarks as they are while introducing new datasets and sampling frequencies that cover unique patterns. This approach allows for consistency with existing benchmarks, showcases the correct reproduction of existing models, demonstrates the necessity of new datasets and sampling frequencies, and reveals what can be discovered given this new benchmark.

### Questions
See weaknesses.

My critical concerns centered around the rationale of selecting/adding/filtering evaluation datasets and sampling frequencies, the missing discussion of some highly related studies, and incomplete experimental results and analyses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces GIFT-Eval, a benchmark aimed at evaluation for time series foundation models across diverse datasets. GIFT-Eval encompasses 28 datasets and divides them according to 4 characteristics and 6 features. It also includes a non-leaking pretraining dataset. It then evaluates 17 different baseline models, including 4 types of foundation models and some statistical and deep learning models on this benchmark. Based on the evaluation results, it discusses different models in the context of various benchmark characteristics and offers some qualitative analysis.

### Strengths
* Foundation models are a new and promising research topic in time series forecasting. It is of value to establish a benchmark for evaluating these models.

* This paper does a lot of work in collecting large-scale data for evaluation and running various baseline models on these various datasets.

### Weaknesses
 * This paper emphasizes the inclusion of a non-leaking pretraining dataset, but its value and usage are not clear. Is this dataset used to re-train all foundation models instead of using their public checkpoints? Is it necessarily better than the original pretraining datasets of each foundation model? Since the application on downstream data is the main goal of foundation models, do we really need to keep consistency in pretraining to evaluate these models as discussed in the Introduction?

* Section 3.1.1 mentions covariates in time series forecasting, but it is unclear how are the covariates considered in this benchmark. Can all baselines in the benchmark perform forecasting with covariates?

* The divisions of some characteristics such as variates and frequencies are not reasonable enough, and it is unclear why we should evaluate methods according to these characteristics. For example, Multivariate v.s. Univariate may not be the intrinsic differences that influence forecasting, as even some multivariate datasets do not have strong correlations between variates. So simply claiming that some models perform best on multivariate or univariate datasets may be misleading.

* The experiments mainly point out that some specific models perform best in some specific datasets. There are not many consistent conclusions from the evaluations that help us understand the characteristics of different models. Some results or claims are also confusing. In Page 7, how can we get the conclusion that ‘foundation models consistently outperform both statistical and deep learning models’ from Table 6, since PatchTST also performs very well? In Page 8, what is the meaning of ‘This trend indicates that the fine-tuning of foundation models effectively captures longer-term dependencies’? In Page 9, why does Moirai, which is a foundation model considering multivariate correlation, perform best on univariate datasets instead?

* The qualitative results only show results in some special cases. It is doubtful whether these phenomena and analyses are general to all different data. It is also confusing that different data are used to evaluate foundation models and other models, which makes these models incomparable.

### Questions
Please see Weaknesses.

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
5

### Summary
In this work the authors introduce a large collective time series benchmark named GIFT-EVAL. They demonstrate the diversity and legitimacy of this benchmark with the analyses on both the characteristics of involved datasets and the benchmark results of state-of-the-art supervised and foundation time series models on it.

### Strengths
This work address an important and pressing problem of the time series forecasting community that there lacks a large and comprehensive common benchmark. The collection and complication of the datasets itself is a significant result.

### Weaknesses
Despite the comprehensive data analyses, the paper currently lacks the reasoning behind the selection of GIFT-EVAL components. And the empirical study follows suboptimal standards which makes the results less convincing. See questions.

### Questions
Regarding the creation of GIFT-EVAL:
1. As mentioned in the weakness, GIFT-EVAL seems to be a straightforward ensemble of some available datasets. What are the reasons behind the selection of this particular ensemble vs the datasets, especially given the data analytics done on them?

Regarding benchmarking:
1. My major concern of the work: MAPE is well recognized as a bad point forecasting metric on its own, due to e.g. its favoring underprediction, sensitivity near ground truth 0 (this is recognized by the authors too), (see e.g., [1] and many community posts online). It would be helpful to switch to or also report other more robust metrics, e.g. MASE. 
2. In case normalized metrics are used, consider reporting geometric means [2].
3. Given the 6 properties of component datasets, it would be helpful to see the benchmark results sliced on these properties as well.

[1] Goodwin, Paul, and Richard Lawton. "On the asymmetry of the symmetric MAPE." International journal of forecasting 15.4 (1999): 405-408. 
[2] Fleming, Philip J., and John J. Wallace. "How not to lie with statistics: the correct way to summarize benchmark results." Communications of the ACM 29.3 (1986): 218-221.

### Soundness
2

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
The existing benchmark evaluations are incomplete (lacking evaluation of foundation models), so the paper introduces the General Time Series Forecasting Model Evaluation (GIFT-Eval), including statistical models, deep learning models, and foundation models. It tests on 28 different test datasets and provides a large-scale pretraining dataset to better evaluate foundation models. Finally, the paper offers a qualitative analysis that spans both deep learning models and foundation models.

### Strengths
S1: Model Level: GIFT-Eval provides a comprehensive evaluation for time series forecasting models, including statistical models, deep learning models, and foundation models.

S2: Experiment and Dataset Level: GIFT-Eval conducts extensive experiments, testing on 28 different test datasets, and also provides a non-leaking pretraining dataset to better evaluate foundation models

### Weaknesses
W1: I believe that analyzing foundation models based on four time series characteristics—domain, frequency, prediction length, and the number of variates—combined with six time series features—trend, seasonality, entropy, Hurst, stability, and lumpiness—is not very meaningful, especially regarding the number of variates. I don't think it has any relation to these six features. Why not directly analyze the time series features for each test dataset, and then evaluate the performance of foundation models on various datasets to assess their strengths and weaknesses concerning these six features?

W2: The paper only analyzes the features of the test data. It is necessary to include an analysis of the pretraining data as well. This would help better assess whether the foundation models perform well on these features due to the presence of these characteristics in the pretraining data itself, the generalization ability of the foundation models, or other reasons.

W3: Please elaborate on the details of the data splitting for train/val/test datasets, specifically how the validation data is constructed. What does the statement "The final window of the training data serves as validation" mean, and why is a common splitting ratio like 7:1:2 or 6:2:2 not used?

W4: The experimental settings are unclear, for example: what are the input and output lengths for short-term, medium-term, and long-term forecasting? Are the foundation models performing zero-shot or full-shot forecasting in Tables 6-10? Why are common metrics like MSE and MAE not chosen for point forecasting?

W5: About experimental results: 1) PatchTST performs best on multivariate datasets, so why is Moirai, a model specifically designed for variable correlation, not used? Also, why do foundation models perform well on univariate data but not on multivariate data? 2) The paper states that Moirai has good prediction performance in short-term forecasting; does this conclusion contradict the original Moirai paper, which uses very long input sequences?

W6: The qualitative analysis is relatively limited; more in-depth analysis (not just visualization) may be needed to highlight the characteristics of the foundation models and draw more meaningful conclusions.

### Questions
See W1-W6.

### Soundness
3

### Presentation
2

### Contribution
3
