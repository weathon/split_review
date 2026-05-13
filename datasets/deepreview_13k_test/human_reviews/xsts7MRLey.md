# DEEP UNSUPERVISED DOMAIN ADAPTATION FOR TIME SERIES CLASSIFICATION: A BENCHMARK

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
Unsupervised Domain Adaptation (UDA) aims to harness labeled source data to train models for unlabeled target data. 
Despite extensive research in domains like computer vision and natural language processing, UDA remains underexplored for time series data, which has widespread real-world applications ranging from medicine and manufacturing to earth observation and human activity recognition.
Our paper addresses this gap by introducing a comprehensive benchmark for evaluating UDA techniques for time series classification, with a focus on deep learning methods. 
We provide seven new benchmark datasets covering various domain shifts and temporal dynamics, facilitating fair and standardized UDA method assessments with state of the art neural network backbones (e.g. Inception) for time series data. 
This benchmark offers insights into the strengths and limitations of the evaluated approaches while preserving the unsupervised nature of domain adaptation, making it directly applicable to practical problems. 
Our paper serves as a vital resource for researchers and practitioners, advancing domain adaptation solutions for time series data and fostering innovation in this critical field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a thorough benchmarking study on time-series unsupervised domain adaptation, primarily focusing on deep learning techniques. It examines the impact of model backbones and hyperparameter tuning approaches. Furthermore, the authors evaluate various existing unsupervised domain adaptation methods across multiple domains, including seven new benchmark datasets.

### Strengths
1. The study delivers a detailed benchmark on unsupervised domain adaptation for time-series data, delving into the effect of domain adaptation algorithms, model backbones, and hyperparameter tuning strategies.
2. The paper evaluates a range of unsupervised domain adaptation methods on datasets from diverse domains, including seven newly introduced datasets and existing benchmarks.

### Weaknesses
1. The discussion on the effect of model backbone in the paper is limited primarily to the Inception model. A broader examination involving diverse backbone models is crucial to substantiate the claim that "backbones do not have a significant impact".
2. More discussions on different types of unsupervised domain adaptation methods would be beneficial. Specifically, it would be informative to explore under what specific conditions certain domain adaptation approaches may outperform others.
3. Additional discussions regarding the choice of model backbones is helpful too. For example, I am curious if Inception is the best model backbone over all domains, or we need different model backbones for different time-series domains and data characteristics.
4. Figure 2 (b) and 5 should be merged since they lead to similar findings.

### Questions
See Weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors present benchmark research on deep unsupervised domain adaptation (UDA) for time series classification (TSC). Specifically, seven new datasets are introduced for this TSC UDA task, and experiments of several existing TSC UDA baselines are tested on these datasets.

### Strengths
Strength:

1.	The paper introduces 7 new datasets for TSC UDA task.

2.	The paper conduct experiments on several existing UDA baselines on the new datasets.

3.	The paper has potential to be a benchmark for the following TSC UDA research.

### Weaknesses
Weakness:

1.	The major concern of the work is on the technical novelty. All the datasets and baselines (including hyper-parameter tuning methods) are from existing literatures, and there is no novel technical contribution proposed. 

2.	For UDA TSC, some important related works are missing, for instance (to name a few), unsupervised video domain adaptation [ref1], transfer gaussian process [ref2], and time-series domain adaptation [ref3]. The authors may need to present a more comprehensive related work section to discuss more related works. 

3.	More analyses on the new datasets are expected, for instance, the domain discrepancy analyses (both marginal and conditional can be involved) on different domain pairs. From the experiments results of the source only baseline, the domain discrepancy differs considerably among different domain pairs, see, Table 5 domain 0 and domain 3, Table 9 domain 9 and domain 18. 

4.	More analyses on the comparison results are also expected. For instance, analyzing why some baselines achieve positive transfer on some tasks but negative transfer on others, e.g., see OTDA/VRADA in table 9. It would be more interesting to see constructive insights or conclusions that can benefit the community. 

[ref1] Video Unsupervised Domain Adaptation with Deep Learning

[ref2] Adaptive Transfer Kernel Learning for Transfer Gaussian Process Regression

[ref3] Time Series Domain Adaptation via Sparse Associative Structure Alignment

### Questions
Please refer to the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work explores the use of unsupervised domain adaptation (UDA) for time series classification (TSC), with a particular focus on deep learning methods. In UDA, which has been extensively explored in vision and natural language applications, two domains of data exist: a labelled source domain and an unlabelled target domain that has some form of shift in the time series data (e.g. differences in data used for training and data used during deployment). The objective is to leverage the labelled source data to make predicts in the target domain.

In addition to five existing datasets, this work proposes the use of seven new datasets for UDA TSC (taken from existing sources). This collection of datasets serves as a benchmarking evaluation tool for assessing the efficacy of different UDA TSC deep learning approaches, notably with different algorithms, hyperparameter optimisation approaches, and model backbones. Consistent experimentation is used to compare the performance of these different approaches and make observations of which elements contribute the most to performance.

### Strengths
**Originality**  
O1. The main novelty of the work lies in the proposal of additional datasets and a consistent, fair framework for evaluation the UDA TSC methods. This also extends to the insights that can be drawn from this evaluation.  
O2. There is also some originality in the deep UDA methods that are used, notably using consistent a consistent backbone (InceptionTime) across different approaches.  

**Quality**  
Q1. The experimental setup is well-structured and makes steps to ensure fairness across all algorithms (e.g. limiting GPU time for training/hyperopt).  
Q2. Results analysis provides some comparisons between the choice of different classifiers, hyperopt methods, and backbones.  

**Clarity**  
C1. Clear descriptions of all the different elements of the experiments are given (models, hyperopt methods, datasets, and pipelines).  
C2. Figures are communicative and support conclusions drawn from the work.

**Significance**  
S1. This work could serve as a stable baseline for further developing UDA TSC deep learning approaches, helping to progress the area of research.  
S2. Insights into the performance of different methods (e.g. InceptionRain seemingly being the strongest method) is useful for establishing the current SOTA and assessing the relative performance.

### Weaknesses
**Presentation of Results**  
P1. While Figure 1 compares model performance within hyperopt methods (a, b, c), it does not provide an overall comparison of all models with all hyperopt methods. As such, it is difficult to determine which complete approach (model + tuning approach) actually has the best performance. An additional critical difference diagram comparing the (5?) top methods for each tuning approach would make this much clearer.  
P2. While the figures provide some information, and the Appendix gives a full set of results for each dataset, it remains difficult to assess the margins between the approaches. A summary table of average accuracy across all datasets for each experimental configuration would be beneficial in conveying this information.  
P3. Further variations of Figure 4 for other models/datasets would be useful to see if the revealed trend is consistent.  
P4. I think the violin plots in Figure 7 are a strong way of communicating the results, and potentially should be moved to the main body if possible. As mentioned above, combining the some selection of the top methods for each tuning approach into a single plot would further aid comparison.  

**Significance**  
S1. I believe this work has the most potential if the evaluation is released to allow further development of methods. I appreciate the source code is planned to be released upon acceptance, but potentially taking this a step further and allowing for easy reproducibility/extensibility would improve the impact of the work and help progress the research area.

### Questions
1. To what extent is there dataset imbalance in the datasets? Additional results, for example using balanced accuracy, may be warranted if dataset imbalanced is high. At the very least, a discussion on any dataset imbalances would be helpful. I appreciate F1 score results are given in the appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
