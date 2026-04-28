# Is Graph Convolution Always Beneficial For Every Feature?

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Graph Neural Networks (GNNs) have demonstrated strong capabilities in processing structured data. While traditional GNNs typically treat each feature dimension equally during graph convolution, we raise an important question: \textit{Is the graph convolution operation equally beneficial for each feature dimension?} If not, the convolution operation on certain feature dimensions can possibly lead to harmful effects, even worse than the convolution-free models. In prior studies, to assess the impacts of graph convolution on features, people proposed metrics based on feature homophily to measure feature consistency with the graph topology. However, these metrics have shown unsatisfactory alignment with GNN performance and have not been effectively employed to guide feature selection in GNNs. To address these limitations, we introduce a novel metric, Topological Feature Informativeness (TFI), to distinguish between GNN-favored and GNN-disfavored features, where its effectiveness is validated through both theoretical analysis and empirical observations. Based on TFI, we propose a simple yet effective Graph Feature Selection (GFS) method, which processes GNN-favored and GNN-disfavored features separately, using GNNs and non-GNN models. Compared to original GNNs, GFS significantly improves the extraction of useful topological information from each feature with comparable computational costs. Extensive experiments show that after applying GFS to $8$ baseline and state-of-the-art (SOTA) GNN architectures across $10$ datasets, $83.75$\% of the GFS-augmented cases show significant performance boosts. Furthermore, our proposed TFI metric outperforms other feature selection methods. These results validate the effectiveness of both GFS and TFI. Additionally, we demonstrate that GFS’s improvements are robust to hyperparameter tuning, highlighting its potential as a universal method for enhancing various GNN architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the problem of feature selection for graph Convolution Networks (GCNs). It begins by introducing TFI, a metric designed to guide the selection of relevant features. Following that, it introduces GFS, a plug-in method that distinguishes between features that benefit graph convolution and those that do not contribute positively or may even have a negative impact. Then, the two sets of features are processed separately using GCN and Multi-Layer Perceptrons (MLP), respectively. Evaluations on node classification tasks demonstrate the effectiveness of the proposed TFI and GFS.

### Strengths
1 This paper is well-organized and easy to follow. 

2 The figures regarding the design motivation and the proposed framework (Figures 1 and 3) are clear.

3 The theoretical proofs are detailed.

### Weaknesses
1 The proposed feature selection metric TFI, which leverages mutual information between features and labels, is not novel. This is a conventional approach for feature selection, as outlined in [1]. Although the TFI utilizes the features derived from the neighborhood average (AX), the approach is incremental. 

2 This paper lacks a comparative analysis of classic feature selection methods, such as [2]. 

3 The GPS exhibits limited robustness to the selection of the hyperparameter r.

4 It is unclear how the high-pass filters of FAGCN and ACMGNN, as presented in Table 1, align with the TFI metric with low-pass AX.

5 A significant concern is the applicability of the proposed GFS. The paper asserts that TFI is computed on training nodes. Thus, I am concerned that the unusual dataset division of 50/25/25 for training/validation/testing employed in this paper is crucial for the effectiveness of GFS. The question then becomes: how would the results be affected if a public splitting, such as 20 per class for training in GCN, SGC, GAT, and APPNP, were applied?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new method to identify features that are favored and disfavored by GNNs. It uses topological feature selection to integrate these features into GNNs, leading to significant improvements in their performance.

### Strengths
1. The paper is well-motivated and presents a novel approach to distinguish between GNN-favored and GNN-disfavored features, treating them separately to learn with different methods.
2. The paper is clearly presented and includes solid theoretical guarantees, making it easy to follow.
3. The authors provide sufficient empirical analysis, including ablation studies and comparisons with state-of-the-art methods.

### Weaknesses
The evaluation method is not fair enough. The performance results in Table 1 should be presented with only the difference of with or without GPS, while keeping the model architecture the same (e.g., number of layers and hidden dimension). The current evaluation strategy, which appears to modify both the model architecture and the feature processing simultaneously, makes it difficult to isolate the impact of the proposed Graph Feature Selection (GFS) method. Specifically, it's unclear whether the observed performance gains are due to the feature selection process itself or the changes in the model architecture. This lack of controlled comparison hinders a clear understanding of the method's effectiveness. Furthermore, the analysis in Figure 2, while insightful, does not fully explain the significant performance gains observed in Figure 4. The minimal performance gap between GCN and MLP in low TFI regions in Figure 2 raises questions about the consistency of the results. The paper also lacks clarity on whether TFI is computed once at the beginning or at each layer. This ambiguity makes it difficult to understand the dynamics of feature selection during the training process.

### Questions
1. As shown in Figure 2, the performance gap for the Roman dataset between GCN and MLP in regions with low TFI is minimal. How is the improvement over GCN in Figure 4 so significant regardless of $r$?
2. Since features are updated in each GNN/MLP layer, is the TFI computed at each layer to get (dis)favored features, or is it only computed at the beginning? This point does not seem clearly explained in the paper.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
GNNs have strong graph learning capabilities. However, GNNs are not effective at learning all graph data features. In previous work, many metrics based on graph topology and features have been proposed to describe feature homogeneity in order to assess the effectiveness of GNNs. However, there has been no metric that can directly and effectively guide which features GNNs should learn. To fill this gap, this paper proposes an evaluation metric, Topological Feature Informative (TFI), to compute the learnability of features for GNNs. Subsequently, a dual-channel embedding architecture combining GNNs and MLPs is used to embed these features separately.

### Strengths
1. The writing of the paper is clear and easy to understand, with a well-defined theme.
2. The paper provides a theoretical foundation for using TFI to guide feature selection through simple proofs.
3. The experimental results on node classification tasks are impressively good.

### Weaknesses
The paper does not provide any statistical analysis of the selected features, which raises some questions.

### Questions
1. How is the decomposition of node features in the graph executed? 
2. What impact does the dimension of the initial node features have?
3. Can this method only be applied to node features, or can it also be used on edge features, and what would be the effect?
4. Is it possible to measure what a "good heterophily" feature looks like? Can other metrics be used for supplementary description, such as Label Homophily, Feature Homophily, Mutual Information, and so on?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper explores the varying impact of graph convolution across different feature dimensions in GNNs. It introduces a novel metric called Topological Feature Informativeness (TFI), designed to identify features that are either favored or disfavored by GNNs. The authors propose a Graph Feature Selection (GFS) method that leverages TFI to process GNN-favored features with GNNs and GNN-disfavored features with MLPs, enhancing overall performance. The experimental results across multiple GNN architectures and datasets demonstrate that GFS improves accuracy with minimal computational overhead. The work emphasizes the importance of feature-aware processing in GNNs, showing that graph convolution is not uniformly beneficial for all feature dimensions.

### Strengths
S1: The concept of distinguishing between GNN-favored and GNN-disfavored features is interesting and novel. 

S2: The paper is well-written and structured, easy for readers to follow the methodology and findings. 

S3:  The experimental results consistently demonstrate the effectiveness of the proposed GFS trick.

### Weaknesses
W1: As far as I am concerned, the theoretical analysis of the proposed strategy is incomplete. The paper does not clearly explain the specific conditions under which distinguishing between GNN-favored and GNN-disfavored features is most effective. It lacks a rigorous exploration of how the interplay between feature characteristics and graph structure impacts the performance gains of the proposed method. Specifically, the paper does not delve into how the degree of feature correlation, both within and across feature sets, influences the effectiveness of the proposed feature selection strategy. A more detailed analysis of these factors would be beneficial.

W2: The proposed TFI metric, while beneficial, appears similar to existing mutual information-based methods. The authors need to provide more clarification on how TFI uniquely contributes to feature selection in graph learning, emphasizing its distinct advantages over prior approaches. The paper does not adequately address how TFI accounts for the inherent dependencies between nodes in a graph, which are not captured by standard mutual information calculations. Furthermore, the paper should clarify how TFI handles situations where feature informativeness is highly dependent on the local neighborhood structure, a common scenario in graph data.

W3: Although the experimental results demonstrate strong performance of the GFS-augmented models, I remain somewhat unconvinced. To strengthen the validity of the findings, it would be helpful to include experiments on synthetic datasets, such as those generated by the SBM model with varying levels of heterophily and homophily. Such experiments could offer more reliable insights into the potential advantages of the proposed methodology. The current experiments do not sufficiently explore the method's behavior under different graph structural conditions, such as varying degrees of node connectivity and community structure, which could significantly impact the effectiveness of the proposed approach.

### Questions
Q1: I am still unclear about how TFI fundamentally differs from other mutual information-based metrics for feature selection in graph learning. Could the authors provide a clearer explanation of its unique contributions and advantages?

Q2: How does the proposed method handle extremely sparse features, which are common in real-world graphs? Are there specific challenges or limitations in this context?

Q3: It appears that the proposed method offers limited advantages on homophilous graphs compared to its performance on heterophilous graphs. Could the authors provide insights to clarify this discrepancy and explain why the method may be less effective in homophilous settings?

Q4: I am curious about the robustness of the proposed method when applied to noisy graphs, where certain features may contain varying levels of noise. Could the authors provide insights or results on its performance in these scenarios?"

### Soundness
3

### Presentation
3

### Contribution
3
