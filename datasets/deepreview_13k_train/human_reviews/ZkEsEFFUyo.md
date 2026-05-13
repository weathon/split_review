# Pushing the Limits of Pre-training for Time Series Forecasting in the CloudOps Domain

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Time series has been left behind in the era of pre-training and transfer learning. While research in the fields of natural language processing and computer vision are enjoying progressively larger datasets to train massive models, the most popular time series datasets consist of only tens of thousands of time steps, limiting our ability to study the effectiveness of pre-training and scaling. Recent studies have also cast doubt on the need for expressive models and scale. To alleviate these issues, we  introduce three large-scale time series forecasting datasets from the cloud operations (CloudOps) domain, the largest having billions of observations, enabling further study into pre-training and scaling of time series models. We build the empirical groundwork for studying pre-training and scaling of time series models and pave the way for future research by identifying a promising candidate architecture. We show that it is a strong zero-shot baseline and benefits from further scaling, both in model and dataset size. Accompanying these datasets and results is a suite of comprehensive benchmark results comparing classical and deep learning baselines to our pre-trained method -- achieving a 27\% reduction in error on the largest dataset.\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This scientific paper addresses the limited progress in applying pre-training and transfer learning to time series data. To bridge this gap, the authors introduce three large-scale time series forecasting datasets from the CloudOps domain, with the largest dataset containing billions of observations. This substantial dataset size allows for a comprehensive investigation into the effectiveness of pre-training and scaling for time series models. The paper establishes the groundwork for studying pre-training and scaling of time series models and identifies a promising architecture for the task. This architecture serves as a strong zero-shot baseline and exhibits further improvements with increased model and dataset size. The authors provide a benchmark comparing several classical and deep learning methods with their proposed pre-trained approach, demonstrating significant reduction in error on the largest dataset.

### Strengths
1. The manuscript is well-written and easy to follow. The authors thoroughly explain various setups, such as pretraining and fine-tuning, and make an attempt to define a taxonomy of time series data based on domains, collections, and individual time series.
2. The work introduces three large-scale time series forecasting datasets, which enable a deeper exploration of pretraining and transfer learning for time series models. The authors provide concrete details into the process of transforming raw data into useful time series data.
3. The paper goes on to examine various Transformer architectures for forecasting, conducts a comprehensive benchmarking analysis against classical and deep learning forecasting methods, and also compares their proposed pretraining approaches with existing methods. Additionally, the study investigates the impact of scaling in terms of model parameters and training data size on time series forecasting.

### Weaknesses
1. Lack of Novelty: The paper's approach is primarily centered on training a large transformer model on an extensive time series dataset, which may not offer a novel contribution to the field. The core idea of leveraging large-scale datasets for pre-training transformers is not new, and the paper does not introduce significant architectural or methodological innovations beyond this. The application to time series data, while valuable, does not represent a fundamental breakthrough in the pre-training paradigm itself.

2. Limited Analysis of Transfer Learning: The study raises concerns regarding the assessment of transfer learning, as the model is trained on one dataset and tested on a similar one without sufficient information about their differences. This makes it challenging to interpret the extent of transfer learning within an in-collection setting. Specifically, the paper lacks a rigorous analysis of the distribution shift between the pre-training and fine-tuning datasets. Without this, it is difficult to ascertain whether the observed performance gains are due to genuine transfer learning or simply the model's ability to memorize patterns within a relatively homogenous dataset. Additionally, the diversity of time series within the CloudOps datasets remains unclear, which could lead to potential overfitting issues, particularly for large models. The paper needs to provide more detailed analysis of the time series characteristics within each dataset.

3. Inadequate Baseline Model Details: The paper lacks essential information about the baseline models, including their model size and training duration. For instance, while DeepAR emerges as the second best method in Table 5, it is uncertain if its number of parameters is comparable to the proposed transformer models. A comparison with DeepAR models of similar scale and training iterations would provide valuable insights. The paper should also clarify if the baseline models are trained from scratch or if they are also pre-trained, as this could significantly impact their performance.

4. Limited Improvements in Larger Models: The paper reveals that the gains achieved with "Large" and "xLarge" models are not significant when compared to the base model size. Particularly, the "xLarge" model, despite being over eight times larger than the base model, exhibits only marginal improvements. This suggests that the base model may already be overfitting the datasets. The paper does not sufficiently explore the reasons behind this saturation, such as potential limitations in the dataset's complexity or the model's architecture.

### Questions
See weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents pre-training time-series model in the cloud operations domain to enhance downstream forecasting accuracy. The authors conduct experiments to compare various model architectures and investigate the scaling laws impacting both model and data size. Their findings indicate promising results in zero-shot scenarios.

### Strengths
1. The paper introduces the first pre-trained time-series model specifically for cloud operation domains.
2. The study evaluates different model architectures in the context of pre-training and examines the effects of model and data size on performance with scaling laws.

### Weaknesses
1. The pre-training and zero-shot testing appear to be conducted within the same dataset. If this is correct, it raises concerns about the true generality of the zero-shot performance, particularly regarding its effectiveness in diverse or new datasets and domains.
2. The paper mainly focuses on benchmarking existing pre-training model architectures without significant novel adaptations or designs tailored to the specific requirements of the cloud operation domain.
3. Is the model randomly initialized? Given the effectiveness of the baseline one-fits-all model, an exploration into using pre-trained language models as initialization might be helpful.
4. It remains unclear whether deep learning benchmarks such as N-BEATS, Autoformer, and FEDformer are only trained on designated training sets. Exploring whether similar performance improvements could be achieved by training these models on the pre-training set, using the same loss function, might offer deeper insights. This also helps determine the source of the proposed model's performance gains—whether from the architecture itself or mostly from expanded datasets.

### Questions
See Weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces three new large datasets from the CloudOps domains with billions of observations for time series forecasting. Further, the authors provide a performance analysis including time series forecasting models for the cases where models are trained from scratch, fine tuned, and zero-shot. The authors show further evaluate different transformer variants and show that the proposed baseline achieves a 27% error reduction on largest dataset.

### Strengths
1. The authors provide three new large datasets from the CloudOps field. This contribution is relevant in the field of time series forecasting, as there is certain lack of this kind of datasets, holding back the progress in the topic of pretrained models or LLM-based forecasting models.
2. The authors provide an interesting evaluation of several existing models. These evaluations provide an interesting reference on how well-established models perform in these datasets, and how they compare with pretrained models.
3. The authors provide an interesting analysis on variants of transformer models, providing further insights on what approaches are more promising in the future.
4. The paper is well written and it makes an effort on having well structured terminology in these new and developing field.

### Weaknesses
The main weakness of the paper is that the contribution of this paper is basically three new datasets. I acknowledge the non-trivial effort that it implies to gather this kind of large scale datasets. Nevertheless, I share as well my concern that there is not much of an analysis of what are the main challenges that these datasets pose. For instance: 1/ Do they have missing values? 2/ how strong is the seasonality in these datasets? 3/ Is there any interesting trend in the data? Are there any distribution shifts (for instance, something like a black-friday regime, a change around covid lockdowns, etc)?

### Questions
1. what is the main challenge that these datasets pose?
2. how diverse are these three datasets? I understand that they come from the CloudOps field, but is there any fundamental difference between them?
3. Is there any distribution shift captured in these datasets?
4. How do these datasets look in the test windows used for evaluation? And how do the forecasts per model look? I understand that for ali2018 the forecasts are potentially similar as Naive performs very good, but what about azure 2017 where the proposed baselines are performing exceptionally well?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
