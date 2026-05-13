# CaPulse: Detecting Anomalies by Tuning in to the Causal Rhythms of Time Series

- Decision: Reject
- Scores: 3, 5, 5, 8

## Abstract
Time series anomaly detection has garnered considerable attention across diverse domains. While existing methods often fail to capture the underlying mechanisms behind anomaly generation in time series data. In addition, time series anomaly detection often faces several data-related inherent challenges, i.e., label scarcity, data imbalance, and complex multi-periodicity. In this paper, we leverage causal tools and introduce a new causality-based framework, **CaPulse**, which *tunes in* to the underlying *causal pulse* of time series data to effectively detect anomalies. Concretely, we begin by building a structural causal model to decipher the generation processes behind anomalies. To tackle the challenges posed by the data, we propose Periodical Normalizing Flows with a novel mask mechanism and carefully designed periodical learners, creating a periodicity-aware, density-based anomaly detection approach. Extensive experiments on seven real-world datasets demonstrate that CaPulse consistently outperforms existing methods, achieving AUROC improvements of 3% to 17%, with enhanced interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an anomaly detection framework that combines several existing algorithmic building blocks, including normalized flows, FFTs, and patch-based masking. The overall objective is to maximize the log-likelihood, which appears to produce a latent representation attributed to causal factors.

### Strengths
The paper makes an effort to integrate multiple algorithmic building blocks into a learning system.

### Weaknesses
It seems that the learning problem could benefit from a clearer explanation. The objective function appears to be conditioned by $ C_\text{ind} $ and $C_0$, but the criteria for selecting these values are not immediately obvious. This aspect is essential, especially when considering unsupervised learning tasks with latent variables. It is possible that a two-stage optimization strategy, where $C$ parameters and other model parameters are optimized in an alternating fashion, has been implemented, though a detailed description of this approach does not seem to be readily available. At the very least, it would be helpful if the parameters to be learned were clearly specified.

In my attempt to understand the algorithm’s operation and the rationale behind its design choices, I encountered a few challenging aspects. These include, for example, the use of FFT in Eq. (1), the orthogonality condition on $ C_\text{ind} $ and its connection to causal learning, and the role of the "pyramid" structure, which may be intended for multi-scale convolution across spatial and temporal dimensions. There are various possible approaches for identifying independent causal factors or periodic patterns at different granularities. In general, a well-written paper typically provides some technical rationale when selecting a specific approach. At present, there appears to be a slight disconnect between the authors’ intended objectives and the selected algorithmic components. For instance, it remains somewhat unclear why the resulting subspaces would lend themselves to causal interpretation or how the noise injection approach contributes to distinguishing confounders.

Given these considerations, I find it somewhat challenging to fully assess the framework’s novelty at this stage. I am inclined to suggest that additional development and clarification may be beneficial for the paper to reach its full potential for publication.

### Questions
Please address what described in weakness.

### Soundness
2

### Presentation
1

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
The paper proposes CaPulse a method for time series anomaly detection that leverages causal inference. It introduces a structural causal model to understand anomaly generation, combines it with periodical normalizing flows for density estimation. The paper purports to address key challenges including label scarcity, data imbalance, and multiple periodicities.

---

Update: I appreciate the author's rebuttal that addressed a lot of my concerns, in particular around baselines, evaluation, and benchmarks. However, I agree with professor Keogh's point regarding the mischaracterization of MP and fail to understand the author's statement that "MP-based methods fall outside the primary scope of our paper" and that the focus of the paper in on Deep-learning. This does not appear to be the initially defined scope of the paper.

### Strengths
The paper's main strength is its integration of causal inference with time series anomaly detection and proposed solution for handling multiple periodicities. This method offers some degree of interpretability through SHAP. The authors do establish strong theoretical foundation for their method.

### Weaknesses
In my view the main weakness is with the empirical evaluation. The proposed method is extremely complex, likely computationally demanding with a large number of hyperparameters. The authors do perform some sensitivity analysis but it is limited. The baselines used for the empirical comparison relies exclusively on similarly complex baselines. The authors do not compare to simple, algorithmic baselines or methods such as Matrix Profile which have proven to outperform state of the art at a computational cost several orders of magnitude smaller. Without such comparisons, it is impossible to assess whether the complexity of the method is justified.

### Questions
How does the computational complexity scale with time series length and dimensionality?
What are the computational requirements during training and inference?
How is the optimal hyperparameter configuration (Appendix E) for each dataset established?
Can you provide a comparison with more parameter-efficient baselines?

### Soundness
2

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
The paper proposes a structural causal model (SCM) to understand the generation process of anomalies in time series data. CaPulse leverages causal tools to identify the true underlying causes of anomalies, enhancing interpretability and generalization capabilities. Additionally, it employs Periodical Normalizing Flows (PeNF) with a novel mask mechanism and attention mechanism to capture multi-period dynamics. This enables the model to effectively address the challenges of label scarcity, data imbalance, and complex multi-periodicity in TSAD.

### Strengths
S1. Time series anomaly detection is important to various domains.

S2. There are quite a few nice illustrations.

S3. This work focuses on an important problem that could have real-world applications.

S4. The figures and tables used in this work are clear and easy to read.

### Weaknesses
W1. The paper conducts ablation experiments solely on two datasets, as shown in Table 2. This narrow focus raises concerns about the generalizability of the findings. A more comprehensive analysis involving additional datasets, particularly those with different characteristics (e.g., varying anomaly frequencies, noise levels, and data dimensionality), could provide valuable insights into the method's performance and limitations. For example, datasets with more complex temporal dependencies or higher levels of noise could reveal potential weaknesses in the proposed approach that are not apparent in the current evaluation.

W2. The approach presented appears to lack novelty, as it primarily builds upon established methods of causal inference and frequency domain analysis without offering significant advancements. The paper combines existing techniques such as structural causal models and normalizing flows, but does not introduce any novel theoretical insights or methodological innovations. Instead of innovating, the proposed method seems to merely combine existing techniques, and the specific way these are combined does not seem to present a significant departure from existing approaches.

W3. The comparative analysis in Table 1 is limited, as the authors do not engage with the most advanced and relevant methods currently available in the literature. The selection of baseline models is inadequate, as it overlooks several cutting-edge techniques that could offer a more rigorous benchmark. For instance, recent deep learning-based anomaly detection methods that incorporate attention mechanisms or graph neural networks are absent from the comparison. To strengthen their evaluation, the authors should include comparisons with a wider array of state-of-the-art anomaly detection algorithms, thereby providing a clearer context for assessing the performance of their proposed method. The current baselines do not adequately represent the current state of the art in time series anomaly detection.

### Questions
Q1: Why were ablation experiments only conducted on two datasets in Table 2, and what were the effects on the other datasets?

Q2: Causal inference and frequency domain-based methods have already been proposed before. Your method doesn’t seem to have anything novel compared to existing methods. It seems like you are just combining them.

Q3: In Table 1, the methods you compare with are not the best current methods. There is a lack of comparison with the latest methods.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposed CaPulse, which is a new causality-based framework for time series anomaly detection. The framework includes PaCM, MpCF moduls for causal treatment and multimple periodicities. This approach is periodicity-aware and density-based anomaly detection. Unlike traditional approaches that may fail to capture the underlying mechanisms of anomaly generation, CaPulse builds a structural causal model to understand the root causes of time-series anomalies. The experiments show better accuracy and interpretability than exiting methods.

### Strengths
- The CaPulse framework presents a novel approach to time-series anomaly detection by introducing causal inference. In this point, this work is different from traditional deep learning-based methods.
- Another innovative aspect is the introduction of Periodic Normalizing Flows(PeNF) with a mask mechanism for periodicity awareness. This approach is particularly well-suited for time series with complex multi-periodicity, enhancing both anomaly detection performance and interpretability.
- This paper provides empirical evidence to support the claims, with interpretability analysis.

### Weaknesses
 - From section 3, a causal view of TSAD includes hard assumptions that might not hold in various real-world settings.
- The limited number of baselines and benchmark datasets.
- There is no friendly explanation for the interpretability plot, especially in Figure 7.

### Questions
1. As mentioned in the paper, I wonder if some non-causal factors(U) such as “user malfunction” or “data collection jitter” can also be considered as causal factors depending on the domain?
2. What is the rationale for augmenting the raw input time series in the pipeline of CaPulse? Does the method of augmentation influence the performance of the entire framework? Or would it be more helpful to have multiple ways of augmenting instead of just one? Is it enough to simulate real-world disturbances?
3. How to determine an anomaly judgment based on an anomaly score? Is there a threshold?
4. What is the meaning of Figure 6c? What was the author trying to express?
5. In Figure 6a, I don't understand why CaPulse is the only one that can accurately predict the anomalies because I don't know why they are anomalies through the time-series plot.

### Soundness
2

### Presentation
3

### Contribution
3
