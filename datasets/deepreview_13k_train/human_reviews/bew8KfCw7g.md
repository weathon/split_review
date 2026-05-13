# CTGC: Cluster-Aware Transformer for Graph Clustering

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Graph clustering is a fundamental unsupervised task in graph mining. However, mainstream clustering methods are built on graph neural networks, thus inevitably suffer from the difficulty in long-range dependencies capturing. Moreover, current two-stage clustering scheme, consisting of representation learning and clustering, limits the ability of the graph encoder to fully exploit task-related information, resulting in suboptimal embeddings. In this work, we propose CTGC ($\textbf{C}$luster-Aware $\textbf{T}$ransformer for $\textbf{G}$raph $\textbf{C}$lustering) to mitigate these issues. Specifically, considering the excellence of transformer in long-range dependencies modeling, we first introduce transformer to graph clustering as the crucial graph encoder. To further enhance the task awareness of encoder during representation learning, we presents two mechanisms: momentum cluster-aware attention and cluster-aware regularization. In momentum cluster-aware attention, previous clustering results are adopted to guide the node embedding production with specially designed cluster-aware queries. Cluster-aware regularization is designed to fuse the cluster information into bordering nodes through minimizing the overlap between different clusters while maximizing the completeness of each cluster. We evaluate our method on seven real-world graph datasets and achieve superior results compared to existing state-of-the-art methods, demonstrating its effectiveness in improving the quality of graph clustering.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Graph clustering faces challenges with long-range dependencies and suboptimal embeddings due to a two-stage approach. CTGC addresses these by integrating transformers for better dependency modeling and introducing mechanisms to enhance task awareness, leading to improved clustering quality on real-world datasets.

### Strengths
1. Nice presentation with clear figures.

2. Technique sound. Lots of experiments are provided.

3. The paper is well-written and organized.

### Weaknesses
1. From my idea, the proposed method seems to integrate Transformer frameworks in node-level clustering, which lacks novelty. Maybe you should emphasize the importance of why you use transformer instead of other frameworks. In other words, the motivation should be more clear.

2. As for the long-range dependencies, I would recommend the authors add case studies to intuitively show that the Transformer framework indeed helps with it, rather than only relying on the performance.

3. Maybe larger datasets should be used for comparison.

4. If possible, I would like to see the performances of the proposed method on graph-level clustering.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents CTGC, a novel approach integrating transformers into graph clustering to effectively capture long-range dependencies. The method enhances representation learning through momentum cluster-aware attention and cluster-aware regularization, resulting in improved clustering performance on seven real-world graph datasets compared to existing SOTAs.

### Strengths
1.  CTGC effectively models long-range dependencies in graph clustering, overcoming the limitations of traditional GNN methods that primarily focus on local node aggregation.

2. The paper includes numerous experiments that validate the effectiveness of the proposed method, providing strong empirical support for its claims.

3. The article is well-structured, making it easy to read and follow, which enhances the understanding of the proposed methods and results.

### Weaknesses
The paper states, “To the best of our knowledge, we are the first to introduce a transformer for graph clustering to alleviate long-range dependency modeling.” However, existing studies have already applied transformers in graph clustering, which questions the novelty of this approach. For example[1],[2]. Including these recent works in the baseline would enhance the credibility of the claims.

### Questions
What is the time complexity of the CTGC algorithm, particularly for the momentum cluster-aware attention and cluster-aware regularization mechanisms? How does it compare to traditional clustering methods?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces an approach to graph clustering by incorporating the transformer architecture, which is particularly excel at capturing long-range dependencies. The authors propose two key mechanisms: momentum cluster-aware attention and cluster-aware regularization, to enhance the model's task awareness during representation learning.

### Strengths
- Alleviating the long-distance dependency problem in graph clustering is a research challenge.
- The paper is written in a very clear and accessible manner.

### Weaknesses
 - The author claims to be the first to introduce the graph transformer, but this statement isn't entirely accurate. Several prior studies[1,2] on graph clustering have likely also incorporated graph transformers.
- How does the transformer's ability to capture long-range dependencies translate to improved clustering performance compared to traditional GNNs, and what theoretical justifications exist for this choice?
- The long-distance dependencies in graph clustering are constrained by the over-smoothing problem. Does the method proposed by the authors effectively address the over-smoothing issue in GNNs?
- Could the authors elaborate on the design choices behind the momentum cluster-aware attention mechanism, and how it contributes to the model's ability to learn more effective representations?
- Given the computational complexity of transformer models, how does the proposed model scale with larger and more complex graphs?
- The authors' method is very similar to [3]. Could you explain the differences between them?

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2
