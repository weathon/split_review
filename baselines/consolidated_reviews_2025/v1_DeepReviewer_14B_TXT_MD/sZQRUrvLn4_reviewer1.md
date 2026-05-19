### Summary

The paper studies the ability of GNNs to count substructures. The authors provide sufficient conditions on the graph families under which GNNs can count subgraphs and learn to count subgraphs sample-efficiently. They also propose dynamic programming algorithms for restricted variants of subtree isomorphism and show that message-passing GNNs can simulate these algorithms. The theoretical results are supported by empirical validation on real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical analysis of GNNs' subgraph counting abilities beyond worst-case scenarios, offering sufficient conditions for GNNs to count subgraphs. 
2. It introduces novel dynamic programming algorithms for restricted subtree isomorphism problems and demonstrates that message-passing GNNs can efficiently simulate these algorithms.
3. The theoretical claims are empirically validated on real-world datasets, providing evidence that the derived conditions for GNNs to count subgraphs hold in practice.

### Weaknesses

#### Some Related Works


#### comment

1. The conditions and algorithms proposed may be restricted to certain types of graphs and patterns, which could limit the generalizability of the findings. Specifically, the focus on tree patterns and the reliance on the universal cover property may not extend to more complex graph structures with cycles or other non-tree-like characteristics. The paper does not adequately address how the proposed methods would perform on graphs with significant heterogeneity in node degrees or complex structural motifs beyond trees.
2. The paper's theoretical analysis and algorithms may be complex and difficult to understand for readers without a strong background in graph theory and GNNs. The concepts of k-local functions, (l,k)-identifiability, and the use of universal covers are not intuitively explained, making it challenging for a broader audience to grasp the core ideas. The connection between these theoretical constructs and the practical performance of GNNs is not made sufficiently clear.
3. While the paper provides empirical validation, further experiments on diverse datasets and with different GNN architectures could strengthen the findings. The current experiments primarily focus on molecular datasets, which may not be representative of all real-world graph data. The paper lacks a thorough exploration of how the proposed methods perform on graphs with different characteristics, such as social networks, citation networks, or graphs with varying sizes and densities.

### Suggestions

To address the limitations regarding the scope of graph types, the authors should explore the applicability of their methods to graphs with more complex structures. This could involve investigating how the dynamic programming algorithms can be adapted to handle cycles or other non-tree-like substructures. Furthermore, the authors should provide a more detailed analysis of the limitations of their approach, explicitly stating the types of graphs and patterns for which their methods are not suitable. It would be beneficial to include experiments on datasets with more diverse graph structures to demonstrate the generalizability of the findings. For example, experiments on social networks or citation networks could provide valuable insights into the performance of the proposed methods in different contexts. The authors could also consider exploring alternative representations or algorithms that are less restrictive in terms of the graph structures they can handle.

To improve the clarity and accessibility of the theoretical analysis, the authors should provide more intuitive explanations of the key concepts. This could involve including more illustrative examples and diagrams to help readers understand the meaning of k-local functions, (l,k)-identifiability, and universal covers. The authors should also provide a clearer explanation of how these theoretical constructs relate to the practical performance of GNNs. A step-by-step walkthrough of the dynamic programming algorithms, with concrete examples, would also be beneficial. Furthermore, the authors could consider providing a simplified version of their theoretical results for a broader audience, while still maintaining the rigor of their analysis. This could involve highlighting the key insights and implications of their findings without getting bogged down in technical details.

To strengthen the empirical validation, the authors should conduct more extensive experiments on diverse datasets and with different GNN architectures. This should include datasets with varying graph sizes, densities, and structural characteristics. The authors should also explore the performance of their methods with different GNN architectures, including both message-passing and non-message-passing models. It would be beneficial to include a more detailed analysis of the experimental results, including a discussion of the limitations of the proposed methods and the potential for future improvements. The authors should also consider comparing their methods to other existing approaches for subgraph counting, providing a more comprehensive evaluation of their contributions.

### Questions

1. How do the proposed conditions and algorithms perform on graph datasets that do not satisfy the sufficient conditions outlined in the paper?
2. Can the authors provide more intuitive explanations and examples for the theoretical concepts introduced in the paper, such as k-local functions, (l,k)-identifiability, and quite-colorful subgraph isomorphism?
3. How do the proposed methods compare to other existing approaches for subgraph counting in terms of computational complexity and practical performance?

### Rating

6

### Confidence

3

**********
