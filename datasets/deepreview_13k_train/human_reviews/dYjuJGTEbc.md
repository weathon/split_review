# An Enhanced Gromov-Wasserstein Barycenter Method for Graph-based Clustering

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Optimal Transport (OT) recently has gained remarkable success in machine learning. These methods based on the Gromov-Wasserstein (GW) distance have proven highly effective in capturing complex data topologies and underlying structures.
More specifically, Gromov-Wasserstein Learning (GWL) has recently introduced a framework for graph partitioning by minimizing the GW distance. Various improved versions stemming from this framework have showcased state-of-the-art performance on clustering tasks. 
Building upon GW barycenter, we introduce a novel approach that significantly enhances other GW-based models flexibility by relaxing the target distribution (cluster size) in GWL and using a wide class of positive semi-definite matrices.
We then develop an efficient algorithm to solve the resulting non-convex problem by utilizing regularization and the successive upper-bound minimization techniques.
The proposed method exhibits the capacity to identify improved partition results within an enriched searching space, as validated by our developed theoretical framework and numerical experiments. 
Furthermore, we bridge the proposed model with the well-known clustering methods including Non-negative Matrix Factorization, Min-Cut, Max-Dicut and other GW-based models. 
This connection provides a new solution to these traditional clustering problems from the perspective of OT. 
Real data experiments illustrate our method outperforms state-of-the-art graph partitioning methods on both directed and undirected graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a Gromov Wasserstein (GW) Clustering Method based on a single marginal GW Barycenter : EGWB. The method also allows to add marginal or ambient metric constraints on the barycenter. Thus effectively showing that their method is a generalization of existing GW Learning methods. Later on more precise links are made with existing methods.
They first introduce a Monge type barycenter problem and a Kantorovich relaxation of it. It is shown that under appropriate conditions the two problems are equivalent.
An optimization algorithm relying on entropic regularization is presented. The convergence of the algorithm is shown.
Finally their method is benchmarked against existing GW Clustering methods, on synthetic and real data. On all accounts EGWB outperforms existing GW methods.

The contributions are the following:
- Introduced a generalization of existing GW Learning Methods
- Demonstrated theoretically and empirically their algorithm for solving the problem converges and has state of the art performances

### Strengths
The paper presents a unifying framework for GW methods. It does so clearly.

The core idea is to introduce the GW barycenter problem and note that adding constraints recover existing methods. This problem seems novel in that context and they address with clarity the first questions one can have  : equivalence between the Monge and Kantorovich type formulations, link with other methods in GW Learning as well as in Graph partitioning.

Their algorithm is an alternating minimization one. However they address the non convexity of the transport plan update by using an interesting combination of existing regularization methods : entropic regularization, link with the Wasserstein Barycenter problem which has better structure.

The synthetic data example is informative of how the barycentric nature of the problem allows for more efficient clustering. In the analysis of the performance on real data the explanation of the performance in relationship with the structure of the data is appreciated.

### Weaknesses
In the paragraph about Kantorovich relaxation it is stated that the minimum is attained at an extremal point under some conditions which are detailed in appendix. This point is central to the use of the algorithm afterwards. Thus I believe the conditions should be put forward in the main text.

In theorem 3 it is unclear in which case the algorithm converges with entropic regularization, however this is central to showing that the implemented algorithm does converge.

### Questions
How does the result of theorem 3 relates to the convergence of the algorithm implemented in practice?

Are there a stability result of the limit of the algorithm/solution of the problem with respect to the epsilon parameter?

In practice what are the optimal value used for the epsilon parameter for each datasets?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this submission, the authors propose a new graph partitioning framework EGWB, which relaxes the target structure and distribution constraints in Gromov-Wasserstein Learning (GWL) with a class of positive semi-definite matrices.
In particular, by learning the target structure matrix associated with the transport plan, the authors extend the GWL framework to a special GW barycenter problem (with only one graph), which enhances the flexibility of the GWL framework.
The proposed method is shown to be effective according to empirical results in various graph partitioning tasks.

### Strengths
Graph partitioning based on utilization of the Gromov-Wasserstein (GW) distance is an interesting and significant problem.

### Weaknesses
1. How to initialize $D’(0)$? How to set the value of $K$?

2. It seems the authors confuse the task of graph partitioning and that of graph clustering. They muddle up partitioning and clustering throughout this paper. 
I think the experiments in section 4.2 are more likely to be a graph partitioning task, rather than graph clustering, as is claimed by the authors. Please use one of the two definitions consistently in the paper.

3. In the subsection of Results and Discussion, the authors say they employ five metrics, however, I only find AMI. If they take the results reported in appendix into account, then should clarify this in the main context.

4. Are the datasets in section 4.2 asymmetric or symmetric? Do the authors symmetrize the directed graphs? 

5. What do the two axes in Fig.3 represent? It should be labeled in the figure.

6. There are typos and careless statements and the authors need to polish this paper carefully. For example, 1) page 1, it should be $G_1(D_1,P_1)$ in the third row from the bottom, 2) page 2, the second paragraph, the second point of the limitations has grammatical mistakes, 3) What is EGWB an abbreviation for? The author put forward EGWB without any explanations in page 6.

### Questions
Please see above.

### Soundness
2 fair

### Presentation
2 fair

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
The paper propose a graph partitioning approach based on the Gromov-Wasserstein (GW) distance. This approach minimizes the GW distance between the target graph and an empty graph with fewer number of nodes. The optimization problem finds an optimal mapping, which determines the node clusters. It jointly optimizes node mass distribution and pairwise distance relations in the empty graph, the later constrained to be diagonal. The authors propose an algorithm which alternates the minimization of these variables and provide theoretical convergence guarantees.

Furthermore, the authors establish connections between their approach and existing GW-based methods, as well as alternative techniques like Min-Cut. Finally, they empirically demonstrate the effectiveness of their proposed method.

### Strengths
The authors present an extension of previous GW-based clustering methods, while connecting them with other approaches such as the Min-Cut or Non-negative Matrix Factorization. In addition, they propose an algorithm with theoretical guarantees. In this regard, the paper seems to be theoretically well founded.

Additionally, their proposed algorithm showcases remarkable robustness against edge noise when compared to the competing methods outlined in the paper.

### Weaknesses
 - Challenges in Readability: In certain instances, the meaning of the notation, although not formally introduced, can be grasped from the context (e.g., $mathbb{I}_K$ denoting the identity matrix with $K$ rows). However, there are situations where the notation becomes confusing, posing a challenge to the paper's readability. For example, in the discussion of the "Monge's type Gromov-Wasserstein barycenter" in Section 3, the optimal mapping matrix is denoted as $MGW(G, G′)$, but this notation is also used as the objective in the minimization equation (7). The concept of minimizing a matrix raises confusion. In addition, the symbols $\pi$ and $\Gamma$ are interchangeably used to refer to the same object. For instance, three lines before equation (7), it states $\nu=\pi^T 1_N$, but in this context, as far as I did not misunderstand it, we are assuming a hard clustering mapping and therefore $\Gamma$ should be the appropriate symbol. Furthermore, though it is not crucial, adding the labels to the x-axis and y-axis of the plots would also ease the readability of the figures.

- The proposed method initialization depends on the results of other methods such as GWL and SpecGWL.

### Questions
- Initialization dependency: The paper mentions using a linear combination of GWL, SpecGWL, and joint distribution results as initial values for EGWB. However, it's unclear how the algorithm relies on this initialization. Could a less informed start, like the uniform distribution, yield comparable results or does one need to start from a relatively good initialization?
- Computational cost: While the paper outlines the computational cost per iteration, the average number of iterations required for convergence remains undisclosed. Additionally, considering the initialization dependency, it's crucial to know the overall time needed to run EGWB, especially if solutions for GWL and SpecGWL must be computed beforehand.
- Synthetic data: Figure 4 exhibits superior results for GWL and SpecGWL compared to Figure 2. Moreover, in Figure 4 GWL out performs SpecGWL given the true cluster size distribution. Is there any reason why is that the case? I am actually surprised that, for these apparently simple problems GWL and SpecGWL fail to retrieve the right clustering. Understanding the specific reasons for their failure is beneficial in order to comprehend why EGWB, in contrast, succeeds.
- Number of clusters: A parameter that needs to be set is the expected number of clusters $K$. This is indicated by the number of nodes in the empty graph. How robust is the algorithm to the choice of $K$? Particularly intriguing is the scenario where $K$ exceeds the actual number of clusters. In theory, it is possible that the optimal mapping does not assign any mass to the extra nodes of the empty graph. In that case, the algorithm would still be able to retrieve the true partition. Does this happen in practice, and how does the algorithm adapt to such situations?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Over a single input graph (D, h), authors study the problem of learning via the Gromov-Wasserstein loss (GW) a non-negative diagonal target structure D’ and its masses h’, in order to perform a partitioning of (D, h) via the underlying estimated (GW) transport plan. They propose to use a Block-Coordinate Descent algorithm that alternates between i) estimating a semi-relaxed GW transport plan using a mirror-descent scheme with an additional strictly concave regularization; ii) updating the diagonal structure D’ in closed-form. Authors empirically study the concavity of the resulting problem, and provide proofs of convergence for their algorithm. Then, they connect this GW (diagonal barycenter) problem or simplified variants to well-known clustering methods such as Min-Cut based methods, NMF and Max-Dicut. Finally, they study the relevance of their approach for graph partitioning of synthetic and real-world datasets.

### Strengths
-	Introduce a novel GW-based transport problem to perform graph partitioning.
-	Provide first results on the concavity of this problem. Then provide an algorithm to and introduce a strictly concave regularization of this problem that might help for such tasks.
-	Proof of convergence of their BCD algorithm.
-	Interesting but simple connections with existing clustering methods such as Min-Cut based methods , NMF and Max-Dicut.
-	Benchmark on GW-based and SOTA approaches for graph partitioning.

### Weaknesses
 **Overall appreciation**: This paper tends to omit very similar recent works and the theoretical results seem either incomplete (analysis of concavity and relationships with existing graph partitioning/clustering methods) or incremental.

*NB: I added comments after authors' rebuttal in italic for each point*

- **1. Authors omit several recent contributions on GW**:
     - **a)** [A] studies the complete (sr)GW barycenter problem where the target structure is not forced to be a non-negative diagonal matrix. This paper shows that it is a SOTA method for spectrum-preservation graph coarsening and provide strong theoretical contributions supporting its use.
       **i)** These spectrum properties are also of particular interest for graph partitioning, hence the (sr)GW barycenter problem should be rigorously compared theoretically and empirically to the (sr)GW diagonal barycenter problem. **ii)** I believe that simple Stochastic Block Models (SBM) could provide a stress test over which the srGW diagonal barycenter problem fails contrary to the srGW barycenter problem : e.g using non-assortative SBM with a unique intra-cluster connectivity p smaller than inter-cluster connectivities $q_{cluster_i, cluster_j}$. Moreover I expect the diagonal structure to be more sensitive to contrasts within any SBM, i.e small variations between intra/inter-connectivities. Could authors perform such empirical sanity-checks ?

        [*None of these points have been clearly addressed by the authors during rebuttal*]

     - **b)** relations to srGW [Vincent-Cuaz et al, 2022] : **i)** The (sr)GW barycenter problem over a single input graph is a particular case of their dictionary learning. **ii)** The srGW solver proposed by authors is exactly the mirror-descent algorithm introduced in this other paper over which a concave regularization is added. These two points should be clearly stated in the paper.

        [*None of these points have been clearly addressed by the authors during rebuttal*]

     - **c)** On the proof of convergence for the algorithm: **i)**  [B, C] provide a scheme of proof to establish a non-asymptotic convergence of the regularized srGW solver. [*Not considered by the authors during rebuttal*] 

         **ii)** An overview of the proof strategy for Theorem 3 should be clearly state  [*Not considered by the authors during rebuttal*]. More importantly Lemma 2 should be clarified : as such it seems wrong/ incomplete to me, e.g differentiability issues at the border are avoided, limits are considered out of the domain, continuity arguments are used without defining any topology etc...

         [*I am sorry I made a mistake on this matter, Lemma 2 is correct. As first suggested, an overview of the proof strategy would have helped for readability. Moreover authors follow a proof scheme from another more generic paper over which it would have been relevant to discuss relations. From my understanding, the first convergence proof for the srGW problem provides bounds involved in their finale convergence analysis. A sharper convergence proof - following B, C - could provide a sharper analysis and adaptive scheme for their regularization parameter.*]

         **iii)** The overall learning algorithm seems to be a particular case of two-block BCD well-studied in [D]. [*Reference not considered by authors. It implies that more generic converge proofs already exist for their BCD.*]

     - **d)** First parts of the supplementary materials: (minor) paragraph  ‘Non-convexity of GW discrepancy’ exposes known relations. (more important) paragraph ‘Assumption of uniform distribution’ seems to be a bad justification for the choice of input distributions that only translates the notion of weak-isomorphism discussed in [Chowdhury et al, 2019].

        [*Rebuttal made by authors is not compelling.  My point is that this dilution of mass// duplication of points of the support is absolutely not a justification for assuming a uniform distribution. What matter is the total mass assigned to the original point of the support. Your justification is misleading and formally wrong if you rigorously acknowledge the support of the measure. You can say we pick uniform distributions because it is the most common choice, note that there are other options (degrees etc..)... Moreover the sensitivity analysis in the supplemetary material is really not clear, that would be better to see a complete benchmark with same hyper parameter validation with several cases as b = 0 / b =1 / b in ]0, 1[. Maybe that is a by-product of learning the diagonal/complete barycenter, or just of diverse regularization coefficients. "which further validates our mass splitting technique." just does not make sense.*]


- **2. The several concavity analysis done by authors are incomplete and not conclusive:**
     - **a)** Could you detail the experiments illustrated in Figure 1 ? What is D’ in this setting ? What Is the initial transport plan used for these experiments ? Are these findings consistent w.r.t these initial transport plans (should be validated using the MCMC sampler in SpecGWL) ? What are the solvers used for these experiments ? If entropically regularized ones, please compare results to exact solvers such as conditional gradient solvers. *[Partially addressed by authors]*
    - **b)** Are these findings specific to heat kernels or do they generalize to PSD matrices e.g Laplacians  ? *[Misunderstood by authors - no time for discussions]*
    - **c)** None of the theoretical studies on the concavity of the overall learning problem are complete or convincing: **i)** proof/paragraph: "One common condition for extremal points" only shows that for an optimal target masses nu*, the resulting GW problem is concave hence solutions are extremities of admissible coupling with marginals mu and nu*. It does not show that extremities of the set of semi-relaxed couplings with first marginal mu, i.e hard-clustering matrices, are solutions. *[Incomplete analysis by authors maybe we misunderstood each other on the term extremities, considering that they always assume the existence of corners for $U(mu, nu^\star)$ no matter $nu^\star$ .]*

      **ii)** I do not see when the other condition in equation 19 could be applied, authors should discuss this point. *[partially addressed but still emphasises the strong specificity of this result]*.

      **iii)** Remark: Overall, a too recent contribution [E] to be taken into account at the submission date deals with these concavity problems for srGW barycenters and could guide authors to derive an analog result for the srGW diagonal barycenters.


- **3. Zero masses**: Authors do no mention the flexibility of this learning problem to get optimal target masses which are equal to zero and might allow to detect true number of clusters in some settings, as discussed in [Vincent-Cuaz et al, 2022]. *[partially addressed by authors]*


- **4. Missing points in experiments**: 
    - **i)** Please benchmark methods in terms of running times too. Trade-off in terms of performances and speed should be explicit. *[partially addressed by authors]*
    - **ii)** The strongly concave regularization with continuation scheme proposed by authors introduce several hyperparameters. Please conduct an ablation study over this regularization. Plus could you complete Figure 11  that shows that the method is quite sensitive to these hyperparameters, with other datasets ? *[Ablation study not considered by authors. Sensitivity analysis apparently completed but from the revised paper version we can not even know what is the dataset used in these experiments]*
    - **iii)** Authors rely on other GW-based methods to get initial transport plans for their method. Whereas [Vincent-Cuaz et al, 2022] proposed to leverage k-means algorithm, which is a quite common technique in the clustering or graph partitioning literature. I guess, in concave setting solvers can be stuck at extremities, hence it would be relevant to force initial within the polytope e.g with kmeans + mu.nu^T. Could you further compare these choices ? *[not considered by authors]*

- **5. Some parts in Section 3.3 are not clear** and should be clarified: **i)** srGW to Identity: ‘This results in each cluster containing an equal number of data points.’ It clearly does not seem to be the case. **ii)** relation to NMF: does it really coincide with the srGW diagonal barycenter problem or rather with the complete barycenter problem ? *[addressed by authors]*

### Questions
I invite the authors to discuss the above-mentioned weaknesses and to answer the questions (potentially implying additional experiments) I have associated with them in order to complete my development.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
