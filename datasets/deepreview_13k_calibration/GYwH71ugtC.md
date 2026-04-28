# Retrieval Augmented Time Series Forecasting

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
Retrieval-augmented generation (RAG) is a central component of modern LLM systems, particularly in scenarios where up-to-date information is crucial for accurately responding to user queries or when queries exceed the scope of the training data. The advent of time-series foundation models (TSFM), such as Chronos, and the need for effective zero-shot forecasting performance across various time-series domains motivates the question: Do benefits of RAG similarly carry over to time series forecasting? In this paper, we advocate that the dynamic and event-driven nature of time-series data makes RAG a crucial component of TSFMs and introduce a principled RAG framework for time-series forecasting, called \emph{Retrieval Augmented Forecasting} (RAF). Within RAF, we develop efficient strategies for retrieving related time-series examples and incorporating them into forecast. Through experiments and mechanistic studies, we demonstrate that RAF indeed improves the forecasting accuracy across diverse time series domains and the improvement is more significant for larger TSFM sizes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to incorporate a retrieval module for the time series forecasting task. It proposes to perform retrieval in observation space, selecting the `m` most similar lookback windows, and calculating a weighted average of their corresponding horizons, where the weights are a softmax of the similarity scores previously computed. Following this, several linear layers are used to project both the original lookback window and retrieved time series into the prediction. A "multiple period" extension is also proposed, which performs the same process on downsampled versions of the time series, which are incorporated into the final forecast.

The paper performs experiments on the long sequence forecasting setting and shows improved performance compared to several (older) baselines.

### Strengths
Retrieval is an interesting idea to explore in the context of time series forecasting. The paper shows that the proposed model improves over some baselines, and presents some analysis surrounding the proposed method.

### Weaknesses
From my reading, I am unclear on what is the set of datapoints the retrieval is being performed on. Is it on the entire time series, i.e. the whole training + validation set + the test set that is becoming available during rolling window evaluation? Or is there a limit to how much data is being searched over, and how is this set?

Related to this, is my concern regarding the motivation of the paper - the introduction argues that existing methods are memorizing the training set, and retrieval is a solution to help generalize by extracting information relevant to the query. However, it turns out that the proposed approach is still retrieving from the train set. I see no big difference between the proposed approach and a Transformer model which is also attending to the lookback window. Retrieval seems to only make sense in the zero-shot setting, where we are trying to make predictions on a time series from a completely new dataset, and performance can be improved by retrieving related time series from that dataset, and critically, this dataset wasn't in the training set, so that we can show that it is not just memorization. 

The experiment design for ablating the effects of the different components of the proposed method, especially to isolate the improvements from the retrieval component can be improved. The current experiments simply take NLinear as "without retrieval", but the design space is much larger and this is an important set of experiments to better understand the effects of retrieval. Specifically, the proposed model has projections f, g, and h. While I am comfortable with saying that g is part of the retrieval module, I am not, with f. These are additional learnable parameters which challenges the notion that NLinear is the appropriate ablation.

### Questions
1. Question from the weaknesses section regarding what is the set of datapoints for retrieval.
2. The introduction states: ``This paper examines a critical open question in time-series forecasting: “do current models possess the necessary inductive biases and learning capacity to extract generalizable patterns from training data and achieve high accuracy?” '' -- what are the conclusions regarding this research question?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes RAFT (Retrieval-Augmented Forecasting of Time-series), a novel method for time series forecasting that leverages a retrieval module to provide the model with relevant historical patterns. The key idea is to retrieve the most similar historical data to the current input and utilize the future values of these retrieved candidates to enhance predictions. This reduces the burden on the model to memorize all possible patterns, especially rare or complex ones.
The retrieval module operates by finding the most similar key patches to the input query from the entire training time series, and then retrieving the corresponding future value patches. An attention-like mechanism is used to weigh the retrieved value patches based on their similarity to the input. RAFT extends this idea to multiple time series generated by downsampling the original series at different periods, allowing it to capture patterns at various temporal resolutions.
The method is built upon a simple MLP architecture, demonstrating that a well-designed retrieval module can provide an effective inductive bias for time series forecasting. Extensive experiments on eight benchmark datasets show that RAFT consistently outperforms state-of-the-art baselines, achieving an average win ratio of 86% for multivariate forecasting and 80% for univariate forecasting tasks.
Further analyses using synthetic datasets reveal that RAFT is particularly beneficial when rare patterns repeat in the time series or when patterns are less temporally correlated. The retrieval module enables the model to directly leverage relevant historical patterns in such scenarios.
Overall, the paper presents a novel perspective on enhancing time series forecasting models with retrieval-based methods, opening up new possibilities in this domain.

### Strengths
This paper presents several noteworthy strengths across various dimensions:

Originality: The proposed RAFT method offers a novel approach to time series forecasting by incorporating a retrieval module. While retrieval-augmented methods have been explored in other domains like natural language processing, their application to time series forecasting is innovative. By directly leveraging relevant historical patterns, RAFT introduces a new paradigm for handling complex and rare patterns in time series data.
Quality: The paper is well-structured and thoroughly evaluates the proposed method. The authors provide a clear description of the retrieval module architecture and how it is integrated into the overall forecasting model. The experimental setup is comprehensive, considering both multivariate and univariate forecasting tasks across eight diverse benchmark datasets. The results convincingly demonstrate the superiority of RAFT over state-of-the-art baselines.
Clarity: The paper is well-written and easy to follow. The authors provide a clear motivation for their approach and explain the technical details of RAFT in a concise and understandable manner. The use of illustrative figures, such as the retrieval module architecture (Figure 2) and the overall RAFT architecture (Figure 3), enhances the clarity of the proposed method. The experimental results are presented in a readable format, making it easy to compare RAFT's performance against the baselines.
Significance: The paper makes a significant contribution to the field of time series forecasting. By demonstrating the effectiveness of retrieval-augmented methods, RAFT opens up new research directions and possibilities for improving forecasting models. The analyses using synthetic datasets provide valuable insights into the scenarios where retrieval is particularly beneficial, such as handling rare patterns or less temporally correlated data. These findings have important implications for real-world applications where such characteristics are common.

Moreover, the paper's results challenge the current reliance on increasing model capacity to capture complex patterns. RAFT shows that a simpler MLP architecture, when augmented with a well-designed retrieval module, can outperform more sophisticated models. This highlights the potential of retrieval-based methods as a complementary approach to improving time series forecasting.
In summary, the paper's originality, quality, clarity, and significance make it a valuable contribution to the field, offering new insights and directions for future research in time series forecasting.

### Weaknesses
While the paper presents a novel and effective approach to time series forecasting, there are a few areas that could be improved or require further clarification:

Retrieval module design: The current retrieval module uses a simple similarity measure (Pearson correlation) to find the most relevant historical patterns. However, the authors do not provide a thorough justification for this choice or explore alternative similarity measures. Time series data often exhibit complex, nonlinear, and nonstationary characteristics, which may not be well-captured by linear correlation. Exploring more sophisticated similarity measures, such as those that can capture phase differences or non-linear relationships, or learning adaptive similarity functions could potentially improve the retrieval process and the overall forecasting performance. For instance, dynamic time warping (DTW) could be considered for its ability to handle time series with varying speeds, or kernel-based methods could capture non-linear dependencies.

Computational efficiency: The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed method. The retrieval process involves comparing the input query with all key patches in the training data, which could be computationally expensive for large datasets. While the authors mention that the stride for the sliding window can be adjusted for computational efficiency (Section 3.2), they do not provide empirical results or discussions on the trade-off between computational cost and forecasting accuracy. A more comprehensive analysis of the method's scalability and efficiency is needed, including a breakdown of the time complexity of the retrieval process and the impact of different stride values on both computational cost and forecasting accuracy. Furthermore, the memory footprint of storing all key patches should be considered.

Sensitivity to hyperparameters: The performance of RAFT may be sensitive to the choice of hyperparameters, such as the number of retrieved patches (m), the temperature (τ), and the set of periods (P) used for generating multiple time series. While the authors provide the chosen values of m for each experiment setting (Appendix B), they do not discuss how these values were determined or provide insights into the sensitivity of the results to these hyperparameters. A more systematic analysis of the impact of these hyperparameters on the forecasting performance is needed, including sensitivity analysis and potentially using techniques like cross-validation or Bayesian optimization to find optimal values. Furthermore, the interaction between these hyperparameters should be explored.

Limited ablation studies: The paper would benefit from more extensive ablation studies to better understand the individual contributions of the proposed components. For example, the authors could evaluate the performance of RAFT without the multi-period extension to assess the impact of capturing patterns at different temporal resolutions. Similarly, comparing the performance of RAFT with and without the attention-like weighting of the retrieved value patches could provide insights into the importance of this mechanism. Additionally, an ablation study on the impact of the number of retrieved patches (m) on performance would be valuable.

Evaluation on more diverse datasets: While the paper evaluates RAFT on eight benchmark datasets, these datasets are primarily from the energy, traffic, and weather domains. To demonstrate the generalizability of the proposed method, it would be valuable to include datasets from a wider range of application domains, such as finance, healthcare, or social media. Moreover, the paper could benefit from evaluations on datasets with different characteristics, such as varying lengths, missing values, or irregularly sampled time series. The performance of the model on datasets with longer time series and different noise characteristics should also be investigated.

### Questions
1. Choice of similarity measure: Can you provide more insights into the choice of Pearson correlation as the similarity measure in the retrieval module? Have you considered or experimented with other similarity measures, such as dynamic time warping (DTW), cross-correlation, or learned similarity functions? How do you think the choice of similarity measure affects the retrieval process and the overall forecasting performance?
2. Computational efficiency: Can you provide more details on the computational complexity and efficiency of the proposed method, particularly the retrieval process? How does the computational cost scale with the size of the dataset and the length of the time series? Have you considered any techniques to improve the efficiency of the retrieval process, such as indexing or approximate nearest neighbor search?
3. Hyperparameter sensitivity: How sensitive are the results to the choice of hyperparameters, such as the number of retrieved patches (m), the temperature (τ), and the set of periods (P)? Can you provide more details on how these hyperparameters were determined for each experiment setting? Have you considered using techniques like cross-validation or Bayesian optimization to tune these hyperparameters?
Ablation studies: Can you provide more ablation studies to investigate the individual contributions of the proposed components? For example, how does the performance of RAFT change when the multi-period extension is removed? How important is the attention-like weighting of the retrieved value patches compared to using a simple average or the most similar patch?
Evaluation on diverse datasets: Have you considered evaluating RAFT on datasets from a wider range of application domains beyond energy, traffic, and weather? How do you expect the proposed method to perform on datasets with different characteristics, such as varying lengths, missing values, or irregularly sampled time series? Providing results on more diverse datasets could strengthen the claims of generalizability.
Handling multiple retrieved patterns: In the current implementation, RAFT retrieves the top-m most similar patterns and aggregates them using an attention-like weighting scheme. Have you considered other approaches to handle multiple retrieved patterns, such as clustering similar patterns or using a more sophisticated aggregation method? How do you think these alternative approaches would impact the forecasting performance?
Comparison with other retrieval-based methods: While the paper compares RAFT with several state-of-the-art forecasting methods, it would be interesting to see a comparison with other retrieval-based methods, such as those mentioned in the related work. How does RAFT differ from these existing retrieval-based approaches, and how does it compare in terms of performance and efficiency?
Visualization of retrieved patterns: Can you provide more visualizations of the retrieved patterns and their corresponding future values? It would be helpful to see examples of how the retrieved patterns contribute to the final forecasting results, particularly in cases where RAFT significantly outperforms the baselines. Such visualizations could provide additional insights into the effectiveness of the retrieval process.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduced RAFT - a retrieval augmented time series forecasting model. The main idea is to use the a similarity function between the current time series context (query) and context and forecast horizon pairs (key/value) to retrieve similar time series patches from the training for forecasting. A similarity function between the query and key patches is used to compute attention weights for the value patches. These retrieved patches are then concatenated with the input and the forecast is generated with a linear model. Optionally, the model also uses downsampling of the input to different resolutions and using multiple downsampled retrieval results for forecasting. The authors compare their model with different baseline models on eight datasets. They also perform synthetic experiment to provide evidence when retrieval is useful. The authors's experiments suggest that retrieval is useful when keys are similar to the query, rate patterns are present, and the patterns are temporally less correlated.

### Strengths
### Originality and Significance 
The authors introduce a conceptually interesting model with a straightforward instantiation. As the proposed method is mainly a simplification of existing attention-based forecasting ideas, the significance in this work is mainly into the experimental evidence whether these simplified instantiations work well for time series forecasting. 

### Quality 
The paper evaluates the model on eight datasets and several baselines from literature. Additionally, the authors discuss their results with additional synthetic experiments to demonstrate under which conditions the retrieval module in RAFT benefits brings a benefit to forecasting. However, I have concerns regarding the evaluation which I elaborate in the Weaknesses section. 

### Clarity 
The paper is clearly written. The proposed idea and the experiments are easy to follow through the presentation of the proposed idea by the used notation and supporting illustrations.

### Weaknesses
The main two weaknesses in the paper are the presentation of the related work and the empirical evaluation.

### Related work 
The model uses a similarity function and attention weights to get a weighted average candidate value patches from the training dataset and an MLP network to forecast. This is conceptually similar to transformer variants for forecasting as the main difference is mainly in the interaction of learnable weights in the transformer architecture. Such a simplification might be effective, but this is not discussed in the related work. Moreover, there is related work on few-shot forecasting that presents an (arguably more complex) instantiation of the model proposed in this paper (Iwata and Kumagai, 2020; https://arxiv.org/abs/2009.14379). This work should be compared and discussed. In light of this prior work, the novelty of this work is limited.

Another concern I have with the related work is that recent work on pretrained/foundational time series model are not mentioned (Woo et al., ICML 2024: https://arxiv.org/abs/2402.02592; Das et al., ICML 2024: https://openreview.net/forum?id=jn2iTJas6h; Ansari et al., preprint 2024: https://arxiv.org/abs/2403.07815). I would argue that the proposed idea of using RAG for forecasting could benefit exactly this model class to forecast time series that are not in the pretrainig corpus. This should be discussed in the related work.

### Evaluation
The main concern I have on the paper is on the evaluation in the Experiments section.

1.The authors evaluate their method on only eight different datasets. While these datasets have been used widely, many more datasets became available, which allows for a more thorough evaluation. Several of these datasets (Woo et al., ICML 2024: https://arxiv.org/abs/2402.02592; Ansari et al., preprint 2024: https://arxiv.org/abs/2403.07815) from recent papers are publicly available. Running the evaluation on more datasets would give stronger evidence on the performance of the model.

2. I also have concerns about the choice and setup of the baselines. The authors mention that they use the same experimental setup for each baseline, which includes number of training epochs. However, the number of training epochs are arguably an important hyperparameter for tuning a model. I would argue that the real-world performance is best compared by choosing the best possible setting for the baselines, rather than a uniform setting that might result into suboptimal performance of several baselines. Additionally, I think a strong baseline (PatchTST; Nie et al., ICLR 2023: https://arxiv.org/abs/2211.14730) is missing and should be included. When I compare the MSE/MAE of the models in this work with the models in the PatchTST paper, I find that the models in this work perform much weaker. This might suggest that the chosen setting leads to suboptimal performance of the baselines, which might affect the conclusion of this paper. For example: D-Linear has a 0.0764 MSE for the univariate setup in this work and a 0.056 MSE for ETTh1 in the PatchTST paper (Nie at al., ICLR 2023). This suggests that there is actually a better setting to run this baseline and this setting should be used for comparison. I noticed that both papers cite different sources of the datasets, but I checked briefly and at least the ETT datasets seem identical. There might be something different in the setup that I'm not aware off that also explains this difference.

I consider this point critical and this needs to be addressed for me to consider to change my score. Specifically, I would ask the authors to revise the setup and use the settings for the baselines so they are comparable to the results in Nie at al. 2023. I would also like to ask the authors to include the PatchTST baseline.

3. I also have concerns on the win matrix to compare the results. I would argue that in this setup it is not relevant how often RAFT outperforms other baselines, but rather how it compares to the strong baselines. Thus, the reported average win ratio of 86% is somewhat misleading and it would be more useful for the reader to report the win-rate to the next best model and the absolute/relative improvement in MSE/MAE when averaged over the datasets. I would also argue that in the context of the cited paper (Bahri et al., ICLR 2022), the win matrix is used over 65 datasets, while here only over 8 datasets with different forecast horizons. Hence, this introduces redundancy when aggregating the results in a win matrix. It is also not clear how ties are handled. Bahri et al., ICLR 2022 explicitly mention that ties are broken by a statistical test. How is this handled in this work?

### Questions
1.  It is not clear how ties are handled in the statistical test. Bahri et al., ICLR 2022 explicitly mention that ties are broken by a statistical test. How is this handled in this work? 

2. Is the setup/datasets in this work noticeably different from the setup/datasets in the PatchTST paper? 

3. In several points of the paper the authors mention the inductive bias of RAFT and that it is more suited for forecasting. It is unclear to me what this inductive bias specifically means. In particular, there is one argument that existing models make i.i.d. assumptions and this is a limitation. How does RAFT overcome this limitation, especially with the empirical result that it is more effective when temporal correlation is lacking? I would kindly ask the authors what the specific inductive bias is that RAFT introduces and how it is a different inductive bias from existing models.

### Soundness
2

### Presentation
3

### Contribution
2
