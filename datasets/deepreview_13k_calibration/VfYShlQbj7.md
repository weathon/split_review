# Demystifying GNN Distillation by Replacing the GNN

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
It has recently emerged that Multilayer Perceptrons (MLPs) can achieve excellent performance on graph node classification, but only if they distill a previously-trained Graph Neural Network (GNN). This finding is confusing; if MLPs are expressive enough to perform node classification, what is the role of the GNNs? This paper aims to answer this question. Rather than suggesting a new technique, we aim to demystify GNN distillation methods. Through our analysis, we identify the key properties of GNNs that enable them to serve as effective regularizers, thereby overcoming limited training data. We validate our analysis by demonstrating an MLP training process that successfully leverages GNN-like properties without actually training a GNN.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors first investigate " Why are distillation methods so successful? ".

To determine whether GNNs ability comes from increased expressivity or a inductive bias, they analyze their performance against MLPs with varying training set sizes. The authors in their work show that GNNs primarily act as regularizers in distillation, rather than increasing model expressivity. Further, they show that GNNs benefit from unlabeled data through the message passing mechanism.

The paper proposes  method for node classification that replaces GNNs with regularization techniques: consistency loss and iterative pseudo-labeling. This approach leverages unlabeled data and captures structural information using label histograms.

The authors perform empirical evaluation on diverse datasets. They show their method performs empirically better than existing methods. Further, ablation is conducted for diff components to understand its importance.

Overall a good paper.

### Strengths
1. Interesting observation: The paper demystifies GNN distillation by highlighting their role as regularizers. 

2. The proposed approach of label histogram and pseudo labeling is easy/simple and effective

3. The authors do highlight limitations of their work. ( homophilic prior vs heterophily).

4. code is provided

5. Ablation studies are also provided.

### Weaknesses
1. Would recommend authors to add homophily ratio for each dataset so that one can understand how the results vary with diff homophily rates.

2. Why is only GraphSage taken as base GNN in Table3? Why GNNs like GAT are not considered?

3. What is the impact of gamma in eq.3? impact of weightage to itself and neighbor?
 
4. Does the degree of a node have some role to play? Since label histogram and consistency loss use neighborhood data. How is the performance on nodes of different degrees? Are there any studies? How much is the impact of degree/ availability of neighborhood data etc. on performance. Are there any studies on noisy neighbors?

### Questions
See weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the GNN-to-MLP distillation problem. This paper introduces a framework including three techniques: smoothing-regularization loss, label-histogram as a structural embedding, and iterative pseudo label smoothing. Considering the motivations, the proposed techniques are reasonable and effective. These techniques are based on the observations of the performance gap between GNNs and MLPs with varying label rates. The authors also claim that GNN distillation loss could be equivalent to smoothing regularization loss under certain conditions. The experiments are conducted on several datasets and the results show that the proposed techniques are effective. The ablation study also shows the effectiveness of each technique.

### Strengths
1. The insight that distillation loss could be equivalent to smoothing regularization loss is interesting.

2. The writing is clear and straightforward. One can easily follow the paper.

3. Label histogram as a structural embedding seems much more effective and reasonable than the deepwalk embedding used in NOSMOG.

4. Notable improvements in performance are observed with the proposed techniques in some datasets.

### Weaknesses
1. (Soundness) Several claims are not well supported or not appropriate. For example, in lines 132-133, the authors claim that "MLPs overfit" with observations that MLPs perform poorly in few-labels setting. As far as I know, overfitting describes the performance gap between training and test sets, which is not the case here. The authors could provide the train-test performance gaps of GNNs and MLPs to support this claim. Another example is the claim in lines 139-140 that "distillation overcomes it by increasing the size of the training set with GNN pseudo-labels." This claim is not well supported, since for distillation, not only more pseudo-labels are introduced, but also the information inside these pseudo-labels is distinctive to what MLP itself could provide. The result of an additional ablative experiment in which GNN pseudo-labels are replaced with MLP's own pseudo-labels (in a self-training way) may help to validate this claim in a more convincing way.

2. (Novelty) Regularizing the MLP using graph structure is not a new idea. Some related works [1,2] are missing in this topic. Furthermore, the smoothing-regularization loss seems equivalent to the contrastive loss of [4] under the homophily assumption. The authors should make a distinction between these works and their work. Specifically, while both the proposed method and [4] encourage similar representations for connected nodes, the contrastive loss in [4] also explicitly pushes apart representations of non-connected nodes. It is unclear if the proposed method is simply a reduced version of [4] that only considers positive pairs.

3. (Novelty) The iterative pseudo-labeling is also a common practice [5] in topics of GNN few-labels learning. Furthermore, this technique lacks sufficient intuition since the topic of this paper is distillation, not few-labels learning. The authors should provide more insights on why this technique is effective in distillation, especially in a normal setting where labels are sufficient. The claim that "GNN distillation is mostly needed in cases where labels are scarce" is not well-supported, as the connection between GNN distillation and few-label learning is not clear. Moreover, an ablation study replacing GNN pseudo-labels with MLP's own pseudo-labels in a self-training manner is still missing.

4. (Experiment) As far as I know, the main focused benchmark in GNN-to-MLP distillation is the inductive setting. However, the authors put this important inductive setting in the appendix while the main experiments are conducted in the transductive setting. Furthermore, the proposed method is even surpassed by the weak baseline GLNN in some datasets in this setting, which makes it hard to believe the effectiveness of the proposed techniques. In the inductive setting, the proposed method is also surpassed by NOSMOG in many datasets, further questioning the effectiveness of the proposed techniques.

5. (Experiment) Only GraphSAGE is used as the GNN model. The authors should provide more GNN teachers such as GCN, GAT, APPNP, etc. to make the results more convincing. It is important to evaluate the proposed method with various GNN teachers, not just as baseline models.

6. (Contribution) Most of the insights and techniques heavily rely on the assumption of homophily, which limits the contribution of the paper. The authors should provide evidence to support the claim that "neither the GNN distillation methods nor the direct regularization technique yield strong performance in scenarios characterized by heterophily". Even if this claim is true, the design of the proposed methods which explicitly depends on homophily is not a good design, since it could not extend to general graphs.

### Questions
Most of the questions and suggestions are already mentioned in the weaknesses section. I would like to mention some minor points here.

1. The authors should use "GCN" explicitly instead of "GNN" in their claims, since they only use GCN architecture in the analysis and don't extend their analysis to general GNN models.

2. How does this method compute the label histogram of unobserved test nodes in the inductive setting? Will it access the graph during inference?

3. Inference time of this method should be discussed in the paper. Comparison of training costs would also be helpful.

4. I think Label histogram as a structural embedding is more important than the other two techniques, while little theoretical or empirical insight of it is discussed in the paper. More intuitions and studies on this technique would be helpful.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper discusses the distillation process from GNN to MLP. Rather than suggesting a new technique, the authors aim to demystify GNN distillation methods. They propose two hypotheses:(1) GNNs serve as consistency regularizers, and (2) GNNs leverage unlabeled data effectively. Their experimentals indicate that the distillation process of GNN2MLP can be replaced by other manually designed methods (without the need for GNN)

### Strengths
1. To understanding the process of GNN2MLP is quite important. The previous methods empirically confirmed the distillation process is  effective, but this work for the first time summarizes them into a unified hypothesis and verifies it through experiments.

2. The MLP trained by the author achieved performance comparable to GNN on different dataset sizes

### Weaknesses
1. All hypotheses have been experimentally proven, not theoretically. And the author only reported accuracy and lacked further analysis of the experimental results

2. During the iteration process, it seems that the nodes with pseudo-labels are constantly being replaced into the training set, and these nodes appear to come from outside the training set, which may lead to unfairness in the evaluation.

### Questions
1. During the iteration process, where does the node  with pseudo-labels come from? Will they be used for testing?


2. In Section 4.3.1, is the consistency loss highly correlated with the datasets? Using such a loss on the high homophily dataset used in the experiment seems to easily improve performance. Can you compare [homophily prediction encouraged by GNN during distillation] with [ homophily prediction encouraged by your suggested loss during MLP training]?


3. Can there be more analysis in the experiment, for example, on which specific nodes did your proposed method perform well? Is the performance improvement node brought by your method consistent with the performance improvement node brought by the GNN2MLP distillation process?

4. Line 343, "As our goal is to understand GNN distillation, we want to optimize the MLP model such that during inference we do not utilize neighboring nodes. Thus, we apply prediction smoothing only to the pseudo-labels within the iterative training algorithm." What is the causal relationship here?

Overall, I think the perspective of this paper is reasonable and interesting. But the manuscript is worth further revisions, and if the author can address my concerns, I am willing to increase my score.  :  )

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on demystifying the role of Graph Neural Networks (GNNs) in graph distillation methods for graph node classification. It is found that GNNs primarily function as regularizers during distillation. Through theoretical and empirical investigations, the authors replace GNN distillation with explicit regularization strategies and propose label histogram as an alternative to positional embedding. The paper also validates its claims through comprehensive experiments on multiple datasets and comparisons with existing state-of-the-art methods.

### Strengths
1. The research perspective of the paper is interesting. It demonstrates that GNNs in distillation methods act as regularizers, which is supported by experiments comparing GNN distillation with an alternative approach of training MLPs with direct regularization.
2. The replacement of implicit GNN regularization with explicit terms can achieve comparable results to GNN distillation without training GNNs.
3. The writing is clear and good. The descriptions and explanations of individual methods are easy to follow.

### Weaknesses
1. The analysis is mainly focused on homophily graphs, and the performance on heterophily graphs is not well explored. A proper addition to this part of the results would strengthen my confidence on this paper. Another important issue is that I feel that “neighborhood smoothing” is an overly strong assumption, which makes the proposed method less applicable. Specifically, the reliance on strong homophily might limit the method's effectiveness in real-world scenarios where graphs often exhibit more complex mixing patterns. The paper should include a more thorough discussion of the limitations imposed by this assumption.

2. Proposition 1 and its proof seem to be based only on a linear setting. However, the actual MLP contains nonlinear activation, and I'm curious if the GNN distillation loss and consistency loss are still equivalent? The theoretical analysis needs to be extended to account for the non-linearities introduced by activation functions. The current analysis, based on a linearized network, may not fully capture the behavior of the proposed method in practice. A more rigorous treatment of the non-linear case is needed to strengthen the theoretical foundation of the work.

3. I have noticed that the datasets used in this paper are actually small, and it is very necessary to validate the effectiveness of the method on larger-scale ogb-arxiv and ogb-products datasets. The current evaluation is limited by the scale of the datasets used. The paper should include experiments on larger, more challenging datasets to demonstrate the scalability and robustness of the proposed approach. This is crucial for assessing the practical applicability of the method.

4. Lack of comparison with important baselines mentioned in related work, e.g. VQGraph and FF-G2M, etc. The paper should provide a more comprehensive comparison with existing state-of-the-art methods, especially those mentioned in the related work. This would help to better contextualize the contribution of the proposed method and highlight its advantages and disadvantages compared to other approaches.

5. The technical contribution of the article as a whole is limited, because the three proposed methods (1) label consistency; (2) iterative pseudo-labeling; and (3) label histograms share similar ideas with many past works. Combining them is indeed effective but an incremental contribution. The novelty of the proposed method is questionable, as it largely combines existing techniques. The paper should clearly articulate the novel aspects of the proposed approach and justify its contribution beyond simply combining existing methods.

### Questions
Please address my concerns about weakness.

### Soundness
2

### Presentation
3

### Contribution
2
