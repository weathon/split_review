# Connecting the Patches: Multivariate Long-term Forecasting using Graph and Recurrent Neural Network

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
Many Transformer-based models have achieved great performance on multivariate long-term time series forecasting (MLTSF) tasks in the past few years, but they are ineffective in capturing cross-channel dependencies and temporal order information. In multivariate time series analysis, the cross-channel dependencies can help the model understand the correlations between multivariate time series, and the consistency of time series is also essential for more accurate predictions. Therefore, we propose GRformer, adopting the Graph neural network (GNN) and position encoding based on recurrent neural network (RNN) to better process multivariate time series data. We design a mix-hop propagation layer and embed it in the feedforward neural network to encourage proper interaction between different time series. To introduce temporal order information, we use a multi-layer RNN to recursively generate positional embeddings for sequence elements. Experiments on eight real-world datasets show that our model can achieve more accurate predictions on MLTSF tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes GRformer, a new neural architecture for multivariate long-term time series forecasting (MLTSF). The authors propose a hybrid architecture that consists of a Transformer-based graph neural network to model cross-channel dependencies and a recurrent neural network to model temporal dependencies. The proposed model shows promising performance on eight benchmarks. However, the motivation and reasoning behind the criticism of the Transformer-based approach are difficult to understand. Some of the claims are made without proper evidence, or by simply citing previous work, without providing any further detailed study or analysis. Additionally, the performance improvements on the benchmarks seem to outperform the baselines. However, I believe the claim of achieving a performance improvement with a 5.7% decrease in MSE and 6.1% decrease in MAE is misleading. These numbers are calculated by averaging MSE and MAE without considering the scales between different benchmarks and metrics. ILI has much higher mean squared errors (MSEs) and mean absolute errors (MAEs) than other benchmarks. This means that if you compute the average score in this way, the average score can be dominated by the relative improvement in this specific dataset. The tone reporting the improvement suggests that the model showed around a 6% decrease in errors on all benchmarks, but the average relative improvement for each benchmark at different metrics is actually 2.55% for MSE and 4.96% for MAE.

### Strengths
The model achieves improvements over 7 different benchmarks using 4 metrics for each benchmark dataset. The experiments are done extensively with ablation on different positional encoding strategies. This however raises a question on why the RNN is needed (Table 3. R: the first column vs L: the second column show a very minor difference).

### Weaknesses
I am not sure what I am seeing in Figure 1(b), and I don’t understand how to interpret the authors' claim that cross-channel interaction is chaotic based on simply visualizing the weight matrices of the Transformer's dense layer (internal MLP). The authors need to provide a more rigorous analysis of these weight matrices, perhaps by showing the distribution of the weights and comparing them to the correlation structure of the input data. It is not clear how a visualization of the weight matrix alone can justify the claim of chaotic interactions. 

I am not sure I understand the authors' point about positional encoding not being able to represent temporal orders well. RNNs have their own problems, such as vanishing gradients when modeling long-term temporal dependencies. Are you suggesting that RNNs outperform Transformers in multivariate long-term time series forecasting (MLTSF)?
-> Are the ablation results in Table 3 the experiments to back this claim? If that's the case, the performance difference between an RNN-based positional encoding (?) vs a learned positional embedding is almost 0. The ablation study does not provide strong evidence for the superiority of RNN-based positional encoding. The performance differences are marginal, and it is not clear if they are statistically significant.

What exactly is the RNN-based position encoding method? In the caption for Figure 2, it says "The multi-layer RNN injects temporal order information." However, RNNs are not just injecting temporal order information as some sort of advanced positional encoding method; they can actually learn temporal dependencies. I am not sure if you are distinguishing between positional encoding and learning temporal representation. The description of the RNN-based positional encoding is ambiguous and requires more clarification. It is not clear how the RNN is used to generate positional encodings, and how this differs from using the RNN to directly model temporal dependencies. Figure 2 (b) is hard to understand, at least explain the operator signs in the caption, arrows are not clear.

### Questions
What is the main evidence that Transformer-based models are ineffective at capturing cross-channel dependencies and temporal orders? If Transformers were bad at capturing temporal orders, they would not have become as popular as they are today. I am curious why the authors make such claims, as I do not see any plausible supporting evidence in the manuscript.

The authors mentioned that they used multi-layered RNNs, however in the appendix, it's said 1-layer RNN was used. Can you clarify the details of the RNN architecture?

“To properly capture temporal dependencies, we consider using a multilayer RNN to encode the positions in the time series.” Why deep RNNs can properly capture temporal dependencies while Transformers can’t?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper enhances Transformer with GNN and position embedding generated by RNN for multivariate time series forecasting. The proposed GRformer constructs graph by pearson correlation and uses a mix-hop propagation GNN layer to capture cross-channel dependency. For temporal dependency, it uses an RNN to recursively generate positional embeddings. Experiments on eight real-world datasets show that the proposed GRformer is on compare with SOTA model, PatchTST.

### Strengths
- This paper is well-written and easy to follow.
- Using pearson correlation for graph constructing is reasonable and efficient.

### Weaknesses
My main concern is that the novelty is limited:

- For RNN-based position embedding:
  1. The idea of enhance Transformer with RNN is not new [1].
  2. RNN operates recursively and cannot be parallelized, which offsets the efficiency advantages of Transformers that can be highly parallelized.
  3. Ablation study in Table 3 shows that the improvement of RNN against previous learnable position embedding is not significant.
- For Mix-hop propagation:
    1. The mix-hop propagation layer is **exactly the same** as that in [2] and there is no explicit reference to it in Section 3.2.3.
    2. Besides the graph construction via Pearson correlation, this is a direct combination of PatchTST and "Connecting the dots".

### Questions
- What is the authors' primary objective in visualizing the weights of the MLP in Figure 1(b), given that it only reflects the correlation among hidden states? 
- Could you provide a comparison of the computational efficiency between your RNN-based position embedding and a learnable position embedding, particularly in relation to varying sequence lengths?
- How were the hyperparameters (0.8 and $k$) in Equations (2) and (3) chosen, and what impact do these specific values have on the model's performance and behavior?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper delves into the challenges presented by multivariate long-term time series forecasting (MLTSF), specifically the difficulty of capturing cross-channel dependencies and temporal order information using current Transformer-based models. Despite the achievements of Transformer models in various fields, their application in MLTSF reveals certain inadequacies. Models like Informer, Autoformer, and FEDformer, while advanced, still face challenges in understanding intricate channel relationships in multivariate time series. 

To address these issues, the authors propose the GRformer model. This innovative solution combines the strengths of Graph Neural Networks (GNN) and position encoding derived from Recurrent Neural Networks (RNN). The inclusion of a mix-hop propagation layer within a feedforward neural network promotes efficient interaction between different time series data points. Additionally, by leveraging a multi-layer RNN, the model recursively generates positional embeddings, emphasizing the importance of sequence order. 

The paper's empirical tests, conducted on eight real-world datasets, demonstrate the GRformer's superior predictive accuracy in MLTSF tasks, underlining its potential as a novel solution in the field of time series forecasting.

### Strengths
**Strengths**:

1. **Originality**: 
   - The GRformer presents a unique fusion of GNN and RNN-based position encoding within a Transformer framework, addressing gaps in MLTSF.
   - The incorporation of the Pearson correlation coefficient for graph structure is a notable innovation.

2. **Quality**: 
   - Rigorous empirical validation is conducted on eight real-world datasets, ensuring robustness.
   - The model's design is comprehensive, with the mix-hop propagation layer and RNN-based position encoding as highlights.

3. **Clarity**: 
   - The paper delineates complex concepts coherently, facilitating reader understanding.
   - Distinctive features and advantages of GRformer over existing models are clearly articulated.

4. **Significance**: 
   - The GRformer's advancements in capturing cross-channel dependencies have potential broad impacts in time series forecasting.
   - The paper paves the way for future research by highlighting existing challenges and areas of improvement.

In essence, the paper excels in its innovative methodology, thorough validation, lucid presentation, and relevance in the field.

### Weaknesses
1. **Mathematical Notation Consistency**:
   - The authors' use of mathematical notation appears inconsistent. For instance, function names should ideally be presented in regular typeface rather than italic. Proper notation ensures clarity and avoids potential confusion.

2. **Graph Construction Using Pearson Coefficient**:
   - While the authors opted for the Pearson correlation coefficient for graph construction, which subsequently serves as the foundational structure for the GNN, one might question the exclusion of making GNN parameters learnable. This adaptability could potentially offer more flexibility to the model. Specifically, the Pearson correlation, while computationally efficient, captures only linear relationships between time series. The graph structure, being static, might not adapt to the dynamic changes in the underlying relationships between the time series, which could limit the model's performance in complex scenarios.

3. **Assumption of Homoscedasticity**:
   - The Pearson coefficient assumes homoscedasticity in the data. It's unclear if the authors verified this assumption across their datasets. Such checks are crucial to ensure the validity of the chosen coefficient. The presence of heteroscedasticity could lead to inaccurate correlation estimates, which would negatively impact the graph structure and, consequently, the model's performance. Furthermore, the impact of outliers on the Pearson correlation could be significant, potentially leading to a skewed representation of the relationships between time series.

4. **Alternative Correlation Metrics**:
   - The paper doesn't seem to explore or discuss other potentially beneficial correlation coefficients like Time-Lagged Cross-Correlation (TLCC) or Dynamic Time Warping (DTW). An exploration or justification of the chosen metric over others could have added depth to their methodology. TLCC, for instance, could capture lagged relationships, which are common in time series data, while DTW could handle time series with varying speeds and lengths. The lack of discussion on these alternatives leaves a gap in the justification of the chosen method.

### Questions
**Hyperparameter Selection in Graph Construction**:
   - The methodology introduced by the authors involves several hyperparameters, which seemingly have a significant impact on the model's outcomes. Specifically, when constructing the graph structure:
     - How was the threshold value of 0.8 determined?
     - Regarding the 'topk' selection, how was the value of \( k \) chosen, and does it correlate with the number of variables?

 **Mix-hop Propagation Parameter**:
   - How was the value for the EMA parameter \( \alpha \) in the mix-hop propagation process determined?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
