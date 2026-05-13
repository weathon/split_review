# Monophilic Neighbourhood Transformers

- Decision: Reject
- Scores: 5, 8, 5

## Abstract
Graph neural networks (GNNs) have seen widespread application across diverse fields, including social network analysis, chemical research, and computer vision.
Nevertheless, their efficacy is compromised by an inherent reliance on the homophily assumption, which posits that adjacent nodes should exhibit relevance or similarity.
This assumption becomes a limitation when dealing with heterophilic graphs, where it is more common for dissimilar nodes to be connected.
Addressing this challenge, recent research indicates that real-world graphs generally exhibit monophily, a characteristic where a node tends to be related to the neighbours of its neighbours.
Inspired by this insight, we introduce Neighbourhood Transformers (NT), a novel approach that employs self-attention within every neighbourhood of the graph to generate informative messages for the nodes within, as opposed to the central node in conventional GNN frameworks.
We develop a neighbourhood partitioning strategy equipped with switchable attentions, significantly reducing space consumption by over 95\% and time consumption by up to 92.67\% in NT.
Experimental results on node classification tasks across 5 heterophilic and 5 homophilic graphs demonstrate that NT outperforms current state-of-the-art methods, showcasing their expressiveness and adaptability to different graph types.
The code for this study is available at https://anonymous.4open.science/r/MoNT-BD3C .

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a neighborhood transformer approach to encode the monophily characteristic, which has been shown to be crucial to handle heterophilic graphs. With transformer applied to the neighborhood of all nodes, a neighborhood partitioning algorithm is designed to reduce the memory footprint of the quadratic transformer costs. Experiments show the better performance on both homophilic and heterophilic graphs than the GNN-based approaches.

### Strengths
1. The proposed method is designed to encapsulate the monophilic property of the graph benchmarks by neighborhood transformer, which shows good improvements compared to the GNN-based approaches.
2. The efficiency and memory footprint of the proposed model are further optimized by leveraging linear transformer (i.e., Performer) and designing neighborhood partitioning algorithms based on neighborhood size and area.

### Weaknesses
1. The neighborhood transformer is not quite scalable to handle large-scale graphs given the fact that it requires to apply transformers to the neighborhood of all nodes. Despite the partitioning algorithms, the computations are still intense. The partitioning algorithm, while reducing memory, still necessitates processing all neighborhoods, which limits scalability to very large graphs. The computational cost of applying transformers to each neighborhood, even with partitioning, remains a significant bottleneck, especially when considering the quadratic complexity of standard attention mechanisms within the transformer.
2. There exist a lot of efficient graph transformers which can handle million-scale graphs, which perform well even on heterophilic graphs, e.g., NAGphormer, VCR-Graphormer etc.
   - From the scalability perspective, the proposed approach was only tested on the graphs with 40k node at most which is not sufficient to demonstrate the optimization from its partitioning algorithms. The experiments do not adequately demonstrate the scalability of the proposed method. Testing on graphs with only 40k nodes is insufficient to validate the effectiveness of the partitioning algorithm for large-scale graphs. The paper needs to show results on much larger graphs to prove the utility of the partitioning strategy.
   - From the evaluation perspective, the paper does not compare with any graph transformer baselines which have been shown to be the SOTA on quite a few benchmarks. The lack of comparison with state-of-the-art graph transformers is a significant oversight. The paper should include a comparison with models like GraphGPS, which have demonstrated strong performance on both homophilic and heterophilic graphs.
3. Equations 1~3 should be reversed to correctly show the computation orders step-by-step. 
4. Technically, the novelty and soundness of this work is insufficient. To me, the major contribution is the partitioning algorithm which does not seem to be quite neat. E.g., for the size based partitioning, how is the p determined? For the area based partitioning, what are the pros and cons compared to those classic graph partitioning algorithms (e.g., METIS) and sparsification algorithms? The partitioning algorithm, while a practical contribution, lacks a strong theoretical foundation. The paper does not adequately justify the choice of size-based and area-based partitioning over existing graph partitioning methods like METIS, or sparsification techniques. The lack of a clear rationale for the proposed partitioning method weakens the overall contribution.

### Questions
1. For the size based partitioning, how is the p determined?
2. For the area based partitioning, what are the pros and cons compared to those classic graph partitioning algorithms (e.g., METIS) and sparsification algorithms?
3. Does the proposed approach perform better than the SOTA graph transformers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Neighbourhood Transformers (NT), a new model to leverage the monophily for graph learning. NT uses self-attention to share information among nodes and collect data from their broader neighborhoods, focusing on nodes more similar to their 2-hop connections. Besides, NT addresses the problem of high memory and time demands due to different neighborhood sizes.

### Strengths
-The introduction of Neighbourhood Transformers (NT) based on the monophily assumption can be viewed as a contribution to graph learning, and its capacity for expansion appears to be advantageous .

-The paper is generally structured clearly and well-written. 

-Experimental results show that the proposed model has comparable or improved performance.

### Weaknesses
 -It is recommended to discuss related work focusing on monophily.

-Some aspects of the experimental analysis lack depth. For instance, it is observed that the performance improvement of NT on homophilic graphs is not as significant as on heterogeneous graphs, yet no in-depth analysis is provided.

### Questions
-Since linear attention part in NT is inspired by existing work, is there has any limitations of the linear attention mechanism , and how might these affect the model's performance? Are there specific scenarios where linear attention might fall short compared to traditional self-attention?

-How does the NT perform on graphs with extreme degree distributions that are significantly different from those in the training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the node classification problem on graphs beyond homophily. Its proposed technique is very straightforward, a variant of graph Transformer whose messages will have an extra interaction before aggregating into the node embeddings.

### Strengths
S1. This paper's presentation is good and clear. I can easily follow most of the content.

S2. The experimental section should be comprehensive and cover 10 datasets, including both homophilic and heterophilic graphs. 

S3. From Table 1 and Table 2, the performance improvement against the SOTA is decent and appreciated.

### Weaknesses
W1. This paper claims that the proposed method has good expressiveness. However, I found no (theoretical) analysis regarding the expressiveness. Specifically, the paper lacks a formal analysis demonstrating an improvement in expressiveness compared to existing graph neural networks, such as through the lens of the Weisfeiler-Lehman (WL) test or signal processing-based analysis. The claim of 'good expressiveness' needs to be substantiated with rigorous theoretical results.

W2. The proposed method is actually pretty simple, and the rationale is simple, monophyly (lines 50-52), i.e., 2-hop neighbors are helpful for node classification on both homophilic and heterophilic graphs. Such a simplicity is good, but I found some defects unsolved.

W2.1 Why are 2-hop neighbors useful for node classification on graphs regardless of whether they are homophilic or heterophilic?

W2.2 It looks like the proposed method (from Eq. 1 to 3, Figure 2 c) still utilizes information from 1-hop neighbors. In my understanding, the core idea of this paper is to collect edge messages (from 1-hop neighbors) by Eq. 3 and then let the edge messages interact via a self-attention module Eq. 2. However, overall, no information from 2-hop neighbors is included. Again, this method is simple, but it is highly unclear why it is effective.

W2.3 Why previous methods cannot capture the information from 2-hop neighbors? If the 2-hop information is that useful, I think many previously proposed methods should be able to capture it. E.g., GPRGNN [1], ACM-GNN [2]. The paper does not adequately explain why existing methods, which can also incorporate multi-hop information, fail to capture the relevant 2-hop information effectively. Methods like GPRGNN can adaptively assign weights to different hops, and it's unclear why the proposed method offers a unique advantage in this regard.

*Minor weaknesses: *

W3. Some baselines are missing [3-5]. After adding them back, the performance advantage of the proposed method is not that significant on datasets Roman Empire, A-ratings, and Tolokers.

W4 The strategies proposed in Section 4.2 are a bit heuristic-based. The partitioning strategy lacks a theoretical justification for its effectiveness. The paper does not provide a formal analysis of why this particular partitioning method is optimal or even near-optimal. The approach seems ad hoc, and the paper would benefit from a more rigorous treatment of this aspect.

W5. The code is not provided, which lowers the reproducibility of this study.

### Questions
Please check the weaknesses I mentioned.

### Soundness
2

### Presentation
3

### Contribution
2
