### Summary

This paper studies the subgraph counting/canonical labeling problem in graph learning. It is proved that GNNs can count subgraphs under certain conditions. The paper also develops a dynamic programming algorithm for the subgraph isomorphism problem on trees and shows that GNNs can efficiently simulate the algorithm.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and well-organized. The authors provide a theoretical understanding of the subgraph counting problem in graph learning. The paper also develops a dynamic programming algorithm for the subgraph isomorphism problem on trees and shows that GNNs can efficiently simulate the algorithm.

### Weaknesses

#### Some Related Works

[1] Subgraph Recognition by Relational WeisfeilerLeman.
[2] Subgraph Recognition by ROLAP.
[3] Subgraph recognition by WL algorithms is also useful for subgraph counting.

#### comment

1. The motivation of this paper is not clear. The authors mention that GNNs are unable to count subgraphs, and many real-world graph datasets satisfy the sufficient conditions of the point (1) in Theorem 2. However, the authors do not explain why counting subgraphs is important for graph learning. The authors should provide more motivations for counting subgraphs.

2. The contribution of this paper is limited. The results in Theorem 2 and Theorem 3 are trivial. Theorem 2 is a direct corollary of the color-coding algorithm and the 1-WL algorithm, and Theorem 3 is a direct corollary of the dynamic programming algorithm and the expressivity of GNNs. The authors should clarify the novelty of these theorems.

3. The authors claim that many real-world graph datasets satisfy the sufficient conditions of the point (1) in Theorem 2. However, the authors do not provide any references or experimental results to support this claim. The authors should provide more evidence to support this claim.

4. The authors claim that GNNs can count subgraphs, but the authors do not provide any experimental results to support this claim. The authors should provide experimental results to support this claim.

5. The authors claim that GNNs can simulate the dynamic programming algorithm for the subgraph isomorphism problem on trees. However, the authors do not provide any experimental results to support this claim. The authors should provide experimental results to support this claim.

6. The authors should compare their results with previous works [1,2,3]. The authors should clarify the novelty of their results compared with previous works.

### Suggestions

The paper's core weakness lies in its unclear motivation and limited empirical validation. While the theoretical results are presented, their practical significance and novelty are not sufficiently justified. The authors need to articulate more clearly why subgraph counting is a crucial task in graph learning, beyond simply stating that GNNs are unable to do it. For instance, they could discuss specific applications where accurate subgraph counting is essential, such as identifying functional groups in molecules or detecting specific patterns in social networks. Furthermore, the paper should provide a more detailed explanation of how the theoretical results translate into practical advantages. For example, how does the ability of GNNs to count subgraphs under certain conditions lead to better performance in downstream tasks? The authors should also clarify the limitations of their approach and discuss scenarios where their results might not hold.

To address the limited contribution concern, the authors should more clearly delineate the novelty of their theorems. While it's true that Theorem 3 is related to the expressivity of GNNs, the authors should emphasize the specific conditions under which their results hold and how these conditions differ from existing results. For example, they should explicitly state how their sufficient conditions for subgraph counting are different from the conditions required by the color-coding algorithm and the 1-WL algorithm. Similarly, for Theorem 3, they should highlight the specific aspects of their dynamic programming algorithm that allow GNNs to efficiently simulate it, and how this differs from existing simulations. The authors should also provide a more detailed comparison with existing dynamic programming algorithms for subgraph isomorphism, and explain why their approach is more suitable for GNNs. The paper should also include a more thorough discussion of the limitations of their approach and the potential for future work.

Finally, the lack of experimental results is a major concern. The authors should provide empirical evidence to support their theoretical claims. For example, they could conduct experiments on benchmark datasets for subgraph counting or canonical labeling, and compare the performance of GNNs with other methods. These experiments should be designed to specifically test the conditions under which their theorems hold. The authors should also provide experimental results to support their claim that GNNs can simulate the dynamic programming algorithm for the subgraph isomorphism problem on trees. The experimental results should be presented in a clear and concise manner, with appropriate statistical analysis to validate the findings. The authors should also compare their results with previous works [1,2,3] and clearly articulate the novelty of their contributions in the context of existing literature.

### Questions

Please see the weaknesses.

### Rating

3

### Confidence

4

**********
