# Diss-l-ECT: Dissecting Graph Data with local Euler Characteristic Transforms

- Decision: Reject
- Scores: 8, 6, 6, 3

## Abstract
The Euler Characteristic Transform (ECT) is an efficiently-computable
    geometrical-topological invariant that characterizes the global shape of data. 
    In this paper, we introduce the Local Euler Characteristic Transform (l-ECT), a novel extension of the ECT particularly designed to enhance expressivity and interpretability in graph representation learning.
    Unlike traditional Graph Neural Networks (GNNs), which may lose critical local details through aggregation, the l-ECT provides a lossless representation of local neighborhoods.
    This approach addresses key limitations in GNNs by preserving nuanced local structures while maintaining global interpretability.
    Moreover, we construct a rotation-invariant metric based on l-ECTs for spatial alignment of data spaces.
    Our method exhibits superior performance than standard GNNs on a variety of node classification tasks, particularly in graphs with high heterophily.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the Local Euler Characteristic Transform (L-ECT), an extension of the Euler Characteristic Transform (ECT) designed for graph representation learning. Unlike traditional Graph Neural Networks (GNNs), which can obscure local details through node aggregation, the L-ECT maintains local structural data, thus enhancing interpretability and performance, especially in heterogeneous (high heterophily) graphs. By capturing spatial and structural characteristics of local neighborhoods, the L-ECT provides a rotation-invariant metric for data alignment, showcasing improved performance over GNNs in node classification tasks. The method’s compatibility with machine learning models enables use cases beyond standard GNN architectures, offering more accessible and interpretable models, such as tree-based classifiers. Empirical results demonstrate that L-ECT outperforms GNNs in heterogeneous datasets and facilitates robust spatial alignment in both synthetic and high-dimensional data. This research suggests future exploration into scaling L-ECT and integrating global and local information in complex graph structures.

### Strengths
The paper presents the Local Euler Characteristic Transform (L-ECT) as an extension of the traditional Euler Characteristic Transform, enabling a lossless representation of local graph structures and addressing key limitations of Graph Neural Networks (GNNs) such as oversmoothing and loss of local detail in high heterophily graphs. This novel transformation preserves intricate topological information, allowing for more nuanced node representations by capturing both structural and spatial data and offering an alternative to GNN message-passing frameworks. Additionally, the authors introduce a rotation-invariant metric that enables robust spatial alignment of data in Euclidean space, enhancing the method’s applicability in graph-structured data and increasing resilience to coordinate transformations. Empirical results underscore L-ECT’s effectiveness, showing superior performance over standard GNNs in high-heterophily datasets like WebKB, Roman Empire, and Amazon Ratings. Furthermore, L-ECT’s model-agnostic nature facilitates integration with interpretable machine learning models, such as XGBoost, making it ideal for use in regulated fields like healthcare and finance where transparency is paramount. Beyond graph representation, L-ECT extends to point clouds and other high-dimensional data, proving robust to noise and outliers and enabling efficient spatial alignment without the need for exhaustive pairwise distance computations.

The methods section is detailed yet readable, presenting L-ECT’s mathematical foundation and integrating a rotation-invariant metric for spatial alignment, which adds to the paper’s originality. While the experiments section is robust and results are well-presented through tables and figures, additional visual aids could further clarify data characteristics and enhance accessibility.

the discussion on the limitations of the approaches proposed in the paper is appreciated

### Weaknesses
The paper would benefit, both in making more persuasive the novelty of the work with respect to contemporary literature as well as clarity of the work itself, with a more robust background and related works section

Including a more robust and explicit comparison to related works, which also addresses the novelty of the work being proposed, would be appreciated.

The L-ECT approach, while innovative, faces several limitations and lacks certain aspects of novelty. Its computational complexity scales with graph size and density, making it less efficient for very large or dense graphs and primarily feasible for medium-sized datasets. Although L-ECT emphasizes local information preservation, similar topology-aware or geometric GNN approaches also capture neighborhood-specific details, reducing the uniqueness of this feature. Additionally, traditional GNNs perform comparably well on low-heterophily datasets, indicating that L-ECT may not consistently outperform them across all types of graph data. The approach’s scalability is further limited by sampling trade-offs, as its accuracy depends on carefully chosen parameters, such as direction and filtration steps, which challenge fidelity and computational efficiency at scale. Moreover, despite its model-agnostic design, L-ECT’s interpretability hinges on pre-defined features, potentially restricting its flexibility for complex, dynamic graphs. Finally, L-ECT does not support end-to-end learning as GNNs do; instead, it relies on external classifiers (e.g., XGBoost), which may limit its integration into more comprehensive, end-to-end pipelines.

The authors should include comparison other works which construct topological representations of graphs and graphs neighborhoods and include reference to those related methods such as “graph filtration learning” by Hofer et. al. and other approaches as discussed in survey works such as  “A Survey of Topological Machine Learning Methods” by Hensel et. al.

The authors provide comparative experimental analysis to a number of datasets. It may be misleading, however, to not include other models as discussed in “A critical look at the evaluation of GNNs under heterophily: Are we really making progress?” by Platonov et. al.

### Questions
Would it be possible to include experimental results for the other datasets offered in “A critical look at the evaluation of GNNs under heterophily: Are we really making progress?” by Platonov et. al. or an argument as to why this is done?

### Soundness
3

### Presentation
3

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
This paper introduces the Local Euler Characteristic Transform ($l$-ECT), an extension of the Euler Characteristic Transform (ECT) designed to enhance expressivity and interpretability in graph representation learning. It provides a lossless representation of local neighborhoods and addresses key limitations in GNNs by preserving nuanced local structures while maintaining global interpretability. Their method demonstrates superior performance over standard GNNs on node classification tasks, particularly in graphs with heterophily.

### Strengths
1. Innovative Use of Euler Characteristic Transform: Employing the ECT to enhance graph representation learning, especially in settings with heterophily, is a novel and interesting approach.

2. Solid Theoretical Foundation: The work is thorough, with strong theoretical results that effectively support the proposed method.

### Weaknesses
Missing Important Related Works & Limited Experimental Comparisons: The quantitative experiments focus mainly on node classification tasks in heterophilic graphs but compare the proposed method only with basic models like GCN and GAT. While the authors acknowledge related works on GNNs designed for heterophily in Section 3, the coverage is still limited. It is suggested that the authors include more related works such as [1-5] and select appropriate GNNs for experimental comparison to strengthen the validation of their method.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors introduce a new topological feature extraction methods, Local Euler Characteristic Transform (l-ECT), extending the Euler Characteristic Transform (ECT) to provide a lossless, interpretable representation of local graph neighborhoods, addressing limitations in traditional Graph Neural Networks (GNNs). This novel approach improves performance in node classification tasks, especially in heterophilous graphs, by preserving both local and global structural details.

### Strengths
1. **Novel l-ECT Framework**: Extending the Euler Characteristic Transform to capture local graph details in embedded simplicial complexes is impactful, with theoretical insights enhancing its expressivity, especially for featured graphs.

2. **Extracting  Key Information from Node Neighborhoods from Attribute Space**: The l-ECT enables to obtain node neighborhood information by effectively utilizing the information from attribute space.

3. **Experimental Validation**: The l-ECT consistently outperforms traditional GNNs in node classification tasks, particularly in high-heterophily settings, highlighting its interpretability and effectiveness.

4. **Presentation:** The presentation is very good.

### Weaknesses
1. **Limited Applicability:** The proposed approach is constrained to graphs with node feature vectors in $\mathbb{R}^n$, limiting its applicability to datasets that fit this specific structure. While many datasets do use continuous features, many others, such as citation networks, use binary features. The method's reliance on a continuous feature space makes it less versatile compared to methods that can handle discrete or mixed feature types.

2. **Effectiveness of Approach:** While the concept of embedding the graph into an attribute space using node attribute vectors is promising, the subsequent steps for extracting meaningful information appear less effective. The l-ECT, while theoretically sound, may not be the most efficient way to capture relevant information from the embedded ego networks. The topological output of the l-ECT is often invariant to continuous shape changes and size variations, which may cause the method to miss finer geometric details that could be more informative for node classification. Simpler geometric measures, such as the diameter or convex hull volume of the ego network in $\mathbb{R}^n$, might provide more effective features.

3. **Feasibility in High Dimensions:** As the dimension $n$ of the feature space increases, the number $m$ of representative vectors on $S^{n-1}$ must grow nearly exponentially to maintain a reasonable density. Furthermore, the range of feature vectors impacts the number of intervals {$t_i$} needed for the l-ECT calculation. For high-dimensional and wide-range data, this results in a very high-dimensional $l$-ECT vector, making the approach impractical for real-world applications. The paper lacks a clear strategy for handling high-dimensional feature spaces, and the selection of representative vectors and thresholds is not well-defined, making it challenging for new users to apply the method effectively. Dimension reduction techniques should be explored, and normalization of feature vectors is crucial to ensure consistent performance across datasets.

4. **Theoretical Contributions vs. Practical Applications:** While the rotation-invariant metric is mathematically appealing, its practical relevance is questionable since it relies on the infimum over all rotations, which is computationally expensive and may not be necessary for effective node classification. Also, the discussion of graph isomorphism seems tangential, as Definition 2 is highly restrictive, applicable only to isomorphic graphs with identical feature vectors. This theoretical discussion does not translate well into practical benefits.

5. **Experimental Results:** The presented results are uninformative and potentially misleading. The models used, GCN and GAT, are older and are known to perform poorly in heterophilic settings. The authors should consider comparing their approach with newer GNN models that perform well on heterophilic datasets and include more homophilic datasets (other than Computers and Photo) to provide a comprehensive performance assessment. The lack of comparison with state-of-the-art models makes it difficult to assess the true contribution of the proposed method. Furthermore, exploring the integration of $l$-ECT vectors with a more recent GNN model could provide valuable insights into performance enhancement.

### Questions
See weaknesess.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a local Euler characteristic transform for enhancing feature representation for graph learning. This approach addresses key limitations in GNNs by preserving nuanced local structures while maintaining global interpretability.

### Strengths
Using local Euler characteristic transform for graph representation is novel to me.

### Weaknesses
1. To compute ECT or l-ECT, one needs to embed a simplicial complex in a Euclidean space. The authors propose to embed using node features. However, I don't think this is a genuine embedding. For example, if the feature space is \mathbb{R}^2, then even if the nodes are embedded to the place in a 1-1 fashion, the edges may cross each other. Therefore, only talking about vertex embedding is insufficient as a graph or a simplicial complex has additional structures. The core issue is that the proposed embedding, based solely on node features, does not guarantee preservation of graph structure. Specifically, the embedding does not ensure that adjacencies in the original graph are maintained in the embedded space, which is crucial for topological properties like the Euler characteristic to be meaningful in the context of the original graph. The embedding process may introduce artificial intersections and alter the connectivity of the graph, thus invalidating the topological interpretation.
2. Related to 1. The author should be more specific on ``embedding'', whether it is metrical embedding, differential embedding, or topological embedding (or something else?). The lack of clarity on the type of embedding used makes it difficult to assess the validity of the approach. A metrical embedding would focus on preserving distances, a differential embedding on preserving local geometric structures, and a topological embedding on preserving connectivity and topological invariants. The authors need to specify which type of embedding they are using and justify why it is appropriate for the proposed method. Without this, it is unclear how the Euler characteristic transform applied to the embedded graph relates to the original graph's structure.
3. The proofs are poorly written. The statements are vague and imprecise. Many details are missing. It is hard to assess the correctness of the results. For example, in Theorem 1, the notation "$\approx$" is used without defining what kind of convergence or approximation it represents. Similarly, in Theorem 2, the statement that the l-ECT "provides the necessary information for performing a single message-passing step" is not precise enough. It is unclear what information is provided, how it is used, and what the error bounds are for this reconstruction. The lack of rigor in the proofs makes it difficult to verify the theoretical claims of the paper.
4. It seems to me that the proposed l-ECTs capture local structural information. They are used as node features, but not used to guide feature aggregation. I fail to get the intuition of why they can be useful for the node classification task. However, on the other hand, they might be useful for the graph classification task. The use of l-ECTs as node features without directly influencing the aggregation process is questionable. While l-ECTs might capture local structural information, it is not clear how this information is relevant for distinguishing between node classes, especially considering that nodes with the same label can have completely different neighborhood structures. The authors should provide a clearer justification for why these features are useful for node classification, or alternatively, consider using them for graph classification tasks where local topological features might be more relevant.
5. The compared benchmarks are very limited (only GCN and GAT). From my own experience, the results are not very impressive, e.g., for the Actor, Squirrel, and Chameleon datasets, there are more recent benchmarks (e.g., ACM-GCN) whose performance is at least 5%-10% higher than those reported by the authors. The experimental evaluation is not comprehensive enough. The choice of GCN and GAT as baselines is insufficient, as there are more recent and advanced models that achieve significantly better performance on the datasets used. The authors should compare their method against state-of-the-art models, particularly those designed for heterophilic graphs, to provide a more realistic assessment of its performance.
6. Ablation study is missing. It is hard to assess whether l-ECTs play an important role in the reults shown. Without an ablation study, it is impossible to determine the contribution of the l-ECTs to the overall performance. It is crucial to evaluate the performance of the model with and without the l-ECT features to understand their impact. This study should also include variations in the parameters of l-ECT to determine their sensitivity.

### Questions
See weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2
