# From GNNs to Trees: Multi-Granular Interpretability for Graph Neural Networks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Interpretable Graph Neural Networks (GNNs) aim to reveal the underlying reasoning behind model predictions, attributing their decisions to specific subgraphs that are informative. However, existing subgraph-based interpretable methods suffer from an overemphasis on local structure, potentially overlooking long-range dependencies within the entire graphs. Although recent efforts that rely on graph coarsening have proven beneficial for global interpretability, they inevitably reduce the graphs to a fixed granularity. Such inflexible way can only capture graph connectivity at a specific level, whereas real-world graph tasks often exhibit relationships at varying granularities (e.g., relevant interactions in proteins span from functional groups, to amino acids, and up to protein domains). In this paper, we introduce a novel Tree-like Interpretable Framework (TIF) for graph classification, where plain GNNs are transformed into hierarchical trees, with each level featuring coarsened graphs of different granularity as tree nodes. Specifically, TIF iteratively adopts a graph coarsening module to compress original graphs  (i.e., root nodes of trees) into increasingly coarser ones (i.e., child nodes of trees), while preserving diversity among tree nodes within different branches through a dedicated graph perturbation module. Finally, we propose an adaptive routing module to identify the most informative root-to-leaf paths, providing not only the final prediction but also the multi-granular interpretability for decision-making process. Extensive experiments on the graph classification benchmarks with both synthetic and real-world datasets demonstrate the superiority of TIF in interpretability, while also delivering a competitive prediction performance akin to the state-of-the-art counterparts. Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a TIF that transforms GNNs into hierarchical tree structures to provide multi-granular interpretability for graph classification tasks.

### Strengths
The paper is very interesting, and the author finds that multi-granular interpretability in GNNs is important but was overlooked by previous works. Thus, they propose TIF to enhance multi-granular interpretability. Extensive experiments show that the proposed method is effective and demonstrates good interpretability.

### Weaknesses
Overall the paper is good but why does Table 2 have no std value?

The framework requires significant computational resources to maintain and process multiple branches and paths per node, along with multiple perturbation matrices for each node. The hierarchical tree structure adds computational complexity at each level.

The architecture is complex with three major modules (coarsening, perturbation, routing) and requires careful tuning of 5 different hyperparameters (α1-α5). This makes it more difficult to implement and maintain than simpler interpretability approaches, especially considering the additional logic needed for the dynamic hardening mechanism.

There is no formal mathematical justification for why the multi-granular approach improves interpretability, nor are there guarantees regarding the optimality of the tree structure.

### Questions
The training process requires balancing various loss terms, but the paper offers limited guidance on optimizing this process.

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
This paper introduces a Tree-like Interpretable Framework (TIF) for inerpretable graph classification, transforming standard GNNs into hierarchical trees that represent graphs at varying granularities. TIF uses a graph coarsening module to compress graphs while maintaining diversity among tree nodes, and an adaptive routing module to highlight the most informative paths for decision-making. Extensive experiments show that TIF improves interpretability and achieves competitive prediction performance compared to state-of-the-art methods.

### Strengths
1. It is reasonable to require hierarchical explanations for the graph classification tasks of GNNs, and the issue addressed in this paper is of practical significance.
2. The paper employs sufficient comparative algorithms to demonstrate the effectiveness of the proposed algorithm.
3. The introduction is well-written and provides clarity, greatly aiding in the understanding of the paper's contributions and innovations.

### Weaknesses
1. The notation in the methods section is quite confusing due to the various subscripts, making it very difficult to follow.
2. The evaluation metrics used to measure the effectiveness of model explanations are not sufficiently convincing.
3. There is a lack of visual comparisons between the various interpretable GNNs, such as GSAT vs the proposed method.
4. There is a lack of analysis regarding the algorithm's complexity and running efficiency.
5. The proposed algorithms lack clear theoretical foundations and appear to be based solely on heuristic designs.

### Questions
1. In Fig. 1, what do "finer graph" and "moderate graph" represent? Why is the progression from finer to moderate to coarsen? It is recommended to explain this in the caption or the main text.
2. what is the relationship between $ \hat A$ and $A^{(l+1)}$?  Additionally, as shown in eq (5), does the coarsened adjacency matrix $ \hat A$ have the same dimensions $n*n$ as the adjacency matrix of the original graph? Why eq(5) can help the model ensure the connectivity of the coarsened graph?
3. Regarding the explanation accuracy metric, can the softmax output from the GNN be considered as confidence? This lacks theoretical justification.
4. Regarding the consistency metric, is the capability of graph kernels sufficient for distinguishing structural differences?
5. Conducting explanation experiments on the Mutag dataset is necessary.
6. Please provide visual explanations of algorithms like GSAT on the MultipleCycle dataset.

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
5

### Summary
The authors propose a novel interpretable graph learning method, i.e., TIF, which transforms the GNN into a hierarchical tree. Within the hierarchical tree, each layer represents a graph granularity and each node represents a coarsened graph. In detail, the hierarchical graph coarsening module clusters the graph nodes into coarser clusters and then the learnable graph perturbation module introduce various perturbations to propel the robustness and the diversity of the coarsened graph. At last, an adaptive router identifies the best root-to-leaf path and provides the prediction result. Sufficient experiments demonstrate the effectiveness of TIF in both interpretation and prediction.

### Strengths
1. The tree structure based interpretation method is intriguing and can further enlighten the GNN explanation field.
2. The manuscript is well-organized and the proposed TIF framework is clearly introduced, making the whole work easy to understand.
3. The experiments are sufficient and discussed in detail, verifying the effectiveness of the proposed TIF model.
4. The Figures and Tables are insightful and well-analyzed, deriving meaningful conclusions that facilitates the understanding to TIF.

### Weaknesses
1. The definition of interpretation in this work is opaque. Whether the selected root-to-leaf path or the final leaf node serves as the interpretation to the input graph? Furthermore, why the coarsened graph can be considered as a kind of explanation? An example of input graph, the prediction result, and the corresponding explanation is helpful to figure this issue out. The connection between the coarsened graphs at each layer and a ground-truth explanation, particularly for synthetic datasets where such ground truth is available, is not clearly established. It remains unclear how the hierarchical coarsening process relates to known interpretable structures within the data.
2. The evaluation metrics adopted in experiments fail to reflect the sparsity of the generated explanation. A trivial explanation, such as the original graph, is meaningless to practical applications. The compression ratio, while mentioned, does not fully capture the quality of the explanation in terms of its informativeness and relevance to the prediction task. A more direct measure of explanation sparsity and its impact on prediction accuracy should be considered.
3. Some terminologies are used before giving definition. In Figure 3(c), the definition of path importance is missing in the manuscript. In Section 4.4, the compression ratio q is discussed without introduction or definition. The lack of clear definitions for these key terms hinders the understanding of the proposed method and its evaluation.
4. In Figure 4 and Figure 5, what is the principle to measure the quality of the generated explanations? For example, which instance of the finer graphs in Figure 4 is closer to the ground-truth explanation? Furthermore, the explanation provided by GIP is grey (without color), while that of TIF is colorful. If this difference represents some superiorities of TIF, and please elaborate if yes. The criteria for evaluating the quality of the generated explanations are not well-defined, making it difficult to objectively assess the superiority of the proposed method.
5. In Figure 7, the notations "IAR" and "LV" lack definition and the discussion of Figure 7 mismatches with it. The absence of definitions for these notations makes it difficult to understand the experimental setup and results.

### Questions
1. Could you provide an example which contains the input graph, the root-to-leaf path, the coarsened graphs of each layer, and the final prediction. A detailed analysis to  the input, the explanation, and the prediction can facilitate the comprehension of TIF.
2. An ablation study towards the graph perturbation module is recommended, to demonstrate the effectiveness of enhancing diversity.

### Soundness
3

### Presentation
3

### Contribution
3
