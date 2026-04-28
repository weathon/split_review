# SEESAW: Do Graph Neural Networks Improve Node Representation Learning for All?

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Graph Neural Networks (GNNs) have manifested significant proficiency in various graph learning tasks over recent years. Owing to their exemplary performance, GNNs have garnered increasing attention from both the research community and industrial practitioners. Consequently, there has been a notable transition away from the conventional and prevalent shallow graph embedding methods. However, in tandem with this transition, an imperative question arises: do GNNs always outperform shallow embedding methods in node representation learning? Despite the doubts cast by multiple recent studies, the field of graph machine learning still lacks a systematic understanding, which is essential for meticulously paving its advancement. To properly answer this question, in this work, we propose a principled framework that unifies the pipelines of representative shallow graph embedding methods and GNNs. With rigorous comparative analysis, we first characterize the primary differences in their design from two different perspectives: the prior of node representation learning, and the neighborhood aggregation mechanism. We then analyze the benefits and drawbacks of using GNNs instead of shallow embedding methods through comprehensive experiments on ten real-world graph datasets. Furthermore, we also empirically validate that our analysis can be generalized to GNNs under various learning paradigms. Armed with these insights, we propose a guide for practitioners in choosing appropriate graph representation learning models under different scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work aims to compare the performance of GNNs and shallow embedding methods and delves into scenarios where GNNs may not always outperform shallow embedding methods. The authors present a systematic framework, SEESAW, to compare these two approaches. They identify key differences in learning priors and neighborhood aggregation and analyze when GNNs exhibit drawbacks. The study finds that GNNs may struggle in (1) attribute-poor scenarios, leading to dimensional collapse, and can adversely affect the performance of specific node subgroups in certain cases; (2) highly heterophilic networks, as the neighborhood aggregation may jeopardize the performance of heterophilic nodes. Thus, this paper suggests that practitioners should consider shallow embedding methods in attribute-poor scenarios and networks with heterophilic nodes.

### Strengths
1. This paper is well-structured and easy to follow.
2. The topic of comparing shallow embedding methods and GNN methods for graph representation learning is meaningful.
3. The experimental setting is clear, and code is provided.

### Weaknesses
1. Novelty is not good. The findings that GNNs face some challenges when we do not have enough attribute information (e.g.[1][2]) and when we have heterophilic data (e.g.[3]) are already identified by other works.

2. Only empirical results are provided, there is no theoretical analysis or deep explanation regarding the empirical results, which makes this work less solid. 

3. For the experiments, only Deepwalk is compared among all the shallow methods, and only homophilic datasets are used while some heterophilic datasets are missing (e.g. datasets in [3]).

### Questions
Q1. In difference 1, I personally feel GNN is very flexible to the learning prior. Though one of the most frequently used learning prior would be the transformed node attributes, but it can also take uniform initialization (i.e. treat the input graph as an unattributed graph, then assign uniform initial features on each node). So, it seems to me that, it is unfair to claim GNN is limited to taking the transformed node attributes as prior？

Q2. Only DeepWalk is examined among all the shallow methods. Is it representative enough? Can it outperform all other shallow methods on all datasets? If yes, then why?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper compares classic graph embedding methods (e.g., DeepWalk) and GNNs. For this, the authors first unify the setups: namely, GNN optimizes the same random walk objective. The paper argues that there are two main differences between GNNs and classic approaches: different prior representations and different updating operations (whether there is aggregation over the neighbors).
 
In the experiments the following observations are made:
- On one out of ten datasets DeepWalk outperforms GNNs;
- The performance of GNNs drops when features are removed;
- For GNNs, the dimensionality of learned representations decreases when features are removed;
- The performance of GNNs and shallow models is better for high-homophily nodes. For low-homophily nodes removing neighborhood aggregation improves the performance.
 
Based on the conducted experiments, suggestions for when it is better to use which model are given.

### Strengths
1. The paper addresses an important topic.

2. Extensive experiments are conducted to analyze and compare the performance of GNNs and classic methods.

3. The paper is in general clearly written and easy to follow.

### Weaknesses
1. The novelty of the work seems limited - most of the observations are straightforward or appeared in previous research.

2. While the paper contains a guide for practitioners about which model to choose, it is not specific to be directly applied to a given application. For instance, in Section 5, it is written "we recommend adopting GNNs and shallow embedding methods on attribute-rich and attribute-poor networks, respeectively." However, it is not clear how to decide whether the attributes are rich. For instance, in both Flickr and PubMed, there are 500 features, but the results on them are completely different. So, it is not the number of features that can be used for this decision.

### Questions
Q1. How to decide whether the features are sufficiently rich?

Q2. It is written that "It is difficult for shallow embedding methods to properly exploit information encoded in node attributes and make use of the homophily nature of most graphs" - why the latter is true? Classic methods have similar embeddings for nodes located close to each other in the graph. Under the homophily assumption, such nodes often have the same label.

Q3. The fact that GNNs strongly rely on node features and removing them leads to decreased performance is very natural. Can this problem be solved by augmenting node features with structural graph-based features? Or maybe even with random features? Both options can also increase the representation effective dimension.

Q4. Can small representation effective dimension be explained just by the dimension of the initial feature set? This would also explain Figure 5(b) since increased rank bound cannot solve this issue.

Q5. The concatenation experiment is conducted only on one dataset (DBLPFull). Are the results on other datasets consistent with this?

Q6. Do I understand correctly that GNN w/o Agg (Figure 6) does not use any graph structure?

There are some typos throughout the text:
- Page 2: "the most graph popular representation"
- Page 2: footnote is placed before the punctuation mark
- Page 3: (line 2, line 3): "output" -> "outputs"
- Page 3: "There have been various of GNNs"
- Section 4.2: "We hypothesis that"
- Section 4.2: "methods preserves"
- Section 4.2, page 6: in the definition of matrices Z, C, F, the matrix Z repeats twice (same typo in appendix, page 17)
- Page 9: "respeectively"
- Page 20: "the available node attributes becomes"

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper scrutinizes drawbacks of GNNs compared to shallow embedding approaches. Specifically, the authors observe that GNNs suffer dimensional collapse and exhibit poor performance when input features are limited. Furthermore, in heterophilic graphs, GNNs with aggregation also show inferior performance compared to GNNs without aggregation and shallow embedding methods. Considering these observations, they suggest to use GNNs when input attributes are rich, graphs are homophilic, transductive or large.

### Strengths
* The paper is well-written.
* The authors validate their hypothesis on various datasets.

### Weaknesses
 * It is already shown that MLPs (which is same with GNNs without aggregation) outperforms commonly used GNNs such as GCN, GAT, and SAGE. Furthermore, several methods are proposed to perform well on both homophilous and heterophilous graphs [1, 2, 3].
* It seems that the circumstances where input features are limited is not common in the real-world senarios and we can augment input features with large language models even in attribute-poor settings [4].
* It is not surprising that GNNs suffer dimensional collapses when input features are poor since it is well-known for general neural netoworks. 

### Questions
* There are several models combining walking-based approaches and GNNs such as APPNP [1]. I think that this kind of mechanism might alleviate the problem of GNNs due to the adoption of pagerank. Does APPNP also suffer similar problems as other GNNs?
* Several approaches such as LINKX [2] encode node topology and node attribute separately and combine two representations later. Since these approaches can learn how much to reflect node attributes on node representations, I think that these methods might not suffer dimensional collapse. Does LINKX also suffer similar problems?

[1] Gasteiger, Johannes, Aleksandar Bojchevski, and Stephan Günnemann. "Predict then propagate: Graph neural networks meet personalized pagerank." arXiv preprint arXiv:1810.05997 (2018).

[2] Lim, Derek, et al. "Large scale learning on non-homophilous graphs: New benchmarks and strong simple methods." Advances in Neural Information Processing Systems 34 (2021): 20887-20902.

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes a framework that unifies shallow graph embedding methods and Graph Neural Networks (GNNs) for node representation learning. The authors conduct a comparative analysis of the primary differences in design between the two approaches from the perspectives of node representation learning and neighborhood aggregation mechanism. Through comprehensive experiments on ten real-world graph datasets, the authors provide insights into the benefits and drawbacks of using GNNs and propose a guide for practitioners in choosing appropriate graph representation learning models under different scenarios. The paper aims to provide a broader perspective on graph learning and to recalibrate the academic perspective on the effectiveness of GNNs compared to conventional shallow embedding methods.

### Strengths
1. The author meticulously elaborated step by step on the relationship between prediction performance drop of GNNs and attribute dimension, as well as dimension collapse in hidden space,  which is sound.
2. The paper helps clarify the respective strengths and weaknesses of GNN and shallow embedding methods, making it a valuable reference for practitioners.

### Weaknesses
1. This article lacks novelty to some extent, despite providing detailed analysis and experiments. The conclusions are relatively trivial and are already a consensus in the community.
2. The paper may be improved if it discusses some works that combine the advantage of network embedding and GNN, like [1,2].

### Questions
(1) The result of E2E-GCN on GCN, CiteSeer, Pubmed is lower than that reported in the paper. Can the authors explain the difference of experimal setting?    
(2) Since the GNNs usually contain non-linear activation functions, is it reasonable to measure the Dimensional Collapse by evaluating rank of the embedding matrix?     
(3) Is it possible to overcome the weakness of both GNNs and shallow embedding methods, and propose a new graph representation paradigm to combine their strengths?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
