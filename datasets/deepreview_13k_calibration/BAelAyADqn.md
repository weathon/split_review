# MuHBoost: A Multi-Label Boosting Method For Practical Longitudinal Human Behavior Modeling

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Longitudinal human behavior modeling has received increasing attention over the years due to its widespread applications to patient monitoring, dietary and lifestyle recommendations, and just-in-time intervention for at-risk individuals (e.g., problematic drug users and struggling students), to name a few. Using in-the-moment health data collected via ubiquitous devices (e.g., smartphones and smartwatches), this multidisciplinary field focuses on developing predictive models for certain health or well-being outcomes (e.g., depression and stress) in the short future given the time series of individual behaviors (e.g., resting heart rate, sleep quality, and current feelings). Yet, most existing models on these data, which we refer to as ubiquitous health data, do not achieve adequate accuracy. The latest works that yielded promising results have yet to consider realistic aspects of ubiquitous health data (e.g., containing features of different types and high rate of missing values) and the consumption of various resources (e.g., computing power, time, and cost). Given these two shortcomings, it is dubious whether these studies could translate to realistic settings. In this paper, we propose MuHBoost, a multi-label boosting method for addressing these shortcomings, by leveraging advanced methods in large language model (LLM) prompting and multi-label classification (MLC) to jointly predict multiple health or well-being outcomes. Because LLMs can hallucinate when tasked with answering multiple questions simultaneously, we also develop two variants of MuHBoost that alleviate this issue and thereby enhance its predictive performance. We conduct extensive experiments to evaluate MuHBoost and its variants on 13 health and well-being prediction tasks defined from four realistic ubiquitous health datasets. Our results show that our three developed methods outperform all considered baselines across three standard MLC metrics, demonstrating their effectiveness while ensuring resource efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel approach named MuHBoost to model longitudinal human behavior. It is based on large language models (LLM) and aims to address the limitations of prior related works: inadequate consideration of realistic data type and the consumption of computing resources.

### Strengths
1. the proposal of MuHBoost as a resource-efficient multi-label classification method holds promise for solving the problem of multi-outcome health prediction.
2. The inclusion of both time series and ancillary data demonstrates the versatility of dealing with heterogeneous data formats common in health behavior modeling.
3. Comparative analyses show that MuHBoost generally outperforms benchmark methods on a variety of datasets, demonstrating its effectiveness.

### Weaknesses
1.The limited sample size of some datasets may affect the generalizability of the findings. This issue is only briefly acknowledged. The authors should provide a more thorough discussion on how the small sample sizes in certain datasets might limit the applicability of MuHBoost to broader contexts, especially when compared to methods that rely on larger datasets for training. A more detailed analysis of the potential biases introduced by these small samples is needed.
2. Scalability issues remain, especially in terms of the computational resources required when using MuHBoost for larger datasets or a wider range of applications. The paper lacks a detailed analysis of the computational complexity of MuHBoost, especially in relation to the number of labels and the length of the time series data. This is crucial for understanding the practical limitations of the method. The authors should also address the memory footprint of the model, which is particularly relevant when dealing with high-dimensional time series data.
3. The ideas presented in the article should be supported by more detailed derivation of the principle formulas. The paper lacks a rigorous mathematical foundation, making it difficult to understand the underlying mechanisms of MuHBoost. The authors should provide a step-by-step derivation of the core equations, including the loss function and the optimization process. This would enhance the reproducibility and interpretability of the proposed method.

### Questions
1.	In Section 1, the authors need more explicit narration of how their model tackles the three challenges presented. Adding a clearer distinction between MuHBoost and previous LLM-based approaches would help readers better understand the unique contributions of the model.

2.	In Section 2, most of the Multi-Label Classification related works are a bit out-of-date, more recent works (2023/2024) should be included.

3.	In Section 3, “the increased computational burden due to longer and more complex prompts may lead to hallucinations from LLMs”needs more solid proof. The hallucination of LLM is a widely and deeply studied topic, the authors haven’t provided clearly (experimentally/theoretically) how their proposed method addresses this issue.  For section 3.1: The data transformation process could be graphically illustrated to make it clearer to readers who are not familiar with data aggregation techniques.

4.	In Section 4, some of the compared baselines are too old (e.g., Random Forest and XGBoost). The state-of-the-art results are not convincing enough. 

5.	In Section 4 and Appendix C.3, the resource consumption problem is not fully elaborated. The time complexity analysis needs further proof. In addition, more experimental indicators (e.g., FLOPS) should be included to prove the efficiency of the proposed method.

### Soundness
3

### Presentation
3

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
This paper proposes a LLM-based method for multi-label classification, with focus on longitudinal human behavior. Built on SummaryBoost, this paper aims to address two limitations in the existing framework. First, the data could be heterogeneous in terms of data type (e.g., continuous measurements such as heart rate, and categorical responses, such as EMA data). Second, minimize the consumption of computing, time etc for inference. The proposed MuHBoost can handle the heterogeneous data type and enable efficient MLC. At the same time, two variants are proposed to mitigate hallucinations from LLMs. Extensive numerical experiments are conducted to evaluate the performance of the proposal, showing its potential advantages in longitudinal human behavior.

### Strengths
1. The paper identifies some significant issues of the existing LLM-based prediction methods, especially when dealing with multi-labels in longitudinal human behavior data. 

2. The paper is well-written, and easy to follow, even if I do not have much research experience in this area.

3. The proposed enhancement for MuHBoost is helpful for small sample size problem, where N < 2^Q.

### Weaknesses
1. I don't think the proposed method can handle realistic high-dimensional time series, for example, movement, heart rate data collected from smartwatch. In the numerical experiments, the highest dimensionality of consideration is less than 30. Traditional machine learning, such as (Zhang et al., 2024) can handle very high frequency time series data (seconds, minutes), which can capture the human behavior in much finer level. Therefore, I think it is essential to discuss the limitations of the proposed method for high-frequency time series data, or justify the performance in numerical experiments, for example, authors can test the proposal on LifeSnaps dataset with much finer data. In addition, the authors may compare the proposal with the aforementioned method for prediction. If it is difficult to handle high-frequency time series data in the current proposal, authors may discuss how their method can be extended to those realistic settings.

Reference: Zhang, J., Xue, F., Xu, Q., Lee, J. and Qu, A., 2024. Individualized dynamic latent factor model for multi-resolutional data with application to mobile health. Biometrika, p.asae015.

2. I think the enhancement of MuHBoost in Section 3.3 lack novelties. Two approaches are largely motivated by two papers mentioned in the text. Specifically, LP+ is motivated by (Nam et al., 2017) while CC relies on the AdaBoost.C2 (Li et al., 2023). Please emphasize the novelties differentiated from these papers. Emphasize its benefits when adapting these approaches to the MuHBoost.

### Questions
1. In the original SummaryBoost paper, the numerical results show that SummaryBoost actually perform worse than traditional Xgboost when datasets have many continuous features. I think this is also the case for longitudinal human behavior data, such as heart rate. Did authors observe this phenomenon in the experiments? 

2. Following the question 1, what are the input for MLkNN and MLTSVM? are they original measurements or embedding of text information or something else?

3. I think it worth comparing the proposed method with some traditional machine learning algorithms dealing with longitudinal data, such as RNN-type methods.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces MuHBoost, a multi-label boosting approach for predicting health and well-being outcomes from longitudinal human behavior data. MuHBoost is designed to address challenges associated with heterogeneous data, missing values, and computational demands in existing models. By incorporating LLM prompting with multi-label classification, MuHBoost aims to predict multiple health outcomes concurrently. Additionally, two variants of MuHBoost are proposed to manage potential hallucinations in LLMs, potentially enhancing model robustness. Evaluated on 13 prediction tasks using four health datasets, MuHBoost reportedly outperforms baseline models across multiple metrics, with resource efficiency highlighted as a key feature

### Strengths
* Demonstrates how LLMs can be used as multi-label boosting method for temporal tabular data and auxiliary tabular data.

### Weaknesses
 * Iterative improvements on prior SummaryBoost work with limited novelty
	* The new data conversion uses a seemingly straightforward two-step approach based on LLM prompting in Section 3.1. The prompting itself does not seem to be very innovative, and while Table 2 does demonstrate an empirical performance increase, it is unclear how exactly each step of the two step approach helped. Specifically, the first step involves generating a textual description of the time series data, and the second step uses that description to generate features. It is not clear what specific aspects of the textual description are most important for the feature generation, and how this approach compares to more direct feature extraction methods.
	* MuHBoost modifies the original ClusterSampling algorithm by emphasizing rarer classes in the sampling procedure, then the follow-up methodologies MuHBoost[LP+] and MuHBoost[CC] seem to be straightforward adaptations of prior methods from Nam et al., 2017 and Adaboost.C2. The adaptation of the label propagation method seems particularly incremental, as it primarily involves modifying the inference prompt for the LLM. The classifier chain approach, while potentially useful, also appears to be a direct application of existing techniques to the LLM setting.
	* Prior work section does not seem to contextualize the importance and relevance of SummaryBoost, especially in context of the longitudinal ubiquitous computing domain.

### Questions
Comments:
* \cite is incorrectly used throughout the paper when \citep should be used

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors consider the task of using longitudinal ubiquitous health data to predict human behavior. They create a model, called MuHBoost, based on both LLMs (SummaryBoost model methodology) and multilabel classification (label powerset and classifier chain methods). The authors compare their model to various baselines and show that MuHBoost outperforms all baselines and presents two key advantages: (i) MuHBoost can consider different feature types and missing values and (ii) MuHBoost requires less computing time and cost. To address LLM hallucination the authors also build two extensions of their base model (which result in better performance). The authors apply their model to 4 datasets to predict psychology, student performance, and drug use.

### Strengths
S1 - Important application. The authors investigate an important application of longitudinal human behavior modeling with applications to patient monitoring, interventions for drug users, etc.

S2 - Multiple datasets: The authors evaluate their model on multiple, diverse datasets with a range on the number of labels (ranging from 2 to 6 labels).

S3 - Multiple baselines and metrics: The authors compare their model to a diverse set of baselines and evaluate on multiple standard MLC metrics.

S4 - Multiple robustness checks: The authors run various robustness checks including on SummaryBoost’s extract-then-refine procedure and on the use of GPT4 (more resource expensive) vs GPT3.5 (less resource expensive).

### Weaknesses
W1 - Needs more background clarification: The main weakness of the paper is a lack of background clarification. The authors should give more clarification on the SummaryBoost, LP and CC methods which the MuHBoost model is built off of. Specifically, the paper lacks a detailed explanation of how SummaryBoost operates, including its core mechanisms for feature summarization and refinement. Without this, it is difficult to fully understand the novelty and contribution of MuHBoost. The descriptions of Label Powerset (LP) and Classifier Chains (CC) are also too brief, lacking details on their specific implementations and limitations within the context of the proposed model.

W2 - Comparison to multilabel text classification: The authors state that the use of LLMs for MLC type prediction tasks have been done in multilabel text classification works. How do these methods compare to MuHBost? It is unclear how the proposed method differentiates itself from existing approaches in multilabel text classification that also leverage LLMs. The paper should provide a more thorough comparison, highlighting the specific advantages and disadvantages of MuHBoost compared to these existing methods, particularly regarding the types of data they handle and their performance characteristics.

W3 - Statistical significance: Are the results in table 1 statistically significant? The paper presents results in Table 1, but it's unclear whether the performance differences between MuHBoost and the baselines are statistically significant. The lack of statistical significance testing makes it difficult to assess the robustness of the results and the true advantage of the proposed method. Reporting only average performance across splits is insufficient to establish the superiority of MuHBoost.

W4 - Only binary class predictions: The authors claim that MuHBoost presents an advantage over prior work because their model can consider different feature types. However, all experiments run in the paper only consider binary class predictions. Have the authors evaluated the model on other feature types as well (e.g. categorical/continuous prediction)? The claim that MuHBoost can handle different feature types is not fully supported by the experimental results, which are limited to binary classification tasks. The paper should provide empirical evidence demonstrating the model's ability to handle categorical or continuous features in a multilabel setting, or at least acknowledge this limitation.

### Questions
1. How do the authors combine data descriptions across topics?
2. For the two psychology datasets (LifeSnaps and GLOBEM), why are some tasks (e.g., negative emotions or anxiety) defined differently across datasets?
3. When describing baselines in Section 4.2, what do problem transformation and algorithm adaptation mean?

Minor comments / suggestions: 

- Throughout I recommend using parenthetical citations (citep instead of cite)
- At multiple points, footnotes referenced in the main text were placed in the appendix. Could each footnote be placed on the page they are first referenced on?
- Line 081: “have the two following”
- Line 206: “require” instead of “requires”

### Soundness
4

### Presentation
2

### Contribution
3
