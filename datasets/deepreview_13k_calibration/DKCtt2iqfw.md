# Channel-wise Influence: Estimating Data Influence for Multivariate Time Series

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
The influence function, a technique from robust statistics, measures the impact on model parameters or related functions when training data is removed or modified. This {effective} and valuable post-hoc method allows for studying the interpretability of machine learning models without requiring costly model retraining. {It would provide extensions like increasing model performance, improving model generalization, and offering interpretability.}
Recently, {\bf M}ultivariate {\bf T}ime {\bf S}eries (MTS) analysis has become an important yet challenging task, attracting significant attention. However, there is no preceding research on the influence functions of MTS to shed light on the effects of modifying the channel of training MTS. Given that each channel in an MTS plays a crucial role in its analysis, it is essential to characterize the influence of different channels. To fill this gap, we propose a channel-wise influence function, {which is the first method that can estimate the influence of different channels in MTS}, utilizing a first-order gradient approximation that leverages the more informative average gradient of the data set. Additionally, we demonstrate how this influence function can be used to estimate the impact of a channel in MTS. Finally, we validated the accuracy and effectiveness of our influence estimation function in critical MTS analysis tasks, such as MTS anomaly detection and MTS forecasting. According to abundant experiments on real-world dataset, the original influence function performs worse than our method and even fail for the channel pruning problem, which demonstrate the superiority and  {necessity} of channel-wise influence function in MTS analysis tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces the Channel-wise Influence Function, a novel method tailored for multivariate time series (MTS) data to enhance model interpretability and performance by assessing the impact of individual channels. While MTS data are pivotal in domains like healthcare, traffic forecasting, and finance, traditional deep learning approaches have primarily focused on architectural improvements rather than understanding the unique contributions of each channel. Existing influence functions, effective in areas with independent data, fall short for MTS due to their inability to differentiate channel-specific effects. The proposed Channel-wise Influence Function addresses this by using a first-order gradient approximation to evaluate each channel’s contribution, proving especially useful in tasks like anomaly detection and forecasting. Extensive experiments show that this new approach outperforms traditional influence functions on real-world datasets, offering a more effective, interpretable tool for MTS analysis.

### Strengths
Innovation: The paper introduces the Channel-wise Influence Function, a novel method for analyzing the influence relationships between different channels in multi-channel time series (MTS) data. This approach is relatively rare in existing research and provides a new perspective for understanding and optimizing multi-channel data.
Fine-grained Dependency Analysis: Traditional influence function methods typically calculate only the overall influence, while the channel-wise influence function enables detailed quantification of each channel's influence on other channels. This fine-grained analysis is valuable in prediction and anomaly detection tasks for multi-channel data.
Broad Application Scenarios: The proposed method holds potential for various tasks, such as anomaly detection, channel pruning, and feature selection. The channel-wise influence function can help identify key channels, simplify models, and improve prediction accuracy, making it highly practical in real-world applications.

### Weaknesses
Lack of Clarity in Presentation: Figure 1, intended as an overview of the framework, does not clearly correspond with the main text, leaving several critical points unexplained. For instance, the calculation of the "Score" in the figure is not detailed, nor is its derivation clearly defined in the "CHANNEL-WISE INFLUENCE FUNCTION" section. Additionally, the term "well-trained model" lacks a concrete description of what type of model is being referred to. The paper also mentions that the "Channel-wise Influence" can serve as an explainable method to assess the channel-modeling capabilities of different approaches; however, it lacks detailed explanations and specific case studies to illustrate this claim.
Limited Datasets, Leading to Less Convincing Results: The experiments are conducted on a limited number of datasets, which reduces the generalizability and representativeness of the results. For example, in the time series forecasting task, only the electricity, solar-energy, and traffic datasets were used, without evaluating common benchmarks like ETTh, ETTm, and Exchange. Additionally, the forecast length was fixed at 96, which may restrict the credibility of the results and the method's broader applicability.
Insufficient Comparison with Baseline Models: The paper lacks comparison with enough baseline models, especially current mainstream state-of-the-art (SOTA) methods. This limitation makes it difficult to fully assess the proposed method's effectiveness relative to existing approaches, thus limiting the demonstration of its advantages. For instance, in time series forecasting, only PatchTST and iTransformer were used for comparison, while other competitive models like GPHT, SimMTM, TSMixer, TimesNet, and DLinear were omitted. Additionally, while the authors designed a CHANNEL PRUNING experiment, it would also be valuable to see how the Channel-wise Influence method performs in a standard time series forecasting setup for a more comprehensive evaluation.

### Questions
1. The framework figure (Figure 1) does not clearly correspond with the main text, particularly in areas like the calculation and derivation of "Score" and the definition of "well-trained model." Could you provide additional explanations or examples to clarify these components and better illustrate the core concept of the channel-wise influence function?
2. You mentioned that "it can serve as an explainable method to reflect the channel-modeling ability of different approaches." (6nd paragraph, line 293) Could you provide more specific explanations or examples, perhaps through case studies or illustrative examples, to demonstrate how the channel-wise influence function explains or evaluates different models' abilities to capture channel dependencies?
3. The current experiment includes only a few baseline comparisons, especially missing mainstream SOTA models like GPHT, SimMTM, TSMixer, TimesNet, and DLinear in time series forecasting. Do you plan to add comparisons with these models in future work to better demonstrate your method's competitiveness?
4. Given the limited datasets used in the experiments (electricity, solar-energy, and traffic) and the fixed forecast length of 96, the generalizability of the results might be limited. Would testing on additional datasets, such as ETTh, ETTm, and Exchange, with varied forecast lengths, help further validate the method's applicability?

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
This paper studies the problem of influence function for multivariate time series (MTS), which is the first study of MTS in deep learning. To effectively estimate the influence of MTS, this paper proposes a first-order gradient approximation. Then, the authors propose two channel-wise influence function-based algorithms for MTS anomaly detection and forecasting, respectively.

### Strengths
- It is the first work of influence function for MTS in deep learning. 

- Two channel-wise influence function-based algorithms is proposed in this paper to be applied in MTS anomaly detection and forecasting tasks.

### Weaknesses
 - The technical contribution of this paper is not very high. Only the influence function is proposed in MTS, which has been well-studied in other domains.

- The experimental results are not very impressive. In Table 2, we can observe that by using of proposed influence the improvement is not very significant. And also the datasets used in this paper are not enough. 

- The time complexity of the proposed method is not analyzed in this paper. 

- The code of this paper is not provided.

### Questions
See above weaknesses.

### Soundness
3

### Presentation
2

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
This paper introduces the Channel-wise Influence Function, a method designed to analyze the influence of individual channels in MTS data on the performance of ML models. The authors argue that existing influence function methods, commonly applied in CV and NLP, are inadequate for MTS analysis due to temporal dependencies and diverse information contained within different channels of MTS data. The proposed method leverages a first-order gradient approximation, drawing inspiration from the TracIn method, to quantify how training with a specific channel in the MTS data affects the model's ability to predict another channel. This method is presented to provide insights into the relationship between data and model behavior.

### Strengths
(1) The proposed method addresses a limitation in existing influence function methods by studying the unique contributions of individual channels within MTS data. While traditional methods assess the impact of entire data samples on model performance.
(2) By ranking channels based on their self-influence scores, the proposed method enables the selection of a reduced subset of channels without significant compromise to the model's predictive accuracy. This is particularly advantageous in scenarios where training with the entire set of channels is computationally expensive or infeasible.

### Weaknesses
(1) The paper primarily focuses on anomaly detection and forecasting, leaving the application to other relevant MTS tasks, such as classification, clustering, or imputation, unexplored. This limited scope restricts the paper's ability to fully demonstrate the potential of the proposed method in diverse MTS applications.
(2) The method relies on gradient computations, which can become computationally demanding for complex models, particularly when applied to large-scale MTS datasets. To address this, the paper proposes using gradients from a subset of model parameters to improve efficiency. However, a more detailed analysis of the trade-off between computational cost and performance when employing a reduced set of gradients is warranted. Specifically, the paper should analyze the computational complexity of the proposed method, particularly its scalability with high-dimensional data, and the trade-off between this complexity and the achieved performance gains, rather than just the complexity for a single channel.
(3) The paper employs an equidistant sampling strategy to select channels based on their ranked self-influence scores. This approach may introduce biases, particularly when the distribution of influence scores is uneven.  For instance, if a large number of channels have similar influence scores, the equidistant sampling might lead to the exclusion of potentially informative channels simply because they are clustered together in the ranking.
(4) The observation that a simple MLP model with only one layer outperforms a Transformer model raises concerns about the chosen datasets. It is possible that the datasets used might lack the complexity typically observed in real-world multivariate time series (MTS) data, where intricate temporal dynamics are prevalent.

### Questions
(1) Several works have successfully applied influence functions to analyze MTS data. For instance, TimeInf (Li et al., 2024) utilizes influence functions to quantify the impact of individual data points on the model's predictions. It would be beneficial for the authors to explicitly discuss how the proposed method compares to, or builds upon, these existing approaches.

1. TimeInf: Time Series Data Contribution via Influence Functions. https://arxiv.org/abs/2407.15247
2. Interdependency Matters: Graph Alignment for Multivariate Time Series Anomaly Detection. https://arxiv.org/abs/2410.08877
3. sTransformer: A Modular Approach for Extracting Inter-Sequential and Temporal Information for Time-Series Forecasting. https://arxiv.org/abs/2408.09723

(2) The paper primarily focuses on comparing with the original influence function and naive channel selection methods. A more comprehensive evaluation would involve comparing with other channel selection techniques, such as those based on feature importance scores or attention mechanisms, to provide a more robust assessment of its effectiveness.

(3) Computational complexity analysis of the proposed method as the number of channels increases  is crucial. Hence, an empirical evaluation using larger and more diverse datasets, such as the publicly available ETT, Electricity, and Traffic datasets (link: https://drive.google.com/file/d/1l51QsKvQPcqILT3DwfjCgx8Dsg2rpjot/view), would be beneficial.

(4) While the paper emphasizes the potential of the proposed method for post-hoc model analysis, particularly in the context of channel pruning, it is worth exploring further applications. For instance, could metrics derived from the channel influence matrix, such as entropy or diversity of influential channels, be leveraged to compare and evaluate different MTS models? Such metrics might provide insights into a model’s ability to capture complex channel relationships and its overall performance.

(5) For the selection of representative channels, I'm wondering if methods like top-k selection or adaptive sampling based on the influence score distribution be more appropriate?

(6) The 1-Layer MLP model in Table 3 appears to refer to a single-layer Multilayer Perceptron as the entire model architecture. It is intriguing that such a simple model can achieve comparable, and in some cases, superior performance to a more complex Transformer-based model?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new channel-wise influence function designed to address limitations in multivariate time series (MTS) analysis. Unlike previous model-centric methods, this approach provides a data-centric view, allowing the estimation of the influence of each channel within the MTS. The authors propose an influence function leveraging a first-order gradient approximation to improve MTS anomaly detection and forecasting tasks. Experimental results on various datasets indicate that the method outperforms traditional influence functions, especially in anomaly detection and channel pruning for forecasting.

### Strengths
Originality: Proposes a unique channel-wise influence function, filling an important gap in MTS analysis by focusing on data-centric rather than model-centric approaches.

Quality:Demonstrates robust experiments across datasets, highlighting improvements in MTS anomaly detection and forecasting.

Clarity: Clear, structured explanations and well-supported claims for the impact of the influence function on downstream MTS tasks.

Significance: The model holds practical relevance across domains where MTS is essential, particularly in applications needing channel-wise insights.

### Weaknesses
1. Figure 1 is not cited within the paper.
2. Algorithm 2 could be polished.

3. The paper does not sufficiently justify the need for channel pruning, especially given the marginal performance gains observed in Table 5. The core motivation seems to be interpretability, but the practical benefits for forecasting or anomaly detection tasks are not clearly demonstrated. The experiments should more rigorously test whether pruning leads to genuine improvements or if it is merely a computationally cheaper alternative with comparable performance.

4. The channel-wise influence function is presented as a data-centric approach, but its connection to the underlying model architecture (e.g., PatchTST) is not thoroughly explored. Given that PatchTST is channel-independent, the mechanism by which removing channels enhances overall performance requires more detailed explanation. The paper should address whether the influence function is truly capturing channel importance or if it is simply identifying channels with higher or lower predictability, which could be misleading in the context of overall MTS performance.

5. The analysis of channel interactions is limited. While the paper mentions that the influence matrix reflects channel correlations, it does not provide a detailed analysis of how these interactions evolve over time or how they impact model predictions. The paper should consider exploring dynamic channel relationships, as real-world MTS often exhibit time-varying dependencies.

### Questions
1. After channel pruning, does the final prediction use the pruned channels or the full set of channels? Clarifying this will help determine whether pruning directly improves prediction or simply reduces computational costs, and why are the pruned channels still accurately predicted? How does the model achieve this?

2. Given that PatchTST is channel-independent, how can we justify that removing channels enhances overall performance? For example, certain channels may have lower MSE due to higher predictability, while others may be more erratic, resulting in higher MSE. If more erratic channels are removed, this might artificially lower the overall MSE, which could be misleading.

3. Rather than pruning channels, would it be more insightful to analyze the interactions between channels? For example, investigating how one channel affects another could provide a deeper understanding of channel dependencies in MTS.

4. Real-world MTS often exhibit dynamic relationships between channels, which may vary over time. For instance, two channels might show positive correlation at one point and no correlation at another. Could pruning lead to a loss of such dynamic, context-dependent information?

5. From the results in Table 5, it appears that the pruned models only slightly outperform or match the full-channel models. This raises questions about the necessity and practical benefits of pruning. How does channel pruning substantively benefit the analysis or forecasting tasks, given these marginal differences?

6. Based on the above Q1 and Q2, the biggest confusion is：we think all comparison experiments should maintain consistent output channels (i.e., the same number of channels) to ensure fairness and accuracy when evaluating the model's performance?

### Soundness
3

### Presentation
3

### Contribution
3
