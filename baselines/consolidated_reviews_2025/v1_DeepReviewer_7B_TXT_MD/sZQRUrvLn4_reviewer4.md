### Summary

This paper studies the subgraph counting problem on graphs. It provides a theoretical explanation of the empirical success of GNNs in this task, bridging the gap between theory and practice. The authors show that GNNs can efficiently simulate dynamic programming algorithms for subgraph counting tasks, particularly for tree patterns. They also introduce novel algorithms for solving the subgraph isomorphism problem on trees and demonstrate that GNNs can efficiently simulate these algorithms. The paper provides empirical validation of the theoretical findings on real-world datasets, showing that GNNs perform well on subgraph counting tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical explanation for the empirical success of GNNs in subgraph counting tasks, which is a novel and important contribution to the field. It bridges the gap between theory and practice by showing that GNNs can efficiently simulate dynamic programming algorithms for subgraph counting tasks.

2. The paper introduces novel algorithms for solving the subgraph isomorphism problem on trees and demonstrates that GNNs can efficiently simulate these algorithms. This is a significant contribution to the field of graph learning.

3. The paper provides empirical validation of the theoretical findings on real-world datasets, showing that GNNs perform well on subgraph counting tasks. This is an important contribution to the field of graph learning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on subgraph counting on graphs, which is a special case of the substructure counting problem. The authors should discuss the relationship between the subgraph counting problem and the substructure counting problem. Specifically, the paper should clarify how the proposed GNN-based approach would extend to more general substructure counting problems, such as counting specific graph motifs or induced subgraphs, and whether the local distinguishability condition would still hold or need to be adapted. The current analysis is limited to subgraphs, and it is unclear how the results would generalize to other substructure counting tasks.

2. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on hypergraphs. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on hypergraphs. The paper should address how the proposed GNN-based approach could be extended to handle hypergraphs, and what modifications to the GNN architecture or training procedure would be necessary to achieve this. Furthermore, the computational complexity of extending the proposed approach to hypergraphs should be discussed, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

3. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on simplicial complexes. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on simplicial complexes. The paper should clarify how the proposed approach could be extended to handle simplicial complexes, and what modifications to the GNN architecture or training procedure would be necessary to achieve this. The paper should also discuss the computational complexity of extending the proposed approach to simplicial complexes, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

4. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on topological spaces. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on topological spaces. The paper should address how the proposed GNN-based approach could be extended to handle topological spaces, and what modifications to the GNN architecture or training procedure would be necessary to achieve this. Furthermore, the computational complexity of extending the proposed approach to topological spaces should be discussed, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

5. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on geometric graphs. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on geometric graphs. The paper should clarify how the proposed approach would extend to geometric graphs, and whether the local distinguishability condition would still hold or need to be adapted. The paper should also discuss the computational complexity of extending the proposed approach to geometric graphs, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

6. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on spatial networks. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on spatial networks. The paper should address how the proposed GNN-based approach could be extended to handle spatial networks, and what modifications to the GNN architecture or training procedure would be necessary to achieve this. Furthermore, the computational complexity of extending the proposed approach to spatial networks should be discussed, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

7. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on networks. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on networks. The paper should clarify how the proposed approach would extend to networks, and whether the local distinguishability condition would still hold or need to be adapted. The paper should also discuss the computational complexity of extending the proposed approach to networks, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

8. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on graphs with attributes. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on graphs with attributes. The paper should address how the proposed GNN-based approach could be extended to handle graphs with attributes, and what modifications to the GNN architecture or training procedure would be necessary to achieve this. Furthermore, the computational complexity of extending the proposed approach to graphs with attributes should be discussed, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

9. The paper only considers the subgraph counting problem on graphs, which is a special case of the subgraph counting problem on attributed graphs. The authors should discuss the relationship between the subgraph counting problem on graphs and the subgraph counting problem on attributed graphs. The paper should clarify how the proposed approach would extend to attributed graphs, and whether the local distinguishability condition would still hold or need to be adapted. The paper should also discuss the computational complexity of extending the proposed approach to attributed graphs, and whether the local distinguishability condition would still be a sufficient criterion for efficient subgraph counting in this more general setting.

### Suggestions

The paper's focus on subgraph counting on graphs, while providing a solid theoretical foundation, limits its applicability to a broader range of graph-related problems. To enhance the paper's impact, the authors should explore the extension of their theoretical framework to more complex graph structures, such as hypergraphs, simplicial complexes, topological spaces, geometric graphs, spatial networks, networks, graphs with attributes, and attributed graphs. For each of these extensions, the authors should discuss the necessary modifications to their theoretical analysis, particularly regarding the local distinguishability condition. For instance, in the case of hypergraphs, the notion of local distinguishability might need to be redefined to account for the higher-order relationships between nodes and hyperedges. Similarly, for simplicial complexes, the analysis should consider the topological properties of the complexes. The authors should also discuss the computational complexity of extending their approach to these more complex structures and whether the local distinguishability condition remains a sufficient criterion for efficient subgraph counting in these settings. This would significantly broaden the scope and impact of the paper, making it more relevant to a wider range of real-world applications.

Furthermore, the paper should provide a more detailed discussion on the practical implications of the theoretical results. While the authors demonstrate that GNNs can count subgraphs under certain conditions, they should also discuss how these conditions can be verified in practice. For example, how can one determine whether a given graph pattern satisfies the local distinguishability condition? The authors could explore the use of graph kernels or other graph similarity measures to assess the distinguishability of subgraphs. Additionally, the authors should provide empirical evidence to support their theoretical claims. While the paper includes some experimental results, these are limited to molecular datasets. The authors should conduct more extensive experiments on a wider range of datasets, including synthetic datasets designed to test the limits of their theoretical framework. These experiments should focus on evaluating the performance of GNNs on subgraph counting tasks under different conditions, such as varying graph sizes, pattern complexities, and levels of local distinguishability. This would provide a more comprehensive understanding of the practical applicability of the proposed approach.

Finally, the paper should address the limitations of the proposed approach and discuss potential avenues for future research. For example, the authors could explore the use of more expressive GNN architectures, such as graph transformers, to improve the performance of subgraph counting. They could also investigate the use of different training strategies, such as contrastive learning, to enhance the ability of GNNs to learn subgraph patterns. Furthermore, the authors should discuss the potential impact of noise and uncertainty in real-world graph data on the performance of their approach. Addressing these limitations and exploring future research directions would further strengthen the paper and contribute to the advancement of the field.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
