# MoAT: Multi-Modal Augmented Time Series Forecasting

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Time series forecasting plays a pivotal role in various domains, facilitating optimized resource allocation and strategic decision-making. However, the scarcity of training samples often hinders the accuracy of the forecasting task. To address this, we explore the potential of leveraging information from different modalities that are commonly associated with time series data. In this paper, we introduce MoAT, a novel multi-modal augmented time series forecasting approach that strategically integrates both feature-wise and sample-wise augmentation methods to enrich multi-modal representation learning. It further enhances prediction accuracy through joint trend-seasonal decomposition across all modalities and fuses the information for the final prediction. Extensive experiments show that MoAT outperforms state-of-the-art methods, resulting in a substantial reduction in mean squared error ranging from 6.5% to 71.7%, which demonstrates the effectiveness and robustness in addressing the limitations imposed by data scarcity. The datasets and code are available at https://anonymous.4open.science/r/MoAT-201E.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on multi-modal time series forecasting, particularly the text data augmented time series. It includes three main components, i.e., patch-wise embedding, multi-modal augmented encoder, and a trend-seasonal decomposition. 
The experimental evaluation is through several financial datasets.

### Strengths
1. This paper focuses on an interesting applied problem, i.e., exploring the integration of text data into time series to enhance forecasting.
This problem is not new and widely studied in quantitative finance, data mining, etc. 

2.  The experimental evaluation is conducted on several real financial price data across different markets. The authors augment the time series by collecting real news from news data providers. These datasets, if open-sourced, would be very helpful for the community.

### Weaknesses
1. This paper is mostly applied and combines several existing techniques, e.g., patch-wise embedding, and pattern decomposition.
The authors are expected to better position this work by clarifying the technical novelty, contribution, or new insights. Specifically, the combination of patch-wise embedding and trend-seasonal decomposition, while individually established, requires a more detailed justification for their synergistic effect within this multi-modal context. The paper needs to articulate why this particular combination is more effective than other potential pairings of time-series analysis techniques.

2. The evaluation is mostly on financial datasets. But for finance, the error metric MSE is not the main interest, since in the real world the prediction is to serve downstream tasks, e.g., portfolio construction, risk management, etc, and practically MSE does not directly translate to the improvement for downstream tasks. It would be better to show the prediction by the proposed method can facilitate an example downstream task. e.g., portfolio construction is commonly used. Furthermore, the paper should address the limitations of MSE in capturing the nuances of financial time series, such as volatility clustering and fat tails, which are crucial for risk management. A more comprehensive evaluation should include metrics that are more relevant to financial applications, such as Sharpe ratio or maximum drawdown when applied to a portfolio construction task.

### Questions
1. On page 5, the part "multi-modal augmented encoder" is essentially a combination of time series and text modalities, and what does the "augmented" refer to? 

2. On page 6, in the part "joint trend-seasonal decomposition", trend-seasonal decomposition is reasonable for time series because of the underlying generative process. But, for text data, especially the embedding of news text, applying trend-seasonal decomposition is not intuitively understandable. News content is highly dependent on real-world happenings where the trend-seasonal decomposition is not necessarily existent. 

3. In Table 1,  MSE are mostly low-magnitude values, while the real price of the finance assets of the data used in the experiment differs greatly in magnitudes. Is this due to some data standardization? If so, it is better to report the errors in the original scale of data, because the prediction on the standardized domain would be less useful for downstream tasks in many cases.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose MoAT, multi-modal augmented general time series forecasting model that leverages multi-modal cross fusion and prediction synthesis

### Strengths
- originality: new application of multimodal time series for general time series forecasting
- quality: extensive experiments with good results, many ablations
- clarity: well-written paper, good structure
- significance: time series forecasting and foundation models are timely and relevant

### Weaknesses
 - Lack of experiments assessing whether the model performs well with scarce data, which is painted as the main motivation of MoAT. Furthermore, figure 5c does not seem to corroborate the story that MoAT performs significantly better than other methods with data scarcity (hard to say without variance). MoAT still seems to derive its main performance improvements from increasing the train ratio.

- Lack of details in the caption of the T-SNE decomposition between time series and texts.

- The remarks about information uniqueness of cross-modal vs unimodal representations are not backed up, no reason for their contained information to be unique.

- Not obvious that the text data trend-seasonal decomposition actually decomposes into trend and seasonal data, it seems like you just use two sets of attention parameters. How do you actually get these to attend to either trend or seasonal information in the texts? This just seems like it introduces more parameters into the model.

- In fact, there is no comparison of model sizes and various scaling parameters for different methods. If you don't normalize, how do you know your performance increases aren't simply due to scaling up model size?

- Unclear empirical design for hyperparameter tuning. Why default at hidden dim of 64? What does if mean dropout =0.2 "if needed"? Why is the search for optimal learning rates and decay across two values each? If you're limited by compute or have a lot of hyperparameters, random search could be better than grid search.

- Formatting needs more consistency (e.g. "Fig." vs "Figure", figure 5 before figure 4, etc.)

### Questions
- how is text data decomposed into trend and seasonal components?

- What does "(non-)overlapping patches" mean? Clearly patches are overlapping if they share S values.

- Why are the texts unordered at each timestep? Is this a feature of the dataset used, or a design choice to ignore some of the granularity of the timestep?

- Why channel-specific parameters? Channel independence is a strong assumption.

- Is the forecasting in Figure 5 a autoregressive? What are you providing as inputs at each time step? What are the document inputs when autoregressively predicting? The visualization in figure 5 a is so zoomed out as to be uninformative (hard to tell the difference between the methods).

- the motivation for offline prediction synthesis discusses improved parameter efficiency, referencing Liang et al., 2022, but parameter efficiency is not discussed in the rest of the paper, nor when comparing methods? Furthermore, why is modularity desirable in this setting?

- Any intuition as to why MoAT_{time} is the best performer on the Fuel dataset?

- The ablations in table 2 suggest that the augmentations are not really helpful, considering the relative improvement compared to MoAT_{time} and MoAT_{text}. MoAT_{sample} seems pretty performant itself, being the best on Metal and Bitcoin, and second best on Fuel and Covid.

- Ridge regression includes a loss penalty. What weight did you choose for this?

- Why are the prediction lengths so short?


Overall, I'm giving this a 5 before discussion, as the storyline does not seem to align with the experiments. I am happy to amend my score following discussions.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an interesting method for enhancing time-series forecasting by incorporating textual data. It applies both feature-wise and sample-wise augmentation techniques and integrates information about trend and seasonality to improve prediction accuracy. The authors have also contributed to the research community by publishing a new multimodal time-series and textual dataset.

### Strengths
1. The study introduces a new multimodal forecasting framework that integrates sample/feature-wise augmentation, cross-modal fusion, and seasonal-trend decomposition.
2. A new multimodal time-series and text dataset is presented as a contribution to the field.
3. The efficacy of the proposed approach is validated through experiments on six multimodal datasets.

### Weaknesses
1. It requires further clarification why the proposed textual decomposition components map to the trend and seasonality aspects of the time-series data. Specifically, the mechanism by which textual features are aligned with the temporal patterns of trend and seasonality is not clearly defined. The paper should elaborate on how the textual information is processed to extract features that correspond to these specific temporal components, and provide a more detailed explanation of the underlying assumptions.
2. The paper focuses on short-term forecasting, with the horizons in the experiments and even in the Appendix being relatively short when compared to existing benchmarks that typically extend from 96 to 712 timesteps. The limited forecasting horizon raises concerns about the model's ability to capture long-term dependencies and its practical applicability in scenarios requiring extended predictions. The evaluation should include experiments with longer forecasting horizons to demonstrate the model's robustness.
3. The datasets primarily feature monthly or weekly sampling intervals. This raises concerns about the applicability of the approach to datasets with higher frequency sampling, such as hourly, where acquiring corresponding textual information could be challenging. The paper needs to address the limitations of the proposed approach when dealing with high-frequency time series data, and discuss the potential impact of missing or sparse textual data on the model's performance.
4. In Table 2, the MoAT_time model, even without textual data, appears to outperform many baseline models. The specific factors contributing to this enhanced performance are not adequately explained. It is unclear whether the performance gain is due to the model architecture itself or the specific decomposition and patching techniques employed, and a more detailed analysis is needed to isolate the contributing factors.
5. The results in Table 2 suggest that dual augmentation does not significantly enhance performance, questioning its effectiveness in the proposed framework. The marginal improvement from dual augmentation raises concerns about the added complexity and computational cost, and the paper should provide a more detailed analysis of the conditions under which dual augmentation is beneficial.

### Questions
See Weaknesses above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces MoAT (Multi-Modal Augmented Time Series Forecasting), an approach that leverages multimodal data, particularly text, to enhance time series forecasting by addressing data scarcity. In MoAT, text information is embedded into hidden vectors using a pretrained language model and aggregated into patches similar to time series patches. These patched time series and text data are then fed into a multi-modal augmented encoder that combines sample-wise and feature-wise augmentation methods to enrich multimodal representation learning. A joint trend-seasonal decomposition process is employed to capture underlying patterns in the data. The paper pairs all four representations (feature or sample, trend or season) of the two modalities (time series and text) into 16 combinations to make the final prediction. Extensive experiments conducted on real-world datasets demonstrate MoAT's effectiveness compared to previous state-of-the-art methods for single-modal time series forecasting.

### Strengths
- The concept of using multimodal data to tackle data scarcity and enhance time series forecasting is innovative and holds significant promise.
- The datasets collected and soon to be released in this paper will contribute positively to the community.
- The multi-modal augmented encoder, combining sample-wise and feature-wise augmentation, is an interesting and reasonable approach.

### Weaknesses
 - It is not appropriate to directly transfer methods used for processing time series to text data:
   1. As a single value at a specific timestamp provides little information, PatchTST and Crossformer patch time series to form informative tokens. Text data already contains a wealth of information, not to mention that there are multiple texts at each time step, so using patching is unreasonable here. The patching mechanism, designed to create informative tokens from sparse time series data, seems misapplied to text, where each token already holds significant semantic meaning. Applying a patching strategy to text may lead to unnecessary fragmentation of the textual information, potentially hindering the model's ability to capture long-range dependencies and contextual nuances within the text.
   2. The decomposition of text data is unclear, particularly the definitions of "trend" and "season" for text. Equation (6) shows that the so-called trend-seasonal decomposition is just the same attention pooling with different sets of parameters, raising doubts about its ability to capture trend and seasonal dynamics as claimed. The application of trend-seasonal decomposition, a technique rooted in time series analysis, to text data lacks a clear justification. The concepts of 'trend' and 'seasonality' are inherently temporal and do not have a direct analogue in the semantic space of text. The use of attention pooling with different parameters does not inherently capture trend and seasonal dynamics, and the lack of a clear definition of these concepts in the context of text makes this approach questionable.
- Datasets and baselines used in experiments are not so propoer:
  1. Table 3 shows that the largest dataset, Bitcoin， contains only 741 * 4 = 2,964 scalars， while the smallest contains less than 1,000. This raises concerns about the suitability of training complex neural networks with such limited data. The limited size of the datasets, with the largest containing fewer than 3,000 data points, raises serious concerns about the reliability of training complex neural networks. Such small datasets are prone to overfitting, and the performance of the model may not generalize well to unseen data. The use of complex models like transformers on such small datasets is likely to result in memorization of training data rather than learning meaningful patterns.
  2. The main experiment focuses on an input8-output1 setting, with both input and output series being very short. While most selected baselines are for longer term forecasting, i.e. they perform at least input96-output96 task. So the comparison is not so fair. The experimental setup, focusing on very short input and output sequences (input8-output1), does not align with the typical use cases of the chosen baselines, which are designed for longer-term forecasting tasks (e.g., input96-output96). This discrepancy in task settings makes the comparison unfair and limits the conclusions that can be drawn about the effectiveness of the proposed method relative to existing state-of-the-art techniques.

### Questions
1. It is advisable to conduct experiments to validate the necessity of using patching for text data.
2. Could you clarify the meaning of "trend" and "season" in the context of text data? Additionally, please elaborate on how the pooling in Equation (6), without further constraints, extracts trend and season.
3. Given the small dataset size and short input/output lengths, it is recommend to add traditional and straightforward models as baselines, such as: 1)repeat last: just repeating the last timestamp's value $x_{L}$ as prediction; 2)Vector autoregressive moving average; 3)DeepAR.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
