### Summary

This paper proposes a new random embedding method called Rademacher-like embedding (RLE), which aims to reduce the computational complexity of random embeddings while maintaining their desirable properties. The authors provide a theoretical analysis of RLE, demonstrating its linear time and space complexity and its ability to preserve the square of the 2-norm of high-dimensional vectors after embedding. They also apply RLE to single-pass randomized singular value decomposition (RSVD) and the randomized Arnoldi process, showing that it achieves speedups of 1.7x and 1.3x on average, respectively, while maintaining or improving accuracy.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel Rademacher-like embedding (RLE) method that achieves linear time and space complexity, which is a significant improvement over existing methods like Gaussian and Rademacher embeddings.

2. The authors provide a comprehensive theoretical analysis of RLE, proving its linear complexity and demonstrating that it preserves the square of the 2-norm of high-dimensional vectors after embedding.

3. The paper applies RLE to two important applications: single-pass RSVD and the randomized Arnoldi process, showing that it achieves significant speedups while maintaining or improving accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed comparison of the proposed RLE method with other state-of-the-art random embedding methods, such as Count Sketch and SRHT, in terms of both theoretical properties and practical performance. Specifically, the paper lacks a rigorous analysis of how RLE's performance compares to these methods in terms of subspace embedding guarantees, which are crucial for many applications. The absence of a direct comparison makes it difficult to assess the true advantages and disadvantages of RLE relative to existing techniques.

2. The paper does not explore the potential limitations or drawbacks of the proposed RLE method. For example, it does not discuss the sensitivity of RLE to the choice of parameters, such as the size of the Rademacher matrix and the number of auxiliary random arrays. It also does not address the potential for numerical instability or the impact of using finite-precision arithmetic, which could affect the practical performance of the method.

3. The paper does not provide a detailed analysis of the practical implications of the proposed RLE method. For example, it does not discuss how RLE can be used in other applications beyond single-pass RSVD and the randomized Arnoldi process. It also does not address the potential challenges of implementing RLE in real-world systems, such as the need for efficient data structures and algorithms to handle the auxiliary random arrays.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing random embedding techniques, particularly Count Sketch and SRHT. This comparison should not only focus on empirical performance but also delve into the theoretical guarantees provided by each method. For instance, a detailed analysis of the subspace embedding properties of RLE, including the distortion parameters and the required embedding dimension, should be presented and contrasted with those of Count Sketch and SRHT. This would involve a rigorous mathematical analysis of how well RLE preserves the geometry of the input data compared to these alternatives. Furthermore, the authors should provide a clear explanation of the trade-offs between the different methods, highlighting the specific scenarios where RLE is expected to outperform the others and vice versa. This would provide a more comprehensive understanding of the strengths and weaknesses of RLE and its applicability in various contexts.

To address the lack of discussion on the limitations of RLE, the authors should investigate the sensitivity of the method to its parameters. This could involve a theoretical analysis of how the choice of the Rademacher matrix size and the number of auxiliary random arrays affects the performance of RLE. Specifically, the authors should explore the impact of these parameters on the distortion of the embedded vectors and the overall accuracy of the downstream tasks. Additionally, the authors should conduct experiments to evaluate the robustness of RLE to numerical instability and the use of finite-precision arithmetic. This could involve testing the method on a range of hardware platforms and with different numerical precision settings. The results of these experiments should be presented and discussed in detail, providing practical guidance on the optimal parameter settings and the limitations of RLE in real-world scenarios.

Finally, the paper should broaden its discussion of the practical implications of RLE. This could involve exploring the potential applications of RLE in other areas beyond single-pass RSVD and the randomized Arnoldi process. For example, the authors could investigate the use of RLE in machine learning tasks such as clustering, classification, and dimensionality reduction. Furthermore, the authors should provide a detailed discussion of the implementation challenges of RLE, including the data structures and algorithms required to efficiently handle the auxiliary random arrays. This discussion should include practical considerations such as memory usage, computational complexity, and the potential for parallelization. By addressing these points, the paper would provide a more comprehensive and practical guide to the use of RLE in real-world applications.

### Questions

1. How does the proposed RLE method compare to other state-of-the-art random embedding methods, such as Count Sketch and SRHT, in terms of both theoretical properties and practical performance?

2. What are the potential limitations or drawbacks of the proposed RLE method, and how can they be addressed?

3. What are the practical implications of the proposed RLE method, and how can it be applied to other applications beyond single-pass RSVD and the randomized Arnoldi process?

### Rating

5

### Confidence

3

**********
