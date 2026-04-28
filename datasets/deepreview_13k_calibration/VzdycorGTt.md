# packetLSTM: Dynamic LSTM Framework for Streaming Data with Varying Feature Space

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 6, 3, 5

## Abstract
We study the online learning problem characterized by the varying input feature space of streaming data. Although LSTMs have been employed to effectively capture the temporal nature of streaming data, they cannot handle the dimension-varying streams in an online learning setting. Therefore, we propose a dynamic LSTM-based novel method, called packetLSTM, to model the dimension-varying streams. The packetLSTM's dynamic framework consists of an evolving packet of LSTMs, each dedicated to processing one input feature. Each LSTM retains the local information of its corresponding feature, while a shared common memory consolidates global information. This configuration facilitates continuous learning and mitigates the issue of forgetting, even when certain features are absent for extended time periods. The idea of utilizing one LSTM per feature coupled with a dimension-invariant operator for information aggregation enhances the dynamic nature of packetLSTM. This dynamic nature is evidenced by the model's ability to activate, deactivate, and add new LSTMs as required, thus seamlessly accommodating varying input dimensions. The packetLSTM achieves state-of-the-art results on five datasets, and its underlying principle is extended to other RNN types, like GRU and vanilla RNN.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces packetLSTM, a dynamic LSTM-based framework designed to handle streaming data with varying input feature dimensions in online learning settings. The key innovation is using a packet of LSTMs, where each LSTM is dedicated to processing one input feature, along with a shared common memory for global information. The framework can dynamically activate, deactivate, and add new LSTMs as features appear or disappear. The authors demonstrate superior performance over existing methods across 5 datasets and extend their approach to other RNN architectures (GRU, vanilla RNN). They also introduce a new Transformer-based baseline called HapTransformer.

### Strengths
1. The authors propose novel architecture about their models with clean and intuitive design using one LSTM per feature with shared memory, dynamic handling of varying input dimensions through activation/deactivation of LSTMs, and effective balance between local feature information and global shared information
2. The evaluation in the experiments is comprehensive. For exmaple, the authors use 5 diverse datasets, detailed ablation studies examining each component, strong empirical results consistently outperforming 10 baselines. and well-designed challenging scenarios testing model capabilities.
3. The complexity analysis is also beneficial and brings more applicability of the model. The proposed HapTransformer is also a novel contribution in the hot transformer domain.
4. The extensive hyperparameter search protocols is also promising.

### Weaknesses
1. Some important literatures about varying input feature dimensions are missing. The authors are encouraged to include many fundamental works from this domain. For example, the authors should cite [1] and [2] and several other references from [3].  Specifically, the paper lacks discussion on methods that explicitly address feature arrival and departure in online learning scenarios, such as those that use feature selection or adaptive model structures. The current literature review does not adequately cover the breadth of techniques that handle dynamic feature spaces, which is crucial for situating the proposed method within the existing body of work.
2. This work focuses primarily on binary classification tasks. It would be better to see more diverse task such as multi-class classification and regression problem. No need to bring forward such results during rebuttal but I would like to see some of them in the final version.

### Questions
1. Given the space complexity challenges, what are the practical limits on the number of features the model can handle efficiently?
2. Could the approach be extended to handle structured data types (e.g., graphs, images) where features have inherent relationships?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a dynamic LSTM-based online learning model called packetLSTM, designed to model streaming data with varying dimensionality. The core idea of the packetLSTM model is that each data feature corresponds to a separate LSTM network, which addresses the issue of changing feature dimensions. The authors conduct comparative experiments on multiple datasets, evaluating the performance of the packetLSTM model against several baseline models.

### Strengths
The authors propose a dynamic LSTM-based online learning model called packetLSTM, designed to model streaming data with varying dimensionality. The core idea of the packetLSTM model is that each data feature corresponds to a separate LSTM network, which addresses the issue of changing feature dimensions. The authors conduct comparative experiments on multiple datasets, evaluating the performance of the packetLSTM model against several baseline models.

### Weaknesses
1. The core design of packetLSTM, where each feature corresponds to an individual LSTM network, raises concerns about the model's practical applicability and scalability. While the authors provide a theoretical analysis of the spatial and temporal complexity of packetLSTM, there is a lack of specific experimental data to support these claims, such as memory consumption and training time. This absence of empirical evidence may lead readers to question the true potential of the model in real-world applications.

2. The authors mention that "packetLSTM easily handles the 7500 features in the IMDb dataset." However, it is unclear what these 7500 features refer to, as most samples in the IMDb dataset do not have that many features. Do the 7500 features represent the total word count across all samples, or has the dataset undergone specific processing to yield this number? Could the authors clarify this point?

3. The authors claim that packetLSTM effectively prevents catastrophic forgetting. However, it appears that the experimental design does not sufficiently validate this assertion. Specifically, when features that have not been seen for a long time reappear, does the model genuinely maintain comparable performance? Could the authors provide additional evidence or analysis to support this claim?

4. The authors reference the results from the OCDS paper, which report accuracies exceeding 80% on the IMDb, A8A, and Magic04 datasets. However, the accuracy achieved by the authors in replicating the OCDS results on these datasets is significantly lower. What might explain this discrepancy in performance? Could the authors provide insights into the differences in experimental setup or any other factors that could contribute to this variation in accuracy?

5. The authors set the parameter p to 0.25, 0.50, and 0.75 to simulate different degrees of feature missingness. However, would it be beneficial for the authors to provide a baseline evaluation of packetLSTM with complete features (i.e., p=0)? This would allow for an assessment of packetLSTM's optimal performance when all features are available, serving as a reference point for interpreting the results under varying levels of feature absence.

6. I have concerns about the reliability of some experimental results presented in the paper. The authors mention that the balanced accuracy on the IMDb dataset for the DistilBERT, BERT, and OCDS models is only slightly above 50%. Given that IMDb is a binary classification dataset, this low balanced accuracy may indicate that the models are not effectively learning useful information, with performance levels approaching random guessing. What might explain these results? A balanced accuracy of 50% suggests that the mean sensitivity and specificity are both around 0.5, raising the possibility that the model may be making complete errors in one class while performing well in the other, which typically indicates significant bias. Additionally, since some datasets are inherently balanced, random feature missingness should theoretically have minimal impact on the dataset's balance. Would the authors consider providing additional metrics, such as standard accuracy, to further clarify model performance?

### Questions
1. The authors mention that "packetLSTM easily handles the 7500 features in the IMDb dataset." However, it is unclear what these 7500 features refer to, as most samples in the IMDb dataset do not have that many features. Do the 7500 features represent the total word count across all samples, or has the dataset undergone specific processing to yield this number? Could the authors clarify this point?

2. The authors claim that packetLSTM effectively prevents catastrophic forgetting. However, it appears that the experimental design does not sufficiently validate this assertion. Specifically, when features that have not been seen for a long time reappear, does the model genuinely maintain comparable performance? Could the authors provide additional evidence or analysis to support this claim?

3The authors reference the results from the OCDS paper, which report accuracies exceeding 80% on the IMDb, A8A, and Magic04 datasets. However, the accuracy achieved by the authors in replicating the OCDS results on these datasets is significantly lower. What might explain this discrepancy in performance? Could the authors provide insights into the differences in experimental setup or any other factors that could contribute to this variation in accuracy?

4.he authors set the parameter p to 0.25, 0.50, and 0.75 to simulate different degrees of feature missingness. However, would it be beneficial for the authors to provide a baseline evaluation of packetLSTM with complete features (i.e., p=0)? This would allow for an assessment of packetLSTM's optimal performance when all features are available, serving as a reference point for interpreting the results under varying levels of feature absence.

5, I have concerns about the reliability of some experimental results presented in the paper. The authors mention that the balanced accuracy on the IMDb dataset for the DistilBERT, BERT, and OCDS models is only slightly above 50%. Given that IMDb is a binary classification dataset, this low balanced accuracy may indicate that the models are not effectively learning useful information, with performance levels approaching random guessing. What might explain these results? A balanced accuracy of 50% suggests that the mean sensitivity and specificity are both around 0.5, raising the possibility that the model may be making complete errors in one class while performing well in the other, which typically indicates significant bias. Additionally, since some datasets are inherently balanced, random feature missingness should theoretically have minimal impact on the dataset's balance. Would the authors consider providing additional metrics, such as standard accuracy, to further clarify model performance?

### Soundness
3

### Presentation
4

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
The paper presents PacketLSTM, a dynamic LSTM-based framework for streaming data with changing feature dimensions. Each input feature has a dedicated LSTM unit, allowing PacketLSTM to handle missing or new features continuously. The architecture combines shared memory for global representation and short-term memory for local representation. PacketLSTM achieves reasonable results across datasets.

### Strengths
- The paper addresses a pressing issue in streaming data analysis—handling temporal hazard inputs or dynamic features—which is crucial for the research community.
- The authors include a comprehensive set of experiments, including ablation studies and scenarios involving sudden and obsolete features, to verify the robustness of their proposed model.

### Weaknesses
 - The paper does not implement several existing techniques for handling dynamic inputs within LSTM models. To establish PacketLSTM as the best choice, additional comparisons with implemented baseline methods for hazard input processing are necessary.
-  The proposed method, while interesting, may lack sufficient complexity and novelty to meet ICLR's technical bar.
- Performance improvements in the tables show small margin gains over other methods, so significance testing should be conducted to verify the robustness of these results.

### Questions
See weakness.
Some additional questions:
- Have the authors considered additional baseline implementations for handling dynamic inputs within LSTM models to strengthen their claim of superiority?
- How does PacketLSTM handle the computational complexity introduced by creating separate LSTMs for each feature? Is there a computational cost analysis for real-time applications?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces packetLSTM, a novel LSTM-based framework tailored for handling streaming data with varying input feature dimensions. Each feature in the streaming data is managed by an individual LSTM unit, promoting effective handling of temporal variations in feature space. The packetLSTM architecture is claimed to mitigate catastrophic forgetting by leveraging both feature-specific short-term memory and a shared global memory. The model shows competitive or superior performance compared to baselines on multiple datasets and is versatile across other RNN architectures.

### Strengths
1. The architecture's capacity to accommodate missing features through individual LSTM management enhances its robustness in varied real-world data.
2. The inclusion of ablation studies and detailed results across various dataset conditions strengthens the reliability of the model's claims.
3. Comprehensive experiments on five datasets, along with competitive metrics, solidifies the framework’s potential as a state-of-the-art solution.

### Weaknesses
1. Given that available features trigger the activation of corresponding LSTMs, what are the hidden states from the previous timestamp that are input into the currently activated LSTM but not activated in the last timestamp?

2. The proposed method demonstrates limited novelty, as it directly adapts LSTM to handle dimension-varying streams.

3. In Table 2, the authors indicate that the Max operator yields the best performance as the aggregation (AGG) function. However, this approach may overlook valuable information from other dimensions. Including an ablation study with a self-attention mechanism in the AGG operator, which may potentially enhance the aggregation of information across different features.

4. The paper would benefit from a more thorough theoretical analysis.

5. The yellow color text in Figure 2 is too light, making it difficult to read clearly.

### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
2
