# xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Memories

- Decision: Reject
- Scores: 6, 3, 5, 8, 3

## Abstract
Time series data is prevalent across numerous fields, necessitating the development of robust and accurate forecasting models.
    Capturing patterns both within and between temporal and multivariate components is crucial for reliable predictions.
    We introduce \ours{}, a model designed to effectively integrate temporal sequences, joint time-variate information, and multiple perspectives for robust forecasting.
    Our approach begins with a linear forecast shared across variates, which is then refined by xLSTM blocks.
    They serve as key elements for modeling the complex dynamics of challenging time series data.
    \ours{} ultimately reconciles two distinct views to produce the final forecast.
    Our extensive evaluations demonstrate its superior long-term forecasting performance compared to recent state-of-the-art methods.
    A thorough model analysis provides further insights into its key components and confirms its robustness and effectiveness.
    This work contributes to the resurgence of recurrent models in time series forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces xLSTM-Mixer, a new model for forecasting complex time series data with multiple variables. It combines the xLSTM architecture with multi-view processing and variate mixing. The model works in three stages: first, it creates an initial forecast, then it uses xLSTM blocks to combine time and variable patterns, and finally, it merges two different forecast views for results in most cases beating baseline models. xLSTM-Mixer addresses challenges associated with Transformer models, such as high computational costs and data requirements for long sequences.

### Strengths
**Originality**
xLSTM-Mixer combines temporal sequences, joint time-variate information, and multi-view perspectives to handle multivariate time series complexities, capturing temporal and cross-variate patterns for accurate predictions, it builds on prior work, but combines it in an intricate way. The work enhances the xLSTM architecture, however limiting itself to the sLSTM.

**Quality**
The work is written with enough clarity, related work is addressed and the paper is fairly easy to understand. The graphical presentation of the model allows for easy following.

**Significance**
Authors do not claim state-of-the-art performance, however, they do beat the current baselines to which they compare themselves. It is the second work relating to the use of xLSTM to time series, and authors raise concerns about the first one, those concerns must be backed in the future.

### Weaknesses
**Weaknesses**

1. The authors conduct experiments on only a subset of datasets, specifically focusing on a subset of the Informer long-horizon forecasting datasets and omitting the Exchange dataset, which would add considerable value if included. The reviewers would appreciate a deeper analysis of why the XLSTM-Mixer performs better on some datasets and worse on others, particularly through an exploration of cross-correlation between variables and model performance.

2. The ablation study, conducted on only two datasets, lacks breadth. Expanding this experiment across additional datasets would significantly strengthen the findings.

3. The experiments do not address a critical aspect: the model's sensitivity to the order of variates, as it is not permutation invariant in this regard.

### Questions
1. The term "Mix View" in Table 3, line 332, is unclear and challenging to interpret. Could you clarify if this refers to the performance of channel mixing?

2. The dataset selection could be expanded to include the Exchange from the  (Informer long-horizon forecasting datasets) datasets and more extensive ablation studies across additional datasets to provide a thorough evaluation of the xLSTM-Mixer’s performance, including an exploration of cross-correlation between variables and model effectiveness on different datasets or synthetic ones.

3. Consider incorporating synthetic data to facilitate verification of learnable concepts and addressing the model’s sensitivity to the order of variates, as it lacks permutation invariance.

4. I would highly encourage you to back the claims of challenges in the reproducibility of prior works and why trend-seasonality decomposition is redundant.

### Soundness
2

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
4

### Summary
This paper introduces a new time series prediction model called xLSTM-Mixer, which aims to effectively capture and integrate complex patterns in time series data by combining linear prediction with xLSTM blocks. The model first uses a shared linear model to make initial predictions for each variable, then fine-tunes and mixes these predictions through a series of sLSTM modules, and finally generates the final prediction result by integrating two different perspectives' predictions. Experimental results show that xLSTM-Mixer has significant advantages in long-term time series prediction tasks, achieving better predictive accuracy than current state-of-the-art methods on multiple benchmark datasets. In addition, the article conducts detailed analysis of the model, including A/B testing, sensitivity analysis of hyperparameters, and research on initial embedding vectors, further validating the effectiveness and robustness of the model. This work not only improves the level of deep learning-based time series prediction technology but also provides new directions for future related research.

### Strengths
- Superior long-term forecasting performance: xLSTM-Mixer outperforms recent state-of-the-art methods in terms of predictive accuracy on various benchmark datasets.

- Robustness and effectiveness: Detailed model analysis, including A/B testing, sensitivity analysis of hyperparameters, and research on initial embedding vectors, further validates the effectiveness and robustness of the model.

- Contribution to the resurgence of recurrent models in time series forecasting: By combining linear prediction with xLSTM blocks and integrating time, variate, and multi-view mixing, xLSTM-Mixer enhances the learning of necessary features and offers a viable alternative to current sequence models, contributing to the resurgence of recurrent models in time series forecasting.

### Weaknesses
- The contribution regarding advancement of  xLSTM-Mixer over the base xLSTM model is not clearly defined. The novelty and significant contributions need further clarification to distinguish xLSTM-Mixer as more than a trivial modification.

- The paper asserts that longer lookback lengths improve forecasting but Figure 5 shows increased MSE at a lookback length of 1024 compared to 768. This requires further exploration as it conflicts with the claims.

- The manuscript dismisses trend-seasonality decomposition without empirical support, which is a significant weakness given the technique's established value in forecasting.

- The paper omits a comparison of the xLSTM-Mixer's computational complexity and cost against other methods, a critical evaluation factor for practical model deployment.

### Questions
- The manuscript fails to convincingly argue the substantial novelty of xLSTM-Mixer compared to prior xLSTM models. Authors should clarify that xLSTM-Mixer is not merely a combination of xLSTM and Multi-View Mixing, as the current description lacks the depth to establish its significance.

- While the manuscript acknowledges xLSTM-Mixer's performance with varying lookback windows (Figure 5), it lacks a thorough experimental setup to explore different input/output ratios. A comprehensive analysis should include varied input lengths relative to output horizons to assess model robustness. The absence of this setup limits understanding of performance in diverse forecasting conditions. Additional experiments with varying input/output ratios, as suggested by Table 6, are recommended.

- The paper does not explain the increase in MSE at a lookback length of 1024, leaving readers unclear about the model's behavior. To strengthen the manuscript, the authors should provide a plausible explanation or conduct additional experiments to verify performance consistency across different lookback lengths.

- A significant issue is the claim that a simple NLinear normalization scheme is sufficient without rigorous testing or theoretical backing. The decision to forgo trend-seasonality decomposition and rely solely on NLinear normalization lacks the necessary validation, raising questions about the model's robustness. More experimental corroboration against established methods is needed.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel design - xLSTM-Mixer which is based on LSTM and a set of mixing machanism for multivariate time series forecasting. The model builds on the idea of recurrent structures, integrating three mixing strategy: an initial linear forecast with time mixing, joint mixing with sLSTM blocks, and a final view mixing stage. Evaluations show that xLSTM-Mixer achieves state-of-the-art forecasting performance across multiple datasets which is a key contribution to the ongoing development of recurrent models.

### Strengths
**Innovation in Model Architecture**: The integration of time and variate mixing with xLSTM blocks is an innovative approach. This design tackles some limitations of conventional recurrent and transformer-based models in capturing complex temporal dependencies, which is especially challenging in multivariate time series data. 

**Empirical Performance**: The experiments show that xLSTM-Mixer outperforms a variety of established methods (e.g., Time-Mixer, iTransformer, MICN) in terms of mean squared error (MSE) and mean absolute error (MAE) across multiple datasets, together with comprehensive ablation studies on initializations, size of hidden dimension and length of lookback window shows the model’s robustness and generalizability.

### Weaknesses
**Model structure**: 
LSTM-Mixer appears to be an incremental improvement over xLSTM, and the mixing machisim does not seems to be very siginificant regards to the Ablation Study on Table 3. An experiment with alternative recurrent structures may help here. Instead of relying solely on the sLSTM block with the joint mixing machinism, it would be usefule to assess the performance of other recurrent models, such as GRU and Mamba.

**Computational Efficiency**: 
The complexity of xLSTM-Mixer’s mixing machanism and recurrent structures would be computationally intensive. Further discussion on the computational costs relative to attentions and SSMs would be beneficial. 

**Evaluation on Short-Term Forecasting**:
While the model demonstrates strong performance in long-term forecasting, the short-term forecasting evaluation is inadequate. Adding a more robust short-term evaluation could highlight the model’s flexibility across different forecasting horizons.

**Evaluation on Long-Term Forecasting**:
Although most studies follow the 96, 192, 336, 720 prediction length on benchmarks, regards to this work highlighted long-term forecasting as a distinctive feature, a prediction length of 720 is insufficient.

### Questions
**More discussion on the use of Multivariate information**:
- Firstly, the primary innovation claimed by the authors is the use of multivariate time series forecasting. However, simply explaining how the new method works and benchmarking with other multivariate models is insufficient. Since the impact of using multivariate information varies across different datasets and variables, and given that multivariate mixing is the core innovation, additional analysis on this aspect should be provided.
- Secondly, whats are the authors' opinion on the heterogeneity of variates, and how important is this compare to the temporal dependency in terms of forecasting? 
- Thirdly, the authors mention that variate ordering may impact performance but leave this for future work. Given the importance of variate dependencies in time series, a preliminary exploration of this factor could provide additional insights into potential model improvements.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduce  a novel time series forecasting model with time and variate mixing in the context of recurrent models.

### Strengths
- Figure 1 provides a clear overview of the method.
- Several commonly used benchmark datasets are included.
- The proposed xLSTM-Mixer model consistently achieves state-of-the-art performance across a broad range of benchmarks.
- Informative forecast plots are included.
- A comprehensive set of baseline models from different architecture categories including, Transformer-based, CNN-based, MLP-based, and Recurrent architectures.
- The ablation study on architecture choices is highly insightful and supports the combined aspects of the proposed model.
- Open-source code is available with reproducible experiments

### Weaknesses
1. Random seeds were included as a hyperparameter, but it would be beneficial to train the model over several trials to compute the average and standard deviation of the results. This approach would provide a more robust measure of performance consistency across runs.
2. The approach does not reference similar architectures, such as iTransformer, which utilizes the attention and feed-forward network on inverted dimensions. In iTransformer, individual time points are embedded as variate tokens, leveraging the attention mechanism to capture multivariate correlations. This bears a resemblance to the proposed method, which jointly combines time and variate information to capture complex patterns in the data by employing transposed input dimensions to invert the series. Mentioning this may help emphasize the translatable similarities across architecture backbones.
3. The motivation for the reverse-up projected embedding is not explicitly explained. Including an ablation study of the model with and without this embedding would be useful to help justify this architectural choice.
4. Some models cited in prior work are missing as baselines, including TFT, N-HiTS, and N-BEATS.

### Questions
Suggestions:
- Adding dimensions to Fig. 1 would help clarify input shapes after higher-dimensional projections and transpositions.
- Lines 41-42: Regarding Transformer architectures, the authors state, “For instance, they typically require large datasets to train successfully, restricting their use to only a subset of applications.” However, I do not believe this claim is fully supported by the literature. For example, common benchmarks for long-horizon forecasting include datasets like ILI, Traffic, and Weather. The ILI dataset, with only 966 timestamps, could be considered relatively small, yet PatchTST outperforms other Transformer and linear models on this dataset [1]. Similarly, for ILI, Autoformer outperforms other models, including recurrent architectures like LSTMs [2].
- It would help motivate the proposed approach to illustrate the trade-offs in computational complexity between the proposed model, Transformer-based models, and MLP-based models for both training and inference.
- While model hyperparameters for the proposed model are included in the appendix, it would be helpful to provide hyperparameters and the number of training epochs for the baseline models as well.
- Additional benchmark datasets could include ILI and Exchange datasets which are used in prior work [2].

References:
1. “A Time Series is Worth 64 Words: Long-term Forecasting with Transformers”
2. “Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting”

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work proposed xLSTM-Mixer for multivariate time series forecasting that combines linear forecasters (NLinear) with efficient recurrent xLSTM blocks. By adapting xLSTM modules for the temporal and variate dimensions, the model refined the predictions of NLinear with the utilization of time-variate information. The model also employs techniques like reversible instance normalization and soft prompt tokens to further improve the performance. Empirical experiments demonstrate that xLSTM-Mixer can outperform several baseline methods in most cases in long-term forecasting.

### Strengths
1. The motivations are well-summarized and the paper's writing is easy to follow.
2. The author provides the code to ensure the reproducibility of the paper.

### Weaknesses
1. The main contribution of this paper is to refine the predictions obtained from NLinear by introducing xLSTM modules, which may lack novelty and motivation in technology. On the one hand, please clarify more about the advantages of xLSTM modules that have been refined over (linear forecaster + renorm). For example, to support the mentioned advantages of modeling variate relationships, you can provide a comparative analysis of xLSTM against MLP mixers and efficient attention modules in the Mixer architecture. Also, extending ablation studies (Table 3) to more datasets and different variate-mixing modules would provide a more comprehensive evaluation of the model's effectiveness.
2. It is uncertain whether the authors use the unidirectional xLSTM, which is generally adopted for sequential modeling, to model the correlations of variates. If it is unidirectional, please explain how it addresses the non-sequential nature of the variate correlation, and discuss the potential benefits or drawbacks of using a bidirectional approach in this context.
3. This paper mainly provides the results of long-term forecasting. The lookback seems to be fixed at 96. Considering the extensive overfitting of current deep models on these datasets, it is recommended that the author provide more comparisons with varying lookback lengths and on additional datasets that are less prone to overfitting. This would provide a more robust evaluation of the model's performance.
4. Compared with related recurrent models (such as xLSTMTime), the performance improvement of the proposed model is not significant shown in Table 2. The author should add more recent recurrent models (e.g., SutraNets and P-sLSTM) and more discussions with related work.
5. The showcases in Figure 2 do not reflect the advantages of xLSTM-Mixer in multivariate modeling. To make it more specific, please include visualizations that explicitly show how xLSTM-Mixer captures relationships between multiple variates in its predictions.
6. The paper concludes by highlighting the potential of xLSTM-Mixer for future research in areas such as short-term forecasting, time series classification, and imputation. I wonder if there are some results on these analysis tasks using xLSTMs.

### Questions
1. Has the author tried to train on time series with randomly shuffled temporal orders, and what will happen to the results?
2. About the experiments of enlarging lookback (Figure 3): In the DLinear paper, the performance can also be improved by increasing the lookback using a single linear layer. It is suggested that the author introduce such linear models into the baseline. Otherwise, the advantage can only be due to NLinear. It is also encouraged to provide the model performance with a longer lookback length to verify whether the proposed can continuously improve the performance (or keep it stable in a very long lookback length).

### Soundness
2

### Presentation
2

### Contribution
1
