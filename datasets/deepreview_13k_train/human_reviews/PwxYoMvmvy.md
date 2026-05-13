# Beyond Random Masking: When Dropout meets Graph Convolutional Networks

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Graph Convolutional Networks (GCNs) have emerged as powerful tools for learning on graph-structured data, yet the behavior of dropout in these models remains poorly understood. This paper presents a comprehensive theoretical analysis of dropout in GCNs, revealing its unique interactions with graph structure. We demonstrate that dropout in GCNs creates dimension-specific stochastic sub-graphs, leading to a form of structural regularization not present in standard neural networks. Our analysis shows that dropout effects are inherently degree-dependent, resulting in adaptive regularization that considers the topological importance of nodes. We provide new insights into dropout's role in mitigating oversmoothing and derive novel generalization bounds that account for graph-specific dropout effects. Furthermore, we analyze the synergistic interaction between dropout and batch normalization in GCNs, uncovering a mechanism that enhances overall regularization. Our theoretical findings are validated through extensive experiments on both node-level and graph-level tasks across 14 datasets. Notably, GCN with dropout and batch normalization outperforms state-of-the-art methods on several benchmarks. This work bridges a critical gap in the theoretical understanding of regularization in GCNs and provides practical insights for designing more effective graph learning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the role of dropout in GCNs, addressing a gap in understanding how dropout interacts with graph structure in these models. The authors provide a theoretical analysis that dropout in GCNs generates dimension-specific stochastic subgraphs, which introduces a unique form of structural regularization that doesn’t appear in traditional neural networks. The study highlights that dropout’s effects vary based on node degree, leading to adaptive regularization that leverages topological node importance. The paper also discuss dropout’s capacity to reduce oversmoothing and presents generalization bounds tailored to graph-specific dropout effects. Additionally, it explores the combined effect of dropout and batch normalization in GCNs, identifying a mechanism that enhances overall regularization.

### Strengths
- The paper focuses on the role of dropout in GCNs, specifically analyzing its unique interactions with graph structure. This originality is meaningful to the community.
- The work presents a well-developed theoretical framework, introducing concepts like dimension-specific stochastic subgraphs, adaptive regularization based on node degree, and graph-specific generalization bounds.
- Including comprehensive experiments across 16 datasets for both node-level and graph-level tasks is encouraging.

### Weaknesses
 - The authors provide generalization bounds for graph neural networks with dropout. However, further clarification is needed on how this finding offers insights into understanding and designing graph neural networks, or any specific guidance on selecting dropout rates. With this theory, is it possible to get the best dropout rate with a specific graph structure and GNN? This would help demonstrate the practical relevance of the theory. Additionally, can the experiments provide corresponding analyses regarding this theory? For example, whether the change in performance at different dropout rates is consistent with the change in generalization bounds can be analyzed from the theory.
- The use of dropout or similar strategies designed specifically for graphs is also widely applied in GNNs, like DropNode, DropEdge, DropMeassge, etc [1, 2, 3]. The authors may need to discuss its relevance to this study, including whether the proposed theory can analyze these methods and the essential difference and connection between dropout and these methods. Compared to traditional dropout, does dropout on the graph structure more directly enhance the performance of graph neural networks?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the theoretical analysis of dropout in Graph Convolutional Networks (GCNs) and its impact on regularization and model performance.

This paper establishes a mathematical framework to analyze dropout's behavior in GCNs. 
It shows the dropout in GCN is similar to adaptive regularization that considers the topological importance of nodes, and is effective in mitigating over-smoothing in GCNs. And the dropout has synergy with batch normalization in GCNs for enhanced regularization.

### Strengths
1. The paper provides a mathematical framework that deepens the understanding of dropout in Graph Convolutional Networks (GCNs), addressing its relation to adaptive regularization and batch normalization.
2. The empirical analysis is extensive, including empirical observation of theorems and evaluation results on various datasets.
3. The idea of using active path subgraphs to understand graph feature dropout is interesting.

### Weaknesses
1. Dropout is a general and well-known technique, to achieve performance gain via dropout, the question can be how to tune the parameter. Can the theoretical analysis of dropout in GCNs provide insights on how to select the dropout hyperparameter?
2.  The paper primarily focuses on dropout in GCNs, but it may not sufficiently compare the method with other graph learning regularization techniques, e.g. [1], [2]

### Questions
- Can the theoretical analysis of dropout in GCNs provide insights on how to select the dropout hyperparameter?

### Soundness
3

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
2

### Summary
This paper develops a comprehensive theoretical framework analyzing how dropout uniquely interacts with Graph Convolutional Networks (GCNs), revealing that it creates dimension-specific stochastic sub-graphs and provides degree-dependent adaptive regularization. The research provides new theoretical insights into dropout's role in mitigating oversmoothing and its synergistic interaction with batch normalization, deriving novel generalization bounds specific to graph structures. These theoretical findings are validated through extensive experiments across 16 datasets, demonstrating improved performance on benchmark datasets like Cora, CiteSeer, and PubMed.

### Strengths
The paper demonstrates rigorous theoretical analysis with a comprehensive mathematical framework for understanding dropout in GCNs, introducing well-defined concepts like dimension-specific sub-graphs and feature-topology coupling matrices.

The research reveals novel insights about unique interactions between dropout and graph structure, particularly showing how dropout creates dimension-specific stochastic sub-graphs and exhibits degree-dependent effects leading to adaptive regularization.

The analysis is thorough and multi-faceted, examining structural regularization, oversmoothing mitigation, and interaction with batch normalization, supported by extensive experiments across 16 datasets for both node-level and graph-level tasks.

The work successfully bridges theory and practice, providing actionable insights for GCN design and training while demonstrating improved performance on benchmark datasets like Cora, CiteSeer, and PubMed.

### Weaknesses
The experimental validation lacks detailed information about the 16 datasets used, and the comparative analysis with state-of-the-art methods could be more comprehensive. Some experimental results mentioned in figures are truncated in the provided content.

The theoretical framework makes limiting assumptions about undirected graphs, and doesn't adequately address the extension to directed graphs. The interaction between dropout and different activation functions, as well as the impact of graph density on dropout effectiveness, need more exploration.

The paper lacks clear guidelines for selecting optimal dropout rates based on graph properties, analysis of scalability to very large graphs, and discussion of computational overhead for implementing the theoretical framework.

### Questions
How does the computational overhead compare to traditional dropout implementations?

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
4

### Summary
The paper performs a comprehensive theoretical analysis of dropout in the case of Graph Convolution Networks (GCN) from multiple perspectives: dimension-specific graph structure modification during training, degree-dependent effect on nodes, impact on over-smoothing, and it’s combined effect with batch normalization.

### Strengths
- The theoretical analyses are detailed and sound. 
- Mathematics and the overall logic of the paper is easy to follow.
- The paper attempts to better understand the internal workings of dropout in GCNs.

### Weaknesses
While I like the theoretical analyses presented in the paper, I think the experiments do not quite align to support the theoretical claims. Below are my concerns with the paper.

- The authors referring to the dropout and batch normalization as “our approach” in lines 409-410 and 466 is misleading since the techniques have been well-established in deep learning for improving performance. The contribution of the authors lies in the detailed theoretical analysis of these techniques within the context of a GCN. While it is a valuable contribution, the techniques should not be claimed as their approaches.
- The major concern is with the conclusions drawn from the experiments. It is already established in deep learning that dropout and batch normalization enhance performance through regularization. Therefore, only comparing the performance in Tables 1, 2, and 3 does not provide sufficient evidence that the observed improvements are specifically due to the additional effects of dropout in graph neural networks, as analyzed in the theorems. The authors need to design experiments that can directly validate their theoretical analysis. Specifically, the experiments should isolate the effects of dropout on graph structure, node degree, and over-smoothing, rather than just showing overall performance gains. The current experiments do not sufficiently disentangle the general regularization effects of dropout from the specific graph-related effects highlighted in the theoretical analysis.
- Section 3.4 describes an interesting connection between dropout, the number of GCN layers, and over-smoothing. However, the authors fail to provide experimental evidence to support this relationship. Demonstrating how dropout affects over-smoothing in GCN with varying layer depths would strengthen the paper. For instance, the authors could analyze the change in node representations or the spectrum of the graph Laplacian as the number of layers increases, both with and without dropout. This would provide a more direct validation of their theoretical claims.
- Line 472 (regarding Table 1) and line 483 (regarding Table 2) draw contrasting conclusions about the effect of dropout on Dirichlet Energy. What is the reason behind this difference in the behavior of dropout?
- Minor: Repeated use of variable 'd' for denoting degree (line 133) and node feature dimensionality (line 141).

### Questions
- Section 3.2 introduces the concept of dimension-specific subgraphs. How does this impact the aggregated node representation (including all dimensions)? Since the performance of a GCN ultimately depends on the aggregated representation, it would be insightful to explore this relationship.

### Soundness
1

### Presentation
3

### Contribution
2
