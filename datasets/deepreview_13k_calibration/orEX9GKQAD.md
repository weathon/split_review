# EBES: Easy Benchmarking for Event Sequences

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Event sequences, characterized by irregular sampling intervals and a mix of categorical and numerical features, are common data structures in various real-world domains such as healthcare, finance, and user interaction logs. Despite advances in temporal data modeling techniques, there is no standardized benchmarks for evaluating their performance on event sequences. This complicates result comparison across different papers due to varying evaluation protocols, potentially misleading progress in this field.
We introduce EBES, a comprehensive benchmarking tool with standardized evaluation scenarios and  protocols, focusing on regression and classification problems with sequence-level targets. It includes a novel synthetic dataset and provides preprocessed real-world datasets, including the largest publicly available banking dataset.
Our results provide an in-depth analysis of datasets, identifying some as unsuitable for model comparison. We investigate the importance of modeling temporal and sequential components, as well as the robustness and scaling properties of the models. These findings highlight potential directions for future research. Our benchmark aim is to facilitate reproducible research, expediting progress and increasing real-world impacts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a benchmarking set for event sequences, consisting of several known open datasets from various domains. It then provides empirical results with various model architectures (e.g., GRU, Mamba, transformer, etc), on this dataset.

### Strengths
Event sequences are a practically relevant problem setting that has indeed gotten relatively less attention from the ML community. Having benchmarking sets is important to progress the field, hence I applaud this effort.

### Weaknesses
The authors state on page 3: “One of the primary challenges in benchmarking is ensuring that the datasets used are high quality and **accurately represent the problem domain**. I very much agree with the observation that the value of benchmarking sets lies in their degree of representativity of the problem domain as a whole. Here I wonder if this is the case. Looking at Table 1, I see one dataset with a regression target (Pendulum, which is synthetic), and 5 datasets with a classification target.:
- The first question that can be asked here is whether these should be considered to be the same domain at all. If these are separate problem domains, then perhaps these should instead each have their own benchmark. I would love to see a motivation on why this is a single domain.
- Can we really claim that the domain is covered by this benchmark if there is one regression dataset included? I found that doubtful. Also 5 datasets on the classification-side is still quite limited. 
- This work would be much more convincing if the benchmark would have a much larger scale, which would mitigate any concerns about the benchmark sufficiently covering the event sequence domain.

I would like to highlight to the authors the Business Process Intelligence challenge, which has published one event sequence dataset each year since 2011. These are all from the domain of business process management and contain event sequences logged during execution of a business process.

- https://ais.win.tue.nl/bpi/2011/challenge.html until https://ais.win.tue.nl/bpi/2018/challenge.html (change year in url for 2012-2017)

- https://icpmconference.org/2019/icpm-2019/contests-challenges/bpi-challenge-2019/

- https://www.tf-pm.org/competitions-awards/bpi-challenge/2020 

There has been extensive literature on machine learning methods on these event sequence datasets (see [2, 3, 4] for surveys). In particular, some of these works already explicitly intend to serve as a benchmark of ML methods on event sequence datasets (e.g., [1] and [3]). I suggest authors incorporate some of these works into their related work. Given that these datasets are all publicly available and exactly fit the event sequence format that is the focus of this paper, it also appears natural to include (some of) these datasets into their benchmark. This may be a step towards addressing the current limitations of insufficient scale.

### Questions
- Page 5: Is the Holm-Bonferroni correction the right correction? It is not clear why in this setting we would want to control the family-wise error rate rather than the false discovery rate. The latter can be controlled with a Benjamini-Hochberg, and seems to me the more relevant statistical quantity to control. I would like to hear motivation from the authors why instead the decision was made to control the family-wise error rate.

### Soundness
3

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
4

### Summary
This paper proposes a benchmark for event sequence classification and regression. The benchmark includes several commonly used datasets and a synthetic dataset. It examines the behaviors of several machine learning models and how they capture time and orders related features of events.

### Strengths
This paper provides experimental results of assessing several sequence models using different types of datasets, which could benefit future research in this field. 

This paper adopts the hyperparameter optimization and Monte-Carlos cross validation for a fair comparison among models.

### Weaknesses
Even though the paper compares time series data and event sequences in Figure 1, it fails to explain the differences in terms of research challenges of the prediction tasks, thus justifying the motivation and novelty of the proposed benchmark. In fact, several models selected in the paper to assess are the ones for time series data, not particularly for event sequences.

The selection of the publicly available datasets does not show much diversity in terms of data scales, formats, difficulty levels (such as the number of classes), and domains. The assessment results also indicate that the models tend to behave similarly in different datasets. Therefore, it is hard to identify the strengths and weaknesses of a model using the benchmark datasets. The paper also generates a synthetic dataset, Pendulum. But it is unclear how the synthetic dataset complements those real-world datasets and what unique perspectives it can bring to the assessment, especially since it is the only dataset of regression tasks and could introduce biases to the assessment. More datasets for regression tasks, especially the real world ones, should be included in the benchmark.

The benchmark mainly focuses on sequence classification with a small number of classes. In those tasks, time/order could help the performance but not critical as it is not part of the predicted results. The benchmark could include more complex and challenging prediction tasks, such as those mentioned in the first paragraph in Page 2, to have a more thorough study on event sequence models.

### Questions
What are the unique research challenges for event sequence prediction compared to general sequence prediction? The experiment results indicate that general sequence prediction models can also perform well for event prediction. Why is there a need to propose a new benchmark? What are the unique benefits of the new benchmark compared to the existing ones?

What are the principles of selecting the real-world datasets (besides they are publicly available) and designing the synthetic datasets? How can those datasets assess the behavior of a model from different perspectives? 

The selected MLP, GRU, and Transforms are general DL models which can be used to build more specific sequence models for a certain application domain. The paper should include more specific models that better represent the SOTA for event prediction. 

The benchmark mainly focuses on sequence classification with a small number of classes. In those tasks, time/order could help the performance but not critical as it is not part of the predicted results. The benchmark could include more complex and challenging prediction tasks, such as those mentioned in the first paragraph in Page 2, to have a more thorough study on event sequence models. 

The results of Table 2 and Figure 3 need to be explained. For example, why GRU outperforms Transformer even though the latter is more complex? What is the scale of each model in terms of the number of the tunable parameters, what conclusion can be drawn from Table 2, how pretrained model performs differently than others, why mTAND performs better than others with the Pendulum dataset but fails to do so with other datasets. In Figure 3, if no linear trend is observed, what does it suggest? 

There is no description of the Taobao dataset used in the assessment.

### Soundness
3

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
The paper introduces EBES, a benchmarking framework designed specifically for evaluating event-sequence (EvS) data, where sequences of events are characterized by irregular time intervals and a mix of categorical and numerical features. The paper proposes a unified framework including datasets, models, evaluation protocols to enable benchmarking on event-sequence tasks.

### Strengths
EBES provides a unified framework including both datasets, models, and experimental protocols to facilitate reproducible research and consistent evaluations. EBES includes datasets from different application domains, such as medical records, transaction sequences, and synthetic datasets, enhancing its diversity, applicability and utility. The framework also offers a wide range of comprehensive models, such as GRU, Transformer, or specialized ones, mTAND and CoLES. This ensures a thorough evaluation about model performance on event sequences related tasks. The framework also analyzes the importance of modeling time and sequence order in event-sequence data in prediction accuracy.

### Weaknesses
The proposed benchmark framework lacks a comparison with existing tools such as the multi-level task framework for event sequences [1] or [2], hence causes difficulties to assert its advantages over existing frameworks and tools. The dataset diversity is also limited. It is suggested that authors should extend their framework to other application domains, such as the smart city, weather and renewable energy, traffic, social network to further improve the applicability of their framework. Further, evaluation on large scale datasets or real-time event datasets should be conducted to assert the performance and scalability of the benchmark.

### Questions
- How does EBES compare to other event-sequence benchmarks and frameworks, such as the multi-level task framework [1] or other existing benchmarks in event-sequence modeling and temporal point processes?
- Does EBES have plans to incorporate additional datasets from other domains like smart cities, weather forecasting, renewable energy, traffic data, or social networks? Are there plans for incorporating such datasets?
- Has EBES been tested with large-scale or real-time datasets to evaluate its scalability and performance under real world conditions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new benchmark for classification/regression tasks on event sequences (EBSE). The authors consider different types of event sequences, including numerical and categorical features, as well as varying time granularities. EBSE includes seven datasets, one of which is a synthetic dataset proposed by the authors (Pendulum). After a preprocessing step, various models are tested on these datasets, and the results are presented in the paper. Model performance is evaluated using Monte Carlo cross-validation as proposed by Qing-Song Xu and Yi-Zeng Liang in “Monte Carlo cross validation” (Chemometrics and Intelligent Laboratory Systems, 2001). The corresponding code will be made available by the authors after the paper's acceptance.

### Strengths
Benchmarking tools for algorithms used in time series or event sequences are valuable to the scientific community. The authors propose an evaluation protocol that could be of interest. The statistical analysis of the results is also noteworthy.

### Weaknesses
In my opinion, this work is at an early stage of development. A significant aspect of this work is not correctly implemented: the evaluation of a model built on event sequences. The splitting of a dataset into training/validation/test sets should be done based on the order (or timestamps, if working with temporal series) of events. If the dataset is split using a random selection of events, the evaluation results may not reflect real performance. The training set must consist of the oldest data, while the test set should contain the most recent data; otherwise, there is a significant risk of overfitting. The authors use a Monte Carlo cross-validation method originally proposed in a chemistry journal (https://libpls.net/publication/MCCV_2001.pdf). This method is not suitable for event sequences or time series, and the original paper does not address this type of data. For a benchmark to be credible, the performance evaluation process of a model must adhere to scientific rigor, and this part needs more detail from the authors. The code is not yet available, and the paper does not explain how the evaluation is performed on event sequences.

The goal of the paper is to present a new benchmark, which should be characterized by at least several aspects: the number of datasets (seven are proposed here), a set of algorithms, the ability to integrate new algorithms easily, a method to build models using these algorithms, and an evaluation procedure and metrics dedicated to event sequence data.

### Questions
- Q1. Regarding the weakness mentioned, what is the detailed evaluation process for the performance of a model built on an event sequence?
- Q2. On page 3, the authors state they are focused on “ensuring that the datasets used are high quality and accurately represent the problem domain.” How do you verify that a dataset “accurately represents the problem domain” without involving a domain expert? Additionally, what qualifies as a “high-quality” dataset? The preprocessing step proposed in the benchmark, including the handling of missing values, is also domain-dependent in my opinion. Integrating it into a benchmark can be challenging, although I understand the need to compare different models on the same dataset without missing values.
- Q3. What is an MLP? While the reader may infer it to be a Multilayer Perceptron, the term is not explained, and no references are provided.

### Soundness
2

### Presentation
2

### Contribution
2
