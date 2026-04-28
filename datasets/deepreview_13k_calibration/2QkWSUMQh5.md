# Robustness of Truss Decomposition and Implications for GNN-based Edge Classification

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Truss decomposition is an effective and practical algorithm for dense subgraph discovery. However, it is sensitive to the changes in the graph: dropping a few edges or a bit of noise can drastically impact the truss numbers of the edges. It is of practical importance to understand and characterize the robustness of truss decomposition. In this work, we study and utilize the robustness of truss decomposition in an edge-driven way. We propose to construct a dependency graph among edges to denote the impact of an edge's removal on the neighboring edges. By using the dependency graph, we introduce three measures to capture the diverse and unique properties of the edges. We provide theoretical findings and design an efficient algorithm to compute the dependency graph faster than the naive baseline. We also show that our new edge-based truss robustness measures capture intrinsic graph structures and have the potential to unearth peculiar differences that can help with various downstream tasks, such as edge classification. We integrate our measures into the state-of-the-art GNN for edge classification and demonstrate improved performance on multi-class datasets. The overhead of computing our edge-based measures is insignificant when compared to the training time. We believe that utilizing edge-based truss and robustness measures can further be helpful in edge-driven downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper quantifies the effect of removing an edge from a graph on the truss decomposition result. The authors construct a dependency graph to compute truss robustness of each edge and propose a faster heuristic based on their theoretical findings. The authors also show the effectiveness and efficiency of the proposed truss robustness to the edge classification task.

### Strengths
1.  The idea of truss robustness and dependency graph is intuitive and interesting.
2.  Theoretical findings in section 4 make the process of computing truss robustness efficient.

### Weaknesses
1. I like the first half of the paper, including the whole idea and conceptualisation of truss robustness and subsequent optimisation. However, it is unclear how truss robustness or truss decomposition effect on edge classification tasks. The authors present an interesting and computable quantitative metric for each edge, but where the metric can be effectively applied should be elaborated. It seems intuitive to me that there exists a significant portion of graph edge classifications that are not sensitive to truss robustness at all. 
2. The applicability of truss robustness seems slightly narrower due to the fact that it can be used only as a feature for edge classification. Truss robustness is expected in the study of other edge-based tasks in graph representation learning such as link prediction.
3. Moreover, only one edge classification model TER-AER was reported in experimental result. And more experiments to verify the effectiveness of truss robustness on edge classification tasks are expected. Given the results so far, it seems that the entire work's only proposes a new feature for one model  on edge classification task, making it appear that the potential impact of the entire work is limited.

Assorted minor comments:

1.  I recommend that all mentioned notations should appear in Table 3.
2.  In time complexity analysis: $|E^{1.5}| \rightarrow |E|^{1.5}$
3.  I suggest that the authors use a different notation to indicate that the set of edges sharing a triangle with a particular edge  (i.e., $E(e, G)$) to distinguish from the notation of set consisting of all the edges of the graph.
4.  In Line 137, $ts(e,G)=\Gamma_{\geq}(e,\phi(e)\text{-truss})/2 \rightarrow ts(e,G)=|\Gamma_{\geq}(e,\phi(e)\text{-truss})|/2$ ?

### Questions
1. Can the authors go into more far-reaching detail about how truss robustness can help with the edge classification task?
2. Are there any other edge classification models apart from TER+AER for which truss robustness can be applied?
3. Are there any hyperparameters such as damping factor in edgerank? If so, how are these parameters chosen?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces novel measures for edge-based robustness in truss decomposition, a method for dense subgraph discovery. The authors propose constructing a dependency graph among edges to model truss robustness and introduce three measures: Edge Robustness, Edge Strength, and EdgeRank. They provide theoretical findings and an efficient algorithm for computing the dependency graph. The paper demonstrates the effectiveness of these measures in improving edge classification tasks using Graph Neural Networks (GNNs).

### Strengths
1. The study presented in the paper fills a gap in the literature.
2. The toy exmple in Figure 1 is very helpful in understanding the concept.
3. The proposed measures show potential in improving downstream tasks like edge classification, particularly for rare classes in imbalanced datasets.

### Weaknesses
1. The paper primarily focuses on edge classification to demonstrate the effectiveness of the proposed measures. Exploring other applications, particularly those that leverage the unique properties of truss decomposition, such as identifying critical connections in network flow or community structure analysis, could significantly broaden the impact and applicability of this work.
2. Comparison with core decomposition SOTA measures could provide more context for the proposed measures' effectiveness. Specifically, a more detailed analysis of how the proposed edge robustness measures compare to existing core decomposition metrics in terms of computational complexity, sensitivity to graph density, and ability to capture different aspects of network structure would be beneficial. It would be helpful to see a comparison beyond just the core number sum, perhaps including metrics like k-shell decomposition or other related measures.

### Questions
1. Have you considered applying these measures to other edge-centric tasks beyond classification, such as link prediction or graph matching?
2. How sensitive are the proposed measures to noise or small perturbations in the graph structure? Is there a way to quantify this sensitivity?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to study the edge level truss robustness and improve the performance of edge classification.
The authors propose three metrics to measure the truss robustness based on the dependency graph.
To speed up the computation, they propose an algorithm based on the theorems of truss number computation.
The experiments of edge classification have been conducted on six real-world graphs.

### Strengths
1. Theoretical analysis is provided.
2. The algorithm for fast computation is proposed based on theorems.

### Weaknesses
1. The writing of the paper can be improved.
2. Crucial evaluations of the proposed metrics are missing.

### Questions
1. In line 96, use the math symbol “$\times$” instead of an English character “x”.
2. In line 104, the word “cutting-edge” is overly strong.
3. In Figure 2b, why use standard deviation (STD) to measure the importance of edge features? First, are all the features normalized to ensure their STDs are comparable? Second, if the goal is effective classification, why not use the idea of linear probing and report the classification performance of a linear classifier?
4. In Section 3, last paragraph, continuing from the previous question, the role of this paragraph is unclear to me. These metrics are proposed to measure the truss robustness of an edge. Instead of showing how precise these metrics measure the truss robustness, this paragraph shows they are useful for edge classification. A paragraph showing how well these metrics measure robustness should be provided.
5. In Section 4, what is the time complexity of the naive computation of the dependency graph? How much faster is the proposed algorithm?
6. In Figure 3, the same problem as Question 4, showing the proposed metrics have different distributions from the existing ones does not justify their correctness. The important thing is to measure how accurate these metrics are in estimating truss robustness.
7. In Table 2, the last two columns seem to be statistically tied. Could you provide the p-values from the t-test?
8. In summary, in my opinion, it is important to study the truss robustness of the edges and have a fast algorithm. However, the writing of this paper and the title seem to emphasize its usefulness on edge classification. While the first part lacks crucial evaluations and data analysis, the second part lacks novelty. It would be helpful if the authors can clarify this.

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
This paper, titled "Robustness of Truss Decomposition and Implications for GNN-Based Edge Classification," addresses the sensitivity of truss decomposition in dense subgraph discovery. Truss decomposition is noted to be highly effective but sensitive to small changes, like edge removals, which significantly impact edge truss values. The authors propose a new framework for characterizing truss robustness on an edge level by constructing a dependency graph that captures the impact of each edge's removal on its neighbors. They further use the captured robustness and dependencies in downstream edge classification problem via GNN.

### Strengths
1. The abstract is well-written.
2. The observation of this paper is insightful.
3. The proposed method is interesting and mathematically grounded.

### Weaknesses
1. In section 2, the paper introduces several truss-related concepts (e.g., truss number and trussness support), which can initially be confusing, especially the distinction between trussness support and truss number. An example would help clarify these concepts and highlight their differences. Additionally, the definition of trussness support in the formula (line 137) is missing the cardinality notation "∣∣" and should be corrected for clarity.
2. In Figure 2(a), the dependency graph does not fully align with the truss number definition. For example, there should be a single directed edge between e2 and e1, and an edge should also exist between e2 and e5, right? Furthermore, the statement “as is the case (e3, e5) for which are incident on the left but not connected on the right” contradicts figure 2(a), as e3 and e5 are indeed unconnected in the dependency graph. 3.
3. In Section 3, the paper lacks a formula for computing EdgeRank, which reduces the transparency and reproducibility of the method.
4. In Figure 2(b), Edge Robustness (ER) shows a relatively low standard deviation, yet no explanation is provided. It would be helpful to discuss why ER might show limited variability across classes.
5. The Experiments section lacks a direct comparison with the baseline from Chen et al. (2021) and omits runtime data for other robustness indicators like RS_{OD}, RS_{ID}, degree, and core number, which makes the efficiency claims not fully supported by experimental results. Adding a comparison with Chen et al. (2021) and reporting the runtime of other measures would provide a more comprehensive evaluation of computational efficiency and better support the paper’s claims.
6. According to Table 5, the improvement of the proposed method over coreness+degree is quite marginal, and perhaps coreness is easier to compute than the metrics proposed in this paper. Any justifications or explanations?
7. Are there other combinations (among metrics proposed in this paper and previous degree, coreness, etc) that could achieve better results? Seems they can be combined?

### Questions
Please refer to the weakness

### Soundness
2

### Presentation
1

### Contribution
2
