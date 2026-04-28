# Unified Long-Term Time-Series Forecasting  Benchmark

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
In order to support the advancement of machine learning methods for predicting time-series data, we present a comprehensive dataset designed explicitly for long-term time-series forecasting. We incorporate a collection of datasets obtained from diverse, dynamic systems and real-life records. Each dataset is standardized by dividing it into training and test trajectories with predetermined lookback lengths. We include trajectories of length up to $2000$ to ensure a reliable evaluation of long-term forecasting capabilities. To determine the most effective model in diverse scenarios, we conduct an extensive benchmarking analysis using classical and state-of-the-art models, namely LSTM, DeepAR, NLinear, N-Hits, PatchTST, and LatentODE. Our findings reveal intriguing performance comparisons among these models, highlighting the dataset-dependent nature of model effectiveness. Notably, we introduce a custom latent NLinear model and enhance DeepAR with a curriculum learning phase. Both consistently outperform their vanilla counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a standardised time series dataset for use in benchmarking long-term time series forecasting (LTSF) methods. A variety of methods are tested on the dataset, with slightly simpler methods (NLinear and DeepAR-CL) demonstrating consistently better performance.

### Strengths
Providing researchers with additional datasets for testing would help to strengthen the claims of new LSTF architectures proposed.

### Weaknesses
However, it is not immediately clear what novel methods the authors have created and what the value proposition of the paper is. While additional datasets can be beneficial to strengthen claims, it is not immediately unclear why the existing datasets for benchmarking (often real world diverse datasets) are insufficient, or why the synthetic datasets proposed (which can also be found in other time series papers, particularly MuJoCo) are better models the LSTF problem. In addition, details on hyperparameter tuning are sparse, with critical hyperparams such as learning rates and regularisation params (e.g. dropout) omitted from the paper. Given the diversity of time series datasets, performance of hyperparams are highly dataset specific -- and without full tuning it is difficult to disenteagle if underperformance is due to improperly selected hyperparams (e.g. with LSTM on sine waves). This is particularly the case for larger transformer models, especially when transferred onto simpler datasets. The paper lacks a clear articulation of the specific limitations of existing LTSF benchmarks that this new dataset aims to address, making the contribution less impactful. The choice of synthetic datasets, while offering control over data generation, does not fully address the complexities and nuances of real-world time series data, raising questions about the generalizability of the findings. Furthermore, the absence of details regarding the selection of hyperparameters, especially for complex models like transformers, makes it difficult to ascertain whether the reported performance differences are due to inherent model capabilities or suboptimal hyperparameter configurations. This lack of transparency hinders the reproducibility and interpretability of the results.

### Questions
1. How would authors describe the novelty of the paper, and what new methods have been created/proposed?
2. Why are the synthetic datasets suggested better suited for the LSTF problem?
3. How is hyperparam tuning concretely performed, and how are learning rates/regularisation params set?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
**Summary:**

This paper presents a comprehensive dataset specifically designed for long-term time-series forecasting, which includes simulated data as well as real-life data. The authors standardize each dataset into training and test trajectories with predetermined lookback lengths and conduct an extensive benchmarking analysis using both classical and state-of-the-art models, including a custom latent NLinear model and an enhanced DeepAR with a curriculum learning phase.

**Strengths:**

1. Several simulated datasets are proposed.

2. lookback windows are standardized.


**Weaknesses:**

1. I'm not fully convinced that including various simulated datasets would be helpful. One significant feature of long-term forecasting is high volatility, such as weather and stock prices. The evolving procedure can hardly be described by several relatively simple equations. Thus even if a model works well in the simulated dataset, it still may not necessarily also work well in real-world datasets.

2. No new real-world datasets are proposed.


**Questions:**

1. I'm wondering if the authors could elaborate more on the necessity of including simulated datasets and the performance correlation between simulated datasets and real-world datasets.


At the current stage, the paper's contributions, while noteworthy, do not seem to meet the high threshold of a top-tier machine learning conference like ICLR.  However, I'm not a expert in dataset track and I am open to reconsidering my decision after rebuttal .

### Strengths
Please refer to the Strengths section in Summary.

### Weaknesses
1. I'm not fully convinced that including various simulated datasets would be helpful. One significant feature of long-term forecasting is high volatility, such as weather and stock prices. The evolving procedure can hardly be described by several relatively simple equations. Thus even if a model works well in the simulated dataset, it still may not necessarily also work well in real-world datasets.

2. No new real-world datasets are proposed.

### Questions
Please refer to the Questions section in Summary.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a unified benchmark dataset for long-term time-series forecasting (LTSF), addressing the limitations of existing datasets. The dataset includes real-life and synthetic data from diverse domains, enabling comprehensive evaluations of LTSF methods. The datasets are split into training and testing trajectories with fixed lengths, allowing for standardized evaluations. The paper introduces two new hand-crafted models, the latent NLinear model and DeepAR enhanced with curriculum learning, which outperform existing models. The benchmark includes classical and state-of-the-art models such as LSTM, DeepAR, N-Hits, PatchTST, and LatentODE, and evaluates their performance on the dataset. The paper emphasizes the importance of dataset diversity, facilitating ML model training and testing, and introducing new models to improve LTSF accuracy. The paper concludes by providing an open-source library with implementations to promote further advancements in LTSF research.

### Strengths
1. Comprehensive dataset: The article presents a comprehensive dataset that incorporates real-life and synthetic data from diverse domains, enabling the evaluation of long-term time-series forecasting methods in a wide range of contexts. This comprehensive dataset helps in gaining a more holistic understanding of the strengths and weaknesses of different methods across various domains.

2. Standardized evaluation: To ensure consistency and comparability, the authors split the dataset into training and testing trajectories with fixed lengths. This standardized evaluation approach allows for more accurate and reliable comparisons between different methods.

3. Introduction of new models: The article introduces two new hand-crafted models, namely the latent NLinear model and DeepAR enhanced with curriculum learning. These new models demonstrate significant improvements across the entire dataset, showcasing their effectiveness and potential in long-term time-series forecasting.

4. Extensive method comparison: The article conducts a thorough benchmarking analysis, evaluating a range of neural network-based models including classical approaches and state-of-the-art methods. By comparing the performance of these methods on the dataset, a better understanding of their strengths and limitations can be gained, fostering advancements in the field.

5. Open-source code library: To facilitate further advancements in the field, the authors provide an open-source code library that includes implementations of the methods discussed. This enables other researchers to easily replicate and extend these methods, accelerating progress in the field.

### Weaknesses
1. Regarding innovation:

   (1) The proposed methods in this article seem to have had little impact on the overall benchmark and did not address any gaps in the existing methodological framework or provide substantial insights or innovations. The article needs to clearly articulate the innovative aspects of its methods and how they improve upon existing approaches. Specifically, the latent NLinear model, while utilizing a latent space, does not clearly demonstrate a novel approach to capturing non-linear dependencies beyond standard dimensionality reduction techniques. The claim of 'linearization' of the state space needs more rigorous justification and comparison to existing methods that achieve similar effects through different mechanisms. The DeepAR enhancement with curriculum learning, while potentially beneficial, lacks a detailed analysis of how the curriculum is designed and how it specifically addresses the challenges of long-term forecasting.

   (2) The benchmark dataset created in the article consists of two parts: SYNTHETIC and REAL-LIFE. However, while the REAL-LIFE part mainly comprises existing time-series datasets, the contribution of the SYNTHETIC part in addressing the limitations of the existing REAL-LIFE datasets is not adequately explained. The article should analyze the potential shortcomings of the existing real-life datasets, such as limited variability, lack of long-range dependencies, or specific types of non-stationarity, and explain how the SYNTHETIC dataset complements them. The description of the synthetic data generation process is also lacking in detail, making it difficult to assess the diversity and complexity of the generated data.

2. Regarding experiments:

   (1) The description of the process for jointly evaluating models using artificial and real-life data is overly concise and fails to analyze the fundamental differences between artificial and real-life data. It is recommended to propose a systematic evaluation framework for time-series models that goes beyond presenting a series of datasets. Specifically, the evaluation should address the potential for models to overfit to the specific characteristics of either synthetic or real-life data, and how the benchmark mitigates this risk. The paper lacks a discussion on how the different statistical properties of the datasets (e.g., stationarity, autocorrelation, noise characteristics) affect the performance of different models.

   (2) The experimental evaluation of Transformer models only includes one model, PatchTST, thereby lacking a comprehensive exploration of other Transformer models. It is advisable to include a wider range of Transformer models in the experiments for a more comprehensive comparison and evaluation. The absence of other popular Transformer models, such as Informer or Autoformer, limits the scope of the benchmark and prevents a thorough assessment of the performance of different Transformer architectures on the proposed dataset.

3. Regarding presentation:

   (1) The "BENCHMARK SYNERGY" section lacks formulas and illustrations, making it difficult for readers to understand its content. It is recommended to provide more visualizations and illustrations in this section to aid reader comprehension. The section should clearly articulate the specific properties of the synthetic and real-life datasets and how they complement each other to provide a more comprehensive evaluation of LTSF models. The lack of visual aids makes it difficult to grasp the key message of the section.

   (2) The article lacks basic visual analysis and conclusions, making it challenging for readers to grasp the experimental results intuitively. Including more data visualizations and clear conclusions in the article would provide more intuitive information. The current presentation relies heavily on tables, which makes it difficult to quickly assess the relative performance of different models across different datasets. Visualizations, such as box plots or line graphs, would be beneficial for comparing model performance.

   (3) The article lacks intuitive descriptions of the datasets, such as data-time graph representations, making it difficult for readers to understand the characteristics and structure of the datasets clearly. The absence of time-series plots for each dataset makes it difficult to understand the underlying patterns and temporal dependencies present in the data. This is especially important for the synthetic datasets, where the generating processes are not immediately obvious.

   (4) There is a lack of illustrations for different data generation methods, impeding readers' understanding of the data generation process and methods. It would be beneficial to include relevant figures to help readers comprehend the data generation process. The paper should provide a more detailed explanation of the parameters used in the synthetic data generation process, and how these parameters affect the characteristics of the generated data. This would allow for a better understanding of the diversity and complexity of the synthetic datasets.

   (5) The absence of data-time graph representations for the predictive performance of different models hinders readers' ability to visually compare the performance of various models. It is recommended to provide data-time graph representations in the results section to facilitate a better understanding of the predictive performance of the different models.

### Questions
1. Flaw: The author says: "The most dominant class of LTSF benchmarks relies on datasets with rather uniform characteristics composed of nine widely-used real-world datasets: Electricity Transformer Temperature (ETT) from Zhou et al. (2021a) (split into four cases: ETTh1, ETTh2, ETTm1, ETTm2), Traffic, Electricity, Weather, ILI, ExchangeRate. All of them are univariate time series with a significant degree of non-deterministicity (these are real-life measurements)." However, they are mostly multivariate time series.

2. What I am concerned about most is listed in the weakness, I won't refuse to raise my points if the author can address my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
