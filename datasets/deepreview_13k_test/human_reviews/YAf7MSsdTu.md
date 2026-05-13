# Local-Global Shortest Path Algorithms on Random Graphs, Enhanced with GNNs

- Decision: Reject
- Scores: 8, 6, 1

## Abstract
Graph neural networks (GNNs) using local message passing were recently shown to inherit the intrinsic limitations of local algorithms in solving combinatorial graph optimization problems such as finding shortest distances (Loukas, 2020). To address this issue, Awasthi et al. (2022) proposed architectures based on Bourgain’s (1985) seminal work on Hilbert space embeddings. These architectures enhance local message passing in GNNs with a single global computation, yielding a local-global algorithm. This paper focuses on the average-case analysis of more general local-global algorithms for finding shortest distances (of which GNN+ is a particular case). Our primary contribution is a theoretical analysis of these algorithms on Erdős-Rényi (ER) random graphs. We prove that, on random graphs, these algorithms have lower distortion of shortest distances for most pairs of nodes w.h.p. while requiring a lower embedding dimension. Inspired by Awasthi et al. (2022), and to automate local computations and improve computational efficiency in practical scenarios, we further propose a modification to these algorithms that incorporates GNNs in the local computation phase. Empirical results on ER graphs and benchmark graph datasets demonstrate the enhanced performance of the GNN-augmented algorithm over the traditional approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper analyzes hybrid algorithms that combine local and global approaches to solve shortest path problems on graphs, especially focusing on Erdős-Rényi random graphs. By adding Graph Neural Networks (GNNs) into the local phase, the algorithm becomes faster and more scalable for big graph networks. Through theoretical analysis on Erdős-Rényi random graphs, the authors show that their method provides tight distance estimates for most node pairs. Experiments on both synthetic and real-world graphs highlight the improved performance of the GNN-enhanced approach.

### Strengths
The paper introduces an innovative hybrid algorithm for shortest path approximation on random graphs that uses the locality of GNNs and the global approximation bounds provided by Bourgain's theorem.

### Weaknesses
Although inspired by Awasthi et al.'s framework, there isn’t a direct comparison of results, such as accuracy or runtime metrics. The proof sections are a bit difficult to follow, especially for people without a sound background in this field. A detailed table introducing all the variables introduced in the algorithms and proofs would help to understand them easily.

### Questions
1. How does this method perform on large-scale networks with millions of nodes, like social or biological networks? SNAP dataset collection of Stanford University has some very large social network datasets.
2. How does the GNN-based approach handle real-world sparse networks where long-range dependencies are more challenging? Could alternative GNN architectures improve performance in such cases?
3. Could the approach be adapted to handle other graph structures (like protein graphs) effectively?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the limitations of local message passing in GNNs for solving shortest path problems in graphs. Building on prior research by Awasthi et al. (2022), the authors conduct a theoretical analysis of local-global algorithms applied to Erdős-Rényi (ER) random graphs, demonstrating that these algorithms can achieve improved accuracy in estimating shortest distances with reduced distortion and embedding dimensions. They propose an enhancement that integrates GNNs into the local computation phase to boost efficiency. Empirical results confirm that the GNN-augmented algorithms significantly outperform traditional methods on both ER graphs and benchmark datasets, highlighting their applicability in real-world scenarios, such as social networks. Overall, this work advances the understanding of effective strategies for shortest path computation in complex networks.

### Strengths
1. The paper presents a novel integration of GNNs into existing local-global algorithms for shortest path computation. This combination of traditional algorithms with modern neural approaches is timely and relevant, particularly as GNNs gain traction in graph-related problems.

2. The methodology is well-defined, with a clear explanation of the algorithmic framework. The theoretical analysis provided adds rigor to the claims, showing a strong foundation for the proposed enhancements.

3. The writing is generally clear and well-structured, allowing readers to follow the development of ideas easily.

### Weaknesses
1. While the authors claim superior performance, there is limited comparative analysis with other shortest-path based GNN approaches [1, 2, 3]. A more detailed benchmarking against established methods could validate the claims and provide a clearer context for the contributions.

2. The theoretical analysis is strong but could be expanded to cover edge cases or graph types beyond Erdős-Rényi. This would enhance the generalizability of the findings and provide deeper insights into the algorithm’s performance.

3. More detailed information / empirical study on the computational complexity and memory requirements of the proposed method would be beneficial.

References:

[1] Shouheng et al., Local Vertex Colouring Graph Neural Networks, ICML 2023.

[2] Bohang et al., Rethinking the Expressive Power of GNNs via Graph Biconnectivity, ICLR 2023.

[3] Petar et al., Neural Execution of Graph Algorithms, ICLR 2020.

### Questions
1. Could you elaborate on the specific architectural choices made for the GNNs? How do these choices influence their performance when transferred to larger graphs?

2. What criteria were used to evaluate the transferability of GNNs across varying graph sizes? Were there instances where transferability was not achieved?

3. Could you elaborate on how your GNN-enhanced approach stacks up against other leading algorithms in terms of efficiency and accuracy? A detailed comparison would help clarify the unique contributions of your work.

4. How do your theoretical bounds perform under various graph distributions beyond the Erdős-Rényi model?

5. In the experiments section, authors mention a notable performance increase when the GNN is trained on graphs with 200 nodes for the larger $n^{′}$-node graph. What are the practical implications of this finding, especially when graph sizes vary widely?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper addresses the shortest-path distance problem using a machine learning approach. The authors employ a local-global algorithm to approximate shortest-path distances, analyzing the lower and upper bound distortions of these approximations on Erdős–Rényi (ER) random graphs. They propose using a GNN to implement the local step of the algorithm. Experimental results are reported on ER graphs and two social network datasets.

### Strengths
**Originality** 

The concept of the local-global algorithm is largely drawn from existing work, and using GNNs to implement the local step does not introduce much new insights. The main contribution of this paper lies in the analysis of lower and upper bound distortions on Erdős–Rényi random graphs.

**Quality**

I have concerns about the proposed method, as it appears to be effective only on small graphs, even when computing approximate distances. This limitation raises questions about its scalability and practical applicability to larger networks.

**Clarity**

The presentation could benefit from improvements in several areas. For instance, the research problem (tackling the shortest-path distance problem using machine learning) lacks clear motivation. The transferability of the GNN from small graphs to large graphs is not adequately justified. The experiments are limited, and the results are not thoroughly explained.


**Significance**

The paper overlooks a substantial body of literature (e.g., [1,2,3,4]) on fast and scalable shortest-path algorithms that can compute exact shortest-path distances on large networks (with millions or even billions of nodes) within milliseconds per query, and in some cases, even microseconds for specific network types like road networks. Given these existing solutions, the significance of this work is questionable.

References:

[1] Fast Exact Shortest-Path Distance Queries on Large Networks by Pruned Landmark Labeling, Akiba et al. SIGMOD 2012

[2] Fully Dynamic Shortest-Path Distance Query Acceleration on Massive Networks, Hayashi et al. CIKM 2016

[3] A Highly Scalable Labelling Approach for Exact Distance Queries in Complex Networks, Farhan, et al., EDBT 2019

[4] When Hierarchy Meets 2-Hop-Labeling: Efficient Shortest Distance Queries on Road Networks, Quyang, SIGMOD 2018

### Weaknesses
W1: The research problem may need to be revisited or reconsidered. The authors argue that “modern networks often consist of billions of nodes, and global algorithms take hours to be implemented, whereas approximate solutions are typically needed with ultra-low latency.” However, this claim lacks citations or sources of information. Can the authors provide specific citations supporting the claim about computational challenges on very large networks? In recent literature on shortest-path distance algorithms, for complex networks with billions of nodes, it often takes only a couple of hours to build an index, with exact shortest-path distance queries completing in under one microsecond [1].  To better justify the need for an approximate method, I would suggest a comparison with existing efficient exact algorithms. 


W2: The proposed method is primarily analyzed and evaluated based on Erdős–Rényi (ER) random graphs. However, it is well known that shortest-path distance problems on different graph structures may require different algorithmic designs. For instance, road networks typically have low node degrees, while social networks often have a dense core, leading to significantly different design choices. Therefore, the results on ER random graphs have limited applicability in practice.

W3: The design of the GNN appears to follow the basic principles of message passing within a local neighborhood. However, it is unclear how long-distances would be managed if the GNN depth is small. Conversely, increasing the GNN depth could lead to the oversmoothing problem. Also, since the shortest-path distance problem is to calculate the number of edges in the shortest path between two vertices, it is unclear how the node features contribute meaningfully in this context. Providing examples or intuitive explanations would help clarify this aspect. Finally, the rationale behind the transferability of the model is not well-justified in this setting and would benefit from further clarification.

W4: The experiments do not align with the stated motivation of the work, which criticizes traditional approaches for the high computational cost of shortest-path calculations. Most experiments are conducted on Erdős–Rényi graphs with sizes ranging from just 25 nodes to 3200 nodes, which fails to demonstrate the scalability of the proposed method on large networks. In Figure 2, even on a small graph with 50 nodes, the GNN performs poorly in predicting distances when the distances are larger, which raises concerns about its effectiveness. In Figures 4(b)–(c), why the MSE of BFS remains flat as n increases from 25 to 3200, whereas in Figure 3, the MSE of BFS increases with n? 

There are various real-world graphs and networks commonly used by researchers to benchmark shortest-path distance algorithms (e.g., [1,2,3,4]), such as road networks with sizes up to 24 million nodes and complex networks (including social networks) ranging from 1 million to 2 billion nodes. However, the paper only benchmarks on small ER graphs and two small real world social networks against the BFS algorithm. It would be more informative to compare the proposed method with state-of-the-art shortest-path algorithms on these larger, real-world datasets to better assess its effectiveness and scalability.

### Questions
See the questions in "Weaknesses"

### Soundness
2

### Presentation
2

### Contribution
1
