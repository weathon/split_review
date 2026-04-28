# Neighbor-aware Geodesic Transportation for Neighborhood Refinery

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Neighborhood refinery aims to enhance the neighbor relationships by refining the original distance matrix to ensure pairwise consistency.
Traditional context-based methods, which encode instances alongside their local neighbors in a contextual affinity space, are limited in capturing global relationships and are vulnerable to the negative impacts of outliers in the neighborhood. To overcome these limitations, we propose a novel Neighbor-aware Geodesic Transportation (NGT) for the neighborhood refinery. NGT first constructs a global-aware distribution for each instance, capturing the intrinsic manifold relationships among all instances. This is followed by an optimization transportation process that utilizes the global-aware distribution within the underlying manifold, incorporating global geometric spatial information to generate a refined distance. NGT first involves Manifold-aware Neighbor Encoding (MNE) to project each instance into a global-aware distribution by constraining pairwise similarity with the corresponding affinity graph to capture global relationships. Subsequently, a Regularized Barycenter Refinery (RBR) module is proposed to integrate local neighbors into a barycenter, employing a Wasserstein term to reduce the influence of outliers. Lastly, Geodesic Transportation (GT) leverages geometric and global context information to transport the barycenter distribution along the geodesic paths within the affinity graph. Extensive evaluations on several tasks, such as re-ranking and deep clustering, demonstrate the superiority of our proposed NGT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposed a novel Neighbor-aware Geodesic Transportation (NGT) for the neighborhood refinery, which constructs a global-aware distribution for each instance, capturing the intrinsic manifold relationships among all instances.

### Strengths
The authors proposed a novel approach for neighborhood refinery that addresses two limitations of previous methods, such as the failure to consider global relationships and not taking into account the negative impact of outliers. The proposed modules Regularized Barycenter Refinery and Geodesic Transportation provide theoretical innovations for solving previous problems. At the same time, a large number of experimental results on re-ranking and deep clustering also provide empirical support. Overall, although the idea is simple and clear, it is indeed effective and provides new insights for subsequent research.

### Weaknesses
1) The algorithm involves three modules, which introduces more hyper-parameters and the complexity of each module is the cube of the number of images n.

2) Considering that the proposed method is progressive and contains many steps, an overall algorithm description should be placed in the main text to facilitate the understanding and use of the algorithm.

3) The paper's presentation could be further strengthened to improve readability.

4) Please check for Ps1=a in Line 251, which is not the same as Ps1=ai in line 267. At the same time, double-check for other possible formula errors.

5) In Line 520, Ablations of GT are indicated in Table 4 and is actually shown in Figure 4.

6) GT incorporate the original Euclidean distance and the optimal transport-based distance, and θ is the balance weight. It is encouraged to set θ = 0 to investigate the performance of the method with only the optimal transport-based distance.

### Questions
see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates how to refine neighbor relationships within the data manifold. Unlike traditional methods that overlook global relationships, this work proposes a novel neighbor-aware geodesic transportation method. Specifically, the paper introduces three modules. The first module is Manifold-aware Neighbor Encoding that project the samples into a nolinear space. The second module is Regularized Barycenter Refinery that integrates local neighbors. The third module is Geodesic Transportation that calculates the shortest path in the affinity graph.

### Strengths
a. This paper presents a solution for neighborhood refinement, capturing global relationships to enhance robustness against outliers.

b. The experiments are sufficient and diverse.

### Weaknesses
 a. Many techniques actually have been proposed and the proposed model seems a combinations of existing methods. For instance, in the Manifold-aware Neighbor Encoding, the authors utilize a Gaussian kernel to construct a manifold-aware space, differing from the traditional use of Euclidean distance to create a Euclidean space. This mapping approach to a nonlinear space is actually a typical technique in spectral clustering. Furthermore, both the neighbor search method in Eq. (3) and the bidirectional similarity diffusion in Eq. (4) are common practices in prior research. Thus, the paper presents limited novel insights.

b. The authors introduce a Regularized Barycenter Refinement module aimed at enhancing robustness against outliers. However, Eq. (6) combines the Euclidean and Wasserstein distances. It’s worth noting that Euclidean distance is inherently sensitive to outliers, making this choice potentially questionable for addressing this issue. It seems that this approach is primarily driven by optimization convenience rather than a robust outlier solution.

c. The third module, as claimed by the authors, uses an existing technique to compute the shortest path in an affinity graph. Consequently, the three primary modules in this work are largely based on established methods.

d. While the authors aim to address robustness to outliers, they do not provide any visual or convincing evidence to support their claims regarding this issue.

e. The authors assert that their approach captures global relationships; however, the techniques employed are still grounded in conventional methods that calculate pairwise affinity weights. Additionally, the lack of visual evidence or further analysis undermines this claim, making it unconvincing.

f. Key experimental details are missing. Firstly, none of the results include standard deviations, which is crucial given the sensitivity of deep learning models to seed selection. Secondly, despite the model’s strict analysis and explicit formulation, the authors do not provide convergence analysis and empirical validation, which is an important omission.

### Questions
My questions are in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a Neighbor-aware Geodesic Transportation (NGT) strategy for enhancing the performance of deep clustering and image retrieval tasks. The proposed method consists of three main components: Manifold-aware Neighbor Encoding (MNE), Regularized Barycenter Refinery (RBR), and Geodesic Transportation (GT). By integrating these components, NGT aims to improve the robustness of neighbor identification within the data manifold, thus enhancing the feature learning and clustering results. The method is evaluated on several benchmark datasets, demonstrating superior performance compared to baseline and state-of-the-art methods.

### Strengths
(1) Comprehensive Approach: The paper proposes a comprehensive method that integrates multiple strategies (MNE, RBR, GT) to address the challenging task of identifying robust neighbors within the data manifold.
(2) Solid Theoretical Foundation: The method is grounded in solid theoretical principles, with clear explanations of the motivations and methodologies behind each component.
(3) Experimental Validation: The proposed method is thoroughly evaluated on multiple benchmark datasets, demonstrating significant improvements in clustering and retrieval performance compared to baseline and state-of-the-art methods.

### Weaknesses
 (1) Lack of Novelty: While the proposed method integrates multiple existing techniques, it lacks significant novelty in the underlying algorithms or methodologies. The components (MNE, RBR, GT) are adaptations or combinations of existing approaches rather than entirely new contributions. Specifically, the Manifold-aware Neighbor Encoding (MNE) appears to be a variation of existing diffusion-based methods, and the Regularized Barycenter Refinery (RBR) seems to be built upon standard Wasserstein barycenter computations. The Geodesic Transportation (GT) also appears to be an adaptation of shortest-path algorithms on graphs, lacking a fundamentally new approach to distance computation.
(2) Complexity and computational cost: the proposed methodology involves multiple steps and components, which increases the computational complexity and cost compared to simpler baseline methods. Even though the authors performed a time complexity analysis, the practical implications of the $\mathcal{O}(n^3)$ complexity for large datasets remain a concern. The iterative optimization strategies and parallelization may not fully mitigate the computational burden, especially when dealing with high-dimensional feature spaces or very large datasets. The coarse-to-fine strategy, while helpful, may still introduce approximations that could affect the final results.
(3) Limited Scope: The method is specifically tailored for deep clustering and image retrieval tasks and may not be directly applicable to other machine learning or computer vision problems. This limits the broader impact and applicability of the proposed work. For example, the method's reliance on manifold assumptions might not hold for datasets with complex or non-manifold structures. The specific design choices for image data might not translate well to other modalities such as time-series or text data.
(4) Incremental Improvement: While the proposed method demonstrates improvements over baseline and state-of-the-art methods, the magnitude of these improvements is incremental rather than transformative. The reported performance gains, while statistically significant, do not represent a major breakthrough in performance. The improvements might be due to the careful combination of existing techniques rather than a fundamentally new approach, and the gains may not justify the increased complexity and computational cost in all practical scenarios.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the topic of neighborhood refinery. To capture global relationships and mitigate the negative impacts of outliers in the neighborhood, a method named NGT is proposed, which consists of three main components, namely Manifold-aware Neighbor Encoding
(MNE), Regularized Barycenter Refinery (RBR), and Geodesic Transportation (GT). The effectiveness of the proposed method is demonstrated on re-ranking and deep clustering tasks. However, I have concerns about its novelty and its presentation.

### Strengths
1. Neighborhood refinery is an important topic that benefits many downstream tasks.
2. The proposed method seems to perform well on most tasks, revealing its effectiveness. Yet, the complexity of the proposed method may limit its scalability and practical applications.

### Weaknesses
1. The novelty of the proposed method is limited. In particular, many concepts are ponderously used, lacking clear explanations. For example, the claim that the similarity matrix F is manifold-aware (line 212) is not sufficiently justified. The authors need to provide a rigorous analysis of how the proposed bidirectional smoothness criterion actually enforces manifold awareness, and how this differs from existing graph-based regularization techniques. It is unclear how the specific form of the smoothness criterion relates to the underlying manifold structure.
2. The presentation is poor. Many notations are ambiguous or lack specifications. For example, what is $\delta$ in line 258? Is the cost matrix C in line 257 the same as the geodesic distance matrix C in line 318? The lack of clarity in notation makes it difficult to follow the technical details of the method. Furthermore, the relationship between the different cost matrices used in the Regularized Barycenter Refinery (RBR) and Geodesic Transportation (GT) components is not clearly explained, making it hard to understand the overall method.
3. The details of datasets are not provided. Summarize them in a table would be helpful. The absence of dataset details makes it difficult to reproduce the experiments and evaluate the generalizability of the proposed method. Key information such as the number of samples, dimensionality, and class distributions should be included for each dataset.
4. The effect of parameter $k_1$ is not discussed. The authors should provide an analysis of how $k_1$ influences the performance of the method. Specifically, how does the choice of $k_1$ affect the neighborhood structure and the resulting learned representations? A sensitivity analysis is needed to understand the robustness of the method to different values of $k_1$.
5. In Table 2, the best result on Hard ROxf is not achieved by your method, which has been mistakenly highlighted in bold. This error undermines the credibility of the experimental results.
6. The method is claimed to reduce the negative impact of outliers in neighborhoods, but the authors do not provide relevant experimental results to support their claims. The authors should provide specific experiments that demonstrate the method's ability to mitigate the influence of outliers. For instance, they could introduce synthetic outliers and show how the proposed method is less affected compared to baseline methods. The current evaluation does not directly address this claim.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
