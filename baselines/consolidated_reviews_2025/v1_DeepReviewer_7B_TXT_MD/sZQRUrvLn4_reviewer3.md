### Summary

This paper studies the subgraph counting problem in graph neural networks (GNNs) and aims to explain why GNNs can perform this task effectively despite the theoretical limitations of the Weisfeiler-Leman (1-WL) test. The authors provide conditions under which GNNs can efficiently count subgraphs and develop novel algorithms for solving the subgraph isomorphism problem on trees. The paper also shows that GNNs can simulate these algorithms, providing a theoretical foundation for their empirical success in subgraph counting tasks.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides a theoretical explanation for the empirical success of GNNs in subgraph counting tasks, addressing a gap in the literature where previous work has focused on the limitations of GNNs in this area.
2. The paper introduces novel algorithms for solving the subgraph isomorphism problem on trees and demonstrates that GNNs can efficiently simulate these algorithms, providing a theoretical foundation for their empirical success in subgraph counting tasks.
3. The paper presents a rigorous analysis of the conditions under which GNNs can count subgraphs, providing insights into the expressive power of GNNs in this context.

### Weaknesses

#### Some Related Works

[1] Subgraph counting by vertex and edge coloring
[2] Subgraph counting by dynamic programming

#### comment

1. The paper does not provide a detailed comparison with existing methods for subgraph counting, such as those based on vertex and edge coloring [1] or dynamic programming [2]. A more thorough comparison would help to clarify the advantages and limitations of the proposed approach in relation to existing techniques. Specifically, the paper should discuss how the proposed method compares in terms of computational complexity, memory requirements, and accuracy for various types of subgraphs and graph structures. The lack of such a comparison makes it difficult to assess the practical significance of the theoretical results.
2. The paper does not discuss the limitations of the proposed approach, such as the types of subgraphs for which it is not effective or the types of graphs for which it does not perform well. A discussion of these limitations would provide a more balanced view of the proposed method and help to identify areas for future research. For example, it would be useful to understand how the performance of the method degrades as the size of the subgraphs increases or the complexity of the graph structure grows. The paper should also discuss the sensitivity of the method to different graph parameters, such as node and edge features.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed algorithms, which is crucial for understanding their scalability and practical applicability. The analysis should include a breakdown of the time and space complexity of each step in the algorithm, as well as a comparison with the complexity of existing methods. This analysis should also consider the impact of different graph parameters on the complexity, such as the number of nodes, edges, and subgraph size. Without a clear understanding of the computational cost, it is difficult to assess the practical feasibility of the proposed approach.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing subgraph counting methods. Specifically, the authors should include a table that summarizes the key characteristics of their approach in relation to methods based on vertex and edge coloring, as well as dynamic programming. This table should include columns for the types of subgraphs considered, the computational complexity of each method, the memory requirements, and the accuracy achieved. For example, the table could compare the proposed method with the algorithm by Chen et al. [1] for counting subgraphs of bounded treewidth, and with the dynamic programming approach by Garey et al. [2] for counting all subgraphs. This comparison should also discuss the specific scenarios where each method is most effective, highlighting the trade-offs between theoretical guarantees and practical performance. Furthermore, the authors should discuss the limitations of their approach in comparison to these existing methods. For instance, how does the proposed method handle subgraphs that are not bounded in treewidth, or graphs with complex structures? This discussion should also include an analysis of the sensitivity of the proposed method to different graph parameters, such as node and edge features, and how these parameters affect the accuracy and computational cost of the algorithm.

To address the lack of discussion on limitations, the authors should include a section that explicitly outlines the scenarios where the proposed method is not effective. This section should discuss the types of subgraphs and graph structures for which the method performs poorly, as well as the computational cost associated with these scenarios. For example, the authors could analyze the performance of the method on subgraphs with high degrees of symmetry or on graphs with a large number of nodes and edges. The authors should also discuss the limitations of the method in terms of the size of the subgraphs that can be handled efficiently. Furthermore, the authors should analyze the sensitivity of the method to different graph parameters, such as node and edge features, and how these parameters affect the accuracy and computational cost of the algorithm. This analysis should also include a discussion of the practical implications of these limitations, such as the types of real-world applications where the method may not be suitable. This would provide a more balanced view of the proposed method and help to identify areas for future research.

Finally, the paper needs a more detailed analysis of the computational complexity of the proposed algorithms. The authors should provide a breakdown of the time and space complexity of each step in the algorithm, as well as a comparison with the complexity of existing methods. This analysis should include a discussion of the impact of different graph parameters on the complexity, such as the number of nodes, edges, and subgraph size. The authors should also discuss the practical implications of the computational complexity, such as the scalability of the method to large graphs and the feasibility of using the method in real-world applications. This analysis should also include a discussion of the memory requirements of the algorithm, and how these requirements scale with the size of the graph and the subgraph. This would provide a more complete understanding of the practical feasibility of the proposed approach and help to assess its potential for real-world applications.

### Questions

1. How does the proposed approach compare to existing methods for subgraph counting, such as those based on vertex and edge coloring [1] or dynamic programming [2]?
2. What are the limitations of the proposed approach, and in which scenarios is it not effective?
3. What is the computational complexity of the proposed algorithms, and how does it compare to existing methods?

### Rating

6

### Confidence

3

**********
