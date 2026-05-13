# How Does Message Passing Improve Collaborative Filtering?

- Decision: Reject
- Scores: 8, 3, 3, 5

## Abstract
Collaborative filtering (CF) has exhibited prominent results for recommender systems and been broadly utilized for real-world applications.
A branch of research enhances CF methods by message passing (MP) used in graph neural networks, due to its strong capabilities of extracting knowledge from graph-structured data, like user-item bipartite graphs that naturally exist in CF.
They assume that MP helps CF methods in a manner akin to its benefits for graph-based learning tasks in general (e.g., node classification). 
However, even though MP empirically improves CF, whether or not this assumption is correct still needs verification.
To address this gap, we formally investigate why MP helps CF from multiple perspectives and show that many assumptions made by previous works are not entirely accurate. 
With our curated ablation studies and theoretical analyses, we discover that \textit{\textbf{(i)} MP improves the CF performance primarily by additional representations passed from neighbors during the forward pass instead of additional gradient updates to neighbor representations during the model back-propagation and \textbf{(ii)} MP usually helps low-degree nodes more than high-degree nodes.}
Utilizing these novel findings, we present \fullname, namely \textbf{\method}, a test-time augmentation framework that only conducts MP once at inference time. 
The key novelty of \method is that it effectively utilizes graph knowledge while circumventing most of notorious computational overheads of MP. 
Besides, \method is extremely versatile can be used as a plug-and-play module to enhance representations trained by different CF supervision signals.
Evaluated on six datasets (i.e., five academic benchmarks and one real-world industrial dataset), \method consistently improves the recommendation performance of CF methods without graph by up to \textbf{39.2\%} on cold users and \textbf{31.7}\% on all users, with little to no extra computational overheads.
Furthermore, compared with trending graph-enhanced CF methods, \method delivers comparable or even better performance \textit{\underline{with less than \textbf{1\%} of their total training times}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the (positive) role of message passing in graph collaborative filtering. The analysis is initially driven by the assumption that, even though message passing in graph collaborative filtering is applied exactly as it appears in other graph learning tasks, evidence (in terms of recommendation performance) demonstrates that message passing in graph collaborative filtering may be working in a different manner. On one side, through a simple reformulation of the message passing (in the case of LightGCN) the authors show that it inherently comes with the usual user-item similarity score (as in MF) plus additional inductive biases accounting for other more refined interactions between users and/or items. This suggests that the message passing could improve MF-like approaches in two ways, namely: 1) neighborhood aggregation and 2) the additional gradient updates. An empirical analysis demonstrates that it is the neighborhood aggregation to provide the highest contribution to the improved performance. On another side, the authors empirically and mathematically prove that, differently from what happens in graph learning, high degree nodes seem to benefit from message passing more than low degree ones. In the light of above, the authors propose TAG-CF, short for Test-time Aggregation for Collaborative Filtering, a simple but effective model agnostic solution which performs message passing on top of any MF-like recommender system only at inference time. Extensive experimental analyses confirm the efficacy of the proposed approach over several baselines and on popular recommendation datasets. The evaluation is complemented through ablation studies and a computational time assessment.

### Strengths
+ The paper proposes a pivotal question to assess the actual role of message passing in collaborative filtering.
+ The empirical and theoretical preliminary analyses are sound and help supporting the proposal of the TAG-CF solution.
+ The proposed approach is simple and effective from a theoretical and experimental point of view.
+ The experimental setting is extensive.
+ The code is released at review time.

### Weaknesses
 - Some important related work and baselines may be missing. For instance, GFCF [1] is another work questioning the role of graph convolutional network in recommendation; UltraGCN [2] and SVD-GCN [3] discuss the role of additional neighborhood aggregation types (e.g., user-user and item-item) in collaborative filtering.
- Some clarification needs to be provided regarding the low degree aspect (i.e., section 3.2). Specifically, the paper observes that high-degree nodes benefit more from message passing, but this could be an artifact of the collaborative filtering paradigm itself, which tends to favor active users. It's not clear if this is a unique characteristic of graph-based methods or a general trend in recommendation datasets. The analysis should clarify whether the observed performance differences are due to the message passing mechanism or inherent biases in the data and evaluation process.


### Questions
* Did the authors consider testing the proposed approach against UltraGCN? Indeed, UltraGCN is described as extremely simplified version of LightGCN also in terms of computational time. What is more, it almost removes the message passing from the training phase and proposes an approximation of infinite propagation layers through additional loss components. 
* Reading the discussion about low and high degree nodes in section 3.2, it seems that the observed behaviour (i.e., good performance on high degree nodes) could be ascribed to the fact that, in general, all recommendation approaches built on the collaborative filtering paradigm tend to provide higher-quality recommendations for active users at the detriment of less active ones (i.e., warm/cold users respectively). Thus, maybe this trend is only linked to the specific characteristics of each recommendation dataset, and it is not unique for graph-based recommender systems. Could the authors elaborate on this aspect?

**After the rebuttal.** The rebuttal answered all questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors initially conduct experiments to illustrate that the message-passing process contributes more significant benefits to collaborative filtering than those derived from gradient updates. Subsequently, they discover that the message-passing mechanism offers more substantial advantages for nodes with fewer connections. Ultimately, the paper suggests that TAG-CF does not implement message-passing during the training phase. Instead, it exclusively applies this technique during the inference process.

### Strengths
1.	The paper attempts to explain the role of message passing in collaborative filtering, which is a promising avenue of investigation.
2.	The article is easy to read, and the tables and illustrations are quite clear and comprehensible.

### Weaknesses
Weaknesses:

1. The conclusions drawn from the experiments on LightGCN are well-known and lack a deeper theoretical foundation.

In Section 3.1 of the paper, the conclusions drawn are not groundbreaking; instead, they represent widely accepted knowledge, lacking innovation. Moreover, the article fails to provide theoretical underpinnings for the hypotheses and conclusions presented, making it challenging to extend these findings to collaborative filtering algorithms beyond LightGCN. The research solely relies on the LightGCN model in experiments conducted on three datasets with relatively high sparsity, which may introduce bias. The experimental results indicate two key points: 1. Message passing and gradient updates have practical significance for collaborative filtering recommendation systems, and 2. Message passing primarily contributes to performance improvements in collaborative filtering. It's worth noting that since the article exclusively investigates the LightGCN model, the conclusion predominantly emphasizes the role of message passing in enhancing LightGCN's performance. While this conclusion holds for LightGCN, it may not necessarily apply to other models, warranting further exploration.

Indeed, further theoretical exploration may be necessary.

2. The setup of the exploratory experiments is problematic, and this experimental design lacks fairness and equity.

Furthermore, in the exploratory experiments of Section 3.1, the experimental design lacks the necessary rigor to effectively validate the author's hypotheses. In the case of (LightGCNw/o neigh. info), a message passing mechanism is employed during training but not during inference. During training, embedding representations are improved through message passing to obtain new user and item embeddings, which are then used to compute BPR loss. The optimization objective of message passing is to enhance the similarity and dissimilarity between embedding features after message passing. However, in the inference phase, the experiments omit message passing and use the original features as embeddings for users and items. This results in inconsistent optimization objectives between training and inference, with inference embeddings notably lacking in similarity and collaborative signals. Consequently, the (LightGCNw/o neigh. info) model's performance unavoidably becomes suboptimal. These experimental results, therefore, cannot effectively prove that message passing is the most critical factor.

3. Applying TAG-CF solely to MF and ENMF is insufficient to demonstrate the effectiveness of TAG-CF, and in some experiments, the results show non-statistically significant improvements.

The proposed TAG-CF essentially involves deactivating message passing during model training and enabling it during inference. In the primary experiment, only ENMF and MF had an additional message passing step during inference to validate its effectiveness. However, these experiments are considered insufficiently comprehensive. It might be necessary to apply TAG-CF to a broader range of classic Graph-based recommendation models to thoroughly confirm its effectiveness. Limiting the application to the simplest ENMF and MF models alone may not be sufficient to fully demonstrate the effectiveness of TAG-CF. The comparative models solely comprise classic NGCF and LightGCN; thus, it might be necessary to include more recent models in the experiments. Additionally, on some datasets, the improvement is less than 2%, which is not statistically significant.

4. The choice of datasets in this study is limited to a single type.

Additionally, the choice of datasets in this study is confined to a single type. The paper's model primarily focuses on node degrees, but the datasets used in the experiments all have relatively high sparsity. It would be beneficial to include datasets with lower sparsity, such as Movielens-1M, to ensure a more comprehensive evaluation of the model's performance.

5. Despite the computational complexity, the improvements achieved with TAG-CF+ are not significantly greater than those of TAG-CF.

TAG-CF+ involves exclusively passing messages to nodes with lower degrees. However, the computation of node degrees, selection of low-degree nodes, and the search for neighbors of low-degree nodes represent computationally complex tasks.

### Questions
1. In the experiments in Section 3.2, how many layers of LightGCN are used?
2. Regarding sensitivity to node degrees, are there experiments being conducted on datasets with even higher sparsity levels, which are commonly known to have higher degrees of sparsity?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article analyzes and empirically verifies that message passing improves collaborative filtering mainly by: (1) information passed from neighbors instead of additional gradients; (2) more benefits for low-degree nodes than high-degree nodes. Inspired by these findings, the authors propose a test-time augmentation framework that only use message passing once at inference time, named Test-time Aggregation for Collaborative Filtering (TAG-CF). And extensive experiments are conducted on five open datasets to demonstrate the effectiveness and efficiency of TAG-CF and verify the previous findings again.

### Strengths
1. The experiments are sufficient in the elaboration of the proposed two findings. The authors provide ablation studies on different parts of the message passing used for collaborative filtering. From the perspective of improvement gains of subgroups, the conclusions are opposite to those in other graph tasks except CF. 
2. From multiple perspectives, the authors demonstrate the usability of the framework TAG-CF on CF models. Experiments are done on five datasets, especially including one large-scale dataset. And as a plug-and-play module, TAG-CF is putted in two MF methods trained by two supervision signals. Experiments are also carried out to compare time efficiency with other models.

### Weaknesses
1. The analysis of experiments and theories is inadequate in section 3. For example: (1) the comparison of LightGCN_(w/o both) with other variants is missing; (2) the logic of the analysis of how supervision signals can lead to limited improvement on high-degree users doesn’t make sense. The theoretical analysis that “these two supervision signals could inadvertently conduct message passing in the backward step” can’t adequately explain why the improvement on high-degree users could be limited more than low-degree users.

2. The experimental results of the proposed framework are not significant and the scope of application is narrow. (1) Although the proposed TAG-CF can improve the CF methods by using messaging in the test phase, it does not work well compared to GNN-based models, such as the mentioned SGL and LightGCL. (2) And from the design philosophy of using message passing only for testing, this framework can only be used on non-GNN-based models. However, as there are many works that modify the message passing for CF with great performance rather than being limited to LightGCN, it is difficult to bridge the gap in the benefits of training with it. (3) In terms of time efficiency, there is no significant advantage over the relatively light GNN-based models recently. You can find some more recent models to compare the efficiency to show the benefits in this regard.

3. The arrangement of Table 2 is not very reasonable. The comparison of results on low-degree users and overall performance is poorly readable. Results in these two sub-tables can be compared longitudinally in a single table.

### Questions
As the object you're analyzing is message passing for CF, are there any similar ablation analyses done for other Graph-based CF methods except LightGCN?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Collaborative filtering (CF) is a widely used technique in recommender systems, and some researchers have tried to improve it using message passing in graph neural networks. However, the reasons for the improvement remain unclear. This study investigates the effects of message passing on CF from various perspectives and finds that it primarily improves CF performance through information passed from neighbors and typically benefits low-degree nodes more than high-degree ones. Based on these findings, the authors propose a test-time augmentation framework called TAG-CF, which performs message passing only once at inference time and can be used as a plug-and-play module. Tested on five datasets, TAG-CF achieves similar or better results than existing graph-based CF methods with significantly less training time. The study also shows that test-time aggregation in TAG-CF improves recommendation performance similarly to training-time aggregation, validating the findings on why message passing improves CF.

### Strengths
1. The ablation study of neighbor information and gradients is reasonable and novel.
2. The experiments are very detailed for reproducing; the authors provided code and configures of the experiments of information passed from neighbors, additional gradients for neighbors, and individual improvement gains of subgroups.

### Weaknesses
1. The analysis of chapter 3.2 is not rigorous; it doesn't safe to conclude that message passing in CF helps low-degree users More. The authors used BPR and DirectAU to denote CF methods whereas both losses belong to pair-wise learning. Generally CF also includes pointwise and listing learning, which are not discussed in the paper.
2. I agree that the Theorem 1 can reveal that for embed-based CF methods with pairwise losses: "the room for improvement on high-degree users could be limited, since part of these improvements might already have been claimed by the supervision signal itself". However, it does not mean that low-degree users will benefit more from message passing. Actually it the same conclusion for low-degree users. The difference of experimental evidences may be due to underfitting of low-degree users.
3. The authors claimed "TAG-CF cannot update any parameters since it is applied at test time, and hence requires tune-able normalization hyper-parameters". This disadvantage makes the method unstable and hard to jduge.

### Questions
1. Please address the concerns listed in the weakness. 
2. I suggest doing up-sampling for low-degree users' data and retraining a MF or ENMF model. I conjecture this will achieve competitive result against TAG-CF variants.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
