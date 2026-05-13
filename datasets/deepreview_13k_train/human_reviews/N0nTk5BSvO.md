# TESTAM: A Time-Enhanced Spatio-Temporal Attention Model with Mixture of Experts

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Accurate traffic forecasting is challenging due to the complex interdependencies of large road networks and abrupt speed changes caused by unexpected events. 
Recent work has focused on spatial modeling with adaptive graph embedding or graph attention but has paid less attention to the temporal characteristics and effectiveness of in-situ modeling. 
In this paper, we propose the time-enhanced spatio-temporal attention model (\toolname) to better capture recurring and non-recurring traffic patterns with mixture-of-experts model with three experts for temporal modeling, spatio-temporal modeling with a static graph, and spatio-temporal dependency modeling with a dynamic graph. 
By introducing different experts and properly routing them, \toolname better captures traffic patterns under various circumstances, including cases of spatially isolated roads, highly interconnected roads, and recurring and non-recurring events. 
For proper routing, we reformulate a gating problem as a classification task with pseudo labels. Experimental results on three public traffic network datasets, METR-LA, PEMS-BAY, and EXPY-TKY, demonstrate that \toolname outperforms 13 existing methods in terms of accuracy due to its better modeling of recurring and non-recurring traffic patterns

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel deep learning model named TESTAM, which individually models recurring and non-recurring traffic patterns by a mixture-of-experts model with three experts on temporal modeling, spatiotemporal modeling with static graph, and dynamic spatio-temporal dependency modeling with dynamic graph.
By introducing different experts and properly routing them, TESTAM could better model various circumstances, including spatially isolated nodes, highly related nodes, and recurring and non-recurring events.
The evaluation is conducted with three open datasets and compares the proposed method and existing methods.

### Strengths
The idea of the proposed method, which utilizes multiple experts models and switches between them adaptively to deal with various traffic conditions, is reasonable and interesting for forecasting urban traffic affected by various factors.

The proposed method's level of prediction compared to existing techniques is demonstrated by utilizing three datasets and comparing it to a number of existing methods.

The structure of the paper is easy to understand and the individual contents are clearly described.

### Weaknesses
Table 1 shows that the error is small in many conditions compared to existing methods, but the difference is not large, and it is not clear what the significance of this error is.

It is also not clear where the computational cost of the proposed method in model building and forecasting stands in comparison to other methods. In my opinion, this is important information, especially how the proposed method relates in terms of computational cost to methods that do not have very large differences in accuracy.

It is not clear how the proposed method is able to deal with the "various circumstances" described in the intro of the paper.

### Questions
Once the information pointed out in Weakness is clarified, the validity of the proposed method will become clearer.
Could the authoer please clarify these points?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a mixture of experts model for traffic forecasting where each expert model uses a different spatial correlation learning model. In addition, a time-enhanced attention is added to help model the temporal correlation on top of the usual attention module. Experiments haven been conducted on three datasets, two of which of commonly used benchmark datasets. There are 13 baseline models, including one from 2022 and one from 2023.

### Strengths
1. While the core of the proposed model is based on mixture of experts, there are new designs to the components including an extra time-enhanced attention module and an enhanced routing classification loss considering the best-routing selection. 

2. The paper is very well written overall and is easy to follow. 

3. There are quite a few baseline models including some of the latest.

### Weaknesses
The main issue of the paper is perhaps the relatively weak experimental results. As shown in Table 1, the proposed model TESTAM has very similar performance to MegaCRN (Jiang et al., 2023) and sometimes PM-MemNet (Lee et al., 2022). 

There are no model training time results. I wonder if TESTAM is even slower than MegaCRN and/or PM-MemNet to train. 

The discussion of the results have focused on comparisons with GMAN and StemGNN which are from 2020 and are relatively "old" methods already. 

Overall, the importance of the proposed techniques has not been shown with strong evidence. 

Minor presentation issues:
Typo: "is noisy sensitive", "ahve", "Let define";
Check "where f(X(t), θ)" below Equation 1;
Grammar: "traffic data is noisy and contains many non-stationary, make the best route selection hard."

### Questions
See the weak points.

### Soundness
3 good

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
In this paper, authors introduce TESTAM, a novel Time-Enhanced Spatial-Temporal Attention Model to realize accurate traffic forecasting. TESTAM is a Mixture-of-Experts model that incorporates attention mechanisms, allowing real-time spatial modeling under both normal and abnormal circumstances. By reformulating the routing problem as a classification task, TESTAM can adapt to different traffic conditions, enabling the selection of appropriate spatial modeling methods.

### Strengths
- S1. Considering the complex dependency on road networks, the use of an expert mixture model in spatial-temporal forecasting is an innovative design.

- S2. The paper provides a clear categorization of spatial modeling types for spatial-temporal forecasting, and the selection of different spatial models (identity experts, adaptive experts, attention experts) is highly representative.

### Weaknesses
W1. There are many typos, and some incorrect writings can seriously mislead the readers:
   - '...choose spatial modeling methods (i.e., expert) properly; and' on page one.
   - $f(X^{(t)},\theta)$ should be replaced by 'g(X^{(t)},\theta)' on page three.
   - In the formulas at the bottom of page five, the superscript (k) in $W_{q}^{(k)}$ and $W_{k}^{(k)}$ appears to be meaningless and should be replaced by $W_q$ and $W_k$.
   - On the fifth page, $\[\tau^{(t+1),...,\tau^{(t+T)}\]$ should be changed to $\[\tau^{(t+1),...,\tau^{(t+T')}\]$.
   - In formula 5 on the sixth page, 'larger than q-th quantile' should be corrected to 'smaller than q-th quantile.'
   - In the seventh page, the sentence 'excludes the relatively coarse-grained loss function only' should have 'only' removed.
   - The functions such as 'Concat' and the activation functions 'relu' should be written as upright letters.
   - Some formulas have equation numbers, while others do not.

W2. The effectiveness of Time-enhanced Attention has not been verified through ablation experiments, and readers cannot determine whether it truly enhances the model's predictive performance.

W3. The distinction between best-route selection and worst routing avoidance is not clear. When introducing best-route selection, the authors mention node-wise routing and node-wise pseudo-label but haven't explained them. Additionally, changing 'smaller than q-th quantile' to 'smaller than (1-q)-th quantile' alone is considered best-route selection, but the reason for this change has not been provided.

W4. Experimental results:
   - The experimental results are inconsistent. In Table 2, the results for TESTAM in the ablation experiment are for a 30-minute forecast, but they do not match the results in Table 1. Additionally, I noticed that in Table 2, the PEMS-BAY dataset performs better in the 'w/o gating' condition than the complete TESTAM model in Table 1.

   - The magnitude of the performance improvement is minimal. Table 1 shows that many metrics only slightly improve in terms of percentiles, at the cost of three times the computational time and memory for building three expert models.

W5. The title doesn’t well match with this study itself. Actually, this work mostly focuses on traffic forecasting, but the title   suggesting a new general Spatio-Temporal Attention Model with MoE seems much more general and broader.

### Questions
Q1- Q2: Please refer  to W3 and W4.
Q3. In memory-based gating networks, why the similarity between the model's input and output is used as the routing probability? This lacks a certain theoretical foundation (or some analysis) and explanation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors point out that accurate traffic forecasting requires capturing two distinct traffic patterns, recurring and non-recurring. To accomplish this goal, they propose TESTAM, a mixture-of-expert model with three heterogeneous experts responsible for different aspects of spatio-temporal modeling. By properly routing the experts, the model learns to handle various circumstances adaptively. Experimental results on three benchmark datasets verify the effectiveness of TESAM.

### Strengths
1. The manuscript is well-organized and easy to follow.
2. The introduction of mixture-of-expert models increases the capacity of spatial modeling for traffic forecasting, and to some extent, increases the interpretablility.

### Weaknesses
1. In terms of spatial and temporal modeling, this manuscript does not seem to bring new techniques. The use of graph neural networks for spatial modeling and recurrent networks or attention mechanisms for temporal modeling is quite standard. The authors should clarify what specific innovations they have introduced in these modules beyond existing approaches. For example, are they using a novel graph convolution or attention mechanism, or are they simply applying existing techniques to a new problem?
2. There are multiple sets of terminologies describing the same thing without an explicit connection. For example, when categorizing traffic patterns, both "recurring vs non-recurring" and "normal vs abnormal" (in Conclusion) are used; when describing the three experts, "temporal modeling, spatio-temporal modeling with static graph, spatio-temporal modeling with dynamic graph" (in Abstract) and "identity experts, adaptive experts, attention experts" (in Figure 1). The lack of clarity in the roles of the three experts is particularly problematic. It is unclear how the 'identity expert' performs temporal modeling, and how it differs from the temporal aspects of the other two experts. Clarifying these key concepts and providing a consistent terminology will make the presentation clearer.
3. Only the overall metrics for predicting accuracy are reported. It is unclear what recurring and non-recurring patterns that TESTAM captured while other methods miss. Some in-depth experimental analysis (see Q4 for details) will better support the claim of the first contribution. The authors should provide a breakdown of performance on different types of traffic patterns, such as recurring congestion during rush hour versus non-recurring congestion due to accidents. Without this, it is difficult to assess whether the mixture-of-experts approach is truly effective at capturing different traffic dynamics.

### Questions
1. Why the proposed method is abbreviated as TESTAM?
2. What does "in-situ" mean in the context of this manuscript?
3. The temporal information embedding and time-enhanced attention seem novel for traffic forecasting. Do they affect the performance? Some discussion or ablation study is needed.
4. In the abstract, the authors state that TESTAM can model isolated nodes, highly related nodes, and recurring and non-recurring events. Can you provide some experimental results and analysis for this claim, e.g. case study?

Minor:
1. Please add comments to the meaning of results in bold and underlined in Table 1.
2. Descriptions and analysis of the qualitative examples in the supplementary material are missing.
3. Why are some equations in section 3 not numbered? I believe some of them are proposed by the authors, e.g. time-enhanced attention, and thus should be numbered.
4. Please provide an explicit formula for the best-route loss, at least in the supplementary material.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
