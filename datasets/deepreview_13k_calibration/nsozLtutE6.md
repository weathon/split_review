# MMFNet: Multi-Scale Frequency Masking Neural Network for Multivariate Time Series Forecasting

- Decision: Reject
- Avg Score: 3.83
- Scores: 3, 3, 3, 5, 6, 3

## Abstract
Long-term Time Series Forecasting (LTSF) is critical for numerous real-world applications, such as electricity consumption planning, financial forecasting, and disease propagation analysis. LTSF requires capturing long-range dependencies between inputs and outputs, which poses significant challenges due to complex temporal dynamics and high computational demands. While linear models reduce model complexity by employing frequency domain decomposition, current approaches often assume stationarity and filter out high-frequency components that may contain crucial short-term fluctuations. In this paper, we introduce MMFNet, a novel model designed to enhance long-term multivariate forecasting by leveraging a multi-scale masked frequency decomposition approach. MMFNet captures fine, intermediate, and coarse-grained temporal patterns by converting time series into frequency segments at varying scales while employing a learnable mask to filter out irrelevant components adaptively.
Extensive experimentation with benchmark datasets shows that MMFNet not only addresses the limitations of the existing methods but also consistently achieves good performance. Specifically, MMFNet achieves up to $6.0\%$ reductions in the Mean Squared Error (MSE) compared to state-of-the-art models designed for multivariate forecasting tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MMFNet, a model aimed at enhancing long-term time series forecasting (LTSF) by employing a multi-scale frequency decomposition technique. Addressing limitations of existing models that assume stationarity and filter out high-frequency components—thus potentially overlooking short-term fluctuations—MMFNet captures both short-term variations and long-term trends by decomposing time series data into fine, intermediate, and coarse segments. These segments are selectively filtered through a learnable mask to focus on relevant frequencies.

### Strengths
- The paper is well-organized, with a logical flow from the introduction to the proposed method and experiments
- The motivation section highlights the limitations of current LTSF models in capturing both short-term fluctuations and long-term trends, emphasizing the need for a model that can balance these aspects. By framing MMFNet as a solution to this gap, the paper sets a compelling context for its multi-scale approach.
- The experiments cover a range of popular LTSF datasets (e.g. ETT, Weather, Traffic, and Electricity), and inclusion of both high-channel and low-channel datasets helps validate the model’s versatility in different settings.

### Weaknesses
Despite the performance gains across multiple datasets, the motivation is not fully substantiated: 

- The rationale for multi-scale frequency decomposition lacks empirical grounding, as the manuscript does not convincingly demonstrate why a single-scale approach falls short. While the authors reference assumptions of stationarity, they do not provide empirical evidence or citations that highlight the limitations of single-scale models in specific LTSF scenarios. The paper needs to show concrete examples where single-scale methods fail, particularly in capturing both short-term and long-term dependencies simultaneously. A more rigorous analysis of the frequency characteristics of the datasets used, showing how these characteristics vary across different time scales, would strengthen the justification for the multi-scale approach.

Additionally, several design choices require further explanation:

- The learnable mask's role in frequency filtering is not well-clarified in terms of its operational benefits over traditional fixed-frequency filters. While described as "self-adaptive," the paper does not detail how the mask parameters are optimized or discuss their consistent effectiveness across datasets. For instance, the appendix includes some masking results, but without analysis on how these masks contribute to the model’s forecasting accuracy. The paper should include a more detailed analysis of the mask's behavior, showing how it adapts to different frequency components and how this adaptation leads to improved forecasting performance. A comparison of the learned masks across different datasets and time series would also be beneficial.

Improving the experimental design to highlight robustness in non-stationary settings would enhance the study's validity:

- Although MMFNet achieves moderate performance improvements on benchmark datasets, its robustness to non-stationary data remains unclear. The experiments do not include clearly non-stationary datasets or demonstrate superior performance under such conditions. The chosen datasets, like ETTh1 and Electricity, mainly display seasonal patterns, making it uncertain if MMFNet is truly resilient to non-stationary series. The paper needs to include datasets with more complex, non-stationary characteristics and provide a detailed analysis of how MMFNet performs in these scenarios. This would involve showing how the model adapts to changes in the statistical properties of the time series over time.

Lastly, computational analysis and comparisons to related works [1][2] would be beneficial:

- The multi-scale decomposition and frequency masking likely introduce computational overhead, but the paper does not quantify these costs or evaluate MMFNet’s efficiency in practical applications. A detailed comparison of MMFNet’s computational complexity against simpler models would clarify the trade-offs between overhead and performance. Additionally, recent relevant baselines, such as [2], have not been addressed in the manuscript.

### Questions
In conclusion, while the paper proposes a novel approach to long-term time series forecasting through multi-scale frequency decomposition, the necessity of this complex approach is not fully justified. Although the motivation to capture both short-term fluctuations and long-term trends is valid, the rationale behind key design choices, such as the adaptive masking mechanism, is underexplained. Furthermore, the model’s empirical gains over existing baselines are modest and inconsistent across datasets, reducing the impact of the experimental findings. Nonetheless, the paper is well-organized, and the architecture shows potential, especially if the authors can clarify the interpretability of the frequency masking mechanism and strengthen the model's practical applicability through more targeted benchmarks.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
MMFNet is a predictive model designed for non-stationary time series, addressing the limitations of Single-scale Frequency Decomposition methods like FITS, which struggle to capture non-stationary patterns and may miss short-term fluctuations. To overcome these limitations, MMFNet introduces a Multi-scale Frequency Decomposition approach. Additionally, it incorporates a learnable mask that selectively filters out irrelevant frequency components at each scale, thereby enhancing prediction accuracy and effectively capturing both short-term variations and long-term trends.

### Strengths
1. Clear Identification of Limitations: The paper effectively identifies the limitations of existing methods like FITS, particularly in handling non-stationary data and capturing short-term fluctuations. This acknowledgment establishes a strong rationale and relevance for the proposed research.
2. Well-Organized Presentation: The methodology is well-organized and explained step-by-step, making the approach accessible and easier for readers to understand.

### Weaknesses
1. Unclear Motivation: The paper aims to analyze time series data across multiple scales, an approach that has also been explored by methods like TimeMixer, PITS, and FITS. However, it lacks a clear motivation for why this particular approach is necessary and does not sufficiently explain how MMFNet differs from or improves upon these existing methods. It would help if the authors more explicitly justified their approach by highlighting the specific advantages or unique aspects of MMFNet that set it apart from similar multi-scale methods.

2. Limited Novelty: The proposed method feels more like a variation on established approaches rather than a fundamentally new concept. Both multi-scale analysis and frequency masking techniques have been explored previously in time series research, making it challenging to see where MMFNet offers substantial innovation. The paper could benefit from a clearer articulation of its novel aspects, such as whether MMFNet provides specific advancements in frequency decomposition or interpretability that distinguish it from other multi-scale approaches.

3. Insufficient Comparative Experiments with Existing Models: The paper lacks enough experimental comparisons with other prominent models (e.g., TimeMixer) to effectively demonstrate any performance advantages or unique capabilities of MMFNet. Direct comparisons on standard datasets with similar metrics could better showcase the proposed model’s strengths and allow readers to more easily assess its advantages over existing approaches.

4. Limited Persuasiveness Due to Lack of Novelty: Given the number of studies on multi-scale time series analysis, the paper does not provide sufficient differentiation to persuade readers of MMFNet's unique contributions. Expanding the explanation of MMFNet’s specific innovations and benefits could strengthen its positioning as a valuable addition to the existing research.

### Questions
1. How does the proposed Multi-scale Frequency Decomposition specifically address non-stationarity?
Further explanation of how multi-scale decomposition effectively handles non-stationary characteristics would help clarify this point.

2. What are the limitations of the multi-scale approach, and are there any suggested improvements?
Every multi-scale approach may have limitations, such as increased noise or computational complexity. It would be valuable to discuss any potential drawbacks of this method and ways to mitigate them.

3. How does the proposed method compare in terms of computational cost or time complexity to existing models?
Providing a comparison of computational efficiency would help readers understand the practicality of the proposed model.

4. Are there experimental results on the National Illness dataset?
Results on such datasets would help demonstrate the relevance and applicability of the method, particularly for health-related time series data.

### Soundness
3

### Presentation
3

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
This paper presents MMFNet, a multi-scale frequency masking model for long-term time series forecasting. Unlike most existing models that operate in the time domain, MMFNet follows the light-weight model, FITS (ICLR’24), to learn and capture the dynamic variations in the frequency domain. Compared with FITS, MMFNet has made the following improvements: (1) the multi-scale frequency decomposition to effectively capture both local and global patterns in data; (2) the learnable frequency mask to focus on the most informative frequency components. MMFNet achieves competitive performance to SOTA baselines on several widely-used long-term time series forecasting (LTSF) datasets.

### Strengths
- The paper is well-organized and highly readable, and the figures makes it easy to understand the model designs.
- Authors provide ablation analysis to demonstrate the effectiveness of the proposed techniques, i.e,  the multi-scale frequency decomposition and learnable masking.
- I especially appreciated the exploration of  frequency domain for time series modeling, and the experiments show its promising performance.

### Weaknesses
 - MMFNet seems to be an incremental improvement over FITS, and it appears that the motivation and claim are not well-supported. Specifically, MMFNet may not adequately address the“non-stationary characteristics that SFT may "overlook". Since learnable masks are trained and shared across the whole time series dataset, different time series will be masked out in the same way (via the shared masks).  Therefore, the learnable mask is not so “adaptive”.

- The paper lacks some details. For methodology, it is unclear how to interpolate $X_{DCT}$ of various-length segments and merge them together, some formulas are needed. For experiment settings, the segment num of different temporal scales and the look-back window lengths for various forecasting horizons are not mentioned. I am especially curious about input window length for ultra-long-term forecasting. 

- The experimental evaluation seems insufficient. For ablation study, in section 4.3, the impact of different segment num combinations on MMFT should be explored; in section 4.4, the results comparing “Mask” vs. “low pass filter” should be provided to support the paper’s claim. Additionally, I would greatly appreciate it if more comprehensive comparisons could be included in the paper. For examples, the results on different look-back window lengths and visualization of prediction results.

### Questions
More discussions: 
- FITS can handle the anomaly detection task, does MMFNet also have such capabilities? Since the MMFNet adopts a masking and interpolation approach, it seems more suitable for reconstruction tasks?
- Is the number of model parameters large? From my understanding, each segment has its own learnable mask and linear layer. Consequently, it appears that increasing the number of segments could lead to a significant expansion in the model's parameter count.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary: 
This paper introduces MMFNet, a novel model designed to enhance long-term multivariate forecasting by leveraging a multi-scale masked frequency decomposition approach. Experimentation with benchmark datasets shows that MMFNet achieves good performance.

### Strengths
Strengths: 
1. MMFNet employs multi-scale frequency domain decomposition, exhibiting a certain degree of innovation.
2.MMFNet achieves good performance in a variety of multivariate time series forecasting tasks.
3.The paper is largely understandable.

### Weaknesses
Weaknesses:
1.The motivation behind the paper is not clearly articulated. The author mentions: “While single-scale frequency domain decomposition offers a global perspective of time series data in the frequency domain, it lacks the ability to localize specific frequency components within the sequence.” This statement requires further explanation—why is it unable to localize specific frequencies? Similarly, the author needs to further elaborate on why MMFNet can handle non-stationary series (along with detailed examples). These are key points and contributions of the paper.
2.Using only the MSE metric is insufficient. Does the model show similar performance when evaluated using other metrics such as MAE?
3.The visualization work in the paper is not particularly sufficient. The authors should include more comparative figures between Single-Scale Frequency Transformation and Multi-Scale Frequency Transformation, as well as visualizations of the mask effects, and prediction showcases of different models.
4.The authors should compare the models across more dimensions, such as parameter count, training and inference time.
5.The baseline models are not very rich; the current research primarily focuses on analysis at the temporal scale. Recently, there has been some work exploring the variable perspective, yielding good results, such as with the iTransformer and Client models. It is recommended to include these comparisons as well.
6.The authors claim that "Transformer-based architectures have demonstrated exceptional capacity in capturing complex temporal patterns by effectively modeling long-range dependencies through self-attention mechanisms at the cost of heavy computational workload, particularly when facing large-scale time series data, which significantly limits their practicality in real-time applications." This claim is not comprehensive; a more significant limitation of Transformer-based models is their tendency to overfit.

### Questions
Questions:
1.What is the length of the historical look-back window used in the experiments reported in Table 1? Were the baselines’ results in Table 1 obtained from other literature or tested by the authors?
2.Can the Multi-Scale Frequency Transformation and Masked Frequency Interpolation methods proposed in the paper be used as plug-and-play components with other time series models?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a simple time-series prediction model, MMFNet, based on multi-scale feature fusion using DCT combined with a masking mechanism. The model first divides the input sequence into three different scales, applies DCT transformation to each scale, and obtains frequency domain features at different scales. Then, adaptive filtering is applied to these frequency domain features using a masking operation. A simple linear interpolation layer is used to obtain predictions at each scale, and the final prediction is obtained by applying the inverse DCT and summing these results. The authors validate the model's effectiveness through a series of experiments and demonstrate the importance of the masking mechanism and multi-scale feature fusion to the model's performance through ablation studies.

### Strengths
1. The model design appears very simple and achieves good results, surpassing existing mainstream models.
2. The authors validate the effectiveness of multi-scale frequency domain feature extraction and the masking mechanism on the model's performance through a series of visual experiments and ablation studies, providing some explanations for these.
3. The experiments on extending the horizon sufficiently show that the model has excellent long-term sequence prediction capabilities.

### Weaknesses
1. The authors did not explain why DCT was chosen rather than other transformations, such as the more common Fourier transform. What's the advantage of DCT? Are there other transformation methods that could be used instead? Specifically, the paper lacks a discussion on the computational complexity and potential information loss associated with using DCT compared to other transforms like the Short-Time Fourier Transform (STFT), which could offer a time-frequency representation. A more thorough justification of this choice is needed, considering the specific characteristics of the time-series data being analyzed.
2. The authors argued that this is the first model to use multi-scale frequency domain feature fusion, but there is no discussion on the advantage of frequency domain processing compared to time domain multi-scale feature fusion. The paper should elaborate on why transforming to the frequency domain is beneficial for multi-scale analysis in this context. A comparison to existing time-domain multi-scale methods, highlighting the specific limitations they face when dealing with periodic or global patterns, would strengthen the argument for using frequency domain processing.
3. The paper claimed that multi-scale frequency decomposition can capture short-term fluctuation characteristics, but there is no intuitive result that demonstrates this. Moreover, what's different information captured by the features at different scales? The paper needs to provide more concrete evidence, such as visualizations of the transformed data at each scale, to support the claim that short-term fluctuations are captured. Without this, it's difficult to understand how the model differentiates between short-term noise and actual short-term patterns. Furthermore, a detailed explanation of the specific types of information captured at each scale (fine, intermediate, coarse) is missing, making it hard to interpret the model's behavior.

### Questions
1. In the paper,  three specific scales were designed. Why were these particular sizes (2, 24, 720) chosen? Are there other choices for small and medium scales (such as 4, 48)? Is the model's performance sensitive to the choice of these scales?
2. In Figures 2 and 3 of the appendix, the actual output of the mask is shown, but the shape of the mask seems inconsistent with what was described in the text. The segment lengths for fine-scale and intermediate-scale are 2 and 24, respectively, so the mask lengths should correspond to 2 and 24. However, the mask length in the figure seems to be 720. Was there an intermediate step involved? Can the authors clarify this?
3. The mask output seems to exhibit certain low-pass characteristics at fine-scale and intermediate-scale, while showing high-pass characteristics at coarse-scale. Can you further explain this phenomenon?
4. Can you provide some visualizations of the features learned at different scales? For example, the weights of the linear interpolation layer corresponding to different scales and the final output, etc.
5. During the inversion step, the 3 output were first applied with the inverse DCT, then summed up. Is there any reason for this? Because from a theoretical perspective, the inverse DCT is a linear operation, so the sum of the inverse DCT of the 3 outputs is equivalent to the inverse DCT of the sum of the 3 outputs. By swapping the order of the sum and the inverse DCT, the computational complexity can be greatly reduced. Can you explain this design choice?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the multivariate time series forecasting task and proposes the MMFNet for decomposing the input series into multi-scale segments and further capturing the multi-frequency components. A learnable masking and frequency interpolation strategy is employed for prediction. The authors have tested MMFNet on typical time-series forecasting benchmarks.

### Strengths
This paper is overall well written.

The experiments and ablations are relatively comprehensive.

The idea of decomposing time series into multi-frequency components is reasonable and effective.

### Weaknesses
1.	About the method design.

As shown in Figure 1, the authors implement the frequency decomposition by segmenting the input series into multiscale subseries. 

I am curious about does this design perform like directly segmenting the transformed frequency domain. I mean that we do not need to split the input series at first for multifrequency components. Directly applying FFT to the original input series and then splitting the frequency domain can obtain the same results.

Going further, I think without multifrequency decomposition, a learnable mask strategy along with frequency interpolation can achieve a similar performance. Thus, I am doubtful about the actual novelty of this paper.

2.	About the claim of “multivariate time series forecasting”.

I am not sure if MMFNet employs the same “channel independent” training strategy as PatchTST. I believe that channel-independent training is not “multivariate series modeling”, which does not consider the correlation among different series.

Besides, I think the current design can be extended to univariate series (as presented in Figure 1). The experiments on M4 are necessary. Actually, as discussed in FITS, these linear models may fail in M4, which contains much more complex temporal variations than the widely used LTSF benchmarks.

With the experiments on complex datasets, I cannot confirm whether the proposed method is really effective.

3.	How about the efficiency of MMFNet w.r.t. other linear models, including GPU memory, parameter size, and running time?

4.	Since the absolution promotion is kind of limited, the standard deviation or confidence level is expected.

### Questions
Does MMFNet employ the “channel independent” strategy for training?

### Soundness
2

### Presentation
3

### Contribution
2
