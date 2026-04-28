# TILDE-Q: A Transformation Invariant Loss Function for Time-Series Forecasting

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Time-series forecasting has gained increasing attention in the field of artificial intelligence due to its potential to address real-world problems across various domains, including energy, weather, traffic, and economy. While time-series forecasting is a well-researched field, predicting complex temporal patterns such as sudden changes in sequential data still poses a challenge with current models. This difficulty stems from minimizing $L_p$ norm distances as loss functions, such as mean absolute error (MAE) or mean square error (MSE), which are susceptible to both intricate temporal dynamics modeling and signal shape capturing. Furthermore, these functions often cause models to behave aberrantly and generate uncorrelated results with the original time-series. Consequently, the development of a shape-aware loss function that goes beyond mere point-wise comparison is essential. In this paper, we examine the definition of shape and distortions, which are crucial for shape-awareness in time-series forecasting, and provide a design rationale for the shape-aware loss function. Based on our design rationale, we propose a novel, compact loss function called \toolname (Transformation Invariant Loss function with Distance EQuilibrium) that considers not only amplitude and phase distortions but also allows models to capture the shape of time-series sequences. Furthermore, \toolname supports the simultaneous modeling of periodic and nonperiodic temporal dynamics. We evaluate the efficacy of \toolname by conducting extensive experiments under both periodic and nonperiodic conditions with various models ranging from naive to state-of-the-art. The experimental results show that the models trained with \toolname surpass those trained with other metrics, such as MSE and DILATE, in various real-world applications, including electricity, traffic, illness, economics, weather, and electricity transformer temperature (ETT). Dealing with drastic changes, temporal patterns, and shapes in sequential data, which is hardly predicted using existing models, is a critical issue. This is because most time-series forecasting methods aim to minimize $L_p$ norm distances as loss functions, such as mean absolute error (MAE) or mean square error (MSE). These loss functions are vulnerable to not only considering temporal dynamics modeling but also capturing the shape of signals. In addition, these functions often make models misbehave and return uncorrelated results to the original time-series. An effective loss function must be invariant to the set of distortions between two time-series data instead of just comparing the exact values. In this paper, we propose a novel loss function called \toolname (Transformation Invariant Loss function with Distance EQuilibrium), which not only considers distortions in amplitude and phase but also allows models to capture the shape of time-series sequences. In addition, \toolname supports simultaneous modeling of periodic and nonperiodic temporal dynamics. We evaluate the effectiveness of \toolname by conducting extensive experiments with respect to periodic and nonperiodic conditions of data, from naive models to state-of-the-art models. The experimental results indicate that the models trained with \toolname outperform those trained with other metrics (e.g., MSE, dynamic time warping (DTW), temporal distortion index (TDI), and longest common subsequence (LCSS)).
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A shape aware loss function, TILDE-Q, is introduced to capture distortios between time-series signals. TILDE-Q aims to be invariant to shift and scale distortions, both in space and time, to capture, e.g., shifts in phase and amplitude. Compared to traditional losses, such as MSE and DILATE, the proposed TILDE-Q loss helps various models to generate more accurate predictions on numerous datasets.

### Strengths
_Originality:_ The conducted analysis reveals relevant aspekts for time-series forecasting and the proposed method seems to reasonably compensate the limitations of conventional loss functions. You may want to add temporal convolution networks (TCN) from [Lea et al. (2016)](https://link.springer.com/chapter/10.1007/978-3-319-49409-8_7) and [Kalchbrenner et al. (2016)](https://arxiv.org/abs/1610.10099) to your related work section. Otherwise, the manuscript adequately cites related work.

_Quality:_ The writing, presentation, and demonstrations are well approachable and claims are properly supported by exhaustive experimental results. Some comments about limitations of TILDE-Q would be highly appreciated.

_Clarity:_ The organization of the manuscript is appealing and the arguments are well presented and iteratively constructed. In general, the manuscript provides the necessary information to understand the core message and to follow the clear line of argumentation.

_Significance:_ Results demonstrate the effectiveness of the proposed method and have the potential to provide valuable insights to the time-series forecasting community. Given the computational overhead is not too large, the proposed loss could evolve to an alternative to traditional loss functions, especially replacing MSE.

### Weaknesses
1. Improvements often seem to be marginal only (even though the score in a metric does not necessarily correlate with the actual quality of the qualitative forecast). Since you report that 10 models were trained, it would be easier to assess the loss quality if you provide error variations in form of $\sigma$ scores. The lack of these variations makes it difficult to determine if the observed improvements are statistically significant or simply due to random fluctuations in the training process. Furthermore, it is unclear if the reported improvements are consistent across different datasets and model architectures, or if they are specific to certain scenarios. A more detailed analysis of the variance in performance is needed to fully evaluate the robustness of the proposed loss function.
2. Given the various computations required to calculate the TILDE-Q loss, it is unclear how much computational overhead the method introduces and whether the benefits outweigh and justify the increased time complexity. Specifically, the manuscript does not provide a detailed breakdown of the computational cost associated with each step of the TILDE-Q calculation, making it difficult to assess its practical applicability in real-world scenarios. Without a clear understanding of the computational burden, it is challenging to determine if the potential gains in accuracy justify the additional resources required.

### Questions
1. Could TILDE-Q serve as a performance measure itself too? The challenge of quantifying the skill of a time-series forecast is ubiquous. If the TILDE-Q score matches closely with visual inspections, this would be agreat metric as well. It would be a great outcome, if the judgement of subjects on the similarity of two time-series would correlate strongly with TILDE-Q.
2. Inspecting the qualitative results in the appendix, can you formulate situations in which TILDE-Q performs poorly (consistently)?

### Soundness
3 good

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
This work investigates distortion handling in time series forecasting problems, specifically introducing a novel loss function to guide models in considering amplitude, phase, and uniform amplification shifting invariance.

### Strengths
1. The related work is comprehensive and shows a thorough analysis of different time series distortions.

### Weaknesses
1. It appears that the authors did not provide the complete version of the paper, as the appendices are missing.
2. The experiments lack recent time series forecasting models.
3. The experiments are not complete.
4. The experiments lack detailed analysis.

### Questions
The paper is not complete since some important appendices related to experiments are missing.
1. I'm interested in seeing additional results using TILDE-Q on recent time series forecasting models, including NLinear, DLinear, Scaleformer, PatchTST, Depts, N-hits, and SCINet.
2. More in-depth analysis of the primary results are expected.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a new loss function for time series forecasting models, TILDE-Q. TILDE-Q is a combination of three terms designed to penalize predictions while preserving invariance to one specific "distortion" (each): amplitude shifting (constant value shifting), phase shifting (constant translation), and amplitude scaling.

### Strengths
The method is well-motivated and intuitive, and the evaluation is thorough, including most common deep learning time series baseline methods and tasks.

### Weaknesses
My main reservations with this work are limited novelty (softmax and frequency domain losses are arguably the most basic type of objective in forecasting), and the work does not spend any time on the analysis of the proposed method, or on providing further insights. As an example, comments about softmax-ratios being invariant to constant shifts could be expanded with additional results, or providing a discussion on other ways to achieve invariance to constant scaling. The same goes for the caveats related to computing a loss in frequency domain (Sec 4.2, paragraph 2) and choice of dominant Fourier coefficients, which is not at all trivial in practice, especially for varied datasets.

I don't see how the softmax loss can satisfy your eq (1) requirement; the optimal solution where $d(y_i, \hat y_i) = k$ will result in a non-zero $\mathcal{L}_{a,shift}$. Could the authors clarify on how the softmax helps strengthen value shift invariance?

How do you choose the dominant frequency-domain coefficients for $\mathcal{L}_{phase}$? Does regularizing "non-dominant" frequencies for noise robustness help in practice? How do you deal with the fact that time series are finite-length signals (and there could be boundary effects)?

How do you choose $\alpha$ and $\gamma$? Why stop at three terms in the loss function? Did you empirically find these distortions to be most common in the datasets of interest?

It would have been valuable to carry out an analysis and see how common these distortions are in the datasets you evaluate on. It is difficult to assess significance otherwise (other than looking at the aggregate metrics)

### Questions
* I don't see how the softmax loss can satisfy your eq (1) requirement; the optimal solution where $d(y_i, \hat y_i) = k$ will result in a non-zero $\mathcal{L}_{a,shift}$. Could the authors clarify on how the softmax helps strengthen value shift invariance? 
*  How do you choose the dominant frequency-domain coefficients for $\mathcal{L}_{phase}$? Does regularizing "non-dominant" frequencies for noise robustness help in practice? How do you deal with the fact that time series are finite-length signals (and there could be boundary effects)?
* How do you choose $\alpha$ and $\gamma$? Why stop at three terms in the loss function? Did you empirically find these distortions to be most common in the datasets of interest? 
* It would have been valuable to carry out an analysis and see how common these distortions are in the datasets you evaluate on. It is difficult to assess significance otherwise (other than looking at the aggregate metrics)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed a loss function to account for distortions in the time series data. In particular, the loss function is designed to account for the amplitude and phase shifting in the prediction. The authors performed extensive numerical experiments to demonstrate advantages of the proposed method.

### Strengths
It looks relatively easy to apply the proposed method to improve existing time series models.  The authors performed extensive experiments using various combinations of the model and the proposed loss function.

### Weaknesses
The proposed loss function only deals with the amplitude and phase shifts in the prediction, unlike the various types of distortions described in the manuscript. The level of novelty and robustness of the manuscript seem below the standard of ICLR. Please, see the questions below.

Major concerns:

1. The amplitude shifting loss seems not optimal for noisy time series data, which is almost all time series of interest. The MSE loss aims to estimate the expectation of the probability distribution of the time series, which is the optimal solution, while the amplitude shifting loss always introduces a bias so that the prediction is always above or below of the noisy signal.

2. Similar to question 1, in many cases, the amplitude shifting loss will compete against the standard MSE loss. For some problems, MSE loss will be optimal and, for the other cases, probably the amplitude shifting loss makes sense. However, how to decide which one to use?

3. The Fourier loss makes a much more sense than the amplitude shifting loss. It will capture the periodicity of the time series data. Recently, it has been shown in many studies that capturing a periodicity is a key element in time series forecasting. However, the authors should elaborate how they compute the Fourier coefficients. For example, when if the signal is not periodic, the Fourier series do not converge, meaning it is difficult to truncate the Fourier series. So, deciding the dominant frequency is non-trivial. What's the theoretical reason to choose $\sqrt{T'}$ to truncate the Fourier seires?

4. The loss based on the auto-correlation also makes a sense. However, I don't fully understand the explanation of the weakness of the Fourier loss. The authors explained three reasons why the Fourier method fails to represent the characteristics of the time series. But all of the three reasons exactly apply the same for the auto-correlation function. As the authors explained, if the time series is non-stationary, the auto-correlation also keeps changing, like the Fourier series. As a matter of fact, auto-correlation and Fourier series are like two sides of a coin. 

5. What's the logic behind of the structure of the loss function in (7)? Why is $L_{phase}$ grouped with $L_{shift}$? And $L_{amp}$ is separate?

6. It may be interesting to compare the results with DLinear (https://arxiv.org/pdf/2205.13504.pdf), where they proposed a very simple linear model with trend and seasonality decomposition, which should be similar to the loss functions proposed.

### Questions
Major concerns:

1. The amplitude shifting loss seems not optimal for noisy time series data, which is almost all time series of interest. The MSE loss aims to estimate the expectation of the probability distribution of the time series, which is the optimal solution, while the amplitude shifting loss always introduces a bias so that the prediction is always above or below of the noisy signal. 

2. Similar to question 1, in many cases, the amplitude shifting loss will compete against the standard MSE loss. For some problems, MSE loss will be optimal and, for the other cases, probably the amplitude shifting loss makes sense. However, how to decide which one to use?

3. The Fourier loss makes a much more sense than the amplitude shifting loss. It will capture the periodicity of the time series data. Recently, it has been shown in many studies that capturing a periodicity is a key element in time series forecasting. However, the authors should elaborate how they compute the Fourier coefficients. For example, when if the signal is not periodic, the Fourier series do not converge, meaning it is difficult to truncate the Fourier series. So, deciding the dominant frequency is non-trivial. What's the theoretical reason to choose $\sqrt{T'}$ to truncate the Fourier seires?

4. The loss based on the auto-correlation also makes a sense. However, I don't fully understand the explanation of the weakness of the Fourier loss. The authors explained three reasons why the Fourier method fails to represent the characteristics of the time series. But all of the three reasons exactly apply the same for the auto-correlation function. As the authors explained, if the time series is non-stationary, the auto-correlation also keeps changing, like the Fourier series. As a matter of fact, auto-correlation and Fourier series are like two sides of a coin. 

5. What's the logic behind of the structure of the loss function in (7)? Why is $L_{phase}$ grouped with $L_{shift}$? And $L_{amp}$ is separate?

6. It may be interesting to compare the results with DLinear (https://arxiv.org/pdf/2205.13504.pdf), where they proposed a very simple linear model with trend and seasonality decomposition, which should be similar to the loss functions proposed.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
