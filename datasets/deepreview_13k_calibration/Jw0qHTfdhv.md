# Learning to Generate Predictor for Long-Term Time Series Forecasting

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Long-term time series forecasting (LTSF) is a significant challenge in machine learning with numerous real-world applications. Although transformer architecture have shown promising performance in the LTSF task, recent research suggests that they are not suitable for time series forecasting due to their permutation invariant characteristic, and proposes a simple linear predictor which outperforms all existing transformer architectures. However, the linear predictor is inflexible and cannot reflect the characteristics of the time series for prediction due to its simple architecture. In this paper, we introduce a novel Learning to Generate Predictor (LGPred) framework, which generates a linear predictor adaptively to the given input time series by leveraging time series decomposition. LGPred obtains representations from the decomposed time series and generates a predictor suitable for the given time series from these representations.
Our extensive experiments demonstrate that LGPred achieves state-of-the-art performance for both multivariate and univariate forecasting tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the Learning to Generate Predictor (LGPred) framework, a novel approach to enhancing linear time series forecasting models. LGPred adaptively generates a linear predictor tailored to the specific characteristics of a given time series by time series decomposition. This allows the model to discern and adapt to each time series' unique trend and seasonality components. Experimental evidence presented in the paper indicates that LGPred consistently delivers top-tier performance on various benchmarks.

### Strengths
1. The proposed method provides clear motivation for its designs.
2. Empirical results showcase commendable performance, effectively outperforming many preceding methodologies.

### Weaknesses
1. The paper seems to omit discussions on contemporary related works. Notably, the structure of the proposed trend representation module is almost the same as TSMixer [1]. Furthermore, TiDE [2] has previously delved into refining linear models specifically for time series forecasting. Given the architectural similarities between these MLP-based models, a more in-depth comparison and differentiation would enhance clarity. The lack of discussion on how the proposed method differs in its approach to time series decomposition and linear predictor generation from these existing methods makes it difficult to assess the novelty of the contribution.
2. The absence of comprehensive ablation studies leaves the intrinsic value of each component in the proposed method ambiguous. For instance, the ablation analysis in [1] revealed that simpler stacked linear models (i.e., TMix-Only) could rival the performance of the presented methodology. This raises questions regarding the neccesity of LGPred's individual components. Specifically, an ablation study should examine the impact of removing the trend representation module, the seasonality module, and the adaptive predictor generation mechanism individually and in combination to understand their contributions to the overall performance.
3. The delineation of the dimensions for the linear and fully-connected layers remains ambiguous. For multivariate time series data, these layers could be applied across either time or feature dimensions, as depicted in Figure 2. Unfortunately, the descriptions on the predictor generator and template predictor (page 4) do not explain the dimensional characteristics of these layers adequately. It is unclear whether the linear layers are applied independently to each feature or across all features simultaneously, and how the flattening operation is performed before predictor generation.

### Questions
1. Does the proposed architecture incorporate any non-linear activation functions? It's worth noting that certain linear modules, such as $b_{gen}$, might be redundant given that the concatenation of multiple linear layers essentially functions as a single linear layer.
2. Considering the insights from recent works ([1], [2]) highlighting the potential inadequacy of LTSF benchmarks in reflecting models' capability in handling cross-variate correlations, can the LGPred framework be generalized to tackle more intricate datasets like M5 or Favorita, as explored in [1] and [2]?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a learning-to-generate-predictor model, LGPred, for long-term forecasting. In particular, LGPred consists of two parts, a weights generator, and a feature extraction, and then uses a bilinear-type structure to merge them. Moreover, the seasonality trend decomposition is used in the weights generator. Numerical results on 9 datasets are reported.

### Strengths
The usage of bilinear structure seems new in the time series forecasting domain.

### Weaknesses
1. The term *Learning to Generate Predictor* is a little bit overstated from my perspective. My first impression would be a meta-learning model is considered. However, after reading the paper and codes. It seems just a usage of bilinear-type layer for me. I appreciate applying the bilinear layer since it seems not being used in recent forecasting literature. But *Learning to Generate Predictor* may not be the best term to summarize the model novelty for me. If the authors still prefer using *Learning to Generate Predictor*, it would be better to add more discussion to clearly state the difference from the meta-learning type model.

2. The statement "*LGPred is the first attempt at adaptively generating a predictor reflecting the characteristics of each time series.*" seems also a little bit overclaimed. For example, in DeepAR, the network will first generate the $\mu$/$\sigma$ or $\mu$/$\alpha$ for Gaussian distribution or negative binomial (NB) distribution respectively. During the inference stage, the forecasting point will be sampled from the Gaussian/NB distribution. In this case, the Gaussian/NB distribution can be viewed as the *Predictor*, and the parameters in the predictor are learned with a network. The core difference is whether the predictor is a distribution or a deterministic function, and this should be clarified.

3. The test data loader sets `drop_last = True`. In this case, the last several test samples are ignored, which will impact the accuracy of results in Table 1- Table 3. It would be better if the authors could fix it. This is especially concerning given the relatively small size of some of the datasets used, where dropping the last batch could significantly skew the results.

4. It seems that the random control experiments are not conducted. The lack of random control experiments makes it difficult to assess the true contribution of the proposed method, as it's unclear whether the observed performance gains are due to the specific architecture or simply random variations in training.

### Questions
1. The main results in Table 1 - Table 3 are from the model after hyperparameter searching. I'm wondering if the authors can provide a sensitive analysis of the parameter choices to further highlight the robustness of the proposed model.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a model (LGPred) which learns the predictor for each sample in the long-term time series forecasting tasks. The LGPred generates a part of weights and bias for the projection from the input to the output, based on representations learnt from the trend and seasonality of each sample. Experiments on several benchmark datasets are conducted to evaluate the effectiveness of LGPred.

### Strengths
The proposed LGPred can generate dynamic predictors for different samples, which is novel for the long-term time series prediction tasks. The paper is well-written in general and easy to understand.

### Weaknesses
1. Some parts in the Preliminary and Method sections are not clear, e.g.,

-It is not clear why time series forecasting with T>48 is considered as LTSF problem, are there any reasons or references?

-Why change the number of channels in the trend block? The justification for reducing the channel dimension in the trend block, while maintaining the temporal dimension, is not sufficiently explained. Specifically, what is the impact of this channel reduction on the model's ability to capture complex trend patterns?

-The dilated temporal convolutional network should be introduced, in case some readers do not have related background Knowledge. The specific configuration of the dilated TCN, such as the number of layers, dilation rates, and kernel sizes, should be detailed. Without this, it's difficult to assess the effectiveness of this component.

2. The comparison with baselines may be unfair and experiments are insufficient.

-I think it is unfair to compare with PatchTST/64 which uses lookback window length 512 only. As shown in the Figure 2 of the PatchTST paper, the performance is changed with different lookback windows. It is better to choose the best results from different lookback windows for PatchTST for a fair comparison. In addition, even based on the current results shown in the Table 1, the proposed LGPred cannot beat PatchTST/64. The comparison should include a more comprehensive hyperparameter search for PatchTST, or at least justify why the chosen configuration is representative of its best performance. Furthermore, the performance difference between LGPred and PatchTST/64 is not statistically significant in many cases, which raises concerns about the practical advantage of the proposed method.

-It is better to add the results of PatchTST in Table 3 due to its superiority. The absence of PatchTST results in Table 3 makes it difficult to assess the performance of LGPred in short input length scenarios, especially given PatchTST's strong performance in other experiments.

-There is no complexity analysis between the proposal and baselines. A detailed analysis of the computational complexity (e.g., number of parameters, FLOPs) and training/inference time of LGPred compared to the baselines is necessary to understand its practical applicability.

-It is better to provide some experiment results of using RNN and transformer for the trend component. The choice of using a fully connected layer for the trend component is not sufficiently justified. An ablation study comparing different architectures, such as RNNs or Transformers, for the trend component would provide valuable insights into the design choices.

### Questions
Same to the Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new framework called Learning to Generate Predictor (LGPred) for long-term time series forecasting. The key idea is to generate a linear predictor dynamically tailored to the input time series, to overcome limitations of fixed linear predictors. LGPred uses time series decomposition into trend and seasonality components. Separate representation modules extract features from each component. A predictor generator uses the extracted features to generate the weights and biases of a linear predictor suited to the input series. A template predictor with bottleneck architecture is used to incorporate common forecasting knowledge and reduce computation cost. Experiments show state-of-the-art performance on 6 benchmark datasets covering disease, economics, energy, traffic and weather domains.

### Strengths
(1) Novel idea of generating parameters of predictor based on input series, enabling adaptation to each series.

(2) Bottleneck template predictor shares knowledge among different time series and reduces computational cost.

(3) Well-written paper and easy to understand.

### Weaknesses
 (1) The proposed method includes multiple modules, specifically the trend and seasonality representation modules, the predictor generator, and the template predictor, each with their own sets of hyperparameters. The paper does not provide sufficient detail on how these hyperparameters should be tuned, and the lack of extensive hyperparameter tuning experiments is a concern. Furthermore, the rationale for using a bottleneck architecture within the template predictor is not clearly explained. While reducing the number of parameters is mentioned, the specific benefits and potential drawbacks of this design choice, such as the impact on the expressiveness of the predictor, are not discussed in detail.

(2) Time series decomposition into trend and seasonality components is a well-established technique, and the paper does not sufficiently differentiate its approach from existing methods that utilize similar decomposition techniques. The novelty of the approach is not clearly articulated in the context of prior work that also uses time series decomposition.

(3) The experimental results lack crucial statistical information, such as the mean and standard deviation of the performance metrics across multiple runs. This omission makes it difficult to assess the robustness of the proposed method and its sensitivity to initialization. Without this information, it is hard to determine if the reported results are consistent or if they are subject to significant variability.

(4) The experimental evaluation is limited to datasets with relatively simple patterns. The paper does not address the performance of the proposed method on time series data with more complex and non-linear patterns. The applicability of a linear predictor, even a dynamically generated one, to datasets with intricate patterns is questionable, and the paper should include either experimental results or a more detailed discussion of the limitations of the proposed method in such scenarios. The paper also lacks discussion on how the method would perform on time series with different distributions.

### Questions
See my comments in Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
