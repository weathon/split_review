# Timer-XL: Long-Context Transformers for Unified Time Series Forecasting

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
We present Timer-XL, a generative Transformer for unified time series forecasting. To uniformly predict 1D and 2D time series, we generalize next token prediction, predominantly adopted for causal generation of 1D sequences, to \emph{multivariate next token prediction}. The proposed paradigm uniformly formulates various forecasting scenarios as a \emph{long-context} generation problem. We opt for the generative Transformer, which can capture global-range and causal dependencies while providing contextual flexibility, to implement unified forecasting on univariate series characterized by non-stationarity, multivariate time series with complicated dynamics and correlations, and covariate-informed contexts that include both endogenous and exogenous variables. Technically, we propose a universal \emph{TimeAttention} to facilitate generative Transformers on time series, which can effectively capture fine-grained intra- and inter-series dependencies of flattened time series tokens (patches) and is further strengthened by position embeddings in both temporal and variable dimensions. Timer-XL achieves state-of-the-art performance across challenging forecasting benchmarks through a unified approach. As a large time series model, it demonstrates notable model transferability by large-scale pre-training, as well as contextual flexibility in token lengths, positioning it as a one-for-all forecaster.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes Timer-XL, a transformer decoder model for time series forecasting. Building upon the existing Timer model, Timer-XL extends the model with a longer context and a masking-based approach called TimeAttention to handle multivariate/covariate scenarios. Empirical results have been reported on univariate, multivariate and covariate experiments on some benchmark datasets.

### Strengths
a) The paper studies an interesting problem of long context modeling in the context of time series forecasting. Authors attempt to connect long context to scenarios beyond univariate modeling through next-token style modeling of multivariate and covariate-informed time series. 

b) Experiments have been conducted on many diverse settings although the experiments themselves have some limitations.

### Weaknesses
 a) While the problem of long context modeling is interesting, the primary weakness of this work is the lack of clarity about the goal and a proper scope. The discussion is confusing and often only loosely relates to the long context setting which appears to be the primary goal. Authors claim that "existing transformers in the time series field crucially encounter the context bottleneck" which is not as critical of a problem as being portrayed here. Such claims require serious empirical justification which is missing from the paper (experiment 1 does not go too far, see below). In reality, long context scenarios may be helpful but _mostly_ in specific high-frequency scenarios. Consider a 5min granularity time series with weekly seasonal behavior. One would need a context larger than 2K to understand the seasonal behavior from the time series history. Such cases should have been better highlighted to justify the central claim of the paper. That said, long context univariate modeling may not always yield improvements. It may also worsen the accuracy, e.g., in the case of distribution shifts.

Coming to the utility of long context for multivariate/covariate-informed forecasting, this has been studied (although not explicitly) in Moirai. While the explicit perspective in this paper is interesting, the primary problem is not that one can do multivariate/covariate modeling through long context but that one needs to be able to do it in a zero-shot sense, as attempted in Moirai. As per my understanding, the settings being studied here are task-specific and not a single pretrained Timer-XL model being used for all experiments. Please correct me if I am wrong. 

b) The technical novelty of this work is limited in light of works such as Moirai. "TimeAttention" is a masking scheme that extends causal univariate patch-based modeling to the multivariate setting.

c) The empirical results lack comprehensiveness and are not particularly strong.

**Experiment 4.1**: The benchmark is fairly small to draw conclusions. Even in these scenarios, the benchmark shows that long context yields to diminishing returns (or worse performance) beyond a point, 1 month in most cases. 1 month @ 1h granularity amounts to a context length of 720 which is not far off from the context length of many time series models (Chronos, Moirai, TimesFM, etc.). Furthermore, I don't understand why PatchTST is the only baseline being studied here. I also don't quite understand what's unique about Timer-XL here that yields better performance over PatchTST. Could it be the larger number of parameters? 

Minor: The analysis on normalization does not belong to this section and brings limited value to the discussion. Normalization mostly helps when time series in a dataset have drastically different scales. Models working fine without normalization for a single task of land-surface temperature forecasting is not a surprising result.  

**Experiment 4.2**: The results in Table 2 and 4 are not strong when compared to pretrained baselines such as Moirai. Why is Moirai missing from Fig 4? 

Minor: DeepAR and N-BEATS are not numerical simulation based methods. 

**Experiment 4.3**: More baselines that can incorporate covariates are needed before conclusions can be drawn. For example, you can consider adding N-BEATSx, NHITS, DeepAR, etc. GluonTS also provides an implementation of PatchTST which can incorporate covariates. 

**Experiment 4.4**: The benchmark selected in this experiment for out of domain generalization is severely limited. 5/7 datasets belong to the same domain and with 4 being essentially the same dataset (ETTh1, ETTh2, ETTm1, ETTm2). This is not enough to draw conclusions about a "pretrained model". Please check the benchmarks in the Chronos or TimesFM papers. 

d) The model only enables point predictions. In forecasting, one is often interested in the entire distribution of future possibilities.

### Questions
See above.

- Which version of Moirai was used for the experiments? 1.0 or 1.1?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Timer-XL, a generative Transformer model for uni & mul-variate time series forecasting, which addresses the limitation of short context lengths in existing time series Transformers and allows the model to capture both intra- and inter-series dependencies. Specifically, the authors design TimeAttention, which incorporates relative position embeddings and causal masking to effectively learn temporal dependencies. Evaluations across various benchmarks demonstrate that Timer-XL achieves state-of-the-art performance in univariate, multivariate, and covariate-informed forecasting tasks.

### Strengths
1. The paper proposes multivariate next token prediction for time series forecasting. This paradigm unifies univariate, multivariate, and covariate-informed forecasting, by treating them as a long-context generation problem.
2. This paper introduces TimeAttention, a novel self-attention mechanism for time series data. TimeAttention captures fine-grained intra and inter-series dependencies, preserves causality in forecasting, and incorporates position embeddings.
3. Experiments show that extending the context length generally improves accuracy, highlighting the context bottleneck issue.

### Weaknesses
1. This paper focuses heavily on comparing Timer-XL with other Transformer models, particularly PatchTST, Timer, and lacks a broader comparison with other non-Transformer time series forecasting models. Also, how is Timer-XL compared with some recent LLM-based models? e.g., [1], [2].
2. This paper doesn't extensively discuss the computational cost of Timer-XL. Though it provides a theoretical derivation, a more detailed analysis of the computational resources required, especially when handling high-dimensional time series with long contexts. E.g., how about the number of parameters or training/inference time of Timer-XL as compared with existing solutions. 
3. The extension from univriate to multivariate seems to be an over-simplied way, in that using RoPE to as a positional embedding. Take traffic data as an example, how can RoPE reflect the spatial correlations among traffic network?
4. The authors emphasize long context for time series forecasting, however, for some domains, it may not be necessary for such a long context, e.g., traffic data with periodicities. This is also shown in Figure 3.  Also, one can define a large patch token (more time points). In this way, can the context length also be shortened?

### Questions
Please see the weaknesses. 
Also, it will be good if the authors can use a figure to illustrate patch token for univariate and multivariate data.

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
4

### Summary
This paper introduces Timer-XL, a method for unified time series forecasting, which addresses challenges in hard to uniformly predict 1D and 2D time series. It utilizes generative Transformer with relative position embedding to capture the correlations between the temporal and variable dimensions. Also, it proposes a novel TimeAttention to capture causal patch-wise dependencies within and among all variables. Experiments demonstrate that Timer-XL achieves state-of-the-art performance across challenging forecasting benchmarks through a unified approach,

### Strengths
1. The manuscript demonstrates a high level of completeness.
2. It provides an effective large-scale framework for advancing large models in time series analysis.
3. The empirical evaluation is comprehensive and promising results are shown.

### Weaknesses
1. My biggest question lies with Equations 4, 5, 7, and 8. Since Timer-XL is a unified time series framework, these equations include processing steps that sort each time series. For example, with 𝑁 time series, does the order after flattening the sequences significantly affect the causal relationship in Equations 4 and 5? Specifically, the flattening operation in Equations 4 and 5 concatenates time series data, and it's unclear if the model is truly invariant to the order of these concatenated series. This could lead to inconsistent results if the input order changes, which is a critical concern for a unified framework. The same question applies to Equations 7 and 8, where the masking operation might be sensitive to the ordering of the flattened sequence, potentially disrupting the intended causal relationships between variables.
2. As a unified time series framework, the author needs to compare it with Moirai in a zero-shot scenario. In Figure 5 of the manuscript, a corresponding comparison experiment should be added. It is important to evaluate the model's ability to generalize to unseen datasets without any fine-tuning, which is a key aspect of a unified framework. The lack of zero-shot comparison with a relevant model like Moirai makes it difficult to assess the true potential of Timer-XL as a general-purpose time series forecasting model.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
