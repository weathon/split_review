# Expand and Compress: Exploring Tuning Principles for Continual Spatio-Temporal Graph Forecasting

- Decision: Accept
- Avg Score: 6.75
- Scores: 3, 8, 8, 8

## Abstract
The widespread deployment of sensing devices leads to a surge in data for spatio-temporal forecasting applications such as traffic flow, air quality, and wind energy. Although spatio-temporal graph neural networks (STGNNs) have achieved success in modeling various static spatio-temporal forecasting scenarios, real-world spatio-temporal data are typically received in a streaming manner, and the network continuously expands with the installation of new sensors. Thus, spatio-temporal forecasting in streaming scenarios faces dual challenges: the inefficiency of retraining models over newly-arrived data and the detrimental effects of catastrophic forgetting over long-term history. To address these challenges, we propose a novel prompt tuning-based continuous forecasting method, \model, following two fundamental tuning principles guided by empirical and theoretical analysis: \textit{\underline{e}xpand \underline{a}nd \underline{c}ompress}, which effectively resolve the aforementioned problems with lightweight tuning parameters. Specifically, we integrate the base STGNN with a continuous prompt pool, utilizing stored prompts (\ie, few learnable parameters) in memory, and jointly optimize them with the base STGNN. This method ensures that the model sequentially learns from the spatio-temporal data stream to accomplish tasks for corresponding periods. Extensive experimental results on multiple real-world datasets demonstrate the multi-faceted superiority of \model over the state-of-the-art baselines, including effectiveness, efficiency, universality, etc.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes EAC, a continuous spatio-temporal graph forecasting framework based on a continuous prompt parameter pool, aiming to address prediction challenges in dynamic streaming spatio-temporal data. EAC’s core idea is to freeze the base STGNN model and dynamically adjust the prompt parameter pool to adapt to new node data, achieving efficient knowledge transfer and mitigating catastrophic forgetting. The two tuning principles proposed in the paper, “expansion” and “compression,” along with their corresponding implementation schemes, demonstrate innovation and practical value.

### Strengths
1. The paper presents a prompt-based continuous spatio-temporal forecasting framework, EAC, introducing the “expansion” and “compression” principles and offering a new perspective on solving dynamic streaming spatio-temporal data prediction problems.
2. EAC can be combined with different STGNN architectures and performs well on various spatio-temporal data types.
3. By freezing the base STGNN model and adjusting a limited number of parameters in the prompt parameter pool, EAC can improve speed and reduce the number of parameters to be adjusted, demonstrating its efficiency.

### Weaknesses
Overall, my concerns are mainly about experiments.
(1) How does the performance of the schema adopt all historical spatio-temporal data for training, which is not mentioned in Fig. 1? It would be better if the performance of such schema were also discussed and included in the performance comparison. Specifically, the practical challenges of implementing a full historical training approach should be addressed, such as the computational cost of retraining and the memory requirements for storing all historical data. Furthermore, the impact of changing graph structures over time on the feasibility of this approach needs to be considered. 
(2) Section 5.2 provides a detailed comparison between different methods, and a further discussion on the difference in results across different domains (weather, traffic, and energy) should also be provided. This discussion should include an analysis of the unique characteristics of each domain that might influence model performance, such as the spatial dependencies and temporal dynamics inherent in each dataset. For example, the smoothness of traffic data compared to the more volatile nature of energy data should be explored.
(3) The efficiency of EAC is observed to be largely influenced by the scale of the dataset in Section 5.4. Thus, a more in-depth analysis of the impact of the dataset scale on the model performance should be provided. This makes the real-world application questionable. The analysis should include a discussion of how the number of nodes and the temporal length of the data affect the model's training time, memory usage, and prediction accuracy. Furthermore, the scalability of the proposed method compared to other approaches should be explicitly addressed.
(4) Many details of the baselines and datasets are missing. Specifically, the hyperparameter settings, network architectures, and training procedures for the baselines are not sufficiently detailed. For the datasets, the data preprocessing steps, feature selection methods, and statistical properties are not clearly specified.
(5) More baselines published in 2023 and 2024 should be considered. This is important to ensure that the proposed method is compared against the most recent state-of-the-art approaches in the field.

### Questions
Please address the questions above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a prompt-tuning approach for continual spatio-temporal graph forecasting, specifically addressing the challenges of dynamic data streams. The authors propose the EAC framework, guided by two tuning principles, "Expand" and "Compress," to handle continual learning in STGNNs. By utilizing a continual prompt pool, EAC allows the base STGNN to accommodate new data while minimizing catastrophic forgetting. The authors demonstrate the approach’s effectiveness across various datasets, showcasing improvements in efficiency and adaptability compared to other methods.

### Strengths
S1.  EAC’s application of prompt tuning principles in continual spatio-temporal forecasting is novel, integrating dynamic prompt pool adjustments to effectively handle incoming data.
S2. The methodology is backed by both empirical and theoretical analysis, and the explanations are clear.
S3. The experimental results are impressive.

### Weaknesses
W1: While EAC is compared with several traditional and just-in-time tuning baselines, it is not included in comparison with other recent continuous learning techniques, such as combinations with reinforcement learning (Xiao et al., 2022) and data augmentation (Miao et al., 2024) mentioned in RELATED WORK. The reasons for the missing baselines are required. 
W2: The Prompt Parameter Pool in EAC may introduce an issue of parameter bloat, which needs to be discussed.

### Questions
See the above.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel framework, EAC, for continual spatio-temporal graph forecasting. The authors address the challenges of retraining inefficiency and catastrophic forgetting in streaming spatio-temporal data scenarios by proposing a prompt tuning-based approach. They present two tuning principles—expand and compress—that guide both empirical and theoretical analysis. The expand principle addresses the dynamic heterogeneity of the data, while the compress principle tackles parameter inflation. Results demonstrate that EAC is effective, efficient, universal, and lightweight in tuning, with extensive experiments on real-world datasets supporting these claims.

### Strengths
- The problem addressed is significant, as spatio-temporal graph forecasting has applications in areas such as traffic flow and air quality monitoring. The proposed solution offers potential improvements in efficiency and model effectiveness in dynamic, real-world environments compared to previous methods.

- The paper presents a novel approach to continual learning within the context of spatio-temporal graph forecasting. The exploration of prompt tuning principles is innovative, and the authors offer a detailed and well-supported discussion of existing paradigms along with an extensive experimental analysis.

- The methodology is well-developed, with clear explanations of the theoretical foundations and empirical insights leading to the expand and compress tuning principles. While node-level parameters and low-rank decomposition are common in the field, the authors’ thorough analysis and discussion bring valuable new perspectives.

- The paper is well-organized and clearly written, making complex concepts accessible. The figures and tables are clear and complement the textual explanations effectively.

### Weaknesses
 - While the prompt-based tuning paradigm for continual spatio-temporal forecasting is novel, similar recent methods [1,2,3] are only briefly mentioned in related work. A more detailed discussion of these approaches and their connection to the present work would be beneficial. Specifically, the authors should clarify how their method differs from these approaches in terms of handling dynamic graph structures and continuous learning scenarios. For instance, do these methods also employ node-level prompts, and how do they address the challenge of parameter inflation in the context of streaming data?

 - The approach still has several limitations, such as performance over long time spans and parameter inflation. Although the authors address these limitations in the appendix, the core paper should include a more detailed discussion of the trade-offs between model performance and parameter growth, especially as the number of nodes and time steps increase. The paper should also explore the practical implications of these limitations, such as the computational resources required for large-scale deployments and the potential for performance degradation over extended periods.

### Questions
- The authors note that the choice of pre-training backbone model is crucial. Does this imply that their method is more effective with larger-scale STGNN backbones?

- How would the EAC model adapt if the graph were to shrink, for instance, due to the removal of sensors or monitoring stations? Why was this scenario not included in the comparisons?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper addresses the challenges of continual learning in spatio-temporal forecasting, particularly for data streams that evolve due to the deployment of new sensors. Traditional spatio-temporal graph neural networks struggle with retraining inefficiencies and catastrophic forgetting when applied to such streaming data scenarios. To overcome these issues, the authors propose a novel method called EAC (Expand and Compress). The proposed approach enhances the model’s capacity to manage evolving data without the need for full retraining, ensuring efficient and effective handling of dynamic spatio-temporal data streams.

### Strengths
1. The paper addresses a highly practical problem in spatio-temporal graph forecasting. On the one hand, new sensors are deployed over time, on the other hand, the patterns of spatio-temporal dynamics evolve.

2. One of the strengths of the paper lies in its strong motivation, backed by both empirical and theoretical analysis.  The authors provide a clear rationale for addressing catastrophic forgetting and the challenges of handling dynamic, continuously evolving spatio-temporal data.

3. The proposed method is reasonable.  I appreciate the idea of fixing the backbone of the spatio-temporal graph model and updating the prompt pool.  This approach strikes a balance: on the one hand, it preserves knowledge from previously trained samples, and on the other hand, it adapts to new incoming data effectively.

### Weaknesses
1. The design of the prompt pool is not clearly explained. Specifically, it is unclear what the prompt pool contains and how exactly these prompts are utilized within the model. Additionally, there is a lack of clarity on how the system handles the incorporation of new sensors in dynamic environments, which is a crucial aspect of the proposed approach.

2. The evaluation lacks a comparison with models trained separately for each period. While the proposed continual learning method shows promising results, it is essential to establish a performance upper bound by comparing it to a scenario where separate models are trained for different periods. 

3. While the method outperforms baselines, I am concerned about its long-term effectiveness. In Figure 5, the model’s performance shows significant degradation over time, with the RMSE increasing from 24 to 28—indicating a more than 10% reduction in performance. Although this is in the context of few-shot learning, I suspect a similar trend would be observed in non-few-shot scenarios as well.
While separate training for each period may be more time-consuming, it could potentially achieve better performance, and it is storage-efficient since only the latest model needs to be saved. Therefore, it is crucial to assess whether the trade-off between reduced performance and computational efficiency is truly justified.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
