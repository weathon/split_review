# TimeRAG: It's Time for Retrieval-Augmented Generation in Time-Series Forecasting

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Time-series data are essential for forecasting tasks across various domains. While Large Language Models (LLMs) have excelled in many areas, they encounter significant challenges in time-series forecasting, particularly in extracting relevant information from extensive temporal datasets. Unlike textual data, time-series data lack explicit retrieval ground truths, complicating the retrieval process. To tackle these issues, we present TimeRAG, a novel retrieval-augmented approach tailored for time-series forecasting. Our method uniquely applies to continuous and complex temporal sequences, and it is trained using LLM feedback, effectively addressing the absence of ground truth and aligning the priorities of the retriever and the LLM. Experimental results demonstrate the effectiveness of TimeRAG, highlighting its ability to significantly enhance forecasting performance and showcasing the potential of LLMs in time-series prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a retrieval-augmented generation (RAG) framework specifically designed to improve time-series forecasting with large language models (LLMs). To address LLMs’ challenges with continuous temporal data, TimeRAG retrieves and embeds relevant historical data sequences in JSON format, making sequential dependencies more accessible to the model. This approach leverages LLM feedback to train the retriever, allowing it to prioritize historical sequences that align with predictive tasks such as stock movement forecasting. Evaluations across financial datasets demonstrate TimeRAG’s superiority over traditional LLM methods, suggesting its potential to enhance forecasting accuracy by focusing on task-aligned, contextually relevant data.

### Strengths
1. The "comprehension gap" TimeRAG addresses by structuring time-series data in JSON is tailored to LLM processing. This unique formatting approach is not emphasized in LLM-Embedder and is essential for making continuous data accessible to LLMs.
2. TimeRAG demonstrates its effectiveness specifically in stock movement prediction across multiple time-series datasets. This evaluation focuses on Matthews Correlation Coefficient (MCC) and Accuracy (ACC), which are metrics relevant for forecasting accuracy rather than general retrieval quality.

### Weaknesses
1. Problem Formulation Issue
    - Framing time-series forecasting as a binary classification task is unconventional and raises concerns regarding the model’s applicability. This approach simplifies the problem, reducing the predictive granularity necessary for effective forecasting. The reduction to a binary 'rise' or 'fall' classification discards valuable information about the magnitude of price changes, which is crucial for practical trading strategies and risk management. Furthermore, this binary view fails to capture the nuances of market behavior, such as periods of low volatility or sideways movement, which are critical for a comprehensive understanding of market dynamics.
    - Additionally, limiting predictions to only "rise" or "fall" cases ignores the frequent occurrence of "freeze" or neutral movements, a common scenario in real-world financial data. Excluding this category may significantly hinder the model’s practical utility and its ability to generalize across diverse market conditions. The absence of a 'neutral' category means the model is forced to misclassify these periods, potentially leading to inaccurate performance metrics and unreliable predictions in real-world scenarios where such periods are common.

2. Lack of Novelty Compared to LLM-Embedder
    - The methodology in TimeRAG closely mirrors the framework established in LLM-Embedder, lacking clear innovation. Key components, such as reward formulation based on LLM feedback, knowledge distillation using KL Divergence, and in-batch negative sampling (contrastive learning), are replicated with minimal adaptation. These similarities suggest limited original contribution. The core architecture and training process appear to be a direct application of LLM-Embedder's techniques, with the only modification being the input data format, which does not constitute a significant methodological advancement.

3. Lack of Non-LLM Baselines in Time-Series Forecasting
    - The evaluation lacks comparisons with established time-series forecasting models outside the LLM domain. Forecasters like PatchTST and DLinear, widely regarded as effective baselines, are notably absent. Incorporating these models would provide a more comprehensive and rigorous performance benchmark, better situating TimeRAG’s effectiveness within the context of time-series forecasting research. Without these comparisons, it is difficult to ascertain whether TimeRAG's performance gains are due to the novel approach or simply the inherent capabilities of the underlying LLM, especially when compared to state-of-the-art time-series specific models.

### Questions
1. Suggest switching the time-series forecasting task from classification to regression. This would allow the model to capture continuous trends in the data, which is generally more appropriate and beneficial for real-world forecasting applications.
2. In Table 4, the content appears to be graphical and might be better presented as a figure. Additionally, could you clarify whether t-SNE was used for dimensionality reduction in this visualization? This detail would help in interpreting the retrieval model’s embedding performance.

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
In this paper, the author proposed a RAG approach to retrieve historical trades from other stocks to help LLM to better predict the trend of the target stock in the future. After preparing the positive candidates, a retriever model is trained. Experiments are conducted on real-world stock datasets and show the effectiveness of the proposed method.

### Strengths
1. The experiments are conducted on real-world stock datasets and the proposed method outperforms many baselines.

### Weaknesses
1. The presentation of the paper needs significant improvement. I feel it difficult to follow. Motivation is not clear and figures technical part are difficult to follow. See Q1-Q4.
2. The experimental settings are vague, which makes it difficult to reproduce the results. How the training split is conducted? Which are the hyperparameters and how did the authors tune them? See. Q5
3. Only LLM baselines are compared. The authors should include more non-LLM baselines, e.g. classic time series classification models. See. Q6-Q7.

### Questions
1. The motivation is not clear. With only numerical data, why can LLM do the job of stock trend prediction, if only a little text (e.g. open price, volume.) information is used?  Why not try some basic ML models for this task? What is the intuition behind using LLM? The authors are suggested to better motivate the paper with an example showing which kind information do LLM use in the RAG.
2.  Figure 1 is difficult to understand. There are two almost identical prompts in Task definition prompt. What are the relationships to the results shown above and below them. The authors are suggested to improve the presentation of the figure.
3. How do you derive P(c) in Section 3.2 specifically? Please give the detailed steps.
4. What do you mean by LLM's rewards? Please clarify.
5. The experimental setting is not clear. Which part of the datasets are used for training/validation/testing and hyperparameter settings? Please clarify. 
6. Some good results are shown, but the intuition is not clear. What retrieved the content helped LLM to answer better? The case study is not helpful for understanding this. The authors should include more non-LLM baselines, e.g. classic time series classification models. 
7. The term time series forecasting may not be accurate. It is more related to forecasting the exact value in the future. Time series trend forecasting may be more appropriate for the paper.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work investigates a retrieval augmented generation-enhanced stock series prediction model using LLM feedback, addressing the absence of ground truth and aligning the priorities of the retriever and the LLM. Experimental implementations across four stock datasets including ACL18, BIGDATA22, CIKM18, and Stock23 have verified the effectiveness of proposed TimeRAG.

### Strengths
- S1. Good paper organization and it is easy to read.

- S2. The propsed TimeRAG can leverage the LLM feedback to train the retrieval, which employs the KL-divergence to minimize the gap between the distributions of candidates computed and those predicted by the embedding model, results in an outcome-oriented approach to filter relevant data from extensive historical contents.

- S3. The experimental results on four real-world datasets show the superiority of the proposed solution. And experiments also verify the motivation of RAG (retrieval-based generation).

### Weaknesses
 - W1. The title of 'TIMERAG: IT’S TIME FOR RETRIEVAL-AUGMENTED GENERATION IN TIME-SERIES FORECASTING' may be not suitable, as the authors only investigate and implement experiments on only one task, i.e., stock series prediction. More experiments on various domains are required or the modification of the title is needed.

- W2. Lacking generalization capacity. The proposed TimeRAG requires re-training the model for each stock, results in the limited generalization capacity.

- W3. Short of literature review, evaluation baselines and issues on technical contributions. There are many baselines using LLM for time-series prediction, but have not been compared in this work. To name a few but not all, e.g., Time-LLM [1], LLMTime [2], GPT4TS [3]. More discussions on these abovementioned works and select some of them as baselines for comparisons are encouraged. Also, to my knowledge, there are other financial rag models such as AlphaFin [4] and FinGPT [5]; you should compare your model's performance with theirs. Therefore, the technical contributions of this work should be emphasized and distinguished.

- W4. This work only investigates the learnable scheme on retrieval side, but is there any designs for coupling the stock prediction with RAG from the LLM side or prompt side? Can learnable elements be inserted into the prompt side? More discussions or prospective solution should be presented.

### Questions
Please see my weaknesses.

### Soundness
2

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
In this paper, the authors proposed a retrieval augmented generation for time series prediction, specifically on the stock movement prediction. The main challenge is the lack of ground truth data for retriever and the authors proposed to use outcome-oriented feedback from the LLM to guide the retriever. The retriever is optimized through contrastive learning with positive and negative samples defined by the LLM’s probability of generating correct trend. The authors showed experimental result that demonstrated the advantage of the proposed RAG framework compared to pretrained language models and other retrieval models.

### Strengths
Strength: this is the first work that attempts to address RAG for continuous, temporal signals. 

The challenges for applying RAG on time series are well motivated and clearly explained.

### Weaknesses
Limitation: The scope of this paper is limited. This is not exactly time series forecasting, the title is somewhat misleading as the experiments are purely focused on stock price movement prediction. The baseline choices are irrelevant to time series forecasting. 

Some choices of the setting is not well-justified: “select the top-1 sequences as a positive candidate and the last 15 sequences as negative candidates.” It’s not clear how this is decided. The selection of negative samples, specifically using the *last* 15 sequences, is concerning. This could introduce bias, as these sequences are likely to be temporally correlated with the query sequence, making them poor negatives for contrastive learning. A more robust approach would involve selecting negative samples from a broader range of the historical data, or even from different stocks, to ensure the model learns to distinguish truly dissimilar patterns.

“we don’t predict the freeze movement in query sequences, we only use it to calculate the recent movement list. In this way, we filter out minor and statistically insignificant price movements, thereby focusing on more significant trends.” the freeze situation also seems important as many people would like to know if the stock price will remain relatively stable. Ignoring periods of stability could limit the model's practical applicability, as predicting periods of no change is often just as important as predicting price fluctuations.

The presentation of the paper can be improved such as adding a main figure for the overall pipeline. Additionally, in figure 1 the grey text are not explained. Is it a task definition prompt that was tried but discarded for use in the end. The only explanation is “An example is highlighted in gray in Figure 1. In these trials, we name the list of open prices in the recent five days as ’open price’, ’open list’, or ’recent open list’. Once we definite feature names, we use the same name for candidate features.” but this explanation is not concerned with the task definition prompt at all. The lack of clarity regarding the grey text in Figure 1 is a significant issue, as it obscures the experimental setup and makes it difficult to reproduce the results. The description provided does not clarify the purpose of these alternative prompts, leaving the reader to guess their role in the overall methodology.

The outcome oriented model may lack generalizability to other applications.

### Questions
Questions: 

- why is historical data of the same stock chosen as candidates instead of other stocks from the same & very recent periods. The intuition is that recent stock prices or other stocks from same period may have more influence on the future trend of the query stock. It seems counterintuitive that some distant past of the same stock would help prediction.
- In the candidate sequence representation section, it’s mentioned that “After trials, we find the movement and recent movements of candidate sequences are noise for prediction. Therefore, we remove these two features, as is shown in Figure 1.” However, it’s not clear what trials are done. How much data are used for these trials?
- I’m a little puzzled in the case study (figure 4), does retrieving the closest datapoint justify “model is effectively capturing the subtle patterns and dynamics in the time-series data, enabling more accurate retrieval.”? From my understanding, it could well be the case that the information retrieved could be complementary information not present in the input data and that would still effectively help the model and be considered good retrieval. This figure feels like the retriever acts like a KNN model (k=1).

### Soundness
2

### Presentation
2

### Contribution
2
