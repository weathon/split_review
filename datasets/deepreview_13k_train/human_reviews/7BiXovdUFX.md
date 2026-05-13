# OCEAN: Online Multi-modal Root Cause Analysis for Microservice Systems

- Decision: Reject
- Scores: 5, 3, 5, 3, 3

## Abstract
Root Cause Analysis (RCA) is essential for pinpointing the root causes of failures in microservice systems. Traditional data-driven RCA methods are typically limited to offline applications due to high computational demands, and existing online RCA methods handle only single-modal data, overlooking complex interactions in multi-modal systems. In this paper, we introduce OCEAN, a novel online multi-modal causal structure learning method for root cause localization. OCEAN employs a dilated convolutional neural network to capture long-term temporal dependencies and graph neural networks to learn causal relationships among system entities and key performance indicators. We further design a multi-factor attention mechanism to analyze and reassess the relationships among different metrics and log indicators/attributes for enhanced online causal graph learning. Additionally, a contrastive mutual information maximization-based graph fusion module is developed to effectively model the relationships across various modalities. Extensive experiments on three real-world datasets demonstrate the effectiveness and efficiency of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the OCEAN framework for online multi-modal root cause analysis (RCA) in microservice systems, showing significant improvements in accuracy and computational efficiency across multiple real-world datasets. However, it is critiqued for its limited methodological innovation. While the approach achieves good results, it primarily builds on existing techniques, such as dilated convolution, which have been extensively studied in related research. The paper focuses on addressing common challenges in multi-modal learning that have already been explored, rather than tackling the specific and unique challenges of multi-modal RCA. Additionally, it lacks a clear explanation of how its methods enhance real-time processing and reduce resource consumption. Minor issues include inconsistencies in the font of an equation.

### Strengths
This paper presents a novel and highly effective approach to online multi-modal root cause analysis in microservice systems. The proposed OCEAN framework showcases impressive advancements in both accuracy and computational efficiency, achieving good results across multiple real-world datasets.

### Weaknesses
Limited Innovation and Contribution: While the paper achieves good results, it lacks methodological innovation specifically for online root cause analysis. For example, the core method used to reduce computational time, dilated convolution, has been previously employed. Although the appendix discusses its time complexity in comparison to LSTM and Transformers, paper [1] as early as 2018 introduced the use of dilated convolutional neural networks for capturing temporal dependencies. Furthermore, paper [2] in 2022 utilized this approach specifically for capturing long-term temporal dependencies.
The proposed methods primarily address common issues (C1,C2, and C3) in multi-modal learning and do not make substantial progress in tackling the unique challenges of root cause analysis in the multi-modal domain. For example, Method 2, as referenced in the paper, utilizes approaches similar to those in MULAN[3] to extract multi-modal features from offline datasets. However, this paper lacks a detailed explanation of the potential relationships among factors from both modalities and does not clarify why it achieves better results than MULAN. Furthermore, in Method 3, Learning Multi-modal Causal Structures, the paper does not adequately address modality reliability or the reliability of the causal graph, leaving the approach lacking in clear interpretability.
Motivation Not Clear: The primary novelty of this paper appears to focus on "online" multi-modal root cause analysis (RCA) for microservice systems. However, the methodology introduced lacks a clear explanation of how it enhances real-time processing capabilities or reduces resource consumption in practice. The paper proposes the use of dilated convolutional neural networks (DCNNs) and a graph-based approach but does not sufficiently justify how these choices directly contribute to improved real-time performance or lower computational overhead.
•Minor Issues: The font in Equation (13) is somewhat inconsistent.

### Questions
In the "weaknesses" part, it is essential to address all the issues mentioned, particularly the concern that the proposed methods appear to be direct employment of existing approaches and seem to target general problems in multimodal scenarios rather than being specifically tailored for multimodal Root Cause Analysis (RCA). Additionally, a clear explanation is needed as to why the proposed methods can improve real-time performance and reduce resource consumption. This should be supported by supplementary experimental evidence.

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
In this paper, the authors proposed a new online causal structure learning method from time series which is then evaluated in microservice systems RCA problem. The authors combine a so-called dilated CNN and GCN to learn the structure by autoregressively forecasting the future time series. In addition, an attention mechanism is used to reweight and fuse the learned graph. Finally, random walk with restart is used to determine the root cause using the learned graph. Experiments show the effectiveness of the proposed method.

### Strengths
1. The proposed method seems to be effective, which outperforms many existing methods.

### Weaknesses
1. The introduction and problem definition is not clear, especially the multi-model part and online setting part. The paper is more about online causal structure learning from time series and is evaluated in the microservice setting. The authors are suggested to change the title and rewrite the introduction to stand out the focus of the paper. 
2. The experimental setting is not clear. The online evaluation setting is not described, nor the online problem setting. The authors are suggested to define the online problem setting and clearly describe the evaluation setting. 
3. The source code is not provided, which makes reproducibility of the paper low. The authors are suggested to open source the code.
4. Please clearly define online / offline RCA in introduction. RCA is usually triggered by KPI anomalies. Therefore, it is not a function that needs to be conducted continuously, like anomaly detection. I believe many of the existing works have been deployed in the production system. Are they online RCA methods according to the authors' definition? It is not clear to me that the authors stated that most existing methods are designed for offline use. Methods can be trained offline and used online.
5. The example in the introduction stating that log is necessary apart from metrics is not convincing. "Disk Space Full" can be solely identified by metrics. Regarding "Database Query Failures", what specific problem do the authors want to identify? For which kind of system OLTP or OLAP? Why is solely using metrics not enough?
6. When talking about multi-modal data, the authors metrics and logs, why not consider trace, which seems to be more important for microservice systems. For instance, [1] proposed a method deployed in the production system which considers both metrics and traces and this work is overlooked by the authors.
7. "T1", "T2", "n-1" and $d_M$ are defined without usage in line 156.
8. It seems that the authors converted log to metric data. The problem is only defined on metric data. What is the difference between the old metrics and new metrics converted from log? For me, at least the method is only for single modal data. It is not clear why existing single model methods cannot be applied in such a setting.
9. In the problem definition, the authors ignore the physical relation but propose to use a purely data-driven model to learn the causal structure. Relationships like which service calls the other service, which pod is in which virtual machines and which physical machines, are known but ignored. Can the authors explain the reason behind such a choice? Which practical scenario matches the setting that the authors would like to study?
10. After reading Section 3, I found that the main focus of the paper is online causal graph learning from time series data. The title and introduction is way broader than the studied problem, which does not match to the content of the paper from my point of view. Moreover, in the microservice setting, why would the causal graph be changing overtime if it is a causal graph reflecting the ground truth? The authors are suggested to better motivate this point.
11. The proposed model seems to be very complex with several components. How many weights does the model own? How do the authors avoid overfitting and catastrophical forgetting problems during online structure learning?
12. In Table 2, the proposed method can be used for both metric only and log only settings. The authors are suggested to give both results.
13. The experimental setting is not clear. Since the proposed method is online, so when will the proposed method be used? What is the batch used for evaluation? And after how batches will the method be evaluated? Again, this confusion may be due to the fact that the online setting is not clearly defined.
14. It seems that there is no code to reproduce the experiments. In addition, did the authors reproduce the results from other methods or copy the number from their paper? Please give the specific parameter setting or state clearly that the numbers are copied from the papers.

### Questions
1. Please clearly define online / offline RCA in introduction. RCA is usually triggered by KPI anomalies. Therefore, it is not a function that needs to be conducted continuously, like anomaly detection. I believe many of the existing works have been deployed in the production system. Are they online RCA methods according to the authors' definition? It is not clear to me that the authors stated that most existing methods are designed for offline use. Methods can be trained offline and used online.
2. The example in the introduction stating that log is necessary apart from metrics is not convincing. "Disk Space Full" can be solely identified by metrics. Regarding "Database Query Failures", what specific problem do the authors want to identify? For which kind of system OLTP or OLAP? Why is solely using metrics not enough?
3. When talking about multi-modal data, the authors metrics and logs, why not consider trace, which seems to be more important for microservice systems. For instance, [1] proposed a method deployed in the production system which considers both metrics and traces and this work is overlooked by the authors.
4. "T1", "T2", "n-1" and $d_M$ are defined without usage in line 156.
5. It seems that the authors converted log to metric data. The problem is only defined on metric data. What is the difference between the old metrics and new metrics converted from log? For me, at least the method is only for single modal data. It is not clear why existing single model methods cannot be applied in such a setting.
6. In the problem definition, the authors ignore the physical relation but propose to use a purely data-driven model to learn the causal structure. Relationships like which service calls the other service, which pod is in which virtual machines and which physical machines, are known but ignored. Can the authors explain the reason behind such a choice? Which practical scenario matches the setting that the authors would like to study?
7. After reading Section 3, I found that the main focus of the paper is online causal graph learning from time series data. The title and introduction is way broader than the studied problem, which does not match to the content of the paper from my point of view. Moreover, in the microservice setting, why would the causal graph be changing overtime if it is a causal graph reflecting the ground truth? The authors are suggested to better motivate this point.
8. The proposed model seems to be very complex with several components. How many weights does the model own? How do the authors avoid overfitting and catastrophical forgetting problems during online structure learning?
9. In Table 2, the proposed method can be used for both metric only and log only settings. The authors are suggested to give both results.
10. The experimental setting is not clear. Since the proposed method is online, so when will the proposed method be used? What is the batch used for evaluation? And after how batches will the method be evaluated? Again, this confusion may be due to the fact that the online setting is not clearly defined.
11. It seems that there is no code to reproduce the experiments. In addition, did the authors reproduce the results from other methods or copy the number from their paper? Please give the specific parameter setting or state clearly that the numbers are copied from the papers. 

[1] ShapleyIQ: Influence Quantification by Shapley Values for Performance Debugging of Microservices. ASPLOS 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article proposes the OCEAN model for anomaly detection in microservice systems. It uses diffuse convolution to capture long-term temporal dependencies, introduces two modalities of data, log data and metric data, and adaptively models the causal relationship structure between and within data based on the attention mechanism. It also develops a contrast graph fusion module based on mutual information maximization to effectively model the relationship between various modalities.

### Strengths
Quality: The experimental workload of the article is relatively substantial.
Significance: It provides a multi-modal solution for anomaly detection in online micro-systems.

### Weaknesses
-This paper introduces diffuse convolution to model long-term temporal dependencies, attention mechanism to model causal structures, and mutual information fusion causal graphs, and describes and experiments with them as the core innovations of this paper. However, these three methods have been around for a long time, and the author did not explain well how this paper improves them.
-Causal graph learning is an important component of the OCEAN model, but lack of corresponding causal analysis or experimental results.
-There are many errors in the article's consistency of symbols and textual expression.

### Questions
1. On page 2, line 83, the author introduces a factor attention mechanism to analyze the relationship between different factors and re-evaluate their impact on online causal graph learning. As far as I know, many methods use attention mechanisms to model and analyze the relationship between different variables, as shown in references 1-2. What is the essential innovation of this paper compared with them?
[1] Wu X, Ajorlou A, Wu Z, et al. Demystifying over-smoothing in attention-based graph neural networks[C]. Advances in NeurIPS, 2024.
[2] Cai J, Zhang M, Yang H, et al. A novel graph-attention based multimodal fusion network for joint classification of hyperspectral image and LiDAR data[J]. Expert Systems with Applications, 2024, 249: 123587.
2. Page 4, line 186 indicates that this paper uses the 2021 MSSA algorithm and claims it is the most advanced online fault detection method. Why is the most advanced online fault diagnosis method from 2021? We searched for several online fault diagnosis algorithms published in recent years as shown in references 1-2.
[1] Zeiser A, Özcan B, van Stein B, et al. Evaluation of deep unsupervised anomaly detection methods with a data-centric approach for on-line inspection[J]. Computers in Industry, 2023, 146: 103852.
[2] Wang X, Yao Z, Papaefthymiou M. A real-time electrical load forecasting and unsupervised anomaly detection framework[J]. Applied Energy, 2023, 330: 120279.
3. The dimensions of \textbf{\emph{H}}_{0}^{M}[\emph{j}]^{T} and \textbf{\emph{W}}^{3} in Formula 9 are [T_3 \times \emph{d}_{M}] and [T_3 \times T_3] respectively. Why can they be directly matrix multiplied?
4. Among the 7 compared algorithms, is it fair to compare them with 4 algorithms that focus on learning causal graphs rather than fault diagnosis algorithms? We list some recent fault diagnosis algorithms as shown in the references 1-3.
[1] Chen, D., Liu, R., Hu, Q., & Ding, S. X.. Interaction-aware graph neural networks for fault diagnosis of complex industrial processes. IEEE Transactions on neural networks and learning systems, 2021, 34(9), 6015-6028.
[2] Liu Y, Jafarpour B. Graph attention network with Granger causality map for fault detection and root cause diagnosis[J]. Computers & Chemical Engineering, 2024, 180: 108453.
[3] Zhou Q, Pang G, Tian Y, et al. AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection[C]. The Twelfth International Conference on Learning Representations,2024.
5. The authors show that the proposed method can learn inter-modal and intra-modal causal graphs. Can the learned causal graph structure be further demonstrated experimentally?
6. There are many errors in the organization logic, symbol unification and text expression of the article, so I suggest careful revision. For example: \emph{d}_{M} in line 158 does not match the description given in Table 1; two identical \textbf{\emph{a}}^{0}_{L}[\emph{j}] appear in line 291 of page 6; there is missing punctuation before “so that” in line 304, etc.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes OCEAN as an online RCA method for multi-modal data in microservice systems. It combines dilated CNNs and GNNs to model temporal dependencies and causal relationships, with a multi-factor attention mechanism and a graph fusion module for cross-modal integration. Experiments show OCEAN’s effectiveness and efficiency in real-time RCA.

### Strengths
1. Clear presentation of RCA, especially in the area of multi-modal RCA.
2. Extensive experimental validations.
3. I beileve that the multi-modal information is of importance for RCA, as the combination from diverse sources might be beneficial.

### Weaknesses
1. **Main concern 1**:  The necessity of introducing causal discovery (CD) into root-cause analysis.
- RCA is a differenct task from CD,as the former requires identifying a subset of variables while the latter requires the identification of orientations.
- When the prior knowledge is present, e.g., in some cases of microservices, the causal graph is already given. When the prior knowledge is not sufficient, the discovery of causal graph is lack of validation, and the resulting RCA becomes wield.
- My suggestion is that, based on the SCM model, designing some statistics from the data rather the first-discover-then-identify approach, as the latter paradigm is somehow incremental and risky.

2. **Main Concern 2**: As this paper is not the first work to introduce multi-modal information into RCA, I think that this paper should focus on building theoretical understanding on why and how multi-modal information will be beneficial towards RCA. The contribution of this paper, including a causal-structure learning module and a temporal learning framework, seems very incremental such that I do not agree that this paper's novelty reaches the bar of ICLR.

### Questions
See Weaknesses

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents OCEAN, an online multi-modal method for root cause analysis (RCA) in microservice systems. The approach utilizes various techniques, including a dilated convolutional neural network to capture long-term temporal relationships, multi-factor attention for encoding feature correlation, a graph neural network (GNN) for identifying causal relationships, and a random walk with revisiting on the derived causal graph for ranking root causes, etc.

### Strengths
- The problem of online multi-modal RCA is highly relevant and valuable.
- The performance of OCEAN appears to be exceptional.

### Weaknesses
 - The notations used throughout the paper lack clarity.
- Several implementation details are omitted, such as the architecture of the MLP used in L_MI and the hyperparameters.

- The notations in the problem statement are not sufficiently clear, e.g.,  $n-1$ and $d_M$ in line 158. It would be helpful for the authors to specify the dimensions of the matrices involved. Additionally, do all system entities share the same "entity metrics" as features?

- Is $n-1$ referring to the number of system "entities" or "entity metrics"?
- Is only one system KPI considered?  Is the bold symbol $\boldsymbol{y}$ simply a one-dimensional vector? I had assumed multiple KPIs could be monitored.
- I find it challenging to understand the replication of the KPI $d_M$ times to create a tensor version of $\hat{X}$. If all entities share the same "metrics," that makes sense; could you clarify this?
- The 1-D dilated convolution described in Eq. (2-5) is unclear. Is $\boldsymbol{f}(t)$ a scalar or a vector? Additionally, could you elaborate on Eq. (2-3) in relation to the tensor input x? What is the rationale for using "two" 1D kernels and activation functions (tanh, sigmoid) in Eq. (3)?

- It seems that Eq. (8) or Eq. (13) represents the loss for only the i-th batch, yet the authors incorporate them into their final objective (18). What is the precise training procedure for the online framework?

- If the goal is to maximize (14), then L_MI in (18) should have a negative sign.

- In Figure 2 (b,c,d), the setting of other hyper-parameters should be revealed. 
- The proposed method is based on GCN for causal discovery, have you tried other GNN-based causal discovery methods?

- The choice of $\lambda_2$ and $\lambda_3$ in Figure 2b is unclear. How are these parameters selected?

### Questions
1. The notations in the problem statement are not sufficiently clear, e.g.,  $n-1$ and $d_M$ in line 158. It would be helpful for the authors to specify the dimensions of the matrices involved. Additionally, do all system entities share the same "entity metrics" as features?

I would appreciate clarification on the following points:

- Is $n-1$ referring to the number of system "entities" or "entity metrics"?
- Is only one system KPI considered?  Is the bold symbol $\boldsymbol{y}$ simply a one-dimensional vector? I had assumed multiple KPIs could be monitored.
- I find it challenging to understand the replication of the KPI $d_M$ times to create a tensor version of $\hat{X}$. If all entities share the same "metrics," that makes sense; could you clarify this?
- The 1-D dilated convolution described in Eq. (2-5) is unclear. Is $\boldsymbol{f}(t)$ a scalar or a vector? Additionally, could you elaborate on Eq. (2-3) in relation to the tensor input x? What is the rationale for using "two" 1D kernels and activation functions (tanh, sigmoid) in Eq. (3)?

2. It seems that Eq. (8) or Eq. (13) represents the loss for only the i-th batch, yet the authors incorporate them into their final objective (18). What is the precise training procedure for the online framework?

3. If the goal is to maximize (14), then L_MI in (18) should have a negative sign.

4. In Figure 2 (b,c,d), the setting of other hyper-parameters should be revealed. 
5. The proposed method is based on GCN for causal discovery, have you tried other GNN-based causal discovery methods?

### Soundness
2

### Presentation
1

### Contribution
3
