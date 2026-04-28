# Forecasting Needles in a Time Series Haystack

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Shocks and sudden spikes are common characteristics of real-world time series data. For example, demand surges or electricity outages often occur in time series data, manifesting as spikes (“Needles”) added to the regular time series (“Haystack”). Despite their importance, it is surprising to find their absence in the benchmarking protocol at the frontier of time series research—Time Series Foundation Models (TSFMs). To address this gap, we present the Needle-in-a-Time-Series-Haystack (NiTH) Benchmark, which includes both synthetic and real-world spiky time series data from diverse domains like traffic, energy, and biomedical systems. For synthetic data, we develop a flexible framework using Poisson-based modeling to generate spiky time series, allowing us to evaluate forecast models under various conditions. To accurately assess model performance, we introduce a new metric based on Dynamic Time Warping, specifically designed for spiky data. We evaluate the zero-shot forecasting capabilities of 6 popular TSFMs over 64 million observations, identifying their limitations related to architecture, tokenization, and loss functions. Furthermore, we demonstrate that the incorporation of the proposed NiTH dataset, due to its diversity compared to the common pre-training corpus of TSFMs, results in improved performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors study the problem of forecasting spiky time series. They proposed a dataset called Needles in the Time Series Haystack (NITH), which they used to evaluate multiple times series foundation models in zero-shot settings. They also propose a scalable way to generate spiky time series, and a novel metric to evaluate models on spiky time series. They found that most time series foundation models cannot model spiky time series. The authors also evaluate how design choices of foundation models affect their performance on spiky data.

### Strengths
1. The paper studies an important problem. Forecasting or predicting spiky data is indeed understudied. 
2. The authors conduct a **lot** of experiments-- with multiple times series foundation models, and their design choices
3. The author propose a scalable way to generate spiky time series, and evaluate models on forecasting spiky data

### Weaknesses
1. **Clarity**: The paper introduces a lot of "novel" things, and mathematical instruments to model and evaluate time series models on spiky data. There's a lot of notation which is hard to follow ($\alpha, \beta, \theta, \omega$, to name a few) as sometimes symbols apply prior to their usage. For example, it is particularly hard to follow 219 -- 225, where it's unclear what $\alpha$ and $\beta$ are until it is introduced in Algorithm 1.  
2. **Too many "novel" things, but their :** The authors propose too many new things, that it is hard to keep track. Moreover, it seems that the authors miss a lot of basic things and instead over-complicate their proposed solutions. For example, [1] proposes a simple way to inject spikes in time series which was not considered. For the "haystack", the authors use Gaussian Processes, when simpler time series can be generated using polynomial or linear trends, periodicity (sine waves), and some noise (Gaussian or Random walks). Similarly, there has been a lot of work in time series anomaly detection on better metrics to evaluate time series of similar natures, for example [2]. Moreover, simpler metrics such as $\alpha^{T}(Y - \hat{Y})$, where $\alpha$ is a vector which gives more weight to needles rather than the haystack. 
3. **Baselines and related work:** The authors only consider time series foundation models. They do not consider any statistical models such as ARIMA, or models which are designed to predict spiky time series. Moreover, the authors do not consider any prior work on modeling or evaluating spiky time series, e.g. [3, 4, 5, 6]. Also, the authors continually pre-train pretty large models on NITH, perhaps smaller models can be fine-tuned more effectively on spiky time series.
4. **Normalization:** All time series models including foundation models use some form of normalization (e.g. Chronos uses mean scaling while TimesFM uses RevIN), and I believe that this influences the forecasting performance. This is perhaps the most component of the design space of these models.  
5. **Lags and lack of connection to a real-world application:** The authors mention (random) lag multiple times in the paper, but it is unclear to me why is this an important consideration for spiky time series? I feel this is also where connection to a real-world problem (e.g. energy load prediction) would be helpful. For example, in these cases it may be more important for to predict whether there will be spikes, or the number of spikes and the amplitude of the spike, each of which is a different problem (classification or regression), and can be evaluated with different metrics.   
6. **Loss function:** Most TSFMs are trained to predict some notion of conditional mean (MSE) or median (MAE) of a time series. These loss functions are not appropriate for training models that can be expected to do well on spiky data, thus the fact that TSFMs don't perform too well is not surprising. On the other hand, I feel that the authors could have spent more time on this important aspect.  
7. **Memorization:** The authors claim that the benchmark tests a model's ability to memorize spikes. Could the authors provide more information and evidence on why this is the case? 

### Questions
1. Is DTW or it's scaled version as you have proposed differentiable? If not, how are models trained using these as a loss function?  
2. What loss function is used to continually pre-train Chronos and TimesFM?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The manuscript investigates the performance of learners capable of predicting spikes in time series. 
Although shocks and sudden spikes are common characteristics in real-world time series (according to the authors), their main motivation is the absence of a benchmarking protocol.
To address this issue, the authors collected previously published real-world time series, created synthetic time series with those characteristics, tested some time series foundation models, and presented an extension version of DTW as a new measure.

### Strengths
The most important contribution is the organization of a vast amount of time series published in the literature. 
This type of manuscript has great potential to be cited and is important for guiding new researchers to find more appropriate time series. 
Another relevant aspect presented by the authors is the execution of foundational time series models, a hot topic nowadays, as benchmarks for their datasets. 
I believe these experimental results are relevant for positioning the current research status as a foundation for future contributions. In summary, this suggests that new studies should, in some way, improve upon the presented results. 
Finally, another notable strength is the volume of experiments conducted by the authors.

### Weaknesses
The major weakness, in my opinion, is the difficulty in clearly understanding the manuscript's goals by reading the title and abstract. 
When the authors say that shocks and sudden spikes are common characteristics in real-world time series, I suppose there is substantial data available to address this problem. So, from the real-world perspective, is the authors' main contribution just the compilation of those data? 
On the other hand, the authors also proposed a function to create "spiky" time series. It is an interesting proposal, but their focus is essentially on modifying the stochastic component. It is not clear whether it is also possible to modify the deterministic part of the time series, thereby varying the general behavior of the time series. 
Moreover, I understand that foundational time series models are currently prominent, making it natural to use them to attract readers' attention. However, it is unclear why classical approaches were not considered in their investigation. 
Another important point is the authors' choice to select MAE, MSE, and DTW as evaluation "metrics." Why were these selected? I understand they are important when comparing predicted observations, but the application presented by the authors involves not only predicting observations, but also predicting spikes. There are more appropriate "metrics" for this task that are not influenced by non-spike predictions.

I recommend revising all definitions and terms. For example, DTW cannot be considered a metric since it does not satisfy the triangle inequality. How does this affect the analysis? And how does it impact the proposed "metric"?

The authors opted to use MAE, MSE, and DTW to evaluate their experiments. However, these may not be the most appropriate metrics. Given the focus on spikes, it’s also crucial to assess the timing of spike predictions. When comparing predictors, it is important to evaluate their ability to predict spikes accurately and the time deviation from the expected occurrence. Metrics commonly used for concept drift or change point detection might be more suitable. Why not consider more consistent evaluators?

In Section 3.1.1, the authors mention that "haystack" is the base time series without spikes. Does this "base" refer to a stationary process, or could it represent any kind of time series behavior?

When the authors state that "No TSFMs could accurately forecast needles across all settings," is this a result of their research? Is there a citation supporting this claim?

The authors mention, "We apply our filtering algorithm." Was this algorithm proposed in this work? Where is it described, and how was it evaluated?

Was "D_T" defined on Page 4?

Several equations lack clarity, such as "\tau," "\hat{\tau}," and U(3,5).

Figure 2 includes "pred1," which is not discussed in the text.

Does Figure 3 show results for all time series?

Figure 3 is not visually easy to read, especially with text closely surrounding it.

The impact of adding noise to the synthetic time series should be discussed more thoroughly, particularly regarding the signal-to-noise ratio.

The discussion on results often includes phrases like "We believe...," which implies some uncertainty. This phrasing gives the impression that the authors may not be entirely confident in their conclusions. Based on the results, I share the authors’ sense of uncertainty, as the conclusions do not seem fully substantiated. Consequently, the claim in the introduction about context length remains unconvincing.

When creating synthetic time series, is it possible to alter the function used for generating the deterministic part of the series, independent of spike generation?

In the appendices, the authors included a section on time series statistics. While it contains several plots, the statistical information does not appear substantial.

### Questions
1 - I recommend revising all definitions and terms. For example, DTW cannot be considered a metric since it does not satisfy the triangle inequality. How does this affect the analysis? And how does it impact the proposed "metric"?

2 -The authors opted to use MAE, MSE, and DTW to evaluate their experiments. However, these may not be the most appropriate metrics. Given the focus on spikes, it’s also crucial to assess the timing of spike predictions. When comparing predictors, it is important to evaluate their ability to predict spikes accurately and the time deviation from the expected occurrence. Metrics commonly used for concept drift or change point detection might be more suitable. Why not consider more consistent evaluators?

3 -In Section 3.1.1, the authors mention that "haystack" is the base time series without spikes. Does this "base" refer to a stationary process, or could it represent any kind of time series behavior?

4 - When the authors state that "No TSFMs could accurately forecast needles across all settings," is this a result of their research? Is there a citation supporting this claim?

5 - The authors mention, "We apply our filtering algorithm." Was this algorithm proposed in this work? Where is it described, and how was it evaluated?

6 - Was "D_T" defined on Page 4?

7 - Several equations lack clarity, such as "\tau," "\hat{\tau}," and U(3,5).

8 - Figure 2 includes "pred1," which is not discussed in the text.

9 - Does Figure 3 show results for all time series?

10 - Figure 3 is not visually easy to read, especially with text closely surrounding it.

11 - The impact of adding noise to the synthetic time series should be discussed more thoroughly, particularly regarding the signal-to-noise ratio.

12 - The discussion on results often includes phrases like "We believe...," which implies some uncertainty. This phrasing gives the impression that the authors may not be entirely confident in their conclusions. Based on the results, I share the authors’ sense of uncertainty, as the conclusions do not seem fully substantiated. Consequently, the claim in the introduction about context length remains unconvincing.

13 - When creating synthetic time series, is it possible to alter the function used for generating the deterministic part of the series, independent of spike generation?

14 - In the appendices, the authors included a section on time series statistics. While it contains several plots, the statistical information does not appear substantial.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors tackle the challenge of predicting rare spikes in time series data. To help improve forecasting for these “needle” events, the authors introduce a benchmark called NITH with both synthetic and real-world datasets. They test several prominent time series foundation models and find that they generally struggle with these sharp, rare events. To improve evaluation, they propose a new metric called Scaled Dynamic Time Warping (SDTW) tailored to these spikes. Additionally, they show that pre-training models on synthetic data created to mimic real-world spiky patterns can boost model performance in this setting.

### Strengths
S1. The introduction of SDTW is a helpful contribution which addresses issues with existing metrics for measuring performance on the specific tasks of spiky time series forecasting. 

S2. The new benchmarks (NITH-Synth, NITH-Real) capture an important subset of time-series forecasting problems, and provide a new way of evaluating and probing existing foundation models. Construction of useful benchmarks is an important way to continue to make progress on these models.

### Weaknesses
W1. Very strong constraints are applied to the time series setting (>8 spikes, >512 segments, etc) in order to establish the synthetic spike benchmarks. It is not clear from this work how helpful these constraints are when applying the benchmark to other real-world settings and under what settings they could be relaxed. Better establishing the importance of the ‘spike’ setting could improve this weakness. Specifically, the choice of a minimum of 8 spikes seems arbitrary and may not reflect real-world scenarios where fewer, but still significant, spikes occur. The 512 segment length constraint also limits the applicability to longer time series, which are common in many domains. A more thorough justification of these specific thresholds is needed, along with an analysis of how performance varies as these constraints are relaxed.

W2. The NITH-Real dataset seems likely to have some overlap with the foundation model training sets, particularly through its use of the UCR Anomaly and NAB benchmarks. Separating out the results by benchmark and analyzing the overlap where possible could help reduce this risk. It would be beneficial to not only separate the results but also to quantify the degree of overlap, if possible. This could involve comparing the specific time series used in NITH-Real with known datasets used for pre-training the foundation models. Without this analysis, the reported performance gains could be partially attributed to memorization rather than genuine generalization.

W3. The continuous pre-training approach can lead to loss of generalization. Could the authors evaluate how the models trained on the NITH-Synth benchmark fare on other standard forecasting benchmarks? There are many existing methods for improving continual pre-training which can be applied in this setting as well to mitigate this performance difference if it exists. It's important to understand if the pre-training on synthetic data leads to a catastrophic forgetting of previously learned patterns. Evaluating performance on a diverse set of standard time series forecasting benchmarks, such as those used in the M4 or M5 competitions, would provide a more complete picture of the model's capabilities and limitations after this pre-training.

### Questions
Q1. A significant problem with previous metrics seems to be the equal weighting of timesteps when compared to the practitioners interest in only those anomalous or spiky time-steps which follow a different frequency and magnitude. SDTW requires the ground truth needle locations as a result. Is there some way to remove this requirement, perhaps by applying a standard filter to the time-series so that MSE or DTW can be used instead?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The Time Series Foundation Model (TSFM) has been a debated topic in recent years. Proper evaluation and selection of the most suitable model are also desired. The paper presents a benchmark that includes both synthetic and real data from various domains, which fills the gap in the absence of benchmarking. The paper introduces a Possion-based modeling method for generating spiky time series for synthetic data, which enables the evaluation to proceed in various conditions. The paper uses a Dynamic Time Warping based metric to define the model performance, and extensive experiments are conducted to examine the zero-shot forecasting performance of six well-established TSFMs on spiky time series.

### Strengths
The paper introduces a theoretical generation scheme for the spiky time series generation. The spiky time series generation follows the models of Markov chain transitioning between haystack signals that are sampled from the Gaussian process, while the needle signals are generated from a separate Gaussian process, along with outlier and rarity constraints. The paper is well-organized and has good clarity except for some minor issues in the figures.  The dataset in the benchmark is rich and full of diversity, so I believe it is useful for the evaluation of TSFMs.

### Weaknesses
Though the benchmark is only designed for time series forecasting, and the model performance is only evaluated in terms of the zero-shot forecasting capabilities, evaluation of other tasks might be required, e.g., classification.  

Also, it would be interesting to discuss other stochastic processes for the time series generation and include an additional experiment for the ablation study. 

It is hard to read in some figures in the paper, e.g., Figure 4, Figure 6-8 and Figure 14-35; I believe the fontsize should be increased.

### Questions
1. why the haystack distribution is set as the scaled Poisson distribution, and are there any advantages to using the scaled variant?
2. why the Gaussian process was chosen rather than other stochastic process, needs to clarify
3. what's the advantages of the method over other related generation methods [1][2], it seems like the needles signals can be instead 
generated with other schemes together with the method [1].   


References:
[1] https://arxiv.org/abs/2311.01388
[2 ] https://arxiv.org/pdf/2403.03698

### Soundness
2

### Presentation
2

### Contribution
2
