# LINK PREDICTION USING NEUMANN EIGENVALUES

- Decision: Reject
- Scores: 3, 3, 6, 8

## Abstract
Recently, graph-structured data benefits from the advent of Graph Neural Networks (GNNs). Link prediction (LP) is a crucial task in graph-structured data, aiming to estimate the likelihood of non-observable links based on known graph structure and node/edge features. Despite GNN's success in solving graph-level tasks, their results, compared to classical methods, are worse in solving node-level tasks (e.g., LP). The main reason lies in the limitations of Message Passing GNNs (MPNNs), the most common technique used in GNNs. One of the main limitations of MPNNs is their inability to distinguish between some graphs, e.g., k-regular graphs. Discriminating between k-regular graphs lets us count the sub-structures and triangles, which are crucial in the success of classical methods for the LP task. Encoding Link representation instead of node representation can solve this problem, but the previous methods are prohibitively expensive and thus impractical. We propose a novel light learnable eigenbasis to encode the link representation and induced subgraphs efficiently and explicitly. Specifically, we introduce Neumann eigenvalues and encode its corresponding constraints to the eigenbasis. Given the Neumann constraints, the Neumann basis splits the nodes into two (one-hop and two-hop away nodes) and efficiently encodes the relation between them. By formulating the eigenvalue problem with linear constraints, we efficiently implement our proposed convolutional layer with a novel learnable Lanczos algorithm with linear constraints LLwLC. We also conducted experiments investigating the effect of encoding different linear constraints (subgraphs). Although our theoretical results apply to many problem settings, we report our results on link prediction tasks achieving state-of-the-art in benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper generalizes LanczosNet for representation learning of induced subgraphs for link prediction by formulating subgraphs as Neumann boundary conditions of the eigenvalue problem, which is solved by the Lanczo algorithm with linear constraints. As a result, a new expressive feature based on Neumann constraints is proposed to mitigate the limited expressive power of MPNNs. The proposed model LLwLC is evaluated on four citation networks and shows its effectiveness.

### Strengths
- A new type of structural feature is proposed, which shows its effectiveness in enhancing the MPNN framework.
- The proposed model builds a connection between spectral graph theory, numerical analysis, and subgraph-GNN.

### Weaknesses
- The benefit of introducing the proposed Neumann feature is debatable for link prediction. It shows that the node automorphism issue is addressed, but the model still depends on instance features for more expressiveness. Particularly, SubGNNs with simple features of low computation cost (e.g. zero-one labeling or DRNL) are already good enough, and the ablation study does not exactly separate the contribution between them.
- LLwLC is claimed to be lightweight and efficient, However, neither the theoretical complexity nor the wall-clock time is provided. Meanwhile, the proposed model is subgraph-based, which still suffers from the computation overhead of subgraph extraction and raises my concerns over its scalability on larger graphs (other OGB LP benchmark datasets).
- The organization of the paper needs some polishing, especially clearly establishing the connection between Neumann constraints and subgraphs, better illustration of figures, and differentiating the content/contribution from [1] for the result of numerical analysis. More comprehensive experiments including large-scale datasets, stronger baselines, clearer ablation studies, and runtime comparison are needed.

[1] Golub, Gene H., Zhenyue Zhang, and Hongyuan Zha. "Large sparse symmetric eigenvalue problems with homogeneous linear constraints: the Lanczos process with inner–outer iterations." Linear Algebra and its Applications 309.1-3 (2000): 289-306.

### Questions
* Is the proposed Neumann features only beneficial for the node automorphism issue? Can it also address the limitation of MPNN in counting sub-structures and triangles (other than the expressiveness inherited from subgraph-based models)?
* SEAL and BUDDY are not necessarily limited to 2-hop neighborhoods (the former is limited by scalability, the latter can be applied to arbitrary $k$ order). Can the Neumann basis be applied to more than 2-hop?
* It would be great to have a detailed example of Fig. 1 to show the construction of linear constraints.
* What is the complexity of the proposed method to extract a bag of subgraphs, obtain $\delta S$, and construct $C$ for each link?
* Technical detail:
  - Sec. 2 Related Work, the embedding methods are (not) inductive? 
  - The iteration of sample Lanczos from [1] starts from $k=0$ while $j=1$ in LanczosNet. The inconsistency causes confusion about the iteration of the Lanczos Algorithm in introduced Sec 3, especially the coefficients of $q_{j-1}$, $q_{j+1}$.
  - What does it mean that “SEAL does not encode the pairwise node representation”? SEAL converts the link prediction as subgraph classification, which encodes the induced subgraph of two queried nodes with their distance labels. A similar framework is also adopted by LLwLC.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In link prediction, because existing works of encoding link representation are prohibitively expensive，this paper proposes a novel light learnable eigen basis to encode the link representation and induced subgraphs efficiently and explicitly. Experiments shows the efficacy of the proposed method, and achieve the SOTA in benchmark datasets.

### Strengths
The proposed method is effective on some common datasets.

### Weaknesses
1. The writing of this paper is poor. For example, I cannot understand the motivation of this article from the introduction section. On the contrary, there is too much content about existing work in the introduction. Still, I cannot see the connection between these existing methods and the proposed method from this section.
2. What is the relationship between LLwLC and link prediction? LLwLC is only designed as a matrix factorization method for GNN.
3. This paper states that LLwLC has improved the efficiency of encoding link representations, but no specific form of link representation is mentioned in Section 4.
4. The conclusion of this article is not clear and requires a comparison between different methods, such as NBFNet and Seal, in terms of their link representation approach and complexity.
5. It is necessary to compare the running time to show the efficiency of the proposed method.
6. It is better to compare more methods on Ogbl-Collab. Currently, only LanczosNet is compared.

### Questions
See weakness

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new algorithm to perform Link Prediction/Classification. The main idea is to encode subgraph information via a captured eigenbasis of a constrained Laplacian matrix. According to the paper, the new basis makes the features more expressive by explicitly encoding the linear constraints over the graph. Numerical experiments verify the effectiveness of the new algorithm.

### Strengths
-) The paper considers important and relevant problems.
-) Numerical experiments suggest that the proposed algorithm can attain high accuracy versus other competitive approaches.

### Weaknesses
-) The paper is not very clear. I had to repeat many sentences several times in order to understand what the authors aimed to state. 
The language also needs improvements.
-) Wall-clock time comparisons are absent.
-) The new algorithm seems to be a relative minor extension, especially the parts related to Lanczos and its theoretical analysis. What is the novel theoretical analysis? Most results are standard from what I know in the subject. Please elaborate more on these two fronts.

### Questions
-) "Proposition. If we start simple Lanczos with ν ∈ N (C⊤), then qj ∈ N (C⊤) for all j." This is true only in theory as in practice round-off errors re-introduce the deflated direction. This is well-known in numerical linear algebra and Lanczos is very rarely used without some form of restart precisely for this reason.

-) In Figure 2, purple box: you mention "svd(T)" but it is clear you mean "eig(T)".

-) The statement about the orthogonal projector is wrong. C(C^TC)^{-1} holds for the case of independent rows in C; instead, in your case you have linearly independent columns thus it should be  (C^TC)^{-1}C^T. You can verify then that P=I-C(C^TC)^{-1}C^T is what you want, and not P=I-CC(C^TC)^{-1} which the math indicate in your paper (the multiplication CC is not even defined).

-) The discussion in Sections 4.2 and 4.3 are basically straightforward and read as textbook-style material. I would remove both.

-) The results indicate superior performance for LLwLC but no timings are shown. In other words, higher accuracy should not be accompanied by high costs. Indeed, the authors do a lot more work per Lanczos step via LSQR -- this is essentially applying Lanczos 
with shift-and-invert.

-) The keyword 'Neumann' keeps appearing only to be explained on page 7.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on link prediction tasks in GNNs. It addresses the issue of traditional GNNs being unable to distinguish between some graphs due to their message-passing structures. The authors tackle this challenge by proposing a novel learnable Lanczos algorithm with linear constraints, LLwLC. Specifically, the authors extend the Lanczos algorithm and project the approximated eigenvectors with a Neumann constraint matrix to efficiently encodes the relation between nodes. The experimental results demonstrate the effcitiveness of the proposed algorithem in link prediction tasks.

### Strengths
+ The paper is technically solid and introduces a novel spectral GNN structure, offering an insightful exploration of utlizing linear constraints on subgraph structures in eigenspaces.
+ The proposed LLwLC has the capability to distinguish the k-regular graphs, which is an improvement over the MPNNs.
+ Experimental results show the effectiveness of the proposed LLwLC in link prediction tasks.

### Weaknesses
- The language and presentation of the paper could be further improved, particularly in figures and visual representations. (e.g. Figure 2).
- While the paper is designed for link prediction tasks, the motivation behind applying LLwLC in link prediction is not well-explained, especially given that the propagation process appears to be a learnable spectral graph filter. It would be helpful to clarify why LLwLC is particularly suited for link prediction tasks.
- Though the authors have demonstrated that the expressiveness LLwLC propagation is superior to MPNNs on k-regular graphs, they are still a limited subset of all the 1-WL isomorphism graphs.
- The implementation of the proposed model is not accessible, which makes it difficult for others to reproduce the experiments and further validate the results.

### Questions
1. What motivated the application of LLwLC in link prediction tasks? How does the model's performance compare in other node-wise downstream tasks, such as node classification?
2. Can you proof the superiority of LLwLC over MPNNs on a wider range of 1-WL isomorphism graphs?
3. Can you provide information about the computational complexity of the proposed LLwLC algorithm?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
