# CausalRivers - Scaling up benchmarking of causal discovery for real-world time-series

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Causal discovery, or identifying causal relationships from observational data, is a notoriously challenging task, with numerous methods proposed to tackle it.
Despite this, in-the-wild evaluation is still lacking, as works frequently rely on synthetic data evaluation and sparse real-world examples under critical theoretical assumptions. 
Real-world causal structures, however, are often complex, evolving over time, non-linear, and influenced by unobserved factors, making
it hard for practitioners to select appropriate methods. 
To bridge this gap, we introduce CausalRivers, the largest in-the-wild causal discovery benchmarking kit for time series data to date.
CausalRivers features an extensive dataset on river discharge that covers the complete eastern German territory (666 measurement stations) and the state of Bavaria (494  measurement stations). 
It spans the years 2019 to 2023 with a 15-minute temporal resolution. 
Further, we provide data from a recent flood around the Elbe River, as an event with a pronounced distributional shift. 
Leveraging multiple sources of information and time-series meta-data, we constructed two distinct causal ground truth graphs (Bavaria and eastern Germany).
These graphs can be sampled to generate thousands of subgraphs to benchmark causal discovery across diverse and challenging settings.
To demonstrate the utility of our benchmarking kit, we evaluate several causal discovery approaches through multiple experiments and introduce effective baselines, identifying several areas for enhancement.
CausalRivers has the potential to facilitate robust evaluations and comparisons of causal discovery methods.
Besides this primary purpose, we also expect that this dataset will be relevant for connected areas of research, such as time series forecasting and anomaly detection.
Based on this, we hope to establish benchmark-driven method development that fosters advanced techniques for causal discovery, as is the case for many other areas of machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a high resolution dataset of river discharges that covers two large geographical regions in Germany with the purpose of benchmarking causal discovery algorithms. The presented dataset is interesting and presents a significant improvement over existing benchmarks in terms of scale and resolution and has the potential to be a significantly contribution to the development of causal discovery algorithms.

### Strengths
- The dataset is interesting and improves over existing benchmarks both in terms of size and resolution. 
-  The authors provide a reliable baseline for the causal relations in the dataset. 
-  The paper is well written and easy to follow. 
-  The authors provide an extensive set of experimental baselines along with multiple software tools for analysing and processing the dataset.  
- The authors commit to publishing the full pipeline used to construct the data set ensuring reproducibility.

### Weaknesses
 - The authors could have discussed the completeness and reliability of the dataset, such as data quality checks and missing data handling more extensively. 
- Allowing the reviewers access the dataset and software resources would have been beneficial but is understandable given the nature of the article. 
- Although the authors mention that the data is compiled the from multiple sources these are not specified in the paper, providing a list of specific data sources would enhance transparency and reproducibility.

### Questions
- see weaknesses above

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
4

### Summary
This paper introduces the CausalRivers benchmarking kit for comprehensive time series data analysis of river discharge in Germany. With high-frequency sampling every 15 minutes, the dataset includes data from a significant flood event on the Elbe River, making it suitable for testing causal discovery under real-world conditions with distributional shifts. The kit supports a range of causal discovery methods, from traditional approaches like Granger causality to advanced models like PCMCI, VARLINGAM, Dynotears, and CDMI, and allows sampling of subgraphs for diverse benchmarking cases. 
The experimental evaluation uses data from 666 and 494 stations across eastern Germany and Bavaria, respectively, from 2019 to 2023. 
The results revealed that while advanced methods struggle with real-world complexities like non-stationarity and high dimensionality, simple baselines performed robustly in identifying causal links. Domain adaptation via fine-tuning also showed performance gains.

### Strengths
The paper’s main strength is the extensive, realistic testing of causal discovery methods in the wild, which provides valuable insights into performance in a complex problem. CausalRivers supports various graph structures and sampling techniques, making it adaptable for different scenarios. It is obvious that benchmarks are important, and CausalRivers’ advanced methods allow for comprehensive performance comparisons across various scenarios.

### Weaknesses
Although this paper has an intensive assessment of models, its main weakness is that it is a technical benchmark. That is, the dataset’s complexity, along with various methods, may present implementation challenges for causal discovery researchers, and thus, it offers scientific opportunities. However, the scientific insight from the paper is missing (unless ICLR has changed its structure and now accepts also non-research but technical contributions, in which case this paper would be a good fit)

### Questions
NA

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
4

### Summary
This paper provides a large-scale benchmark dataset for causal discovery to estimate causal relationships between time series. The dataset consists of river flow measurements from East Germany and Bavaria, collected at 15-minute intervals from 2019 to 2023, and also includes flood data from the Elbe River area. Benchmark experiments using various causal discovery methods on the time series data revealed that a simple baseline method demonstrated the most consistent performance, outperforming many other causal discovery techniques. Additionally, the use of deep learning-based causal discovery methods showed a significant improvement in performance through domain adaptation across different datasets. This dataset represents an unprecedented benchmark for causal discovery in time series data and is expected to greatly contribute to advancing research in this field.

### Strengths
This paper presents a large-scale benchmark dataset for causal discovery to estimate causal relationships between multivariate time series. The dataset provides an unprecedented scale of ground-truth data for causal discovery in time series, and it is expected to contribute to the advancement of research in this area significantly. Furthermore, the benchmark experiments conducted using this dataset revealed that a simple baseline method outperformed many other causal discovery techniques, offering important insights into the field, which has traditionally relied on evaluations using artificial data or simpler real-world datasets.

### Weaknesses
The benchmark dataset provided in this paper is of unprecedented scale and will undoubtedly contribute significantly to the field of causal discovery. However, the task may be somewhat simplified because the dataset is tied to geographical information. Predicting causal relationships between nearby river basins is relatively easy, meaning that causal discovery might only need to focus on a limited subset of the series. This could slightly diminish the dataset's overall value. The experiments seem to focus only on causal discovery within subsets of the time series. A broader evaluation of causal discovery across all series could lead to a more in-depth discussion.

Additionally, there are a few minor typographical errors. For instance, in Section 3.2.1, the phrase "benchmarking kid" should be corrected to "benchmarking kit." Moreover, variables with upper bars are used in the same section without explanation, and the notation should be clearly defined.

### Questions
As noted in Table 1, there is still a lack of sufficient benchmark datasets for causal discovery in non-time-series domains, even for real-world data. Would it be feasible to construct similar benchmark datasets for causal discovery in non-time-series settings?

### Soundness
3

### Presentation
3

### Contribution
4
