# ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
We present \shortname, a novel graph transformer architecture that achieves linear complexity through an efficient reassignment technique between nodes and virtual nodes. Graph transformers have become increasingly important in graph learning for their ability to utilize long-range node communication explicitly, addressing limitations such as oversmoothing and oversquashing found in message-passing graph networks. However, their dense attention mechanism scales quadratically with the number of nodes, limiting their applicability to large-scale graphs.
\shortname draws inspiration from the airline industry's hub-and-spoke model, where flights are  assigned to optimize operational efficiency. In our approach, graph nodes (spokes) are dynamically reassigned to a fixed number of virtual nodes (hubs) at each model layer. Recent work, Neural Atoms~\citep{li2024neural}, has demonstrated impressive and consistent improvements over GNN baselines by utilizing such virtual nodes; their findings suggest that the number of hubs strongly influences performance. However, increasing the number of hubs typically raises complexity, requiring a trade-off to maintain linear complexity.
Our key insight is that each node only needs to interact with a small subset of hubs to achieve linear complexity, even when the total number of hubs is large. To leverage all hubs without incurring additional computational costs, we propose a simple yet effective adaptive reassignment technique based on hub-hub similarity scores, eliminating the need for expensive node-hub computations.
Our experiments on long-range graph benchmarks indicate a consistent improvement in results over the base method, Neural Atoms, while maintaining a linear complexity instead of $O(n^{3/2})$. Remarkably, our sparse model achieves performance on par with its non-sparse counterpart. Furthermore, \shortname outperforms competitive baselines and consistently ranks among the top performers across various benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents ReHub, an improved graph transformer that leverages dynamic hub reassignment to achieve linear complexity.

### Strengths
- The proposed method is simple
- Experimental results demonstrate that ReHub consistently achieves higher accuracy than existing SOTA methods.

### Weaknesses
Major:
- This paper highlights linear complexity of the proposed algorithm, but the experimental efficiency comparison is missing. Specifically, the paper lacks a direct comparison of wall-clock time or throughput against existing methods, making it difficult to assess the practical speedup achieved by the claimed linear complexity. The memory usage comparison is also not comprehensive; it should include a breakdown of memory usage for different components of the model, such as the attention mechanism and the hub assignment process.
- Convergence comparison is missing. ReHub achieves higher accuracy, but it's not clear whether ReHub needs more iterations to converge. The paper should include a convergence plot showing the training loss and validation accuracy over training epochs for ReHub and the baselines, which is critical to understand the training dynamics and efficiency of the proposed method.
- The datasets used in experiments are too small. The largest graph only contains 169K nodes. This raises concerns about the scalability of the proposed method to larger, real-world graphs. The experimental evaluation should include datasets with millions or billions of nodes to demonstrate the practical applicability of the linear complexity claim.

Minor:
- It would be better if the authors can visualize the hub assignment to see if the proposed method generates meaningful pattern.

### Questions
Please address weaknesses mentioned above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
ReHub is a scalable graph transformer that achieves linear complexity through adaptive spoke-hub reassignment, drawing inspiration from hub-based systems like airlines. By assigning nodes to a limited number of virtual "hubs" and using efficient hub-hub similarity for reassignment, ReHub maintains global attention without high computational costs. Experiments show it outperforms baselines and maintains sparse model performance comparable to dense architectures on long-range benchmarks.

### Strengths
- The paper is clearly written and easy to follow.
- The proposed architecture is well-motivated.
- Spokes and Hub is a plausible algorithm for graph learning.

### Weaknesses
While the proposed method is intriguing, the experimental evaluation lacks comprehensiveness. Several key recent baselines are missing, which undermines the validity of the results. The authors aim to reduce the complexity of self-attention-based graph transformers, yet they only test on a single large dataset, **ogbn-arxiv**. On this dataset, the proposed model does not outperform the vanilla **GraphSAGE** model, which is not even included in the baseline comparisons.

In **Table 1**, crucial baselines such as **Graph-ViT/MLP-Mixer** [1] and **GRIT** [2] are absent, both of which achieve significantly higher performance than the highlighted metrics. Additionally, **GECO** [3], a graph learning model based on SSMs, outperforms the presented method across datasets in **Tables 1-3**, including **ogbn-arxiv**, with significant margins. 

The results in **Table 3** are not compelling due to the absence of proper GNN and GT baselines. The proposed model is designed to reduce the quadratic complexity of Graph Transformers with respect to the number of nodes \( N \) in the graph. However, aside from **ogbn-arxiv**, all other datasets have very small \( N \) values, as **Tables 1 and 2** focus on graph-level tasks. Notably, the performance on **ogbn-arxiv** is unimpressive, failing to surpass vanilla **GCN** or **GraphSAGE** models, which themselves are outperformed by **Exphormer**. Yet, **GraphSAGE** and **GCN** are missing from the evaluation.

Since this paper’s motivation is to reduce the complexity of Graph Transformers, evaluating on large-node prediction datasets is crucial to demonstrate the effectiveness of the proposed method. However, the current experiments lack both comprehensiveness and compelling experimental evidence.

Even on the smaller datasets in **Tables 1 and 2**, the results are underwhelming, with many recent baselines absent. These missing baselines include **SGFormer** [4], **Polynormer** [5], and possibly others, suggesting a need for a more extensive literature review.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ReHub, a novel graph transformer architecture with linear computational complexity. The architecture leverages an adaptive hub-spoke reassignment strategy. Nodes (spokes) are connected to a subset of virtual nodes (hubs) with a deliberately chosen size to optimize long-range communication and maintain efficiency. Through experiments on LRGB and large graph benchmarks, ReHub demonstrates comparable or better performance than existing methods with reduced memory consumption.

### Strengths
1. The method demonstrates wide applicability to various graph tasks with a minor modification of the prediction head in architecture.

2. The evaluation section covers various datasets and baseline methods to provide comprehensive results on enhanced long-range information capturing ability over existing methods.

3. The writing and presentation is clear and easy to follow.

### Weaknesses
1. The motivation is intuitive: from the spoke-to-hub transportation model, the motivation of such structure is somewhat insufficient. The Hub Reassignment motivation and strategy are intuitively explained, with little further support.

2. In the evaluation of complexity, only (peak) memory consumption is compared with other models to empirically show the low memory complexity, while the claim is that both time and memory complexity are constrained. The empirical results of time complexity remains to be discussed on real-world datasets.

3. The two large graph benchmarks in experiment section seem to still fall within small to medium-sized graphs according to OGB benchmark [Ref.1]. The peak memory consumption of previous method Exphormer on these datasets is only 2~3 GBs. The comparison of memory consumption on these small datasets cannot truly demonstrate the advancement of ReHub because memory is not a bottleneck on these datasets.

### Questions
1. In 3.4 (5) Hub (Re)Assignment, why should every spoke utilize all available hubs? It makes sense in transportation domain to balance the load, but it is not well motivated here.

2. From complexity perspective, only peak memory is evaluated to demonstrate that ReHub is memory efficient. With the multi-layer network consisting of message passing, attention and reassignment, is ReHub also empirically computation efficient compared to other methods?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
GNN is considered an important approach for extensively uncovering and analyzing the intrinsic relational information across various scenarios. However, the rapid expansion of neighborhood space limits its effectiveness. For a long time, many efforts have been made in this area, such as sampling techniques. In the past year or two, the method of introducing virtual nodes has emerged. This paper follows this basic approach and proposes “ReHub,” coining new terms “Spokes” and “Hubs”,  corresponding to graph nodes and virtual nodes, respectively. Furthermore, it dynamically assigns graph nodes to the corresponding virtual nodes. Drawing an analogy to a transportation hub system, for each graph node (termed a “Spoke” in the paper), a fixed-size, interconnected set of virtual nodes, termed a “Hub” by the authors, is assigned. To effectively manage the allocation and reduce overhead, an adaptive reallocation mechanism is employed, as well as hub-to-hub similarity. Overall, this work is seen as transforming one complex problem into another.

### Strengths
1. The method is intuitive and easy to understand. It leverages the general observation that each node only needs to interact with a small subset of hubs, enabling the model to maintain linear complexity even as the total number of hubs increases significantly.

2. Accordingly, a key component of ReHub’s architecture is the long-range spoke update layer, which utilizes both the spoke graph and the connections between spokes and hubs.

3. This structure achieves near-linear complexity, preventing rapid expansion of the state space within the graph structure and thereby reducing memory usage and other computational costs.

### Weaknesses
1. Overall, this work is seen as transforming one complex problem into another without addressing a fundamental solution to the original issue. The challenge lies in determining the relationship between a node and a hub, as well as the relationships between hubs that connect sets of nodes. The difficulty is not merely in establishing this two-tier relationship but in effectively defining these associations for different types of graphs. Moreover, this structure could potentially be extended to three layers or even more.

2. The paper initiates ReHub by creating  N_h = r \sqrt{N_s}  hubs, where r, the hub-ratio, is set to 1 in most benchmarks. However, this approach lacks a necessary theoretical foundation, raising concerns about its universality. It appears to be more of an empirical method rather than one grounded in rigorous theoretical principles.

3. The testing workloads are quite targeted, focusing on evaluating ReHub’s (1) long-range communication capabilities and (2) memory efficiency on large graphs. Since graph structures in GNNs vary widely, determining whether a particular graph type is well-suited to this approach may also be an open question.

### Questions
1. How does the method proposed in this paper differ from the approach of dividing a graph into clusters and finding a central node within each cluster? Although the initial stage of the method in this paper also utilizes basic clustering for classification.

2. r  and  k  are two important hyperparameters;  r  determines the number of hubs, while  k  dictates the number of connections between spokes and hubs. The appendix also analyzes the impact of these two hyperparameters. The question is whether there is a universal method for determining these hyperparameters.

3. Why is there no comparison with clustering methods and sampling methods in the experimental section? Essentially, these methods also analyze the graph as individual subgraphs (or virtual subgraphs), establishing parameter relationships within and between the subgraphs through training.

### Soundness
2

### Presentation
3

### Contribution
2
