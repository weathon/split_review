### Summary

The paper proposes a framework to improve message passing neural networks (MPNNs). The proposed framework, Curvature-Constrained Message Passing (CCMP), is based on the edge curvature. CCMP can be applied to any MPNN architecture. CCMP tries to solve the oversquashing problem that occurs in MPNNs. Oversquashing occurs when there is a large difference in the number of nodes between the input set and the output set of a message passing function. The paper is set out as follows. First, the relationship between oversquashing and edge curvature is explained. Next, a new homophily measure is proposed that takes into account the edge curvature. Then, the method CCMP is explained in detail. Finally, the results of the experiments are presented. The results show that CCMP performs better than existing graph rewiring methods on several node classification tasks.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to improve MPNNs. CCMP is a framework that can be applied to any MPNN architecture. CCMP is based on edge curvature. The use of edge curvature to improve MPNNs is a new idea.
- CCMP shows good performance on several node classification tasks. CCMP outperforms existing graph rewiring methods on several datasets.
- The paper is easy to read.

### Weaknesses

#### Some Related Works

[1] A tutorial on oversquashing in gnns
[2] How does oversquashing affect graph neural networks?
[3] The expressive power of labeled and deep graph convolutional networks

#### comment

 - The paper does not mention the computational complexity of CCMP. It would be useful to know how the computational complexity of CCMP compares to existing methods.
- The paper does not discuss the limitations of CCMP. It would be useful to know the limitations of CCMP.
- The paper does not compare CCMP to other methods that are not based on graph rewiring. It would be useful to compare CCMP to other methods that are not based on graph rewiring, such as [1], [2], and [3].
- The paper does not provide any theoretical analysis of CCMP. It would be useful to provide some theoretical analysis of CCMP, such as an analysis of its expressive power or its convergence properties.

### Suggestions

The paper should include a detailed analysis of the computational complexity of CCMP, particularly in comparison to existing graph rewiring methods. This analysis should consider both time and space complexity, and should account for the cost of calculating edge curvature, which can be computationally expensive, especially for large graphs. For example, the paper could analyze the number of operations required to compute the curvature for each edge and how this scales with the size of the graph. Furthermore, the paper should discuss the practical implications of this complexity, such as the maximum graph size that can be handled efficiently. It would also be beneficial to explore potential optimizations or approximations to reduce the computational burden of curvature calculation, such as using sparse matrix representations or sampling techniques.

The paper should also provide a thorough discussion of the limitations of CCMP. This discussion should go beyond simply stating that the method has limitations and should instead identify specific scenarios where CCMP might not perform well. For example, the paper could discuss how CCMP might be affected by noisy or incomplete graph data, or by graphs with specific structural properties. It would also be useful to explore the sensitivity of CCMP to the choice of curvature measure and the parameters of the method. Furthermore, the paper should discuss the potential for overfitting when using CCMP, and how this can be mitigated. A clear understanding of these limitations is crucial for the practical application of CCMP and for guiding future research.

Finally, the paper should include a comparison of CCMP to methods that are not based on graph rewiring, such as those mentioned in the original review [1,2,3]. This comparison should not only focus on empirical performance but also on the theoretical properties of these methods. For example, the paper could compare the expressive power of CCMP to that of other methods, such as those based on spectral graph theory or higher-order message passing. It would also be useful to discuss the convergence properties of CCMP and how they compare to those of other methods. This comparison should provide a more comprehensive understanding of the strengths and weaknesses of CCMP and its place within the broader landscape of graph neural network research.

### Questions

- How does the computational complexity of CCMP compare to existing methods?
- What are the limitations of CCMP?
- How does CCMP compare to other methods that are not based on graph rewiring?
- Can you provide any theoretical analysis of CCMP?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
