# Commute Graph Neural Networks

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
Graph Neural Networks (GNNs) have shown remarkable success in learning from graph-structured data. However, their application to directed graphs (digraphs) presents unique challenges, primarily due to the inherent asymmetry in node relationships. Traditional GNNs are adept at capturing unidirectional relations but fall short in encoding the mutual path dependencies between nodes, such as asymmetrical shortest paths typically found in digraphs. Recognizing this gap, we introduce Commute Graph Neural Networks (CGNN), an approach that seamlessly integrates node-wise commute time into the message passing scheme. The cornerstone of CGNN is an efficient method for computing commute time using a newly formulated digraph Laplacian. Commute time is then integrated into the neighborhood aggregation process, with neighbor contributions weighted according to their respective commute time to the central node in each layer. It enables CGNN to directly capture the mutual, asymmetric relationships in digraphs. Extensive experiments confirm the superior performance of CGNN.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In the submitted manuscript, the authors propose a novel digraph Laplacian, which is later used to more efficiently calculate the commute time of pairs of nodes. They furthermore propose a simple node feature based rewiring scheme, which allows them to ensure that the resulting graph gives rise to an aperiodic, irreducible Markov Chain, which has a unique steady state. The authors then propose to calculate commute times on this rewired graph, to transform these commute times by taking the exponential function of this matrix and subsequently sparsifying it with the adjacency matrix. This then allows the authors to propose a variant of the DirGNN, called CGNN, in which edges are reweighted by their transformed commute times. The authors finally evaluate the empirical performance of their CGNNs against a large variety of baseline models on a large number of datasets and find consistently good, although sometimes marginal performance improvements. They furthermore analyse these results and provide several insightful further experiments on runtimes and ablation studies of different model components.

### Strengths
- The rewiring scheme that you propose is simple, but rather nice in my opinion. It would be interesting to see further study of its impact on the overall graph structure. 

- Your proposed CGNNs are compared to a comprehensive set of baseline models, which great to see.  

- The analysis of the application scope of your proposed model is very strong indeed and something that is generally not done enough in our literature.

### Weaknesses
Please find further details on my listed weaknesses in my questions below.
- The proposed model boils down a weighting of the DirGNN by an efficiently calculated function of the commute times, which is a rather trivial change. 
- The derivation of the DiLap matrix appears to be flawed. 
-  Your ablation studies could be improved and extended.

### Questions
1] The derivation of your DiLap operator appears to be flawed. In particular, in the second line of Equation (12) when you pull $s_i$ out of the sum, the term $s_i$ arises $d_i^{out}$ times and therefore, Line 2 should be $s_i - \frac{1}{d_i^{out}} \sum s_j.$ The correction of this error means that you should be working with the random walk Laplacian (see e.g. [1]), which would be far more intuitive. To me it seems that for it to be possible to accept this paper at ICLR, the derivation of your operator needs to be corrected and the subsequent experiments should be adjusted. 

2] I am unsure what adjacency matrix you use in Line 314 to sparsify the matrix $\tilde{\mathcal{C}}.$ Are you using the adjacency matrix corresponding to the graph in which you have added the node feature similarity edges? And if not, could you hypothesise how severe the impact may be of calculating the commute times on a rewired graph and to then message pass with the original graph. 

3] Your method appears to be relatively memory intensive. In particular, you seem to require the evaluation of the exponential function fo the dense matrix $\tilde{\mathcal{C}}$. Empirical evaluation of, not only the time, but also memory complexity of your method in comparison to your baseline methods would be very valuable. 

4] The ablation study in Table 2 is very interesting! I think it should be extended in scope to also extend to homophilic datasets and to also include other commonly used message passing operators, such as the symmetrically normalised adjacency matrix used in the GCN and the PageRank matrix used in the PPrGo model [2].

5] It does not seem sensible to me to compare your sparisfied commute time based CGNN to the CGNN$_{ppr}$ using the dense PageRank matrix. It seems to be fairer to me to either compare dense versions of both matrices or sparse versions of both matrices. In particular, since you sparify your commute time matrix with the adjacency matrix, it would be interesting to compare your model to a PageRank-based scheme, where the PageRank matrix is also sparsified with the adjacency matrix. 

6] Minor comments:

6.1] The abbreviation "SPD" is used in Line 45 before its definition. 

6.2] The contributions of your paper are not explicitly listed. 


[1] Von Luxburg, U., 2007. A tutorial on spectral clustering. Statistics and computing, 17, pp.395-416.

[2] Bojchevski, A., Gasteiger, J., Perozzi, B., Kapoor, A., Blais, M., Rózemberczki, B., Lukasik, M. and Günnemann, S., 2020, August. Scaling graph neural networks with approximate pagerank. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 2464-2473).

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a method for weighing the features of the neighbors of a node during aggregation step of GNN based on the commute distance of the neighbor to the node. The commute distance between nodes A and B is the average number of steps that a random walk takes traversing from node A to node B and back to node A. This distance is particularly relevant for directed graphs because although all nearest neighbors are one hop away from a node, their commute distances might vary because of the constraints imposed by the directions of the edges. One neighbor might require a circuitous path along many other nodes before returning to the original node (have longer commute distance) whereas another neighbor could be closer. The authors' key idea is to weight the importance of the features of the neighbors of a node during the aggregation step of GNN based on the commute distance of the node to those neighbors. Besides this weighing, the aggregation and update scheme that they use is based on that of Rossi et al. where the features of the incoming and outgoing neighbors are aggregated separately and used alongside the node's own features during the update step. The authors also propose an efficient way of computing commute distance. To do so, they introduce a weighted Laplacian for directed graphs that accounts both for the directional connectivity of the nodes and their importance (computed as the stationary probability at each node of a random walk on the graph). The authors also introduce a way to rewire a graph to ensure that it is irreducible and aperiodic while keeping the graph sparse (unlike alternative methods such as PageRank). The commute distance can then be efficiently computed using the sparse weighted Laplacian. Finally, the authors show empirically that their proposed approach improves on existing methods when applied to many standard directed graph data sets such as Squirrel and Chameleon.

### Strengths
This is an interesting paper with a clever insight. It is sensible to say that not all nearest neighbors on a directed graph are created equal. Weighing the features of some neighbors more during the aggregation step of a GNN based on the shorter commute distance of those neighbors to the original node is an intriguing idea. Weighing based on the commute distance certainly sounds reasonable. The proposed method for rewiring a graph to make it irreducible and aperiodic while still retaining sparsity is also clever as is the weighted Laplacian that can be used to efficiently compute the commute distance leveraging its sparsity using methods such as randomized truncated singular value decomposition.

The state-of-the-art performance achieved using the author's method on some of the most commonly used directed graph data sets, such as Squirrel, Chameleon, etc. is impressive and provides reasonable empirical proof of the validity of the proposed approach. The authors also include solid empirical evidence on running times of their algorithm and convincing comparisons to PageRank for graph rewiring and calculation of commute distances.

### Weaknesses
To this reviewer, the biggest weakness of the paper was that although weighing neighbors by commute time is sensible, it is not necessarily principled. Is there any reason to a priori expect that neighbors of a node that have shorter commute times to that node somehow contain more relevant features for learning on graphs? This seems to depend on the nature of the learning problem and the data set. Now, the authors can argue that their empirical evidence is sufficient to motivate their approach. However, more should be done here to support the author's proposal. Some evidence is provided in that an adjacency matrix constructed by weighing the neighbors by their commute distance more closely resembles an adjacency matrix constrained to edges that connect nodes within the same class. The authors should expand on this. What does this look like for other data sets? How does aggregation of information using these weighted neighbors look across multiple hops and longer distances across the graph? The authors should have come up with synthetic data sets that can elucidate the mechanism behind the improvement that they are seeing.

If empirical evidence is the main motivation behind the proposed schemes, the authors could have dome more to build a stronger case. An argument is made in the paper that with the weighing of the neighbors less irrelevant information is aggregated as the GNN models go deeper. The authors should empirically demonstrate this by showing how the performance of their model changes with depth and contrast with existing models. In general, it would have been very interesting to see the impact of the weights proposed in this paper on multi-hop GNN models, such MixHop, Shortest Path Networks, or DRew. In addition, it would have been more convincing if the authors had applied their approach to real world problems of directed graphs in addition to standard benchmark data sets used in Table 1 such as temporal web traffic data, power grids, traffic flow, etc.

The method proposed in the paper to rewire the graph to ensure irreducible and aperiodic graphs is also ad hoc and not very principled. The method certainly produces a sparse graph unlike PageRank, however, other approaches can also be used to generate irreducible graphs that are sparse such as generating a kNN graph based on the node features. It is not clear that the proposed method is optimal in any way other than that it outperforms the amended probabilities used in PageRank. See Questions below for suggestions on how the authors can evaluate this empirically.

### Questions
As outline in the weaknesses above, can the authors provide a principled reason for why features aggregated from a node's neighbors should be weighed by the commute distance of the node to its neighbors? Can the authors provide any theoretical justification for using commute distance for such weighing?

The authors provide one figure where they show for Chameleon and Squirrel data sets that an adjacency matrix constructed from nearest neighbors weighted by their commute distance more closely resembles an adjacency matrix constrained to connecting nodes within the same class. Can the authors include other empirical measures of how the weighting of neighbors can improve performance of GNNs? Can the authors look at properties of longer hops (going beyond one-hop neighbors) and how information is aggregated across nodes within or outside the same class? Would it be possible to construct a synthetic data set that would shed light on the mechanism behind why they see an improvement?

How does the proposed model's performance change with depth? The authors claim that the weighted neighbors avoids the problem of aggregation of irrelevant information as depth is increased? It would be informative to see an empirical demonstration of this. The authors should plot the performance of their model as a function of model depth and compare with existing models.

In addition, can the authors apply their approach a real world problem on directed graphs that requires long range information transmission, such as power grids or traffic flow data? This would bolster the empirical support for their method.

As noted in the weaknesses above, can the authors try alternative methods for graph rewiring that also produce sparse graphs, such as constructing a kNN graph using the node features? The authors should include an empirical comparison or provide theoretical justification for their method. Is the proposed similarity-based rewiring mode optimal?

How much of the improvement is coming from the fact that the Laplacian proposed by the authors is weighted by the stationary probability of random walks on the graph (or what the authors call the importance of a node)? Can the authors do an ablation study to disentangle this from the commute distance?

This reviewer was confused by the comment that general GNNs can outperform models tailored for directed graphs with hyper-parameter tuning. In Table 1, DirGNN, a model tailored for directed graphs, outperforms GCN. Can the authors clarify what they mean by this comment?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a novel approach that integrates node-wise commute time into a message-passing framework, introducing the Commute Graph Neural Network (CGNN). The central contribution of CGNN is the development of a new directed graph Laplacian, designed to address path asymmetry in directed graphs. The authors demonstrate that CGNN outperforms existing baselines across most datasets and effectively motivates the significance of the problem they address.

Overall, I found the paper well-executed and recommend it for acceptance.

### Strengths
This paper is engaging and well-written, with a thorough background review that enhances accessibility and readability. Key strengths I noted include:

1. **Novel Approach with Significant Potential:** The proposed method, particularly the newly formulated digraph Laplacian, offers a fresh perspective with substantial potential for future research and applications.

2. **Comprehensive Component Analysis (Section 5.3):** The inclusion of a component analysis strengthens the paper by providing an effective ablation study.

3. **Clear Contribution and Baseline Comparison:** The authors clearly articulate their contributions, outlining the distinctions between their method and existing baselines. They explain where prior approaches fall short and demonstrate how their approach addresses these limitations.

4. **Effective Visual Aids:** Figures 1 and 2 are well-designed and enhance understanding by clarifying details within the method.

5. **Robust Experimental Validation:** he paper validates its approach across a wide variety of datasets and multiple baseline comparisons, highlighting the robustness and generalizability of the proposed method.

6. **Reproducibility:** The authors provide code for reproducing their experiments.

### Weaknesses
Overall, this paper is strong in its methodology and results, though I have a few recommendations that could enhance its clarity and depth.

1.  **Graph Density in Rewiring Approach:** While I appreciate that the authors provided commute times before and after rewiring in Table 3, it would be beneficial to also examine how rewiring affects graph density. This additional metric could offer deeper insights into structural changes post-rewiring.

2.  **Unobserved Edges in Definition of $m_{i,in}^{(l)}$ and $m_{i,out}^{(l)}$:** Given that unobserved edges are introduced to the graph, I suggest adjusting the definitions of $m_{i,in}^{(l)}$ and $m_{i,out}^{(l)}$  to account for these edges, potentially assigning them a lower weight than observed edges. This adjustment could yield a more realistic representation of edge significance.

3.  **Model Complexity:** The model’s complexity is relatively high, even though it’s reported to be on par with other GNN models. This complexity, particularly in precomputation, might be a barrier in some cases. However, I do not consider this a critical issue, as future work could address and optimize this aspect.

4. Inclusion of Synthetic Datasets: While the paper impressively covers a range of empirical datasets, the addition of synthetic datasets could improve interpretability. By embedding known patterns, synthetic data could highlight the model's strengths and limitations in detecting specific features.

5. Reordering Related Work: Placing the Related Work section (currently Section 6) closer to the beginning would make the reading experience smoother, giving readers essential context before diving into the methodology and results.

### Questions
I have no further questions, though I would recommend that the authors address the previously noted weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes  Commute Graph Neural Networks (CGNN) for directed graphs, which is based on a new digraph Laplacian matrix taking into the commute time on a (possibly rewired) strongly connected graph. Theoretical and empirical analysis is provided.

### Strengths
1) The idea of considering commute time is novel and reasonable.
2) The topic of directed graph neural networks is important.
3) The source code is provided.

### Weaknesses
1) It is unclear why the proposed Laplacian is sparse. From Eq. (5), the matrix $P$ seems to be a complete matrix.
2) It is unclear what the relationship is between Eq. (5) and $D^{-2}L$ and why you should choose Eq. (5).
3) Being strongly connected is too strong an assumption, and it is not clear why the rewiring procedure only minimally alters the overall semantics of the original graph.
4) [1] mentions flow imbalance in directed graphs and is not discussed. It is also unclear whether the idea in [1] is considered unidirectional by the authors.
5) (minor) Grammar issues: e.g., line 115.5 "notations. We" should be "notations, we"

### Questions
1) Why is the proposed Laplacian sparse? From Eq. (5), the matrix $P$ seems to be a complete matrix.
2) What is the relationship between Eq. (5) and $D^{-2}L$ and why do you should choose Eq. (5)?
3) Why does the rewiring procedure only minimally alter the overall semantics of the original graph?

### Soundness
2

### Presentation
2

### Contribution
2
