# When Will It Fail?: Anomaly to Prompt for Forecasting Future Anomalies in Time Series

- Decision: Reject
- Scores: 6, 5, 3, 3, 3

## Abstract
Recently, time series forecasting, which predicts future signals, and time series anomaly detection, which identifies abnormal signals in given data, have achieved impressive success. However, in the real world, merely forecasting future signals or detecting anomalies in existing signals is not sufficiently informative to prevent potential system breakdowns, which lead to huge costs and require intensive human labor. In this work, we tackle a challenging and under-explored problem of time series anomaly prediction. In this scenario, the models are required to forecast the upcoming signals while considering anomaly points to detect them. To resolve this challenging task, we propose a simple yet effective framework, Anomaly to Prompt (A2P), which is jointly trained via the forecasting and anomaly detection objectives while sharing the feature extractor for better representation. On top of that, A2P leverages Anomaly-Aware Forecasting (AAF), which derives the anomaly probability by random anomaly injection to forecast abnormal time points. Furthermore, we propose Synthetic Anomaly Prompting (SAP) for more robust anomaly detection by enhancing the diversity of abnormal input signals for training anomaly detection model. As a result, our model achieves state-of-the-art performances on seven real-world datasets, proving the effectiveness of our proposed framework A2P for a new time series anomaly prediction task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper primarily introduces the scenario of anomaly prediction and provides a solution called AAF. Based on historical input time series, AAF predicts whether an anomaly will occur at a future point. Before training AAF, an Anomaly Prompt Pool (APP) is pre-trained to generate an anomaly prompt pool. Detailed experiments have proven that this method significantly outperforms well-known existing methods, such as iTransformer and P-TST.

### Strengths
1. Anomaly prediction is a promising direction that can leave valuable time for subsequent fault elimination and even predict and avoid potential faults in advance.
2. The method of joint training for time series prediction and anomaly detection makes sense.

### Weaknesses
1. There is an inconsistency between Figure 4 and Figure 3 in the paper. In Figure 3, e_{in}  serves as a key and value, but in Figure 4,  e_{in}  serves as a query.
2. See the following questions.

### Questions
1. It is common that many anomalies are sudden drops or rises in indicators that have no relation to the preceding time series. Theoretically, these cannot be predicted. The paper's generally low F1-score below 50% seems to confirm this point. Can the authors provide statistics on how many of these unpredictable cases there are in the evaluation dataset to prove the feasibility of anomaly prediction or its theoretical limits?
2. The APP pre-training generates an anomaly prompt pool for the subsequent random injection of anomalies during training to learn the relationship between anomalies and time series. However, these injected faults, no matter how similar they appear with normal input, may differ significantly from actual situations and could affect the model's performance. Can the authors explain why these artificially injected anomalies can help learn the relationship between real-world anomalies and time series?
3. During the large-scale pre-training process, was the test dataset seen, and is there a data leakage issue?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose to predict anomalies in future amples in a time
seriese that have not arrived yet.  First, the future samples are
forecasted, then anomalies are detected.  Cross attention is used
between the forecasted future input and previous input.  Based on QKV
embeddings, Q is the future input, K and V are from previous input.
The probability of an anomaly is estimated as the activation function
of the attention value from Anomaly-Aware Forecasting Network (AAFN).
The loss function is the MSE of estimated and actual probability.

For forecasting future samples with potential synthetic anomalies, an
Anomaly Prompt Pool (APP) is used, which is learned.  Anomalies from
the pool are injected into the forecasted signal similar to (Darban et
al 2025).  First, a feature extractor is trained on normal signal.
Second, the previous signal is the query, and an anomaly prompt in the
pool is a key.  The prompts that correspond to the closest keys that
match the query are "attached" to the embedded previous input. The
prompts help generate abnormal signals.  To train APP, they use
Intra-Signal Anomaly Discrepancy Loss. They use the energy score from
(Liu et al, 2020)--low energy scores indicate normal samples, while
higher engergy scores indicate abnormal samples.

Additionally, they have a reconstruction loss for the previous signal
and a forecast loss for the future signal.  Moreover, they have
Inter-Signal Anomaly Divergence Loss.

They compare their porposed method A2P with 4 existing methods over 6
datasets. Empirical results indicate that A2P generally outperforms
the existing methods.  Ablation studies indicate contributions from
the different components.

### Strengths
Anomaly prediction is an interesting problem.  The proposed methods
for training the Anomaly Prompt Pool is interesting.

Empirical results indicate that A2P generally outperforms the existing
methods.  Ablation studies indicate contributions from the diferent
components.

### Weaknesses
Different parts of the methods could use more explanation,
particularly how the future signal, $\hat{X}_{out}$, is forecasted (see questions below).

When synthetic anomlies are injected into the forecasted signal, you
already know where they are.  Do you need to detect them?

Evaluating how well the future signal is forecasted would be
beneficial.  Though not the primary goal, forecasting the future
signal is an intermediate goal.

### Questions
line 300: How do you tranfrom the original normal signal to an
abnormal signal based on the "attached" prompts.  Also, "the output
anomaly prompts are then removed".  How are these output prompts
obtained?  Are they the prompts attached in Eq 2?

Eq 4: What are the gamma function and k_m?.  Why does the
division in the first term measure discrepancy?

Eq 5: The two X' terms could use more explanation--what are they and
how are they obtained?

Eq 7: How is $\hat{X}_{out}$ obtained?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose a simple yet effective framework, Anomaly to Prompt (A2P) to tackle a problem of time series anomaly prediction. It derives the anomaly probability by random anomaly injection to forecast abnormal time points. It achieves robust anomaly detection by synthesizing anomalies to enhance the diversity of abnormal signals.

### Strengths
S1. This paper presents an interesting approach for the task of time series anomaly prediction.

  S2. The experimental findings illustrate the effectiveness of this approach.

  S3. The experiments show improvements with the ablation study.

### Weaknesses
W1. The main weakness of this paper is its claimed novelty in defining a new scenario that "forecasts and detects anomaly points in the future signal". However, prediction-based anomaly detection methods already address similar tasks by identifying anomalies through trend forecasting in time series. For example,  "Timeseries anomaly detection using temporal hierarchical one-class network"[1] and "Beyond Sharing: Conflict-Aware Multivariate Time Series Anomaly Detection"[2]. The authors should include and compare these existing models by novelty and effectiveness.

  W2. Meanwhile, "Precursor-of-Anomaly Detection for Irregular Time Series" [3] already introduces a novel task for precursor of anomaly detection, which not only examines current anomalies but also predict potential anomalies in future signals. This paper lacks innovations and novelty in task definition and ignore these most related works and baselines.

  W3. As the paper consider the anomaly probability by random anomaly injection, the authors should also include related works of existing probability models and and anomaly injection models, and compare them by novelty and effectiveness, such as "CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation"[4] and "AutoTSAD: Unsupervised Holistic Anomaly Detection for Time Series Data"[5]. 


  W4. Directly using MSE loss to compute AAFN's output anomaly probability with the true labels is not a compatible approach. The authors should explain why they choose MSE.


  W5. Injecting random anomalies into the future predictions in \( X_{out} \) seems unreasonable. Anomaly prediction should be based on known historical trends, and injecting anomalies into future time segments is more likely to cause errors. For example, how to make decision that one historical trends should injecting anomalies into future time segments and another historical trends should not inject anomalies into future time segments. Moreover, this design disrupts the true normal trend, making it challenging for the model to distinguish genuine anomalies from normal sequences.

  W6. \( M \) and \( N \) determine the number of anomaly prompts and the number of best-matched prompts with the input signal, respectively. The paper lacks specific selection ranges for \( M \) and does not provide guidance on whether adjustments are needed based on the requirements of different domains.

  W7. To ensure the reproducibility of this work, can you make the code anonymously publicly available?

### Questions
See weaknesses.

Q1: Why does the paper lack classic anomaly detection and prediction models? The authors should add more baselines for comparison, such as [1-5].

Q2: Why only a single baseline and a non-optimal one are used for comparison in the *Results on Forecasting* and *Results on Diverse Tolerances* experiments?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel time series scenario, "anomaly prediction," where time series forecasting and anomaly detection are conducted simultaneously. First, it proposes a new AAFN designed to enhance anomaly-aware time series forecasting. Additionally, the paper presents an SAP module, incorporating a novel concept called APP. These APPs are trainable parameters that represent different types of anomalies. The proposed approach jointly trains this module by optimizing a predictive loss, a reconstruction loss, and two newly designed intra-signal and inter-signal correlation losses. Finally, in the main stage, part of the parameters from the AAFN and SAP modules are frozen, allowing for training of the anomaly prediction task to achieve both anomaly-aware forecasting and anomaly detection in time series data.

The key contributions of this paper include:

1. Proposing an interesting and novel application scenario in time series data, "anomaly prediction."
2. Designing the AAFN model to enable anomaly-aware time series forecasting.
3. Developing the SAP module with partially trainable parameters that provide anomaly indications, which effectively support the subsequent anomaly prediction task.
4. Conducting comprehensive experimental evaluations and ablation studies.

### Strengths
1. This paper proposes a novel and compelling time series scenario, "anomaly prediction," which considers anomaly information during time series forecasting while simultaneously performing anomaly detection.
2. For each target, dedicated loss functions are designed to address specific objectives effectively.
3. Extensive experiments are conducted to demonstrate the method's effectiveness.

### Weaknesses
1. While the problem definition is interesting, in my opinion, predicting future anomaly patterns under the current theoretical framework is impractical. The connection between current anomalies and future anomalies is often weak in many scenarios. Your experimental results indirectly support this view, as the F1 scores after point adjustment mostly fall below 0.5, which is unacceptable in anomaly detection. Even with an F1 of 0.9, many false alarms are likely; an F1 of 0.5 would mean that operations personnel would be handling alerts almost daily.
2. Anomalies are generated through injection, which may lead the SAP module to learn anomaly parameter information that does not accurately reflect real-world anomaly scenarios. Likewise, the parameters learned by AAFN might differ significantly from those that would represent anomalies in real environments.
3. There are some grammatical errors, such as "figure 3" in line 235.
4. The design of numerous loss functions risks complicating training and requires additional effort to optimize parameters.

### Questions
1. There is still significant room for development in time series forecasting, especially in long-term forecasting, which presents numerous challenges due to high randomness. How do you conclude that time series forecasting can be performed concurrently with anomaly detection?
2. In the AAFN, you handle anomalies similarly to a 0-1 classifier. However, in real-world scenarios, classifiers cannot manage the complexities of time series anomaly detection. Furthermore, your anomalies are synthetically injected, which greatly differs from real-world environments. How, then, is the effectiveness of AAFN achieved?
3. In my opinion, the SAP module includes time series forecasting but does not consider anomaly information, while the AAFN includes time series forecasting and does consider anomaly information. Why are there two separate forecasting modules? Could this be redundant? And why does the SAP module’s forecasting omit anomaly information?
4. Upon reproduction, it appears that DCdetector and the anomaly-transformer are not the state-of-the-art in anomaly detection. Using other methods might yield better results. Additionally, you mentioned that time series forecasting tends to predict future normal patterns, so are the comparative methods used in your experiments appropriate? Shouldn’t you also train the baseline models on time series data with substantial injected anomalies for consistency?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addressed an interesting scenario named Anomaly Prediction (AP), where the model needs to detect abnormal time points from the unarrived future signals. It tackled this issue by establishing a unified architecture that shares the feature extractor for forecasting and anomaly detection models.

### Strengths
S1. Time series anomaly prediction is important to various domains.

  S2. This work focuses on an important problem that could have real-world applications.

  S3. Appropriate ablation studies.

  S4. Experimental results on various datasets.

### Weaknesses
W1. Codes and more implementation details should be provided for reproducibility.

  W2: There are too few baseline methods for comparison. Many important related works and baselines are missing, such as [1] and [2]. Without caparison to these existing related works, the contributions and novelty in this paper are flawed.

[1]Multivariate Time-Series Anomaly Detection with Temporal Self-supervision and Graphs: Application to Vehicle Failure Prediction. ECML 2023.

[2]Time Series Based Data Explorer and Stream Analysis for Anomaly Prediction. 2022.

  W3. The evaluation metrics reported in the work are relatively limited. Can the performance of the algorithm be reflected on other diversified metrics. Such as "AUC-ROC", "VUS_ROC", "VUS_PR"[3].  Including additional or alternative evaluation metrics could provide a more comprehensive assessment of AD methods, especially in complex scenarios.

[3] Volume Under the Surface: A New Accuracy Evaluation Measure for Time-Series Anomaly Detection.

  W4. The specific innovation points of the entire article are insufficient, mostly utilizing existing technologies, such as the forecasting mechanism are widely used in anomaly tasks. The authors should add more clarification on motivations for why they choose these existing technologies.

  W5. The writing quality of the article is poor and many related works are missing, making it difficult to follow, and the charts are not clearly presented. For example, Figure 2 of 68 is labeled incorrectly, it should be Figure 1.

### Questions
See weaknesses.

Q1: More benchmarks, such as UCR [4] should be considered. The authors should justify their choice of datasets and explain why they believe their current selections are sufficient or how they plan to expand their evaluation.   

[4] Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress.

Q2: Why are the experiments in Table 8 not conducted when t<10, especially when t=0. Please discuss the implications of using t=0 or very small t values for evaluating the precision of the anomaly prediction method.

Q3: Why were the experiments in Table 3-8 only conducted on a few datasets, especially the experiments in Tables 7 and 8 were only conducted on MSL.

### Soundness
2

### Presentation
1

### Contribution
1
