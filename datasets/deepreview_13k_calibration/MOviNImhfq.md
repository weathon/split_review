# Effective Graph Representation Learning via Smoothed Contrastive Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 8, 3

## Abstract
Graph contrastive learning (GCL) aligns node representations through the utilization of positive/negative node pairs, a selection process that typically relies on the correspondences and non-correspondences among nodes within two augmented graphs. The conventional GCL approaches incorporate negative samples uniformly in the contrastive loss, resulting in the equal treatment of misclassified false negative nodes, regardless of their proximity to the true positive. In this paper, we present a Smoothed Graph Contrastive Learning model (SGCL), which leverages the geometric structure of augmented graphs to exploit proximity information associated with positive/negative pairs in contrastive loss. The proposed SGCL adjusts the significance of these pairs in contrastive loss by incorporating three distinct smoothing techniques that yield smoothed positive/negative pairs. To enhance scalability for large-scale graphs, the proposed framework incorporates a graph batch-generating strategy that partitions the given graphs into multiple subgraphs, facilitating efficient training in separate batches. Through extensive experimentation in an unsupervised setting on various benchmark datasets, particularly those of large scale, we demonstrate the superiority of our proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the challenge in Graph contrastive learning (GCL), particularly the problem of uniformly incorporating negative samples in the contrastive loss, which may not account for the proximity of the true positive nodes. The authors introduced a new method Smoothed Graph Contrastive Learning model (SGCL), aiming to consider the geometric structure of augmented graphs and exploit proximity information for better representation learning.

### Strengths
1. The presentation is clear.
2. The studied problem is interesting.

### Weaknesses
1. The newest baseline is published in 2022. Therefore the paper misses a lot SOTA methods.
2. The paper doesn't involve computational cost analysis. Moreover, the cost should be compared with baselines.
3. Smoothing for graph contrastive learning seems to be a little trivial to me. 
4. Can the proposed methods be adopted for graph-level tasks [1,2]?

### Questions
See above

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
This paper introduces Smoothed Graph Contrastive Learning to address the issues of false positives and false negatives in graph contrastive learning. The primary idea is to leverage the structural information of the graph to obtain pairwise proximity information and assign weights to each pair. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
- The approach presented in this paper, using graph structural information to smooth the contrastive learning loss, is both intriguing and innovative.
- The proposed method has a solid theoretical foundation.
- The paper provides ample background knowledge to assist readers who may not be familiar with graph smoothing.

### Weaknesses
 - The structure and organization of this paper appear quite impractical. The author dedicates a substantial portion of Section 3 to background knowledge, occupying a significant amount of space, and only begins to introduce the proposed method towards the end of Page 5. This has resulted in an insufficiently detailed experimental section. It is advisable for the author to trim down the content in Section 3 and allocate more space to the experimental aspects of the paper.
- The author fails to provide the rationale and intuition behind using the loss function as depicted in Eq.4. This loss function does not appear to be particularly innovative. Additionally, I believe that the choice of lambda is crucial, but the author does not explain how lambda is selected.
- The experiments in this paper seem overly simplified, and the dataset splits chosen do not align with commonly used splits in self-supervised learning (public split). The selection of baselines appears outdated, and the reported results in the paper do not align with the results reported for these baseline methods in their original sources.

### Questions
I have some questions about the definition of Equation 4.

- In Equation 4, the author claims that $C$ is the cross-correlation matrix of the embedding matrix. However, according to the definition of cross-correlation, $C$ should be an $F\times F$ matrix rather than an $N\times N$ matrix, which contradicts Equation 5. I would recommend the author to double-check this issue.
- In Equation 4, when $i≠j$ and $\hat{\pi}(i, j) = 1$, Eq.4 assigns a high weight to minimize $c_{ij}$. This seems counterintuitive because $\hat{\pi}(i, j) = 1$ should imply that nodes i and j are very likely to be false negatives, so $c_{ij}$ should be maximized rather than minimized.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method called Smoothed Graph Contrastive Learning (SGCL) that tries to use the graph structure to spread out the weights for positive and negative pairs. The matrix $\tilde\Pi_{pos}^{(i,j)}$ is the smoothed out matrix of positive weights (smoothing is done for example using the graph Laplacian matrix). Positive pairs between graph views $\mathcal{G}^{(i)}, \mathcal{G}^{(j)}$ are encouraged to have embeddings with a cosine similarity close to 1. Negative pairs are encouraged to have orthogonal embeddings.

The main contribution of the paper is the idea to smooth positive/negative weights based on graph structure. Experimental results are compellingly in favor of the proposed method.

### Strengths
* The main idea to smooth out weights is simple. 
* The proposed method performs really well in experiments.

### Weaknesses
None that I can come up with.

### Questions
What are the final embedding dimensions in the experiments?

Typo:
* page 3, Section 3.2, second paragraph: ${0,1}$ should be $\{0,1\}$ 
* Section 4.2.3: Is $\tilde D_{ii}$ the degree + 1?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on tackling the equal treatment issue of misclassified false negative nodes in conventional GCL approaches. Specifically, the paper presents a Smoothed Graph Contrastive Learning model which leverages the geometric structure of augmented graphs to exploit proximity information associated with positive/negative pairs in contrastive loss. This enables the significance of node pairs to be adjusted. Furthermore, a graph batch-generating strategy that partitions the given graphs into multiple subgraphs is also proposed to facilitate efficient training in separate batches. Experiments show the superiority of the proposed framework.

### Strengths
1. This paper is well-motivated. Equal treatment of misclassified false negative nodes and the lack of a mechanism to differentiate misclassified nodes based on proximity can be harmful to graph contrastive learning.
2. Applying smoothing approaches to pair matrices is novel and interesting.

### Weaknesses
1. The writing of the paper should be improved. There are many minor mistakes in the paper:
  - "These methods, including , including Deep Graph Infomax" in paragraph 2 of Section 2.
  - "Therfore" in paragraph 2 of Section 3.1.
  - In caption of Figure 2, g(j) is not a positive pair.
  - "distinguishe" in paragraph 1 of Section 4.2.4.
2. A persuasive demonstration of why misaligning negative pairs is harmful should be provided.
3. The smoothing method only employs the original graph information. However, the node relationship can be highly changed after augmentation. For example, two highly related nodes can be dissimilar when one of them is dropped. In such cases, is the proposal still efficient?
4. The proposal seems incremental - the smoothing technique, loss function and subgraph generating can be easily detached from the framework.
5. Can previous contrastive objectives be used in the proposal? There is a lack of ablation studies to exclude the effect of the proposed contrastive objective.
6. A time analysis should be provided to verify the efficiency of the proposal.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
