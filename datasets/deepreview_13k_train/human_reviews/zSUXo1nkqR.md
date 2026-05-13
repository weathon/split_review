# TreeX: Generating Global Graphical GNN Explanations via Critical Subtree Extraction

- Decision: Reject
- Scores: 5, 3, 3, 3, 3

## Abstract
The growing demand for transparency and interpretability in critical domains has driven increased interests in comprehending the explainability of Message-Passing (MP) Graph Neural Networks (GNNs). Although substantial research efforts have been made to generate explanations for individual graph instances, identifying global explaining concepts for a GNN still poses great challenges, especially when concepts are desired in a graphical form on the dataset level. While most prior works treat GNNs as black boxes, in this paper, we propose to unbox GNNs by analyzing and extracting critical subtrees incurred by the inner workings of message passing, which correspond to critical subgraphs in the datasets. By aggregating subtrees in an embedding space with an efficient algorithm, which does not require complex subgraph matching or search, we can make intuitive graphical explanations for Message-Passing GNNs on local, class and global levels. We empirically show that our proposed approach not only generates clean subgraph concepts on a dataset level in contrast to existing global explaining methods which generate non-graphical rules (e.g., language or embeddings) as explanations, but it is also capable of providing explanations for individual instances with a comparable or even superior performance as compared to leading local-level GNN explainers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for providing global explanations in GNNs, specifically targeting maximally powerful MPGNNs. The approach leverages clustering based on node embeddings within MPGNNs to explain substructure information at a global level. Its effectiveness is evaluated across various datasets.

### Strengths
- Providing global explanations is a crucial aspect in the development of trustworthy GNN models.
 - The paper provides adequate background information through preliminaries and related sections.
 - The effectiveness of the proposed method is evaluated by multiple datasets.

### Weaknesses
 - The methodological details in the paper are unclear. For example, while it mentions identifying graph substructures based on node embeddings, the specific approach is not adequately detailed, making it challenging to understand. The paper lacks a clear explanation of how node embeddings are transformed into substructure representations, and how the clustering algorithm is applied to these representations. The description of the overlap detection process is also vague, leaving the reader with an incomplete picture of the method.
 - A significant issue is the limited evaluation measures, with insufficient justification provided. Various measures, such as sparsity, fidelity (+ and -), and fidelity\delta [1], are commonly used and could be considered in the evaluation. The paper only uses AccFidelity and ProbFidelity, which are similar to Fid-, but it does not explain why other metrics, such as those evaluating the impact of feature removal, are not relevant. The lack of justification for the chosen metrics makes it difficult to assess the completeness of the evaluation.
 - More comparisons with existing global XAI methodologies are needed. Methods like D4Explainer [2] and TAGE [3], which also can provide global explanations, would enhance the baseline comparisons. The paper does not adequately discuss how its approach differs from these methods in terms of the type of explanations generated, the tasks they are designed for, and their underlying assumptions. This lack of comparison makes it difficult to position the proposed method within the broader landscape of global graph explainability.

### Questions
Please refer to the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a type of global GNN explanation methods, by extracting the subtrees incurred by the GNN message passing mechanisms. The paper argues that this can provide more intuitive local, class, and global level explanations.

### Strengths
- The proposed method is intuitive and technically sound.
- The experimental analysis is abundant.

### Weaknesses
 - First, the definitions for different types of GNN explanations are quite vague. This paper claims that GNN explanation methods can be categorized into local and global levels; it claims that instance-level explanation is local-level. Under this definition, the proposed method should be considered as local-level, since it only works in the instance-level graph graph classification task where all the subtrees are extracted from the graph to be predicted. 
- Second, the proposed methods only seem to work with graph-level prediction tasks and do not seem to work with node-level prediction tasks. I did not find the paper explicitly discussing that. The existing popular GNN explainability methods, such as GNN Explainer, can work with both node and graph-level prediction tasks. The paper should clearly emphasize its limitations.
- A key idea of this paper - last layer node embedding represents the full L-hop subtrees, is a well-known result in the GNN research domain (for example, it has been taught throughout the Stanford CS224W course with millions of views on Youtube). The justifications in Section 4.2 look redundant to me. Furthermore, Theorem 4.2 and its proof are a direct application of the results from the GIN paper, which is also redundant. 
- Overall, I do not find the proposed method offers a new understanding of the explainable GNN domains, especially given that it can only work with graph-level prediction tasks, and the performance is only on par or even worse than existing methods (Table 1). I am happy to defend my opinion further if needed

### Questions
- Has the authors considered a more basic baseline, where we can use an attention-based aggregator over last layer node embeddings to make the final graph level prediction? The, we can simply return the top-k subtrees based on the attention scores. I found this method to be more convenient, easier to implement, and more efficient to compute. I did not get how the proposed approach fundamentally differs from that simpler baseline.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents TreeX, a method for GNN explainability. It extracts subtree information to construct local concepts, global concepts, and further generate rules for class-specific interpretations. TreeX is computationally efficient compared to previous subgraph-based methods, as it leverages message passing to capture subtree features, while still delivering meaningful concepts for interpretability.

### Strengths
The proposed method is fast comparing to previous subgraph based method with last layer embedding after message aggregation, which makes it potentially more scalable comparing to subgraph based enumeration method.

The proposed method can cover both local and global concept extraction.

### Weaknesses
The subtree features extracted by last layer embedding might not be able to fully reflect meaningful concept, and could ignore certain patterns that are useful for explainability. See questions for more details.
The evaluation is not sufficient, deeper experiments should be done on more architectures (GCN, GraphSAGE, GAN, etc), as different GNN architectures have varying expressive power and aggregation mechanisms. Besides, variations in last layer embedding quality across architectures could influence the interpretability in TreeX.

### Questions
I have some questions regarding the methodology for constructing concepts based on the last-layer embeddings.  

How does the method ensure these clusters are reflecting meaningful, distinct structural concepts within the graph? Elaborated below.
The paper uses last-layer embeddings to construct concept. It is true that the last layer embedding for a specific root node aggregates the nodes within L-hops. However, this aggregation would overlook finer subgraph features (i.e. specific motifs or relational patterns[1][2]). Will this affect the explainability and how does the method address this limitation?
Additionally, how to validate the meaningfulness of these clusters?  Regarding the clustering algorithm, given the similarities in last-layer embeddings, k-means may face issues that embeddings can be smooth or overlapping. As a result, it might not distinguish nuanced structural variations effectively. Did you evaluate whether k-means clustering accurately captures meaningful and distinct concepts in the last-layer embeddings? Do you consider alternative clustering approaches for finer clustering?
[1] GNNExplainer: Generating Explanations for Graph Neural Networks
[2] PGM-Explainer: Probabilistic Graphical Model Explanations for Graph Neural Networks

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
TreeX introduces an explanation method primarily for graph classifiers, providing both local and global explanations based on the subgraph concept derived from their proposed subtree extraction method. Local concepts are extracted from subtrees in individual instance graphs. Final local concepts for each input graph are obtained by clustering through $k$-means. Global concepts are then extracted by aggregating and clustering these local concepts. To understand the impact of the discovered global concepts, the weight of each concept is optimized to represent the prediction of a certain class.

### Strengths
Providing local and global explanations is crucial for understanding predictive outputs at both individual and class levels. Figure 1 offers an insightful perspective on how each instance's prediction compares to class-specific patterns, making it easier to debug predictive outputs. Furthermore, extracting concepts based on subtrees presents a novel approach to mining meaningful patterns.

### Weaknesses
W1. The proposed method's heavy reliance on K-means clustering for both local and global concept extraction introduces several inherent weaknesses. Consequently, the proposed method exposes the weaknesses and limitations of clustering such as initialization issues, sub-optimal issues, the sensitivity of hyper-parameter $k$, and quality issues such as under-clustering or over-clustering. Due to this well-known limitation, the assignment of clusters is likely to be sensitive. Thus, explanations based on the clustering method may not be robust.

W2. The process of providing final explanations in Figures 8, 9, 10, and 11 is not clear. Based on class-specific global rules,  connecting concepts and subgraphs in the specific input graph.

W3. Experiments are not thorough in several aspects as below.

(1)  A quantitative evaluation of global explanations is lacking, which is a key contribution of the proposed method. This aspect should be more thoroughly examined.

(2) Global explainers in the graph domain such as XGNN [1] and GNNInterpreter [2] are not considered in the comparison.

(3) No visualization of the local explanations.

(4) AccFidelity is an easy metric to achieve decent performance as it counts the explanation as correct even when $\hat{y}_i=0.51$ in binary classification tasks. Nevertheless, authors only use $Fid^{-}$, excluding the $Fid^{+}$ [3] which is the most common measurement in many literatures.

(5) The time analysis focuses solely on explanation inference, omitting the process of concept extraction. This process likely incurs significant computational costs due to its use of k-means algorithms in twice and post-processing steps to extract final concepts. A more comprehensive time analysis would provide a clearer picture of the method's efficiency.

Minor typo in line 352, e.g., In the he BA-2Motifs data.

### Questions
Q1. The authors currently evaluate the performance of the proposed method under different random seeds when splitting the data. Given that clustering algorithms are sensitive to initialization based on random seeds, how do the explanation results change under different cluster assignments resulting from different initialization?

Q2. Why are the extraction processes for local concepts in Eq. 4 and global concepts (which are closest to the center of cluster $U_j$) from clusters different? Can you further discuss the motivation behind the proposed method?

Q3. How can explicit local explanations be derived from the global rules in the form of presenting important subgraphs?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a method to explain message-passing GNNs via critical subtree extraction. It analyzes and extracts critical subtrees incurred by the inner workings of message passing. An efficient algorithm which doesn't require  complex subgraph search is proposed to aggregate subtrees in the embedding space. As a result, we can make intuitive graphical explanations for Message-Passing GNNs on local, class and global levels.

### Strengths
The paper made two innovative contributions:
1. It providing a global explanations of GNNs on the dataset or class level in the format of subgraphs rather than nodes, language rules or prototype embeddings in the previous literature. 
2. Instead of subgraph enumeration or search, the paper proposed an efficient algorithm for subtree extraction, and using the root node embedding as subtree embedding.

### Weaknesses
I have concern on the global concept extraction method outlined between lines 200-206. How can the method ensure that the spaces of embedding across $D$ graph instances are aligned? The authors should provide a detailed explanation of this process, as without it, I am skeptical about the possibility of clustering the $kD$ local graph concepts, because these concepts originate from $D$ distinct embedding spaces.

In the "global rule generation for each class" (line 220-), I doubt the method can always work in general situations. The global rules are generated through frequency-based analysis, and it may be challenging to ensure that these frequency-based features always possess the necessary discriminative power to distinguish the differences between classes.

The innovation of this paper is not significant. Please compare the proposed method with 
- Motif-driven Subgraph Structure Learning for Graph Classification (https://arxiv.org/abs/2406.08897)
- STExplainer: Global Explainability of GNNs via Frequent SubTree Mining (https://openreview.net/forum?id=HgSfV6sGIn)

### Questions
P196: Should the $max$  operator or $top_k$ operator be in equation 4?
P264:  presentaions --> representations?

### Soundness
2

### Presentation
3

### Contribution
2
