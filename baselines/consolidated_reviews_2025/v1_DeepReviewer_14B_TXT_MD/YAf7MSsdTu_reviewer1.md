### Summary

The paper studies the problem of learning a local-global shortest path algorithm, which is a two-stage algorithm that first learns to compute shortest path distances between a set of landmark nodes and every other node, and then uses the precomputed distances to approximate all-pairs shortest path distances using triangle inequality. The paper proposes GNN-based algorithms for the first step, and empirically shows that the resulting local-global shortest path algorithm provides a better approximation than the naive implementation of the two-step algorithm.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The problem of approximating shortest path distances is a well-studied problem, and the local-global shortest path algorithm is a natural heuristic for this problem. The paper provides empirical studies to show the effectiveness of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide any theoretical contribution. The only theoretical results are from previous works, and they are only guarantees for the heuristic algorithm but not the GNN-based algorithm proposed in the paper. The use of GNNs to learn some intermediate variables for a downstream optimization problem has become a popular approach in the last decade, and the proposed algorithm is not the first one in the context of all-pairs shortest paths either. Therefore, the empirical studies alone are not sufficient to justify the novelty and significance of the paper.

In experiment 1, the paper shows that GNNs cannot predict shortest path distances accurately. However, it is not clear why this is a surprising or important result. It has been known for a long time that standard GNNs such as GCN, GraphSAGE, and GAT are not capable of predicting shortest path distances even with supervision, and more sophisticated GNN architectures are proposed to address this issue, such as the referenced Rethinking the Power of GNNs in Predicting Shortest Path Distances.

In experiment 2, it is not clear what the proposed GNN-based algorithm is compared with. The paper mentions that "the vanilla lower bound is computed using exact distances to the nodes in the seed sets", but it is not clear how these exact distances are obtained. In addition, the proposed GNN-based algorithm also seems to provide a lower bound, so it is not clear what the proposed algorithm is compared with.

In experiment 3, the proposed GNN-based algorithm is compared with the vanilla algorithm when approximating shortest path distances on real networks, but it is not clear if the GNN-based algorithm is even used in the process. The proposed local-global shortest path algorithm first precomputes the distances between landmark nodes and every other node, so it is possible that experiment 3 only evaluates the ability of a vanilla algorithm to approximate shortest path distances, instead of evaluating the proposed GNN-based algorithm.

### Suggestions

The paper's primary weakness lies in its lack of theoretical justification for the proposed GNN-based approach. While the empirical results may show some practical benefit, the absence of theoretical guarantees significantly limits the contribution. The paper should provide a more rigorous analysis of why the GNN is expected to learn effective local distances, and how these learned distances relate to the true shortest path distances. For example, the authors could investigate the approximation properties of the GNN's learned embeddings, and establish a connection between the embedding space and the shortest path metric. Without such theoretical underpinnings, it is difficult to assess the generalizability and robustness of the proposed method. Furthermore, the paper should clearly articulate the novelty of the proposed approach compared to existing GNN-based methods for all-pairs shortest path approximation. A more detailed comparison with related work, highlighting the specific advantages of the proposed method, is needed to justify its significance.

The experimental setup also needs significant clarification. The description of how the 'vanilla lower bound' is computed is insufficient. The paper should explicitly state whether Dijkstra's algorithm or BFS is used to compute the exact distances to the seed nodes, and why this choice is made. Furthermore, the comparison between the proposed GNN-based algorithm and the vanilla algorithm is unclear. The paper should clarify whether the GNN is used to directly predict the shortest path distances, or to predict the distances to the landmark nodes. If the GNN is used to predict distances to landmark nodes, then the paper should clearly state how these predicted distances are used to approximate the all-pairs shortest path distances. The experimental section should also include a comparison with other GNN-based methods for all-pairs shortest path approximation, to better demonstrate the effectiveness of the proposed approach. The current experimental setup makes it difficult to isolate the contribution of the GNN component.

Finally, the paper should address the limitations of using standard GNNs for predicting shortest path distances. The authors should acknowledge that standard GNNs are known to struggle with this task, and explain why they still choose to use them. If the authors are using standard GNNs as a baseline, this should be explicitly stated. The paper should also discuss the potential benefits of using more sophisticated GNN architectures that have been specifically designed for shortest path prediction. The paper should also clarify whether the GNN is used in experiment 3, and if so, how the precomputed distances are used in the downstream task. The paper should provide a more detailed description of the experimental setup, including the specific parameters used for the GNN, and the training procedure. Without these details, it is difficult to reproduce the results and assess the validity of the proposed method.

### Questions

1. In experiment 1, the paper shows that GNNs cannot predict shortest path distances accurately. However, is this a surprising or important result? It has been known for a long time that standard GNNs such as GCN, GraphSAGE, and GAT are not capable of predicting shortest path distances even with supervision, and more sophisticated GNN architectures are proposed to address this issue, such as the referenced Rethinking the Power of GNNs in Predicting Shortest Path Distances. Why is this observation important, and why do the subsequent experiments train GNNs using the same setting as in experiment 1 instead of using the more sophisticated GNN architectures proposed in the literature?

2. In experiment 2, it is not clear what the proposed GNN-based algorithm is compared with. The paper mentions that "the vanilla lower bound is computed using exact distances to the nodes in the seed sets", but it is not clear how these exact distances are obtained. In addition, the proposed GNN-based algorithm also seems to provide a lower bound, so it is not clear what the proposed algorithm is compared with.

3. In experiment 3, the proposed GNN-based algorithm is compared with the vanilla algorithm when approximating shortest path distances on real networks, but it is not clear if the GNN-based algorithm is even used in the process. The proposed local-global shortest path algorithm first precomputes the distances between landmark nodes and every other node, so it is possible that experiment 3 only evaluates the ability of a vanilla algorithm to approximate shortest path distances, instead of evaluating the proposed GNN-based algorithm.

### Rating

3

### Confidence

4

**********
