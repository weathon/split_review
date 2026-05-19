# From Graphs to Hypergraphs: Hypergraph Projection and its Reconstruction

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We study the implications of the modeling choice to use a graph, instead of a hypergraph, to represent real-world interconnected systems whose constituent relationships are of higher order by nature. Such a modeling choice typically involves an underlying projection process that maps the original hypergraph onto a graph, and is prevalent in graph-based analysis.  While hypergraph projection can potentially lead to loss of higher-order relations, there exists very limited studies on the consequences of doing so, as well as its remediation. This work fills this gap by doing two things: (1) we develop analysis based on graph and set theory, showing two ubiquitous patterns of hyperedges that are root to structural information loss in all hypergraph projections; we also quantify the combinatorial impossibility of recovering the lost higher-order structures if no extra help is provided; (2) we still seek to recover the lost higher-order structures in hypergraph projection, and in light of (1)'s findings we make reasonable assumptions to allow the help of some prior knowledge of the application domain. Under this problem setting, we develop a learning-based hypergraph reconstruction method based on an important statistic of hyperedge distributions that we find. Our reconstruction method is systematically evaluated on 8 real-world datasets under different settings, and exhibits consistently top performance. We also demonstrate benefits of the reconstructed hypergraphs through use cases of protein rankings and link predictions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors (a) analyze the hardness of reconstructing a hypergraph from its clique expansion, (b) propose a supervised algorithm for hypergraph reconstruction, and (c) empirically demonstrate the effectiveness of the proposed algorithm, compared to previous approaches. The proposed algorithm begins by sampling potential hyperedges based on domain-based patterns, followed by the classification of these candidates.

### Strengths
S1. The proposed formulation and algorithm are a novel blend of empirical insights and theory.

S2. The difficulty of problem at hand and the approximation guarantee of the proposed algorithm are theoretically analyzed.

S3. The proposed method reconstructs hypergraphs more accurately, compared to baseline approaches, and the reconstructed hypergraphs are shown useful for downstream tasks compared to graph representations (i.e., clique expansions).

S4. The paper is exceptionally well-written.

### Weaknesses
W1. The graph representations (e.g., clique expansions) and hypergraph representations have been compared in many contexts, which are largely ignored in the paper (see [R1]-[R3]).
- [R1] The why, how, and when of representations for complex systems
- [R2] How Much and When Do We Need Higher-order Information in Hypergraphs? A Case Study on Hyperedge Prediction
- [R3] HNHN: Hypergraph Networks with Hyperedge Neurons

W2. The comparison between the structures of the original hypergraphs and the reconstructed ones is limited, relying on basic statistical metrics. It's important to note that hypergraph structures can exhibit variations even when their basic statistics align. To conduct a more comprehensive comparison, additional measures and analytical tools should be considered [R4].
- [R4] Mining of Real-world Hypergraphs: Patterns, Tools, and Generators

W3. The algorithm is divided into two components: sampling and classification. Notably, the classification accuracy may vary across different (n,k) combinations. However, this aspect was not considered during the formulation and theoretical analysis of the sampling part.

### Questions
I served as a reviewer for this submission at other conferences and had enough opportunities to (anonymously) interact with the authors. I do not have any further questions or inquiries.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the reconstruction of a hypergraph from a projected graph. The authors propose a learning-based hypergraph reconstruction method based on their observation of the distributions of hyperedges within maximal cliques. They utilize a clique sampler and a hyperedge classifier to reconstruct hypergraphs.

The authors evaluate their method for hypergraph reconstruction and downstream tasks using the reconstructed hypergraphs. They show that their method outperforms existing methods for hypergraph reconstruction. Using hypergraphs reconstructed by their method improves performance on downstream tasks compared to using projected graphs.

### Strengths
1. This paper is well-written and easy to understand.

2. The proposed method effectively address problems with appropriate approaches.

3. It seems to provide a foundation for the underexplored problem of hypergraph reconstruction from a projected graph.

4. The experimental setup for reconstruction is well-designed and the proposed method yields good performance.

### Weaknesses
1. I'm uncertain about the necessity of addressing this problem.

2. It would be advantageous to incorporate supplementary experiments to illustrate the benefits of utilizing reconstructed hypergraphs. Although the experiments show the proposed method's strong performance in reconstructing hypergraphs, its impact on downstream tasks remains unclear.

3. In experiments for link prediction (In F.4), the authors append several structural features of hyperedges to the final link embeddings. However, in cases of projected graphs, additional structural features cannot be used. Is it a fair comparision?

### Questions
1. Could the performance improvement in experiments on link prediction have originated from the use of additional structural information?

2. Could the authors demonstrate the benefits of reconstructed hypergraphs through additional experiments?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the task of recovering a hypergraph from its projected graph (i.e., the graph formed by forming an edge between any two nodes that are a part of the same hyper-edge). 

The first main contribution is a set of theoretical results stating when it is possible to reconstruct the hyper-edges based on the maximal cliques of the projected graph, G. In particular, the authors identify two necessary and sufficient conditions for the recovery of the hypergraph from G: (1) the lack of any "nested" hyper-edges, and (2) the lack of any "uncovered triangles" (Thm 1). Moreover, when (2) is not satisfied, the reconstruction accuracy using maximal cliques can be exponentially small in the number of hyper-edges (Thm 3). 

The second main contribution is a learning-based approach that leverages side information in the form of same-domain hypergraphs to reconstruct a hypergraph from its projection. The method follows a 4-step procedure. First, the distribution of hyper-edges within maximal cliques of G is computed for the training data (the known hypergraph of the same domain); these are denoted by the $\rho(n,k)$'s. Using this information, cliques in G are sampled  in a way that is optimized for the $\rho(n,k)$'s and a query budget (since the total search space is very large). Finally, cliques are classified as hyperedges or not based on the local structure of the cliques with respect to the surrounding graph. The methodology is assessed on a variety of datasets with favorable results.

### Strengths
Reconstructing hypergraphs from their graph projections is an important task in several domains, and this is summarized very well by the authors in the introduction. This task has received little to no attention previously, making the fundamental analysis in this paper quite valuable.

The authors' contributions are substantive and fundamental, spanning both theory and practical implementations. The motivation for studying cliques is clear, and the authors derive a nice, fundamental characterization for general hypergraph recovery using maximal cliques. The authors' development of a scalable, learning-based approach to overcome the shortcomings of an approach without side information serves as a nice, practical complement to the theoretical results.

### Weaknesses
The approaches outlined in the paper are somewhat basic (which itself is not a weakness, as the problem is novel and the contributions fundamental). What are potential future directions for the design of possibly more sophisticated methods? What other types of information could be taken into account to improve guarantees for hypergraph reconstruction? Some discussion of these and related questions would be quite valuable.

### Questions
- Concerning the characterization of "conformal" in Theorem 2, it might be worth describing the explicit connection between uncovered triangles and hyper-edge reconstruction. That is, the triangle would induce a 3-clique among the "points" of the triangle, which would not be part of a hyper-edge if the triangle is uncovered. 
- Are there any natural strategies you'd expect to perform better than looking at maximal cliques, for the case of no side information?
- The notation $\mathbb{E}^c$ (denoting expected cardinality) is a bit nonstandard. Perhaps just write $\mathbb{E}[|S|]$ for the expected size of a set S.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method of constructing a hypergraph from a given graph. The proposed method includes analyzing cliques present in the graph and classifying them into potential hyperedges. The proposed method is compared against baselines, and the results show superior performance of the proposed method.

### Strengths
1. The problem is very important. Many times, getting hypergraph-based representation is hard. The proposed approach can be used to convert a graph-based representation to an underlying hypergraph.
2. The proposed approach builds on the clique finding algorithm, a known approach for finding potential hyperedges. Its key challenges, such as predicting hyperedges that are a complete subset of larger hyperedges, computational challenges, etc., are tackled well.
3. The results show that the proposed method outperforms the baseline approaches.

### Weaknesses
1. The paper lacks a comparison of their method with several other works in the domain. I have listed them in the Questions section. 
2. Writing lacks a clear outline of the contributions. In the proposed pipeline, what is already proposed vs. what is novel, is not clear.
3. The problem and solution are discussed in detail, but the experiments and results are not justified. What properties of a hypergraph make the proposed algorithm more suitable? On some datasets. The baseline methods demonstrate comparable performance; what is the reason behind that?
4. Other weaknesses are asked in the Questions section.  

Minor typos (does not affect the rating):
Page 3: as well as and

### Questions
1. Conditions stated in Theorem 1 are explained as necessary conditions to reconstruct a hypergraph from a given projection using the max-clique algorithm. But are these conditions sufficient? Is there any theoretical justification for that?
2. The clique-sampler tries to sample for as many as possible hyperedges. Will it not affect the size of hyperedges being predicted?
3. The performance of the proposed method is not very different from the baselines on hypergraphs where the average hyperedge size is large. Is there any justification for that? Also, from the predicted hyperedges, is it possible to provide a stratified evaluation to understand how the proposed method works on large vs small hyperedges?
4. Can you think of a real-world scenario where converting a graph to a hypergraph (where we know that there are underlying group interactions) is essential, and this approach can help?
5. Apart from clique-based projections, there are other hypergraph projection methods, such as the node-degree-preserving method[4]. Can this approach recover hyperedges from such projected graphs?


6. I request the authors to provide justification for the following.
a. In the Introduction section, whether the hyperedges are observable or not actually depends on the objective of experiments conducted on the system. For example, protein-protein, gene-gene interactions have semantics defined for pairwise interactions where protein complexes are inherently super-dyadic relations of proteins, and experiments observe them in the protein complex form [1].
b. Unpublished: True, author-author interaction datasets do not provide the underlying hypergraph structure, but one should go with other bibliographic datasets such as AMiner[2] to get a complete view of the system.
c. Relevance to the hyperedge prediction problem: The problem of hyperedge prediction is actually relevant. The hyperedge prediction methods consume a hypergraph as input, and the right way to see it is every graph is also a hypergraph (more precisely, 2-uniform hypergraph), and the methods [3] where a set of candidate hyperedges is not used can identify underlying hyperedges. Especially when you are using the sample hypergraphs from a given domain, methods like HPRA can generate new hyperedges using the known hyperedge degree distribution.


[1] "Hypergraphs and cellular networks." PLoS computational biology 5.5 (2009): e1000385.
[2] https://www.arnetminer.org/
[3] "HPRA: Hyperedge prediction using resource allocation." Proceedings of the 12th ACM Conference on Web Science. 2020.
[4]  "Hypergraph clustering by iteratively reweighted modularity maximization." Applied Network Science 5.1 (2020): 1-22.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
