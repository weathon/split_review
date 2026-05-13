# Bag of Features: New Baselines for GNNs for Link Prediction

- Decision: Reject
- Scores: 3, 3, 5, 8

## Abstract
Graph Neural Networks (GNNs) have brought a significant transformation in the realm of graph representation learning. They achieve this by employing a neighborhood aggregation approach, wherein a node's representation vector is iteratively calculated by aggregating and modifying the corresponding vectors of its neighboring nodes. Despite GNNs demonstrating superior performance in various domains over the last ten years, recent theoretical studies have raised concerns about their expressive capabilities, where they show that GNN models yield results comparable to the well-established Weisfeiler-Lehman algorithm.

In this paper, driven by this motivation, we compare the performance of current GNN models with conventional feature extraction methods in the context of link prediction. Our experiments reveal that when applied to standard feature sets derived from node neighborhoods and node features, standard machine learning (ML) models deliver highly competitive results, even when pitted against cutting-edge GNN models. This holds true across both small and large benchmark datasets, including those from the Open Graph Benchmark (OGB). Our empirical findings corroborate the previously mentioned theoretical observations and imply that there exists ample room for enhancement in current GNN models to reach their potential.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes bags of heuristics for link prediction. The experiments show the effectiveness of the proposed method.

### Strengths
This paper shows that the conventional features of the graph can be utilized to outperform GNN in link prediction.

### Weaknesses
1. The conclusion that graph heuristics can outperform GNN in link prediction is not a new contribution. This article only proposes some heuristics but does not explain why they are effective.
2. This paper overclaims its contribution. The method and experiments of this paper are designed for link prediction, but the contribution of this paper lies in discussing that GNN is not good at graph learning. As far as I know, heuristics perform better than GNN only in link prediction, and there seems to be no similar phenomenon in other domains such as graph classification, node classification, and graph regression.
3. The experimental part of this article does not compare with state-of-the-art GNN methods, such as NBFNet[1] and Seal[2].

### Questions
see weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper leverages different graph structural features with node attributes for link prediction tasks. Then, an XGBoost method is utilized based on these features for link prediction.

### Strengths
1. The authors explore different graph structural features for link prediction.
2. The paper is well-written and easy to follow.

### Weaknesses
1. The paper's novelty appears constrained. The significance of graph structural features in the realm of link prediction has been previously underscored by several studies, such as [1][2][3]. The specific combination of features used, while potentially effective, does not present a fundamentally new approach in the context of existing literature.
2. The evaluation omits several critical baselines that similarly exploit graph structural features. Notably absent are BUDDY, Neo-GNN, NCN, NCNC, and NBFNet. These methods represent the current state-of-the-art in leveraging structural information for link prediction, and their absence makes it difficult to assess the relative performance of the proposed method.
3. The experimental setup seems to miss out on key datasets such as ogbl-ddi, ogbl-ppa, and ogbl-citation2. These datasets are widely used in the link prediction community and provide a more comprehensive evaluation of the proposed method's generalizability.
4. There are no ablation studies about the importance of each feature. This makes it difficult to understand which features are most important for the performance of the proposed method and whether some features are redundant or even detrimental.
5. While the method demonstrates commendable efficacy on the OGBL-Collab dataset, it's concerning that the associated code is inaccessible, given the empty repository link. This hinders reproducibility and makes it difficult for other researchers to build upon this work.
6. Using the original feature to measure the node similarity might be unreasonable. The original node features may not always be the most relevant for capturing node similarity in the context of link prediction, especially when the graph structure itself contains rich relational information.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work unifies conventional feature extraction methods for link prediction and uses standard machine learning models to learn from them. The result model delivers highly competitive results on various datasets.

### Strengths
1. Clear method.

2. Solid experiments.

### Weaknesses
1. Novelty is limited. Most methods are ordinary feature extraction tricks.

2. Experiments are not conducted on OGB datasets other than collab.

### Questions
1. Please add experiments on other OGB datasets.

2. This work used XGBoost as the ML model. Did you conduct ablation study for it? For example, use Logistic regression and SVM instead?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the performance of Graph Neural Networks (GNNs) for link prediction tasks in comparison to traditional feature extraction methods. The authors propose a simple machine learning model called "Bag of Features," which combines structural features based on node proximity in the graph structure and domain features based on feature space similarity. Their findings show that this model delivers highly competitive results when compared to state-of-the-art GNN models across various benchmark datasets. This supports recent theoretical observations that current GNNs may not be fully exploiting their potential, suggesting a need for innovative approaches to unlock the full capabilities of GNNs.

### Strengths
1. The proposed Bag of Features (BFLP) model is elegant, simple, and effective, combining both structural features and domain features to create a powerful machine learning model for link prediction tasks.

2. The model demonstrates consistently competitive results when compared to state-of-the-art GNN models, providing empirical evidence that there is room for improvement in current GNN approaches.

3. The paper highlights the potential for conventional feature extraction methods to be integrated into future ML models to enhance their performance.

4. The work is likely to inspire future research in the link prediction domain, encouraging researchers to explore alternative methods and improve upon existing GNN techniques.

Overall, I enjoyed reading the paper and it is a significant contribution to the application of link prediction.

### Weaknesses
Several improvements can be made to enhance the quality of the work. Addressing these comments may lead to a higher score:
1. Rectify the discrepancies between baseline performances in Table 5 and those on the OGB website (refer to Comment 1 for details).

2. Broaden the evaluation datasets to encompass a variety of network structures and domains (see Comments 2 and 3 for clarification).

3. Perform ablation studies to gain a deeper understanding of the contributions made by the Bag of Features model components (refer to Comment 4 for more information).

### Questions
1. A discrepancy exists between the performance reported in Table 5 and the OGB website. For instance, GraphSAGE shows a 48.10 on the OGB website, but the paper reports 56.88. The performance in Table 5 closely aligns with the validation performance on the OGB website. The authors should verify if Table 5 reflects the validation dataset performance and determine the cause of this inconsistency.

2. Tables 3 and 4 follow the methods of (Zhao et al., 2022) and (Guo et al., 2022), respectively. To enhance comprehensiveness, the authors should consider adding Facebook and OGB-DDI to Table 3, and Cora, Citeseer, and DBLP to Table 4.

3. The paper focuses on homophilous graph datasets, but the proposed method could also be applied to heterophyllous graph datasets. Including these datasets would increase the paper's impact.

4. The ablation studies only examine the removal of all structural or domain features. A more detailed table illustrating the impact of each individual feature on the datasets would make the results more appealing.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
