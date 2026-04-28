# Structural Fairness-aware Active Learning for Graph Neural Networks

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Graph Neural Networks (GNNs) have seen significant achievements in semi-supervised node classification. Yet, their efficacy often hinges on access to high-quality labeled node samples, which may not always be available in real-world scenarios. While active learning is commonly employed across various domains to pinpoint and label high-quality samples based on data features, graph data present unique challenges due to their intrinsic structures that render nodes non-i.i.d. Furthermore, biases emerge from the positioning of labeled nodes; for instance, nodes closer to the labeled counterparts often yield better performance. To better leverage graph structure and mitigate structural bias in active learning, we present a unified optimization framework (SCARCE), which is also easily incorporated with node features.  Extensive experiments demonstrate that the proposed method not only improves the GNNs performance but also paves the way for more fair results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Existing active learning models for GNNs heavily rely on the quality of initial node features and ignore the impact of label position bias in the selection of representative nodes. To address these limitations, this paper proposes a novel framework called SCARCE.

### Strengths
+ They identify the limitations in current active learning methods, specifically the oversight regarding feature quality and position bias.
+ They propose a novel framework to tackle the aforementioned limitations.
+ Extensive experiments validate the effectiveness of the proposed framework.

### Weaknesses
 - There are concerns regarding the fundamental motivation behind active learning. While the primary motivation for active learning lies in the difficulty of obtaining high-quality labels in real-world scenarios, the iterative addition of labels for learned target nodes during the optimization process raises doubts about the original motivation. This creates some contradiction as it suggests that labels for target nodes might be easy to obtain.
- The improvement compared to baselines seems not statistically significant.
- They argue that existing methods heavily rely on the quality of initial node features while the proposed framework can mitigate this problem. However, there lack of experimental support. The features of datasets seem typical, lacking any characteristics such as unavailability and noise. There is a need for a quantifiable evaluation to support this point.

### Questions
Please refer to the weaknesses.
- There are concerns regarding the fundamental motivation behind active learning. While the primary motivation for active learning lies in the difficulty of obtaining high-quality labels in real-world scenarios, the iterative addition of labels for learned target nodes during the optimization process raises doubts about the original motivation. This creates some contradiction as it suggests that labels for target nodes might be easy to obtain.
- The improvement compared to baselines seems not statistically significant.
- They argue that existing methods heavily rely on the quality of initial node features while the proposed framework can mitigate this problem. However, there lack of experimental support. The features of datasets seem typical, lacking any characteristics such as unavailability and noise. There is a need for a quantifiable evaluation to support this point.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a unified optimization framework for active learning on graph neural networks (GNNs) that can flexibly incorporate different selection criteria such as structure inertia score (SIS) and label proximity score (LPS) variance. It is empirically demonstrated that SCARCE outperforms existing baselines on node classification tasks across multiple benchmark datasets. In particular, SCARCE achieves higher accuracy than methods like FeatProp and GraphPart while also enhancing fairness by reducing variance in LPS across nodes.

### Strengths
(1) This paper is generally well-organized and easy-to-follow.

(2) The proposed unified optimization framework is flexible and does not require extensive hyperparameter tuning, which is especially useful for active learning. In addition, the scalability seems promising as well.

(3) The superiority on utility and fairness seems significant given the presented results in section 4.3 and 4.4.

### Weaknesses
(1) There lacks a formal introduction of the notion for fairness at the beginning of this paper.

(2) Despite the discussion on scalability, this paper does not perform any experiments on large-scale network datasets. The scalability discussion remains theoretical without empirical validation on datasets with millions of nodes.

(3) Only performing experiments on two GNN backbones undermines the superiority of the proposed framework. In addition, one advantage of this paper lies in the applicability on featureless networks, which is not tested in this paper either. The experiments should include a wider range of GNN architectures and explicitly test the performance on graphs where node features are absent or unreliable.

### Questions
(1) I would suggest to add a formal introduction about the fairness notion studied in this paper in Section 2, and add a descriptive discussion in the Introduction accordingly.

(2) If the proposed framework can be easily generalized onto large network data, will the performance superiority still be maintained?

(3) If the proposed framework can be easily generalized onto featureless network data, will the performance superiority still be maintained? Note that in such cases, the feature input of GNNs can be generated following traditional ways.

(4) Can the proposed framework achieve generally good performance across different state-of-the-art GNN backbones? It would be better to adopt more backbones for experiments.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To leverage graph structure and mitigate structural bias in active learning, the authors present a unified optimization framework.

### Strengths
Originality: The investigation of structure fairness using active learning is something new.

Quality: The technical quality is below average. Many details are missing. For example, label position bias is a new term that was recently proposed, and the authors should elaborate more on it with a more intuitive explanation instead of just some formula. Also, at the beginning of Sec. 3.1, $t$ is a binary vector, and thus it should be $t \in \\{0,1\\}^n$. The relaxation in the paper does not make sense to the reviewer.

Clarity: In general, it is ok. The reviewer understands how the proposed method works but sometimes fails to see why.

Significance: The fairness and active learning problems for graphs are important.

### Weaknesses
1. The paper tries to solve the structure fairness problem using active learning. However, the connection between these two is weak, and the reviewer does not find any strong motivations to do so. The authors claim that "in active learning, strategically choosing labeling nodes, represented by t, can potentially reduce the LPS variance, promoting fairness in GNNs" in the second para. of Sec. 2.2, but the reviewer does not find any theoretical guarantees to motivate this finding. The core issue is that minimizing Label Proximity Score (LPS) variance does not directly translate to improved fairness, as fairness is typically concerned with equitable performance across different groups or attributes, not just the uniformity of proximity to labeled nodes. The paper lacks a clear explanation of how minimizing LPS variance ensures that nodes with lower LPS scores also achieve acceptable performance levels, rather than just having similar scores to those with high LPS. 

2. The goal of active learning is different from mitigating the bias in graphs and the ultimate goal of AL is to use as few as labeled nodes to achieve the best prediction performance. Therefore, the motivation of this work is totally unclear. The paper does not adequately explain why an active learning framework is the appropriate tool for addressing structural bias. Active learning focuses on selecting the most informative samples to label to improve overall model accuracy, while fairness is about ensuring equitable performance across different groups or nodes. The paper needs to clarify how selecting nodes to minimize LPS variance aligns with the goal of maximizing model performance using minimal labels, and why this approach is superior to other bias mitigation techniques.

3. The paper does not provide any theoretical proof to support the findings or the motivations. The relaxation used in the unified framework is also misleading. The relaxation of the binary vector $t$ to its convex hull is not well-justified, and the paper lacks a discussion on the implications of this relaxation. Specifically, the authors do not explain how the relaxed solution relates to the original discrete problem, and whether the relaxed solution can be effectively converted back to a valid solution in the original space. The paper also lacks theoretical analysis of the convergence properties of the proposed optimization framework and whether the proposed method is guaranteed to converge to a solution that minimizes the LPS variance.

### Questions
1. Why can we use the relaxation of the binary vector t to its convex hull?
2. How does the proposed method solve the fairness issue from the theoretical aspect? 
3. What is the formal definition of the structure bias in graphs, and how can we quantify it?
4. Why do we use active learning to solve the fairness issue in graphs? What if we do not have access to the oracle?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study focuses on enhancing the performance of GNNs for semi-supervised node classification, even when high-quality labeled samples are scarce. Traditional active learning methods may not work optimally in graph data, given their unique structures and the bias introduced by the positioning of labeled nodes. To address this, the researchers introduce a unified optimization framework called SCARCE, which can be combined with node features. Their experiments confirm that this method not only enhances GNN performance but also helps mitigate structural bias and improve fairness in the results.

### Strengths
1. Comparison with many baselines in this paper is very good.

### Weaknesses
1. The paper is not easy to follow. I suggest the existing work on fairness in GNN should be discussed. Otherwise, it is very hard to estimate the significance of this work.

2. My major concern is that the fairness definition in this paper is not very clear. We usually use demographic party (DP) or equal odds (EO) to measure fairness. However, this paper only uses the Standard Deviation (SD) and the Coefficient of Variation. Why do the authors consider them instead of DP and EO?

3. Figure 6 and Figure 7 are also not very clear to me. The authors discussed that 'SCARCE, which combines both SIS and LPS variance, SCARCE can not only elevate overall performance but also attain commendable fairness'. However, it is very hard to get this result from these two figures. I suggest the authors provide more details for examination.

4. This paper should focus on fairness instead of classification accuracy. However, Tables 1 and 2 provide more details about the classification accuracy. There should be a trade-off between accuracy and fairness. Only showing accuracy does not make any sense. In addition, how to balance the trade-off between accuracy and fairness in this paper. I do not find any implementation details related to this.

### Questions
See Weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
