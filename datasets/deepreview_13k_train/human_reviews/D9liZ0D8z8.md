# Enhancing Foundation Models for Time Series Forecasting via Wavelet-based Tokenization

- Decision: Reject
- Scores: 3, 8, 6, 5

## Abstract
How to best develop foundational models for time series forecasting remains an important open question.
\emph{Tokenization} is a crucial consideration in this effort: what is an effective discrete vocabulary for a real-valued sequential input? To address this question, we develop \wavetoken{}, a wavelet-based tokenizer that allows models to learn complex representations directly in the space of time-localized frequencies. Our method first scales and decomposes the input time series, then thresholds and quantizes the wavelet coefficients, and finally pre-trains an autoregressive model to forecast coefficients for the forecast horizon. By decomposing coarse and fine structures in the inputs, wavelets provide an eloquent and compact language for time series forecasting that simplifies learning.
Empirical results on a comprehensive benchmark, including 42 datasets for both in-domain and zero-shot settings, show that \wavetoken{}: 
\textit{i)} provides better accuracy than recently proposed foundation models for forecasting while using a much smaller vocabulary (1024 tokens), and performs on par or better than modern deep learning models \textit{trained specifically on each dataset}; and 
\textit{ii)} exhibits superior generalization capabilities, achieving the \textit{best average rank across all datasets} for three complementary metrics. In addition, we show that our method can easily capture complex temporal patterns of practical relevance that are challenging for other recent pre-trained models, including trends, sparse spikes, and non-stationary time series with varying frequencies evolving over time.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a novel tokenizer, WaveToken, to time series analysis via wavelet transforms. The method first normalizes input time series using z-score scaling, then applies a maximally decimated Discrete Wavelet Transform using the Biorthogonal-2.2 wavelet family. This decomposition separates signals into approximation coefficients (low-frequency) and detail coefficients (high-frequency) while preserving input length. The coefficients are quantized into discrete tokens using Freedman-Diaconis binning, creating a compact 1024-token vocabulary that captures both global and local patterns. The tokenized coefficients are concatenated and fed into a T5 encoder-decoder architecture trained via next-token prediction. During inference, the model autoregressively generates tokens representing future wavelet coefficients, which are then inverse-transformed to produce forecasts. The model shows strong zero-shot generalization across domains.

### Strengths
1. Introduces wavelet-based tokenizer which bridges classical signal processing with modern deep learning.
2. Gets comparable or better performance with a smaller vocabulary (1024 vs 4096 tokens), demonstrating better information density
3. Comprehensive empirical evaluation on multiple datasets

### Weaknesses
1. Novelty issue:
- Core idea of wavelet-based tokenization for large models has been explored in previous work, e.g., Wave-ViT (Zhu ETL. 2024), though in different domains. Insufficient discussion of how this approach differs fundamentally from or improves upon prior works in wavelet-based tokenizer
2. Design justification:
- The marginal improvement over Chronos raises questions about whether the gains justify the additional benefits of wavelet-based tokenization. An ablation study comparing against simpler tokenization approaches would help validate the necessity of wavelets.
- Mismatch between extensive thresholding theory (Section 3.2) and empirical findings that no thresholding works best in the 8-gpu case.
3. Minor issues:
- The main text lacks a clear mathematical formulation of problem setup and wavelet decomposition, making it harder to understand the key transformation.
- Insufficient explanation of unexpected results in other normalization choices (Line 221)
- No clear shape information for approximation ($a_k$) and detail ($d_k$) coefficients (Line 225).
- Unclear explanation of length preservation in DWT (Line 227). It takes time to think if it is due to the downsampling.

### Questions
1. How does your wavelet-based tokenization fundamentally differ from prior approaches like Wave-ViT, particularly in handling temporal vs spatial data? Are concepts like "pixel-space token embedding" fundamentally different from the wavelet-based tokens in TS? 
2. The finding that single-level decomposition is optimal seems to contradict the motivation for using wavelets. Could you explain this apparent contradiction? Does this undermine the motivation for using wavelets?
3. Could you provide ablation studies comparing against simpler tokenization approaches to justify the added complexity of wavelets?
4. How sensitive is the model's performance to different batch sizes and computing configurations, given the significant difference between single-GPU and 8-GPU results?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a wavelet-based tokenization approach (WaveToken) to enhance time series forecasting using language models. It discusses one critical issue, i.e., tokenizing continuous, real-valued time series data, which hinders handling it using LLMs.

### Strengths
In overall, I agree with the importance of the problem. The paper is well-motivated and well-written. The mathematical formulations and methodological steps are sound.

### Weaknesses
The practical impact of the thresholding decisions on model generalization is uncertain. For example, aggressive thresholding could obscure subtle patterns, which could limit the model's robustness across diverse datasets. So, how do you ensure such an effect would not happen?
- Using cross-entropy loss for next-token prediction in a continuous-data domain is unconventional, as it aligns more with the categorical outputs. So, how it guides learning for continuous variables is still ambiguous for me. Is it possible to compare with other loss functions, e.g. MSE?
- Will the code be released?

### Questions
- The practical impact of the thresholding decisions on model generalization is uncertain. For example, aggressive thresholding could obscure subtle patterns, which could limit the model's robustness across diverse datasets. So, how do you ensure such an effect would not happen?
- Using cross-entropy loss for next-token prediction in a continuous-data domain is unconventional, as it aligns more with the categorical outputs. So, how it guides learning for continuous variables is still ambiguous for me. Is it possible to compare with other loss functions, e.g. MSE?
- Will the code be released?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to develop foundation models for time series forecasting. The authors have delved into the tokenization approach for real-valued time series inputs and propose WaveToken, a wavelet-based tokenizer that involves scaling, decomposing, and quantizing the wavelet coefficients on time series. An autoregressive language model is adapted to generate future tokens of wavelet coefficients. Experimental results demonstrate that the model performs well across diverse datasets in both in-distribution and zero-shot settings, using a smaller vocabulary compared with the previous tokenization method.

### Strengths
1. The paper proposes a novel tokenization from the perspective of the frequency domain.
2. The model is pre-trained on a large corpus of diverse datasets, with evaluations showing its effectiveness in capturing local and global patterns.

### Weaknesses
1. There are some overclaims: WaveToken claimed to be a foundation model, however, being limited to a fixed context length is a pronounced defect. 
2. Limited refinement over previous works: From the experimental results, the performance of the proposed model is not significant. The overall promotions (Table 3 and Table 4) are close to that of Chronos. Besides, the model seems to have a disadvantage in efficiency compared with the straightforward quantizing tokenization of Chronos.
3. Learning autoregressive models on the wavelet coefficients, which do not preserve the temporal transitions, does not make sense to me. The author also noticed the counter-intuition. However, the insignificance of experimental results and lack of theoretical proof amplifies this irrationality. Can the author give more explanations and proofs in this respect? I am not denying the wavelet tokens, which have been extensively explored in previous works before. It might be more reasonable to learn the diffusion process on the decomposition-based coefficients. Whether the author has tried in this regard?
4. About the experiments to support wavelet tokenization: As previously stated, the main evidence in the paper supporting wavelet tokenization comes from the performance of in-domain and zero-shot generalization. However, recent work has shown that there is a risk of overfitting these smaller time series datasets with the LLM [1]. It is recommended that the author provide more comparisons on diverse benchmarks. 
5. Being able to use a smaller vocabulary does not seem like a particularly appealing advantage at present. Could the authors provide more results to verify whether the wavelet-based vocabulary can be extremely small?

### Questions
1. How does WaveToken perform in long-term forecasting? Recent work has shown that Chronos can be less effective at predicting long horizons than models that adopt patch tokens (such as TimesFM). It may be due to the multi-step error accumulation caused by its point-wise tokenization. I wonder if WaveToken can effectively solve this problem.
2. WaveToken and Chronos both adopt the LLM-style discrete vocabulary, which can naturally support probabilistic forecasting. Meanwhile, deep forecasters using continuous embeddings (linear layers or MLPs) can also support it by introducing a probabilistic head (such as TimesFM and Moirai). What other advantages do you think discrete vocabularies have over continuous embeddings in time series forecasters?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces WaveToken, a tokeniser that equips a time series model with wavelet-based features for uni-variate forecasting applications. The authors adapt an existing Transformer-based forecasting model, namely Chronos, by extracting features from a discrete wavelet transform during tokenisation. Evaluations in both in-distribution and zero-shot settings indicate that the use of wavelet-based features during tokenisation might be benfecial across uni-variate forecasting applications.

### Strengths
1. The paper is well structured.
2. The paper is clearly written.
3. The authors conduct extensive forecasting experiments, including 15 in-distribution and 27 zero-shot applications, to evaluate their method.
4. The authors perform a simple qualitative analysis using attention maps and conduct ablation studies to provide insights into their approach.

### Weaknesses
1. Time series models utilising wavelet-based features have been well studied for time series analysis [1,2,3,4,5,6]. As the work under review combines wavelet-based feature extraction with an existing time series model, namely Chronos, for a very specific task, i.e. uni-variate forecasting, it offers a limited technical contribution to the field of time series analysis.

2. In their qualitative analysis and their conclusion, the authors claim "excellent forecasting accuracy" as well as "superior generalization capabilities". However, the results in Figure 3 and 4 reveal that using wavelet-based features does not improve downstream performance with respect to weighted quantile loss (WQL) and mean absolute scaled error (MASE), in both in-distribution and zero-shot settings. In the former setting, wavelet-based tokenisation even hurts performance compaired to the adapted Chronos model. Only in the newly introduced visual relative squared error (VRSE) [7], the results indicate incremental improvements compared to the baselines. 

3. The authors only analyse wavelet-based features for autoregressive models, i.e. Chronos. It would be worth exploring WaveToken in combination with other forecasting models, e.g. non-autoregressive models, or even general time series models. This would provide detailed insight whether wavelet-based features may be beneficial for other architectures or for other tasks such as classification, regression, or imputation.

4. The authors do not report their results across multiple seeds to ensure robustness.

5. The authors do not elaborate on the limitations of their work.

6. The authors neither provide configurations for hyperparamter tuning (including the final hyperparameter setting) nor share their code to support reproducibility.

7. The terminology of the paper lacks clarity. For instance, the authors use the term "language model" throughout their work, which might be confusing since the model is trained from scratch on a large collection of time series. The term time series model would be more appropriate. Additionally, the authors alternate between forecasting "accuracy" and "performance", with the latter being the more suitable term. It should be used consistently throughout the paper to avoid confusion. While technical terms such as "time-localized frequencies" (ll. 14-15) may be familiar in the signal processing community, a brief explanation would help make these concepts accessible to a broader time series audience. In line 415, the authors state "Both Chronos, TimesFM, and Moirai" where I believe they intended to say "~~Both~~ Chronos, TimesFM, and Moirai".

### Questions
1. Have the authors analysed the learned vocabulary? Are there any patterns present in the vocabulary that can be leveraged to further improve tokenisation and ideally downstream performance?

2. The authors state that existing time series models which preserve the natural temporal dependency "tend to focus more either on the recent history or uniformly over all time steps" (ll. 78-79), however, without providing any ground for this claim. Existing time series models [8,9,10,11,12] employ attention-based Transformers, that are known for their attention-weighted (i.e., non-uniform) focus on time steps. Could the authors therefore elaborate further on their statement?

3. How do the authors determine the "average rank" (l. 395) reported e.g. in Figure 10?

4. The authors state that the cross-entropy loss "lends itself well to forecasting applications, where it is often important to capture the correct shape or pattern of the time series without imposing structural limitations such as those inherent in traditional loss functions like MSE and MAE" (ll. 295-298). Could the authors elaborate further on this statement? 

5. Why would the authors "use the last $H$ observations of each time series as a held-out test set" (l. 357) even for zero-shot benchmarking? Are they training or evaluating on the remaining time steps? Why not evaluate the entire time series in the established rolling window fashion [13]?

[8] Ansari et al. "Chronos: Learning the language of time series." arXiv (2024).

[9] Woo et al. "Unified training of universal time series forecasting transformers." ICML (2024).

[10] Goswami et al. "Moment: A family of open time-series foundation models." ICML (2024).

[11] Yang et al. "Biot: Biosignal transformer for cross-data learning in the wild." NeurIPS (2024).

[12] Jiang et al. "Large brain model for learning generic representations with tremendous EEG data in BCI." ICLR (2024).

[13] Zhou et al. "Informer: Beyond efficient transformer for long sequence time-series forecasting." AAAI (2021).

### Soundness
3

### Presentation
3

### Contribution
2
