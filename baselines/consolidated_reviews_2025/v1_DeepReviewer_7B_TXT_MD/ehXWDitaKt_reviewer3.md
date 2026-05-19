### Summary

This paper proposes a new loss function called Newton Loss, which is designed to improve the performance of differentiable algorithms. The authors introduce two variants of Newton Loss: one using the empirical Fisher and another using the empirical Hessian. They evaluate their method on various tasks, including ranking and shortest path problems, and demonstrate that it outperforms existing differentiable algorithms.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, and the authors provide extensive experiments to demonstrate its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is very simple and lacks novelty.
2. The authors only compare their method with differentiable algorithms, but not with non-differentiable algorithms. It would be better to compare with non-differentiable algorithms such as sorting and ranking algorithms.
3. The authors only test on small-scale problems, and it is unclear how the proposed method would perform on large-scale problems.

### Suggestions

The paper would benefit from a more thorough comparison against non-differentiable algorithms. For ranking tasks, it is essential to compare against traditional sorting algorithms or established ranking algorithms like LambdaMART. These methods, while not differentiable, are widely used and provide a crucial benchmark for evaluating the performance of any new approach. Similarly, for shortest path problems, comparisons against standard graph algorithms would be beneficial. This would help to contextualize the performance of the proposed Newton Loss method and demonstrate its advantages over existing techniques. The absence of these comparisons makes it difficult to assess the true novelty and practical impact of the proposed method. Furthermore, the authors should consider comparing against other differentiable methods that use second-order information, such as those based on Hessian approximations, to better contextualize the contribution of their approach. This would help to clarify the specific advantages of their method over existing techniques.

To address the concern about scalability, the authors should provide a more detailed analysis of the computational complexity of their method. This analysis should include both theoretical considerations and empirical results on larger datasets. Specifically, they should investigate how the runtime and memory usage of their method scale with the size of the input data. It would be beneficial to test the method on problems with a significantly larger number of nodes or edges, as well as a larger number of variables. This would provide a more comprehensive understanding of the method's practical applicability. The authors should also discuss the potential limitations of their method in terms of scalability and suggest potential directions for future research to address these limitations. For example, they could explore techniques for reducing the computational cost of calculating the Hessian or Fisher information matrix, or investigate the use of stochastic approximations.

Finally, the paper would be strengthened by a more detailed discussion of the theoretical properties of the proposed Newton Loss. While the empirical results are promising, a theoretical analysis of the convergence properties and the relationship to existing optimization methods would provide a deeper understanding of the method. This would involve analyzing the conditions under which the proposed method is guaranteed to converge and comparing its convergence rate to other optimization algorithms. The authors should also discuss the potential limitations of their method in terms of convergence and suggest potential directions for future research to address these limitations. This would help to establish a stronger theoretical foundation for the proposed method and increase its credibility.

### Questions

See weakness.

### Rating

5

### Confidence

3

**********
