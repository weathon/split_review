# VMFTransformer: An Angle-Preserving and Auto-Scaling Machine for Multi-horizon Probabilistic Forecasting

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Time series forecasting has historically been a key area of academic research and industrial applications. As deep learning develops, the major research methodologies of time series forecasting can be divided into two categories, i.e., iterative and direct methods. In the iterative methods, since a small amount of error is produced at each time step, the recursive structure can potentially lead to large error accumulations over longer forecasting horizons. Although the direct methods can avoid this puzzle involved in the iterative methods, it faces abuse of conditional independence among time points. This impractical assumption can also lead to biased models. To solve these challenges, we propose a direct approach for multi-horizon probabilistic forecasting, which can effectively characterize the dependence across future horizons. Specifically, we consider the multi-horizon target as a random vector. The direction of the vector embodies the temporal dependence, and the length of the vector measures the overall scale across each horizon. Therefore, we respectively apply the von Mises-Fisher (VMF) distribution and the truncated normal distribution to characterize the angle and the magnitude of the target vector in our model. We evaluate the performance of our framework on three benchmarks. Extensive results demonstrate the superiority of our framework over six state-of-the-art methods and show the remarkable versatility and extensibility for different time series forecasting tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
1. This paper addresses the challenges in time series forecasting, specifically in multi-horizon probabilistic forecasting, by proposing a direct approach that effectively characterizes the dependence across future horizons. Technically, the authors consider the multi-horizon target as a random vector and apply the von Mises-Fisher (VMF) distribution and the truncated normal distribution to model the angle and magnitude of the target vector. 

2. The performance of the proposed framework is evaluated on three benchmarks, demonstrating its superiority over six state-of-the-art methods in different time series forecasting tasks.

### Strengths
1. The paper is well-written and exhibits clarity in its presentation. The visual results help to comprehend the proposed framework.
2. Authors propose a novel similarity measurement termed “Angle&Scale” similarity for the attention module and show that the Angle&Scale similarity outperforms the dot-product similarity in most cases in ablation studies.
3. The proposed VMFTransformer consistently outperforms all baselines in  MSE and q-risk.

### Weaknesses
1. The current version of the paper solely presents the average value obtained from five trials without including information about the standard deviation. It is highly recommended to include error bars.
2. Why use the VMF distribution and the truncated normal distribution to characterize the angle and magnitude of the target vector? The motivation behind this is unclear to me.
3. Metrics used to evaluate uncertainty are not sufficiently convincing,  a more commonly used metric, CRPS [1], was not used in the experiment.
4. Some probabilistic time series baselines are not compared with the proposed method in the experiment, such as TransMAF [2], [3].

### Questions
Please see my comments in Weaknesses.

I would also appreciate if the authors can respond, if they can, to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper contributes to time series forecasting by proposing a new model, the VMFTransformer, which tackles the inherent problems in iterative and direct forecasting methods. Iterative methods suffer from cumulative errors, and direct methods often incorrectly presume independence between future time points. The VMFTransformer addresses these issues by conceptualizing forecasts as random vectors, utilizing the von Mises-Fisher distribution to maintain temporal directionality and a truncated normal distribution for magnitude, accurately preserving time-dependent relationships. Benchmarked against several methods, the VMFTransformer demonstrates enhanced predictive performance, showing its effectiveness, and adaptability for a range of time series forecasting applications.

### Strengths
1. Error Accumulation Mitigation: Effectively addresses the issue of error accumulation inherent in iterative forecasting methods.


2. Temporal Independence: Overcomes the unrealistic assumption of temporal independence used by direct forecasting methods.


3. Directional Dependencies: Employs the von Mises-Fisher distribution to accurately capture the directional dependencies in time series data.


4. Magnitude Characterization: Utilizes a truncated normal distribution to model the magnitude of forecasts, enhancing predictive accuracy.

### Weaknesses
1. Lack of Recent Benchmarks: The VMFTransformer has not been compared with the most recent benchmarks such as PatchTST [1], or with most comparisons made against older methods. for instance please consider looking at recnet benchmarks provided by https://github.com/timeseriesAI/tsai


2. Limited comparison for different horizons: The scope of comparison is limited, which may not adequately reflect the model's performance across a broader range of forecasting scenarios.


3. Formatting Issues: There is room for improvement in the formatting of the equations, which could enhance readability and comprehension.


4. Presentation Clarity: The paper could better articulate the main contribution, as the current presentation may be challenging to follow, possibly obscuring the model's innovation.


5. Insufficient Experimentation: Without more extensive experimentation, it's difficult to ascertain the paper's meaningful contribution to the community and its practical applicability.

### Questions
Please consider the comments I provided above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
To mitigate the accumulation of forecast errors associated with the recursive strategy and the conditional assumption of the direct strategy, the authors propose a novel approach for multi-horizon probabilistic forecasting. This new strategy effectively captures the interdependence across future horizons by modeling the multi-horizon target as a random vector. The direction of this vector represents temporal dependence, while its length measures the overall scale across each horizon. The authors assume that the angle and magnitude of these vectors follow a von Mises-Fisher (VMF) and a truncated normal distribution, respectively. The authors conducted experiments on three benchmark datasets, including an ablation study, demonstrating the advantages of their proposed method over six state-of-the-art techniques.

### Strengths
- The paper addresses an important challenge in time series forecasting, providing new forecasting strategies for multi-horizon probabilistic forecasting.

- The approach of modeling the direction and length of future random vectors is innovative in the context of multi-horizon forecasting strategies.

- The proposed method is compared against multiple state-of-the-art methods.

### Weaknesses
 - The proposed method appears to be relatively complex, yet it does not seem to offer substantial improvements over simpler existing methods. Additionally, the motivations behind various design choices lack clarity in the paper.

	- The method involves intricate elements such as the Bessel function and modeling assumptions like the von Mises-Fisher and truncated normal distributions. The justification for these specific choices is not sufficiently detailed. For instance, the paper does not explore the sensitivity of the results to these distributional assumptions, nor does it compare them against simpler alternatives. The use of a truncated normal distribution for the magnitude, while perhaps intuitive, lacks a rigorous justification compared to other bounded distributions or even unbounded distributions with appropriate regularization.
	- In the field of time series forecasting, simpler methods often yield satisfactory results. The paper does not convincingly justify the necessity of such complexity in deep time series forecasting. The added complexity should be counterbalanced by a significant performance gain or a clear theoretical advantage, which is not evident in the current presentation. The authors should provide a more thorough analysis of the trade-offs between complexity and performance.
	- The authors should thoroughly discuss their modeling assumptions and their impact relative to alternative methods. For instance, why opt for a truncated normal distribution? Are there other alternatives? The paper should include a sensitivity analysis to assess the impact of this choice. Furthermore, the rationale behind incorporating a multi-head convolutional self-attention mechanism should be explained more clearly, including why this specific architecture was chosen over other alternatives and how it contributes to the overall performance.
	- While the authors aim to model interdependence across future horizons, they have not employed multivariate scoring rules to evaluate this aspect. The use of univariate scoring rules does not fully capture the benefits of modeling the joint distribution of future horizons. Multivariate scoring rules, such as the energy score or the continuous ranked probability score (CRPS) for vector-valued forecasts, would be more appropriate for evaluating the proposed method.
	- The paper asserts that recursive and direct strategies can yield high forecast errors, but it remains unclear how the proposed strategy compares with other forecasting approaches that use the same underlying model. A comparison with a direct or recursive strategy using the same base model would isolate the impact of the proposed multi-horizon strategy.

- Experiments:

	- The choice of only three datasets for experimentation raises questions, as many machine learning papers on time series forecasting examine more extensive benchmark datasets. For example, see the Monash Time Series Forecasting Archive (https://arxiv.org/abs/2105.06643). The limited number of datasets makes it difficult to generalize the findings and assess the robustness of the proposed method across different types of time series.

	- Many time series datasets exhibit a pronounced seasonal component that dominates the signal. Consequently, it may be challenging to surpass simpler methods that effectively estimate this seasonal component. The paper should address the strength of the seasonal component in the considered datasets. A detailed analysis of the autocorrelation structure of the datasets would be beneficial to understand the impact of seasonality.

	- The authors have not included simple benchmarks such as auto.arima or exponential smoothing in their comparisons. These methods are standard baselines in time series forecasting and should be included to provide a more comprehensive evaluation. The absence of these baselines makes it difficult to assess the practical relevance of the proposed method.

	- Learning curves should be provided to demonstrate the stability of the training procedure. The absence of learning curves makes it difficult to assess whether the model is converging properly and whether the reported results are reliable.

	- The proposed method is trained using maximum likelihood estimation. The authors should also provide the negative log-likelihood (NLL) for all density-based methods. Reporting the NLL would provide a more direct measure of the model's fit to the data and allow for a more detailed comparison of the density-based methods.

	- The authors did not report standard errors and information regarding the number of runs performed. The absence of standard errors and information about the number of runs makes it difficult to assess the statistical significance of the results and the robustness of the findings.

	- The results for specific forecast horizons (e.g., h = 1, 2, 3, etc.) should be reported to assess if the procedure increases forecast error for initial horizons while improving the average error across horizons. Reporting horizon-specific results would allow for a more detailed analysis of the method's performance across different forecast lengths and help identify potential trade-offs.

### Questions
- Refer to the "Weaknesses" section for questions.


	- Typos and Improvements:
		- Equation 6 is rimarily computing the logarithm of expression (5). For clarity, it may be better to move it to the appendix.
		- On page 6, the figure number is missing.
		- The sentence beginning with "It should be noted that in Equation equation 7," is not clear.
		- "the provide the proof." Furthermore, clarify that you are citing a reference and not presenting a proof.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a direct approach for multi-horizon probabilistic forecasting that characterizes the dependence across future horizons. The model treats the multi-horizon target as a random vector, using the von Mises-Fisher (VMF) distribution to characterize the direction and a truncated normal distribution for the magnitude. Additionally, it introduces the concept of "Angle&Scale" similarity to replace the traditional dot-product similarity in self-attention. The model's performance is evaluated on three datasets and shows superiority over some previous methods.

### Strengths
- The paper is well-written and easy to follow.
- The motivation behind modeling dependencies among future horizons is clearly articulated and logically sound.
- The idea of decoupling the target vector into angle and scale is both interesting and innovative.

### Weaknesses
 - Overall, this work proposes two orthogonal methods: and objective function based on VMF distribution and the “Angle&Scale” similarity to replace dot-product in self-attention. The motivation behind the latter is not as evident. The computation process, i.e. equations at the bottom of page 5, are confusing due to the misleading subscripts. And a figure for visualization is missing here.

- Baselines for comparison are somewhat outdated.

### Questions
- Could you provide a more detailed and clear explanation of the "Angle&Scale" similarity, specifically the shape of these matrices and computation process of variables $Z, Q, K, V$?
- As the objective and “Angle&Scale” similarity are orthogonal, the ablation stduy should compare four models: 1.VMF loss+Dot product; 2.VMF loss+Angle&Scale; 3.MSE loss+Dot product; 4.MSE loss+Angle&Scale. Please complete 3 and 4 to show the effectiveness of the proposed objective function.
- Please compare with some recent models, such as DLinear and PatchTST.
- Consider evaluating the speed and memory usage of the "Angle&Scale" similarity with the Dot-product method, as the constant terms in complexity analysis can significantly impact practical efficiency.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
