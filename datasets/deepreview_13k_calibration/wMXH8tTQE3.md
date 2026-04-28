# ProbTS: A Unified Toolkit to Probe Deep Time-series Forecasting

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 8, 6, 3

## Abstract
Time-series forecasting serves as a linchpin in a myriad of applications, spanning various domains. With the growth of deep learning, this arena has bifurcated into two salient branches: one focuses on crafting specific neural architectures tailored for time series, and the other harnesses advanced deep generative models for probabilistic forecasting. While both branches have made significant progress, their differences across data scenarios, methodological focuses, and decoding schemes pose profound, yet unexplored, research questions. To bridge this knowledge chasm, we introduce ProbTS, a pioneering toolkit developed to synergize and compare these two distinct branches. Endowed with a unified data module, a modularized model module, and a comprehensive evaluator module, ProbTS allows us to revisit and benchmark leading methods from both branches. The scrutiny with ProbTS highlights their distinct characteristics, relative strengths and weaknesses, and areas that need further exploration. Our analyses point to new avenues for research, aiming for more effective time-series forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a novel framework for joint training and evaluation of deep time series models on a multitude of datasets available in the literature. The key feature of the proposed approach is the ability to combine and evaluate probabilistic and non-probabilistic methods in one place.

### Strengths
- Work on developing a unified deep learning framework for time-series forecasting is very much appreciated
- The case study reveals interesting insights comparing short term and long term and probabilistic and non-probabilistic models

### Weaknesses
 - ProbTS does not include any naive and statisitcal models (e.g. ETS). The lack of good functioning naive/statistical models for probabilistic forecasting is actually a significant gap in the modern deep learning literature. Could you please include a few methods from this area as baselines in the proposed framework?
- The benchmark contains many datasets, however key datasets that have been instrumental in designing some of the current architectures are missing. Can you include M4, M5, TOURISM?
- Most datasets included in the benchmark are small-scale. For the purpose of studying model scaling and ability to model complex distributions, it feels urgent that large scale time series datasets are included in modern benchmarks. In this context, I can think of FRED from https://arxiv.org/abs/2002.02887

### Questions
- Does your benchmark support zero-shot/few-shot/transfer learning training/testing, pretrained models, model zoo? If not, is it easy to extend it to this scenario? Can you touch on this topic in the paper?
- Does the framework support datasets that don't fit in RAM, what is the mechanism for dataset storage and loading? How do you deal with the licenses of original datasets?
- I included a number of questions and concerns and will be very happy to revise my score accordingly if all of them are addressed meticulously.

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
The authors propose a toolkit to evaluate time-series forecasting methods on various datasets. They observe that there are two main branches: long-term forecasting where data revlease strong trends and seasonality patterns, and a second branch oriented towards short-term forecasting

Highlighting that different data characteristics and forecasting horizons prefer different design

Long - term forecasting : specializing in neural network architecture design with various inductive biases, restricting themselves to point-forecasts
Short - lean towards conventional neural network designs

### Strengths
- Authors implement quite a few models which are evaluated on on the datasets
- The framework provides a standardized way of evaluating methods

### Weaknesses
There are multiple time-series survey/benchmark papers in the literature for forecasting which emphasize standardization across datasets [1], others that emphasize architectural studies [2] and [3] which classifies time-series forecasting methods along the same direction as this work.

It’s not clear where the authors proposed framework fits amongst these previous studies on time-series forecasting, it looks like another way of characterizing time-series forecasting models which is partially covered in [3]. Specifically, the proposed framework does not adequately differentiate itself from the comprehensive dataset standardization presented in [1]. Furthermore, while the paper touches upon architectural considerations, it fails to provide a detailed comparative analysis against the architectural studies highlighted in [2]. The classification methodology appears to overlap significantly with the framework established in [3], raising concerns about the novelty of the proposed approach in this context.

### Questions
- Why don’t authors compare with simpler methods such as XGBoost (with hand crafted features?) 
   - it's quite hard to beat this baseline on the datasets that were used in this paper.
- The datasets used are quite small, I'm curious if these findings hold if we increase dataset size
- Hyperparameters and preprocessing steps used for these datasets could dramatically effect model performance. Were these tuned individually for each of the methods? And why is this not included as part of the text
- What is the guiding mechanism for determining whether a dataset suits the short-forecast or long-forecast category? Is it simply the forecasting window? Or rather intrinsic property to the dataset 
- I believe although initially the paper tries to consider both model/and data aspects of the time-series forecasting domain it fails to provide concrete guidance on how one effects the other, i.e. a quantifiable way of delineating which approach should be taken

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces ProbTS, a novel toolkit aimed at bridging the gap between two prominent research branches in time-series forecasting: one focused on customized neural network architectures and the other on advanced probabilistic estimations. The paper highlights key insights from the toolkit's analysis, revealing that long-term forecasting scenarios often exhibit strong trending and seasonality patterns, while short-term scenarios have more complex data distributions. It also identifies the strengths and weaknesses of different methodological focuses, showing that probabilistic forecasting excels in modeling data distributions, but may produce poor point forecasts. Additionally, the autoregressive decoding scheme is effective in cases with strong seasonality but struggles with pronounced trending, while the non-autoregressive scheme is preferred for long-term forecasting. The paper concludes by emphasizing the potential of combining these research branches to revolutionize time-series forecasting and anticipates that ProbTS will catalyze groundbreaking research in the field.

### Strengths
The paper possesses several strengths. Firstly, it is well-written, displaying a high level of clarity and organization. The insights provided are undeniably valuable, shedding light on the challenging questions arising from the divergence in data scenarios, methodological approaches, and decoding schemes within the realm of time-series forecasting. The paper effectively highlights the significant gap in the existing literature, where no prior solution has successfully bridged the divide between these two distinct research branches. This emphasis on addressing an unexplored area of research stimulates further groundbreaking work in the field. Moreover, the sharing of the ProbTS toolkit included in the paper will benefit the research community, offering a practical resource to help researchers understand and effectively handle these complex issues, ultimately fostering collaboration and collective progress in the field.

### Weaknesses
While this paper offers valuable insights and contributions, there are a few areas where it could be improved. Firstly, while the ProbTS toolkit is undoubtedly a valuable resource, for me, the insights presented in the paper are very informative, and I believe that placing a stronger emphasis on these insights would have been greatly beneficial. Specifically, the paper could better highlight the practical implications of the observed performance differences between probabilistic and point forecasting methods, and autoregressive versus non-autoregressive decoding schemes. The current presentation, while clear, could be enhanced by more directly linking these findings to actionable recommendations for practitioners.

Additionally, the paper could benefit from more extensive discussions on other critical characteristics of time-series forecasting, such as dimensionality, data length, or the volume of training data. These factors can significantly impact forecasting performance, and a deeper exploration of their effects would be highly informative. For instance, the paper does not delve into how the number of input variables or the length of the historical time series affects the relative performance of the different models. Furthermore, the impact of varying training data sizes on the stability and generalization of the models is not discussed, which is a crucial aspect for real-world applications.

Moreover, the insights presented in the paper could have been more rigorously developed and supported. The use of synthetic datasets and controlled experiments could have strengthened the empirical evidence, particularly since the datasets used in the analysis exhibit diverse characteristics that might confound the results. The paper would benefit from a more systematic approach to isolating the effects of specific time-series characteristics, such as trend, seasonality, and noise, on the performance of the different forecasting methods. This would allow for more definitive conclusions about the strengths and weaknesses of each approach. Lastly, a minor point of improvement lies in the Contributions section of the Introduction, where the term CRPS is mentioned before its definition. Providing a definition before using the abbreviation would enhance the clarity of the paper.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose ProbTS, a toolkit for timeseries forecasting that implements a wide range of methods, and report a series of benchmarks that are thoroughly analyzed.

### Strengths
- This work presents an interesting analysis of various time-series forecasting methods, the authors do a great job bridging the gap between two different branches. The benchmarking of these methods across various datasets is valuable and the analysis is very insightful. The work reflects on the current strategies, and provides a unified view of current approaches and existing challenges, and would be invaluable for researchers working on these problems.
- I find the analyses incredibly insightful. The differences between the CRPS and NMAE metrics is interesting.
- The proposed toolbox is thorough and provides a unified framework for comparing various methods at an equal footing (same data pre-processing..). The most recent methods are implemented. This tool should be useful for researchers and could help bridge the gap between the two branches.

### Weaknesses
1. The datasets being studied are on the smaller scale. While these are the main benchmark datasets used in the field, comparing methods on datasets of varying sizes would be important. One might suggest that probabilistic methods excel with large amounts of data. 
2. A noticeably absent aspect of time series is its multi-variate nature. Some methods like PatchTST for example independently process channels. Do different methods present limitations from not modeling the cross-channel interactions?

### Questions
1. Does ProbTS use standard hyperparameter tuning packages like raytune? 
2. For transformer-based models, how were patch sizes determined? 
3. How does model performance compare to performances reported in each method's respective paper? Were all the methods implemented in ProbTS reproduced successfully?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper highlights two main directions of deep learning for time series forecasting - architecture design, and probabilistic forecasting heads. They present a new library which attempts to address both directions, and present some benchmark results and empirical studies.

### Strengths
The paper presents a nice position and overview on the research directions for time series forecasting within the deep learning community.

### Weaknesses
Unfortunately, this paper tries to do too much and too little at the same time.
1. As a paper introducing a new library, there is insufficient details of the design and implementation of the library. It also has insufficient comparison with existing libraries - what sets it apart from existing work?

    a. Table 1 does not really make sense -- the header for column 1 is "Model", all the comparisons are different models, but ProbTS is not a model. It would make more sense to compare ProbTS with other libraries/packages (e.g. GluonTS, TSLib, etc.) rather than specific models/papers.

    b. More attributes for libraries should be compared -- metrics, datasets, data transformations, data loading efficiency, ...

    c. More library comparisons should be added [1, 2, 3], and many others.

    d. The characterization of GluonTS as "each specializing in a single forecasting paradigm, fall short of our research objective to unify the two distinct research branches" is not accurate -- new architectures can and have been implemented in it. Also see how it has been used in [4].

2. As a benchmark paper, it fails to perform a comprehensive evaluation in both dimensions of architecture design and probabilistic forecasting head.

    a. In Table 4, only a small number of methods from each dimension has been evaluated on.

    b. A more comprehensive evaluation, combining different architectures with different probabilistic forecasting heads can be presented.

3. As a an empirical study, it does not yield any definitive insights into the interplay between architecture design and probabilistic forecasting head.

    a. More insights regarding various architecture designs should be given -- e.g. for architectures like Autoformer -- how can be attach probabilistic heads, since the architecture design outputs the prediction based on seasonality + trend? What about PatchTST, how does patching affect probabilistic heads?

Note that I am not saying the paper should achieve everything mentioned above, but one particular direction should be chosen to go all in.

### Questions
None

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
