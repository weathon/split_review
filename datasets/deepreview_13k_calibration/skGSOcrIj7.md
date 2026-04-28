# Neural Spacetimes for DAG Representation Learning

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 8, 6, 6

## Abstract
We propose a class of trainable deep learning-based geometries called Neural Spacetimes (NSTs), which can universally represent nodes in weighted directed acyclic graphs (DAGs) as events in a spacetime manifold. While most works in the literature focus on undirected graph representation learning or causality embedding separately, our differentiable geometry can encode both graph edge weights in its spatial dimensions and causality in the form of edge directionality in its temporal dimensions. We use a product manifold that combines a quasi-metric (for space) and a partial order (for time). NSTs are implemented as three neural networks trained in an end-to-end manner: an embedding network, which learns to optimize the location of nodes as events in the spacetime manifold, and two other networks that optimize the space and time geometries in parallel, which we call a neural (quasi-)metric and a neural partial order, respectively. The latter two networks leverage recent ideas at the intersection of fractal geometry and deep learning to shape the geometry of the representation space in a data-driven fashion, unlike other works in the literature that use fixed spacetime manifolds such as Minkowski space or De Sitter space to embed DAGs. Our main theoretical guarantee is a universal embedding theorem, showing that any $k$-point DAG can be embedded into an NST with $1+\mathcal{O}(\log(k))$ distortion while exactly preserving its causal structure. The total number of parameters defining the NST is sub-cubic in $k$ and linear in the width of the DAG. If the DAG has a planar Hasse diagram, this is improved to $\mathcal{O}(\log(k)) + 2)$ spatial and 2 temporal dimensions. We validate our framework computationally with synthetic weighted DAGs and real-world network embeddings; in both cases, the NSTs achieve lower embedding distortions than their counterparts using fixed spacetime geometries.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Neural SpaceTimes (NSTs), a class of trainable geometries that can encode nodes of weighted Directed Acyclic Graphs (DAGs) into a spacetime manifold. NSTs are designed to capture both spatial and causal (temporal) information by using a product manifold combining spatial quasi-metrics with temporal partial orders to represent graph weights and directionality. Besides, theoretical analysis of the universal embedding theorem shows that NSTs can learn low-distortion embeddings for any DAG. Some experiments are also conducted to validate the effectiveness of NSTs.

### Strengths
1. The problem tackled in this paper, i.e., representation learning in DAGs, is challenging and significant in the graph machine learning community.
2. Theoretical guarantees of the proposed approach are provided in the manuscript.

### Weaknesses
Despite the merits of the paper, I have the following concerns.
1. Most results presented in this paper pertain to distortion and directionality, which demonstrate that NSTs perform robustly when evaluated by these two measures. However, there are no concrete results showing the performance of NSTs in real-world learning tasks, e.g., (semi-supervised/unsupervised) node classification, link prediction, and graph classification in synthetic DAGs, real-world DAGs (e.g., web page hyperlink graphs and citation graphs), and spatiotemporal graphs (e.g., encrypted transaction graphs). Authors are suggested to conduct some previously mentioned learning tasks and investigate how NSTs perform.
2. Some test datasets used in the experiments are always considered by those graph neural networks tackling graph heterophily (e.g., CPGNN). Compared with these graph neural networks tackling graph heterophily, how do NSTs perform in real-world tasks?
3. Most test datasets considered in this paper are also used to test conventional graph neural networks, e.g., GCN, GAT, GraphSAGE, and Graph Transformer. The authors should compare NSTs with conventional graph neural networks in real-world learning tasks (as mentioned in point 1).
4. The test datasets used in this paper are relatively small. How do NSTs perform in larger datasets? The authors can consider using datasets from OGBN, and other large datasets.

### Questions
1. How do NSTs perform in real-world learning tasks evaluated by well-established metrics (e.g., accuracy, NMI, and F1, ROC-AUC)?
2. How do NSTs perform when compared with conventional GNNs in real-world learning tasks?
3. Do NSTs still perform robustly in massive graphs?
4. How do NSTs perform when compared with GNNs tackling heterophily?

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
The paper sets forth a new neural network architecture capable of learning the embedding of a DAG into a pseudo-Riemannian manifold, which encodes both the spatial and temporal distance between nodes of the DAG in a continuous way. Some conditions (along with proof) are given which guarantee that the embedding is faithful.

The network itself is composed of three separate networks, namely, an initial latent space embedding $\mathcal{E}: \mathbb{R}^N \rightarrow \mathbb{R}^{D+T}$, a modified neural snowflake $\mathcal{D}: \mathbb{R}^{D+T} \times \mathbb{R}^{D+T} \rightarrow [0, \infty)$ which is the quasi-metric on the manifold, and a partial order $\mathcal{T}: \mathbb{R}^{D+T} \rightarrow \mathbb{R}^T$ which encodes the causal relationships in the DAG. These latter two networks are trained parallel to each other and are optimized with respect to an aggregated loss function $\mathcal{L} = \mathcal{L}^{\mathcal{D}} + \mathcal{L}^{\mathcal{T}}$.

Empirical results are given over several datasets, some synthetic with a complex pseudo-metric and others real-world webpage hyperlink DAGs. The results are favorable of the new architecture compared to those of Minkowski and De Sitter space embeddings, showing that the new architecture shows little distortion in the learned quasi-metric and almost always preserves the causal relationships among nodes in the DAGs.

### Strengths
The paper offers originality within its domain by constructing a novel architecture capable of embedding a DAG into a pseudo-Riemannian manifold which has several spatial and temporal components. In particular, adding the capability of embedding a given DAG into more than one temporal component is a novel contribution and allows the network to represent and preserve more complex causal structure from the DAG. Furthermore, the authors modify the neural snowflake model for use as a learnable quasi-metric.

The quality of the paper is also very good given that the authors cited several relevant related works and gave ample justification in the form of mathematical proof for their many propositions and theorems, thus adding to the already existing clarity of the paper.

I believe this paper makes a significant contribution to the field by adding the ability to represent discrete structures in a continuous fashion with very little approximation error, thus presenting a new and powerful tool to various application domains.

### Weaknesses
The paper would benefit from further experimentation, e.g., showcasing the results of the network to various distributions of DAGs and being explicit about any potential weaknesses. It would be nice to know where this architecture breaks down or how. robust it is to perturbations in the assumptions.

The language in lines 420-422 becomes imprecise and can lead to confusion. I would suggest sticking to a single convention here when using variables in a description. Similarly when the switch is made from using $T$ to using $W$, it's not clear why this is done and can lead to confusion.

Also, there seems to be a type on line 215 that would make a significant difference. The elements $x_1, x_2 \in \mathcal{X}$ cannot be compared using the metric from $\mathcal{Y}$. I assume you meant to say $\rho(f(x_1), f(x_2))$ not $\rho(x_1, x_2)$.

### Questions
1) In the latent space embedding, is there any guarantee that $\mathcal{E}$ maps feature vectors in such a way that the resulting embedding can be partitioned into spatial and temporal components? E.g., you embed features from $\mathbb{R}^N$ into $\mathbb{R}^{D+T}$ and later separate the embedding by slicing the results ($1:D$ and $D+1:D+T$) for use in the recursions of $\mathcal{D}$ and $\mathcal{T}$. Therefore, my question is, how do you guarantee that spatial information ends up only in the first $D$ dimensions, and temporal in the last $T$ dimensions?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Neural SpaceTimes (NSTs), a framework for embedding directed acyclic graphs (DGAs) in continuous geometries which can encode both edge weights and directionality. Unlike previous methods that use fixed spacetime manifolds, NSTs learn the geometry itself through three neural networks -- an embedding network for mapping nodes to coordinates, a neural quasi-metric network for encoding distances in space dimensions, and a neural partial order network for encoding causality in time dimensions. The authors provide theoretical guarantees showing that NSTs can universally embed any k-point DAG with low distortion while preserving its causal structure. Experiments on both synthetic and real-world directed graphs demonstrate that NSTs achieve lower embedding distortions compared to baseline methods using fixed geometries like Minkowski or de Sitter spaces.

### Strengths
* The paper is well-organized with clear problem statement , goal (Section 1), and the proposed solution (Section 3).
* The theoretical framework in Section 3 decouples spatial and temporal components while maintaining their interaction through the embedding network. 
* The theoretical development in Section 3.1 establishes embedding guarantees through Theorem 1, showing NSTs can universally embed k-point DAGs.
* The experimental validation in Section 4 demonstrates clear improvements over baselines, particularly for low-dimensional embeddings where NSTs maintain average distortion near 1.0 while other methods show much higher distortion.
* The practical applicability is well explained through the analysis of real-world networks in Table 2.

### Weaknesses
 * In Section 3.1, while the paper proves existence of neural sapcetime embeddings with low distortion, it provides limited practical guidence on selecting the number of temporal dimension. This could be important for complex DAGs where the minimal sufficient dimension is not immediately clear. Specifically, the paper lacks a discussion on how the structural properties of the DAG, such as the length of the longest chain or the width of the widest antichain, might inform the choice of temporal dimensionality. Without this, practitioners may struggle to apply the method effectively to diverse DAG structures.
* The optimization approach in Section 3.2 focuses on preserving local structure during training. While the authors provide theoretical guarantees about global structure preservation, the empirical validation concentrates mainly on local metrics. This discrepancy between the theoretical claims and the empirical evaluation raises concerns about the practical implications of the theoretical results. The paper does not adequately address how local optimization affects the preservation of global properties like path lengths or reachability between distant nodes, which are crucial for many real-world applications of DAG embeddings.

### Questions
1. How does the framework scale to very large graphs? The current larges experiment uses ~200 k nodes, but many real-world networks could be larger.
2. The local vs. global geometry optimization tradeoff warrants deeper analysis -- could hierarchical or multi-scale approaches help bridge this gap while maintaining computational tractability? 
3. While the paper shows NST can encode both local distances and causality, how well does it preserve higher-order DAG properties like path lengths between distant nodes or branching structures? This could be particularly relevant for applications like computational workflow graphs or neural architecture search where these properties are important.
4. For DAGs with hierarchical structure (like computational graphs or dependency trees), how does the learned geometry reflect this hierarchy? Additional analysis of how NSTs capture hierarchical relationships would strengthen the practical applications.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a framework of quasimetric embeddings using spacetime as the embedding manifold.

### Strengths
1. The method seems well-motivated to me. In particular, the decomposition makes sense as a space for DAG-like data, and the paper proposes a nice way of doing so with neural networks.
2. The empirical results seem promising, as the method seems to be able near perfectly embed many common DAG graph datasets.

### Weaknesses
While the paper seems to be mostly complete to me, several concerning aspects about the experiments did not sit right with me.

1. The empirical results have some concerning aspects about them. In particular, the Minkowski embedding is able to largely get to near the same final distortion on both the real world graph datasets. Since the proposed method uses neural networks as well as node features (at least for the real-world data) while the previous methods do not (as is my understanding from skimming the Law and Lucas paper), this suggests that the difference provided by the proposed method is not very large with respect to the required additional effort or that the test tasks are too simple.
2. While the distortion is near perfect, the downstream effects of using these embeddings is never studied. In particular, some GNN-type experiments would be greatly appreciated.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors introduce a novel architecture, Neural SpaceTimes (NSTs), which represents nodes in Directed Acyclic Graphs (DAGs) as events in a trainable spacetime manifold. This framework innovatively unifies spatial distances and causal directionality into a single representation space, designed to improve upon fixed spacetime geometries typically used in graph embedding. The authors implement this system through three neural networks: an embedding network, a neural quasi-metric, and a neural partial order network.

### Strengths
S1. NSTs' combination of quasi-metric spaces for spatial information and partial orders for causal information presents an elegant and flexible solution to representing DAGs.

S2. The authors provide a robust theoretical foundation. 

S3. The experimental results on synthetic and real-world DAG datasets indicate the NST’s capability to achieve lower embedding distortions.

### Weaknesses
W1. Could authors provide more explanations about the experimental results? How is NST compared to closed-form spacetimes such as the Minkowski? Why the NST is better than the closed-from spacetimes? Besides, comparison with more baselines can be more convincing.

W2. It would be good to see a time complexity analysis for the proposed NST.

### Questions
Q1. In line 215 about the metric embedding, what is $\rho(x_1,x_2)$? Since $\rho$ is defined on $\mathcal{Y}$, how can $\rho$ compute on $\mathcal{X}$?

### Soundness
3

### Presentation
2

### Contribution
3
