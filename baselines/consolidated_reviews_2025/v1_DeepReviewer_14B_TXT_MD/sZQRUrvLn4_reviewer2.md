### Summary

This paper studies the subgraph counting problem, which is known to be beyond the capability of standard message-passing GNNs. The authors present a series of results that go beyond the worst-case analysis and provide sufficient conditions for GNNs to count subgraphs, as well as sample-efficiently learn to count subgraphs. They also develop novel dynamic programming algorithms for restricted variants of subtree isomorphism and show that message-passing GNNs can simulate these algorithms. Finally, they empirically validate that their sufficient conditions for GNNs to count subgraphs hold on many real-world datasets, providing a theoretically-grounded explanation to their motivating observations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel analysis of the subgraph counting problem, providing a more nuanced understanding of the capabilities and limitations of GNNs in this context.
2. The authors develop new dynamic programming algorithms for restricted variants of subtree isomorphism and show that message-passing GNNs can simulate these algorithms. This provides a new perspective on the computational capabilities of GNNs and their relationship to classical graph algorithms.
3. The paper is well-written and clearly presents its results, with a logical flow and clear explanations of the key concepts and contributions.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed methods are primarily focused on tree patterns, which may not be applicable to more complex graph structures. The authors do not provide sufficient justification for why the results on tree patterns are relevant to more general graph patterns. Specifically, while the paper mentions that many small subgraphs in molecular graphs are trees, it does not address the limitations of this approach when dealing with non-tree subgraphs, which are also present in real-world datasets. The lack of a clear strategy for handling cycles and more complex graph topologies is a significant limitation.
2. The theoretical results rely on several assumptions and conditions, such as the $(l,k)$-identifiability of graphs, which may not always hold in practice. The paper does not provide a thorough discussion of the implications of these assumptions not holding, nor does it explore the robustness of the proposed methods when these conditions are violated. For example, it is unclear how the performance of the GNNs would degrade if the graphs are not perfectly $(l,k)$-identifiable, or if the subgraph counting task involves patterns that do not satisfy the 'quite-colorful' condition.
3. The experimental evaluation is limited in scope and does not fully explore the practical implications of the theoretical results. The experiments primarily focus on molecular graphs and do not include a diverse range of datasets with varying graph structures and sizes. Furthermore, the paper does not provide a detailed analysis of the computational cost of the proposed methods, particularly in terms of training time and memory requirements, which is crucial for assessing their practical applicability.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of focusing solely on tree patterns. While the authors acknowledge that many small subgraphs are trees, they should also address the challenges of extending their approach to more complex graph structures. This could involve exploring alternative methods for handling cycles and non-tree-like subgraphs, or at least providing a clear roadmap for future research in this direction. For instance, the authors could investigate the use of graph kernels or other techniques that are capable of handling arbitrary graph structures, and compare their performance with the proposed tree-based approach. Additionally, the paper should include a more detailed analysis of the types of subgraphs that are not well-handled by the current approach, and provide examples of real-world scenarios where these limitations would be particularly problematic.

To strengthen the theoretical results, the authors should provide a more in-depth analysis of the assumptions and conditions under which their results hold. This should include a discussion of the implications of these assumptions not holding, and an exploration of the robustness of the proposed methods when these conditions are violated. For example, the authors could investigate how the performance of the GNNs degrades when the graphs are not perfectly $(l,k)$-identifiable, or when the subgraph counting task involves patterns that do not satisfy the 'quite-colorful' condition. Furthermore, the paper should provide a more detailed analysis of the sample complexity of the proposed methods, and compare it with the sample complexity of other existing approaches. This would help to clarify the practical implications of the theoretical results and provide a more complete picture of the strengths and weaknesses of the proposed methods.

Finally, the experimental evaluation should be significantly expanded to include a more diverse range of datasets and tasks. This should include datasets with varying graph structures and sizes, as well as tasks that involve more complex subgraph patterns. The paper should also provide a more detailed analysis of the computational cost of the proposed methods, including training time and memory requirements. This would help to assess the practical applicability of the proposed methods and identify potential bottlenecks. Furthermore, the authors should compare the performance of their methods with other existing approaches for subgraph counting, including both GNN-based and non-GNN-based methods. This would provide a more comprehensive evaluation of the proposed methods and help to identify their strengths and weaknesses relative to existing techniques.

### Questions

1. How do the proposed methods perform on graph datasets that do not satisfy the sufficient conditions outlined in the paper?
2. Can the authors provide more insights into the practical implications of their theoretical results, such as the computational complexity and sample efficiency of the proposed methods?
3. How do the proposed methods compare to other existing approaches for subgraph counting in terms of accuracy, efficiency, and scalability?

### Rating

6

### Confidence

3

**********
