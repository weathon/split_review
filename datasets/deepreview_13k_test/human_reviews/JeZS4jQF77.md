# LiNo: Advancing Recursive Residual Decomposition of Linear and Nonlinear Patterns for Robust Time Series Forecasting

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Forecasting models are pivotal in a data-driven world with vast volumes of time series data that appear as a compound of vast \textbf{Li}near and \textbf{No}nlinear patterns. 
Recent deep time series forecasting models struggle to utilize seasonal and trend decomposition to separate the entangled components. Such a strategy only explicitly extracts simple linear patterns like trends, leaving the other linear modes and vast unexplored nonlinear patterns to the residual. Their flawed linear and nonlinear feature extraction models and shallow-level decomposition limit their adaptation to the diverse patterns present in real-world scenarios.
Given this, we innovate Recursive Residual Decomposition by introducing explicit extraction of both linear and nonlinear patterns. This deeper-level decomposition framework, which is named \textbf{LiNo}, captures linear patterns using a Li block which can be a moving average kernel, and models nonlinear patterns using a No block which can be a Transformer encoder. The extraction of these two patterns is performed alternatively and recursively. To achieve the full potential of LiNo, we develop the current simple linear pattern extractor to a general learnable autoregressive model, and design a novel No block that can handle all essential nonlinear patterns.
Remarkably, the proposed LiNo achieves state-of-the-art on thirteen real-world benchmarks under univariate and multivariate forecasting scenarios. Experiments show that current forecasting models can deliver more robust and precise results through this advanced Recursive Residual Decomposition. We hope this work could offer insight into designing more effective forecasting models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new neural network architecture for multi-variate time series forecasting. The main idea is to iteratively extract linear and non-linear patterns from the time series which are easier to learn and forecast. The linear patterns are extracted using 1D convolutions (part of the Li Block) where as the non linear features (part of the No Block) are extracted using linear projections on the frequency (FFT) and time domain (temporal variation features). The inter time-series dependencies are modeled using a weighted mean (akin to a pooling function) where the weights are computed using a softmax function.

The LiNo blocks are iteratively applied to the residuals to build predictors for each residual. All the predictors are finally added to produce the final prediction. The authors have presented extensive experimentation showing the effectiveness of the approach yielding state of the art results on several benchmark datasets.

### Strengths
Strengths:
- The author presented a novel time series forecasting method based on the idea of iteratively extracting linear and non-linear features from the residuals. While the idea has been introduced earlier in the literature (RRD), this paper extends the idea using neural networks.
- The experiments performed in this paper are extensive and the baselines used are state of the art. Comparison with several state of the art baselines on benchmark performance shows improved prediction accuracy.
- Additionally, the analysis presented in the paper including the ablation studies are extensive furthering strengthening the proposed method.

### Weaknesses
Weaknesses
- Several parts of the paper are unclear. In particular the design of the model (see questions below)
- The paper builds on the ideas of residual modeling and non-linear feature extraction using FFT, both which have been explored earlier in the literature [1, 2, 3] ([1] has not been cited), weakening the novelty of the approach slightly.

[1] Oreshkin, Boris N., et al. "N-BEATS: Neural basis expansion analysis for interpretable time series forecasting." arXiv preprint arXiv:1905.10437 (2019).

[2] Challu, Cristian, et al. "Nhits: Neural hierarchical interpolation for time series forecasting." Proceedings of the AAAI conference on artificial intelligence. Vol. 37. No. 6. 2023.

[3] Xu, Zhijian, Ailing Zeng, and Qiang Xu. "FITS: Modeling time series with $10 k $ parameters." arXiv preprint arXiv:2307.03756 (2023).

### Questions
- What is the advantage of using frequency domain operations? How do they benefit the predictions? Is it only useful if there are cyclical seasonal patterns? Will it be useful in cases where there is no seasonality or the frequency of the seasonal pattern can shift?
- Line 239 to 243: Can you elaborate on how the softmax is applied and the weighted mean is computed? It would be helpful to include a figure showing this operation in detail.
- How is the FFT and IFFT calculated? In particular, is this operation differentiable is is back-propagated through?
- Where does H_i sit in figure 2?
- Figure 2 No Block: Why is the MLP applied to the final prediction (right before adding the prediction from the Li Block) but not when computing the residual for the next block?
- Figure 2: What does the backbone consist of?
- What is the purpose of dropout in Equation 2? Does it help with spreading out the coefficients across the whole input window rather than have it concentrated on a few time steps?

Some suggested clarifications in the text:
- Line 078: "Another problem is the design of current nonlinear models, which mainly focus on
one or two types of nonlinear patterns."
Which types of non-linear patterns are being talked about here.
- Line 090: What is "traditional RRD"?
- Line 143: Typo "closely close"
- Eq 3: did you mean T<D?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The paper identifies explicitly and iteratively extracting linear and nonlinear patterns from time series as an opportunity to learn highly effective forecasting models.
- The extracted patterns are combined via simple linear layers to form the forecast.
- The method is then evaluated in a variety of experiments.

I did not check the entire appendix.

### Strengths
- I am not aware of these ideas being proposed before. However, I am not sufficiently familiar with the topic to rule it out definitively.
- The quality of the presentation ranges from poor (method section) to good (experiments).
- Time series forecasting is relevant in many domains and is far from being solved. The proposed method investigates a method that is interesting due to its interpretability and fair performance.
- The experiments go beyond mere performance metrics, performing an ablation study, other variations, depth sensitivity analysis, and lookback length investigations.

### Weaknesses
1. The method presentation in (mainly) Sec. 3.2 is poor. The notation is more complicated than necessary (e.g., it includes a batch dimension) while not being sufficiently precise to fully specify the computation (e.g., in l. 239 to 243). The accompanying Figure 2 further complicates things by its inconsistent colors, the red cutout not showing what it points at (on the left, the projections were independent), the MLPs only being linear layers, the "Cat" being a Hadamard product, arrows leading into the nothingness, and inconsistent formatting. See also the Questions section.
2. It is unclear to me why the Li block is called Linear. Going by Fig. 2 or Fig. 5, neither the pattern nor the prediction is linear in the time index, and the learned function is neither (e.g., there is a Dropout layer).
3. The learned representations are somewhat redundant. See, e.g., LP2 and LP3 in Fig. 5 (ETTh1, center) or NP1 and NP2 in Fig. 5 (ETTh1, right). These representations are not used for model interpretability.

#### Minor Comments
- The text size for the figure captions was very likely reduced from what is specified in the template.
- The reference's formatting is very sloppy (missing venues, capitalization of titles and names, broken math notation, and inconsistency).
- Section 3 could be simplified by omitting the batch dimension, as every operation only operates on a single time series. Given the deep learning context, a batch dimension can be conceptually added simply in one sentence without complicating notation.
- Language: "TSMxier" typo in l. 103. Reference in l. 118. Used citet instead of citep in l. 252. ...
- The convention of typesetting vectors and matrices in bold might ease readability (starting in Sec. 3.1).
- The images are not included as vector graphics, limiting accessibility, the ability to zoom in (cf. Fig. 3), and increasing file size.
#### References
- Oreshkin, Boris N., Dmitri Carpov, Nicolas Chapados, and Yoshua Bengio. “N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting.” In International Conference on Learning Representations, 2019.
- Lin, Shengsheng, Weiwei Lin, Wentai Wu, Feiyu Zhao, Ruichao Mo, and Haotong Zhang. “SegRNN: Segment Recurrent Neural Network for Long-Term Time Series Forecasting.” arXiv, August 22, 2023. https://doi.org/10.48550/arXiv.2308.11200.
- Wang, Shiyu, Haixu Wu, Xiaoming Shi, Tengge Hu, Huakun Luo, Lintao Ma, James Y. Zhang, and Jun Zhou. “TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting.” In The Twelfth International Conference on Learning Representations, 2024.

### Questions
Note: The most important questions are listed first.

1. What is meant by "multi-level characteristics of real-world time series" (Sec. 1)? How do the time series in Fig. 1 relate to each other? How are they combined (additively?)?
2. L. 299f states, "These models represent the latest advancements in multivariate time series forecasting and encompass all mainstream prediction model types". However, recurrent models such as SegRNN (Lin et al. 2023) and the empirically strong TimeMixer model (Wang et al. 2024) are missing. Was this a deliberate choice?
3. Regarding the Li Block (Sec. 3.2): Why is padding performed? Is the linear prediction in l. 221 the same as the (not very linear) MLP in Fig. 2? Which of the model components are learned via gradient descent?
4. Regarding Fig. 2: What is the "backbone"?
5. Regarding the No Block (Sec. 3.2): Again, MLP blocks are suddenly linear projections (matrix multiplications). If the addition in l. 238 is element-wise, isn't the overall $N_i^{TF}$  entirely linear up to the point of activation. How can it be beneficial over a simple linear layer? Why is Tanh chosen, given that ReLU is a more common choice today? I do not understand the motivation behind the construction in l. 239-250.
6. The iterative pattern extraction reminds me of N-BEATS (Oreshkin et al., 2019). Are they that closely related? If so, this might be relevant for Sec. 2.
7. What are the diagonal stripes in, for instance, Fig. 19 (bottom, left)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces LiNo, a Recursive Residual Decomposition framework for time series forecasting. LiNo addresses the limitations of existing deep learning models by extracting both linear and nonlinear patterns. The framework employs a Li block to capture linear patterns and a No block to model nonlinear patterns. This recursive and deeper-level decomposition enhances the extraction of complex, multi-granular patterns in real-world time series data. Experimental results on thirteen real-world benchmarks show that LiNo outperforms state-of-the-art models in both univariate and multivariate forecasting scenarios, providing robust and precise predictions.

### Strengths
1. In experimental evaluations, the proposed method surpasses state-of-the-art models in both univariate and multivariate forecasting scenarios.
2. The method is easy to understand.
3. This paper proposes an efficient method to capture the linear and nonlinear patterns for time series forecasting.

### Weaknesses
1. The components of the method, while effective, are not entirely novel. Recursive residual decomposition has been demonstrated to be effective in N-BEATS [1], and the utility of frequency-domain MLPs is highlighted in FreMLP [2]. Additionally, the channel mixing technique used in LiNo is similar to that used in SOFTS [3], and it would be beneficial to include a more detailed comparison and discussion of these similarities.
2. The authors argue that the primary distribution involves linear and nonlinear decomposition, with ablation studies primarily focused on multivariate time series forecasting. In line 428, they state, "Extracting nonlinear patterns, such as inter-series dependencies, temporal variations, and frequency information, is crucial for accurate predictions." The classification of inter-series dependencies as nonlinear patterns may be debatable, as methods like the Multivariate Autoregressive Model, which are inherently linear, can also capture such dependencies. It would be valuable to separately study the effects of the channel mixing method and the linear-nonlinear decomposition. The claimed superiority of the No block ablation, using iTransformer and TSMixer, which mainly attributes its performance to the channel mixing part, could benefit from further evidence (Table 5, Figure 4).
3. The paper lacks an error bar analysis. To demonstrate the robustness of the proposed method, the experiments should be conducted multiple times using different random seeds.
4. The paper contains a few minor typographical errors. For instance, on line 103, "TSMxier" should be corrected to "TSMixer," and on line 252, "ReVIN" should be changed to "RevIN."

[1] Oreshkin B N, Carpov D, Chapados N, et al. N-BEATS: Neural basis expansion analysis for interpretable time series forecasting[J]. ICLR, 2020.

[2] Yi K, Zhang Q, Fan W, et al. Frequency-domain MLPs are more effective learners in time series forecasting[J]. NeurIPS, 2023.

[3] Lu H, XY Chen, et al. SOFTS: Efficient Multivariate Time Series Forecasting with Series-Core Fusion. ArXiv, 2024.

### Questions
Please see the weaknesses above.

### Soundness
2

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
3

### Summary
It's a complex time series forecasting model incorporating recursive residual, frequency, and linear/non-linear designs

### Strengths
The numerical performance is relative good.

### Weaknesses
I'm concerned that the work resembles a LEGO model: it combines various components into a high-level narrative without detailed mapping. The motivation and underlying problem are weak. The ablation should focus on the concept of Recursive Residual Decomposition instead of individual components. Removing entire modules that result in extremely poor outcomes doesn't provide meaningful insights. It would be more effective to compare it with similar residual-based designs or variations to evaluate the overarching idea.

### Questions
Could you elaborate on the design choices for the complex components? Beyond being a complicated module featuring recursive, residual, frequency, and linear elements, what insights can we gain from your design?

### Soundness
3

### Presentation
2

### Contribution
2
