# MLOT: Extending the Bipartite Structure towards Multi-Layered Structure for Optimal Transport

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Despite its remarkable success and widespread adoption in various domains, optimal transport (OT) has a rather simple structure, relying on bipartite graphs with only two layers of nodes for transportation. In this paper, we propose a multi-layered OT approach that extends the original two-layer structure to handle transportation problems across multiple hierarchical levels. Within this framework, the source distribution flows through intermediate layers, before reaching the target distribution. Unlike previous variants of OT that involve multiple distributions, our multi-layered OT typically involves uncertain intermediate distributions, which need to be computed based on the relationships between the preceding and succeeding distributions. Under entropic regularization, MLOT-Sinkhorn algorithm is further proposed for multi-layered OT, which can be accelerated using GPUs and significantly outperforms general solvers such as Gurobi. The theoretical results of our entropic MLOT are also given in this paper. In the experiments, we validate its speed advantage and convergence performance. We further validate its feasibility through Text-Image retrieval and intermediate image computing task, which demonstrates reformulating the problems as MLOT can achieve better results. Source code will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose to discretize the path of intermediate distributions between source and target distributions in the OT problem. They added up the total cost between each two adjacent transportation problems on the path and adopted the Sinkhorm iterations to alternatively solve for the intermediates and the couplings which ensemble the transportation plan. Convergence was provided and experiments showed performance gains in solving the text-image retrieval problem.

### Strengths
The authors wrapped their MLOT formation with the Sinkhorn algorithm and thus inherited all the computational benefits of it. Theoretical results seem solid to me. Convergence analysis was provided and verified with synthetic data.

### Weaknesses
The main problem I find in the paper is that the authors didn't answer the very question that they raised. In the second paragraph (line 039), they referenced transportation as the "real-world" example of the benefit of MLOT, by optimizing the freight transportation to reduce the cost and environmental impact, as suggested by their reference Bektas et al. 2019. However, throughout the paper, they didn't answer the question. Can MLOT help find the optimal routes and minimize the total cost?

In real-world problems, the intermediate distributions have certain constraints like the routes (cost matrix) and max capacity of the stops (intermediate distributions) in freight transportation example. The paper doesn't mention such constraints either in methodology or experiments. Specifically, the cost matrices between intermediate layers are not necessarily the same, and the capacity constraints at each intermediate node are crucial for real-world applicability, which the paper does not address. The methodology should explicitly incorporate these constraints, and experiments should demonstrate the method's performance under such conditions.

In 4.2, MLOT was compared against softmax so it's not clear whether the gains were from OT or from the multi-layer formulation or both. The comparison should isolate the effect of the multi-layer formulation from the underlying OT method. A more controlled experiment would involve comparing the multi-layer OT with a single-layer OT baseline, both using the same Sinkhorn algorithm, to determine the true benefit of the multi-layer approach. It's also unclear if the data augmentation is performed on the input or the feature space, which should be clarified.

Figure 7 in 4.3 also demonstrated that intermediate distributions may not be physically meaningful and smooth and thus not applicable to solving "real-world problems". The lack of smoothness and physical interpretability of the intermediate distributions raises concerns about the practical applicability of the method in scenarios where these properties are important.

### Questions
Line 323: Therefore, out MLOT can offer new perspectives and approximate computations for Dynamic OT and the Schrodinger bridge. What are the new perspectives? That MLOT can "approximate computations for Dynamic OT and the Schrodinger bridge" is a serious claim. I'd like the authors to provide evidence for that or tune down the sentence to something like whether we can approximate dynamic OT via MLOT is a future direction. And it's not clear in what aspect do we approximate. Is it the total cost or the transportation map or something else.

Comparing MLOT with barycenters should be expanded. In line 182, "when $S=2$ in Eq.6 and $K=3$ in Eq.5, the optimization of our MLOT is equivalent to solving the Wasserstein barycenter." It's not, because for that to be true you have to assume $\lambda = \frac{1}{S} = \frac{1}{2}$, don't you? As we change $\lambda$ in barycenters, we could also form a path of intermediate distributions between the target and the source. How is that process compared to MLOT?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposed multi-step optimal transport when finding the OT mapping from one distribution to other distribution, given the supports of "transitional" distributions are known (cost matrices are known). The method is presented in Section 3 with entropic regularization that leads to adapted version of Sinkhorn algorithm to solve the problem. Proposition 3 prove the convergence property of the method. Real applications are text-image retrieval task and generating intermediate images.

### Strengths
Empirical results shown in text-image retrieval task, although the setting is quite simple, by creating layers based on flipping the image. 
I wonder if there is another work that use augmented data to do this task.

### Weaknesses
The theory part is just straight adaptation from known work of Sinkhorn algorithm. In proposition 4, convergence rate depends on $\gamma$, which is not easy to quantify. 

For task of generating intermediate images, there is no baselines, or quantity to compare/assess the current method with others. This contribution is limited. 

It is not clear (theoretically, intuitively) that in text-image retrieval task, why do we need to use data augmentation to create another layer for OT?

Cost metric in the task text-image retrieval  could be negative, since it is defined as the cosine similarity, does this affect the definition and algorithm of and using OT?

### Questions
Cost metric in the task text-image retrieval  could be negative, since it is defined as the cosine similarity, does this affect the definition and algorithm of and using OT?

In both real applications, is there any empirical rule to choose parameter?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces multi-layered traditional optimal transport, which finds an optimal transport map between the input and output distribution through multiple layers as an extension of traditional optimal transport. Compared with other optimal transport methods involving multiple distributions, the authors introduce uncertain intermediate distributions computed based on the previous and the next distributions. Additionally, the authors further propose MLOT-Sinkorn, which is designed specifically for MLOT to accelerate computation. The experimental results show that MLOT achieved better results than previous optimization methods.

### Strengths
1. This paper introduces a variant of multiple distributions optimal transport and a corresponding variant of the Sinkhorn algorithm to solve this problem.
2. The results of the method significantly outperform existing methods for multiple distributions.
3. The experimental section is thorough and clearly written, detailing the settings and configurations for each task.

### Weaknesses
1. The motivation for the introduction of MLOT compared with other multiple distributions for optimal transport is not written. Please refer to Question 1 in the Questions section for more details.
2. The related works section doesn't mention any previous works on multiple distributions in optimal transport although in the abstract, the authors state that "Unlike previous variants of OT that involve multiple distributions,..." (L19)
3. Although the experimental results demonstrate significant improvements with MLOT over other optimization methods for multiple distributions, a comparison with other optimal transport (OT) methods of similar scope is missing. Specifically, the authors evaluated MLOT-Sinkhorn against non-OT methods, yet did not compare it with other OT-based approaches for finding optimal transport distances between multiple distributions.
4. The overall writing is vague and the flow of the paper is difficult to follow. The related works are non-relevant to the methods proposed. For example, in Section 2, the authors mention Optimal Transport on a Graph and state that "However, the above works rely on the shortest distances on the graph and do not directly compute the transport couplings in the graph. In this paper, we attempt to directly compute the transportation between nodes in a multi-layer structure.". However, the paper lacks further comparisons or references to this aspect in later sections. The connection between the graph-based OT and the proposed method is not clear.
5. Typo: In line 259, "As shown in Fig. ,", the figure is not specified.

### Questions
1. My biggest question lies in the motivation for finding the OT distance between multiple distributions, which involves uncertain intermediate distributions, and only the source and the target distribution are known. As far as I understand, the motivation of the paper is from real-world problems, where finding the OT distance between two distributions is not enough, the case in which we assume that the source and the target distribution are known.
2. How to compute the intermediate distributions as mentioned in the paper?
3. Can you provide more baselines or related works of optimal transports in literature and explain clearly what is the difference between your methods and these methods?
4. As far as I understand, the authors of (1) propose Sobolev Transport, which aims to find the optimal transport distance between 2 distributions, in which supports of these two distributions are nodes of the graph, which is different from the main purpose of this paper to find optimal transport map between multiple distributions. What does it mean by "we attempt to directly compute the transportation between nodes in a multi-layer structure." (L135-136) since in (1), the nodes of one graph are support of two distributions?

**Remark**: I gave a score of 5, but I am open to raising it once the above concerns are addressed and I have a clearer understanding of the paper. I will also reconsider my score following the rebuttal to ensure my evaluation is fully justified.

(1) Tam Le, Truyen Nguyen, Dinh Phung, and Viet Anh Nguyen. Sobolev transport: A scalable metric for probability measures with graph metrics. In International Conference on Artificial Intelligence and Statistics, pp.9844–9868. PMLR, 2022.

### Soundness
2

### Presentation
2

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
This paper introduces a Multi-Layered Optimal Transport (MLOT) problem and proposes a Sinkhorn algorithm for solving this problem. The MLOT problem generalizes the standard OT problem by modeling transport from the source distribution to the target distribution through the multiple intermediate layers. The proposed Sinkhorn algorithm offers superior efficiency on complex problems while maintaining comparable accuracy to the LP solver, such as Gurobi. The proposed method is also evaluated on real-world tasks, such as Text-Image retrieval and intermediate image computation.

### Strengths
- This paper introduces an interesting variant of the standard OT problem and demonstrates its practical utility by applying the MLOT framework to real-world tasks.
- This paper presents theoretical results on the convergence of the proposed algorithm.
- This paper is easy to follow.

### Weaknesses
 - Please refer to the questions section.

### Questions
- Could you provide the wall-clock computation time for the Image-Text Retrieval task in Table 2? The proposed method is likely to be slower compared to the standard softmax operation.
- In the Image-Text Retrieval task (Fig 6), the two couplings (the coupling between Query image and Caption, and the coupling between Caption and Augmented image) can indicate different image-caption pairings. How coherent are these two couplings?
- In the Image-Text Retrieval task, the standard OT problem can be directly applied between the Query image and Caption using the same cost as in the MLOT, i.e., the negative cosine similarity between the normalized embeddings. Is there a meaningful difference in performance between the MLOT and OT frameworks (Table 2)?
- In the intermediate image experiments (Fig 7), how do the MLOT results differ from the standard OT barycenter?
- In the synthetic data experiments (Sec 4.1), the data points in the intermediate layers are also sampled, e.g., $(n\_{k})\_{k} = \\{3, 10, 20, 20, 10, 3\\}$ in Line 373. Could you provide the reason for sampling these intermediate samples? Is it just for setting the support of the intermediate distributions $a\_{k}$?

### Soundness
3

### Presentation
3

### Contribution
2
