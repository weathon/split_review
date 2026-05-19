### Summary

This paper proposes a novel method to improve the performance of differentiable algorithms by replacing their loss functions with Newton Loss, which is a Newton loss using the empirical Fisher and Hessian. The authors demonstrate the effectiveness of their method on various tasks, including ranking and shortest path problems.

### Soundness

2

### Presentation

2

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

The paper introduces a method that replaces the loss function of differentiable algorithms with a Newton loss based on the empirical Fisher and Hessian. While the idea is interesting, the simplicity of the approach raises concerns about its novelty. The core idea of using a Newton loss is not new, and the paper does not sufficiently demonstrate a significant departure from existing methods. The authors should more clearly articulate the specific novelty of their approach, perhaps by highlighting a unique combination of techniques or a specific problem setting where their method excels compared to existing Newton loss formulations. A more thorough discussion of related work, particularly those that also leverage second-order information, would be beneficial to better contextualize the contribution. Furthermore, the paper should provide a more detailed analysis of the computational cost of the proposed method, especially in comparison to other Newton loss-based approaches. This would help to clarify the practical advantages of the proposed method.

To address the lack of comparison with non-differentiable algorithms, the authors should consider including a more comprehensive experimental evaluation. While differentiable algorithms are relevant, comparing against traditional sorting and ranking algorithms would provide a more complete picture of the proposed method's performance. For example, the authors could compare their method against standard sorting algorithms on the shortest path problem, or against traditional ranking algorithms on the ranking tasks. This would help to demonstrate the advantages of the proposed method in scenarios where non-differentiable approaches are commonly used. The authors should also consider including a wider range of non-differentiable algorithms in the comparison, as there are many different approaches to these problems. This would help to ensure that the proposed method is not only effective compared to other differentiable methods, but also compared to a broader range of existing techniques.

Finally, the paper should address the scalability of the proposed method. The experiments are currently limited to small-scale problems, and it is unclear how the method would perform on larger datasets. The authors should provide a more detailed analysis of the computational complexity of their method, and they should also include experiments on larger-scale problems to demonstrate the practical applicability of their approach. This could include experiments on datasets with a larger number of nodes or edges, or experiments on problems with a larger number of variables. The authors should also discuss any potential limitations of their method in terms of scalability, and they should suggest potential directions for future research to address these limitations.

### Questions

See weakness.

### Rating

5

### Confidence

3

**********
