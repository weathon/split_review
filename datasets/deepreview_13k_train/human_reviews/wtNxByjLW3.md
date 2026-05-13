# Identify Dominators: The Key To Improve Large-Scale Maximum Inner Product Search

- Decision: Reject
- Scores: 6, 5, 6, 1, 6

## Abstract
Maximum Inner Product Search (MIPS) is essential for machine learning and information retrieval, particularly in applications that operate on high-dimensional data, such as recommender systems and retrieval-augmented generation (RAG), using inner product or cosine similarity. While numerous techniques have been developed for efficient MIPS, their performance often suffers due to a limited understanding of the geometric properties of Inner Product (IP) space.  Many approaches reduce MIPS to Nearest Neighbor Search (NNS) through nonlinear transformations, which rely on strong assumptions and can hinder performance. To address these limitations, we propose a novel approach that directly leverages the geometry of IP space. We focus on a class of special vectors called dominators and introduce the Monotonic Relative Dominator Graph MRDG, an IP-space-native, sparse, and strongly-connected graph designed for efficient MIPS, offering theoretical solid foundations. To ensure scalability, we further introduce the Approximate Relative Dominator Graph (ARDG), which retains MRDG’s benefits while significantly reducing indexing complexity. Extensive experiments on 8 public datasets demonstrate that ARDG achieves a 30% average speedup in search at high precision and reduces index size by 2x compared to state-of-the-art graph-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes ARDG as a new proximity graph index for maximum inner product search (MIPS). The observation is that only some vectors in the dataset can be the results of MIPS, which is called dominators. ARDG connects each vector to its nearby dominators and prunes the edges of the graph. Empirical results show that ARDG improves existing indexes for MIPS.

### Strengths
1.	The concept of dominators for MIPS is novel.

2.	Extensive theoretical analysis is conducted for the algorithm designs. 

3.	The empirical results are good, showing large performance improvements over existing methods.

### Weaknesses
1.	The discussions of related work can be improved. In particular, [1] first uses IP-Voronoi cell, and it is natural that only vectors with a non-empty Voronoi cell can the results of MIPS (i.e., dominators in the paper). [2] is the first to observe that MIPS results cluster around large-norm vectors. [3] is a seminal work for LSH-based MIPS, and [4] is an important vector quantization method for MIPS.

2.	Presentation can be improved.
(1)	Algorithm 2 requires to connect each vector to its local dominators. What is the complexity of finding the dominators of a dataset?
(2)	The dominator ratio of the datasets (Table 2 in Appendix C) can be reported in Table 1of the paper.
(3)	Some index building time results (e.g., for the large datasets) can be included in the main paper.

3.	Experiments can be improved.
(1)	The implementation paragraph in Section 5.1 says that for each index, a unified parameter configuration is used for all datasets. This is not the common practice for evaluating vector search indexes as the index parameters (e.g., out-degree, ef-search) are usually tuned for each dataset. Please be carful to separate the tuning and search queries.
(2)	Section 4.1 first connects each vector to its local MIP neighbors and then conducts pruning. An ablation study for the pruning may be conducted.
(3)	The paper can report some results of searching other values of k (e.g., k=10, 20, 50). To save space, the main paper may only use the million-scale or larger datasets, while the results for the small datasets may be reported in the Appendix.

### Questions
How to identify the dominators for a vector dataset? What is the complexity of this step?

### Soundness
3

### Presentation
2

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
The paper is on the Maximum Inner Product Search (MIPS) problem in high-dimensional  spaces.  This is a well-motivated "nearest-neighbor"-type (NN) problem in IR and related fields.  A common way to solve it is to reduce it to a standard NN problem on the Euclidean space, which is far better understood.  But this is not good in many settings.  The paper aims to study the problem directly in the Hilbert space.  Note inner product is a similarity metric and not a distance metric.  Hence properties such as the triangle inequality do not hold in this inner product space.  The main tool in the paper is to explore the Voronoi cells and the associated Delauney graph, induced by the data.  

The paper has two contributions from a technical point of view.  The first is to identify self-dominators as an important subset of data for MIPS purposes; there is natural associated graph called Monotonic Relative Dominator Graph (MRDG).  The second is to approximate MRDG by edge pruning to obtain ARDG - which has better computational properties.  It reduces the indexing costs from $O(d n^2)$ to 
 $O(nd (\log n + r^2))$, where $r$ is max of 2-hop neighborhood size.  

The paper performs detailed experiments on public data to show 30% speed up over existing methods.

### Strengths
* The MIPS problem is an important problem in information retrieval and NLP settings
* The paper shows good experimental results - a 30% improvement on public datasets over some existing methods is a decent practical win

### Weaknesses
* The novelty is on the low side. The paper is not the first one to study the geometry of the IP space. For example, the paper of Mozorov and Babenko (NIPS 2018) [1] studied the Voronoi cells and their properties. Algorithm 1 is from there. It it likely that there are even earlier references. The paper also uses observations from the prior work of Liu et al (AAAI 2020) [2] and Tan et al (EMNLP 2019) [3], to motivate self-dominators. The MRNG notion seems to be from Fu et al. (VLDB 2019) [4].

* The theoretical contributions are not compelling. Theorem 2 is a straightforward and special case. Theorems 3 & 4 are equally straightforward, with Theorem 4 largely built upon [4]. Specifically, Theorem 2's reliance on i.i.d. normal vectors significantly limits its applicability to real-world datasets, which often deviate from this idealized distribution. While Theorem 4 builds upon existing work, it fails to provide substantial new insights into the problem's inherent complexity or offer novel bounds for the proposed algorithm's performance under more general conditions.

* The paper is based on heuristic approaches for a problem where nice algorithmic ideas are likely to exist (as seen in some previous works). The theoretical contributions can be completely discounted and the paper's merits stands only on the practical wins. The reliance on heuristics, such as the edge pruning strategy to obtain ARDG from MRDG, raises concerns about the algorithm's robustness and generalizability. Without a more rigorous theoretical analysis, it is difficult to assess the algorithm's performance guarantees and its sensitivity to variations in data distribution and dimensionality.

* The paper suffers from extremely poor writing. There are many typos and overstated claims in the text. 

Theorem 2: overclaimed - special case - vectors are iid and normal. 

Main contribution:

In what way ARDG approximates MRNG?

Minor comments:

l22: theoretical solid foundations -> solid theoretical foundations

l39: overstatement: deep understanding of the geometric properties of the inner product (IP) space remains elusive

l53: strongly connected to self-dominators? please explain

l56: what is the expectation over?

l57: what is $n$?

l74: preliminary -> preliminaries

l77: represents -> represent

l89: "IP is not a typical metric": what is typical

l135: frequent index rebuilding: unclear what is meant here

l145: $x_i$ is contained in $V_{x_j}$; Need to explain why this asymmetry while the edge you add is bidirectional. Also explain if $x_i$ contained in $V_{x_j}$ woudl imply $V_{x_i} \subseteq V_{x_j}$? IP Voronoi cells behave differently from Euclidean Voronoi cells and it is better to explain things clearer since most readers will be familiar with the latter. For eg, in the case of inner product the Voronoi cells for some points are empty.

l173: exloring -> exploring

l175: Something that could be clarified with this definition: if $V_x$ is the Voronoi cell of $x$, then by Definition 1, isn't it the dominator as well? Ie, the conditions in Definition 1 and Definition 3 look identical. 

l177: "finite full coverage of": explain what you mean

l178: ${\cal S}_{dom}$ dominator set never defined 

l183: Why is this a Theorem. This seems like a definition.

l191: should it be $||x||^2$?

l219: overclaimed: this statement assumes that the dataset comes from the iid normal. The text is written as if it holds for all datasets.

l328: How do you justify the assumption that $r$ is a constant?

l461: overclaimed: Many other papers have investigated this problem

l703: Proof - doesn't these follow from prior work?

### Questions
What is the notion of approximation are you using for ARDG?  It appears to be just a heuristic.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a graph-based ANN method for MIPS. The experiments on public datasets show that the proposed method achieves a 30% average speedup in search at high precision compared to state-of-the-art graph-based methods.

### Strengths
S1. This paper proposes a simple but effective method for selecting edges in proximity graph. The procedure adapts the edge selection procedure in HNSW to the MIPS context.
S2. The discussion of self-dominator makes the proposed method intuitive. 
S3. The empirical evaluations show that the proposed method outperforms baselines.

### Weaknesses
W1. Line 130: "the Mobius transformation normalizes each vector p \in R^d to p/|p|". This is incorrect. In Zhou et al., 2019, it should be p/(|p|^2). The Mobius transformation is not a normalization, instead, it maps the vectors with larger norms closer to the zero point for faster searching in the proximity graph.

W2. The author claims the transformation method introduces data distortion, which is not clearly explained. I would suggest the author to illustrate why this distortion is problematic. For example, followed by W1, the Mobius transformation is only applied on the data during the indexing stage. On the searching time, original data is employed to compute the inner product. What are the disadvantages of this transformation?

W3. Algorithm 1 is unclear and incorrect. R should be a min heap instead of max heap because it maintains the current most similar vector ids and always pops out the worst one within the heap. The batch_insert function is not explained.

W4. The experiments is slightly flawed. "For query execution, we disable additional compiler optimizations and use same number of threads to ensure a fair comparison" What is the additional compiler optimizations? Since the query time is the main comparison in the experiment, I assume we should enable all optimizations (which reduces the implementation gaps) to show

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The article proposes a graph method called Approximate Relative Dominator Graph (ARDG) for approximate maximum inner product search (MIPS). The article begins by exploring the properties of the Voronoi diagram and its dual, Delaunay graph, when defined under the inner product (IP) instead of the Euclidean distance. The authors call a database point that belongs to its own IP-Voronoi region (the IP-Voronoi region corresponding to the database point $x_i$ is a region of points whose inner product with $x_i$ is larger than their inner product with any other database point) a self-dominator. The proposed method is based on (approximately) identifying the self-dominators, and building a graph that maintains sparse connections between them. According to the empirical results, the proposed method outperforms the earlier MIPS methods.

### Strengths
The exploration of the geometric properties of the inner product is interesting. The indexing methodology is novel as far as I know. According to the experiments, the proposed method performs well.

### Weaknesses
There are so many unclear parts and outright errors in the article that I find it very hard to read. For instance:

- In the illustration of IP-Delaunay graph in Figure 1 (b), there are connections between some of the ordinary (non-dominating) points that belong to the adjacent IP-Voronoi cells. But these connections do not follow from Definition 2 (according to Definition 2, there should only be connections between the dominators of the adjacent cells, and between a point and the dominator of the cell that point belongs to).
-  The definition of the IP-Delaunay graph (Definition 2) is different than the definition given in the earlier literature, but no explanation is given for this different definition (see Questions).
- In Figures 1 (c) and Figures 1 (d) the point at approximately (-0.4,-0,8) is an out-dominator and should be dark green.
- In Figure 1 (g) labels refer to out-dominators 4 and 5 that do not exist.
- The claim of Theorem 1 is not well-defined (see Questions).
- Figure 1 (c) claims to illustrate the NDG graph built by the algorithm described in the claim of Theorem 1. However, for any point $x_i$, the algorithm given in Theorem should produce edges between $x_i$ and all the self-dominators $\mathcal{S}_{dom}$. In Figure 1 (c), there is only an edge between $x_i$ and the dominator of the Voronoi cell the point $x_i$ belongs to (In addition, there is an edge between the point at (-0.4,-0,8) and the out-dominator. This edge should not exist according to the algorithm given in Theorem 1). 
- Given Definition 1, Definition 3 is superfluous. You should remove Definition 3 and simply say in Definition 1 that the associated vector $x$ is called a dominator.
- The claim of Theorem 2 does not hold. Clearly the dataset size $n$ affects the probability that a dataset point with a given norm is a self-dominator, and this probability goes to zero as $n$ grows to infinity by the law of large numbers. You are computing a probability that _one_ random vector whose components are drawn i.i.d. from $N(0,1)$ dominates a point with a norm $r$.

These examples are only the ones I found when carefully reading the first couple of pages of material. Based on this, I can only assume that the rest of the article is of equally low quality.

In addition to the errors in the theoretical material, the empirical evaluation is insufficient. The authors admit that the algorithms are not fine-tuned for the benchmark data sets and claim that this favors algorithms with low parameter sensitivity. However, I do not think this is a fair setting for a comparison. This is because naturally authors (in general) are always more aware of the sensible hyperparameter settings of their own algorihm (and spend more time and effort for choosing the hyperparameters) compared to the baselines. Consequently, baseline methods are often tested at sub-optimal hyperparameter combinations, which distorts the results. For instance, in this case the authors state that the baselines Fargo and ScaNN are absent from some figures (e.g., Deep10M) due to instability that worsens as cardinality and dimensionality increase. But this is almost surely because of insufficient hyperparameter grids. The benchmark data sets are small or moderate-sized, and ScaNN should have no issue at all with these data sets if hyperparameters were even in the ballpark.

Thus, I see that there are only two ways to ensure a fair performance comparison: (1) to enable the authors of the baseline algorithms to select their own hyperparameter grids, as is done in ANN-benchmarks (Aumüller et al., 2020) that is the gold standard for the performance evaluation in the field; or (2) to carefully tune the hyperparameters of the baseline methods to ensure that the algorithms are compared at near-optimal hyperparameter settings.

In summary, the technical quality of the article is very low, and it is clearly sent unfinished. There is no way the article can be accepted for this conference. However, the approach is interesting and the results seem promising, so I recommend that authors continue working on the manuscript.

### Questions
(1) What you exactly want to prove in Theorem 1? I cannot parse the claim. The theorem claims that Naive Dominator Graph (NDG) can be build by a given algorithm, but NDG is not defined anywhere. Or is the claim that the graph built by the algorithm (and that you call NDG) given in the claim is strongly connected? If this is the case, what means a strongly connected NDG $\mathcal{G}$ on the dominator set $\mathcal{P}$? I know what is a connected graph, but i do not know what is the meaning of a connected graph on a subset of nodes. Do you mean that the nodes $\mathcal{S}_{\mathrm{dom}}$ are connected to each other? Finally, strong connectivity is a property of directed graphs, whereas you build an undirected graph (you should simply say that the graph is connected). 

(2) Why do you redefine IP-Delaunay graph (Definition 2) differently from earlier literature (Morozov & Babenko 2018)? You add an edge between a point $x_i$ and the dominator of the Voronoi cell the point $x_i$ belongs to. Morozov & Babenko (2018) prove (Corollary 1) that greedy search in any graph that has an IP-Delaunay graph (their definition) as a subgraph always converges to the exact solution of the MIPS problem. Hence, what is the motivation of adding extra edges?

Morozov, Stanislav, and Artem Babenko. "Non-metric similarity graphs for maximum inner product search." Advances in Neural Information Processing Systems 31 (2018).

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies a graph-based algorithm for maximal inner product search (MIPS). Compared to previous solutions that reduce MIPS to nearest neighbor search (NNS), this paper leverages the intrinsic geometry of the inner product space. The authors provide a theoretical running time analysis for randomly generated data. Experiments verify that the proposed method provides better query performance score (QPS) compared to other baselines by a significant margin.

### Strengths
1. I appreciate the authors for choosing a meaningful yet often overlooked problem, as maximal inner product search (MIPS) is usually reduced to nearest neighbor search (NNS).
2. Both theoretical and empirical results are provided for the proposed method. I especially appreciate the worst-case analysis in the appendix, as many similar papers on graph-based search algorithms often overlook their worst-case behaviors. You can find some similar works that focus on the worst-case analysis of NNS. Regarding the experimental results, I commend the authors for their efforts in including a diverse range of datasets and baselines.
3. The paper is clearly written and easy to follow.

### Weaknesses
1. The algorithmic framework is not novel compared to many graph-based algorithms for nearest neighbor search (NNS). For example, it first proposes a new graph with a defined property, proves some convergence bounds under random data distribution, and then adds heuristics to make it empirically fast. This approach mirrors the structure of many existing graph-based NNS methods, such as those based on proximity graphs or navigable small-world graphs. The core idea of constructing a graph where proximity reflects similarity, and then using graph traversal for search, is not a new concept in this field. The specific graph construction and traversal details might differ, but the overall framework is quite similar.

### Questions
n/a

### Soundness
4

### Presentation
4

### Contribution
3
