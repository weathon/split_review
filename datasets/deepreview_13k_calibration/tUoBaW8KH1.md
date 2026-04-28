# Rethinking the Smoothness of Node Features Learned by Graph Convolutional Networks

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
It has been proved that graph convolutional layers (GCLs) using ReLU or leaky ReLU activation function smooth node features. Such a smoothing process is beneficial for node classification using a few GCLs. However, deep graph convolutional networks (GCNs) tend to learn homogeneous node feature vectors over the graph, making nodes indistinguishable. In this paper, we develop a new understanding of the smoothness of node features learned by GCNs by establishing a fine-grained analysis of how ReLU or leaky ReLU affects the smoothness of its input vectors. First, we establish a geometric relationship between the input and output of ReLU or leaky ReLU. Then we show that if one ignores the magnitude of the feature vectors, ReLU and leaky ReLU smooth their input feature vectors, echoing existing theory. We further show that taking the magnitude of feature vectors into account, ReLU and leaky ReLU can increase, decrease, or preserve the smoothness of their input vectors. Our theory informs the design of a simple yet effective approach to let GCN learn node features with a desired smoothness that improves its empirical performance for graph node classification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper first shows that the image of ReLU and Leaky ReLU is contained in a particular sphere. As a corollary, alternative proofs are given to the contraction property of ReLU and Leaky ReLU (with respect to the distance to the eigenspace $\mathcal{M}$). Then, this paper defines the normalized smooth index $s(\cdot)$ for each feature dimension and elucidate how the parallel component of a feature vector to $\mathcal{M}$ affects the change of $s(\cdot)$ by applying ReLU and Leaky ReLU. Based on this, this paper proposes Smoothness Control Term (SCT) to adjust the feature component parallel to $\mathcal{M}$ as bias terms of GNN layers. SCT is applied to GCNII and EGCN models and evaluates its performance on five Citation Network datasets and node classification problems on five heterophilic datasets.

### Strengths
- The proposed method improves prediction accuracy, especially for datasets with high heterophily (Table 2). This result is consistent with the claim that the proposed method is effective for over-smoothing.
- The proposed method applies to most GNNs of MPNN type, although numerical verifications are limited to GCNII and ECGN.
- The proof is carefully written and easy to follow.

### Weaknesses
 - The proof about the contraction property applies only to ReLU and Leaky ReLU. Therefore, this theoretical analysis does not broaden the applicable GNN types.


### Questions
* P.2: *We prove that there is a high-dimensional sphere ... ReLU or leaky ReLU*: It is difficult to grasp what is intended by this sentence alone. It would be better to be more specific. For example, *We prove the output of ReLU or Leaky ReLU lies in a high-dimensional space characterized by the input.*
* P.5, Definition 4.1: $\|\boldsymbol{z}_{\mathcal{M}}^{(i)}\|$ is undefined.
* P.7: If I understand correctly, the $\beta_l$ parametrization comes from the work of GCNII. If this paper references it, the paper should be cited explicitly.
* P.7: $\boldsymbol{W}^1$ -> $\boldsymbol{W}^l$
* P.8, Table 1: The column "16 Layers" is not aligned.

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
This paper explores how ReLU and leaky ReLU activation functions affect the smoothness of node features in Graph Convolutional Networks (GCNs). It introduces a theoretical framework and a practical algorithm to control feature smoothness. The paper's main contributions include demonstrating that these activations smooth input features without considering magnitude and proposing a learnable smoothness control term (SCT) to enhance node classification in GCNs. This work is the first to comprehensively investigate these aspects, offering insights and practical improvements for graph node classification with GCNs.

### Strengths
1) This paper comprehensively investigates the impact of ReLU and leaky ReLU for the first time in graph convolution, which is very meaningful.
2) The theoretical and empirical evidence presented in this paper appears to be quite sound.
3) The proposed learnable smoothness control term (SCT) can enhance the performance of existing GNN models in node classification.

### Weaknesses
1) The writing of this paper needs further improvement, as the theoretical part is not very easy to understand. It is recommended to add a summary of notations and optimize the formatting. Specifically, the geometric interpretation of how ReLU and leaky ReLU affect feature smoothness is not immediately clear, and the connection between the projection onto the eigenspace \mathcal{M} and the resulting smoothness needs more explicit explanation. The current presentation makes it difficult to follow the logical flow of the theoretical arguments. A more intuitive explanation of the core concepts would be beneficial.
2) Experiments show that the performance improvement of SCT on deep models like GCNII and EGNN is relatively marginal. While the paper claims consistent improvements, the magnitude of these improvements, especially on homophilic graphs, is not substantial. It raises questions about the practical significance of SCT in complex architectures. The reported gains on smaller datasets also need to be more thoroughly analyzed to determine if they are statistically significant or due to random variations.

### Questions
1) Please refer to the aforementioned weaknesses.
2) I don't have major concerns about this paper. My concern lies in the further improvement in writing is needed. Additionally, I haven't thoroughly reviewed the paper's proofs, and I will consider the opinions of other reviewers and relevant discussions before making a final decision.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the properties of node features learned by Graph Convolutional Networks (GCNs) with a focus on the smoothness of the features. It challenges the conventional understanding of the role of activation functions like ReLU or leaky ReLU in the smoothing process of node features in GCNs. Traditionally, it was believed that these activation functions contribute to smoothing the node features, which is beneficial for tasks like node classification when using a limited number of Graph Convolutional Layers (GCLs). However, the authors argue that this might not always be the case, especially in deeper GCNs. Through empirical studies and theoretical analysis, the paper presents evidence that in deeper networks, the node features might actually become less smooth, contrary to the established belief. This finding is significant as it opens up new avenues for understanding and improving the learning process in deep GCNs, particularly concerning the choice and role of activation functions in shaping the learned node features.

### Strengths
* The argument that challenges the traditional understanding of activation function roles in GCNs seems to be presented clearly and logically, enhancing the paper’s accessibility and impact.

* The paper appears to delve deeply into the nuances of node feature smoothness in GCNs, providing a comprehensive analysis that bolsters the quality of the work.

### Weaknesses
 * The paper seems to heavily rely on previous works [1,2] for its theoretical results. A more independent theoretical contribution or a clearer delineation of the novel aspects beyond the referenced works would strengthen the paper's originality.  

* The empirical validation could be broadened to enhance the robustness of the findings. Incorporating a more diverse array of datasets and experimenting with various network architectures would be beneficial. Notably, the largest non-homophily graph used is the Squirrel dataset, which consists of 5201 nodes. Exploring larger and more varied graphs could provide more comprehensive insights.

* The proposed method, as represented by Equation 6, appears to be a somewhat incremental modification, seemingly adding only a bias term to the graph layer. A deeper discussion on the novelty and impact of this modification would be beneficial to understand its significance and contribution better.

* The presentation of results in Table 1 could be improved for clarity and comprehensiveness.

* The benifit of proposed method is somewhat weak when nerual network is deep.

### Questions
* Could you clarify the specific novel contributions of your theoretical analysis beyond the foundations laid by references [1,2]?

* Have you considered testing your approach on a broader variety of datasets, especially larger and more complex non-homophily graphs beyond the Squirrel dataset?

* Could you elaborate on the novelty and significance of the modification introduced in Equation 6? How does the addition of a bias term fundamentally impact the model's behavior or performance?

* It seems that the benefits of the proposed method diminish in deeper neural networks. Could you provide more insights into why this might be the case and whether there are ways to mitigate this limitation?


-----------------------
Thank you for addressing the feedback provided. After reviewing your rebuttal and considering other reviewers' comments, I have decided to maintain my original score for your paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the impact of ReLU and LeakyReLU nonlinearities on the smoothness of node features and proposes a method for regulating feature smoothness under a normalized smoothness metric. While earlier theories suggested that these nonlinearities always result in smoother features, this study reveals that, when considering feature magnitude and applying a normalized smoothness metric, ReLU and LeakyReLU can actually increase, decrease, or maintain the smoothness metric. Notably, by adjusting the input's projection in certain eigenspaces, one can manipulate the output's smoothness to achieve a desired level. The paper introduces a technique known as the "smoothness control term" (SCT), which is designed to regulate node feature smoothness, and it is experimentally tested to validate its effectiveness.

### Strengths
1. Understanding the effect of nonlinearities is an important question.
2. The empirical performance of SCT looks promising in Table 2.

### Weaknesses
1. Although seemingly making sense, “normalized smoothness”, as measured by s defined in eq.(4) is not valid for interpretation. It disconnects node smoothness from model performance, making it carry no insights into practice and thus it is meaningless to study.

    For instance, consider a graph with two classes of nodes: one class having feature values of 1, and the other class with feature values of -1. In this case, a linear classifier would have perfect classification performance.  If we consistently add one to each node's feature, the differences among node features would not change, and if we apply a classifier again to classify based on the new features, the performance would not change either---We are basically shifting all the node features by the same value and the bias term of a classifier can easily accommodate that. Such a phenomenon is well justified by the unnormalized metrics such as conventional Dirichlet energy because it would remain the same before and after we add the same value to each node. However, the normalized smoothness metric s proposed in this paper would get larger and larger, indicating that the node features are getting "smoother" and "smoother".

    Given the above concern and the established research on the effects of ReLU and LeakyReLU under unnormalized smoothness [5, 27] (citations provided by the paper), this paper provides very little new theoretical insight.



2. I also checked [5] (citation provided by the paper), and I didn’t see any serious evidence, either theoretical or empirical, supporting the following highlighted claim in this paper:

> [5] points out that over-smoothing – measured by the distance of node features to the eigenspace M or the Dirichlet energy – is a misnomer, and the real smoothness of a graph signal should be characterized by a normalized smoothness, e.g., normalizing the Dirichlet energy by the magnitude of the features. 

The only related sentence I saw was

> Finally, analyzing the real over-smoothing effect, i.e., the Rayleigh quotient $\frac{tr(X^T \tilde{\Delta} X)}{||X||^2_2}$ for
deep GNNs is still an open and important question.

 But this itself doesn't justify the validity of the normalized smoothness. 

3.  The improvement over stronger baselines (GCNII and EGNN) in Table 1 is limited in most cases, which raises doubts about the overall effectiveness of SCT.

### Questions
Could the authors provide standard deviations for the experimental results in Table 1 (particularly for the baseline methods) and Table 2?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
