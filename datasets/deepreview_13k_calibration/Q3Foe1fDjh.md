# Expected Probabilistic Hierarchies

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
Hierarchical clustering has usually been addressed by discrete optimization using heuristics or continuous optimization of relaxed scores for hierarchies. In this work, we propose to optimize expected scores under a probabilistic model over hierarchies. (1) We show theoretically that the global optimal values of the expected Dasgupta cost and Tree-Sampling divergence (TSD), two unsupervised metrics for hierarchical clustering, are equal to the optimal values of their discrete counterparts contrary to some relaxed scores. (2) We propose Expected Probabilistic Hierarchies (EPH), a probabilistic model to learn hierarchies in data by optimizing expected scores. EPH uses differentiable hierarchy sampling enabling end-to-end gradient descent based optimization, and an unbiased subgraph sampling approach to scale to large datasets. (3) We evaluate EPH on synthetic and real-world datasets including vector and graph datasets. EPH outperforms all other approaches on quantitative results and provides meaningful hierarchies in qualitative evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents methods for hierarchical clustering using gradient-based methods, in particular a optimizing the expected score (e.g., Dasgupta cost) over a distribution of tree structures. 

The authors demonstrate that the proposed approach has several nice properties (e.g., global optimal corresponds to optima of discrete cost). 

The proposed approach performs well empirically compared to a variety of other approaches, compared to classic approaches such as average/ward linkage agglomerative methods and other gradient-based methods..

### Strengths
This paper presents an interesting approach for gradient-based hierarchical clustering. Strengths include:

* **Well-Written & Thorough** - The paper is quite complete, it is a pleasure to read and provides a clear outline of the approach, provides analysis of the empirical results (e.g., Fig 3,4,5, + much of supplement), and helpful remarks about the technical details of the approach (e.g., page 5 limitations)
* **Methodological Approach** - While the parameterization of tree structures is similar to Zügner et al (2022), the details of the sampling based approach seem to be distinct and the core contribution of the paper. While these are based on existing methods, the application here is intriguing.
* **Empirical Results** - The proposed approach performs well empirically, outperforming most other methods in terms of these cost functions. There is thorough analysis which investigates the performance of the method throughout the supplemental material.

Minor:
Page 23 cuts off

### Weaknesses
Limitations of the paper include:
* I think that the paper could have benefited from discussion of how the proposed cost functions relate to down stream tasks of clustering (e.g., evaluation against target labels, target hierarchies, etc.) and how continuous cost functions compare to discrete ones in this setting. Specifically, it's unclear how optimizing a continuous relaxation of the Dasgupta cost translates to performance on discrete clustering tasks, and whether the properties of the continuous cost function are preserved when converting back to a discrete tree structure. A more detailed analysis of the approximation error introduced by this relaxation would be beneficial. Furthermore, the paper could explore the relationship between the optimized cost and the quality of the resulting clusters in real-world scenarios, where ground truth hierarchies may not be perfectly aligned with the assumptions of the Dasgupta cost.
* Similarly, discussion about when one prefers such methods in practice could be interesting (e.g., are there end-to-end applications?) It would be helpful to understand the computational trade-offs of the proposed approach compared to traditional methods, particularly in terms of scalability and memory usage. Are there specific problem sizes or data characteristics where the gradient-based approach offers a clear advantage? It would also be useful to discuss the sensitivity of the method to hyperparameter settings and initialization, as these factors can significantly impact the quality of the learned hierarchies. The paper should also clarify if the method can be used in an online or streaming setting, where data arrives sequentially, or if it is limited to batch processing.
* More details about the line: "To obtain these for EPH and FPH, we take the most likely edge for each row in A and B, as Zügner et al. ¨ (2022) proposed" It is unclear why selecting the most likely edge is a good approximation for finding the optimal discrete hierarchy. A more detailed justification of this step, including a discussion of its potential limitations and alternative approaches, would be valuable. For example, what is the impact of this approximation on the final cost, and are there scenarios where it might lead to suboptimal results?

### Questions
Apologies, if I have missed something, are the trees produced by EPH binary? Do you convert them into binary trees for Dasgupta cost evaluation?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a probabilistic model to learn a hierarchical clustering by optimizing the expectation of a quality metric (TSD or Dasgupta score).

They show that if this criterion has the same optimal value as the discrete counterpart (unlike say a continous relaxation based approach), and so is a reasonable target to optimize for. They use a end-to-end gradient based optimizer to optimize for this target.

Experiments were performed to show that their proposed method outperforms reasonable baselines, including a simple relaxation based method.

### Strengths
Use of hierarchical sampling to enable end-to-end differentiable optimization instead of the more obvious relaxation approach is interesting.

### Weaknesses
While the resulting clustering does seem to be improved (judged by the improvement in the target criteria), it is unclear how much more expensive this process is compared to the baseline, or how the quality changes with changes in the number of samples used.

### Questions
Please include some more details around 1) how much the results vary with the number of samples used 2) speed comparisons

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a differentiable optimization approach for solving the hierarchical clustering problem. Specifically, for the Dasgupta’s objective and TSD objective. To this end, the authors begin by encoding the tree structure as two 0-1 matrices $\hat{A}, \hat{B}$. Then they relax the integer constraint and obtain two continuous matrices $A,B$, which can be interpreted as the probability distribution over the discrete tree structure. Consequently, the goal is transformed into optimizing the expectation over the distribution represented by $A$ and $B$. Moreover, the authors prove that the optimal value of the expectation is equivalent to the discrete version. 

In the optimization procedure, the authors replace the expectation with its appriximation, the mean computed from sampled hierarchies. Due to the high complexity of computing Dasgupta’s objectives, they employ subgraph sampling techniques to accelerate the evaluation process.

Finally, the proposed method is extensively evaluated on diverse datasets to assess its performance and effectiveness.

### Strengths
- The overall completeness of this work is good. It demonstrates clarity in writing and provides detailed explanations.
- In my opinion, the expected objectives presented in this paper (eq. 4) are more reasonable compared to previous work. For instance, considering $Das(\tilde{T})$, $c(v_i\wedge v_j)$ is the number of leaves under $LCA(v_i, v_j)$ and it should be computed as $\sum_{z\in Z}\sum_{v\in V}\Pr(z=LCA(v_i,v_j)\ and \text{ v is under z})$ in the probabilistic tree. The two conditions in the formula are not independent hence eq. 13 is more accurate than eq. 9.
- The new scaling method proposed by this work has better explainability than its counterpart in [1].
- The experiment results demonstrate that EPH method is competitive in practical application.

[1] End-to-End Learning of Probabilistic Hierarchies on Graphs

### Weaknesses
I have not found obvious weaknesses of this paper. However, there is a concern about the novelty contribution when it is compared with [1]. The overal strategy and presentation closely resemble the scheme of [1]. Both the expected objectives and scaling trick appear to be modifications of the results presented in [1].

### Questions
- The example $K_4$ graph illustrates the advantage of EPH over FPH. Can you provide an example graph whose edges weights are not the same? As in the context of hierarchical clustering, unweighted graph has no real hierarchy. An instance with non-uniform weights would be more persuasive.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
