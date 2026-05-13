# TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis

- Decision: Accept
- Avg Score: 8.00
- Scores: 10, 8, 6

## Abstract
Time series analysis plays a critical role in numerous applications, supporting tasks such as forecasting, classification, anomaly detection, and imputation. In this work, we present the \emph{time series pattern machine} (TSPM), a model designed to excel in a broad range of time series tasks through powerful representation and pattern extraction capabilities. Traditional time series models often struggle to capture universal patterns, limiting their effectiveness across diverse tasks. To address this, we define multiple scales in the time domain and various resolutions in the frequency domain, employing various mixing strategies to extract intricate, task-adaptive time series patterns. Specifically, we introduce \method, a general-purpose TSPM that processes multi-scale time series using (1) \emph{multi-resolution time imaging} (MRTI), (2) \emph{time image decomposition} (TID), (3) \emph{multi-scale mixing} (MCM), and (4) \emph{multi-resolution mixing} (MRM) to extract comprehensive temporal patterns. MRTI transforms multi-scale time series into multi-resolution time images, capturing patterns across both temporal and frequency domains. TID leverages dual-axis attention to extract seasonal and trend patterns, while MCM hierarchically aggregates these patterns across scales. MRM adaptively integrates all representations across resolutions. \method achieves state-of-the-art performance across 8 time series analytical tasks, consistently surpassing both general-purpose and task-specific models. Our work marks a promising step toward the next generation of TSPMs, paving the way for further advancements in time series analysis.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper presents TIMEMIXER++, a general-purpose model for various time series tasks, including forecasting, classification, anomaly detection, and imputation. Utilizing a multi-scale, multi-resolution framework, the proposed method transforms time series data into multi-resolution images to capture complex temporal and frequency-domain patterns, enabling flexibility across analytical applications. The model’s approach includes dual-axis attention for decomposing seasonal and trend components and hierarchical multi-scale and multi-resolution mixing to integrate patterns across scales. The proposal achieves strong performance across eight benchmark tasks, outperforming both general-purpose and task-specific models. This work contributes to advancing time series analysis with new state-of-the-art benchmarks across settings.

### Strengths
S1. The proposed model captures both short- and long-term dependencies by transforming time series data into multi-resolution images, enabling the analysis of complex temporal and frequency-domain patterns that challenge traditional models. The authors validate this with experimental results showing the new architecture outperforms SOTA models on most standard benchmarks. The ablation study helps validate the importance of the individual parts of the architecture – the channel mixing, image decomposition, and multi-scale and multi-resolution mixing. This approach continues to validate the benefits of integrating image analysis techniques with time series tasks.

S2. The architecture is flexible for supporting different kinds of time-series tasks. The hierarchical multi-scale and multi-resolution mixing modules enable the model to flexibly adapt across various time series tasks, from forecasting to anomaly detection, promoting robust and accurate performance across applications.

S3. Empirical Validation: the testing in this paper on eight benchmark time series tasks, including the hyperparameter ablation results, shows TIMEMIXER++ consistently surpasses both general-purpose and task-specific models, affirming its potential as a high-performance, general-purpose solution for time series analysis. The experiments were very thorough.

### Weaknesses
W1. There is little exploration of scaling of model size, which would be an interesting avenue for validating the model architecture in a zero shot setting. The current zero-shot experiments are primarily in-domain and not cross-task.

### Questions
Q1. The proposed architecture adds significant computational cost to the internal representation of the model compared to vanilla transformers and some of the previously proposed models. It seems this does not have a significant effect on the training time compute and memory complexity of the model. Have the authors conducted any studies to compare the inference-time cost of TM++ compared to other methods? 

Q2. As mentioned by authors, some time series tasks (imputation, anomaly detection) benefit more from diverse representations while others like forecasting and classification benefit from consistent representation. Given this, is there any way to leverage a routing model dependent on the proposed task type, which could lower the inference-time cost of this model?

Q3. MTS-Mixer (Li et. al., 2023) presents another approach to channel decomposition which similarly outperformed competing models, but they found the approach worked best with MLPs rather than attention-based models. Have the authors explored this technique for separating from attention mechanisms which could lead to further efficiency and model performance?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents TimeMixer++, an advanced framework designed to enhance general time series analysis. TimeMixer++ integrates multi-resolution time imaging, multi-scale mixing, and dual-axis attention mechanisms to effectively capture and adapt to diverse patterns within time series data. This innovative approach allows for robust and flexible analysis across various temporal scales and resolutions.

### Strengths
1. the authors introduce a robust framework TimeMixer++ that leverages multi-resolution time imaging, multi-scale mixing, and dual-axis attention to enhance general time series analysis. They present SOTA results on four different tasks.
2. the integration of both multi-scale and multi-resolution mixing strategies for adaptive pattern extraction demonstrates innovation.
3. the manuscript and appendix are well-prepared, but the authors have not yet released the promised code.

### Weaknesses
1. the fonts in the figures should be enlarged for better readability. For example, in Figure 1 (right), the label "Benchmarking model performance across representation analysis in four tasks" appears blurred. Additionally, consider using a single set of legends for all four tasks to enhance clarity.
2. the source code repository has not released for reproducing, i will consider raising the score if the released repository and the consistency of the results.
3. more detail on how it compares to recent models like TimesNet and iTransformer on specific time series tasks would strengthen the paper’s claims.
4. including a discussion on computational efficiency (e.g., FLOPs, memory usage) for different tasks could enhance the paper’s utility.

### Questions
See weaknesses (W2, W3, W4).

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a time series pattern machine method called TimeMixer++ for processing multiscale time series. The method transforms time series into multi-resolution time images to enable pattern extraction with respect to temporal and frequency domains followed by three dominant modules - (1) input projection; (2) a stack of Mixerblocks; (3) output projection.  Extensive experiments show the proposed method obtains improvement over the well-established competing methods.

### Strengths
The methods used in the paper (e.g., time imaging and image decomposition) are very interesting. The evaluation is comprehensive: the authors discuss long and short-term forecasting, zero-short forecasting, classification, and anomaly detection.

### Weaknesses
In terms of the forecasting results shown in Tables 3 and 4, the performance gain is negligible, and such minor improved performance certainly can be attributed to the parameter tuning, e.g., a well-tuned parameter settings for TimeMixer++ while a weak parameter settings for other competing methods.  

The paper barely offers insights both theoretically and experimentally. The theoretical understanding of the improvement as well as its time imaging and multi-resolution mixing is lacking, mostly based on intuition and simply blending the models. 

There are some papers that already discussed the use of frequency analysis and the frequency components extraction for model deployment (e.g., [1][2][3]) to capture the periodic patterns, and they all claim it can capture the global interaction and patterns among time series, so what is the benefits of introducing multi-resolution time imaging, and it is worthwhile to compare them in ablation study? In addition, it is encouraged to cite the papers [1][2][3] if not yet in the references.

### Questions
[1] Questions follow from the points listed in the weakness section.
[2] What is the naming of the method, i.e., TimeMixer++ in terms of? or just because both the methods target processing multi-scale time series? 
[3] What is the connection with the method TimeMixer?

### Soundness
2

### Presentation
3

### Contribution
2
