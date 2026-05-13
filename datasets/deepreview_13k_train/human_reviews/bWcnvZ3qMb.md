# FITS: Modeling Time Series with $10k$ Parameters

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
In this paper, we introduce FITS, a lightweight yet powerful model for time series analysis. Unlike existing models that directly process raw time-domain data, FITS operates on the principle that time series can be manipulated through interpolation in the complex frequency domain, achieving performance comparable to state-of-the-art models for time series forecasting and anomaly detection tasks.
Notably, FITS accomplishes this with a svelte profile of just about $10k$ parameters, making it ideally suited for edge devices and paving the way for a wide range of applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an impressive compact model, named FITS, for time series tasks, including forecasting and anomaly detection. FITS achieves manipulation to time series through interpolation in the frequency domain. The whole framework is quite simple and has remarkably few parameters. FITS achieves competitive performance to SOTA baselines on both forecasting and anomaly detection with about 50 times fewer parameters. With such impressive performance, the proposed model would have a certain impact on the community.

### Strengths
1. The experiment result is surprisingly good considering the tiny footprint of the model. The standard deviation of the error is very small which may indicate that the model is very stable because of its simplicity. 
2. Authors provide comprehensive ablation analysis to show light-weightness of the model and its superior performance across the hyper-parameters.
3. Authors use a synthetic dataset to show the key idea of FITS which is devide and conquer the different frequency. It also explained the effectiveness of the model on the AD task.

### Weaknesses
1. The result on anomaly detection is not remarkable. Especially on the SMAP and MSL dataset. Some more in depth analysis is needed to find out the reason. The model's performance on these datasets appears to be significantly lower than on others, suggesting a potential limitation in its ability to handle certain types of time series data. Specifically, it would be beneficial to explore whether the frequency domain approach is inherently less suitable for the characteristics of the SMAP and MSL datasets, which might exhibit more abrupt, non-periodic anomalies that are not easily captured by frequency analysis. Further investigation should be conducted into the nature of the data in these datasets, such as the prevalence of binary or categorical values, which could explain the model's difficulty in extracting meaningful features in the frequency domain.
2. Even though the FITS have far fewer parameters comparing to the DLinear, it still need more time to inference on the GPU (0.6 and 0.4 ms respectively). Does this mean the DLinear is still the best choice for the real-time application? The inference time difference, while seemingly small, could be significant in real-time applications where latency is critical. It's important to consider that while parameter count is a good proxy for model complexity, it does not always translate directly to inference speed. The computational overhead of the frequency domain transformations in FITS could be a contributing factor to the slower inference time. It would be valuable to explore the specific operations that contribute most to this overhead and consider whether optimizations are possible.

### Questions
1. How do author deploy the model on devices that do not support the complex computation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents FITS, a lightweight model designed for time series analysis. In contrast to conventional models that work directly with raw time-domain data, FITS operates within the complex frequency domain. It utilizes a streamlined linear layer and an efficient low-pass filter, achieving state-of-the-art performance in forecasting and anomaly detection tasks with a mere 10k parameters. FITS offers a novel perspective on these tasks, viewing them as interpolation exercises within the frequency domain. This approach extends time series segments for forecasting and reconstructing downsampled data. FITS employs a complex-valued linear layer to master amplitude scaling and phase shift, facilitating efficient complex frequency domain interpolation. Its compact size and competitive performance render FITS an excellent choice for edge devices, unlocking a wide array of applications in time series analysis.

### Strengths
The paper stands out for its clear and well-structured writing, making it easy to grasp the presented ideas. Addressing a critical issue, the paper tackles the challenge of developing time series analysis models suitable for deployment on resource-constrained edge devices, ensuring optimal performance. Furthermore, the paper impressively conducts a comprehensive evaluation. It includes a comparison with various state-of-the-art methods, even though these methods vastly differ in size from the proposed approach. The paper also introduces an efficient method for selecting the cutoff frequency, explores the impact of different lookback window sizes through ablation studies, and offers detailed insights into the training process. Notably, the approach ingeniously combines simple components such as RevIN, LPF, and the Complex-valued Linear layer to create a robust architecture that can be applied to industrial-grade time series analysis tasks.

### Weaknesses
The method's limitation lies in its inability to generate probabilistic forecasts, a crucial requirement for numerous industrial applications. Moreover, the evaluations conducted on benchmark datasets may not accurately reflect the real-world scenarios of edge devices. These benchmark datasets, such as those related to traffic and weather, typically do not require processing on edge devices and can be handled in offline settings. It remains uncertain how well the model will perform when applied to data from edge devices, like healthcare devices or industrial sensors, which present different challenges and requirements. Specifically, the lack of evaluation on datasets with high-frequency, noisy sensor data is a concern. The model's performance might degrade significantly when faced with the type of irregular sampling and signal corruption common in edge device applications. Furthermore, the linear interpolation in the frequency domain, while efficient, might oversimplify complex non-linear dynamics present in real-world time series data from edge devices. This could limit the model's ability to capture intricate patterns and make accurate predictions in such scenarios.

### Questions
Did you try fitting a larger neural network for frequency interpolation task? It would be interesting to see if the performance of this architecture scales with the size.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a parameter-efficient model architecture for time series anomaly detection and forecasting. The model's pipeline consists of the Fourier transform of the original time series, followed by a low-pass filter in the freq. domain, a linear layer (complex-valued), padding, and the inverse transform to map back into the time domain. For forecasting, the result of the inverse transform can be used directly, while for anomaly detection, a reconstruction error threshold, which increases the F1-score, is determined on the validation set. The authors show competitive performance on various benchmark data sets.

### Strengths
The manuscript is well-organized and clearly written. I appreciate the preliminary section, which is very instructive. The experimental evaluation is thorough, and many competing methods are compared in a rigorous manner. Lastly, I appreciate the different ablation studies the authors performed. Overall, the results are convincing, and I believe the proposed method sets a great benchmark for such a parameter-efficient method.

### Weaknesses
The presentation of FITS could be more comprehensive (more details in the questions). Furthermore, I would like to see more "basic" baselines (e.g., ARIMA, DeepAR for forecasting, and Random Cut Forest for Anomaly detection). To further substantiate the claims about performance (and to put them on a statistically sound foundation), a critical difference plot[1] may be a useful analysis tool. Lastly, the method employs several heuristics that need to be tuned in the real world, a drawback it shares with other methods.

### Questions
* Can you explain why $x(t-\tau)$ is a shift forward in time, rather than backward?
* Can you add a more thorough caption to Fig. 2? As it stands, it is not comprehensible enough to fully understand your method. Is it just a single linear layer/what is the output dimension? What are the typical dimensions of $\tilde{X}$? Are (i)RIN and (i)rFFT performed in parallel or sequentially? Please elaborate more on how RIN works, either in the Figure or its caption. 
* Have you experimented with more sophisticated layers than just linear? 
* What is the back-casting task, and how is it used in training?
* Can you motivate in 1-2 sentences why the output length needs to be controlled (Section 3.3)?
* You say the LPF discards components beyond the model's learning capabilities. What do you mean by this? The model's capabilities are independent of the signal, and high frequencies are not always noise or irrelevant. It seems domain-specific. Furthermore, you say high-frequency components such as trends are filtered out. First, trend signals can be low-frequency, and second, they are particularly important in the forecasting realm.
* The method is particularly interesting because of its parameter-effectiveness. Can you perform experiments on real-time inference time on simple hardware (not necessarily edge devices) to substantiate this (e.g., real-time anomaly detection)? What are the challenges regarding domain shifts and refitting, and how could they be addressed? This could substantially improve the focus and contribution of the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Modern time series forecasting methods are heavily-parametrised, and in spite of their compelling performance on benchmark datasets, may not be appropriate in resource-constrained settings. In the spirit of recent work leveraging representations of time series in the frequency domain, the authors propose a new methodology that captures amplitude and phase information using a real-valued neural network. A low-pass filter is also included to further reduce the size of the model. An extensive experimental evaluation demonstrates how model performance is comparable (and sometimes better) to other SOTA techniques while also having orders of magnitude less parameters. The suitability of the model to anomaly detection via time series reconstruction is also validated on a variety of datasets.

### Strengths
- The reduction in model size enabled by the proposed architecture is commendable, and the minor trade-off with predictive performance (if any at all in some cases) makes this a compelling model for practitioners working with time series forecasting models.
- The paper is well-written and nicely structured. Although there has been a recent resurgence in interest on how analysis in the frequency domain can be applied to forecasting, the authors adequately position this paper in the context of related work.
- The experimental evaluation is extensive, and I especially appreciated the extension to anomaly detection, which is one of the more common downstream tasks stemming from time series forecasting. The insights on why the model works better on some datasets than others (e.g. citing the binary nature of some time series, as well as overall limitations with benchmarks in the field) was also appreciated.

### Weaknesses
 - There are quite a few bits and pieces to the model pipeline, and at times the extent to which each component contributes towards overall performance is unclear. Specifically, the interaction between the low-pass filter, the real-valued neural network for amplitude and phase, and the interpolation rate is not fully explored. It would be beneficial to understand how much each of these components contributes to the final performance, and whether some components are more critical than others for different types of time series. For example, do time series with higher frequency components benefit more from the low-pass filter, or does the interpolation rate have a larger effect on time series with lower frequency components?
- The concluding remarks of the paper focus on a few settings where the method may not be most appropriate, but I would have liked to see broader thoughts on future work, such as further reductions to model size, and possibly interpretability. While the paper acknowledges limitations, a discussion on potential avenues for future research, such as exploring complex-valued networks or attention mechanisms, would add further value. Furthermore, the paper could benefit from a discussion on model interpretability, particularly in understanding which frequency components are most important for different time series.
- While I appreciated the experiment on anomaly detection, this is a field of study where (as referenced by the authors themselves), a few metrics may not be sufficient for fully capturing the success of different techniques. There is consequently a risk that the experiment featured here might not be sufficiently conclusive. The use of simple metrics like precision and recall, while common, might not fully capture the nuances of anomaly detection, especially in time series data. For example, the model's ability to detect anomalies of different magnitudes or durations is not fully explored.

### Questions
Please refer to comments in the section on *Weaknesses* as a guide for the rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
