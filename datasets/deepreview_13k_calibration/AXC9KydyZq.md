# M3C: A Framework towards Convergent, Flexible, and Unsupervised Learning of Mixture Graph Matching and Clustering

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Existing graph matching methods typically assume that there are similar structures between graphs and they are matchable. However, these assumptions do not align with real-world applications. This work addresses a more realistic scenario where graphs exhibit diverse modes, requiring graph grouping before or along with matching, a task termed mixture graph matching and clustering. We introduce Minorize-Maximization Matching and Clustering (M3C), a learning-free algorithm that guarantees theoretical convergence through the Minorize-Maximization framework and offers enhanced flexibility via relaxed clustering. Building on M3C, we develop UM3C, an unsupervised model that incorporates novel edge-wise affinity learning and pseudo label selection. Extensive experimental results on public benchmarks demonstrate that our method outperforms state-of-the-art graph matching and mixture graph matching and clustering approaches in both accuracy and efficiency. Source code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author(s) introduce a manner to jointly solve the problem of graph matching and graph clustering. For, they propose an objective function and develop an algorithm in the framework of Minorize-Maximization. The resulting method is called M3C, after adding a relaxation of the hard cluster assignment. The last element of the work is to embed the M3C method into a learning framework for the affinity matrices, so that the method becomes unsupervised.  Numerical experiments study the usefulness of the proposed method.

The contributions are :
i) the proposition of the joint matching and clustering for graphs, and that is interesting
ii) the algorithm to solve that, involving MM, then relaxation of the hard assignment matrix, and then the plugging into deep learning methods so as to obtain an unsupervised version. 

All that is moderately original, still it has the advantage that it appears to work.

### Strengths
- A sound problem, to try to study jointly matching and clustering for graphs

- The theoretical parts, often postponed in the supplementary sections, are well written. Yet they are coming straight from classical results.

- The numerical experiments are well conducted.

- Adequate numerical performance on the two used datasets for comparison to other methods

- A large choice of numerical  experiments, both in the main text and in the appendices

### Weaknesses
 - The problem is sound, yet it does not appear to be really important. In addition, I am not certain of the added value of solving the two problems at the same time ; the authors should spend more energy to convince the readers of that. For instance, it seems that frameworks coming from optimal transport for graphs would solve both matching and clustering for graphs. Or isn't it possible ? Why is it better to design a method focusing on both in 1 step ?

- In the absence of an insightful discussion (or proof...) about the necessity of considering graph matching and graph clustering in a joint approach, the article is over-stating somehow its contribution ; even if UM3C works, it's not certain it is needed.

- the criteria proposed in equation (2) appear to be ad hoc 

- the Minorize-Maximization (MM) framework is not new, and here used in a classical way (hence most of it would move to the appendices)

- the writing could be improved.
The presentation is nearly adequate, yet it comes with some repetitions. 
The derivation of the overall objective for joint matching and clustering, eq (2), is not well presented and one does not fully know where it comes from, if there could be other choices, and globally what is ad hoc in this formulation and what is mandatory.

- The authors rely heavily on the figures (1 and 2) for the readers to understand the full picture, but for me they are not that clear because there are too many elements displayed at the same place.

### Questions
- The topic of joint matching and clustering for graphs is sound, although the authors should strive to find situations that are more elaborated than their examples on images. This assumes that images are best coded as graphs, yet nothing is said in support of that; also; the graphs representing images are quite simple.
The authors should think about situations where the affinity graphs are less simple, and the graphs more complex. 

- page 1 : K (the affinity matrix) is not defined 

- p 6 in 5.1: Where is \Lambda defined ?

- Is there a comparison to simpler graph matching methods, for instance using optimal transport distance, that are known to also be usable for clustering ?

- In 4.2, and then in 4.3, a softened version of the hard assignment matrix, C, is introduced. Is it only anrelaxation for easier convergence, or does the relaxed matrices capture something about possible confusion between the clusters ? It would be useful if it is the case,  as we often have clusters which are not as clear  cut as hard assignment is assuming.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel algorithm to jointly optimize graph clustering and matching. The optimization problem is formulated as a minorize-maximization problem with guaranteed convergence. An unsupervised variant is further introduced to incorporate edge-wise affinity and pseudo label selection. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
-	It is a novel idea to jointly address graph clustering and matching problems simultaneously, which are mutually beneficial.
-	Fast convergence is achieved by the minorize-maximization framework.

### Weaknesses
 - The presentation of the paper needs further improvements. Several confusing symbols/notations are abused or used w/o declaration. For instance, in Definition 2, $k_1,k_2,…$ and $N$ are used without definition. Additionally, the multiplication of matrices $X_{ik_1}$ with $X_{k_1k_2}$ is presented, although they are not necessarily of the same shape. The vertex set $\mathcal{V}$ is defined as a set of graphs, which is unconventional.
- The theoretical analysis may need further justification. The convergence statement above Eq.(3) claims that the objective function is non-decreasing, but this alone does not guarantee convergence. A more rigorous explanation should consider the finite solution space (X, C). Furthermore, Proposition 4.1 uses $N_{g_i}$ without definition and assumes the sizes of clusters remain the same in two consecutive iterations, which is a strict condition. A convergence rate analysis is necessary to support the claim of 'quick convergence' in Appendix C.3.
- Though the UM3C method is called to be unsupervised, it still requires the hand-crafted affinity matrix $K^{raw}$, which is another kind of supervision. The authors claim their method is unsupervised, yet Eq. (8) relies on a pre-computed $K^{raw}$. This introduces a level of supervision that contradicts the unsupervised claim. A more detailed explanation of how $K^{raw}$ is derived and its impact on the unsupervised nature of the method is needed.
- Section 4.2 claims disregarding the transitive relations as an advantage. However, the greedy search to get the top-$rN^2$ values may break the transitive constraint, making it possible to have $c_{ik}=1,c_{kj}=1$ but $c_{ij}\neq 1$, which is logically inconsistent. A clearer explanation of why disregarding transitivity is beneficial and how the greedy search maintains consistency is required.
- Eq. (6): the selection of $r$ is not clearly defined. This parameter appears highly heuristic and may significantly influence model performance. A more systematic approach to selecting or tuning $r$ should be provided.

### Questions
-	Section 4.1: what’s the definition for $g(X|X^t)$? Is it the graph matching objective function given the clustering result h(X^t)?
-	Convergence statement above Eq.(3): Eq.(3) only guarantees your objective function is non-decreasing, but not necessarily guarantee convergence? I think another important reason for the convergence of f is that the solution space (X,C) is finite. In some scenarios, even the objective function remains unchanged, multiple optimal solutions may exists (i.e., $f(X_i,C_i)=f(X_j,C_j)$), and the solution may switch between $(X_i,C_i$ and $X_j,C_j$) instead of converging.
-	Proposition 4.1: $N_{g_i}$ are used w/o definition. How can you guarantee the if condition that the sizes of clusters are the same in two consecutive iterations? I think this is a quite strict condition, and hence I don’t think this proposition provide insightful understanding to the convergence. Besides, you claimed a ‘quick convergence’ in Appendix C.3, it’s necessary to provide a convergence rate.
-	Section 4.2: you claimed disregarding the transitive relations as an advantage, can you explain why? As mentioned later you adopt a greedy search to get the top-$ rN^2$ values, this may breaks the transitive constraint, making it possible to have c_{ik}=1,c_{kj}=1$ but $c_{ij}\neq 1$, which does not make sense to me.
-	Eq. (6): how are $r$ selected? I think this is highly heuristic and may dramatically influence the model performance.
-	Eq. (8): you claimed your method as unsupervised, but you need the hand-crafted $K^{raw}$ as input, which actually is another kind of supervision.
-	Writing
  - Definition 2: $k_1,k_2,…$ and $N$ used w/o definition; How can you multiply the two matrices $X_{ik_1}$ with $X_{k_1k_2}$ as they are not necessarily (and mostly) with the same shape? The vertex set $\mathcal{V}$ is defined as a set of graphs.
  - Eq.(18): $c_{ij}^t\to c_{ij}^{(t)}$.
  - For equations not quoted in the main text, you should not number it and use ‘equation*’ environment instead.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work explores a practical scenario in graph matching, where the collected graphs are of different types. To tackle this issue, the authors introduced a strategy named MGMC which simultaneously performs graph clustering and graph matching, along with a novel method M3C as an implementation of such strategy. M3C not only handles graph matching with mixed types, but also addresses several drawbacks of previous graph matching methods. Overall, the studied topic is meaningful and the work is solid despite some minor weaknesses, so I recommend acceptance for presenting it at ICLR.

### Strengths
* The paper is easy to read, and well-written in general.
* The studied scenario in which the dataset is a mixture of different graph types is important in practical applications.
* The proposed model along with its MM-based optimization algorithm solves several drawbacks of previous graph matching methods.

### Weaknesses
 * The literature part lacks state-of-the-art works published in the last two years.
* The authors didn't compare with the latest works. The most recent competitor MGM-Floyd was published in 2021.


### Questions
* What's the major benefit of MGMC? For matching with mixed graph types, we could employ graph-level classification or clustering (so that labeling is also avoided) methods to preprocess the dataset and apply conventional graph matching methods to individual classes. No ablation experiment is conducted to verify the effectiveness of MGMC anyway.
* Is it possible to integrate the proposed method into a fully end-to-end GM pipeline (such as NGMv2)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a full framework dedicated to graph matching using both unsupervised and supervised methods. The framework mixes graph matching and clustering leading to a method able to deal with heterogeneous set of graphs in a fully unsupervised way. The experiments show promising results on classical datasets.

### Strengths
The framework seems very general and address a very classical problem in computer vision. Compared to previous methods it can use both node and edges attributes for matching. The combination of supervised and unsupervised methods helps to improve classical methods with only handcraft features. Most of the paper is clear and easy to read.

### Weaknesses
The proposed work has several weakness,

- the pairwise graph matching relies on the Lawler's QAP formulation which is known to not scale well with the size of the graphs. In the experiement all the graphs are shorts (less than 20 nodes for most), this is not the case in general. The reliance on QAP, while a classical approach, inherently limits the method's applicability to larger, more complex graphs commonly encountered in real-world scenarios. The computational cost of solving QAP grows rapidly with the number of nodes, making it impractical for graphs with even moderately more nodes than those tested.
- the framework need an initialization with a classical pairwise method. We may expect some sentivity with the chosen method. I did not see any discussion on this part. Furthermore there exists better methods than RRWM like
    - [KerGM](https://proceedings.neurips.cc/paper_files/paper/2019/hash/cd63a3eec3319fd9c84c942a08316e00-Abstract.html) which is able to use edge attributes
    - [GWL](http://proceedings.mlr.press/v97/xu19b.html)
  The lack of discussion regarding the sensitivity to the chosen initialization method is a significant oversight. The performance of the entire framework could be highly dependent on the quality of the initial pairwise matching. The mentioned alternative methods, such as KerGM and GWL, offer more sophisticated approaches to pairwise matching and could potentially improve the overall performance and robustness of the proposed framework.
- the comparison with the state of art is missing many others existing methods. The proposed methods are all from the very same team. I would expect a better state-of-art. For example on the deep learning side we have (to cite a few),
    - [SIGMA](https://proceedings.mlr.press/v139/liu21i/liu21i.pdf)
    - [Universe Points Representation Learning for Partial Multi-Graph Matching](https://arxiv.org/abs/2212.00780)
    - [DGMC](https://openreview.net/forum?id=HyeJf1HKvS)
  The absence of a comprehensive comparison against a broader range of state-of-the-art methods, particularly those leveraging deep learning, is a major concern. The current comparisons are insufficient to establish the true novelty and effectiveness of the proposed approach. The inclusion of methods like SIGMA, Universe Points Representation Learning, and DGMC would provide a more complete and rigorous evaluation.
- the full framework is focus on images. It is difficult to assess if it can be extended to general graphs. For example, in the DGMC paper there is an experiment where the attributes are only coordinates.

### Questions
I have some questions on the cluster part,
- the MM method asks to solve two problems (namely equations (6) and (7)). Both problems remain hard to solve so I don't see how they can be solved in a proper way. Only one method is proposed but not really described.
- the supergraph is an important tool here. How is it really built? Do we need some heuristic to lessen the problem?

Some other questions on the deep learning part,
- how the features on edges are build? I don't see how the VGG-16 features are used in this case.
- how much the method is sensitive toward the initialization of the pseudo-labels? From the experiments, RRWM seems good enough (in the sense they don't completely failed).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
