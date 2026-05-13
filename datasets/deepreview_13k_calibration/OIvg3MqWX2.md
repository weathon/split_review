# A Theoretically-Principled Sparse, Connected, and Rigid Graph Representation of Molecules

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 10, 6, 8

## Abstract
Graph neural networks (GNNs) -- learn graph representations by exploiting graph's sparsity, connectivity, and symmetries -- have become indispensable for learning geometric data like molecules. However, the most used graphs (e.g., radial cutoff graphs) in molecular modeling lack theoretical guarantees for achieving connectivity and sparsity simultaneously, which are essential for the performance and scalability of GNNs. Furthermore, existing widely used graph construction methods for molecules lack rigidity, limiting GNNs' ability to exploit graph nodes' spatial arrangement. In this paper, we introduce a new hyperparameter-free graph construction of molecules and beyond with sparsity, connectivity, and rigidity guarantees. Remarkably, our method consistently generates connected and sparse graphs with the edge-to-node ratio being bounded above by 3. Our graphs' rigidity guarantees that edge distances and dihedral angles are sufficient to uniquely determine general spatial arrangements of atoms. We substantiate the effectiveness and efficiency of our proposed graphs in various molecular modeling benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The present manuscript proposes a novel graph construction method, SCHull for molecular modeling thorugh GNNs. The authors start by introducing limitations of the currently existing graph construction  methods (e.g. radial cuttoff, and knn graphs), that cannot deal with sparsity, connectivity, and rigidity at the same time.

The method constructs graphs in two steps, first by projecting points onto the unit sphere. and secondly by constructing a convex hull for the projected points, and adding edges to the graph, based on the convex hull. According to the authors' motivation, the resulting graphs are sparse, connected, and rigid, making them suitable for learning molecular representations using GNNs.

The authors show the impact of SCHull, by integrating it into current molecular Gnns, and test it in various benchmarks, including MD17, as well as protein modeling tasks (fold, enzyme reaction classification, Protein-ligand binding).

### Strengths
1. I particularly find Theorem 3.6 interesting, and useful for the distinction of point clouds through their corresponding SCHull graphs. In general, the authors provide a well-defined set of propositions for defining connectivity, rigidity, and sparsity for the SChull graphs, making it useful for predicting their impact on GNN's performance and scalability.

2. The motivation for a hyper-parameter free approach for graph construction is very intriguing, and can be proven very useful for molecular modeling tasks, where the distance thresholds can play an important role. 

3. The empirical results show that in both small- and large-molecular modeling tasks, SChull has a positive impact in a couple of GNNs. 

4. The paper is well-written, the formulations are clear, and the experimentation setup is nicely described.

5. It's very interesting that Tables 4, and 5 show a comparable increase of the runtime cost, with respect to the methods without the SChull. I would expect a much longer runtime discrepancy, due to the point projection, and the CH computation.

5. The code is available, seemingly containing all variants of models and benchmarks appeared in the manuscript. I cannot assess its validity, as I did not run it.

### Weaknesses
1.  The paper primarily compares SCHull to radial cutoff and k-nearest neighbor graphs, as well as chemical graphs. It lacks  some compariso with more recent or complex molecular graph construction methods, such as power graphs [1] (which are by the way already mentioned by the authors but not benchmarked) or methods focusing on higher-order graphs, such as simplicial complexes [2] ( that define volumes of data points), or combinatorial complexes [3] (that particularly make use of convex hulls and their corresponding volumes in point clouds).

2. An approach on learning new geometric interactions might be useful in better interpreting the correlation of geometry and function, which could be particularly a motivation for this paper. The paper should focus on exploring or at least mention how such a convex hull approach, despite a comparable computational cost can help on finding interpretable structures.

3. Since the method is focusing on the three properties of sparsity, connectivity, and rigidity, it'd be great if the authors can show empirically the impact of SChull on each of these properties independently.

### Questions
Based on my comments in the weaknesses section: 

1. Can the authors provide a comparison (at least conceptual, but ideally an empirical one) with methods that include power graphs, or higher-order structures?

2. Do the authors think that such a method can provide interpretability benefits? If yes, I think that the motivation could be much strengthened. In that case, is it possible to provide an interoperability analysis?

3. Can the authors show the impact of the method empirically on each graph property mentioned in the paper (I..econnectivity, and rigidity)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper proposes a novel method for constructing sparse yet connected geometric graphs: Project the points onto a sphere, construct a polyhedron, and construct a graph from its edge structure. This aims to mitigate earlier costly approaches of taking the power graph of the original graph. The authors first prove theoretical properties of their construction and show that maximally expressive MPNNs with particular initializations for node and edge features can distinguish among generic graphs, essentially proving that via a sparse graph structure (degree bounded by 3) 1-WL can distinguish all generic point cloud configurations (i.e. not assuming a fully connected point cloud as in earlier works). The authors then empirically show the construction's efficacy and value of the SCHull face angles that allow for universality on sparse configurations, by obtaining consistently better results on synthetic, classification, and regression tasks.

### Strengths
1. Novel technique relying on a fast (n*log(n)) algorithm is scalable and empirically also negligible computational overhead
2. Introduces a novel technique to a paradigm not challenged much in research: the distance cutoff construction for geometric graphs. Theoretical and empirical proof this approach is sound.
3. An architecture-agnostic method that can be applied to a large variety of MPNN-like models

### Weaknesses
1. Proofs mainly rely on previous work and the construction of the graph is also backed by a known algorithm, thus there is a notion of an incremental advance. Although, I believe that tying these two areas together constitutes a strong advancement for ML.

2. The empirical results are consistent yet are not pushing the boundary on SOTA, but rather give a `boost' to low expressive models. It would be nice to see the performance of working on SCHull graphs with the initial edge and node features for more expressive architecture, for instance, MACE or SEGNN ("Geometric and physical quantities improve equivariant message passing", Brandstetter et al.) I suspect it would make less of a difference but please prove me wrong. Anyway, only having a comparable result to these architectures (when they process distance-restricted graphs) with faster inference is still a great achievement. If this is performed I may increase my score.

3. The background for geometric deep learning is insufficient in my opinion. For instance, there is no discussion on research on expressivity when point clouds are not necessarily generic and a comparison of your approach with models that are universal (or complete) on **all** point clouds. For a couple of papers on this topic please note:

Hordan, S., Amir, T. and Dym, N., 2024. Weisfeiler Leman for Euclidean Equivariant Machine Learning. ICML 2024

Li, Zian, et al. "Is distance matrix enough for geometric deep learning?." Advances in Neural Information Processing Systems 36 (2024).

Overall this paper has strong potential, addressing these weaknesses will likely increase the rating.

### Questions
1. Overall I think the proof of Theorem 3.6 is correct. I do have a few questions though:
a) "Since the degrees of corresponding nodes are equal, both graphs have the same number of edges, i.e., |E| = |E′|." I don't see why this is true, later you discuss how the corresponding edges match because of the generic nature of the point cloud, and then by equality of multisets you could have claimed the number of edges is equivalent.I might be missing something.
b) "Next, we observe that the triple (∥xi − xj ∥, ∥xi − x∥ , ∥xj − x∥) uniquely determines the distance between
projected points px(xi), px(xj ) on the unit sphere." 
I don't see how I recover $|| \frac{x_i - \bar{x}}{|| x_i - \bar{x}||} - \frac{x_j - \bar{x}}{|| x_j - \bar{x}||} ||$ from those three distances, please enlighten me.

2. There exist known counterexamples for fully connected geometric graphs that 1-WL cannot distinguish. It may be the case that your maximally expressive SCHull-MPNN with edge features and node features can distinguish. One such example is depicted in Figure 1 in [Li et al.]. They have code for the coordinates of these shapes or I can also provide them if necessary. Is the maximally expressive architecture you propose able to distinguish among them?


[Li et al.]Li, Zian, et al. "Is distance matrix enough for geometric deep learning?." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a hyperparameter-free graph construction method for molecular modeling that ensures sparsity, connectivity, and rigidity. It addresses the limitations of traditional methods, like radial cutoff graphs, which lack guarantees for both connectivity and sparsity and fail to leverage spatial arrangements effectively. The proposed method consistently generates connected, sparse graphs with an edge-to-node ratio capped at 3, and ensures rigidity, making spatial arrangements uniquely determinable. The approach is proven effective and efficient in various molecular modeling benchmarks.

### Strengths
1.The proposed SCHull method is quite innovative. I appreciate the author's idea of introducing unit spherical mapping, which makes the graph construction more reasonable and reliable. The implementation is also very clever.

2.The paper provides thorough validation of the proposed method in well-justified experimental settings.

3.The paper conducts comprehensive theoretical validation to demonstrate the effectiveness of the method.

### Weaknesses
1.The discussion primarily focuses on molecular analysis, which may make the paper lean somewhat towards chemistry and biology. However, this does not detract from it being a strong paper. It may be worth considering whether this method could be applied to other types of graph data analysis.

2.Could consider conducting some visualization experiments, if the level of difficulty permits.

### Questions
1.Since the method is primarily applied to molecular analysis, do the conclusions require alignment with relevant chemical principles? The paper explains the utility of the SCHull graph in enhancing GNN capabilities, but could such a projection result in the loss of certain chemical properties?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Overall, the paper provides valuable contributions and should be accepted, though it requires both minor and significant revisions. I have given a lower score to ensure that all issues are addressed. The paper effectively tackles the challenge of defining the underlying combinatorial graph, which is crucial for performing accurate analysis and properly separating point clouds.

### Strengths
Here’s an expanded version of your statement:

"The paper presents a pioneering approach for constructing an underlying combinatorial graph for a given point cloud, addressing several crucial challenges in graph-based data representation. The proposed method ensures key properties such as connectivity, sparsity of the graph, and the ability to accurately reconstruct the original point cloud. These properties are essential for both efficient computation and the preservation of the inherent structure of the data.

By focusing on these aspects, the authors effectively balance the need for a graph that is sufficiently sparse—thereby reducing computational complexity—while still maintaining connectivity, which is necessary for capturing the relationships between points in the cloud. This delicate balance is often difficult to achieve, as sparse graphs may lose critical information, and densely connected graphs can lead to inefficiency and overfitting. The authors’ method overcomes this trade-off and ensures that the graph retains the essential features of the point cloud, enabling reliable downstream analysis.

Additionally, the paper demonstrates how the performance of existing methods can be significantly improved by replacing the traditional graph construction techniques with the newly proposed combinatorial graph. The empirical results presented show notable enhancements in areas such as classification accuracy, clustering performance, and point cloud segmentation, underscoring the practical benefits of the new graph structure. These improvements are a testament to the robustness and effectiveness of the method, positioning it as a valuable tool for a wide range of applications in fields such as computer vision, machine learning, and graph signal processing.

The introduction of this novel graph construction framework represents a substantial step forward in the field, potentially opening new avenues for research on graph-based point cloud analysis. It not only improves existing methodologies but also provides a foundation for further exploration of how combinatorial structures can be leveraged to better understand and manipulate high-dimensional data."

### Weaknesses
The main weakness of the paper is that the proposed graph construction is not continuous and doesn't operate on a pre-existing attributed graph. Instead, it creates its own selected graph, which may limit its applicability in cases where the underlying graph already contains valuable domain-specific information. This approach lacks flexibility, especially in scenarios where a smooth transition or integration with existing graph structures is required. As a result, the method may overlook important attributes or contextual details in real-world applications, reducing its versatility. The main concern is that the point cloud may become copolar and thus, the convex hull would become 2-dimensional. Does it happen in real-world datasets?

### Questions
First of all your algorithm is very similar to the one proposed in the paper Congruence, Similarity, and Symmetries of Geometric Objects, 1987. You didn't cite but this citation must be added, as the first two steps are identical to it. No problem with it but citation must be added.

**Technical Issues:**
1. Line 167 should use "if and only if" in reference to edge isomorphism.
2. After Theorem 3.6, add a remark noting that implementations of maximally expressive GNNs for generic point clouds exist, such as in Sverdlov & Dym.
3. Figure 4 and its details should be moved to the experiments section.
4. All theorems and propositions should either be restated in the appendix or, at the very least, have a mention of what is to be proven there.

**Conceptual Issues:**
1. In your framework, you separate complete generic geometric graphs, unlike Joshi [23] and Sverdlov [24], who work with given combinatorial graphs. This difference should be explicitly stated in your setup, and it should be clear that the goal is to construct the underlying graph.
2. The discontinuity of your graph construction should be discussed. Since the function is discrete, it cannot be continuous, but this point should be acknowledged.
3. Proposition 3.1 is not proven at all. Some minimal proof or explanation is necessary.
4. Regarding the MD17 experiments, I would like to know which models you considered in your comparison and, specifically, if your method improved in the SOTA method. Same for protein folding.
5. What is the computational running time for complete graphs? Does considering the complete structure degrade performance?
6. When you combine the k-hop/threshold graph, how do you choose the parameters to ensure connectivity, sparseness, and constructability?

### Soundness
3

### Presentation
3

### Contribution
3
