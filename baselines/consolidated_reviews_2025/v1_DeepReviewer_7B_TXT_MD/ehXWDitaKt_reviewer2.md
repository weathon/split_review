### Summary

This paper proposes Newton Loss, a method to improve the performance of differentiable algorithms by replacing their loss functions with a Newton loss. The authors introduce two variants of Newton Loss: one using the empirical Fisher and another using the empirical Hessian. They evaluate their method on various tasks, including ranking and shortest path problems, and demonstrate that it outperforms existing differentiable algorithms.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective, and the authors provide extensive experiments to demonstrate its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is very simple and lacks novelty.
- The authors only compare their method with differentiable algorithms, but not with non-differentiable algorithms. It would be better to compare with non-differentiable algorithms such as sorting and ranking algorithms.
- The authors only test on small-scale problems, and it is unclear how the proposed method would perform on large-scale problems.

### Suggestions

The paper's primary weakness lies in its limited scope of comparison and lack of novelty. While the authors demonstrate the effectiveness of Newton Loss on several tasks, the absence of comparisons with non-differentiable algorithms is a significant oversight. Specifically, for ranking tasks, it would be beneficial to compare against traditional sorting algorithms or established ranking algorithms like LambdaMART. Similarly, for shortest path problems, comparisons against standard graph algorithms would provide a more comprehensive evaluation. The authors should also consider comparing against other differentiable methods that use second-order information, such as those based on Hessian approximations, to better contextualize the contribution of their approach. Without these comparisons, it is difficult to assess the true advantage of the proposed method.

Furthermore, the paper's focus on small-scale problems raises concerns about its practical applicability. The authors should provide a more thorough analysis of the computational complexity of their method and demonstrate its performance on larger datasets. This would involve testing on problems with a significantly larger number of nodes or edges, as well as a larger number of variables. The current experiments do not provide sufficient evidence to support the claim that the proposed method is scalable. It is also important to analyze the memory requirements of the method, as this can be a limiting factor for large-scale problems. The authors should also discuss the potential limitations of their method in terms of scalability and suggest potential directions for future research to address these limitations.

Finally, the paper would benefit from a more detailed discussion of the theoretical properties of the proposed Newton Loss. While the authors demonstrate its empirical effectiveness, a theoretical analysis of its convergence properties and its relationship to existing optimization methods would strengthen the paper. This would involve analyzing the conditions under which the proposed method is guaranteed to converge and comparing its convergence rate to other optimization algorithms. The authors should also discuss the potential limitations of their method in terms of convergence and suggest potential directions for future research to address these limitations.

### Questions

See weakness.

### Rating

5

### Confidence

4

**********
