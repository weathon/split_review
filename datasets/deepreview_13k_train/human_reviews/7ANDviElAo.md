# Graph Sparsification via Mixture of Graphs

- Decision: Accept
- Scores: 8, 5, 8, 8

## Abstract
\vspace{-0.5em}
Graph Neural Networks (GNNs) have demonstrated superior performance across various graph learning tasks but face significant computational challenges when applied to large-scale graphs. One effective approach to mitigate these challenges is graph sparsification, which involves removing non-essential edges to reduce computational overhead. However, previous graph sparsification methods often rely on a single global sparsity setting and uniform pruning criteria, failing to provide customized sparsification schemes for each node's complex local context.
In this paper, we introduce Mixture-of-Graphs (MoG), leveraging the concept of Mixture-of-Experts (MoE), to dynamically select tailored pruning solutions for each node. Specifically, MoG incorporates multiple sparsifier experts, each characterized by unique sparsity levels and pruning criteria, and selects the appropriate experts for each node. Subsequently, MoG performs a mixture of the sparse graphs produced by different experts on the Grassmann manifold to derive an optimal sparse graph. One notable property of MoG is its entirely local nature, as it depends on the specific circumstances of each individual node. Extensive experiments on four large-scale OGB datasets and two superpixel datasets, equipped with five GNN backbones, demonstrate that MoG (I) identifies subgraphs at higher sparsity levels ($8.67\%\sim 50.85\%$), with performance equal to or better than the dense graph, (II) achieves $1.47-2.62\times$ speedup in GNN inference with negligible performance drop, and (III) boosts ``top-student'' GNN performance ($1.02\%\uparrow$ on RevGNN+\textsc{ogbn-proteins} and $1.74\%\uparrow$ on DeeperGCN+\textsc{ogbg-ppa}).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel graph sparsification method, Mixture-of-Graphs (MoG), to optimize Graph Neural Networks (GNNs) for large-scale graphs. MoG dynamically selects node-specific sparsification levels and criteria, improving computational efficiency and performance.
Inspired by the Mixture-of-Experts framework, MoG employs multiple sparsifier experts, each with distinct sparsity settings and pruning criteria. This approach customizes edge pruning for each node, addressing limitations of previous global sparsification techniques.
MoG assembles sparse subgraphs on the Grassmann manifold, enhancing graph structure while preserving node connectivity. Extensive experiments across diverse datasets demonstrate MoG’s ability to achieve significant sparsity with minimal performance loss.
The authors validate MoG’s effectiveness through experiments on large-scale datasets. MoG achieves faster GNN inference and better performance in some cases. MoG’s flexible sparsification method shows potential for advancing GNN deployment in resource-limited environments.

-----------------------------------
After reading all the responses and the improved manuscript, I think this paper can be considered to be accepted. Thus, I raised my rating to 'accept', because there is no '7'.

### Strengths
1. The experiments show the MoG's adaptability across different graph learning tasks. They also show MoG’s ability to improve inference speed while maintaining or even boosting accuracy (up to 1.74% in some cases) demonstrates its practical benefits. 
2. The paper introduces a novel method, Mixture-of-Graphs (MoG), which applies the Mixture-of-Experts (MoE) concept to graph sparsification. Unlike traditional sparsification methods with uniform criteria, MoG combines sparsity levels and pruning criterias to each node’s local context.
3. The paper clearly defines the MoG framework, including the sparsifier expert selection process, node-wise routing, and mixture on the Grassmann manifold. The mathematical framework is well-detailed, particularly in describing the sparsifier expert selection via the noisy top-k gating mechanism and the Grassmann manifold’s role in mixing sparse subgraphs.
4. MoG's ability to achieve significant sparsity without a substantial performance drop highlights its potential to improve GNN deployment in resource-limited environments. By effectively balancing computational efficiency and accuracy, MoG could effectively serve as a plugin to boost GNN performance, from real-time social network analysis to large-scale molecular data processing.

### Weaknesses
1. The paper does not clarify in “4 EXPERIMENTS” or “Appendix F.6” why the specific 12 combinations of sparsity levels and criteria were selected. Additionally, the variance of each row across combinations in Table 8 is minimal, raising questions about the distinctiveness of each sparsifier. Furthermore, in “Appendix F.6”, different sparsity criteria are applied in different datasets without an explanation of the selection rationale. To enhance experimental completeness, the authors might consider exploring a wider range of sparsity combinations with greater variance. Additionally, providing the reasoning behind dataset-specific combinations would help readers understand the adaptability of MoG across different graph structures.

2. The process of integrating sparse subgraphs on the Grassmann manifold, as outlined in Section 3.4, is mathematically dense and lacks intuitive explanation. While the theoretical basis is strong, the connection between the Grassmann manifold’s properties and its benefits for graph sparsification may not be immediately clear to all readers.

3. The terminology for sparsifiers and experts appears inconsistent across sections, which could lead to confusion. For instance, “sparsifier experts” and “experts” are used interchangeably.

Minor Comment:
4. In Section 2, there is a spelling error in the title “TECHNICAL BACKGOUND,” which should be “TECHNICAL BACKGROUND.” I recommend reviewing the document to ensure there are no similar spelling errors throughout.

### Questions
Please refer to the weaknesses above.

### Soundness
3

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
This paper proposes a method called **MoG**, which uses the technique of MoE to integrate multiple ego-net sparsifier strategies in GNNs. 

First, for each ego-net, the authors introduce a simple noisy top-k gating mechanism as a routing module to select K sparsifier experts, each with different sparsity levels and sparsification strategies. 

Then, using Grassmann manifold techniques, the authors combine these sparsified ego graphs, with objective function Eq.11 and its closed-form solution in Eq.12.

The experiments show that compared to other sparsification methods:
- In terms of accuracy, MoG has a slight advantage in two node classification datasets and a more noticeable effect in two graph classification datasets.
- In terms of balancing inference speed and accuracy, MoG achieves higher accuracy when reaching the same speedup.

The authors also conducted additional experiments, such as sensitivity analysis.

### Strengths
1. The proposed method has a certain degree of innovation, especially in the use of MoE and the approach to combining graphs.
2. The proposed method can be integrated with any framework.
3. The paper includes extensive experiments.

### Weaknesses
 1. Eq.11 is a core objective, but it is quite heuristic. Moreover, after obtaining the combined graph with Eq.12, there is a post-sparsification operation. Does the final ensembled sparse Laplacian truly integrate the eigenvectors of multiple sparsified ego-net Laplacians as the authors hope? Regardless of the degree achieved, it would be helpful to see experimental evidence here. Specifically, it's unclear how the Grassmann manifold optimization in Eq. 12 ensures that the spectral properties of individual sparsified Laplacians are preserved in the final ensembled graph, especially given the subsequent post-sparsification. The post-sparsification step could potentially negate the benefits of the Grassmann optimization if it significantly alters the spectral characteristics. A more detailed analysis of the eigenvalue distributions of the individual sparsified Laplacians, the intermediate result after Grassmann optimization, and the final post-sparsified Laplacian would be beneficial to validate the claim of spectral property preservation.

2. There are only two node classification and two graph classification datasets, which is relatively few.

### Questions
Please check weakness 1.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a mixture-of-graphs (MoG) approach inspired by mixture-of-experts for graph sparsification. Instead of having global/uniform pruning criteria, they create a dynamic strategy tailored to each node’s neighborhood. This is done by utilizing each node’s egograph to select a few sparsifiers (experts) from a larger pool. The outputs of selected sparsifiers are ensembled using Grassmann manifold theory to generate a single sparsified ego graph per node and are later re-combined to form the final graph. Their approach outperforms baselines across several datasets, maintaining performance at higher sparsity levels and sometimes even improving it due to reduction of noise after sparsification.

### Strengths
1. Tackles a topical and highly relevant problem in graph learning on large graphs.
2. Highly flexible, well-motivated approach that accounts for local node variations while determining optimal pruning strategy.
3. Ample experiments across baselines and datasets, replete with sensitivity analysis, ablation studies, and efficiency comparison.

### Weaknesses
Adding below-mentioned minor clarifications around methodology may be useful:

1. How are post-sparsified ego-graphs assembled? Is it possible that for two nodes $i$ and $j$, the post-sparsified ego graph of $i$ connects to $j$ but the post-sparsified ego graph of $j$ doesn’t connect to $i$? If yes, how is this handled?
2. How do we select $p$ in equation 10? What is its impact on performance?
3. What does $D$ in eq. 13 correspond to? Is it from the original ego graph of the given node? If yes, why do we use the same $D$? Would it not introduce some approximation error since it doesn’t correspond exactly to the learned laplacian?
4. The method seems entirely local. For some downstream tasks, it may be relevant to take the global graph structure into consideration, for example, to ensure the graph stays connected. How does the proposed approach tackle this?

### Questions
A couple of questions on output:

1. In figure 1 (Middle), we attribute edge pruning to different sparsifiers. Did we perform this qualitative analysis on an actual sparsified graph, or is it an imagined example to represent our hypothesis? Although not required to perform this if not done already, I was simply wondering if it was the case and was interested in knowing more about it.
2. What is the difference between observed average sparsity just after ensembling in eq. 13 and after the post-sparsification step of eq. 14? Curious to understand how much more the graph density changes after the optimization in eq 11.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work leverages the Mixture-of-Experts (MoE) approach, a well-established technique in deep learning domains such as language modeling, to scale model capacity (i.e., the number of parameters) while managing computational demands. In this context, the MoE concept is applied dynamically and locally sparsity to the underlying graph during GNN inference. The authors demonstrate that this method maintains performance while reducing inference time.

### Strengths
I thought the writing was clear for the most part, with the exception being the contributions/intro (see Weaknesses). The figures are excellent. I haven't seen prior work on MoE re: sparsity, so I believe it to be original, although not very confident. 

&nbsp;

This work could be significant. Indeed, GNN inference cost has motivated much GNN research in the past; see Questions for more of my thoughts on this.

### Weaknesses
 **Making Contributions Clear**

I suggest making more clear the contributions of the paper and what the authors are claiming novelty on. Many papers use bullet points at the end of the introduction section to denote this; this work has bullet points near the end of the introduction, but they do not correspond to contributions, making the reading a bit confusing for regular readers of ICLR proceedings.

&nbsp;

**Some Missing Background in Graph Sparsification**

There is extensive literature on graph sparsification coming from the statistics and optimization world, commonly referred to under the umbrella term ‘Graph Structure Learning’. Most of these approaches indeed use some global sparsity promoting criteria; you could state how your approach has advantages over this more coarse approach. I include references to a classical work and a recent work. The latter has an overview of recent Graph Structure Learning approaches, most of which indeed use some global sparsity criterion in their objective.

&nbsp;

Friedman, Jerome, Trevor Hastie, and Robert Tibshirani. "Sparse inverse covariance estimation with the graphical lasso." Biostatistics 9.3 (2008): 432-441.

Wasserman, Max, and Gonzalo Mateos. "Graph Structure Learning with Interpretable Bayesian Neural Networks." Transactions on machine learning research (2024).

&nbsp;

**Missing Experiment/Ablation Study**

A simple baseline I expect to see would be to somehow prune the graph to a particular sparsity level and run a GNN on that. Perhaps some sort of edge sampling procedure selects a subset of edges to prune such that the global sparsity is set to ~=x, perhaps preferring edges to remove in proportional to the adjacent nodes' degree, while ensuring no disconnected nodes. Do so for a few sparsity levels. This would provide a good idea for how much benefit is really to be gotten from this whole effort, beyond the straightforward pruning approach.

Perhaps this ablation study is done implicitly in one of the baselines. Please correct me if so.

### Questions
**Significance**

Is there a real use case the authors can point to where SpMM compute limits people who are using/want to use GNNs? In my opinion, the significance of this type of ML research is measured by the significance of the problem it is solving/the capability it unlocks. Otherwise this is a more of a neat contribution to the literature which we simply speculate to be useful eventually.

&nbsp;

**The use of Gaussian Noise in the MoE step**

Perhaps I show my naivety re: MoE, but why do we believe added \epsilon \sim N(0,1) noise is of a suitable scale to effectively alter the routing? Is there a particular normalization of activations to ensure \epsilon interacts with numbers of this scale?

### Soundness
4

### Presentation
4

### Contribution
2
