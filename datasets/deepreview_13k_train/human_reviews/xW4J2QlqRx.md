# Context Matters: Leveraging Contextual Features for Time Series Forecasting

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Time series forecasts are often influenced by exogenous contextual features in addition to their corresponding history. For example, in financial settings, it is hard to accurately predict a stock price without considering public sentiments and policy decisions in the form of news articles, tweets, etc. Though this is common knowledge, the current state-of-the-art (SOTA) forecasting models fail to incorporate such contextual information, owing to its heterogeneity and multimodal nature. To address this, we introduce ContextFormer, a novel plug-and-play method to surgically integrate multimodal contextual information into existing pre-trained forecasting models. ContextFormer effectively distills forecast-specific information from rich multimodal contexts, including categorical, continuous, time-varying, and even textual information, to significantly enhance the performance of existing base forecasters. ContextFormer outperforms SOTA forecasting models by up to 30% on a range of real-world datasets spanning energy, traffic, environmental, and financial domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a work on aggregating contextual information into time series forecasting. Specifically, the authors propose to use a universal context encoder to encode the contextual information as embedding and boost the time series forecastor with the encoding. Experimental results suggest that the contextual information boost the performance.

### Strengths
The writing is easy to follow

### Weaknesses
1. The contribution is limited. This paper mainly discuss about contextual information in time series forecasting. However, it is well known that the contextual information is helpful for time series. What really matters is how to make use of it. In this paper, the authors list three reasons about why it is hard to make use of the information, such as multi modality and non-uniformity across domains. However, when really talking about how to make use of the context, the authors just simply concatenate the category variables with continuous variables. This design is unrelevant with the challenges mentioned. What if some out-of-domain dataset contain some variables that are unseen on the training data? Also, the design is well-justified. Why not align the metadata as one modality (like text) and then convert it to embeddings with one shared encoder? Do we need to align the timely metadata (like news with timestamp) with the speific timestamp before forwarding them all into the cross attention?

2. The theoretic analysis is useless but takes 1.5 pages. All the theoretic results are trivial corollary of conclusions from introductory undergraduate-level text book of information theory and machine learning. I suggest that the authors are just trying to decorate their papers with some theoretic analysis

3. Experimental results are not comprehensive enough. We prefer experiments on more datasets (like ETT) and baselines (like TimesNet).

4. The authors list 4 reasons why they prefer fine-tuning in Sec 5.2. But there is lack of empirical supports. I did not see training curves that reflect the unstable training of all-from-scratch. 

5. The bitcoin-news dataset description is too short. This could be the most insightful part about how to collect contextual data. But there is no details. How and where did you get the data? Are the data filtered? Are the collection based on time or keywords? Some many details are missing.

### Questions
See the weakness

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a framework designed to incorporate exogenous variables into time series forecasting.

### Strengths
1. The presentation is clear.
2. The problem studied is interesting.

### Weaknesses
1. The contribution is limited.
2. There is a lack of comparison with SOTA models.

### Questions
The presentation and problem setup are clear and easy to follow. However, I have two major concerns regarding the theoretical analysis of the benefits of adding exogenous variables and the overall technical contribution of the paper.
1. By definition, mutual information is non-negative. Even in the worst-case scenario where A and C are completely independent, the increase in mutual information is 0. A higher mutual information value does not necessarily translate to higher accuracy or better performance. Noisy or even misleading data can also increase mutual information as long as some degree of dependency exists. Could the authors elaborate on this issue?
2. Adding exogenous variables to time series forecasting models is not a novel concept. It is a natural extension of general time series forecasting models and is a dominant approach for work in some domains, such as financial market predictions. For example, older transformer-based models like Autoformer can be adapted to include exogenous variables and are often used as baselines in other papers. Moreover, newer transformer-based models, such as Timexer, also support this approach natively. There are also attempts to use large language models (LLMs) to incorporate exogenous market information for stock movement prediction, such as Plutos. Therefore, I believe the overall contribution of the work is somewhat weak, as it does not introduce a new concept.
3. It is expected that the authors should at least compare the proposed framework with other models that can accept the same input. Otherwise, it is difficult to justify the performance of the proposed framework.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article proposes ContextFormer, a novel plug-and-play framework that utilizes cross-attention blocks to integrate multimodal metadata, including categorical, continuous, time-varying contexts, and even textual information, into existing any context-agnostic base forecasters. The author selects two SOTA models of PatchTST and iTransformer as the base forecasters and validates ContextFormer framework on seven real-world datasets spanning energy, traffic, environmental, and financial domains. Experimental results confirm the effectiveness of the framework.

### Strengths
1. The starting point of this article is good. Exogenous contextual features can indeed serve as key auxiliary information to influence time series forecasting.
2. The paper is mostly well-presented and easy to follow.

### Weaknesses
1. Introduction part summarizes three challenges in incorporating metadata into forecasting models, but this article does not provide a detailed explanation of why ContextFormer can solve these problems. For example, the first challenge mentions the importance of aligning time series history and multimodal metadata. However, there is a lack of evidence on how ContextFormer ensures that the two have been aligned, the alignment effect, and the impact of aligned representation on forecasting results. Although the effectiveness of ContextFormer is reflected in the final MSE/MAE metrics, I mainly focus on these intermediate results and suggest the author to supplement these explanations.

2. In related works part, the author lists some methods for forecasting with covariates. As far as I know, it also includes methods such as TFT, TSMixer, and TimeXer, etc., but this article does not compare with these methods. It is suggested that the author supplements these comparison experiments.
Some references:
TFT: https://doi.org/10.1016/j.ijforecast.2021.03.012,
TSMixer: https://arxiv.org/pdf/2303.06053,
TimeXer: https://arxiv.org/pdf/2402.19072.

3. In Table 2 caption, it is mentioned that "The best results for each base model in each row are highlighted in bold.". However, the results of the Retail dataset (horizon=96, MSE metric) do not match this statement. It is recommended to revise the wording.

4. Doubt about lines 491-492:
    1) The explicit motivation for comparing with Chronos and whether the comparison is fair?  
    2) Are the results in Table 2 sufficient to support this conclusion? I agree with the example provided by the author (486~487), but for other datasets, I have the following questions: (a) Is it still necessary to compare the context-aware model with Chronos for the two datasets of Air quality and Electricity, as the context-agnostic model is already better than Chronos? (b) For the Retail and Bitcoin datasets, Chronos performs the best. I hope the author can provide detailed explanations to alleviate my concerns.

### Questions
Refer to "Strengths And Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ContextFormer, a method designed to incorporate multimodal contextual information into existing time series forecasting models. Traditional models typically rely solely on historical data, neglecting external influences such as news, weather, and market trends that can significantly impact predictions. ContextFormer effectively addresses this limitation by integrating diverse types of metadata—including categorical, continuous, time-varying, and textual information—using cross-attention mechanisms. The experiments demonstrate that ContextFormer can enhance forecasting performance by up to 30% compared to state-of-the-art models across various datasets in fields such as energy, traffic, environment, and finance.

### Strengths
1. As a plug-in solution, ContextFormer can be integrated with various predictive backbones for a diverse array of applications.  
2. The two-stage fine-tuning methodology guarantees that the lower bound of ContextFormer is at least equivalent to that of context-agnostic approaches.
3. The extensive experiments look hopeful.

### Weaknesses
1. **Inadequate Presentation.** The organization of the paper lacks rationality. Excessive emphasis is placed on the importance of external context, which is well-known. The methods section is overly succinct. The descriptions of Metadata Embedding and Temporal Embedding are overly concise, leaving the application dimensions and the output shape ambiguous. Specifically, it is unclear how categorical variables are embedded, what the dimensionality of the continuous embeddings are, and how time-varying features are handled. Furthermore, the embedded interaction in the Information Fusion component is similarly unclear, too. Its applicability to both a single embedding for one variable (iTransformer and PatchTS) and a single embedding for one timestamp (Informer and Autoformer) across two distinct architectures remains uncertain. The paper does not clearly articulate how the cross-attention mechanism is adapted to these different input structures. In summary, the workflow of the algorithm is perplexing.

2. **Limited Innovativeness.** Although the author presents a case in the introduction regarding the influence of news on stock prices, the treatment of this unstructured external text information is only mentioned in Appendix C.7 cursory and lacks corresponding experimental results on BITCOIN-NEWS. The models and data discussed throughout the paper primarily rely on structured auxiliary information, despite incorporating both continuous and categorical variables. The prior research has focused on integrating structured external information to enhance prediction accuracy, including exogenous variables [1] and timestamps [2]. The paper's core contribution remains ambiguous. Moreover, The three challenges outlined in the introduction are unpersuasive. The paper does not clearly demonstrate how the proposed method addresses these challenges in a novel way compared to existing approaches.

3. **Unrigorous Experiments.** As stated in Weaknesses 2, there has been some prior work aimed at integrating structured external information to enhance prediction accuracy. This paper should be compared with these frameworks that utilize external information, rather than solely with models that lack auxiliary information. The current experimental setup does not sufficiently isolate the contribution of the proposed method from the base forecasting models. Furthermore, the paper lacks ablation studies to demonstrate the impact of different metadata types and the specific contribution of the cross-attention mechanism.

### Questions
The authors can refer to the weakness listed above.

### Soundness
2

### Presentation
2

### Contribution
2
