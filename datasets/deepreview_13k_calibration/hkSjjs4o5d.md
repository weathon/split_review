# A Differentially Private Clustering Algorithm for Well-Clustered Graphs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
We study differentially private (DP) algorithms for recovering clusters in well-clustered graphs, which are graphs whose vertex set can be partitioned into a small number of sets, each inducing a subgraph of high inner conductance and small outer conductance. Such graphs have widespread application as a benchmark in the theoretical analysis of spectral clustering.
We provide an efficient ($\epsilon$,$\delta$)-DP algorithm tailored specifically for such graphs. Our algorithm draws inspiration from the recent work of Chen et al. [NeurIPS'23], who developed DP algorithms for recovery of stochastic block models in cases where the graph comprises exactly two nearly-balanced clusters. Our algorithm works for well-clustered graphs with $k$ nearly-balanced clusters, and the misclassification ratio almost matches the one of the best-known non-private algorithms. We conduct experimental evaluations on datasets with known ground truth clusters to substantiate the prowess of our algorithm. We also show that any (pure) $\epsilon$-DP algorithm would result in substantial error.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission studies differentially private (DP) algorithms for recovering clusters in well-clustered graphs, and it proposes a private algorithm that works for well-clustered graphs with k nearly-balanced clusters. The authors also show that any (pure) ϵ-DP algorithm would result in substantial error.

### Strengths
1. The results seem interesting: The private algorithm in this submission works for
k nearly balanced clusters while the previous reference only works for 2.

2. The empirical results look promising, in comparison between RR+SDP and Algorithm 1.

### Weaknesses
1. The condition "WELL-CLUSTERED GRAPHS" may reveal sensitive information in edge privacy. Specifically, the definition of 'well-clustered' is not explicitly tied to a formal privacy parameter, and it's unclear how much information about the graph structure is leaked by assuming this property. For instance, if 'well-clustered' implies a specific range of edge densities within and between clusters, this could be exploited to infer the existence or absence of certain edges, especially when combined with the knowledge of the number of clusters (k). This is a concern because the algorithm's utility guarantee relies on this assumption, potentially creating a tension between utility and privacy.



### Questions
1. The authors claim that this submission is inspired by a recent work of Chen et al, so what is the main difference between this submission and Chen et al's paper in the technique aspect?

2. For two adjacent data sets (graph) D and D' differing in one edge, could it happen that D is well-clustered while D' is not?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper gives a DP algorithm for well-clustered graphs. Here a "well-clustered graph" is similar to graphs generated from some stochastic block model, such that there exists an underlying partition of the graph, where edges between clusters are sparse (i.e, small outer-conductance) while each cluster internally is well-connected (large inner-conductance). The task is to recover this underlying partition in a differentially-private way.
The paper gives a spectral algorithm for the problem: first solve a SDP relaxation of the problem to extract the cluster structure, where (the assignment of) each vertex is embedded as a k-dimensional vector, then apply standard Gaussian DP scheme to (the Gram matrix of) the embedding vectors, which gives a perturbed version of the embedding. The final clustering is obtained by standard k-means clustering over the perturbed vectors.
The paper gives theoretical analysis on the algorithm performance, measured by the volume of the misclassified vertices, and prove it satisfy DP requirement.

### Strengths
- The paper gives the first DP algorithm for a hard (?) problem. The algorithm achieves good error bound and utility that are close to best-known non-private algorithms.
- The algorithm given is very simple (maybe except for the SDP, whose formulation I believe lacks sufficient explanation), while the analysis seems quite non-trivial.

### Weaknesses
 - I'm not familiar with spectral methods, so I'm not going to comment on technical merits. Although I can follow most proofs, I find it difficult to grasp the intuitions. One example is the SDP with the constraint (1). It would be much more reader-friendly if the authors can give intuitive summary of the ideas instead of directly jumping to proofs.

 - I'm curious what's the relation of this well-clustered graph with stochastic block model? The SBM seems to attract much more research interests. Is the problem studied here a generalization of SBM, or a special case, or neither?

 - It would be very helpful if the authors can give some intuition & motivation of the SDP, in particular how the regularizer and the constraint (1) are designed. Specifically, the role of the trace term and the constraint that $X$ must have a trace of $n$ is unclear. It's not obvious why this particular constraint is necessary for the SDP to work correctly, and how it relates to the overall goal of recovering the cluster structure.

 - I'm curious why the DP noise is applied to the Gram matrix X rather than directly to vectors associated with each vertex? It seems like applying noise to the Gram matrix might obscure the underlying geometric structure of the embeddings, making the subsequent k-means clustering less effective. It would be helpful to understand the trade-offs involved in this design choice.

 - Proof of Lemma 4.4: I think the upper bound on $\sum_{i=1}^k|E(C_i,V-C_i)|$ is $\phi_\text{out}\cdot2m$, not $\phi_\text{out}\cdot m/2$.

 - Proof of Lemma 4.4: Could you give a detailed explanation on how the second smallest eigenvalue $\mu$ of $L_{G\{C_i\}}$ can be obtained by minimizing the quotient given in the paper. The connection between the Rayleigh quotient and the second smallest eigenvalue of the Laplacian is not immediately obvious and requires further explanation.

 - In experiment the baseline is random response + SDP  *without regularizer*. Why do you remove the regularizer? It is unclear why the regularizer is detrimental in the baseline case, and why it is needed in the proposed algorithm but not in the baseline.

### Questions
- I'm curious what's the relation of this well-clustered graph with stochastic block model? The SBM seems to attract much more research interests. Is the problem studied here a generalization of SBM, or a special case, or neither?
- It would be very helpful if the authors can give some intuition & motivation of the SDP, in particular how the regularizer and the constraint (1) are designed.
- I'm curious why the DP noise is applied to the Gram matrix X rather than directly to vectors associated with each vertex?
- Proof of Lemma 4.4: I think the upper bound on $\sum_{i=1}^k|E(C_i,V-C_i)|$ is $\phi_\text{out}\cdot2m$, not $\phi_\text{out}\cdot m/2$.
- Proof of Lemma 4.4: Could you give a detailed explanation on how the second smallest eigenvalue $\mu$ of $L_{G\{C_i\}}can be obtained by minimizing the quotient given in the paper.
- In experiment the baseline is random response + SDP  *without regularizer*. Why do you remove the regularizer?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies differentially private algorithms for cluster recovery on well-clusterable graphs. A well clusterable graph is an unweighted graph that has a bounded ratio between outer conductance and inner conductance. The notion of privacy is (eps, delta)-differntial privacy, and it is measured on neighboring graphs that have one edge difference. The goal is to minimize the (relative) number of points that are mis-clustered in every cluster, provided that the input graph is well clusterable into k clusters (and assuming k is known).

The main result achieves a misclassification ratio only slightly worse than the state-of-the-art non-private version with respect to the main parameters. The price of privacy is mostly on the requirement of the desntiy of graphs, i.e., the number of edges must be at least some poly(\phi_in / \phi_out) / eps^2 * log(1 / \delta) factor larger than the number of vertices. Lower bounds were also obtained to justify this price of privacy. Finally, some experiments were provided to justify the usefulness of the new algorithm.

### Strengths
- The bound looks strong since it is very close to the non-private version — The privacy guarantee does not directly add to the misclassification ratio. The factor of poly(phi_in / phi_out) in the “price of privacy” seems to be natural and is probably necessary (even though the paper did not justify this).

- The techniques are not particularly novel, but combining existing techniques and obtaining interesting results is also a solid contribution.

- The paper is well-written and easy to read.

### Weaknesses
 - One thing I’m not sure: does the balance parameter c also appear in the bound of Peng et al. 2015? This is not clearly discussed in your paper, and I think that this is very important.

- Whether (eps, delta)-DP is necessary is not justified; the upper bound is (eps, delta)-DP and the lower bound is about eps-DP. It would be helpful to have a more detailed discussion on the necessity of the relaxed delta-DP, especially given the lower bound result.

- The approach requires to solve SDP which is heavy for larger datasets. The computational cost of solving the SDP, especially in relation to the size of the graph, should be discussed more thoroughly. The paper should also discuss potential approximations or heuristics that could be used to mitigate this computational bottleneck.

- The experiment is not comprehensive and I find it not very convincing. The experiments are limited in scope and do not fully explore the parameter space or different graph structures. The justification for the chosen datasets and parameters is also weak, and it is unclear how well the results generalize to other settings.

### Questions
- The presentation is technically heavy. It would be helpful to talk about more intuitions and less calculations in the main text.

- In Theorem 1, n and m are not quantified. Also, the quantification of \sigma is not very clear — “for every” or “exists”?

- In the experiments, it would be nice to define or at least explain what AMI and NMI are, and what do they indicate. I’m not even sure if larger value is better.

- I found only arXiv version is cited for several papers — are they published in a conference? Please check and update.

- You mentioned that your experiments are to somehow verify that “when the noise added to the adjacency matrix by randomized response is balancing with its signal, the output of Algorithm 1 still has significant utility”, but I don’t see this clearly discussed. For instance, from what data did you see that the noise added by randomized response is balancing with its signal? And how exactly does your Algorithm 1 compare w.r.t. utility? 

- I may have missed something, but did you say the value of eps and delta that you use in the experiments?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies differentially private clustering algorithms for balanced and well-clustered graphs. The notion of ‘’well-clustered’’ is defined by a high ratio between the inner and the outer conductances, and the notion of ‘’balanced’’ is defined by the graph volume. The paper considers the problem with any fixed $k$ number of clusters, which is a natural extension of a recent result by CCDEIST [Neurips’23] that studied the DP clustering algorithms for balanced and well-clustered instances with 2 clusters. Instead of using a cost function, the goal in this setting is to ‘’almost entirely’’ recover the clustering labels while still preserving the differential privacy. This is a reasonably strong goal given the strong assumption on the underlying instances. 

The main result of the paper is an $(\epsilon, \delta)$-DP algorithm that recovers the clusters correctly up to an $O(\log(1/\delta)/\epsilon^2)$ multiplicative factor on the *volume* of the (ground truth) cluster (assuming constant balance factor). The paper also provides a lower bound showing that we cannot hope for zero-error algorithms under this setting (unlike the exact recovery of CCDEIST [Neurips’23]). Finally, the paper conducts several experiments on synthetic datasets, and the results show that the proposed algorithm is competitive in the *utility* metric (but did not test for privacy).  

The main technical ingredient of the paper is a white-box adaptation of the results of CCDEIST [Neurips’23]. In particular, the algorithm uses a variate of the $\ell_1$ sensitivity bound by CCDEIST [Neurips’23] for strongly convex functions and shows that their SDP objective function satisfies the desired convexity property. As such, they can get a levy on the level of Gaussian noise put on the output of the SDP solution. They further use known results in spectral clustering to show that the added noise level does not induce too much error on the utility.

### Strengths
My general evaluation of the paper is positive: it studies an interesting problem, which in turn is a natural follow-up of a well-established result. The paper is well-written, and the technical steps are rigorous and easy to follow. The organization of the paper also looks quite nice.

I checked the privacy proof, and things look correct to me, barring the details of the proof of Lemma 3.1. Unfortunately, due to the limits on the review timeline, I did not get a chance to verify the algebra for the utility proof – a spot-check indicates that nothing is wrong. 

Finally, I think the results have nice applications due to the widespread popularity of the SBM model and the fact that a lot of networks satisfy the ``clustered’’ property. The experiment results show that the running time of the algorithm is not too bad, at least on small-scale of data.

### Weaknesses
Presentation problems in the main theorem. a). DP is not formally defined before the statement of theorem 1. Please at least add a pointer to your definition in section 2. b). The notation for $G_1 \Delta G_2$ is never defined. (And it’s never defined anywhere in the paper! :)) ) and c). The trade-off between the utility and the $(\epsilon,\delta)$-DP is not clear in the statement (although there is a lower bound on $m$), and it was unclear until Lemma 4.3. I would prefer to state the bound for general instances and factor the trade-off in the multiplicative error.

The notion of $(\kappa, D_{1}, D_{2})$-strongly convex is not defined in the preliminary (and only becomes clear to me after looking into the proof).

While I understand this is a mainly-theory paper, I would still suggest the authors spend more passages to properly motivate the study of the clustering of well-clustered graphs. I think CCDEIST [Neurips’23] has a nice example on this front by discussing the motivations from stochastic block models and downstream applications. Some discussion on this front is especially important for the broader appeal of the ICLR audiences.

Given the fact that the algorithm needs to run SDP, it’s unlikely that the algorithm can be scaled to modern social networks, which are the best candidates for well-clustered properties. Purely combinatorial algorithms would be much more helpful on this front.

Defining balance with volume seems to be a strong notion since it rules out the case when the clusters have comparable sizes but different densities. In contrast, I believe setting of CCDEIST [Neurips’23] only requires the *vertices* in two clusters to be balanced. Do you have any comments on this front?

### Questions
Defining balance with volume seems to be a strong notion since it rules out the case when the clusters have comparable sizes but different densities. In contrast, I believe setting of CCDEIST [Neurips’23] only requires the *vertices* in two clusters to be balanced. Do you have any comments on this front?

Can you report the runtime of your experiments and the hardware for your experiments? I want to get a sense of how far this algorithm is from being implementable in the real world and in the industry. (Please note that a bad performance will not affect my score, so please don’t do it strategically :)))

Your lower bound is for pure DP, can you get any result for pure $\epsilon$-DP upper bound with your technique? In particular, since you have a bound for the $\ell_{1}$ sensitivity of $f$, can you use Laplace mechanism to obtain a pure DP result?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
