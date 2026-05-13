# Homomorphism Expressivity of Spectral Invariant Graph Neural Networks

- Decision: Accept
- Scores: 8, 6, 8, 6, 10

## Abstract
Graph spectra are an important class of structural features on graphs that have shown promising results in enhancing Graph Neural Networks (GNNs). Despite their widespread practical use, the theoretical understanding of the power of spectral invariants --- particularly their contribution to GNNs --- remains incomplete. In this paper, we address this fundamental question through the lens of homomorphism expressivity, providing a comprehensive and quantitative analysis of the expressive power of spectral invariants. Specifically, we prove that spectral invariant GNNs can homomorphism-count exactly a class of specific tree-like graphs which we refer to as \emph{parallel trees}. We highlight the significance of this result in various contexts, including establishing a quantitative expressiveness hierarchy across different architectural variants, offering insights into the impact of GNN depth, and understanding the subgraph counting capabilities of spectral invariant GNNs. In particular, our results significantly extend \citet{arvind2024hierarchy} and settle their open questions. Finally, we generalize our analysis to higher-order GNNs and answer an open question raised by \citet{zhang2024expressive}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates the expressive power of spectral-invariant GNNs through the homomorphism expressivity perspective. The authors prove the followings: (1) projection-based spectral invariants and corresponding GNNs are strictly bounded by 2-FWL, and establish a quantitative hierarchy among spectral invariants and a family of WL-test variants; (2) increasing numbers of iterations can improve expressive power with an upper-bound; (3) substructure counting capabilities of certain spectral invariant GNNs. Experiments on synthetic and real-world datasets are conducted.

### Strengths
The paper is well-organized. The theoretical contributions are significant, addressing several remaining open questions including existence of homomorphism expressivity of certain GNN architectures. The paper quantitatively characterizes the expressivity of spectral invariant GNNs through parallel tree, establishes connections with k-FWL hierarchy, proves counting abilities of several substructures, and extends to higher-order spectral invariant GNNs. I check with proofs and they are solid.

### Weaknesses
While the paper is theoretically grounded, the experimental part could be strengthened. (1) The expressivity of spectral-invariant GNNs can be further validated on classical benchmarks of GNN expressivity, e.g., EXP, CSL, SR25, and BREC [1]. (2) The study on real-world datasets is insufficient. In many circumstances, expressive power does not necessarily determine the empirical performance on real-world datasets, so the authors should carry more extensive experiments on more benchmarks with careful tuning.

[1] Wang, Y., & Zhang, M. (2023). Towards better evaluation of gnn expressiveness with brec dataset. arXiv preprint arXiv:2304.07702.

### Questions
N/A

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the expressive power of spectral invariants in GNNs by employing a homomorphism-based approach. The authors theoretically demonstrate that spectral invariant GNNs can homomorphism-count certain tree-like structures, thus providing a quantitative hierarchy of expressiveness across different GNN architectures. This hierarchy assesses the influence of spectral invariants on the capability of counting substructures, such as small cycles. Empirical results test how homomorphism expressivity is related with performance in downstream tasks.

### Strengths
The paper is well-written and organized. The key concepts, such as spectral invariants, homomorphism expressivity, and the hierarchy of expressiveness, are presented in a manner that facilitates readability.

This analysis introduces a novel perspective, providing an alternative theoretical framework for examining the expressive power and function approximation capabilities of GNNs.

### Weaknesses
I am concerned about the significance of the paper's contributions. The work presents a limited set of novel results and falls short in advancing our understanding of the expressive power of message-passing and spectral invariant GNNs. While the paper is well-written and accessible, it does not substantially enhance our knowledge of GNN architecture or provide actionable insights for designing more efficient models.

Some important related work is missing:

Kanatsoulis, C. and Ribeiro, A., Counting Graph Substructures with Graph Neural Networks. In The Twelfth International Conference on Learning Representations.

Black, M., Wan, Z., Mishne, G., Nayyeri, A. and Wang, Y., Comparing Graph Transformers via Positional Encodings. In Forty-first International Conference on Machine Learning.

How does the submitted paper compare to these previous works?

### Questions
Please see weaknesses

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
This paper explores the expressive power of spectral invariant GNNs through the concept of homomorphism expressivity. The authors provide a framework for characterizing the homomorphism expressivity of spectral invariant GNNs and prove that such GNNs can accurately count homomorphisms for parallel trees. They establish a hierarchy comparing the expressive power of spectral invariant GNNs with other GNN architectures and demonstrate that, while these GNNs have greater expressivity than 1-WL but are bounded by 2-FWL. The paper also extends these results to understand the subgraph counting capabilities of spectral invariant GNNs.

### Strengths
The paper provides a rigorous theoretical framework for understanding the expressive power of spectral invariant GNNs, using the novel concept of homomorphism expressivity. By introducing the concept of parallel trees, authors show how spectral invariant GNNs can count homomorphisms for such structures. The authors position spectral invariant GNNs between 1-WL and 2-FWL in terms of expressive power.

### Weaknesses
* The sec 2.1, the definition of spectral invariant GNN uses a not so standard eigen-decomposition involves projection matrices. The projection matries need to be idempotent which is an extra constraint. I would expect a more detailed description of this somewhere in the paper.
* As the spectral invariant GNNs is defined differently to existing spectral GNNs such as ChebNet, GCN, etc. The connection to these classical spectral GNNs are not discussed in the paper. If they are not related, the contribution of this paper could be further limited as the results are only applicable to this GNN which can be expensive to run in practice (as it requires full eigendecomposition).
* Dicussion on related work is limited and scattered across multiple places, making it harder to understand the position of this paper in literature.

### Questions
* How does the eigen-decomposition described in sec 2.1 work? What are the methods to compute it? Complexity and is it guranteed to find these projection matrices?
* How is spectral invariant GNN relate to other spectral GNNs? Does the results in this paper apply to these GNNs?
(happy to raise score if these concerns are addressed)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper is a theoretical work, which studies the homorphism expressivity of spectral invariant GNNs, and proves the fundamental conjecture that 'spectral invariant GNNs converge within constant iterations'. Specifically, the authors show that the homomorphism expressivity of spectral invariant GNNs can be characterized by the set of parallel trees, which bridges between homomorphism and spectral invariants. The authors proves the strict order of the expressiveness of MPNN, spectral GIN, subgraph GNN, and Local 2-GNN with both theories and experiments.

### Strengths
1. The authors develop new theoretical tools, e.g. the parallel tree decomposition (Def. A.3) and pebble game for spectral IGN (Def. 3.18), to identify the quantifiable expressiveness of spectral IGNs.
2. The authors conduct empirical experiments in validating the expressiveness inequality / order of mainstream GNN structures (Table 1 and Section 3.2).

### Weaknesses
The weakness listed below does not compromise the contribution of this paper.

Although the authors have characterized the homomorphism expressivity of spectral IGNs, there still exists a gap between such expressiveness and the approximation error and generation error of practical spectral IGNs (or other GNN architectures) in machine learning practice (e.g. graph / node / edge prediction). 'Whether we can predict or bound the training / generalization error based on the proven homorphsim expressivity' seems to be a challenging open question (which is out of the scope of this paper). From my perspective, this requires to consider the homomorphism complexity of the data distribution, while this paper only focus on the expressiveness of the hypothesis set / GNN backbone.

### Questions
I wonder whether the proposed homomorphism expressiveness can help discriminating between different GNN models (w.r.t both model weights and architectures), so that one can design learning algorithms to improve the training and architecture design of GNN. Or whether this expressiveness can guide GNN designing, e.g. finding GNN paradigm that 'enjoys a larger set of  homomorphism expressiveness'.  

May the authors add some illustrations on how can the proposed quantifiable expressiveness benefit GNN learning and design? This can help audiences that do not have a learning theory / GNN expressiveness background to better feel the impact of the series of this work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The present manuscript tackles the theoretical understanding of the power of spectral invariants over graphs, in particular linking such power to the expressive power of GNNs built accordingly. The paper provides a comprehensive analysis of the expressive power of such invariants by exploiting the concept of homomorphism expressivity, which characterizes class of graphs in term of pseudo-isomorphism test algorithms, such as coloring algorithms. An experimental framework is also provided to validate the theoretical findings.

### Strengths
The manuscript presents an impressive comprehensive overview over the expressive power of spectral invariants, bridging together many elements from the literature and providing answers to open problems on the topic. 
The presentation of the paper is well structured and made very clear to the reader.

### Weaknesses
I do not find any particular flaw in the manuscript. The argumentations seem solid and the scientific analysis is carried on in a proper way.

### Questions
Corollaries 3.11 and 3.13 state that increasing the number of iterations would make the spectral invariant GNNs more powerful. How would the authors relate such a theoretical statement with the known issues of over smoothing and gradient vanishing in GNNs? A comment in this regard would be insightful.

I wonder how the datasets used for the experimental validation were selected. Is there a particular criterion?

### Soundness
4

### Presentation
4

### Contribution
4
