# Multi-Resolution Decomposable Diffusion Model for Non-Stationary Time Series Anomaly Detection

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Recently, generative models have shown considerable promise in unsupervised time series anomaly detection. Nonetheless, the task of effectively capturing complex temporal patterns and minimizing false alarms becomes increasingly challenging when dealing with non-stationary time series, characterized by continuously fluctuating statistical attributes and joint distributions. To confront these challenges, we underscore the benefits of multi-resolution modeling, which improves the ability to distinguish between anomalies and non-stationary behaviors by leveraging correlations across various resolution scales. In response, we introduce a **M**ulti-Res**o**lution **De**composable Diffusion **M**odel (MODEM), which integrates a coarse-to-fine diffusion paradigm with a frequency-enhanced decomposable network to adeptly navigate the intricacies of non-stationarity. Technically, the coarse-to-fine diffusion model embeds cross-resolution correlations into the forward process to optimize diffusion transitions mathematically. It then innovatively employs low-resolution recovery to guide the reverse trajectories of high-resolution series in a coarse-to-fine manner, enhancing the model's ability to learn and elucidate underlying temporal patterns. Furthermore, the frequency-enhanced decomposable network operates in the frequency domain to extract globally shared time-invariant information and time-variant temporal dynamics for accurate series reconstruction. Extensive experiments conducted across five real-world datasets demonstrate that our proposed MODEM achieves state-of-the-art performance and can be generalized to other time series tasks. The code will be publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce a multiscale diffusion model for anomaly detection in non-stationary time series that relies on combining representations of the time series at multiple temporal resolutions.

### Strengths
- The paper is well written, mathematically sound and clearly formulates subcomponents of the method. 

- The experimental evaluation and comparisons are rather extensive.

### Weaknesses
 - My main concern centres around hyperparameter settings for which the authors claim to follow empirical tuning with Bayesian selection without providing further details. I understand the difficulties stated by the authors in properly tuning the large number of hyperparameters; however without an objective method for setting parameters based on training data alone it is not clear whether the selected parameter settings will generalise well to other datasets. Here, the authors should at least provide some analysis of how sensitive the results are to variations of individual parameter values by keeping the rest of the parameters at their suggested values. 
- The resolution parameter R is set to a rather low value of 4 in the experiments and hence covers only a narrow range of resolutions which seems contrary to the overall claim of the authors that the method leverages correlations across various resolution scales. 
- The method seems to be mainly improving on the recall value while trailing behind interns of precision, sometimes significantly, compared to other methods. I believe further clarification of this tradeoff in practical scenarios is needed.  
- The authors should provide more details on the pooling operation in the MRD sampler.
- No code is provided which makes proper assesment of the experimental results and method difficult.

### Questions
- see Weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, authors design a modal named MODEM（Multi-Resolution Decomposable Diffusion Model）for anomaly detection in non-stationary time series data. The proposed model integrates a coarse-to-fine diffusion paradigm with a frequency-enhanced decomposable network to enhance the modal’s ability of handing the non-stationary time series data. Through this approach, the proposed model allows for utilizing the multiple resolutions information of non-stationary time series data, which varies for each datasets.

### Strengths
1)The proposed method MODEM is novel , it can utilize the multiple resolutions information of non-stationary time series data to improve the modal’s ability of anomaly detection.

2)The authors conducted experiments on diverse datasets, and their proposed method demonstrated excellent performance.

3)The authors presented a clear exposition of their research motivation and proposed solution. The analyze of difference between low-resolution time series and high-resolution time series helps understand the effect of the proposed modules.

### Weaknesses
1)While the model achieved the best F-score performance due to higher recall values, its precision values were comparatively lower than other models (Table 3). The authors should explain this observation.

2)There is no comparison of computational cost(# of params, Gflops...) compared to existing models, while the diffusion model is extended into a multi-resolution paradigm, leading directly to an R-fold increase in the number of sampling steps.

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

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
The paper introduces a novel Multi-Resolution Decomposable Diffusion Model (MODEM), designed for unsupervised non-stationary time-series anomaly detection. It addresses the challenge of capturing complex temporal patterns in non-stationary data by leveraging multi-resolution modeling. MODEM employs a coarse-to-fine diffusion process to handle cross-resolution correlations, improving anomaly detection and time-series reconstruction. A frequency-enhanced decomposable network in MODEM extracts both global and time-variant dynamics. Extensive experiments across five real-world datasets demonstrate its superior performance.

### Strengths
The paper is well-organized with clear writing and visualization. The experiments are comprehensive.

### Weaknesses
1.	Considering the FFT process and the multi-resolution, it may cast a concern on the training time and the computational complexity, which are not sufficiently discussed in the paper, since ADD seems to be a metric for responsiveness of the method, not its computational efficiency.

2.	In addition to reconstructed-based and forecasting-based methods, there are also some density-based methods can be discussed [1,2].

### Questions
1.	Regarding the ablation study, for SMD, increasing R from 1 to 4 improves the performance in Figure 4. Does this generalize to other datasets? For datasets with many short-lasting anomalies (spanning only a few time points), would these anomalies only be captured in high-resolution data? If so, the utility of low-resolution data in such cases remains questionable.

2.	Is the time series in Figure 1 are real-world data? If so, which domain does the data belong to, and do similar time series challenges appear across other domains?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MODEM, a conditional diffusion model for non-stationary time series anomaly detection that incorporates (1) frequency-enhanced decomposable network, (2) multi-resolution guidance and (3) contextualized (cross-scale contextual) diffusion. The underlying network consists of two parallel encoders using residual Transformer and dilated ModernTCN blocks respectively, while a frequency decomposition module is built to disentangle time-invariant and time-variant components. Empirical studies on a variety of datasets show that this coarse-to-fine diffusion framework achieves good reconstruction performance and captures the key information in the non-stationary data, while ablations show that the specific design of the MODEM outperforms reasonable alternatives.

### Strengths
- The paper is well-structured and the main ideas are clearly presented. The figures and supplementary details are relevant and informative.
- To my best knowledge, this is the first work to introduce a multi-granularity mechanism into time series anomaly detection. The same applies to the contextualized forward and reverse conditional diffusion processes.
- The approach is studied through a broad set of experiments that show it consistently outperforms recent, relevant competitor methods in terms of some standard quality metrics for both real-world and non-stationary time series anomaly detection. The additional experiments are conducted, e.g. multivariate time series forecasting and imputation, despite being relatively weak.
- This paper also provides a series of ablation experiments to test the effect of each important choice.

### Weaknesses
1. The novelty of the proposal is somehow modest overall. The main body of the proposed method is like a stack of existing works (framework $\rightarrow$ CONTEXTDIFF [1], Top-K iFFT $\rightarrow$ ETSFormer [2], network $\rightarrow$ ModernTCN [3] and D$^3$R [4], multi-resolution $\rightarrow$ MG-TSD [5]), although applying algorithms from different tasks (text-to-image, prediction) to a new task (anomaly detection) can also be seen as a valid contribution.
2. The content of Section 3.3 with theoretical  derivation is very similar to CONTEXTDIFF [1], where the difference is just *coarse-resolution sequence $\leftarrow$ text (condition)* and *high-resolution sequence $\leftarrow$ image (target)*. However, the authors did not clearly tell this point in their paper where the proper citation is not given. In particular, the entire paper cites [1] in `Section 3.3 Multi-Resolution Forward Process` for only once (in an inconspicuous place), and [1] is completely omitted in the theoretical results in Appendix A. I understand that these sections make the paper more solid, but I suggest the authors emphasize contributions of the prior work when necessary. 
3. Although important works in the field of anomaly detection are analyzed in Section 2, there are some other diffusion-based approaches that should be included, such as related conditional diffusion model [1], diffusion model for time series [5,6] and so on.

### Questions
1. See the "Weaknesses" section.
2.  From `Section 3.2 Multi-Resolution Data Sampler`: "This strategy enables our model to learn the evolutionary characteristics of non-stationary time series across multiple resolutions, ... "  $\rightarrow$ This statement describes multi-resolution as the contributor of non-stationary time series learning, but how does this facilitation occur ?
3. The computational cost is a concern of diffusion models, especially under real-time anomaly detection. Therefore, comparison of the efficiency of different methods (diffusion and non-diffusion) is of great interest. Can the authors provide more accurate estimates w.r.t. benchmarks within a reasonable time and parameters ?
4. As far as I know, TSDiff was developed for univariate time series generation. Can the authors give more details of your changes in its original paper ?

### Soundness
2

### Presentation
3

### Contribution
2
