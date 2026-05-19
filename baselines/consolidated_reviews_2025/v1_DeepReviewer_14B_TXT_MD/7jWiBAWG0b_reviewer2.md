### Summary

This paper investigates the generalization and optimization properties of non-convex pairwise SGD under heavy-tailed gradient noise using an algorithmic stability approach. The authors first establish generalization bounds for non-convex pairwise SGD by linking $\ell_1$ on-average model stability and generalization error. They then refine these bounds by introducing sub-Weibull gradient noise, removing the need for bounded gradients. Under the Polyak-Lojasiewicz (PL) condition, they provide sharper bounds for generalization error and excess risk. Finally, they extend their analysis to minibatch pairwise SGD, deriving the first stability-based near-optimal generalization and optimization bounds.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-organized and easy to follow. 

2. The theoretical results are solid and novel. 

3. The authors provide a thorough comparison with existing results in Table 2.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks experimental results to validate the theoretical findings. 

2. Some assumptions, such as the PL condition, may be restrictive in practice.

### Suggestions

The lack of experimental validation is a significant weakness. While the theoretical results are interesting, it is crucial to demonstrate their practical relevance. The authors should consider conducting experiments on synthetic or real-world datasets to verify the derived generalization and optimization bounds. For example, they could compare the performance of non-convex pairwise SGD with and without heavy-tailed noise, and check if the observed generalization error aligns with the theoretical predictions. Furthermore, experiments should explore the impact of different sub-Weibull parameters on the convergence and generalization behavior. Such empirical validation would greatly strengthen the paper's contribution and provide valuable insights into the practical applicability of the theoretical findings. The experiments should also include a comparison with other optimization methods to highlight the advantages and disadvantages of the proposed approach.

The reliance on the Polyak-Lojasiewicz (PL) condition is another concern. While the PL condition is a common assumption in optimization, it is not always satisfied in practice, especially for complex non-convex functions. The authors should discuss the limitations of this assumption and explore potential relaxations or alternative conditions that could be more realistic. For instance, they could investigate the possibility of using the Kurdyka-Łojasiewicz (KL) condition, which is a more general assumption that encompasses a wider class of non-convex functions. Furthermore, it would be beneficial to provide examples of practical scenarios where the PL condition is likely to hold and where it is likely to be violated. This would help the reader to better understand the scope and limitations of the theoretical results. The authors should also discuss the implications of violating the PL condition on the derived bounds.

Finally, the paper could benefit from a more detailed discussion of the practical implications of the theoretical results. While the authors provide a comparison with existing results, it is not clear how these results can be used to guide the design of practical algorithms. For example, how should one choose the step size and batch size in non-convex pairwise SGD with heavy-tailed noise? What are the trade-offs between generalization error and optimization error? The authors should provide more concrete guidance on how to apply their theoretical findings in practice. This could include providing specific recommendations for parameter tuning and algorithm design. Additionally, it would be helpful to discuss the computational cost of the proposed methods and compare it with other existing approaches.

### Questions

1. Can the authors provide experimental results to validate their theoretical findings? 

2. Are there any potential relaxations or alternative conditions that could be more realistic in practice?

### Rating

6

### Confidence

3

**********
